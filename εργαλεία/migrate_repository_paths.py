#!/usr/bin/env python3
"""One-off migration of repository infrastructure paths to English names.

The migration changes paths and technical identifiers only. It does not translate
scientific prose or source/evidence content. Tracked files are moved with `git mv`
so Git history remains traceable. Any Greek path that is not covered by the mapping
is left unchanged and reported for a follow-up mapping pass.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GREEK_RE = re.compile(r"[Α-Ωα-ωΆΈΉΊΌΎΏάέήίόύώϊΐϋΰ]")

DIR_MAP = {
    "πηγές": "sources",
    "αναλύσεις": "analyses",
    "αποσπάσματα": "evidence",
    "κατάλογος": "catalog",
    "πρωτότυπα": "originals",
    "νέα-πρωτότυπα": "new-originals",
    "νέες-πηγές": "new-sources",
    "μετατροπή": "conversion",
    "εργαλεία": "tools",
    "πακέτο-διπλωματικής": "thesis-package",
    "πρότυπα": "templates",
    "συγχρονισμός": "sync",
    "μη-ταυτοποιημένα": "unidentified",
    "παρτίδες-ανάλυσης": "analysis-batches",
}

FILE_MAP = {
    # Root / documentation files.
    "ΑΡΧΕΙΟ_ΠΗΓΩΝ.md": "SOURCE_ARCHIVE.md",

    # Catalog files.
    "πηγές.csv": "sources.csv",
    "πηγές.md": "sources.md",
    "πρωτότυπα.csv": "originals.csv",
    "πρωτότυπα.md": "originals.md",
    "επιλογή-διπλωματικής.csv": "thesis-selection.csv",
    "επιλογή-διπλωματικής.md": "thesis-selection.md",
    "κατάσταση-αναλύσεων.csv": "analysis-status.csv",
    "κατάσταση-αναλύσεων.md": "analysis-status.md",
    "κατάσταση-μετατροπών.csv": "conversion-status.csv",
    "κατάσταση-μετατροπών.md": "conversion-status.md",
    "εκκρεμή-πρωτότυπα.md": "pending-originals.md",
    "προβληματικές-πηγές.md": "problematic-sources.md",

    # Templates.
    "ανάλυση-πηγής.md": "source-analysis.md",
    "απόσπασμα-πηγής.md": "source-evidence.md",

    # Permanent workflows.
    "ενημέρωση-μεταδεδομένων.yml": "update-metadata.yml",
    "ενημέρωση-συγκεντρωτικών.yml": "update-aggregates.yml",
    "πακέτο-διπλωματικής.yml": "thesis-package.yml",
    "αυτόματη-εισαγωγή.yml": "automatic-import.yml",
    "ενημέρωση-πρωτοτύπων.yml": "update-originals.yml",

    # Tools.
    "έλεγχος.py": "validate.py",
    "εισαγωγή.py": "import_sources.py",
    "πρωτότυπα.py": "originals.py",
    "κοινά_πηγών.py": "sources_common.py",
    "μεταδεδομένα.py": "metadata.py",
    "συγκεντρωτικά.py": "aggregates.py",
    "μετατροπή-pdf.py": "convert_pdf.py",
    "επόμενες-πηγές.py": "next_sources.py",
    "οριστικοποίηση.py": "finalize.py",
    "πρωτότυπα_κοινά.py": "originals_common.py",
    "διόρθωση-τίτλων.py": "fix_titles.py",
    "pdf-προς-μετατροπή.py": "pdfs_to_convert.py",
    "πρωτότυπα_αρχεία.py": "originals_files.py",
    "πρωτότυπα_λήψεις.py": "originals_downloads.py",
    "ακριβή-διπλότυπα.py": "exact_duplicates.py",
    "κατάσταση_απόφασης.py": "decision_status.py",
    "γνωστές-διορθώσεις.py": "known_fixes.py",
    "κατάσταση-αναλύσεων.py": "analysis_status.py",
    "καθαρισμός-συνδέσεων.py": "clean_links.py",
    "συγχρονισμός-επιλογής.py": "sync_selection.py",
    "εξαγωγή-διπλωματικής.py": "export_thesis.py",
}

# Bare Python module references need updates in addition to path replacements.
MODULE_MAP = {
    Path(old).stem: Path(new).stem
    for old, new in FILE_MAP.items()
    if old.endswith(".py") and new.endswith(".py")
}


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, check=check, capture_output=True)


def tracked_files() -> list[str]:
    result = run("git", "ls-files", "-z")
    return [item for item in result.stdout.split("\0") if item]


def map_component(component: str) -> str:
    if component in DIR_MAP:
        return DIR_MAP[component]
    if component in FILE_MAP:
        return FILE_MAP[component]
    match = re.fullmatch(r"παρτίδα-(\d+)\.md", component)
    if match:
        return f"batch-{match.group(1)}.md"
    return component


def target_path(path: str) -> str:
    return "/".join(map_component(part) for part in path.split("/"))


def ensure_parent(path: str) -> None:
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)


def move_files() -> dict[str, str]:
    original = tracked_files()
    mapping = {old: target_path(old) for old in original}
    mapping = {old: new for old, new in mapping.items() if old != new}

    targets: dict[str, str] = {}
    for old, new in mapping.items():
        if new in targets and targets[new] != old:
            raise RuntimeError(f"Path collision: {targets[new]} and {old} -> {new}")
        targets[new] = old

    # Moving files individually avoids ordering problems when both a directory and
    # basenames change in the same migration.
    for old in sorted(mapping, key=lambda value: (value.count("/"), len(value)), reverse=True):
        new = mapping[old]
        if not (ROOT / old).exists():
            continue
        ensure_parent(new)
        run("git", "mv", old, new)
    return mapping


def technical_replacements(mapping: dict[str, str]) -> list[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set(mapping.items())

    # Directory prefixes and quoted directory tokens catch generated paths and Path(...)
    # constants without translating ordinary prose words.
    for old, new in DIR_MAP.items():
        pairs.add((old + "/", new + "/"))
        pairs.add((f'"{old}"', f'"{new}"'))
        pairs.add((f"'{old}'", f"'{new}'"))
        pairs.add((f"`{old}`", f"`{new}`"))

    for old, new in FILE_MAP.items():
        pairs.add((old, new))

    # Longer paths first prevents a directory-prefix replacement from hiding an exact path.
    return sorted(pairs, key=lambda item: len(item[0]), reverse=True)


def update_text_references(mapping: dict[str, str]) -> int:
    replacements = technical_replacements(mapping)
    changed = 0
    for rel in tracked_files():
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        original = text
        for old, new in replacements:
            text = text.replace(old, new)
        if path.suffix == ".py":
            for old, new in MODULE_MAP.items():
                text = re.sub(rf"(?m)(\bfrom\s+){re.escape(old)}(\s+import\b)", rf"\1{new}\2", text)
                text = re.sub(rf"(?m)(\bimport\s+){re.escape(old)}\b", rf"\1{new}", text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def residual_greek_paths() -> list[str]:
    return sorted(path for path in tracked_files() if GREEK_RE.search(path))


def write_report(mapping: dict[str, str], changed_text_files: int) -> None:
    report = ROOT / "catalog" / "path-migration-report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    residual = residual_greek_paths()
    lines = [
        "# English path migration report",
        "",
        f"- Tracked paths moved in this pass: **{len(mapping)}**",
        f"- UTF-8 files with updated technical references: **{changed_text_files}**",
        f"- Remaining tracked paths containing Greek characters: **{len(residual)}**",
        "",
    ]
    if residual:
        lines += [
            "## Remaining Greek paths",
            "",
            "These paths were deliberately left unchanged because no semantic English mapping was defined yet.",
            "They must be mapped in a follow-up pass; transliteration is not treated as an English-name fix.",
            "",
        ] + [f"- `{path}`" for path in residual] + [""]
    else:
        lines += ["No tracked path contains Greek characters.", ""]
    report.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    mapping = move_files()
    changed = update_text_references(mapping)
    write_report(mapping, changed)
    residual = residual_greek_paths()
    print(f"Moved {len(mapping)} tracked paths; updated {changed} text files; residual Greek paths={len(residual)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
