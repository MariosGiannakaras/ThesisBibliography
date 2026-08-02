---
κωδικός: SRC-FE2C0A3E00
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — AI Safety Gridworlds

## Evidence E1 — Gridworlds as controlled minimal testbeds

- **Type:** faithful paraphrase
- **Location:** pp. 1–2, Section 1, paragraphs motivating the use of gridworlds
- **Claim:** Small gridworlds are useful controlled testbeds when the purpose is to isolate a specific failure mode rather than reproduce the full complexity of a real deployment environment.
- **Thesis use:** methodology; experimental-environment design
- **Topics:** gridworld; benchmark design; confounding factors
- **Status:** verified

### Faithful paraphrase
The authors deliberately use two-dimensional gridworlds because the environments are simple enough to make the learning problem easy and to limit experimental confounders. They treat these environments as minimal safety checks: failure under such simple conditions is informative, even though success does not establish safe behavior in much more complicated real-world systems.

### Context and limitation
This rationale supports a controlled testbed, not a claim that gridworlds are uniquely appropriate or externally representative. The thesis should therefore present GridWorld results as controlled comparative evidence rather than as direct evidence about deployment-scale systems.

### Reference
Leike et al. (2017), pp. 1–2, Section 1.

## Evidence E2 — Observed reward can differ from the evaluator's performance criterion

- **Type:** faithful paraphrase
- **Location:** pp. 2–3, Sections 1–2, definition of reward and performance functions
- **Claim:** Agent evaluation need not be limited to the visible cumulative reward when the behavior that the evaluator actually wants can require a separate hidden performance criterion.
- **Thesis use:** metrics; experimental protocol
- **Topics:** reward; performance function; robustness; specification
- **Status:** verified

### Faithful paraphrase
Each environment has a reward function observed by the agent and a separate performance function used by the evaluator to represent the intended behavior. When the two functions coincide, the paper classifies the problem as a robustness problem; when they differ, it classifies it as a specification problem. A learner can therefore optimize the signal available to it while still performing poorly according to the evaluator's intended criterion.

### Context and limitation
The paper's performance functions are tailored to individual environments and should not be presented as a universal definition of resilience. For the thesis, the broader lesson is that task return, safety cost, degradation, and recovery can require distinct evaluation signals.

### Reference
Leike et al. (2017), pp. 2–3, Sections 1–2.

## Evidence E3 — Small train/test changes can expose severe distribution-shift failures

- **Type:** faithful paraphrase
- **Location:** Section 2.2.2 and Section 3.2, including the lava-world train/test layouts and reported agent behavior
- **Claim:** A small change between training and testing can produce a large performance failure even when the learner performed well in the training configuration.
- **Thesis use:** shift scenarios; post-change degradation
- **Topics:** distributional shift; layout change; robustness failure
- **Status:** verified

### Faithful paraphrase
In the lava-world distributional-shift task, training and testing use closely related layouts but the safe route changes. The reported A2C and Rainbow behavior shows that competence in the training layout does not guarantee competent behavior after the layout change; the agents can continue to act according to patterns that were useful before the shift and incur large negative outcomes after it.

### Context and limitation
The result concerns particular deep-RL baselines in a toy environment without a dedicated online adaptation mechanism. It should not be generalized into a claim that every small layout change causes the same failure or that all RL algorithms fail under such shifts.

### Reference
Leike et al. (2017), Sections 2.2.2 and 3.2.

## Evidence E4 — Passing a benchmark does not establish absence of the failure mode

- **Type:** faithful paraphrase
- **Location:** Discussion/Outlook, pp. 15–16
- **Claim:** A benchmark can reveal a failure and support comparison, but success on a finite suite does not prove that the underlying safety problem has been solved in general.
- **Thesis use:** threats to validity; benchmark interpretation
- **Topics:** benchmark validity; overfitting; external validity
- **Status:** verified

### Faithful paraphrase
The authors caution that solutions can become tailored to the particular environments in a test suite. The value of the suite is therefore in making concrete failure modes measurable and reproducible, not in certifying that an agent that passes the suite is safe across arbitrary environments.

### Context and limitation
The same limitation applies to a resilience benchmark: the experiment can compare methods under declared shift families and resource budgets, but it cannot establish universal resilience.

### Reference
Leike et al. (2017), Discussion and Outlook, pp. 15–16.

## Avoid overclaiming
This source should not be used to claim that GridWorld is the only appropriate experimental platform, that the paper defines resilience or post-shift recovery, that observed reward and a resilience metric must always be different functions, or that success on a toy benchmark transfers directly to real-world systems.
