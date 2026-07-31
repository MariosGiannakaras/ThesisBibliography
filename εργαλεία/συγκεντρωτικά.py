#!/usr/bin/env python3
"""Παράγει τις συγκεντρωτικές προβολές του bibliography repository.

Παράγωγα αρχεία:
- ΑΡΧΕΙΟ_ΠΗΓΩΝ.md
- ΧΡΗΣΙΜΑ_ΑΠΟΣΠΑΣΜΑΤΑ.md

Πηγές αλήθειας:
- κατάλογος/πηγές.csv
- πηγές/SRC-*.md
- αποσπάσματα/SRC-*.md
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable, Mapping, Sequence

REQUIRED_COLUMNS = (
    "Κωδικός",
    "Τίτλος",
    "Συγγραφείς",
    "Έτος",
    "Σύνδεσμος",
    "Τύπος",
    "Θέματα",
    "Κατάσταση",
    "Επιβεβαίωση",
    "Προτεραιότητα",
    "Σημειώσεις",
)

ARCHIVE_FILENAME = "ΑΡΧΕΙΟ_ΠΗΓΩΝ.md"
EXCERPTS_FILENAME = "ΧΡΗΣΙΜΑ_ΑΠΟΣΠΑΣΜΑΤΑ.md"
VERIFIED_STATUS = "επαληθευμένο"
SOURCE_ID_RE = re.compile(r"SRC-[0-9A-F]{10}")


def normalize(value: object) -> str:
    return " ".join(str(value or "").split())


def markdown_escape(value: object) -> str:
    text = normalize(value)
    return text.replace("\\", "\\\\").replace("|", "\\|") or "—"


def safe_link(url: object, label: str = "άνοιγμα") -> str:
    value = normalize(url)
    if not re.match(r"^https?://", value, flags=re.IGNORECASE):
        return "—"
    return f"[{markdown_escape(label)}]({value})"


def read_catalog(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"Δεν βρέθηκε ο κατάλογος: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        missing = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
        if missing:
            raise ValueError("Λείπουν πεδία καταλόγου: " + ", ".join(missing))

        rows: list[dict[str, str]] = []
        seen: set[str] = set()
        for line_number, raw in enumerate(reader, start=2):
            row = {name: normalize(raw.get(name, "")) for name in REQUIRED_COLUMNS}
            code = row["Κωδικός"]
            if SOURCE_ID_RE.fullmatch(code) is None:
                raise ValueError(f"Μη έγκυρος κωδικός στη γραμμή {line_number}: {code!r}")
            if code in seen:
                raise ValueError(f"Διπλός κωδικός στον κατάλογο: {code}")
            seen.add(code)
            rows.append(row)

    return sorted(
        rows,
        key=lambda row: (row["Τίτλος"].casefold(), row["Έτος"], row["Κωδικός"]),
    )


def split_topics(value: str) -> Iterable[str]:
    for item in value.split(";"):
        item = normalize(item)
        if item:
            yield item


def count_column(rows: Sequence[Mapping[str, str]], column: str) -> Counter[str]:
    return Counter(normalize(row.get(column, "")) or "χωρίς τιμή" for row in rows)


def count_topics(rows: Sequence[Mapping[str, str]]) -> Counter[str]:
    result: Counter[str] = Counter()
    for row in rows:
        topics = list(split_topics(normalize(row.get("Θέματα", ""))))
        result.update(topics or ["χωρίς κατηγορία"])
    return result


def render_counter(counter: Counter[str], heading: str) -> list[str]:
    lines = [f"| {heading} | Πλήθος |", "|---|---:|"]
    for label, count in sorted(counter.items(), key=lambda item: (-item[1], item[0].casefold())):
        lines.append(f"| {markdown_escape(label)} | {count} |")
    return lines


def generate_archive(root: Path, rows: Sequence[Mapping[str, str]]) -> str:
    source_dir = root / "πηγές"
    missing = [row["Κωδικός"] for row in rows if not (source_dir / f"{row['Κωδικός']}.md").is_file()]

    lines = [
        "# Αρχείο πηγών",
        "",
        "> Generated αρχείο. Μην το επεξεργάζεσαι χειροκίνητα.",
        "> Η δομημένη πηγή αλήθειας είναι το `κατάλογος/πηγές.csv` και όλα τα πλήρη",
        "> Markdown βρίσκονται στον ενιαίο φάκελο `πηγές/`.",
        "",
        f"- **Συνολικές ενεργές πηγές:** {len(rows)}",
        f"- **Πλήρη Markdown που λείπουν:** {len(missing)}",
        "- **Χρήση:** απογραφή, φίλτρα, έλεγχος μεταδεδομένων και επιλογή πηγών για τη διπλωματική.",
        "",
        "Η καταχώριση δεν σημαίνει ότι η πηγή έχει επαληθευτεί ή εγκριθεί για παραπομπή.",
        "",
        "## Σύνοψη ανά τύπο",
        "",
        *render_counter(count_column(rows, "Τύπος"), "Τύπος πηγής"),
        "",
        "## Σύνοψη ανά θέμα / tag",
        "",
        *render_counter(count_topics(rows), "Θέμα / tag"),
        "",
        "## Σύνοψη κατάστασης",
        "",
        *render_counter(count_column(rows, "Κατάσταση"), "Κατάσταση"),
        "",
        "## Πλήρης πίνακας πηγών",
        "",
        "| Κωδικός | Τίτλος | Συγγραφείς | Έτος | Τύπος | Κατηγορίες / tags | Κατάσταση | Επιβεβαίωση | Προτεραιότητα | Markdown | Link | Σημειώσεις |",
        "|---|---|---|---:|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        code = row["Κωδικός"]
        local = source_dir / f"{code}.md"
        cells = (
            f"`{code}`",
            markdown_escape(row["Τίτλος"]),
            markdown_escape(row["Συγγραφείς"]),
            markdown_escape(row["Έτος"]),
            markdown_escape(row["Τύπος"]),
            markdown_escape(row["Θέματα"]),
            markdown_escape(row["Κατάσταση"]),
            markdown_escape(row["Επιβεβαίωση"]),
            markdown_escape(row["Προτεραιότητα"]),
            f"[πηγή](πηγές/{code}.md)" if local.is_file() else "λείπει",
            safe_link(row["Σύνδεσμος"]),
            markdown_escape(row["Σημειώσεις"]),
        )
        lines.append("| " + " | ".join(cells) + " |")

    if missing:
        lines.extend(["", "## Markdown που λείπουν", "", *[f"- `{code}`" for code in missing]])

    return "\n".join([*lines, ""])


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text.strip()
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}, text.strip()

    metadata: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        key, separator, value = line.partition(":")
        if separator:
            # Δεν γίνεται casefold στα keys: το ελληνικό τελικό ς θα μετατρεπόταν σε σ.
            metadata[normalize(key)] = normalize(value).strip("\"'")
    return metadata, text[closing + 5 :].strip()


def remove_first_h1(body: str) -> str:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            del lines[index]
            while index < len(lines) and not lines[index].strip():
                del lines[index]
            break
    return "\n".join(lines).strip()


def verified_excerpt_files(root: Path) -> list[tuple[str, Path, dict[str, str], str]]:
    folder = root / "αποσπάσματα"
    if not folder.is_dir():
        return []

    result: list[tuple[str, Path, dict[str, str], str]] = []
    for path in sorted(folder.glob("SRC-*.md"), key=lambda item: item.name):
        metadata, body = parse_front_matter(path.read_text(encoding="utf-8"))
        code = normalize(metadata.get("κωδικός", "")) or path.stem

        if SOURCE_ID_RE.fullmatch(code) is None:
            raise ValueError(f"Μη έγκυρος κωδικός στο {path}: {code!r}")
        if code != path.stem:
            raise ValueError(f"Ασυμφωνία κωδικού στο {path}: {code} != {path.stem}")

        status = normalize(metadata.get("κατάσταση", "")).casefold()
        checked = normalize(metadata.get("ελεγχθέν-πρωτότυπο", "")).casefold()
        if status != VERIFIED_STATUS or checked not in {"ναι", "yes", "true"}:
            continue
        result.append((code, path, metadata, remove_first_h1(body)))
    return result


def generate_excerpts(root: Path, rows: Sequence[Mapping[str, str]]) -> str:
    catalog = {row["Κωδικός"]: row for row in rows}
    included = verified_excerpt_files(root)

    lines = [
        "# Χρήσιμα αποσπάσματα",
        "",
        "> Generated αρχείο από τα επαληθευμένα `αποσπάσματα/SRC-*.md`.",
        "> Περιλαμβάνονται μόνο αρχεία με `κατάσταση: επαληθευμένο` και",
        "> `ελεγχθέν-πρωτότυπο: ναι`. Πρόχειρες επιλογές NotebookLM δεν είναι citation-ready evidence.",
        "",
        f"- **Πηγές με επαληθευμένα αποσπάσματα:** {len(included)}",
        "- **Ιχνηλασιμότητα:** κωδικός `SRC-*`, ακριβής θέση, ισχυρισμός, συμφραζόμενα και περιορισμοί.",
        "",
        "## Ευρετήριο",
        "",
        "| Κωδικός | Πηγή | Συγγραφείς | Έτος | Θέματα | Αποσπάσματα | Πλήρες Markdown | Link |",
        "|---|---|---|---:|---|---|---|---|",
    ]

    for code, path, _metadata, _body in included:
        row = catalog.get(code)
        if row is None:
            raise ValueError(f"Το {path} δεν αντιστοιχεί σε καταχωρισμένη πηγή")
        cells = (
            f"`{code}`",
            markdown_escape(row["Τίτλος"]),
            markdown_escape(row["Συγγραφείς"]),
            markdown_escape(row["Έτος"]),
            markdown_escape(row["Θέματα"]),
            f"[αρχείο](αποσπάσματα/{code}.md)",
            f"[πηγή](πηγές/{code}.md)",
            safe_link(row["Σύνδεσμος"]),
        )
        lines.append("| " + " | ".join(cells) + " |")

    if not included:
        return "\n".join([*lines, "", "Δεν υπάρχουν ακόμη επαληθευμένα αποσπάσματα.", ""])

    for code, _path, metadata, body in included:
        row = catalog[code]
        lines.extend(
            [
                "",
                "---",
                "",
                f"## `{code}` — {row['Τίτλος']}",
                "",
                f"- **Συγγραφείς:** {row['Συγγραφείς'] or '—'}",
                f"- **Έτος:** {row['Έτος'] or '—'}",
                f"- **Τύπος:** {row['Τύπος'] or '—'}",
                f"- **Θέματα / tags:** {row['Θέματα'] or '—'}",
                f"- **Ημερομηνία ελέγχου:** {metadata.get('ημερομηνία-ελέγχου', '—') or '—'}",
                f"- **Αρχεία:** [πλήρες Markdown](πηγές/{code}.md) · [αποσπάσματα](αποσπάσματα/{code}.md)",
                f"- **Εξωτερική πηγή:** {safe_link(row['Σύνδεσμος'])}",
                "",
                body or "_Δεν υπάρχει σώμα αποσπασμάτων._",
            ]
        )

    return "\n".join([*lines, ""])


def generate_outputs(root: Path) -> dict[Path, str]:
    root = root.resolve()
    rows = read_catalog(root / "κατάλογος" / "πηγές.csv")
    return {
        root / ARCHIVE_FILENAME: generate_archive(root, rows),
        root / EXCERPTS_FILENAME: generate_excerpts(root, rows),
    }


def write_outputs(outputs: Mapping[Path, str]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(path)


def check_outputs(outputs: Mapping[Path, str]) -> bool:
    stale = [
        path
        for path, expected in outputs.items()
        if not path.is_file() or path.read_text(encoding="utf-8") != expected
    ]
    if stale:
        print("Τα παρακάτω συγκεντρωτικά αρχεία λείπουν ή είναι παρωχημένα:", file=sys.stderr)
        for path in stale:
            print(f"- {path}", file=sys.stderr)
        return False
    return True


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    try:
        outputs = generate_outputs(args.root)
        if args.check:
            return 0 if check_outputs(outputs) else 1
        write_outputs(outputs)
    except (OSError, ValueError) as exc:
        print(f"Σφάλμα δημιουργίας συγκεντρωτικών αρχείων: {exc}", file=sys.stderr)
        return 2

    for path in outputs:
        print(f"Ενημερώθηκε: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
