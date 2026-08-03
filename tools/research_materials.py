#!/usr/bin/env python3
"""Preserve every otherwise-uncovered PDF as a searchable research material.

This layer is intentionally broader than the citation registry. A material may be
useful for drafting even when its title, author, URL, or citation identity is not
known. Extracted text is never translated and the original PDF remains canonical.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

try:
    from pypdf import PdfReader  # type: ignore
except ImportError:  # pragma: no cover
    PdfReader = None  # type: ignore[assignment]

LFS_PREFIX = b"version https://git-lfs.github.com/spec/v1"
LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.I)
GENERATED_MARKER = "<!-- GENERATED_RESEARCH_MATERIAL: v1 -->"
INVENTORY_FIELDS = [
    "material_id", "filename", "title_candidate", "author_candidate", "year_candidate",
    "candidate_source", "content_status", "page_count", "text_characters", "sha256",
    "original_path", "original_url", "linked_source_id",
]
REVIEW_FIELDS = [
    "material_id", "canonical_title", "authors", "year", "url",
    "identification_status", "confidence", "thesis_relevance", "notes",
]


@dataclass
class ExtractedPdf:
    pages: list[str]
    title: str
    author: str
    year: str
    candidate_source: str


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.splitlines()]
    out: list[str] = []
    blank = False
    for line in lines:
        if line.strip():
            out.append(line)
            blank = False
        elif not blank:
            out.append("")
            blank = True
    return "\n".join(out).strip()


def useful_word_count(text: str) -> int:
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-zΑ-Ωα-ωΆ-ώ0-9]{2,}", text))


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


def is_lfs_pointer(path: Path) -> bool:
    return path.read_bytes()[:200].startswith(LFS_PREFIX)


def git_commit(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def clean_metadata(value: object) -> str:
    text = normalize_text(str(value or ""))
    if text.casefold() in {"none", "unknown", "untitled", "anonymous"}:
        return ""
    return text[:500]


def first_content_title(pages: list[str], filename: str) -> str:
    weak = {"original", "document", "chapter", "pdf"}
    stem = re.sub(r"^[A-F0-9]{16}__", "", Path(filename).stem, flags=re.I)
    normalized_stem = re.sub(r"[_-]+", " ", stem).strip()
    if normalized_stem and normalized_stem.casefold() not in weak and not re.fullmatch(r"(?:0?\d+\s*)?chapter\s*\d+", normalized_stem, re.I):
        return normalized_stem
    if not pages:
        return normalized_stem
    for raw in pages[0].splitlines()[:80]:
        line = re.sub(r"\s+", " ", raw).strip(" -–—|\t")
        if not (5 <= len(line) <= 220):
            continue
        if re.fullmatch(r"\d+", line) or line.lower().startswith(("http://", "https://", "www.")):
            continue
        if useful_word_count(line) < 2:
            continue
        return line
    return normalized_stem


def extract_pdf(path: Path) -> ExtractedPdf:
    if PdfReader is None:
        raise RuntimeError("pypdf is required")
    if is_lfs_pointer(path):
        raise RuntimeError(f"Git LFS content is not checked out: {path}")
    reader = PdfReader(str(path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            pages.append(normalize_text(page.extract_text() or ""))
        except Exception as exc:  # pragma: no cover - damaged PDFs vary
            pages.append(f"[Text extraction failed: {type(exc).__name__}]")
    metadata = reader.metadata or {}
    title = clean_metadata(metadata.get("/Title"))
    author = clean_metadata(metadata.get("/Author"))
    creation = clean_metadata(metadata.get("/CreationDate"))
    year_match = re.search(r"(?:19|20)\d{2}", creation)
    year = year_match.group(0) if year_match else ""
    candidate_source = "pdf-metadata" if title else "first-page-or-filename"
    if not title:
        title = first_content_title(pages, path.name)
    if not year:
        probe = "\n".join(pages[:3])[:30000]
        match = re.search(r"\b(?:19|20)\d{2}\b", probe)
        year = match.group(0) if match else ""
    return ExtractedPdf(pages, title, author, year, candidate_source)


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if not sep:
            continue
        value = value.strip()
        try:
            result[key.strip()] = str(json.loads(value))
        except json.JSONDecodeError:
            result[key.strip()] = value.strip('"')
    return result


def source_id_from_original(path: Path) -> str:
    match = re.fullmatch(r"(SRC-[A-F0-9]{10})\.pdf", path.name, re.I)
    return match.group(1).upper() if match else ""


def source_covers_original(root: Path, pdf: Path) -> bool:
    source_id = source_id_from_original(pdf)
    if not source_id:
        return False
    source = root / "sources" / f"{source_id}.md"
    if not source.exists():
        return False
    text = source.read_text(encoding="utf-8", errors="replace")
    return useful_word_count(text) >= 120


def candidate_pdfs(root: Path) -> list[Path]:
    originals = root / "originals"
    result: list[Path] = []
    if not originals.exists():
        return result
    for pdf in sorted(originals.rglob("*.pdf")):
        if "unidentified" in pdf.parts or not source_covers_original(root, pdf):
            result.append(pdf)
    return result


def material_id(identity: str) -> str:
    return f"MAT-{identity[:10].upper()}"


def immutable_url(root: Path, path: Path, commit: str) -> str:
    rel = path.relative_to(root).as_posix()
    from urllib.parse import quote
    return (
        "https://github.com/MariosGiannakaras/ThesisBibliography/blob/"
        f"{commit}/{quote(rel, safe='/')}"
    )


def render_material(root: Path, pdf: Path, identity: str, extracted: ExtractedPdf, commit: str) -> str:
    mid = material_id(identity)
    rel = pdf.relative_to(root).as_posix()
    chars = sum(len(page) for page in extracted.pages)
    status = "full-text-extracted" if chars >= max(500, len(extracted.pages) * 100) else "partial-text-extracted"
    lines = [
        "---",
        f"material_id: {json.dumps(mid)}",
        f"original_path: {json.dumps(rel, ensure_ascii=False)}",
        f"original_sha256: {json.dumps(identity)}",
        f"original_url: {json.dumps(immutable_url(root, pdf, commit))}",
        f"linked_source_id: {json.dumps(source_id_from_original(pdf))}",
        f"citation_status: {json.dumps('not-citation-ready')}",
        f"identification_status: {json.dumps('pending-review')}",
        f"content_status: {json.dumps(status)}",
        f"page_count: {len(extracted.pages)}",
        f"text_characters: {chars}",
        "---",
        GENERATED_MARKER,
        "",
        f"# {extracted.title or pdf.stem}",
        "",
        "> Research material retained for drafting and discovery. It may be useful even without complete citation metadata.",
        "> The text below is an un-translated extraction. The original PDF and SHA-256 remain authoritative.",
        "",
        "## Technical identity",
        "",
        f"- **Material ID:** `{mid}`",
        f"- **Original file:** `{rel}`",
        f"- **SHA-256:** `{identity}`",
        f"- **Title candidate:** {extracted.title or 'unknown'}",
        f"- **Author candidate:** {extracted.author or 'unknown'}",
        f"- **Year candidate:** {extracted.year or 'unknown'}",
        f"- **Candidate source:** {extracted.candidate_source}",
        "- **Citation status:** not citation-ready; content remains available for writing and later identification",
        "",
        "## Full extracted text by page",
        "",
    ]
    for number, page in enumerate(extracted.pages, start=1):
        lines.extend([
            f"<!-- PDF_PAGE: {number} -->",
            f"### Page {number}",
            "",
            page or "[No readable text was extracted from this page.]",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build(root: Path) -> None:
    materials = root / "materials"
    inventory_path = root / "catalog" / "research-materials.csv"
    review_path = root / "catalog" / "research-material-review.csv"
    materials.mkdir(parents=True, exist_ok=True)
    commit = git_commit(root)
    existing_reviews = {row.get("material_id", ""): row for row in read_csv(review_path)}
    inventory: list[dict[str, str]] = []
    reviews: list[dict[str, str]] = []
    expected_files: set[str] = set()

    for pdf in candidate_pdfs(root):
        identity = file_identity(pdf)
        mid = material_id(identity)
        extracted = extract_pdf(pdf)
        target = materials / f"{mid}.md"
        target.write_text(render_material(root, pdf, identity, extracted, commit), encoding="utf-8")
        expected_files.add(target.name)
        chars = sum(len(page) for page in extracted.pages)
        status = "full-text-extracted" if chars >= max(500, len(extracted.pages) * 100) else "partial-text-extracted"
        inventory.append({
            "material_id": mid,
            "filename": pdf.name,
            "title_candidate": extracted.title,
            "author_candidate": extracted.author,
            "year_candidate": extracted.year,
            "candidate_source": extracted.candidate_source,
            "content_status": status,
            "page_count": str(len(extracted.pages)),
            "text_characters": str(chars),
            "sha256": identity,
            "original_path": pdf.relative_to(root).as_posix(),
            "original_url": immutable_url(root, pdf, commit),
            "linked_source_id": source_id_from_original(pdf),
        })
        review = existing_reviews.get(mid) or {
            "material_id": mid,
            "canonical_title": "",
            "authors": "",
            "year": "",
            "url": "",
            "identification_status": "pending",
            "confidence": "",
            "thesis_relevance": "unreviewed",
            "notes": "",
        }
        reviews.append({field: review.get(field, "") for field in REVIEW_FIELDS})

    for path in materials.glob("MAT-*.md"):
        if path.name not in expected_files and GENERATED_MARKER in path.read_text(encoding="utf-8", errors="replace"):
            path.unlink()

    inventory.sort(key=lambda row: row["material_id"])
    reviews.sort(key=lambda row: row["material_id"])
    write_csv(inventory_path, INVENTORY_FIELDS, inventory)
    write_csv(review_path, REVIEW_FIELDS, reviews)
    print(f"Built {len(inventory)} research materials.")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    inventory_path = root / "catalog" / "research-materials.csv"
    review_path = root / "catalog" / "research-material-review.csv"
    inventory = read_csv(inventory_path)
    reviews = read_csv(review_path)
    by_id = {row.get("material_id", ""): row for row in inventory}
    review_ids = {row.get("material_id", "") for row in reviews}
    if len(by_id) != len(inventory):
        errors.append("Duplicate material IDs in research-materials.csv")

    expected: dict[str, tuple[Path, str]] = {}
    for pdf in candidate_pdfs(root):
        identity = file_identity(pdf)
        expected[material_id(identity)] = (pdf, identity)
    if set(by_id) != set(expected):
        errors.append(
            "Research material inventory does not match uncovered originals: "
            f"missing={sorted(set(expected)-set(by_id))}, extra={sorted(set(by_id)-set(expected))}"
        )
    if review_ids != set(expected):
        errors.append(
            "Research material review registry does not match inventory: "
            f"missing={sorted(set(expected)-review_ids)}, extra={sorted(review_ids-set(expected))}"
        )

    for mid, (pdf, identity) in expected.items():
        row = by_id.get(mid, {})
        if row.get("sha256") != identity:
            errors.append(f"{mid}: SHA mismatch in inventory")
        if row.get("original_path") != pdf.relative_to(root).as_posix():
            errors.append(f"{mid}: original path mismatch")
        material = root / "materials" / f"{mid}.md"
        if not material.exists():
            errors.append(f"{mid}: missing extracted material Markdown")
            continue
        text = material.read_text(encoding="utf-8", errors="replace")
        meta = parse_front_matter(text)
        if GENERATED_MARKER not in text:
            errors.append(f"{mid}: missing generated material marker")
        if meta.get("original_sha256") != identity:
            errors.append(f"{mid}: Markdown SHA mismatch")
        if meta.get("original_path") != pdf.relative_to(root).as_posix():
            errors.append(f"{mid}: Markdown path mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("build", "validate"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "build":
        build(root)
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Research material coverage is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
