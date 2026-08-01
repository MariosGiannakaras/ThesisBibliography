---
κωδικός: SRC-21EBE15D15
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — A Survey of Zero-shot Generalisation in Deep Reinforcement Learning

## E1 — Strict zero-shot evaluation excludes test-environment learning

- **Type:** faithful paraphrase
- **Location:** Introduction and Scope
- **Claim:** In the survey's zero-shot setting, the policy is evaluated on unseen environment instances without additional training or data from those test instances.
- **Status:** verified

### Faithful paraphrase

Kirk et al. define zero-shot generalisation as evaluating a learned policy on environment instances different from those used for training while prohibiting additional training or use of data from the test instances. Methods that adapt using target-environment data therefore belong to a different evaluation regime.

### Context and limits

Zero-shot evaluation is useful for measuring immediate transfer, but it does not replace evaluation of an agent that is explicitly designed to learn after deployment.

### Thesis use

Run a frozen-policy test before any online adaptation phase and never label post-update recovery as zero-shot generalisation.

### Citation

Kirk et al. (2023), Introduction and Scope.

## E2 — Zero-shot generalisation is a class of problems, not one scalar ability

- **Type:** faithful paraphrase
- **Location:** Introduction; Section 3
- **Claim:** Generalisation problems differ in factors of variation, context observability, train/test distributions, interpolation versus extrapolation, and other structural assumptions.
- **Status:** verified

### Faithful paraphrase

The survey formalizes zero-shot generalisation through contextual MDPs and emphasizes that “generalisation” is underspecified without describing the relevant context distribution and structural assumptions. A method may improve one form of generalisation while harming another, so results from a single shift type do not justify a universal generalisation claim.

### Thesis use

Label every static generalisation experiment as IID held-out, interpolation, extrapolation, or another explicitly defined context shift.

### Citation

Kirk et al. (2023), Introduction and Section 3.

## E3 — A benchmark is the combination of an environment and an evaluation protocol

- **Type:** faithful paraphrase
- **Location:** Section 4
- **Claim:** The environment defines available context-MDPs, while the evaluation protocol defines training/test context sets, sampling restrictions, and interaction budgets.
- **Status:** verified

### Faithful paraphrase

The survey separates the design of an environment from the protocol used to evaluate generalisation in it. The same simulator can support different benchmarks depending on how contexts are divided between training and testing, how many training contexts are available, how they are sampled, and what interaction or update rules are permitted.

### Thesis use

Configuration files and reports must record train/validation/test context sets, seeds, perturbation factors, severity levels, and whether test-time updates are allowed.

### Citation

Kirk et al. (2023), Section 4.

## E4 — Pure procedural generation can obscure factor-specific conclusions

- **Type:** faithful paraphrase
- **Location:** Sections 4 and 7, benchmark recommendations
- **Claim:** Purely procedural generation provides diversity but can make it difficult to isolate which environmental factor caused a generalisation success or failure.
- **Status:** verified

### Faithful paraphrase

Kirk et al. argue that fully procedural environments often expose a seed while entangling many underlying sources of variation. They recommend combining procedural diversity with controllable factors so that experiments can target a particular type of generalisation and interpret the resulting failure modes more precisely.

### Context and limits

Controlled factors improve internal validity and interpretability; they do not make a toy environment inherently realistic.

### Thesis use

Randomize layouts if useful, but control transition noise, reward changes, obstacle changes, and action failures independently.

### Citation

Kirk et al. (2023), benchmark discussion and recommendations.

## E5 — Held-out random seeds alone are a weak test of targeted OOD generalisation

- **Type:** faithful paraphrase
- **Location:** Section 4.2, procedural-generation evaluation protocols
- **Claim:** Holding out random seeds is useful for detecting memorization, but without interpretable context factors it does not identify robustness to a specific dynamics or reward shift.
- **Status:** verified

### Faithful paraphrase

The survey treats protocols that train over most of a procedural seed space and test on unseen seeds as a relatively weak form of zero-shot generalisation. Such a split is better than testing on exactly the same instances, but it primarily indicates whether the policy has overfit to particular generated instances rather than whether it can extrapolate along a known environmental factor.

### Thesis use

Use held-out layout seeds as a memorization diagnostic, not as the only evidence for robustness or resilience.

### Citation

Kirk et al. (2023), Section 4.2.

## E6 — Zero-shot generalisation and online adaptation should be reported as distinct phases

- **Type:** synthesis grounded in the survey scope and future-work discussion
- **Location:** Scope; future directions
- **Claim:** The survey excludes test-time learning from ZSG while identifying fast online adaptation as an important neighboring research direction.
- **Status:** verified

### Faithful paraphrase

The survey's strict ZSG definition freezes the policy on test instances, yet its broader discussion recognizes fast online adaptation as important for realistic changing environments. This makes the two capabilities complementary but experimentally distinct.

### Thesis use

Report `clean/train → frozen zero-shot test → online adaptation` as separate phases whenever both generalisation and resilience are studied.

### Citation

Kirk et al. (2023), Scope and future-directions discussion.
