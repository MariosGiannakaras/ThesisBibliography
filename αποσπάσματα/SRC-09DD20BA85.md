---
κωδικός: SRC-09DD20BA85
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Bounded Robustness in Reinforcement Learning via Lexicographic Objectives

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 2–4, Section 2, Definition 1
- **Ισχυρισμός:** Ο θόρυβος παρατήρησης μπορεί να μοντελοποιηθεί με stochastic kernel T(y|x), όπου η πραγματική κατάσταση παραμένει x αλλά ο agent λαμβάνει την παρατήρηση y.
- **Κεφάλαιο:** Μοντέλο αβεβαιότητας
- **Θέματα:** observation noise, DOMDP, sensor error, partial observability
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το observationally-disturbed MDP διατηρεί το state space, τις actions, τις transitions και τη reward function του MDP, αλλά προσθέτει kernel T. Η ποσότητα T(y|x) είναι η πιθανότητα ο agent να μετρήσει y όταν η πραγματική κατάσταση είναι x. Η policy ενεργεί πάνω στη διαταραγμένη παρατήρηση και μπορεί συνεπώς να επιλέξει action ακατάλληλη για το πραγματικό state, χωρίς να έχει αλλάξει η ίδια η transition dynamics.

### Συμφραζόμενα

Το μοντέλο στοχεύει sensor faults, communication errors ή άγνωστη stochastic corruption κατά το deployment. Η adversarial παρατήρηση είναι ειδική περίπτωση και όχι ο μόνος τύπος disturbance.

### Περιορισμοί και κίνδυνος παρερμηνείας

Observation corruption, transition noise και action failure πρέπει να υλοποιούνται ως διαφορετικοί μηχανισμοί. Η αλλαγή της πραγματικής θέσης του agent δεν είναι observation noise.

### Προτεινόμενη χρήση

Να ορίσει formal data-noise scenarios σε GridWorld, όπως neighbour-cell misreporting ή feature dropout, με severity p.

### Παραπομπή

Jarne Ornia et al. (2023), σελ. 2–4, Section 2 και Definition 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–4, Definition 2 και Problem 1
- **Ισχυρισμός:** Η robustness απέναντι σε observation noise μπορεί να μετρηθεί ως διαφορά expected return μεταξύ καθαρής και διαταραγμένης εκτέλεσης της ίδιας policy.
- **Κεφάλαιο:** Μετρικές robustness
- **Θέματα:** robustness regret, clean performance, stressed performance, utility loss
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς ορίζουν disturbed policy ως τον μέσο μετασχηματισμό της αρχικής policy μέσω του noise kernel. Το robustness regret ρ(π,T) ισούται με J(π)−J(⟨π,T⟩). Μηδενική τιμή σημαίνει ότι η expected utility δεν αλλάζει από το disturbance, ενώ θετική τιμή εκφράζει τη ζημιά που προκαλεί ο θόρυβος. Το optimization problem αναζητά robust policy μέσα στο σύνολο policies που παραμένουν εντός ε από την optimal clean utility.

### Συμφραζόμενα

Η μετρική απομονώνει το observation-noise cost, αλλά δεν μετρά από μόνη της recovery time ή adaptation μετά από change point.

### Περιορισμοί και κίνδυνος παρερμηνείας

Ένας agent μπορεί να έχει μικρό robustness regret επειδή είναι εξίσου κακός σε clean και noisy conditions. Γι’ αυτό πρέπει να αναφέρονται μαζί clean return, noisy return και regret.

### Προτεινόμενη χρήση

Να προστεθεί normalized performance drop ή clean-to-stress gap στις μετρικές της διπλωματικής, χωρίς να αντικατασταθούν success rate και recovery metrics.

### Παραπομπή

Jarne Ornia et al. (2023), σελ. 3–4, Definition 2 και Problem 1.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 6–8, Section 4.1, Algorithm 1 και Theorem 6
- **Ισχυρισμός:** Η robustness–utility ανταλλαγή μπορεί να οριστεί ρητά με ανοχή ε, ώστε η robustness να βελτιστοποιείται μόνο μέσα σε policy set με bounded απώλεια primary-task performance.
- **Κεφάλαιο:** Robust-agent design
- **Θέματα:** lexicographic objectives, epsilon-optimality, bounded utility cost
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το LRPG αντιμετωπίζει την expected task utility ως υψηλότερης προτεραιότητας objective και τη robustness ως δευτερεύον objective. Η ανοχή ε διευρύνει το σύνολο acceptable policies γύρω από το optimum, επιτρέποντας επιλογή policy που είναι πιο robust χωρίς να πέφτει κάτω από προκαθορισμένο utility threshold. Υπό τις assumptions του base policy-gradient algorithm, το update διατηρεί convergence και sub-optimality properties.

### Συμφραζόμενα

Η συγκεκριμένη guarantee συνδέεται με το theoretical setup και τις assumptions, όχι με κάθε πρακτική regularizer. Η ιδέα της bounded clean-performance loss είναι ευρύτερα χρήσιμη από τον ίδιο τον LRPG algorithm.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η επιλογή ε είναι normative design decision. Μεγάλο ε μπορεί να επιτρέψει υπερβολικό nominal degradation, ενώ πολύ μικρό ε μπορεί να μην αφήσει χώρο για ουσιαστική robustness.

### Προτεινόμενη χρήση

Να οριστεί αποδεκτό nominal-cost criterion ή Pareto-style αναφορά, αντί να κατατάσσονται agents μόνο από stressed performance.

### Παραπομπή

Jarne Ornia et al. (2023), σελ. 6–8, Section 4.1, Algorithm 1 και Theorem 6.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 8–10, Section 6, Table 1 και Section 7
- **Ισχυρισμός:** Η observational robustness πρέπει να αξιολογείται σε clean, seen stochastic και unseen/adversarial noise regimes, επειδή η επίδοση εξαρτάται από τον base algorithm και τον τύπο disturbance.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** MiniGrid, uniform noise, Gaussian noise, adversarial noise, baselines
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι LR-PPO και LR-A2C policies εκπαιδεύονται με design disturbances και δοκιμάζονται χωρίς θόρυβο, με bounded uniform noise, Gaussian noise και state-adversarial perturbations. Η αξιολόγηση περιλαμβάνει MiniGrid LavaGap, LavaCrossing και DynamicObstacles. Η LRPG μειώνει robustness regret σε αρκετές περιπτώσεις, αλλά η συμπεριφορά διαφέρει ανά PPO/A2C και η adversarially trained SA-PPO παραμένει ιδιαίτερα ισχυρή στο adversarial regime.

### Συμφραζόμενα

Η εργασία χρησιμοποιεί 10 independent agents, αλλά αναφέρει κυρίως median-agent roll-outs. Η διπλωματική πρέπει να χρησιμοποιήσει aggregate uncertainty-aware reporting πάνω σε όλα τα seeds.

### Περιορισμοί και κίνδυνος παρερμηνείας

Seen-noise performance δεν αποδεικνύει γενική robustness. Επίσης, η partially observable φύση ορισμένων MiniGrid tasks μπορεί να επηρεάζει τα αποτελέσματα πέρα από το injected noise.

### Προτεινόμενη χρήση

Να σχεδιαστούν clean, in-range και out-of-range observation-noise tests, με κοινό evaluation budget και ισχυρά vanilla baselines.

### Παραπομπή

Jarne Ornia et al. (2023), σελ. 8–10, Section 6, Table 1 και Section 7.
