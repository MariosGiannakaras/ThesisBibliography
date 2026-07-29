#!/usr/bin/env python3
"""Repair and enrich bibliography metadata using source content and official APIs."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_JSON = ROOT / "catalog" / "source-catalog.json"
CATALOG_CSV = ROOT / "catalog" / "source-catalog.csv"
CATALOG_MD = ROOT / "catalog" / "source-catalog.md"
MALFORMED_MD = ROOT / "catalog" / "malformed-or-missing.md"
DUPLICATES_MD = ROOT / "catalog" / "duplicate-groups.md"
EXCLUSION_MD = ROOT / "catalog" / "peripheral-or-exclusion-candidates.md"
VERIFICATION_LOG = ROOT / "catalog" / "metadata-verification-log.json"
PATH_MAP = ROOT / "archive" / "original-path-map.csv"
EXCERPT_ROOT = ROOT / "excerpts" / "by-source"
TOPIC_ROOT = ROOT / "excerpts" / "by-topic"

USER_AGENT = "ThesisBibliography/1.0 scholarly-metadata-curation"
ARXIV_RE = re.compile(r"(?:arxiv:|arxiv\.org/(?:abs|pdf|html)/|\b)(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
SOURCE_RE = re.compile(r"^\s*>?\s*Source\s*:\s*(https?://\S+)\s*$", re.IGNORECASE | re.MULTILINE)
GENERIC_TITLES = ("skip to", "jump to", "sitemap", "navigation", "foreign process", "nan / nan", "show more", "home >", "by: tokenring", "aptitude & reasoning")
TOPIC_RULES: dict[str, tuple[str, ...]] = {
    "robust-rl": ("robust reinforcement", "robust mdp", "distributionally robust", "adversarial reinforcement"),
    "resilience-recovery": ("resilien", "recovery time", "recover from", "adaptation speed", "mean time to"),
    "nonstationary-rl": ("non-stationary", "nonstationary", "changing dynamics", "change point", "environmental change"),
    "safe-rl": ("safe reinforcement", "constrained mdp", "safety constraint", "safety gridworld"),
    "uncertainty": ("uncertainty", "uncertain environment", "epistemic", "aleatoric", "ambiguity set"),
    "gridworld": ("gridworld", "grid world", "cliffwalking", "minigrid"),
    "rl-foundations": ("reinforcement learning", "q-learning", "sarsa", "bellman", "policy iteration", "value iteration"),
    "evaluation-statistics": ("confidence interval", "effect size", "statistical", "multiple seeds", "reliable evaluation", "rliable"),
    "multi-agent": ("multi-agent", "multiagent", "markov game", "marl"),
    "ai-safety-alignment": ("ai safety", "alignment", "reward hacking", "specification gaming"),
    "agentic-ai": ("agentic ai", "llm agent", "autonomous agent"),
    "gridworld-implementation": ("github", "gymnasium", "environment creator", "custom environment", "minigrid"),
    "thesis": ("master thesis", "doctoral thesis", "phd thesis", "dissertation", "διπλωματική", "διατριβή"),
}
LOW_VALUE_DOMAINS = {"wikipedia.org", "medium.com", "towardsdatascience.com", "geeksforgeeks.org", "reddit.com", "oceanofpdf.com", "ilide.info"}


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def slugify(value: str, limit: int = 90) -> str:
    slug = normalize_text(value).replace(" ", "-")
    return slug[:limit].rstrip("-") or "untitled"


def clean_title(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip(" \t\r\n-_|`")
    return re.sub(r"\s+-\s+(arxiv|youtube|github|wikipedia|ibm|aws|medium)$", "", value, flags=re.IGNORECASE)


def filename_title(record: dict[str, Any]) -> str:
    stem = Path(str(record.get("original_path", ""))).stem
    stem = re.sub(r"^\d+[-_ ]+", "", stem)
    return clean_title(stem.replace("_", " "))


def is_opaque(title: str) -> bool:
    lower = title.lower()
    return not title or any(lower.startswith(prefix) for prefix in GENERIC_TITLES) or lower.startswith("http") or re.fullmatch(r"[\d._-]+(?:pdf)?", lower) is not None or (".pdf" in lower and len(title.split()) <= 4) or lower in {"fulltext02.pdf", "binder1.pdf"}


def best_local_title(record: dict[str, Any], text: str) -> str:
    fallback = filename_title(record)
    current = clean_title(str(record.get("title", "")))
    if fallback and not is_opaque(fallback):
        return fallback
    if current and not is_opaque(current):
        return current
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text[:10000], flags=re.MULTILINE):
        candidate = clean_title(match.group(1))
        if 8 <= len(candidate) <= 240 and not is_opaque(candidate):
            return candidate
    for line in text[:5000].splitlines():
        candidate = clean_title(re.sub(r"^[>#*_`\s]+", "", line))
        if candidate.lower().startswith("source:"):
            continue
        if 8 <= len(candidate) <= 240 and len(candidate.split()) >= 3 and not is_opaque(candidate):
            return candidate
    return fallback or current or "Untitled source"


def clean_url(url: str) -> str:
    return url.rstrip(".,;:)>]}\"")


def first_source_url(text: str) -> str | None:
    match = SOURCE_RE.search(text)
    return clean_url(match.group(1)) if match else None


def infer_url(record: dict[str, Any], title: str, text: str) -> str | None:
    existing = first_source_url(text) or str(record.get("source_url") or "")
    if existing:
        return clean_url(existing)
    combined = f"{filename_title(record)} {title} {text[:3000]}"
    arxiv = ARXIV_RE.search(combined)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = DOI_RE.search(combined)
    if doi:
        return f"https://doi.org/{doi.group(0).rstrip('.,;)').lower()}"
    stem = Path(str(record.get("original_path", ""))).stem.lower()
    match = re.search(r"arxiv[-_ ](?:org[-_ ])?(?:pdf[-_ ]|abs[-_ ])?(\d{4})[-_.](\d{4,5})", stem)
    return f"https://arxiv.org/abs/{match.group(1)}.{match.group(2)}" if match else None


def canonical_url(url: str | None) -> str:
    if not url:
        return ""
    url = clean_url(url)
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.rstrip("/")
    arxiv = ARXIV_RE.search(url)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    if host == "doi.org":
        return f"https://doi.org/{path.lstrip('/').lower()}"
    if host == "youtu.be":
        return f"https://www.youtube.com/watch?v={path.lstrip('/')}"
    if host == "youtube.com":
        video = urllib.parse.parse_qs(parsed.query).get("v", [])
        if video:
            return f"https://www.youtube.com/watch?v={video[0]}"
    return f"{parsed.scheme or 'https'}://{host}{path}" if host else url


def domain(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower().removeprefix("www.") if url else ""


def extract_primary_ids(title: str, source_url: str, text: str) -> tuple[str, str]:
    region = f"{source_url}\n{title}\n{text[:6000]}"
    arxiv_match = ARXIV_RE.search(region)
    doi_match = DOI_RE.search(region)
    return (doi_match.group(0).rstrip(".,;)").lower() if doi_match else "", arxiv_match.group(1) if arxiv_match else "")


def classify_type(title: str, url: str, text: str) -> str:
    host = domain(url)
    lower = f"{title} {text[:4000]}".lower()
    if host in {"youtube.com", "youtu.be"}:
        return "video-transcript"
    if host == "github.com" or "github" in title.lower():
        return "software-repository"
    if any(term in lower for term in ("master thesis", "phd thesis", "doctoral thesis", "dissertation", "διπλωματική", "διατριβή")):
        return "thesis-dissertation"
    if any(term in lower for term in ("survey", "systematic review", "review of")):
        return "survey-review"
    if host in {"arxiv.org", "openreview.net", "proceedings.mlr.press", "papers.nips.cc", "ieeexplore.ieee.org", "dl.acm.org"} or DOI_RE.search(f"{url}\n{text[:6000]}"):
        return "research-paper"
    if any(term in lower for term in ("book", "textbook", "second edition", "ebook")):
        return "book"
    if host.endswith("farama.org") or "documentation" in lower or "docs." in host:
        return "technical-documentation"
    if any(term in lower for term in ("report", "whitepaper", "framework")):
        return "report-whitepaper"
    return "web-article-or-unknown"


def infer_topics(title: str, text: str, url: str) -> list[str]:
    haystack = f"{title}\n{text[:8000]}\n{url}".lower()
    topics = [topic for topic, keywords in TOPIC_RULES.items() if any(keyword in haystack for keyword in keywords)]
    return sorted(set(topics)) or ["uncategorized"]


def infer_relevance(topics: list[str], title: str, url: str) -> tuple[str, list[str]]:
    topic_set = set(topics)
    if {"robust-rl", "resilience-recovery", "nonstationary-rl", "gridworld"} & topic_set:
        return "primary", []
    if {"safe-rl", "uncertainty", "rl-foundations", "evaluation-statistics", "gridworld-implementation", "thesis"} & topic_set:
        return "supporting", []
    reasons: list[str] = []
    host = domain(url)
    if any(host == item or host.endswith(f".{item}") for item in LOW_VALUE_DOMAINS):
        reasons.append("low-authority-domain")
    lower = title.lower()
    if any(term in lower for term in ("millionaire", "marketing", "finance agent", "operator mastery", "playbook for 2025")):
        reasons.append("commercial-or-off-topic")
    if "agentic-ai" in topic_set and not ({"rl-foundations", "uncertainty", "ai-safety-alignment"} & topic_set):
        reasons.append("agentic-ai-without-rl-link")
    return ("exclude-candidate", reasons) if reasons else ("peripheral", [])


def get_json(url: str, attempts: int = 3) -> dict[str, Any] | None:
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=35) as response:  # noqa: S310
                return json.loads(response.read().decode("utf-8"))
        except Exception:
            if attempt + 1 < attempts:
                time.sleep(1.0 + attempt)
    return None


def arxiv_metadata(ids: list[str]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    for offset in range(0, len(ids), 25):
        batch = ids[offset : offset + 25]
        try:
            request = urllib.request.Request("https://export.arxiv.org/api/query?id_list=" + ",".join(batch), headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=45) as response:  # noqa: S310
                root = ET.fromstring(response.read())
            for entry in root.findall("atom:entry", ns):
                identifier = re.sub(r"v\d+$", "", entry.findtext("atom:id", default="", namespaces=ns).rstrip("/").split("/")[-1])
                result[identifier] = {
                    "title": " ".join(entry.findtext("atom:title", default="", namespaces=ns).split()),
                    "authors": "; ".join(author.findtext("atom:name", default="", namespaces=ns) for author in entry.findall("atom:author", ns)),
                    "year": entry.findtext("atom:published", default="", namespaces=ns)[:4],
                    "doi": entry.findtext("arxiv:doi", default="", namespaces=ns) or "",
                    "venue": entry.findtext("arxiv:journal_ref", default="", namespaces=ns) or "arXiv",
                    "provider": "arXiv API",
                }
        except Exception:
            pass
        time.sleep(0.5)
    return result


def crossref_metadata(doi: str) -> dict[str, Any] | None:
    payload = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
    if not payload or not isinstance(payload.get("message"), dict):
        return None
    item = payload["message"]
    titles = item.get("title") or []
    authors = []
    for author in item.get("author") or []:
        name = " ".join(filter(None, (author.get("given"), author.get("family"))))
        if name:
            authors.append(name)
    date_parts = ((item.get("published") or item.get("issued") or {}).get("date-parts") or [[]])[0]
    return {"title": titles[0] if titles else "", "authors": "; ".join(authors), "year": str(date_parts[0]) if date_parts else "", "doi": str(item.get("DOI") or doi).lower(), "venue": "; ".join(item.get("container-title") or []), "provider": "Crossref API"}


def openalex_match(title: str) -> tuple[dict[str, Any] | None, float]:
    payload = get_json("https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per-page": 3}))
    if not payload:
        return None, 0.0
    target = normalize_text(title)
    best: dict[str, Any] | None = None
    best_score = 0.0
    for item in payload.get("results") or []:
        candidate_title = str(item.get("display_name") or item.get("title") or "")
        score = SequenceMatcher(None, target, normalize_text(candidate_title)).ratio()
        if score > best_score:
            authors = [(authorship.get("author") or {}).get("display_name") for authorship in item.get("authorships") or []]
            primary = item.get("primary_location") or {}
            source = primary.get("source") or {}
            best = {"title": candidate_title, "authors": "; ".join(item for item in authors if item), "year": str(item.get("publication_year") or ""), "doi": str(item.get("doi") or "").removeprefix("https://doi.org/"), "venue": str(source.get("display_name") or ""), "landing_page_url": str(primary.get("landing_page_url") or ""), "provider": "OpenAlex API"}
            best_score = score
    return best, best_score


def write_csv(path: Path, records: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({key: "; ".join(str(item) for item in value) if isinstance(value, list) else value for key, value in record.items()})


def table(title: str, intro: str, records: list[dict[str, Any]], columns: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", "", intro, ""]
    if not records:
        return "\n".join(lines + ["No entries."]) + "\n"
    lines.extend(["| " + " | ".join(label for _key, label in columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"])
    for record in records:
        cells = []
        for key, _label in columns:
            value = record.get(key, "")
            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)
            cells.append(str(value or "").replace("|", "\\|").replace("\n", " ")[:300])
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def required_issues(record: dict[str, Any]) -> list[str]:
    issues = [item for item in record.get("issues", []) if item not in {"missing-authors", "missing-year", "opaque-or-unverified-title"}]
    if not record.get("source_url"):
        issues.append("missing-source-url")
    if is_opaque(str(record.get("title") or "")):
        issues.append("opaque-or-unverified-title")
    if record.get("source_type") in {"research-paper", "survey-review", "thesis-dissertation", "book"}:
        if not record.get("authors"):
            issues.append("missing-authors")
        if not record.get("year"):
            issues.append("missing-year")
    if record.get("content_quality") in {"empty", "sparse", "source-link-only", "metadata-only", "noisy-web-scrape"}:
        issues.append(f"content-{record['content_quality']}")
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    args = parser.parse_args()
    records: list[dict[str, Any]] = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))["sources"]
    log: list[dict[str, Any]] = []

    for record in records:
        path = ROOT / record["normalized_path"]
        text = path.read_text(encoding="utf-8", errors="replace")
        title = best_local_title(record, text)
        url = infer_url(record, title, text) or ""
        doi, arxiv_id = extract_primary_ids(title, url, text)
        record.update({"title": title, "source_url": url, "canonical_url": canonical_url(url), "doi": doi, "arxiv_id": arxiv_id, "source_type": classify_type(title, url, text)})
        record["topics"] = infer_topics(title, text, url)
        record["relevance"], extra = infer_relevance(record["topics"], title, url)
        record["issues"] = sorted(set(list(record.get("issues") or []) + extra))

    arxiv_data = arxiv_metadata(sorted({record["arxiv_id"] for record in records if record.get("arxiv_id")})) if args.online else {}
    crossref_cache: dict[str, dict[str, Any] | None] = {}
    for index, record in enumerate(records):
        metadata: dict[str, Any] | None = None
        score = 1.0
        provider = ""
        if record.get("arxiv_id") and record["arxiv_id"] in arxiv_data:
            metadata, provider = arxiv_data[record["arxiv_id"]], "arXiv API"
        elif args.online and record.get("doi"):
            doi = str(record["doi"])
            if doi not in crossref_cache:
                crossref_cache[doi] = crossref_metadata(doi)
                time.sleep(0.12)
            metadata = crossref_cache[doi]
            provider = "Crossref API" if metadata else ""
        elif args.online and record["source_type"] in {"research-paper", "survey-review", "thesis-dissertation", "book"} and not is_opaque(record["title"]):
            metadata, score = openalex_match(record["title"])
            if score < 0.90:
                metadata = None
            provider = "OpenAlex API" if metadata else ""
            time.sleep(0.12)

        if metadata:
            old_title = record["title"]
            record["title"] = clean_title(str(metadata.get("title") or old_title))
            record["authors"] = str(metadata.get("authors") or record.get("authors") or "")
            record["year"] = str(metadata.get("year") or record.get("year") or "")
            record["doi"] = str(metadata.get("doi") or record.get("doi") or "").lower()
            if not record.get("source_url") and metadata.get("landing_page_url"):
                record["source_url"] = metadata["landing_page_url"]
                record["canonical_url"] = canonical_url(record["source_url"])
            record["venue"] = str(metadata.get("venue") or "")
            record["verification_status"] = "verified-metadata-api" if provider in {"arXiv API", "Crossref API"} else "probable-openalex-match"
            log.append({"source_id": record["source_id"], "provider": provider, "match_score": round(score, 4), "previous_title": old_title, "verified_title": record["title"]})
        else:
            record["venue"] = str(record.get("venue") or "")
            record["verification_status"] = "source-link-recorded-not-verified" if record.get("source_url") else "unresolved"
        record["issues"] = required_issues(record)
        record["metadata_status"] = "complete-for-type" if not record["issues"] else "needs-verification"

        path = ROOT / record["normalized_path"]
        desired = path.with_name(f"{str(record['source_id']).lower()}__{slugify(record['title'])}.md")
        if desired != path:
            if desired.exists() and desired.read_bytes() != path.read_bytes():
                desired = path.with_name(f"{str(record['source_id']).lower()}__{slugify(record['title'])}__{index + 1}.md")
            if not desired.exists():
                path.rename(desired)
            else:
                path.unlink()
            record["normalized_path"] = desired.relative_to(ROOT).as_posix()

    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    by_id = {record["source_id"]: record for record in records}
    for record in records:
        record["duplicate_group"] = ""
        groups[("exact-content", str(record["sha256"]))].append(record["source_id"])
        if record.get("canonical_url"):
            groups[("canonical-url", str(record["canonical_url"]))].append(record["source_id"])
        groups[("normalized-title", normalize_text(record["title"]))].append(record["source_id"])
    duplicate_sets: list[tuple[str, str, list[str]]] = []
    signatures: set[tuple[str, ...]] = set()
    for (mechanism, _key), members in groups.items():
        members = sorted(set(members))
        if len(members) < 2 or tuple(members) in signatures:
            continue
        signatures.add(tuple(members))
        gid = f"DUP-{len(duplicate_sets) + 1:04d}"
        duplicate_sets.append((gid, mechanism, members))
        for member in members:
            current = by_id[member].get("duplicate_group") or ""
            by_id[member]["duplicate_group"] = ";".join(filter(None, (current, gid)))

    fields = ["source_id", "group", "title", "authors", "year", "venue", "source_type", "relevance", "topics", "source_url", "canonical_url", "doi", "arxiv_id", "content_quality", "metadata_status", "verification_status", "duplicate_group", "word_count", "line_count", "sha256", "normalized_path", "original_path", "issues", "reference_extraction_status"]
    records.sort(key=lambda item: item["source_id"])
    write_csv(CATALOG_CSV, records, fields)
    CATALOG_JSON.write_text(json.dumps({"schema_version": 2, "sources": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(PATH_MAP, [{"source_id": item["source_id"], "original_path": item["original_path"], "normalized_path": item["normalized_path"], "sha256": item["sha256"]} for item in records], ["source_id", "original_path", "normalized_path", "sha256"])
    VERIFICATION_LOG.write_text(json.dumps({"schema_version": 1, "matches": log}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    CATALOG_MD.write_text(table("Source Catalog", "The authoritative working index. API-verified metadata and probable OpenAlex matches are distinguished in the verification column.", records, [("source_id", "ID"), ("title", "Title"), ("authors", "Authors"), ("year", "Year"), ("venue", "Venue"), ("source_type", "Type"), ("relevance", "Relevance"), ("topics", "Tags"), ("canonical_url", "Link"), ("verification_status", "Verification")]), encoding="utf-8")
    malformed = [item for item in records if item["issues"]]
    MALFORMED_MD.write_text(table("Malformed or Missing Source Data", "Only metadata required for the source type is mandatory. Entries remain archived until repaired or explicitly excluded.", malformed, [("source_id", "ID"), ("title", "Title"), ("issues", "Problems"), ("normalized_path", "File"), ("source_url", "Recorded source")]), encoding="utf-8")
    excluded = [item for item in records if item["relevance"] in {"peripheral", "exclude-candidate"}]
    EXCLUSION_MD.write_text(table("Peripheral or Exclusion Candidates", "Automated relevance labels are screening aids, not deletion decisions.", excluded, [("source_id", "ID"), ("title", "Title"), ("relevance", "Status"), ("issues", "Reason"), ("source_type", "Type")]), encoding="utf-8")

    duplicate_lines = ["# Duplicate Groups", "", "Retain all versions until a preferred scholarly version is selected. Groups use exact content, canonical URL, or repaired title.", ""]
    for gid, mechanism, members in duplicate_sets:
        duplicate_lines.extend([f"## {gid} — {mechanism}", ""])
        duplicate_lines.extend(f"- `{member}` — {by_id[member]['title']} — `{by_id[member]['normalized_path']}`" for member in members)
        duplicate_lines.append("")
    DUPLICATES_MD.write_text("\n".join(duplicate_lines), encoding="utf-8")

    for path in TOPIC_ROOT.glob("*.md"):
        path.unlink()
    topic_members: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        for topic in record["topics"]:
            topic_members[topic].append(record)
        excerpt = EXCERPT_ROOT / f"{str(record['source_id']).lower()}__candidate-excerpts.md"
        if excerpt.exists():
            body = excerpt.read_text(encoding="utf-8", errors="replace")
            body = re.sub(r"^# Candidate Excerpts — .*?$", f"# Candidate Excerpts — {record['title']}", body, count=1, flags=re.MULTILINE)
            body = re.sub(r"^- Source file: `.*?`$", f"- Source file: `{record['normalized_path']}`", body, count=1, flags=re.MULTILINE)
            excerpt.write_text(body, encoding="utf-8")
    for topic, members in sorted(topic_members.items()):
        lines = [f"# Topic Index — {topic}", "", "Automatic index; review before using it as a thesis taxonomy.", ""]
        for record in sorted(members, key=lambda item: item["source_id"]):
            excerpt = EXCERPT_ROOT / f"{str(record['source_id']).lower()}__candidate-excerpts.md"
            extra = f"; excerpts: `../by-source/{excerpt.name}`" if excerpt.exists() else ""
            lines.append(f"- `{record['source_id']}` — {record['title']} — raw: `../../{record['normalized_path']}`{extra}")
        (TOPIC_ROOT / f"{topic}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (TOPIC_ROOT / "README.md").write_text("# By-topic Excerpt Indexes\n\nGenerated links to source Markdown and candidate excerpts.\n", encoding="utf-8")

    print(json.dumps({"sources": len(records), "api_matches": len(log), "malformed": len(malformed), "duplicate_groups": len(duplicate_sets)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
