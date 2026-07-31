# SRC-4D2B7DDC38 — Επαληθευμένα τεκμήρια

## 1. Support-shift hardness

Η εργασία δείχνει ότι interactive robust RL δεν είναι γενικά sample-efficient όταν το training και το testing environment έχουν ουσιαστικά ασύνδετες supports. States κρίσιμα στο deployment μπορεί να μην είναι προσβάσιμα μέσω αλληλεπίδρασης στο training MDP.

## 2. Exploration δεν λύνει κάθε structural gap

Περισσότερο exploration στο ίδιο training environment δεν δημιουργεί evidence για states ή transitions που το training dynamics δεν μπορεί να παράγει. Αυτό περιορίζει claims robustness από fixed-layout training.

## 3. Coverage-aware evaluation

Τα scenarios πρέπει να διακρίνουν:

- in-support αλλαγή παραμέτρων,
- low-probability αλλά reachable transitions,
- out-of-support structural αλλαγή.

Η διάκριση είναι απαραίτητη για την ερμηνεία failure και recovery.

## 4. Πρόσθετες assumptions

Η near-optimal algorithmic εγγύηση ισχύει σε tractable subclass με ειδική assumption και total-variation robust set. Δεν επιτρέπεται να παρουσιαστεί ως γενική λύση στο sim-to-real gap.

## 5. Χρήση στη διπλωματική

- Threat to validity για ανεπαρκή environment coverage.
- Justification για multiple training layouts και held-out structural tests.
- Coverage-overlap diagnostic πριν από algorithm ranking.