---
κωδικός: SRC-AD8A2E9A85
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Evidence — Q-learning (Watkins & Dayan, 1992)

## E1 — Q-learning is model-free control in Markovian domains

- **Type:** faithful paraphrase
- **Location:** Abstract and Section 1, p. 279
- **Claim:** Q-learning learns action values from experienced consequences without requiring an explicit learned map/model of the domain.
- **Thesis use:** theoretical basis of Fixed Q-Learning and Adaptive Q-Learning.
- **Status:** verified

### Faithful paraphrase
The paper presents Q-learning as a model-free reinforcement-learning method that incrementally improves action-value estimates from interaction in controlled Markovian domains.

### Limitation
Do not extend this statement into a claim that Q-learning is model-free with respect to every possible implementation aid or that it is automatically appropriate for non-stationary deployment.

## E2 — Classical convergence is conditional, not a resilience guarantee

- **Type:** faithful paraphrase
- **Location:** Abstract; convergence theorem developed in the paper
- **Claim:** The paper establishes probability-one convergence to optimal action values under its stated discrete representation and repeated-sampling assumptions.
- **Thesis use:** distinguish stationary convergence theory from finite post-change adaptation.
- **Status:** verified

### Faithful paraphrase
Under the paper's stated assumptions, including repeated sampling of actions in states and discrete action-value representation, Q-learning converges to optimal action values with probability one.

### Limitation
The theorem does not establish bounded recovery time, low cumulative deficit, or optimal tracking after an unannounced change in transition/action/observation behavior.

## E3 — Off-policy bootstrap target distinguishes Q-learning from SARSA

- **Type:** algorithmic interpretation checked against the paper's Q-learning rule
- **Location:** Section 2, Q-learning update definition
- **Claim:** Q-learning's bootstrap target uses the best estimated next-state action value rather than the value of the next behavior action.
- **Thesis use:** mechanism contrast with SARSA.
- **Status:** verified

### Safe use
Describe Adaptive Q-Learning as ordinary off-policy continual TD control and SARSA as on-policy continual TD control. Do not claim one mechanism is generally more resilient before observing the predeclared experiment.

## E4 — Fixed versus Adaptive Q-Learning is a protocol intervention

- **Type:** thesis-safe methodological inference
- **Location:** Q-learning mechanism in this source + thesis deployment contract
- **Claim:** Both thesis strategies may share the same Q-learning theory/checkpoint; disabling versus continuing post-change updates isolates the effect of online adaptation.
- **Thesis use:** methods chapter and agent-strategy rationale.
- **Status:** verified as a thesis design inference

## Avoid overclaiming

This source does not prove that:
- Q-learning is resilient under non-stationarity;
- continual updating always improves post-change performance;
- the thesis learning rate/exploration setting is theoretically optimal;
- finite-run recovery follows from the asymptotic convergence theorem.