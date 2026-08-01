---
κωδικός: SRC-8E22CBA55A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Safe Model-based Reinforcement Learning with Stability Guarantees

## E1 — Safety is defined through asymptotic stability and a region of attraction
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section 2
- **Claim:** The paper treats safety as keeping trajectories inside a forward-invariant region from which the closed-loop system converges to an equilibrium.
- **Status:** verified

### Faithful paraphrase
Berkenkamp et al. use a control-theoretic definition of safety based on Lyapunov stability. A policy is certified on a region of attraction when trajectories starting inside that region remain inside it and eventually converge to the goal equilibrium. This is a different safety semantics from an expected cumulative CMDP cost.

### Thesis use
Keep Lyapunov/stability safety separate from expected-cost, chance-constrained, or empirical-violation formulations.

### Citation
Berkenkamp et al. (2017), Abstract, Introduction, and Section 2.

## E2 — Safe exploration is restricted to points whose consequences can be certified
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 2–3
- **Claim:** New dynamics data are collected only at state–action points that remain within the certified stability region under the statistical model and Lyapunov conditions.
- **Status:** verified

### Faithful paraphrase
The method combines confidence intervals for the learned dynamics with a Lyapunov decrease condition. Candidate exploratory actions are accepted only when the uncertainty bounds support a high-probability certificate that the resulting behavior remains inside the currently safe region. Information gathering is therefore constrained by the safety certificate rather than being unrestricted trial and error.

### Thesis use
Report certified-region size, denied/intervened actions, exploration coverage, and opportunity cost for certificate-based safe learning.

### Citation
Berkenkamp et al. (2017), Sections 2–3.

## E3 — The method requires an initial locally safe policy and structural assumptions
- **Type:** faithful paraphrase
- **Location:** Section 2, assumptions and Initial safe policy
- **Claim:** Safe learning starts from a policy already known to stabilize at least a small region and relies on regularity and calibrated dynamics-model assumptions.
- **Status:** verified

### Faithful paraphrase
The theoretical setup assumes an initial controller that makes the equilibrium asymptotically stable in a nonempty local set. It also assumes Lipschitz continuity and a statistical dynamics model whose confidence intervals cover the true dynamics with high probability. These assumptions provide prior safety structure before the learning algorithm begins expanding the certified region.

### Thesis use
Count a pre-existing fallback/safe policy and prior dynamics structure as prior information when comparing against baselines without such knowledge.

### Citation
Berkenkamp et al. (2017), Section 2.

## E4 — A dynamics shift can invalidate a pre-change certificate
- **Type:** thesis-protocol implication grounded in the certificate assumptions
- **Location:** Sections 2–3
- **Claim:** The high-probability safety certificate is conditional on the learned dynamics confidence set containing the true dynamics.
- **Status:** verified

### Thesis use
After a dynamics changepoint, do not assume the old certified region remains valid. Track out-of-certificate visits and certificate revalidation latency if this safety paradigm is studied.

### Citation
Berkenkamp et al. (2017), Sections 2–3.

## E5 — Stability recovery is not post-shift learning recovery
- **Type:** scope synthesis grounded in the paper
- **Location:** Introduction and overall formulation
- **Claim:** “Recovery” in the control-theoretic motivation means returning toward a safe equilibrium/region; it does not mean restoring task-policy performance after a non-stationary environmental shift.
- **Status:** verified

### Thesis use
Do not use a Lyapunov stability guarantee as evidence of fast adaptation, changepoint detection, or relearning after a changing GridWorld regime.

### Citation
Berkenkamp et al. (2017), Introduction and overall formulation.