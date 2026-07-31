# SRC-7C18826BEE — Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Yarin Gal, Zoubin Ghahramani
- **Έκδοση:** ICML 2016, PMLR 48
- **Τύπος:** foundational uncertainty-quantification paper
- **Ρόλος στη διπλωματική:** υπόβαθρο

## Κεντρική συνεισφορά

Η εργασία δείχνει ότι dropout training σε neural networks μπορεί να ερμηνευθεί ως approximate variational inference σε deep Gaussian process. Με dropout ενεργό κατά το test time και πολλαπλά stochastic forward passes, μπορεί να υπολογιστεί Monte Carlo estimate της predictive mean και variance (`MC dropout`).

Το αποτέλεσμα παρέχει computationally relatively cheap approximation της epistemic/model uncertainty χωρίς ξεχωριστό ensemble πολλών independently trained networks.

## Σχέση με reinforcement learning

Η εργασία συνδέει uncertainty estimates με exploration και παρουσιάζει εφαρμογή σε Q-value approximation. Η predictive variance μπορεί να χρησιμοποιηθεί ως input σε Thompson-style exploration ή ως diagnostic για states/actions με ανεπαρκή δεδομένα.

Στη διπλωματική η πηγή έχει αξία μόνο εάν προστεθεί neural Q-function ή neural detector. Για το βασικό tabular matrix, visitation counts και empirical transition uncertainty είναι απλούστερα και πιο διαφανή.

## Κρίσιμες διακρίσεις

- Softmax probability δεν είναι epistemic confidence.
- MC-dropout variance είναι approximation που εξαρτάται από architecture, dropout probability, weight decay και αριθμό stochastic passes.
- Υψηλή uncertainty δεν είναι από μόνη της changepoint event.
- Prediction variance πρέπει να βαθμονομείται και να αξιολογείται για false alarms/delay πριν χρησιμοποιηθεί ως detector trigger.

## Πρωτόκολλο

Εάν χρησιμοποιηθεί MC dropout:

- dropout παραμένει ενεργό στο evaluation pass,
- αναφέρεται αριθμός stochastic forward passes T,
- αναφέρονται dropout rates και architecture,
- μετρώνται calibration, AUROC/AUPR όπου υπάρχει ground truth shift label,
- uncertainty και task performance αναφέρονται χωριστά,
- compute overhead ανά environment step καταγράφεται,
- συγκρίνεται με deterministic network και ensemble ή tabular confidence baseline.

## Περιορισμοί

- Η κύρια θεωρία/αξιολόγηση είναι supervised regression/classification, με περιορισμένη RL εφαρμογή.
- Approximate Bayesian interpretation δεν εγγυάται calibrated uncertainty σε distribution shift.
- Dropout samples δεν είναι ανεξάρτητα trained posterior models.
- Η μέθοδος αφορά neural function approximation και μπορεί να είναι περιττή για μικρό GridWorld.
- Δεν παρέχει adaptation/recovery algorithm.

## Απόφαση

**Επιλογή ως background πηγή.** Χρησιμοποιείται για ορθή περιγραφή MC-dropout epistemic uncertainty και για να αποτραπεί η ερμηνεία softmax/Q magnitude ως confidence. Δεν προστίθεται αυτόματα στο implementation scope.