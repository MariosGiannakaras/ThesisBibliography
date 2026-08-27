---
κωδικός: SRC-4C34DF3E17
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Evidence — Loss of plasticity in deep continual learning

## Evidence E1 — Standard deep learning can lose plasticity during prolonged continual learning
- **Type:** faithful paraphrase
- **Location:** Abstract; reinforcement-learning experiments
- **Claim:** Standard deep-learning methods can become progressively less able to learn new data during extended continual learning.
- **Thesis use:** interpretation of deep Continual regimes
- **Status:** verified

### Thesis-safe implication
A `Continual` deep branch is an empirical continued-training baseline; continued gradient updates do not guarantee successful adaptation.

## Evidence E2 — Standard PPO degraded under repeated abrupt dynamics changes in the paper’s RL setting
- **Type:** faithful paraphrase
- **Location:** Figure 3 and “Details and further analysis in reinforcement learning”
- **Claim:** In Ant-v3 with friction changed after successive two-million-step intervals, standard PPO performance worsened across changes, while plasticity-preserving variants performed better.
- **Thesis use:** non-stationary deep-RL caveat
- **Status:** verified

### Limitation
This is a long-horizon continuous-control experiment. It does not predict that PPO will fail in the thesis GridWorld.

## Evidence E3 — Loss of plasticity is distinct from catastrophic forgetting
- **Type:** faithful paraphrase
- **Location:** Introduction/definition discussion
- **Claim:** Plasticity loss concerns reduced capacity to learn new information, whereas catastrophic forgetting concerns loss of performance on old information.
- **Thesis use:** terminology and failure interpretation
- **Status:** verified

## Evidence E4 — Plasticity-preserving changes are interventions, not neutral implementation details
- **Type:** faithful paraphrase
- **Location:** continual-backpropagation, L2 and optimizer experiments
- **Claim:** Continual backpropagation, regularization and optimizer changes alter learning behavior and can mitigate degradation in the studied settings.
- **Thesis use:** protocol boundary
- **Status:** verified

### Thesis-safe implication
Protocol-v2 must not silently add replay resets, reinitialization, special regularization or continual-backpropagation to make a deep Continual branch recover. Such changes require a separate predeclared method/RQ.

## Avoid overclaiming
This source is strong evidence that plasticity is a real deep-continual-learning threat. It is not evidence that every neural method fails under every environmental change, nor that a particular mitigation should be part of the thesis final matrix.
