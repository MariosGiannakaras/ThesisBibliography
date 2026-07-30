#!/usr/bin/env python3
"""Κεντρική εντολή συγχρονισμού πρωτοτύπων πηγών."""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from κοινά_πηγών import SOURCE_ID_RE, source_text
from πρωτότυπα_αρχεία import (
    import_uploaded,
    match_uploaded,
    write_pending_report,
    write_report,
)
from πρωτότυπα_κοινά import (
    ORIGINALS,
    ROOT,
    SOURCES,
    is_document_candidate,
    is_url_only,
    read_catalog,
    read_previous,
    write_catalog,
    write_shortcut,
)
from πρωτότυπα_λήψεις import candidate_urls, download_pdf, looks_like_pdf

__all__ = [
    "candidate_urls",
    "download_pdf",
    "looks_like_pdf",
    "match_uploaded",
    "main",
]


def requested_ids(path: Path | None) -> set[str] | None:
    if not path or not path.exists():
        return None
    result = set(SOURCE_ID_RE.findall(path.read_text(encoding="utf-8", errors="replace")))
    return result or None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--λήψη", "--download", action="store_true")
    parser.add_argument("--όριο", "--limit", type=int, default=30)
    parser.add_argument("--κωδικοί-αρχείο", "--ids-file", type=Path)
    parser.add_argument("--επανάληψη", "--retry", action="store_true")
    parser.add_argument("--χωρίς-νέες-εγγραφές", "--no-create-missing", action="store_true")
    args = parser.parse_args()

    rows = read_catalog()
    previous = read_previous()
    notes, pending, catalog_changed = import_uploaded(
        rows,
        create_missing=not args.χωρίς_νέες_εγγραφές,
    )
    if catalog_changed:
        write_catalog(rows)
        subprocess.run(
            [sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"],
            cwd=ROOT,
            check=True,
        )

    wanted = requested_ids(args.κωδικοί_αρχείο)
    results = {}

    for row in rows:
        source_id = row["Κωδικός"]
        shortcut = ORIGINALS / f"{source_id}.url"
        if (ORIGINALS / f"{source_id}.pdf").exists() or is_document_candidate(row):
            if shortcut.exists():
                shortcut.unlink()
        elif is_url_only(row) and row.get("Σύνδεσμος"):
            write_shortcut(source_id, row["Σύνδεσμος"])

    if args.λήψη:
        priorities = {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}
        candidates = []
        for row in rows:
            source_id = row["Κωδικός"]
            if wanted is not None and source_id not in wanted:
                continue
            if (
                (ORIGINALS / f"{source_id}.pdf").exists()
                or is_url_only(row)
                or not row.get("Σύνδεσμος")
            ):
                continue
            attempts = int(previous.get(source_id, {}).get("Προσπάθειες", "0") or 0)
            if attempts >= 3 and not args.επανάληψη:
                continue
            candidates.append(
                (
                    priorities.get(row.get("Προτεραιότητα", ""), 9),
                    attempts,
                    row["Τίτλος"].casefold(),
                    row,
                )
            )
        candidates.sort(key=lambda item: item[:3])
        for _, _, _, row in candidates[: max(0, args.όριο)]:
            source_id = row["Κωδικός"]
            results[source_id] = download_pdf(
                source_id,
                row,
                source_text(SOURCES, source_id),
            )
            print(f"{source_id}: {results[source_id].status}")
            time.sleep(0.15)

    write_pending_report(pending)
    write_report(rows, previous, results, notes)
    print(
        f"Ελέγχθηκαν {len(rows)} πηγές, έγιναν {len(results)} προσπάθειες λήψης "
        f"και παρέμειναν {len(pending)} μη ασφαλείς αντιστοιχίσεις."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
