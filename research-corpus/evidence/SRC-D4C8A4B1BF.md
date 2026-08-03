---
κωδικός: SRC-D4C8A4B1BF
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Resilience and Resilient Systems of Artificial Intelligence: Taxonomy, Models and Methods

## E1 — Resilience is broader than robustness or fault tolerance alone
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.2, Research Gap
- **Claim:** The review argues that resilience should not be reduced to one isolated property such as adversarial robustness or fault tolerance.
- **Status:** verified

### Faithful paraphrase
Moskalenko et al. identify substantial inconsistency in how AI resilience is used across the literature. They argue that a resilient AI system should be able not only to withstand disturbance but also to detect or handle destructive influences, degrade in a controlled way when full performance cannot be maintained, restore lost functionality, and adapt to future changes.

### Thesis use
Use this review to support the conceptual boundary between static robustness and a broader temporal resilience process.

### Citation
Moskalenko et al. (2023), Abstract and Section 1.2.

## E2 — System resilience can be decomposed into preparation, absorption, recovery, and adaptation
- **Type:** faithful paraphrase
- **Location:** Section 3.1; Figure 1
- **Claim:** The review adopts a four-stage system-resilience process: planning/preparation, disturbance absorption, recovery, and adaptation.
- **Status:** verified

### Faithful paraphrase
Preparation includes activities such as risk assessment, disturbance-detection readiness, vulnerability reduction, and recovery planning. Absorption limits the immediate impact of a disturbance. Recovery restores lost functionality and performance. Adaptation changes the system so it can cope better with future threats or environmental changes.

### Context and limits
This is a broad systems-engineering taxonomy. Mapping its phases onto a specific detector, performance curve, or learning update is an application made by the thesis rather than a direct prescription from the review.

### Thesis use
Organize measurements around pre-change readiness, immediate degradation, recovery, and post-recovery learning without claiming that one scalar captures all four phases.

### Citation
Moskalenko et al. (2023), Section 3.1 and Figure 1.

## E3 — Graceful degradation preserves core functionality when full performance cannot be maintained
- **Type:** faithful paraphrase
- **Location:** Section 3.1
- **Claim:** A resilient system can deliberately move to a less functional but acceptable operating state when a disturbance cannot be fully absorbed.
- **Status:** verified

### Faithful paraphrase
The review describes graceful degradation as controlled reduction of non-essential functionality while preserving priority operations for as long as possible. Such fallback behavior is distinguished from uncontrolled collapse because the degraded mode represents an explicit trade-off among functionality, performance, and cost.

### Thesis use
Distinguish controlled fallback performance from uncontrolled post-shift failure and report the utility cost of fallback.

### Citation
Moskalenko et al. (2023), Section 3.1.

## E4 — Resilience should be evaluated together with resource and nominal-performance cost
- **Type:** faithful paraphrase
- **Location:** Section 3.1, Affordable Resilience discussion
- **Claim:** Affordable resilience seeks a balance between lifecycle/resource cost and technical resilience characteristics rather than maximizing resilience without constraint.
- **Status:** verified

### Faithful paraphrase
The review discusses affordable resilience as an engineering trade-off between the benefits of increased resilience and the lifecycle cost of achieving it. It also cites formulations that balance nominal performance against an aggregate resilience indicator subject to resource constraints.

### Thesis use
Report memory, compute, prior-data, interaction, and nominal-performance overhead alongside recovery benefit.

### Citation
Moskalenko et al. (2023), Section 3.1, Affordable Resilience discussion.

## E5 — One resilience metric usually covers only part of the concept
- **Type:** faithful paraphrase
- **Location:** Section 1.2; resilience-indicator discussion
- **Claim:** The review notes that many studies measure only disturbance absorption or only recovery rate, leaving other resilience properties unmeasured.
- **Status:** verified

### Faithful paraphrase
The authors identify a recurring evaluation gap: papers often report one resilience-related property while ignoring the rest of the response process. They cite examples that measure perturbation absorption but omit recovery, and others that focus on recovery rate while ignoring other indicators.

### Thesis use
If an aggregate resilience score is reported, always accompany it with component measures for degradation, recovery, adapted return, safety, and resource cost.

### Citation
Moskalenko et al. (2023), Section 1.2 and resilience-indicator discussion.

## E6 — Broad resilient-AI taxonomy should not be mistaken for an RL algorithm
- **Type:** scope boundary grounded in the review
- **Location:** Overall paper
- **Claim:** The paper is a cross-domain review and taxonomy, not an empirical comparison of specific single-agent RL adaptation algorithms.
- **Status:** verified

### Thesis use
Use it for definitions and evaluation dimensions, not as evidence that a particular thesis agent will outperform another.

### Citation
Moskalenko et al. (2023), overall scope.