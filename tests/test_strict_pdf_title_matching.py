import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from originals_common import PdfInfo, title_score


class StrictPdfTitleMatchingTests(unittest.TestCase):
    def test_generic_reinforcement_learning_title_cannot_identify_pdf(self):
        info = PdfInfo(
            title="Reinforcement Learning and Stochastic Games",
            text="Reinforcement Learning is discussed throughout this document.",
        )
        score = title_score(
            "Reinforcement Learning",
            Path("Reinforcement Learning and stochastic games.pdf"),
            info,
        )
        self.assertEqual(0.0, score)

    def test_generic_ai_heading_in_body_cannot_identify_unrelated_pdf(self):
        info = PdfInfo(
            title="Logic Programming Techniques with Prolog",
            text="Chapter 7 includes an introduction to Τεχνητή νοημοσύνη and expert systems.",
        )
        score = title_score(
            "Τεχνητή νοημοσύνη",
            Path("LPTechniquesProlog_ΚΟΥ.pdf"),
            info,
        )
        self.assertEqual(0.0, score)

    def test_body_occurrence_does_not_create_title_identity(self):
        info = PdfInfo(
            title="A Completely Different Technical Monograph",
            text=(
                "Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations "
                "is cited in the introduction."
            ),
        )
        score = title_score(
            "Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations",
            Path("different-monograph.pdf"),
            info,
        )
        self.assertLess(score, 0.90)

    def test_distinctive_exact_metadata_title_remains_matchable(self):
        title = "Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations"
        info = PdfInfo(title=title, text=title)
        score = title_score(title, Path("download.pdf"), info)
        self.assertGreaterEqual(score, 0.99)

    def test_distinctive_exact_filename_title_remains_matchable(self):
        title = "Scaling Up Robust MDPs by Reinforcement Learning"
        info = PdfInfo(title="", text="")
        score = title_score(title, Path("Scaling Up Robust MDPs by Reinforcement Learning.pdf"), info)
        self.assertGreaterEqual(score, 0.97)


if __name__ == "__main__":
    unittest.main()
