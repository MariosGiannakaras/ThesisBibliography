---
κωδικός: SRC-A5DF23299C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management

## E1 — Robustness and resilience emphasize different temporal properties

- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** The paper describes robustness as maintaining performance under perturbations and resilience as preparing for, adapting to, and recovering from perturbations or unexpected changes.
- **Status:** verified

### Faithful paraphrase

Tjhay, Bessa, and Paulos distinguish an agent that remains stable while perturbed from an agent whose performance degrades and is subsequently restored. Their resilience framing emphasizes the temporal response to disruption, while robustness focuses on limiting performance impact under the perturbation itself.

### Context and limits

The terminology is used in a power-grid decision-support setting and should not be presented as the only possible formal definition of resilience.

### Thesis use

Keep immediate disturbed performance separate from the post-change recovery process.

### Citation

Tjhay, Bessa, and Paulos (2025), Abstract and Introduction.

## E2 — Resilience depends on both magnitude and duration of degradation

- **Type:** faithful paraphrase
- **Location:** Section III-C
- **Claim:** The proposed resilience assessment compares a perturbed performance trajectory with an unperturbed reference and accounts for how far and how long performance deviates.
- **Status:** verified

### Faithful paraphrase

The methodology evaluates reward behavior after the perturbation against a reference trajectory from the unperturbed system. Resilience is therefore not represented only by the final reward: the depth and temporal extent of the performance loss contribute to the assessment.

### Thesis use

Use matched reference runs and report transient deficit together with final recovery quality.

### Citation

Tjhay et al. (2025), Section III-C.

## E3 — Area between reference and perturbed curves is a resilience metric

- **Type:** faithful paraphrase
- **Location:** Section III-C, Equation 11
- **Claim:** The paper defines a resilience quantity from the area between perturbed and unperturbed reward trajectories after a disturbance.
- **Status:** verified

### Faithful paraphrase

The integral of the reward difference after perturbation summarizes accumulated performance loss over the observation window. A larger or longer degradation increases this area even if the agent later returns to a high score.

### Context and limits

The value depends on the reference trajectory, window definition, and reward scale.

### Thesis use

Use a normalized post-change performance-gap AUC alongside raw recovery curves and matched-seed references.

### Citation

Tjhay et al. (2025), Section III-C, Equation 11.

## E4 — Degradation time and restorative time describe different phases

- **Type:** faithful paraphrase
- **Location:** Section III-C, Equations 12–15
- **Claim:** The framework separates the interval from perturbation onset to minimum performance from the interval between that minimum and later restored performance.
- **Status:** verified

### Faithful paraphrase

The assessment identifies how quickly the agent reaches its post-perturbation minimum and how long it then takes to restore performance toward its later recovered level. These timing quantities complement the magnitudes of the minimum and recovered scores.

### Thesis use

Report `time_to_minimum`, `restorative_time`, minimum post-change performance, and maximum recovered performance separately.

### Citation

Tjhay et al. (2025), Section III-C, Equations 12–15.

## E5 — Natural measurement errors and intentional attacks are different threat models

- **Type:** faithful paraphrase
- **Location:** Section III-A
- **Claim:** The evaluation includes random perturbations representing missing or erroneous measurements and separate adversarial agents that intentionally manipulate observations.
- **Status:** verified

### Faithful paraphrase

The random perturbation agent models natural or operational data problems, whereas the other perturbation agents deliberately construct adversarial inputs. The mechanisms differ in intent and information assumptions even though both alter the AI agent's observed input rather than the underlying physical state.

### Thesis use

Transfer only the non-adversarial measurement-noise case directly into the main uncertainty benchmark unless an explicit attacker model is added as a separate threat model.

### Citation

Tjhay et al. (2025), Section III-A.

## E6 — Behavioral recovery under test-time perturbation does not prove parameter adaptation

- **Type:** faithful paraphrase
- **Location:** Introduction; Section III; experimental framing
- **Claim:** The study primarily assesses pretrained agents at test time, so changes in reward after a perturbation should not automatically be interpreted as continued learning or parameter adaptation.
- **Status:** verified

### Faithful paraphrase

The methodology is presented as conformity-style assessment of pretrained AI agents under injected perturbations. A performance trajectory may improve after a transient disturbance even when the learned parameters remain fixed, so behavioral restoration and online learning are distinct mechanisms.

### Thesis use

Every recovery curve should state whether Q-values, weights, memory, or other policy parameters continue to update after the change.

### Citation

Tjhay et al. (2025), Introduction and assessment methodology.
