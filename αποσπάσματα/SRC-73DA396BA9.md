---
κωδικός: SRC-73DA396BA9
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-73DA396BA9 — Επαληθευμένα τεκμήρια

## Χρήσιμα τεκμήρια για συγγραφή

### 1. Πεπερασμένη βιβλιοθήκη transition prototypes

Η εργασία μοντελοποιεί την αβεβαιότητα ως πεπερασμένο σύνολο γνωστών transition kernels, ένας από τους οποίους θεωρείται αληθινός. Αυτό παρέχει σαφή θεωρητική βάση για regime/model library, αλλά μόνο όταν η library είναι structural prior και όχι αυθαίρετη αποθήκη policies.

### 2. Robust policy όσο παραμένει αβεβαιότητα

Ο πράκτορας υπολογίζει policy ως προς το ενεργό σύνολο μη αποκλεισμένων prototypes. Η robust φάση προστατεύει την early-stage απόδοση όταν τα observations δεν επαρκούν ακόμη για ασφαλή hard selection.

### 3. Online συρρίκνωση ambiguity set

Με τη συλλογή trajectories, empirical transition evidence χρησιμοποιείται για elimination ασύμβατων candidates. Το ambiguity-set size αποτελεί επομένως observable diagnostic και όχι μόνο εσωτερική μεταβλητή του algorithm.

### 4. Early stopping και specialization

Όταν υπάρχει επαρκές evidence για μοναδικό transition prototype, η μέθοδος μπορεί να τερματίσει την robust learning phase και να χρησιμοποιήσει την policy του επιλεγμένου model. Αυτό στηρίζει architecture `robust fallback → regime-specific policy`.

### 5. Κρίσιμο caveat

Τα guarantees προϋποθέτουν ότι ο αληθινός kernel βρίσκεται στη γνωστή prototype library. Novel regime εκτός library πρέπει να αξιολογείται χωριστά και δεν επιτρέπεται να παρουσιαστεί ως καλυπτόμενο από το βασικό theorem.

## Προτεινόμενη χρήση

- Κεφάλαιο model/context libraries.
- Justification για active candidate-set logging.
- Ablation hard selection έναντι robust candidate-set policy.
- Threat to validity για out-of-library regimes και finite-horizon assumptions.