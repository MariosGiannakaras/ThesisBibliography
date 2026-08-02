# Παρτίδα 40 — adaptation metrics και resilience protocol

Ημερομηνία: 2026-08-01

## Reconciliation
Το generated status περιέχει stale/orphan rows που δεν αντιστοιχούν σε current source files. Χρησιμοποιείται μόνο για discovery. Ο historical denominator 486 δεν χρησιμοποιείται πλέον για exact remaining count μέχρι directory-level reconciliation.

## Selected — 4
- `SRC-1B40F8B37A` — supporting metric source: perturbation severity, relative-to-optimum vs relative-to-origin resilience, low-baseline/no-op metric pathology, perturbation distribution.
- `SRC-13B66B20D8` — κύρια: sudden environmental change, NovGrid novelty ontology, adaptive efficiency, final adaptive performance, transfer AUC, convergence frequency, exploration × novelty-type interaction.
- `SRC-D4C8A4B1BF` — supporting conceptual source: robustness ≠ resilience, preparation/absorption/recovery/adaptation, graceful degradation, affordable resilience.
- `SRC-85335DDDA6` — supporting evaluation source: modality-specific robustness/resilience, severity sweeps, hyperparameter/tuning fairness. MARL findings δεν μεταφέρονται ως single-agent algorithm claims.

## Exclusions — 10
- `SRC-A1906370CC` — duplicate project page του `SRC-7702DAEF48`.
- `SRC-A281BA721E` — duplicate HTML record του `SRC-D4C8A4B1BF`.
- `SRC-16E5F21F41` — MSc metadata-only safe-exploration record.
- `SRC-3EF475E25A` — robust average-reward MDP formulation εκτός current core.
- `SRC-85D1CCAE1E` — advanced robust-constrained RL, non-core formulation.
- `SRC-7238AA0BDC` — offline-RL uncertainty MSc metadata/abstract.
- `SRC-47085E14BA` — MARL agent-change mechanism, εκτός single-agent scope.
- `SRC-89009123A3` — causal-confounding/off-policy evaluation, διαφορετικό uncertainty problem.
- `SRC-0A9340F46A` — offline OOD dynamics generalization MSc metadata.
- `SRC-C248E7DB93` — duplicate του `SRC-0A9340F46A`.

## Protocol decisions
1. Resilience ratio συνοδεύεται πάντα από absolute pre/post-change utility.
2. Shift severity και perturbation sampling distribution δηλώνονται.
3. Adaptation time-to-threshold/convergence συνοδεύεται από success/convergence fraction.
4. Recovery speed και final adapted performance αναφέρονται χωριστά.
5. Area-under-recovery metric δηλώνει πώς χειρίζεται failed/non-converged runs.
6. Exploration ablations γίνονται σε πολλαπλά shift types.
7. Graceful degradation ορίζεται operationally, όχι μόνο λεκτικά.
8. Resource overhead αναφέρεται μαζί με resilience benefit.
9. Tuning budget/search space είναι μέρος του fairness protocol.
10. Persistent robustness, transient-shock recovery και continuing adaptation αξιολογούνται χωριστά.

## Canonical ledger
Starting ledger μετά την Παρτίδα 39: 366 decisions = 97 selected + 269 exclusions.

Παρτίδα 40: 14 decisions = 4 selected + 10 exclusions.

**Ledger μετά την Παρτίδα 40: 380 decisions = 101 selected + 279 exclusions.**

Exact remaining count δεν δηλώνεται μέχρι source-directory reconciliation, επειδή το generated index περιέχει orphan rows.

Generated status, curated CSV και thesis package παραμένουν μη συγχρονισμένα με τις canonical analyses.