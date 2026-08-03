---
κωδικός: SRC-B9911A6CFB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Safe Reinforcement Learning via Shielding under Partial Observability

## E1 — State estimation and shielding are distinct mechanisms

- **Type:** faithful paraphrase
- **Location:** Introduction; Section 3; Figure 1
- **Claim:** Under partial observability, a state estimator supplies belief-support information, while a shield separately restricts available actions to preserve a reach-avoid safety condition.
- **Status:** verified

### Faithful paraphrase

Carr et al. treat the state estimator and the shield as two different knowledge interfaces. The estimator tracks which POMDP states remain possible given the observation–action history. The shield uses that support together with a safety specification to allow only actions whose possible successor supports remain inside a winning region.

### Context and limits

Additional state information can improve learning, but the formal safety property comes from action restriction by the shield, not from state-estimation accuracy alone.

### Thesis use

Log context/state-estimation quality separately from shield intervention rate and safety outcomes.

### Citation

Carr et al. (2023), Introduction, Section 3, and Figure 1.

## E2 — The shield uses transition-support knowledge even when probabilities are unknown

- **Type:** faithful paraphrase
- **Location:** Sections 3.1–3.3
- **Claim:** Belief-support updates and shields can avoid requiring precise transition probabilities, but they rely on a graph-preserving partial model that identifies which transitions are possible.
- **Status:** verified

### Faithful paraphrase

The method computes belief supports from the POMDP graph and constructs shields using a partial model whose transition probabilities and rewards may be unknown. The partial model must nevertheless preserve transition support: a transition has positive probability in the approximation exactly when it is possible in the true model.

### Context and limits

This structural support information is a strong prior-information advantage relative to a model-free learner. If a structural environmental change creates or removes possible transitions, a shield computed from the old graph does not automatically retain its guarantee.

### Thesis use

Record `prior_transition_support` and, for structural shifts, whether and when the shield is revalidated or reconstructed.

### Citation

Carr et al. (2023), Sections 3.1–3.3.

## E3 — Reach-avoid shielding restricts actions rather than learning a recovery policy

- **Type:** faithful paraphrase
- **Location:** Section 3.2, Definition 2 and Theorems 2–3
- **Claim:** The shield is a permissive policy that filters actions so the agent remains in winning belief-support regions.
- **Status:** verified

### Faithful paraphrase

A shield maps the current belief support to a set of allowed actions. For avoid specifications, admissible policies that respect the shield remain safe; for reach-avoid specifications, the paper additionally requires fairness assumptions to ensure eventual reachability. The shield therefore constrains what the RL agent may do rather than replacing the agent with a learned recovery controller.

### Context and limits

A shield can be conservative and may reduce task performance. Reachability guarantees rely on the assumptions stated in the theorems.

### Thesis use

Treat shield interventions and any nominal-utility loss as explicit costs, distinct from learned recovery performance.

### Citation

Carr et al. (2023), Section 3.2, Definition 2 and Theorems 2–3.

## E4 — Structural change can invalidate a precomputed shield

- **Type:** protocol inference grounded in the partial-model guarantee
- **Location:** Section 3.3
- **Claim:** The safety guarantee transfers across models only while the relevant graph/support relation is preserved.
- **Status:** verified

### Faithful paraphrase

The paper's partial-model argument relies on graph-preserving approximations. Consequently, a deployment change that modifies which transitions are possible changes the premise under which the shield was computed. Continuing to apply the old shield without checking that premise would not be justified by the paper's guarantee.

### Thesis use

For any shielded structural-shift experiment, report shield validity, revalidation latency, and behavior while the model is potentially stale.

### Citation

Carr et al. (2023), Section 3.3.
