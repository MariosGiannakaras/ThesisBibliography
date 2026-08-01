---
κωδικός: SRC-E9D551F27C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-E9D551F27C — Επαληθευμένα τεκμήρια

## 1. Robustness budget ως curriculum

Η εργασία αντιμετωπίζει την ακτίνα/robustness budget του uncertainty set ως μεταβαλλόμενη training quantity και όχι ως σταθερό hyperparameter.

## 2. Fixed-budget trade-off

Μικρό budget μπορεί να διατηρεί nominal performance αλλά να μην καλύπτει perturbations, ενώ μεγάλο budget μπορεί να αυξάνει conservativeness και training instability.

## 3. Development-only schedule

Ένα severity curriculum μπορεί να χρησιμοποιηθεί για training ή pilot tuning, αλλά το final test sequence πρέπει να παραμένει held out. Η online αλλαγή του budget με γνώση test severity θα ήταν oracle leakage.

## 4. Required comparisons

Κάθε adaptive schedule συγκρίνεται με fixed-small, fixed-large και απλό heuristic schedule, με κοινό interaction/compute budget.

## 5. Scope boundary

Self-paced robust training παράγει policy προετοιμασμένη για perturbation family. Δεν αποτελεί changepoint detector ή continued-learning recovery μετά την deployment αλλαγή.