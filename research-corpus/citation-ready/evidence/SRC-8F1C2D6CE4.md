---
κωδικός: SRC-8F1C2D6CE4
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty

## E1 — Representation capacity participates in a bias–variance trade-off under model uncertainty
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1 and 3
- **Claim:** The paper argues that policy/model rank can affect robustness under epistemic dynamics uncertainty because insufficient rank increases approximation bias while excessive rank can increase variance and sensitivity.
- **Status:** verified

### Faithful paraphrase
Li et al. study robust policy learning through representational capacity rather than only through an adversarial Bellman backup. Their theoretical motivation is that the effective rank of the policy/value representation should be matched to the task's intrinsic complexity: overly restrictive representations can underfit, while unnecessary capacity can increase variance under uncertain dynamics.

### Thesis use
If neural agents are included, hold architecture capacity constant across algorithm comparisons or report it as an explicit experimental factor.

### Citation
Li et al. (2025), Abstract and Sections 1 and 3.

## E2 — AdaRL adapts rank through bi-level optimization instead of solving nested worst-case dynamics at every update
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 4
- **Claim:** The lower-level optimization trains the policy under a fixed-rank constraint while the upper level adjusts rank to balance expressiveness and robustness.
- **Status:** verified

### Faithful paraphrase
AdaRL alternates ordinary policy optimization constrained to a selected low-rank manifold with a separate update that modifies the representational rank. Dynamics are sampled from a Wasserstein neighborhood of a centroid model, but the method is explicitly proposed as an alternative to repeatedly solving a nested min–max transition optimization.

### Context and limits
This is a robustness/representation mechanism, not a temporal change detector.

### Thesis use
Use it only as neural feasibility/background unless the final scope explicitly includes adaptive-capacity agents.

### Citation
Li et al. (2025), Abstract and Section 4.

## E3 — Neural capacity is a confound unless it is exposed in the experiment record
- **Type:** protocol implication grounded in the method
- **Location:** Sections 3–5
- **Claim:** Because AdaRL explicitly changes effective rank, part of any performance difference can come from representational capacity rather than only from the high-level RL update rule.
- **Status:** verified

### Thesis use
For neural comparisons, report parameter count, effective rank, rank trajectory, optimizer cost, and nominal-performance impact. Do not hide architecture differences under an algorithm label.

### Citation
Li et al. (2025), Sections 3–5.

## E4 — The reported evidence is from continuous-control model-uncertainty experiments
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 5
- **Claim:** AdaRL is evaluated on MuJoCo continuous-control benchmarks against fixed-rank and robust-RL baselines.
- **Status:** verified

### Context and limits
The experiments do not establish rapid recovery in a tabular GridWorld after repeated unknown changepoints. Model-uncertainty robustness and continual relearning remain different settings.

### Thesis use
Do not transfer the empirical ranking directly into the thesis baseline selection.

### Citation
Li et al. (2025), Abstract and Section 5.

## E5 — Adaptive capacity is not environmental adaptation by itself
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall formulation
- **Claim:** Adjusting representational rank can improve generalization under uncertain dynamics but does not itself infer a regime boundary, recall a previous context, or define post-shift recovery time.
- **Status:** verified

### Thesis use
Keep `adaptive_representation_capacity` separate from `environment_change_detection` and `policy_recovery` in the agent taxonomy.

### Citation
Li et al. (2025), overall formulation.