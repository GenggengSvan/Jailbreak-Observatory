#!/usr/bin/env python3
"""Run the per-conference latest-edition collectors with failure isolation.

The conference pages do not share a schema, so this module deliberately acts
as an orchestrator rather than trying to parse every site itself.  Each venue
is delegated to the adapter in ``update_2026_papers.py``.  A failed adapter is
recorded and skipped; successful adapters can still update the other venues.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "data" / "conference_update_history.json"
VENUES = ("ICLR", "ICML", "AAAI", "ACL", "WWW", "SP", "CCS", "NDSS", "KDD", "IJCAI", "USENIX Security")


def files_for(venue: str, year: int) -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "data" / f"conference_{year}.json"]
    paths.append(ROOT / "Conference" / venue / f"{venue.lower().replace(' ', '')}{year}.md")
    return paths


def digest(paths: list[Path]) -> dict[str, str]:
    result = {}
    for path in paths:
        if path.exists():
            result[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main() -> int:
    checked = dt.date.today().isoformat()
    target_year = dt.date.today().year
    records = []
    any_success = False
    for venue in VENUES:
        paths = files_for(venue, target_year)
        before = digest(paths)
        expected_output = ROOT / "Conference" / venue / f"{venue.lower().replace(' ', '')}{target_year}.md"
        if expected_output.exists():
            any_success = True
            print(f"{venue}: skipped_existing ({target_year})")
            records.append({"venue": venue, "status": "skipped_existing", "changedFiles": []})
            continue
        command = [sys.executable, str(ROOT / "scripts" / "update_2026_papers.py"), "--year", str(target_year), "--venues", venue]
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        after = digest(paths)
        changed = sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path))
        if completed.returncode == 0:
            any_success = True
            status = "updated" if changed else "unchanged"
            print(f"{venue}: {status}")
        else:
            status = "failed"
            print(f"{venue}: failed (adapter exit {completed.returncode})", file=sys.stderr)
            if completed.stderr:
                print(completed.stderr[-2000:], file=sys.stderr)
        records.append({"venue": venue, "status": status, "changedFiles": changed})

    history = json.loads(HISTORY.read_text(encoding="utf-8")) if HISTORY.exists() else {"updates": []}
    history.setdefault("updates", []).append({"date": checked, "year": target_year, "venues": records})
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = sum(item["status"] == "failed" for item in records)
    skipped = sum(item["status"] == "skipped_existing" for item in records)
    print(f"Checked {len(records)} venues: {len(records) - failed - skipped} updated, {skipped} existing skipped, {failed} failed.")
    return 0 if any_success else 1


if __name__ == "__main__":
    raise SystemExit(main())
