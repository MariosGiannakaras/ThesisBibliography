---
κωδικός: SRC-0FD9BE81AC
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-09-05"
source-language: en
---

# Evidence — Continual Reinforcement Learning by Planning with Online World Models

## E1 — Continual RL requires learning new tasks without forgetting old skills

- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1, Introduction
- **Claim:** The paper frames continual reinforcement learning as sequential task learning and identifies catastrophic forgetting as a central obstacle.
- **Status:** verified

### Faithful paraphrase

Liu et al. study continual reinforcement learning in which tasks are presented sequentially and the agent must keep evolving through interaction. They identify catastrophic forgetting—loss of competence on earlier tasks while learning later ones—as a central difficulty, so evaluation cannot be limited to performance on only the newest task.

### Context and limits

This is a multi-task continual-learning setting. The thesis uses a narrower post-change adaptation/recovery protocol rather than a long sequence of tasks repeatedly evaluated for forgetting and transfer.

### Thesis use

Use in Related Work and scope limitations to distinguish post-change adaptation from full continual-RL evaluation.

### Citation

Liu et al. (2025), Abstract and Section 1.

## E2 — Shared dynamics knowledge can be separated from task-specific reward and planning

- **Type:** faithful paraphrase
- **Location:** Section 3.2; Sections 4.1 and 4.3
- **Claim:** The proposed Online Agent maintains an incrementally learned world-dynamics model and derives actions by planning with MPC/CEM, while tasks are specified through reward functions.
- **Status:** verified

### Faithful paraphrase

The Online Agent treats world dynamics as reusable knowledge shared across tasks. It learns a shallow Follow-The-Leader world model incrementally from state-action transitions and constructs behavior at decision time through model predictive control with cross-entropy-method planning. Different tasks can therefore change the reward objective while reusing the same dynamics model.

### Context and limits

This architecture is not tabular Dyna-Q or Dyna-Q+. Dyna-style planning commonly uses learned-model transitions to produce additional learning updates, whereas Liu et al. plan directly through the current learned model with MPC/CEM.

### Thesis use

Support a careful conceptual comparison between model-based continual planning and the thesis Dyna-Q+ comparator without implying algorithmic equivalence.

### Citation

Liu et al. (2025), Sections 3.2, 4.1 and 4.3.

## E3 — The no-regret result is specific to the sparse FTL world-model construction

- **Type:** faithful paraphrase
- **Location:** Section 4.2, Theorem 1; Appendix E.3.2
- **Claim:** The paper proves a sublinear regret bound for its sparse online world-model update under stated assumptions.
- **Status:** verified

### Faithful paraphrase

The theoretical result applies to the paper's sparse Follow-The-Leader model update. Under assumptions concerning feature-map stabilization, bounded quantities and the sparsity/update parameter, Theorem 1 bounds cumulative model-learning regret sublinearly in time. The guarantee therefore concerns this particular online model-learning construction rather than model-based RL in general.

### Context and limits

The assumptions and model class must accompany any mention of the guarantee. It is not evidence that every learned world model, MPC agent, Dyna implementation or thesis agent is immune to forgetting.

### Thesis use

Use only when explaining why the proposed Online Agent is designed as a persistent online model; do not transfer the guarantee to thesis algorithms.

### Citation

Liu et al. (2025), Section 4.2, Theorem 1, with proof in Appendix E.3.2.

## E4 — Continual Bench intentionally uses unified dynamics and reward-defined task switches

- **Type:** faithful paraphrase
- **Location:** Figure 3; Section 6.1; Appendix B
- **Claim:** Continual Bench contains six manipulation tasks sharing unified physical dynamics and common state/action structure; the reward changes at task switches.
- **Status:** verified

### Faithful paraphrase

Continual Bench is built from six MuJoCo/Meta-World manipulation tasks that share one world-dynamics representation. In the reported sequence, the reward function changes when the active task changes, while task-boundary information is not supplied to world-model learning unless a comparison method explicitly requires it. Appendix B reports a 26-dimensional state and 4-dimensional action representation and episodic tasks of at most 500 steps.

### Context and limits

This non-stationarity is mainly a sequence of reward-defined objectives under shared dynamics. It is materially different from the thesis's persistent action-semantic remapping, stochastic no-op action failure and observation corruption.

### Thesis use

Support the taxonomy of distinct non-stationarity regimes and explain why results from one regime do not directly predict recovery in another.

### Citation

Liu et al. (2025), Figure 3, Section 6.1 and Appendix B.

## E5 — The empirical advantage is demonstrated within a matched model-planning benchmark, not universally

- **Type:** faithful paraphrase
- **Location:** Sections 6.3–6.4; Figures 5–6; Table 1
- **Claim:** In Continual Bench, OA retains prior-task performance better than several deep world-model continual-learning baselines and attains the lowest reported regret among the compared methods under the paper's framework.
- **Status:** verified

### Faithful paraphrase

Under a common model-based planning setup using learned world models and CEM/MPC, the paper reports that fine-tuning and several continual-learning mitigations lose performance on earlier tasks to differing degrees, while OA retains high performance across previously seen tasks. Table 1 reports OA with 72.93% average performance and 27.62% regret; the deep-model Perfect Memory comparator reaches 73.09% average performance and 30.95% regret.

### Context and limits

These numbers belong only to Continual Bench and the compared implementations. The result does not establish a general advantage of model-based RL, world models, Dyna-Q+ or any thesis method across arbitrary non-stationary environments.

### Thesis use

Use as recent primary related-work evidence that model retention and planning architecture materially affect continual-learning behavior, while preserving the benchmark boundary.

### Citation

Liu et al. (2025), Sections 6.3–6.4, Figures 5–6 and Table 1.

## E6 — The authors state important representation, uncertainty, exploration and benchmark limits

- **Type:** faithful paraphrase
- **Location:** Appendix D, Limitations and Future Work
- **Claim:** The current method is limited to moderate-dimensional state observations, does not represent world uncertainty, lacks explicit exploration in planning, and is evaluated in an episodic benchmark with task switches across episodes.
- **Status:** verified

### Faithful paraphrase

The authors explicitly limit the present Online Agent to moderate-dimensional state-based observations and note that its world model does not capture uncertainty. They also state that planning has no explicit exploration mechanism and that Continual Bench is episodic, with task switching between episodes rather than a reset-free lifelong stream.

### Context and limits

These limitations are especially important for thesis use because the thesis includes observation corruption and hidden persistent disturbances and does not assume a sequence of clearly separated reward-defined tasks.

### Thesis use

Use in Discussion/Future Work to delimit what recent online-world-model continual RL demonstrates and what remains outside both that paper and the present thesis.

### Citation

Liu et al. (2025), Appendix D.
