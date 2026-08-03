#!/usr/bin/env python3
"""Build and validate the complete writing-oriented research corpus.

Unlike thesis-package/, this export is not restricted to citation-ready evidence.
It preserves every available source text, analysis, evidence file, research note,
and otherwise-uncovered original as searchable Markdown with explicit trust labels.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.I)
DEFAULT_DIRS = ("sources", "analyses", "evidence", "materials", "notes")
CATALOG_FILES = (
    "sources.csv",
    "thesis-selection.csv",
    "analysis-status.csv",
    "conversion-status.csv",
    "research-materials.csv",
    "research-material-review.csv",
)
ROOT_FILES = ("SOURCE_ARCHIVE.md", "USEFUL_EVIDENCE.md")
METADATA_REL = Path("catalog/package-metadata.json")
CHECKSUM_REL = Path("catalog/SHA256SUMS")


def git_commit(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def file_identity(path: Path) -> str:
    prefix = path.read_bytes()[:512]
    match = LFS_OID_RE.search(prefix)
    if match:
        return match.group(1).decode("ascii").lower()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def immutable_url(path: Path, root: Path, commit: str) -> str:
    rel = path.relative_to(root).as_posix()
    return (
        "https://github.com/MariosGiannakaras/ThesisBibliography/blob/"
        f"{commit}/{quote(rel, safe='/')}"
    )


def copy_tree_if_exists(source: Path, target: Path) -> int:
    if not source.exists():
        return 0
    shutil.copytree(source, target, dirs_exist_ok=True)
    return sum(1 for path in target.rglob("*") if path.is_file())


def count_csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def originals_index(root: Path, output: Path, commit: str) -> int:
    materials: dict[str, str] = {}
    inventory = root / "catalog" / "research-materials.csv"
    if inventory.exists():
        with inventory.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                materials[row.get("original_path", "")] = row.get("material_id", "")
    rows: list[dict[str, str]] = []
    originals = root / "originals"
    paths = sorted(originals.rglob("*.pdf")) if originals.exists() else []
    for path in paths:
        rel = path.relative_to(root).as_posix()
        match = re.fullmatch(r"SRC-[A-F0-9]{10}", path.stem, re.I)
        rows.append({
            "original_path": rel,
            "sha256": file_identity(path),
            "linked_source_id": path.stem.upper() if match else "",
            "research_material_id": materials.get(rel, ""),
            "immutable_url": immutable_url(path, root, commit),
            "storage": "Git LFS in ThesisBibliography",
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "original_path", "sha256", "linked_source_id", "research_material_id",
            "immutable_url", "storage",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def content_files(output: Path) -> list[Path]:
    return sorted(
        path for path in output.rglob("*")
        if path.is_file() and path.relative_to(output) not in {METADATA_REL, CHECKSUM_REL}
    )


def write_integrity(output: Path, metadata: dict[str, object]) -> None:
    files = content_files(output)
    checksum_path = output / CHECKSUM_REL
    checksum_path.parent.mkdir(parents=True, exist_ok=True)
    checksum_path.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(output).as_posix()}\n" for path in files),
        encoding="utf-8",
    )
    metadata = dict(metadata)
    metadata.update({
        "schema_version": 1,
        "package_type": "ThesisBibliography complete research corpus",
        "hash_algorithm": "sha256",
        "checksum_file": CHECKSUM_REL.as_posix(),
        "integrity_scope": "all corpus files except catalog/package-metadata.json and catalog/SHA256SUMS",
        "file_count": len(files),
    })
    metadata_path = output / METADATA_REL
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def build(root: Path, output: Path) -> None:
    required = [
        root / "catalog" / "sources.csv",
        root / "catalog" / "research-materials.csv",
        root / "catalog" / "research-material-review.csv",
        root / "thesis-package",
    ]
    missing = [path.relative_to(root).as_posix() for path in required if not path.exists()]
    if missing:
        raise RuntimeError("Cannot build research corpus; missing: " + ", ".join(missing))
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    commit = git_commit(root)
    (output / "SOURCE_COMMIT").write_text(commit + "\n", encoding="utf-8")

    readme = """# Complete research corpus

This export is the writing-oriented superset of `thesis-package/`.

## Trust layers

- `citation-ready/`: the strict, verified citation package.
- `sources/`: every canonical source text, including rejected and non-citation material.
- `analyses/`: every scientific decision and analysis currently available.
- `evidence/`: every evidence file currently available.
- `materials/`: otherwise-uncovered PDF content extracted without translation. A material may be useful for drafting even when citation metadata is incomplete.
- `notes/`: user-authored fragments and working text. No bibliographic metadata is required.
- `catalog/originals-index.csv`: immutable paths, hashes, and URLs for all original PDFs.

