---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — A Bayesian Approach to Robust Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 1–2, Abstract και Section 1
- **Ισχυρισμός:** Τα κλασικά Robust MDPs μπορεί να παράγουν υπερβολικά συντηρητικές πολιτικές όταν το uncertainty set είναι μεγάλο ή rectangular.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο και σχετικές εργασίες
- **Θέματα:** robust MDP, uncertainty set, conservatism
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο κλασικό RMDP ο agent μεγιστοποιεί τη χειρότερη δυνατή απόδοση μέσα σε ένα δομημένο uncertainty set μεταβάσεων. Η state-action rectangularity επιτρέπει τη χωριστή επιλογή worst-case transition ανά state και action, ακόμη και όταν αυτές οι επιλογές δεν θα μπορούσαν να συνυπάρξουν στο ίδιο πραγματικό μοντέλο. Μαζί με ένα υπερβολικά ευρύ uncertainty set, αυτή η υπόθεση μπορεί να οδηγήσει σε overly pessimistic πολιτικές.

### Συμφραζόμενα

Η παρατήρηση αφορά worst-case planning υπό model uncertainty και όχι κάθε είδος robustness. Στο πείραμα της διπλωματικής απαιτείται χωριστή αναφορά του κόστους robust προστασίας στην ονομαστική απόδοση.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν σημαίνει ότι τα robust objectives είναι άχρηστα. Σημαίνει ότι η δομή και η βαθμονόμηση του uncertainty set αποτελούν μέρος της μεθοδολογικής υπόθεσης.

### Προτεινόμενη χρήση

Να αιτιολογήσει nominal-performance metric και explicit robustness-cost metric δίπλα στη stressed performance.

### Παραπομπή

Derman et al. (2019), σελ. 1–2, Abstract και Section 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–5, Sections 4–6, Lemma 4.1 και Theorem 4.1
- **Ισχυρισμός:** Η posterior αβεβαιότητα των robust Q-values μπορεί να εκτιμηθεί μέσω Bellman-like recursion και να χρησιμοποιηθεί ως σήμα εξερεύνησης.
- **Κεφάλαιο:** Μοντέλο αβεβαιότητας και επιλογή αλγορίθμων
- **Θέματα:** URBE, epistemic uncertainty, safe exploration
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Με Dirichlet posterior στις transition distributions, οι robust Q-values είναι τυχαίες μεταβλητές επειδή εξαρτώνται από το posterior uncertainty set. Οι συγγραφείς δίνουν άνω φράγμα της conditional posterior variance το οποίο ικανοποιεί robust Bellman recursion. Η λύση της URBE χρησιμοποιείται ως uncertainty estimate και, στην πρακτική μέθοδο, προστίθεται στη robust Q-function ώστε ο agent να εξερευνά state-action περιοχές όπου η γνώση του worst-case model παραμένει ανεπαρκής.

### Συμφραζόμενα

Το exploration bonus αφορά epistemic model uncertainty. Δεν πρέπει να ταυτιστεί με τη γνωστή stochastic πιθανότητα αποτυχίας μιας ενέργειας.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η θεωρία χρησιμοποιεί finite horizon, bounded rewards, acyclic worst-case transition graph και rectangular sets. Η deep approximation δεν κληρονομεί αυτομάτως όλες τις θεωρητικές εγγυήσεις.

### Προτεινόμενη χρήση

Να τεκμηριώσει adaptive exploration ή uncertainty-aware baseline και τον διαχωρισμό epistemic από aleatoric uncertainty.

### Παραπομπή

Derman et al. (2019), σελ. 3–5, Sections 4–6.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 6–7, Sections 7.1–7.2 και Figures 2–4
- **Ισχυρισμός:** Η αξιολόγηση robust adaptation χρειάζεται controlled severity levels και χωριστή σύγκριση nominal και misspecified dynamics.
- **Κεφάλαιο:** Πειραματικό περιβάλλον και scenarios
- **Θέματα:** gridworld, transition failure, perturbation severity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο toy MDP η adversarial transition probability αλλάζει διαδοχικά σε 0.001, 0.8, 0.1 και 0.9, επιτρέποντας την παρατήρηση απόκρισης μετά από γνωστές μεταβολές. Στο 10×10 Mars Rover gridworld οι agents εκπαιδεύονται με nominal failure probability 0.005 και δοκιμάζονται επίσης σε 0.2. Το fixed robust DQN εμφανίζεται υπερβολικά συντηρητικό στο nominal model, ενώ το DQN-URBE φτάνει στον στόχο· υπό σοβαρότερο misspecification το URBE εμφανίζεται πιο robust από το UBE.

