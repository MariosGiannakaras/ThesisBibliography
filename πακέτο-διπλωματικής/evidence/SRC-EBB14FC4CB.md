---
κωδικός: SRC-EBB14FC4CB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Reinforcement Learning for Non-Stationary Markov Decision Processes: The Blessing of (More) Optimism

## Evidence E1 — Reward and transition non-stationarity are separate sources of variation
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1 and 2.2
- **Claim:** The model allows reward means and transition distributions to vary over time and controls them through separate variation budgets.
- **Thesis use:** shift taxonomy; drifting environments
- **Topics:** reward drift; transition drift; variation budget
- **Status:** verified

### Faithful paraphrase
The paper defines a non-stationary MDP in which both the expected reward function and the transition kernel may evolve with time. Their total changes are quantified separately, so reward drift and transition drift are distinct components of environmental non-stationarity rather than one undifferentiated perturbation.

## Evidence E2 — Forgetting is necessary because historical data can become obsolete
- **Type:** faithful paraphrase
- **Location:** Section 1 and Table 1
- **Claim:** Methods that use the entire history deteriorate under exogenous change because old observations can cease to represent the current environment.
- **Thesis use:** recency baseline rationale
- **Topics:** forgetting; recency; obsolete data
- **Status:** verified

### Faithful paraphrase
In a changing environment, the standard stationary strategy of estimating from all accumulated observations can become harmful because older samples reflect outdated rewards or dynamics. The paper therefore combines forgetting through a sliding window with additional optimism.

### Limitation
Forgetting is not a changepoint detector. It continuously limits how much historical data affects current estimates.

## Evidence E3 — SWUCRL2-CW combines a sliding window with confidence widening
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1; algorithm formulation
- **Claim:** SWUCRL2-CW uses recent observations and deliberately widens confidence regions to handle a difficulty specific to non-stationary RL.
- **Thesis use:** theoretical background for recency plus uncertainty handling
- **Topics:** sliding window; confidence widening; optimism
- **Status:** verified

### Faithful paraphrase
The proposed base algorithm forgets sufficiently old observations through a sliding window and then expands the model confidence region rather than constructing the tightest possible plausible set. The extra optimism is introduced because, in a changing MDP, conventionally tight confidence regions can contain models with unfavorable diameter properties and lead to poor dynamic-regret behavior.

## Evidence E4 — Known variation budgets are an oracle/prior-information assumption
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1
- **Claim:** The parameterization of SWUCRL2-CW assumes knowledge of the reward and transition variation budgets.
- **Thesis use:** oracle/non-oracle protocol
- **Topics:** prior knowledge; variation budget; tuning
- **Status:** verified

### Faithful paraphrase
The paper's budget-aware guarantee for SWUCRL2-CW is derived when the total reward and transition variation budgets are known. In an empirical benchmark, giving an algorithm such information should therefore be labeled as an oracle or prior-information condition rather than treated as ordinary online detection.

## Evidence E5 — BORL removes variation-budget knowledge, not all tuning or cost
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1; Section 7
- **Claim:** BORL adaptively tunes the base learner without receiving the variation budgets and retains the same order of dynamic-regret guarantee.
- **Thesis use:** non-oracle adaptive tuning background
- **Topics:** parameter-free; BORL; dynamic regret
- **Status:** verified

### Faithful paraphrase
BORL places an additional bandit-style tuning procedure around SWUCRL2-CW so that the algorithm does not need the variation budgets as inputs. The term parameter-free in this claim concerns those budgets; it does not imply zero hyperparameters, zero computational overhead, or zero prior design choices.

## Evidence E6 — Dynamic regret and local recovery metrics answer different questions
- **Type:** faithful paraphrase
- **Location:** Section 2.2
- **Claim:** Dynamic regret compares cumulative reward against time-indexed stationary optima and is not the same quantity as detection delay or time to recovery after a discrete shift.
- **Thesis use:** metric separation
- **Topics:** dynamic regret; recovery time; detection delay
- **Status:** verified

### Faithful paraphrase
The paper measures performance through dynamic regret relative to the sequence of long-run average rewards of the MDP defined by the reward and transition model at each time. This gives a cumulative non-stationary performance criterion, whereas a changepoint benchmark can additionally report local transient quantities such as detection delay, maximum degradation, and time to regain a threshold level of performance.

## Avoid overclaiming
The paper is primarily theoretical. It should not be cited as empirical evidence that SWUCRL2-CW or BORL will rank above lightweight tabular baselines in the thesis GridWorld, and knowledge of a variation budget should not be mislabeled as online change detection.
