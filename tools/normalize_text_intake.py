#!/usr/bin/env python3
"""Normalize structured/textual intake while preserving original bytes.

Recognized JATS XML becomes canonical Markdown before normal source import.
Other textual artifacts remain accessible as research notes instead of being
silently discarded. Original non-PDF payloads are archived byte-for-byte under
``structured-originals/`` with content-derived ASCII-safe names.
"""
from __future__ import annotations

import csv
import hashlib
import re
import shutil
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_FIELDS = [
    "Stored path",
    "Original intake path",
    "Content SHA-256",
    "Media type",
    "Derived path",
]
AUXILIARY_SUFFIXES = {".txt", ".csv", ".json"}


@dataclass(frozen=True)
class IntakePaths:
    root: Path

    @property
    def incoming(self) -> Path:
        return self.root / "new-sources"

    @property
    def incoming_originals(self) -> Path:
        return self.root / "new-originals"

    @property
    def archive(self) -> Path:
        return self.root / "structured-originals"

    @property
    def index(self) -> Path:
        return self.archive / "index.csv"

    @property
    def notes(self) -> Path:
        return self.root / "research-notes" / "intake"


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


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def is_jats_text(text: str) -> bool:
    sample = text.lstrip("\ufeff\n\r\t ")[:12000]
    return "<article" in sample and "<article-title" in sample


def parse_xml(text: str) -> ET.Element:
    return ET.fromstring(text.lstrip("\ufeff"))


def child(element: ET.Element, name: str) -> ET.Element | None:
    return next((item for item in element if local_name(item) == name), None)


def descendants(element: ET.Element, name: str) -> list[ET.Element]:
    return [item for item in element.iter() if local_name(item) == name]


def render_section(section: ET.Element, depth: int = 2) -> list[str]:
    lines: list[str] = []
    heading = element_text(child(section, "title"))
    if heading:
        lines.extend([f"{'#' * min(depth, 6)} {heading}", ""])

    for item in section:
        name = local_name(item)
        if name == "title":
            continue
        if name == "sec":
            lines.extend(render_section(item, depth + 1))
        elif name == "p":
            text = element_text(item)
            if text:
                lines.extend([text, ""])
        elif name == "list":
            for list_item in descendants(item, "list-item"):
                text = element_text(list_item)
                if text:
                    lines.append(f"- {text}")
            if lines and lines[-1] != "":
                lines.append("")
        elif name in {"fig", "table-wrap", "boxed-text", "disp-quote", "statement"}:
            text = element_text(item)
            if text:
                lines.extend([text, ""])
    return lines


def jats_to_markdown(text: str) -> str:
    root = parse_xml(text)
    article_meta = next(iter(descendants(root, "article-meta")), None)
    if article_meta is None:
        raise RuntimeError("JATS article has no article-meta")

    title_nodes = descendants(article_meta, "article-title")
    title = element_text(title_nodes[0]) if title_nodes else "Untitled JATS article"

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
            if local_name(item) == "sec":
                lines.extend(render_section(item, 2))
            elif local_name(item) == "p":
                value = element_text(item)
                if value:
                    lines.extend([value, ""])

    references = [element_text(item) for item in descendants(root, "ref")]
    references = [value for value in references if value]
    if references:
        lines.extend(["## References", ""])
        lines.extend(f"{index}. {value}" for index, value in enumerate(references, start=1))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def load_index(paths: IntakePaths) -> list[dict[str, str]]:
    if not paths.index.exists():
        return []
    with paths.index.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != INDEX_FIELDS:
            raise RuntimeError("Unexpected structured-originals index schema")
        return [dict(row) for row in reader]


def write_index(rows: list[dict[str, str]], paths: IntakePaths) -> None:
    paths.archive.mkdir(parents=True, exist_ok=True)
    by_key = {(row["Stored path"], row["Original intake path"]): row for row in rows}
    ordered = sorted(by_key.values(), key=lambda row: (row["Stored path"], row["Original intake path"]))
    with paths.index.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INDEX_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ordered)


