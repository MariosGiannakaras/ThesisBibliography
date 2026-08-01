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


def plain_markdown(value: str | None) -> str:
    return re.sub(r"[*_`]", "", normalize(value))


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"(?im)^\s*{re.escape(key)}\s*:\s*[\"']?(.*?)[\"']?\s*$", text)
    return normalize(match.group(1)) if match else ""


def decision_section(text: str) -> str:
    matches = list(
        re.finditer(
            r"(?im)^##\s+(?:Απόφαση|Κατάσταση επαλήθευσης|Τελική απόφαση|Decision|Final decision)\s*$",
            text,
        )
    )
    if matches:
        return text[matches[-1].start():]
    return text[-3000:]


def infer_role(text: str) -> str:
    normalized = plain_markdown(text)
    patterns = (
        r"(?:ρόλος στη διπλωματική|προτεινόμενος ρόλος|ρόλος|thesis role|role)\s*:\s*(κύρια|υποστηρικτική|υπόβαθρο|main|supporting|background)",
        r"(?:επιλογή|επιλέγεται|επαληθευμένη[^\n]{0,80}εξαγωγή\s+ναι)[^\n]{0,120}?\b(κύρια|υποστηρικτική|υπόβαθρο)\b",
        r"\bως\s+(κύρια|υποστηρικτική|υπόβαθρο)\s+(?:πηγή|αναφορά|τεκμήριο)",
    )
    role_aliases = {
        "main": "κύρια",
        "supporting": "υποστηρικτική",
        "background": "υπόβαθρο",
    }
    for pattern in patterns:
        match = re.search(pattern, normalized, re.IGNORECASE)
        if match:
            role = match.group(1)
            return role_aliases.get(role, role)
    return ""


def infer_decision(text: str) -> str:
    """Επιστρέφει selected, rejected ή draft χωρίς να μαντεύει από γενικές αναφορές."""
    state = frontmatter_value(text, "κατάσταση")
    if state in REJECTED_STATES:
        return "rejected"

    section = plain_markdown(decision_section(text))
    rejection_markers = (
        "απόφαση: απόρριψη",
        "απόρριψη λόγω",
        "απόρριψη ως",
        "δεν εξάγεται",
        "εκτός εξαγωγής",
        "εξαγωγή όχι",
        "εξαγωγή: όχι",
        "ρόλος: απόρριψη",
        "rejected from the curated",
        "rejected as",
        "decision: reject",
        "decision: rejected",
    )
    if any(marker in section for marker in rejection_markers):
        return "rejected"

    # Legacy analyses often use a dedicated Decision section whose first substantive
    # line is simply “Απόρριψη.”. Matching this only inside the decision section is
    # conservative and avoids treating ordinary discussion of rejection as a decision.
    if re.search(r"(?im)^\s*(?:απόρριψη|απορρίπτεται|reject|rejected)\b", section):
        return "rejected"

    full_plain = plain_markdown(text)
    if re.search(r"(?im)^\s*-?\s*ρόλος\s*:\s*απόρριψη\s*$", full_plain):
        return "rejected"
    if "απορρίπτεται από το thesis export gate" in full_plain:
        return "rejected"
    if "απορρίπτεται από το τρέχον scope" in full_plain:
        return "rejected"

    if state in VERIFIED_ANALYSIS_STATES:
        return "selected"

    role = infer_role(text)
    selection_markers = (
        "επιλογή",
        "επιλέγεται ως",
        "εξαγωγή ναι",
        "εξαγωγή: ναι",
        "επαληθευμένη",
        "selected as",
        "selected for",
    )
    if role in SELECTED_ROLES and any(marker in section for marker in selection_markers):
        return "selected"
    if role in SELECTED_ROLES and ("## απόφαση" in section or "## decision" in section or "## final decision" in section):
        return "selected"
    return "draft"


def excerpt_is_verified(path: Path) -> bool:
    if not path.exists():
        return False
    text = normalize(path.read_text(encoding="utf-8", errors="replace"))
    greek_verified = "κατάσταση: επαληθευμένο" in text and "ελεγχθέν-πρωτότυπο: ναι" in text
    english_verified = "status: verified" in text and "original-checked: yes" in text
    return greek_verified or english_verified


def analysis_original_checked(text: str) -> bool:
    normalized = normalize(text)
    return "ελεγχθέν-πρωτότυπο: ναι" in normalized or "original-checked: yes" in normalized
