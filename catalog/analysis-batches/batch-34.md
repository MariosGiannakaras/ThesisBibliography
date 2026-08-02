# Παρτίδα 34 — consolidation γενίκευσης, MARL και agent guides

Ημερομηνία: 2026-08-01

## Αποτέλεσμα
Η παρτίδα έκλεισε 20 records χωρίς νέα selected πηγή. Οι αποκλεισμοί δεν οφείλονται όλοι σε χαμηλή ποιότητα: αρκετές είναι υψηλής ποιότητας εργασίες που είναι redundant ή ανήκουν σε διαφορετικό experimental object.

## Exclusions
1. `SRC-CF2FB64E6A` — AISTATS representation-generalization paper: high quality αλλά optional neural representation theory, redundant για current core.
2. `SRC-FC22553C08` — alternate Google Research record της ίδιας εργασίας.
3. `SRC-532FCB72DC` — seminal POET open-ended environment/solution coevolution: high quality αλλά scope-heavy και redundant με selected UED/Procgen sources.
4. `SRC-1B6E17DDF1` — unusable OpenReview record για observational robustness; direct full-text coverage υπάρχει ήδη.
5. `SRC-A5DDBF1534` — unusable OpenReview meta-RL conversion.
6. `SRC-31DF05187A` — recent rigorous meta-learning/meta-RL survey, broad/redundant για non-stationary core.
7. `SRC-22F8C2C41C` — MARL diffusion MSc thesis.
8. `SRC-CD69FAEC54` — theoretical MARL overview; opponent/policy-induced non-stationarity ≠ exogenous environment shift.
9. `SRC-6C2389B5D2` — neuro-symbolic AI systematic review.
10. `SRC-D5D57992D2` — NIST AI RMF Playbook; derivative of selected RMF.
11. `SRC-81ACE350D5` — third-party NIST RMF summary.
12. `SRC-51561BFA26` — LLM multi-agent resilience against malicious agents.
13. `SRC-2573249C69` — unusable OpenReview wrapper for online robust policy optimization.
14. `SRC-9F53B39DE0` — second unusable OpenReview wrapper.
15. `SRC-FBFDD51DA0` — proceedings duplicate of selected `SRC-D1B6BA711E`.
16. `SRC-7199E9FBD5` — Reddit LLM-agent tools discussion.
17. `SRC-FD3AFA347D` — duplicate scrape of same Reddit discussion.
18. `SRC-1D07EB467A` — Operator AI practitioner guide/book.
19. `SRC-982F8CA1EC` — OpenAI practical LLM-agent engineering guide.
20. `SRC-C6B4E40E10` — OpenSpiel high-quality framework paper, but broad game/MARL scope without thesis-specific recovery evidence.

## Επιστημονικές αποφάσεις
- Representation quality/generalization is not the same as online resilience; neural representation theory remains optional unless a neural arm becomes central.
- Open-ended curriculum/environment generation is not a fair direct replacement for a fixed shared evaluation schedule.
- Meta-RL assumes a task distribution/meta-training regime and must not be silently equated with continual/changepoint adaptation.
- Multi-agent policy-induced non-stationarity remains outside the single-agent exogenous-change causal model.
- Governance playbooks and practitioner agent guides do not count as independent technical evidence when primary scientific/institutional sources exist.
- Multiple hosting/review/proceedings records of the same robust-MDP paper count once.

## Totals μετά την παρτίδα
- Νέες αποφάσεις: 20
- Νέες selected: 0
- Νέες exclusions: 20
- Canonical σύνολο: **273 αποφασισμένες = 96 selected + 177 exclusions**
- Υπόλοιπη ουρά: **213 / 486 ενεργές πηγές**
