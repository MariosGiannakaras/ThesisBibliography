#!/usr/bin/env python3
"""Normalize stale intake flags/metadata for explicitly verified sources.

This migration is deliberately narrow. It only changes enumerated sources whose
analyses and evidence already record completed human review. It does not infer
bibliographic metadata for arbitrary catalog rows.
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
SOURCES = ROOT / "sources"

LEGACY_TARGETS = {
    "SRC-70772C0629",
    "SRC-76B2247457",
    "SRC-9464421E55",
}
# Backward-compatible public name used by the existing migration tests.
TARGETS = LEGACY_TARGETS

STALE_PRIORITY = "χρειάζεται διόρθωση"
READY_PRIORITY = "υψηλή"
STALE_NOTE = "Αυτόματη πλήρης μετατροπή PDF με OCR· τεχνικά πλήρης, προς ανθρώπινο έλεγχο"
READY_NOTE = (
    "Αυτόματη πλήρης μετατροπή PDF· ο ανθρώπινος έλεγχος του πρωτοτύπου, "
    "της ανάλυσης και του evidence ολοκληρώθηκε στις 2026-08-03"
)

# These two records were intentionally introduced through URL-first intake. Their
# full scientific analyses/evidence now verify the official publication identities,
# so the catalog must no longer retain the coarse intake guesses (blank authors,
# GridWorld topic, or webpage type).
T716_METADATA_FIXES: dict[str, dict[str, str]] = {
    "SRC-0FD9BE81AC": {
        "Τίτλος": "Continual Reinforcement Learning by Planning with Online World Models",
        "Συγγραφείς": "Zichen Liu; Guoji Fu; Chao Du; Wee Sun Lee; Min Lin",
        "Έτος": "2025",
        "Σύνδεσμος": "https://proceedings.mlr.press/v267/liu25p.html",
        "Τύπος": "ακαδημαϊκή εργασία",
        "Θέματα": "μη στασιμότητα; ενισχυτική μάθηση με μοντέλο; συνεχής προσαρμογή",
        "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
        "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
        "Προτεραιότητα": "υψηλή",
    },
    "SRC-327CD7B903": {
        "Τίτλος": "Quantitative Resilience Modeling for Autonomous Cyber Defense",
        "Συγγραφείς": "Xavier Cadet; Simona Boboila; Edward Koh; Peter Chin; Alina Oprea",
        "Έτος": "2025",
        "Σύνδεσμος": "https://rlj.cs.umass.edu/2025/papers/Paper99.html",
        "Τύπος": "ακαδημαϊκή εργασία",
        "Θέματα": "ανθεκτικότητα και ανάκαμψη; στατιστική αξιολόγηση",
        "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
        "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
        "Προτεραιότητα": "υψηλή",
    },
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def verified_text(path: Path, status_value: str, review_date: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    return (
        f"κατάσταση: {status_value}" in text
        and "ελεγχθέν-πρωτότυπο: ναι" in text
        and f'ημερομηνία-ελέγχου: "{review_date}"' in text
    )


def active_t716_targets(root: Path) -> tuple[set[str], list[str]]:
    """Return active T-716 rows while preserving isolated legacy-test fixtures.

    Repository state must contain either both T-716 rows or neither. The latter is
    permitted only so the pre-existing unit tests can exercise the older migration
    in a minimal synthetic catalog without fabricating unrelated T-716 files.
    """
    _, catalog_rows = read_csv(root / "catalog" / "sources.csv")
    catalog_ids = {row.get("Κωδικός", "").strip() for row in catalog_rows}
    expected = set(T716_METADATA_FIXES)
    present = expected & catalog_ids
    if present and present != expected:
        missing = ", ".join(sorted(expected - present))
        return present, [f"Incomplete T-716 catalog migration set; missing: {missing}"]
    return present, []


def validate_prerequisites(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    selection_path = root / "catalog" / "thesis-selection.csv"
    _, selection_rows = read_csv(selection_path)
    selected = {
        row.get("Κωδικός", "").strip(): row
        for row in selection_rows
        if row.get("Κωδικός", "").strip()
    }

    # Preserve the original narrow migration contract for the August 2026 sources.
    for source_id in sorted(LEGACY_TARGETS):
        row = selected.get(source_id)
        if not row:
            errors.append(f"{source_id}: missing from thesis selection")
            continue
        if row.get("Κατάσταση", "").strip() != "επαληθευμένη":
            errors.append(f"{source_id}: selection is not verified")
        if row.get("Εξαγωγή", "").strip() != "ναι":
            errors.append(f"{source_id}: selection is not exported")
        if not verified_text(root / "analyses" / f"{source_id}.md", "επαληθευμένη", "2026-08-03"):
            errors.append(f"{source_id}: verified analysis/manual-review marker missing")
        if not verified_text(root / "evidence" / f"{source_id}.md", "επαληθευμένο", "2026-08-03"):
            errors.append(f"{source_id}: verified evidence/manual-review marker missing")

    t716_targets, target_errors = active_t716_targets(root)
    errors.extend(target_errors)
    if target_errors:
        return errors

    # Package normalization runs before sync_selection.py. Therefore the T-716
    # records are gated directly by their checked analysis/evidence rather than by
    # a selection row that may not yet have been generated.
    for source_id in sorted(t716_targets):
        if not (root / "sources" / f"{source_id}.md").exists():
            errors.append(f"{source_id}: canonical source Markdown missing")
        if not verified_text(root / "analyses" / f"{source_id}.md", "επαληθευμένη", "2026-09-05"):
            errors.append(f"{source_id}: verified T-716 analysis/manual-review marker missing")
        if not verified_text(root / "evidence" / f"{source_id}.md", "επαληθευμένο", "2026-09-05"):
            errors.append(f"{source_id}: verified T-716 evidence/manual-review marker missing")

    return errors


def normalize(root: Path = ROOT, apply: bool = False) -> list[str]:
    errors = validate_prerequisites(root)
    if errors:
        return errors

    catalog_path = root / "catalog" / "sources.csv"
    fields, rows = read_csv(catalog_path)
    by_id = {row.get("Κωδικός", "").strip(): row for row in rows}
    missing_legacy = LEGACY_TARGETS - set(by_id)
    if missing_legacy:
        return ["Missing catalog rows: " + ", ".join(sorted(missing_legacy))]

    t716_targets, target_errors = active_t716_targets(root)
    if target_errors:
        return target_errors

    legacy_changes = 0
    migration_changes = 0
    for source_id in sorted(LEGACY_TARGETS):
        row = by_id[source_id]
        priority = row.get("Προτεραιότητα", "").strip()
        if priority not in {STALE_PRIORITY, READY_PRIORITY}:
            errors.append(f"{source_id}: unexpected priority value: {priority!r}")
            continue

        notes = row.get("Σημειώσεις", "")
        if priority == STALE_PRIORITY:
            row["Προτεραιότητα"] = READY_PRIORITY
            legacy_changes += 1
        if STALE_NOTE in notes:
            row["Σημειώσεις"] = notes.replace(STALE_NOTE, READY_NOTE)
            legacy_changes += 1
        elif "προς ανθρώπινο έλεγχο" in notes:
            errors.append(f"{source_id}: unexpected stale manual-review wording")
        elif READY_NOTE not in notes:
            row["Σημειώσεις"] = f"{notes} | {READY_NOTE}".strip(" |")
            legacy_changes += 1

    for source_id in sorted(t716_targets):
        row = by_id[source_id]
        expected = T716_METADATA_FIXES[source_id]
        for field, value in expected.items():
            if field not in fields:
                errors.append(f"{source_id}: catalog field missing: {field}")
                continue
            if row.get(field, "") != value:
                row[field] = value
                migration_changes += 1

    if errors:
        return errors

    # Historical completed-review flags are required to be converged in every
    # checkout. The new T-716 metadata repair is intentionally package-applied:
    # dry-run validation verifies its manual-review prerequisites, while the
    # governed thesis-package workflow invokes --apply before regeneration.
    if not apply:
        if legacy_changes:
            return [f"{legacy_changes} stale verified catalog fields require normalization"]
        return []

    total_changes = legacy_changes + migration_changes
    if total_changes:
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
    print("Verified catalog flags and metadata are normalized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
