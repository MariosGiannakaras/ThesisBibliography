---
κωδικός: SRC-6E7AFA8AC0
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια

## 1. Uncertainty-set structure επηρεάζει sample complexity
- Τύπος: πιστή παράφραση
- Θέση: Abstract, Section 1.1, Tables 1–2
- Ισχυρισμός: Η απαιτούμενη δειγματοληψία μεταβάλλεται με rectangularity, divergence family, radius, discount factor και state/action size.
- Κεφάλαιο: Robust baselines / Trade-offs
- Θέματα: robust MDP; sample complexity; rectangularity
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Τα robust-MDP guarantees δεν είναι ανεξάρτητα από τον τρόπο ορισμού του ambiguity set· ειδικά η s-rectangular περίπτωση είναι γενικά πιο απαιτητική από την (s,a)-rectangular.

### Συμφραζόμενα
Αφορά finite tabular robust MDPs με generative/offline data.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν αποδεικνύει ότι μεγαλύτερο uncertainty radius αυξάνει πάντα practical performance.

### Προτεινόμενη χρήση
Να δηλώνεται ως hyperparameter/protocol factor το uncertainty-set family, radius και rectangularity assumption.

### Παραπομπή
Yang, Zhang & Zhang, Annals of Statistics, 2022.

## 2. Robust MDP δεν είναι online changepoint model
- Τύπος: πιστή παράφραση
- Θέση: Introduction, problem formulation
- Ισχυρισμός: Η αβεβαιότητα μοντελοποιείται ως σύνολο πιθανών transition kernels γύρω από estimated/nominal dynamics.
- Κεφάλαιο: Θεωρητικό υπόβαθρο
- Θέματα: model mismatch; uncertainty set; robustness
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Ο στόχος είναι policy που είναι λιγότερο ευαίσθητη σε transition-model estimation errors ή deployment mismatch, όχι agent που πρώτα ανιχνεύει και μετά μαθαίνει νέο regime.

### Συμφραζόμενα
Το formulation μπορεί να χρησιμοποιηθεί ως comparator για robustness χωρίς update.

### Περιορισμοί και κίνδυνος παρερμηνείας
Worst-case robustness δεν πρέπει να ονομάζεται resilience ή adaptation.

### Προτεινόμενη χρήση
Για τη σαφή διάκριση robust baseline από detector/adaptor baselines.

### Παραπομπή
Yang, Zhang & Zhang, 2022.