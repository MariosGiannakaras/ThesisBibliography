---
κωδικός: SRC-E5CA725A6C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Deep Reinforcement Learning in Non-stationary Environments

## E1 — Unknown change points define a non-oracle non-stationary RL setting
- **Type:** faithful paraphrase
- **Location:** Abstract; Chapter 3, Sections 3.1–3.2
- **Claim:** The thesis formalizes sequential interaction with changing MDPs when the true environmental change times are not supplied to the agent.
- **Status:** verified

### Faithful paraphrase
Liu studies environments whose reward or transition structure can change abruptly and unpredictably over time. In the unknown-change-point setting, the agent does not receive the true change time as an oracle signal. It must infer when the environment has changed and then adapt its policy to the new regime.

### Context and limits
The evaluator can still know the injected ground-truth change times for scoring detector precision, recall, and delay; “unknown” refers to information withheld from the agent.

### Thesis use
Use this as a direct formal precedent for non-oracle detector-triggered adaptation experiments.

### Citation
Liu (2024), Abstract and Chapter 3.

## E2 — Change detection and policy adaptation are separate subsystems
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Sections 3.3.1–3.3.3
- **Claim:** Detection-Adaptation RL separates environment-change detection from a policy-adaptation mechanism that uses the detected change to guide transfer of previous knowledge.
- **Status:** verified

### Faithful paraphrase
DARL first constructs evidence that the state–action behavior distribution has changed and produces detected change points. Policy adaptation is then handled by a separate gradient-constrained mechanism that decides how previous policies should influence learning in the new environment. The detector and adapter therefore solve different problems even though the full method couples them.

### Thesis use
Maintain independent detector and adapter scorecards and include ablations that isolate each subsystem.

### Citation
Liu (2024), Chapter 3, Sections 3.3.1–3.3.3.

## E3 — F1 score does not measure detection latency
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Tables 3.3 and 3.5 and surrounding discussion
- **Claim:** Detectors with similar or perfect event-level F1 can still declare true changes at different times.
- **Status:** verified

### Faithful paraphrase
The reported CartPole and LunarLander experiments show that event-detection correctness and alarm timing are not identical. In some settings, methods attain the same or similar precision/recall-based scores while one detector identifies the injected change several episodes later than another.

### Context and limits
The numerical delays in the dissertation are benchmark-specific and should not be generalized as a universal algorithm ordering.

### Thesis use
Report precision, recall, F1, and detection delay separately; never use F1 as a substitute for latency.

### Citation
Liu (2024), Chapter 3, Tables 3.3 and 3.5.

## E4 — Combining change signals can improve detection fidelity in the reported ablation
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.3; Table 3.4; Figure 3.8
- **Claim:** In the reported DARL ablation, joint use of policy/behavior change and episodic state-distribution evidence reduced detection errors relative to using either signal alone.
- **Status:** verified

### Faithful paraphrase
The thesis evaluates components of its change detector separately and reports that neither a policy-oriented signal nor a state-distribution signal reliably identifies all true changes by itself in the tested benchmark. Their combined decision filters more false indications and improves event-level detection performance.

### Context and limits
This is evidence for the specific calibrated signals and tasks in the dissertation, not a general theorem that combining any two detector statistics is superior.

### Thesis use
If a multi-signal detector is tested, calibrate it on validation shifts and compare every component plus the joint rule under matched thresholds/tuning budgets.

### Citation
Liu (2024), Section 3.4.3.

## E5 — Previous policies can cause negative transfer after a regime change
- **Type:** faithful paraphrase
- **Location:** Chapter 3, adaptation ablations and Figures 3.6 and 3.10
- **Claim:** Preserving or transferring knowledge from an irrelevant previous policy can restrict learning in the new environment and degrade adaptation.
- **Status:** verified

### Faithful paraphrase
Liu explicitly studies cases where an earlier policy is poorly matched to the current environment. Strong constraints that force the new policy to remain compatible with such prior behavior can hinder learning, and the problem becomes more severe as additional regimes accumulate. The proposed adaptation mechanism therefore weights or relaxes prior-policy influence according to relevance.

### Thesis use
Require a scratch/no-transfer comparator and report a negative-transfer gap for every policy/context-reuse mechanism.

### Citation
Liu (2024), Chapter 3 adaptation analysis.

## E6 — False alarms and missed changes have different downstream costs
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.4
- **Claim:** A false detection can trigger unnecessary adaptation, whereas a missed change can leave the learner using an inappropriate policy and delay recovery.
- **Status:** verified

### Faithful paraphrase
The dissertation analyzes detection failures in terms of their consequences for the coupled adaptation process. A false positive is not merely a detector bookkeeping error: it can cause needless policy modification and performance loss. A false negative can be more damaging in another way because adaptation is not triggered when the environment actually changes.

### Thesis use
Report both false-alarm rate and missed-change rate together with the utility cost induced by each error type.

### Citation
Liu (2024), Section 3.4.4.

## E7 — Bayesian uncertainty is one possible detection signal, not change evidence by definition
- **Type:** faithful paraphrase and scope clarification
- **Location:** Abstract; later methodology chapters
- **Claim:** The thesis investigates changes in Bayesian uncertainty as one signal for non-stationarity, alongside behavior- and distribution-based methods.
- **Status:** verified

### Faithful paraphrase
One of the thesis approaches monitors how posterior uncertainty changes during learning and uses that behavior as evidence relevant to environment change. The broader dissertation also proposes other detectors, demonstrating that uncertainty change is a designed statistic within a detection procedure rather than a self-interpreting changepoint label.

### Thesis use
Any uncertainty-based detector still requires threshold calibration, false-alarm evaluation, and delay measurement.

### Citation
Liu (2024), Abstract and change-detection methodology chapters.

## E8 — Deep detector/adapter methods are evidence for protocol design, not mandatory tabular implementations
- **Type:** thesis-scope synthesis
- **Location:** Overall dissertation
- **Claim:** The proposed methods use deep policies, distributional tests, gradients, Gaussian-process/posterior machinery, and latent models that are substantially heavier than the resource-aware core baseline matrix.
- **Status:** verified

### Thesis use
Use the dissertation primarily to justify detector–adapter decomposition, non-oracle evaluation, failure metrics, and negative-transfer controls; only implement a lightweight analogue if feasibility tests support it.

### Citation
Liu (2024), overall dissertation.