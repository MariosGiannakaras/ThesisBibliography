---
κωδικός: SRC-CC5B34C28C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Best-Effort Policies for Robust Markov Decision Processes

## E1 — Equal worst-case value does not imply equal performance across the uncertainty set

- **Type:** faithful paraphrase
- **Location:** Abstract; Introduction
- **Claim:** Multiple optimal robust policies can have the same worst-case return while differing substantially under non-adversarial transition choices.
- **Status:** verified

### Faithful paraphrase

Abate et al. point out that the standard robust objective can leave several policies tied because each achieves the same maximal worst-case expected return. Those policies need not behave equally well for other transition functions inside the uncertainty set, especially when the environment is uncertain rather than strategically adversarial.

### Context and limits

The proposed refinement remains inside the fixed robust-MDP uncertainty set. It does not address post-change learning or recovery outside that set.

### Thesis use

Report worst-case, nominal/clean, and representative in-set returns rather than using worst-case value as the only robust-policy metric.

### Citation

Abate et al. (2026), Abstract and Introduction.

## E2 — Dominance provides a tie-breaker among robust-optimal policies

- **Type:** faithful paraphrase
- **Location:** Section 3, Definitions 4–6
- **Claim:** A policy is dominated if another policy is never worse over the uncertainty set and is strictly better for at least one admissible transition model.
- **Status:** verified

### Faithful paraphrase

The paper defines policy dominance pointwise over every transition function in the RMDP uncertainty set. A best-effort policy is one for which no alternative is weakly better everywhere and strictly better somewhere. This criterion filters out policies that sacrifice attainable performance without gaining anything under another allowed model.

### Context and limits

Best-effort policies can still be incomparable with one another and do not define a total ranking over all robust policies.

### Thesis use

If several robust policies tie on worst-case value, specify a secondary selection criterion rather than choosing one implicitly.

### Citation

Abate et al. (2026), Section 3, Definitions 4–6.

## E3 — ORBE preserves robust optimality while adding best-effort refinement

- **Type:** faithful paraphrase
- **Location:** Sections 3–5
- **Claim:** An optimal robust best-effort policy is both worst-case optimal and not dominated by another policy in the uncertainty set.
- **Status:** verified

### Faithful paraphrase

ORBE policies are selected from the robust-optimal set and then refined using the best-effort criterion. The construction therefore does not trade away the original worst-case guarantee in order to improve typical performance; it uses dominance as a principled tie-breaker among policies that already satisfy robust optimality.

### Context and limits

The paper assumes an `s`-rectangular RMDP and inherits the structural assumptions of that formulation.

### Thesis use

Treat tie-breaking and uncertainty-set structure as explicit configuration fields for robust baselines.

### Citation

Abate et al. (2026), Sections 3–5.

## E4 — Robust-policy conservativeness is different from resilience

- **Type:** scope inference grounded in the formulation
- **Location:** Sections 1–6
- **Claim:** ORBE addresses policy selection within a fixed ambiguity set; it does not detect environmental changes or continue learning after deployment.
- **Status:** verified

### Faithful paraphrase

The method refines how a robust policy is chosen before execution so that non-adversarial models inside the uncertainty set are handled more effectively. There is no changepoint detector, context-memory mechanism, reset rule, or post-shift learning process in the contribution.

### Thesis use

Keep `robust_policy_selection` separate from online resilience and recovery baselines.

### Citation

Abate et al. (2026), overall method scope.
