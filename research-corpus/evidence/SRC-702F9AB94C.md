---
κωδικός: SRC-702F9AB94C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Block Contextual MDPs for Continual Learning

## E1 — Structured non-stationarity can be represented by a changing latent context

- **Type:** faithful paraphrase
- **Location:** Sections 1 and 3, Definitions 1–3
- **Claim:** The BC-MDP framework maps a context to rewards, transition dynamics, and observations and uses changing context to represent related non-stationary tasks.
- **Status:** verified

### Faithful paraphrase

Sodhani et al. combine contextual MDPs with rich-observation block MDPs. A context identifies the reward and transition functions and may also determine the observation space. In the continual setting, the context changes without explicit task boundaries, producing non-stationarity across a related family of tasks.

### Context and limits

The paper focuses on task families with exploitable shared structure and smoothness assumptions rather than arbitrary changes to the state/action interface.

### Thesis use

Use `latent_context` as a distinct non-stationarity model and state whether context changes are expected to be related or smooth.

### Citation

Sodhani et al. (2022), Sections 1 and 3, Definitions 1–3.

## E2 — Generalization guarantees depend on context identifiability and task distance

- **Type:** faithful paraphrase
- **Location:** Section 4, Assumption 1 and Theorem 2
- **Claim:** The theory assumes a new context can be inferred from a bounded interaction history and that performance error grows with context-estimation error and distance from known tasks.
- **Status:** verified

### Faithful paraphrase

The framework assumes that a context encoder can estimate the active context from a fixed number of recent transition tuples. Its value-error bounds then depend on how closely that inferred context matches the true one and on a task metric constructed from reward and transition differences.

### Context and limits

A regime that is not identifiable from recent observations, or that lies far from learned contexts, falls outside the strongest guarantee.

### Thesis use

Make context identifiability and distance-to-library explicit assumptions for context-conditioned agents.

### Citation

Sodhani et al. (2022), Section 4, Assumption 1 and Theorem 2.

## E3 — ZeUS performs context inference without test-time parameter updates

- **Type:** faithful paraphrase
- **Location:** Section 5; Figure 1
- **Claim:** At evaluation time, ZeUS conditions a pretrained policy on context inferred from recent interaction history and does not update model parameters on the new task.
- **Status:** verified

### Faithful paraphrase

The context encoder summarizes the recent trajectory into a task representation and the policy acts conditioned on that representation. Adaptation occurs through online inference of the active context rather than gradient-based relearning of the policy or encoder.

### Context and limits

The representation and policy were learned in advance over a task family. This is context inference, not post-change parameter learning.

### Thesis use

Keep frozen-policy generalization, history-conditioned context inference, and online updating as separate agent categories.

### Citation

Sodhani et al. (2022), Section 5 and Figure 1.

## E4 — Interpolation and extrapolation require separate reporting

- **Type:** faithful paraphrase
- **Location:** Sections 6.1–6.3; Figures 2–3
- **Claim:** The experiments distinguish held-out contexts inside the training range from contexts outside that range.
- **Status:** verified

### Faithful paraphrase

For non-stationary dynamics, the study evaluates contexts both within and beyond parameter ranges used for training. Reward-task experiments use a different context setup, so success there cannot be interpreted as evidence for reward extrapolation outside the training range.

### Thesis use

Label results as interpolation, extrapolation, or structurally novel change rather than reporting one undifferentiated context-generalization score.

### Citation

Sodhani et al. (2022), Sections 6.1–6.3, Figures 2–3.

## E5 — Context representation should be evaluated with an ablation

- **Type:** faithful paraphrase
- **Location:** Sections 6.3–6.4; Figures 2–4
- **Claim:** The task-structured context-learning loss improves both held-out-task performance and alignment of learned context distances with task distances in the reported experiments.
- **Status:** verified

### Faithful paraphrase

ZeUS is compared with a version that removes the explicit context-structure loss. The full method performs better on held-out tasks and produces a context geometry more correlated with the underlying task metric in the studied task family.

### Context and limits

The reported correlation is task-specific and does not prove that a learned representation is universally causal or semantically correct.

### Thesis use

If a learned context representation is used, include a no-context-structure ablation or simpler explicit-context comparator.

### Citation

Sodhani et al. (2022), Sections 6.3–6.4, Figures 2–4.

## E6 — Performance degrades as evaluation contexts move away from the training distribution

- **Type:** faithful paraphrase
- **Location:** Section 7; Figure 5
- **Claim:** Even a structured context-inference method loses performance on increasingly distant OOD contexts.
- **Status:** verified

### Faithful paraphrase

The paper reports decreasing ZeUS performance as target contexts move farther beyond the range represented during training and notes practical dependence on informative reward or transition signals for distinguishing tasks.

### Thesis use

Evaluate performance as a function of context distance and include a regime that is absent from the context library or training range.

### Citation

Sodhani et al. (2022), Section 7 and Figure 5.
