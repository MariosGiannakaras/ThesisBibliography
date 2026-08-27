# Protocol-v2 Thesis-Writing Evidence Crosswalk — 2026-08-28

## Purpose

This note consolidates the protocol-v2 literature work into a writing-oriented evidence map. It is **not an external source**, **not final thesis prose**, and **not a substitute for the canonical `analyses/` and `evidence/` records**. Its purpose is to prevent later writing from losing the distinction between:

1. claims directly supported by literature;
2. project-specific experimental-design decisions motivated by that literature; and
3. empirical claims that can only be made after protocol-v2 results exist.

Use the original-language canonical analysis/evidence records when drafting citations. Do not cite this note as scientific evidence.

## 1. Empirical RL design and fair comparison

### Canonical sources

- `SRC-4ED8B918E3` — Patterson et al., *Empirical Design in Reinforcement Learning* (JMLR, 2024).
- `SRC-8D4F62D85D` — Henderson et al., *Deep Reinforcement Learning that Matters* (AAAI, 2018).

### Thesis-safe supported claims

- RL comparisons are sensitive to random variation, hyperparameter choices, implementation details, environment selection and reporting choices.
- Comparing methods at equal episode counts can imply unequal amounts of environment experience when episode lengths differ; environment interactions/timesteps are a more meaningful common experience currency.
- Hyperparameter-search opportunity is part of experimental fairness. Giving one method materially more search effort can bias apparent superiority.
- Seeds/repeated runs measure stochastic variation and must not be treated as hyperparameters from which the best run is selected.
- Strong statistical reporting cannot repair a biased experimental design after the fact.

### Project-specific protocol-v2 decisions motivated by these sources

- Phase-A principal learning budget is actual agent–environment interactions, not equal episode count or equal optimizer updates.
- Each retained method receives a predeclared, comparable tuning opportunity on tuning-only evidence.
- Standardized no-learning evaluation probes are used to separate policy quality from exploratory/stochastic training return.
- Root/seed is the independent randomization unit; episodes and checkpoints are nested repeated observations.
- Final environment selection, primary metrics, contrasts and tuning rules are frozen before confirmatory outcomes are inspected.

### Do not overclaim

Neither source prescribes the final number of roots, final GridWorld size, exact training budget, one universal CI procedure, or which method should win this thesis.

## 2. Time limits, termination and truncation

### Canonical source

- `SRC-69D02D7E25` — Pardo et al., *Time Limits in Reinforcement Learning* (ICML, 2018).

### Thesis-safe supported claims

- A time limit can be an artificial interaction cutoff rather than a true terminal state of the underlying task.
- Treating such a cutoff as terminal can produce incorrect learning targets when the task is conceptually continuing beyond the cutoff.
- Time-limit handling must therefore distinguish task termination from administrative truncation.

### Project-specific protocol-v2 decisions motivated by this source

- `max_steps` is an administrative truncation unless the scenario explicitly defines a true finite-horizon terminal objective.
- Value-learning methods bootstrap across administrative truncation according to the common task semantics rather than silently forcing terminal value zero.
- `terminated` and `truncated` remain separate fields throughout environment, adapter, checkpoint and analysis layers.

### Historical-writing use

The earlier v1.x option `bootstrap_on_truncation` can be reported as a historical implementation/protocol choice. It must not be rewritten retrospectively. Protocol-v2 makes the semantics explicit and common across methods.

### Do not overclaim

Pardo et al. do not determine this thesis's numerical horizon, training budget, post-change window or episode length.

## 3. Q-Learning and SARSA as tabular mechanism contrasts

### Canonical sources

- `SRC-701E163AC8` — Sutton & Barto, *Reinforcement Learning: An Introduction*, second edition.
- `SRC-D52DF7B9A4` — focused Q-learning / TD-control material already retained in the bibliography.

### Thesis-safe supported claims

- Q-learning is an off-policy TD-control method whose one-step target uses a greedy maximum over next-state action values.
- SARSA is an on-policy TD-control method whose one-step target uses the next action selected by the behavior policy.
- Under exploratory behavior, this target distinction can produce materially different learning behavior.

### Project-specific interpretation

Q-Learning and SARSA are retained because they provide a low-complexity, interpretable off-policy/on-policy tabular contrast under exactly the same agent-visible task semantics. Their inclusion is not a claim that either is universally more robust or more resilient.

