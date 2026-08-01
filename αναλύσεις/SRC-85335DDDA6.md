---
κωδικός: SRC-85335DDDA6
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "NeurIPS 2025"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Empirical Study on Robustness and Resilience in Cooperative Multi-Agent Reinforcement Learning

## Βιβλιογραφική ταυτότητα
Simin Li et al. NeurIPS 2025. Large-scale empirical MARL study with 82,620 experiments across multiple environments, uncertainty types, algorithms and hyperparameters.

## Σκοπός
Η εργασία εξετάζει empirical relationships μεταξύ cooperation, robustness και resilience υπό διαφορετικές uncertainty modalities και hyperparameter settings. Παρότι το domain είναι cooperative MARL, η experimental methodology προσθέτει χρήσιμες γενικές αρχές για trustworthy RL evaluation.

## Robustness έναντι resilience
Η εργασία διαχωρίζει:
- **robustness**: performance while uncertainty/perturbation είναι ενεργή,
- **resilience**: ικανότητα recovery αφού το σύστημα βρεθεί σε perturbed state και η disturbance πάψει να εφαρμόζεται.

Αυτή η distinction είναι εξαιρετικά συμβατή με το thesis protocol:
- persistent-noise robustness test,
- transient-shock + post-shock recovery test,
- piecewise-stationary environment-change adaptation test.

Τα τρία δεν πρέπει να συγχωνεύονται.

## Κύρια empirical ευρήματα
### 1. Robustness/resilience δεν γενικεύονται καθολικά
Η εργασία βρίσκει ότι καλή επίδοση υπό μία uncertainty modality δεν συνεπάγεται καλή επίδοση σε άλλη. Για παράδειγμα, action noise, observation noise και environment shifts μπορούν να δίνουν διαφορετικές method rankings. Επίσης group-level και single-agent perturbations σε MARL δεν έχουν ίδια behavior.

### 2. Severity αλλάζει τις σχέσεις
Σε mild perturbations, υψηλή nominal/cooperative performance μπορεί να συσχετίζεται με robustness/resilience. Καθώς αυξάνεται η severity, αυτή η σχέση εξασθενεί και οι rankings μπορούν να αλλάξουν.

### 3. Hyperparameters είναι μέρος της μεθόδου
Σε μεγάλο μέρος των tasks, implementation/hyperparameter choices επηρεάζουν robustness και resilience εξαιρετικά έντονα. Η εργασία αναφέρει ότι common choices όπως parameter sharing, GAE ή PopArt μπορούν σε ορισμένα settings να μειώσουν uncertainty performance, ενώ άλλες choices βοηθούν.

Το ακριβές MARL ranking δεν μεταφέρεται στο thesis. Η γενική methodological συνέπεια όμως είναι ισχυρή: **δεν επιτρέπεται να συγκρίνουμε resilience algorithms με άνισο ή αδιαφανές tuning budget**.

## Πειραματική κλίμακα
Η εργασία αναφέρει 82,620 experiments, 4 real-world-inspired environments, 13 uncertainty types και 15 hyperparameters. Αυτό κάνει την πηγή χρήσιμη κυρίως για meta-evaluation conclusions και όχι για αντιγραφή συγκεκριμένου algorithm.

## Συνάφεια με τη διπλωματική
Η πηγή ενισχύει τις ακόλουθες requirements:
1. shift/uncertainty modalities αξιολογούνται χωριστά,
2. severity sweep, όχι single perturbation level,
3. ίδια tuning/search budget ανά agent,
4. hyperparameter sensitivity report για κρίσιμες παραμέτρους,
5. nominal performance δεν χρησιμοποιείται ως proxy resilience,
6. persistent-uncertainty robustness και recovery-after-shock μετρώνται σε διαφορετικά experiments.

## Περιορισμοί
- Cooperative MARL / Dec-POMDP, όχι single-agent MDP.
- Πολλά uncertainty scenarios περιλαμβάνουν agent-specific effects που δεν υπάρχουν στο GridWorld core.
- Δεν αποτελεί evidence ότι οι συγκεκριμένες MARL hyperparameter recommendations ισχύουν σε tabular Q-learning.
- Η empirical study είναι compute-heavy και δεν προτείνεται να αναπαραχθεί σε κλίμακα.

## Χρήση στη διπλωματική
**Υποστηρικτική protocol/evaluation πηγή μόνο.** Δεν δικαιολογεί MARL implementation.

Χρησιμοποιείται για:
- modality-specific rankings,
- severity sweeps,
- tuning-budget fairness,
- hyperparameter sensitivity,
- separation of persistent robustness from post-disturbance resilience.

## Νέες protocol απαιτήσεις
- Κάθε βασικός agent να έχει ίδιο tuning budget/search space class όπου είναι εφικτό.
- Να αναφέρεται αν hyperparameters είναι global ή retuned ανά shift type/severity.
- Να υπάρχει sensitivity analysis για learning rate, exploration/decay rate και detector threshold.
- Να μην γενικεύεται ranking από ένα uncertainty type σε άλλο.

## Κατάσταση επαλήθευσης
Ελέγχθηκε το πλήρες NeurIPS 2025 paper. **Επιλέγεται ως supporting evaluation source με αυστηρό MARL caveat.**