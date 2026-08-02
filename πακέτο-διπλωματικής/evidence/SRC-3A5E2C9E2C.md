---
κωδικός: SRC-3A5E2C9E2C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — A Review of Safe Reinforcement Learning: Methods, Theories and Applications

## E1 — Safety must be operationalized before agents are compared

- **Type:** faithful paraphrase
- **Location:** Introduction, safety definitions and 2H3W framing
- **Claim:** The safe-RL literature uses multiple safety semantics, so an experiment must state the observable criterion that counts as safe behavior.
- **Status:** verified

### Faithful paraphrase

Gu et al. survey several notions of safety, including protection from harm or risk, maintaining recognized dangers below an acceptable level, avoiding states designated unsafe, acting in accordance with human preferences, and retaining reversibility over visited states. The diversity of these definitions shows that “safe” is not a self-defining experimental label.

### Context and limits

The review does not establish one universally correct definition. A concrete study must choose and report its own operational safety variables.

### Thesis use

Predefine unsafe events, hazards, and costs before running the final comparison, and keep safety distinct from robustness and resilience.

### Citation

Gu et al., Introduction.

## E2 — CMDPs separate task reward from safety cost

- **Type:** faithful paraphrase
- **Location:** Section 2.1, safe-RL problem formulation
- **Claim:** A constrained MDP maximizes reward while requiring one or more safety-cost objectives to satisfy explicit bounds.
- **Status:** verified

### Faithful paraphrase

The review presents the CMDP as a common mathematical formulation for safe RL. The policy seeks high expected reward while cost objectives represent safety constraints that must remain below specified limits. This formulation keeps utility and safety signals conceptually separate instead of hiding all safety considerations inside a single reward scalar.

### Context and limits

Expected cumulative constraints may still permit rare severe violations; hard, chance, or other constraint formulations may be more appropriate for catastrophic hazards.

### Thesis use

Log return, cumulative cost, violation count, and violation severity separately for every regime.

### Citation

Gu et al., Section 2.1.

## E3 — Safety bounds create a utility–safety trade-off

- **Type:** faithful paraphrase
- **Location:** Introduction, discussion of safety benchmarks
- **Claim:** A constraint can be too weak to protect the agent or so conservative that task reward becomes unacceptably low.
- **Status:** verified

### Faithful paraphrase

The review notes that loose cost functions or bounds may fail to provide meaningful safety during learning, whereas overly conservative constraints can strongly reduce reward performance. Benchmark design therefore needs to expose both utility and safety rather than reporting only one side of the trade-off.

### Context and limits

The source does not identify a universally optimal constraint value.

### Thesis use

Use predefined constraint-severity settings and plot return against safety violations instead of ranking methods by a single opaque score.

### Citation

Gu et al., Introduction, safety-benchmark discussion.

## E4 — Gridworlds are used as controlled safe-RL benchmarks

- **Type:** faithful paraphrase
- **Location:** Section 6.1.1, AI Safety Gridworlds
- **Claim:** The review identifies two-dimensional gridworlds as established controlled environments for evaluating specific safety properties.
- **Status:** verified

### Faithful paraphrase

In its benchmark survey, the paper describes AI Safety Gridworlds as two-dimensional discrete environments in which agents move between cells and encounter task-specific objects, obstacles, and hazards. Their simplicity supports targeted evaluation of individual safety problems.

### Context and limits

This is secondary evidence. The primary AI Safety Gridworlds paper remains the stronger source for benchmark-design claims.

### Thesis use

Use the review only as supporting context for a minimal controlled GridWorld, not as evidence of real-world external validity.

### Citation

Gu et al., Section 6.1.1.

## E5 — Simulation success does not settle deployment safety

- **Type:** faithful paraphrase
- **Location:** Sections 7–8
- **Claim:** The review treats human compatibility, application standards, and real-world deployment as open safe-RL challenges beyond benchmark performance.
- **Status:** verified

### Faithful paraphrase

The review highlights unresolved issues including human and environmental safety, deployment standards, ethical and preference-related questions, and the gap between simulated experiments and practical applications. High scores on a safe-RL benchmark therefore do not imply that deployment safety has been established.

### Thesis use

State explicitly that the GridWorld study evaluates controlled comparative behavior and does not validate safety in real operational systems.

### Citation

Gu et al., Sections 7–8.
