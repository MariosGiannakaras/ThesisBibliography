---
κωδικός: SRC-CA06A28C0B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Evidence — Open-World Learning for Radically Autonomous Agents

## 1. Open-world learning requires both change detection and expertise repair
- Type: faithful paraphrase
- Location: Section 2, “Elements of Open-World Learning”
- Claim: The task is defined as detecting when sudden, unannounced environmental changes occurred and revising expertise so that acceptable performance can be restored from limited experience.
- Thesis use: problem formulation; detector–adapter separation
- Topics: novelty; change detection; adaptation; recovery
- Status: verified

### Faithful paraphrase
An open-world agent starts with expertise that is adequate for a known class of environments. When an unannounced environmental change degrades performance, the agent must identify that a change occurred and revise the relevant expertise quickly enough to recover acceptable behavior.

### Context and limitation
The formulation is architectural and domain-general. It does not identify one RL algorithm as the preferred implementation.

## 2. Monitoring, diagnosis, and repair are distinct functions
- Type: faithful paraphrase
- Location: Section 2
- Claim: The proposed architecture separates monitoring for anomalies, diagnosis of the likely cause, and repair of the affected expertise.
- Thesis use: experimental mechanism definitions
- Topics: detector; diagnosis; adapter
- Status: verified

### Faithful paraphrase
The monitoring component compares observations with expectations to identify anomalies; a diagnostic component localizes possible causes; and a repair component revises the expertise judged responsible for the performance problem.

### Safe use
Use this distinction to justify reporting detector quality separately from post-detection recovery quality.

## 3. Environmental novelty should be decomposed by mechanism
- Type: faithful paraphrase
- Location: Sections 3–4
- Claim: Environmental transformations may affect fields, structures, processes, constraints, goals, or other components of the environment.
- Thesis use: benchmark taxonomy
- Topics: structural shift; transition shift; observation shift; goal/reward shift
- Status: verified

### Faithful paraphrase
Novelty can arise through changes to spatial or temporal fields, object categories and attributes, physical/control/perceptual processes, or environmental constraints and goals. These are qualitatively different forms of change and need not be treated as one undifferentiated perturbation.

## 4. Novelty-response curves expose degradation and recovery
- Type: faithful paraphrase
- Location: Section 5, “Experiments with Open-World Learning”
- Claim: Performance should be plotted over time with novelty events marked so that degradation and subsequent recovery are visible.
- Thesis use: metrics and plotting protocol
- Topics: recovery curve; transient degradation; changepoint
- Status: verified

### Faithful paraphrase
A novelty-response curve tracks performance over time and marks the points at which novelty is introduced. The expected pattern is a performance drop after the change followed by recovery as the learner detects and adapts to the new situation.

## 5. Detection time and adaptation rate should be measured separately
- Type: faithful paraphrase
- Location: Section 5
- Claim: Experiments can separately measure how long change detection takes and how quickly performance improves after detection.
- Thesis use: primary evaluation metrics
- Topics: detection delay; adaptation rate; credit assignment
- Status: verified

### Faithful paraphrase
The time required to detect an environmental change and the rate of performance improvement after detection are separate outcomes. Measuring them independently helps attribute success or failure to different components of an adaptive architecture.

## 6. Novelty timing should not be trivially predictable
- Type: faithful paraphrase
- Location: Section 5
- Claim: Randomized novelty timing is desirable to prevent an agent from anticipating a fixed change schedule.
- Thesis use: benchmark design
- Topics: randomized changepoint; anticipation leakage
- Status: verified

### Faithful paraphrase
If novelty is always introduced at a fixed, predictable point, an agent can potentially exploit the schedule rather than genuinely detect change. Randomizing novelty timing reduces this form of leakage.

## Avoid overclaiming
This source does not establish that:
- a particular statistical detector is optimal,
- monitoring alone constitutes recovery,
- its full symbolic architecture is required for the thesis,
- all proposed novelty categories must be implemented in the GridWorld benchmark.
