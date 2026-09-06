#!/usr/bin/env python3
"""Collect 2026 published and officially accepted jailbreak papers.

Eligibility is established only by an official proceedings, accepted-papers,
or conference-program page. Abstracts enrich relevance scoring; arXiv alone is
never treated as evidence of acceptance.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup

from update_conference_papers import (
    CANDIDATE_RE,
    apply_classification,
    crossref_author_metadata,
    fetch,
    load_overrides,
    markdown_for,
    normalize_doi,
    openalex_abstract,
    relevance,
    strip_tags,
)


ROOT = Path(__file__).resolve().parents[1]
YEAR = 2026
METADATA_PATH = ROOT / "data" / f"conference_{YEAR}.json"


def eligible(paper: dict, overrides: dict[str, dict[str, str]]) -> dict | None:
    title = re.sub(r"\s+", " ", html.unescape(paper["title"])).strip()
    abstract = re.sub(r"\s+", " ", html.unescape(paper.get("abstract", ""))).strip()
    if not CANDIDATE_RE.search(title):
        return None
    score, signals = relevance(title, abstract)
    if score < 5:
        return None
    paper.update(title=title, abstract=abstract, relevanceScore=score, relevanceSignals=signals)
    return apply_classification(paper, overrides)


def parallel_map(function, values: list, workers: int = 8) -> list:
    results = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(function, value): value for value in values}
        for future in as_completed(futures):
            try:
                value = future.result()
            except Exception as error:  # keep one transient page from aborting the full update
                print(f"warning: {futures[future]}: {error}", file=sys.stderr)
                continue
            if value:
                results.append(value)
    return results


def collect_virtual(venue: str, index_url: str, overrides: dict) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(fetch(index_url), "html.parser")
    candidates: dict[str, str] = {}
    for link in soup.select(f'a[href*="/virtual/{YEAR}/poster/"]'):
        title = link.get_text(" ", strip=True)
        if title and CANDIDATE_RE.search(title):
            candidates[urllib.parse.urljoin(index_url, link.get("href"))] = title

    def detail(item: tuple[str, str]) -> dict | None:
        url, fallback_title = item
        page = BeautifulSoup(fetch(url), "html.parser")
        metadata = {}
        for script in page.select('script[type="application/ld+json"]'):
            try:
                value = json.loads(script.string or "{}")
            except json.JSONDecodeError:
                continue
            records = value if isinstance(value, list) else [value]
            metadata = next((record for record in records if isinstance(record, dict) and record.get("name")), metadata)
        authors = []
        for author in metadata.get("author", []):
            name = author.get("name", "") if isinstance(author, dict) else str(author)
            if name:
                authors.append(name)
        abstract_node = page.select_one(".abstract-text-inner") or page.select_one(".abstract-section")
        paper = {
            "venue": venue,
            "year": YEAR,
            "title": metadata.get("name") or fallback_title,
            "authors": authors,
            "firstAuthorAffiliation": "N/A",
            "track": "Main Conference",
            "status": "Accepted",
            "doi": "",
            "url": url,
            "officialSource": index_url,
            "abstractSource": url,
            "abstract": abstract_node.get_text(" ", strip=True) if abstract_node else metadata.get("description", ""),
        }
        return eligible(paper, overrides)

    return index_url, sorted(parallel_map(detail, list(candidates.items())), key=lambda p: p["title"].lower())


def collect_acl(overrides: dict) -> tuple[str, list[dict]]:
    source_url = f"https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{YEAR}.acl.xml"
    root = ET.fromstring(fetch(source_url))
    papers = []
    for volume in root.findall("volume"):
        volume_id = volume.get("id", "")
        if volume_id not in {"long", "short", "industry"}:
            continue
        track = f"ACL {YEAR} " + volume_id.title()
        for node in volume.findall("paper"):
            title_node = node.find("title")
            if title_node is None:
                continue
            title = "".join(title_node.itertext())
            if not CANDIDATE_RE.search(title):
                continue
            anthology_id = (node.findtext("url") or f"{YEAR}.acl-{volume_id}.{node.get('id')}").strip()
            authors = []
            first_affiliation = "N/A"
            for author in node.findall("author"):
                name = " ".join(filter(None, [author.findtext("first"), author.findtext("last")])).strip()
                if name:
                    authors.append(name)
                if first_affiliation == "N/A" and author.findtext("affiliation"):
                    first_affiliation = author.findtext("affiliation").strip()
            doi = normalize_doi(node.findtext("doi") or "")
            paper = {
                "venue": "ACL", "year": YEAR, "title": title, "authors": authors,
                "firstAuthorAffiliation": first_affiliation, "track": track, "status": "Published",
                "doi": doi, "url": f"https://aclanthology.org/{anthology_id}/",
                "officialSource": source_url, "abstractSource": source_url,
                "abstract": node.findtext("abstract") or "",
            }
            value = eligible(paper, overrides)
            if value:
                papers.append(value)
    return source_url, sorted(papers, key=lambda p: p["title"].lower())


def crossref_items(container: str) -> list[dict]:
    exact: list[dict] = []
    offset = 0
    total = None
    base_url = (
        "https://api.crossref.org/journals/2374-3468/works"
        if container == "Proceedings of the AAAI Conference on Artificial Intelligence"
        else "https://api.crossref.org/works"
    )
    while total is None or offset < total:
        params = urllib.parse.urlencode({
            "query.container-title": container,
            "filter": f"from-pub-date:{YEAR}-01-01,until-pub-date:{YEAR}-12-31",
            "rows": 1000,
            "offset": offset,
            "mailto": "research@example.com",
        })
        message = json.loads(fetch(f"{base_url}?{params}"))["message"]
        batch = message.get("items", [])
        total = min(int(message.get("total-results", 0)), 10000 if "journals/" in base_url else 2000)
        exact.extend(item for item in batch if html.unescape((item.get("container-title") or [""])[0]) == container)
        if not batch:
            break
        offset += len(batch)
        time.sleep(0.2)
    return list({normalize_doi(item.get("DOI", "")): item for item in exact}.values())


def collect_crossref(venue: str, container: str, source_url: str, overrides: dict) -> tuple[str, list[dict]]:
    candidates = [
        item for item in crossref_items(container)
        if CANDIDATE_RE.search(strip_tags((item.get("title") or [""])[0]))
    ]

    def detail(item: dict) -> dict | None:
        title = strip_tags((item.get("title") or [""])[0])
        doi = normalize_doi(item.get("DOI", ""))
        abstract = strip_tags(item.get("abstract", "")) or openalex_abstract(doi)
        bibliography = crossref_author_metadata(item)
        paper = {
            "venue": venue, "year": YEAR, "title": title,
            "authors": bibliography.get("authors", []),
            "firstAuthorAffiliation": bibliography.get("firstAuthorAffiliation", "N/A"),
            "track": container, "status": "Published", "doi": doi,
            "url": f"https://doi.org/{doi}", "officialSource": source_url,
            "abstractSource": f"https://api.openalex.org/works/https://doi.org/{doi}",
            "abstract": abstract,
        }
        return eligible(paper, overrides)

    return source_url, sorted(parallel_map(detail, candidates, workers=6), key=lambda p: p["title"].lower())


def collect_ccs(overrides: dict) -> tuple[str, list[dict]]:
    """Parse CCS's official accepted-paper table before Crossref indexing."""
    source_url = f"https://www.sigsac.org/ccs/CCS{YEAR}/program/accepted-papers.html"
    soup = BeautifulSoup(fetch(source_url), "html.parser")
    papers = []
    for row in soup.select("table.accepted-papers-table tr"):
        cells = row.find_all("td", recursive=False)
        if len(cells) < 2:
            continue
        title = cells[0].get_text(" ", strip=True)
        if not title or not CANDIDATE_RE.search(title):
            continue
        author_lines = [line.strip() for line in cells[1].stripped_strings if line.strip()]
        first_affiliation = "N/A"
        if author_lines:
            affiliation = re.search(r"\(([^()]*)\)\s*$", author_lines[0])
            if affiliation:
                first_affiliation = affiliation.group(1).strip()
        paper = {
            "venue": "CCS", "year": YEAR, "title": title,
            "authors": author_lines, "firstAuthorAffiliation": first_affiliation,
            "track": "Accepted Papers", "status": "Accepted", "doi": "",
            "url": source_url, "officialSource": source_url,
            "abstractSource": source_url, "abstract": "",
        }
        value = eligible(paper, overrides)
        if value:
            papers.append(value)
    return source_url, sorted(papers, key=lambda p: p["title"].lower())


