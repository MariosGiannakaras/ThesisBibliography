#!/usr/bin/env python3
"""Κοινή, συντηρητική ερμηνεία της canonical απόφασης μιας ανάλυσης."""
from __future__ import annotations

import re
from pathlib import Path

SELECTED_ROLES = {"κύρια", "υποστηρικτική", "υπόβαθρο"}
REJECTED_STATES = {"απόρριψη", "απορρίφθηκε", "rejected", "reject"}
VERIFIED_ANALYSIS_STATES = {"επαληθευμένη", "verified"}
YES_VALUES = {"ναι", "yes", "true", "1"}


def normalize(value: str | None) -> str:
    return (value or "").strip().casefold()


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"(?im)^\s*{re.escape(key)}\s*:\s*[\"']?(.*?)[\"']?\s*$", text)
    return normalize(match.group(1)) if match else ""


def decision_section(text: str) -> str:
    matches = list(
        re.finditer(
            r"(?im)^##\s+(?:Απόφαση|Κατάσταση επαλήθευσης|Τελική απόφαση)\s*$",
            text,
        )
    )
    if matches:
        return text[matches[-1].start():]
    return text[-3000:]


def infer_role(text: str) -> str:
    normalized = normalize(text)
    patterns = (
        r"(?:ρόλος στη διπλωματική|προτεινόμενος ρόλος|ρόλος)\s*:\s*\**\s*(κύρια|υποστηρικτική|υπόβαθρο)",
        r"(?:επιλογή|επιλέγεται|επαληθευμένη[^\n]{0,80}εξαγωγή\s+ναι)[^\n]{0,120}?\b(κύρια|υποστηρικτική|υπόβαθρο)\b",
        r"\bως\s+(κύρια|υποστηρικτική|υπόβαθρο)\s+(?:πηγή|αναφορά|τεκμήριο)",
    )
    for pattern in patterns:
        match = re.search(pattern, normalized, re.IGNORECASE)
        if match:
            return match.group(1)
    return ""


def infer_decision(text: str) -> str:
    """Επιστρέφει selected, rejected ή draft χωρίς να μαντεύει από γενικές αναφορές."""
    state = frontmatter_value(text, "κατάσταση")
    if state in REJECTED_STATES:
        return "rejected"

    section = normalize(decision_section(text))
    rejection_markers = (
        "**απόρριψη",
        "απόφαση:** απόρριψη",
        "απόφαση: απόρριψη",
        "απόρριψη λόγω",
        "απόρριψη ως",
        "δεν εξάγεται",
        "εξαγωγή όχι",
        "εξαγωγή: όχι",
        "ρόλος: απόρριψη",
    )
    if any(marker in section for marker in rejection_markers):
        return "rejected"

    if state in VERIFIED_ANALYSIS_STATES:
        return "selected"

    role = infer_role(text)
    selection_markers = (
        "**επιλογή",
        "επιλέγεται ως",
        "εξαγωγή ναι",
        "εξαγωγή: ναι",
        "**επαληθευμένη",
    )
    if role in SELECTED_ROLES and any(marker in section for marker in selection_markers):
        return "selected"
    if role in SELECTED_ROLES and "## απόφαση" in section:
        return "selected"
    return "draft"


def excerpt_is_verified(path: Path) -> bool:
    if not path.exists():
        return False
    text = normalize(path.read_text(encoding="utf-8", errors="replace"))
    return "κατάσταση: επαληθευμένο" in text and "ελεγχθέν-πρωτότυπο: ναι" in text


def analysis_original_checked(text: str) -> bool:
    return "ελεγχθέν-πρωτότυπο: ναι" in normalize(text)
