---
κωδικός: SRC-85335DDDA6
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια — Empirical Study on Robustness and Resilience in Cooperative MARL

## 1. Robustness και resilience είναι διαφορετικά
- Τύπος: πιστή παράφραση
- Θέση: Sections 1 and 3
- Ισχυρισμός: Η εργασία ορίζει robustness ως διατήρηση performance υπό ενεργή uncertainty και resilience ως recovery μετά από disruption.
- Κατάσταση: επαληθευμένο

### Προτεινόμενη χρήση
Persistent-noise robustness, transient-shock recovery και online adaptation να αξιολογούνται σε διαφορετικά protocols.

## 2. Rankings δεν γενικεύονται μεταξύ uncertainty modalities
- Τύπος: πιστή παράφραση
- Θέση: Main findings
- Ισχυρισμός: Policies που αποδίδουν robustly/resiliently σε μία uncertainty type μπορούν να αποτυγχάνουν σε άλλη.
- Κατάσταση: επαληθευμένο

### Προτεινόμενη χρήση
Action failure, observation corruption, transition/environment shift και structural change να έχουν χωριστά scorecards.

## 3. Severity μπορεί να αλλάξει τις σχέσεις
- Τύπος: πιστή παράφραση
- Θέση: Main findings
- Ισχυρισμός: Η σχέση nominal performance–robustness/resilience εξασθενεί όταν αυξάνεται η perturbation severity.
- Κατάσταση: επαληθευμένο

### Προτεινόμενη χρήση
Severity sweep και performance-vs-severity curve, όχι ένα μόνο perturbation level.

## 4. Hyperparameters μπορούν να κυριαρχήσουν στο empirical αποτέλεσμα
- Τύπος: πιστή παράφραση
- Θέση: Introduction / Main findings
- Ισχυρισμός: Σε αρκετά εξεταζόμενα MARL tasks, hyperparameter/implementation choices επηρεάζουν robustness/resilience περισσότερο από το algorithm label.
- Κατάσταση: επαληθευμένο

### Περιορισμοί
Οι συγκεκριμένες MARL hyperparameter συστάσεις δεν μεταφέρονται αυτούσιες σε tabular RL.

### Προτεινόμενη χρήση
Matched tuning budget, declared search space και sensitivity analysis για κρίσιμες hyperparameters.

## 5. MARL caveat
Η empirical superiority συγκεκριμένων MARL variants δεν χρησιμοποιείται ως evidence για single-agent GridWorld. Η πηγή χρησιμοποιείται μόνο για evaluation methodology.