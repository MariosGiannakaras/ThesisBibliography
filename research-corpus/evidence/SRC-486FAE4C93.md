---
κωδικός: SRC-486FAE4C93
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — NIST AI Risk Management Framework 1.0

## E1 — AI risk can change with data and deployment context
- **Type:** faithful paraphrase
- **Location:** Executive Summary, pp. 1–3
- **Claim:** AI systems may operate on data or in contexts that change over time, sometimes significantly and unexpectedly, affecting functionality and trustworthiness.
- **Status:** verified

### Faithful paraphrase
NIST notes that AI systems can be trained on or exposed to data that change over time and that deployment contexts are often complex. Such changes can alter system behavior and trustworthiness in ways that are difficult to detect or respond to, motivating lifecycle-oriented risk management rather than a one-time pre-deployment assessment.

### Context and limits
The framework is broad institutional guidance. It does not define a reinforcement-learning changepoint detector, adaptation algorithm, or recovery metric.

### Thesis use
Use as institutional motivation for evaluating controlled post-deployment changes and for documenting monitoring assumptions.

### Citation
NIST (2023), AI RMF 1.0, Executive Summary.

## E2 — Trustworthiness is multidimensional
- **Type:** faithful paraphrase
- **Location:** Section 3, pp. 12–17
- **Claim:** Validity and reliability, safety, security and resilience, accountability, explainability, privacy, and fairness are distinct trustworthiness characteristics.
- **Status:** verified

### Faithful paraphrase
The AI RMF presents valid and reliable behavior as foundational but separately discusses safety, secure and resilient operation, accountability and transparency, explainability and interpretability, privacy enhancement, and fairness with harmful bias managed. A system can therefore perform well on one characteristic without satisfying the others.

### Context and limits
These categories are intentionally general and do not supply task-specific thresholds for a GridWorld experiment.

### Thesis use
Avoid treating average return as a complete proxy for reliability, safety, or resilience; retain separate metric families.

### Citation
NIST (2023), Section 3.

## E3 — Failure to measure a risk is not evidence that the risk is absent
- **Type:** faithful paraphrase
- **Location:** Section 1.2.1, Risk Measurement
- **Claim:** Poorly defined or inadequately understood risks are difficult to measure, and the inability to measure them does not imply that the system is low-risk or high-risk.
- **Status:** verified

### Faithful paraphrase
NIST emphasizes that risk measurement can fail because concepts are not well defined, reliable metrics are unavailable, methods do not transfer across contexts, or simplified metrics can be gamed or omit important nuance. Measurement limitations must therefore be documented rather than interpreted as evidence of safety.

### Context and limits
This principle does not justify avoiding quantitative evaluation when suitable technical measurements are available.

### Thesis use
Report metric assumptions and limitations and do not rely on a single composite resilience score without its component degradation, recovery, and safety measures.

### Citation
NIST (2023), Section 1.2.1.

## E4 — GOVERN, MAP, MEASURE, and MANAGE form a lifecycle process
- **Type:** faithful paraphrase
- **Location:** Part 2, Section 5, pp. 20–33
- **Claim:** The AI RMF organizes risk-management activities into interacting GOVERN, MAP, MEASURE, and MANAGE functions applied throughout the system lifecycle.
- **Status:** verified

### Faithful paraphrase
GOVERN establishes cross-cutting policies and responsibilities, MAP connects the system to its deployment context and potential risks, MEASURE evaluates system behavior and trustworthiness, and MANAGE prioritizes and responds to identified risks. These functions are designed to interact and recur rather than act as a single sequential checklist.

### Context and limits
A thesis benchmark can borrow documentation and monitoring principles from this structure but should not claim organizational compliance with the AI RMF.

### Thesis use
Structure the experimental record around explicit assumptions, mapped perturbation scenarios, measured effects, and documented response mechanisms.

### Citation
NIST (2023), Part 2, Section 5.

## E5 — “Resilient” in the AI RMF should not be substituted for the thesis's operational recovery definition
- **Type:** scope clarification grounded in the framework
- **Location:** Section 3.3, Secure and Resilient
- **Claim:** NIST uses resilience within a broad trustworthiness and security context; a reinforcement-learning experiment still needs a precise operational definition of post-disruption performance and recovery.
- **Status:** verified

### Faithful paraphrase
The AI RMF groups secure and resilient characteristics with protection against adverse events and the ability to withstand or recover from them. This broad framing is useful context but does not define the exact temporal quantities needed to compare learning agents after controlled environmental shifts.

### Thesis use
Use NIST only as high-level motivation and retain the thesis-specific metrics for immediate degradation, recovery time, recovered level, repeated-change behavior, and safety cost.

### Citation
NIST (2023), Section 3.3.