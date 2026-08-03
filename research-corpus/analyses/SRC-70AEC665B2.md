# SRC-70AEC665B2 — On Calibration of Modern Neural Networks

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger
- **Έκδοση:** ICML 2017, PMLR 70
- **Τύπος:** primary neural confidence-calibration study
- **Ρόλος στη διπλωματική:** υποστηρικτική, μόνο για neural uncertainty/detection arm

## Αντικείμενο

Η εργασία μελετά αν τα confidence scores σύγχρονων neural classifiers αντιστοιχούν στην πραγματική πιθανότητα ορθής πρόβλεψης. Δείχνει ότι υψηλή accuracy δεν συνεπάγεται calibrated confidence και αξιολογεί post-hoc calibration methods, με temperature scaling ως ιδιαίτερα απλή και αποτελεσματική επιλογή στα datasets της εργασίας.

## Κύρια σημεία

- Modern neural networks μπορούν να είναι συστηματικά overconfident.
- Reliability diagrams συγκρίνουν empirical accuracy και confidence ανά bin.
- Expected Calibration Error (ECE) συνοψίζει weighted calibration gaps.
- Maximum Calibration Error (MCE) εστιάζει στο μεγαλύτερο observed gap.
- Temperature scaling αλλάζει confidence calibration χωρίς να αλλάζει την predicted class ordering.

## Συνάφεια

Η εργασία δεν είναι RL ούτε change-detection paper, αλλά θέτει σημαντικό restriction σε οποιοδήποτε neural uncertainty score χρησιμοποιηθεί ως trigger:

**confidence ≠ calibrated probability**.

Αν ένα neural detector ή context classifier χρησιμοποιεί softmax confidence/entropy, η διπλωματική δεν πρέπει να ονομάζει ένα threshold “90% certainty” χωρίς held-out calibration evidence.

## Πρωτόκολλο που προκύπτει

Εάν χρησιμοποιηθεί neural classifier/detector:

- κρατείται ξεχωριστό calibration split που δεν περιέχει final test changepoints,
- παρουσιάζεται reliability diagram ή equivalent calibration summary,
- αναφέρονται ECE/MCE ή άλλο pre-specified calibration metric,
- threshold tuning γίνεται μόνο σε development data,
- detection false-alarm rate και delay παραμένουν ξεχωριστές RL metrics.

Temperature scaling μπορεί να χρησιμοποιηθεί μόνο εάν υπάρχει πραγματικό classification target/context label. Δεν είναι γενικός τρόπος calibration arbitrary TD error ή novelty score.

## Περιορισμοί

- Supervised multiclass classification, όχι sequential RL.
- ECE εξαρτάται από binning και δεν αποτελεί πλήρη characterization calibration.
- Calibration υπό stationary held-out data δεν εγγυάται calibration μετά από distribution shift.
- Δεν παρέχει change detector ή adaptation mechanism.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή μόνο για neural detection/context experiments.** Στο tabular core δεν απαιτείται· χρησιμοποιείται για να αποφεύγονται ατεκμηρίωτες probabilistic ερμηνείες neural confidence scores.