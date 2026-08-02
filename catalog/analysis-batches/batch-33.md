# Παρτίδα 33 — dynamic options, Procgen και resilience metrics

Ημερομηνία: 2026-08-01

## Selected

### `SRC-92397254FB` — I-QOption / interruptible temporal abstraction
- **Ρόλος:** υποστηρικτική
- Dynamic four-/six-room GridWorld με obstacle variation μεταξύ episodes.
- Predefined options μπορούν να διακόπτονται όταν η συνέχιση εκτιμάται χειρότερη από νέα επιλογή.
- Χρήση: option-interruption diagnostics και fairness για prior option libraries.
- Όριο: random per-episode variation ≠ hidden piecewise-stationary changepoint.

### `SRC-630F83DAD7` — Leveraging Procedural Generation to Benchmark Reinforcement Learning
- **Ρόλος:** κύρια benchmark/generalization πηγή
- Canonical Procgen ICML 2020 paper.
- Χρήση: procedural environment distributions, disjoint train/test levels, held-out seeds, overfitting controls, solvability validation.
- Όριο: zero-shot/static generalization ≠ online post-change adaptation.

### `SRC-A5DF23299C` — On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management
- **Ρόλος:** κύρια/μετρική πηγή
- Διαχωρίζει robustness από resilience και operationalizes degradation/recovery με reference curves.
- Χρήση: AUC performance-gap, degradation time, restorative time, minimum post-change performance, maximum recovered performance.
- Μόνο η non-adversarial/random perturbation υποπερίπτωση μεταφέρεται άμεσα στο thesis core.

## Exclusions
1. `SRC-4CA982BE87` — duplicate/alternate conversion του selected I-QOption paper.
2. `SRC-1E5026EDE1` — high-quality NeurIPS reward-misspecification/expert-guidance paper, αλλά redundant/out-of-scope για online external reward changes.
3. `SRC-F020E1D46A` — high-quality Lyapunov continuous-control safe-policy optimization, redundant με selected CMDP/Lyapunov/shield/recovery sources.
4. `SRC-626E641889` — stability-guarantee MSc; equilibrium recovery ≠ task-policy recovery και abstract-level record.
5. `SRC-947D011514` — SIAM nonrectangular robust-MDP policy gradient; advanced but redundant για current uncertainty-set protocol.
6. `SRC-F985D31ADB` — arXiv duplicate του `SRC-947D011514`.
7. `SRC-D8433D488F` — stored OpenReview anti-bot page, όχι πραγματικό paper content· re-evaluate only if full text is added.
8. `SRC-23C1899DBE` — Microsoft BDI tutorial.
9. `SRC-40FD71BC15` — duplicate Microsoft BDI tutorial.
10. `SRC-92C828647B` — legal liability in healthcare.
11. `SRC-BCAAFDCD46` — unrelated Rydberg-molecule physics paper.
12. `SRC-495952EBB9` — Gymnasium custom-environment implementation docs.
13. `SRC-4A12CAF92D` — MiniGrid implementation docs; scientific paper already selected.
14. `SRC-0B609C8E04` — legacy gym-minigrid code repository.
15. `SRC-E842F87F3F` — practitioner LLM-agent e-book.
16. `SRC-513B748715` — derivative misalignment-examples page.
17. `SRC-A391B94101` — generic MCTS tutorial; robust-planning/query fairness already covered directly.

## Βιβλιογραφική διόρθωση — Procgen
Το `SRC-630F83DAD7` είναι το πραγματικό canonical scientific Procgen paper (*Leveraging Procedural Generation to Benchmark Reinforcement Learning*, ICML 2020, arXiv:1912.01588).

Το `SRC-9DCA1F02C1` είναι διαφορετική εργασία (*General Video Game AI: a Multi-Track Framework...*) και **δεν πρέπει να αναφέρεται ως Procgen**.

Το `SRC-C512E9AE92` είναι Procgen code repository και παραμένει implementation artifact, όχι δεύτερη scientific evidence unit.

## Επιστημονικές αποφάσεις
- Interruptible macro-actions/options είναι ξεχωριστός adaptation design axis από detection/reset/context recall.
- Predefined option libraries αποτελούν prior knowledge και πρέπει να χρεώνονται στη fairness σύγκριση.
- Procedural generalization protocol και online resilience protocol παραμένουν χωριστά αλλά συμπληρωματικά.
- Resilience curve metrics απαιτούν matched unperturbed reference και σαφή perturbation onset.
- Behavioral/frozen-policy recovery δεν πρέπει να αποδίδεται σε learning αν parameters/Q-values δεν ενημερώνονται.
- Rectangularity/nonrectangularity είναι ουσιαστικό robust-MDP assumption, αλλά δεν απαιτείται πλήρης advanced robust optimization implementation για το thesis core.

## Αποτέλεσμα
- Νέες αποφάσεις: 20
- Νέες selected: 3
- Νέες exclusions: 17
- Νέα/αναβαθμισμένα citation-ready excerpt sets: 3
- Canonical σύνολο μετά την παρτίδα: **253 αποφασισμένες πηγές = 96 selected + 157 exclusions**.
- Υπόλοιπη ουρά: **233 από 486 ενεργές πηγές**.
