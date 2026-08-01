---
κωδικός: SRC-70AEC665B2
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-70AEC665B2 — verified excerpts

## Accuracy ≠ calibration

Η εργασία δείχνει ότι σύγχρονα neural networks μπορούν να έχουν υψηλή classification accuracy αλλά confidence scores που είναι overconfident και δεν αντιστοιχούν στην empirical correctness probability.

**Χρήση:** neural confidence δεν θεωρείται probability χωρίς calibration evidence.

## Reliability diagrams

Calibration μπορεί να εξεταστεί συγκρίνοντας empirical accuracy και mean confidence σε bins.

**Protocol implication:** neural context/detection arm χρειάζεται held-out calibration diagnostic, όχι μόνο accuracy/AUROC.

## ECE και MCE

ECE συνοψίζει weighted confidence–accuracy gaps, ενώ MCE εστιάζει στο μεγαλύτερο calibration gap.

**Boundary:** οι metrics εξαρτώνται από finite-sample estimation/binning και δεν αντικαθιστούν false-alarm/detection-delay evaluation.

## Temperature scaling

Η εργασία βρίσκει ότι temperature scaling είναι απλό αποτελεσματικό post-hoc calibration method στα classification benchmarks που μελετά.

**Χρήση:** μόνο για classifier-like scores με development labels· όχι αυθαίρετο calibration TD error ή prediction-error detector.

## Distribution shift caveat

Calibration σε stationary validation data δεν συνεπάγεται ότι confidence παραμένει calibrated μετά από environmental shift.

**Thesis-ready rule:** calibration split, changepoint test sequence και detector-threshold tuning παραμένουν διαχωρισμένα.