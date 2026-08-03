---
κωδικός: SRC-6E7AFA8AC0
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Toward Theoretical Understandings of Robust Markov Decision Processes: Sample Complexity and Asymptotics

## E1 — Robust-MDP sample complexity depends on uncertainty-set structure
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1; Tables 1–2
- **Claim:** Finite-sample guarantees vary with the uncertainty-set family, radius, rectangularity assumption, discount factor, and state/action dimensions.
- **Status:** verified

### Faithful paraphrase
Yang, Zhang, and Zhang analyze tabular robust MDPs under several divergence-ball uncertainty sets, including `L1`, chi-square, and KL balls. Their bounds differ across these choices and across `(s,a)`-rectangular and `s`-rectangular structures. The `s`-rectangular setting is generally more sample-demanding in their analysis than the corresponding `(s,a)`-rectangular case.

### Thesis use
Treat uncertainty-set family, radius, and rectangularity as part of the method specification and experimental protocol, not as interchangeable implementation details.

### Citation
Yang, Zhang, and Zhang (2022), Abstract, Section 1.1, Tables 1–2.

## E2 — Rectangularity is a structural assumption that enables tractable robust optimization
- **Type:** faithful paraphrase
- **Location:** Introduction
- **Claim:** Robust-MDP solution theory commonly assumes independent uncertainty across state–action pairs or states; dropping these structures can make robust optimization substantially harder.
- **Status:** verified

### Faithful paraphrase
The paper explains that `(s,a)`-rectangular and `s`-rectangular uncertainty sets permit efficient robust-MDP solution methods, while more general coupling of uncertain transition probabilities can make the problem NP-hard. The choice therefore encodes a substantive assumption about how model uncertainty factorizes.

### Thesis use
If a robust baseline is included, state whether its ambiguity set is rectangular and why that assumption is plausible for the simulated perturbation.

### Citation
Yang, Zhang, and Zhang (2022), Introduction.

## E3 — The theory is built around model estimation from a generative model or offline data
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1
- **Claim:** The main finite-sample results analyze robust value and policy estimation from sampled transition data, with primary results for a generative-model setting and extensions to offline data.
- **Status:** verified

### Faithful paraphrase
The study is statistical rather than a changepoint-learning paper. It asks how many transition samples are needed for an empirical robust MDP to approximate the target robust policy/value under specified uncertainty assumptions. The main development assumes generative sampling, and additional results treat an offline dataset generated under a behavior occupancy distribution.

### Thesis use
Do not compare these guarantees directly with pure-online adaptation unless simulator-query and offline-data access are matched and reported.

### Citation
Yang, Zhang, and Zhang (2022), Abstract and Section 1.1.

## E4 — A larger uncertainty radius is not automatically better
- **Type:** interpretation constrained by the theory
- **Location:** Section 1.1 and robust-MDP formulation
- **Claim:** The uncertainty radius appears in statistical bounds and changes the robust optimization problem; it is not a monotonic empirical-performance knob.
- **Status:** verified

### Faithful paraphrase
The paper derives how finite-sample estimation behaves as a function of the uncertainty-set radius, but robust policies simultaneously become more conservative as the ambiguity set changes. Statistical sample efficiency therefore does not imply that increasing the radius will improve nominal or disturbed task performance.

### Thesis use
Report nominal return, disturbed return, and conservativeness gap as a function of the chosen radius rather than selecting it from final test performance.

### Citation
Yang, Zhang, and Zhang (2022), Section 1.1 and formulation.

## E5 — Robust MDPs address model mismatch, not post-changepoint relearning
- **Type:** scope inference grounded in the formulation
- **Location:** Introduction and problem formulation
- **Claim:** The method seeks a policy that performs well over transition models in a predefined ambiguity set around estimated dynamics; it does not detect a temporal regime change and then learn a new policy.
- **Status:** verified

### Thesis use
Use robust MDPs as static/worst-case robustness comparators and keep `online_resilience` metrics separate.

### Citation
Yang, Zhang, and Zhang (2022), Introduction and problem formulation.

## E6 — Statistical inference on robust values is a separate contribution from resilience evaluation
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1.1
- **Claim:** The paper establishes asymptotic normality for estimated optimal robust value functions under its assumptions, enabling statistical inference about robust estimators.
- **Status:** verified

### Thesis use
Do not conflate confidence intervals for an estimated robust value with uncertainty about a changepoint, recovery time, or detector calibration.

### Citation
Yang, Zhang, and Zhang (2022), Abstract and Section 1.1.