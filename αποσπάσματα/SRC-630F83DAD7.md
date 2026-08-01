---
κωδικός: SRC-630F83DAD7
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Leveraging Procedural Generation to Benchmark Reinforcement Learning

## E1 — Procedural diversity is part of the benchmark distribution
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section 2
- **Claim:** Procgen uses procedurally generated level distributions so agents encounter substantial environment variation rather than repeatedly training on near-identical states.
- **Status:** verified

### Faithful paraphrase
Cobbe et al. design Procgen so layout, entities, assets, and other task details vary across generated levels. The resulting diversity is an environment property used to train and evaluate generalization; it is not merely an augmentation applied inside the agent.

### Thesis use
Version GridWorld map families and environment-generation seeds as part of the benchmark definition.

### Citation
Cobbe et al. (2020), Abstract, Introduction, and Section 2.

## E2 — Generalization uses held-out levels
- **Type:** faithful paraphrase
- **Location:** Section 2.2; Section 3.3
- **Claim:** For generalization evaluation, agents train on a finite set of generated levels and are tested on held-out levels drawn from the environment distribution.
- **Status:** verified

### Faithful paraphrase
The benchmark separates the levels used during training from those used for zero-shot testing. This makes test performance an estimate of generalization beyond memorized training trajectories rather than another measurement on the same finite set.

### Thesis use
Keep train, validation/tuning, and final test map seeds disjoint, and separate those splits from changepoint schedules.

### Citation
Cobbe et al. (2020), Sections 2.2 and 3.3.

## E3 — Large finite training sets can still be overfit
- **Type:** faithful paraphrase
- **Location:** Introduction; Section 3.1; Figure 2
- **Claim:** Deep RL agents can exhibit substantial train–test gaps even after training on many distinct levels.
- **Status:** verified

### Faithful paraphrase
The paper varies training-set size from hundreds to many thousands of levels and shows that generalization gaps can remain large. The result warns that strong training performance on a large finite collection is not sufficient evidence that an agent learned structure that transfers to unseen levels.

### Thesis use
Retain held-out map evaluation even if the training generator produces many layouts.

### Citation
Cobbe et al. (2020), Section 3.1 and Figure 2.

## E4 — Procedural generation does not guarantee solvability
- **Type:** faithful paraphrase
- **Location:** Section 2.1, Level Solvability
- **Claim:** Procgen aims to generate solvable levels but does not provide an absolute solvability guarantee.
- **Status:** verified

### Faithful paraphrase
The authors state that their generators strive to make all levels solvable and estimate that more than 99% are solvable, while acknowledging that solvability is not strictly guaranteed.

### Thesis use
Run explicit reachability/solvability validation on every generated or structurally perturbed GridWorld used in an experiment.

### Citation
Cobbe et al. (2020), Section 2.1.

## E5 — Fixed-sequence competence can create an illusion of progress
- **Type:** faithful paraphrase
- **Location:** Section 3.2; Figure 3
- **Claim:** Agents trained on a deterministic level sequence can become competent on the early training levels while performing poorly when the sequence is randomized at test time.
- **Status:** verified

### Thesis use
Use held-out randomized layouts and avoid interpreting repeated success on a fixed route or fixed layout sequence as generalization.

### Citation
Cobbe et al. (2020), Section 3.2 and Figure 3.

## E6 — Zero-shot generalization is not online recovery
- **Type:** scope synthesis grounded in the benchmark
- **Location:** Overall generalization protocol
- **Claim:** Procgen evaluates performance on unseen levels after training; it does not introduce a within-run unknown changepoint and then measure detection and relearning.
- **Status:** verified

### Thesis use
Run frozen zero-shot testing separately from any later online adaptation phase.

### Citation
Cobbe et al. (2020), overall protocol.