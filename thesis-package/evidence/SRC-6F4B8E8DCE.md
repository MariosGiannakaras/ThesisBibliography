---
κωδικός: SRC-6F4B8E8DCE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms

## E1 — Safety formulation and guarantee type are part of the problem definition

- **Type:** faithful paraphrase
- **Location:** Sections 2–3, Problems 1–4 and Theorem 3.1
- **Claim:** Cumulative, state-based, and instantaneous safety constraints encode different requirements, and the paper's generalized formulation covers specific almost-sure formulations rather than every risk constraint.
- **Status:** verified

### Faithful paraphrase

Wachi et al. distinguish expected cumulative-cost constraints from stricter formulations that require constraint satisfaction almost surely or with high probability during learning. They describe cumulative, unsafe-state, and instantaneous constraints and show how several of these stricter formulations can be transformed into their generalized safe-exploration problem through suitable safety-cost and threshold definitions.

### Context and limits

The paper explicitly states that conventional expected cumulative-cost CMDPs and general CVaR or chance-constrained formulations are not all equivalent to the GSE problem.

### Thesis use

Record the exact safety-constraint semantics and guarantee type before comparing safe agents.

### Citation

Wachi et al. (2023), Sections 2–3 and Theorem 3.1.

## E2 — MASE relies on an externally available emergency-stop capability

- **Type:** faithful paraphrase
- **Location:** Assumptions 3.2–3.4; Section 4
- **Claim:** If no action can be certified as safe with sufficient confidence, MASE executes an emergency-stop action that returns the system to the initial state.
- **Status:** verified

### Faithful paraphrase

The method constructs a set of actions whose estimated safety cost plus an uncertainty bound lies below the current threshold. When that certified-safe set is empty, the algorithm invokes a special emergency-stop action. The analysis assumes that this action safely resets the environment and that a suitable uncertainty quantifier covers the unknown true safety cost with high probability.

### Context and limits

Emergency stopping is a prior system capability, not a behavior learned by the RL policy. The paper notes that such interventions can be expensive and points to learned reset policies as a different future direction.

### Thesis use

Report intervention count, reset count, and task-utility cost separately and never credit emergency-stop availability as learned recovery.

### Citation

Wachi et al. (2023), Assumptions 3.2–3.4 and Section 4.

## E3 — High-probability safety depends on uncertainty-quantifier validity

- **Type:** faithful paraphrase
- **Location:** Assumption 3.4; Section 4
- **Claim:** MASE's action certification is only as reliable as the confidence bound used for the unknown safety-cost function.
- **Status:** verified

### Faithful paraphrase

The algorithm assumes an uncertainty quantifier `Gamma(s,a)` such that the true safety cost lies within the estimated mean plus or minus that bound for all state–action pairs with probability at least `1-delta`. Actions are certified safe through the corresponding upper confidence bound.

### Context and limits

A learned or approximate uncertainty model must therefore be validated; calling a method “safe” without checking the bound assumptions would overstate the guarantee.

### Thesis use

If a safety critic or uncertainty model is included, report its calibration/coverage assumptions separately from empirical violation counts.

### Citation

Wachi et al. (2023), Assumption 3.4 and Section 4.

## E4 — Safe exploration and environmental-change recovery remain separate capabilities

- **Type:** scope inference grounded in the formulation
- **Location:** Sections 2–5
- **Claim:** MASE constrains learning actions to avoid safety violations; it does not identify unknown environmental regime changes or measure post-change recovery.
- **Status:** verified

### Faithful paraphrase

The contribution wraps an unconstrained RL learner with action certification, safety penalties, and emergency stopping. Its objective is safe exploration within the stated CMDP/GSE formulation, not changepoint detection, context recall, or continued-learning resilience after an exogenous regime shift.

### Thesis use

Keep safety-intervention metrics separate from degradation, detection-delay, and recovery-time metrics.

### Citation

Wachi et al. (2023), overall method scope.
