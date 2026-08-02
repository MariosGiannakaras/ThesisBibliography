# Επιστημονική ανάλυση — Παρτίδα 24

## Στόχος

Επεξεργασία δέκα πηγών γύρω από:

1. POMDP/belief-state reasoning,
2. replay memory και stale experience,
3. classical robust RL,
4. neural confidence calibration,
5. καθαρισμό redundant neural-UQ/shield surveys και εκπαιδευτικών video records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-E8CAAF02BE` | Planning and Acting in Partially Observable Stochastic Domains | Κύρια θεωρητική |
| `SRC-A203ABEEFE` | Prioritized Experience Replay | Υποστηρικτική |
| `SRC-5E062C81BA` | Robust Reinforcement Learning | Υποστηρικτική ιστορική primary |
| `SRC-70AEC665B2` | On Calibration of Modern Neural Networks | Υποστηρικτική, neural arm only |
| `SRC-CE71F210EE` | SNGP / Distance Awareness | Απόρριψη: supervised-UQ redundancy |
| `SRC-8EE2492823` | Shields for Safe RL | Απόρριψη: survey redundancy |
| `SRC-1BF9FE1A37` | 5 simple AI Agents | Απόρριψη: commercial/tutorial scope |
| `SRC-93F2331D50` | 5 Types of AI Agents | Απόρριψη: introductory video taxonomy |
| `SRC-B790DF867B` | Monte Carlo/GridWorld lecture | Απόρριψη ως scientific evidence |
| `SRC-AE8219876F` | Same Monte Carlo lecture | Απόρριψη ως duplicate |

## Κλειδωμένες επιστημονικές αποφάσεις

### Partial observability

Διαχωρίζονται:

- noisy/corrupted observation του current state,
- uncertainty για latent context/regime,
- πραγματικό environmental changepoint.

Σε belief/context agent καταγράφονται posterior mass στο true state/context, belief entropy και κόστος information-gathering actions. Explicit model/prior access δηλώνεται ως prior-information advantage.

### Replay under non-stationarity

Μετά από changepoint το replay buffer μπορεί να περιέχει incompatible regimes. Καταγράφονται:

- buffer size,
- age distribution,
- pre-change/post-change fraction ανά minibatch,
- TD-error ανά regime,
- replay ratio,
- flush/reset policy.

Ablations: no replay, uniform replay, PER, oracle true-changepoint flush και detector-triggered flush. TD error δεν θεωρείται calibrated detector.

### Zero-update robustness

Robust policy training αξιολογείται πρώτα με frozen parameters αμέσως μετά το shift. Μόνο η μεταγενέστερη βελτίωση που οφείλεται σε updates ονομάζεται adaptation.

Αναφέρονται χωριστά:

- immediate frozen post-change return,
- post-update recovery curve,
- clean performance,
- conservativeness cost.

### Calibration

Για neural context/detection arm:

- confidence δεν ισοδυναμεί με probability χωρίς calibration,
- calibration split δεν περιέχει final test changepoints,
- ECE/MCE/reliability diagnostics είναι συμπληρωματικά,
- false-alarm rate και detection delay παραμένουν οι κύριες sequential detector metrics,
- temperature scaling εφαρμόζεται μόνο σε classifier-like outputs, όχι αυθαίρετα σε TD error.

## Scope policy

- Supervised OOD/UQ architectures δεν προστίθενται όταν οι concepts καλύπτονται ήδη και δεν υπάρχει neural implementation need.
- Shield surveys δεν διπλομετρώνται όταν runtime assurance/shield evidence είναι ήδη selected.
- General AI-agent videos δεν χρησιμοποιούνται ως επιστημονικός ορισμός agent.
- Lecture transcripts παραμένουν εκπαιδευτικά resources, όχι citation-ready evidence.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Baseline implications

Το core παραμένει:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Προαιρετικά diagnostics/ablations:

- belief/context inference quality,
- replay/no-replay/buffer-flush comparison,
- frozen robust-policy evaluation,
- calibrated neural detector μόνο εάν προστεθεί neural arm.

## Generated layer

Το generated package παραμένει derived/stale μέχρι πραγματική εκτέλεση του exporter. Η canonical κατάσταση είναι τα analysis/excerpt files και το curated CSV.