---
κωδικός: SRC-7C18826BEE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-7C18826BEE — Επαληθευμένα τεκμήρια

## 1. MC dropout

Με dropout ενεργό κατά το test time και T stochastic forward passes, μπορούν να εκτιμηθούν predictive mean και variance. Η διαδικασία αποτελεί approximate Bayesian uncertainty method, όχι exact posterior inference.

## 2. Softmax/Q magnitude δεν είναι confidence

Ένα neural model μπορεί να δίνει υψηλή predictive probability ή μεγάλη Q-value σε input μακριά από τα training data. Point predictions δεν πρέπει να ερμηνεύονται ως epistemic certainty.

## 3. Hyperparameter dependence

Η uncertainty estimate εξαρτάται από dropout rate, architecture, regularization και αριθμό MC passes. Όλα αποτελούν reportable protocol parameters.

## 4. RL scope

MC-dropout variance μπορεί να υποστηρίξει exploration ή uncertainty diagnostics, αλλά υψηλή variance δεν αποτελεί calibrated changepoint detector χωρίς false-alarm/delay validation.

## 5. Resource-aware χρήση

Για μικρό tabular GridWorld προτιμώνται empirical counts/transition estimates. MC dropout είναι optional μόνο εάν υλοποιηθεί neural Q-function ή neural detection model.