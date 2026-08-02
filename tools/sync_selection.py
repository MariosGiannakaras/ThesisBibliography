#!/usr/bin/env python3
"""Συγχρονίζει συντηρητικά το curated registry από τις canonical αναλύσεις.

Το υπάρχον χειροκίνητο metadata (κεφάλαια/θέματα/σημειώσεις) διατηρείται. Νέες
ή μεταγενέστερα διορθωμένες αποφάσεις ενημερώνουν μόνο Ρόλο/Κατάσταση/Εξαγωγή.
"""
from __future__ import annotations

import csv
from pathlib import Path

from decision_status import SELECTED_ROLES, excerpt_is_verified, infer_decision, infer_role

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "sources.csv"
SELECTION = ROOT / "catalog" / "thesis-selection.csv"
ANALYSES = ROOT / "analyses"
EXCERPTS = ROOT / "evidence"

FIELDS = ["Κωδικός", "Ρόλος", "Κατάσταση", "Κεφάλαια", "Θέματα", "Εξαγωγή", "Σημείωση"]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def normalized_row(row: dict[str, str]) -> dict[str, str]:
    return {field: (row.get(field, "") or "").strip() for field in FIELDS}


def main() -> int:
    catalog_rows = read_csv(CATALOG)
    catalog = {row.get("Κωδικός", "").strip(): row for row in catalog_rows if row.get("Κωδικός", "").strip()}
    existing_rows = [normalized_row(row) for row in read_csv(SELECTION)]
    existing = {row["Κωδικός"]: row for row in existing_rows if row["Κωδικός"]}

    errors: list[str] = []
    final_rows: dict[str, dict[str, str]] = {}
    selected = rejected = theory_only = drafts = 0

    for source_id, source in catalog.items():
        previous = existing.get(source_id, {field: "" for field in FIELDS})
        previous_role = (previous.get("Ρόλος", "") or "").strip().casefold()
        previous_status = (previous.get("Κατάσταση", "") or "").strip().casefold()
        analysis_path = ANALYSES / f"{source_id}.md"
        if not analysis_path.exists():
            if previous.get("Κωδικός"):
                row = dict(previous)
                row["Εξαγωγή"] = "όχι"
                if row.get("Κατάσταση", "").casefold() == "επαληθευμένη":
                    row["Κατάσταση"] = "προς ανάλυση"
                final_rows[source_id] = row
            continue

        text = analysis_path.read_text(encoding="utf-8", errors="replace")
        decision = infer_decision(text)
        inferred_role = infer_role(text)

        # Legacy canonical fallback: older analyses may not use a uniform Decision
        # heading, while the curated registry already records an explicit final role.
        # A parsed canonical decision always has priority over this fallback.
        if decision == "draft" and previous_role == "απόρριψη":
            decision = "rejected"
        if decision == "draft" and previous_role in SELECTED_ROLES and previous_status == "επαληθευμένη":
            decision = "selected"

        row = dict(previous)
        row["Κωδικός"] = source_id

        if decision == "rejected":
            rejected += 1
            row["Ρόλος"] = "απόρριψη"
            row["Κατάσταση"] = "απορρίφθηκε"
            row["Εξαγωγή"] = "όχι"
        elif decision == "theory-only":
            theory_only += 1
            row["Ρόλος"] = "θεωρητικό υλικό"
            row["Κατάσταση"] = "ελεγμένο-μη-παραπομπή"
            row["Εξαγωγή"] = "όχι"
        elif decision == "selected":
            selected += 1
            role = inferred_role or row.get("Ρόλος", "")
            if role not in SELECTED_ROLES:
                errors.append(f"{source_id}: selected analysis χωρίς σαφή ρόλο")
                row["Ρόλος"] = role
                row["Κατάσταση"] = "πρόχειρη"
                row["Εξαγωγή"] = "όχι"
            else:
                row["Ρόλος"] = role
                verified = excerpt_is_verified(EXCERPTS / f"{source_id}.md")
                row["Κατάσταση"] = "επαληθευμένη" if verified else "πρόχειρη"
                row["Εξαγωγή"] = "ναι" if verified else "όχι"
                if not verified:
                    errors.append(f"{source_id}: selected analysis χωρίς verified citation-ready excerpts")
        else:
            drafts += 1
            if not row.get("Ρόλος"):
                row["Ρόλος"] = inferred_role
            row["Κατάσταση"] = "πρόχειρη"
            row["Εξαγωγή"] = "όχι"

        if not row.get("Θέματα"):
            row["Θέματα"] = (source.get("Θέματα", "") or "").strip()
        if not row.get("Σημείωση"):
            row["Σημείωση"] = "Συγχρονισμός από canonical analysis."
        final_rows[source_id] = row

    ordered: list[dict[str, str]] = []
    seen: set[str] = set()
    for old in existing_rows:
        source_id = old.get("Κωδικός", "")
        if source_id in final_rows and source_id not in seen:
            ordered.append(final_rows[source_id])
            seen.add(source_id)
    for source in catalog_rows:
        source_id = (source.get("Κωδικός", "") or "").strip()
        if source_id in final_rows and source_id not in seen:
            ordered.append(final_rows[source_id])
            seen.add(source_id)

    with SELECTION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ordered)

    print(
        f"Συγχρονισμός επιλογής: {len(ordered)} rows, "
        f"selected={selected}, rejected={rejected}, theory_only={theory_only}, drafts={drafts}."
    )
    if errors:
        print("Προειδοποιήσεις συγχρονισμού:")
        for error in errors:
            print(f"- {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
