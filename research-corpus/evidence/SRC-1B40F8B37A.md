---
κωδικός: SRC-1B40F8B37A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Collaboration Promotes Group Resilience in Multi-Agent RL

## E1 — Resilience is evaluated under bounded environmental perturbations

- **Type:** faithful paraphrase
- **Location:** Section 3, “Measuring Group Resilience”
- **Claim:** The paper defines resilience relative to perturbed environments whose distance from a reference MDP is bounded by a user-specified severity limit.
- **Status:** verified

### Faithful paraphrase

Shraga et al. introduce a distance `delta(M,M')` between the reference environment and a perturbed environment and a bound `K` that limits which perturbations are included in the resilience assessment. Resilience then asks whether performance in those bounded perturbations retains a specified fraction of reference performance.

### Context and limits

The distance metric is part of the problem definition and is not domain-neutral. Different distances can assign different severity ordering to the same physical changes.

### Thesis use

Define perturbation severity explicitly and publish performance-versus-severity curves rather than a single undifferentiated resilience score.

### Citation

Shraga et al. (2025), Section 3.

## E2 — Relative-to-optimum and relative-to-origin normalization answer different questions

- **Type:** faithful paraphrase
- **Location:** Definitions 1–3
- **Claim:** Resilience can be normalized against each perturbed environment's achievable optimum or against the same policy/group's original utility.
- **Status:** verified

### Faithful paraphrase

The relative-to-optimum definition accounts for the fact that a perturbation can change the best utility achievable in the environment, whereas the relative-to-origin definition compares perturbed performance directly with the group's performance before the perturbation. The latter is easier to compute when the new optimum is unknown but measures retention rather than optimality in the changed regime.

### Thesis use

Report retained-performance ratios separately from any score normalized by a regime-specific optimum or oracle.

### Citation

Shraga et al. (2025), Definitions 1–3.

## E3 — Low baseline performance can make a ratio-based resilience score misleading

- **Type:** faithful paraphrase
- **Location:** Discussion after Definitions 2–3
- **Claim:** A poor or no-op policy can appear highly resilient if resilience is measured only as the fraction of its own already-low baseline performance that it retains.
- **Status:** verified

### Faithful paraphrase

The authors explicitly note that relative-to-origin definitions can reward a policy that starts from weak performance because such a policy has little utility to lose under perturbation. They therefore motivate complementary baseline normalization when the analysis requires meaningful task competence as well as stability.

### Thesis use

Every resilience ratio must be accompanied by absolute pre-change and post-change performance and, where feasible, a gap or regret relative to the regime-specific optimum.

### Citation

Shraga et al. (2025), discussion following Definitions 2–3.

## E4 — Transition, reward, and initial-state perturbations are distinct atomic changes

- **Type:** faithful paraphrase
- **Location:** Section 3.1, Definitions 4–6
- **Claim:** The paper formalizes separate perturbations of transition dynamics, reward values, and the initial state.
- **Status:** verified

### Faithful paraphrase

An atomic transition perturbation changes the next-state distribution for a selected state–action pair, a reward perturbation changes its reward, and an initial-state perturbation changes where the process begins. These operations alter different components of the MDP and can have different behavioral consequences.

### Thesis use

Do not collapse reward, transition, and initial-state changes into one generic “uncertainty” category.

### Citation

Shraga et al. (2025), Section 3.1, Definitions 4–6.

## E5 — Expected resilience depends on the perturbation distribution

- **Type:** faithful paraphrase
- **Location:** Definition 3
- **Claim:** When resilience is defined in expectation, the sampling distribution over bounded perturbations is part of the benchmark definition.
- **Status:** verified

### Faithful paraphrase

The resilience-in-expectation formulation averages utility over perturbed MDPs sampled from a distribution `Psi` conditioned on remaining within the severity bound. Consequently, changing the perturbation generator or its sampling probabilities changes the quantity being estimated.

### Thesis use

Record the perturbation generator, seed distribution, and severity-sampling policy used for every expected-resilience statistic.

### Citation

Shraga et al. (2025), Definition 3.

## E6 — The empirical collaboration claim is outside the single-agent thesis scope

- **Type:** scope inference grounded in the paper
- **Location:** Abstract; Sections 1–5
- **Claim:** The paper's empirical contribution concerns collaboration and group resilience in MARL; only its formal metric insights transfer directly to a single-agent benchmark.
- **Status:** verified

### Thesis use

Use this source for perturbation-distance and resilience-normalization design, not as evidence that collaboration improves single-agent resilience.

### Citation

Shraga et al. (2025), overall scope.
