---
κωδικός: SRC-BB9CAB4CBB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Decision-making under uncertainty: beyond probabilities

## Evidence E1 — Aleatoric and epistemic uncertainty are different uncertainty types
- **Type:** faithful paraphrase
- **Location:** Introduction; Section 2.3
- **Claim:** Aleatoric uncertainty is intrinsic variability, whereas epistemic uncertainty arises from lack of knowledge and can in principle be reduced by acquiring more information.
- **Thesis use:** uncertainty taxonomy
- **Topics:** aleatoric uncertainty; epistemic uncertainty
- **Status:** verified

### Faithful paraphrase
Aleatoric uncertainty describes randomness inherent in the process, such as stochastic action outcomes or noisy measurements. Epistemic uncertainty describes uncertainty caused by incomplete knowledge of the system and can be reduced by collecting additional data or otherwise improving the model.

## Evidence E2 — A probability kernel and uncertainty about that kernel are not the same thing
- **Type:** faithful paraphrase
- **Location:** Introduction; Sections 2.3 and 3
- **Claim:** Classical MDPs/POMDPs use probability distributions to represent aleatoric uncertainty, while uncertain or robust model families can additionally represent epistemic uncertainty over the probabilities themselves.
- **Thesis use:** transition-noise/model-uncertainty boundary
- **Topics:** MDP; uncertain MDP; transition uncertainty
- **Status:** verified

### Faithful paraphrase
A stochastic transition kernel specifies the random outcomes expected under a given model. If the transition probabilities themselves are only approximately known, a single point estimate is insufficient; an uncertainty model can instead represent a set or family of plausible probability distributions.

## Evidence E3 — Exploration can reduce epistemic uncertainty but not intrinsic randomness
- **Type:** faithful paraphrase
- **Location:** Section 2.3 and RL discussion
- **Claim:** Additional interaction or measurements can improve knowledge of an uncertain system, but cannot eliminate genuinely aleatoric variability.
- **Thesis use:** interpretation of exploration
- **Topics:** exploration; information gathering; reducible uncertainty
- **Status:** verified

### Faithful paraphrase
When uncertainty is epistemic, gathering more informative observations can narrow what the agent does not know. In contrast, repeated sampling does not remove irreducible stochasticity in the environment; it can only estimate its distribution more accurately.

## Evidence E4 — Robust uncertainty handling can introduce conservativeness
- **Type:** faithful paraphrase
- **Location:** planning/robustness discussion
- **Claim:** Worst-case reasoning over uncertainty models can provide protection but may produce overly conservative decisions.
- **Thesis use:** nominal-vs-disturbed performance reporting
- **Topics:** robust optimization; conservativeness; utility
- **Status:** verified

### Faithful paraphrase
Policies designed to perform acceptably across a broad set of plausible models can sacrifice performance in the nominal or most likely model. Robustness results should therefore be reported together with the utility cost of the conservatism that produces them.

## Evidence E5 — Rare observations and true distribution change are difficult to distinguish
- **Type:** faithful paraphrase
- **Location:** challenges/perspectives discussion on changing uncertainty
- **Claim:** In changing distributions, an important challenge is deciding whether surprising observations are normal stochastic outcomes or evidence that the underlying model has changed.
- **Thesis use:** change-detection protocol
- **Topics:** prediction error; false alarm; distribution change
- **Status:** verified

### Faithful paraphrase
An unusual observation under a stochastic model is not sufficient by itself to establish that the environment changed. A detector must accumulate or calibrate evidence so that ordinary low-probability outcomes are not systematically mistaken for regime changes.

### Thesis-safe implication
A prediction-error spike can be a useful signal, but it is not a calibrated change detector until false alarms, missed changes, thresholds, and detection delay are evaluated explicitly.

## Evidence E6 — The paper surveys model families and research challenges, not an empirical algorithm ranking
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1 and 6
- **Claim:** The contribution is a perspective and taxonomy spanning uncertainty models and solution approaches.
- **Thesis use:** claim boundary
- **Topics:** taxonomy; planning; RL; formal methods
- **Status:** verified

## Avoid overclaiming
This source supports distinctions between uncertainty types and modeling assumptions. It does not establish that one robust or uncertainty-aware algorithm is universally preferable for the thesis benchmark.
