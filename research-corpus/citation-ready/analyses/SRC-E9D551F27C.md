# SRC-E9D551F27C — Distributionally Robust Self-Paced Curriculum Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Anirudh Satheesh, Keenan Powell, Vaneet Aggarwal
- **Έκδοση:** arXiv:2511.05694v3, 8 Μαρτίου 2026
- **Τύπος:** empirical distributionally robust RL preprint
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Πρόβλημα

Στο distributionally robust RL, η robustness budget ε καθορίζει το μέγεθος του uncertainty set. Σταθερό μικρό ε μπορεί να προσφέρει υψηλή nominal performance αλλά αδύναμη προστασία, ενώ σταθερό μεγάλο ε μπορεί να προκαλέσει αστάθεια ή υπερβολικά conservative policy.

Η εργασία προτείνει να αντιμετωπίζεται το ε ως curriculum variable που αυξάνεται ή προσαρμόζεται ανάλογα με την πρόοδο του agent.

## Μέθοδος

Η DR-SPCRL συνδυάζει self-paced curriculum learning με distributionally robust optimization. Ο agent ξεκινά από ευκολότερο/στενότερο robustness setting και μετακινείται προς μεγαλύτερη perturbation budget όταν το performance criterion το επιτρέπει.

Σύμφωνα με το διαθέσιμο abstract, η adaptive schedule βελτιώνει τη σταθερότητα και το robustness–performance trade-off έναντι fixed ή heuristic schedules σε πολλαπλά environments.

## Συνάφεια

Η βασική αξία είναι η μεταφορά του robustness radius από σταθερό hyperparameter σε observable schedule. Για τη διπλωματική αυτό υποστηρίζει ένα απλό severity curriculum κατά την training/development phase:

- αρχικά χαμηλή perturbation severity,
- σταδιακή αύξηση όταν η clean/robust performance σταθεροποιείται,
- τελική αξιολόγηση σε held-out severities χωρίς online oracle adjustment.

Η μέθοδος δεν πρέπει να συγχέεται με deployment adaptation. Το curriculum χρησιμοποιείται κατά την εκπαίδευση για robust frozen policy και δεν αποτελεί detector ή recovery mechanism μετά από απρόβλεπτο changepoint.

## Πρωτόκολλο

- Log ε/severity schedule ανά training step.
- Δηλώνεται το progress criterion που αλλάζει το budget.
- Fixed-small, fixed-large και heuristic schedule comparators.
- Clean return και robust return ανά severity.
- Training stability και sample/compute overhead.
- Held-out test severities και extrapolation beyond maximum training ε.
- Απαγόρευση tuning της schedule πάνω στο final test sequence.

## Περιορισμοί

- Πρόσφατο arXiv preprint χωρίς peer-reviewed publication στο record.
- Το repository περιέχει abstract page, όχι πλήρες converted paper.
- Οι reported average improvements δεν μεταφέρονται αυτόματα στο GridWorld ή σε άλλους algorithms.
- Adaptive training curriculum δεν είναι online resilience.
- Η επιλογή progress criterion μπορεί να εισάγει νέο oracle/tuning channel.
- Μεγαλύτερη robustness budget μπορεί να μειώσει nominal utility ακόμη και με curriculum.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για development-only robustness/severity curricula και hyperparameter protocol, όχι ως βασικός deployment agent.