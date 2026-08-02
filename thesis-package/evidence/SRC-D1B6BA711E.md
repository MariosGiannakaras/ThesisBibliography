---
κωδικός: SRC-D1B6BA711E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Online Policy Optimization for Robust MDP

## E1 — Online robust learning can be studied without a generative-model oracle
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** The paper studies robust MDP learning through sequential interaction with an unknown nominal system, so the agent must balance exploration and exploitation rather than request arbitrary simulator samples.
- **Status:** verified

### Faithful paraphrase
Dong et al. distinguish their setting from robust-MDP analyses that assume a generative model or an offline dataset. Their learner interacts online with the nominal environment, collects only the transitions produced by its own policy, and must learn a robust policy while managing the ordinary exploration–exploitation problem.

### Context and limits
The uncertainty set around the nominal model is still specified in advance. “Online” here describes data collection, not a temporal changepoint in the nominal system.

### Thesis use
An online robust comparator should receive the same interaction budget as other online agents and must declare its uncertainty-set prior separately.

### Citation
Dong et al. (2022), Abstract and Introduction.

## E2 — Robust online learning contains two different sources of uncertainty
- **Type:** faithful paraphrase
- **Location:** Introduction; robust optimistic update discussion
- **Claim:** The algorithm must handle uncertainty from limited historical data in addition to the deployment/model ambiguity already encoded by the robust MDP.
- **Status:** verified

### Faithful paraphrase
The paper's optimistic construction accounts for statistical uncertainty because the nominal transition dynamics are initially unknown and only partially observed through interaction. Separately, the robust objective evaluates the learned policy against transitions that may vary within the predefined ambiguity set. These two uncertainties enter the algorithm for different reasons.

### Context and limits
This distinction is not the same as a calibrated aleatoric/epistemic decomposition for changepoint detection.

### Thesis use
Report `estimation_uncertainty` and `assumed_deployment_ambiguity` as separate design quantities.

### Citation
Dong et al. (2022), Introduction.

## E3 — Robust MDP optimizes a max–min objective over a fixed ambiguity set
- **Type:** faithful paraphrase
- **Location:** Sections 1 and 3
- **Claim:** The learned policy maximizes value against the worst transition kernel allowed by the uncertainty set around the nominal system.
- **Status:** verified

### Faithful paraphrase
The robust value of a policy is defined by minimizing its expected return over transition kernels contained in the specified uncertainty set. The robust optimal policy then maximizes this worst-case value. The paper studies both `(s,a)`-rectangular and `s`-rectangular sets built around nominal transitions.

### Context and limits
The ambiguity radius and rectangularity are model assumptions. They should not be tuned on final shifted-test performance.

### Thesis use
State the uncertainty radius, distance metric, and rectangularity alongside every robust-policy result.

### Citation
Dong et al. (2022), Sections 1 and 3.

## E4 — Online interaction does not turn robust optimization into changepoint adaptation
- **Type:** scope inference grounded in the formulation
- **Location:** Abstract; Sections 1–3
- **Claim:** The nominal system is learned online while robustness protects against transitions in a predefined set; the paper does not detect a time at which the nominal environment changes and then switch or reset learning.
- **Status:** verified

### Thesis use
Do not classify this method as detector-triggered resilience. It is an `online_robust_learning` comparator unless an additional shift-detection mechanism is added.

### Citation
Dong et al. (2022), overall formulation.

## E5 — Rectangularity changes both policy structure and theoretical complexity
- **Type:** faithful paraphrase
- **Location:** Section 3; theoretical results
- **Claim:** The paper separately treats `(s,a)`-rectangular and `s`-rectangular uncertainty sets, with different regret/sample-complexity expressions and potentially different optimal-policy structure.
- **Status:** verified

### Faithful paraphrase
Under `(s,a)`-rectangular uncertainty, an optimal robust policy can be deterministic, whereas the more general `s`-rectangular case can require randomized policies. The regret bounds also carry different dependence on action-space size across these structures.

### Thesis use
Do not compare robust methods across different ambiguity structures without exposing the structural assumption.

### Citation
Dong et al. (2022), Section 3 and theoretical results.

## E6 — Generative-model and online robust results should not be compared as if they share the same data access
- **Type:** protocol implication grounded in the Introduction and Table 1
- **Location:** Introduction; Table 1
- **Claim:** The paper explicitly distinguishes prior results that require a generative model from its online setting.
- **Status:** verified

### Thesis use
Count simulator queries, offline samples, and ordinary online interactions separately in the resource ledger.

### Citation
Dong et al. (2022), Introduction and Table 1.