---
κωδικός: SRC-D52DF7B9A4
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Q-learning: Off-policy TD Control

## E1 — Q-learning is off-policy TD control
- **Type:** faithful paraphrase
- **Location:** Section 6.5, pp. 131–132
- **Claim:** Q-learning updates an action value toward the immediate reward plus the maximum estimated value available in the next state.
- **Status:** verified

### Faithful paraphrase
Sutton and Barto define Q-learning as an off-policy temporal-difference control method. Its update uses the observed reward and the largest current action-value estimate in the successor state, so the learned value function targets greedy optimal action values even when the behavior policy that generates experience is exploratory.

### Context and limits
The behavior policy still determines which state–action pairs are visited and therefore which estimates receive data. Off-policy learning does not remove the need for adequate exploration or coverage.

### Thesis use
Use tabular Q-learning as the simplest continual-learning baseline and distinguish its target policy from the exploratory behavior policy used online.

### Citation
Sutton and Barto, Chapter 6, Section 6.5.

## E2 — Classical convergence assumptions do not cover a repeatedly changing target MDP
- **Type:** faithful paraphrase plus scope boundary
- **Location:** Section 6.5, p. 131
- **Claim:** The standard tabular convergence statement assumes continued updates of all state–action pairs and suitable stochastic-approximation step sizes in a fixed problem.
- **Status:** verified

### Faithful paraphrase
The text notes that Q-learning converges to the optimal action-value function under continued updating of every state–action pair and appropriate step-size conditions. This result concerns a stationary target value function. If rewards or transition dynamics repeatedly change, the target itself moves and the classical convergence statement no longer establishes post-change recovery behavior.

### Thesis use
Do not cite stationary Q-learning convergence as evidence of resilience; evaluate degradation and recovery empirically after every controlled shift.

### Citation
Sutton and Barto, Section 6.5.

## E3 — Greedy optimality and online exploratory performance can disagree
- **Type:** faithful paraphrase
- **Location:** Example 6.6, Cliff Walking, pp. 132–134
- **Claim:** An off-policy method can learn the values of a shorter greedy path while performing worse online because exploratory actions expose the behavior policy to large penalties.
- **Status:** verified

### Faithful paraphrase
In Cliff Walking, Q-learning learns values corresponding to the shortest path along the cliff edge. With continued epsilon-greedy action selection, occasional exploratory actions can send the agent into the cliff and incur a large penalty. Sarsa incorporates the exploratory behavior into its on-policy value estimates and learns a longer route that has better online reward under that fixed exploration rate.

### Context and limits
The example does not establish that Sarsa is universally safer or superior; the outcome depends on the task and exploration schedule.

### Thesis use
Report training-time hazards and online return in addition to greedy evaluation return, especially when adaptation requires renewed exploration.

### Citation
Sutton and Barto, Example 6.6.

## E4 — Maximization over noisy estimates creates positive bias
- **Type:** faithful paraphrase
- **Location:** Section 6.7; Figure 6.5
- **Claim:** Using the same noisy estimates to select and evaluate a maximizing action can bias the estimated maximum upward.
- **Status:** verified

### Faithful paraphrase
The maximization operation tends to select actions whose current estimation error is favorable, producing a positive bias when the same estimates are used both for selection and evaluation. Double learning reduces this effect by maintaining two value estimates so that one can select an action while the other evaluates it.

### Context and limits
Reducing maximization bias addresses an estimation problem; it is not a changepoint detector and does not guarantee faster recovery in a non-stationary environment.

### Thesis use
Consider Double Q-learning as a targeted ablation when reward or transition stochasticity makes maximization bias materially visible.

### Citation
Sutton and Barto, Section 6.7 and Figure 6.5.

## E5 — Full reset is a comparator, not a property of Q-learning
- **Type:** thesis-scope inference
- **Location:** Section 6.5 algorithm definition
- **Claim:** The textbook algorithm specifies initialization and iterative updates but does not define environment-change detection or reset semantics.
- **Status:** verified

### Faithful paraphrase
Standard Q-learning continues to update its existing table from new experience unless an experimenter explicitly reinitializes it. Resetting the Q-table after a known change is therefore a separate benchmark intervention rather than a feature implied by the algorithm.

### Thesis use
Keep continual Q-learning, full reset, and detector-triggered reset as separate baselines with explicit reset semantics.

### Citation
Sutton and Barto, Section 6.5.