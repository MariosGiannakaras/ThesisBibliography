---
κωδικός: SRC-A5DF23299C
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2504.13314v1, On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επιστημονική ανάλυση — SRC-A5DF23299C

## Βιβλιογραφική ταυτότητα
- **Τίτλος:** On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management
- **Συγγραφείς:** Timothy Tjhay, Ricardo J. Bessa, José Paulos
- **Έτος:** 2025
- **Ρόλος:** κύρια/μετρική πηγή

## Ερευνητικό αντικείμενο
Η εργασία προτείνει quantitative framework για robustness και resilience RL agents σε Grid2Op congestion management. Ξεχωρίζει ρητά robustness — διατήρηση performance υπό perturbation — από resilience — adaptation/recovery μετά από degradation — και ορίζει metrics πάνω σε reward trajectories και system-state effects.

## Perturbations
Η αξιολόγηση γίνεται κυρίως σε pre-trained RL agent κατά test time. Χρησιμοποιούνται perturbation agents που αλλοιώνουν το **input/observation** του AI system χωρίς να αλλάζουν το πραγματικό environment state. Περιλαμβάνονται:
- random perturbations που προσομοιώνουν missing/erroneous measurements,
- δύο intentional/adversarial perturbation schemes.

Η natural/random perturbation υποπερίπτωση είναι άμεσα σχετική με non-adversarial observation corruption· τα malicious attacks δεν μεταφέρονται στο core thesis threat model.

## Robustness metrics
Η paper περιλαμβάνει metrics για:
- reward impact,
- stability/reachability/failure avoidance,
- reward per non-noop action,
- action sensitivity σε perturbed inputs,
- weak spots/input components που αλλάζουν decisions.

## Resilience metrics
Η resilience συνδέεται με **μέγεθος και διάρκεια performance degradation** σε σχέση με unperturbed reference curve. Προτείνονται:
1. area μεταξύ perturbed και unperturbed reward curves μετά την έναρξη perturbation,
2. degradation time από perturbation onset έως το minimum-performance episode,
3. restorative time από minimum έως post-perturbation maximum,
4. minimum degradation performance και maximum restored performance,
5. similarity πραγματικού system state μεταξύ perturbed και reference trajectories.

## Σχέση με τη διπλωματική
Η πηγή είναι πολύ χρήσιμη για operationalization resilience σε single-agent RL, παρότι το domain είναι power-grid management. Ενισχύει την ήδη κλειδωμένη process-based λογική: δεν αρκεί final return, πρέπει να μετριούνται transient loss, degradation, recovery duration και residual performance gap.

Στο GridWorld η ακριβής μεταφορά είναι:
- `reference_performance_curve`,
- `post_change_performance_gap_auc`,
- `time_to_minimum_after_change`,
- `restorative_time`,
- `minimum_post_change_performance`,
- `maximum_recovered_performance`,
- optional state/occupancy divergence έναντι matched reference.

## Κρίσιμα όρια
- Η paper χρησιμοποιεί τόσο natural όσο και adversarial observation perturbations. Το thesis core θα κρατήσει μόνο non-adversarial/random/noisy cases ως direct evidence.
- Η αξιολόγηση είναι κυρίως test-time perturbation σε pre-trained agent, όχι continued-learning algorithm comparison.
- Recovery σε reward curve μπορεί να προκύψει από transient perturbation pattern χωρίς parameter adaptation· άρα πρέπει να δηλώνεται αν η policy ενημερώνεται.
- Power-grid state similarity δεν μεταφέρεται αυτούσια σε GridWorld· μπορεί να αντικατασταθεί με occupancy/state-distribution distance.

## Πειραματικές επιπτώσεις
- Κάθε recovery curve χρειάζεται matched unperturbed reference under same seed/context.
- AUC loss και time-to-recovery δεν συγχωνεύονται σε έναν scalar χωρίς reporting των components.
- Ορίζεται perturbation onset ακριβώς.
- Δηλώνεται αν recovery είναι behavioral/frozen-policy ή learning-based.
- Natural και adversarial perturbations αναφέρονται χωριστά.

## Απόφαση
**Επαληθευμένη — εξαγωγή ναι ως κύρια/μετρική πηγή.** Χρησιμοποιείται για quantitative robustness/resilience definitions και curve-based recovery metrics, με ρητή απομόνωση του non-adversarial υποσυνόλου.