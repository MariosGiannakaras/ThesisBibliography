---
κωδικός: SRC-BE53B7970E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επαληθευμένα τεκμήρια — SRC-BE53B7970E

## 1. Maximization bias στο Q-learning
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Introduction, Theorem 1
- **Ισχυρισμός:** Ο max operator πάνω σε ανακριβείς action-value estimates μπορεί να δημιουργήσει systematic upward bias ακόμη και όταν τα individual estimates δεν είναι συνολικά biased.
- **Κεφάλαιο:** Baselines / Threats to validity
- **Θέματα:** Q-learning; overestimation; estimation error
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η χρήση της ίδιας noisy/approximate value estimate για επιλογή και αξιολόγηση της καλύτερης action ευνοεί υπερεκτιμημένες actions.

### Προτεινόμενη χρήση
Overestimation diagnostic για neural value-based baseline.

## 2. Η non-stationarity μπορεί να αυξήσει estimation error
- **Τύπος:** πιστή παράφραση
- **Θέση:** Overoptimism due to estimation errors
- **Ισχυρισμός:** Η θεωρητική αιτία του maximization bias δεν εξαρτάται από συγκεκριμένη πηγή error· η εργασία αναφέρει environmental noise, function approximation και non-stationarity μεταξύ των πιθανών πηγών ανακριβών value estimates.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** non-stationarity; value error; confounding
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Μετά από αλλαγή regime, αυξημένο Q-estimation error μπορεί να δημιουργήσει transient overoptimism χωρίς αυτό να αποτελεί ξεχωριστό adaptation failure.

### Περιορισμοί και κίνδυνος παρερμηνείας
Το paper δεν μελετά changepoint recovery· η σύνδεση χρησιμοποιείται μόνο ως confound/diagnostic rationale.

## 3. Double DQN αποσυνδέει selection και evaluation
- **Τύπος:** πιστή παράφραση
- **Θέση:** Double Q-learning section
- **Ισχυρισμός:** Στο Double DQN το online network επιλέγει το maximizing action, ενώ το target network χρησιμοποιείται για την αξιολόγηση της επιλεγμένης action.
- **Κεφάλαιο:** Agent baselines
- **Θέματα:** Double DQN; target network; baseline fairness
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Αν συμπεριληφθεί DQN-family agent, Double DQN ή αντίστοιχο ablation μειώνει το γνωστό maximization-bias confound.

## 4. Scope boundary
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, experiments
- **Ισχυρισμός:** Τα reported gains αφορούν value accuracy και Atari performance· δεν υπάρχει change detector, context memory ή continual-learning mechanism.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** robustness boundary; adaptation boundary
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Double DQN είναι καλύτερα ελεγχόμενος neural Q-learning comparator, όχι resilience algorithm.

### Παραπομπή
van Hasselt, Guez & Silver, *Deep Reinforcement Learning with Double Q-learning*, AAAI 2016.