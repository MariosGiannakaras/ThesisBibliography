---
κωδικός: SRC-D52DF7B9A4
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Q-learning: Off-policy TD Control

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 6.5, pp. 131–132
- **Ισχυρισμός:** Ο Q-learning είναι off-policy TD control και ενημερώνει προς το greedy value της επόμενης κατάστασης.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο
- **Θέματα:** Q-learning; off-policy; TD
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η ενημέρωση του `Q(S,A)` χρησιμοποιεί immediate reward και το μέγιστο `Q` μεταξύ των actions στην επόμενη state. Έτσι η learned target policy είναι greedy, ενώ διαφορετική behavior policy μπορεί να παράγει τα δεδομένα.

### Συμφραζόμενα

Η behavior policy εξακολουθεί να καθορίζει ποια state-action pairs επισκέπτονται και ενημερώνονται.

### Περιορισμοί και κίνδυνος παρερμηνείας

Off-policy δεν σημαίνει ανεξαρτησία από data coverage ή exploration.

### Προτεινόμενη χρήση

Ορισμός του tabular baseline και διάκριση target/behavior policy.

### Παραπομπή

Sutton and Barto, Chapter 6, Section 6.5, pp. 131–132; Q-learning originally Watkins (1989).

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 6.5, p. 131
- **Ισχυρισμός:** Η κλασική convergence guarantee του tabular Q-learning απαιτεί συνεχή ενημέρωση όλων των state-action pairs και κατάλληλα step sizes.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** convergence; visitation; stationarity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η σύγκλιση προς το optimal action-value function βασίζεται στην απαίτηση ότι κάθε state-action pair συνεχίζει να ενημερώνεται και ότι οι learning rates ικανοποιούν stochastic-approximation conditions.

### Συμφραζόμενα

Η διατύπωση αφορά stationary tabular problem.

### Περιορισμοί και κίνδυνος παρερμηνείας

Repeated environment changes παραβιάζουν τη σταθερότητα του target και δεν καλύπτονται από την εγγύηση.

### Προτεινόμενη χρήση

Σαφής περιορισμός θεωρητικών claims και απαίτηση empirical recovery tests.

### Παραπομπή

Sutton and Barto, Chapter 6, p. 131.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** Example 6.6, Cliff Walking, pp. 132–134
- **Ισχυρισμός:** Policy με καλύτερο greedy path μπορεί να έχει χειρότερη online απόδοση όταν η behavior policy συνεχίζει stochastic exploration.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** Sarsa; Q-learning; exploration risk
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Ο Q-learning μαθαίνει τη σύντομη διαδρομή δίπλα στον γκρεμό, αλλά η ε-greedy behavior προκαλεί περιστασιακές μεγάλες ποινές. Η on-policy Sarsa λαμβάνει υπόψη αυτή τη stochastic behavior και μαθαίνει μεγαλύτερη αλλά ασφαλέστερη διαδρομή με καλύτερο online reward κατά την εκπαίδευση.

### Συμφραζόμενα

Το αποτέλεσμα εξαρτάται από το exploration rate και το συγκεκριμένο reward landscape.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν αποδεικνύει καθολική υπεροχή Sarsa ή safety guarantee.

### Προτεινόμενη χρήση

Απαίτηση να αναφέρονται training-time failures και όχι μόνο greedy evaluation return.

### Παραπομπή

Sutton and Barto, Example 6.6, pp. 132–134.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 6.7 and Figure 6.5, p. 135
- **Ισχυρισμός:** Το maximization πάνω σε noisy value estimates δημιουργεί positive bias και το Double Q-learning μειώνει τη μεροληψία διαχωρίζοντας selection από evaluation.
- **Κεφάλαιο:** Μοντέλα
- **Θέματα:** maximization bias; Double Q-learning
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Όταν οι ίδιες noisy estimates χρησιμοποιούνται για να επιλεγεί η μέγιστη action και να εκτιμηθεί η αξία της, η estimate τείνει να είναι θετικά μεροληπτική. Δύο ανεξάρτητες Q estimates επιτρέπουν η μία να επιλέγει και η άλλη να αξιολογεί.

### Συμφραζόμενα

Η ιδέα είναι ιδιαίτερα σχετική όταν rewards ή transitions έχουν stochastic noise.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η μείωση maximization bias δεν εγγυάται καλύτερο recovery σε non-stationary environment.

### Προτεινόμενη χρήση

Επιστημονική αιτιολόγηση Double Q-learning ως πιθανό baseline υπό reward noise.

### Παραπομπή

Sutton and Barto, Section 6.7 and Figure 6.5, p. 135.