---
κωδικός: SRC-09DD20BA85
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Bounded Robustness in Reinforcement Learning via Lexicographic Objectives

## E1 — Observation corruption induces a disturbed effective policy

- **Type:** faithful paraphrase
- **Location:** Section 2, Definitions 1–2
- **Claim:** Observational disturbance should be modeled explicitly through an observation-noise kernel, because the agent acts on a corrupted measurement rather than on the true state.
- **Status:** verified

### Faithful paraphrase

The paper models an observationally disturbed MDP with a stochastic kernel `T(y|x)` that maps the true state to a possibly corrupted measurement. Since the policy chooses actions from that measurement, the deployed behavior is equivalent to a disturbed effective policy obtained by averaging the original policy through the noise kernel. Robustness regret is then defined as the utility difference between the nominal policy and this disturbed policy.

### Context and limits

This formulation specifically concerns state-observation corruption. Reward noise, delayed observations, or missing observations may require different operators or a different POMDP formulation.

### Thesis use

For observation-noise experiments, store the true state, the observed state, and the disturbance parameters separately, and evaluate clean and disturbed execution explicitly.

### Citation

Jarne Ornia et al. (2024), Section 2, Definitions 1–2.

## E2 — Robustness should be constrained by a nominal-utility tolerance

- **Type:** faithful paraphrase
- **Location:** Problem 1; lexicographic formulation; LRPG contribution
- **Claim:** The method optimizes robustness only among policies whose nominal utility remains within a specified tolerance of the primary objective.
- **Status:** verified

### Faithful paraphrase

The paper formulates the design problem as finding the most robust policy inside an `epsilon`-optimal set for the nominal return. The higher-priority objective is therefore nominal utility, and robustness is optimized subject to an explicit bound on how far the resulting policy may move from the nominal optimum. LRPG implements this lexicographic ordering while retaining the formal convergence structure of the underlying policy-gradient method under the paper's assumptions.

### Context and limits

The tolerance is a design choice, not a value supplied automatically by the theory. The formal guarantees also depend on the policy and convergence assumptions made in the analysis.

### Thesis use

Report nominal return and disturbed return together; do not label a method superior merely because it is robust if that robustness is purchased by a large clean-condition loss.

### Citation

Jarne Ornia et al. (2024), Problem 1 and the LRPG formulation.

## E3 — Robustness experiments should expose several disturbance regimes

- **Type:** faithful paraphrase
- **Location:** Experimental section; MiniGrid evaluation; discussion
- **Claim:** The empirical study evaluates clean and multiple disturbed conditions rather than treating robustness as a single scalar property.
- **Status:** verified

### Faithful paraphrase

The authors apply LRPG on top of PPO and A2C in MiniGrid tasks and evaluate policies under clean execution as well as several bounded stochastic and adversarial observation perturbations. The relative behavior of the methods varies across tasks, base algorithms, and robustness objectives, and the discussion notes that explicit model-based filtering may be preferable when a suitable disturbance model is available.

### Context and limits

The paper's representative-agent reporting does not fully characterize training uncertainty. Its quantitative algorithm ranking should not be transferred directly to a new GridWorld benchmark.

### Thesis use

Use multiple observation-noise regimes, but report all evaluation seeds with uncertainty intervals and retain per-scenario results rather than only a representative score.

### Citation

Jarne Ornia et al. (2024), experimental section and discussion.

## E4 — Robustness regret is not a recovery metric

- **Type:** scope inference grounded in the formulation
- **Location:** Sections 2–4
- **Claim:** The paper's robustness objective measures degradation under observational disturbance; it does not measure post-change relearning or time to recovery.
- **Status:** verified

### Faithful paraphrase

The method compares nominal policy utility with the utility of the noise-altered effective policy and searches for policies that limit this loss. It does not define a changepoint detector, online reset mechanism, context recall, or recovery trajectory after an environmental regime change.

### Thesis use

Keep observational robustness metrics separate from resilience metrics such as degradation depth, recovery time, and post-change adaptation success.

### Citation

Jarne Ornia et al. (2024), method scope, Sections 2–4.
