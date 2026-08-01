---
κωδικός: SRC-3EA1176D3A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Solving robust MDPs as a sequence of static RL problems

## E1 — Robustness and resilience are different capabilities

- **Type:** faithful paraphrase
- **Location:** Section 1, opening paragraph
- **Claim:** The paper uses robustness for retaining guaranteed performance without further training and resilience for recovering from environmental change through continued learning.
- **Status:** verified

### Faithful paraphrase

Zouitine, Geist, and Rachelson explicitly contrast robustness with resilience. In their terminology, robustness is the ability of a learned policy to retain an acceptable level of performance when the controlled system differs from the training system, without additional training. Resilience instead concerns recovery from environmental changes by continuing to learn.

### Context and limits

This terminology is particularly useful for separating a fixed robust controller from an adaptive agent, but it is a definition used in this robust-RL paper rather than a universally mandated standard.

### Thesis use

Keep two research questions separate: whether performance is preserved without updating, and whether performance recovers when online updating is allowed.

### Citation

Zouitine, Geist, and Rachelson (2024), Section 1.

## E2 — Static and dynamic transition uncertainty encode different environment-change models

- **Type:** faithful paraphrase
- **Location:** Section 2, robust MDP formulation and static model
- **Claim:** In the dynamic model, transition dynamics may vary at every step; in the static model, one transition function is selected and remains fixed throughout a trajectory.
- **Status:** verified

### Faithful paraphrase

The paper defines the dynamic robust-MDP formulation as a game in which an adversarial environment may choose transition dynamics over time. The static model instead selects one transition function from the uncertainty set and keeps that model fixed for the trajectory. Under stationary policies and rectangular uncertainty sets, the robust stationary-policy values admit a specific equivalence, but the general static optimization problem is not thereby made trivial.

### Context and limits

Per-step stochastic disturbances, episode-level persistent variants, and abrupt persistent regime changes should not be treated as the same experimental condition.

### Thesis use

Label perturbations explicitly by temporal semantics: per-step disturbance, persistent episode model, or changepoint followed by a persistent new regime.

### Citation

Zouitine, Geist, and Rachelson (2024), Section 2.

## E3 — Simple gridworlds can isolate transition-model uncertainty

- **Type:** faithful paraphrase
- **Location:** Section 4, illustration; Algorithm 1; Figure 1
- **Claim:** The paper uses a small gridworld to make transition uncertainty, worst-case model search, and robust-policy evaluation directly inspectable.
- **Status:** verified

### Faithful paraphrase

The Windy Walk example gives the agent alternative routes whose transition behavior depends on a controlled wind parameter. A discrete uncertainty set contains candidate values of this transition parameter. IWOCS repeatedly solves ordinary MDP problems for candidate models, maintains pessimistic value information over the models already discovered, and searches for an additional model that is adverse for the current policy.

### Context and limits

The gridworld is an illustrative instrumented problem. It supports controlled robust-policy analysis but does not establish real-world external validity or measure change-detection delay and post-change learning recovery.

### Thesis use

Use a minimal gridworld when exact rule versions and oracle evaluations are needed to isolate model uncertainty without adding unrelated confounds.

### Citation

Zouitine, Geist, and Rachelson (2024), Section 4, Algorithm 1, and Figure 1.

## E4 — Robust policies can be conservative

- **Type:** faithful paraphrase
- **Location:** Section 2, discussion of robust value iteration
- **Claim:** Worst-case robust policies can become conservative, especially for large uncertainty sets under rectangularity assumptions.
- **Status:** verified

### Faithful paraphrase

The paper notes that robust value iteration can produce highly conservative policies because it optimizes against adverse transition models in the uncertainty set. It discusses prior work that reduces this conservatism by learning tighter uncertainty sets, relaxing rectangularity, or otherwise incorporating more structure into the uncertainty model.

### Context and limits

Higher disturbed performance alone does not establish overall superiority if the policy sacrifices substantial nominal utility.

### Thesis use

Report clean-condition utility together with disturbed-condition performance for every robust baseline.

### Citation

Zouitine, Geist, and Rachelson (2024), Section 2.
