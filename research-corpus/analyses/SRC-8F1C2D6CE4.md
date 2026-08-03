# SRC-8F1C2D6CE4 — ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Chenliang Li, Junyu Leng, Jiaxiang Li, Youbang Sun, Shixiang Chen, Shahin Shahrampour, Alfredo Garcia
- **Έκδοση:** arXiv:2510.11899v1, 13 Οκτωβρίου 2025
- **Τύπος:** theoretical/empirical deep robust RL preprint
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Κεντρική ιδέα

Η εργασία αντιμετωπίζει τη robustness υπό epistemic dynamics uncertainty μέσω adaptive control της model capacity. Αντί να επιλύει nested worst-case min–max problem σε κάθε update, η AdaRL προσαρμόζει τον rank της policy/value representation ώστε να ισορροπεί:

- χαμηλή variance και καλύτερη generalization υπό περιορισμένα/μετατοπισμένα δεδομένα,
- επαρκή expressiveness για την task dynamics,
- αποφυγή over-parameterization και υπερβολικής conservatism.

Η lower-level optimization εκπαιδεύει policy υπό fixed-rank constraint με dynamics samples από Wasserstein ball. Η upper-level optimization μεταβάλλει τον rank μέσω projection σε low-rank manifold.

## Αποτελέσματα

Η εργασία παρέχει θεωρητική ανάλυση bias–variance για entropy-regularized RL με linear parameterization και epistemic uncertainty. Στα MuJoCo experiments αναφέρει καλύτερη απόδοση από fixed-rank, nominal και robust baselines, καθώς και σύγκλιση προς task-dependent intrinsic rank.

## Συνάφεια

Η βασική συνεισφορά στη διπλωματική είναι η υπενθύμιση ότι η agent capacity αποτελεί resilience/robustness hyperparameter. Ένας agent μπορεί να αποτυγχάνει όχι μόνο επειδή διατηρεί παλιά δεδομένα, αλλά και επειδή:

- είναι υπερβολικά απλός για το νέο regime,
- είναι υπερβολικά σύνθετος και υψηλής variance,
- προσαρμόζει λάθος capacity μετά από shift.

Ωστόσο, η μέθοδος αφορά deep continuous-control representation learning και δεν μεταφέρεται άμεσα στο tabular GridWorld.

## Πρωτόκολλο που προκύπτει

Εφόσον χρησιμοποιηθεί neural agent:

- αναφορά parameter count και effective rank,
- fixed-rank ablations,
- nominal versus perturbed performance,
- compute/memory για rank adaptation,
- clean performance loss από capacity restriction,
- rank trajectory πριν και μετά από dynamics shifts.

Σε tabular agents η αντίστοιχη αρχή εξετάζεται απλούστερα μέσω state abstraction ή factored/context-specific tables, όχι μέσω low-rank neural projection.

## Περιορισμοί

- arXiv v1 χωρίς peer-reviewed publication στο διαθέσιμο record,
- αξιολόγηση σε MuJoCo και όχι repeated GridWorld changepoints,
- robustness σε sampled model uncertainty, όχι explicit detection/recovery,
- σημαντική bi-level optimization πολυπλοκότητα,
- πιθανή σύγχυση intrinsic rank με γενικό task difficulty,
- δεν αποδεικνύει superiority έναντι απλών reset/recency mechanisms.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για capacity–uncertainty trade-offs και neural-agent threats to validity. Η AdaRL δεν εντάσσεται στο βασικό implementation matrix.