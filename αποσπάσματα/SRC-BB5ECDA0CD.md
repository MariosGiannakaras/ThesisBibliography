---
κωδικός: SRC-BB5ECDA0CD
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Online Robust Reinforcement Learning Through Monte-Carlo Planning

## E1 — Robust MCTS incorporates transition and reward ambiguity into tree-search backups
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** The method extends Monte Carlo Tree Search so planning accounts explicitly for ambiguity in both transition dynamics and reward distributions.
- **Status:** verified

### Faithful paraphrase
Dam et al. formulate simulation-to-reality mismatch through ambiguity sets around nominal transition and reward models. Their robust MCTS replaces ordinary tree-search value propagation with a robust backup and modifies exploration bonuses so action selection reflects adverse models in those sets rather than assuming the simulator is exact.

### Thesis use
Treat robust MCTS as a planning-based robustness comparator, not as an environmental change detector.

### Citation
Dam et al. (2025), Abstract and Introduction.

## E2 — The ambiguity-set family is part of the algorithm specification
- **Type:** faithful paraphrase
- **Location:** Introduction; method overview
- **Claim:** The framework supports ambiguity sets based on total variation, KL, chi-squared, and Wasserstein measures.
- **Status:** verified

### Faithful paraphrase
The robust backup and its associated exploration treatment depend on how admissible transition or reward distributions are defined. The paper considers several divergence/distance families, making the ambiguity metric and robustness budget explicit components of the planning problem.

### Thesis use
For any robust planner, report set family, radius/budget, nominal simulator, and calibration rule.

### Citation
Dam et al. (2025), Introduction and method overview.

## E3 — The reported root-value convergence rate matches standard MCTS in sample order under the paper's assumptions
- **Type:** faithful paraphrase
- **Location:** Abstract; Contributions
- **Claim:** The paper derives an `O(n^-1/2)` finite-sample convergence rate for robust root-value estimation, comparable in order to standard MCTS.
- **Status:** verified

### Context and limits
Comparable sample-order does not imply equal constants, memory, or wall-clock latency. Robust backups and ambiguity handling add computation per search update.

### Thesis use
Report simulator rollouts and decision latency separately from environment interactions.

### Citation
Dam et al. (2025), Abstract and Contributions.

## E4 — FrozenLake evidence is robustness-under-mismatch evidence
- **Type:** faithful paraphrase
- **Location:** Contributions and experiments
- **Claim:** The empirical evaluation includes FrozenLake and reports stronger performance of robust MCTS than standard MCTS under the tested model mismatches.
- **Status:** verified

### Context and limits
This comparison concerns planning under an ambiguity set. It does not evaluate unknown repeated changepoints, detector false alarms, context recall, or post-shift relearning.

### Thesis use
Use FrozenLake results only as evidence that robust planning can hedge model mismatch in a discrete navigation domain.

### Citation
Dam et al. (2025), experiments.

## E5 — MCTS planning queries and model-free learning interactions are not the same resource
- **Type:** protocol implication grounded in the planning architecture
- **Location:** Introduction; search-based planning discussion
- **Claim:** MCTS allocates simulated rollouts at decision time, whereas model-free agents primarily spend real/environment interaction on learning updates.
- **Status:** verified

### Thesis use
Maintain separate counters for environment steps, simulator/model queries, planning rollouts, and wall-clock decision latency in cross-family comparisons.

### Citation
Dam et al. (2025), search-based planning discussion.

## E6 — Search-tree bandit non-stationarity is not benchmark-environment non-stationarity
- **Type:** scope clarification grounded in the theoretical analysis
- **Location:** Contributions
- **Claim:** The analysis can view nodes in the changing search tree as non-stationary bandit problems, but this internal planning phenomenon is distinct from an exogenous temporal change in the deployed MDP.
- **Status:** verified

### Thesis use
Do not cite the search-tree analysis as evidence of environmental changepoint resilience.

### Citation
Dam et al. (2025), Contributions and theoretical discussion.