def walk_named_records(value):
    if isinstance(value, dict):
        if value.get("name") and value.get("desc") and value.get("tracks"):
            yield value
        for child in value.values():
            yield from walk_named_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_named_records(child)


def collect_kdd(overrides: dict) -> tuple[str, list[dict]]:
    if YEAR != 2026:
        raise RuntimeError("KDD's event API ID is not configured for this year")
    source_url = f"https://kdd{YEAR}.kdd.org/full-program/"
    api_url = (
        "https://whova.com/xems/apis/event_webpage/agenda/public/get_agendas/"
        "?event_id=As22EvgjdjIC7XoLbAG4Y41bA2JQnxLAEK-iJyT4y1Y%3D"
    )
    records = {}
    for item in walk_named_records(json.loads(fetch(api_url))):
        title = html.unescape(item["name"]).strip()
        doi_match = re.search(r"doi\.org/(10\.[^/\s<]+/[^\s<]+)", item.get("desc", ""), re.I)
        tracks = [track.get("name", "") for track in item.get("tracks", [])]
        if doi_match and CANDIDATE_RE.search(title) and any("Track" in track for track in tracks):
            records[normalize_doi(doi_match.group(1).rstrip("/"))] = (title, ", ".join(tracks))

    def detail(item: tuple[str, tuple[str, str]]) -> dict | None:
        doi, (title, track) = item
        published = True
        try:
            bibliography = crossref_author_metadata(json.loads(fetch(f"https://api.crossref.org/works/{doi}"))["message"])
        except Exception:
            bibliography = {}
            published = False
        paper = {
            "venue": "KDD", "year": YEAR, "title": title,
            "authors": bibliography.get("authors", []),
            "firstAuthorAffiliation": bibliography.get("firstAuthorAffiliation", "N/A"),
            "track": track, "status": "Published" if published else "Accepted", "doi": doi,
            "url": f"https://doi.org/{doi}", "officialSource": source_url,
            "abstractSource": f"https://api.openalex.org/works/https://doi.org/{doi}",
            "abstract": openalex_abstract(doi),
        }
        return eligible(paper, overrides)

    return source_url, sorted(parallel_map(detail, list(records.items()), workers=6), key=lambda p: p["title"].lower())


