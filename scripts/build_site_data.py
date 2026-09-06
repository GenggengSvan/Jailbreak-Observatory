#!/usr/bin/env python3
"""Build the static visualization dataset from the repository's Markdown files."""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "data.js"
CONFERENCE_METADATA = sorted((ROOT / "data").glob("conference_*.json"))

CATEGORY_ORDER = {"Attack": 0, "Defense": 1, "Benchmark": 2, "Mechanism": 3, "Other": 4}
RELATION_LIMITS = {"affinity": 2, "counterpoint": 1, "context": 1}
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "against", "by", "for", "from", "in",
    "into", "is", "it", "language", "large", "llm", "llms", "model", "models", "of",
    "on", "or", "the", "their", "through", "to", "toward", "towards", "using", "via",
    "with", "jailbreak", "jailbreaking", "attack", "attacks", "defense", "defending",
}


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", value)
    return html.unescape(value).strip().strip("|").strip()


def normalize_title(value: str) -> str:
    value = html.unescape(value).lower().replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9]+", "", value)


def normalize_target(value: str) -> str:
    value = re.sub(r"\s*\(\d+\s+papers?\)\s*$", "", clean(value), flags=re.I)
    return value or "Text"


def normalize_category(value: str) -> str:
    value = clean(value)
    return value if value in CATEGORY_ORDER else "Other"


def stable_id(title: str) -> str:
    return "p-" + hashlib.sha1(normalize_title(title).encode()).hexdigest()[:12]


def parse_conference_files() -> list[dict]:
    papers: dict[str, dict] = {}
    for path in sorted((ROOT / "Conference").glob("*/*.md")):
        venue = path.parent.name
        year_match = re.search(r"20\d{2}", path.stem)
        if not year_match:
            continue
        year = int(year_match.group())
        category = "Other"
        target = "Text"

        for raw_line in path.read_text(encoding="utf-8").splitlines():
            if raw_line.startswith("## ") and not raw_line.startswith("### "):
                candidate = clean(raw_line[3:])
                if candidate in CATEGORY_ORDER:
                    category = candidate
                continue
            if raw_line.startswith("### "):
                candidate = normalize_target(raw_line[4:])
                if candidate:
                    target = candidate
                continue
            if not raw_line.startswith("|") or "http" not in raw_line or "---" in raw_line:
                continue

            cells = [clean(cell) for cell in raw_line.strip().strip("|").split("|")]
            if not cells or cells[0].lower() == "title":
                continue
            link_match = re.search(r"\((https?://[^)]+)\)", raw_line)
            title = cells[0]
            if not title or not link_match:
                continue

            key = normalize_title(title)
            paper = papers.setdefault(
                key,
                {
                    "id": stable_id(title),
                    "title": title,
                    "year": year,
                    "venue": venue,
                    "category": category,
                    "target": target,
                    "url": link_match.group(1),
                    "citations": None,
                    "abstract": "",
                    "source": str(path.relative_to(ROOT)),
                },
            )
            paper.update({"year": year, "venue": venue, "category": category, "target": target})
    return list(papers.values())


def parse_citations() -> list[dict]:
    path = ROOT / "citations_over_50.md"
    content = path.read_text(encoding="utf-8")
    entries = []
    for block in re.split(r"(?m)^## ", content)[1:]:
        title, _, body = block.partition("\n")
        citations = re.search(r"📑 Citations:\s*(\d+)", body)
        meta = re.search(r"🎯 Target:\s*(.*?)\s+🗂️ Category:\s*(\w+)", body)
        publication = re.search(r"📅 Year:\s*(\d{4})\s+📍 Venue:\s*(.+)", body)
        abstract = re.search(r"Abstract:\s*\n(.*?)(?=\n(?:## |$))", body, re.S)
        if not (citations and meta and publication):
            continue
        abstract_text = re.sub(r"\s+", " ", abstract.group(1).strip()) if abstract else ""
        code_match = re.search(r"https?://github\.com/[^\s.)]+", abstract_text)
        entries.append(
            {
                "id": stable_id(title),
                "title": clean(title),
                "year": int(publication.group(1)),
                "venue": publication.group(2).strip(),
                "category": normalize_category(meta.group(2)),
                "target": normalize_target(meta.group(1)),
                "url": "",
                "codeUrl": code_match.group(0) if code_match else "",
                "citations": int(citations.group(1)),
                "abstract": abstract_text,
                "source": "citations_over_50.md",
            }
        )
    return entries


