---
κωδικός: SRC-8D4F62D85D
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Evidence — Deep Reinforcement Learning That Matters

## Evidence E1 — Deep-RL outcomes are sensitive to random seeds
- **Type:** faithful paraphrase
- **Location:** empirical variability experiments and reproducibility discussion
- **Claim:** Different random seeds can produce materially different performance distributions for the same nominal algorithm/configuration.
- **Thesis use:** independent-root design
- **Status:** verified

### Thesis-safe implication
No DQN/PPO/A2C claim may rest on a favorable single seed or selected top runs; independent roots and uncertainty must be retained.

## Evidence E2 — Hyperparameters and implementation details can change conclusions
- **Type:** faithful paraphrase
- **Location:** hyperparameter, architecture, reward-scaling and implementation analyses
- **Claim:** Reported deep-RL performance is sensitive to choices beyond the algorithm name.
- **Thesis use:** reproducible implementation and fair tuning
- **Status:** verified

### Thesis-safe implication
Every deep method requires a version-pinned implementation, declared architecture/update configuration and comparable tuning opportunity. Library defaults are starting points, not automatically fair final settings.

## Evidence E3 — Reporting only favorable runs is methodologically weak
- **Type:** faithful paraphrase
- **Location:** statistical/reporting discussion
- **Claim:** Small or selectively reported run sets can exaggerate apparent improvements.
- **Thesis use:** result retention/reporting
- **Status:** verified

### Thesis-safe implication
Poor, unstable and failed runs remain in the evidence trail under predeclared failure rules; “best-seed” selection is prohibited.

## Evidence E4 — Standardized experimental reporting is required for reproducibility
- **Type:** faithful paraphrase
- **Location:** recommendations/conclusions
- **Claim:** Reproducibility depends on reporting the actual experimental choices and statistical uncertainty, not only the algorithm label.
- **Thesis use:** provenance contract
- **Status:** verified

### Thesis-safe implication
Protocol-v2 stores resolved method configuration, library/version, seeds, budgets, checkpoint provenance and evaluation rules for every whole experiment.

## Avoid overclaiming
The paper is evidence about reproducibility and sensitivity. It does not establish that any particular deep algorithm is resilient to the thesis change mechanisms, nor does it prescribe the final number of roots or one universal hyperparameter-search procedure.
