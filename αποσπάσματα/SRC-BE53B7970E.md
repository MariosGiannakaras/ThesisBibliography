---
κωδικός: SRC-BE53B7970E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Deep Reinforcement Learning with Double Q-learning

## E1 — Maximization over inaccurate action values can create upward bias

- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Theorem 1
- **Claim:** Q-learning can systematically overestimate action values when the same inaccurate estimates are used to select and evaluate the maximizing action.
- **Status:** verified

### Faithful paraphrase

Van Hasselt, Guez, and Silver show that maximization preferentially selects overestimated actions. Their theoretical argument demonstrates that even when individual value estimates are unbiased in aggregate, estimation errors can make the maximum exceed the true optimal value. The effect is not tied to one particular source of error.

### Context and limits

Overestimation is not identical to deliberate optimism for exploration, and a uniform upward shift in all values need not harm action ranking.

### Thesis use

If a neural Q-learning baseline is included, measure value overestimation as a possible confound rather than interpreting every transient Q-value spike after a shift as failed adaptation.

### Citation

Van Hasselt, Guez, and Silver (2016), Abstract, Introduction, and Theorem 1.

## E2 — Non-stationarity is one possible source of estimation error, not the paper's adaptation target

- **Type:** faithful paraphrase
- **Location:** “Overoptimism due to estimation errors”
- **Claim:** The paper explicitly notes that environmental noise, function approximation, non-stationarity, and other mechanisms can all make value estimates inaccurate enough to induce maximization bias.
- **Status:** verified

### Faithful paraphrase

The maximization-bias argument depends on the existence of value-estimation errors rather than on why they arose. The authors list non-stationarity among several possible causes, which means a regime change can increase the conditions under which overestimation appears without making maximization bias itself a change-detection or recovery mechanism.

### Thesis use

Treat maximization bias as a diagnostic confound for value-based agents under change, not as evidence that Double DQN is a resilience algorithm.

### Citation

Van Hasselt et al. (2016), “Overoptimism due to estimation errors.”

## E3 — Double DQN separates action selection from target evaluation

- **Type:** faithful paraphrase
- **Location:** Double Q-learning and Double DQN sections
- **Claim:** Double DQN uses the online network to select the greedy next action and the target network to evaluate that selected action.
- **Status:** verified

### Faithful paraphrase

Standard DQN uses target-network values both to choose and evaluate the maximizing action. Double DQN decouples these roles: the current online network selects the action, while the target network supplies the value used in the TD target. This adapts the Double Q-learning principle without requiring two completely independent deep networks.

### Thesis use

Use Double DQN or a corresponding ablation if a DQN-family baseline is included, so known maximization bias does not dominate the comparison unnecessarily.

### Citation

Van Hasselt et al. (2016), Double Q-learning and Double DQN sections.

## E4 — Double DQN improves value accuracy, not environmental resilience by itself

- **Type:** faithful paraphrase
- **Location:** Abstract; experimental sections
- **Claim:** The reported contribution is reduced value overestimation and improved Atari performance, not changepoint detection, context memory, or continual adaptation.
- **Status:** verified

### Faithful paraphrase

The empirical results show that Double DQN can reduce DQN's observed value overestimation and improve policy quality in several Atari games. The training protocol does not introduce an external environmental shift followed by explicit detection and recovery.

### Thesis use

Classify Double DQN as a better-controlled neural Q-learning comparator, not as a resilience mechanism.

### Citation

Van Hasselt et al. (2016), Abstract and experiments.
