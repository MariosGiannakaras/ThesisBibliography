---
κωδικός: SRC-2C9FFED27E
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Efficient Policy Optimization in Robust Constrained MDPs with Iteration Complexity Guarantees

## E1 — Robust feasibility must hold under model mismatch, not only in the nominal simulator
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction; Section 2
- **Claim:** An RCMDP seeks a policy whose objective and safety constraints remain acceptable against worst-case transition models in an uncertainty set around the nominal model.
- **Status:** verified

### Faithful paraphrase
Ganguly et al. motivate robust constrained control by noting that a policy satisfying a safety constraint in a simulator can violate it after deployment when the real transition dynamics differ. Their RCMDP formulation therefore evaluates the task objective and every constraint against adverse transition kernels inside a prescribed uncertainty set.

### Thesis use
For safety-oriented robust baselines, report nominal feasibility and disturbed/worst-case feasibility separately.

### Citation
Ganguly et al. (2025), Abstract, Introduction, and Section 2.

## E2 — Reward and constraint functions can have different worst-case transition models
- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** The transition model that is worst for the task objective need not be the model that is worst for a safety constraint.
- **Status:** verified

### Faithful paraphrase
The paper explains why a standard robust value-iteration update on a single composite Lagrangian is problematic in RCMDPs. Because the robust objective and each robust constraint independently maximize over model uncertainty, their worst-case transition kernels can differ. Collapsing them into one shared worst-case model can therefore misrepresent the constrained robust problem.

### Thesis use
Do not use one undifferentiated “worst-case return” as a substitute for separately evaluating task utility and safety costs.

### Citation
Ganguly et al. (2025), Abstract and Introduction.

## E3 — The proposed optimization gives priority to removing constraint violations
- **Type:** faithful paraphrase
- **Location:** Introduction, Contributions; Equation 3
- **Claim:** The RNPG formulation focuses on the largest constraint violation while the policy is infeasible and optimizes the robust task objective once the constraints are satisfied.
- **Status:** verified

### Faithful paraphrase
The proposed max-type reformulation exposes the current dominant objective. When at least one robust constraint exceeds its bound, the update is driven by reducing violation. When all constraints are feasible, the robust task objective becomes the active quantity. The method is designed to obtain a feasible policy without the binary search used by the compared epigraph approach.

### Thesis use
Report objective return, each constraint margin, and the fraction of evaluation runs that remain feasible instead of hiding them inside one aggregate score.

### Citation
Ganguly et al. (2025), Introduction and Equation 3.

## E4 — Computational efficiency is part of the contribution
- **Type:** faithful paraphrase
- **Location:** Abstract; Table 1; Contributions
- **Claim:** RNPG is designed to improve iteration complexity and wall-clock cost relative to the compared EPIRC-PGS solver.
- **Status:** verified

### Faithful paraphrase
The authors avoid the outer binary-search procedure of the competing epigraph method and use a KL-regularized policy update. Their finite-state experiments report materially lower execution times across several environments, with the advantage increasing for some high-discount settings.

### Context and limits
These runtime numbers depend on the implementation, hardware, solver settings, discount factor, and environments used in the paper.

### Thesis use
Include measured wall-clock/update cost and memory alongside final utility and feasibility when comparing safety or robust methods.

### Citation
Ganguly et al. (2025), Abstract, Table 1, and Contributions.

## E5 — The uncertainty-set structure is an explicit assumption
- **Type:** faithful paraphrase
- **Location:** Section 2, Equation 6
- **Claim:** The main formulation uses an `(s,a)`-rectangular ambiguity set around a nominal model, with extensions possible when a suitable robust policy evaluator exists.
- **Status:** verified

### Faithful paraphrase
The paper defines local uncertainty sets around nominal transition distributions using a divergence radius and takes their product across state–action pairs. It notes that extensions to other structures are possible only when the corresponding robust value evaluation can be performed; without suitable structure, robust evaluation can become computationally hard.

### Thesis use
State uncertainty distance, radius, and rectangularity explicitly for every robust-constrained comparator.

### Citation
Ganguly et al. (2025), Section 2, Equation 6.

## E6 — Robust constrained optimization is not repeated-shift adaptation
- **Type:** scope synthesis grounded in the paper
- **Location:** Overall formulation
- **Claim:** The paper solves a static robust constrained optimization problem around model uncertainty; it does not provide a changepoint detector, context memory, or recovery-delay metric for repeated environmental shifts.
- **Status:** verified

### Thesis use
Classify RNPG/RCMDP under robust safety optimization, not as a detector-triggered resilience mechanism.

### Citation
Ganguly et al. (2025), overall formulation.