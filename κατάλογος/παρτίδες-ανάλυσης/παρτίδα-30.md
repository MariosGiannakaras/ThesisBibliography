# Παρτίδα 30 — Bayesian risk semantics και τεχνικό scope cleanup

Ημερομηνία: 2026-08-01

## Στόχος
Αξιολόγηση τεχνικών πηγών γύρω από uncertainty/risk/safety ώστε να διαχωριστούν οι πραγματικά χρήσιμες MDP/RL έννοιες από formal-method lectures, LLM-agent frameworks, application-specific theses και διαφορετικές σημασίες της uncertainty.

## Selected

### `SRC-9CC11ECF41` — Approximate Bilevel Difference Convex Programming for Bayesian Risk Markov Decision Processes
- **Ρόλος:** υποστηρικτική
- **Κατάσταση:** επαληθευμένη
- **Εξαγωγή:** ναι
- **Κύρια χρήση:** Bayesian posterior uncertainty, risk-sensitive control, posterior-versus-ambiguity distinction, conservativeness reporting.
- **Κρίσιμο όριο:** offline Bayesian learning σε fixed unknown MDP δεν αποτελεί sequential changepoint adaptation ή repeated-regime resilience.

## Exclusions

1. `SRC-4FF5AB08E6` — formal verification/synthesis colloquium transcript· σοβαρό αλλά derivative/redundant.
2. `SRC-7DA66E226E` — CoReaAgents LLM multi-agent reasoning framework.
3. `SRC-847A095FA3` — MSc safe-RL application σε energy-efficient federated learning/wireless networks.
4. `SRC-F82F4BD836` — alternate record της ίδιας MSc thesis.
5. `SRC-B4F46326ED` — AI-safety/RL position seminar, χωρίς πλήρες primary result protocol.
6. `SRC-7714A58280` — adversarial robustness σε supervised sound-event detection.
7. `SRC-97A931D29F` — duplicate/full-PDF record του Google Agents whitepaper `SRC-10236BC6DB`.
8. `SRC-CCCFFD4365` — moral/normative uncertainty, διαφορετικό uncertainty semantics.
9. `SRC-F4B012F78F` — economics/markets chapter για LLM-based AI agents.
10. `SRC-8FC523FC42` — Azure application/infrastructure self-healing guidance.

## Επιστημονικές αποφάσεις που κλειδώνουν

- Posterior belief και risk attitude είναι χωριστές design dimensions.
- Bayesian parameter learning σε stationary unknown model δεν ισοδυναμεί με detection/adaptation σε piecewise-stationary αλλαγές.
- Moral uncertainty δεν πρέπει να συγχέεται με aleatoric/epistemic model uncertainty.
- Cloud/component self-healing δεν αποτελεί policy recovery.
- Formal-method lectures μπορούν να χρησιμοποιούνται για discovery/κατανόηση, αλλά όταν υπάρχουν primary sources δεν μετρούν ως ανεξάρτητο evidence.
- Application-specific safe RL δεν μεταφέρεται ως evidence για GridWorld resilience χωρίς αντίστοιχο change/recovery protocol.

## Αποτέλεσμα
- Νέες αποφάσεις: 11
- Νέες selected: 1
- Νέες exclusions: 10
- Νέα citation-ready excerpt sets: 1
- Canonical σύνολο μετά την παρτίδα: 193 αποφασισμένες πηγές = 92 selected + 101 exclusions.
- Υπόλοιπη ουρά: 293 από 486 ενεργές πηγές.
