#!/usr/bin/env python3
"""Write and validate deterministic integrity metadata for the verified thesis package."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKAGE = ROOT / "thesis-package"
SCHEMA_VERSION = 1
METADATA_REL = Path("catalog/package-metadata.json")
CHECKSUMS_REL = Path("catalog/SHA256SUMS")
EXCLUDED = {METADATA_REL.as_posix(), CHECKSUMS_REL.as_posix()}
COMMIT_RE = re.compile(r"[0-9a-f]{40}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_files(package: Path) -> list[Path]:
    files: list[Path] = []
    for path in package.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(package).as_posix()
        if relative in EXCLUDED:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(package).as_posix())


def read_source_commit(package: Path) -> str:
    path = package / "SOURCE_COMMIT"
    if not path.exists():
        raise ValueError("missing SOURCE_COMMIT")
    commit = path.read_text(encoding="utf-8", errors="replace").strip()
    if not COMMIT_RE.fullmatch(commit):
        raise ValueError("SOURCE_COMMIT is not a full lowercase Git SHA")
    return commit


def manifest_count(package: Path) -> int:
    path = package / "manifest.csv"
    if not path.exists():
        raise ValueError("missing manifest.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def checksum_rows(package: Path) -> list[tuple[str, str]]:
    return [
        (sha256(path), path.relative_to(package).as_posix())
        for path in content_files(package)
    ]


def metadata(package: Path, rows: list[tuple[str, str]]) -> dict[str, object]:
    return {
        "schema_version": SCHEMA_VERSION,
        "package_type": "ThesisBibliography verified thesis package",
        "source_commit": read_source_commit(package),
        "selected_sources": manifest_count(package),
        "hash_algorithm": "sha256",
        "checksum_file": CHECKSUMS_REL.as_posix(),
        "integrity_scope": "all package files except catalog/package-metadata.json and catalog/SHA256SUMS",
        "file_count": len(rows),
        "content_roots": [
            "README.md",
            "SOURCE_COMMIT",
            "manifest.csv",
            "catalog/sources.csv",
            "analyses/",
            "evidence/",
        ],
    }


def write_integrity(package: Path) -> None:
    if not package.exists():
        raise ValueError(f"package does not exist: {package}")
    rows = checksum_rows(package)
    meta = metadata(package, rows)
    metadata_path = package / METADATA_REL
    checksums_path = package / CHECKSUMS_REL
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    checksums_path.write_text(
        "".join(f"{digest}  {relative}\n" for digest, relative in rows),
        encoding="utf-8",
    )


def parse_checksums(path: Path, errors: list[str]) -> dict[str, str]:
    rows: dict[str, str] = {}
    if not path.exists():
        errors.append(f"missing {CHECKSUMS_REL.as_posix()}")
        return rows
    for line_number, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if not raw.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", raw)
        if not match:
            errors.append(f"invalid checksum line {line_number}")
            continue
        digest, relative = match.groups()
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts or relative in EXCLUDED:
            errors.append(f"unsafe or excluded checksum path: {relative}")
            continue
        if relative in rows:
            errors.append(f"duplicate checksum path: {relative}")
            continue
        rows[relative] = digest
    return rows


def validate_integrity(package: Path) -> list[str]:
    errors: list[str] = []
    if not package.exists():
        return [f"package does not exist: {package}"]

    metadata_path = package / METADATA_REL
    checksums_path = package / CHECKSUMS_REL
    meta: dict[str, object] = {}
    if not metadata_path.exists():
        errors.append(f"missing {METADATA_REL.as_posix()}")
    else:
        try:
            loaded = json.loads(metadata_path.read_text(encoding="utf-8"))
            if not isinstance(loaded, dict):
                errors.append("package metadata must be a JSON object")
            else:
                meta = loaded
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid package metadata: {type(exc).__name__}")

    try:
        source_commit = read_source_commit(package)
    except ValueError as exc:
        errors.append(str(exc))
        source_commit = ""
    try:
        selected_sources = manifest_count(package)
    except ValueError as exc:
        errors.append(str(exc))
        selected_sources = -1

    if meta:
        if meta.get("schema_version") != SCHEMA_VERSION:
            errors.append(f"unsupported package schema_version: {meta.get('schema_version')}")
        if meta.get("package_type") != "ThesisBibliography verified thesis package":
            errors.append("unexpected package_type")
        if meta.get("hash_algorithm") != "sha256":
            errors.append("package hash_algorithm must be sha256")
        if meta.get("checksum_file") != CHECKSUMS_REL.as_posix():
            errors.append("package checksum_file path is inconsistent")
        if source_commit and meta.get("source_commit") != source_commit:
            errors.append("package metadata source_commit differs from SOURCE_COMMIT")
        if selected_sources >= 0 and meta.get("selected_sources") != selected_sources:
            errors.append("package metadata selected_sources differs from manifest.csv")

    recorded = parse_checksums(checksums_path, errors)
    actual_paths = {
        path.relative_to(package).as_posix(): path
        for path in content_files(package)
    }
    recorded_paths = set(recorded)
    expected_paths = set(actual_paths)
    missing = sorted(expected_paths - recorded_paths)
    extra = sorted(recorded_paths - expected_paths)
    if missing:
        errors.append("checksums missing package files: " + ", ".join(missing[:10]))
    if extra:
        errors.append("checksums reference missing package files: " + ", ".join(extra[:10]))

    for relative in sorted(expected_paths & recorded_paths):
        actual = sha256(actual_paths[relative])
        if recorded[relative] != actual:
            errors.append(f"checksum mismatch: {relative}")

    if meta and meta.get("file_count") != len(expected_paths):
        errors.append("package metadata file_count differs from integrity scope")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("write", "validate"))
    parser.add_argument("package", nargs="?", type=Path, default=DEFAULT_PACKAGE)
    args = parser.parse_args()
    package = args.package if args.package.is_absolute() else ROOT / args.package

    if args.action == "write":
        try:
            write_integrity(package)
        except ValueError as exc:
            print(f"Package integrity generation failed: {exc}", file=sys.stderr)
            return 1
        print(f"Wrote deterministic SHA-256 integrity metadata for {package}.")
        return 0

    errors = validate_integrity(package)
    if errors:
        print("Package integrity validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Package integrity is valid for {package}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
