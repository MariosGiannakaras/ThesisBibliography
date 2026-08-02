---
κωδικός: SRC-70AEC665B2
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — On Calibration of Modern Neural Networks

## E1 — Accuracy and calibration are different properties
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Figure 1
- **Claim:** A neural classifier can achieve strong predictive accuracy while assigning confidence values that do not match empirical probabilities of correctness.
- **Status:** verified

### Faithful paraphrase
Guo et al. define a calibrated classifier as one whose reported confidence corresponds to the observed frequency of correct predictions. Their experiments show that modern deep networks can be more accurate than earlier models while being substantially more overconfident, demonstrating that classification accuracy alone does not establish trustworthy probability estimates.

### Thesis use
Do not interpret neural action probabilities, classifier confidence, or detector scores as calibrated probabilities without separate calibration evidence.

### Citation
Guo et al. (2017), Abstract, Introduction, and Figure 1.

## E2 — Reliability diagrams compare empirical accuracy with mean confidence
- **Type:** faithful paraphrase
- **Location:** Section 2
- **Claim:** Reliability diagrams bin predictions by confidence and compare each bin's empirical accuracy with its average reported confidence.
- **Status:** verified

### Faithful paraphrase
For a well-calibrated classifier, bins of predictions with a given confidence should have approximately the same fraction of correct labels. A reliability diagram visualizes the deviation between these quantities, while finite binning approximates the underlying continuous calibration relation.

### Thesis use
For classifier-like detector scores, include held-out reliability diagnostics rather than reporting discrimination metrics alone.

### Citation
Guo et al. (2017), Section 2.

## E3 — ECE and MCE summarize different calibration gaps
- **Type:** faithful paraphrase
- **Location:** Section 2, Equations 3 and 5
- **Claim:** Expected Calibration Error averages confidence–accuracy gaps across bins with sample-frequency weighting, while Maximum Calibration Error reports the largest observed bin gap.
- **Status:** verified

### Context and limits
Both metrics depend on finite samples and a binning scheme. They summarize calibration of classification confidence and do not replace sequential false-alarm or detection-delay metrics.

### Thesis use
If used, report binning/calibration protocol and retain detector precision/recall, false alarms, misses, and latency separately.

### Citation
Guo et al. (2017), Section 2.

## E4 — Temperature scaling is a simple post-hoc calibration method for classifier logits
- **Type:** faithful paraphrase
- **Location:** Abstract; calibration-method experiments
- **Claim:** On the classification benchmarks studied, a single temperature parameter fitted on validation data often substantially improves confidence calibration without changing the predicted class ordering.
- **Status:** verified

### Faithful paraphrase
Temperature scaling rescales a trained classifier's logits before the softmax using one learned scalar. The paper finds it surprisingly effective across many tested vision and language classification models when the temperature is selected on held-out validation data.

### Context and limits
This result concerns classifier logits. It does not justify applying temperature scaling arbitrarily to TD error, prediction error, or an unnormalized RL novelty score.

### Thesis use
Use temperature scaling only for detector outputs with an appropriate probabilistic/classification interpretation and a separate calibration split.

### Citation
Guo et al. (2017), Abstract and calibration-method experiments.

## E5 — Calibration measured on one distribution is not a guarantee under environmental shift
- **Type:** scope/protocol implication
- **Location:** The paper's stationary supervised-learning formulation
- **Claim:** Calibration is estimated with samples from the evaluated data distribution; the paper does not establish that a fitted calibration map remains valid after an arbitrary distribution shift.
- **Status:** verified

### Thesis use
Keep calibration data, detector-threshold tuning data, and final changepoint test sequences disjoint, and re-evaluate calibration under shifted regimes rather than assuming transfer.

### Citation
Guo et al. (2017), problem formulation and experiments.