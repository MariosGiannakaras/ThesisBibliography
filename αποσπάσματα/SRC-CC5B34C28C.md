---
κωδικός: SRC-CC5B34C28C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια

## 1. Worst-case ισοδυναμία δεν συνεπάγεται ισοδύναμη πρακτική απόδοση
- Τύπος: πιστή παράφραση
- Θέση: Abstract, Introduction
- Ισχυρισμός: Πολλές optimal robust policies μπορούν να έχουν ίδια worst-case value αλλά διαφορετική απόδοση υπό μη πλήρως adversarial transition choices.
- Κεφάλαιο: Robust baselines / Μετρικές
- Θέματα: worst-case return; nominal performance; conservativeness
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η standard robust objective μπορεί να αφήνει ακαθόριστη επιλογή μεταξύ policies που είναι όλες worst-case optimal, παρότι κάποιες αποδίδουν καλύτερα σε άλλες plausible realizations του uncertainty set.

### Συμφραζόμενα
Η εργασία εισάγει best-effort dominance ως tie-breaker.

### Περιορισμοί και κίνδυνος παρερμηνείας
Το best-effort criterion δεν εγκαταλείπει το worst-case objective και δεν αφορά post-failure recovery.

### Προτεινόμενη χρήση
Να αναφέρονται μαζί worst-case, nominal/clean και typical in-set returns.

### Παραπομπή
Abate et al., AAAI 2026.

## 2. ORBE ως robust-policy tie-breaker
- Τύπος: πιστή παράφραση
- Θέση: Sections 3–5
- Ισχυρισμός: ORBE policies είναι worst-case optimal και δεν κυριαρχούνται από άλλη policy στο uncertainty set.
- Κεφάλαιο: Policy selection
- Θέματα: ORBE; dominance; robust optimality
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Το ORBE criterion επιλέγει policy μέσα στο σύνολο των robust-optimal candidates ώστε να αποφεύγεται policy που είναι παντού όχι καλύτερη και κάπου αυστηρά χειρότερη.

### Συμφραζόμενα
Πρόκειται για s-rectangular RMDP setting.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν καλύπτει out-of-set structural changes ή continued learning.

### Προτεινόμενη χρήση
Για explicit tie-breaking rule και conservativeness analysis robust baselines.

### Παραπομπή
Abate et al., Sections 3–5.