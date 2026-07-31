---
κωδικός: SRC-71F2ECA651
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Robust Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract και Ενότητα 1, PDF σελ. 1
- **Ισχυρισμός:** Το model mismatch και οι input disturbances μπορούν να προκαλέσουν ανεπιθύμητη συμπεριφορά σε policy που βελτιστοποιήθηκε μόνο για nominal model.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο
- **Θέματα:** model mismatch; disturbance; robust RL
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η διαφορά μεταξύ learned/simulated model και πραγματικού περιβάλλοντος μπορεί να καταστήσει την nominal RL policy απρόβλεπτη ή ανεπαρκή.

### Συμφραζόμενα

Η εργασία χρησιμοποιεί αυτό το πρόβλημα ως κίνητρο για worst-case robust formulation.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν αφορά κάθε μορφή data uncertainty ούτε αποδεικνύει ότι worst-case optimization είναι πάντα επιθυμητή.

### Προτεινόμενη χρήση

Ιστορικό motivation για robustness.

### Παραπομπή

Morimoto & Doya, 2000, Abstract και §1, PDF σελ. 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** Formulation sections, PDF σελ. 2–4
- **Ισχυρισμός:** Η robust RL formulation μπορεί να ιδωθεί ως minimax παιχνίδι actor και disturber.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο
- **Θέματα:** minimax; actor-disturber; H-infinity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Ο disturber επιδιώκει δυσμενές input disturbance, ενώ ο actor επιλέγει control που περιορίζει το worst-case output deviation υπό penalty για το μέγεθος disturbance.

### Συμφραζόμενα

Η διατύπωση αντλεί από `H∞` control και differential games.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η επιλογή disturbance norm και trade-off parameter είναι μέρος της προδιαγραφής και δεν είναι ουδέτερη.

### Προτεινόμενη χρήση

Εξήγηση της προέλευσης adversarial robust objectives.

### Παραπομπή

Morimoto & Doya, 2000, formulation, PDF σελ. 2–4.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** Linear experiment, PDF σελ. 4–5
- **Ισχυρισμός:** Η learned robust solution ελέγχθηκε έναντι αναλυτικής λύσης σε linear setting.
- **Κεφάλαιο:** Μεθοδολογία· Validation
- **Θέματα:** analytical validation; known solution
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο linear inverted-pendulum problem, learned policy και value function συμφωνούν με την αντίστοιχη analytical `H∞` solution.

### Συμφραζόμενα

Η σύγκριση χρησιμοποιείται ως έλεγχος ορθότητας της online learning formulation.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η συμφωνία σε linear problem δεν αποτελεί απόδειξη για arbitrary nonlinear ή discrete environments.

### Προτεινόμενη χρήση

Παράδειγμα validation against known ground truth.

### Παραπομπή

Morimoto & Doya, 2000, linear experiment, PDF σελ. 4–5.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** Nonlinear experiment και conclusion, PDF σελ. 5–7
- **Ισχυρισμός:** Στο συγκεκριμένο nonlinear pendulum test, robust RL διατήρησε καλύτερο control υπό αλλαγές weight/friction από standard RL.
- **Κεφάλαιο:** Σχετικές εργασίες
- **Θέματα:** model parameter shift; empirical robustness
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η robust policy αντιμετώπισε μεταβολές στις φυσικές παραμέτρους που αποσταθεροποίησαν την nominal standard-RL policy.

### Συμφραζόμενα

Το experiment είναι continuous-control case study και όχι γενικό benchmark.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν επιτρέπεται γενίκευση σε GridWorld ή σύγχρονες deep-RL methods χωρίς νέα πειράματα.

### Προτεινόμενη χρήση

Ιστορικό empirical evidence για robustness under model mismatch.

### Παραπομπή

Morimoto & Doya, 2000, nonlinear experiment/conclusion, PDF σελ. 5–7.

## Τεκμήριο E5

- **Τύπος:** κριτική σύνθεση από το ελεγμένο πρωτότυπο
- **Θέση:** συνολική formulation και experiments, PDF σελ. 1–7
- **Ισχυρισμός:** Worst-case robustness δεν ισοδυναμεί με online resilience και recovery.
- **Κεφάλαιο:** Ορισμοί· Threats to validity
- **Θέματα:** robustness; adaptation boundary
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η εργασία μαθαίνει policy απέναντι σε disturbance formulation, αλλά δεν εισάγει unknown changepoint, detection phase ή post-change recovery metric.

### Συμφραζόμενα

Η πηγή είναι θεμελιώδης για robustness, όχι για το πλήρες resilience lifecycle.

### Περιορισμοί και κίνδυνος παρερμηνείας

Robust policy μπορεί να μειώσει την αρχική πτώση και έτσι να συμβάλει στην resilience, αλλά δεν αποδεικνύει προσαρμογή.

### Προτεινόμενη χρήση

Ορολογικός διαχωρισμός robustness και resilience.

### Παραπομπή

Morimoto & Doya, 2000, συνολική formulation και experiments.
