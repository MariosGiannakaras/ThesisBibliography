#!/usr/bin/env python3
"""Validate that the committed thesis package matches the canonical export state.

The package intentionally pins the bibliography commit that produced it, so a byte-for-byte
regeneration at the current HEAD would always change provenance fields after the package is
committed. This validator therefore checks semantic/content convergence while preserving that
source-state pin.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

import export_thesis

EXPORT_INPUT_PATHS = [
    "catalog/sources.csv",
    "catalog/thesis-selection.csv",
    "analyses",
    "evidence",
    "tools/decision_status.py",
    "tools/language_audit.py",
    "tools/sync_selection.py",
    "tools/analysis_status.py",
    "tools/convert_pdf.py",
    "tools/export_thesis.py",
]
EXPECTED_TOP_LEVEL = {
    "README.md",
    "SOURCE_COMMIT",
    "manifest.csv",
    "catalog",
    "analyses",
    "evidence",
}
README_COUNT_RE = re.compile(r"Επιλεγμένες πηγές:\s*\*\*(\d+)\*\*")
README_COMMIT_RE = re.compile(r"Commit `ThesisBibliography`:\s*`([0-9a-f]{40})`")
COMMIT_RE = re.compile(r"[0-9a-f]{40}")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def source_ids(directory: Path) -> set[str]:
    if not directory.exists():
        return set()
    return {path.stem for path in directory.glob("SRC-*.md") if path.is_file()}


def relative_list(values: set[str]) -> str:
    return ", ".join(sorted(values)[:10])


def validate_provenance(package: Path, source_commit: str, errors: list[str]) -> None:
    """Ensure the package pin is a real ancestor and no exporter inputs changed after it."""
    root = export_thesis.ROOT
    git_dir = root / ".git"
    if not git_dir.exists():
        return

    verify = subprocess.run(
        ["git", "cat-file", "-e", f"{source_commit}^{{commit}}"],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if verify.returncode != 0:
        errors.append(f"thesis-package: SOURCE_COMMIT is not available in Git history: {source_commit}")
        return

    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_commit, "HEAD"],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if ancestor.returncode != 0:
        errors.append(f"thesis-package: SOURCE_COMMIT is not an ancestor of HEAD: {source_commit}")
        return

    changed = subprocess.run(
        ["git", "diff", "--quiet", f"{source_commit}..HEAD", "--", *EXPORT_INPUT_PATHS],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if changed.returncode == 1:
        errors.append(
            "thesis-package is stale: canonical export inputs changed after SOURCE_COMMIT "
            f"{source_commit}"
        )
    elif changed.returncode not in {0, 1}:
        errors.append("thesis-package: failed to compare SOURCE_COMMIT with current export inputs")


def validate_package(package: Path | None = None) -> list[str]:
    package = package or export_thesis.DEFAULT_OUTPUT
    errors: list[str] = []

    export_errors, exported, catalog, catalog_fields = export_thesis.validate()
    if export_errors:
        return [f"canonical export validation: {error}" for error in export_errors]

    expected_ids = {row["Κωδικός"].strip() for row in exported}
    if not package.exists():
        return [f"Missing committed thesis package: {package}"]

    top_level = {path.name for path in package.iterdir()}
    missing_top = EXPECTED_TOP_LEVEL - top_level
    extra_top = top_level - EXPECTED_TOP_LEVEL
    if missing_top:
        errors.append("thesis-package: missing top-level entries: " + relative_list(missing_top))
    if extra_top:
        errors.append("thesis-package: unexpected top-level entries: " + relative_list(extra_top))

    pdfs = [path.relative_to(package).as_posix() for path in package.rglob("*.pdf")]
    if pdfs:
        errors.append("thesis-package must not contain PDFs: " + ", ".join(sorted(pdfs)[:10]))
    if (package / "sources").exists():
        errors.append("thesis-package must not contain canonical/raw source Markdown")

    analyses_dir = package / "analyses"
    evidence_dir = package / "evidence"
    analysis_ids = source_ids(analyses_dir)
    evidence_ids = source_ids(evidence_dir)
    if analysis_ids != expected_ids:
        missing = expected_ids - analysis_ids
        extra = analysis_ids - expected_ids
        if missing:
            errors.append("thesis-package analyses missing selected IDs: " + relative_list(missing))
        if extra:
            errors.append("thesis-package analyses contain unselected IDs: " + relative_list(extra))
    if evidence_ids != expected_ids:
        missing = expected_ids - evidence_ids
        extra = evidence_ids - expected_ids
        if missing:
            errors.append("thesis-package evidence missing selected IDs: " + relative_list(missing))
        if extra:
            errors.append("thesis-package evidence contain unselected IDs: " + relative_list(extra))

    for source_id in sorted(expected_ids & analysis_ids):
        canonical = export_thesis.ANALYSES / f"{source_id}.md"
        packaged = analyses_dir / f"{source_id}.md"
        if canonical.read_bytes() != packaged.read_bytes():
            errors.append(f"thesis-package analysis differs from canonical analysis: {source_id}")
    for source_id in sorted(expected_ids & evidence_ids):
        canonical = export_thesis.EXCERPTS / f"{source_id}.md"
        packaged = evidence_dir / f"{source_id}.md"
        if canonical.read_bytes() != packaged.read_bytes():
            errors.append(f"thesis-package evidence differs from canonical evidence: {source_id}")

    package_catalog = package / "catalog" / "sources.csv"
    if not package_catalog.exists():
        errors.append("thesis-package: missing catalog/sources.csv")
    else:
        fields, rows = read_csv(package_catalog)
        if fields != catalog_fields:
            errors.append("thesis-package catalog fields differ from canonical catalog")
        packaged_catalog = {row.get("Κωδικός", "").strip(): row for row in rows}
        if set(packaged_catalog) != expected_ids:
            missing = expected_ids - set(packaged_catalog)
            extra = set(packaged_catalog) - expected_ids
            if missing:
                errors.append("thesis-package catalog missing selected IDs: " + relative_list(missing))
            if extra:
                errors.append("thesis-package catalog contains unselected IDs: " + relative_list(extra))
        for source_id in sorted(expected_ids & set(packaged_catalog)):
            expected_row = {field: catalog[source_id].get(field, "") for field in catalog_fields}
            actual_row = {field: packaged_catalog[source_id].get(field, "") for field in catalog_fields}
            if actual_row != expected_row:
                errors.append(f"thesis-package catalog row differs from canonical catalog: {source_id}")

    manifest_path = package / "manifest.csv"
    manifest_commits: set[str] = set()
    if not manifest_path.exists():
        errors.append("thesis-package: missing manifest.csv")
    else:
        manifest_fields, manifest_rows = read_csv(manifest_path)
        expected_fields = export_thesis.SELECTION_FIELDS + [
            "Τίτλος",
            "Σύνδεσμος",
            "Commit βιβλιογραφίας",
        ]
        if manifest_fields != expected_fields:
            errors.append("thesis-package manifest fields differ from exporter schema")
        manifest = {row.get("Κωδικός", "").strip(): row for row in manifest_rows}
        if set(manifest) != expected_ids:
            missing = expected_ids - set(manifest)
            extra = set(manifest) - expected_ids
            if missing:
                errors.append("thesis-package manifest missing selected IDs: " + relative_list(missing))
            if extra:
                errors.append("thesis-package manifest contains unselected IDs: " + relative_list(extra))

        selection = {row["Κωδικός"].strip(): row for row in exported}
        for source_id in sorted(expected_ids & set(manifest)):
            actual = manifest[source_id]
            expected = selection[source_id]
            for field in export_thesis.SELECTION_FIELDS:
                if actual.get(field, "") != expected.get(field, ""):
                    errors.append(f"thesis-package manifest differs from selection for {source_id}: {field}")
                    break
            if actual.get("Τίτλος", "") != catalog[source_id].get("Τίτλος", ""):
                errors.append(f"thesis-package manifest title differs from catalog: {source_id}")
            if actual.get("Σύνδεσμος", "") != catalog[source_id].get("Σύνδεσμος", ""):
                errors.append(f"thesis-package manifest link differs from catalog: {source_id}")
            commit = actual.get("Commit βιβλιογραφίας", "").strip()
            if commit:
                manifest_commits.add(commit)
            else:
                errors.append(f"thesis-package manifest lacks source commit: {source_id}")

    source_commit_path = package / "SOURCE_COMMIT"
    source_commit = ""
    if not source_commit_path.exists():
        errors.append("thesis-package: missing SOURCE_COMMIT")
    else:
        source_commit = source_commit_path.read_text(encoding="utf-8", errors="replace").strip()
        if not COMMIT_RE.fullmatch(source_commit):
            errors.append("thesis-package: SOURCE_COMMIT is not a full Git commit SHA")

    if len(manifest_commits) > 1:
        errors.append("thesis-package manifest contains multiple bibliography commit pins")
    elif manifest_commits and source_commit and manifest_commits != {source_commit}:
        errors.append("thesis-package manifest commit pin differs from SOURCE_COMMIT")

    readme_path = package / "README.md"
    if not readme_path.exists():
        errors.append("thesis-package: missing README.md")
    else:
        readme = readme_path.read_text(encoding="utf-8", errors="replace")
        count_match = README_COUNT_RE.search(readme)
        if not count_match:
            errors.append("thesis-package README lacks selected-source count")
        elif int(count_match.group(1)) != len(expected_ids):
            errors.append(
                "thesis-package README selected-source count is stale: "
                f"{count_match.group(1)} != {len(expected_ids)}"
            )
        commit_match = README_COMMIT_RE.search(readme)
        if not commit_match:
            errors.append("thesis-package README lacks bibliography commit pin")
        elif source_commit and commit_match.group(1) != source_commit:
            errors.append("thesis-package README commit pin differs from SOURCE_COMMIT")

    if source_commit and COMMIT_RE.fullmatch(source_commit):
        validate_provenance(package, source_commit, errors)

    return errors


def main() -> int:
    errors = validate_package()
    if errors:
        print("Committed thesis package validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Committed thesis package matches the canonical verified export state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
