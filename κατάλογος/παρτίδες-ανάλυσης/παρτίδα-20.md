# Επιστημονική ανάλυση — Παρτίδα 20

## Στόχος

Μαζική επεξεργασία δέκα πηγών με άξονες:

1. online identification από transition-prototype library,
2. incremental model-free robust Q-learning,
3. reproducible MiniGrid environment design,
4. support-shift limitations της interactive robust μάθησης,
5. learned recovery-controller conflicts,
6. αποκλεισμό application-specific, introductory ή documentation-only records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-73DA396BA9` | Online MDP with Transition Prototypes | Κύρια |
| `SRC-3C0F7CC819` | Online Robust RL with Model Uncertainty | Υποστηρικτική |
| `SRC-A4DC00B75B` | MiniGrid & MiniWorld | Κύρια environment source |
| `SRC-4D2B7DDC38` | Distributionally Robust RL with Interactive Data | Υποστηρικτική |
| `SRC-3BF9404CC3` | Learning to Recover for Safe RL | Υποστηρικτική |
| `SRC-1602A6C071` | Inventory replenishment RL thesis | Απόρριψη: application-specific |
| `SRC-1DBBBC39D2` | CARLA DRL MSc metadata | Απόρριψη: metadata/application scope |
| `SRC-576D988D14` | Εισαγωγή στην Ενισχυτική Μάθηση | Απόρριψη: redundant introductory source |
| `SRC-04D061C2E0` | Safety unit tests MSc thesis | Απόρριψη: redundant/lower evidence tier |
| `SRC-3275F3E7B0` | FrozenLake documentation | Απόρριψη ως evidence· implementation only |

## Κλειδωμένες επιστημονικές αποφάσεις

### Prototype/model libraries

- Candidate-set robust policy και hard nearest-model selection είναι διαφορετικά mechanisms.
- Καταγράφονται active-library size, elimination events και χρόνος έως specialization.
- False elimination του αληθινού regime αποτελεί ξεχωριστό failure mode.
- Out-of-library regime είναι υποχρεωτικό stress test.

### Robust Q-learning

- Robust incremental update δεν θεωρείται change detector.
- Η uncertainty-set ακτίνα δηλώνεται ως oracle, tuned ή data-derived.
- Clean utility, disturbed utility και conservativeness gap αναφέρονται μαζί.

### Environment implementation

- Το MiniGrid χρησιμοποιείται ως modular substrate, όχι ως έτοιμο resilience benchmark.
- Map seed και agent seed αποθηκεύονται χωριστά.
- Κάθε structural perturbation περνά solvability validation.
- Environment version, serialized layout και wrappers αποτελούν μέρος του experiment artifact.

### Support shift

- In-support parameter changes και out-of-support structural changes αξιολογούνται χωριστά.
- Περισσότερη αλληλεπίδραση σε fixed training MDP δεν θεωρείται evidence για unreachable deployment states.
- Προστίθεται coverage-overlap diagnostic όπου είναι εφικτό.

### Recovery-controller interference

Για safety fallback καταγράφονται:

- proposed task action,
- executed action,
- task–recovery disagreement,
- intervention burst duration,
- stuck/oscillation rate,
- controller-induced delay,
- nominal utility loss.

Η επιστροφή σε safe state δεν συγχέεται με policy recovery μετά από environmental change.

## Baseline implications

Το βασικό matrix παραμένει:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Προαιρετικά feasibility comparators:

- robust active prototype set,
- incremental robust Q-learning,
- local recovery/fallback controller.

## Source-quality policy

- Εφαρμοστικές διατριβές χωρίς controlled shift protocol δεν χρησιμοποιούνται για algorithm ranking.
- Introductory theses δεν προστίθενται όταν υπάρχουν canonical textbooks.
- Documentation pages παραμένουν implementation resources, όχι scientific evidence.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Generated layer

Η παρτίδα ενημερώνει μόνο canonical analyses, excerpts και curated selection. Το generated package παραμένει ξεχωριστό derived artifact μέχρι πραγματική εκτέλεση του exporter.