def parse_latest_metadata() -> list[dict]:
    entries = []
    for metadata_path in CONFERENCE_METADATA:
        if metadata_path.name == "conference_overrides.json":
            continue
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
        for paper in payload.get("papers", []):
            entries.append({
                "id": stable_id(paper["title"]),
                "title": paper["title"],
                "year": int(paper["year"]),
                "venue": paper["venue"],
                "category": normalize_category(paper["category"]),
                "target": normalize_target(paper["target"]),
                "url": paper["url"],
                "codeUrl": "",
                "citations": None,
                "abstract": paper.get("abstract", ""),
                "doi": paper.get("doi", ""),
                "officialSource": paper.get("officialSource", ""),
                "relevanceSignals": paper.get("relevanceSignals", []),
                "status": paper.get("status", "Published"),
                "source": str(metadata_path.relative_to(ROOT)),
            })
    return entries


def merge_papers(conference: list[dict], cited: list[dict], latest: list[dict]) -> list[dict]:
    by_title = {normalize_title(p["title"]): p for p in conference}
    for enriched in [*cited, *latest]:
        key = normalize_title(enriched["title"])
        if key in by_title:
            existing = by_title[key]
            existing.update(
                abstract=enriched.get("abstract", "") or existing.get("abstract", ""),
                codeUrl=enriched.get("codeUrl", "") or existing.get("codeUrl", ""),
            )
            if enriched.get("citations") is not None:
                existing["citations"] = enriched["citations"]
            for field in ("doi", "officialSource", "relevanceSignals", "status"):
                if enriched.get(field):
                    existing[field] = enriched[field]
            if not existing.get("url"):
                existing["url"] = enriched.get("url", "")
        else:
            by_title[key] = enriched
    return sorted(
        by_title.values(),
        key=lambda p: (p["year"], CATEGORY_ORDER.get(p["category"], 9), p["venue"], p["title"]),
    )


def tokens(title: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", title.lower())
        if len(token) > 2 and token not in STOP_WORDS
    }


def relation_score(a: dict, b: dict) -> tuple[float, str]:
    ta, tb = tokens(a["title"]), tokens(b["title"])
    union = ta | tb
    overlap = len(ta & tb) / len(union) if union else 0
    same_target = a["target"] == b["target"]
    same_category = a["category"] == b["category"]
    opposite = {a["category"], b["category"]} == {"Attack", "Defense"}

    if opposite and same_target:
        score = 1.15 + overlap * 5 + max(0, 1 - abs(a["year"] - b["year"]) * 0.3)
        return score, "counterpoint"
    if same_category and same_target:
        score = 1.4 + overlap * 6 + (0.35 if a["venue"] == b["venue"] else 0)
        return score, "affinity"
    if same_target and ({a["category"], b["category"]} & {"Benchmark", "Mechanism"}):
        score = 0.85 + overlap * 5
        return score, "context"
    return overlap * 3, "context"


def build_relations(papers: list[dict]) -> list[dict]:
    candidates: list[tuple[float, str, int, int]] = []
    for left in range(len(papers)):
        for right in range(left + 1, len(papers)):
            score, kind = relation_score(papers[left], papers[right])
            if score >= (1.1 if kind == "context" else 1.4):
                candidates.append((score, kind, left, right))

    relation_counts = [dict.fromkeys(RELATION_LIMITS, 0) for _ in papers]
    chosen: list[tuple[float, str, int, int]] = []
    ranked = sorted(
        candidates,
        key=lambda option: (
            -option[0],
            option[1],
            papers[option[2]]["id"],
            papers[option[3]]["id"],
        ),
    )
    for score, kind, left, right in ranked:
        limit = RELATION_LIMITS[kind]
        if relation_counts[left][kind] >= limit or relation_counts[right][kind] >= limit:
            continue
        chosen.append((score, kind, left, right))
        relation_counts[left][kind] += 1
        relation_counts[right][kind] += 1

    return [
        {
            "source": papers[left]["id"],
            "target": papers[right]["id"],
            "kind": kind,
            "score": round(score, 3),
        }
        for score, kind, left, right in sorted(chosen, key=lambda item: (item[2], item[3], item[1]))
    ]


def main() -> None:
    papers = merge_papers(parse_conference_files(), parse_citations(), parse_latest_metadata())
    relations = build_relations(papers)
    payload = {
        "generatedFrom": "Conference/**/*.md + citations_over_50.md + data/conference_*.json",
        "papers": papers,
        "relations": relations,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "window.OBSERVATORY_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(papers)} papers and {len(relations)} relations to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
