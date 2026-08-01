# Παρτίδα 31 — neural baseline fairness και scope/dedup cleanup

Ημερομηνία: 2026-08-01

## Στόχος
Να κλείσουν duplicate/adversarial/agentic/offline records και να αξιολογηθούν primary RL candidates που μπορούν να επηρεάσουν τη fairness της τελικής σύγκρισης.

## Selected

### `SRC-BE53B7970E` — Deep Reinforcement Learning with Double Q-learning
- **Ρόλος:** υποστηρικτική / neural-baseline reference
- **Κατάσταση:** επαληθευμένη
- **Εξαγωγή:** ναι
- **Χρήση:** maximization/overestimation bias, Double-DQN selection/evaluation decoupling, neural baseline fairness.
- **Όριο:** δεν είναι detector, continual learner ή resilience mechanism.

## Exclusions

1. `SRC-8E6D76457D` — LLM agentic-framework/protocol survey.
2. `SRC-A6DBFC5357` — Andrew Ng agentic-AI keynote.
3. `SRC-69F70663B3` — Andrew Ng/LangChain agentic fireside.
4. `SRC-D057CF6978` — Alignment Newsletter secondary summary.
5. `SRC-AFCB3FE8DF` — adversarial-state pessimistic Q-learning; malicious threat model and redundant observation-robustness scope.
6. `SRC-822FFD1EF7` — conference duplicate of `SRC-AFCB3FE8DF`.
7. `SRC-F43D9994F4` — author-hosted duplicate of selected ORBE source `SRC-CC5B34C28C`.
8. `SRC-E41D012B99` — arXiv duplicate of the same ORBE paper.
9. `SRC-D6F2B11A5D` — socio-technical workshop extension of Concrete Problems in AI Safety; redundant for technical protocol.
10. `SRC-5F508C4383` — directly relevant continual-RL MSc, but repository evidence is abstract-level metadata and lower tier; retained as implementation lead only.
11. `SRC-2CA4104ACF` — historical ICML cross-domain transfer paper; high quality but redundant with selected transfer sources for current questions.
12. `SRC-5736A9A37B` — BDI Wikipedia.
13. `SRC-CDCEC02AAA` — offline/batch deep-RL benchmark, different fixed-dataset problem.
14. `SRC-24038FBE78` — no-code LLM-agent tutorial.
15. `SRC-B1B0E55CA6` — AWS generative-agent operational resilience guidance.
16. `SRC-F7E7C38BFD` — IBM application-resilience/product remediation article.
17. `SRC-98B4CE528B` — DeepMind safety blog framing, derivative/redundant with primary selected sources.
18. `SRC-ACB00B414D` — duplicate MDPI PDF of CoReaAgents.
19. `SRC-F355021435` — practitioner AI-agent builder tutorial.

## Επιστημονικές αποφάσεις που κλειδώνουν

- Αν χρησιμοποιηθεί neural value-based comparator, το known maximization bias του DQN πρέπει να ελεγχθεί ώστε να μη συγχέεται με resilience failure.
- Double DQN είναι baseline-quality improvement, όχι adaptation mechanism.
- Adversarial state corruption δεν χρησιμοποιείται ως άμεση evidence base για ordinary observation noise/non-adversarial shifts.
- Offline/batch distribution support problems δεν ταυτίζονται με online stale-data/replay contamination μετά από changepoint.
- Directly relevant grey literature μπορεί να παραμένει discovery/implementation lead χωρίς να ανεβαίνει σε citation-ready status όταν δεν έχει ελεγχθεί πλήρες πρωτότυπο.
- Operational resilience LLM/cloud applications δεν αποτελεί policy-resilience evidence.

## Αποτέλεσμα
- Νέες αποφάσεις: 20
- Νέες selected: 1
- Νέες exclusions: 19
- Νέα citation-ready excerpt sets: 1
- Canonical σύνολο μετά την παρτίδα: 213 αποφασισμένες πηγές = 93 selected + 120 exclusions.
- Υπόλοιπη ουρά: 273 από 486 ενεργές πηγές.
