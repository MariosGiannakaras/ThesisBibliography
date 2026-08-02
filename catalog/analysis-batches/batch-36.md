# Παρτίδα 36 — State Entropy provenance και boundary consolidation

Ημερομηνία: 2026-08-01

## Canonical provenance migration

### `SRC-E467A29609` — State Entropy Regularization for Robust Reinforcement Learning
- Πλήρες NeurIPS 2025 conference paper.
- Γίνεται το canonical selected scientific record.
- Χρήση: state-visitation entropy έναντι policy entropy, structured/spatial perturbations, coverage, regularization/conservativeness, rollout-budget sensitivity και failure cases.

### `SRC-C90D59EC8C`
- Ήταν official poster/abstract record της ίδιας εργασίας.
- Μετατρέπεται από selected σε `απόρριψη` ως bibliographic/metadata duplicate.
- Το παλιό excerpt record απενεργοποιήθηκε ώστε να μη μετρά δεύτερη φορά.

Η migration είναι **1-for-1**: ο συνολικός αριθμός selected δεν αλλάζει.

## Νέες exclusions
1. `SRC-DDD62BEA2D` — Self-Initiated Open World Learning: conceptually useful novelty framework, αλλά κυρίως supervised/open-world και όχι RL changepoint algorithm.
2. `SRC-8D9C7ADFD3` — Stanford continual-safety seminar; derivative lifecycle/safety-assurance synthesis.
3. `SRC-05EDAEDFA0` — McKinsey/QuantumBlack agentic-AI CEO playbook.
4. `SRC-ACAA62B248` — CARLA sensor implementation documentation.
5. `SRC-42B0E2B976` — Sergey Levine offline-data safety seminar transcript.
6. `SRC-439938DD4C` — duplicate transcript of the same seminar.
7. `SRC-AE21B23099` — Williams 1992 REINFORCE; foundational but redundant unless vanilla policy-gradient derivation enters core.
8. `SRC-2583FFAA52` — adversarial machine learning in MARL SoK.
9. `SRC-7E393FD42E` — CMU dissertation on LLM/web agents for real-world procedural tasks.
10. `SRC-070BF489A5` — unusable OpenReview verification wrapper for robust-MDP work.
11. `SRC-70B654D7DC` — Stanford seminar on safe/efficient physical-world learning and safe Bayesian optimization.
12. `SRC-732D12A2CC` — Towards a Science of AI Agent Reliability; interesting LLM-agent reliability dimensions but different experimental object.
13. `SRC-958647DE4E` — Madry et al. adversarial robustness for supervised classifiers; foundational but adversarial/non-RL.
14. `SRC-DA324C815B` — technically strong distributionally robust offline RL; fixed logged-data setting, not online post-change adaptation.
15. `SRC-E7E736ACE8` — broad supervised OOD-generalization survey; redundant with direct RL generalization/OOD sources.

## Επιστημονικές αποφάσεις
- State entropy and policy entropy remain separate exploration/coverage variables.
- Full paper supersedes poster/abstract metadata as canonical evidence.
- Open-world novelty frameworks can inform terminology without becoming RL adaptation baselines.
- Continual safety assurance is a useful lifecycle concept, but seminar synthesis does not replace primary safety/revalidation sources.
- Offline RL, supervised adversarial robustness and supervised OOD generalization are distinct problem settings from online RL resilience.
- Modern LLM-agent reliability metrics are external-validity context, not direct substitutes for RL recovery metrics.

## Totals μετά την παρτίδα
- Pending records resolved: 16
- Provenance reclassification: 1 selected ID migrated to another full-paper ID
- Net selected count: unchanged
- Canonical σύνολο: **309 αποφασισμένες = 96 selected + 213 exclusions**
- Υπόλοιπη ουρά: **177 / 486 ενεργές πηγές**
