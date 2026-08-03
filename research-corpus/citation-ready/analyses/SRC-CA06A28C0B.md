---
κωδικός: SRC-CA06A28C0B
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI-20, Open-World Learning for Radically Autonomous Agents"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Scientific analysis — SRC-CA06A28C0B

## Bibliographic identity
Pat Langley, **Open-World Learning for Radically Autonomous Agents**, Proceedings of the AAAI Conference on Artificial Intelligence, AAAI-20, 2020.

- **Thesis role:** supporting

## Purpose and research problem
The paper formulates open-world learning as a setting in which an autonomous agent begins with expertise that is adequate for a class of environments, but then encounters **sudden, unannounced, long-lasting changes** that degrade its performance. With only limited new experience, the agent must determine when the environment has changed and revise its expertise quickly enough to regain acceptable performance.

The formulation is broader than reinforcement learning and does not prescribe one RL algorithm. It is nevertheless directly relevant to the thesis protocol because it explicitly separates monitoring/change detection, diagnosis, and repair/adaptation.

## Architectural distinction
The paper distinguishes four functions:
1. a **performance element** that uses current expertise,
2. a **monitoring element** that compares observations with expectations and detects anomalies,
3. a **diagnostic element** that localizes likely causes of failure,
4. a **repair element** that revises the expertise responsible for the failure.

This supports the thesis boundary **detector ≠ adapter**. Monitoring evidence is not itself policy recovery, and repair quality must not be conflated with detection accuracy.

## Taxonomy of environmental changes
The paper proposes a framework in which transformations may affect:
- spatial/temporal fields and parameters,
- object categories and attributes,
- physical, control, or perceptual processes,
- constraints, goals, and values.

For the GridWorld benchmark this supports treating reward semantics, transition dynamics, action capabilities, observation processes, and structural constraints as distinct shift families rather than collapsing them into one scalar perturbation.

## Evaluation design
A particularly useful proposal is the **novelty response curve**: performance is plotted over time with novelty events marked, making the post-change degradation and subsequent recovery/adaptation visible. The paper also argues that time to detect an environmental change and the rate of performance improvement after detection should be measured separately.

It further identifies experimental variables such as:
- novelty type,
- novelty frequency,
- number of changes,
- randomized novelty timing so the agent cannot anticipate the changepoint.

## Relevance to the thesis
The source directly supports:
- unannounced changepoints,
- detector/diagnosis/repair separation,
- multiple shift families,
- recovery curves,
- detection delay separated from adaptation rate,
- randomized changepoint timing,
- repeated changes without assuming full relearning from scratch.

The full symbolic/open-world architecture proposed in the paper does not need to be implemented.

## Limitations and validity risks
- Position/framework paper rather than a matched empirical RL benchmark.
- No specific learning algorithm or quantitative detector baseline is established.
- Expertise may be symbolic/model-based rather than a value-function policy.
- The proposed novelty categories are broader than the resource-aware GridWorld scope.
- It does not establish that its monitoring/diagnosis architecture outperforms a simple statistical changepoint detector.

## Use in the thesis
Use as a **supporting source for problem formulation and evaluation protocol**, especially for the detection–repair distinction and novelty-response curves. Do not use it to claim algorithmic superiority for a particular agent.

## Decision
**Selected as a supporting source.**
