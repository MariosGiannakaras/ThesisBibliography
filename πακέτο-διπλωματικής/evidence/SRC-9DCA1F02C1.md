---
κωδικός: SRC-9DCA1F02C1
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Leveraging Procedural Generation to Benchmark Reinforcement Learning

## Evidence E1 — Generalization requires distinct training and test level distributions
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1–2.2
- **Claim:** Procedural generation makes it possible to create distinct training and test level distributions and thereby measure whether a policy generalizes beyond the levels it experienced during training.
- **Thesis use:** train/test split design
- **Topics:** procedural generation; held-out levels; generalization
- **Status:** verified

### Faithful paraphrase
Procgen uses procedurally generated levels so that agents can be trained on one set or distribution of environments and evaluated on unseen levels. This makes memorization of specific trajectories distinguishable from learning behavior that transfers across the underlying level distribution.

## Evidence E2 — Sample efficiency and generalization use different protocols
- **Type:** faithful paraphrase
- **Location:** Section 2.2
- **Claim:** Procgen evaluates sample efficiency by training and testing on the full level distribution, whereas generalization is evaluated after training on a finite level set and testing on the broader unseen distribution.
- **Thesis use:** protocol separation
- **Topics:** sample efficiency; zero-shot generalization; test distribution
- **Status:** verified

### Faithful paraphrase
The benchmark deliberately separates two questions. For sample efficiency, the learner is exposed to the full distribution during training and evaluation. For generalization, training is restricted to a finite collection of levels and testing is performed on held-out levels. The two outcomes should therefore not be reported as if they measured the same property.

## Evidence E3 — Small training sets can produce severe overfitting
- **Type:** faithful paraphrase
- **Location:** Section 3.1
- **Claim:** Across most Procgen environments, agents substantially overfit small training sets and may require thousands of distinct levels before the train/test generalization gap narrows.
- **Thesis use:** memorization diagnostic
- **Topics:** overfitting; training-set size; held-out performance
- **Status:** verified

### Faithful paraphrase
When the number of training levels is small, performance on those levels can become much higher than performance on held-out levels. Increasing environment diversity can improve generalization and, in some cases, even improve training performance by forcing the agent to learn reusable structure.

## Evidence E4 — A deterministic level sequence can create an illusion of progress
- **Type:** faithful paraphrase
- **Location:** Section 3.2
- **Claim:** Agents trained on a fixed deterministic level sequence can appear competent on the early training sequence while performing poorly when the sequence is randomized at test time.
- **Thesis use:** leakage/memorization threat
- **Topics:** deterministic training sequence; test randomization; memorization
- **Status:** verified

### Faithful paraphrase
In the deterministic-level ablation, agents become effective on the first training levels, which can look like meaningful learning. Once deterministic sequencing is removed at test time, the results show that little of the underlying level distribution has actually been learned. This demonstrates why diversity is needed in both training and evaluation.

## Evidence E5 — Held-out zero-shot evaluation is a separate phase from online adaptation
- **Type:** faithful paraphrase
- **Location:** Section 3.3
- **Claim:** The recommended Procgen generalization benchmark evaluates zero-shot performance on unseen held-out levels after training on a fixed set of levels.
- **Thesis use:** phase ordering
- **Topics:** zero-shot test; held-out seeds; online adaptation boundary
- **Status:** verified

### Faithful paraphrase
Procgen's generalization protocol measures the trained policy on levels that were not used for training. No post-test learning is needed for that metric. If the thesis also studies online adaptation, the frozen zero-shot evaluation should therefore be completed before the agent is allowed to update on the shifted test environment.

### Limitation
The paper's recommended count of 500 training levels is benchmark-specific and should not be copied mechanically into a small GridWorld study.

## Evidence E6 — Compute and architecture can change measured performance
- **Type:** faithful paraphrase
- **Location:** Sections 2.2, 4 and 5
- **Claim:** Model size, computational budget, and algorithm implementation choices materially affect sample efficiency and generalization results.
- **Thesis use:** resource reporting; fair comparison
- **Topics:** model size; compute; algorithm comparison
- **Status:** verified

### Faithful paraphrase
The experiments show that larger architectures often improve both sample efficiency and generalization, and that PPO and Rainbow do not have a uniform ordering across all environments. Benchmark results therefore need to report resource and implementation conditions instead of implying an architecture-independent universal ranking.

## Avoid overclaiming
Procgen supports held-out generalization methodology; it does not by itself evaluate online recovery after an environmental changepoint. Generalization and adaptation must remain separate experimental phases.
