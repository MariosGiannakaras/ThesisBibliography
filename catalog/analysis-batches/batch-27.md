# Επιστημονική ανάλυση — Παρτίδα 27

## Στόχος

Μαζική επεξεργασία δέκα πηγών γύρω από:

1. generalized safe exploration,
2. partial-observability shielding,
3. safe transfer και guide policies,
4. foundational runtime shielding,
5. recovery shielding με online learned dynamics,
6. αποκλεισμό adversarial/cyber, LLM-UQ, encyclopedic και broad active-learning records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-6F4B8E8DCE` | Safe Exploration in RL: Generalized Formulation and Algorithms | Υποστηρικτική |
| `SRC-B9911A6CFB` | Safe RL via Shielding under Partial Observability | Υποστηρικτική |
| `SRC-19858252B7` | Reinforcement Learning by Guided Safe Exploration | Υποστηρικτική |
| `SRC-8718299821` | Safe Reinforcement Learning via Shielding | Υποστηρικτική |
| `SRC-B1E5732635` | Recovery-based Shielding with GP Dynamics Models | Υποστηρικτική, recent preprint |
| `SRC-715B37A148` | Commercial adversarial ML article | Απόρριψη |
| `SRC-F491B6986C` | NIST Adversarial ML Taxonomy | Απόρριψη λόγω adversarial scope |
| `SRC-0BC87F6189` | Agentic AI — Wikipedia | Απόρριψη |
| `SRC-E242123630` | LLM Uncertainty Quantification Survey | Απόρριψη λόγω LLM-specific scope |
| `SRC-556A26CC39` | Active Learning for Autonomous Intelligent Agents | Απόρριψη λόγω broad redundancy |

## Κλειδωμένες επιστημονικές αποφάσεις

### Safety guarantee type

Κάθε safety experiment δηλώνει ρητά αν η απαίτηση είναι:

- expected cumulative cost,
- chance/probability constraint,
- instantaneous constraint,
- almost-sure/high-probability no-violation requirement.

Δεν συγκρίνονται safety methods σαν να λύνουν το ίδιο πρόβλημα όταν οι guarantee semantics διαφέρουν.

### Prior capabilities

Καταγράφονται χωριστά ως prior-information/capability advantages:

- emergency-stop/reset authority,
- precomputed backup controller,
- invariant safe set,
- transition-support graph/partial model,
- formal safety specification,
- pretrained safety guide,
- source/pretraining interaction budget.

Οι capabilities αυτές δεν αποδίδονται στην learned resilience του task policy.

### Shield intervention accounting

Για shielded agents καταγράφονται:

- proposed action,
- executed action,
- blocked/overridden-action fraction,
- preemptive ή post-posed shield mode,
- backup dwell time,
- intervention bursts,
- task utility loss λόγω intervention.

### Partial observability

State estimator και shield είναι διαφορετικά components. Καταγράφονται χωριστά:

- belief/context estimation quality,
- shield safety interventions,
- violations,
- information/model assumptions.

Transition-support knowledge αποτελεί prior-information advantage.

### Structural changes και certificate validity

Μετά από dynamics/structural changepoint:

- pre-change shield/model certificate δεν θεωρείται αυτόματα valid,
- μετράται `shield_revalidation_latency` / `safety_model_revalidation_latency`,
- δηλώνεται fallback behavior μέχρι την revalidation.

### Safe transfer metrics

Για pretrained guide/context/safety transfer αναφέρονται:

- safety jump-start,
- Δ time to safety,
- return jump-start,
- Δ time to optimum,
- guide-use fraction,
- source-training budget.

Απαιτείται source-target safety-dynamics mismatch ablation ώστε να εντοπίζεται negative transfer.

## Baseline implications

Ο core resilience πίνακας παραμένει αμετάβλητος. Τα safety mechanisms είναι overlays/comparators και όχι νέος ορισμός resilience.

Safety recovery προς safe region και task-policy recovery προς καλή απόδοση αναφέρονται χωριστά.

## Scope policy

- Adversarial/cyber threat models παραμένουν εκτός του βασικού non-adversarial experimental question.
- LLM token/semantic uncertainty δεν μεταφέρεται αυθαίρετα σε RL detector metrics.
- Wikipedia δεν χρησιμοποιείται ως canonical scientific source.
- Broad active-learning surveys δεν προστίθενται όταν οι χρήσιμες concepts καλύπτονται από direct RL evidence.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Generated layer

Το canonical scientific state βρίσκεται στα analysis/excerpt files και στο curated CSV. Derived/generated αρχεία αξιολογούνται χωριστά ως προς freshness.