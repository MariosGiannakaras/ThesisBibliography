---
κωδικός: SRC-EA5D0E318E
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "NeurIPS 2017, Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Scientific analysis — SRC-EA5D0E318E

## Bibliographic identity
Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell, **Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles**, NeurIPS 2017.

- **Thesis role:** background

## Research problem
The paper addresses predictive uncertainty in deep neural networks. Standard neural networks can be overconfident and do not naturally provide reliable uncertainty estimates. The authors propose a simple ensemble-based alternative to approximate Bayesian neural networks and evaluate both calibration and behavior under dataset shift.

## Method
The method trains multiple probabilistic neural networks independently, using proper scoring rules as training objectives. Predictions from the independently initialized models are then combined as an ensemble. The paper also studies adversarial training as a way to smooth predictive distributions.

The key engineering property is that the method requires only modest changes to a conventional neural-network training pipeline and can be parallelized.

## Main findings
Across the supervised classification/regression benchmarks studied in the paper, deep ensembles provide strong predictive uncertainty estimates and compare favorably with the approximate Bayesian baselines considered. Under distribution shift, the ensembles tend to express greater uncertainty on examples from unknown distributions.

The paper also emphasizes calibration as a distinct property from predictive accuracy: a model may be accurate but poorly calibrated, or calibrated while not highly accurate.

## Critical distinctions
### Predictive uncertainty ≠ changepoint detection
The paper evaluates uncertainty under static dataset shift. It does not study sequential changepoints, detection delay, false-alarm rate, or post-detection adaptation. An ensemble uncertainty score can therefore be a detector input or diagnostic signal, but it is not automatically a calibrated online change detector.

### Calibration ≠ accuracy
Calibration evaluates whether probabilistic confidence agrees with empirical frequencies. It should not be replaced by ordinary task return or classification accuracy.

### Epistemic-style ensemble disagreement ≠ aleatoric noise
The ensemble construction is useful for model/predictive uncertainty, but it does not make all uncertainty reducible or uniquely identify the source of uncertainty.

## Relevance to the thesis
The source provides foundational support for an optional neural uncertainty baseline if the thesis includes a deep agent or neural detector. In that case:
- use ensemble disagreement or predictive variance only as a signal,
- calibrate a decision threshold on validation environments,
- evaluate false alarms and missed changes separately,
- report sequential detection delay in addition to static OOD metrics,
- do not infer adaptation ability from uncertainty quality.

For the resource-aware tabular core, the method is not required and should remain a feasibility/background option rather than a mandatory baseline.

## Limitations
- The experiments are supervised-learning benchmarks, not non-stationary RL sequences.
- Training several neural networks increases compute and memory cost.
- High uncertainty on OOD inputs does not identify which environment mechanism changed.
- Strong performance in the reported benchmarks does not imply universal superiority over other uncertainty methods.

## Use in the thesis
Use as a **background source for neural predictive uncertainty and calibration**, and as a justification for treating ensembles as an optional uncertainty signal. Do not cite it as evidence that ensembles are themselves a complete online change-detection or resilience mechanism.

## Decision
**Selected as a background source.**
