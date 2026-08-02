#!/usr/bin/env python3
"""Migrate repository infrastructure paths to English without touching scientific prose."""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NON_ASCII_RE = re.compile(r"[^\x00-\x7F]")
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".csv", ".json", ".txt", ".toml", ".ini", ".cfg", ".sh"}
ROOT_TEXT_NAMES = {"README.md", "LANGUAGE_POLICY.md", "SOURCE_ARCHIVE.md", "USEFUL_EVIDENCE.md", ".gitignore", ".gitattributes"}
REWRITE_TOP_LEVEL = {".github", "tools", "tests", "catalog", "templates", "sync", "thesis-package"}

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
    "ΑΡΧΕΙΟ_ΠΗΓΩΝ.md": "SOURCE_ARCHIVE.md",
    "ΧΡΗΣΙΜΑ_ΑΠΟΣΠΑΣΜΑΤΑ.md": "USEFUL_EVIDENCE.md",
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
    "ανάλυση-πηγής.md": "source-analysis.md",
    "απόσπασμα-πηγής.md": "source-evidence.md",
    "ενημέρωση-μεταδεδομένων.yml": "update-metadata.yml",
    "ενημέρωση-συγκεντρωτικών.yml": "update-aggregates.yml",
    "πακέτο-διπλωματικής.yml": "thesis-package.yml",
    "αυτόματη-εισαγωγή.yml": "automatic-import.yml",
    "ενημέρωση-πρωτοτύπων.yml": "update-originals.yml",
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
    "test_συγκεντρωτικά.py": "test_aggregates.py",
}

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


def planned_mapping() -> dict[str, str]:
    original = tracked_files()
    original_set = set(original)
    mapping = {old: target_path(old) for old in original}
    mapping = {old: new for old, new in mapping.items() if old != new}
    targets: dict[str, str] = {}
    for old, new in mapping.items():
        if new in targets and targets[new] != old:
            raise RuntimeError(f"Path collision: {targets[new]} and {old} -> {new}")
        if new in original_set and new not in mapping:
            raise RuntimeError(f"Path collision with existing tracked file: {old} -> {new}")
        targets[new] = old
    return mapping


def working_tree_entries() -> tuple[list[Path], list[Path]]:
    directories: list[Path] = []
    files: list[Path] = []
    for root, dirnames, filenames in os.walk(ROOT, topdown=True):
        dirnames[:] = [name for name in dirnames if name != ".git"]
        root_path = Path(root)
        directories.extend(root_path / name for name in dirnames)
        files.extend(root_path / name for name in filenames)
    return directories, files


def move_paths() -> dict[str, str]:
    mapping = planned_mapping()
    directories, _ = working_tree_entries()
    for path in sorted(directories, key=lambda p: len(p.relative_to(ROOT).parts), reverse=True):
        new_name = DIR_MAP.get(path.name)
        if not new_name or not path.exists():
            continue
        target = path.with_name(new_name)
        if target.exists():
            raise RuntimeError(f"Directory collision: {path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        path.rename(target)

    _, files = working_tree_entries()
    for path in files:
        new_name = FILE_MAP.get(path.name)
        if not new_name:
            match = re.fullmatch(r"παρτίδα-(\d+)\.md", path.name)
            if match:
                new_name = f"batch-{match.group(1)}.md"
        if not new_name or not path.exists():
            continue
        target = path.with_name(new_name)
        if target.exists():
            raise RuntimeError(f"File collision: {path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        path.rename(target)

    run("git", "add", "-A")
    return mapping


def technical_replacements() -> list[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for old, new in DIR_MAP.items():
        pairs.add((old + "/", new + "/"))
        pairs.add((f'"{old}"', f'"{new}"'))
        pairs.add((f"'{old}'", f"'{new}'"))
        pairs.add((f"`{old}`", f"`{new}`"))
    pairs.update(FILE_MAP.items())
    return sorted(pairs, key=lambda item: len(item[0]), reverse=True)


def is_text_candidate(rel: str, path: Path) -> bool:
    parts = Path(rel).parts
    if not parts:
        return False
    if len(parts) == 1:
        return path.name in ROOT_TEXT_NAMES
    if parts[0] not in REWRITE_TOP_LEVEL:
        return False
    if len(parts) >= 2 and parts[0] == "thesis-package" and parts[1] in {"analyses", "evidence"}:
        return False
    return path.suffix.casefold() in TEXT_SUFFIXES


def update_text_references() -> int:
    replacements = technical_replacements()
    changed = 0
    for rel in tracked_files():
        path = ROOT / rel
        if not path.is_file() or not is_text_candidate(rel, path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        original = text
        for old, new in replacements:
            if old in text:
                text = text.replace(old, new)
        text = re.sub(r"παρτίδα-(\d+)\.md", r"batch-\1.md", text)
        if path.suffix == ".py":
            for old, new in MODULE_MAP.items():
                text = re.sub(rf"(?m)(\bfrom\s+){re.escape(old)}(\s+import\b)", rf"\1{new}\2", text)
                text = re.sub(rf"(?m)(\bimport\s+){re.escape(old)}\b", rf"\1{new}", text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    run("git", "add", "-A")
    return changed


def residual_non_ascii_paths() -> list[str]:
    return sorted(path for path in tracked_files() if NON_ASCII_RE.search(path))


def write_report(mapping: dict[str, str], changed_text_files: int) -> None:
    report = ROOT / "catalog" / "path-migration-report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    residual = residual_non_ascii_paths()
    lines = [
        "# English path migration report",
        "",
        f"- Tracked paths moved in this pass: **{len(mapping)}**",
        f"- Infrastructure files with updated technical references: **{changed_text_files}**",
        f"- Remaining tracked paths containing non-ASCII characters: **{len(residual)}**",
        "",
    ]
    if residual:
        lines.extend(["## Remaining non-ASCII paths", "", *[f"- `{path}`" for path in residual], ""])
    else:
        lines.extend(["No tracked path contains non-ASCII characters.", ""])
    report.write_text("\n".join(lines), encoding="utf-8")
    run("git", "add", "-A")


def main() -> int:
    mapping = move_paths()
    changed = update_text_references()
    write_report(mapping, changed)
    residual = residual_non_ascii_paths()
    print(
        f"Moved {len(mapping)} tracked paths; updated {changed} infrastructure files; "
        f"residual non-ASCII paths={len(residual)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
