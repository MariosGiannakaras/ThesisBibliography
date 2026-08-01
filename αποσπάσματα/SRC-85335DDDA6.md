---
κωδικός: SRC-85335DDDA6
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Empirical Study on Robustness and Resilience in Cooperative Multi-Agent Reinforcement Learning

## E1 — Robustness and resilience are evaluated as different properties
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1 and 3
- **Claim:** The paper treats robustness as maintaining functionality while uncertainty is active and resilience as recovery after a disruption has moved the system to a perturbed state.
- **Status:** verified

### Faithful paraphrase
Li et al. explicitly separate two deployment properties that are often conflated in MARL. Robustness measures performance while observation, action, or environmental uncertainty is present. Their resilience formulation instead evaluates performance after a perturbation has produced a disturbed state and the continuing uncertainty is removed, thereby focusing on the ability to recover from the shock.

### Thesis use
Keep persistent-noise robustness, transient-shock recovery, and online relearning as separate evaluation protocols.

### Citation
Li et al. (2025), Abstract and Sections 1 and 3.

## E2 — Performance under one uncertainty modality does not predict another
- **Type:** faithful paraphrase
- **Location:** Abstract; main findings
- **Claim:** Robustness and resilience vary by uncertainty type and agent scope, and a policy that performs well under one perturbation can fail under another.
- **Status:** verified

### Faithful paraphrase
The large-scale study finds that rankings change across observation, action, and environment uncertainties and across perturbations applied to one agent versus the whole group. The authors therefore argue against using performance under a single uncertainty mode as evidence of general trustworthy behavior.

### Thesis use
Maintain separate scorecards for action failure, observation corruption, transition/environment change, and structural shift.

### Citation
Li et al. (2025), Abstract and main findings.

## E3 — Perturbation severity changes the relationship between nominal performance and robustness/resilience
- **Type:** faithful paraphrase
- **Location:** Abstract; main findings
- **Claim:** Better cooperative performance is more strongly associated with robustness/resilience under mild uncertainty than under severe perturbations.
- **Status:** verified

### Thesis use
Use severity sweeps and performance-versus-severity curves rather than evaluating one arbitrarily chosen perturbation level.

### Citation
Li et al. (2025), Abstract and main findings.

## E4 — Hyperparameter choices can rival or exceed the effect of the algorithm label
- **Type:** faithful paraphrase
- **Location:** Introduction; main findings; Table 1
- **Claim:** In many studied MARL tasks, implementation and hyperparameter choices materially change cooperation, robustness, and resilience and can explain more variation than the selected MARL backbone.
- **Status:** verified

### Faithful paraphrase
The study sweeps a broad set of architecture and optimization choices and reports that several conventional settings can either improve or degrade uncertainty performance. Its analysis highlights that algorithm comparisons can be misleading when tuning budgets, search spaces, or implementation details differ.

### Context and limits
The specific MARL hyperparameter recommendations are not direct prescriptions for tabular single-agent RL.

### Thesis use
Use matched tuning budgets, declared search spaces, and sensitivity analysis for the small number of influential hyperparameters in each thesis baseline.

### Citation
Li et al. (2025), Introduction, main findings, and Table 1.

## E5 — The collaboration/algorithm findings are MARL-specific
- **Type:** scope boundary grounded in the paper
- **Location:** Overall experiments
- **Claim:** The empirical rankings concern cooperative multi-agent systems and should not be transferred to a single-agent GridWorld.
- **Status:** verified

### Thesis use
Use this source for evaluation methodology and robustness/resilience separation only; do not cite its MARL algorithm ordering as evidence for the thesis's single-agent agents.

### Citation
Li et al. (2025), overall experiments.