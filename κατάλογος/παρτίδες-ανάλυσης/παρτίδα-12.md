# Επιστημονική ανάλυση — Παρτίδα 12

## Στόχος

Κάλυψη των επόμενων κρίσιμων κενών του επίσημου scope:

1. online ανίχνευση abrupt changes και detector-triggered adaptation,
2. robustness σε observation corruption με σαφή διάκριση true και observed state,
3. τεκμηριωμένη απόρριψη αδύναμης/διπλότυπης GridWorld πηγής.

## Επαληθευμένες πηγές

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-7456165CEA` | Restarted Bayesian Online Change-point Detection for Non-Stationary Markov Decision Processes | Κύρια — change detection, restart adaptation και detector metrics |
| `SRC-620F17076C` | Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations | Υποστηρικτική — worst-case observation robustness και policy smoothness |
| `SRC-A62DDB9298` | Avoiding Catastrophic Forgetting in Safety Gridworld | Απόρριψη — μη peer-reviewed course report με ανεπαρκή empirical rigor |
| `SRC-D30B6E2BD6` | ίδια εργασία, δεύτερη repository εγγραφή | Απόρριψη — ακριβές διπλότυπο του `SRC-A62DDB9298` |

## Κύριες αποφάσεις που υποστηρίζονται

1. Change detection και post-change recovery θα μετρώνται χωριστά.
2. Κάθε detector-enabled run θα καταγράφει actual/detected change step, delay, false positives, missed changes και restart event.
3. Θα υπάρχει απλός detector-plus-reset baseline, αλλά δεν θα θεωρείται αυτομάτως καλύτερος από continual update ή context recall.
4. Observation scenarios θα διατηρούν χωριστά true state, observed state, perturbation mode, magnitude και frequency.
5. Worst-case adversarial observation robustness δεν θα παρουσιάζεται ως ισοδύναμη με ordinary stochastic sensor noise.
6. Robust pre-training χωρίς unknown change-point ή continued learning δεν θα χαρακτηρίζεται online resilience.
7. Το EWC+DQN course project δεν θα εξαχθεί ως citation-ready evidence και η duplicate εγγραφή δεν θα μετρηθεί ως δεύτερη πηγή.

## Νέες απαιτήσεις πρωτοκόλλου

### Detection

- `change_step`
- `detected_change_step`
- detection delay
- false-positive count/rate
- missed-change count/rate
- restart/update count
- recovery measured both from actual change and from detection event

### Observation corruption

- `true_state`
- `observed_state`
- perturbation mode
- magnitude/budget
- probability/frequency
- clean return
- disturbed return
- action-disagreement rate

## Ανοιχτά σημεία

- Detector threshold και minimum detectable severity θα κλειδώσουν μετά από pilot curves.
- Το R-BOCPD-UCRL2 θα παραμείνει implementation candidate μόνο αν το model-based state-action event stream και το CPU cost είναι διαχειρίσιμα.
- Για observation robustness θα προτιμηθεί πρώτα απλή tabular consistency/smoothing baseline πριν εξεταστεί deep SA-DQN.
