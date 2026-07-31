# SRC-C90D59EC8C — Επαληθευμένα τεκμήρια

## 1. State entropy έναντι policy entropy

Η state entropy μετρά την κάλυψη του state space, ενώ η policy entropy μετρά τη διασπορά actions υπό μία κατάσταση. Οι δύο regularizers δεν πρέπει να συγχέονται σε έναν γενικό όρο `exploration`.

## 2. Structured perturbations

Το επίσημο abstract αναφέρει robustness οφέλη της state entropy σε structured και spatially correlated reward/transition uncertainty. Αυτό είναι πιο κοντά σε συνεκτικές wall/region αλλαγές από ό,τι ανεξάρτητο μικρό transition noise.

## 3. Tabular approximation

Σε GridWorld, visitation counts παρέχουν άμεσο state-distribution estimate. Έτσι μπορεί να εξεταστεί count/state-entropy bonus χωρίς neural density estimator.

## 4. Evaluation-rollout sensitivity

Τα robustness οφέλη δηλώνονται ευαίσθητα στον αριθμό rollouts που χρησιμοποιούνται για policy evaluation. Ο αριθμός rollouts είναι επομένως protocol parameter και όχι αόρατη implementation λεπτομέρεια.

## 5. Scope και safety caveat

Υψηλή state coverage δεν αποτελεί change detector ούτε εγγύηση ασφαλούς exploration. Πρέπει να αναφέρονται utility, newly-relevant-state coverage και hazard/violation cost μαζί.