### Συμφραζόμενα

Το Mars Rover είναι άμεσο παράδειγμα απλού controlled grid environment, συμβατό με την περιγραφή «απλό προσομοιωμένο περιβάλλον» της αίτησης χωρίς να καθιστά το GridWorld επίσημη απαίτηση.

### Περιορισμοί και κίνδυνος παρερμηνείας

Οι heatmaps και testing episodes είναι evidence για τα συγκεκριμένα trained models. Δεν δίνουν γενική κατάταξη όλων των robust methods ούτε πλήρη στατιστική ανάλυση.

### Προτεινόμενη χρήση

Να αιτιολογήσει προκαθορισμένη κλίμακα severity, nominal/stressed test matrix και state-visitation diagnostics.

### Παραπομπή

Derman et al. (2019), σελ. 6–7, Sections 7.1–7.2 και Figures 2–4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 7–9, Section 7.3, Figures 5–6 και Conclusion
- **Ισχυρισμός:** Η ταχύτητα ανάκαμψης μετά από αλλαγή dynamics είναι διακριτή μετρική από την τελική robust απόδοση.
- **Κεφάλαιο:** Μετρικές ανθεκτικότητας και recovery
- **Θέματα:** recovery speed, dynamic change, post-change curve
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο CartPole οι agents εκπαιδεύονται με pole length 0.75 και, αφού συγκλίνουν, το μήκος αλλάζει σε 1.25. Η αναφερόμενη training curve δείχνει ότι το DQN-URBE, παρότι αρχικά συγκλίνει πιο αργά, επανέρχεται πολύ γρηγορότερα μετά τη μεταβολή, φτάνοντας ξανά το μέγιστο reward. Ο fixed robust DQN δεν ανακάμπτει στην προηγούμενη βέλτιστη επίδοση μέσα στο παρατηρούμενο training horizon.

### Συμφραζόμενα

Η καμπύλη υποστηρίζει τη μέτρηση transient degradation και recovery trajectory. Δεν αρκεί να συγκρίνεται μόνο ο μέσος όρος πριν και πολύ μετά την αλλαγή.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η εργασία δεν παρέχει καθολικό recovery threshold ούτε confidence interval για συγκεκριμένο recovery-time estimate. Η διπλωματική πρέπει να ορίσει δικό της threshold και uncertainty reporting πριν τα final runs.

### Προτεινόμενη χρήση

Να στηρίξει metrics όπως performance drop, time-to-recover, post-change area under curve και unrecovered-run rate.

### Παραπομπή

Derman et al. (2019), σελ. 7–9, Section 7.3, Figures 5–6.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδα 9, Section 9 Conclusion
- **Ισχυρισμός:** Τα αποτελέσματα της URBE δεν καθιερώνουν ακόμη asymptotic behavior ή γενική επίδραση του uncertainty-set size.
- **Κεφάλαιο:** Περιορισμοί και threats to validity
- **Θέματα:** asymptotic behavior, uncertainty calibration, evidence limits
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς παρουσιάζουν την URBE ως μέθοδο που ενθαρρύνει safe exploration και προσαρμόζει έμμεσα το uncertainty set από νέες παρατηρήσεις. Ωστόσο, δηλώνουν ρητά ότι η asymptotic συμπεριφορά της μεθόδου και η επίδραση του μεγέθους του posterior uncertainty set στην variance των robust Q-values παραμένουν αντικείμενα μελλοντικής έρευνας.

### Συμφραζόμενα

Η πηγή είναι ισχυρή για σχεδιαστικές αρχές και συγκεκριμένα experiments, αλλά όχι για καθολική εγγύηση convergence σε arbitrary dynamic environments.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να μετατραπεί το empirical faster recovery σε θεωρητική guarantee. Επίσης, το uncertainty set απαιτεί δική του τεκμηριωμένη βαθμονόμηση.

### Προτεινόμενη χρήση

Να περιορίσει τα claims και να καταγράψει calibration sensitivity ως threat to validity.

### Παραπομπή

Derman et al. (2019), σελ. 9, Conclusion.
