#!/usr/bin/env python3
"""Validate the normalized temporary bibliography repository."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "source-catalog.json"
RAW_ROOT = ROOT / "sources" / "raw-md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    if not CATALOG.exists():
        errors.append("Missing catalog/source-catalog.json")
        records = []
    else:
        payload = json.loads(CATALOG.read_text(encoding="utf-8"))
        records = payload.get("sources", [])
        if not isinstance(records, list):
            errors.append("Catalog 'sources' must be a list")
            records = []

    ids: set[str] = set()
    paths: set[str] = set()
    for record in records:
        source_id = str(record.get("source_id") or "")
        normalized_path = str(record.get("normalized_path") or "")
        if not source_id:
            errors.append("Catalog record without source_id")
        elif source_id in ids:
            errors.append(f"Duplicate source_id: {source_id}")
        ids.add(source_id)
        if not normalized_path:
            errors.append(f"{source_id}: missing normalized_path")
            continue
        if normalized_path in paths:
            errors.append(f"Duplicate normalized_path: {normalized_path}")
        paths.add(normalized_path)
        path = ROOT / normalized_path
        if not path.exists():
            errors.append(f"{source_id}: missing file {normalized_path}")
            continue
        if path.suffix.lower() != ".md":
            errors.append(f"{source_id}: raw archive path is not Markdown: {normalized_path}")
        expected = str(record.get("sha256") or "")
        if expected and sha256(path) != expected:
            errors.append(f"{source_id}: SHA-256 mismatch for {normalized_path}")

    raw_files = {path.relative_to(ROOT).as_posix() for path in RAW_ROOT.glob("*.md")}
    untracked = sorted(raw_files - paths)
    missing_from_raw = sorted(paths - raw_files)
    if untracked:
        errors.append(f"Uncataloged raw Markdown files: {', '.join(untracked[:10])}")
    if missing_from_raw:
        errors.append(f"Catalog paths outside/missing from raw archive: {', '.join(missing_from_raw[:10])}")

    legacy = [path.as_posix() for path in ROOT.glob("Group*/Group*Files") if path.is_dir()]
    if legacy:
        errors.append(f"Legacy grouped source directories remain: {', '.join(legacy)}")

    required_paths = [
        ROOT / "sources" / "group-reports",
        ROOT / "catalog" / "source-catalog.csv",
        ROOT / "catalog" / "malformed-or-missing.md",
        ROOT / "catalog" / "duplicate-groups.md",
        ROOT / "excerpts" / "by-source",
        ROOT / "excerpts" / "by-topic",
        ROOT / "queues" / "next-sources.md",
        ROOT / "queues" / "references-to-screen.csv",
        ROOT / "archive" / "original-path-map.csv",
        ROOT / "incoming" / "README.md",
    ]
    for path in required_paths:
        if not path.exists():
            errors.append(f"Missing required path: {path.relative_to(ROOT)}")

    path_map = ROOT / "archive" / "original-path-map.csv"
    if path_map.exists():
        with path_map.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != len(records):
            errors.append(f"Path map has {len(rows)} rows but catalog has {len(records)} sources")

    if errors:
        print("Bibliography validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Bibliography validation passed for {len(records)} sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