## 4. DQN and experience replay

### Canonical sources

- `SRC-32A0866AF8` — canonical DQN foundation record.
- `SRC-CBA29E303A` — Fedus et al., *Revisiting Fundamentals of Experience Replay* (ICML, 2020).

### Thesis-safe supported claims

- DQN combines neural value approximation with replay and a target-network mechanism to stabilize value-learning updates.
- Replay-buffer size, replay ratio/update frequency and related replay choices can materially affect deep-RL learning behavior; replay is not a transparent storage implementation detail.

### Protocol-v2 consequences

A scientific DQN configuration records replay capacity, sampling/update semantics, target-network update semantics, exploration schedule and architecture. A continuation-capable checkpoint must preserve at least the online network, target network, optimizer, replay contents and logical state, exploration/counter state, preprocessing state where applicable, and relevant RNG state.

### Adaptation interpretation

Keeping pre-change replay in a normal Continual DQN branch is part of ordinary continued DQN training. Clearing, reweighting or selectively replaying memory after a change would be a distinct intervention and must not be silently introduced as checkpoint handling.

### Do not overclaim

Fedus et al. do not prove that a particular replay-buffer size is optimal for this GridWorld, nor that replay necessarily improves or harms adaptation after the thesis's action remapping. Those are empirical questions.

## 5. PPO and implementation sensitivity

### Canonical sources

- `SRC-CD5F67F3E6` — Schulman et al., *Proximal Policy Optimization Algorithms* (2017).
- `SRC-5D0E7E5BD7` — Engstrom et al., *Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO* (2020).

### Thesis-safe supported claims

- PPO is an on-policy policy-optimization method using a clipped surrogate objective to limit excessively large policy updates.
- PPO's published algorithmic description does not uniquely determine observed performance: implementation-level choices can materially affect results.

### Protocol-v2 consequences

The PPO adapter/configuration must expose and record the implementation details that affect the learning process, including rollout size, minibatch/update epochs, advantage/value settings, optimizer configuration, network architecture and library/version provenance. A continuation checkpoint must include policy/value parameters, optimizer and schedule/counter state, normalization/preprocessing state where applicable, and relevant RNG state. Checkpoints used to fork protocol-v2 branches are taken only at a complete rollout/update boundary.

### Do not overclaim

PPO clipping is not an environmental-robustness guarantee. The literature does not imply that PPO is intrinsically resilient to the thesis's changepoint conditions.

## 6. Dyna, Dyna-Q and Dyna-Q+

### Canonical sources

- `SRC-F6BD3A6B18` — Sutton, *Integrated Modeling and Control Based on Reinforcement Learning and Dynamic Programming*.
- `SRC-701E163AC8` — Sutton & Barto, Dyna and changing-environment treatment.

### Thesis-safe supported claims

- Dyna integrates direct learning from real experience with learning a model and using model-generated experience for planning updates.
- In changing environments, an outdated learned model can make planning propagate stale information until affected state-action pairs are revisited.
- Dyna-Q+ adds directed re-exploration based on how long actions have gone untried, providing a mechanism for rediscovering changed consequences.

### Protocol-v2 interpretation

Dyna-Q+ supplies a mechanism-level comparator that is more distinct from PPO than another closely related actor-critic baseline would be. Plain Dyna-Q is best treated as a targeted planning-versus-recency ablation rather than automatically multiplying the full final experiment matrix.

A scientific Dyna-Q+ checkpoint preserves Q values, empirical model, planning state, recency state/counters and both action-selection/planning RNG state. Resetting the model or recency information after a changepoint is a separate intervention.

### Do not overclaim

Dyna-Q+ is not guaranteed to dominate model-free methods. Directed re-exploration can have an immediate reward cost and its benefit depends on the structure and detectability of the change.

## 7. Non-stationarity, adaptation and continual-learning threats

### Canonical sources

- `SRC-660560956D` — Steinparz et al., non-stationary RL / re-exploration evidence already retained.
- `SRC-4C34DF3E17` — Dohare et al., long-horizon deep-RL plasticity-loss evidence.
- `SRC-46CF36BC1E` — Nikishin et al., *The Primacy Bias in Deep Reinforcement Learning*.

### Thesis-safe supported claims

