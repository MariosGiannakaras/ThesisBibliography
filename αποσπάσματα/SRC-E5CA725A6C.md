---
κωδικός: SRC-E5CA725A6C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Deep Reinforcement Learning in Non-stationary Environments

## E1 — Unknown changepoints define a non-oracle adaptation problem

- **Type:** faithful paraphrase
- **Location:** Abstract; Chapter 3, Sections 3.1–3.2
- **Claim:** The thesis studies sequences of MDP regimes in which changes to reward or transition distributions occur at times that are not supplied to the agent.
- **Status:** verified

### Faithful paraphrase

Liu formalizes deep reinforcement learning in non-stationary environments with abrupt, unknown change points. The state and action spaces remain compatible across regimes, while reward and transition distributions can change. The learner must infer change events from interaction rather than receive the true changepoints as an oracle signal.

### Context and limits

The evaluator can still know the true changepoints so detector latency and correctness can be measured. “Unknown to the agent” does not mean “unknown in the experimental ground truth.”

### Thesis use

Use this as support for a non-oracle detection protocol with hidden changepoints and evaluator-side ground truth.

### Citation

Liu (2024), Abstract and Chapter 3, Sections 3.1–3.2.

## E2 — Detection and adaptation are separate subsystems

- **Type:** faithful paraphrase
- **Location:** Chapter 3, Sections 3.3.1–3.3.3
- **Claim:** DARL separates environmental change detection from the policy-adaptation mechanism that is invoked after a detected change.
- **Status:** verified

### Faithful paraphrase

The model-free framework first searches for evidence that the joint state–action behavior has changed and then uses a separate gradient-constrained mechanism to adapt the policy while selectively preserving prior knowledge. The detection stage determines whether a change has occurred; the adaptation stage determines how the policy is updated afterward.

### Context and limits

A detector can be accurate while the resulting adapter performs poorly, and a strong adapter can be triggered by a poor detector.

### Thesis use

Maintain independent detector and adapter scorecards and ablations.

### Citation

Liu (2024), Chapter 3, Sections 3.3.1–3.3.3.

## E3 — F1 score does not capture detection latency

- **Type:** faithful paraphrase
- **Location:** Chapter 3, Tables 3.3 and 3.5
- **Claim:** Detectors with similar or even perfect event-level F1 can still identify the same true changepoints at different delays.
- **Status:** verified

### Faithful paraphrase

In the reported CartPole experiments, DARL and CRL-Unsup can both attain an event-level F1 of 1.0 while their detected changepoints occur at different times after the true changes. The LunarLander results likewise show that classification-style detector quality and latency are not interchangeable measurements.

### Context and limits

The numerical delays are specific to the studied benchmarks and detector settings.

### Thesis use

Report precision, recall, F1, and detection delay separately.

### Citation

Liu (2024), Chapter 3, Tables 3.3 and 3.5.

## E4 — Combining complementary change signals can reduce false detections in the studied setting

- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.3; Table 3.4; Figure 3.8
- **Claim:** The joint use of policy/behavior change and state-distribution evidence detects the studied changes more faithfully than either component alone.
- **Status:** verified

### Faithful paraphrase

The ablation study shows that relying only on the policy-change signal or only on episodic/state-distribution evidence misses or misidentifies some changes. Requiring complementary evidence from both signals filters more spurious detections in the reported environments.

### Context and limits

This does not imply that adding more detector signals is universally beneficial; thresholds and signals still require validation.

### Thesis use

If a multi-signal detector is implemented, compare it with each component separately and measure false alarms and delay.

### Citation

Liu (2024), Chapter 3, Section 3.4.3, Table 3.4, and Figure 3.8.

## E5 — Preserving prior policies can cause negative transfer

- **Type:** faithful paraphrase
- **Location:** Chapter 3, adaptation analysis; Figures 3.6 and 3.10
- **Claim:** Previous-policy knowledge can hinder adaptation when it is irrelevant or conflicting with the new regime.
- **Status:** verified

### Faithful paraphrase

The thesis includes experiments in which a deliberately poor prior policy is introduced and shows that strong constraints forcing preservation of previous policies can increasingly obstruct learning in later regimes. DARL attempts to reduce this problem by weighting prior knowledge according to its relevance to the current environment.

### Context and limits

The mechanism is developed for gradient-based deep policies and should not be imported directly into a tabular agent without separate validation.

### Thesis use

Require scratch/no-transfer comparators and report a negative-transfer gap for any policy-reuse or context-memory mechanism.

### Citation

Liu (2024), Chapter 3, Sections 3.4.3–3.4.4 and Figures 3.6 and 3.10.

## E6 — False alarms and missed changes impose different adaptation costs

- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.4
- **Claim:** A false positive can trigger unnecessary adaptation, while a missed change leaves the agent operating with an obsolete policy; these failure modes should not be collapsed into one detector error rate.
- **Status:** verified

### Faithful paraphrase

The thesis analyzes detector failures through their downstream consequences. Spurious detections can cause needless policy updates and potential performance disruption, whereas missed changes delay adaptation and allow the old policy to remain active in an environment for which it is no longer appropriate.

### Thesis use

Log false-trigger adaptation cost and missed-change recovery cost separately.

### Citation

Liu (2024), Chapter 3, Section 3.4.4.

## E7 — The dissertation's deep methods are evidence for architecture principles, not mandatory thesis implementations

- **Type:** scope inference grounded in the dissertation
- **Location:** Chapters 3–6
- **Claim:** The dissertation proposes several deep model-free and model-based detection/adaptation systems, including latent-space approaches for high-dimensional inputs; these are more complex than the resource-aware tabular benchmark requires.
- **Status:** verified

### Thesis use

Use the source to justify detector/adapter separation, non-oracle evaluation, and negative-transfer controls. Implement the full deep frameworks only if the final experimental scope explicitly expands beyond the current resource-aware baseline set.

### Citation

Liu (2024), Chapters 3–6.
