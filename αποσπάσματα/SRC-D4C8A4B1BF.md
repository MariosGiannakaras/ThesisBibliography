---
κωδικός: SRC-D4C8A4B1BF
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια — Resilience and Resilient Systems of Artificial Intelligence

## 1. Robustness δεν αρκεί για resilience
- Τύπος: πιστή παράφραση
- Θέση: Introduction / Research Gap
- Ισχυρισμός: Η review διαχωρίζει resilience από μεμονωμένες ιδιότητες όπως robustness ή fault tolerance.
- Κεφάλαιο: Θεωρητικό πλαίσιο
- Θέματα: robustness; resilience; recovery; adaptation
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η εργασία υποστηρίζει ότι resilient AI system δεν χαρακτηρίζεται μόνο από ικανότητα να αντέχει disturbances. Χρειάζεται επίσης detection/handling, graceful degradation, recovery και adaptation σε μεταβαλλόμενες συνθήκες.

### Προτεινόμενη χρήση
Για τον βασικό ορισμό ότι static/worst-case robustness δεν ταυτίζεται με online resilience.

## 2. Τέσσερις φάσεις system resilience
- Τύπος: πιστή παράφραση
- Θέση: Section 3.1
- Ισχυρισμός: Η resilience process αναλύεται σε preparation, absorption, recovery και adaptation.
- Κεφάλαιο: Evaluation framework
- Θέματα: preparation; absorption; recovery; adaptation
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η planning/preparation φάση αφορά risk assessment και detection readiness, η absorption φάση περιορίζει την άμεση επίδραση της διαταραχής, η recovery αποκαθιστά χαμένη λειτουργικότητα/performance και η adaptation αλλάζει το system ώστε να αντιμετωπίζει καλύτερα μελλοντικές disturbances.

### Περιορισμοί και κίνδυνος παρερμηνείας
Η πηγή είναι broad AI/system review· η αντιστοίχιση των phases σε detector, degradation curve και policy learning είναι εφαρμογή της διπλωματικής.

### Προτεινόμενη χρήση
Για να οργανωθούν οι thesis metrics σε immediate degradation, recovery και post-recovery learning.

## 3. Graceful degradation
- Τύπος: πιστή παράφραση
- Θέση: Section 3.1
- Ισχυρισμός: Όταν disturbance δεν μπορεί να απορροφηθεί πλήρως, resilient system μπορεί να υποβαθμίζει ελεγχόμενα μη κρίσιμες λειτουργίες διατηρώντας core functionality.
- Κεφάλαιο: Safety / robustness metrics
- Θέματα: graceful degradation; fallback; retained functionality
- Κατάσταση: επαληθευμένο

### Προτεινόμενη χρήση
Για να διαχωριστεί ελεγχόμενη fallback performance από ανεξέλεγκτη collapse μετά από shift.

## 4. Affordable resilience
- Τύπος: πιστή παράφραση
- Θέση: Section 3.1, Affordable Resilience discussion
- Ισχυρισμός: Η resilience πρέπει να σταθμίζεται με lifecycle/resource cost και nominal performance.
- Κεφάλαιο: Resource-aware evaluation
- Θέματα: resource cost; performance trade-off; affordable resilience
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η review περιγράφει affordable resilience ως ισορροπία μεταξύ τεχνικών resilience χαρακτηριστικών και κόστους, και συζητά optimization που ανταλλάσσει nominal performance με resilience indicator υπό περιορισμούς.

### Προτεινόμενη χρήση
Για να δικαιολογηθεί report memory, compute, prior-data και interaction overhead μαζί με recovery benefit.

## 5. Ένα μόνο resilience metric είναι ανεπαρκές
- Τύπος: πιστή παράφραση
- Θέση: Research Gap / resilience-indicator discussion
- Ισχυρισμός: Η review παρατηρεί ότι πολλές μελέτες μετρούν μόνο perturbation absorption ή μόνο recovery rate και έτσι καλύπτουν μόνο μέρος του resilience concept.
- Κεφάλαιο: Threats to validity
- Θέματα: multidimensional metrics; scalar score
- Κατάσταση: επαληθευμένο

### Προτεινόμενη χρήση
Αν παρουσιαστεί aggregate resilience score, να συνοδεύεται από constituent metrics: degradation, recovery, adapted return, safety και resource cost.