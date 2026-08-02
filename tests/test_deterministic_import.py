import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location(
    "deterministic_import_tool", TOOLS / "deterministic_import_sources.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DeterministicImportTests(unittest.TestCase):
    def test_same_hash_produces_same_source_id(self):
        digest = "0123456789ABCDEF" * 4
        first = MODULE.deterministic_source_id(set(), digest)
        second = MODULE.deterministic_source_id(set(), digest)
        self.assertEqual("SRC-0123456789", first)
        self.assertEqual(first, second)

    def test_prefix_collision_uses_next_digest_window_deterministically(self):
        digest = "0123456789ABCDEF" * 4
        source_id = MODULE.deterministic_source_id({"SRC-0123456789"}, digest)
        self.assertEqual("SRC-123456789A", source_id)

    def test_invalid_digest_fails_closed(self):
        with self.assertRaises(ValueError):
            MODULE.deterministic_source_id(set(), "not-a-sha")

    def test_tracking_hash_only_tracks_incoming_markdown(self):
        original_incoming = MODULE.import_sources.INCOMING
        original_sha = MODULE._ORIGINAL_SHA256
        original_current = MODULE._CURRENT_INCOMING_HASH
        try:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                incoming = root / "new-sources"
                incoming.mkdir()
                source = incoming / "paper.md"
                other = root / "other.md"
                source.write_text("source content", encoding="utf-8")
                other.write_text("other content", encoding="utf-8")
                MODULE.import_sources.INCOMING = incoming
                MODULE._CURRENT_INCOMING_HASH = None
                expected = original_sha(source)
                MODULE.tracking_sha256(source)
                self.assertEqual(expected, MODULE._CURRENT_INCOMING_HASH)
                MODULE.tracking_sha256(other)
                self.assertEqual(expected, MODULE._CURRENT_INCOMING_HASH)
        finally:
            MODULE.import_sources.INCOMING = original_incoming
            MODULE._CURRENT_INCOMING_HASH = original_current


if __name__ == "__main__":
    unittest.main()
