---
κωδικός: SRC-5D0E7E5BD7
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# Evidence — Implementation Matters in Deep Policy Gradients

## Evidence E1 — Code-level optimizations materially affect measured behavior
- **Type:** faithful paraphrase
- **Location:** official arXiv abstract
- **Claim:** Implementation augmentations that look secondary can have a major impact on agent behavior.
- **Thesis use:** PPO implementation/provenance contract
- **Status:** verified

### Thesis-safe implication
The thesis must identify and freeze the concrete PPO implementation and resolved settings rather than treating the label `PPO` as a complete experimental specification.

## Evidence E2 — Performance attribution can be confounded by implementation
- **Type:** faithful paraphrase
- **Location:** official arXiv abstract
- **Claim:** In the authors’ PPO/TRPO case study, code-level choices account for much of PPO’s cumulative-reward gain over TRPO and can fundamentally change method behavior.
- **Thesis use:** threats to internal/construct validity
- **Status:** verified

### Thesis-safe implication
A cross-method result should not be attributed purely to an abstract algorithm family when important implementation choices are uncontrolled or unreported.

## Evidence E3 — Implementation identity belongs in reproducibility metadata
- **Type:** methodological implication from E1–E2
- **Location:** official arXiv abstract and stated study objective
- **Claim:** Reproducing or interpreting a deep policy-gradient result requires more than the algorithm name.
- **Thesis use:** versioned adapter/configuration provenance
- **Status:** verified within the stated case-study scope

## Avoid overclaiming
This source is a PPO/TRPO implementation case study. It does not determine the thesis PPO hyperparameters, prove the same effect size in GridWorld, or establish a PPO-vs-DQN/tabular ranking.
