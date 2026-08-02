#!/usr/bin/env python3
"""Δημιουργεί authoritative ουρά/αναφορά από catalog + canonical analyses."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from κατάσταση_απόφασης import SELECTED_ROLES, excerpt_is_verified, infer_decision, normalize

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
SELECTION = ROOT / "κατάλογος" / "επιλογή-διπλωματικής.csv"
ANALYSES = ROOT / "αναλύσεις"
EXCERPTS = ROOT / "αποσπάσματα"
REPORT_CSV = ROOT / "κατάλογος" / "κατάσταση-αναλύσεων.csv"
REPORT_MD = ROOT / "κατάλογος" / "κατάσταση-αναλύσεων.md"

FIELDS = [
    "Κωδικός",
    "Τίτλος",
    "Προτεραιότητα",
    "Κατάσταση πηγής",
    "Κατάσταση ανάλυσης",
    "Κατάσταση αποσπασμάτων",
    "Ρόλος",
    "Εξαγωγή",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def analysis_status(source_id: str, chosen: dict[str, str]) -> str:
    path = ANALYSES / f"{source_id}.md"
    if not path.exists():
        return "προς ανάλυση"
    text = path.read_text(encoding="utf-8", errors="replace")
    decision = infer_decision(text)
    role = normalize(chosen.get("Ρόλος"))
    registry_status = normalize(chosen.get("Κατάσταση"))

    if decision == "rejected":
        return "απορρίφθηκε"
    if decision == "theory-only":
        return "θεωρητικό υλικό"
    if decision == "selected" and excerpt_is_verified(EXCERPTS / f"{source_id}.md"):
        return "επαληθευμένη"

    # Legacy fallback μετά τον conservative registry sync.
    if role == "απόρριψη" and registry_status == "απορρίφθηκε":
        return "απορρίφθηκε"
    if role == "θεωρητικό υλικό" and registry_status == "ελεγμένο-μη-παραπομπή":
        return "θεωρητικό υλικό"
    if role in SELECTED_ROLES and registry_status == "επαληθευμένη" and excerpt_is_verified(EXCERPTS / f"{source_id}.md"):
        return "επαληθευμένη"
    return "πρόχειρη"


def excerpt_status(source_id: str) -> str:
    path = EXCERPTS / f"{source_id}.md"
    if not path.exists():
        return "κανένα"
    if excerpt_is_verified(path):
        return "επαληθευμένο"
    return "πρόχειρο"


def main() -> int:
    catalog_rows = read_rows(CATALOG)
    selection = {row.get("Κωδικός", "").strip(): row for row in read_rows(SELECTION)}
    records: list[dict[str, str]] = []

    for source in sorted(catalog_rows, key=lambda row: row.get("Τίτλος", "").casefold()):
        source_id = source.get("Κωδικός", "").strip()
        chosen = selection.get(source_id, {})
        records.append(
            {
                "Κωδικός": source_id,
                "Τίτλος": source.get("Τίτλος", ""),
                "Προτεραιότητα": source.get("Προτεραιότητα", ""),
                "Κατάσταση πηγής": source.get("Κατάσταση", ""),
                "Κατάσταση ανάλυσης": analysis_status(source_id, chosen),
                "Κατάσταση αποσπασμάτων": excerpt_status(source_id),
                "Ρόλος": chosen.get("Ρόλος", ""),
                "Εξαγωγή": chosen.get("Εξαγωγή", ""),
            }
        )

    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    analysis_counts = Counter(row["Κατάσταση ανάλυσης"] for row in records)
    excerpt_counts = Counter(row["Κατάσταση αποσπασμάτων"] for row in records)
    export_count = sum(normalize(row["Εξαγωγή"]) in {"ναι", "yes", "true", "1"} for row in records)
    decided_count = (
        analysis_counts["επαληθευμένη"]
        + analysis_counts["απορρίφθηκε"]
        + analysis_counts["θεωρητικό υλικό"]
    )
    unfinished_count = analysis_counts["προς ανάλυση"] + analysis_counts["πρόχειρη"]

    lines = [
        "# Κατάσταση αναλύσεων",
        "",
        f"- Σύνολο ενεργών πηγών: **{len(records)}**",
        f"- Οριστικές αποφάσεις: **{decided_count}**",
        f"  - Επιλεγμένες/επαληθευμένες: **{analysis_counts['επαληθευμένη']}**",
        f"  - Απορριφθείσες: **{analysis_counts['απορρίφθηκε']}**",
        f"  - Ελεγμένες ως θεωρητικό υλικό χωρίς citation export: **{analysis_counts['θεωρητικό υλικό']}**",
        f"- Εκκρεμείς συνολικά: **{unfinished_count}**",
        f"  - Χωρίς ανάλυση: **{analysis_counts['προς ανάλυση']}**",
        f"  - Πρόχειρες/μη citation-ready: **{analysis_counts['πρόχειρη']}**",
        f"- Επαληθευμένα αρχεία αποσπασμάτων: **{excerpt_counts['επαληθευμένο']}**",
        f"- Επιλεγμένες για εξαγωγή: **{export_count}**",
        "",
        "> Η αναφορά παράγεται από το τρέχον `κατάλογος/πηγές.csv`, τα canonical `αναλύσεις/` "
        "και τα verified `αποσπάσματα/`. Παλιές generated rows δεν χρησιμοποιούνται ως πηγή αλήθειας.",
        "",
        "| Κωδικός | Τίτλος | Ανάλυση | Αποσπάσματα | Ρόλος | Εξαγωγή |",
        "|---|---|---|---|---|---|",
    ]
    for row in records:
        title = row["Τίτλος"].replace("|", "\\|")
        lines.append(
            f"| `{row['Κωδικός']}` | {title} | {row['Κατάσταση ανάλυσης']} | "
            f"{row['Κατάσταση αποσπασμάτων']} | {row['Ρόλος']} | {row['Εξαγωγή']} |"
        )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Καταγράφηκαν {len(records)} πηγές: decisions={decided_count}, "
        f"unfinished={unfinished_count}, export={export_count}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
