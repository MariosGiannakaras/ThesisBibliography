---
κωδικός: SRC-AC30CEB175
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-05"
source-language: en
---

# Evidence — AI Applications to Enhance Resilience in Power Systems and Microgrids—A Review

## E1 — Resilience is organized around phases before, during, and after disruption

- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1.1 and 1.4
- **Claim:** The review treats resilience as a temporal process and explicitly organizes AI applications by pre-event, during-event, and post-event phases.
- **Status:** verified

### Faithful paraphrase

The review describes power-system resilience in terms of preparing for and adapting to changing conditions, resisting or reconfiguring during disruptive events, and restoring operation afterward. Its review design explicitly tracks AI applications according to whether they act before, during, or after an event.

### Context and limits

The phases are discussed for power systems and microgrids. They provide a general temporal decomposition, not a validated single-agent RL protocol.

### Thesis use

Use a phase-aware experimental timeline that separates nominal behavior, disruption onset, immediate degradation, adaptation/recovery, and stabilized post-change behavior.

### Citation

Zahraoui et al. (2024), Abstract and Sections 1.1, 1.4.

## E2 — Service restoration makes post-disruption recovery an explicit optimization concern

- **Type:** faithful paraphrase
- **Location:** Section 5.1, Service Restoration
- **Claim:** Post-event resilience includes restoring critical functionality rapidly under operational constraints rather than measuring only nominal performance.
- **Status:** verified

### Faithful paraphrase

For microgrids affected by major disasters, service restoration aims to recover supply to important loads while respecting system constraints. The review emphasizes swift recovery and describes restoration as a constrained problem in which available resources, switching decisions, and operating limits determine how much functionality can be recovered after the disruption.

### Context and limits

The concrete objective concerns electrical loads, topology, and network constraints. These quantities are domain-specific and should not be copied into the GridWorld benchmark.

### Thesis use

Treat recovery after a known environmental change as an explicit measurable phase. Report recovery time and recovered performance separately from pre-change nominal performance.

### Citation

Zahraoui et al. (2024), Section 5.1.

## E3 — Data quantity and quality constrain AI-based resilience methods

- **Type:** faithful paraphrase
- **Location:** Section 6.1, Limitations of AI Applications in Resilience
- **Claim:** AI resilience applications depend on sufficient, high-quality data, and inconsistent or incomplete data can limit model performance.
- **Status:** verified

### Faithful paraphrase

The review identifies data requirements as a practical limitation of AI-based resilience methods. Training effective models can require substantial data, while renewable-energy and operational data may be inconsistent or incomplete because of changing environmental and contextual conditions.

### Context and limits

The examples are drawn from energy systems. The general point supports careful treatment of observation/data quality but does not establish a particular observation-noise model for the thesis.

### Thesis use

Keep observation degradation and environmental dynamics change as separately controlled factors, and avoid interpreting performance under corrupted observations as evidence about dynamics adaptation unless the protocol isolates the two.

### Citation

Zahraoui et al. (2024), Section 6.1.

## E4 — Simulation and synthetic data are useful research tools but require practical validation

- **Type:** faithful paraphrase
- **Location:** Section 6.2, Future Direction
- **Claim:** Rich simulation can support AI resilience research and synthetic-data generation, but proposed techniques still require practical experimental validation.
- **Status:** verified

### Faithful paraphrase

The authors recommend comprehensive simulation models that cover diverse sources, loads, and fault conditions so that realistic synthetic data can be generated for learning algorithms. In the same future-work discussion, they call for real-time experimental validation to establish the effectiveness and reliability of proposed AI and IoT resilience techniques.

### Context and limits

A microgrid simulation can be much more complex than the deliberately minimal GridWorld planned for this thesis. The relevant transferable principle is that simulation supports controlled experimentation while external validity remains a separate question.

### Thesis use

Use the GridWorld as a controlled diagnostic testbed, state its abstraction limits explicitly, and avoid claiming real-world resilience from simulation results alone.

### Citation

Zahraoui et al. (2024), Section 6.2.

## E5 — The review supports resilience framing, not direct algorithm selection for this thesis

- **Type:** scope inference grounded in the paper
- **Location:** Sections 1.3–1.4; Sections 4–6
- **Claim:** The paper surveys heterogeneous AI applications for microgrid resilience and does not provide a controlled comparison that can directly choose the thesis's single-agent RL model set.
- **Status:** verified

### Faithful paraphrase

The review categorizes many AI techniques and applications across power-system tasks, data sources, event phases, and operational objectives. Its synthesis is intended to map applications, compare approaches within their reported contexts, and identify gaps rather than establish one common benchmark in which candidate learning agents receive identical information and interaction budgets.

### Context and limits

Cross-study results are heterogeneous and domain-specific. Any model-selection decision for the thesis must rely on sources and pilots that directly address comparable RL adaptation settings.

### Thesis use

Use this source for resilience lifecycle, recovery framing, simulation limitations, and operational context. Do not cite it as proof that a specific deep-learning or optimization algorithm should be implemented in the GridWorld experiment.

### Citation

Zahraoui et al. (2024), overall review scope.
