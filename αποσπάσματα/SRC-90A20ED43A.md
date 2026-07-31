---
κωδικός: SRC-90A20ED43A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Αποσπάσματα — Survival of the Fittest: Evolutionary Adaptation of Policies for Environmental Shifts

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract και Introduction
- **Ισχυρισμός:** Η εργασία αντιμετωπίζει μεγάλη μετατόπιση του περιβάλλοντος μέσω post-shift policy adaptation και όχι μόνο μέσω προεκπαίδευσης για bounded robustness.
- **Κεφάλαιο:** Σχετικές εργασίες· Agent taxonomy
- **Θέματα:** environmental shift; adaptation; robust RL boundary
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Όταν η δυναμική του περιβάλλοντος αλλάζει δραστικά, η παλιά optimal policy μπορεί να γίνει υποβέλτιστη ή να αποτύχει. Ο ERPO χρησιμοποιεί νέα trajectories στο μετατοπισμένο περιβάλλον για να προσαρμόσει επαναληπτικά την policy.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρόκειται για frozen robust policy και δεν αποτρέπει κατ’ ανάγκη την αρχική πτώση επίδοσης.

### Προτεινόμενη χρήση

Ορισμός της κατηγορίας `post_shift_retraining` χωριστά από `static_robustness`.

### Παραπομπή

Paul & Deshmukh, 2024, Abstract και §1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 3.2, algorithm description
- **Ισχυρισμός:** Η training policy μεταβαίνει σταδιακά από την παλιά policy προς μια νέα policy.
- **Κεφάλαιο:** Μεθοδολογία· Agent architectures
- **Θέματα:** warm start; old-policy adherence; exploration
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Ο ERPO αρχικοποιεί την training policy ως weighted combination της παλιάς optimal policy και μιας νέας αρχικά τυχαίας policy. Σε κάθε iteration μειώνει το βάρος της παλιάς policy και ενημερώνει τη νέα policy από batches trajectories.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το adherence schedule είναι ουσιώδες hyperparameter και δεν υπάρχει λόγος να θεωρηθεί universal.

### Προτεινόμενη χρήση

Καταγραφή `old_policy_weight` και σύγκριση διαφορετικών decay schedules χωρίς test-set tuning.

### Παραπομπή

Paul & Deshmukh, 2024, §3.2.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** Sections 3–5
- **Ισχυρισμός:** Η ενημέρωση δίνει έμφαση σε trajectories που είναι περισσότερο πληροφοριακές σε σχέση με το batch.
- **Κεφάλαιο:** Μεθοδολογία
- **Θέματα:** replicator dynamics; trajectory weighting; batch adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Αντί να αντιμετωπίζονται όλα τα βήματα ενός batch ως ισοδύναμα, η replicator-style ενημέρωση ενισχύει state–action επιλογές που συνδέονται με trajectories με ουσιαστικά διαφορετική απόδοση από την υπόλοιπη παρτίδα.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η περιγραφή αυτή δεν ισοδυναμεί με απόδειξη ότι το weighting είναι καλύτερο σε όλα τα reward structures.

### Προτεινόμενη χρήση

Αιτιολόγηση ενός προαιρετικού informative-trajectory adaptation pilot.

### Παραπομπή

Paul & Deshmukh, 2024, §§3–5.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 4
- **Ισχυρισμός:** Τα experiments περιλαμβάνουν discrete navigation environments με structural shifts και συγκρίσεις scratch/warm-start.
- **Κεφάλαιο:** Πειραματικό περιβάλλον· Baselines
- **Θέματα:** FrozenLake; Taxi; CliffWalking; MiniGrid; warm start
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η αξιολόγηση χρησιμοποιεί FrozenLake, Taxi, CliffWalking, MiniGrid DistributionShift και Walls&Lava και συγκρίνει ERPO με PPO, PPO-DR, DQN και A2C, με εκπαίδευση από την αρχή ή από προεκπαιδευμένο μοντέλο όπου εφαρμόζεται.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η ποικιλία benchmarks δεν εξαλείφει τις διαφορές implementation και tuning μεταξύ algorithm families.

### Προτεινόμενη χρήση

Σχεδιασμός scratch, warm-start και no-transfer comparators για severe layout changes.

### Παραπομπή

Paul & Deshmukh, 2024, §4.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 5 και Discussion
- **Ισχυρισμός:** Ο ERPO αναφέρεται ότι διατηρεί καλύτερη απόδοση καθώς αυξάνεται η ένταση structural shift στα εξεταζόμενα settings.
- **Κεφάλαιο:** Αποτελέσματα· Threats to validity
- **Θέματα:** adaptation efficiency; shift severity; algorithm comparison
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στα Walls&Lava levels και στα υπόλοιπα εξεταζόμενα benchmarks, οι συγγραφείς αναφέρουν ταχύτερη προσαρμογή και καλύτερη απόδοση του ERPO από τις συγκεκριμένες baseline configurations.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν αποτελεί universal ranking. Στο διαθέσιμο κείμενο δεν εντοπίστηκε ενιαίο πλήρες protocol seeds, confidence intervals και statistical tests για όλες τις συγκρίσεις.

### Προτεινόμενη χρήση

Evidence ότι controlled policy reuse αξίζει feasibility pilot, όχι προαποφασισμένη επιλογή τελικού agent.

### Παραπομπή

Paul & Deshmukh, 2024, §§5–6.

## Τεκμήριο E6

- **Τύπος:** πιστή παράφραση
- **Θέση:** Discussion — Limitations and Future Work
- **Ισχυρισμός:** Η τρέχουσα μέθοδος περιορίζεται σε discrete, single-agent settings.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** discrete state-action; single agent; scope
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς δηλώνουν ότι η τρέχουσα υλοποίηση αφορά διακριτούς χώρους καταστάσεων και ενεργειών και single-agent models, ενώ continuous και multi-agent επεκτάσεις παραμένουν μελλοντική εργασία.

### Προτεινόμενη χρήση

Οριοθέτηση της μεταφοράς των αποτελεσμάτων στο τελικό GridWorld.

### Παραπομπή

Paul & Deshmukh, 2024, §6.
