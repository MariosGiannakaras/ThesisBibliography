# SRC-3C0F7CC819 — Online Robust Reinforcement Learning with Model Uncertainty

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Yue Wang, Shaofeng Zou
- **Έκδοση:** arXiv:2109.14523v2, 2021
- **Τύπος:** θεωρητική εργασία model-free robust RL
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Αντικείμενο

Η εργασία μελετά robust RL όταν το uncertainty set κεντράρεται σε ένα άγνωστο και πιθανώς misspecified MDP από το οποίο παρατηρείται μία online trajectory. Προτείνει incremental, sample-based estimation του uncertainty set και robust updates χωρίς generative model.

Παρουσιάζονται:

- tabular robust Q-learning,
- robust TDC με function approximation,
- convergence και finite-time error bounds.

## Κύρια αποτελέσματα

- Το robust Q-learning συγκλίνει στο optimal robust Q function υπό τις assumptions της εργασίας.
- Το robust TDC συγκλίνει ασυμπτωτικά σε stationary points.
- Οι error rates διατηρούν την τάξη μεγέθους των vanilla counterparts μέχρι σταθερούς παράγοντες.
- Η προσέγγιση μπορεί θεωρητικά να επεκταθεί σε TD, SARSA και άλλους gradient-TD algorithms.

## Συνάφεια

Αποτελεί άμεσο theoretical reference για tabular robust baseline που ενημερώνεται online και δεν απαιτεί πλήρες planning model. Αυτό είναι πιο κοντά στους περιορισμούς της διπλωματικής από deep robust-control architectures.

Ωστόσο, η εργασία δεν είναι change-detection method. Η policy βελτιστοποιείται έναντι model uncertainty set· δεν εντοπίζει ρητά changepoints, δεν αποθηκεύει regimes και δεν μετρά recovery delay μετά από abrupt αλλαγή.

## Πρωτόκολλο που προκύπτει

Για robust-Q comparator πρέπει να δηλώνονται:

- μορφή και ακτίνα uncertainty set,
- τρόπος εκτίμησης του nominal transition distribution,
- αν η ακτίνα είναι oracle, tuned ή data-derived,
- clean-environment return,
- disturbed return,
- conservativeness gap,
- computational overhead ανά update.

Η robust policy πρέπει να αξιολογηθεί και σε shifts εκτός του assumed uncertainty set, επειδή εντός-set robustness δεν συνεπάγεται resilience σε arbitrary structural change.

## Περιορισμοί

- Η αποθηκευμένη πηγή είναι abstract/metadata page και όχι πλήρες converted PDF, άρα τα chapter-ready claims περιορίζονται στα ρητά δηλωμένα αποτελέσματα.
- Πρόκειται για arXiv έκδοση.
- Η αβεβαιότητα αφορά misspecified model γύρω από nominal center, όχι repeated environment switching.
- Robust worst-case optimization μπορεί να μειώσει σημαντικά την nominal utility.
- Δεν παρέχεται τεκμήριο ότι robust Q-learning ανακάμπτει ταχύτερα από reset ή recency-based Q-learning μετά από changepoint.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για τον ορισμό ενός incremental tabular robust-Q feasibility comparator και για τη διάκριση model uncertainty robustness από online change adaptation.