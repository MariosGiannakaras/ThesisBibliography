---
κωδικός: SRC-0F8A6588DC
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — NovGrid: A Flexible Grid World for Evaluating Agent Response to Novelty

## E1 — Novelty is a sudden change to environment mechanics or properties
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Novelty Background and Related Work
- **Claim:** NovGrid defines novelty as an unexpected change to the mechanics or properties of the environment rather than an isolated outlier under an otherwise fixed distribution.
- **Status:** verified

### Faithful paraphrase
Balloch et al. study novelty as a temporal change that transforms the sequential decision problem after an agent has learned under a previous regime. They explicitly distinguish this setting from ordinary outlier detection, because the post-novelty observations belong to a changed environment rather than being aberrant samples that should simply be rejected.

### Context and limits
The paper focuses on abrupt injected changes. Slow continuous drift and independent observation noise require separate formulations.

### Thesis use
Reserve `novelty` or `sudden_shift` for temporal environment changes and do not treat isolated prediction-error spikes as proof that the environment has changed.

### Citation
Balloch et al., Abstract and Novelty Background and Related Work.

## E2 — The ontology separates object/action changes and their effect on the solution set
- **Type:** faithful paraphrase
- **Location:** An Ontology of Novelty for Sequential Decision Making; Table 1
- **Claim:** The proposed ontology distinguishes object versus action novelties, unary versus relational changes, and barrier, delta, or shortcut effects on optimal solutions.
- **Status:** verified

### Faithful paraphrase
The ontology classifies whether a novelty changes objects or action mechanics, whether the changed property is unary or relational, and whether the transformation makes optimal solutions longer, leaves their length broadly unchanged, or creates shorter solutions. The taxonomy is then instantiated with concrete MiniGrid examples such as key–door changes, transition determinism changes, and action-effect changes.

### Context and limits
The ontology is designed for sequential decision making and is not an exhaustive taxonomy of every uncertainty or distribution-shift mechanism.

### Thesis use
Construct a factorized perturbation matrix so structural changes are not mixed arbitrarily with reward drift, observation corruption, or bounded stochastic model error.

### Citation
Balloch et al., An Ontology of Novelty for Sequential Decision Making, Table 1.

## E3 — The interface can remain fixed while the underlying MDP changes
- **Type:** faithful paraphrase
- **Location:** Ontology assumptions; Novelty MiniGrid
- **Claim:** NovGrid keeps the dimensions of the action and observation interfaces compatible across the change while allowing action effects, object properties, reachable states, and dynamics to differ.
- **Status:** verified

### Faithful paraphrase
The framework assumes that the number of actions and the size and shape of observations remain consistent before and after novelty injection. Nevertheless, actions may acquire different effects and observations or states that never occurred before the change may become reachable afterward. The wrapper injects the novelty by switching the environment's reset and grid-generation behavior at a specified episode.

### Context and limits
A fixed interface does not imply a stationary MDP or equal task difficulty across regimes.

### Thesis use
Define interface invariants separately from transition/reward invariants and add validation tests that confirm only the intended mechanism changes.

### Citation
Balloch et al., ontology assumptions and Novelty MiniGrid section.

## E4 — Adaptation should be decomposed into immediate robustness, final performance, and adaptation efficiency
- **Type:** faithful paraphrase
- **Location:** Evaluation and Baseline; Figure 2
- **Claim:** NovGrid proposes multiple metrics because different parts of the post-change learning curve capture different capabilities.
- **Status:** verified

### Faithful paraphrase
The framework includes metrics for the performance of the pre-novelty policy immediately after the change, the final post-novelty performance reached after additional learning, the amount of interaction required to converge, and one-shot performance after very little post-change experience. These quantities intentionally separate immediate resistance from later adaptation.

### Context and limits
The paper's specific metric named “resilience” is one operational definition and should not be treated as a universal definition of resilience.

### Thesis use
Report immediate degradation, adaptation success, recovery time or interactions, recovered performance, and one-shot response as separate metrics before considering any aggregate score.

### Citation
Balloch et al., Evaluation and Baseline, Figure 2.

## E5 — Continued learning is a necessary baseline but not a dedicated novelty-adaptation mechanism
- **Type:** faithful paraphrase
- **Location:** Evaluation and Baseline; Figure 3
- **Claim:** A standard RL agent that simply continues training after novelty provides a useful reference for determining whether a specialized adaptation mechanism adds value.
- **Status:** verified

### Faithful paraphrase
The baseline PPO agent in the NovGrid experiment has no novelty-specific adaptation component. After the injected change, it continues reinforcement learning from task reward. Its post-change learning curve therefore shows what can be achieved by ordinary continued learning under the same changed environment without an explicit novelty detector or specialized response mechanism.

### Context and limits
Calling this baseline a lower bound in the paper does not prove that it will be worse than every specialized method in every environment.

### Thesis use
Retain a `continue_learning` baseline alongside frozen-policy, full-reset, and detector-triggered variants.

### Citation
Balloch et al., Evaluation and Baseline, Figure 3.

## E6 — Reward changes are outside the specific NovGrid ontology used in this paper
- **Type:** faithful paraphrase
- **Location:** ontology assumptions
- **Claim:** The paper keeps the agent mission and extrinsic reward structure fixed across novelty and focuses on changes to environment properties and dynamics.
- **Status:** verified

### Faithful paraphrase
The authors assume that the agent's mission remains the same before and after novelty injection and state that changes to the goal or extrinsic reward structure are left to future integration with continual- and multitask-learning settings.

### Thesis use
Treat reward drift as a separate experimental axis rather than citing NovGrid as direct evidence for reward-change adaptation.

### Citation
Balloch et al., ontology assumptions.