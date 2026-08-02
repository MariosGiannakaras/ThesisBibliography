from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from decision_status import infer_decision  # noqa: E402


class DecisionStatusTests(unittest.TestCase):
    def test_explicit_greek_decision_is_not_hidden_by_later_verification_heading(self) -> None:
        text = """---
κατάσταση: επαληθευμένη
---

## Απόφαση

- **Ρόλος:** απόρριψη από ανεξάρτητη εξαγωγή
- **Εξαγωγή:** όχι

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
"""
        self.assertEqual(infer_decision(text), "rejected")

    def test_explicit_english_decision_is_not_hidden_by_later_notes(self) -> None:
        text = """---
κατάσταση: verified
---

## Final decision

Decision: rejected

## Κατάσταση επαλήθευσης

Status note only.
"""
        self.assertEqual(infer_decision(text), "rejected")

    def test_verified_selected_analysis_without_rejection_stays_selected(self) -> None:
        text = """---
κατάσταση: verified
---

## Decision

Role: supporting
Selected for thesis evidence.
"""
        self.assertEqual(infer_decision(text), "selected")


if __name__ == "__main__":
    unittest.main()
