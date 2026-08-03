---
κωδικός: SRC-85D1CCAE1E
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2508.17448"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality

## Αξιολόγηση
Η εργασία μελετά robust constrained RL όταν transition dynamics ανήκουν σε uncertainty set και οι safety/resource constraints πρέπει να ικανοποιούνται ακόμη και στο worst case. Κύρια θεωρητική συνεισφορά είναι counterexample όπου strong duality δεν ισχύει γενικά και primal-only RRPO algorithm που αποφεύγει την εξάρτηση από primal-dual formulation. Περιλαμβάνει GridWorld και MountainCar experiments.

## Αξία
Υψηλής συνάφειας με το intersection robustness + safety και χρήσιμη προειδοποίηση ότι assumptions από nominal CMDPs δεν μεταφέρονται αυτόματα στο robust constrained problem.

## Γιατί δεν επιλέγεται στο core
- είναι πολύ πρόσφατο arXiv/preprint-level record,
- δεν αντιμετωπίζει changepoint detection/repeated regime recovery,
- το robust-constrained theoretical arm είναι πιο σύνθετο από το resource-aware baseline matrix,
- safety formulations/robust uncertainty-set caveats καλύπτονται ήδη από selected primary sources,
- η strong-duality issue δεν είναι απαραίτητη για τις σχεδιαζόμενες tabular baselines.

## Απόφαση
**Απόρριψη ως advanced but non-core robust-constrained RL source.** Διατηρείται ως technical reference εάν προστεθεί formal robust-CMDP baseline.