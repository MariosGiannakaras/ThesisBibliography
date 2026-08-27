# Agent Strategy Theory Crosswalk — 2026-08-27

## Purpose

This research note records the theoretical rationale for the bounded agent-strategy set currently being evaluated in `resilient-ai-agents-thesis`. It is **not** final thesis prose and it does not turn GridWorld into the research subject. GridWorld is only the common controlled testbed used to expose and compare strategy behavior under uncertainty/change.

The scientific comparison is mechanism-driven:

> no post-change adaptation → off-policy model-free adaptation → on-policy model-free adaptation → learned-model planning → learned-model planning plus directed re-exploration.

The note also keeps robust optimization conceptually separate from online adaptation.

## 1. Fixed Q-Learning

**Definition in this thesis:** a tabular Q-learning policy/value checkpoint learned under the nominal regime, then held fixed during evaluation.

**What it represents:** retention without adaptation. It asks what happens if an agent continues to act using previously learned action values after the environment changes but is not allowed to update them.

**Theory base:** Q-learning itself is off-policy TD control. The “fixed” strategy is not a separate published learning algorithm; it is a deployment condition imposed on the same learned Q-values used to initialize the adaptive comparator.

**Interpretation constraints:** poor post-change performance would show sensitivity of stored nominal values to shift, not a failure of Q-learning's stationary convergence theorem. Good performance would indicate resistance/generalization under a particular disturbance, not active recovery.

Sources:
- Watkins & Dayan (1992), *Q-learning*, DOI 10.1007/BF00992698 — dedicated canonical intake added 2026-08-27.
- Sutton & Barto (2018), `SRC-701E163AC8`, Chapter 6.

## 2. Adaptive Q-Learning

**Definition in this thesis:** the matched tabular Q-learning strategy that continues ordinary online Q-value updates after the environment changes.

**What it represents:** simple continual model-free adaptation without an explicit change detector, reset mechanism, privileged regime signal or learned transition model.

**Mechanism:** the TD target uses the observed reward and the maximum estimated next-state action value. The behavior policy determines collected experience; the update target itself is off-policy.

**Non-stationary meaning:** continual updating can replace stale estimates as new experience arrives, but classical stationary convergence results do not imply optimal tracking of an evolving MDP. Adaptation speed depends on visitation, exploration, step size and the nature/severity of the change.

Sources:
- Watkins & Dayan (1992), dedicated intake.
- Sutton & Barto (2018), `SRC-701E163AC8`.
- Khetarpal et al. (2022) and Padakandla (2021), dedicated continual/non-stationary review intake added 2026-08-27.

## 3. SARSA

**Definition in this thesis:** continual tabular on-policy TD control under the same agent-visible information boundary as the Q-learning strategies.

**Mechanism:** the TD target uses the next action actually selected by the current behavior policy. This is the central algorithmic distinction from Q-learning's greedy maximum target.

**Why it is scientifically distinct:** under exploratory behavior, SARSA learns values that include the consequences of that behavior. The classic cliff-walking example shows that this can produce qualitatively different learned behavior from off-policy Q-learning when exploratory actions carry meaningful risk/cost.

**What must not be claimed:** SARSA is not automatically “safer,” “more robust” or “more resilient.” The on-policy target is a mechanism; resilience remains an empirical outcome under the thesis protocol.

Sources:
- Sutton & Barto (2018), `SRC-701E163AC8`, Chapter 6.
- Existing focused Chapter 6 record `SRC-D52DF7B9A4`.
- Rummery & Niranjan (1994), *On-line Q-learning using connectionist systems*, historical-lineage intake added 2026-08-27. Its function-approximation setting must not be conflated with the thesis's tabular SARSA implementation.

## 4. Dyna-Q

**Definition in this thesis:** a tabular agent that learns from real experience, learns an empirical model of transitions/rewards, and performs additional Q-learning-style planning backups using model-generated experience.

**Mechanism:** Dyna allocates computation to simulated experience. It can propagate newly observed consequences more rapidly than direct updates alone, but this planning relies on the model being sufficiently current.

**Resource distinction:** planning steps are computation, not additional environment interactions. Fair comparison therefore requires both real interaction budgets and planning budgets to be explicit.

**Non-stationary vulnerability:** when environment dynamics change, the learned model can become stale. Planning can repeatedly exploit stale model knowledge until real interaction revisits affected state-action pairs and corrects it.

Sources:
- Sutton, *Integrated Modeling and Control Based on Reinforcement Learning and Dynamic Programming* (NIPS 1990 / volume 3), dedicated primary intake added 2026-08-27.
- Sutton & Barto (2018), `SRC-701E163AC8`, Chapter 8.
- Sutton (1991), *Dyna, an integrated architecture for learning, planning, and reacting*, DOI 10.1145/122344.122377, supporting primary architecture source.

## 5. Dyna-Q+

**Definition in this thesis:** Dyna planning plus an explicit mechanism that encourages re-testing state-action pairs whose real consequences may have become stale.

