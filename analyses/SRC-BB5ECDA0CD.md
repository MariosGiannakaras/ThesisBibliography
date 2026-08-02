# SRC-BB5ECDA0CD — Online Robust Reinforcement Learning Through Monte-Carlo Planning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Tuan Dam, Kishan Panaganti, Brahim Driss, Adam Wierman
- **Έκδοση:** ICML 2025
- **Τύπος:** primary robust planning / MCTS method
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Αντικείμενο

Η εργασία επεκτείνει το Monte Carlo Tree Search σε robust RL με uncertainty τόσο στις transition dynamics όσο και στη reward distribution. Το robust planning γίνεται με ambiguity sets και robust backup operator, ενώ η exploration προσαρμόζεται ώστε να διατηρούνται finite-sample convergence guarantees.

## Κύρια αποτελέσματα

- Προτείνεται robust MCTS για model ambiguity σε transitions και rewards.
- Υποστηρίζονται διαφορετικά ambiguity metrics, όπως total variation, KL, chi-squared και Wasserstein.
- Παρέχονται finite-sample convergence bounds για root-value estimation, της ίδιας τάξης με standard MCTS.
- Η empirical αξιολόγηση περιλαμβάνει Gambler's Problem και FrozenLake και συγκρίνει robust με standard MCTS υπό model mismatch.

## Συνάφεια

Η εργασία επιβεβαιώνει ότι robustness μπορεί να ενσωματωθεί όχι μόνο σε value iteration ή Q-learning αλλά και σε online planning. Για τη διπλωματική είναι χρήσιμη κυρίως ως **planning-side comparator** και όχι ως βασικός learning agent.

Σημαντικό είναι επίσης ότι το MCTS tree αντιμετωπίζει εσωτερικά non-stationary bandit estimates κατά τη search διαδικασία. Αυτό δεν πρέπει να συγχέεται με non-stationarity του εξωτερικού environment benchmark.

## Πρωτόκολλο που προκύπτει

Εάν υλοποιηθεί planning comparator, καταγράφονται:

- planning budget ανά decision,
- search depth,
- number of rollouts,
- ambiguity-set family/radius,
- robust versus nominal backup,
- wall-clock latency ανά action,
- clean and perturbed return.

Για δίκαιη σύγκριση με model-free agents απαιτείται explicit compute budget. Δεν επιτρέπεται MCTS να χρησιμοποιεί απεριόριστες simulator queries όταν Q-learning συγκρίνεται μόνο με real interaction steps.

## Περιορισμοί

- Απαιτεί simulator/planning access που δεν είναι διαθέσιμο σε κάθε online RL setting.
- Robust planning εντός ambiguity set δεν αποτελεί changepoint detection.
- Η FrozenLake αξιολόγηση δεν αρκεί για να αποδειχθεί resilience σε repeated unknown environmental changes.
- Το computational budget είναι διαφορετικής φύσης από tabular continual-learning updates.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για planning-based robustness και για fairness rules σε comparisons όπου simulator-query budget και wall-clock compute πρέπει να αναφέρονται ρητά.