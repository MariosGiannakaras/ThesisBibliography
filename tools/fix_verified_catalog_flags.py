#!/usr/bin/env python3
"""Normalize stale intake flags for already verified selected sources.

This migration is deliberately narrow. It only changes the three August 2026
sources whose analyses and evidence already record completed human review.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "sources.csv"
SELECTION = ROOT / "catalog" / "thesis-selection.csv"
ANALYSES = ROOT / "analyses"
EVIDENCE = ROOT / "evidence"

TARGETS = {
    "SRC-70772C0629",
    "SRC-76B2247457",
    "SRC-9464421E55",
}
STALE_PRIORITY = "χρειάζεται διόρθωση"
READY_PRIORITY = "υψηλή"
STALE_NOTE = "Αυτόματη πλήρης μετατροπή PDF με OCR· τεχνικά πλήρης, προς ανθρώπινο έλεγχο"
READY_NOTE = (
    "Αυτόματη πλήρης μετατροπή PDF· ο ανθρώπινος έλεγχος του πρωτοτύπου, "
    "της ανάλυσης και του evidence ολοκληρώθηκε στις 2026-08-03"
)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def verified_text(path: Path, status_value: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    return (
        f"κατάσταση: {status_value}" in text
        and "ελεγχθέν-πρωτότυπο: ναι" in text
        and 'ημερομηνία-ελέγχου: "2026-08-03"' in text
    )


def validate_prerequisites(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    selection_path = root / "catalog" / "thesis-selection.csv"
    _, selection_rows = read_csv(selection_path)
    selected = {
        row.get("Κωδικός", "").strip(): row
        for row in selection_rows
        if row.get("Κωδικός", "").strip()
    }

    for source_id in sorted(TARGETS):
        row = selected.get(source_id)
        if not row:
            errors.append(f"{source_id}: missing from thesis selection")
            continue
        if row.get("Κατάσταση", "").strip() != "επαληθευμένη":
            errors.append(f"{source_id}: selection is not verified")
        if row.get("Εξαγωγή", "").strip() != "ναι":
            errors.append(f"{source_id}: selection is not exported")
        if not verified_text(root / "analyses" / f"{source_id}.md", "επαληθευμένη"):
            errors.append(f"{source_id}: verified analysis/manual-review marker missing")
        if not verified_text(root / "evidence" / f"{source_id}.md", "επαληθευμένο"):
            errors.append(f"{source_id}: verified evidence/manual-review marker missing")
    return errors


def normalize(root: Path = ROOT, apply: bool = False) -> list[str]:
    errors = validate_prerequisites(root)
    if errors:
        return errors

    catalog_path = root / "catalog" / "sources.csv"
    fields, rows = read_csv(catalog_path)
    by_id = {row.get("Κωδικός", "").strip(): row for row in rows}
    missing = TARGETS - set(by_id)
    if missing:
        return ["Missing catalog rows: " + ", ".join(sorted(missing))]

    changes = 0
    for source_id in sorted(TARGETS):
        row = by_id[source_id]
        priority = row.get("Προτεραιότητα", "").strip()
        if priority not in {STALE_PRIORITY, READY_PRIORITY}:
            errors.append(f"{source_id}: unexpected priority value: {priority!r}")
            continue

        notes = row.get("Σημειώσεις", "")
        if priority == STALE_PRIORITY:
            row["Προτεραιότητα"] = READY_PRIORITY
            changes += 1
        if STALE_NOTE in notes:
            row["Σημειώσεις"] = notes.replace(STALE_NOTE, READY_NOTE)
            changes += 1
        elif "προς ανθρώπινο έλεγχο" in notes:
            errors.append(f"{source_id}: unexpected stale manual-review wording")
        elif READY_NOTE not in notes:
            row["Σημειώσεις"] = f"{notes} | {READY_NOTE}".strip(" |")
            changes += 1

    if errors:
        return errors
    if not apply:
        if changes:
            return [f"{changes} stale verified catalog fields require normalization"]
        return []

    if changes:
        with catalog_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the verified normalization")
    args = parser.parse_args()
    errors = normalize(apply=args.apply)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Verified catalog flags are normalized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
