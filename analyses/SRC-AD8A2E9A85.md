---
κωδικός: SRC-AD8A2E9A85
κατάσταση: επαληθευμένη
ρόλος: κύρια
έκδοση-που-ελέγχθηκε: "Machine Learning 8, 279-292 (1992), author-hosted journal PDF"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Scientific analysis — Q-learning

## Bibliographic identity

Christopher J. C. H. Watkins and Peter Dayan, **Q-learning**, *Machine Learning*, 8, 279–292, 1992. DOI: 10.1007/BF00992698.

- **Primary-source status:** foundational algorithm/convergence paper.
- **Checked text:** author-hosted copy of the published paper at Peter Dayan's UCL/Gatsby publication site.
- **Thesis role:** core theoretical foundation for Fixed Q-Learning and Adaptive Q-Learning.

## Research purpose and scope

The paper formalizes Q-learning as a model-free method for learning optimal action values in controlled Markovian domains and gives a detailed convergence theorem. It is important for the thesis precisely because it makes the boundary of the classical claim clear: the result is about learning optimal action values under the paper's discrete Markov setting and sampling/convergence assumptions. It is not a theorem that ordinary Q-learning will track an abruptly changing or repeatedly non-stationary environment with bounded degradation or recovery time.

## Algorithmic mechanism

Q-learning maintains an action-value estimate Q(s,a). After observing a transition from state s under action a, with reward r and successor state s', the update moves Q(s,a) toward a target formed from the immediate reward plus the discounted value of the currently best-valued action at s'. This maximization target is what makes the control rule off-policy: the target evaluates the greedy action independently of the behavior policy actually used to collect the transition.

This distinction matters in the five-agent thesis comparison:

- **Fixed Q-Learning** and **Adaptive Q-Learning** use the same Q-learning mechanism and the same nominally learned checkpoint/configuration family.
- Their experimental distinction is deployment behavior, not a claim that they are two different published algorithms: Fixed Q-Learning disables post-change learning, while Adaptive Q-Learning continues ordinary Q-learning updates after the hidden environmental change.
- The paper therefore supplies the shared algorithmic foundation; the fixed/adaptive split is a thesis protocol intervention designed to isolate the contribution of continued online updating.

## Convergence claim and its assumptions

The paper states and proves convergence to optimal action values with probability one under the conditions it specifies, including discrete action-value representation and repeated sampling of actions in states, together with the stochastic-approximation/Markov assumptions developed in the theorem. The abstract explicitly ties the result to controlled Markovian domains and repeated sampling.

For thesis use, the important methodological boundary is:

**stationary/Markov convergence is not a non-stationary tracking guarantee.**

Once transition dynamics, observations, action execution, or reward-generating behavior changes over time, previously learned values may become stale. Whether continued Q-learning adapts fast enough then depends on visitation, exploration, step size, disturbance structure, finite evaluation horizon and the information available to the agent. Those quantities must be measured experimentally rather than inferred from the 1992 convergence theorem.

## Relationship to SARSA

Q-learning's next-state target uses the maximum estimated action value rather than the value of the next action actually selected by the behavior policy. This is the exact theoretical contrast needed when SARSA is introduced as the on-policy continual model-free comparator. The thesis should not frame Q-learning versus SARSA as simply two names for temporal-difference control; they differ in the policy represented by the bootstrap target under exploratory behavior.

## Relationship to Dyna-Q

The paper is also directly relevant to the Dyna family because Sutton's Dyna-Q architecture uses Q-learning updates both on real experience and on model-generated hypothetical experience. Dyna therefore changes the source/amount of update experience and adds a learned-model planning mechanism; it does not replace the Q-learning backup with an unrelated value-learning rule.

## Thesis-safe claims

This source can support:

1. Q-learning is a model-free reinforcement-learning/control method for Markovian domains.
2. Its action-value update bootstraps from the best estimated next-state action value, giving the standard off-policy TD-control mechanism.
3. The paper proves a classical convergence result subject to its stated discrete/sampling/Markov assumptions.
4. Fixed and Adaptive Q-Learning in this thesis can legitimately share Q-learning as their theoretical base while differing only in whether post-change updates are allowed.
5. Classical Q-learning convergence should not be presented as evidence of resilience, recovery speed, or optimal tracking under environmental non-stationarity.

## Limitations and threats to misuse

- The paper predates the contemporary continual/non-stationary RL framing used in the thesis.
- Its convergence result is asymptotic and assumption-bound; the thesis evaluates finite post-change windows.
- Repeated state-action sampling is not automatically satisfied by any finite exploratory deployment.
- The paper does not define resilience, cumulative deficit, immediate degradation, terminal gap, or recovery metrics.
- It does not establish that a fixed learning rate is optimal for changing environments.

## Relation to other corpus sources

- `SRC-701E163AC8` (Sutton & Barto, 2018) supplies the modern textbook treatment of Q-learning, SARSA, Dyna-Q and Dyna-Q+ and the stationary/non-stationary distinction.
- `SRC-F6BD3A6B18` (Sutton, 1990) uses Q-learning inside Dyna and evaluates changing-world behavior.
- `SRC-39696F490F` and `SRC-8025C139CE` place these simple mechanisms inside broader continual/non-stationary RL taxonomies.

## Decision

**Verified and selected as a core primary theoretical source.** Use it for the algorithm and bounded convergence claim, while keeping all post-change resilience claims empirical.
