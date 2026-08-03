---
κωδικός: SRC-211B10ADBA
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — A Survey Analyzing Generalization in Deep Reinforcement Learning

## E1 — Generalization limits arise from both incomplete MDP coverage and function approximation

- **Type:** faithful paraphrase
- **Location:** Introduction
- **Claim:** Deep-RL generalization can be limited because high-dimensional MDPs cannot be exhaustively explored and because neural function approximation introduces its own failure modes.
- **Status:** verified

### Faithful paraphrase

Korkmaz identifies incomplete exploration of large MDPs as a root limitation on generalization and separately notes problems inherited from deep neural function approximation. These mechanisms are related but should not be treated as the same cause of failure.

### Thesis use

Keep environment coverage/generalization diagnostics separate from robustness tests aimed at perturbing learned function approximators.

### Citation

Korkmaz (2024), Introduction.

## E2 — RL data collection is policy-dependent and sequential

- **Type:** faithful paraphrase
- **Location:** Section 3.1, Definition 3.1
- **Claim:** A generic RL training algorithm chooses its current policy and subsequent interactions as functions of the history observed so far.
- **Status:** verified

### Faithful paraphrase

The survey formalizes an RL algorithm as maintaining a current policy, querying the MDP, observing transitions and rewards, and updating future behavior using only the accumulated interaction history. Data collection is therefore endogenous to the agent rather than an independent fixed dataset.

### Thesis use

Use matched interaction budgets, controlled seeds, and comparable initialization because different policies can generate different training data even in the same environment.

### Citation

Korkmaz (2024), Section 3.1.

## E3 — Generalization interventions can act on different parts of the RL pipeline

- **Type:** faithful paraphrase
- **Location:** Sections 3.3–3.7
- **Claim:** The survey distinguishes methods that alter the training algorithm, reward, observation/state, transition dynamics, or policy.
- **Status:** verified

### Faithful paraphrase

The taxonomy separates changes to the learning algorithm from transformations applied to rewards, observed states, transition probabilities, or action-selection policies. This identifies where in the RL pipeline a proposed generalization method acts rather than treating all interventions as one class.

### Context and limits

A practical method can combine several categories, and the taxonomy is not a ranking of effectiveness.

### Thesis use

Map perturbations and interventions explicitly to observation, reward/cost, transition/rules, action execution, and learning-algorithm axes.

### Citation

Korkmaz (2024), Sections 3.3–3.7.

## E4 — “Generalization” is underspecified unless the changing component and update regime are stated

- **Type:** methodological inference grounded in the survey taxonomy
- **Location:** Abstract; Introduction; Section 3
- **Claim:** A generalization claim should identify which part of the MDP varies and whether the policy is frozen or updated during evaluation.
- **Status:** verified

### Faithful paraphrase

Because the survey groups generalization approaches by the component that changes or is transformed, reporting only a generic “generalization” score obscures the mechanism under test. For a reproducible evaluation, the changing component, information available to the agent, and test-time update rules need to be stated explicitly.

### Thesis use

Keep frozen-policy robustness/generalization, online recovery, and repeated continual adaptation as distinct experimental modes.

### Citation

Korkmaz (2024), Abstract and Sections 1–3.