**Core changing-environment mechanism:** Dyna-Q+ tracks elapsed time since a state-action pair was tried in real interaction and uses a recency-based planning bonus. Long-untried actions become more attractive to test, which can reveal changes that pure exploitation of a stale model would miss.

**Additional algorithmic distinction:** the textbook changing-environment version also allows previously untried actions from visited states into planning with an initial zero-reward self-loop model. Therefore plain Dyna-Q must not be implemented merely as “Dyna-Q+ with kappa=0” if those extra untried-action semantics remain active.

**Trade-off:** directed re-exploration can improve change discovery but can also reduce immediate reward by deliberately testing uncertain/stale actions. It is a mechanism with a cost, not a dominance guarantee.

Sources:
- Sutton's Dyna changing-world paper, dedicated primary intake added 2026-08-27.
- Sutton & Barto (2018), `SRC-701E163AC8`, Chapter 8.

## 6. Why Dyna-Q and Dyna-Q+ both belong

Keeping both strategies provides an ablation-like mechanism comparison:

- If Dyna-Q and Dyna-Q+ both improve similarly relative to model-free learners, planning/model use may be the main contributor.
- If Dyna-Q+ differs materially from Dyna-Q after change, directed re-exploration is a plausible contributor.
- If both fail, the learned-model/planning mechanism may be insufficient or harmful under the tested uncertainty.

This is stronger scientifically than comparing only Dyna-Q+ to model-free Q-learning because it avoids attributing every difference to the exploration bonus when planning itself also changed.

## 7. Reference strategies

A deterministic **Random Agent** is useful only as a lower reference scale and correctness fixture. It is not a resilient strategy and must not enter the fair ranking.

A fully informed/oracle planner may serve as an upper/debug reference, but privileged evaluator/model knowledge violates the main agents' information contract. It must therefore remain visually and statistically separate from fair competitors.

## 8. Robust planning is a different mechanism

Robust MDP methods optimize against explicit uncertainty/ambiguity sets over dynamics/rewards. This differs from ordinary continual TD updating, behavior-policy TD updating, empirical-model planning, or directed exploration for discovering change.

The repository already contains verified robust-MDP theory, including the classic Nilim–El Ghaoui line and related analysis. Historical R0 evidence showed severe nominal conservativeness in the particular construction used by earlier pilot work. That is evidence about that construction, not proof that robust MDPs are generally unsuitable.

A redesigned Robust Planner is therefore a conditional sixth comparator only if a small predeclared non-final gate demonstrates nominal viability, fair information use and acceptable runtime. It must not be reinstated solely to increase model count.

## 9. Broader non-stationary/continual RL framing

The five main strategies are a bounded experimental cross-section, not an exhaustive taxonomy of continual RL. Broader literature includes changepoint detection/restart, context/task inference, memory/replay management, meta-learning, actor-critic/policy-gradient methods, representation/plasticity methods, robust/adversarial formulations and uncertainty-aware planning.

Khetarpal et al. organize continual RL through properties of non-stationarity and review formulations, algorithms, benchmarks and metrics. Padakandla focuses directly on RL algorithms for dynamically varying environments. Existing repository sources such as `SRC-660560956D`, `SRC-0406E13B97`, `SRC-3C543330E4`, `SRC-5775601BD7` and `SRC-F909CABDEB` provide complementary modern context on non-stationarity, reactive exploration, continual adaptation, computational difficulty and plasticity.

The thesis deliberately avoids turning this broader literature into a large deep-RL benchmark. The selected strategies are small enough to implement, tune, visualize and compare reproducibly while still isolating materially different adaptation/planning mechanisms.

## 10. Fair-comparison implications

For all five main scientific strategies:
- evaluator-only true state, executed action, changepoint indicator, regime ID and disturbance flags remain hidden unless the common observation policy explicitly exposes them;
- pre-change knowledge/training policy must be declared and matched or scientifically justified;
- hyperparameter tuning must use predeclared non-final evidence, not final outcomes;
- multiple seeds/repetitions are required;
- final retained settings must freeze before final results are inspected;
- interaction budget and Dyna planning budget must be separately visible;
- the same disturbance definitions/layout protocol should be used for paired comparison;
- failed/non-recovering runs remain evidence rather than being silently discarded.

## 11. Theory coverage required before thesis writing

The bibliography/evidence layer should support all of the following before WP7:
1. MDP/RL/TD foundations;
2. Q-learning update and stationary convergence assumptions;
3. Fixed versus continual updating as an experimental deployment distinction;
4. SARSA on-policy target versus Q-learning off-policy target;
5. Dyna real-experience/model/planning architecture;
6. Dyna-Q+ recency/untried-action exploration in changing environments;
7. the stationary-to-non-stationary problem and stability/plasticity/adaptation concepts;
8. robust-MDP optimization as a distinct uncertainty mechanism;
9. why the five-strategy set is bounded and mechanism-driven rather than exhaustive.

No section should claim that GridWorld itself motivates these agent families. GridWorld is the shared controlled experimental surface used to make the mechanisms observable and comparisons reproducible.