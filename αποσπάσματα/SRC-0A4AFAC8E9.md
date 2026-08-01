---
κωδικός: SRC-0A4AFAC8E9
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Deep Reinforcement Learning at the Edge of the Statistical Precipice

## Evidence E1 — Few-run RL comparisons need uncertainty, not only point estimates
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1; Table 1
- **Claim:** Mean or median point estimates from a small number of stochastic training runs can give unreliable impressions of algorithm performance.
- **Thesis use:** statistical protocol
- **Topics:** few-run evaluation; uncertainty; reproducibility
- **Status:** verified

### Faithful paraphrase
With only a handful of runs per task and substantial run-to-run variability, aggregate RL scores are themselves uncertain quantities. Reporting only a mean or median can materially overstate or understate expected performance and can change the apparent ranking of algorithms under new independent runs.

### Thesis-safe implication
No superiority claim in the thesis should rest on one seed or on a point estimate without an uncertainty estimate and the underlying run distribution.

## Evidence E2 — Stratified bootstrap intervals preserve benchmark structure
- **Type:** faithful paraphrase
- **Location:** Section 4.1 and Table 1
- **Claim:** The paper recommends interval estimates based on stratified bootstrap resampling for aggregate performance in multi-task RL benchmarks.
- **Thesis use:** confidence intervals
- **Topics:** bootstrap; interval estimate; task/run structure
- **Status:** verified

### Faithful paraphrase
The proposed bootstrap procedure resamples in a way that respects the organization of scores by task and run. It produces an interval of plausible aggregate-performance values rather than treating the observed aggregate as exact. When comparing two agents, uncertainty in their difference should be estimated directly instead of reasoning mechanically from overlap between two separate intervals.

### Limitation
Bootstrap intervals do not repair biased experiment selection, unequal tuning budgets, or dependence created by an invalid sampling design.

## Evidence E3 — IQM is a useful robust aggregate but should not hide tail failures
- **Type:** faithful paraphrase
- **Location:** Table 1; Section 4.3
- **Claim:** Interquartile mean is proposed as a robust and statistically efficient aggregate in the few-run regime.
- **Thesis use:** secondary aggregate metric
- **Topics:** IQM; outliers; aggregate performance
- **Status:** verified

### Faithful paraphrase
IQM averages the middle half of the pooled normalized scores, making it less dominated by extreme tasks than the ordinary mean and often less statistically variable than the median. The authors recommend it as part of a broader reporting set rather than as a complete description of performance.

### Thesis-safe implication
Because resilience research cares about rare catastrophic failures, IQM should be paired with failure rates, tail/worst-case summaries, and per-scenario results.

## Evidence E4 — Evaluation protocol differences can exceed algorithm differences
- **Type:** faithful paraphrase
- **Location:** Section 3 and benchmark case study
- **Claim:** Non-standard choices such as checkpoint/evaluation rules can materially alter reported performance and apparent rankings.
- **Thesis use:** benchmark fairness
- **Topics:** checkpoint selection; evaluation protocol; bias
- **Status:** verified

### Faithful paraphrase
Comparisons become unreliable when one method is scored using a different evaluation rule from another, such as selecting a maximum training score instead of using a common final-evaluation protocol. All agents should use the same evaluation budget, checkpoint-selection rule, normalization, and aggregation procedure, with any model selection performed only on validation data.

## Evidence E5 — A fixed seed is not equivalent to statistical reliability
- **Type:** faithful paraphrase
- **Location:** Section 2 and later reproducibility discussion
- **Claim:** Independent runs can differ because of task stochasticity, exploration, initialization, and software or hardware nondeterminism; fixing a seed does not answer whether conclusions generalize to new random conditions.
- **Thesis use:** seed protocol
- **Topics:** independent runs; random conditions; reproducibility
- **Status:** verified

### Faithful paraphrase
Recording seeds is important for reproducibility, but a result obtained under one fixed random condition does not establish expected performance over future random conditions. Evaluation should therefore use multiple independent runs and report their uncertainty.

## Evidence E6 — Effect size and uncertainty are preferable to dichotomous significance claims
- **Type:** faithful paraphrase
- **Location:** Section 2, confidence-interval discussion
- **Claim:** The authors emphasize interval estimates and effect sizes and caution against binary interpretations based only on statistical-significance thresholds.
- **Thesis use:** result interpretation
- **Topics:** effect size; confidence interval; practical significance
- **Status:** verified

## Avoid overclaiming
This source provides statistical evaluation methodology, not a resilience algorithm. Its benchmark-level aggregate recommendations should complement, not replace, per-shift recovery, safety, and failure analysis.
