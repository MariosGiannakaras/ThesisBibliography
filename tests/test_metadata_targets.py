from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "tools" / "metadata.py"
NEXT_SOURCES_PATH = ROOT / "tools" / "next_sources.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Δεν ήταν δυνατή η φόρτωση του {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NextSourcesTests(unittest.TestCase):
    def test_existing_known_targets_are_marked_present(self) -> None:
        metadata = load_module(METADATA_PATH, "metadata_under_test")
        rows = [
            {"Τίτλος": "NovGrid: A Flexible Grid World for Evaluating Agent Response to Novelty"},
            {"Τίτλος": "CARL: A Benchmark for Contextual and Adaptive Reinforcement Learning"},
        ]

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "προς-προσθήκη.md"
            with (
                mock.patch.object(metadata, "NEXT", output),
                mock.patch.object(metadata, "mine_references", return_value=[]),
            ):
                metadata.write_next_sources(rows)

            text = output.read_text(encoding="utf-8")

        self.assertIn(
            "- [x] [NovGrid: A Flexible Grid World for Evaluating Agent Response to Novelty]",
            text,
        )
        self.assertIn(
            "- [x] [CARL: A Benchmark for Contextual and Adaptive Reinforcement Learning]",
            text,
        )
        self.assertIn("- [ ] [AI Safety Gridworlds]", text)
        self.assertIn("Δεν βρέθηκαν ακόμη επαναλαμβανόμενες εξωτερικές αναφορές.", text)

    def test_title_matching_is_case_and_punctuation_insensitive(self) -> None:
        metadata = load_module(METADATA_PATH, "metadata_title_test")
        left = "CARL: A Benchmark for Contextual and Adaptive Reinforcement Learning"
        right = "carl — a benchmark for contextual and adaptive reinforcement learning"
        self.assertGreaterEqual(metadata.title_similarity(left, right), 0.9)

    def test_pmlr_landing_page_and_pdf_share_the_same_identifier(self) -> None:
        suggestions = load_module(NEXT_SOURCES_PATH, "suggestions_identifier_test")
        landing = "https://proceedings.mlr.press/v232/alami23a.html"
        pdf = "https://proceedings.mlr.press/v232/alami23a/alami23a.pdf"
        self.assertEqual(
            suggestions.canonical_identifier(landing),
            suggestions.canonical_identifier(pdf),
        )

    def test_source_header_identifier_marks_known_target_present(self) -> None:
        metadata = load_module(METADATA_PATH, "metadata_identifier_test")
        suggestions = load_module(NEXT_SOURCES_PATH, "suggestions_augment_test")
        rows = [
            {
                "Κωδικός": "SRC-TEST",
                "Τίτλος": "R-BOCPD for Nonstationary MDPs",
                "Σύνδεσμος": "",
            }
        ]

        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory)
            (sources / "SRC-TEST.md").write_text(
                "> Source: https://proceedings.mlr.press/v232/alami23a/alami23a.pdf\n",
                encoding="utf-8",
            )
            with mock.patch.object(suggestions, "SOURCES", sources):
                augmented = suggestions.augment_rows_with_identifier_matches(rows, metadata)

        titles = [row.get("Τίτλος", "") for row in augmented]
        self.assertIn(
            "Restarted Bayesian Online Change-point Detection for Non-Stationary Markov Decision Processes",
            titles,
        )

    def test_technical_arxiv_conversion_links_are_not_candidates(self) -> None:
        suggestions = load_module(NEXT_SOURCES_PATH, "suggestions_filter_test")
        self.assertFalse(
            suggestions.is_bibliographic_candidate(
                "https://github.com/arXiv/html_feedback/issues"
            )
        )
        self.assertFalse(
            suggestions.is_bibliographic_candidate(
                "https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML"
            )
        )
        self.assertTrue(
            suggestions.is_bibliographic_candidate(
                "https://proceedings.mlr.press/v232/alami23a.html"
            )
        )


if __name__ == "__main__":
    unittest.main()
