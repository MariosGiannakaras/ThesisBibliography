---
κωδικός: SRC-3BF9404CC3
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Learning to Recover for Safe Reinforcement Learning

## E1 — Safety critic, recovery policy, and task policy are separate components
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Safe Reinforcement Learning Architecture
- **Claim:** TU-Recovery trains a safety critic and a task-unaware recovery policy before task learning, then uses them as a safety controller supervising a separate task policy.
- **Status:** verified

### Faithful paraphrase
Wang et al. propose a three-stage architecture. An initial exploration stage learns a safety critic from cost-oriented interaction. A recovery-learning stage trains a policy to minimize that critic. During later task training, an action decider chooses between the task policy's proposed action and the recovery policy's action according to the critic and a risk threshold.

### Context and limits
The task learner does not interact with the original environment dynamics alone: the safety controller changes which proposed actions are actually executed.

### Thesis use
Log the task proposal, recovery proposal, intervention decision, and executed action separately for any recovery-controller baseline.

### Citation
Wang et al. (2023), Abstract and Safe Reinforcement Learning Architecture.

## E2 — Controller disagreement can create oscillation near the recovery boundary
- **Type:** faithful paraphrase
- **Location:** Learning Recover Actions through Auxiliary Reward; Figure 3
- **Claim:** A task policy and recovery policy can propose opposing actions near the boundary of the recovery zone, causing repeated back-and-forth motion and reduced learning efficiency.
- **Status:** verified

### Faithful paraphrase
The paper calls this the adversarial phenomenon. In the navigation example, the task policy attempts to move toward the goal while the recovery policy pushes away from the risky area. If control alternates near the threshold boundary, the agent can become trapped in a small region and repeatedly undo its previous motion.

### Thesis use
For intervention-based safety, measure action disagreement, intervention bursts, oscillation/stuck rate, and controller-induced delay rather than reporting violation count alone.

### Citation
Wang et al. (2023), auxiliary-reward section and Figure 3.

## E3 — The recovery threshold defines a hard intervention rule
- **Type:** faithful paraphrase
- **Location:** Task Training Stage; Equation 3
- **Claim:** The task action is executed when its predicted safety cost remains below the threshold; otherwise the recovery action replaces it.
- **Status:** verified

### Faithful paraphrase
TU-Recovery follows a hard decision rule based on the learned safety critic. If the task action is judged sufficiently safe, it passes through unchanged. If its critic value exceeds the threshold, the controller discards the task proposal and executes the recovery policy's action instead.

### Context and limits
Threshold selection changes both safety and task progress, and critic error can produce false interventions or missed unsafe actions.

### Thesis use
Report threshold, intervention rate, false-intervention proxy, missed violations, and clean-performance cost.

### Citation
Wang et al. (2023), Task Training Stage, Equation 3.

## E4 — Auxiliary reward can reduce policy conflict but changes the task-learning signal
- **Type:** faithful paraphrase
- **Location:** Auxiliary Reward section; experiments
- **Claim:** The paper adds an auxiliary reward intended to teach the task policy recovery-compatible actions and reduce disagreement with the recovery controller.
- **Status:** verified

### Faithful paraphrase
The authors introduce additional reward when the task policy proposes actions that align better with safe recovery behavior. This encourages the task learner to avoid repeatedly entering situations where the safety controller must override it and can reduce the adversarial phenomenon observed near recovery boundaries.

### Context and limits
Because the auxiliary term modifies the learning objective, improved safety cannot be interpreted independently of possible changes to task optimality or nominal return.

### Thesis use
Treat auxiliary reward as a separate ablation and report both safety improvement and task-utility change.

### Citation
Wang et al. (2023), auxiliary-reward section and experiments.

## E5 — Pretraining the safety machinery requires an additional information and interaction budget
- **Type:** faithful paraphrase
- **Location:** Exploration Stage; Recovery Learning Stage
- **Claim:** TU-Recovery trains its safety critic and recovery policy in safety-oriented stages before task training begins.
- **Status:** verified

### Faithful paraphrase
The architecture spends dedicated interaction and optimization effort learning the safety critic and then the recovery policy before the task policy is trained. These stages receive safety-related signals and are distinct from the later task-oriented training phase.

### Thesis use
Account for pretraining interactions and compute when comparing against baselines that receive no prior hazard data or safety-learning phase.

### Citation
Wang et al. (2023), Exploration Stage and Recovery Learning Stage.

## E6 — Recovery-to-safety is not environmental-change adaptation
- **Type:** scope synthesis grounded in the method
- **Location:** Overall formulation
- **Claim:** The recovery policy returns the agent toward a lower-risk region; the method does not infer that reward or transition dynamics have changed and does not measure relearning after a changepoint.
- **Status:** verified

### Thesis use
Keep `safety_controller_recovery` distinct from `post_shift_policy_recovery` in agent names, metrics, and conclusions.

### Citation
Wang et al. (2023), overall method.