def collect_ijcai(overrides: dict) -> tuple[str, list[dict]]:
    source_url = f"https://{YEAR}.ijcai.org/accepted-papers/"
    soup = BeautifulSoup(fetch(source_url), "html.parser")
    papers = []
    for node in soup.select("li.ij-paper"):
        title_node = node.select_one(".ij-ptitle")
        if not title_node:
            continue
        title = title_node.get_text(" ", strip=True)
        if not CANDIDATE_RE.search(title):
            continue
        abstract_node = node.select_one(".ij-abs")
        abstract = abstract_node.get_text(" ", strip=True).removeprefix("Toggle abstract") if abstract_node else ""
        paper = {
            "venue": "IJCAI", "year": YEAR, "title": title,
            "authors": [x.get_text(" ", strip=True) for x in node.select(".ij-author")],
            "firstAuthorAffiliation": "N/A", "track": "Main Conference", "status": "Accepted",
            "doi": "", "url": source_url, "officialSource": source_url,
            "abstractSource": source_url, "abstract": abstract,
        }
        value = eligible(paper, overrides)
        if value:
            papers.append(value)
    return source_url, sorted(papers, key=lambda p: p["title"].lower())


def collect_usenix(overrides: dict) -> tuple[str, list[dict]]:
    source_url = f"https://www.usenix.org/conference/usenixsecurity{str(YEAR)[-2:]}/technical-sessions"
    soup = BeautifulSoup(fetch(source_url), "html.parser")
    links = {}
    for link in soup.select("article.node-paper h2 a"):
        title = link.get_text(" ", strip=True)
        if CANDIDATE_RE.search(title):
            links[urllib.parse.urljoin(source_url, link.get("href"))] = title

    def detail(item: tuple[str, str]) -> dict | None:
        url, fallback_title = item
        page = BeautifulSoup(fetch(url), "html.parser")
        title_node = page.select_one("h1.page-title") or page.select_one("h1")
        abstract_node = page.select_one(".field-name-field-paper-description-long") or page.select_one(".field-name-field-paper-description")
        authors_node = page.select_one(".field-name-field-paper-people-text")
        author_text = authors_node.get_text(" ", strip=True) if authors_node else ""
        paper = {
            "venue": "USENIX Security", "year": YEAR,
            "title": title_node.get_text(" ", strip=True) if title_node else fallback_title,
            "authors": [part.strip() for part in re.split(r",|\band\b", author_text) if part.strip()],
            "firstAuthorAffiliation": "N/A", "track": "Technical Sessions", "status": "Accepted",
            "doi": "", "url": url, "officialSource": source_url,
            "abstractSource": url, "abstract": abstract_node.get_text(" ", strip=True) if abstract_node else "",
        }
        return eligible(paper, overrides)

    return source_url, sorted(parallel_map(detail, list(links.items())), key=lambda p: p["title"].lower())


