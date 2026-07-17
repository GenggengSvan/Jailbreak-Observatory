#!/usr/bin/env python3
"""Collect formally published jailbreak papers from official conference sources.

The discovery adapters currently cover KDD and IJCAI. A paper is eligible only
when it appears in the official proceedings/accepted-paper index and has a
formal DOI or an official proceedings detail page. OpenAlex is used only to
enrich missing abstracts; it never establishes publication eligibility.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "data" / "conference_latest.json"
OVERRIDES_PATH = ROOT / "data" / "conference_overrides.json"
USER_AGENT = "Jailbreak-Observatory/1.0 (+https://github.com/GenggengSvan/Jailbreak-Observatory)"

ALLOWED_CATEGORIES = {"Attack", "Defense", "Benchmark", "Mechanism", "Other"}
ALLOWED_TARGETS = {"Text", "Vision", "Hybrid", "Agent"}

# Broad candidate discovery happens on titles. Abstract scoring below is the
# stricter second pass that determines whether a candidate is included.
CANDIDATE_RE = re.compile(
    r"jailbreak|prompt injection|red[ -]?team|input moderation|image-input harms|"
    r"safety benchmark|safety equity|harmful|guardrail|refusal|safety alignment|"
    r"protecting llms|llm security|agent security",
    re.I,
)

RELEVANCE_RULES = (
    (re.compile(r"\bjailbreak(?:ing|s)?\b", re.I), 8, "jailbreak"),
    (re.compile(r"\b(?:indirect )?prompt injection(?: attacks?)?\b", re.I), 8, "prompt injection"),
    (re.compile(r"\bred[ -]?team(?:ing)?\b", re.I), 6, "red teaming"),
    (re.compile(r"\bcrescendo attack", re.I), 6, "crescendo attack"),
    (re.compile(r"\bsafety benchmark", re.I), 5, "safety benchmark"),
    (re.compile(r"\binput moderation\b", re.I), 5, "input moderation"),
    (re.compile(r"\bimage-input harms?\b", re.I), 5, "image-input harm"),
    (re.compile(r"\bharmful (?:instruction|prompt|query|request|content)s?\b", re.I), 4, "harmful inputs"),
    (re.compile(r"\bbypass(?:ing|es|ed)? (?:the )?(?:safety|safeguards?|guardrails?)\b", re.I), 5, "safety bypass"),
    (re.compile(r"\b(?:safety|human) alignment\b", re.I), 2, "safety alignment"),
)

MODEL_SCOPE_RE = re.compile(
    r"\b(?:large language models?|llms?|vision[- ]language models?|vllms?|multimodal llms?|"
    r"embodied agents?|language-model agents?)\b",
    re.I,
)


def fetch(url: str, *, attempts: int = 3) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/json"})
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as error:
            if error.code in {404, 410}:
                raise RuntimeError(f"Unable to fetch {url}: HTTP {error.code}") from error
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(1.5 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Unable to fetch {url}: {last_error}")


def strip_tags(value: str) -> str:
    value = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_doi(value: str) -> str:
    value = value.strip().rstrip(".,;)")
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.I).lower()


def invert_abstract(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    ordered = sorted((position, word) for word, positions in index.items() for position in positions)
    return " ".join(word for _, word in ordered)


def openalex_abstract(doi: str) -> str:
    url = f"https://api.openalex.org/works/https://doi.org/{doi}?mailto=research@example.com"
    try:
        payload = json.loads(fetch(url))
    except (RuntimeError, json.JSONDecodeError):
        return ""
    return invert_abstract(payload.get("abstract_inverted_index"))


def crossref_metadata(doi: str) -> dict:
    url = f"https://api.crossref.org/works/{doi}"
    try:
        payload = json.loads(fetch(url)).get("message", {})
    except (RuntimeError, json.JSONDecodeError):
        return {}
    authors = []
    first_affiliation = "N/A"
    for author in payload.get("author", []):
        name = " ".join(part for part in (author.get("given", ""), author.get("family", "")) if part).strip()
        if name:
            authors.append(name)
        if first_affiliation == "N/A" and author.get("sequence") == "first" and author.get("affiliation"):
            first_affiliation = author["affiliation"][0].get("name") or "N/A"
    published = payload.get("published", {}).get("date-parts", [[]])[0]
    return {
        "authors": authors,
        "firstAuthorAffiliation": first_affiliation,
        "publishedYear": published[0] if published else None,
        "containerTitle": (payload.get("container-title") or [""])[0],
    }


def relevance(title: str, abstract: str) -> tuple[int, list[str]]:
    text = f"{title}. {abstract}"
    if not MODEL_SCOPE_RE.search(text):
        return 0, []
    score = 0
    signals: list[str] = []
    for pattern, weight, label in RELEVANCE_RULES:
        if pattern.search(text):
            score += weight
            signals.append(label)
    return score, signals


def classify(title: str, abstract: str) -> tuple[str, str]:
    text = f"{title}. {abstract}".lower()
    if re.search(r"benchmark|evaluat|assessment|audit|measurement|taxonomy", text):
        category = "Benchmark"
    elif re.search(r"defen[cs]|mitigat|detect|moderation|protect|guard|filter", text):
        category = "Defense"
    elif re.search(r"mechanism|understand|why |attention distribution|representation", text):
        category = "Mechanism"
    elif re.search(r"attack|jailbreak|exploit|bypass|red[ -]?team", text):
        category = "Attack"
    else:
        category = "Other"

    if re.search(r"embodied|\bagents?\b|tool[- ]use|external content|copilot", text):
        target = "Agent"
    elif re.search(r"vision|visual|image|vlm|multimodal", text):
        target = "Vision"
    elif re.search(r"audio|speech|voice|cross-modal", text):
        target = "Hybrid"
    else:
        target = "Text"
    return category, target


def load_overrides() -> dict[str, dict[str, str]]:
    if not OVERRIDES_PATH.exists():
        return {}
    return {normalize_doi(key): value for key, value in json.loads(OVERRIDES_PATH.read_text()).items()}


def apply_classification(paper: dict, overrides: dict[str, dict[str, str]]) -> dict:
    category, target = classify(paper["title"], paper["abstract"])
    override = overrides.get(normalize_doi(paper.get("doi", "")), {})
    category = override.get("category", category)
    target = override.get("target", target)
    if category not in ALLOWED_CATEGORIES or target not in ALLOWED_TARGETS:
        raise ValueError(f"Invalid classification for {paper['title']}: {category}/{target}")
    paper.update(category=category, target=target)
    return paper


def discover_kdd_year(start_year: int) -> tuple[int, str, str]:
    for year in range(start_year, 2024, -1):
        url = f"https://www.kdd.org/kdd{year}/research-track-papers-2/"
        try:
            page = fetch(url)
        except RuntimeError:
            continue
        page_text = strip_tags(page)
        if (
            "doi.org/10.1145/" in page
            and "Research Track Papers" in page_text
            and re.search(rf"\bKDD\s*{year}\b", page_text, re.I)
        ):
            return year, url, page
    raise RuntimeError("No published KDD proceedings page found")


def collect_kdd(start_year: int, overrides: dict[str, dict[str, str]]) -> tuple[int, str, list[dict]]:
    year, source_url, page = discover_kdd_year(start_year)
    entries = re.findall(
        r"<strong[^>]*>(.*?)</strong>\s*<br\s*/?>\s*DOI:\s*(https?://doi\.org/10\.1145/[^<\s]+)",
        page,
        flags=re.I | re.S,
    )
    papers = []
    for raw_title, doi_url in entries:
        title = strip_tags(raw_title)
        if not CANDIDATE_RE.search(title):
            continue
        doi = normalize_doi(doi_url)
        bibliographic = crossref_metadata(doi)
        if bibliographic.get("publishedYear") != year:
            continue
        abstract = openalex_abstract(doi)
        score, signals = relevance(title, abstract)
        if score < 5:
            continue
        paper = {
            "venue": "KDD",
            "year": year,
            "title": title,
            "authors": bibliographic.get("authors", []),
            "firstAuthorAffiliation": bibliographic.get("firstAuthorAffiliation", "N/A"),
            "track": bibliographic.get("containerTitle", "Proceedings"),
            "status": "Published",
            "doi": doi,
            "url": f"https://doi.org/{doi}",
            "officialSource": source_url,
            "abstractSource": f"https://api.openalex.org/works/https://doi.org/{doi}",
            "abstract": abstract,
            "relevanceScore": score,
            "relevanceSignals": signals,
        }
        papers.append(apply_classification(paper, overrides))
    return year, source_url, sorted(papers, key=lambda item: item["title"].lower())


def discover_ijcai_year(start_year: int) -> tuple[int, str, str]:
    for year in range(start_year, 2024, -1):
        url = f"https://www.ijcai.org/proceedings/{year}/"
        try:
            page = fetch(url)
        except RuntimeError:
            continue
        if f"/proceedings/{year}/" in page and "paper_wrapper" in page:
            return year, url, page
    raise RuntimeError("No published IJCAI proceedings index found")


def parse_ijcai_detail(url: str, year: int) -> dict:
    page = fetch(url)
    title_match = re.search(r'<meta name="citation_title" content="(.*?)"\s*/?>', page, re.I | re.S)
    authors = [html.unescape(value).strip() for value in re.findall(r'<meta name="citation_author" content="(.*?)"\s*/?>', page, re.I | re.S)]
    doi_match = re.search(r'href="https?://doi\.org/([^"]+)"[^>]*class="doi"', page, re.I)
    track_match = re.search(r'<div>([^<]*?(?:Track|Social Good|Survey)[^<]*?)\.\s*Pages', page, re.I | re.S)
    abstract_match = re.search(
        r'<hr\s*/?>\s*<div class="row">\s*<div class="col-md-12">(.*?)</div>\s*<div class="col-md-12">\s*<div class="keywords">',
        page,
        re.I | re.S,
    )
    if not (title_match and doi_match and abstract_match):
        raise RuntimeError(f"Incomplete IJCAI detail page: {url}")
    return {
        "venue": "IJCAI",
        "year": year,
        "title": html.unescape(title_match.group(1)).strip(),
        "authors": authors,
        "firstAuthorAffiliation": "N/A",
        "track": strip_tags(track_match.group(1)) if track_match else "Proceedings",
        "status": "Published",
        "doi": normalize_doi(doi_match.group(1)),
        "url": url,
        "officialSource": url,
        "abstractSource": url,
        "abstract": strip_tags(abstract_match.group(1)),
    }


def collect_ijcai(start_year: int, overrides: dict[str, dict[str, str]]) -> tuple[int, str, list[dict]]:
    year, source_url, index = discover_ijcai_year(start_year)
    entries = re.findall(
        rf'<div id="paper\d+" class="paper_wrapper">.*?<div class="title">(.*?)</div>.*?'
        rf'<a href="(/proceedings/{year}/\d+)">\s*Details</a>',
        index,
        flags=re.I | re.S,
    )
    papers = []
    for raw_title, path in entries:
        title = strip_tags(raw_title)
        if not CANDIDATE_RE.search(title):
            continue
        paper = parse_ijcai_detail(f"https://www.ijcai.org{path}", year)
        score, signals = relevance(paper["title"], paper["abstract"])
        if score < 5:
            continue
        paper.update(relevanceScore=score, relevanceSignals=signals)
        papers.append(apply_classification(paper, overrides))
    return year, source_url, sorted(papers, key=lambda item: item["title"].lower())


def markdown_for(venue: str, year: int, papers: list[dict], source_url: str) -> str:
    grouped: dict[tuple[str, str], list[dict]] = {}
    for paper in papers:
        grouped.setdefault((paper["category"], paper["target"]), []).append(paper)
    lines = [
        f"# {venue.lower()}{year} - Jailbreak Research Papers",
        "",
        f"**Total Papers:** {len(papers)}",
        "",
        f"> Eligibility source: [{venue} {year} official proceedings]({source_url}).",
        "> Candidates are discovered from titles, then retained and classified using title + abstract signals.",
        "",
    ]
    for category in ["Attack", "Defense", "Benchmark", "Mechanism", "Other"]:
        targets = [target for target in ["Text", "Vision", "Hybrid", "Agent"] if (category, target) in grouped]
        if not targets:
            continue
        lines.extend([f"## {category}", ""])
        for target in targets:
            lines.extend(
                [
                    f"### {target}",
                    "",
                    "| Title | First Author Affiliation | Track | Status | Link |",
                    "|---|:---:|:---:|:---:|:---:|",
                ]
            )
            for paper in grouped[(category, target)]:
                safe_title = paper["title"].replace("|", "\\|")
                affiliation = paper["firstAuthorAffiliation"].replace("|", "\\|")
                track = paper["track"].replace("|", "\\|")
                lines.append(
                    f"| {safe_title} | {affiliation} | {track} | {paper['status']} | [🔗]({paper['url']}) |"
                )
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_readme(venue: str, year: int, count: int, relative_path: str) -> None:
    path = ROOT / "README.md"
    content = path.read_text(encoding="utf-8")
    row = (
        f"<tr><td style='text-align:center;vertical-align:middle' rowspan='1'><strong>{venue}</strong></td>"
        f"<td style='text-align:center'>{year}</td><td><a href='{relative_path}'>{venue}{year}</a></td>"
        f"<td style='text-align:center'>{count}</td></tr>"
    )
    pattern = re.compile(
        rf"<tr><td[^>]*><strong>{re.escape(venue)}</strong></td>.*?</tr>", re.I | re.S
    )
    if pattern.search(content):
        content = pattern.sub(row, content, count=1)
    else:
        content = content.replace("</table>", row + "\n</table>", 1)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=dt.date.today().year)
    args = parser.parse_args()
    overrides = load_overrides()

    collections = []
    for collector in (collect_kdd, collect_ijcai):
        collections.append(collector(args.start_year, overrides))

    all_papers: list[dict] = []
    sources = []
    for venue, (year, source_url, papers) in zip(("KDD", "IJCAI"), collections):
        output = ROOT / "Conference" / venue / f"{venue.lower()}{year}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown_for(venue, year, papers, source_url), encoding="utf-8")
        update_readme(venue, year, len(papers), str(output.relative_to(ROOT)))
        sources.append({"venue": venue, "year": year, "url": source_url, "paperCount": len(papers)})
        all_papers.extend(papers)
        print(f"{venue} {year}: wrote {len(papers)} papers to {output.relative_to(ROOT)}")

    payload = {
        "eligibility": "Official proceedings index plus formal DOI/detail page; abstracts are used only for relevance and classification.",
        "sources": sources,
        "papers": all_papers,
    }
    old_payload = {}
    if METADATA_PATH.exists():
        old_payload = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    comparable_old = {key: old_payload.get(key) for key in ("eligibility", "sources", "papers")}
    if comparable_old != payload:
        payload["generatedAt"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    elif old_payload.get("generatedAt"):
        payload["generatedAt"] = old_payload["generatedAt"]
    METADATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    METADATA_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote metadata for {len(all_papers)} papers to {METADATA_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
