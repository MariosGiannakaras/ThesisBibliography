---
κωδικός: SRC-46CF36BC1E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# Evidence — The Primacy Bias in Deep Reinforcement Learning

## Evidence E1 — Early experience can dominate later learning
- **Type:** faithful paraphrase
- **Location:** official PMLR abstract
- **Claim:** Deep-RL agents can rely disproportionately on early interactions and underuse useful evidence encountered later.
- **Thesis use:** interpretation of post-change ordinary learning
- **Status:** verified

### Thesis-safe implication
A weak Adaptive deep-RL response after a change may reflect learning-history/plasticity limitations and should not be generalized beyond the controlled experiment.

## Evidence E2 — Primacy bias can harm the remaining learning process
- **Type:** faithful paraphrase
- **Location:** official PMLR abstract
- **Claim:** Training on progressively growing datasets can risk overfitting to earlier experience, negatively affecting later learning.
- **Thesis use:** threat to validity / continual-learning interpretation
- **Status:** verified

## Evidence E3 — Reset is a substantive intervention
- **Type:** faithful paraphrase
- **Location:** official PMLR abstract
- **Claim:** The paper proposes periodically resetting part of the agent and reports improved performance across studied discrete- and continuous-action domains.
- **Thesis use:** intervention boundary
- **Status:** verified

### Thesis-safe implication
A reset, replay clearing or other plasticity mitigation cannot be inserted into the thesis Adaptive branch as a neutral implementation detail; it would define a different experimental intervention.

## Avoid overclaiming
This source does not show that primacy bias will occur in the thesis GridWorld, does not establish a universal PPO/DQN failure mode and does not justify adding resets to the default protocol-v2 design.
