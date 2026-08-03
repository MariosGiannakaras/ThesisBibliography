---
κωδικός: SRC-01BBBA7EAB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-03"
source-language: en
---

# Evidence — Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations

## E1 — The target failure mode is dynamic missingness plus observation noise
- **Location:** Abstract; Section 1
- **Claim:** The paper studies RL when observation components can be missing at changing time steps and available sensor values are noisy.
- **Status:** verified

### Faithful paraphrase
The authors argue that real systems may lose sensor components because of malfunction, preprocessing delays, or asynchronous sampling while the remaining measurements are noisy. This setting violates the complete-observation assumptions used by many continuous-control RL methods. The missing dimensions and their timing are not assumed to be known in advance, so the problem is represented through partial observability rather than a fixed masked input.

## E2 — Decisions are made from a propagated belief state
- **Location:** Sections 3.2 and 4.1, belief-state propagation
- **Claim:** BI-PPO maintains a posterior belief over latent state using the history of incomplete/noisy observations and actions, and the policy acts from that belief representation.
- **Status:** verified

### Faithful paraphrase
The method propagates an intermediate belief through a learned transition model and then updates it with the available observation components. Missing values are handled within the belief update instead of being treated as ordinary zeros or copied blindly from the previous time step. This is a principled example of resilience to degraded sensing through state estimation, not through modifying the environment transition model itself.

## E3 — The derivation has explicit missingness and distributional assumptions
- **Location:** Section 3.2; Section 4.1
- **Claim:** The method assumes MCAR or MAR missingness and uses Gaussian approximations for tractable belief inference.
- **Status:** verified

### Faithful paraphrase
The observation indicator is assumed independent of the latent state in the sense required by MCAR/MAR formulations. Noise is modeled with a Gaussian distribution, and the transition/belief calculations use Gaussian or local approximations. These assumptions matter when interpreting robustness results: performance under arbitrary adversarial corruption is not established by this experiment.

## E4 — Observation robustness and environment adaptation are distinct
- **Location:** Abstract; experiments; overall formulation
- **Claim:** The reported robustness concerns corrupted or missing observations, not explicit detection and recovery from a changed MDP.
- **Status:** verified

### Faithful paraphrase
The experiments vary incompleteness and noise while the agent uses belief imputation to continue executing the task. The paper does not introduce a changepoint detector, context-switching policy memory, or recovery-time metric for structural environment changes. It therefore supports an observation-robustness axis in the thesis and should not be cited as evidence for online non-stationary adaptation.
