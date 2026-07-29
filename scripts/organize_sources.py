#!/usr/bin/env python3
"""Normalize NotebookLM bibliography groups into a flat, auditable source archive.

The script preserves source Markdown bytes, moves every source into one folder,
keeps NotebookLM reports separately, and rebuilds the catalog and curation views.
It is intentionally conservative: suspected duplicates and low-value sources are
flagged, never silently deleted.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES_DIR = ROOT / "sources" / "markdown"
IMPORTS_DIR = ROOT / "imports" / "notebooklm"
CATALOG_DIR = ROOT / "catalog"
CURATION_DIR = ROOT / "curation"

GROUP_RE = re.compile(r"Group(\d+)$", re.IGNORECASE)
SOURCE_DIR_RE = re.compile(r"Group\d+Files$", re.IGNORECASE)
SOURCE_MARKER_RE = re.compile(r"^>\s*Source:\s*(\S+)", re.MULTILINE)
YEAR_RE = re.compile(r"\b(19\d{2}|20[0-2]\d)\b")

TOPIC_RULES = {
    "robust-rl": [r"robust reinforcement", r"robust mdp", r"distributionally robust", r"ambiguity set", r"uncertainty set"],
    "resilience-recovery": [r"resilien", r"recovery time", r"adaptation speed", r"performance degradation", r"performance drop"],
    "nonstationarity": [r"non[- ]?station", r"sudden change", r"environmental change", r"change[- ]?point", r"concept drift"],
    "gridworld": [r"gridworld", r"grid world", r"frozenlake", r"cliffwalking", r"minigrid", r"novgrid"],
    "safe-rl": [r"safe reinforcement", r"safety grid", r"constrained mdp", r"stability guarantee", r"safe exploration"],
    "transition-uncertainty": [r"transition uncertainty", r"transition perturb", r"uncertain transition", r"model uncertainty"],
    "action-uncertainty": [r"action robust", r"action perturb", r"action failure", r"policy execution uncertainty"],
    "observation-uncertainty": [r"observation perturb", r"state perturb", r"adversarial state", r"noisy observation"],
    "reward-uncertainty": [r"reward uncertainty", r"reward robust", r"reward shaping", r"reward hacking"],
    "partial-observability": [r"pomdp", r"partially observable", r"belief state"],
    "tabular-rl": [r"q[- ]?learning", r"sarsa", r"value iteration", r"policy iteration", r"temporal difference"],
    "deep-rl": [r"deep reinforcement", r"\bdqn\b", r"\bppo\b", r"actor[- ]?critic"],
    "model-based-rl": [r"model[- ]?based reinforcement", r"\bdyna(?:-q)?\b", r"monte carlo planning"],
    "continual-adaptation": [r"continual reinforcement", r"lifelong reinforcement", r"catastrophic forgetting", r"transfer learning", r"meta[- ]?reinforcement"],
    "evaluation-statistics": [r"reliable evaluation", r"confidence interval", r"effect size", r"statistical", r"\brliable\b", r"multiple seeds"],
    "benchmark-tooling": [r"benchmark", r"gymnasium", r"minigrid", r"robust gymnasium", r"mdp playground", r"toolkit"],
    "ai-agents-background": [r"ai agent", r"agentic ai", r"intelligent agent", r"multi-agent system"],
    "governance-ethics": [r"governance", r"ethic", r"legal", r"risk management framework", r"alignment"],
}

OUT_OF_SCOPE_TERMS = [
    "financial advisory", "trading", "stock market", "millionaire", "digital marketing",
    "recommender system", "recommendation system", "manufacturing", "supply chain",
    "inventory control", "quantum control", "covid-19 testing", "sound event detection",
    "healthcare liability", "streetfighter", "supermario", "ms pacman", "vehicle illumination",
    "computational fluid dynamics", "fpga", "power grid stability", "battery operation",
]

CORE_TERMS = [
    "robust reinforcement", "resilient", "non-stationary", "nonstationary", "gridworld",
    "grid world", "uncertainty", "sudden environmental change", "action robust",
    "state perturbation", "transition prototypes", "safe reinforcement learning",
]

LOW_QUALITY_DOMAINS = {
    "wikipedia.org", "medium.com", "geeksforgeeks.org", "marktechpost.com", "netguru.com",
    "milvus.io", "towardsdatascience.com", "rapidinnovation.io", "rezolve.ai",
}

HIGH_QUALITY_DOMAIN_HINTS = (
    "arxiv.org", "proceedings.mlr.press", "openreview.net", "papers.nips.cc",
    "neurips.cc", "ojs.aaai.org", "ieeexplore.ieee.org", "acm.org", "springer.com",
    "sciencedirect.com", "nature.com", ".edu", ".ac.", "lib.", "repository",
    "dspace", "opus.lib", "nvlpubs.nist.gov", "gymnasium.farama.org",
)

KNOWN_COVERAGE_TARGETS = [
    ("AI Safety Gridworlds", "GridWorld safety benchmark and failure-mode isolation"),
    ("NovGrid", "Abrupt novelty, degradation and adaptation/recovery measurement"),
    ("CARL: A Benchmark for Contextual and Adaptive Reinforcement Learning", "Context variation and adaptive RL benchmarking"),
    ("Robust Gymnasium", "Unified robustness benchmark and perturbation taxonomy"),
    ("Rliable", "Reliable aggregate evaluation with few seeds"),
    ("A Bayesian Approach to Robust Reinforcement Learning", "Robust MDP uncertainty sets evaluated in GridWorld"),
    ("Sample Complexity of Robust Reinforcement Learning with a Generative Model", "Theoretical robust-RL sample complexity"),
    ("Action Robust Reinforcement Learning", "Action-execution uncertainty"),
    ("Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations", "Observation/state perturbations"),
    ("Deep Reinforcement Learning in Non-Stationary Environments", "Change detection and adaptation in a complete thesis"),
]


@dataclass
class SourceRecord:
    source_id: str
    title: str
    authors: str
    year: str
    url: str
    domain: str
    source_type: str
    language: str
    original_group: str
    original_path: str
    normalized_path: str
    content_sha256: str
    bytes: int
    lines: int
    words: int
    content_status: str
    relevance: str
    quality: str
    priority: str
    curation_status: str
    review_status: str = "not-reviewed"
    topics: list[str] = field(default_factory=list)
    duplicate_type: str = ""
    duplicate_of: str = ""
    metadata_confidence: str = "low"
    notes: str = ""

    def as_dict(self) -> dict[str, str | int]:
        data = asdict(self)
        data["topics"] = ";".join(self.topics)
        return data


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = re.sub(r"https?\S+", " ", value)
    value = re.sub(r"[^a-z0-9α-ωάέήίόύώϊϋΐΰ]+", " ", value)
    return normalize_space(value)


def slugify(value: str, max_length: int = 72) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-+", "-", value)
    return (value[:max_length].rstrip("-") or "source")


def clean_filename_title(name: str) -> str:
    value = re.sub(r"\.md$", "", name, flags=re.IGNORECASE)
    value = re.sub(r"\.pdf$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^\d+[-_ ]+", "", value)
    value = value.replace("_", " ")
    value = re.sub(r"__?(?:copy|duplicate|dup|\d+)$", "", value, flags=re.IGNORECASE)
    return normalize_space(value)


def extract_title(text: str, filename: str) -> str:
    fallback = clean_filename_title(filename)
    normalized_fallback = normalize_title(fallback)
    fallback_tokens = normalized_fallback.split()
    numeric_ratio = (sum(token.isdigit() for token in fallback_tokens) / len(fallback_tokens)) if fallback_tokens else 0.0
    opaque_filename = (
        len(normalized_fallback) < 10
        or normalized_fallback.startswith("https ")
        or numeric_ratio > 0.35
        or any(token in normalized_fallback for token in ("fulltext", "binder", "pdf md", "document "))
        or re.fullmatch(r"(?:arxiv )?\d{4} \d+(?:v\d+)?", normalized_fallback) is not None
    )
    generic = {
        "contents", "table of contents", "skip navigation", "jump to content",
        "help advanced search", "back", "home", "main menu navigation",
    }
    lines = [line.strip() for line in text.splitlines()]
    for line in lines[:120]:
        if not line.startswith("# ") or len(line) <= 3:
            continue
        candidate = normalize_space(line[2:])
        normalized_candidate = normalize_title(candidate)
        similarity = SequenceMatcher(None, normalized_candidate[:200], normalized_fallback[:200]).ratio()
        if normalized_candidate and normalized_candidate not in generic and (opaque_filename or similarity >= 0.45):
            return candidate
    if not opaque_filename:
        return fallback
    for index, line in enumerate(lines[:80]):
        if not line or SOURCE_MARKER_RE.match(line):
            continue
        candidate = re.sub(r"^[#>*\-\s]+", "", line).strip()
        normalized_candidate = normalize_title(candidate)
        candidate_tokens = normalized_candidate.split()
        candidate_numeric_ratio = (
            sum(token.isdigit() for token in candidate_tokens) / len(candidate_tokens)
            if candidate_tokens else 0.0
        )
        if (
            len(candidate) >= 12
            and candidate_numeric_ratio <= 0.35
            and normalized_candidate not in generic
            and not candidate.lower().startswith(("source:", "skip to", "back ", "logo "))
        ):
            next_lines = []
            for following in lines[index + 1:index + 3]:
                cleaned = re.sub(r"^[#>*\-\s]+", "", following).strip()
                if cleaned and cleaned.upper() == cleaned and re.search(r"[A-Z]", cleaned):
                    next_lines.append(cleaned)
                else:
                    break
            return normalize_space(" ".join([candidate, *next_lines]))
    return fallback


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    url = url.strip().rstrip(".,;)")
    try:
        parts = urlsplit(url)
    except ValueError:
        return url
    host = parts.netloc.lower().removeprefix("www.")
    path = re.sub(r"/+", "/", parts.path).rstrip("/")
    query_pairs = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key.lower() not in {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "sequence", "isallowed"}
    ]
    if host == "arxiv.org":
        match = re.search(r"/(?:abs|pdf|html)/(\d{4}\.\d+)(?:v\d+)?", path)
        if match:
            return f"https://arxiv.org/abs/{match.group(1)}"
    return urlunsplit((parts.scheme.lower() or "https", host, path, urlencode(query_pairs), ""))


def extract_url(text: str) -> str:
    marker = SOURCE_MARKER_RE.search(text)
    if marker:
        return marker.group(1).strip()
    head = "\n".join(text.splitlines()[:220])
    arxiv = re.search(r"https?://(?:www\.)?arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d+)(?:v\d+)?", head)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = re.search(r"https?://(?:dx\.)?doi\.org/10\.\d{4,9}/[^\s)>\]]+", head)
    if doi:
        return doi.group(0).rstrip(".,;:")
    return ""


def is_specific_url(url: str) -> bool:
    if not url:
        return False
    try:
        parts = urlsplit(url)
    except ValueError:
        return False
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/")
    if not path:
        return False
    if host == "arxiv.org":
        return re.fullmatch(r"/abs/\d{4}\.\d+", path) is not None
    if "libguides." in host or path in {"/search", "/index.php", "/c.php"}:
        return False
    if path.endswith("/c.php") or (path == "/c.php" and not parts.query):
        return False
    return True


def domain_of(url: str) -> str:
    try:
        return urlsplit(url).netloc.lower().removeprefix("www.")
    except ValueError:
        return ""


def detect_language(text: str) -> str:
    sample = text[:12000]
    greek = len(re.findall(r"[Α-Ωα-ωάέήίόύώϊϋΐΰ]", sample))
    latin = len(re.findall(r"[A-Za-z]", sample))
    if greek > 100 and greek > latin * 0.35:
        return "el"
    if latin > 50:
        return "en"
    return "unknown"


def content_status(text: str) -> str:
    stripped = text.strip()
    if "Failed to load source content" in stripped or stripped.startswith("> Error:"):
        return "failed-load"
    if len(stripped) < 150 or len(stripped.splitlines()) <= 3:
        return "metadata-only"
    if len(stripped) < 2000:
        return "partial"
    return "full-text"


def is_notebooklm_synthesis(title: str, text: str) -> bool:
    lower_title = title.lower()
    cite_placeholders = len(re.findall(r"\[cite:\s*\d+", text, flags=re.IGNORECASE))
    report_title = any(term in lower_title for term in (
        "research report", "thesis sources analysis", "έκθεση έρευνας",
        "συστηματική σύγκριση και αξιολόγηση ανθεκτικών πρακτόρων",
    ))
    return (cite_placeholders >= 5 and not SOURCE_MARKER_RE.search(text)) or report_title


def source_type(title: str, url: str, text: str) -> str:
    title_lower = title.lower()
    domain = domain_of(url)
    if is_notebooklm_synthesis(title, text):
        return "notebooklm-synthesis"
    if "youtube.com" in domain or "youtu.be" in domain or "youtube" in title_lower:
        return "video-or-lecture"
    if "github.com" in domain or title_lower.startswith("github") or " - github" in title_lower:
        return "code-repository"
    if any(term in title_lower for term in ("phd thesis", "doctoral thesis", "dissertation", "master thesis", "diploma thesis", "διπλωματικ")):
        return "thesis-or-dissertation"
    if any(term in title_lower for term in (" ebook", "e-book", "textbook", "handbook", "reinforcement learning: an introduction")):
        return "book-or-chapter"
    if "nvlpubs.nist.gov" in url or any(term in title_lower for term in ("standard", "risk management framework", "whitepaper", "white paper")):
        return "standard-or-institutional-report"
    if any(host in domain for host in ("arxiv.org", "proceedings.mlr.press", "openreview.net", "aaai.org", "neurips", "ieee", "acm", "springer", "sciencedirect", "mdpi.com")):
        return "academic-paper"
    sample = text[:3000].lower()
    if len(text) > 10000 and "abstract" in sample and any(term in sample for term in ("references", "introduction", "experiment")):
        return "academic-paper"
    if any(term in title_lower for term in ("documentation", "tutorial", "course", "lecture", "seminar")):
        return "documentation-or-educational"
    if domain:
        return "web-article"
    return "unknown"


def classify_topics(title: str, text: str, kind: str) -> list[str]:
    title_haystack = title.lower()
    opening = "\n".join(text.splitlines()[:80]).lower()[:5000]
    topics: list[str] = []
    for topic, patterns in TOPIC_RULES.items():
        title_hit = any(re.search(pattern, title_haystack, flags=re.IGNORECASE) for pattern in patterns)
        opening_hit = any(re.search(pattern, opening, flags=re.IGNORECASE) for pattern in patterns)
        if title_hit or opening_hit:
            topics.append(topic)
    if "benchmark-tooling" in topics and kind not in {"code-repository", "documentation-or-educational"}:
        patterns = TOPIC_RULES["benchmark-tooling"]
        if not any(re.search(pattern, title_haystack, flags=re.IGNORECASE) for pattern in patterns):
            topics.remove("benchmark-tooling")
    return topics or ["unclassified"]


def classify_quality(kind: str, url: str, title: str) -> str:
    domain = domain_of(url)
    if kind == "notebooklm-synthesis":
        return "low"
    if kind in {"academic-paper", "thesis-or-dissertation", "book-or-chapter"}:
        return "high"
    if any(hint in url.lower() for hint in HIGH_QUALITY_DOMAIN_HINTS):
        return "high"
    if domain in LOW_QUALITY_DOMAINS or "wikipedia" in title.lower():
        return "low"
    if kind in {"standard-or-institutional-report", "code-repository", "documentation-or-educational"}:
        return "medium"
    return "medium-low"


def classify_relevance(title: str, text: str, topics: list[str], status: str, kind: str) -> str:
    haystack = f"{title} {text[:3500]}".lower()
    if kind == "notebooklm-synthesis":
        return "auxiliary-non-citable"
    if status == "failed-load":
        return "needs-recovery"
    if any(term in haystack for term in OUT_OF_SCOPE_TERMS):
        return "out-of-scope"
    core_hits = sum(term in haystack for term in CORE_TERMS)
    if "robust-rl" in topics and any(t in topics for t in ("gridworld", "nonstationarity", "transition-uncertainty", "action-uncertainty", "observation-uncertainty", "reward-uncertainty")):
        return "core"
    if core_hits >= 2 or ("gridworld" in topics and any(t in topics for t in ("safe-rl", "continual-adaptation", "evaluation-statistics"))):
        return "core"
    if any(t in topics for t in ("robust-rl", "resilience-recovery", "nonstationarity", "gridworld", "safe-rl", "evaluation-statistics", "benchmark-tooling")):
        return "supporting"
    if any(t in topics for t in ("tabular-rl", "deep-rl", "model-based-rl", "partial-observability", "ai-agents-background")):
        return "background"
    return "needs-review"


def priority_for(relevance: str, quality: str, status: str) -> str:
    if relevance == "auxiliary-non-citable":
        return "P5-archive-only"
    if status in {"failed-load", "metadata-only"}:
        return "P4-recover-or-replace"
    if relevance == "core" and quality == "high":
        return "P1-core"
    if relevance in {"core", "supporting"} and quality in {"high", "medium"}:
        return "P2-supporting"
    if relevance == "out-of-scope" or quality == "low":
        return "P5-archive-only"
    return "P3-review"


def curation_status_for(relevance: str, status: str, kind: str, duplicate_of: str = "") -> str:
    if kind == "notebooklm-synthesis":
        return "non-citable-context"
    if duplicate_of:
        return "duplicate-candidate"
    if status in {"failed-load", "metadata-only", "partial"}:
        return "recover-or-verify"
    return {
        "core": "candidate-core",
        "supporting": "candidate-supporting",
        "background": "background-only",
        "out-of-scope": "archive-only",
        "needs-review": "manual-review",
        "needs-recovery": "recover-or-verify",
        "auxiliary-non-citable": "non-citable-context",
    }.get(relevance, "manual-review")


def extract_year(title: str, text: str) -> str:
    for sample in (title, "\n".join(text.splitlines()[:60])):
        matches = YEAR_RE.findall(sample)
        if matches:
            return matches[0]
    return ""


def load_reference_rows(group_dirs: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for group_dir in group_dirs:
        for csv_path in group_dir.glob("*.csv"):
            with csv_path.open(encoding="utf-8-sig", newline="", errors="replace") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    title = normalize_space(row.get("Source Name", ""))
                    if not title:
                        continue
                    rows.append({
                        "title": title,
                        "normalized_title": normalize_title(title),
                        "authors": normalize_space(row.get("Author(s)", "")),
                        "link": normalize_space(row.get("Link", "")),
                        "group": group_dir.name,
                    })
    return rows


def match_reference(title: str, rows: list[dict[str, str]]) -> tuple[dict[str, str] | None, float]:
    target = normalize_title(title)
    if not target:
        return None, 0.0
    exact = [row for row in rows if row["normalized_title"] == target]
    if exact:
        return exact[0], 1.0
    target_tokens = set(target.split())
    candidates = []
    for row in rows:
        candidate = row["normalized_title"]
        if not candidate:
            continue
        tokens = set(candidate.split())
        overlap = len(target_tokens & tokens) / max(1, len(target_tokens | tokens))
        if overlap < 0.55:
            continue
        ratio = SequenceMatcher(None, target[:240], candidate[:240]).ratio()
        score = 0.65 * ratio + 0.35 * overlap
        if score >= 0.82:
            candidates.append((score, row))
    if not candidates:
        return None, 0.0
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1], candidates[0][0]


def meaningful_paragraphs(text: str) -> list[str]:
    cleaned = re.sub(r"\r", "", text)
    blocks = [normalize_space(block) for block in re.split(r"\n\s*\n", cleaned)]
    result: list[str] = []
    chrome_prefixes = (
        "> source:", "source:", "skip to", "jump to", "back to", "table of contents",
        "main navigation", "cookie", "sign in", "download pdf", "logo back",
    )
    for block in blocks:
        lower = block.lower()
        if len(block) < 140 or len(block) > 3200:
            continue
        if lower.startswith(chrome_prefixes):
            continue
        if lower.startswith(("references", "bibliography")):
            continue
        if block.count("http") > 3 or block.count("[") > 12:
            continue
        if len(re.findall(r"[A-Za-zΑ-Ωα-ω]", block)) < 90:
            continue
        if len(re.findall(r"\b\d+(?:\.\d+)?(?:±|%)", block)) > 12:
            continue
        result.append(block)
    return result


def select_excerpt(text: str, topics: list[str]) -> str:
    paragraphs = meaningful_paragraphs(text)
    if not paragraphs:
        return ""
    keywords = [
        "abstract", "we propose", "we present", "we introduce", "we show", "we demonstrate",
        "results", "experiment", "gridworld", "uncertainty", "robust", "resilien", "recovery",
        "non-stationary", "adaptation", "evaluation",
    ]
    best = ""
    best_score = -1
    for index, paragraph in enumerate(paragraphs[:250]):
        lower = paragraph.lower()
        score = sum(lower.count(keyword) * (3 if keyword in {"abstract", "we propose", "we present", "we show", "results"} else 1) for keyword in keywords)
        score += sum(1 for topic in topics if topic.replace("-", " ") in lower)
        if index < 12:
            score += 2
        if score > best_score:
            best = paragraph
            best_score = score
    if best_score <= 0:
        return ""
    return best[:900].rstrip() + ("…" if len(best) > 900 else "")


def load_existing_catalog() -> dict[str, dict[str, object]]:
    path = CATALOG_DIR / "source_catalog.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(payload, list):
        return {}
    return {
        str(item["source_id"]): item
        for item in payload
        if isinstance(item, dict) and item.get("source_id")
    }


def load_all_reference_rows(group_dirs: list[Path]) -> list[dict[str, str]]:
    rows = load_reference_rows(group_dirs)
    if IMPORTS_DIR.exists():
        pseudo_dirs = sorted(path for path in IMPORTS_DIR.iterdir() if path.is_dir())
        rows.extend(load_reference_rows(pseudo_dirs))
    return rows


def collect_input_sources() -> tuple[list[tuple[Path, str, str]], list[Path]]:
    group_dirs = sorted(path for path in ROOT.iterdir() if path.is_dir() and GROUP_RE.fullmatch(path.name))
    inputs: list[tuple[Path, str, str]] = []
    for group_dir in group_dirs:
        source_dirs = sorted(path for path in group_dir.iterdir() if path.is_dir() and SOURCE_DIR_RE.fullmatch(path.name))
        for source_dir in source_dirs:
            for path in sorted(source_dir.rglob("*.md")):
                inputs.append((path, group_dir.name, path.relative_to(ROOT).as_posix()))
    if SOURCES_DIR.exists():
        for path in sorted(SOURCES_DIR.glob("*.md")):
            inputs.append((path, "normalized", path.relative_to(ROOT).as_posix()))
    return inputs, group_dirs


def move_helper_reports(group_dirs: list[Path]) -> None:
    for group_dir in group_dirs:
        match = GROUP_RE.fullmatch(group_dir.name)
        assert match
        group_number = int(match.group(1))
        destination = IMPORTS_DIR / f"group-{group_number:02d}"
        destination.mkdir(parents=True, exist_ok=True)
        md_files = sorted(path for path in group_dir.glob("*.md") if path.is_file())
        csv_files = sorted(path for path in group_dir.glob("*.csv") if path.is_file())
        for index, path in enumerate(md_files, start=1):
            target_name = "source-audit.md" if index == 1 else f"source-audit-{index:02d}.md"
            shutil.move(str(path), destination / target_name)
        for index, path in enumerate(csv_files, start=1):
            target_name = "extracted-reference-table.csv" if index == 1 else f"extracted-reference-table-{index:02d}.csv"
            shutil.move(str(path), destination / target_name)


def main() -> int:
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    CURATION_DIR.mkdir(parents=True, exist_ok=True)

    inputs, group_dirs = collect_input_sources()
    if not inputs:
        print("No source Markdown files found.", file=sys.stderr)
        return 1

    reference_rows = load_all_reference_rows(group_dirs)
    existing_catalog = load_existing_catalog()
    parsed: list[dict[str, object]] = []

    for path, group, original_path in inputs:
        raw = path.read_bytes()
        text = raw.decode("utf-8", errors="replace")
        sha256 = hashlib.sha256(raw).hexdigest()
        existing_id_match = re.match(r"^(SRC-[A-F0-9]{10})__", path.name)
        source_id = existing_id_match.group(1) if existing_id_match else "SRC-" + hashlib.sha1(f"{original_path}|{sha256}".encode("utf-8")).hexdigest()[:10].upper()
        existing = existing_catalog.get(source_id, {})

        title = extract_title(text, path.name)
        url = canonicalize_url(extract_url(text))
        match, match_score = match_reference(title, reference_rows)
        authors = match["authors"] if match and match["authors"] else ""
        if not url and match and match["link"].startswith("http"):
            url = canonicalize_url(match["link"])
        if existing:
            title = str(existing.get("title") or title)
            authors = str(existing.get("authors") or authors)
            url = str(existing.get("url") or url)
        status = content_status(text)
        kind = source_type(title, url, text)
        if kind == "notebooklm-synthesis":
            url = ""
            authors = "NotebookLM-assisted synthesis"
        topics = classify_topics(title, text, kind)
        quality = classify_quality(kind, url, title)
        relevance = classify_relevance(title, text, topics, status, kind)
        priority = priority_for(relevance, quality, status)
        preserved_group = str(existing.get("original_group") or group)
        preserved_path = str(existing.get("original_path") or original_path)
        parsed.append({
            "path": path,
            "raw": raw,
            "text": text,
            "source_id": source_id,
            "title": title,
            "authors": authors,
            "year": str(existing.get("year") or extract_year(title, text)),
            "url": url,
            "domain": domain_of(url),
            "source_type": kind,
            "language": detect_language(text),
            "original_group": preserved_group,
            "original_path": preserved_path,
            "sha256": sha256,
            "bytes": len(raw),
            "lines": len(text.splitlines()),
            "words": len(re.findall(r"\b\w+\b", text, flags=re.UNICODE)),
            "content_status": status,
            "relevance": relevance,
            "quality": quality,
            "priority": priority,
            "topics": topics,
            "metadata_confidence": str(existing.get("metadata_confidence") or ("high" if match_score >= 0.95 else ("medium" if match_score >= 0.82 or url else "low"))),
            "notes": str(existing.get("notes") or (f"NotebookLM table match={match_score:.2f}" if match_score else "")),
            "review_status": str(existing.get("review_status") or "not-reviewed"),
            "canonical_url": canonicalize_url(url),
            "normalized_title": normalize_title(title),
        })

    duplicate_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in parsed:
        if item["content_status"] == "failed-load" or item["source_type"] == "notebooklm-synthesis":
            continue
        title_key = str(item["normalized_title"])
        if len(title_key) >= 12:
            duplicate_groups["title:" + title_key].append(item)
        canonical_url = str(item["canonical_url"])
        if is_specific_url(canonical_url):
            duplicate_groups["url:" + canonical_url].append(item)

    def canonical_score(item: dict[str, object]) -> tuple[int, int, int, str]:
        relevance_score = {"core": 5, "supporting": 4, "background": 3, "needs-review": 2, "out-of-scope": 1, "auxiliary-non-citable": 0, "needs-recovery": 0}.get(str(item["relevance"]), 0)
        status_score = {"full-text": 4, "partial": 3, "metadata-only": 1, "failed-load": 0}.get(str(item["content_status"]), 0)
        quality_score = {"high": 4, "medium": 3, "medium-low": 2, "low": 1}.get(str(item["quality"]), 0)
        return (relevance_score + quality_score, status_score, int(item["bytes"]), str(item["source_id"]))

    for key, items in duplicate_groups.items():
        unique_items = list({str(item["source_id"]): item for item in items}.values())
        if len(unique_items) < 2:
            continue
        canonical = max(unique_items, key=canonical_score)
        duplicate_kind = "same-specific-url" if key.startswith("url:") else "same-normalized-title"
        if not canonical.get("duplicate_type"):
            canonical["duplicate_type"] = "canonical-with-duplicates"
        for item in unique_items:
            if item is canonical or item.get("duplicate_of"):
                continue
            item["duplicate_type"] = duplicate_kind
            item["duplicate_of"] = canonical["source_id"]

    by_sha: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in parsed:
        if item["content_status"] != "failed-load":
            by_sha[str(item["sha256"])].append(item)
    for items in by_sha.values():
        if len(items) < 2:
            continue
        canonical = max(items, key=canonical_score)
        for item in items:
            if item is canonical:
                item["duplicate_type"] = item.get("duplicate_type") or "canonical-with-exact-duplicates"
            else:
                item["duplicate_type"] = "exact-content"
                item["duplicate_of"] = canonical["source_id"]

    used_names: set[str] = set()
    records: list[SourceRecord] = []
    for item in sorted(parsed, key=lambda row: (str(row["source_id"]), str(row["original_path"]))):
        base_name = f"{item['source_id']}__{slugify(str(item['title']))}.md"
        target_name = base_name
        counter = 2
        while target_name in used_names or ((SOURCES_DIR / target_name).exists() and (SOURCES_DIR / target_name) != item["path"]):
            stem = base_name[:-3]
            target_name = f"{stem}__record-{counter:02d}.md"
            counter += 1
        used_names.add(target_name)
        target = SOURCES_DIR / target_name
        if Path(item["path"]) != target:
            if target.exists():
                raise RuntimeError(f"Refusing to overwrite {target}")
            shutil.move(str(item["path"]), target)
        if hashlib.sha256(target.read_bytes()).hexdigest() != item["sha256"]:
            raise RuntimeError(f"Source bytes changed while moving {item['original_path']}")
        records.append(SourceRecord(
            source_id=str(item["source_id"]),
            title=str(item["title"]),
            authors=str(item["authors"]),
            year=str(item["year"]),
            url=str(item["url"]),
            domain=str(item["domain"]),
            source_type=str(item["source_type"]),
            language=str(item["language"]),
            original_group=str(item["original_group"]),
            original_path=str(item["original_path"]),
            normalized_path=target.relative_to(ROOT).as_posix(),
            content_sha256=str(item["sha256"]),
            bytes=int(item["bytes"]),
            lines=int(item["lines"]),
            words=int(item["words"]),
            content_status=str(item["content_status"]),
            relevance=str(item["relevance"]),
            quality=str(item["quality"]),
            priority=str(item["priority"]),
            curation_status=curation_status_for(str(item["relevance"]), str(item["content_status"]), str(item["source_type"]), str(item.get("duplicate_of", ""))),
            review_status=str(item.get("review_status", "not-reviewed")),
            topics=list(item["topics"]),
            duplicate_type=str(item.get("duplicate_type", "")),
            duplicate_of=str(item.get("duplicate_of", "")),
            metadata_confidence=str(item["metadata_confidence"]),
            notes=str(item["notes"]),
        ))
        item["normalized_path"] = target.relative_to(ROOT).as_posix()

    move_helper_reports(group_dirs)
    for group_dir in group_dirs:
        for path in sorted(group_dir.rglob("*"), reverse=True):
            if path.is_file():
                raise RuntimeError(f"Unexpected unmoved file remains: {path}")
            if path.is_dir():
                path.rmdir()
        group_dir.rmdir()

    fieldnames = list(records[0].as_dict().keys())
    with (CATALOG_DIR / "SOURCE_CATALOG.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(record.as_dict() for record in records)
    (CATALOG_DIR / "source_catalog.json").write_text(json.dumps([record.as_dict() for record in records], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_priority = Counter(record.priority for record in records)
    by_type = Counter(record.source_type for record in records)
    by_topic = Counter(topic for record in records for topic in record.topics)
    by_status = Counter(record.content_status for record in records)
    duplicates = [record for record in records if record.duplicate_of]

    catalog_lines = [
        "# Source Catalog", "",
        "This is the human-readable inventory of every Markdown source currently staged in this temporary repository. The CSV and JSON files are the machine-readable authorities.", "",
        f"- Total source records: **{len(records)}**",
        f"- Core priority: **{by_priority['P1-core']}**",
        f"- Supporting priority: **{by_priority['P2-supporting']}**",
        f"- Suspected duplicate records: **{len(duplicates)}**",
        f"- Failed or metadata-only records: **{by_status['failed-load'] + by_status['metadata-only']}**", "",
        "## Sources", "",
        "| ID | Title | Authors | Year | Type | Priority | Curation | Topics | Link | Duplicate of |",
        "|---|---|---|---:|---|---|---|---|---|---|",
    ]
    for record in sorted(records, key=lambda value: (value.priority, value.title.casefold(), value.source_id)):
        title = record.title.replace("|", "\\|")
        authors = (record.authors or "—").replace("|", "\\|")
        link = f"[source]({record.url})" if record.url else "—"
        topics = ", ".join(record.topics[:5]).replace("|", "\\|")
        catalog_lines.append(f"| `{record.source_id}` | {title} | {authors} | {record.year or '—'} | {record.source_type} | {record.priority} | {record.curation_status} | {topics} | {link} | {record.duplicate_of or '—'} |")
    (CATALOG_DIR / "SOURCE_CATALOG.md").write_text("\n".join(catalog_lines) + "\n", encoding="utf-8")

    duplicate_lines = [
        "# Duplicate Review", "",
        "No source was deleted automatically. The rows below identify exact or likely duplicate records. `duplicate_of` points to the preferred record selected by content completeness, relevance and source quality.", "",
        "| Record | Title | Duplicate type | Preferred record | Original path |",
        "|---|---|---|---|---|",
    ]
    for record in sorted(duplicates, key=lambda value: (value.duplicate_of, value.title.casefold())):
        duplicate_lines.append(f"| `{record.source_id}` | {record.title.replace('|', '\\|')} | {record.duplicate_type} | `{record.duplicate_of}` | `{record.original_path}` |")
    if not duplicates:
        duplicate_lines.append("| — | No duplicates detected | — | — | — |")
    (CATALOG_DIR / "DUPLICATE_REVIEW.md").write_text("\n".join(duplicate_lines) + "\n", encoding="utf-8")

    incomplete = [record for record in records if record.content_status in {"failed-load", "metadata-only", "partial"}]
    incomplete_lines = [
        "# Failed or Incomplete Sources", "",
        "These records are preserved for provenance but are not safe to use as evidence until replaced or verified.", "",
        "| ID | Title | Status | URL | Action |",
        "|---|---|---|---|---|",
    ]
    for record in sorted(incomplete, key=lambda value: (value.content_status, value.title.casefold())):
        action = "Re-import the source or obtain the original PDF/HTML" if record.content_status == "failed-load" else "Verify completeness before use"
        link = f"[source]({record.url})" if record.url else "—"
        incomplete_lines.append(f"| `{record.source_id}` | {record.title.replace('|', '\\|')} | {record.content_status} | {link} | {action} |")
    (CATALOG_DIR / "FAILED_OR_INCOMPLETE_SOURCES.md").write_text("\n".join(incomplete_lines) + "\n", encoding="utf-8")

    gap_lines = [
        "# Coverage Gaps and Verification Targets", "",
        "This file is a research queue, not an automatic inclusion list. Presence is inferred from titles and must be verified from the actual full text.", "",
        "| Target | Why it matters | Current status |",
        "|---|---|---|",
    ]
    for target, reason in KNOWN_COVERAGE_TARGETS:
        tokens = [token for token in normalize_title(target).split() if len(token) > 3]
        present = any(sum(token in normalize_title(record.title) for token in tokens) >= max(1, len(tokens) - 1) for record in records)
        gap_lines.append(f"| {target} | {reason} | {'present; verify quality/version' if present else 'missing or not clearly identified'} |")
    gap_lines.extend(["", "## Topic counts", "", "| Topic | Records |", "|---|---:|"])
    for topic, count in by_topic.most_common():
        gap_lines.append(f"| {topic} | {count} |")
    (CATALOG_DIR / "COVERAGE_GAPS.md").write_text("\n".join(gap_lines) + "\n", encoding="utf-8")

    assessment = """# Assessment of NotebookLM Group Reports

