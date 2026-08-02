# Επιστημονική ανάλυση — Παρτίδα 03

## Στόχος

Κάλυψη των διαστάσεων της επίσημης αίτησης που αφορούν θόρυβο δεδομένων, αποτυχίες/διαταραχές στην αλληλεπίδραση και σαφή διάκριση robustness από resilience.

## Επαληθευμένες πηγές

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-A3D907D882` | Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning | Κύρια — perturbation taxonomy και benchmark design |
| `SRC-3EA1176D3A` | Solving robust MDPs as a sequence of static RL problems | Κύρια — robustness/resilience και static/dynamic uncertainty |
| `SRC-09DD20BA85` | Bounded Robustness in Reinforcement Learning via Lexicographic Objectives | Κύρια — observational noise και utility–robustness trade-off |

## Αποφάσεις που υποστηρίζονται

1. Οι perturbations θα ορίζονται ως `target × mode × severity × frequency × onset`.
2. Θα καταγράφονται χωριστά true/observed state και intended/executed action.
3. Το robustness χωρίς online update δεν θα ονομάζεται resilience.
4. Θα αναφέρονται χωριστά nominal utility, immediate degradation, recovery trajectory και final adapted performance.
5. Το GridWorld είναι instrumented minimal testbed και όχι απαίτηση της επίσημης αίτησης ή απόδειξη real-world generalization.

## Ανοιχτά σημεία

- Ο ακριβής severity grid θα οριστεί μετά από pilot runs.
- Η υλοποίηση IWOCS ή LRPG ως executable baseline θα αποφασιστεί μετά από complexity και dependency assessment.
- Οι publication-specific αριθμητικές κατατάξεις δεν μεταφέρονται ως αναμενόμενα αποτελέσματα στο GridWorld.
