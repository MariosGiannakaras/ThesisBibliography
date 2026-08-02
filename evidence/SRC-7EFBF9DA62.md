---
κωδικός: SRC-7EFBF9DA62
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — A Review of Uncertainty Quantification in Deep Learning: Techniques, Applications and Challenges

## E1 — Aleatoric and epistemic uncertainty have different origins

- **Type:** faithful paraphrase
- **Location:** Introduction; Figure 1
- **Claim:** Aleatoric uncertainty reflects variability inherent in the data-generating process, whereas epistemic uncertainty reflects insufficient knowledge or model coverage.
- **Status:** verified

### Faithful paraphrase

Abdar et al. describe aleatoric uncertainty as irreducible uncertainty associated with noise or variability in the data distribution. Epistemic uncertainty, by contrast, arises from inadequate knowledge or data and is therefore associated with uncertainty about the model or its parameters.

### Context and limits

The practical decomposition depends on the modeling assumptions; observed variability cannot always be assigned uniquely to one category.

### Thesis use

Keep stochastic transition/reward noise separate from uncertainty caused by unseen regimes or insufficient model knowledge.

### Citation

Abdar et al., Introduction and Figure 1.

## E2 — Bayesian predictive uncertainty integrates over parameter uncertainty

- **Type:** faithful paraphrase
- **Location:** Section 2.2, Equations 4–12
- **Claim:** Bayesian uncertainty modeling represents epistemic uncertainty through a distribution over model parameters and integrates predictions over the posterior or an approximation to it.
- **Status:** verified

### Faithful paraphrase

The review presents predictive uncertainty as containing epistemic and aleatoric components. In the Bayesian formulation, a prior is placed over model parameters, data update this distribution to a posterior, and predictions marginalize the likelihood over parameter uncertainty. Because the exact posterior is generally intractable for deep models, approximations such as variational inference and dropout-based inference are commonly used.

### Context and limits

An approximate posterior is not ground-truth uncertainty. Its quality depends on the prior, approximation family, optimization, and available data.

### Thesis use

Any uncertainty-aware baseline must specify its estimator and validate the resulting uncertainty signal rather than assuming calibration.

### Citation

Abdar et al., Section 2.2, Equations 4–12.

## E3 — UQ methods should not be ranked universally across unrelated tasks

- **Type:** faithful paraphrase
- **Location:** Section 1.1, research objectives and scope
- **Claim:** The review explicitly avoids a universal performance ranking because UQ methods were developed and evaluated for different data and tasks.
- **Status:** verified

### Faithful paraphrase

The authors state that comparing the performance of all surveyed uncertainty-quantification methods is outside the scope of the review because the methods target different datasets and application-specific problems. The survey organizes techniques and research gaps instead of identifying a single universal winner.

### Thesis use

Choose a small number of uncertainty estimators through task-specific feasibility tests rather than importing a cross-domain ranking.

### Citation

Abdar et al., Section 1.1.

## E4 — Calibration, data quality, theory, and computational cost remain limitations

- **Type:** faithful paraphrase
- **Location:** Introduction; future-directions discussion
- **Claim:** Reliable UQ is constrained by incomplete theory, imperfect data, calibration problems, and computational expense.
- **Status:** verified

### Faithful paraphrase

The review identifies recurring difficulties including limited theoretical understanding, sensitivity to noisy or incomplete data, imperfect uncertainty calibration, and the computational burden of many Bayesian or ensemble-style methods. Future directions emphasize more reliable inference, calibration, and efficient uncertainty estimation.

### Thesis use

If an uncertainty-aware agent is included, report calibration behavior and computational overhead alongside return and recovery metrics.

### Citation

Abdar et al., Introduction and future-directions section.

## E5 — Uncertainty estimates are decision inputs, not resilience mechanisms by themselves

- **Type:** synthesis grounded in the RL survey material
- **Location:** RL-related survey sections and future directions
- **Claim:** The reviewed literature uses uncertainty for exploration, risk-sensitive decisions, safe RL, and model-based reasoning, but an uncertainty signal alone does not adapt a policy.
- **Status:** verified

### Faithful paraphrase

The review covers uses of uncertainty estimates in Bayesian exploration, temporal-difference uncertainty, model-based RL, epistemic-risk reasoning, and safe decision making. In each case, uncertainty is information consumed by another decision or learning mechanism. High predictive or epistemic uncertainty is therefore a diagnostic signal unless the agent has an explicit rule for converting that signal into action or adaptation.

### Thesis use

Separate uncertainty-estimator quality from detector quality and from post-change recovery performance.

### Citation

Abdar et al., RL-related synthesis and future directions.