The two audit reports and two extracted-reference CSV files were reviewed before source reorganization.

## What they are useful for

- discovering possible duplicates and alternate versions;
- identifying broad topic clusters;
- surfacing candidate papers, theses and repositories;
- providing an initial list of likely irrelevant or low-value material.

## What they are not

They are not authoritative bibliography records and their recommendations are not final research decisions.

- Group 1's report refers to 280 sources, while the repository export contains 285 Group 1 source files.
- Group 2's report refers to a much larger NotebookLM collection, while the repository export currently contains 78 Group 2 source files.
- The CSV files include references cited inside uploaded documents, not only the uploaded source set.
- Some suggested additions are future, unverified, secondary, duplicated, or potentially outside the final bounded research scope.
- Proposed deletions were converted into relevance/priority signals; no source was silently deleted.

The actual files, their hashes, the normalized catalog and later full-text review are the source of truth.
"""
    (CATALOG_DIR / "NOTEBOOKLM_REPORT_ASSESSMENT.md").write_text(assessment, encoding="utf-8")

    taxonomy_lines = ["# Tag Taxonomy", "", "Tags describe content and may overlap. Folder placement does not encode topics.", ""]
    for topic, patterns in TOPIC_RULES.items():
        taxonomy_lines.append(f"- `{topic}` — detected from: {', '.join(patterns[:4])}")
    (CATALOG_DIR / "TAG_TAXONOMY.md").write_text("\n".join(taxonomy_lines) + "\n", encoding="utf-8")

    parsed_by_id = {str(item["source_id"]): item for item in parsed}
    ranked_candidates = sorted(
        (
            record for record in records
            if record.content_status == "full-text"
            and record.relevance in {"core", "supporting"}
            and record.quality in {"high", "medium"}
            and not record.duplicate_of
            and record.source_type != "notebooklm-synthesis"
        ),
        key=lambda record: (
            0 if record.priority == "P1-core" else 1,
            -sum(topic in {"robust-rl", "resilience-recovery", "nonstationarity", "gridworld", "evaluation-statistics"} for topic in record.topics),
            record.title.casefold(),
        ),
    )

    selected: list[tuple[SourceRecord, str]] = []
    needs_manual_excerpt: list[SourceRecord] = []
    for record in ranked_candidates:
        item = parsed_by_id[record.source_id]
        excerpt = select_excerpt(str(item["text"]), record.topics)
        if excerpt and len(selected) < 40:
            selected.append((record, excerpt))
        elif not excerpt:
            needs_manual_excerpt.append(record)

    excerpt_lines = [
        "# Useful Excerpts and Curation Leads", "",
        "This is an initial research-triage layer generated from the uploaded Markdown. It does **not** replace full-text review and is **not citation-ready** unless the passage is checked against the original source and page/section information is recorded.", "",
        f"Machine-selected passages: **{len(selected)}**. High-priority sources requiring manual excerpt selection are listed in `REVIEW_QUEUE.md`.", "",
    ]
    for record, excerpt in selected:
        excerpt_lines.extend([
            f"## {record.source_id} — {record.title}", "",
            f"- **Priority:** {record.priority}",
            f"- **Topics:** {', '.join(record.topics)}",
            f"- **Source:** {record.url or 'URL not extracted'}",
            f"- **Markdown:** `{record.normalized_path}`",
            "- **Review status:** machine-selected; full-text verification pending", "",
            "> " + excerpt.replace("\n", " "), "",
        ])
    (CURATION_DIR / "USEFUL_EXCERPTS.md").write_text("\n".join(excerpt_lines) + "\n", encoding="utf-8")

    queue_lines = [
        "# Manual Curation Queue", "",
        "High-value sources for which no reliable paragraph could be selected automatically. Review the full Markdown and original source before adding a verified note or excerpt.", "",
        "| ID | Title | Priority | Topics | Markdown |",
        "|---|---|---|---|---|",
    ]
    for record in needs_manual_excerpt:
        queue_lines.append(f"| `{record.source_id}` | {record.title.replace('|', '\\|')} | {record.priority} | {', '.join(record.topics)} | `{record.normalized_path}` |")
    (CURATION_DIR / "REVIEW_QUEUE.md").write_text("\n".join(queue_lines) + "\n", encoding="utf-8")

    (CURATION_DIR / "README.md").write_text("""# Curation

