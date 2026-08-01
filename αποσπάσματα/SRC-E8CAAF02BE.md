---
κωδικός: SRC-E8CAAF02BE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Planning and Acting in Partially Observable Stochastic Domains

## E1 — Partial observability requires reasoning about hidden state from history
- **Type:** faithful paraphrase
- **Location:** opening example; Introduction; POMDP formulation
- **Claim:** In a POMDP, the agent cannot directly observe the true world state and must use its history of actions and observations together with a world model to maintain an estimate of that state.
- **Status:** verified

### Faithful paraphrase
Kaelbling, Littman, and Cassandra motivate POMDPs with agents whose actions and observations are both imperfect. Because the current state is uncertain, the agent must combine previous actions, observations, and knowledge of the system dynamics to maintain a state estimate rather than acting as if the latest observation were the true state.

### Thesis use
Model observation uncertainty as partial observability when the hidden state remains decision-relevant; do not silently replace it with transition noise.

### Citation
Kaelbling, Littman, and Cassandra (1998), opening example and Introduction.

## E2 — The belief state is a sufficient information state for POMDP control
- **Type:** faithful paraphrase
- **Location:** POMDP theory sections
- **Claim:** The history can be summarized by a belief distribution over underlying states, and a policy can act on this belief rather than on the raw observation history.
- **Status:** verified

### Faithful paraphrase
The POMDP formulation converts uncertainty about the current state into a probability distribution over possible states. This belief is updated as the agent takes actions and receives observations and can be treated as the state of a corresponding belief-space decision problem.

### Context and limits
The update presumes a transition and observation model. An agent with exact model access therefore receives more prior information than a model-free learner.

### Thesis use
For belief/context agents, log belief entropy and posterior mass assigned to the true simulated state or regime when that quantity is available to the evaluator.

### Citation
Kaelbling, Littman, and Cassandra (1998), POMDP formulation and belief-state discussion.

## E3 — Actions may simultaneously change the world and gather information
- **Type:** faithful paraphrase
- **Location:** Introduction
- **Claim:** In a partially observable problem, an action can have both control value and information value, so acting for the most likely state is not always optimal.
- **Status:** verified

### Faithful paraphrase
The authors emphasize that POMDPs do not create a fundamental divide between actions that manipulate the environment and actions that gather information. The same action can do both. An agent may therefore choose a locally less rewarding action because the resulting observation reduces uncertainty and improves later decisions.

### Thesis use
If active disambiguation is implemented, report information-gathering action count and its reward, delay, and safety cost.

### Citation
Kaelbling, Littman, and Cassandra (1998), Introduction.

## E4 — Most-likely-state control can discard decision-relevant uncertainty
- **Type:** faithful paraphrase
- **Location:** opening example; Introduction
- **Claim:** Choosing the action appropriate for only the most probable state can be inferior to an action selected with the full uncertainty distribution in mind.
- **Status:** verified

### Faithful paraphrase
The navigation example notes that acting as though the most likely location were certain may be sufficient in some situations but not in others. When alternative state hypotheses imply different consequences or when information can be gathered, the complete uncertainty distribution can change the preferred action.

### Thesis use
Compare hard context selection with belief-weighted control rather than assuming the maximum-posterior context is always sufficient.

### Citation
Kaelbling, Littman, and Cassandra (1998), opening discussion.

## E5 — Partial observability, latent model uncertainty, and temporal environmental change are distinct
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall formulation
- **Claim:** A POMDP models uncertainty about the current hidden state under a specified stochastic model; this is not the same problem as uncertainty about which environment model is active or a changepoint that alters that model over time.
- **Status:** verified

### Thesis use
Keep `hidden_state_uncertainty`, `latent_regime_uncertainty`, and `environment_change` as separate experimental mechanisms.

### Citation
Kaelbling, Littman, and Cassandra (1998), overall POMDP formulation.

## E6 — Exact model access changes the fairness of comparisons
- **Type:** thesis-protocol implication
- **Location:** Introduction and formal model
- **Claim:** The planning problem assumes a complete and correct model of world dynamics and reward structure, whereas model-free agents must learn behavior from interaction.
- **Status:** verified

### Thesis use
Record transition-model, observation-model, and prior access for every agent and do not compare a model-informed belief planner against model-free Q-learning as if their information budgets were identical.

### Citation
Kaelbling, Littman, and Cassandra (1998), Introduction.