# SRC-C90D59EC8C — State Entropy Regularization for Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Yonatan Ashlag, Uri Koren, Mirco Mutti, Esther Derman, Pierre-Luc Bacon, Shie Mannor
- **Έκδοση:** NeurIPS 2025, Oral
- **Τύπος:** θεωρητική εργασία με εμπειρική αξιολόγηση
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Κεντρική ιδέα

Η εργασία διακρίνει την policy entropy από τη state-visitation entropy. Η policy entropy ενθαρρύνει stochastic actions τοπικά, ενώ η state entropy ενθαρρύνει ευρύτερη κάλυψη του state space.

Οι συγγραφείς μελετούν κατά πόσο η state-entropy regularization βελτιώνει robustness σε structured και spatially correlated perturbations, δηλαδή αλλαγές που επηρεάζουν συνεκτικές περιοχές του environment αντί για ανεξάρτητο μικρό noise σε κάθε transition.

## Κύρια αποτελέσματα

Σύμφωνα με το επίσημο NeurIPS abstract:

- παρέχονται formal guarantees για reward και transition uncertainty,
- η state entropy μπορεί να βελτιώνει robustness σε structured/spatial perturbations,
- παρουσιάζονται και settings όπου η μέθοδος αποτυγχάνει,
- τα οφέλη είναι πιο ευαίσθητα από την policy entropy στον αριθμό rollouts που χρησιμοποιούνται για policy evaluation.

Η ύπαρξη failure cases είναι σημαντική: υψηλή coverage δεν εγγυάται ότι ο agent θα ανακάμψει γρήγορα ή ότι η εξερεύνηση είναι ασφαλής.

## Συνάφεια με τη διπλωματική

Η πηγή υποστηρίζει ένα απλό exploration/coverage ablation:

- standard epsilon-greedy ή policy-entropy exploration,
- state-count/state-entropy regularization,
- reactive exploration reset μετά από αλλαγή.

Σε tabular GridWorld η state entropy μπορεί να προσεγγιστεί απευθείας από visitation counts, χωρίς neural estimator. Το μέτρο είναι ιδιαίτερα σχετικό σε wall/goal changes που καθιστούν προηγουμένως σπάνιες περιοχές κρίσιμες.

## Πρωτόκολλο

- Αναφορά state-visitation distribution και entropy ανά regime.
- Χωριστή policy-action entropy και state entropy.
- Coverage of newly relevant states μετά από changepoint.
- Ίδιο interaction budget μεταξύ exploration methods.
- Sensitivity στον αριθμό evaluation rollouts.
- Utility και hazard cost της πρόσθετης exploration.
- Χωριστά structured/spatial perturbations και ανεξάρτητο stochastic noise.

## Περιορισμοί

- Το διαθέσιμο repository record είναι official poster/abstract page και όχι πλήρες converted paper, άρα δεν εξάγονται λεπτομερή numerical claims.
- Η εργασία αφορά robustness/generalization από coverage, όχι online change detection.
- State entropy μπορεί να σπαταλά interactions σε άσχετες περιοχές ή να αυξάνει unsafe exploration.
- Τα formal guarantees εξαρτώνται από τον ακριβή uncertainty model.
- Δεν αποδεικνύεται υπεροχή έναντι reset, recency ή context recall σε repeated non-stationarity.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για tabular state-coverage ablation και structured-perturbation reasoning, όχι ως βασικός resilience agent.