---
κωδικός: SRC-B88D51FA3F
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Efficient Adaptation of Reinforcement Learning Agents to Sudden Environmental Change

## Evidence E1 — Sudden novelty requires post-deployment adaptation from new experience
- **Type:** faithful paraphrase
- **Location:** Summary; Chapter 1, Section 1.1; Chapter 2, Sections 2.2.2–2.2.3
- **Claim:** The dissertation studies agents that encounter previously unseen environmental novelty after initial learning and must adapt online from interaction with the changed environment.
- **Thesis use:** problem definition; sudden-change protocol
- **Topics:** novelty; online adaptation; environmental change
- **Status:** verified

### Faithful paraphrase
The work treats novelty as a change that was not part of the agent's original learning experience and that alters the task the agent must solve. Efficient response therefore requires collecting new post-change experience and using it to update behavior rather than assuming that train-time randomization already covered the new regime.

### Limitation
This framing is most directly aligned with sudden novelty. It should not be used as a universal definition for every form of gradual drift or independent observation noise.

## Evidence E2 — NovGrid isolates hidden changes in task semantics
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Sections 3.1–3.3, pp. 31–38
- **Claim:** The dissertation uses controlled novelty environments in which task-relevant rules can change without an explicit novelty label being given to the agent.
- **Thesis use:** benchmark design
- **Topics:** GridWorld; hidden novelty; rule change
- **Status:** verified

### Faithful paraphrase
Novelty MiniGrid is designed so that an agent can face changes in the meaning or consequences of environment elements and must discover those changes through interaction. This supports controlled experiments in which pre-change competence and post-change response can be measured separately while keeping the environment simple enough to inspect.

### Limitation
The benchmark's simplicity improves experimental control but does not make it representative of all real-world changes.

## Evidence E3 — Adaptive efficiency is conditional on successful convergence
- **Type:** faithful paraphrase
- **Location:** Chapter 4, Table 4.2, p. 51
- **Claim:** Adaptive efficiency measures interaction steps from the beginning of the novel task until convergence on the second task, and is calculated only for runs that converge on both tasks.
- **Thesis use:** recovery/adaptation metrics
- **Topics:** adaptation time; convergence; survivorship bias
- **Status:** verified

### Faithful paraphrase
Lower adaptive-efficiency values indicate faster adaptation after novelty, but the metric excludes runs that fail to converge on either task. A time-to-recovery number is therefore incomplete unless the corresponding success/convergence fraction is reported as well.

## Evidence E4 — Transfer AUC summarizes the post-change trajectory but has conditioning requirements
- **Type:** faithful paraphrase
- **Location:** Chapter 4, Table 4.3, p. 52
- **Claim:** The transfer area-under-the-curve metric combines final performance on the first task with the reward trajectory on the second task and is reported only for runs that converged on the first task.
- **Thesis use:** integrated recovery-curve metric
- **Topics:** AUC; transfer; adaptation trajectory
- **Status:** verified

### Faithful paraphrase
Transfer AUC rewards both competence before the change and strong learning performance after transfer. Because it depends on reward scale, horizon, and inclusion criteria, comparisons require a shared protocol and explicit reporting of excluded or failed runs.

## Evidence E5 — Exploration effectiveness depends on the novelty/task
- **Type:** faithful paraphrase
- **Location:** Chapter 4, Sections 4.3–4.5, including Figures 4.3–4.5
- **Claim:** The experiments do not support a universal ranking of exploration methods across novelty tasks.
- **Thesis use:** exploration ablations
- **Topics:** exploration; novelty type; adaptation
- **Status:** verified

### Faithful paraphrase
Exploration strategies that adapt effectively in one transfer setting are not guaranteed to dominate in another. The relative benefit depends on the environment and the novelty being encountered, so exploration mechanisms should be evaluated across more than one shift family.

## Evidence E6 — Knowledge preservation and targeted experience are complementary adaptation concerns
- **Type:** faithful paraphrase
- **Location:** Summary; Chapters 5–7; Conclusions
- **Claim:** The dissertation studies both how experience is selected after change and how useful prior structure can be preserved while the agent adapts.
- **Thesis use:** mechanism decomposition
- **Topics:** retention; exploration; adaptation; model update
- **Status:** verified

### Faithful paraphrase
The dissertation's later contributions separate several adaptation concerns: selecting informative experience for different learning objectives, detecting novelty in learned world models, adapting a policy after novelty, and preserving reusable knowledge in structured representations. These mechanisms should not be collapsed into a single generic notion of resilience.

### Limitation
The proposed model-based and neuro-symbolic methods are substantially more complex than the resource-aware tabular core of the thesis and are not mandatory implementation baselines.

## Avoid overclaiming
This source does not establish that one exploration method is universally best, that convergence-only adaptation metrics are sufficient, or that the dissertation's deep/model-based architectures are necessary for a lightweight GridWorld study.
