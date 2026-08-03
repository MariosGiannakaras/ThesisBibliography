from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from validate_research_material_review import REQUIRED_FIELDS, validate  # noqa: E402


class ResearchMaterialReviewValidationTests(unittest.TestCase):
    def write_csv(self, path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def test_complete_identification_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inventory = root / "inventory.csv"
            review = root / "review.csv"
            self.write_csv(inventory, ["material_id"], [{"material_id": "MAT-ABCDEF1234"}])
            self.write_csv(review, REQUIRED_FIELDS, [{
                "material_id": "MAT-ABCDEF1234",
                "canonical_title": "Example title",
                "authors": "Example Author",
                "year": "2025",
                "url": "https://example.org/item",
                "identification_status": "identified",
                "confidence": "high",
                "thesis_relevance": "medium",
                "notes": "Verified from the title page.",
            }])
            self.assertEqual(validate(inventory, review), [])

    def test_identified_material_requires_bibliographic_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inventory = root / "inventory.csv"
            review = root / "review.csv"
            self.write_csv(inventory, ["material_id"], [{"material_id": "MAT-ABCDEF1234"}])
            self.write_csv(review, REQUIRED_FIELDS, [{
                "material_id": "MAT-ABCDEF1234",
                "canonical_title": "",
                "authors": "",
                "year": "",
                "url": "",
                "identification_status": "identified",
                "confidence": "high",
                "thesis_relevance": "unreviewed",
                "notes": "",
            }])
            errors = validate(inventory, review)
            self.assertTrue(any("missing canonical_title" in error for error in errors))
            self.assertTrue(any("missing authors" in error for error in errors))
            self.assertTrue(any("must have thesis relevance" in error for error in errors))

    def test_registry_must_cover_exact_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inventory = root / "inventory.csv"
            review = root / "review.csv"
            self.write_csv(inventory, ["material_id"], [
                {"material_id": "MAT-ABCDEF1234"},
                {"material_id": "MAT-0123456789"},
            ])
            self.write_csv(review, REQUIRED_FIELDS, [{
                "material_id": "MAT-ABCDEF1234",
                "canonical_title": "",
                "authors": "",
                "year": "",
                "url": "",
                "identification_status": "pending",
                "confidence": "",
                "thesis_relevance": "unreviewed",
                "notes": "",
            }])
            errors = validate(inventory, review)
            self.assertTrue(any("Review registry IDs do not match inventory" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
