---
κωδικός: SRC-D1B6BA711E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια

## 1. Online robust exploration χωρίς generative model
- Τύπος: πιστή παράφραση
- Θέση: Abstract, Introduction
- Ισχυρισμός: Η εργασία μελετά robust policy optimization με πραγματική online interaction και exploration–exploitation, αντί να υποθέτει generative-model oracle.
- Κεφάλαιο: Robust baselines / Computational trade-offs
- Θέματα: online robust MDP; exploration; regret
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Ο agent αλληλεπιδρά διαδοχικά με άγνωστο nominal system και πρέπει να μάθει robust policy ενώ ταυτόχρονα συλλέγει τα δεδομένα που χρειάζονται για την εκτίμηση.

### Συμφραζόμενα
Το worst-case transition παραμένει περιορισμένο σε προκαθορισμένο rectangular uncertainty set.

### Περιορισμοί και κίνδυνος παρερμηνείας
Online interaction εδώ δεν σημαίνει environmental changepoint ή lifelong adaptation.

### Προτεινόμενη χρήση
Για να αιτιολογηθεί online robust comparator μόνο εφόσον υπάρχει σαφές ambiguity set και ίσο interaction budget.

### Παραπομπή
Dong et al., arXiv:2209.13841.

## 2. Δύο διαφορετικές αβεβαιότητες
- Τύπος: πιστή παράφραση
- Θέση: Introduction, robust optimistic update discussion
- Ισχυρισμός: Το algorithm πρέπει να χειριστεί τόσο statistical uncertainty από περιορισμένα observations όσο και uncertainty του robust transition set.
- Κεφάλαιο: Μοντέλο αβεβαιότητας
- Θέματα: epistemic uncertainty; ambiguity set; optimism
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η optimism construction αποτυπώνει uncertainty που προέρχεται από ιστορικά δεδομένα επιπλέον της uncertainty που ήδη περιγράφει το robust MDP.

### Συμφραζόμενα
Η distinction αφορά θεωρητικό online robust learning.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν πρέπει να συγχέεται με aleatoric/epistemic decomposition ενός calibrated detector.

### Προτεινόμενη χρήση
Να δηλώνονται χωριστά estimation uncertainty και assumed deployment ambiguity.

### Παραπομπή
Dong et al., 2022.