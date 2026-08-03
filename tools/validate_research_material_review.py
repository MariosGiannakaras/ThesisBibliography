#!/usr/bin/env python3
"""Validate semantic completeness of the research-material identification registry."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "catalog" / "research-materials.csv"
REVIEW = ROOT / "catalog" / "research-material-review.csv"

REQUIRED_FIELDS = [
    "material_id",
    "canonical_title",
    "authors",
    "year",
    "url",
    "identification_status",
    "confidence",
    "thesis_relevance",
    "notes",
]
IDENTIFIED_STATUSES = {"identified", "identified-from-file"}
ALLOWED_STATUSES = IDENTIFIED_STATUSES | {"pending"}
ALLOWED_CONFIDENCE = {"high", "medium", "low", ""}
ALLOWED_RELEVANCE = {"high", "medium", "low", "unreviewed"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def valid_url(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(inventory_path: Path = INVENTORY, review_path: Path = REVIEW) -> list[str]:
    errors: list[str] = []
    if not inventory_path.exists():
        return [f"Missing inventory: {inventory_path}"]
    if not review_path.exists():
        return [f"Missing review registry: {review_path}"]

    _, inventory_rows = read_csv(inventory_path)
    fields, review_rows = read_csv(review_path)
    missing_fields = [field for field in REQUIRED_FIELDS if field not in fields]
    if missing_fields:
        errors.append("Missing review fields: " + ", ".join(missing_fields))

    inventory_ids = {row.get("material_id", "").strip() for row in inventory_rows}
    review_ids: set[str] = set()
    for line_number, row in enumerate(review_rows, start=2):
        material_id = row.get("material_id", "").strip()
        if not material_id:
            errors.append(f"Line {line_number}: missing material_id")
            continue
        if material_id in review_ids:
            errors.append(f"Duplicate review material_id: {material_id}")
        review_ids.add(material_id)

        status = row.get("identification_status", "").strip()
        confidence = row.get("confidence", "").strip()
        relevance = row.get("thesis_relevance", "").strip()
        year = row.get("year", "").strip()
        url = row.get("url", "").strip()

        if status not in ALLOWED_STATUSES:
            errors.append(f"{material_id}: invalid identification_status {status!r}")
        if confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"{material_id}: invalid confidence {confidence!r}")
        if relevance not in ALLOWED_RELEVANCE:
            errors.append(f"{material_id}: invalid thesis_relevance {relevance!r}")
        if not valid_url(url):
            errors.append(f"{material_id}: invalid URL {url!r}")

        if status in IDENTIFIED_STATUSES:
            for field in ("canonical_title", "authors", "year", "confidence", "notes"):
                if not row.get(field, "").strip():
                    errors.append(f"{material_id}: identified material is missing {field}")
            if year and not re.fullmatch(r"(?:19|20)\d{2}", year):
                errors.append(f"{material_id}: invalid identified year {year!r}")
            if relevance == "unreviewed":
                errors.append(f"{material_id}: identified material must have thesis relevance")
        elif status == "pending":
            if confidence:
                errors.append(f"{material_id}: pending material must not claim confidence")

    if review_ids != inventory_ids:
        errors.append(
            "Review registry IDs do not match inventory: "
            f"missing={sorted(inventory_ids-review_ids)}, extra={sorted(review_ids-inventory_ids)}"
        )
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Research material identification registry is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
