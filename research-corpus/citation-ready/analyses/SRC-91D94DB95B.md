# SRC-91D94DB95B — Constrained Policy Optimization

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Joshua Achiam, David Held, Aviv Tamar, Pieter Abbeel
- **Έκδοση:** ICML 2017, PMLR 70
- **Τύπος:** primary safe/constrained RL method
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Αντικείμενο

Η εργασία διατυπώνει το RL σε Constrained Markov Decision Process (CMDP), όπου η policy πρέπει να μεγιστοποιεί reward ενώ τα expected cumulative auxiliary costs παραμένουν κάτω από προκαθορισμένα limits.

Προτείνεται ο Constrained Policy Optimization (CPO), trust-region policy-search method που στοχεύει σε near-constraint satisfaction σε κάθε update και όχι μόνο σε τελική policy.

## Κύρια αποτελέσματα

- Διατυπώνεται CMDP με reward και μία ή περισσότερες auxiliary cost functions.
- Παράγονται bounds που συνδέουν την αλλαγή expected return/cost μεταξύ δύο policies με average policy divergence.
- Ο CPO χρησιμοποιεί local constrained policy updates ώστε να βελτιώνει reward χωρίς να αγνοεί constraints κατά τη μάθηση.
- Η empirical αξιολόγηση γίνεται σε high-dimensional simulated locomotion tasks.

## Συνάφεια

Η κύρια αξία για τη διπλωματική είναι μεθοδολογική: **reward recovery και safety-cost recovery πρέπει να παρακολουθούνται χωριστά**.

Σε ένα changing GridWorld, ένας agent μπορεί να επαναφέρει γρήγορα το return του αλλά να το επιτυγχάνει με αυξημένες hazard visits ή constraint violations. Ένα resilience score που βλέπει μόνο reward θα έκρυβε αυτό το failure mode.

Ο CPO δεν είναι baseline πρώτης γραμμής για το tabular core, επειδή είναι policy-search method για parametrized policies. Χρησιμοποιείται όμως για το σωστό framing των constraints και των per-update safety measurements.

## Πρωτόκολλο που προκύπτει

Για κάθε constrained/safe experiment καταγράφονται:

- task return,
- κάθε auxiliary cost χωριστά,
- constraint threshold,
- violation margin,
- fraction επεισοδίων/βημάτων με violation,
- performance κατά training και όχι μόνο στην τελική policy,
- nominal utility loss που προκαλεί η constraint handling.

Μετά από changepoint, αναφέρονται χωριστά:

1. χρόνος ανάκτησης του task return,
2. χρόνος επαναφοράς κάτω από το safety threshold,
3. cumulative violations κατά τη recovery περίοδο.

## Περιορισμοί

- Deep/continuous-control setting· δεν αποτελεί άμεση απόδειξη για tabular GridWorld.
- Constraint satisfaction είναι expected-cost notion και δεν ισοδυναμεί με almost-sure safety.
- Δεν αντιμετωπίζει exogenous non-stationarity ή changepoint detection.
- Δεν αποδεικνύει ότι constrained policy search είναι resilience mechanism.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για CMDP semantics και για το requirement να αναφέρονται reward και safety costs ως ανεξάρτητοι άξονες κατά την προσαρμογή.