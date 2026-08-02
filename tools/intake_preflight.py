#!/usr/bin/env python3
"""Preflight incoming source files before canonical bibliography import.

Blank Markdown files do not contain enough evidence to establish source identity.
They are therefore preserved losslessly as unresolved intake records instead of
being imported as metadata-only sources or collapsed together by the identical
zero-byte content hash.
"""
from __future__ import annotations

import csv
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "new-sources"
UNRESOLVED = ROOT / "unresolved-intake"
REPORT = ROOT / "catalog" / "unresolved-intake.csv"
REPORT_FIELDS = ["Stored path", "Original path", "Content SHA-256", "Reason"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ascii_archive_name(relative: Path, content_hash: str) -> str:
    identity = hashlib.sha256(relative.as_posix().encode("utf-8")).hexdigest()[:16].upper()
    suffix = re.sub(r"[^a-z0-9]+", "-", relative.suffix.casefold().lstrip(".")) or "file"
    return f"UNRESOLVED-{identity}-{content_hash[:12].upper()}.{suffix}"


def process_blank_markdown(
    incoming: Path = INCOMING,
    unresolved: Path = UNRESOLVED,
    report: Path = REPORT,
) -> list[dict[str, str]]:
    unresolved.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []

    if incoming.exists():
        for path in sorted(incoming.rglob("*.md")):
            if path.name == "README.md" or not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if text.strip():
                continue

            relative = path.relative_to(incoming)
            content_hash = sha256(path)
            target = unresolved / ascii_archive_name(relative, content_hash)
            if target.exists():
                if sha256(target) != content_hash:
                    raise RuntimeError(f"Unresolved intake archive collision: {target}")
                path.unlink()
            else:
                shutil.move(str(path), target)

            rows.append({
                "Stored path": target.relative_to(ROOT if ROOT in target.parents else unresolved.parent).as_posix()
                if ROOT in target.parents else target.as_posix(),
                "Original path": relative.as_posix(),
                "Content SHA-256": content_hash,
                "Reason": "blank Markdown; source identity cannot be established from content",
            })

    with report.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    return rows


def main() -> int:
    rows = process_blank_markdown()
    print(f"Archived {len(rows)} blank Markdown files as unresolved intake without creating source records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
