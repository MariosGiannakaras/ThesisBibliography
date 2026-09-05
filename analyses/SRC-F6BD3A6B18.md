---
κωδικός: SRC-F6BD3A6B18
κατάσταση: επαληθευμένη
ρόλος: κύρια
έκδοση-που-ελέγχθηκε: "NeurIPS 1990 proceedings full paper, pp. 471-478"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Scientific analysis — Integrated Modeling and Control Based on Reinforcement Learning and Dynamic Programming

## Bibliographic identity

Richard S. Sutton, **Integrated Modeling and Control Based on Reinforcement Learning and Dynamic Programming**, *Advances in Neural Information Processing Systems 3*, 1990, pp. 471–478.

- **Primary-source status:** foundational Dyna paper.
- **Checked original:** official NeurIPS proceedings PDF.
- **Thesis role:** core theoretical and empirical source for Dyna-Q, planning with a learned model, and the recency/exploration mechanism later standardized as Dyna-Q+.

## Core Dyna architecture

The paper defines Dyna architectures as systems that integrate direct trial-and-error reinforcement learning with execution-time planning using a learned forward model. The important architectural point is that real interaction and hypothetical/model-generated experience feed a common incremental learning/planning process rather than being separate offline phases.

For the thesis, this establishes a mechanism-level distinction:

- Adaptive Q-Learning and SARSA are **model-free** continual learners: they update from real interaction only.
- Dyna-Q adds a **learned world model plus planning backups** generated from hypothetical experience.
- Dyna-Q+ adds a further **directed re-exploration/recency mechanism** to the Dyna-Q architecture.

Thus Dyna-Q is required as its own comparator if the experiment intends to identify whether any improvement from Dyna-Q+ is attributable to planning itself or specifically to the extra recency-driven exploration mechanism.

## Dyna-Q mechanism

Section 4 describes Dyna-Q as Q-learning combined with the Dyna idea of using a learned world model to generate hypothetical experience and plan. The same Q-style value-learning rule is therefore updated from both real and model-generated transitions.

The paper's navigation experiments also vary the number of hypothetical experiences generated per real experience. This makes the number of planning steps a real computational/algorithmic budget. Increasing planning does not mean that the agent has received more real environment interactions; it means more updates are produced from its learned model between/alongside real interactions.

This supports a key fairness rule for the thesis: Dyna-Q and Dyna-Q+ should use matched planning-step budgets when the intended comparison is the contribution of Dyna-Q+'s exploration bonus.

## Exploration bonus and Dyna-Q+

The paper identifies inadequate exploration as a problem in changing worlds. It records how long it has been since each state-action pair was tried in real experience and adds a bonus proportional to the square root of elapsed time. Actions that have not been tried recently therefore become more attractive because their consequences are more uncertain.

The paper also allows hypothetical experience for actions never tried before, using an initialized model so that the exploration signal can be propagated backward through planning. This detail matters for implementation fidelity: Dyna-Q+ is not completely characterized by taking a plain Dyna-Q implementation and merely adding a positive `kappa` to already observed state-action pairs. The treatment of previously untried actions is part of the intended change-seeking exploration behavior.

## Changing-world experiments

Section 5 directly compares three systems in two changing-maze experiments, including Dyna-Q with the exploration bonus (called Dyna-Q+) and Dyna-Q without it (called Dyna-Q− in this paper), with matched planning parameter k=10.

### Blocking change

A previously short route is blocked and a longer route becomes necessary. Both Dyna-Q variants eventually adapt, while their adaptation behavior reflects the consequences of model staleness and exploration after the change.

### Shortcut change

A new shortcut is opened without invalidating the old route. The exploration-bonus Dyna-Q+ system discovers the shortcut whereas the non-bonus Dyna-Q system continues exploiting the still-valid old route. This is especially relevant to the thesis rationale: when previously successful actions remain adequate, a purely exploitative/model-updating agent can lack evidence that a better regime has appeared, while explicit recency-driven re-exploration can create that evidence.

These experiments are evidence for a mechanism and a controlled historical example, not proof that Dyna-Q+ will dominate Dyna-Q under the thesis's action remapping, execution failures or observation corruption.

## Why plain Dyna-Q must remain a separate scientific strategy

If the thesis compared only Adaptive Q-Learning against Dyna-Q+, two factors would change simultaneously:

1. learned-model planning is added;
2. explicit recency-driven exploration is added.

A plain Dyna-Q comparator holds the second mechanism off while retaining the first. Therefore the five-agent ladder isolates:

- no post-change adaptation;
- model-free off-policy adaptation;
- model-free on-policy adaptation;
- learned-model planning;
- learned-model planning plus directed re-exploration.

This is a scientifically interpretable mechanism decomposition rather than model-count inflation.

## Thesis-safe claims

This source supports:

1. Dyna combines direct RL, online model learning and planning with model-generated experience.
2. Dyna-Q uses Q-learning as the value-update mechanism while adding a learned world model and planning.
3. The number of hypothetical/model-generated updates per real experience is a planning-computation parameter rather than extra real-world sampling.
4. A recency/uncertainty exploration bonus can make long-untried actions attractive.
5. The Dyna-Q+ changing-world experiments show a concrete case where directed re-exploration discovers an environmental improvement that ordinary Dyna-Q does not discover in the measured interval.
6. Plain Dyna-Q and Dyna-Q+ are mechanism-distinct and should be compared with matched planning budgets when isolating the bonus.

## Limitations

- The experiments use small navigation mazes and historical implementations; they do not constitute a universal ranking.
- The paper's Dyna-Q− name should not be confused with a distinct modern algorithm family; in thesis-facing terminology use **Dyna-Q** for the no-recency-bonus strategy and record historical nomenclature in technical notes.
- The paper does not supply the thesis's exact `kappa` or planning-step values as universally optimal settings.
- It does not evaluate observation mislocalization or the thesis's exact persistent action-remap protocol.
- Model-based planning can amplify stale model errors after a change; empirical behavior must be measured rather than assumed beneficial.

## Relation to other corpus sources

- `SRC-AD8A2E9A85`: primary Q-learning foundation used inside Dyna-Q.
- `SRC-701E163AC8`: canonical modern textbook treatment of Dyna-Q/Dyna-Q+ and SARSA/Q-learning.
- `SRC-39696F490F` and `SRC-8025C139CE`: broader continual/non-stationary framing and evaluation context.

## Decision

**Verified and selected as a core primary theoretical/empirical source for the Dyna-Q versus Dyna-Q+ mechanism contrast.**
