---
κωδικός: SRC-3EF475E25A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI 2023 / arXiv:2301.00858"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Robust Average-Reward Markov Decision Processes

## Αξιολόγηση
Η εργασία των Wang et al. αναπτύσσει θεωρία και robust dynamic programming για average-reward MDPs με general uncertainty sets. Παρέχει σύνδεση discounted→average reward καθώς `γ→1`, robust Bellman equation και robust relative value iteration.

## Επιστημονική αξία
Είναι υψηλής ποιότητας primary robust-MDP source και επισημαίνει ότι long-run average-reward problems έχουν διαφορετική μαθηματική δομή από discounted MDPs.

## Όριο συνάφειας
Το current thesis benchmark είναι episodic/resource-aware με explicit post-change recovery curves και δεν απαιτεί average-reward robust control. Η εργασία δεν παρέχει changepoint detector, repeated-regime adaptation ή recovery metrics. Οι βασικές robust-MDP έννοιες uncertainty sets/Bellman robustness καλύπτονται ήδη από selected canonical sources.

## Απόφαση
**Απόρριψη από το curated core λόγω objective/formulation scope και redundancy, όχι λόγω ποιότητας.** Παραμένει technical reference εάν το benchmark επεκταθεί σε continuing average-reward tasks.