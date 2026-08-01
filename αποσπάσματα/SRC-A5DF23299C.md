---
κωδικός: SRC-A5DF23299C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επαληθευμένα τεκμήρια — SRC-A5DF23299C

## 1. Robustness και resilience είναι διαφορετικές ιδιότητες
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Introduction
- **Ισχυρισμός:** Η robustness αφορά διατήρηση performance υπό perturbation, ενώ η resilience δίνει έμφαση στην προετοιμασία, προσαρμογή και ταχεία ανάκαμψη μετά από degradation ή unexpected change.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο / Ορισμοί
- **Θέματα:** robustness; resilience; recovery
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Θεμελίωση της διάκρισης immediate disturbed performance από post-change recovery process.

## 2. Resilience ως μέγεθος και διάρκεια degradation
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-C
- **Ισχυρισμός:** Η ποσοτικοποίηση resilience συνδέεται με το μέγεθος και τη διάρκεια της πτώσης reward σε σχέση με unperturbed reference system.
- **Κεφάλαιο:** Μετρικές
- **Θέματα:** degradation; duration; reference curve
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η αξιολόγηση recovery πρέπει να αναφέρεται σε matched reference trajectory/curve και όχι μόνο στην απόλυτη τελική επίδοση του perturbed agent.

## 3. Area between perturbed και unperturbed curves
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-C, Eq. 11
- **Ισχυρισμός:** Η εργασία προτείνει το ολοκλήρωμα/area μεταξύ perturbed και unperturbed reward curves μετά την εισαγωγή perturbation ως resilience metric.
- **Κεφάλαιο:** Μετρικές / Recovery
- **Θέματα:** AUC loss; transient degradation; reward curve
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
`post_change_performance_gap_auc` με matched reference seed/context.

## 4. Degradation και restorative time
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-C, Eqs. 12–15
- **Ισχυρισμός:** Ορίζεται χρόνος από perturbation onset μέχρι το minimum performance και στη συνέχεια χρόνος από το minimum μέχρι το καλύτερο μεταγενέστερο recovered performance.
- **Κεφάλαιο:** Μετρικές
- **Θέματα:** degradation time; restorative time; minimum; recovery
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Report `time_to_minimum_after_change`, `restorative_time`, minimum post-change score και maximum recovered score χωριστά.

## 5. Natural και adversarial perturbations δεν συγχέονται
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section III-A
- **Ισχυρισμός:** Η αξιολόγηση περιλαμβάνει random perturbations για missing/erroneous measurements αλλά και intentional adversarial perturbation agents.
- **Κεφάλαιο:** Threat model
- **Θέματα:** observation corruption; adversarial attack; natural perturbation
- **Κατάσταση:** επαληθευμένο

### Περιορισμοί και κίνδυνος παρερμηνείας
Για τη διπλωματική μόνο η non-adversarial/random υποπερίπτωση μεταφέρεται άμεσα. Τα malicious attacks αποτελούν διαφορετικό threat model.

## 6. Recovery curve δεν αποδεικνύει parameter adaptation
- **Τύπος:** πιστή παράφραση
- **Θέση:** Experimental framing / test-time methodology
- **Ισχυρισμός:** Η εργασία αξιολογεί κυρίως pre-trained agents υπό test-time perturbations· συνεπώς η ανάκαμψη της επίδοσης δεν πρέπει αυτομάτως να αποδίδεται σε continued learning.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** frozen policy; behavioral recovery; online learning
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Κάθε thesis curve δηλώνει αν weights/Q-values συνεχίζουν να ενημερώνονται μετά το change.

### Παραπομπή
Tjhay, Bessa & Paulos, *On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management*, arXiv:2504.13314, 2025.