---
κωδικός: SRC-DBDFB80961
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Bayesian Reinforcement Learning: A Survey

## E1 — Bayesian RL represents the agent's current state of knowledge explicitly
- **Type:** faithful paraphrase
- **Location:** Abstract; Chapter 1, Introduction
- **Claim:** Bayesian reinforcement learning combines prior information with data to maintain a posterior distribution that can influence sequential action selection.
- **Status:** verified

### Faithful paraphrase
Ghavamzadeh et al. describe Bayesian RL as an approach in which prior information about either the environment or the solution is represented probabilistically and updated as new interaction data arrive. The posterior summarizes the learner's current state of knowledge, subject to the chosen model, and can be used directly when balancing exploration against exploitation.

### Context and limits
A posterior is only as meaningful as its prior, likelihood, representation, and approximation. Bayesian notation does not by itself guarantee calibrated uncertainty under model misspecification.

### Thesis use
Treat posterior uncertainty as an information signal that can guide exploration or adaptation, while validating its behavior separately from task return.

### Citation
Ghavamzadeh et al. (2015), Abstract and Chapter 1.

## E2 — Model-based and model-free Bayesian RL place priors over different objects
- **Type:** faithful paraphrase
- **Location:** Chapter 1; Chapters 4–5
- **Claim:** Model-based BRL represents uncertainty over environment-model parameters, whereas model-free BRL can place Bayesian structure over value functions, policies, or related solution representations.
- **Status:** verified

### Faithful paraphrase
In the model-based family surveyed in Chapter 4, data update a posterior over unknown parameters of the Markov model and planning uses that distribution. In the model-free family surveyed in Chapter 5, Bayesian inference is applied to the solution space without requiring an explicit complete transition model, for example through distributions over value functions or policy parameters.

### Context and limits
Hybrid methods may combine both forms of representation, so the distinction is an organizing taxonomy rather than a strict law for every algorithm.

### Thesis use
State explicitly what an uncertainty-aware candidate is uncertain about: transition/reward dynamics, values, policy parameters, latent context, or another object.

### Citation
Ghavamzadeh et al. (2015), Chapters 4–5.

## E3 — Bayes-adaptive decision making is computationally harder than ordinary state-based control
- **Type:** faithful paraphrase
- **Location:** Chapter 1; Sections 4.3–4.6
- **Claim:** Acting optimally with respect to the Bayesian information state generally increases computational complexity and motivates approximate planning methods.
- **Status:** verified

### Faithful paraphrase
The survey notes that Bayesian decision making must account not only for the physical state but also for uncertainty about unknown quantities. Solving this enlarged information-state problem exactly is typically more demanding than solving the corresponding known-model MDP. Practical methods therefore rely on approximations such as value approximations, limited or near-myopic lookahead, tree search, sparse sampling, and exploration bonuses.

### Context and limits
A small tabular problem may make some Bayesian methods feasible, but feasibility must be established empirically under the thesis compute budget rather than assumed from state-space size alone.

### Thesis use
Use a feasibility gate and report per-step compute and memory before promoting a Bayesian candidate to the final baseline matrix.

### Citation
Ghavamzadeh et al. (2015), Chapter 1 and Sections 4.3–4.6.

## E4 — Bayesian risk criteria change the optimization objective
- **Type:** faithful paraphrase
- **Location:** Chapter 6, Risk-aware Bayesian Reinforcement Learning
- **Claim:** Parameter uncertainty can be incorporated through risk-sensitive criteria rather than optimizing only posterior-mean performance.
- **Status:** verified

### Faithful paraphrase
The risk-aware chapter surveys objectives that account for uncertainty in model or solution parameters through criteria such as bias–variance trade-offs, percentile-based measures, and min–max formulations. Such criteria can deliberately prefer a more conservative policy than one chosen only for maximum expected return.

### Context and limits
Risk-aware optimization is not the same mechanism as online recovery after a changepoint. A conservative Bayesian policy may be robust without performing any post-shift learning.

### Thesis use
If a Bayesian robust baseline is included, report nominal utility together with disturbed utility and do not label the risk criterion itself as resilience.

### Citation
Ghavamzadeh et al. (2015), Chapter 6.

## E5 — Prior knowledge is useful but can also become a source of misspecification
- **Type:** synthesis grounded in the survey
- **Location:** Chapter 1 and model-based BRL discussion
- **Claim:** Bayesian methods make prior assumptions explicit; those assumptions should be stress-tested when the deployment regime lies outside the modeled family.
- **Status:** verified

### Faithful paraphrase
A principal motivation for Bayesian RL is the ability to incorporate prior structure and regularize learning when data are scarce. The same dependence means that inference and action selection remain conditional on the assumed prior and representation. If the true regime is poorly represented by those assumptions, posterior confidence should not be treated as proof that the inferred model is correct.

### Thesis use
Include misspecified-prior and true-regime-absent-from-library scenarios for any Bayesian/context model that is retained.

### Citation
Ghavamzadeh et al. (2015), Chapter 1 and Chapters 4–6.