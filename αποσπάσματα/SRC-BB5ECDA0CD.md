---
κωδικός: SRC-BB5ECDA0CD
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-BB5ECDA0CD — verified excerpts

## Robust MCTS

Η εργασία ενσωματώνει ambiguity σε transition dynamics και reward distributions μέσα στο Monte Carlo Tree Search και χρησιμοποιεί robust backup operator αντί nominal backup.

**Χρήση:** planning-based robust comparator, όχι detector.

## Ambiguity-set families

Η προσέγγιση εξετάζει uncertainty sets ορισμένα μέσω διαφορετικών distance/divergence measures, όπως total variation, KL, chi-squared και Wasserstein.

**Protocol implication:** κάθε planning experiment πρέπει να δηλώνει ακριβώς set family και robustness radius.

## Finite-sample planning guarantee

Η εργασία παρέχει convergence analysis για robust root-value estimation με sample-rate ίδιας τάξης με standard MCTS.

**Ασφαλής παράφραση:** η προσθήκη robust backup δεν συνεπάγεται απαραίτητα αλλαγή της asymptotic sample-order του MCTS υπό τις assumptions της εργασίας.

## FrozenLake evidence

Η empirical αξιολόγηση περιλαμβάνει FrozenLake και δείχνει robust performance υπό model mismatch σε σχέση με nominal MCTS.

**Όριο:** αυτό είναι robustness-under-mismatch evidence, όχι repeated-changepoint recovery evidence.

## Fair comparison requirement

Το MCTS χρησιμοποιεί simulator rollouts ανά decision, ενώ model-free agents χρησιμοποιούν environment interaction για learning updates.

**Thesis-ready rule:** αναφέρονται χωριστά environment interactions, simulator queries, planning rollouts και wall-clock latency.

## Scope boundary

Η εσωτερική non-stationarity των bandit estimates μέσα στο search tree δεν πρέπει να συγχέεται με εξωτερική non-stationarity του benchmark environment.