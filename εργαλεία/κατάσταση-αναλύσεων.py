#!/usr/bin/env python3
"""Δημιουργεί πλήρη ουρά και αναφορά προόδου ανάλυσης όλων των πηγών."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

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


def normalize(value: str | None) -> str:
    return (value or "").strip().casefold()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def analysis_status(source_id: str) -> str:
    path = ANALYSES / f"{source_id}.md"
    if not path.exists():
        return "προς ανάλυση"
    text = normalize(path.read_text(encoding="utf-8", errors="replace"))
    if "κατάσταση: επαληθευμένη" in text:
        return "επαληθευμένη"
    return "πρόχειρη"


def excerpt_status(source_id: str) -> str:
    path = EXCERPTS / f"{source_id}.md"
    if not path.exists():
        return "κανένα"
    text = normalize(path.read_text(encoding="utf-8", errors="replace"))
    if "κατάσταση: επαληθευμένο" in text:
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
                "Κατάσταση ανάλυσης": analysis_status(source_id),
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
    lines = [
        "# Κατάσταση αναλύσεων",
        "",
        f"- Σύνολο ενεργών πηγών: **{len(records)}**",
        f"- Προς ανάλυση: **{analysis_counts['προς ανάλυση']}**",
        f"- Πρόχειρες αναλύσεις: **{analysis_counts['πρόχειρη']}**",
        f"- Επαληθευμένες αναλύσεις: **{analysis_counts['επαληθευμένη']}**",
        f"- Επαληθευμένα αρχεία αποσπασμάτων: **{excerpt_counts['επαληθευμένο']}**",
        f"- Επιλεγμένες για εξαγωγή: **{export_count}**",
        "",
        "> Η ύπαρξη αρχείου πηγής ή PDF δεν σημαίνει ότι η πηγή έχει αναλυθεί. "
        "Η αναφορά αυτή είναι η πλήρης ουρά εργασίας.",
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
    print(f"Καταγράφηκαν {len(records)} πηγές στην ουρά ανάλυσης.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
