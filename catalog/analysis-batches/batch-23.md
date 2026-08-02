# Επιστημονική ανάλυση — Παρτίδα 23

## Στόχος

Μαζική επεξεργασία δέκα πηγών με έμφαση σε:

1. θεμελιώδη robust MDPs,
2. constrained policy optimization,
3. Lyapunov/model-based safe learning,
4. reachability/returnability-aware safe exploration,
5. robust Monte-Carlo planning,
6. αποκλεισμό LLM-guided, cyber-specific, HRL-application και documentation-only records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-52E62452B8` | Robust Control of MDPs with Uncertain Transition Matrices | Κύρια θεωρητική |
| `SRC-91D94DB95B` | Constrained Policy Optimization | Υποστηρικτική |
| `SRC-8E22CBA55A` | Safe Model-based RL with Stability Guarantees | Υποστηρικτική |
| `SRC-6126015212` | Safe RL in Constrained MDPs / SNO-MDP | Υποστηρικτική |
| `SRC-BB5ECDA0CD` | Online Robust RL Through Monte-Carlo Planning | Υποστηρικτική |
| `SRC-80D1CDD66B` | Uncertainty-aware LLM guidance for RL | Απόρριψη: LLM-guidance scope |
| `SRC-60EF27E7AD` | Cyber resilience measurement | Απόρριψη: cyber-specific/redundant |
| `SRC-0B1E2F30F6` | Dynamic dungeon-crawler HRL | Απόρριψη: HRL application scope |
| `SRC-E59631E883` | Dynamic dungeon-crawler HRL hosted copy | Απόρριψη: duplicate |
| `SRC-30334BD5A0` | HighwayEnv documentation | Απόρριψη ως evidence· implementation only |

## Κλειδωμένες επιστημονικές αποφάσεις

### Robust MDP semantics

- Robustness απαιτεί explicit uncertainty set και nominal model.
- Stationary uncertainty, time-varying worst-case uncertainty και piecewise-stationary changepoints είναι διαφορετικά regimes.
- In-set robust performance αναφέρεται χωριστά από out-of-set structural change.
- Conservativeness gap αναφέρεται μαζί με worst-case improvement.

### Safety metrics

Reward και safety δεν συμπτύσσονται σε ένα scalar score. Μετά από change καταγράφονται χωριστά:

- task-return recovery,
- cumulative constraint cost,
- violation count/rate,
- time until constraints are satisfied again.

### Stability certificates

- Control-theoretic recovery προς equilibrium δεν ισοδυναμεί με relearning/adaptation.
- Pre-change safety certificate δεν θεωρείται valid μετά από dynamics change χωρίς revalidation.
- Καταγράφεται certificate-revalidation latency όπου υπάρχει certified controller.

### Safe reachability και returnability

- State-level safety δεν αρκεί εάν δεν υπάρχει safe route εισόδου/επιστροφής.
- Structural perturbations μπορούν να ακυρώσουν returnability χωρίς αλλαγή local hazard labels.
- Σε safety-aware scenarios καταγράφονται reachable-safe και returnable-safe sets.

### Planning fairness

Για MCTS/planning comparators καταγράφονται χωριστά:

- real environment interactions,
- simulator/model queries,
- rollouts ανά decision,
- search depth,
- wall-clock action latency.

Δεν επιτρέπεται unlimited planning budget απέναντι σε model-free baseline με μόνο online samples.

## Baseline implications

Ο core πίνακας παραμένει:

1. continual tabular Q-learning,
2. recency/decay update,
3. full reset,
4. detector-triggered reset,
5. context recall.

Προαιρετικά diagnostics/comparators:

- robust Bellman baseline,
- constrained safety accounting,
- reachability/returnability monitor,
- robust MCTS μόνο εάν οριστεί ίσο compute/query budget.

## Scope policy

- LLM guidance δεν εισάγεται χωρίς ξεχωριστό research question.
- Cyber-resilience literature δεν διπλομετράται όταν οι γενικές recovery metrics καλύπτονται ήδη από direct resilience sources.
- Dynamic game events δεν ισοδυναμούν με explicit environmental changepoints.
- Documentation pages παραμένουν implementation resources.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Generated layer

Το `thesis-package/SOURCE_COMMIT` παραμένει stale στο `9c3ccdc7801d3a12b29576c4230eba01fa982ad4`. Η canonical επιστημονική κατάσταση βρίσκεται στα `analyses/`, `evidence/` και `catalog/thesis-selection.csv`.