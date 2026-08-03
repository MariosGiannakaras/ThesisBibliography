---
κωδικός: SRC-E6A5B7584B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-03"
source-language: en
---

# Evidence — Reinforcement Learning in Non-Stationary Environments

## E1 — Stationarity is the assumption being relaxed
- **Location:** Abstract; Introduction; Section 3 assumptions
- **Claim:** Classical RL methods are built around stationary transition/reward dynamics, whereas the paper studies settings in which the active environment model changes over time.
- **Status:** verified

### Faithful paraphrase
The paper frames non-stationarity as a direct violation of the stationary transition and reward assumptions underlying standard MDP/RL optimization. When the active model changes, an agent that keeps updating one undifferentiated value function can make sub-optimal decisions because samples collected under different models are mixed together. This supports treating an abrupt environment change as a distinct experimental event rather than as ordinary stochastic transition noise.

## E2 — Context Q-learning combines change detection with policy retention
- **Location:** Section 1.1, “Our Contributions”; Section 5, Context Q-learning
- **Claim:** The proposed method detects model changes from online samples, learns policies for distinct contexts, and can reuse a policy when a previously experienced context returns.
- **Status:** verified

### Faithful paraphrase
Context Q-learning uses observed state/reward samples to detect changes without requiring the transition and reward functions to be supplied to the learner. A detected context is associated with its learned policy; when evidence supports a known context, the method improves or reuses the stored policy instead of discarding all earlier information. The authors explicitly motivate this as a way to avoid catastrophic forgetting across recurring environment models.

## E3 — Detection quality and task reward are measured separately
- **Location:** Section 1.1; Section 6 experiments
- **Claim:** The evaluation reports change-detection metrics in addition to accumulated reward.
- **Status:** verified

### Faithful paraphrase
The experiments assess the detector through quantities such as mean detection delay, precision, and recall, while the RL component is assessed through reward collected in dynamic environments. This separation is methodologically important: a detector can identify a change quickly yet still yield poor recovery, or the agent can retain reward despite imperfect detection. A thesis experiment should therefore report both detection and post-change performance rather than collapsing them into one return value.

## E4 — The method has structured assumptions and is not universal resilience
- **Location:** Section 1.1; problem formulation; related-work discussion
- **Claim:** Context Q-learning is model-free with respect to environment functions but still assumes structured change patterns and a detector/context mechanism.
- **Status:** verified

### Faithful paraphrase
The paper does not claim adaptation to arbitrary open-ended distribution shift. Its approach is designed around changes that can be detected and represented as environment contexts, with stored knowledge available for previously experienced settings. For thesis use, it is therefore a strong adaptive baseline for piecewise-stationary changes, not evidence that context recall solves every form of structural novelty.
