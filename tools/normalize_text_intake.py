#!/usr/bin/env python3
"""Normalize structured/textual intake while preserving original bytes.

JATS XML is converted to canonical Markdown before the normal source importer runs.
Structured/text artifacts that are not bibliography sources are preserved as
research notes instead of being silently discarded. Original non-PDF files are
archived under ``structured-originals/`` with content-derived names.
"""
from __future__ import annotations

import csv
import hashlib
import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "new-sources"
INCOMING_ORIGINALS = ROOT / "new-originals"
ARCHIVE = ROOT / "structured-originals"
INDEX = ARCHIVE / "index.csv"
NOTES = ROOT / "research-notes" / "intake"
INDEX_FIELDS = [
    "Stored path",
    "Original intake path",
    "Content SHA-256",
    "Media type",
    "Derived path",
]
AUXILIARY_SUFFIXES = {".txt", ".csv", ".json"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_text(value: str) -> str:
    return " ".join((value or "").split())


def element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return clean_text("".join(element.itertext()))


def is_jats_text(text: str) -> bool:
    sample = text.lstrip("\ufeff\n\r\t ")[:12000]
    return "<article" in sample and "<article-title" in sample


def parse_xml(text: str) -> ET.Element:
    return ET.fromstring(text.lstrip("\ufeff"))


def child(element: ET.Element, name: str) -> ET.Element | None:
    for item in element:
        if item.tag.rsplit("}", 1)[-1] == name:
            return item
    return None


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [item for item in element if item.tag.rsplit("}", 1)[-1] == name]


def descendants(element: ET.Element, name: str) -> list[ET.Element]:
    return [item for item in element.iter() if item.tag.rsplit("}", 1)[-1] == name]


def render_section(section: ET.Element, depth: int = 2) -> list[str]:
    lines: list[str] = []
    title = child(section, "title")
    heading = element_text(title)
    if heading:
        lines.extend([f"{'#' * min(depth, 6)} {heading}", ""])

    for item in section:
        name = item.tag.rsplit("}", 1)[-1]
        if name == "title":
            continue
        if name == "sec":
            lines.extend(render_section(item, depth + 1))
            continue
        if name == "p":
            text = element_text(item)
            if text:
                lines.extend([text, ""])
            continue
        if name == "list":
            for list_item in descendants(item, "list-item"):
                text = element_text(list_item)
                if text:
                    lines.append(f"- {text}")
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if name in {"fig", "table-wrap", "boxed-text", "disp-quote", "statement"}:
            text = element_text(item)
            if text:
                lines.extend([text, ""])
    return lines


def jats_to_markdown(text: str) -> str:
    root = parse_xml(text)
    article_meta = next(iter(descendants(root, "article-meta")), None)
    if article_meta is None:
        raise RuntimeError("JATS article has no article-meta")

    titles = descendants(article_meta, "article-title")
    title = element_text(titles[0]) if titles else "Untitled JATS article"

    authors: list[str] = []
    for contrib in descendants(article_meta, "contrib"):
        if contrib.attrib.get("contrib-type") != "author":
            continue
        name = child(contrib, "name")
        if name is None:
            continue
        given = element_text(child(name, "given-names"))
        surname = element_text(child(name, "surname"))
        full = clean_text(f"{given} {surname}")
        if full:
            authors.append(full)

    doi = ""
    for article_id in descendants(article_meta, "article-id"):
        if article_id.attrib.get("pub-id-type") == "doi":
            doi = element_text(article_id)
            break

    year = ""
    for pub_date in descendants(article_meta, "pub-date"):
        value = element_text(child(pub_date, "year"))
        if re.fullmatch(r"\d{4}", value):
            year = value
            break

    lines = [f"# {title}", ""]
    if doi:
        lines.extend([f"> Source: https://doi.org/{doi}", ""])
    if authors:
        lines.extend([f"Authors: {'; '.join(authors)}", ""])
    if year:
        lines.extend([f"Year: {year}", ""])
    lines.extend(["Format: JATS XML normalized to Markdown without translation.", ""])

    abstracts = descendants(article_meta, "abstract")
    if abstracts:
        abstract_text = element_text(abstracts[0])
        if abstract_text:
            lines.extend(["## Abstract", "", abstract_text, ""])

    body = next(iter(descendants(root, "body")), None)
    if body is not None:
        for item in body:
            name = item.tag.rsplit("}", 1)[-1]
            if name == "sec":
                lines.extend(render_section(item, 2))
            elif name == "p":
                value = element_text(item)
                if value:
                    lines.extend([value, ""])

    refs = descendants(root, "ref")
    reference_lines = [element_text(item) for item in refs]
    reference_lines = [value for value in reference_lines if value]
    if reference_lines:
        lines.extend(["## References", ""])
        lines.extend(f"{index}. {value}" for index, value in enumerate(reference_lines, start=1))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def load_index(path: Path = INDEX) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != INDEX_FIELDS:
            raise RuntimeError("Unexpected structured-originals index schema")
        return [dict(row) for row in reader]


def write_index(rows: list[dict[str, str]], path: Path = INDEX) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_key = {(row["Stored path"], row["Original intake path"]): row for row in rows}
    ordered = sorted(by_key.values(), key=lambda row: (row["Stored path"], row["Original intake path"]))
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INDEX_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ordered)


