---
κωδικός: SRC-CD5F67F3E6
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Proximal Policy Optimization Algorithms

## E1 — PPO alternates data collection with repeated minibatch optimization
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1 and 5
- **Claim:** PPO collects trajectories with the current policy and then performs multiple epochs of stochastic minibatch optimization on a surrogate objective using that batch.
- **Status:** verified

### Faithful paraphrase
Schulman et al. propose a family of policy-gradient methods that alternate environment interaction with optimization. Unlike a basic policy-gradient update that uses each sample for one update, PPO is designed so that the same collected batch can support several minibatch epochs before new trajectories are gathered.

### Context and limits
The number of actors, rollout length, minibatch size, optimization epochs, and advantage estimator are part of the experimental implementation and should be reported when PPO is used as a baseline.

### Thesis use
If a neural PPO baseline is retained, account for its interaction and optimization budget separately from tabular methods.

### Citation
Schulman et al. (2017), Abstract, Sections 1 and 5.

## E2 — Clipping limits the incentive for large policy-ratio changes
- **Type:** faithful paraphrase
- **Location:** Section 3, Equation 7
- **Claim:** PPO-Clip replaces the unconstrained surrogate with the minimum of the ordinary probability-ratio objective and a clipped version, reducing the optimization incentive to move the new policy too far from the old policy on sampled actions.
- **Status:** verified

### Faithful paraphrase
The clipped surrogate uses the ratio between new and old action probabilities and clips that ratio to an interval around one. Taking the minimum of the clipped and unclipped terms yields a pessimistic surrogate: improvements that rely only on pushing the probability ratio beyond the clipping range are no longer rewarded, while harmful moves remain visible to the objective.

### Context and limits
This is a mechanism for controlling the size and stability of an optimization update in policy space. It is not a guarantee that the learned policy is robust to environmental perturbations.

### Thesis use
Never interpret PPO clipping as `environmental robustness`; use it only to describe the policy-optimization method.

### Citation
Schulman et al. (2017), Section 3, Equation 7.

## E3 — Adaptive KL penalty is a distinct PPO variant
- **Type:** faithful paraphrase
- **Location:** Section 4
- **Claim:** PPO can alternatively penalize KL divergence and adapt the penalty coefficient to keep the observed policy change near a target divergence.
- **Status:** verified

### Faithful paraphrase
The adaptive-KL variant optimizes a surrogate containing a KL penalty and then adjusts its coefficient depending on whether the measured KL divergence falls below or above a target range. The authors retain this as an important baseline but report that it performed worse than clipping in their tested configurations.

### Context and limits
The reported ordering concerns the paper's benchmark and hyperparameter search; it is not a universal ranking of all PPO implementations.

### Thesis use
State explicitly whether the baseline uses clipping, a KL penalty, or another PPO implementation rather than treating all variants as identical.

### Citation
Schulman et al. (2017), Section 4.

## E4 — The surrogate-objective comparison used a small stationary benchmark
- **Type:** faithful paraphrase
- **Location:** Section 6.1; Table 1
- **Claim:** The clipping comparison was run on seven MuJoCo tasks with three random seeds per task and one million training timesteps per task.
- **Status:** verified

### Faithful paraphrase
For the computationally cheaper surrogate-objective study, each algorithm setting was evaluated on seven continuous-control environments and three seeds per environment. The authors normalized the final scores and found the clipped objective with `epsilon = 0.2` highest among the tested surrogate configurations.

### Context and limits
Twenty-one task-seed runs are limited evidence for cross-domain claims, and the benchmark does not contain controlled environmental changepoints or recovery evaluation.

### Thesis use
Do not copy `epsilon = 0.2` as an untuned universal constant; treat it as a default candidate to be validated within a predefined tuning budget.

### Citation
Schulman et al. (2017), Section 6.1 and Table 1.

## E5 — PPO is a learning baseline, not a resilience mechanism
- **Type:** scope inference grounded in the paper
- **Location:** Abstract; Sections 6–7
- **Claim:** The paper evaluates sample complexity and reward performance on continuous-control and Atari tasks but does not introduce environmental-change detection, regime recall, post-shift reset, or recovery metrics.
- **Status:** verified

### Faithful paraphrase
The empirical contribution of PPO is improved and relatively simple policy optimization across standard benchmark tasks. The experimental protocol trains policies within the task being evaluated; it does not define an externally changing environment and then measure detection delay or relearning after the shift.

### Thesis use
If PPO is included, use it as a deep continual-learning comparator whose resilience must be measured by the thesis protocol rather than assumed from the PPO paper.

### Citation
Schulman et al. (2017), Abstract and experiments.

## E6 — Optimizer stability and environmental robustness are different concepts
- **Type:** thesis-scope synthesis
- **Location:** Sections 2–4
- **Claim:** Trust-region, clipping, and KL language in PPO refers to constraining policy updates, not uncertainty sets over transition or reward dynamics.
- **Status:** verified

### Thesis use
Keep `policy_update_stability` separate from `robust_to_environment_shift` in terminology, figures, and conclusions.

### Citation
Schulman et al. (2017), Sections 2–4.