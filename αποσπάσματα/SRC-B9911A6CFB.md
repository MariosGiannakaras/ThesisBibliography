---
κωδικός: SRC-B9911A6CFB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια

## 1. State estimator και shield είναι διαφορετικοί μηχανισμοί
- Τύπος: πιστή παράφραση
- Θέση: Introduction, Section 3
- Ισχυρισμός: Σε partial observability, ο state estimator παρέχει belief-support information ενώ το shield περιορίζει ρητά τις διαθέσιμες actions για να διατηρήσει reach-avoid safety.
- Κεφάλαιο: Agent architecture / Safe RL
- Θέματα: POMDP; belief support; shield
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η πρόσθετη πληροφορία κατάστασης μπορεί να βοηθήσει το learning, αλλά η safety enforcement προκύπτει από το permissive shield που αποκλείει actions έξω από winning regions.

### Συμφραζόμενα
Το shield και ο estimator χρησιμοποιούν partial model knowledge.

### Περιορισμοί και κίνδυνος παρερμηνείας
State inference accuracy δεν πρέπει να συγχέεται με safety guarantee.

### Προτεινόμενη χρήση
Χωριστό logging context-estimation quality και shield intervention rate.

### Παραπομπή
Carr et al., AAAI 2023.

## 2. Prior transition-support knowledge
- Τύπος: πιστή παράφραση
- Θέση: Sections 3.2–3.3
- Ισχυρισμός: Το shield μπορεί να κατασκευαστεί χωρίς ακριβείς transition probabilities, αλλά χρειάζεται graph-preserving partial model του δυνατού transition support.
- Κεφάλαιο: Threats to validity / Fair comparison
- Θέματα: prior model; transition support; formal safety
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η guarantee βασίζεται στη γνώση του ποια transitions έχουν θετική πιθανότητα, ακόμη κι αν οι ίδιες οι πιθανότητες παραμένουν άγνωστες.

### Συμφραζόμενα
Αυτό αποτελεί ισχυρό prior-information advantage έναντι model-free baseline.

### Περιορισμοί και κίνδυνος παρερμηνείας
Αν structural change δημιουργήσει ή αφαιρέσει transition edges, το precomputed shield δεν θεωρείται πλέον αυτόματα valid.

### Προτεινόμενη χρήση
Report `prior_transition_support` και `shield_revalidation_latency` μετά από structural change.

### Παραπομπή
Carr et al., Sections 3.2–3.3.