def collect_ndss(overrides: dict) -> tuple[str, list[dict]]:
    source_url = f"https://www.ndss-symposium.org/ndss{YEAR}/accepted-papers/"
    soup = BeautifulSoup(fetch(source_url), "html.parser")
    links = {
        link.get("href"): link.get_text(" ", strip=True)
        for link in soup.select("h2.pt-cv-title a")
        if CANDIDATE_RE.search(link.get_text(" ", strip=True))
    }

    def detail(item: tuple[str, str]) -> dict | None:
        url, fallback_title = item
        page = BeautifulSoup(fetch(url), "html.parser")
        title_node = page.select_one("h1.entry-title")
        data = page.select_one(".paper-data")
        paragraphs = [p.get_text(" ", strip=True) for p in data.find_all("p", recursive=False)] if data else []
        authors = paragraphs[0] if paragraphs else ""
        abstract = " ".join(paragraphs[1:]) if len(paragraphs) > 1 else ""
        paper = {
            "venue": "NDSS", "year": YEAR,
            "title": title_node.get_text(" ", strip=True) if title_node else fallback_title,
            "authors": [part.strip() for part in re.split(r"\),\s*|,\s*(?=[A-Z][a-z]+\s)", authors) if part.strip()],
            "firstAuthorAffiliation": "N/A", "track": "Accepted Papers", "status": "Accepted",
            "doi": "", "url": url, "officialSource": source_url,
            "abstractSource": url, "abstract": abstract,
        }
        return eligible(paper, overrides)

    return source_url, sorted(parallel_map(detail, list(links.items())), key=lambda p: p["title"].lower())


