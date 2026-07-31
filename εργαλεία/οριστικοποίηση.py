#!/usr/bin/env python3
"""Κλείνει τις εκκρεμότητες χωρίς να διαγράφει χρήσιμο περιεχόμενο ή πρωτότυπα."""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

from πρωτότυπα_αρχεία import archive_unmatched
from πρωτότυπα_κοινά import (
    CATALOG,
    CATALOG_FIELDS,
    INCOMING,
    ORIGINALS,
    REPORT_CSV,
    ROOT,
    SOURCES,
    UNMATCHED,
    pdf_identity,
    write_shortcut,
)

ANALYSES = ROOT / "αναλύσεις"
EXCERPTS = ROOT / "αποσπάσματα"
PENDING_REPORT = ROOT / "κατάλογος" / "εκκρεμή-πρωτότυπα.md"
REPORT_MD = ROOT / "κατάλογος" / "πρωτότυπα.md"
PRESERVED_INCOMING_FILES = {"README.md", ".gitkeep"}


def linked_pdfs(source_id: str) -> list[Path]:
    return sorted(ORIGINALS.glob(f"{source_id}*.pdf"))


def meaningful_text(path: Path, minimum_words: int = 40) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[`#>*_\-|:\[\]()]+", " ", text)
    words = re.findall(r"[A-Za-zΑ-Ωα-ωΆ-ώ0-9]{2,}", text)
    boilerplate = {
        "source", "πηγή", "τίτλος", "συγγραφείς", "έτος", "σύνδεσμος",
        "πρωτότυπο", "χρειάζεται", "έλεγχο", "μεταδεδομένα",
    }
    useful = [word for word in words if word.casefold() not in boilerplate]
    return len(useful) >= minimum_words


def has_useful_content(source_id: str) -> bool:
    return (
        meaningful_text(SOURCES / f"{source_id}.md", 40)
        or meaningful_text(ANALYSES / f"{source_id}.md", 150)
        or meaningful_text(EXCERPTS / f"{source_id}.md", 120)
    )


def remove_related(source_id: str) -> None:
    for path in [
        SOURCES / f"{source_id}.md",
        ANALYSES / f"{source_id}.md",
        EXCERPTS / f"{source_id}.md",
        ORIGINALS / f"{source_id}.url",
    ]:
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


def preserve_unmatched_uploads() -> tuple[int, int]:
    """Μεταφέρει κάθε εισερχόμενο PDF στη μόνιμη αρχειοθήκη· διαγράφει μόνο ακριβή αντίγραφα."""
    if not INCOMING.exists():
        return 0, 0
    archived = 0
    exact_duplicates = 0
    for path in sorted(INCOMING.rglob("*.pdf")):
        if not path.is_file():
            continue
        stored, _ = archive_unmatched(path, originals=ORIGINALS, unmatched=UNMATCHED)
        if stored:
            archived += 1
        else:
            exact_duplicates += 1
    for path in sorted(INCOMING.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass
    INCOMING.mkdir(parents=True, exist_ok=True)
    return archived, exact_duplicates


def write_final_report(rows: list[dict[str, str]]) -> None:
    records = []
    for row in rows:
        source_id = row["Κωδικός"]
        pdfs = linked_pdfs(source_id)
        url = row.get("Σύνδεσμος", "").strip()
        useful = has_useful_content(source_id)
        if pdfs:
            status, filename, note = "διαθέσιμο PDF", pdfs[0].name, "αρχειακό πρωτότυπο"
        elif url:
            status = "μόνο σύνδεσμος"
            filename = write_shortcut(source_id, url).name
            note = "δεν βρέθηκε δημόσιο PDF· διατηρείται ο σύνδεσμος"
        elif useful:
            status = "διαθέσιμο περιεχόμενο"
            filename = f"{source_id}.md"
            note = "διατηρείται επειδή περιέχει χρήσιμες πληροφορίες, ανάλυση ή αποσπάσματα"
        else:
            continue
        records.append({
            "Κωδικός": source_id,
            "Τίτλος": row.get("Τίτλος", ""),
            "Κατάσταση": status,
            "Αρχείο": filename,
            "Σύνδεσμος": url,
            "Προσπάθειες": "1" if url and not pdfs else "0",
            "Τελευταίος έλεγχος": "",
            "Σημείωση": note,
        })

    fields = ["Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος", "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση"]
    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    unmatched = sorted(path for path in UNMATCHED.rglob("*.pdf") if path.is_file())
    pdf_count = sum(item["Κατάσταση"] == "διαθέσιμο PDF" for item in records)
    link_count = sum(item["Κατάσταση"] == "μόνο σύνδεσμος" for item in records)
    content_count = sum(item["Κατάσταση"] == "διαθέσιμο περιεχόμενο" for item in records)
    lines = [
        "# Πρωτότυπα πηγών", "",
        f"- PDF: **{pdf_count}**",
        f"- Μη ταυτοποιημένα PDF που διατηρούνται: **{len(unmatched)}**",
        f"- Σύνδεσμοι: **{link_count}**",
        f"- Πηγές μόνο με χρήσιμο περιεχόμενο: **{content_count}**",
        f"- Εκκρεμούν για ταυτοποίηση: **{len(unmatched)}**", "",
        "> Κάθε εγγραφή έχει PDF, σύνδεσμο ή ουσιαστικό Markdown/ανάλυση/απόσπασμα. Κάθε μη ταυτοποιημένο PDF διατηρείται μόνιμα· διαγράφεται μόνο ακριβές αντίγραφο.", "",
        "| Κωδικός | Τίτλος | Κατάσταση | Αρχείο ή σύνδεσμος |",
        "|---|---|---|---|",
    ]
    for item in records:
        title = item["Τίτλος"].replace("|", "\\|")
        if item["Κατάσταση"] == "μόνο σύνδεσμος":
            target = f"[άνοιγμα]({item['Σύνδεσμος']})"
        else:
            target = item["Αρχείο"]
        lines.append(f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση']} | {target} |")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    pending_lines = [
        "# Εκκρεμή πρωτότυπα", "",
        "Τα παρακάτω PDF διατηρούνται μόνιμα έως ότου αντιστοιχιστούν με ασφάλεια ή μετατραπούν σε πηγή Markdown.", "",
    ]
    if not unmatched:
        pending_lines.append("Δεν υπάρχουν μη ταυτοποιημένα πρωτότυπα.")
    else:
        pending_lines.extend([
            "| Αρχείο | SHA-256 / LFS object ID |",
            "|---|---|",
        ])
        for path in unmatched:
            relative = path.relative_to(ORIGINALS).as_posix().replace("|", "\\|")
            pending_lines.append(f"| `{relative}` | `{pdf_identity(path)}` |")
    PENDING_REPORT.write_text("\n".join(pending_lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = read_rows()
    kept: list[dict[str, str]] = []
    deleted: list[str] = []
    content_only = 0
    for row in rows:
        source_id = row["Κωδικός"]
        has_pdf = bool(linked_pdfs(source_id))
        has_url = bool(row.get("Σύνδεσμος", "").strip())
        useful = has_useful_content(source_id)
        if has_pdf or has_url or useful:
            kept.append(row)
            if useful and not has_pdf and not has_url:
                content_only += 1
        else:
            deleted.append(source_id)
            remove_related(source_id)

    archived_uploads, exact_duplicates = preserve_unmatched_uploads()
    write_rows(kept)
    subprocess.run(
        [sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"],
        cwd=ROOT,
        check=True,
    )
    write_final_report(kept)
    print(f"Διαγράφηκαν {len(deleted)} πραγματικά κενές πηγές.")
    print(
        f"Αρχειοθετήθηκαν {archived_uploads} μη ταυτοποιημένα PDF και "
        f"αφαιρέθηκαν {exact_duplicates} ακριβή αντίγραφα."
    )
    print(f"Διατηρήθηκαν {content_only} πηγές χωρίς PDF/URL επειδή έχουν χρήσιμο περιεχόμενο.")
    print(f"Παρέμειναν {len(kept)} κλεισμένες εγγραφές και {len(list(UNMATCHED.rglob('*.pdf')))} εκκρεμή πρωτότυπα.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
