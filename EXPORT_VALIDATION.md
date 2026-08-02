# Export validation report

- Export validation exit code: **1**
- Export unit-test exit code: **1**

## Export validation

```text
Η εξαγωγή απέτυχε:
- SRC-7C18826BEE: λείπει σημασιολογική ενότητα ανάλυσης για «thesis use»
- SRC-A5DF23299C: λείπει σημασιολογική ενότητα ανάλυσης για «limitations»
- SRC-701E163AC8: λείπει σημασιολογική ενότητα ανάλυσης για «limitations»
- SRC-701E163AC8: λείπει δομημένη ενότητα evidence (Τεκμήριο/Evidence/E#)
- SRC-701E163AC8: λείπει πραγματική ακριβής θέση στο evidence
- SRC-701E163AC8: λείπει πραγματικός ισχυρισμός που υποστηρίζεται
- SRC-CA06A28C0B: λείπει σημασιολογική ενότητα ανάλυσης για «thesis use»
- SRC-CA06A28C0B: λείπει δομημένη ενότητα evidence (Τεκμήριο/Evidence/E#)
- SRC-CA06A28C0B: λείπει πραγματική ακριβής θέση στο evidence
- SRC-CA06A28C0B: λείπει πραγματικός ισχυρισμός που υποστηρίζεται
- SRC-EA5D0E318E: λείπει σημασιολογική ενότητα ανάλυσης για «thesis use»
- SRC-EA5D0E318E: λείπει δομημένη ενότητα evidence (Τεκμήριο/Evidence/E#)
- SRC-EA5D0E318E: λείπει πραγματική ακριβής θέση στο evidence
- SRC-EA5D0E318E: λείπει πραγματικός ισχυρισμός που υποστηρίζεται
```

## Export unit tests

```text
test_cross_language_evidence_is_rejected (tests.test_thesis_export.ThesisExportTests.test_cross_language_evidence_is_rejected) ... ok
test_empty_selection_is_valid (tests.test_thesis_export.ThesisExportTests.test_empty_selection_is_valid) ... ok
test_english_structured_source_language_evidence_is_accepted (tests.test_thesis_export.ThesisExportTests.test_english_structured_source_language_evidence_is_accepted) ... ok
test_template_only_files_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_template_only_files_cannot_be_exported) ... FAIL
test_unchecked_original_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_unchecked_original_cannot_be_exported) ... ok
test_unverified_source_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_unverified_source_cannot_be_exported) ... ok
test_verified_source_builds_english_path_package (tests.test_thesis_export.ThesisExportTests.test_verified_source_builds_english_path_package) ... ok

======================================================================
FAIL: test_template_only_files_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_template_only_files_cannot_be_exported)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/ThesisBibliography/ThesisBibliography/tests/test_thesis_export.py", line 193, in test_template_only_files_cannot_be_exported
    self.assertTrue(any("πραγματική ακριβής θέση" in error for error in errors))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 7 tests in 0.012s

FAILED (failures=1)
```
