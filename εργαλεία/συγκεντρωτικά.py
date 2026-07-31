#!/usr/bin/env python3
"""Παράγει τα δύο συγκεντρωτικά αρχεία πρώτης πρόσβασης του repository.

- ΑΡΧΕΙΟ_ΠΗΓΩΝ.md: πλήρης πίνακας όλων των ενεργών πηγών.
- ΧΡΗΣΙΜΑ_ΑΠΟΣΠΑΣΜΑΤΑ.md: συγκεντρωτική προβολή μόνο επαληθευμένων αποσπασμάτων.

Τα αρχεία είναι παράγωγα. Η πηγή αλήθειας παραμένει το
`κατάλογος/πηγές.csv`, τα `πηγές/SRC-*.md` και τα
`αποσπάσματα/SRC-*.md`.
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


def normalize(value: object) -> str:
    """Επιστρέφει καθαρό κείμενο χωρίς περιττά κενά."""

    return " ".join(str(value or "").split())


def markdown_escape(value: object) -> str:
    """Καθαρίζει τιμές για ασφαλή χρήση σε Markdown table cell."""

    text = normalize(value)
    return text.replace("\\", "\\\\").replace("|", "\\|") or "—"


def safe_link(url: object, label: str = "άνοιγμα") -> str:
    """Δημιουργεί σύνδεσμο μόνο για HTTP(S) URL."""

    value = normalize(url)
    if not re.match(r"^https?://", value, flags=re.IGNORECASE):
        return "—"
    return f"[{markdown_escape(label)}]({value})"


def read_catalog(catalog_path: Path) -> list[dict[str, str]]:
    if not catalog_path.is_file():
        raise FileNotFoundError(f"Δεν βρέθηκε ο κατάλογος: {catalog_path}")

    with catalog_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
        if missing:
            raise ValueError(
                "Ο κατάλογος δεν περιέχει τα υποχρεωτικά πεδία: "
                + ", ".join(missing)
            )

        rows: list[dict[str, str]] = []
        seen_codes: set[str] = set()
        for line_number, raw_row in enumerate(reader, start=2):
            row = {column: normalize(raw_row.get(column, "")) for column in REQUIRED_COLUMNS}
            code = row["Κωδικός"]
            if not re.fullmatch(r"SRC-[0-9A-F]{10}", code):
                raise ValueError(f"Μη έγκυρος κωδικός στη γραμμή {line_number}: {code!r}")
            if code in seen_codes:
                raise ValueError(f"Διπλός κωδικός στον κατάλογο: {code}")
            seen_codes.add(code)
            rows.append(row)

    return sorted(
        rows,
        key=lambda item: (
            item["Τίτλος"].casefold(),
            item["Έτος"],
            item["Κωδικός"],
        ),
    )


def split_topics(value: str) -> Iterable[str]:
    for topic in value.split(";"):
        cleaned = normalize(topic)
        if cleaned:
            yield cleaned


def count_values(rows: Sequence[Mapping[str, str]], column: str) -> Counter[str]:
    return Counter(normalize(row.get(column, "")) or "χωρίς τιμή" for row in rows)


def count_topics(rows: Sequence[Mapping[str, str]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        topics = list(split_topics(normalize(row.get("Θέματα", ""))))
        if topics:
            counter.update(topics)
        else:
            counter["χωρίς κατηγορία"] += 1
    return counter


def counter_table(counter: Counter[str], first_header: str) -> list[str]:
    lines = [f"| {first_header} | Πλήθος |", "|---|---:|"]
    for label, count in sorted(counter.items(), key=lambda item: (-item[1], item[0].casefold())):
        lines.append(f"| {markdown_escape(label)} | {count} |")
    return lines


def generate_archive(root: Path, rows: Sequence[Mapping[str, str]]) -> str:
    source_dir = root / "πηγές"
    missing_source_files = [
        row["Κωδικός"] for row in rows if not (source_dir / f"{row['Κωδικός']}.md").is_file()
    ]

    lines = [
        "# Αρχείο πηγών",
        "",
        "> Αυτό το αρχείο παράγεται αυτόματα. Μην το επεξεργάζεσαι χειροκίνητα.",
        "> Η δομημένη πηγή αλήθειας είναι το `κατάλογος/πηγές.csv` και τα πλήρη",
        "> Markdown βρίσκονται στον ενιαίο φάκελο `πηγές/`.",
        "",
        f"- **Συνολικές ενεργές πηγές:** {len(rows)}",
        f"- **Πλήρη αρχεία Markdown που λείπουν:** {len(missing_source_files)}",
        "- **Σκοπός:** απογραφή, φιλτράρισμα, έλεγχος μεταδεδομένων και προετοιμασία επιλογής για τη διπλωματική.",
        "",
        "Η παρουσία μιας πηγής στον πίνακα δεν σημαίνει ότι έχει επαληθευτεί ή εγκριθεί για παραπομπή.",
        "",
        "## Σύνοψη ανά τύπο",
        "",
        *counter_table(count_values(rows, "Τύπος"), "Τύπος πηγής"),
        "",
        "## Σύνοψη ανά θέμα / tag",
        "",
        *counter_table(count_topics(rows), "Θέμα / tag"),
        "",
        "## Σύνοψη κατάστασης",
        "",
        *counter_table(count_values(rows, "Κατάσταση"), "Κατάσταση"),
        "",
        "## Πλήρης πίνακας πηγών",
        "",
        "| Κωδικός | Τίτλος | Συγγραφείς | Έτος | Τύπος | Κατηγορίες / tags | Κατάσταση | Επιβεβαίωση | Προτεραιότητα | Markdown | Link | Σημειώσεις |",
        "|---|---|---|---:|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        code = row["Κωδικός"]
        source_path = source_dir / f"{code}.md"
        markdown_link = f"[πηγή](πηγές/{code}.md)" if source_path.is_file() else "λείπει"
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
            markdown_link,
            safe_link(row["Σύνδεσμος"]),
            markdown_escape(row["Σημειώσεις"]),
        )
        lines.append("| " + " | ".join(cells) + " |")

    if missing_source_files:
        lines.extend(
            [
                "",
                "## Αρχεία Markdown που λείπουν",
                "",
                *[f"- `{code}`" for code in missing_source_files],
            ]
        )

    lines.append("")
    return "\n".join(lines)


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
            metadata[normalize(key).casefold()] = normalize(value).strip('"\'')
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
    excerpt_dir = root / "αποσπάσματα"
    results: list[tuple[str, Path, dict[str, str], str]] = []
    if not excerpt_dir.is_dir():
        return results

    for path in sorted(excerpt_dir.glob("SRC-*.md"), key=lambda item: item.name):
        text = path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)
        code = normalize(metadata.get("κωδικός", "")) or path.stem
        status = normalize(metadata.get("κατάσταση", "")).casefold()
        checked_original = normalize(metadata.get("ελεγχθέν-πρωτότυπο", "")).casefold()
        if status != VERIFIED_STATUS or checked_original not in {"ναι", "yes", "true"}:
            continue
        if code != path.stem:
            raise ValueError(f"Ασυμφωνία κωδικού στο {path}: {code} != {path.stem}")
        results.append((code, path, metadata, remove_first_h1(body)))
    return results


def generate_excerpts(root: Path, rows: Sequence[Mapping[str, str]]) -> str:
    catalog = {row["Κωδικός"]: row for row in rows}
    included = verified_excerpt_files(root)

    lines = [
        "# Χρήσιμα αποσπάσματα",
        "",
        "> Αυτό το αρχείο παράγεται αυτόματα από τα επαληθευμένα αρχεία του φακέλου `αποσπάσματα/`.",
        "> Περιλαμβάνονται μόνο εγγραφές με `κατάσταση: επαληθευμένο` και",
        "> `ελεγχθέν-πρωτότυπο: ναι`. Πρόχειρες επιλογές του NotebookLM δεν εμφανίζονται ως citation-ready evidence.",
        "",
        f"- **Πηγές με επαληθευμένα αποσπάσματα:** {len(included)}",
        "- **Μονάδα ιχνηλασιμότητας:** κωδικός `SRC-*`, ακριβής θέση, ισχυρισμός, συμφραζόμενα και περιορισμοί.",
        "",
        "## Ευρετήριο",
        "",
        "| Κωδικός | Πηγή | Συγγραφείς | Έτος | Θέματα | Αρχείο αποσπασμάτων | Πλήρες Markdown | Link |",
        "|---|---|---|---:|---|---|---|---|",
    ]

    for code, path, _metadata, _body in included:
        row = catalog.get(code)
        if row is None:
            raise ValueError(f"Το αρχείο αποσπασμάτων {path} δεν υπάρχει στον κατάλογο")
        lines.append(
            "| "
            + " | ".join(
                (
                    f"`{code}`",
                    markdown_escape(row["Τίτλος"]),
                    markdown_escape(row["Συγγραφείς"]),
                    markdown_escape(row["Έτος"]),
                    markdown_escape(row["Θέματα"]),
                    f"[αποσπάσματα](αποσπάσματα/{code}.md)",
                    f"[πηγή](πηγές/{code}.md)",
                    safe_link(row["Σύνδεσμος"]),
                )
            )
            + " |"
        )

    if not included:
        lines.extend(["", "Δεν υπάρχουν ακόμη επαληθευμένα αποσπάσματα.", ""])
        return "\n".join(lines)

    for code, path, metadata, body in included:
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
                f"- **Αρχεία:** [πλήρες Markdown](πηγές/{code}.md) · [αρχείο αποσπασμάτων](αποσπάσματα/{code}.md)",
                f"- **Εξωτερική πηγή:** {safe_link(row['Σύνδεσμος'])}",
                "",
                body or "_Δεν υπάρχει σώμα αποσπασμάτων._",
            ]
        )

    lines.append("")
    return "\n".join(lines)


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
    stale: list[Path] = []
    for path, expected in outputs.items():
        actual = path.read_text(encoding="utf-8") if path.is_file() else None
        if actual != expected:
            stale.append(path)
    if stale:
        print("Τα παρακάτω συγκεντρωτικά αρχεία λείπουν ή είναι παρωχημένα:", file=sys.stderr)
        for path in stale:
            print(f"- {path}", file=sys.stderr)
        return False
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="ρίζα repository (χρήσιμο για tests)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="έλεγχος ότι τα ήδη αποθηκευμένα αρχεία είναι ενημερωμένα",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
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
