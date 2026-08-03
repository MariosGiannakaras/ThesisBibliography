---
κωδικός: SRC-EA5D0E318E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Evidence — Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles

## 1. Calibration and predictive accuracy are different properties
- Type: faithful paraphrase
- Location: Section 1, Introduction
- Claim: Calibration measures agreement between predictive confidence and empirical frequencies and is orthogonal to predictive accuracy.
- Thesis use: uncertainty evaluation
- Topics: calibration; accuracy; uncertainty quality
- Status: verified

### Faithful paraphrase
A neural network can be accurate while its confidence estimates are poorly calibrated, or it can be well calibrated without being highly accurate. Calibration therefore needs its own evaluation rather than being inferred from task performance.

## 2. Deep ensembles provide a simple predictive-uncertainty baseline
- Type: faithful paraphrase
- Location: Sections 1–2
- Claim: Independently trained probabilistic neural networks can be combined into an ensemble to obtain predictive uncertainty estimates without requiring a full Bayesian neural-network training procedure.
- Thesis use: optional neural uncertainty baseline
- Topics: deep ensembles; predictive uncertainty; model uncertainty
- Status: verified

### Faithful paraphrase
The method trains multiple probabilistic neural networks with independent initializations and combines their predictive distributions. This provides a comparatively simple and parallelizable uncertainty-estimation baseline.

## 3. Proper scoring rules are used to train probabilistic predictions
- Type: faithful paraphrase
- Location: Section 2.2
- Claim: Proper scoring rules reward predictive distributions that agree with the true data-generating distribution and can be used as training objectives for probabilistic neural networks.
- Thesis use: calibration methodology
- Topics: proper scoring rules; log likelihood; Brier score
- Status: verified

### Faithful paraphrase
The paper motivates probabilistic-network training with proper scoring rules such as log likelihood and discusses the Brier score as another proper scoring rule for classification probabilities.

## 4. Distribution shift can be evaluated through uncertainty response
- Type: faithful paraphrase
- Location: Section 1 and experimental sections
- Claim: The paper evaluates whether predictive uncertainty increases on examples from unknown distributions as a practical test of uncertainty quality under dataset shift.
- Thesis use: static OOD diagnostics
- Topics: OOD; dataset shift; uncertainty
- Status: verified

### Faithful paraphrase
A useful uncertainty model should express higher uncertainty when inputs come from distributions that differ substantially from the training distribution. The paper evaluates this behavior as a complement to calibration on in-distribution data.

## 5. Static OOD uncertainty is not an online changepoint detector
- Type: thesis-safe inference from study design
- Location: Study scope and experiments
- Claim: The paper does not evaluate sequential changepoints, false alarms, detection delay, or adaptation after a detected change.
- Thesis use: scope boundary
- Topics: detector; OOD score; changepoint
- Status: verified

### Safe use
Treat ensemble disagreement or predictive variance as a possible signal that can feed a detector. If used in the thesis, the detector still requires its own threshold calibration and sequential evaluation.

## 6. Compute cost is part of the method trade-off
- Type: faithful paraphrase
- Location: Introduction and method discussion
- Claim: The method is designed to be simple and parallelizable, but it requires training and storing multiple neural networks.
- Thesis use: resource-aware comparison
- Topics: compute; memory; ensemble size
- Status: verified

### Safe use
If a neural ensemble is included, report ensemble size, training cost, inference cost, and memory footprint rather than treating uncertainty quality as resource-free.

## Avoid overclaiming
This source does not establish that:
- deep ensembles are universally the best uncertainty estimator,
- an ensemble uncertainty score is a calibrated online change detector,
- uncertainty estimation alone provides policy adaptation or recovery,
- a deep-ensemble baseline is necessary for the resource-aware tabular core.
