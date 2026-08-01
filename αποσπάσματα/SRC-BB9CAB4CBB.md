---
κωδικός: SRC-BB9CAB4CBB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Επαληθευμένα τεκμήρια — SRC-BB9CAB4CBB

## 1. Aleatoric και epistemic uncertainty

**Τεκμήριο:** Η εργασία διακρίνει την aleatoric uncertainty ως εγγενή τυχαιότητα του συστήματος από την epistemic uncertainty ως έλλειψη γνώσης που μπορεί να μειωθεί με συλλογή δεδομένων.

**Παράφραση για χρήση:** Η στοχαστικότητα μιας μετάβασης και η άγνοια του agent για το μοντέλο αποτελούν διαφορετικές πηγές αβεβαιότητας και πρέπει να καταγράφονται χωριστά.

**Χρήση:** Θεωρητικό υπόβαθρο· taxonomy perturbations.

## 2. Probabilistic models και αβεβαιότητα μοντέλου

**Τεκμήριο:** Τα κλασικά MDP/POMDP εκφράζουν aleatoric uncertainty μέσω probability distributions, ενώ robust ή uncertain MDPs προσθέτουν uncertainty sets πάνω στις ίδιες τις πιθανότητες.

**Παράφραση για χρήση:** Ένα probability kernel περιγράφει stochastic outcomes, ενώ ένα σύνολο πιθανών kernels περιγράφει αβεβαιότητα για το ποιο μοντέλο ισχύει.

**Χρήση:** Διάκριση action/transition noise από model uncertainty.

## 3. Reducible uncertainty και exploration

**Τεκμήριο:** Στο online RL, η αλληλεπίδραση με το περιβάλλον μπορεί να μειώσει epistemic uncertainty, ενώ η aleatoric variability δεν εξαλείφεται απλώς με περισσότερα samples.

**Παράφραση για χρήση:** Η διερεύνηση μπορεί να βελτιώσει τη γνώση του agent για το περιβάλλον, αλλά δεν καταργεί την εγγενή τυχαιότητα των αποτελεσμάτων.

**Χρήση:** Ερμηνεία exploration mechanisms και uncertainty estimates.

## 4. Robustness και conservativeness

**Τεκμήριο:** Worst-case robust approaches μπορούν να εξασφαλίσουν απόδοση έναντι uncertainty sets, αλλά ενδέχεται να παράγουν υπερβολικά συντηρητικές πολιτικές.

**Παράφραση για χρήση:** Η καλύτερη disturbed performance δεν αρκεί για να χαρακτηριστεί ένας agent ανώτερος, αν αγοράζεται με μεγάλη απώλεια nominal utility.

**Χρήση:** Κοινή αναφορά clean και disturbed return.

## 5. Αλλαγή dynamics έναντι απίθανου stochastic event

**Τεκμήριο:** Για changing distributions, βασική πρόκληση είναι να αποφασιστεί πόσες απίθανες παρατηρήσεις απαιτούνται πριν συμπεράνουμε ότι άλλαξε το περιβάλλον και δεν πρόκειται απλώς για φυσιολογική τυχαιότητα.

**Παράφραση για χρήση:** Ένα prediction-error spike αποτελεί ένδειξη αλλαγής, αλλά χρειάζεται thresholding και αξιολόγηση false alarms/delay πριν θεωρηθεί change detector.

**Χρήση:** Detection protocol και threats to validity.

## 6. Όριο μεταφοράς

**Τεκμήριο:** Η εργασία παρουσιάζει challenges και model families, όχι μια ενιαία empirical ranking αλγορίθμων.

**Παράφραση για χρήση:** Η πηγή τεκμηριώνει τη μοντελοποίηση και τις trade-offs, όχι την επιλογή συγκεκριμένου τελικού agent.

**Χρήση:** Περιορισμός ισχυρισμών.