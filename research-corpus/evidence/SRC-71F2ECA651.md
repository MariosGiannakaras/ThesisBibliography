---
κωδικός: SRC-71F2ECA651
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
verification-source: "Official NeurIPS 2000 proceedings paper, 7-page primary PDF"
---

# Evidence — Robust Reinforcement Learning

## E1 — Model mismatch and input disturbances motivate robust control objectives

- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** A policy optimized for a nominal learned or simulated environment can behave poorly when the real system differs from that model or receives unmodeled disturbances.
- **Status:** verified

### Faithful paraphrase

Morimoto and Doya motivate robust reinforcement learning by noting that environmental models are widely used for simulation-based learning and online planning, but discrepancies between the model and the real environment can produce unwanted behavior. Their formulation therefore incorporates both modeling error and external input disturbance into the control objective.

### Thesis use

Use as historical motivation for static/worst-case robustness under model mismatch, not as evidence of online recovery.

### Citation

Morimoto and Doya (2000), Abstract and Introduction.

## E2 — The method is a minimax actor–disturber game

- **Type:** faithful paraphrase
- **Location:** Sections 2–3
- **Claim:** The robust objective is formulated as a differential game in which an actor chooses control inputs while a disturber chooses adverse disturbances.
- **Status:** verified

### Faithful paraphrase

Drawing on `H-infinity` control, the paper introduces a disturbing agent that seeks the most damaging allowable disturbance and a control agent that seeks the best response. The value function balances the control objective against the disturbance term, producing a minimax learning problem.

### Context and limits

The disturbance model and robustness trade-off are design choices. They define the uncertainty/threat model and are not neutral properties of the environment.

### Thesis use

Use this source to explain the historical actor–disturber origin of robust objectives and keep the disturbance model explicit.

### Citation

Morimoto and Doya (2000), Sections 2–3.

## E3 — The linear experiment validates the learning formulation against an analytic robust-control solution

- **Type:** faithful paraphrase
- **Location:** Section 4.1
- **Claim:** In the linear setting, the learned policy and value function converge toward the corresponding analytical `H-infinity` solution.
- **Status:** verified

### Faithful paraphrase

The authors use a linearized inverted-pendulum problem as a validation check. The learned value-function parameters and actor/disturber policies approach the solution obtained from the corresponding Riccati-equation robust-control formulation.

### Context and limits

Agreement in a linear benchmark validates the formulation under its assumptions; it does not establish general robustness for nonlinear, discrete, or modern deep-RL systems.

### Thesis use

Use as an example of validation against known analytical ground truth, not as a transferable performance ranking.

### Citation

Morimoto and Doya (2000), Section 4.1.

## E4 — The nonlinear case study reports robustness to pendulum parameter changes

- **Type:** faithful paraphrase
- **Location:** Section 4.2; Conclusion
- **Claim:** In the reported nonlinear pendulum task, the robust learned controller tolerated tested changes in pendulum weight and friction that the standard RL controller failed to handle successfully.
- **Status:** verified

### Faithful paraphrase

Both controllers learn the nominal swing-up task, but when the evaluation uses a heavier pendulum and greater friction, the robust controller still succeeds while the standard RL comparator fails to complete the swing-up in the reported test.

### Context and limits

This is one continuous-control case study and should not be generalized to arbitrary GridWorld changes or algorithm families.

### Thesis use

Historical empirical support that pre-emptive robustness to model mismatch can reduce performance loss under parameter shifts.

### Citation

Morimoto and Doya (2000), Section 4.2 and Conclusion.

## E5 — Worst-case robustness is not online resilience

- **Type:** scope synthesis grounded in the paper
- **Location:** Overall formulation and experiments
- **Claim:** The method learns against a prescribed disturbance formulation; it does not introduce an unknown changepoint, a detector, context recall, or a post-change relearning metric.
- **Status:** verified

### Thesis use

A robust policy may reduce the initial degradation caused by a shift, but that effect must remain distinct from detecting the shift and recovering through new learning.

### Citation

Morimoto and Doya (2000), overall formulation.

## Provenance note

The canonical source record was repaired on 2026-08-01 after an older Markdown conversion was found to contain an unrelated archival laboratory page. The scientific claims above were re-verified against the official NeurIPS 2000 proceedings paper, which is the authoritative source for this record.
