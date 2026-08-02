---
κωδικός: SRC-91D94DB95B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Constrained Policy Optimization

## E1 — A CMDP separates task reward from auxiliary constraint costs
- **Type:** faithful paraphrase
- **Location:** Sections 3–4
- **Claim:** A constrained MDP augments the ordinary reward objective with auxiliary cost functions and limits that define the feasible policy set.
- **Status:** verified

### Faithful paraphrase
Achiam et al. formulate a CMDP by adding cost functions `C_i` and corresponding limits `d_i` to an MDP. The task objective remains maximizing expected discounted reward, but optimization is restricted to policies whose expected discounted auxiliary-cost returns remain below every specified limit.

### Thesis use
Keep task return and each safety/constraint cost as separate logged quantities.

### Citation
Achiam et al. (2017), Sections 3–4.

## E2 — CPO is designed to control constraint satisfaction throughout policy optimization
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section 5
- **Claim:** CPO derives local policy updates intended to improve reward while maintaining near-constraint satisfaction at each iteration rather than checking safety only after training ends.
- **Status:** verified

### Faithful paraphrase
The method approximates a constrained local policy-search step using surrogate reward and cost objectives together with a trust region. Its theoretical motivation is to bound both performance change and constraint violation between consecutive policies, allowing safety-oriented constraints to influence the entire learning trajectory.

### Thesis use
Measure violations during post-change adaptation, not only on the final recovered policy.

### Citation
Achiam et al. (2017), Abstract, Introduction, and Section 5.

## E3 — Reward recovery does not imply safety recovery
- **Type:** protocol implication grounded in the CMDP formulation
- **Location:** Section 4
- **Claim:** Reward return and auxiliary cost returns are distinct expectations, so restoring task performance does not establish that safety constraints have recovered.
- **Status:** verified

### Thesis use
After every shift, report task-return recovery time separately from cumulative safety cost, violation rate/count, and time until the declared safety condition is satisfied again.

### Citation
Achiam et al. (2017), Section 4.

## E4 — CMDP constraints are expectation-based
- **Type:** faithful paraphrase
- **Location:** Introduction; Section 4
- **Claim:** The constraints in CPO's CMDP formulation bound expectations of discounted auxiliary costs.
- **Status:** verified

### Context and limits
An expectation constraint is not automatically a pointwise, instantaneous, chance, or almost-sure guarantee. Rare trajectory-level violations can occur even if an expected-cost condition is met.

### Thesis use
Label the safety semantics explicitly and do not describe an expected-cost result as a stronger guarantee than it provides.

### Citation
Achiam et al. (2017), Introduction and Section 4.

## E5 — CPO is not an environmental change detector or continual-adaptation algorithm
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall method and experiments
- **Claim:** CPO addresses constrained policy optimization in a fixed CMDP; it does not define abrupt environment switches, changepoint alarms, context recall, or post-shift recovery metrics.
- **Status:** verified

### Thesis use
Use CPO as safe-RL background or a neural constrained baseline, not as evidence that constrained policy optimization itself provides resilience to a changing GridWorld.

### Citation
Achiam et al. (2017), overall scope.