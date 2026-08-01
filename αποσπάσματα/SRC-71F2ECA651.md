---
κωδικός: SRC-71F2ECA651
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
verification-source: "NeurIPS 2000 primary paper; local source record requires reprocessing"
---

# Evidence — Robust Reinforcement Learning

## E1 — Model mismatch and input disturbances motivate robust control objectives
- **Type:** faithful paraphrase
- **Location:** Abstract; introduction
- **Claim:** A policy optimized for a nominal learned or simulated environment can behave poorly when the real system differs from that model or receives unmodeled disturbances.
- **Status:** verified

### Faithful paraphrase
Morimoto and Doya motivate robust reinforcement learning by noting that environmental models are widely used for simulation-based learning and online planning, but discrepancies between the model and the real environment can produce unwanted behavior. Their formulation therefore incorporates both modeling error and external input disturbance into the control objective.

### Thesis use
Use as historical motivation for static/worst-case robustness under model mismatch, not as evidence of online recovery.

### Citation
Morimoto and Doya (2000), Abstract and introduction.

## E2 — The method is a minimax actor–disturber game
- **Type:** faithful paraphrase
- **Location:** problem formulation
- **Claim:** The robust objective is formulated as a differential game in which an actor chooses control inputs while a disturber chooses adverse disturbances.
- **Status:** verified

### Faithful paraphrase
Drawing on `H-infinity` control, the paper introduces a disturbing agent that seeks the most damaging allowable disturbance and a control agent that seeks the best response. The value function balances output/control objectives against a penalty on disturbance magnitude, producing a minimax learning problem.

### Context and limits
The disturbance norm and robustness trade-off are design choices. They define the threat/uncertainty model and are not neutral properties of the environment.

### Thesis use
Use this source to explain the historical actor–adversary origin of robust objectives and keep the attacker/disturber model explicit.

### Citation
Morimoto and Doya (2000), formulation sections.

## E3 — The linear experiment validates the learning formulation against an analytic robust-control solution
- **Type:** faithful paraphrase
- **Location:** linear inverted-pendulum experiment
- **Claim:** In the linear setting, the learned policy and value function agree with the corresponding analytical `H-infinity` solution.
- **Status:** verified

### Faithful paraphrase
The authors use a linear inverted-pendulum problem as a correctness check for the online learning formulation. In this case, the policy and value function obtained by learning coincide with the analytic solution supplied by linear robust-control theory.

### Context and limits
Agreement in a linear benchmark validates that formulation under its assumptions; it does not establish general robustness for nonlinear, discrete, or modern deep-RL systems.

### Thesis use
Use as an example of validation against known ground truth, not as a transferable performance claim.

### Citation
Morimoto and Doya (2000), linear experiment.

## E4 — The nonlinear case study reports robustness to pendulum parameter changes
- **Type:** faithful paraphrase
- **Location:** nonlinear swing-up experiment; conclusion
- **Claim:** In the reported nonlinear pendulum task, the robust learned controller tolerated changes in pendulum weight and friction that degraded the standard RL controller.
- **Status:** verified

### Faithful paraphrase
The paper tests its robust-learning paradigm on nonlinear swing-up and changes physical parameters after learning. Under those case-study perturbations, the robust controller preserves effective control while the nominal standard-RL controller does not handle the altered dynamics as successfully.

### Context and limits
This is one continuous-control case study and should not be generalized to arbitrary GridWorld changes or algorithm families.

### Thesis use
Historical empirical support that robustness to bounded model mismatch can reduce performance loss under parameter shifts.

### Citation
Morimoto and Doya (2000), nonlinear experiment and conclusion.

## E5 — Worst-case robustness is not online resilience
- **Type:** scope synthesis grounded in the paper
- **Location:** overall formulation and experiments
- **Claim:** The method learns against a prescribed disturbance formulation; it does not introduce an unknown changepoint, a detector, context recall, or a post-change relearning metric.
- **Status:** verified

### Thesis use
A robust policy may reduce the initial degradation caused by a shift, but that effect must remain distinct from detecting the shift and recovering through new learning.

### Citation
Morimoto and Doya (2000), overall formulation.

## Provenance note
The repository's current `πηγές/SRC-71F2ECA651.md` resolves to an archival laboratory page rather than the paper text. This evidence was re-verified against the primary NeurIPS 2000 paper and the local source record should be reprocessed before it is treated as a complete canonical source conversion.