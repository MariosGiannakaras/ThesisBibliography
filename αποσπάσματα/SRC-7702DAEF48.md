---
κωδικός: SRC-7702DAEF48
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

## E1 — Task performance and constraint satisfaction can be assigned to separate policies
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section III
- **Claim:** Recovery RL uses a task policy for reward maximization and a separate recovery policy that takes control when future constraint violation is predicted to be too likely.
- **Status:** verified

### Faithful paraphrase
Thananjeyan et al. separate the competing objectives of task-directed exploration and safety instead of embedding both in one reward. The task policy is trained for the unconstrained task objective. A learned safety critic estimates future violation risk, and a recovery policy is executed when the task policy proposes behavior whose predicted risk exceeds a threshold.

### Context and limits
The composite executed controller is not the same object as the raw task policy. Performance gains must therefore be attributed to the intervention architecture rather than to the task learner alone.

### Thesis use
Log raw task actions, recovery interventions, and executed actions separately for any fallback-controller baseline.

### Citation
Thananjeyan et al., Abstract, Introduction, and Section III.

## E2 — The safety critic estimates discounted future constraint risk
- **Type:** faithful paraphrase
- **Location:** Section III; Section IV-A
- **Claim:** The safety critic estimates a discounted future probability-like quantity for reaching constraint-violating states and is compared with an explicit risk threshold.
- **Status:** verified

### Faithful paraphrase
The paper augments the MDP with a binary constraint-cost signal and defines a safety action-value function that accumulates discounted future constraint costs. Under termination at a violation and with the risk discount set to one, this quantity corresponds to the probability of a future constraint violation. Recovery RL learns a sample-based approximation to this critic and uses the threshold `epsilon_risk` to decide whether the task policy may act.

### Context and limits
The learned critic is an estimate, not a formal oracle. Calibration error, distribution shift, and threshold selection can produce missed hazards or unnecessary interventions.

### Thesis use
Report critic calibration or empirical false-safe/false-intervention behavior if a learned risk monitor is included.

### Citation
Thananjeyan et al., Sections III and IV-A.

## E3 — Offline constraint-violation data can reduce unsafe online exploration
- **Type:** faithful paraphrase
- **Location:** Introduction; Section III; Section IV-C
- **Claim:** Recovery RL can initialize its safety machinery from offline transitions that contain examples of constraint violation without requiring demonstrations of successful task execution.
- **Status:** verified

### Faithful paraphrase
The method assumes access to offline experience containing examples of unsafe behavior. These data are used to learn about constraint-violating regions before the task policy begins unrestricted interaction. The offline set need not demonstrate how to solve the task; it only needs to provide information about ways constraints can be violated. The critic and recovery policy can then continue updating online.

### Thesis use
If prior unsafe examples are supplied to one baseline, account for them as additional information and interaction budget rather than treating the comparison as data-equivalent.

### Citation
Thananjeyan et al., Introduction and Sections III–IV.

## E4 — Recovery acts as a local return to safety rather than a full environment reset
- **Type:** faithful paraphrase
- **Location:** Related Work; Section IV-B
- **Claim:** The recovery policy guides the agent toward nearby safe state–action regions instead of requiring a complete reset to the initial-state distribution.
- **Status:** verified

### Faithful paraphrase
The authors contrast their method with reset policies that are trained to return the system all the way to its initial-state distribution. Recovery RL instead invokes a policy whose objective is to move the agent out of the learned recovery set and back toward a state–action region whose predicted violation risk is below the threshold. The intervention is therefore an approximate local reset.

### Context and limits
“Recovery” here means recovery to a safe operating region. It does not mean recovery of task performance after an environmental changepoint.

### Thesis use
Keep `safety_recovery` distinct from `environment_shift_recovery` in terminology and metrics.

### Citation
Thananjeyan et al., Related Work and Section IV-B.

## E5 — Recovery RL provides empirical safety–task trade-offs, not an unconditional formal guarantee
- **Type:** faithful paraphrase and scope boundary
- **Location:** Abstract; problem formulation; Related Work
- **Claim:** The method empirically improves the trade-off between task success and violations, while stronger formal guarantees require additional assumptions about dynamics and invariant safe sets.
- **Status:** verified

### Faithful paraphrase
The paper reports improved ratios of task success to constraint violation across simulation domains and a physical robot experiment. It also distinguishes Recovery RL from robust-control methods that obtain stronger theoretical guarantees by assuming known dynamics or a certified robust control-invariant safe set. Recovery RL learns its critic and recovery behavior from data, so its practical safety depends on those learned components.

### Thesis use
Report intervention count, intervention duration, violation count, empirical violation probability, task utility, and utility lost to conservatism.

### Citation
Thananjeyan et al., Abstract and Related Work.

## E6 — A recovery controller is not a change detector
- **Type:** thesis-scope synthesis
- **Location:** Overall method
- **Claim:** Recovery RL triggers on predicted constraint risk for the proposed action; it does not infer that the environment's dynamics or reward regime has changed.
- **Status:** verified

### Thesis use
Do not reuse a safety-critic intervention signal as a changepoint label without a separate detection validation.

### Citation
Thananjeyan et al., overall method.