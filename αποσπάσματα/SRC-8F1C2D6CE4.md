# SRC-8F1C2D6CE4 — Επαληθευμένα τεκμήρια

## 1. Capacity ως robustness παράμετρος

Η εργασία συνδέει την model/policy rank με bias–variance trade-off υπό epistemic dynamics uncertainty. Πολύ χαμηλή capacity αυξάνει bias, ενώ υπερβολική capacity μπορεί να αυξήσει variance και sensitivity.

## 2. Adaptive rank αντί nested min–max

Η AdaRL προσαρμόζει τον representational rank μέσω bi-level optimization, αντί να επιλύει worst-case transition problem σε κάθε update. Αυτό είναι computational-design alternative, όχι change-detection mechanism.

## 3. Neural-agent diagnostics

Για neural comparator πρέπει να αναφέρονται parameter count, effective rank, rank trajectory, compute και nominal-performance cost. Διαφορετική architecture capacity δεν επιτρέπεται να κρύβεται ως `algorithm effect`.

## 4. Scope caveat

Το evidence προέρχεται από continuous-control MuJoCo και model-uncertainty experiments. Δεν αποδεικνύει rapid recovery σε tabular repeated changepoints.

## 5. Χρήση

- Capacity-related threat to validity.
- Neural feasibility discussion.
- Αιτιολόγηση fixed-capacity ablations εάν προστεθεί deep agent.