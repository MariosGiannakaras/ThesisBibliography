# Επιστημονική ανάλυση — Παρτίδα 18

## Στόχος

Μαζική επεξεργασία δέκα πηγών γύρω από:

1. drifting rewards/transitions και variation-budget adaptation,
2. environment/curriculum design για difficult-but-solvable scenarios,
3. safe-RL constraint formulations,
4. foundational deep baseline και procedural generalization protocols,
5. αποκλεισμό μη ισοδύναμων, adversarial, redundant ή εκτός-scope studies.

## Αποφάσεις πηγών

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-EBB14FC4CB` | Reinforcement Learning for Non-Stationary MDPs: The Blessing of (More) Optimism | Κύρια |
| `SRC-E05A14A571` | Emergent Complexity and Zero-shot Transfer via UED | Υποστηρικτική |
| `SRC-B72D65A330` | A Survey of Constraint Formulations in Safe RL | Υποστηρικτική |
| `SRC-CD5F67F3E6` | Proximal Policy Optimization Algorithms | Υπόβαθρο |
| `SRC-9DCA1F02C1` | Leveraging Procedural Generation to Benchmark RL | Κύρια |
| `SRC-B9111B3600` | GA agents in dynamic GridWorld | Απόρριψη: μη matched comparison |
| `SRC-77CEB5795F` | Safe non-stationary RL seminar transcript | Απόρριψη: duplicate transcript |
| `SRC-081F931CFA` | Mixed adversarial attacks / ASA-PPO | Απόρριψη: adversarial scope |
| `SRC-B58805342F` | Continuous-space realizable shields | Απόρριψη: redundant continuous-control scope |
| `SRC-41B78C510C` | Autonomous driving with DQN in CARLA | Απόρριψη: χωρίς controlled resilience protocol |

## Επιστημονικές αποφάσεις

### Drifting non-stationarity

- reward και transition variation καταγράφονται χωριστά,
- known variation budget χαρακτηρίζεται ως πρόσθετη πληροφορία,
- parameter-free model selection διαχωρίζεται από oracle tuning,
- dynamic regret συμπληρώνει αλλά δεν αντικαθιστά local recovery metrics,
- tight confidence intervals δεν θεωρούνται αυτομάτως καλύτερα όταν το induced MDP diameter γίνεται δυσμενές.

### Generalization και environment design

- procedural levels χρησιμοποιούν disjoint train/validation/test seeds,
- κάθε generated layout περνά solvability check,
- uniform randomization, minimax adversary και minimax-regret generation θεωρούνται διαφορετικές mechanisms,
- frozen zero-shot test προηγείται οποιουδήποτε online adaptation,
- fixed-level sequence ablation χρησιμοποιείται για εντοπισμό memorization.

### Safe-RL formulation

Κάθε safe baseline δηλώνει:

- expected cumulative cost,
- unsafe-state visit budget,
- chance constraint,
- per-step threshold,
- almost-sure ή άλλο guarantee type.

Expected cost, empirical violation probability, violation count και severity αναφέρονται χωριστά.

### PPO

Το PPO παραμένει standard deep baseline, όχι resilience mechanism. Clipping/KL update control δεν ερμηνεύεται ως environmental robustness, change detection ή uncertainty calibration.

## Quality-control αποφάσεις

- Comparisons με διαφορετικά start states, rewards ή environment implementations απορρίπτονται ως algorithm-ranking evidence.
- Adversarial attacker models δεν συγχέονται με stochastic/non-adversarial uncertainty.
- Redundant formal-shield sources δεν προστίθενται όταν δεν αλλάζουν το discrete GridWorld protocol.
- Application papers χωρίς controlled shift/recovery design δεν εξάγονται μόνο επειδή χρησιμοποιούν DQN ή safety terminology.

## Baseline implications

Το βασικό matrix παραμένει:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Deep PPO, PAIRED/UED και SWUCRL2-CW/BORL παραμένουν background ή feasibility references και όχι υποχρεωτικές υλοποιήσεις.

## Generated layer

Η παρτίδα ενημερώνει τα canonical αρχεία. Τα generated status/package files παραμένουν παλιά μέχρι πραγματική εκτέλεση του exporter.