`USEFUL_EXCERPTS.md` contains machine-selected passages worth reviewing. `REVIEW_QUEUE.md` lists high-priority sources that need manual excerpt selection. Every retained item must later receive source verification, page/section information where available, a paraphrased note, thesis-use labels and a decision to keep, replace or exclude.
""", encoding="utf-8")

    (ROOT / "sources" / "README.md").write_text("""# Source Markdown Archive

All uploaded NotebookLM source Markdown files live flat in `sources/markdown/`. Their bytes are preserved during normalization. Filenames use stable source IDs and readable slugs; topic classification, original group/path, links, authors, duplicate status and quality signals live in `catalog/`.

Do not edit source Markdown for ordinary notes. Put interpretation and thesis-use material in `curation/`.
""", encoding="utf-8")

    (IMPORTS_DIR / "README.md").write_text("""# NotebookLM Import Reports

Each `group-XX/` directory preserves the two group-level files supplied by NotebookLM:

- `source-audit.md` — duplicate/removal/addition suggestions;
- `extracted-reference-table.csv` — references extracted from the group.

These files are provenance and discovery aids. They do not override the normalized source catalog or verified full-text review.
""", encoding="utf-8")

    readme = f"""# ThesisBibliography

Temporary staging repository for literature collected through Gemini NotebookLM for the thesis **“Comparison and Evaluation of Resilient AI Agents in Uncertain Environments.”**

