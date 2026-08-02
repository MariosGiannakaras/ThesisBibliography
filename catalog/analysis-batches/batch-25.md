# Επιστημονική ανάλυση — Παρτίδα 25

## Στόχος

Επεξεργασία δέκα πηγών γύρω από:

1. model-free robust MDPs,
2. RL-specific OOD/change detection,
3. recurring hidden regimes και context memory,
4. safety recovery/dead-end semantics,
5. καθαρισμό duplicate robust/safe-RL editions και application-only records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-9D663D35D0` | Robust Markov Decision Processes without Model Estimation | Υποστηρικτική |
| `SRC-19C2E91926` | Benchmark for Out-of-Distribution Detection in Deep Reinforcement Learning | Υποστηρικτική |
| `SRC-6609D86CD5` | Reinforcement Learning in Nonstationary Environments | Υποστηρικτική ιστορική |
| `SRC-73C145D523` | Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery | Υποστηρικτική |
| `SRC-F36BDC75F4` | Robust MDPs: A Place Where AI and Formal Methods Meet | Απόρριψη: thematic redundancy |
| `SRC-DD7CA18422` | ίδιο robust-MDP survey, arXiv edition | Απόρριψη: duplicate edition |
| `SRC-8E77CE2389` | Safe Model-based RL with Stability Guarantees | Απόρριψη: duplicate canonical paper |
| `SRC-F24D141550` | NIPS Spotlight transcript της ίδιας εργασίας | Απόρριψη: derivative transcript |
| `SRC-4F944A9FEB` | Safe reinforcement learning for real robots | Απόρριψη: application-specific MSc |
| `SRC-D2A07C1635` | ίδιο Aalto MSc record | Απόρριψη: duplicate |

## Κλειδωμένες επιστημονικές αποφάσεις

### Model-free robust comparator

Ένας robust-Q comparator δεν χρειάζεται κατ’ ανάγκη πλήρες transition tensor. Για κάθε robust method δηλώνονται:

- uncertainty/divergence formulation,
- robustness radius ή penalty,
- sample-access model,
- memory footprint,
- computation per update,
- in-set και out-of-set performance,
- clean conservativeness cost.

Generative-model queries δεν εξισώνονται με πραγματικά environment interactions.

### RL-specific OOD detection

Διαχωρίζονται ρητά:

- observation corruption,
- environment/dynamics parameter shift,
- latent-context uncertainty,
- πραγματικό sequential changepoint.

Static OOD detection αξιολογείται με AUROC/AUPR/F1 όπου χρειάζεται, αλλά online detector claims απαιτούν επιπλέον false-alarm rate, detection delay και missed-change rate.

### Recurring regimes

Η recency weighting είναι φυσικό memoryless adaptation baseline αλλά μπορεί να πληρώνει ξανά relearning cost όταν επανέρχεται προηγούμενο regime.

Σε repeated-context experiments καταγράφονται:

- occurrence index,
- first-visit έναντι revisit recovery time,
- context/model retrieval accuracy,
- wrong-context reuse,
- storage cost,
- no-memory comparator.

### Safety recovery

Διαχωρίζονται:

- task-performance recovery,
- safety recovery προς recoverable region.

Dead-end/irrecoverable states είναι διαφορετική έννοια από changepoints. Σε structural changes ελέγχεται αν η pre-change safety boundary/recovery critic παραμένει valid.

Νέα diagnostics:

- dead-end entries,
- interventions,
- intervention duration,
- false-positive interventions,
- safety violations,
- post-change recoverable-set change.

## Scope policy

- Νέα robust-MDP surveys δεν εξάγονται όταν δεν προσθέτουν νέο protocol πέρα από selected primary/foundational sources.
- ArXiv/publisher/landing-page editions της ίδιας εργασίας δεν διπλομετρώνται.
- Presentation transcripts δεν αντικαθιστούν το canonical paper.
- Application MSc work δεν επιλέγεται όταν το κύριο evidence αφορά sim-to-real/domain randomization και όχι controlled post-change resilience.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Baseline implications

Το core παραμένει:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Προαιρετικά comparators/diagnostics:

- model-free robust Q,
- RL-specific OOD detector arm,
- safety recovery/dead-end monitor.

## Generated layer

Το generated package παραμένει derived και δεν θεωρείται source of truth μέχρι να εκτελεστεί επιτυχώς ο exporter.