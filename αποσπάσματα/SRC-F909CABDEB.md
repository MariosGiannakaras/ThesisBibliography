---
κωδικός: SRC-F909CABDEB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-30"
---

# Αποσπάσματα — A Survey of Continual Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-B και Figure 3
- **Ισχυρισμός:** Η continual adaptation πρέπει να αξιολογείται ως ισορροπία stability, plasticity και scalability, όχι μόνο ως τελική επίδοση στο νεότερο περιβάλλον.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο και ερευνητικά κριτήρια
- **Θέματα:** stability, plasticity, scalability, continual RL
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η survey ορίζει stability ως διατήρηση προηγούμενων ικανοτήτων, plasticity ως αποτελεσματική μάθηση και μεταφορά σε νέες συνθήκες, και scalability ως δυνατότητα συνέχισης με περιορισμένη μνήμη και υπολογισμό. Μια μέθοδος που αποθηκεύει κάθε policy ή επανεκπαιδεύεται πλήρως μπορεί να έχει καλή απόδοση αλλά να μην αποτελεί κλιμακώσιμη continual λύση.

### Συμφραζόμενα

Στη διπλωματική η έννοια μπορεί να χρησιμοποιηθεί για να καταγραφεί το κόστος adaptation και αν ο agent διατηρεί επίδοση όταν επιστρέφει παλαιότερη configuration.

### Περιορισμοί και κίνδυνος παρερμηνείας

Αν το experiment δεν επανεξετάζει παλαιότερες συνθήκες, δεν μπορεί να μετρήσει πλήρως stability/forgetting.

### Προτεινόμενη χρήση

Να καθορίσει προαιρετικό recurring-environment test και resource metrics.

### Παραπομπή

Pan et al. (2025), Section III-B και Figure 3.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-C, Equations 7–8
- **Ισχυρισμός:** Average performance και forgetting είναι διαφορετικές μετρικές και πρέπει να αναφέρονται χωριστά σε task sequences.
- **Κεφάλαιο:** Μετρικές
- **Θέματα:** average performance, forgetting, retention
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το average performance συνοψίζει την επίδοση στα tasks που έχουν εμφανιστεί, ενώ το forgetting συγκρίνει την επίδοση ενός task όταν μαθεύτηκε με την τελική επίδοση μετά την εκπαίδευση σε μεταγενέστερα tasks. Υψηλό average score μπορεί να συνυπάρχει με σοβαρή απώλεια παλαιών ικανοτήτων αν το νέο task κυριαρχεί στο aggregate.

### Συμφραζόμενα

Για recurring GridWorld configurations, task μπορεί να είναι κάθε distinct transition/reward regime. Η normalization πρέπει να είναι κοινή και ερμηνεύσιμη.

### Περιορισμοί και κίνδυνος παρερμηνείας

Υπάρχουν διαφορετικοί forgetting definitions, όπως last-vs-best ή signed difference. Πρέπει να επιλεγεί ένας πριν από τα experiments.

### Προτεινόμενη χρήση

Να προστεθεί retention test μόνο αν η μελέτη περιλαμβάνει επαναφορά σε προηγούμενο regime.

### Παραπομπή

Pan et al. (2025), Section III-C, Equations 7–8.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-C, Equations 9–10
- **Ισχυρισμός:** Forward transfer πρέπει να αξιολογεί αν η προηγούμενη γνώση επιταχύνει τη μάθηση νέου task σε σχέση με single-task training from scratch.
- **Κεφάλαιο:** Μετρικές προσαρμογής
- **Θέματα:** forward transfer, backward transfer, learning AUC
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η AUC-based forward-transfer metric συγκρίνει τη learning curve στο νέο task με αντίστοιχο single-task baseline. Θετική τιμή σημαίνει ότι η συσσωρευμένη γνώση επιταχύνει τη μάθηση, ενώ αρνητική τιμή υποδηλώνει negative transfer. Backward transfer εξετάζει αν η μεταγενέστερη μάθηση βελτιώνει παλαιότερα tasks.

### Συμφραζόμενα

Αυτή η λογική είναι πιο κατάλληλη για adaptation speed από σύγκριση μόνο των τελικών returns.

### Περιορισμοί και κίνδυνος παρερμηνείας

Απαιτεί single-task baselines με ίδιο budget και normalization. Δεν είναι δωρεάν προσθήκη στο πειραματικό κόστος.

### Προτεινόμενη χρήση

Να εξεταστεί normalized post-change AUC against restart-from-scratch baseline ως resilience metric.

### Παραπομπή

Pan et al. (2025), Section III-C, Equations 9–10.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-E και Table III
- **Ισχυρισμός:** Η ορατότητα των task boundaries είναι κρίσιμη assumption που διαχωρίζει task-aware από task-agnostic continual learning.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** task boundaries, task identity, non-stationarity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο task-agnostic setting ο agent δεν λαμβάνει task label και μπορεί να μη γνωρίζει πότε άλλαξε το περιβάλλον. Αντίθετα, σε task-incremental ή ορισμένα benchmark settings οι boundaries είναι διαθέσιμες. Η διαφορά αλλάζει ουσιαστικά τη δυσκολία και το αν απαιτείται detector.

### Συμφραζόμενα

Η επίσημη αίτηση αναφέρεται σε απρόβλεπτες αλλαγές, άρα τουλάχιστον ένα evaluation setting πρέπει να μην παρέχει απευθείας change notification στον agent.

### Περιορισμοί και κίνδυνος παρερμηνείας

Known-change experiments παραμένουν χρήσιμα ως oracle ablation για να διαχωριστεί detection από adaptation.

### Προτεινόμενη χρήση

Να συγκριθεί oracle-known change με hidden-change condition.

### Παραπομπή

Pan et al. (2025), Section III-E και Table III.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** Sections III-C–III-D
- **Ισχυρισμός:** Resource metrics όπως memory footprint, model growth, environment interactions και wall-clock overhead είναι απαραίτητο context για scalability claims.
- **Κεφάλαιο:** Μετρικές και περιορισμοί
- **Θέματα:** compute, memory, sample efficiency, scalability
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η survey επισημαίνει ότι δεν υπάρχει ενιαίος scalability scalar. Αντί αυτού, τα benchmarks αναφέρουν proxies όπως model size μετά το task stream, replay-buffer ή auxiliary-model memory, training/inference cost, per-step overhead και interactions μέχρι target performance.

### Συμφραζόμενα

Για τη διπλωματική αυτά τα στοιχεία είναι ιδιαίτερα σημαντικά λόγω περιορισμένου hardware και επειδή ένας σύνθετος adaptive agent μπορεί να κερδίζει λίγο σε reward με πολύ μεγαλύτερο κόστος.

### Περιορισμοί και κίνδυνος παρερμηνείας

Τα proxies δεν είναι πλήρως συγκρίσιμα μεταξύ διαφορετικών implementations ή hardware. Πρέπει να αναφέρονται μαζί με το setup.

### Προτεινόμενη χρήση

Να καταγράφονται environment steps, wall-clock training time, peak memory και parameter count.

### Παραπομπή

Pan et al. (2025), Sections III-C–III-D.