def upsert_readme(venue: str, count: int, relative_path: str) -> None:
    path = ROOT / "README.md"
    content = path.read_text(encoding="utf-8")
    block_pattern = re.compile(
        rf"<tr><td[^>]*><strong>{re.escape(venue)}</strong></td>.*?</tr>"
        rf"(?:\n<tr><td style='text-align:center'>.*?</tr>)*", re.I | re.S,
    )
    match = block_pattern.search(content)
    records = {YEAR: (relative_path, count)}
    if match:
        for year, href, old_count in re.findall(
            r"<td style='text-align:center'>(20\d{2})</td><td><a href='([^']+)'[^>]*>.*?</a></td>"
            r"<td style='text-align:center'>(\d+)</td>", match.group(0), re.S,
        ):
            records.setdefault(int(year), (href, int(old_count)))
    rows = []
    ordered = sorted(records.items(), reverse=True)
    for index, (year, (href, paper_count)) in enumerate(ordered):
        prefix = (
            f"<tr><td style='text-align:center;vertical-align:middle' rowspan='{len(ordered)}'><strong>{venue}</strong></td>"
            if index == 0 else "<tr>"
        )
        rows.append(
            f"{prefix}<td style='text-align:center'>{year}</td><td><a href='{href}'>{venue}{year}</a></td>"
            f"<td style='text-align:center'>{paper_count}</td></tr>"
        )
    replacement = "\n".join(rows)
    if match:
        content = content[:match.start()] + replacement + content[match.end():]
    else:
        content = content.replace("</table>", replacement + "\n</table>", 1)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    global YEAR, METADATA_PATH
    parser = argparse.ArgumentParser()
    parser.add_argument("--venues", nargs="+", help="Update only these venues and preserve other records")
    parser.add_argument("--year", type=int, default=YEAR, help="Conference edition year to collect")
    args = parser.parse_args()
    YEAR = args.year
    METADATA_PATH = ROOT / "data" / f"conference_{YEAR}.json"
    overrides = load_overrides()
    collectors = [
        ("ICLR", lambda: collect_virtual("ICLR", f"https://iclr.cc/virtual/{YEAR}/papers.html?filter=titles", overrides)),
        ("ICML", lambda: collect_virtual("ICML", f"https://icml.cc/virtual/{YEAR}/papers.html?filter=titles", overrides)),
        ("AAAI", lambda: collect_crossref("AAAI", "Proceedings of the AAAI Conference on Artificial Intelligence", "https://ojs.aaai.org/index.php/AAAI/", overrides)),
        ("ACL", lambda: collect_acl(overrides)),
        ("WWW", lambda: collect_crossref("WWW", f"Proceedings of the ACM Web Conference {YEAR}", f"https://www{YEAR}.thewebconf.org/accepted/research-tracks.html", overrides)),
        ("SP", lambda: collect_crossref("SP", f"{YEAR} IEEE Symposium on Security and Privacy (SP)", f"https://sp{YEAR}.ieee-security.org/accepted-papers.html", overrides)),
        ("CCS", lambda: collect_ccs(overrides)),
        ("NDSS", lambda: collect_ndss(overrides)),
        ("KDD", lambda: collect_kdd(overrides)),
        ("IJCAI", lambda: collect_ijcai(overrides)),
        ("USENIX Security", lambda: collect_usenix(overrides)),
    ]
    selected = set(args.venues or [venue for venue, _ in collectors])
    unknown = selected - {venue for venue, _ in collectors}
    if unknown:
        parser.error("unknown venues: " + ", ".join(sorted(unknown)))
    old = json.loads(METADATA_PATH.read_text()) if METADATA_PATH.exists() else {}
    all_papers = [paper for paper in old.get("papers", []) if paper.get("venue") not in selected]
    sources = [source for source in old.get("sources", []) if source.get("venue") not in selected]
    for venue, collector in collectors:
        if venue not in selected:
            continue
        source_url, papers = collector()
        output = ROOT / "Conference" / venue / f"{venue.lower().replace(' ', '')}{YEAR}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown_for(venue, YEAR, papers, source_url).replace("official proceedings", "official proceedings / accepted-paper index"), encoding="utf-8")
        upsert_readme(venue, len(papers), str(output.relative_to(ROOT)))
        sources.append({"venue": venue, "year": YEAR, "url": source_url, "paperCount": len(papers)})
        all_papers.extend(papers)
        print(f"{venue} {YEAR}: wrote {len(papers)} papers to {output.relative_to(ROOT)}")

    payload = {
        "eligibility": "Official proceedings, accepted-paper index, or conference program; preprints alone are excluded.",
        "statusSemantics": {"Published": "Formal proceedings/DOI record", "Accepted": "Official acceptance/program page"},
        "sources": sources,
        "papers": all_papers,
    }
    comparable = {key: old.get(key) for key in payload}
    payload["generatedAt"] = (
        old.get("generatedAt") if comparable == payload and old.get("generatedAt")
        else dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    )
    METADATA_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(all_papers)} accepted/published {YEAR} papers to {METADATA_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
