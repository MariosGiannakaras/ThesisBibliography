#!/usr/bin/env python3
"""Ανανεώνει τη λίστα προτεινόμενων πηγών χωρίς δικτυακό enrichment."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
CATALOG_CSV = ROOT / "κατάλογος" / "πηγές.csv"
METADATA_SCRIPT = ROOT / "εργαλεία" / "μεταδεδομένα.py"


def load_metadata_module() -> ModuleType:
    """Φορτώνει τις κοινές συναρτήσεις χωρίς να εκτελεί το πλήρες enrichment."""
    spec = importlib.util.spec_from_file_location(
        "thesis_bibliography_metadata",
        METADATA_SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Δεν ήταν δυνατή η φόρτωση του {METADATA_SCRIPT}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    with CATALOG_CSV.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    metadata = load_metadata_module()
    metadata.write_next_sources(rows)
    print(f"Ανανεώθηκε η λίστα επόμενων πηγών από {len(rows)} εγγραφές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
