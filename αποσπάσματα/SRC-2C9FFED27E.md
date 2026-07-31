# SRC-2C9FFED27E — Επαληθευμένα τεκμήρια

## 1. Robust constraints και task objective

Σε RCMDP, η policy πρέπει να βελτιστοποιεί task utility και να ικανοποιεί constraints για τα worst-case transition models του uncertainty set. Nominal feasibility στον simulator δεν εγγυάται feasibility μετά από model mismatch.

## 2. Διαφορετικά worst-case models

Το transition model που χειροτερεύει την task objective μπορεί να διαφέρει από εκείνο που μεγιστοποιεί μία constraint cost. Επομένως ένα απλοποιημένο κοινό worst-case backup ή μία άκριτη Lagrangian σύνθεση μπορεί να είναι λανθασμένη.

## 3. Feasibility-first optimization

Η RNPG λογική μειώνει constraint violations όταν υπάρχουν και βελτιστοποιεί την robust objective όταν η policy είναι feasible. Αυτό υποστηρίζει χωριστή αναφορά utility και violation margins, όχι έναν ενιαίο aggregate score.

## 4. Computational cost

Η αποφυγή binary search και η KL-regularized update μειώνουν iteration/wall-clock cost έναντι του συγκρινόμενου epigraph solver. Η σύγκριση algorithms πρέπει να περιλαμβάνει compute, όχι μόνο final return.

## 5. Scope boundary

Η εργασία αφορά static robust constrained optimization. Δεν παρέχει changepoint detector, recovery-delay metric ή continued-learning mechanism μετά από repeated environmental shifts.

## Προτεινόμενη χρήση

- Ορισμός robust feasibility και robust constraint cost.
- Threat to validity για nominal-only safety evaluation.
- Computational trade-off section.
- Αιτιολόγηση χωριστών utility, violation και feasibility metrics.