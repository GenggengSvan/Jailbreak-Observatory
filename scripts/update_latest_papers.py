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


def files_for(venue: str) -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "data" / "conference_2026.json"]
    paths.extend((ROOT / "Conference" / venue).glob("*.md"))
    return paths


def digest(paths: list[Path]) -> dict[str, str]:
    result = {}
    for path in paths:
        if path.exists():
            result[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main() -> int:
    checked = dt.date.today().isoformat()
    records = []
    any_success = False
    for venue in VENUES:
        paths = files_for(venue)
        before = digest(paths)
        command = [sys.executable, str(ROOT / "scripts" / "update_2026_papers.py"), "--venues", venue]
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
    history.setdefault("updates", []).append({"date": checked, "year": 2026, "venues": records})
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = sum(item["status"] == "failed" for item in records)
    print(f"Checked {len(records)} venues: {len(records) - failed} succeeded, {failed} failed.")
    return 0 if any_success else 1


if __name__ == "__main__":
    raise SystemExit(main())
