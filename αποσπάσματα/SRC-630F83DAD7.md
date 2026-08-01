---
κωδικός: SRC-630F83DAD7
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επαληθευμένα τεκμήρια — SRC-630F83DAD7

## 1. Procedural diversity για generalization
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Introduction, Section 2
- **Ισχυρισμός:** Το Procgen χρησιμοποιεί procedural generation ώστε οι agents να εκπαιδεύονται και να αξιολογούνται σε μεγάλες distributions διαφορετικών levels αντί να επαναλαμβάνουν σχεδόν τα ίδια states.
- **Κεφάλαιο:** Benchmark design
- **Θέματα:** procedural generation; environment diversity; overfitting
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η ποικιλία του environment distribution είναι μέρος του benchmark και όχι απλώς augmentation του agent.

### Προτεινόμενη χρήση
Versioned GridWorld map families και disjoint environment seeds.

## 2. Disjoint training και test levels
- **Τύπος:** πιστή παράφραση
- **Θέση:** Introduction, Experimental Protocols
- **Ισχυρισμός:** Το benchmark υποστηρίζει ξεχωριστά generated training και test sets ώστε να μετράται generalization αντί memorization.
- **Κεφάλαιο:** Train-test protocol
- **Θέματα:** held-out seeds; generalization gap; leakage control
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Train/test map distributions παραμένουν χωριστές από changepoint schedules και hyperparameter tuning.

## 3. Μεγάλο finite training set δεν αποκλείει overfitting
- **Τύπος:** πιστή παράφραση
- **Θέση:** Introduction and generalization experiments
- **Ισχυρισμός:** Deep RL agents μπορούν να overfit ακόμη και σε σχετικά μεγάλες finite collections levels, άρα η fixed-sequence training performance δεν αρκεί ως evidence γενίκευσης.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** memorization; overfitting; evaluation
- **Κατάσταση:** επαληθευμένο

## 4. Solvability δεν είναι αυτόματη
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 2.1 Environment Desiderata
- **Ισχυρισμός:** Η procedural generation στοχεύει solvable levels αλλά δεν εγγυάται απόλυτη solvability· οι authors εκτιμούν ποσοστό άνω του 99%.
- **Κεφάλαιο:** Environment validation
- **Θέματα:** solvability; procedural maps; reachability
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Κάθε generated ή perturbed GridWorld περνά explicit reachability/solvability validation.

## 5. Generalization ≠ online recovery
- **Τύπος:** πιστή παράφραση
- **Θέση:** Overall benchmark setup
- **Ισχυρισμός:** Το Procgen μετρά performance σε held-out generated levels με fixed learned policy/training protocol και δεν αποτελεί sequential changepoint adaptation benchmark.
- **Κεφάλαιο:** Theoretical boundaries
- **Θέματα:** zero-shot generalization; online adaptation; benchmark semantics
- **Κατάσταση:** επαληθευμένο

### Παραπομπή
Cobbe et al., *Leveraging Procedural Generation to Benchmark Reinforcement Learning*, ICML 2020, PMLR 119.