- Distribution/environment changes can invalidate learned value estimates, policies or learned models and create a need for renewed exploration or adaptation.
- Standard deep-RL learners can suffer interference, primacy effects or loss of plasticity during extended learning; continued optimization does not guarantee indefinitely preserved ability to adapt.
- Replay/history can interact with non-stationarity in method-specific ways.

### Protocol-v2 interpretation

The primary continual branch is intentionally ordinary method-native continued training. Specialized continual-learning remedies are not added by default, because doing so would change the research question from “how do these standard mechanisms behave under change?” to “which continual-learning intervention works best?”. Plasticity/primacy literature is therefore used primarily as a threat-to-validity and interpretation framework.

### Do not overclaim

Dohare or Nikishin do not predict that PPO/DQN will fail in this thesis's small GridWorld. Their tasks and timescales differ substantially. Use them to justify monitoring and cautious interpretation, not to predeclare a winner or failure mode.

## 8. Phase-A / Phase-B experimental estimands

### Literature-supported ingredients

The fairness/randomization principles above are supported primarily by `SRC-4ED8B918E3` and `SRC-8D4F62D85D`.

### Project-specific causal-isolation design

The exact four-branch protocol is a thesis design, not a published universal standard:

1. **FN** — Frozen, matched nominal reference.
2. **FD** — Frozen, disturbed/change condition.
3. **AN** — Adaptive/Continual, matched nominal reference.
4. **AD** — Adaptive/Continual, disturbed/change condition.

All four branches originate from the method/root's own Phase-A trained state after a shared no-learning prefix and an exact branch point. Adaptive learning begins only after the predeclared boundary.

The primary adaptation estimand is a matched difference-in-differences-style quantity comparing the disturbed-vs-reference change under Adaptive against the same disturbed-vs-reference change under Frozen. This isolates adaptation benefit from ordinary continued-learning drift and from nominal branch drift more cleanly than `AD - FD` alone.

This construction must be described as **our predeclared experimental design**, motivated by causal-isolation/fair-comparison principles. Do not cite a source as though it prescribed these exact four branches.

## 9. Resilience metrics and statistical writing

### Supported framing

Use component outcomes rather than collapsing resilience into one opaque score:

- immediate degradation/resistance;
- cumulative post-change deficit relative to the matched same-regime nominal reference;
- terminal/post-change performance or terminal gap;
- recovery/non-recovery as secondary/sensitivity information;
- computation/runtime reported separately from task performance.

### Independent unit and uncertainty

Root/run is the independent randomization unit. Layouts can be paired/blocked repeated structure within a root according to the frozen aggregation rule. Episodes/checkpoints are not independent replicates.

Primary reporting should emphasize effect estimates and 95% intervals. The current project candidate for root-level paired/DiD mean effects is a Student-t interval, with root-level resampling/robust sensitivity checks. The exact final procedure and root count remain T-527 decisions based on non-final variance/precision evidence.

### Important provenance rule

The project's synthetic coverage stress test is **internal methodological validation**, not an external bibliographic result. It can be described in the methodology/reproducibility section as a protocol-design check, but it must not be attributed to Patterson, Henderson or another source.

## 10. GridWorld scope and environment-selection writing

GridWorld is the controlled testbed, not the thesis's claimed universal environment distribution. The existing project-owned configurable engine is retained because it already exposes the required action-remapping, action-failure and observation-corruption mechanisms while keeping evaluator truth separate from delivered observations.

The final complexity level is selected from a small predeclared ordered ladder using only non-final feasibility/discrimination criteria: avoid a universally trivial ceiling, avoid a universally unsolved floor, preserve the information contract, and remain feasible on the validated thesis machine. The environment must not be chosen because it produces a preferred method ranking.

Claims from the final study must remain scoped to the tested GridWorld family and perturbation definitions unless explicitly supported by broader evidence.

## 11. Uncertainty-condition claim boundaries

The thesis should keep three uncertainty mechanisms conceptually separate:

- **persistent action remapping**: abrupt persistent change in action/transition semantics; primary adaptation condition;
- **action-execution failure**: stochastic actuation uncertainty; robustness diagnostic;
- **observation corruption**: perceptual/information uncertainty and potentially partial-observability-like ambiguity; supporting diagnostic.

