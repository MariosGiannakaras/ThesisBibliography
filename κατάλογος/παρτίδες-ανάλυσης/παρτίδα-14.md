# Επιστημονική ανάλυση — Παρτίδα 14

## Στόχος

Κάλυψη των θεωρητικών και πρακτικών αναγκών για resource-aware adaptation baselines:

1. computational δυσκολία ενημέρωσης μετά από local MDP changes,
2. recent-memory/sliding-window mechanisms για stale data,
3. adaptive multi-scale detection και restart χωρίς γνώση change frequency ή variation,
4. σαφής διάκριση θεωρητικών guarantees από εφαρμόσιμα tabular baselines.

## Επαληθευμένες πηγές

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-3C543330E4` | The Complexity of Non-Stationary Reinforcement Learning | Υπόβαθρο — worst-case update complexity, selective exploration και restart rationale |
| `SRC-4B456A9363` | Non-stationary Reinforcement Learning under General Function Approximation | Υποστηρικτική — sliding windows, local variation και dynamic-regret decomposition |
| `SRC-0A8E4489E8` | Non-stationary Reinforcement Learning without Prior Knowledge: An Optimal Black-box Approach | Υποστηρικτική — multi-scale stationarity tests και adaptive restart χωρίς prior `L`/`Δ` |

## Κύριες αποφάσεις που υποστηρίζονται

1. Η βασική σύγκριση adaptation mechanisms θα περιλαμβάνει χωριστά:
   - continual Q-learning χωρίς forgetting,
   - recency-weighted ή finite-window update,
   - periodic reset,
   - detector-triggered reset,
   - context recall μόνο σε previously seen regimes.
2. Το periodic reset με period ίσο ή άμεσα derived από το πραγματικό change interval θα σημειώνεται ως **oracle baseline**.
3. Window length, discount factor και reset period θα επιλέγονται σε development/pilot scenarios και όχι στο τελικό test sequence.
4. Detector event και reset event θα καταγράφονται χωριστά· detection χωρίς restart και restart χωρίς calibrated detection είναι διαφορετικές παρεμβάσεις.
5. Κάθε hard reset θα αναφέρει τι μηδενίζεται: Q-values, counts, model estimates, exploration schedule και context memory.
6. Το adaptation cost θα περιλαμβάνει environment interactions, update count, wall-clock/CPU όπου είναι διαθέσιμο και nominal-performance loss.
7. Τα MASTER, SW-OPEA και Lazy-QVI δεν αποτελούν υποχρεωτικές τελικές υλοποιήσεις· παρέχουν theoretical design constraints και upper-level mechanisms.
8. Θεωρητικό dynamic regret δεν θα παρουσιάζεται ως ισοδύναμο με empirical resilience score. Θα χρησιμοποιηθούν recovery deficit/AUC, time-to-recovery και post-change return με σαφή reference curve.

## Baseline matrix

| Baseline | Μνήμη | Trigger | Oracle πληροφορία | Κύριο ερώτημα |
|---|---|---|---|---|
| Continual Q-learning | όλη η ιστορία μέσω Q estimates | κανένα | όχι | αρκεί η συνεχιζόμενη ενημέρωση; |
| Recency Q-learning | discounted ή finite recent history | συνεχές | όχι, αν tuned μόνο σε development | μειώνει το stale-information bias; |
| Periodic reset | hard reset ανά σταθερό period | clock | πιθανώς ναι | πόσο ισχυρό είναι ένα schedule με γνωστή/εκτιμημένη συχνότητα; |
| Detector + reset | hard ή partial reset | change score | όχι | αξίζει το detection delay και τα false alarms; |
| Context recall | ξεχωριστά models/Q-tables | inferred/known context | εξαρτάται από context signal | υπερέχει η ανάκληση όταν επιστρέφει γνωστό regime; |

## Νέες απαιτήσεις πρωτοκόλλου

### Memory και forgetting

- `memory_mode`: full / finite-window / exponential / reset / context-library
- `effective_memory_length`
- recency/discount coefficient
- proportion ή proxy stale pre-change information
- state–action entries που μεταβλήθηκαν μετά το change

### Reset

- `reset_trigger`: periodic / detector / oracle / manual experimental control
- `reset_reason`
- `reset_step`
- `reset_scope`: full / Q-only / counts-only / exploration-only / model-only
- cumulative reset count
- false resets και missed necessary resets

### Computational adaptation cost

- environment steps από actual change έως recovery
- agent update count
- wall-clock ή CPU time με σταθερό hardware όταν είναι αξιόπιστα διαθέσιμο
- peak memory ή αριθμός stored contexts/models
- clean-regime cost του adaptation mechanism

### Tuning και leakage control

- παράμετροι forgetting/reset tuned μόνο σε development change schedules
- τελικό test με unseen onset, severity ή interval
- oracle baseline εμφανώς επισημασμένο στους πίνακες και στα plots
- ίδιο interaction budget και ίδιο seed set για όλους τους agents

## Ανοιχτά σημεία

- Η πρώτη υλοποίηση recency baseline θα είναι tabular και απλή: exponential recency ή controlled Q/count decay. Finite transition replay θα χρησιμοποιηθεί μόνο αν ο agent architecture το απαιτεί.
- Partial reset θα εξεταστεί μετά το full-reset pilot, ώστε να μην αυξηθεί πρόωρα το experimental matrix.
- Lightweight short-versus-long moving-average detector μπορεί να δοκιμαστεί ως approximation της multi-scale ιδέας, αλλά δεν θα ονομαστεί MASTER.
- Computational wall-clock comparisons θα αναφέρονται μόνο με deterministic instrumentation και ίδιο execution environment· διαφορετικά θα χρησιμοποιούνται update counts και interaction counts.