def archive_file(path: Path, original_label: str, derived_path: str = "") -> dict[str, str]:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    digest = sha256(path)
    suffix = path.suffix.casefold() or ".bin"
    target = ARCHIVE / f"ORIGINAL-{digest[:16].upper()}{suffix}"
    if target.exists():
        if sha256(target) != digest:
            raise RuntimeError(f"Structured-original archive collision: {target}")
        path.unlink()
    else:
        shutil.move(str(path), target)
    media_type = {
        ".xml": "application/xml",
        ".txt": "text/plain",
        ".csv": "text/csv",
        ".json": "application/json",
        ".md": "text/markdown",
    }.get(suffix, "application/octet-stream")
    return {
        "Stored path": target.relative_to(ROOT).as_posix(),
        "Original intake path": original_label,
        "Content SHA-256": digest,
        "Media type": media_type,
        "Derived path": derived_path,
    }


def note_from_text(path: Path, original_label: str) -> tuple[Path, dict[str, str]]:
    digest = sha256(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    NOTES.mkdir(parents=True, exist_ok=True)
    target = NOTES / f"NOTE-{digest[:16].upper()}.md"
    fence = "json" if path.suffix.casefold() == ".json" else "text"
    note = (
        "# Preserved textual research material\n\n"
        f"- Original intake path: `{original_label}`\n"
        f"- Content SHA-256: `{digest}`\n"
        "- Citation status: not citation-ready; preserved for research and writing access\n\n"
        f"```{fence}\n{raw.rstrip()}\n```\n"
    )
    if target.exists() and target.read_text(encoding="utf-8") != note:
        raise RuntimeError(f"Research-note collision: {target}")
    target.write_text(note, encoding="utf-8")
    row = archive_file(path, original_label, target.relative_to(ROOT).as_posix())
    return target, row


def normalize(root: Path = ROOT) -> dict[str, int]:
    global INCOMING, INCOMING_ORIGINALS, ARCHIVE, INDEX, NOTES
    if root != ROOT:
        INCOMING = root / "new-sources"
        INCOMING_ORIGINALS = root / "new-originals"
        ARCHIVE = root / "structured-originals"
        INDEX = ARCHIVE / "index.csv"
        NOTES = root / "research-notes" / "intake"

    rows = load_index(INDEX)
    counts = {"jats_markdown": 0, "jats_xml": 0, "notes": 0, "archived_originals": 0}

    INCOMING.mkdir(parents=True, exist_ok=True)
    INCOMING_ORIGINALS.mkdir(parents=True, exist_ok=True)

    # Normalize raw JATS that was saved with a .md suffix.
    for path in sorted(INCOMING.rglob("*.md")):
        if path.name == "README.md" or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if is_jats_text(text):
            path.write_text(jats_to_markdown(text), encoding="utf-8")
            counts["jats_markdown"] += 1

    # Direct XML source intake: derive Markdown, archive original bytes.
    for path in sorted(INCOMING.rglob("*.xml")):
        if not path.is_file():
            continue
        original_label = f"new-sources/{path.relative_to(INCOMING).as_posix()}"
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if is_jats_text(text):
            target = path.with_suffix(".md")
            markdown = jats_to_markdown(text)
            if target.exists() and target.read_text(encoding="utf-8-sig", errors="replace") != markdown:
                raise RuntimeError(f"JATS Markdown target already exists with different content: {target}")
            target.write_text(markdown, encoding="utf-8")
            row = archive_file(path, original_label, target.relative_to(root).as_posix())
            rows.append(row)
            counts["jats_xml"] += 1
            counts["archived_originals"] += 1
        else:
            _, row = note_from_text(path, original_label)
            rows.append(row)
            counts["notes"] += 1
            counts["archived_originals"] += 1

    # TXT/CSV/JSON are useful research material unless promoted through source analysis.
    for path in sorted(
        item for item in INCOMING.rglob("*")
        if item.is_file() and item.suffix.casefold() in AUXILIARY_SUFFIXES
    ):
        original_label = f"new-sources/{path.relative_to(INCOMING).as_posix()}"
        _, row = note_from_text(path, original_label)
        rows.append(row)
        counts["notes"] += 1
        counts["archived_originals"] += 1

    # Structured originals may themselves be sufficient to derive a source.
    for path in sorted(INCOMING_ORIGINALS.rglob("*.xml")):
        if not path.is_file():
            continue
        original_label = f"new-originals/{path.relative_to(INCOMING_ORIGINALS).as_posix()}"
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        derived = ""
        if is_jats_text(text):
            target = INCOMING / f"{path.stem}.md"
            markdown = jats_to_markdown(text)
            if target.exists():
                existing = target.read_text(encoding="utf-8-sig", errors="replace")
                if is_jats_text(existing):
                    target.write_text(markdown, encoding="utf-8")
                    counts["jats_markdown"] += 1
                elif existing != markdown:
                    raise RuntimeError(f"Derived JATS Markdown conflicts with existing intake: {target}")
            else:
                target.write_text(markdown, encoding="utf-8")
            derived = target.relative_to(root).as_posix()
            counts["jats_xml"] += 1
        else:
            note_target, _ = note_from_text(path, original_label)
            # note_from_text already archives and removes path.
            rows = load_index(INDEX) + rows
            derived = note_target.relative_to(root).as_posix()
            counts["notes"] += 1
            counts["archived_originals"] += 1
            continue
        row = archive_file(path, original_label, derived)
        rows.append(row)
        counts["archived_originals"] += 1

    write_index(rows, INDEX)
    return counts


def main() -> int:
    counts = normalize()
    print(
        "Structured text intake normalized: "
        f"raw-JATS-md={counts['jats_markdown']}, "
        f"JATS-xml={counts['jats_xml']}, "
        f"research-notes={counts['notes']}, "
        f"archived-originals={counts['archived_originals']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
