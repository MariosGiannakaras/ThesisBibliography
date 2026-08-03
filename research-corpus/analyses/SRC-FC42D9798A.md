---
κωδικός: SRC-FC42D9798A
κατάσταση: επαληθευμένη
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-03"
---

# Scaling Up Robust MDPs by Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Aviv Tamar, Huan Xu, Shie Mannor
- **Έκδοση:** arXiv:1306.6189
- **Τύπος:** θεωρητική/αλγοριθμική εργασία robust MDP
- **Ρόλος:** υποστηρικτική

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς το robust-MDP paradigm μπορεί να εφαρμοστεί όταν ο state space είναι πολύ μεγάλος για ακριβές robust dynamic programming. Οι transition probabilities θεωρούνται αβέβαιες αλλά περιορισμένες σε γνωστό uncertainty set, και το objective παραμένει worst-case robust value.

## Μεθοδολογία και κύρια ευρήματα

Οι συγγραφείς συνδυάζουν robust Bellman operators με approximate dynamic programming και linear function approximation. Για fixed policy διατυπώνεται projected robust Bellman equation, αναλύονται συνθήκες contraction/convergence και αναπτύσσεται sampling-based robust policy evaluation. Η διαδικασία ενσωματώνεται σε policy-improvement scheme ώστε να προσεγγίζεται robust policy χωρίς πλήρη enumeration όλων των states.

Το empirical παράδειγμα αφορά option pricing και χρησιμοποιείται κυρίως για να δείξει ότι το robust-MDP framework μπορεί να κλιμακωθεί μέσω sampling/function approximation.

## Υποθέσεις και ορισμοί

Η εργασία διατηρεί τη βασική robust-MDP υπόθεση ότι η uncertainty set είναι γνωστή και structured, με rectangularity στην transition uncertainty. Το πρόβλημα είναι planning/learning ενός worst-case robust policy μέσα σε αυτή τη family και όχι ανίχνευση άγνωστων environment changepoints.

## Περιορισμοί και απειλές εγκυρότητας

- Η ανάγκη scalability είναι μικρότερη στο tabular GridWorld της διπλωματικής.
- Τα convergence results εξαρτώνται από τεχνικές συνθήκες projection/sampling/function approximation.
- Η robustness περιορίζεται από το uncertainty set και μπορεί να γίνει conservative.
- Δεν παρέχεται change detector, context memory ή explicit recovery mechanism.

## Χρήση στη διπλωματική

Η πηγή συμπληρώνει τον Nilim–El Ghaoui: δείχνει πώς η ίδια static robust-MDP λογική επεκτείνεται πέρα από ακριβές tabular DP. Είναι χρήσιμη κυρίως στη θεωρητική διάκριση «robust policy under model uncertainty» έναντι «agent that detects and adapts after a change».

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Δεν είναι απαραίτητη για την υλοποίηση μικρού GridWorld, αλλά τεκμηριώνει αξιόπιστα τη σύνδεση robust MDP και RL/approximate dynamic programming και ενισχύει τη θεωρητική οριοθέτηση της robustness.
