---
κωδικός: SRC-91D56A10CF
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Deep Reinforcement Learning amidst Continual Structured Non-Stationarity

## E1 — Structured non-stationarity can be represented through latent, temporally related task parameters

- **Type:** faithful paraphrase
- **Location:** Sections 1–2; Figure 2
- **Claim:** The DP-MDP models a sequence of MDPs whose dynamics and rewards are controlled by hidden task parameters that evolve according to a temporal process rather than being sampled independently.
- **Status:** verified

### Faithful paraphrase

Xie et al. define a dynamic-parameter MDP in which each episode presents an MDP determined by an unobserved parameter `z`. Unlike an i.i.d. task distribution, successive task parameters are related through a transition model. If `z` were directly observed, augmenting the state with that parameter would recover a fully observable MDP; the practical challenge is therefore to infer the latent context and learn how it evolves.

### Context and limits

This framework is particularly suited to structured, recurring, or smoothly evolving change. A single unpredictable regime switch with no exploitable temporal structure is a different problem.

### Thesis use

Separate predictable/structured drift from abrupt hidden changepoints in the scenario taxonomy.

### Citation

Xie et al. (2021), Sections 1–2 and Figure 2.

## E2 — Off-policy replay is most useful when experience is conditioned on the relevant context

- **Type:** faithful paraphrase
- **Location:** Sections 4–5
- **Claim:** LILAC combines latent-context inference with an off-policy actor-critic so that past experience can be reused while the policy and value function remain conditioned on the current task representation.
- **Status:** verified

### Faithful paraphrase

LILAC jointly learns a latent representation of the current MDP, a temporal prior over those latent parameters, and a maximum-entropy actor-critic conditioned on the inferred context. This structure lets the agent reuse off-policy trajectories from past tasks without forcing one context-free policy to average incompatible behaviors across changing MDPs.

### Context and limits

The paper does not imply that a neural latent model is necessary in small discrete environments. An explicit context label, model belief, or oracle context can provide simpler comparison points.

### Thesis use

Compare context-free replay with context-conditioned learning and include an oracle-context upper bound where feasible.

### Citation

Xie et al. (2021), Sections 4–5.

## E3 — Reward shifts, dynamics shifts, and combined shifts should be distinguishable

- **Type:** faithful paraphrase
- **Location:** Experimental environments and results
- **Claim:** The study evaluates non-stationarity produced by changing objectives, changing dynamics, and settings where both vary.
- **Status:** verified

### Faithful paraphrase

The experimental suite contains tasks in which target locations or objectives change, tasks in which physical dynamics such as wind or payload change, and tasks such as the HalfCheetah setting where both dynamics and target velocity vary. This shows that non-stationarity is not a single axis and that different components of the MDP can change independently or together.

### Context and limits

The continuous-control domains are implementation examples, not templates that must be reproduced in a tabular GridWorld.

### Thesis use

Use a factorial shift matrix with reward-only, transition/dynamics-only, and combined conditions.

### Citation

Xie et al. (2021), experimental section.

## E4 — Change rate and extrapolation are separate experimental factors

- **Type:** faithful paraphrase
- **Location:** Experimental analysis of Sawyer and continuously varying settings
- **Claim:** The paper varies how quickly latent parameters change and also tests continuation into previously unseen parameter values.
- **Status:** verified

### Faithful paraphrase

The Sawyer experiments vary the step size of a moving target to create different rates of non-stationarity, and the paper also evaluates smoothly varying intra-episode conditions and trajectories that continue into unobserved parameter regions. Performance under a familiar temporal pattern and performance when that pattern extrapolates beyond training are therefore treated as distinct tests.

### Context and limits

The reported extrapolation occurs within a learned structured latent process. It should not be interpreted as generic robustness to arbitrary out-of-distribution changes.

### Thesis use

Evaluate more than one change rate and state explicitly whether the temporal pattern itself appeared during training.

### Citation

Xie et al. (2021), experimental analysis of change rate and extrapolation.

## E5 — Sparse abrupt changes may require an explicit changepoint mechanism

- **Type:** faithful paraphrase
- **Location:** Conclusion and limitations
- **Claim:** The paper identifies sparse, discrete, or otherwise poorly predicted changes as a case where an explicit changepoint-detection mechanism may be useful in addition to latent predictive adaptation.
- **Status:** verified

### Faithful paraphrase

LILAC is designed around structured temporal evolution of hidden task parameters. The authors note that more abrupt or sparse changes can motivate mechanisms that explicitly identify a switch rather than relying only on a smoothly predictive latent transition model.

### Context and limits

A latent context model and a changepoint detector solve related but non-identical inference problems.

### Thesis use

Keep predictive structured-adaptation baselines distinct from detector-triggered reset or context-switching baselines.

### Citation

Xie et al. (2021), conclusion and limitations.
