---
κωδικός: SRC-7C18826BEE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning

## E1 — MC dropout provides an approximate Bayesian predictive distribution
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 3–4
- **Claim:** Keeping dropout stochastic at prediction time and averaging multiple forward passes can approximate predictive moments under the paper's variational Bayesian interpretation.
- **Status:** verified

### Faithful paraphrase
Gal and Ghahramani interpret ordinary dropout training as approximate variational inference in a deep Gaussian-process model. At test time, repeated stochastic dropout masks generate samples from the approximate predictive distribution. The empirical mean of those forward passes estimates predictive mean, and the sample moments can be used to estimate predictive variance.

### Context and limits
This is an approximation to Bayesian inference, not exact posterior computation. Its behavior depends on the trained network, dropout probabilities, model precision assumptions, regularization, and the number of Monte Carlo samples.

### Thesis use
If MC dropout is used for a neural detector or Q-function, report dropout rate, number of stochastic passes, architecture, regularization, and inference-time compute.

### Citation
Gal and Ghahramani (2016), Abstract and Sections 3–4.

## E2 — High softmax probability or a large point prediction is not epistemic certainty
- **Type:** faithful paraphrase
- **Location:** Introduction; Figure 1
- **Claim:** A point-estimate neural network can produce highly confident-looking outputs far from the training data even when model uncertainty should be large.
- **Status:** verified

### Faithful paraphrase
The paper illustrates that passing a single extrapolated function estimate through a softmax can yield near-certain class probability for an input far outside the training region. Representing uncertainty over functions produces a different picture: predictive uncertainty can grow outside the observed data even when one sampled function gives an extreme output.

### Thesis use
Do not interpret Q-value magnitude, action probability, or softmax confidence as a calibrated epistemic-uncertainty estimate.

### Citation
Gal and Ghahramani (2016), Introduction and Figure 1.

## E3 — Uncertainty can support exploration in deep reinforcement learning
- **Type:** faithful paraphrase
- **Location:** Introduction; reinforcement-learning experiment
- **Claim:** The paper uses uncertainty over a neural Q-function to motivate uncertainty-aware action selection rather than purely epsilon-greedy exploration.
- **Status:** verified

### Faithful paraphrase
The authors note that model uncertainty can inform the exploration–exploitation decision in reinforcement learning and demonstrate a dropout-based uncertainty treatment for a neural Q-value setting. The key motivation is that uncertainty over value estimates provides information not contained in the point estimate alone.

### Context and limits
Uncertainty-aware exploration is not the same as detecting that an environment has changed.

### Thesis use
Treat MC-dropout uncertainty as an optional exploration/diagnostic signal if a neural agent is included, not as a changepoint decision rule by itself.

### Citation
Gal and Ghahramani (2016), Introduction and RL experiment.

## E4 — Uncertainty estimates depend on inference and architecture choices
- **Type:** faithful paraphrase and protocol implication
- **Location:** Abstract; Sections 3–4; empirical study
- **Claim:** The paper evaluates uncertainty behavior across architectures and nonlinearities and derives predictive estimates using a finite number of stochastic passes.
- **Status:** verified

### Thesis use
Include architecture, dropout probability, number of MC samples, and uncertainty normalization in the reproducibility record and do not compare detectors with unmatched inference budgets.

### Citation
Gal and Ghahramani (2016), Sections 3–4 and experiments.

## E5 — Predictive variance is not a calibrated changepoint alarm
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall paper
- **Claim:** MC dropout estimates model uncertainty for predictions; the paper does not define a sequential change detector with false-alarm and delay guarantees.
- **Status:** verified

### Thesis use
Any detector built from MC-dropout variance still requires a temporal aggregation rule, threshold calibration, false-alarm rate, missed-change rate, detection delay, and reset/cooldown semantics.

### Citation
Gal and Ghahramani (2016), overall scope.