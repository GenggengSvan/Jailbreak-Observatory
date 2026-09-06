#!/usr/bin/env python3
"""Refresh Google Scholar citation counts and rebuild the >50-citation collection.

Google Scholar has no supported public API.  The workflow therefore expects a
SERPAPI_API_KEY secret (SerpApi's Google Scholar engine) and refuses to write
data when the service returns an error or an empty response.  A direct Scholar
request can be enabled locally with ``--allow-direct`` for small, manual runs,
but it is normally rate-limited on CI runners.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import html
import json
import os
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "citation_catalog.json"
OUTPUT = ROOT / "citations_over_50.md"
README = ROOT / "README.md"
THRESHOLD = 50


def clean_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_title(value: str) -> str:
    value = html.unescape(value).lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def title_similarity(left: str, right: str) -> float:
    a, b = normalize_title(left), normalize_title(right)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def parse_markdown(path: Path) -> list[dict]:
    """Parse the previous citation Markdown, including entries below 50."""
    content = path.read_text(encoding="utf-8")
    entries = []
    for block in re.split(r"(?m)^## ", content)[1:]:
        title, _, body = block.partition("\n")
        citations = re.search(r"📑 Citations:\s*(\d+)", body)
        target = re.search(r"🎯 Target:\s*(.*?)\s+🗂️ Category:\s*(\w+)", body)
        publication = re.search(r"📅 Year:\s*(\d{4})\s+📍 Venue:\s*(.+)", body)
        abstract = re.search(r"Abstract:\s*\n(.*?)(?=\n(?:## |$))", body, re.S)
        if not (citations and target and publication):
            continue
        entries.append({
            "title": title.strip(),
            "year": int(publication.group(1)),
            "venue": publication.group(2).strip(),
            "target": target.group(1).strip(),
            "category": target.group(2).strip(),
            "abstract": re.sub(r"\s+", " ", abstract.group(1).strip()) if abstract else "",
            "citations": int(citations.group(1)),
            "url": "",
            "lastChecked": None,
        })
    return entries


def conference_candidates() -> list[dict]:
    """Load titles already curated in Conference/ and the latest JSON files."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_site_data as site_data  # pylint: disable=import-outside-toplevel

    records = site_data.parse_conference_files() + site_data.parse_latest_metadata()
    result = []
    seen = set()
    for record in records:
        key = normalize_title(record["title"])
        if key in seen:
            continue
        seen.add(key)
        result.append({
            "title": record["title"],
            "year": int(record.get("year") or 0),
            "venue": record.get("venue", ""),
            "target": record.get("target", "Text"),
            "category": record.get("category", "Other"),
            "abstract": record.get("abstract", ""),
            "citations": None,
            "url": record.get("url", ""),
            "lastChecked": None,
        })
    return result


def migrate_catalog(old_path: Path) -> list[dict]:
    if CATALOG.exists():
        return json.loads(CATALOG.read_text(encoding="utf-8"))
    if not old_path.exists():
        raise FileNotFoundError(f"Neither {CATALOG} nor {old_path} exists")
    entries = parse_markdown(old_path)
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return entries


def merge_candidates(entries: list[dict], include_conference: bool) -> list[dict]:
    by_title = {normalize_title(item["title"]): item for item in entries}
    if include_conference:
        for candidate in conference_candidates():
            key = normalize_title(candidate["title"])
            if key not in by_title:
                by_title[key] = candidate
            else:
                existing = by_title[key]
                for field in ("year", "venue", "target", "category", "abstract", "url"):
                    if candidate.get(field) and not existing.get(field):
                        existing[field] = candidate[field]
    return list(by_title.values())


def request_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "JailbreakObservatory/1.0 (+https://github.com/GenggengSvan/Jailbreak-Observatory)"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def scholar_via_serpapi(title: str, api_key: str) -> tuple[int, str]:
    query = urllib.parse.urlencode({
        "engine": "google_scholar",
        "q": f'"{title}"',
        "hl": "en",
        "num": "10",
        "api_key": api_key,
    })
    payload = request_json("https://serpapi.com/search.json?" + query)
    if payload.get("error"):
        raise RuntimeError(payload["error"])
    best = None
    best_score = 0.0
    for result in payload.get("organic_results", []):
        result_title = result.get("title", "")
        score = title_similarity(title, result_title)
        if score > best_score:
            best, best_score = result, score
    if not best or best_score < 0.88:
        raise RuntimeError(f"no confident match (best title similarity {best_score:.2f})")
    cited = best.get("inline_links", {}).get("cited_by", {}).get("total")
    if cited is None:
        raise RuntimeError("matched result has no cited-by count")
    return int(cited), best.get("result_id", "")


