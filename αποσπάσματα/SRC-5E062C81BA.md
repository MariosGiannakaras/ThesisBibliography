# SRC-5E062C81BA — verified excerpts

## Robust RL as min–max learning

Η εργασία εισάγει control agent και worst-case disturber, μεταφέροντας H∞/differential-game ideas στο RL ώστε η policy να μειώνει την ευαισθησία σε disturbance/model error.

**Χρήση:** historical primary source για robust-policy class.

## Environmental parameter change

Στο nonlinear pendulum experiment, η robust policy διατηρεί λειτουργικότητα όταν αλλάζουν mass και friction, ενώ ο nominal comparator αποτυγχάνει στο συγκεκριμένο setup.

**Boundary:** πρόκειται για robustness σε parameter shift, όχι formal repeated-changepoint adaptation benchmark.

## Zero-update robustness

Η ανθεκτικότητα προκύπτει από το training objective με worst disturbance. Δεν απαιτείται explicit detector τη στιγμή της αλλαγής.

**Thesis-ready distinction:** άμεση disturbed performance με frozen parameters πρέπει να μετριέται πριν αποδοθεί οποιαδήποτε βελτίωση σε online adaptation.

## Experimental decomposition

Μετά από shift μετρώνται:

- immediate/frozen post-change return,
- return μετά από continued updates,
- clean nominal performance,
- robustness conservativeness cost.

## Scope boundary

Η H∞ disturbance class και continuous-control assumptions δεν μεταφέρονται αυτούσιες σε tabular GridWorld. Η εργασία δεν αποδεικνύει ότι robust training μειώνει detection delay ή relearning time.