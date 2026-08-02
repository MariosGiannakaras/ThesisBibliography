#!/usr/bin/env python3
"""Remove only redundant exact PDF copies while preserving source records.

A PDF filename, title, DOI, URL, or publication identity is never sufficient for
source-record deletion. This tool groups PDF files only by their actual SHA-256
(or Git LFS object ID), keeps one deterministic best archival copy, removes the
remaining byte-identical files, and records the removal provenance.

Different Markdown/source records are intentionally preserved even when they
happen to point to the same exact PDF artifact.
"""
from __future__ import annotations

import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
ANALYSES = ROOT / "analyses"
EVIDENCE = ROOT / "evidence"
ORIGINALS = ROOT / "originals"
REPORT = ROOT / "catalog" / "exact-pdf-duplicates.csv"
SOURCE_ID_RE = re.compile(r"^(SRC-[A-F0-9]{10})", re.IGNORECASE)
LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.IGNORECASE)
REPORT_FIELDS = ["PDF identity", "Kept path", "Removed path", "Reason"]


def pdf_object_identity(path: Path) -> str:
    """Return the Git LFS object ID or SHA-256 of the actual file bytes."""
    with path.open("rb") as handle:
        prefix = handle.read(512)
    lfs = LFS_OID_RE.search(prefix)
    if lfs:
        return lfs.group(1).decode("ascii").lower()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_id_for(path: Path, originals: Path) -> str | None:
    if path.parent != originals:
        return None
    match = SOURCE_ID_RE.match(path.stem.upper())
    return match.group(1).upper() if match else None


def keeper_rank(
    path: Path,
    *,
    originals: Path,
    sources: Path,
    analyses: Path,
    evidence: Path,
) -> tuple[int, int, int, int, str]:
    """Prefer the most established canonical linked copy deterministically."""
    source_id = source_id_for(path, originals)
    linked = int(source_id is not None)
    primary = int(source_id is not None and path.name.upper() == f"{source_id}.PDF")
    has_source = int(source_id is not None and (sources / f"{source_id}.md").exists())
    reviewed = 0
    if source_id is not None:
        reviewed += 2 * int((evidence / f"{source_id}.md").exists())
        reviewed += int((analyses / f"{source_id}.md").exists())
    # Higher tuple wins; final path term is inverted by sorting explicitly below.
    return linked, reviewed, primary, has_source, path.as_posix()


def load_report(report: Path) -> list[dict[str, str]]:
    if not report.exists():
        return []
    with report.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != REPORT_FIELDS:
            raise RuntimeError("Unexpected exact-PDF duplicate report schema")
        return [dict(row) for row in reader]


def write_report(report: Path, rows: list[dict[str, str]]) -> None:
    report.parent.mkdir(parents=True, exist_ok=True)
    unique: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows:
        key = (row["PDF identity"], row["Kept path"], row["Removed path"])
        unique[key] = row
    with report.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(
            unique[key]
            for key in sorted(unique, key=lambda item: (item[0], item[1], item[2]))
        )


def prune_exact_duplicates(
    *,
    originals: Path = ORIGINALS,
    sources: Path = SOURCES,
    analyses: Path = ANALYSES,
    evidence: Path = EVIDENCE,
    report: Path = REPORT,
) -> list[tuple[Path, Path, str]]:
    """Delete only exact redundant PDF files; never merge/delete source records."""
    if not originals.exists():
        return []

    groups: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(originals.rglob("*.pdf")):
        if path.is_file():
            groups[pdf_object_identity(path)].append(path)

    removed: list[tuple[Path, Path, str]] = []
    report_rows = load_report(report)
    for identity, paths in sorted(groups.items()):
        if len(paths) < 2:
            continue
        ranked = sorted(
            paths,
            key=lambda path: (
                -keeper_rank(
                    path,
                    originals=originals,
                    sources=sources,
                    analyses=analyses,
                    evidence=evidence,
                )[0],
                -keeper_rank(
                    path,
                    originals=originals,
                    sources=sources,
                    analyses=analyses,
                    evidence=evidence,
                )[1],
                -keeper_rank(
                    path,
                    originals=originals,
                    sources=sources,
                    analyses=analyses,
                    evidence=evidence,
                )[2],
                -keeper_rank(
                    path,
                    originals=originals,
                    sources=sources,
                    analyses=analyses,
                    evidence=evidence,
                )[3],
                path.as_posix(),
            ),
        )
        keeper = ranked[0]
        for duplicate in ranked[1:]:
            # Re-check immediately before deletion: only identical PDF content is removable.
            if pdf_object_identity(duplicate) != identity or pdf_object_identity(keeper) != identity:
                raise RuntimeError(f"PDF identity changed during duplicate pruning: {duplicate}")
            duplicate.unlink()
            removed.append((duplicate, keeper, identity))
            report_rows.append({
                "PDF identity": identity,
                "Kept path": keeper.relative_to(ROOT).as_posix() if ROOT in keeper.parents else keeper.as_posix(),
                "Removed path": duplicate.relative_to(ROOT).as_posix() if ROOT in duplicate.parents else duplicate.as_posix(),
                "Reason": "exact SHA-256 / Git LFS object duplicate; source record preserved",
            })

    if removed or report.exists():
        write_report(report, report_rows)
    return removed


def main() -> int:
    removed = prune_exact_duplicates()
    for duplicate, keeper, identity in removed:
        try:
            old = duplicate.relative_to(ROOT)
        except ValueError:
            old = duplicate
        try:
            kept = keeper.relative_to(ROOT)
        except ValueError:
            kept = keeper
        print(f"{old} → removed exact duplicate of {kept} ({identity})")
    print(f"Αφαιρέθηκαν {len(removed)} ακριβή διπλότυπα PDF χωρίς συγχώνευση source records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
