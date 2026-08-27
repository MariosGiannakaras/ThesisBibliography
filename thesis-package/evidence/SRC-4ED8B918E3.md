---
κωδικός: SRC-4ED8B918E3
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Evidence — Empirical Design in Reinforcement Learning

## Evidence E1 — Compare learning against experience, not blindly against episodes
- **Type:** faithful paraphrase
- **Location:** Section 2.1, performance-over-experience discussion
- **Claim:** Episode-index comparisons can give algorithms unequal amounts of environment experience when episode lengths differ.
- **Thesis use:** cross-method learning budget
- **Status:** verified

### Faithful paraphrase
When agents can terminate episodes at different times, comparing performance at the same episode number can compare policies that have consumed different numbers of samples. A steps/interactions axis gives a common experience scale.

### Thesis-safe implication
Protocol-v2 should use environment interactions/timesteps as its principal common Phase-A training budget and record episode counts only as behavioral diagnostics.

## Evidence E2 — Hyperparameter-search opportunity is part of fairness
- **Type:** faithful paraphrase
- **Location:** Section 3, “Picking hyperparameter sets fairly”
- **Claim:** Giving one algorithm more hyperparameter settings/search effort can bias an apparent algorithm comparison.
- **Thesis use:** tuning policy
- **Status:** verified

### Faithful paraphrase
At minimum, compared algorithms should receive the same number of tested hyperparameter settings. If an optimization procedure is used instead, its iteration budget and the steps/seeds used for configuration evaluation should be controlled consistently.

### Thesis-safe implication
Q-Learning must not receive a mature tuned configuration while DQN/PPO receive only defaults; each retained method receives one predeclared comparable tuning opportunity.

## Evidence E3 — Random variation must be measured rather than selected away
- **Type:** faithful paraphrase
- **Location:** Sections on variation/stability and comparing agents
- **Claim:** Stochastic variation across independent runs is part of empirical RL evaluation and must be represented in reported uncertainty.
- **Thesis use:** root/seed protocol
- **Status:** verified

### Thesis-safe implication
Seeds are randomization variables, not tunable choices. No best-seed final selection is valid.

## Evidence E4 — Paired/blocking designs are useful only when their shared randomness is legitimate
- **Type:** faithful paraphrase
- **Location:** multiple-agent comparison and statistical-design discussion
- **Claim:** Controlling shared nuisance variation can improve comparisons, but the design and unit of replication must remain explicit.
- **Thesis use:** Frozen/Continual paired evaluation
- **Status:** verified

### Thesis-safe implication
Matched branches may share environment schedules where scientifically valid, but episodes within a root do not become independent replicates.

## Evidence E5 — Better statistics cannot repair biased experimental design
- **Type:** faithful paraphrase
- **Location:** hyperparameters, experimenter bias, baseline construction
- **Claim:** Experimenter choices about environments, baselines and tuning can create biased conclusions even when downstream statistics are computed correctly.
- **Thesis use:** protocol freeze and environment selection
- **Status:** verified

### Thesis-safe implication
The GridWorld discrimination rule, tuning policy, primary metrics and primary contrast family must be frozen before confirmatory outcomes are inspected.

## Avoid overclaiming
This source supplies empirical-design principles. It does not identify the best algorithm for this thesis, prescribe the final number of roots, or prove that one universal aggregation method fits the project’s root/layout hierarchy.
