---
κωδικός: SRC-5E062C81BA
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Robust Reinforcement Learning

## E1 — Robust RL is formulated as an actor–disturber minimax problem
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 2–3
- **Claim:** The paper adapts `H-infinity` control ideas to reinforcement learning by introducing a disturbing agent that seeks adverse inputs while the control agent seeks the best response.
- **Status:** verified

### Faithful paraphrase
Morimoto and Doya reinterpret modeling error as an adverse disturbance and formulate policy learning as a differential game. The actor optimizes control while a disturber selects the most damaging input allowed by the robustness criterion, producing a minimax value objective rather than ordinary expected-return maximization.

### Thesis use
Use as a historical primary source for the static/worst-case robust-policy category.

### Citation
Morimoto and Doya (2000), Abstract and Sections 2–3.

## E2 — The robustness criterion defines the disturbance class
- **Type:** faithful paraphrase
- **Location:** Sections 2–3
- **Claim:** The `H-infinity`-inspired objective penalizes disturbance magnitude while requiring the controller to perform well against the corresponding worst disturbance.
- **Status:** verified

### Faithful paraphrase
The robust value function combines task/control performance with a term involving disturbance magnitude. The robustness parameter determines which disturbance-to-error gains the controller is designed to tolerate, so robustness is always relative to a specified disturbance model rather than an unrestricted notion of “any change.”

### Thesis use
State the perturbation/threat model explicitly for every robust baseline.

### Citation
Morimoto and Doya (2000), Sections 2–3.

## E3 — The nonlinear pendulum case study shows zero-update robustness to parameter changes
- **Type:** faithful paraphrase
- **Location:** Section 4.2; Figure 4
- **Claim:** A controller trained with the robust objective continued to swing up the pendulum after changing mass and friction, whereas the nominal comparator failed in that reported configuration.
- **Status:** verified

### Faithful paraphrase
Both controllers are trained under the nominal pendulum parameters. The paper then changes physical parameters including mass and friction and reports that the robust controller retains successful swing-up behavior while the standard model-based RL controller does not. The robustness is a property of the already learned controller; no separate change alarm or post-change retraining step is required for this comparison.

### Context and limits
This is a single continuous-control case study and should not be generalized to arbitrary structural changes or tabular environments.

### Thesis use
Measure frozen-policy post-change performance before enabling online updates, so immediate robustness is not attributed to adaptation.

### Citation
Morimoto and Doya (2000), Section 4.2 and Figure 4.

## E4 — Robustness can trade nominal peak performance for tolerance to mismatch
- **Type:** faithful paraphrase
- **Location:** Section 4.2
- **Claim:** In the nominal pendulum condition, the standard controller can complete the task with fewer swings, while the robust controller is designed for stronger tolerance to model variation.
- **Status:** verified

### Thesis use
Report clean/nominal return together with disturbed return and a conservativeness cost for robust agents.

### Citation
Morimoto and Doya (2000), Section 4.2.

## E5 — Worst-case disturbance training is not changepoint adaptation
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall formulation and experiments
- **Claim:** The method has no explicit changepoint detector, recurring-context memory, or repeated-regime recovery metric.
- **Status:** verified

### Thesis use
Keep `frozen_robustness` and `online_post_shift_adaptation` as separate evaluation phases and agent categories.

### Citation
Morimoto and Doya (2000), overall formulation.