---
κωδικός: SRC-6F4F8BE003
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Published conference paper, ICLR 2025, official proceedings PDF"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-09-03"
---

# Ανάλυση — Online Reinforcement Learning in Non-Stationary Context-Driven Environments

## Βιβλιογραφική ταυτότητα
- **Συγγραφείς:** Pouya Hamadanian, Arash Nasr-Esfahany, Malte Schwarzkopf, Siddhartha Sen, Mohammad Alizadeh
- **Έτος:** 2025
- **Δημοσίευση:** International Conference on Learning Representations (ICLR 2025)
- **Ελεγμένη έκδοση:** επίσημη camera-ready έκδοση στα ICLR Proceedings, 35 σελίδες
- **Canonical landing page:** `https://proceedings.iclr.cc/paper_files/paper/2025/hash/fb21dae9e8710a272c0a0ca848f71553-Abstract-Conference.html`

## Σκοπός και ερευνητικό ερώτημα
Η εργασία εξετάζει online reinforcement learning σε μη στάσιμα περιβάλλοντα όπου μια εξωγενής, χρονικά μεταβαλλόμενη και **παρατηρούμενη** μεταβλητή context επηρεάζει τη δυναμική του περιβάλλοντος. Το κεντρικό πρόβλημα είναι η catastrophic forgetting κατά τη συνεχή εκπαίδευση πάνω σε διαδοχικά context distributions. Προτείνει το Locally Constrained Policy Optimization (LCPO), που περιορίζει το πόσο μπορεί να αλλάξει η policy σε παλιότερα, εκτός τρέχουσας κατανομής contexts ενώ βελτιστοποιεί πάνω σε πρόσφατα δεδομένα.

## Μεθοδολογία
- Formalizes a context-driven non-stationary MDP in which the policy receives both state and current context; Sections 1–2 explicitly state that the context is observed and exogenous.
- Introduces LCPO as an on-policy constrained-optimization method. Past experience is kept in a bounded buffer, but stale experiences are used to constrain policy change rather than to perform ordinary off-policy policy optimization.
- Uses an OOD detector over context information to identify experience outside the current context distribution.
- Includes an illustrative discrete GridWorld with two observed context modes and an A2C example showing forgetting/relearning after context switches.
- Evaluates the method on MuJoCo, classic-control and computer-systems environments with synthetic and real context traces; comparisons include on-policy, off-policy, rehearsal/regularization and context-detection-related baselines, plus an idealized prescient offline reference.
- Reports sensitivity analyses for the OOD threshold and retained-buffer size.

## Κύρια ευρήματα με ακριβείς θέσεις
1. **Non-stationarity and forgetting are deployment-time learning problems, not merely static generalization problems.** The abstract and Introduction (pp. 1–2) frame online RL as continual interaction in a changing environment and identify catastrophic forgetting as a major failure mode when a function approximator is trained sequentially on changing data.
2. **The information assumption is explicit and strong.** Section 2, pp. 2–3, defines the current context as observed by the agent and includes it in the policy input. The paper separately discusses latent-context inference as a different problem in Related Work.
3. **The illustrative GridWorld shows retention/relearning behavior under recurring context.** Section 4.1, pp. 4–5, uses two observed GridWorld modes. The A2C policy learns one mode, drifts away from that behavior while trained only in the other mode, and must relearn when the first mode returns.
4. **LCPO separates retention constraints from current-context optimization.** Introduction and Section 4 describe anchoring behavior on old contexts while using fresh/current-context data for policy optimization, rather than treating stale experience as ordinary on-policy training data.
5. **The evaluation is broad within its own setting but does not establish a universal ranking.** Section 5 evaluates multiple continuous-control, classic-control and systems tasks across context traces and compares with several baselines and an idealized prescient agent.
6. **Resource and capacity limits remain material.** Section 5.3 and Section 6, p. 10, report sensitivity to buffer size and discuss finite network capacity, exploration under new contexts and buffer-management choices as limitations/open issues.

## Υποθέσεις και ορισμοί που πρέπει να διατηρηθούν
- The context process is exogenous and the current context is observed by the policy.
- The paper targets catastrophic forgetting after context change; latent-context detection/inference is explicitly a distinct problem.
- The non-stationarity may be smooth or abrupt and need not be a clean task sequence, but its mechanism is context-driven.
- The prescient baseline has access to the full context distribution before deployment and is an idealized reference, not a realistic online competitor.

## Περιορισμοί / threats to validity
- **Critical transfer boundary for this thesis:** the final thesis action-remapping disturbance is not an observed context variable supplied to the learner. Therefore LCPO does not provide direct evidence for performance under the thesis's hidden persistent remap and cannot be used to claim equivalence between the two settings.
- LCPO is a specific neural on-policy adaptation mechanism and is not evidence about the relative ranking of the thesis's Q-Learning, SARSA, DQN, PPO and Dyna-Q+ implementations.
- Its buffer/OOD machinery, training horizon and environments differ substantially from the frozen protocol-v2.1 design.
- Section 6 explicitly notes capacity, exploration and buffer-management limitations.
- The illustrative GridWorld is pedagogical evidence for forgetting behavior under observed context, not a benchmark equivalent to the thesis GridWorld.

## Σχέση με την υπάρχουσα βιβλιογραφία
Η πηγή συμπληρώνει τη γενικότερη continual-RL survey τεκμηρίωση του `SRC-F909CABDEB` με πρόσφατη peer-reviewed πρωτογενή evidence για online non-stationarity και catastrophic forgetting. Προσθέτει επίσης χρήσιμο contrast με πηγές όπου το context είναι latent ή όπου η αλλαγή ανιχνεύεται από transition/reward evidence. Δεν αντικαθιστά τις ήδη canonical πηγές για action failure, observation corruption, changepoint detection ή protocol-v2.1 recovery metrics.

## Χρήση στη διπλωματική
- **Ρόλος:** υποστηρικτική
- **Προτεινόμενα κεφάλαια:** Θεωρητικό υπόβαθρο; Σχετικές εργασίες; Συζήτηση; Περιορισμοί
- **Επιτρεπτές χρήσεις:** πρόσφατη τεκμηρίωση non-stationary online RL, catastrophic forgetting, stability–plasticity tension, recurring-context behavior, distinction between observed-context adaptation and latent/hidden change.
- **Μη επιτρεπτές χρήσεις:** claim ότι LCPO/PPO-like methods είναι ανθεκτικότερα στο protocol-v2.1, claim ότι observed context ισοδυναμεί με hidden action remapping, ή μεταφορά των reported performance values στη δική μας πειραματική κλίμακα.

## Απόφαση
**Επιλογή ως υποστηρικτική πηγή.** Η εργασία είναι peer-reviewed, άμεσα σχετική με το τελικό writing scope και προσθέτει σύγχρονη πρωτογενή evidence για continual online adaptation χωρίς να μεταβάλλει κανένα frozen scientific choice ή αποτέλεσμα της διπλωματικής.

Ρόλος: υποστηρικτική
Εξαγωγή: ναι

## Απαιτούμενα αποσπάσματα
Το `evidence/SRC-6F4F8BE003.md` κρατά citation-ready παραφράσεις για: (1) online non-stationarity/forgetting, (2) observed-context assumption, (3) recurring-context GridWorld behavior, (4) LCPO retention mechanism, και (5) capacity/exploration/buffer limitations.