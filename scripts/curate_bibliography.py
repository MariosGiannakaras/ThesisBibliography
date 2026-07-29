#!/usr/bin/env python3
"""Normalize and index the temporary ThesisBibliography corpus.

The script preserves source text byte-for-byte while moving grouped Markdown files
into a single flat archive. It generates deterministic catalogs, quality reports,
duplicate groups, candidate excerpts, and reference-screening queues.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "sources" / "raw-md"
REPORT_ROOT = ROOT / "sources" / "group-reports"
CATALOG_ROOT = ROOT / "catalog"
EXCERPT_SOURCE_ROOT = ROOT / "excerpts" / "by-source"
EXCERPT_TOPIC_ROOT = ROOT / "excerpts" / "by-topic"
QUEUE_ROOT = ROOT / "queues"
ARCHIVE_ROOT = ROOT / "archive"
INCOMING_ROOT = ROOT / "incoming"

GROUP_RE = re.compile(r"^Group(?P<group>\d+)$", re.IGNORECASE)
SOURCE_DIR_RE = re.compile(r"^Group(?P<group>\d+)Files$", re.IGNORECASE)
NUMBERED_NAME_RE = re.compile(r"^(?P<number>\d+)[-_ ]+(?P<title>.+)$")
URL_RE = re.compile(r"https?://[^\s<>\]\[\)\(\"']+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arxiv:|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")
SOURCE_LINE_RE = re.compile(r"^\s*>?\s*Source\s*:\s*(https?://\S+)\s*$", re.IGNORECASE | re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
AUTHOR_LABEL_RE = re.compile(
    r"^(?:authors?|author\(s\)|συγγραφ(?:έας|είς)|creator)\s*[:：]\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)

TOPIC_RULES: dict[str, tuple[str, ...]] = {
    "robust-rl": ("robust reinforcement", "robust mdp", "distributionally robust", "adversarial reinforcement"),
    "resilience-recovery": ("resilien", "recovery time", "recover from", "adaptation speed", "mean time to"),
    "nonstationary-rl": ("non-stationary", "nonstationary", "changing dynamics", "change point", "environmental change"),
    "safe-rl": ("safe reinforcement", "constrained mdp", "safety constraint", "safety gridworld"),
    "uncertainty": ("uncertainty", "uncertain environment", "epistemic", "aleatoric", "ambiguity set"),
    "gridworld": ("gridworld", "grid world", "cliffwalking", "minigrid"),
    "rl-foundations": ("reinforcement learning", "q-learning", "sarsa", "bellman", "policy iteration", "value iteration"),
    "evaluation-statistics": ("confidence interval", "effect size", "statistical", "multiple seeds", "reliable evaluation"),
    "multi-agent": ("multi-agent", "multiagent", "markov game", "marl"),
    "ai-safety-alignment": ("ai safety", "alignment", "reward hacking", "specification gaming"),
    "agentic-ai": ("agentic ai", "llm agent", "autonomous agent"),
    "gridworld-implementation": ("github", "gymnasium", "environment creator", "custom environment"),
    "thesis": ("master thesis", "doctoral thesis", "phd thesis", "dissertation", "διπλωματική", "διατριβή"),
}

LOW_VALUE_DOMAINS = {
    "wikipedia.org",
    "medium.com",
    "towardsdatascience.com",
    "geeksforgeeks.org",
    "marktechpost.com",
    "reddit.com",
    "oceanofpdf.com",
    "ilide.info",
}

ACADEMIC_MARKERS = (
    "abstract",
    "references",
    "bibliography",
    "doi",
    "arxiv",
    "methodology",
    "experiments",
    "results",
    "conclusion",
)
SCRAPE_MARKERS = (
    "skip to content",
    "cookie settings",
    "accept all cookies",
    "show more",
    "back skip navigation",
    "sign in",
    "privacy policy",
)
EXCERPT_HEADINGS = (
    "abstract",
    "summary",
    "conclusion",
    "conclusions",
    "results",
    "discussion",
    "limitations",
    "method",
    "methodology",
    "experimental setup",
    "evaluation",
    "περίληψη",
    "συμπεράσματα",
    "αποτελέσματα",
    "μεθοδολογία",
    "περιορισμοί",
)


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slugify(value: str, max_length: int = 90) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return (value[:max_length].rstrip("-") or "untitled")


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def clean_url(url: str) -> str:
    return url.rstrip(".,;:)>]}\"")


def domain_of(url: str | None) -> str:
    if not url:
        return ""
    return urlparse(url).netloc.lower().removeprefix("www.")


def canonicalize_url(url: str | None) -> str | None:
    if not url:
        return None
    url = clean_url(url)
    parsed = urlparse(url)
    domain = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.rstrip("/")
    if domain == "arxiv.org":
        match = re.search(r"/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", path)
        if match:
            return f"https://arxiv.org/abs/{match.group(1)}"
    if domain == "doi.org":
        return f"https://doi.org/{path.lstrip('/').lower()}"
    if domain == "youtube.com" and parsed.query:
        video = re.search(r"(?:^|&)v=([^&]+)", parsed.query)
        if video:
            return f"https://www.youtube.com/watch?v={video.group(1)}"
    if domain == "youtu.be":
        return f"https://www.youtube.com/watch?v={path.lstrip('/')}"
    return f"{parsed.scheme or 'https'}://{domain}{path}" if domain else url


def first_source_url(text: str) -> str | None:
    match = SOURCE_LINE_RE.search(text)
    if match:
        return clean_url(match.group(1))
    urls = [clean_url(item) for item in URL_RE.findall(text[:5000])]
    return urls[0] if urls else None


def title_from_content(text: str, fallback: str) -> str:
    for _marks, heading in HEADING_RE.findall(text[:8000]):
        candidate = re.sub(r"[*_`]+", "", heading).strip()
        if 5 <= len(candidate) <= 240 and not candidate.lower().startswith(("source", "contents", "references")):
            return candidate
    for line in text[:5000].splitlines():
        candidate = re.sub(r"^[>\s#*`_-]+", "", line).strip()
        if candidate.lower().startswith("source:"):
            continue
        if 8 <= len(candidate) <= 240 and len(candidate.split()) >= 3:
            return candidate
    return fallback


def authors_from_content(text: str) -> str | None:
    match = AUTHOR_LABEL_RE.search(text[:12000])
    if match:
        value = re.sub(r"\s+", " ", match.group(1)).strip(" -*")
        return value[:500] or None
    return None


def year_from_content(text: str, filename: str) -> str | None:
    matches = YEAR_RE.findall(f"{filename}\n{text[:6000]}")
    plausible = [int(value) for value in matches if 1900 <= int(value) <= 2026]
    return str(plausible[0]) if plausible else None


def classify_type(title: str, text: str, url: str | None, filename: str) -> str:
    lower = f"{title} {filename} {text[:4000]}".lower()
    domain = domain_of(url)
    if "youtube.com" in domain or "youtu.be" in domain:
        return "video-transcript"
    if "github.com" in domain or " - github" in lower:
        return "software-repository"
    if any(token in lower for token in ("master thesis", "phd thesis", "doctoral thesis", "dissertation", "διπλωματική", "διατριβή")):
        return "thesis-dissertation"
    if any(token in lower for token in ("book", "textbook", "second edition", "ebook")):
        return "book"
    if any(token in lower for token in ("survey", "systematic review", "review of")):
        return "survey-review"
    if domain in {"arxiv.org", "openreview.net", "proceedings.mlr.press", "papers.nips.cc", "ieeexplore.ieee.org", "dl.acm.org"}:
        return "research-paper"
    if "doi.org" in domain or DOI_RE.search(text[:8000]):
        return "research-paper"
    if "documentation" in lower or domain.endswith("farama.org") or "docs." in domain:
        return "technical-documentation"
    if "report" in lower or "whitepaper" in lower or "framework" in lower:
        return "report-whitepaper"
    return "web-article-or-unknown"


def content_quality(text: str, url: str | None) -> tuple[str, list[str]]:
    words = len(text.split())
    lower = text.lower()
    issues: list[str] = []
    if not text.strip():
        return "empty", ["empty-file"]
    non_source_lines = [line for line in text.splitlines() if line.strip() and not SOURCE_LINE_RE.match(line)]
    if not non_source_lines:
        return "source-link-only", ["source-link-only"]
    if words < 40:
        return "sparse", ["insufficient-content"]
    if domain_of(url) in {"youtube.com", "youtu.be"}:
        if words < 200:
            issues.append("incomplete-video-transcript")
        return "video-transcript", issues
    scrape_hits = sum(marker in lower[:10000] for marker in SCRAPE_MARKERS)
    academic_hits = sum(marker in lower for marker in ACADEMIC_MARKERS)
    if scrape_hits >= 2 and academic_hits < 2:
        return "noisy-web-scrape", ["web-scrape-noise"]
    if words < 150:
        return "metadata-only", ["metadata-only-or-incomplete"]
    if academic_hits >= 3 and words >= 1000:
        return "full-text-candidate", issues
    if "abstract" in lower and words >= 150:
        return "abstract-or-metadata", issues
    return "usable-general-text", issues


def infer_topics(title: str, text: str, url: str | None) -> list[str]:
    haystack = f"{title}\n{text[:25000]}\n{url or ''}".lower()
    topics = [topic for topic, keywords in TOPIC_RULES.items() if any(keyword in haystack for keyword in keywords)]
    return sorted(set(topics)) or ["uncategorized"]


def relevance(topics: list[str], title: str, url: str | None) -> tuple[str, list[str]]:
    domain = domain_of(url)
    lower_title = title.lower()
    primary = {"robust-rl", "resilience-recovery", "nonstationary-rl", "gridworld"}
    supporting = {"safe-rl", "uncertainty", "rl-foundations", "evaluation-statistics", "gridworld-implementation", "thesis"}
    if primary.intersection(topics):
        return "primary", []
    if supporting.intersection(topics):
        return "supporting", []
    reasons: list[str] = []
    if any(domain == item or domain.endswith(f".{item}") for item in LOW_VALUE_DOMAINS):
        reasons.append("low-authority-domain")
    if any(term in lower_title for term in ("millionaire", "marketing", "finance agent", "operator mastery", "playbook for 2025")):
        reasons.append("commercial-or-off-topic")
    if "agentic-ai" in topics and not ({"rl-foundations", "uncertainty", "ai-safety-alignment"} & set(topics)):
        reasons.append("agentic-ai-without-rl-link")
    return ("exclude-candidate", reasons) if reasons else ("peripheral", [])


def extract_identifiers(text: str, source_url: str | None) -> tuple[list[str], list[str]]:
    combined = f"{source_url or ''}\n{text}"
    dois = sorted({item.rstrip(".,;)").lower() for item in DOI_RE.findall(combined)})
    arxiv_ids = sorted(set(ARXIV_RE.findall(combined)))
    return dois, arxiv_ids


def group_and_number(path: Path) -> tuple[int, int | None, str]:
    relative = path.relative_to(ROOT)
    group_match = GROUP_RE.match(relative.parts[0])
    if not group_match:
        raise ValueError(f"Not a grouped source: {relative}")
    group = int(group_match.group("group"))
    number_match = NUMBERED_NAME_RE.match(path.stem)
    if number_match:
        return group, int(number_match.group("number")), number_match.group("title")
    return group, None, path.stem


def source_id(group: int, number: int | None, checksum: str) -> str:
    return f"SRC-G{group:02d}-{number:04d}" if number is not None else f"SRC-G{group:02d}-{checksum[:8].upper()}"


def source_paths() -> list[Path]:
    paths: list[Path] = []
    for group_dir in ROOT.iterdir():
        if not group_dir.is_dir() or not GROUP_RE.match(group_dir.name):
            continue
        for child in group_dir.iterdir():
            if child.is_dir() and SOURCE_DIR_RE.match(child.name):
                paths.extend(path for path in child.rglob("*") if path.is_file())
    return sorted(paths, key=lambda path: path.as_posix().lower())


def companion_paths() -> list[Path]:
    paths: list[Path] = []
    for group_dir in ROOT.iterdir():
        if not group_dir.is_dir() or not GROUP_RE.match(group_dir.name):
            continue
        for path in group_dir.rglob("*"):
            if not path.is_file():
                continue
            if any(SOURCE_DIR_RE.match(part) for part in path.relative_to(group_dir).parts[:-1]):
                continue
            paths.append(path)
    return sorted(paths, key=lambda path: path.as_posix().lower())


def extract_section_candidates(text: str) -> list[dict[str, object]]:
    lines = text.splitlines()
    candidates: list[dict[str, object]] = []
    headings: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.append((index, match.group(1).strip()))
    for position, (index, heading) in enumerate(headings):
        if not any(label in heading.lower() for label in EXCERPT_HEADINGS):
            continue
        end = headings[position + 1][0] if position + 1 < len(headings) else min(len(lines), index + 40)
        paragraph_lines: list[str] = []
        for line in lines[index + 1 : end]:
            stripped = line.strip()
            if not stripped or stripped.startswith(("#", "```", "|")):
                if paragraph_lines:
                    break
                continue
            paragraph_lines.append(stripped)
            if sum(len(item) for item in paragraph_lines) >= 700:
                break
        passage = " ".join(paragraph_lines)
        if len(passage) >= 80:
            candidates.append({"heading": heading, "start_line": index + 2, "text": passage[:900].rstrip()})
        if len(candidates) >= 5:
            break
    return candidates


def extract_reference_candidates(text: str, own_url: str | None) -> list[str]:
    lower = text.lower()
    starts = [lower.rfind(item) for item in ("\n# references", "\n## references", "\n# bibliography", "\n## bibliography", "\n# βιβλιογραφ")]
    start = max(starts)
    region = text[start:] if start >= 0 else text
    identifiers: set[str] = set()
    own_canonical = canonicalize_url(own_url)
    for url in URL_RE.findall(region):
        canonical = canonicalize_url(clean_url(url))
        if canonical and canonical != own_canonical:
            identifiers.add(canonical)
    for doi in DOI_RE.findall(region):
        identifiers.add(f"https://doi.org/{doi.rstrip('.,;)').lower()}")
    for arxiv_id in ARXIV_RE.findall(region):
        identifiers.add(f"https://arxiv.org/abs/{arxiv_id}")
    return sorted(identifiers)


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            normalized = {key: "; ".join(str(item) for item in value) if isinstance(value, list) else value for key, value in row.items()}
            writer.writerow(normalized)


def report_table(title: str, rows: list[dict[str, object]], columns: list[tuple[str, str]], intro: str) -> str:
    lines = [f"# {title}", "", intro, ""]
    if not rows:
        return "\n".join(lines + ["No entries."]) + "\n"
    lines.append("| " + " | ".join(label for _key, label in columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        cells: list[str] = []
        for key, _label in columns:
            value = row.get(key, "")
            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)
            cells.append(str(value or "").replace("|", "\\|").replace("\n", " ")[:300])
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    paths = source_paths()
    companions = companion_paths()
    if not paths:
        print("No grouped source files found; nothing to normalize.")
        return 0

    for directory in (SOURCE_ROOT, REPORT_ROOT, CATALOG_ROOT, EXCERPT_SOURCE_ROOT, EXCERPT_TOPIC_ROOT, QUEUE_ROOT, ARCHIVE_ROOT, INCOMING_ROOT):
        directory.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, object]] = []
    path_map: list[dict[str, object]] = []
    content_groups: dict[str, list[str]] = defaultdict(list)
    url_groups: dict[str, list[str]] = defaultdict(list)
    title_groups: dict[str, list[str]] = defaultdict(list)
    reference_map: dict[str, set[str]] = defaultdict(set)
    topic_sources: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for old_path in paths:
        data = old_path.read_bytes()
        checksum = sha256_bytes(data)
        text = data.decode("utf-8", errors="replace")
        group, number, fallback_title = group_and_number(old_path)
        fallback_title = fallback_title.replace("_", " ").strip()
        title = title_from_content(text, fallback_title)
        source_url = first_source_url(text)
        canonical_url = canonicalize_url(source_url)
        authors = authors_from_content(text)
        year = year_from_content(text, old_path.name)
        source_type = classify_type(title, text, source_url, old_path.name)
        quality, quality_issues = content_quality(text, source_url)
        topics = infer_topics(title, text, source_url)
        relevance_label, relevance_reasons = relevance(topics, title, source_url)
        dois, arxiv_ids = extract_identifiers(text, source_url)
        sid = source_id(group, number, checksum)
        filename = f"{sid.lower()}__{slugify(title)}.md"
        new_path = SOURCE_ROOT / filename
        counter = 2
        while new_path.exists() and new_path.read_bytes() != data:
            new_path = SOURCE_ROOT / f"{sid.lower()}__{slugify(title)}__{counter}.md"
            counter += 1
        if not new_path.exists():
            new_path.write_bytes(data)
        original_path = old_path.relative_to(ROOT).as_posix()
        old_path.unlink()

        issue_reasons = list(quality_issues)
        if not source_url:
            issue_reasons.append("missing-source-url")
        if not authors:
            issue_reasons.append("missing-authors")
        if not year:
            issue_reasons.append("missing-year")
        if title == fallback_title and (fallback_title.startswith("http") or ".pdf" in fallback_title.lower()):
            issue_reasons.append("opaque-or-unverified-title")
        if "�" in text:
            issue_reasons.append("encoding-artifacts")

        record: dict[str, object] = {
            "source_id": sid,
            "group": f"Group{group}",
            "original_path": original_path,
            "normalized_path": new_path.relative_to(ROOT).as_posix(),
            "title": title,
            "authors": authors or "",
            "year": year or "",
            "source_url": source_url or "",
            "canonical_url": canonical_url or "",
            "doi": dois[0] if dois else "",
            "arxiv_id": arxiv_ids[0] if arxiv_ids else "",
            "source_type": source_type,
            "topics": topics,
            "relevance": relevance_label,
            "content_quality": quality,
            "metadata_status": "needs-verification" if issue_reasons else "parsed",
            "verification_status": "unverified",
            "duplicate_group": "",
            "reference_extraction_status": "screened-automatically",
            "word_count": len(text.split()),
            "line_count": len(text.splitlines()),
            "sha256": checksum,
            "issues": sorted(set(issue_reasons + relevance_reasons)),
        }
        records.append(record)
        path_map.append({"source_id": sid, "original_path": original_path, "normalized_path": record["normalized_path"], "sha256": checksum})
        content_groups[checksum].append(sid)
        if canonical_url:
            url_groups[canonical_url].append(sid)
        normalized_title = normalize_title(title)
        if normalized_title:
            title_groups[normalized_title].append(sid)
        for topic in topics:
            topic_sources[topic].append((sid, title, record["normalized_path"]))
        for candidate in extract_reference_candidates(text, source_url):
            reference_map[candidate].add(sid)

        excerpts = extract_section_candidates(text)
        if excerpts and relevance_label in {"primary", "supporting"}:
            excerpt_lines = [
                f"# Candidate Excerpts — {title}",
                "",
                f"- Source ID: `{sid}`",
                f"- Source file: `{record['normalized_path']}`",
                "- Status: machine-extracted candidates; verify against the source before citation.",
                "",
            ]
            for excerpt in excerpts:
                excerpt_lines.extend([f"## {excerpt['heading']}", "", f"Source line: approximately {excerpt['start_line']}", "", f"> {excerpt['text']}", ""])
            (EXCERPT_SOURCE_ROOT / f"{sid.lower()}__candidate-excerpts.md").write_text("\n".join(excerpt_lines), encoding="utf-8")

    for path in companions:
        group_match = GROUP_RE.match(path.relative_to(ROOT).parts[0])
        group = int(group_match.group("group")) if group_match else 0
        kind = "source-table" if path.suffix.lower() == ".csv" else "audit-report"
        target = REPORT_ROOT / f"group-{group:02d}__notebooklm-{kind}{path.suffix.lower()}"
        if target.exists():
            target.unlink()
        shutil.move(path.as_posix(), target.as_posix())

    for group_dir in sorted(ROOT.glob("Group*"), reverse=True):
        if group_dir.is_dir():
            for child in sorted(group_dir.rglob("*"), reverse=True):
                if child.is_dir():
                    try:
                        child.rmdir()
                    except OSError:
                        pass
            try:
                group_dir.rmdir()
            except OSError:
                pass

    record_by_id = {str(record["source_id"]): record for record in records}
    duplicate_sets: list[tuple[str, str, list[str]]] = []
    seen_duplicate_members: set[tuple[str, ...]] = set()
    for mechanism, groups in (("exact-content", content_groups), ("canonical-url", url_groups), ("normalized-title", title_groups)):
        for _key, members in groups.items():
            unique_members = sorted(set(members))
            if len(unique_members) < 2:
                continue
            signature = tuple(unique_members)
            if signature in seen_duplicate_members:
                continue
            seen_duplicate_members.add(signature)
            group_id = f"DUP-{len(duplicate_sets) + 1:04d}"
            duplicate_sets.append((group_id, mechanism, unique_members))
            for member in unique_members:
                existing = str(record_by_id[member].get("duplicate_group") or "")
                record_by_id[member]["duplicate_group"] = ";".join(filter(None, (existing, group_id)))

    records.sort(key=lambda row: str(row["source_id"]))
    fields = ["source_id", "group", "title", "authors", "year", "source_type", "relevance", "topics", "source_url", "canonical_url", "doi", "arxiv_id", "content_quality", "metadata_status", "verification_status", "duplicate_group", "word_count", "line_count", "sha256", "normalized_path", "original_path", "issues", "reference_extraction_status"]
    write_csv(CATALOG_ROOT / "source-catalog.csv", records, fields)
    (CATALOG_ROOT / "source-catalog.json").write_text(json.dumps({"schema_version": 1, "generated_at_utc": now_utc(), "sources": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (CATALOG_ROOT / "source-catalog.md").write_text(
        report_table(
            "Source Catalog",
            records,
            [("source_id", "ID"), ("title", "Title"), ("authors", "Authors"), ("year", "Year"), ("source_type", "Type"), ("relevance", "Relevance"), ("topics", "Tags"), ("canonical_url", "Link"), ("content_quality", "Content"), ("verification_status", "Verification")],
            "Working catalog for the temporary bibliography repository. NotebookLM output is not treated as verified metadata until independently checked.",
        ),
        encoding="utf-8",
    )

    malformed = [record for record in records if record["issues"] or record["metadata_status"] != "parsed"]
    (CATALOG_ROOT / "malformed-or-missing.md").write_text(
        report_table("Malformed or Missing Source Data", malformed, [("source_id", "ID"), ("title", "Title"), ("issues", "Problems"), ("normalized_path", "File"), ("source_url", "Recorded source")], "Entries require metadata repair, source verification, content replacement, or manual review. They are not silently discarded."),
        encoding="utf-8",
    )
    low_value = [record for record in records if record["relevance"] in {"exclude-candidate", "peripheral"}]
    (CATALOG_ROOT / "peripheral-or-exclusion-candidates.md").write_text(
        report_table("Peripheral or Exclusion Candidates", low_value, [("source_id", "ID"), ("title", "Title"), ("relevance", "Status"), ("issues", "Reason"), ("source_type", "Type")], "These sources remain archived. Exclusion from the active thesis corpus requires review; no source is deleted automatically."),
        encoding="utf-8",
    )

    duplicate_lines = ["# Duplicate Groups", "", "Duplicates are retained in the raw archive until the preferred version is verified. Exact content, canonical URL, and normalized title are separate signals.", ""]
    for group_id, mechanism, members in duplicate_sets:
        duplicate_lines.extend([f"## {group_id} — {mechanism}", ""])
        for member in members:
            record = record_by_id[member]
            duplicate_lines.append(f"- `{member}` — {record['title']} — `{record['normalized_path']}`")
        duplicate_lines.append("")
    (CATALOG_ROOT / "duplicate-groups.md").write_text("\n".join(duplicate_lines), encoding="utf-8")

    write_csv(ARCHIVE_ROOT / "original-path-map.csv", path_map, ["source_id", "original_path", "normalized_path", "sha256"])

    current_urls = {str(record["canonical_url"]) for record in records if record["canonical_url"]}
    reference_rows: list[dict[str, object]] = []
    for candidate, citing_ids in sorted(reference_map.items(), key=lambda item: (-len(item[1]), item[0])):
        reference_rows.append({"candidate": candidate, "cited_by_count": len(citing_ids), "cited_by_source_ids": sorted(citing_ids), "already_in_catalog": candidate in current_urls, "screening_status": "already-present" if candidate in current_urls else "pending", "decision": "", "notes": ""})
    write_csv(QUEUE_ROOT / "references-to-screen.csv", reference_rows, ["candidate", "cited_by_count", "cited_by_source_ids", "already_in_catalog", "screening_status", "decision", "notes"])

    report_candidates: dict[str, set[str]] = defaultdict(set)
    for report in REPORT_ROOT.glob("*"):
        if report.suffix.lower() not in {".md", ".csv", ".txt"}:
            continue
        text = report.read_text(encoding="utf-8", errors="replace")
        for url in URL_RE.findall(text):
            canonical = canonicalize_url(clean_url(url))
            if canonical and canonical not in current_urls:
                report_candidates[canonical].add(report.name)
    next_lines = [
        "# Next Sources to Add or Verify", "",
        "This is a screening queue, not an approved bibliography. Candidates come from NotebookLM reports and source reference lists and must be verified before intake.", "",
        "## Priority process", "",
        "1. Verify title, authors, publication venue/status, year, DOI or stable URL.",
        "2. Check whether the work is already present under another version.",
        "3. Confirm direct relevance to the bounded thesis research question.",
        "4. Prefer peer-reviewed, official, institutional, or author-provided versions.",
        "5. Add approved files to `incoming/` for the next curation pass.", "", "## NotebookLM report candidates", "",
    ]
    for candidate, reports in sorted(report_candidates.items()):
        next_lines.append(f"- [ ] {candidate} — reported by: {', '.join(sorted(reports))}")
    pending_refs = [row for row in reference_rows if row["screening_status"] == "pending"]
    next_lines.extend(["", "## Reference-mining queue", "", f"`queues/references-to-screen.csv` contains {len(pending_refs)} unique candidates extracted from source bibliographies. Prioritize candidates cited by several relevant sources.", ""])
    (QUEUE_ROOT / "next-sources.md").write_text("\n".join(next_lines), encoding="utf-8")
    (QUEUE_ROOT / "manual-verification.md").write_text("# Manual Verification Queue\n\nUse this queue after automated metadata enrichment. Prioritize: opaque filenames, missing source URLs, empty/sparse files, conflicting versions, and primary-relevance sources.\n\n" f"Current malformed or incomplete entries: **{len(malformed)}**. See `catalog/malformed-or-missing.md`.\n", encoding="utf-8")

    for topic, members in sorted(topic_sources.items()):
        topic_lines = [f"# Topic Index — {topic}", "", "Links to raw Markdown and candidate excerpts. Inclusion here is automatic and must be reviewed.", ""]
        for sid, title, raw_path in sorted(members):
            excerpt_path = EXCERPT_SOURCE_ROOT / f"{sid.lower()}__candidate-excerpts.md"
            excerpt_link = f"; excerpts: `../../{excerpt_path.relative_to(ROOT).as_posix()}`" if excerpt_path.exists() else ""
            topic_lines.append(f"- `{sid}` — {title} — raw: `../../{raw_path}`{excerpt_link}")
        (EXCERPT_TOPIC_ROOT / f"{topic}.md").write_text("\n".join(topic_lines) + "\n", encoding="utf-8")

    (EXCERPT_SOURCE_ROOT / "README.md").write_text("# By-source Excerpts\n\nMachine-extracted candidate passages are stored here only for primary/supporting sources with recognizable sections. They are not verified quotations and must be checked against the source before citation.\n", encoding="utf-8")
    (EXCERPT_TOPIC_ROOT / "README.md").write_text("# By-topic Excerpt Indexes\n\nTopic files link to archived source Markdown and any candidate excerpt file. Topics are metadata tags; source files are not duplicated.\n", encoding="utf-8")
    (INCOMING_ROOT / "README.md").write_text("# Incoming Sources\n\nPlace new, unprocessed source files here. Keep original filenames and do not manually mix them into `sources/raw-md/`. The next curation pass will identify the source, check duplicates and versions, normalize its name, update the catalog, extract references, and create candidate excerpts/notes where useful.\n\nAccepted staging formats: Markdown, PDF, CSV source lists, and NotebookLM reports. Do not add pirated copies or files with unclear acquisition rights.\n", encoding="utf-8")
    (INCOMING_ROOT / ".gitkeep").touch()

    summary = {
        "generated_at_utc": now_utc(),
        "sources": len(records),
        "groups": sorted({str(record["group"]) for record in records}),
        "malformed_or_incomplete": len(malformed),
        "duplicate_groups": len(duplicate_sets),
        "primary": sum(record["relevance"] == "primary" for record in records),
        "supporting": sum(record["relevance"] == "supporting" for record in records),
        "peripheral": sum(record["relevance"] == "peripheral" for record in records),
        "exclude_candidates": sum(record["relevance"] == "exclude-candidate" for record in records),
        "reference_candidates": len(reference_rows),
        "notebooklm_report_candidates": len(report_candidates),
    }
    (CATALOG_ROOT / "curation-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
