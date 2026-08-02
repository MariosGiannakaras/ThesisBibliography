# Export validation report

- Export validation exit code: **0**
- Export unit-test exit code: **0**

## Export validation

```text
Το μητρώο εξαγωγής είναι έγκυρο: 104 επαληθευμένες πηγές.
```

## Export unit tests

```text
test_cross_language_evidence_is_rejected (tests.test_thesis_export.ThesisExportTests.test_cross_language_evidence_is_rejected) ... ok
test_empty_selection_is_valid (tests.test_thesis_export.ThesisExportTests.test_empty_selection_is_valid) ... ok
test_english_structured_source_language_evidence_is_accepted (tests.test_thesis_export.ThesisExportTests.test_english_structured_source_language_evidence_is_accepted) ... ok
test_template_only_files_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_template_only_files_cannot_be_exported) ... ok
test_unchecked_original_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_unchecked_original_cannot_be_exported) ... ok
test_unverified_source_cannot_be_exported (tests.test_thesis_export.ThesisExportTests.test_unverified_source_cannot_be_exported) ... ok
test_verified_source_builds_english_path_package (tests.test_thesis_export.ThesisExportTests.test_verified_source_builds_english_path_package) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.020s

OK
```