## Current organization

- `sources/markdown/` — all {len(records)} uploaded source Markdown files in one flat archive;
- `catalog/SOURCE_CATALOG.md` — readable master index;
- `catalog/SOURCE_CATALOG.csv` and `catalog/source_catalog.json` — machine-readable authorities;
- `catalog/DUPLICATE_REVIEW.md` — suspected duplicates, retained rather than deleted;
- `catalog/FAILED_OR_INCOMPLETE_SOURCES.md` — sources requiring re-import or verification;
- `catalog/COVERAGE_GAPS.md` — missing/uncertain literature targets;
- `curation/USEFUL_EXCERPTS.md` — initial useful passages and research leads;
- `curation/REVIEW_QUEUE.md` — high-value sources requiring manual excerpt selection;
- `imports/notebooklm/` — original group audits and extracted reference tables;
- `scripts/organize_sources.py` — repeatable intake normalizer.

## Working rule

Search and writing work from the catalog, curated excerpts and source Markdown. Group reports are advisory. Original PDFs will be archived later in the main thesis repository and linked by source ID.

## Intake rule for future groups

Add each new NotebookLM export as `GroupN/GroupNFiles/*.md` plus its two group-level helper files. Run `python scripts/organize_sources.py` on a branch, review the regenerated catalog and merge only after validation.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    report_lines = [
        "# Organization Report", "",
        f"- Source records preserved: **{len(records)}**",
        f"- Source bytes preserved: **{sum(record.bytes for record in records):,}**",
        f"- Source groups represented: **{len({record.original_group for record in records})}**",
        f"- Suspected duplicates retained and linked: **{len(duplicates)}**",
        f"- Failed loads: **{by_status['failed-load']}**",
        f"- Metadata-only sources: **{by_status['metadata-only']}**",
        f"- Full-text sources: **{by_status['full-text']}**",
        f"- Non-citable NotebookLM syntheses: **{by_type['notebooklm-synthesis']}**", "",
        "## Priority distribution", "",
    ]
    for priority, count in sorted(by_priority.items()):
        report_lines.append(f"- `{priority}`: {count}")
    report_lines.extend(["", "## Source type distribution", ""])
    for kind, count in by_type.most_common():
        report_lines.append(f"- `{kind}`: {count}")
    report_lines.extend([
        "", "## Validation", "",
        "- every source file is located directly under `sources/markdown/`;",
        "- every source has one catalog record and SHA-256;",
        "- source bytes were checked before and after moving;",
        "- no suspected duplicate or out-of-scope item was deleted automatically;",
        "- original NotebookLM helper files were preserved under `imports/notebooklm/`.",
    ])
    (CATALOG_DIR / "ORGANIZATION_REPORT.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    normalized_files = sorted(SOURCES_DIR.glob("*.md"))
    if len(normalized_files) != len(records):
        raise RuntimeError(f"Expected {len(records)} normalized files, found {len(normalized_files)}")
    catalog_paths = {record.normalized_path for record in records}
    actual_paths = {path.relative_to(ROOT).as_posix() for path in normalized_files}
    if catalog_paths != actual_paths:
        raise RuntimeError("Catalog paths do not match normalized source files")
    for record in records:
        path = ROOT / record.normalized_path
        if hashlib.sha256(path.read_bytes()).hexdigest() != record.content_sha256:
            raise RuntimeError(f"Catalog checksum mismatch: {record.normalized_path}")

    if group_dirs and os.environ.get("BIBLIOGRAPHY_STABILIZATION_PASS") != "1":
        os.environ["BIBLIOGRAPHY_STABILIZATION_PASS"] = "1"
        return main()

    print(f"Organized {len(records)} source files.")
    print(f"Catalog: {CATALOG_DIR / 'SOURCE_CATALOG.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
