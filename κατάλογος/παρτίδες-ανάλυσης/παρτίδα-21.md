# Επιστημονική ανάλυση — Παρτίδα 21

## Στόχος

Μαζική επεξεργασία δέκα πηγών γύρω από:

1. robust constrained policy optimization,
2. practical uncertainty-set design,
3. nominal–pessimistic double-agent architectures,
4. state-entropy coverage για structured perturbations,
5. deduplication και διαχωρισμό scientific evidence από software repositories.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-2C9FFED27E` | Efficient Policy Optimization in Robust Constrained MDPs | Υποστηρικτική, canonical NeurIPS 2025 |
| `SRC-7313A97A30` | On Practical Robust Reinforcement Learning | Υποστηρικτική |
| `SRC-C90D59EC8C` | State Entropy Regularization for Robust RL | Υποστηρικτική |
| `SRC-54E00B5A43` | RCMDP arXiv/HTML edition | Απόρριψη ως duplicate του `SRC-2C9FFED27E` |
| `SRC-3EF7E5F425` | Feasible Adversarial Robust RL | Απόρριψη λόγω adversarial PSRO scope και redundancy |
| `SRC-A784C81711` | FARR hosted copy | Απόρριψη ως duplicate του `SRC-3EF7E5F425` |
| `SRC-0A4446E662` | Generalized OOD Detection survey | Απόρριψη λόγω supervised scope και redundancy |
| `SRC-A566FE1E98` | rliable GitHub repository | Implementation-only resource |
| `SRC-1D5EA31EEF` | AI Safety Gridworlds GitHub repository | Implementation/archive resource |
| `SRC-642F9F639D` | MiniGrid GitHub repository | Implementation dependency |

## Κλειδωμένες επιστημονικές αποφάσεις

### Robust safety feasibility

- Nominal constraint satisfaction δεν θεωρείται robust feasibility.
- Worst-case task model και worst-case constraint model μπορεί να διαφέρουν.
- Utility, κάθε constraint cost, violation margin και feasibility rate αναφέρονται χωριστά.
- Strong-duality ή common-Lagrangian assumptions δεν θεωρούνται δεδομένες σε RCMDP.
- Wall-clock και iteration complexity αποτελούν μέρος της σύγκρισης.

### Practical uncertainty sets

- Η ακτίνα και το σχήμα του uncertainty set είναι explicit experimental parameters.
- Καταγράφεται ποια models αποκλείονται ως implausible και με ποιο κριτήριο.
- Πολύ ευρύ set αξιολογείται για conservativeness· πολύ στενό set για coverage failure.
- Σε nominal–pessimistic architecture καταγράφεται η απόκλιση των δύο estimates και το πρόσθετο compute.

### State entropy

- State-visitation entropy και policy/action entropy είναι διαφορετικές quantities.
- Σε tabular GridWorld η state entropy υπολογίζεται από visitation counts.
- Structured/spatial perturbations διαχωρίζονται από ανεξάρτητο stochastic noise.
- Newly relevant state coverage μετά από change καταγράφεται χωριστά.
- Exploration coverage αναφέρεται μαζί με hazard/violation cost.

### Evidence versus software

- Το scientific claim παραπέμπει στο paper, όχι στο repository README.
- Software dependencies καταγράφονται με release ή commit pin.
- Archived repositories διατηρούνται για reproducibility αλλά δεν μετρούν ως ανεξάρτητες πηγές.
- Hosted copies και arXiv/camera-ready εκδόσεις της ίδιας εργασίας μετρούν μία φορά.

## Baseline implications

Το βασικό matrix παραμένει αμετάβλητο:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Προστίθενται μόνο ως feasibility/ablation candidates:

- nominal versus pessimistic Q estimates,
- practical versus broad uncertainty set,
- state-count/state-entropy exploration bonus,
- robust constraint evaluation χωρίς πλήρη RNPG implementation.

## Scope boundaries

- Robust constrained optimization δεν είναι changepoint adaptation.
- State entropy δεν είναι detector και δεν εγγυάται safe exploration.
- Adversarial environment generation δεν συγχέεται με non-adversarial deployment change.
- Supervised OOD taxonomy δεν χρησιμοποιείται ως RL detector evidence χωρίς trajectory-level validation.

## Generated layer

Η παρτίδα ενημερώνει τα canonical analysis, excerpt και curated-selection αρχεία. Το generated package παραμένει ξεχωριστό derived layer μέχρι πραγματική εκτέλεση του exporter.