def scholar_via_html(title: str) -> tuple[int, str]:
    query = urllib.parse.urlencode({"hl": "en", "q": f'"{title}"'})
    request = urllib.request.Request(
        "https://scholar.google.com/scholar?" + query,
        headers={"User-Agent": "Mozilla/5.0 (compatible; JailbreakObservatory/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        page = response.read().decode("utf-8", "replace")
    if any(marker in page.lower() for marker in ("/sorry/", "captcha", "unusual traffic")):
        raise RuntimeError("Google Scholar returned a CAPTCHA/rate-limit page")
    blocks = re.findall(r'<div class="gs_ri".*?</div>\s*</div>', page, flags=re.S)
    best, best_score = None, 0.0
    for block in blocks:
        match = re.search(r'<h3 class="gs_rt".*?>(.*?)</h3>', block, re.S)
        if not match:
            continue
        result_title = clean_html(match.group(1))
        score = title_similarity(title, result_title)
        if score > best_score:
            best, best_score = block, score
    if not best or best_score < 0.88:
        raise RuntimeError(f"no confident match (best title similarity {best_score:.2f})")
    cited = re.search(r"Cited by\s+(\d+)", clean_html(best), re.I)
    if not cited:
        raise RuntimeError("matched result has no cited-by count")
    return int(cited.group(1)), ""


def render_markdown(entries: list[dict], checked: str) -> str:
    selected = sorted(
        (item for item in entries if item.get("citations") is not None and item["citations"] > THRESHOLD),
        key=lambda item: (-item["citations"], item["title"].lower()),
    )
    chunks = [
        "# Papers with More Than 50 Citations",
        "",
        "> Citation counts are queried from Google Scholar and refreshed monthly. Only papers with **more than 50 citations** are included.",
        f"> Last successful refresh: {checked}",
        "",
    ]
    for item in selected:
        chunks.extend([
            f"## {item['title']}",
            f"📑 Citations: {item['citations']}",
            f"🎯 Target: {item.get('target', 'Text')}  🗂️ Category: {item.get('category', 'Other')}",
            f"📅 Year: {item.get('year', '')}  📍 Venue: {item.get('venue', '')}",
            "",
            "Abstract:",
            item.get("abstract", "").strip(),
            "",
        ])
    return "\n".join(chunks).rstrip() + "\n"


def update_readme(entries: list[dict]) -> None:
    text = README.read_text(encoding="utf-8")
    text = text.replace(
        "📑 the [top 100 most cited Jailbreak articles](#cite)",
        "📑 the [Jailbreak articles with more than 50 citations](#cite)",
    )
    start = text.index('<a id="cite"></a>')
    table_start = text.index("<table>", start)
    table_end = text.index("</table>", table_start) + len("</table>")
    selected = sorted(
        (item for item in entries if item.get("citations") is not None and item["citations"] > THRESHOLD),
        key=lambda item: (-item["citations"], item["title"].lower()),
    )
    rows = [
        "<table>",
        "  <thead><tr><th>Target</th><th>Category</th><th>Title</th><th>Citations</th></tr></thead>",
        "  <tbody>",
    ]
    for item in selected:
        rows.append(
            f"  <tr><td>{html.escape(item.get('target', 'Text'))}</td>"
            f"<td>{html.escape(item.get('category', 'Other'))}</td>"
            f"<td>{html.escape(item['title'])}</td><td>{item['citations']}</td></tr>"
        )
    rows.extend(["  </tbody>", "</table>"])
    text = text[:table_start] + "\n".join(rows) + text[table_end:]
    text = text.replace("## 📑 Top 100 Citations", "## 📑 Articles with More Than 50 Citations")
    text = text.replace(
        "For full details, see the citations document <a href='citations_top_100.md'>Citations Top 100</a>.",
        "For full details, see the <a href='citations_over_50.md'>articles with more than 50 citations</a> (Google Scholar; refreshed monthly).",
    )
    README.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-direct", action="store_true", help="Try direct Scholar HTML when SERPAPI_API_KEY is absent")
    parser.add_argument("--include-conference", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--migrate-only", action="store_true", help="Create the catalog and >50 collection without network requests")
    parser.add_argument("--min-delay", type=float, default=2.0)
    parser.add_argument("--max-delay", type=float, default=5.0)
    args = parser.parse_args()

    old_path = ROOT / "citations_top_100.md"
    entries = migrate_catalog(old_path)
    entries = merge_candidates(entries, args.include_conference)
    if args.migrate_only:
        today = dt.date.today().isoformat()
        CATALOG.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        OUTPUT.write_text(render_markdown(entries, today), encoding="utf-8")
        update_readme(entries)
        print(f"Migrated {len(entries)} citation candidates; collection has {sum(1 for item in entries if (item.get('citations') or 0) > THRESHOLD)} papers.")
        return 0
    api_key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if not api_key and not args.allow_direct:
        print("SERPAPI_API_KEY is not configured. Google Scholar has no official public API; refusing an unreliable CI scrape.", file=sys.stderr)
        return 2
    today = dt.date.today().isoformat()
    successes = failures = 0
    for index, item in enumerate(entries, 1):
        try:
            if api_key:
                count, source_id = scholar_via_serpapi(item["title"], api_key)
            else:
                count, source_id = scholar_via_html(item["title"])
            item["citations"] = count
            item["lastChecked"] = today
            if source_id:
                item["sourceId"] = source_id
            successes += 1
            print(f"[{index}/{len(entries)}] {count:>4}  {item['title']}")
        except Exception as exc:  # keep old value for one bad result
            failures += 1
            print(f"[{index}/{len(entries)}] SKIP  {item['title']}: {exc}", file=sys.stderr)
        if index < len(entries):
            time.sleep(random.uniform(args.min_delay, args.max_delay))

    if successes == 0:
        print("No citation counts were returned; no files were changed.", file=sys.stderr)
        return 1
    if successes < max(1, min(10, len(entries) // 20)):
        print(f"Only {successes} citation queries succeeded ({failures} failed); refusing a partial refresh.", file=sys.stderr)
        return 1

    CATALOG.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT.write_text(render_markdown(entries, today), encoding="utf-8")
    update_readme(entries)
    print(f"Updated {successes} papers; retained {failures} previous values; collection has {sum(1 for item in entries if (item.get('citations') or 0) > THRESHOLD)} papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
