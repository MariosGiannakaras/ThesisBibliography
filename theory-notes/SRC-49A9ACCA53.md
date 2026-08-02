---
source_id: SRC-49A9ACCA53
language: en
material_role: supporting-theory
citation_grade: unstable-transcript
review_date: "2026-08-02"
---

# Theory notes — Safe reinforcement learning under non-stationarity seminar

## 1. Non-stationarity makes old experience progressively less representative

The talk motivates forgetting-based learning in environments whose rewards, costs, or transition behavior change over time. If the environment is non-stationary, using all historical data with equal weight can make the agent slow to respond because older observations describe dynamics that may no longer hold.

Mechanisms discussed include periodic restart, sliding-window estimation, and exponentially decayed weighting. These mechanisms implement the same broad principle: recent observations should matter more when the environment is changing.

### Thesis use

This supports the conceptual distinction between a stationary Q-learning baseline and recency-aware or reset-based adaptive agents. It also motivates reporting the amount of history retained after a change.

## 2. Variation budget controls the theoretical forgetting-rate trade-off

The seminar introduces a variation budget as a measure of how much the environment changes over a time interval. When the amount of variation is known or can be estimated, the restart/forgetting frequency can be tuned to the expected level of non-stationarity: faster change justifies more aggressive forgetting, while slower change permits more reuse of older experience.

### Thesis use

A variation budget is not identical to a change detector. It is prior information about the total amount of change. Experiments should distinguish:

- oracle/prior knowledge of change magnitude;
- unknown change magnitude with fixed hyperparameters;
- adaptive detection or tuning from observed data.

## 3. Safe non-stationary RL requires joint performance and constraint accounting

The constrained-MDP part of the talk considers both reward and a safety-cost signal that may themselves change across episodes. The learner therefore has two simultaneous objectives: maintain task performance and control cumulative constraint violation while continuing to learn under non-stationarity.

### Thesis use

Recovery should not be evaluated from return alone. A method can recover reward quickly while causing excessive hazard visits or constraint violations during adaptation. Utility and safety costs should therefore be reported separately.

## 4. Restart-based adaptation and adaptive change detection are different mechanisms

The talk distinguishes methods that choose a restart schedule using prior knowledge of environmental variation from methods that try to detect non-stationarity online. In the latter case, a restart can be triggered when observations violate bounds or expectations that should hold in a stationary regime.

### Thesis use

This is directly relevant to the baseline separation:

- scheduled/recency forgetting;
- detector-triggered reset;
- oracle change notification;
- no detector / continual update.

A detection mechanism should be evaluated with false alarms and detection delay, not only downstream reward.

## 5. Risk-sensitive adaptation can couple safety/risk parameters with non-stationarity detection

The risk-sensitive portion of the seminar explains that, when variation information is known, the forgetting mechanism and the risk-control component can be designed relatively independently. With adaptive detection, however, the detection statistic can depend on the risk-sensitive value representation, coupling the risk parameter and the change-response mechanism.

### Thesis use

If a resilience agent uses a risk-sensitive or uncertainty-sensitive detector, detector behavior should not be treated as independent of the risk hyperparameter. Tuning and ablation must reflect that coupling.

## 6. Within-task non-stationarity differs from explicit multi-task/meta-learning

The talk separates two settings:

1. a single task whose environment changes over time without explicit task boundaries;
2. a sequence of related tasks with known boundaries, where prior tasks can be used to improve the initialization for a new task.

The second setting is closer to meta-learning or context transfer; the first requires detecting or tracking change inside an ongoing task.

### Thesis use

This supports a strict distinction between:

- unknown-regime online adaptation;
- known task-switch signals;
- context recall for recurring regimes;
- meta-learned initialization across explicitly separated tasks.

These settings should not be reported as equivalent forms of resilience.

## 7. Time-varying GridWorld is used as a controlled illustration

The seminar describes a simple GridWorld experiment with time-varying goals and obstacle/safety states to illustrate non-stationary safe exploration.

### Thesis use

This is conceptually relevant to the thesis benchmark design: a small GridWorld can vary task utility and safety structure independently while preserving interpretability. The seminar is useful for this design insight even if exact experimental claims are taken from the underlying papers instead.

## Reliability boundary

These notes preserve the useful conceptual material from the seminar. Because the stored transcript contains substantial automatic-transcription errors, it should not be used alone for exact theorem statements, equations, numerical guarantees, or detailed algorithm reproduction. Those details should be checked against the corresponding primary publications when needed.