`not-citation-ready` does not mean unimportant or inaccessible. It means only that the item must not be presented as a verified bibliographic citation until its identity is reviewed.
"""
    (output / "README.md").write_text(readme, encoding="utf-8")

    copy_tree_if_exists(root / "thesis-package", output / "citation-ready")
    copied_counts: dict[str, int] = {}
    for directory in DEFAULT_DIRS:
        copied_counts[directory] = copy_tree_if_exists(root / directory, output / directory)
    catalog_out = output / "catalog"
    catalog_out.mkdir(parents=True, exist_ok=True)
    for name in CATALOG_FILES:
        source = root / "catalog" / name
        if source.exists():
            shutil.copy2(source, catalog_out / name)
    aggregates = output / "aggregates"
    aggregates.mkdir(parents=True, exist_ok=True)
    for name in ROOT_FILES:
        source = root / name
        if source.exists():
            shutil.copy2(source, aggregates / name)
    original_count = originals_index(root, catalog_out / "originals-index.csv", commit)

    metadata = {
        "source_commit": commit,
        "source_count": count_csv_rows(root / "catalog" / "sources.csv"),
        "selected_source_count": count_csv_rows(root / "thesis-package" / "manifest.csv"),
        "research_material_count": count_csv_rows(root / "catalog" / "research-materials.csv"),
        "original_pdf_count": original_count,
        "copied_file_counts": copied_counts,
        "content_roots": [
            "README.md", "SOURCE_COMMIT", "citation-ready/", "sources/", "analyses/",
            "evidence/", "materials/", "notes/", "aggregates/", "catalog/",
        ],
    }
    write_integrity(output, metadata)
    print(f"Built complete research corpus at {output}")


def parse_checksums(path: Path) -> tuple[dict[str, str], list[str]]:
    checksums: dict[str, str] = {}
    errors: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = re.fullmatch(r"([a-f0-9]{64})  (.+)", line)
        if not match:
            errors.append(f"Malformed checksum line {number}")
            continue
        digest, rel = match.groups()
        if rel in checksums:
            errors.append(f"Duplicate checksum path: {rel}")
        checksums[rel] = digest
    return checksums, errors


def validate(root: Path, output: Path) -> list[str]:
    errors: list[str] = []
    metadata_path = output / METADATA_REL
    checksum_path = output / CHECKSUM_REL
    if not output.exists():
        return [f"Missing research corpus: {output}"]
    if not metadata_path.exists():
        errors.append("Missing research corpus metadata")
    if not checksum_path.exists():
        errors.append("Missing research corpus checksums")
    if errors:
        return errors
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"Invalid research corpus metadata: {exc}"]
    if metadata.get("schema_version") != 1:
        errors.append("Unsupported research corpus schema version")
    if metadata.get("package_type") != "ThesisBibliography complete research corpus":
        errors.append("Unexpected research corpus package type")
    source_commit = (output / "SOURCE_COMMIT").read_text(encoding="utf-8").strip() if (output / "SOURCE_COMMIT").exists() else ""
    if metadata.get("source_commit") != source_commit:
        errors.append("Research corpus source_commit does not match SOURCE_COMMIT")
    checksums, checksum_errors = parse_checksums(checksum_path)
    errors.extend(checksum_errors)
    files = content_files(output)
    expected = {path.relative_to(output).as_posix() for path in files}
    if set(checksums) != expected:
        errors.append(
            "Research corpus checksum path set mismatch: "
            f"missing={sorted(expected-set(checksums))[:10]}, extra={sorted(set(checksums)-expected)[:10]}"
        )
    for path in files:
        rel = path.relative_to(output).as_posix()
        if rel in checksums and sha256(path) != checksums[rel]:
            errors.append(f"Research corpus checksum mismatch: {rel}")
    if metadata.get("file_count") != len(files):
        errors.append("Research corpus file_count mismatch")
    source_count = count_csv_rows(output / "catalog" / "sources.csv")
    if metadata.get("source_count") != source_count:
        errors.append("Research corpus source_count mismatch")
    material_count = count_csv_rows(output / "catalog" / "research-materials.csv")
    if metadata.get("research_material_count") != material_count:
        errors.append("Research corpus research_material_count mismatch")
    required = [
        output / "citation-ready" / "catalog" / "package-metadata.json",
        output / "catalog" / "originals-index.csv",
        output / "sources",
        output / "materials",
        output / "notes" / "README.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required research corpus path: {path.relative_to(output)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("build", "validate"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or (root / "research-corpus")).resolve()
    if args.command == "build":
        build(root, output)
    errors = validate(root, output)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Complete research corpus is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
