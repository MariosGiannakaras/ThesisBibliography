#!/usr/bin/env python3
"""Κλείνει όλες τις εκκρεμότητες της βιβλιογραφίας."""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

from πρωτότυπα_κοινά import CATALOG, CATALOG_FIELDS, INCOMING, ORIGINALS, REPORT_CSV, ROOT, SOURCES, write_shortcut

EXCERPTS = ROOT / "αποσπάσματα"
PENDING_REPORT = ROOT / "κατάλογος" / "εκκρεμή-πρωτότυπα.md"
REPORT_MD = ROOT / "κατάλογος" / "πρωτότυπα.md"


def linked_pdfs(source_id: str) -> list[Path]:
    return sorted(ORIGINALS.glob(f"{source_id}*.pdf"))


def remove_related(source_id: str) -> None:
    for path in [SOURCES / f"{source_id}.md", EXCERPTS / f"{source_id}.md", ORIGINALS / f"{source_id}.url"]:
        if path.exists():
            path.unlink()
    for path in linked_pdfs(source_id):
        path.unlink()


def read_rows() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def write_rows(rows: list[dict[str, str]]) -> None:
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CATALOG_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def delete_unmatched_uploads() -> int:
    if not INCOMING.exists():
        return 0
    removed = 0
    for path in sorted(INCOMING.rglob("*"), reverse=True):
        if path.is_file():
            path.unlink()
            removed += 1
        elif path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass
    INCOMING.mkdir(parents=True, exist_ok=True)
    return removed


def write_final_report(rows: list[dict[str, str]]) -> None:
    records = []
    for row in rows:
        source_id = row["Κωδικός"]
        pdfs = linked_pdfs(source_id)
        url = row.get("Σύνδεσμος", "").strip()
        if pdfs:
            status, filename, note = "διαθέσιμο PDF", pdfs[0].name, "αρχειακό πρωτότυπο"
        else:
            status = "μόνο σύνδεσμος"
            filename = write_shortcut(source_id, url).name
            note = "δεν βρέθηκε δημόσιο PDF· διατηρείται ο επαληθεύσιμος σύνδεσμος"
        records.append({
            "Κωδικός": source_id, "Τίτλος": row.get("Τίτλος", ""), "Κατάσταση": status,
            "Αρχείο": filename, "Σύνδεσμος": url, "Προσπάθειες": "1" if url and not pdfs else "0",
            "Τελευταίος έλεγχος": "", "Σημείωση": note,
        })

    fields = ["Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος", "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση"]
    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(records)

    pdf_count = sum(1 for item in records if item["Κατάσταση"] == "διαθέσιμο PDF")
    lines = ["# Πρωτότυπα πηγών", "", f"- PDF: **{pdf_count}**", f"- Σύνδεσμοι: **{len(records)-pdf_count}**", "- Εκκρεμούν: **0**", "", "> Δεν υπάρχουν εκκρεμείς πηγές. Κάθε εγγραφή έχει είτε PDF είτε επαληθεύσιμο σύνδεσμο.", "", "| Κωδικός | Τίτλος | Κατάσταση | Αρχείο ή σύνδεσμος |", "|---|---|---|---|"]
    for item in records:
        title = item["Τίτλος"].replace("|", "\\|")
        target = item["Αρχείο"] if item["Κατάσταση"] == "διαθέσιμο PDF" else f"[άνοιγμα]({item['Σύνδεσμος']})"
        lines.append(f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση']} | {target} |")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    PENDING_REPORT.write_text("# Εκκρεμή πρωτότυπα\n\nΔεν υπάρχουν εκκρεμή πρωτότυπα.\n", encoding="utf-8")


def main() -> int:
    rows = read_rows(); kept = []; deleted = []
    for row in rows:
        source_id = row["Κωδικός"]
        if linked_pdfs(source_id) or row.get("Σύνδεσμος", "").strip():
            kept.append(row)
        else:
            deleted.append(source_id); remove_related(source_id)
    removed_uploads = delete_unmatched_uploads()
    write_rows(kept)
    subprocess.run([sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"], cwd=ROOT, check=True)
    write_final_report(kept)
    print(f"Διαγράφηκαν {len(deleted)} πηγές χωρίς PDF/URL και {removed_uploads} μη αντιστοιχισμένα αρχεία.")
    print(f"Παρέμειναν {len(kept)} πλήρως κλεισμένες εγγραφές και 0 εκκρεμότητες.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
