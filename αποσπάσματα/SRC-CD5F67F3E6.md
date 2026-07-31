---
κωδικός: SRC-CD5F67F3E6
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Αποσπάσματα — Proximal Policy Optimization Algorithms

## Τεκμήριο E1
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract και §1
- **Ισχυρισμός:** PPO εναλλάσσει data collection και πολλαπλά minibatch optimization epochs.
- **Κατάσταση:** επαληθευμένο

Η policy συλλέγει trajectories και το ίδιο batch χρησιμοποιείται για περισσότερα από ένα stochastic-gradient epochs μέσω surrogate objective.

**Παραπομπή:** Schulman et al., 2017, Abstract και §1.

## Τεκμήριο E2
- **Τύπος:** πιστή παράφραση
- **Θέση:** §3, Equation 7
- **Ισχυρισμός:** Το PPO-Clip περιορίζει το κίνητρο για μεγάλες probability-ratio μεταβολές.
- **Κατάσταση:** επαληθευμένο

Το objective λαμβάνει το minimum του unclipped και του clipped surrogate, δημιουργώντας pessimistic bound όταν η update κινείται υπερβολικά μακριά από την παλιά policy.

**Παραπομπή:** Schulman et al., 2017, §3.

## Τεκμήριο E3
- **Τύπος:** πιστή παράφραση
- **Θέση:** §4
- **Ισχυρισμός:** Adaptive KL penalty είναι διαφορετική PPO variant.
- **Κατάσταση:** επαληθευμένο

Η KL-penalty παραλλαγή προσαρμόζει τον penalty coefficient ώστε η observed KL να παραμένει κοντά σε target, αλλά απέδωσε χειρότερα από το clipping στα reported experiments.

**Παραπομπή:** Schulman et al., 2017, §4.

## Τεκμήριο E4
- **Τύπος:** πιστή παράφραση
- **Θέση:** §6.1 και Table 1
- **Ισχυρισμός:** Η clipping variant αξιολογήθηκε σε επτά MuJoCo tasks με τρία seeds ανά task.
- **Κατάσταση:** επαληθευμένο

Μεταξύ των εξεταζόμενων surrogate settings, clipping με `ε=0.2` είχε το υψηλότερο average normalized score στα 21 runs.

**Περιορισμός:** μικρός αριθμός seeds και stationary benchmark.

**Παραπομπή:** Schulman et al., 2017, §6.1 και Table 1.

## Τεκμήριο E5
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, §§6–7
- **Ισχυρισμός:** PPO είναι standard performance/sample-efficiency baseline, όχι resilience mechanism.
- **Κατάσταση:** επαληθευμένο

Η αξιολόγηση καλύπτει continuous control και Atari, χωρίς environmental changes, recovery, detector ή safety guarantees.

**Παραπομπή:** Schulman et al., 2017, Abstract και experiments.
