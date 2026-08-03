---
κωδικός: SRC-90A20ED43A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Survival of the Fittest: Evolutionary Adaptation of Policies for Environmental Shifts

## Evidence E1 — Severe environmental shifts motivate post-shift retraining
- **Type:** faithful paraphrase
- **Location:** Abstract; Section 1
- **Claim:** The paper distinguishes substantial environmental distribution shifts from the bounded perturbations commonly targeted by domain randomization and robust RL, and treats retraining in the shifted environment as a separate response.
- **Thesis use:** robustness/adaptation taxonomy
- **Topics:** environmental shift; retraining; robust RL boundary
- **Status:** verified

### Faithful paraphrase
The authors argue that a policy that was optimal in the original environment can become suboptimal or fail after a drastic change in the environment's dynamics or layout. Their response is not a frozen worst-case policy: ERPO collects trajectories in the shifted environment and iteratively adapts a policy to that new environment.

### Limitation
This is post-shift adaptation and does not guarantee that the initial performance drop is avoided.

## Evidence E2 — ERPO trades off adherence to the old policy and exploration of a new policy
- **Type:** faithful paraphrase
- **Location:** Section 3.2
- **Claim:** ERPO constructs its training behavior by combining the previous optimal policy with a new policy and progressively reducing adherence to the old policy.
- **Thesis use:** optional policy-reuse feasibility baseline
- **Topics:** warm start; policy reuse; exploration
- **Status:** verified

### Faithful paraphrase
The method begins adaptation with a policy that retains substantial influence from the old optimal policy while allowing a newly initialized policy to contribute. A temperature/adherence schedule shifts weight away from the old policy as new batches of trajectories are collected and the new policy is updated.

### Limitation
The adherence schedule is a consequential tuning choice and should not be selected on the final test shifts.

## Evidence E3 — Policy updates prioritize high-fitness experience
- **Type:** faithful paraphrase
- **Location:** Sections 3–5
- **Claim:** ERPO adapts its policy using a replicator-dynamics-inspired update that gives greater influence to state-action behavior associated with relatively high-return trajectories.
- **Thesis use:** informative-experience adaptation rationale
- **Topics:** replicator dynamics; trajectory weighting; adaptation
- **Status:** verified

### Faithful paraphrase
Rather than treating every trajectory in an adaptation batch as equally informative, the evolutionary update increases the influence of choices associated with higher fitness or return relative to the current batch and decreases the influence of poorer choices.

## Evidence E4 — The experiments include severe structural changes in discrete navigation tasks
- **Type:** faithful paraphrase
- **Location:** Section 4
- **Claim:** The evaluation includes discrete navigation environments with substantial layout changes and compares adaptation against scratch and pretrained/warm-start baselines where applicable.
- **Thesis use:** severe-shift comparator design
- **Topics:** navigation; structural shift; scratch; warm start
- **Status:** verified

### Faithful paraphrase
The paper evaluates ERPO in environments such as FrozenLake, Taxi, CliffWalking and MiniGrid variants including DistributionShift and Walls&Lava. The comparison includes mainstream RL algorithms trained from scratch in the shifted environment, retrained from a model learned in the original environment, and, where relevant, domain-randomized variants.

## Evidence E5 — Reported ERPO gains are benchmark-specific, not a universal ranking
- **Type:** faithful paraphrase
- **Location:** Sections 5–6
- **Claim:** The authors report faster adaptation, higher rewards, and lower adaptation cost for ERPO in many of their evaluated scenarios, but the claim is tied to the paper's discrete tasks and implementation choices.
- **Thesis use:** feasibility evidence
- **Topics:** adaptation efficiency; shift severity; algorithm comparison
- **Status:** verified

### Faithful paraphrase
Across the reported path-finding experiments, ERPO often reaches strong post-shift performance with fewer adaptation episodes or lower computational cost than the particular baseline configurations used in the paper. This supports testing policy reuse as a feasibility option, not assuming in advance that it will dominate a resource-matched GridWorld benchmark.

## Evidence E6 — The current method is scoped to discrete single-agent settings
- **Type:** faithful paraphrase
- **Location:** Section 6, limitations/future work
- **Claim:** The reported implementation is limited to discrete state/action spaces and single-agent models.
- **Thesis use:** scope boundary
- **Topics:** discrete RL; single agent; external validity
- **Status:** verified

### Faithful paraphrase
The authors identify extensions to continuous and multi-agent settings as future work. The present evidence therefore transfers most directly to the thesis's discrete single-agent setting and should not be generalized beyond that scope.

## Avoid overclaiming
ERPO is an adaptive retraining method after substantial shift. It is not evidence that static robustness and resilience are equivalent, that policy reuse removes the need for post-shift exploration, or that one adherence schedule is universally optimal.
