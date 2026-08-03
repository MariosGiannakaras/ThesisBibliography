---
κωδικός: SRC-4D2B7DDC38
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Distributionally Robust Reinforcement Learning with Interactive Data Collection: Fundamental Hardness and Near-Optimal Algorithms

## E1 — Interactive robust RL can be fundamentally hard under support shift
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section 3
- **Claim:** Without additional assumptions, sample-efficient robust learning from interaction with only the training environment can be impossible when testing environments contain important states or transitions outside the support accessible during training.
- **Status:** verified

### Faithful paraphrase
Lu et al. show a fundamental gap between robust RL with interactive training data and settings that provide a generative model or an offline dataset with deployment coverage. If states that matter under plausible test dynamics cannot be reached in the training MDP, no amount of ordinary exploration in that training environment can directly supply evidence about them. Their lower bound formalizes this curse of support shift.

### Thesis use
Separate in-support parameter variation from low-probability reachable transitions and genuinely out-of-support structural shifts when interpreting failures.

### Citation
Lu et al. (2024/2026 revision), Abstract, Introduction, and Section 3.

## E2 — More exploration cannot reveal states forbidden by the training dynamics
- **Type:** faithful paraphrase
- **Location:** Introduction
- **Claim:** Sophisticated exploration does not solve a coverage gap when crucial test states are structurally inaccessible under the training environment.
- **Status:** verified

### Faithful paraphrase
The paper emphasizes that interactive data collection cannot force the training environment to generate a transition or state that its dynamics never permit. By contrast, a generative-model oracle can query arbitrary state–action pairs, and a suitably covered offline dataset may already contain deployment-relevant transitions.

### Thesis use
Do not interpret failure on a held-out structural layout as weak exploration unless the relevant post-shift states were actually reachable during training.

### Citation
Lu et al. (2024/2026 revision), Introduction.

## E3 — Data-access assumptions determine what robustness guarantees are comparable
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** Generative-model access, well-covered offline data, and ordinary interaction with a training environment are materially different information regimes.
- **Status:** verified

### Faithful paraphrase
The authors explicitly distinguish a generative model that can return a next-state sample for any queried state–action pair from an ordinary simulator/training environment whose data distribution is induced by the learner's policy. They also distinguish both from a pre-collected offline dataset with favorable coverage.

### Thesis use
Track simulator queries, offline samples, and ordinary interactions separately and reject algorithm rankings built on unmatched coverage privileges.

### Citation
Lu et al. (2024/2026 revision), Introduction.

## E4 — Near-optimal learning requires an additional structural assumption in the TV-robust case
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 4.1
- **Claim:** The paper restores tractability for a subclass of total-variation robust MDPs using a vanishing-minimal-value assumption that removes the support-shift pathology.
- **Status:** verified

### Faithful paraphrase
After establishing the general impossibility result, the authors identify a restricted class in which the minimal value of the optimal robust value function vanishes. Under this assumption for a total-variation ambiguity set, they design OPROVI-TV and derive near-optimal sample-complexity guarantees.

### Context and limits
This assumption is part of the theorem. The resulting guarantee should not be presented as a generic solution to arbitrary sim-to-real or structural-shift problems.

### Thesis use
Use the theorem primarily as a warning that robust guarantees are conditional on coverage and structural assumptions.

### Citation
Lu et al. (2024/2026 revision), Abstract and Section 4.1.

## E5 — Robustness to an ambiguity set remains distinct from temporal recovery
- **Type:** scope synthesis grounded in the formulation
- **Location:** Sections 1–4
- **Claim:** The paper studies worst-case performance over a predefined family of test environments and online data collection in the training environment; it does not define an unknown deployment changepoint followed by detection and relearning.
- **Status:** verified

### Thesis use
Classify this source under `robust_model_shift/coverage`, not as direct evidence for detector-triggered resilience.

### Citation
Lu et al. (2024/2026 revision), overall formulation.