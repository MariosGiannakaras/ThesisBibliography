---
κωδικός: SRC-A203ABEEFE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Prioritized Experience Replay

## E1 — Replay trades interaction demand for memory and computation
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** Experience replay stores past transitions and reuses them for additional learning updates, reducing temporal correlation and allowing rare experience to influence learning more than once.
- **Status:** verified

### Faithful paraphrase
Schaul et al. describe replay memory as a way to mix experiences from different times and reuse transitions that would otherwise be discarded after a single online update. This can lower the amount of new environment experience needed at the cost of additional storage and optimization work.

### Thesis use
Count replay memory and repeated gradient/value updates as resource costs, not as free sample efficiency.

### Citation
Schaul et al. (2016), Abstract and Introduction.

## E2 — TD-error magnitude is a prioritization proxy, not a change detector
- **Type:** faithful paraphrase
- **Location:** Section 3.2
- **Claim:** Prioritized replay uses the magnitude of temporal-difference error as an accessible proxy for how surprising or potentially useful a transition is for learning.
- **Status:** verified

### Faithful paraphrase
The ideal quantity would be expected learning progress, which is not directly observable. The paper therefore uses absolute TD error as a practical priority signal because it measures disagreement between the current value estimate and its bootstrap target. The authors also note that TD error can be misleading when rewards are noisy or approximation errors persist.

### Thesis use
Do not treat a TD-error spike as calibrated evidence of an environmental changepoint without an independently validated sequential decision rule.

### Citation
Schaul et al. (2016), Section 3.2.

## E3 — Greedy prioritization can lose diversity and over-focus on noise
- **Type:** faithful paraphrase
- **Location:** Section 3.3
- **Claim:** Purely greedy TD-error replay can repeatedly sample a narrow subset of transitions and be sensitive to stochastic noise or persistent approximation errors.
- **Status:** verified

### Faithful paraphrase
The paper identifies several failure modes of greedy replay: priorities become stale for rarely replayed transitions, noise spikes can generate artificially large errors, and large-error transitions can dominate the queue for long periods. Stochastic prioritization is introduced to preserve a nonzero probability of replaying lower-priority experience and improve diversity.

### Thesis use
For non-stationary replay experiments, log the age/regime composition and priority distribution of sampled transitions.

### Citation
Schaul et al. (2016), Section 3.3.

## E4 — Non-uniform replay introduces sampling bias
- **Type:** faithful paraphrase
- **Location:** Section 3.4; Algorithm 1
- **Claim:** Prioritized sampling changes the replay distribution and therefore biases updates unless corrected; the paper uses importance-sampling weights with a tunable correction exponent.
- **Status:** verified

### Faithful paraphrase
Because transitions are no longer drawn uniformly, the update distribution differs from the one implied by ordinary replay. The authors introduce importance-sampling weights controlled by `beta`, with full correction at `beta = 1`, and anneal the correction during training in their implementation.

### Thesis use
Report prioritization exponent, correction exponent/schedule, replay capacity, and replay ratio for any PER baseline.

### Citation
Schaul et al. (2016), Section 3.4 and Algorithm 1.

## E5 — A replay buffer can mix incompatible regimes after a changepoint
- **Type:** thesis-protocol implication grounded in replay semantics
- **Location:** Introduction and Section 3
- **Claim:** Replay intentionally mixes older and newer transitions; in a changing MDP this can cause pre-change and post-change data to be updated together.
- **Status:** verified

### Thesis use
Compare uniform/PER replay against no replay, oracle buffer flush, and detector-triggered flush or recency weighting. Report buffer composition by regime and transition age.

### Citation
Schaul et al. (2016), replay-memory formulation.

## E6 — PER is not a non-stationary adaptation guarantee
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall paper
- **Claim:** The paper studies replay efficiency primarily in Atari DQN and does not define environmental changepoints, recovery delay, or recurring-regime memory.
- **Status:** verified

### Thesis use
Treat PER as a replay mechanism whose effect on recovery must be measured empirically in the thesis protocol.

### Citation
Schaul et al. (2016), overall scope.