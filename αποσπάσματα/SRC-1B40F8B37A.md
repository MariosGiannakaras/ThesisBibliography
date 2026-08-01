---
κωδικός: SRC-1B40F8B37A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια — Collaboration Promotes Group Resilience in Multi-Agent RL

## 1. Resilience υπό bounded environmental perturbation
- Τύπος: πιστή παράφραση
- Θέση: Section 3, Measuring Group Resilience
- Ισχυρισμός: Η resilience συνδέεται με διατήρηση performance όταν το perturbed MDP βρίσκεται εντός προκαθορισμένης απόστασης από το reference MDP.
- Κεφάλαιο: Μετρικές
- Θέματα: resilience; perturbation severity; MDP distance
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η εργασία ορίζει distance `δ(M,M')` μεταξύ αρχικού και perturbed environment και bound `K`, και αξιολογεί αν η utility μετά την perturbation παραμένει πάνω από συγκεκριμένο κλάσμα της original performance.

### Περιορισμοί και κίνδυνος παρερμηνείας
Η επιλογή distance metric είναι μέρος του definition και δεν είναι domain-neutral.

### Προτεινόμενη χρήση
Για να δηλώνεται shift severity και να αναφέρεται performance-vs-severity curve.

## 2. Relative-to-optimum έναντι relative-to-origin
- Τύπος: πιστή παράφραση
- Θέση: Definitions 1–3
- Ισχυρισμός: Η resilience μπορεί να κανονικοποιείται είτε ως προς το optimum κάθε environment είτε ως προς την original utility του ίδιου agent/group.
- Κεφάλαιο: Μετρικές
- Θέματα: normalization; relative resilience
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η relative-to-optimum formulation διορθώνει για αλλαγές στο achievable optimum του perturbed environment, ενώ η relative-to-origin formulation είναι απλούστερη όταν το optimum δεν είναι γνωστό αλλά συγκρίνει απευθείας pre/post perturbation utility.

### Περιορισμοί και κίνδυνος παρερμηνείας
Το optimum μπορεί να είναι άγνωστο ή ακριβό να υπολογιστεί. Η chosen normalization πρέπει να δηλώνεται ρητά.

### Προτεινόμενη χρήση
Για να διαχωριστεί retained-performance score από normalized-to-regime-optimum score.

## 3. No-op / low-baseline pathology
- Τύπος: πιστή παράφραση
- Θέση: discussion after relative-to-origin/in-expectation definitions
- Ισχυρισμός: Μια policy με πολύ χαμηλή αρχική utility μπορεί να φαίνεται τεχνητά resilient σε ratio που μετρά μόνο την πτώση από το δικό της baseline.
- Κεφάλαιο: Threats to validity / Metrics
- Θέματα: metric gaming; baseline quality; absolute return
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Εφόσον η relative-to-origin resilience συγκρίνει perturbed performance με την ίδια policy πριν την perturbation, μία μη βέλτιστη ή no-op policy μπορεί να εμφανίζει μικρή σχετική πτώση και άρα υψηλό resilience score παρά το ότι η πραγματική task performance είναι κακή.

### Προτεινόμενη χρήση
Κάθε resilience ratio να συνοδεύεται υποχρεωτικά από absolute pre-change και post-change return και, όπου είναι εφικτό, από regret/gap προς regime-specific optimum.

## 4. Διακριτοί τύποι perturbation
- Τύπος: πιστή παράφραση
- Θέση: Section 3.1, Definitions 4–6
- Ισχυρισμός: Transition-function, reward-function και initial-state perturbations είναι διαφορετικές atomic αλλαγές του MDP.
- Κεφάλαιο: Experimental design
- Θέματα: transition shift; reward shift; initial-state shift
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η εργασία ορίζει χωριστά perturbation που αλλάζει transition probability για state-action pair, perturbation που αλλάζει reward και perturbation που αλλάζει initial state.

### Προτεινόμενη χρήση
Να μην αναφέρονται διαφορετικά causal shift types ως μία ενιαία κατηγορία “uncertainty”.

## 5. Expected resilience εξαρτάται από perturbation distribution
- Τύπος: πιστή παράφραση
- Θέση: Definition 3
- Ισχυρισμός: Όταν resilience υπολογίζεται ως expectation σε perturbed environments, το αποτέλεσμα εξαρτάται από τη distribution από την οποία δειγματίζονται οι perturbations.
- Κεφάλαιο: Reproducibility / Metrics
- Θέματα: perturbation distribution; seeds; expected resilience
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η resilience-in-expectation ορίζεται ως expected utility πάνω σε perturbed MDPs εντός severity bound. Επομένως το sampling distribution των perturbations αποτελεί μέρος του benchmark definition.

### Προτεινόμενη χρήση
Να δηλώνονται perturbation generator, seed distribution και severity sampling policy.

## Scope caveat
Η empirical contribution της πηγής αφορά collaboration σε MARL. Στη διπλωματική χρησιμοποιούνται μόνο οι metric/formalization insights· δεν μεταφέρεται claim ότι collaboration βελτιώνει single-agent resilience.