Observation-corruption severity requires both occurrence probability and corruption support/magnitude. These conditions must not be pooled into one generic “uncertainty” score or interpreted as interchangeable evidence.

## 12. Representation fairness

The fair-information requirement is semantic rather than data-structure identity. Tabular methods may consume a discrete state representation such as `(x, y)`, while neural methods may receive a deterministic vector/one-hot encoding of exactly the same agent-visible information. Neural methods must not receive pixels, hidden obstacle maps, evaluator truth, true pre-corruption state or explicit change indicators unavailable to tabular methods.

This is a project fairness rule motivated by the empirical-design literature; it should not be presented as a theorem from one source.

## 13. Historical v1.x evidence

Protocol-v1.0 and candidate-v1.1 evidence remain separately reportable historical/project evidence. They must not be numerically pooled with protocol-v2 because training provenance, method set, estimands and experimental contracts differ.

Useful writing roles:

- v1.0: foundational project evidence and initial validated resilience mechanism study;
- v1.1: auditable non-final adaptation-mechanism design history and motivation for protocol-v2 redesign;
- R0: historical negative/diagnostic result for the particular robust-planning construction, not a universal rejection of robust RL.

## 14. Threats-to-validity map for later writing

### Internal validity

- unequal tuning opportunity;
- checkpoint branches that do not start from identical scientific state;
- hidden information leakage;
- stale replay/model state being reset implicitly;
- termination/truncation confusion;
- post-hoc environment or metric selection.

### Construct validity

- interpreting training return as learned-policy quality;
- combining resistance, recovery and terminal performance into one score;
- calling PPO clipping “robustness”;
- calling any continued-learning branch a specialized continual-learning method;
- treating all three uncertainty mechanisms as the same construct.

### Statistical conclusion validity

- treating episodes/layouts as independent roots;
- best-seed selection;
- underpowered cross-method rankings;
- unbounded families of post-hoc contrasts;
- using a CI/bootstrap merely because it is conventional rather than because it fits the root-level estimand.

### External validity

- single controlled GridWorld family;
- compact CPU-feasible neural architectures;
- specific abrupt persistent action remapping rather than every kind of non-stationarity;
- no claim that observed ranking transfers to robotics, continuous control, Atari or large-scale agent systems.

### Reproducibility validity

- library/version and implementation-detail sensitivity (`SRC-5D0E7E5BD7`);
- incomplete deep-RL checkpoints;
- unrecorded replay/rollout/optimizer state;
- unrecorded RNG/state provenance;
- machine-dependent performance claims made from hosted CI rather than the validated Windows thesis machine.

## 15. Citation-ready source shortlist by likely thesis section

### Reinforcement-learning foundations / methods
- `SRC-701E163AC8` — RL/TD/Q/SARSA/Dyna foundations.
- `SRC-32A0866AF8` — DQN foundation.
- `SRC-CD5F67F3E6` — PPO foundation.

### Methodology / fair empirical comparison
- `SRC-4ED8B918E3` — empirical design, experience budget, tuning fairness, variation.
- `SRC-8D4F62D85D` — reproducibility, hyperparameters, random seeds, deep-RL reporting sensitivity.
- `SRC-69D02D7E25` — time limits and truncation semantics.
- `SRC-5D0E7E5BD7` — implementation sensitivity in policy-gradient methods.
- `SRC-CBA29E303A` — experience-replay design sensitivity.

### Non-stationarity / continual adaptation / threats
- `SRC-660560956D` — non-stationarity and re-exploration context.
- `SRC-4C34DF3E17` — plasticity loss in long-horizon deep RL.
- `SRC-46CF36BC1E` — primacy bias in deep RL.

## 16. Writing rule

For every methodological statement in the future thesis draft, classify it before writing:

- **LITERATURE CLAIM** — cite the corresponding canonical source/evidence file and stay inside its claim boundary.
- **PROTOCOL DECISION** — explain that this thesis predeclares the design choice and cite literature only for the principles motivating it.
- **PROJECT EVIDENCE** — cite/identify the immutable experimental artifact or historical protocol, not external literature.
- **RESULT CLAIM** — write only after the relevant protocol-v2 final evidence exists and has passed the acceptance gates.

This classification is the main safeguard against converting literature motivation into false claims that a source “proved” the exact protocol used by this thesis.