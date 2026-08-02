---
κωδικός: SRC-73DA396BA9
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Online MDP with Transition Prototypes: A Robust Adaptive Approach

## E1 — Prior structural knowledge can be represented as a finite transition-prototype set
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1; Section 3.1
- **Claim:** The method assumes that the unknown true transition kernel is one member of a finite set of known transition prototypes.
- **Status:** verified

### Faithful paraphrase
Sun, Qi, and Shen study an online MDP in which the learner does not know which transition model is active but is given a finite collection of plausible transition kernels. These prototypes can come from prior data or other structural knowledge. The learning problem is therefore to act well while identifying which known prototype is the true nominal model.

### Context and limits
This is stronger prior information than ordinary model-free RL. The theoretical setup assumes that the true transition kernel belongs to the supplied prototype set.

### Thesis use
If a finite regime library is evaluated, count the library itself as prior information and compare it with a no-library baseline.

### Citation
Sun, Qi, and Shen (2024), Abstract and Sections 1 and 3.1.

## E2 — Robust control protects early performance while model identity is unresolved
- **Type:** faithful paraphrase
- **Location:** Sections 1 and 4
- **Claim:** RPO-AAS computes a robust policy over the currently plausible prototypes rather than immediately committing to a single model when data are scarce.
- **Status:** verified

### Faithful paraphrase
The proposed algorithm maintains an adaptively updated ambiguity set over transition prototypes. While several prototypes remain plausible, it optimizes a robust policy over that active set. This design is intended to improve worst-case performance during the early online-learning phase, when selecting one prototype from limited data can be unreliable.

### Thesis use
Compare immediate hard model selection against a robust candidate-set fallback under deliberately ambiguous early trajectories.

### Citation
Sun, Qi, and Shen (2024), Sections 1 and 4.

## E3 — The ambiguity set shrinks as transition evidence accumulates
- **Type:** faithful paraphrase
- **Location:** Sections 1, 4, and 5
- **Claim:** Streaming transition observations are used to eliminate incompatible prototypes, causing the active ambiguity set to contract over time.
- **Status:** verified

### Faithful paraphrase
Unlike robust-MDP formulations with a fixed uncertainty-set size, RPO-AAS uses empirical transition data to update which prototypes remain statistically plausible. Its robustness is therefore adaptive: the policy hedges across a larger set when evidence is weak and across a smaller set as the learner gains information about the true transition dynamics.

### Thesis use
Log candidate-set size, eliminated models, and time to unique identification as diagnostics rather than treating context inference as an invisible internal state.

### Citation
Sun, Qi, and Shen (2024), Sections 1, 4, and 5.

## E4 — Sufficient evidence permits a switch from robust fallback to model-specific control
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 5.2; Section 6
- **Claim:** The method includes an early-stopping or identification mechanism and also analyzes a non-robust alternative that selects the candidate closest to empirical transitions.
- **Status:** verified

### Faithful paraphrase
When the accumulated data provide sufficient evidence to distinguish the true transition prototype, the robust-learning phase can terminate and control can specialize to the identified model. The paper separately studies a non-robust prototype-selection method, making explicit that robust hedging and hard candidate selection are different response rules.

### Thesis use
Use the architecture pattern `robust fallback while ambiguous → regime-specific policy after sufficient evidence`, and compare it with immediate hard selection.

### Citation
Sun, Qi, and Shen (2024), Section 5.2 and Section 6.

## E5 — The theorem does not cover an out-of-library regime
- **Type:** assumption boundary grounded in the formulation
- **Location:** Section 3.1 and theoretical results
- **Claim:** The guarantees rely on the true transition kernel being among the known prototypes.
- **Status:** verified

### Faithful paraphrase
The finite-prototype formulation defines one of the supplied kernels as the true underlying transition model. Regret, identification, and stopping guarantees are derived under that premise. If the deployed dynamics are structurally different from every stored prototype, those guarantees no longer describe the problem.

### Thesis use
Include an explicit `true_regime_absent_from_library` test and never report the in-library theorem as protection against that condition.

### Citation
Sun, Qi, and Shen (2024), Section 3.1 and theoretical sections.

## E6 — Adaptive prototype robustness is not a generic changepoint detector
- **Type:** thesis-scope synthesis
- **Location:** Overall problem formulation
- **Claim:** The paper learns which fixed prototype is the true transition model in an online MDP; it does not primarily formulate repeated temporal switching among regimes.
- **Status:** verified

### Thesis use
Use it as evidence for model-library inference and robust early control, while validating repeated-change detection/recall in a separate protocol.

### Citation
Sun, Qi, and Shen (2024), overall formulation.