def archive_file(
    path: Path,
    original_label: str,
    derived_path: str,
    paths: IntakePaths,
) -> dict[str, str]:
    paths.archive.mkdir(parents=True, exist_ok=True)
    digest = sha256(path)
    suffix = path.suffix.casefold() or ".bin"
    target = paths.archive / f"ORIGINAL-{digest[:16].upper()}{suffix}"
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
        "Stored path": target.relative_to(paths.root).as_posix(),
        "Original intake path": original_label,
        "Content SHA-256": digest,
        "Media type": media_type,
        "Derived path": derived_path,
    }


def note_from_text(
    path: Path,
    original_label: str,
    paths: IntakePaths,
) -> tuple[Path, dict[str, str]]:
    digest = sha256(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    paths.notes.mkdir(parents=True, exist_ok=True)
    target = paths.notes / f"NOTE-{digest[:16].upper()}.md"
    fence = "````" if "```" in raw else "```"
    language = "json" if path.suffix.casefold() == ".json" else "text"
    note = (
        "# Preserved textual research material\n\n"
        f"- Original intake path: `{original_label}`\n"
        f"- Content SHA-256: `{digest}`\n"
        "- Citation status: not citation-ready; preserved for research and writing access\n\n"
        f"{fence}{language}\n{raw.rstrip()}\n{fence}\n"
    )
    if target.exists() and target.read_text(encoding="utf-8") != note:
        raise RuntimeError(f"Research-note collision: {target}")
    target.write_text(note, encoding="utf-8")
    row = archive_file(
        path,
        original_label,
        target.relative_to(paths.root).as_posix(),
        paths,
    )
    return target, row


def normalize(root: Path = ROOT) -> dict[str, int]:
    paths = IntakePaths(root.resolve())
    paths.incoming.mkdir(parents=True, exist_ok=True)
    paths.incoming_originals.mkdir(parents=True, exist_ok=True)
    rows = load_index(paths)
    counts = {"jats_markdown": 0, "jats_xml": 0, "notes": 0, "archived_originals": 0}

    # A file can contain JATS even if someone changed only its suffix to .md.
    for path in sorted(paths.incoming.rglob("*.md")):
        if path.name == "README.md" or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if is_jats_text(text):
            path.write_text(jats_to_markdown(text), encoding="utf-8")
            counts["jats_markdown"] += 1

    # Direct XML source intake: derive Markdown and preserve the exact XML bytes.
    for path in sorted(paths.incoming.rglob("*.xml")):
        if not path.is_file():
            continue
        original_label = f"new-sources/{path.relative_to(paths.incoming).as_posix()}"
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if is_jats_text(text):
            target = path.with_suffix(".md")
            markdown = jats_to_markdown(text)
            if target.exists() and target.read_text(encoding="utf-8-sig", errors="replace") != markdown:
                raise RuntimeError(f"JATS Markdown target already exists with different content: {target}")
            target.write_text(markdown, encoding="utf-8")
            rows.append(
                archive_file(
                    path,
                    original_label,
                    target.relative_to(paths.root).as_posix(),
                    paths,
                )
            )
            counts["jats_xml"] += 1
            counts["archived_originals"] += 1
        else:
            _, row = note_from_text(path, original_label, paths)
            rows.append(row)
            counts["notes"] += 1
            counts["archived_originals"] += 1

    # TXT/CSV/JSON are preserved as writing material rather than ignored helpers.
    for path in sorted(
        item for item in paths.incoming.rglob("*")
        if item.is_file() and item.suffix.casefold() in AUXILIARY_SUFFIXES
    ):
        original_label = f"new-sources/{path.relative_to(paths.incoming).as_posix()}"
        _, row = note_from_text(path, original_label, paths)
        rows.append(row)
        counts["notes"] += 1
        counts["archived_originals"] += 1

    # XML uploaded as an original can itself generate a source if it is JATS.
    for path in sorted(paths.incoming_originals.rglob("*.xml")):
        if not path.is_file():
            continue
        original_label = f"new-originals/{path.relative_to(paths.incoming_originals).as_posix()}"
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if is_jats_text(text):
            target = paths.incoming / f"{path.stem}.md"
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
            rows.append(
                archive_file(
                    path,
                    original_label,
                    target.relative_to(paths.root).as_posix(),
                    paths,
                )
            )
            counts["jats_xml"] += 1
            counts["archived_originals"] += 1
        else:
            _, row = note_from_text(path, original_label, paths)
            rows.append(row)
            counts["notes"] += 1
            counts["archived_originals"] += 1

    write_index(rows, paths)
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
