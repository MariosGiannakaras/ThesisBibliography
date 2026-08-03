---
κωδικός: SRC-01BBBA7EAB
κατάσταση: επαληθευμένη
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-03"
---

# Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Yuhui Wang, Hao He, Xiaoyang Tan
- **Έκδοση:** arXiv:1902.05795
- **Τύπος:** πρωτογενής ακαδημαϊκή εργασία
- **Ρόλος:** υποστηρικτική

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει robustness όταν ο agent δεν λαμβάνει αξιόπιστη πλήρη παρατήρηση της κατάστασης. Μέρη του observation vector μπορεί να λείπουν δυναμικά και οι διαθέσιμες μετρήσεις μπορεί να περιέχουν θόρυβο. Το πρόβλημα διατυπώνεται ως POMDP αντί ως πλήρως παρατηρήσιμο MDP.

## Μεθοδολογία και κύρια ευρήματα

Οι συγγραφείς προτείνουν BI-PPO. Κατά την εκτέλεση διατηρείται belief distribution πάνω στη latent state, το οποίο ενημερώνεται από το ιστορικό incomplete/noisy observations και actions. Παράλληλα μαθαίνεται transition model με surrogate loss, ενώ generative/imputation mechanism βοηθά στην ανακατασκευή των ελλιπών components. Η policy χρησιμοποιεί belief information αντί να απαιτεί ένα πλήρες raw observation vector.

Η αξιολόγηση σε continuous-control benchmarks εξετάζει διαφορετικά επίπεδα missingness και noise και αναφέρει καλύτερη επίδοση από τις συγκρινόμενες μεθόδους στα συγκεκριμένα scenarios.

## Υποθέσεις και ορισμοί

Το observation model περιλαμβάνει additive Gaussian noise και δυναμικά missing components. Η derivation βασίζεται σε MCAR/MAR missingness assumptions, ενώ για tractability χρησιμοποιούνται Gaussian/Laplace approximations και learned nonlinear transition functions. Αυτές οι υποθέσεις πρέπει να αναφέρονται όταν μεταφέρεται η ιδέα σε GridWorld.

## Περιορισμοί και απειλές εγκυρότητας

- Η εργασία αφορά observation corruption/partial observability, όχι abrupt αλλαγή της ίδιας της transition topology.
- Η μέθοδος είναι model-based ως προς το learned transition component και εξαρτάται από σωστή belief inference.
- Τα αποτελέσματα continuous control δεν αποδεικνύουν άμεσα απόδοση σε discrete GridWorld.
- Robust execution απέναντι σε sensor noise δεν ισοδυναμεί με recovery μετά από environment changepoint.

## Χρήση στη διπλωματική

Η πηγή δικαιολογεί ξεχωριστή κατηγορία perturbation για **observation uncertainty**. Μπορεί να στηρίξει experiments με missing cells/features, noisy state observations ή observation aliasing. Τα metrics πρέπει να διαχωρίζουν observation robustness από transition/reward adaptation.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Προσθέτει μια καθαρά διαφορετική διάσταση robustness που δεν καλύπτεται από transition uncertainty ή adversarial action/dynamics perturbations.
