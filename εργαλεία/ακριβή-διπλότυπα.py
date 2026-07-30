#!/usr/bin/env python3
"""Συγχωνεύει πηγές μόνο όταν το πρωτεύον PDF είναι ακριβώς το ίδιο.

Λειτουργεί τόσο σε κανονικά PDF όσο και σε Git LFS pointer files. Δεν
χρησιμοποιεί τίτλο ή ομοιότητα ως απόδειξη ταυτότητας.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "εργαλεία"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]
SOURCE_PDF_RE = re.compile(r"SRC-[A-F0-9]{10}\.pdf", re.IGNORECASE)
LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.IGNORECASE)


def load_cleanup_module():
    path = TOOLS / "καθαρισμός-συνδέσεων.py"
    spec = importlib.util.spec_from_file_location("cleanup_links_for_pdf_duplicates", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("δεν φορτώθηκε το εργαλείο καθαρισμού συνδέσεων")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def pdf_object_identity(path: Path) -> str:
    """Επιστρέφει το LFS object ID ή SHA-256 πραγματικού αρχείου."""
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


def load_rows() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def save_rows(rows: list[dict[str, str]]) -> None:
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def main() -> int:
    cleanup = load_cleanup_module()
    rows = load_rows()
    by_id = {row["Κωδικός"]: row for row in rows}
    texts = {
        source_id: cleanup.source_text(SOURCES, source_id)
        for source_id in by_id
    }

    groups: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(ORIGINALS.glob("SRC-*.pdf")):
        if SOURCE_PDF_RE.fullmatch(path.name):
            groups[pdf_object_identity(path)].append(path)

    merged: list[tuple[str, str, str]] = []
    changes: list[str] = []
    for object_id, paths in groups.items():
        source_ids = [path.stem.upper() for path in paths if path.stem.upper() in by_id]
        current = [by_id[source_id] for source_id in source_ids if source_id in by_id]
        if len(current) < 2:
            continue
        ordered = sorted(
            current,
            key=lambda row: cleanup.source_score(row, texts.get(row["Κωδικός"], "")),
            reverse=True,
        )
        primary = ordered[0]
        for duplicate in ordered[1:]:
            if duplicate["Κωδικός"] not in {row["Κωδικός"] for row in rows}:
                continue
            rows = cleanup.merge_one(
                rows,
                texts,
                primary,
                duplicate,
                f"pdf-sha256:{object_id}",
                changes,
                merged,
            )
            by_id.pop(duplicate["Κωδικός"], None)

    if merged:
        save_rows(rows)
        subprocess.run(
            [sys.executable, str(TOOLS / "εισαγωγή.py"), "--catalog-only"],
            cwd=ROOT,
            check=True,
        )
        cleanup.append_report(merged, [], changes)

    for old, new, key in merged:
        print(f"{old} → {new} ({key})")
    print(f"Συγχωνεύθηκαν {len(merged)} ομάδες ακριβώς ίδιων PDF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
