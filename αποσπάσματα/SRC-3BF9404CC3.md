---
κωδικός: SRC-3BF9404CC3
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-3BF9404CC3 — Επαληθευμένα τεκμήρια

## 1. Διαχωρισμός task και recovery policy

Η αρχιτεκτονική χρησιμοποιεί safety critic, recovery policy και action decider χωριστά από την task policy. Αυτό επιτρέπει explicit logging του μηχανισμού παρέμβασης.

## 2. Controller disagreement

Κοντά στο boundary της recovery zone, task και recovery policies μπορεί να προτείνουν αντίθετες actions. Το αποτέλεσμα μπορεί να είναι oscillation ή αδυναμία προόδου, παρότι οι constraint violations μειώνονται.

## 3. Intervention diagnostics

Η αξιολόγηση recovery controller δεν πρέπει να περιορίζεται σε συνολικό violation count. Απαιτούνται:

- task–recovery action disagreement,
- intervention-burst duration,
- controller-induced delay,
- stuck/oscillation rate,
- nominal reward loss.

## 4. Auxiliary-reward caveat

Η χρήση auxiliary reward μπορεί να μειώσει τη σύγκρουση των policies, αλλά αλλάζει το task objective. Η βελτίωση safety δεν πρέπει να παρουσιάζεται χωρίς αναφορά πιθανής απώλειας task optimality.

## 5. Scope boundary

Η recovery policy επαναφέρει τον agent σε safer region. Δεν είναι changepoint detector και δεν τεκμηριώνει policy relearning μετά από αλλαγή dynamics ή reward.