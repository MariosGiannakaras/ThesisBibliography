# SRC-3BF9404CC3 — Learning to Recover for Safe Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Haoyu Wang, Xin Yuan, Qinqing Ren
- **Έτος:** 2023
- **Τύπος:** empirical safe-RL architecture paper
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Πρόβλημα

Η εργασία εξετάζει safe exploration όταν δεν είναι πρακτική η χειροκίνητη κατασκευή safety controller. Προτείνει τριφασική αρχιτεκτονική όπου safety critic και task-unaware recovery policy μαθαίνονται πριν από την task-policy training phase.

## TU-Recovery architecture

Η διαδικασία διαχωρίζεται σε:

1. exploration stage για μάθηση safety critic,
2. recovery-learning stage για policy που ελαχιστοποιεί το risk estimate,
3. task-training stage όπου action decider επιλέγει task ή recovery action.

Το intervention ενεργοποιείται όταν το estimated risk της task action υπερβαίνει threshold.

## Μοναδική χρήσιμη συνεισφορά

Η εργασία αναλύει το `adversarial phenomenon`: κοντά στο boundary της recovery zone, task και recovery policies μπορεί να προτείνουν αντίθετες actions και να προκαλούν oscillation ή stuck behavior. Η παρατήρηση αυτή είναι σημαντική για τη διπλωματική επειδή ένας fallback/controller μπορεί να μειώνει violations αλλά να δημιουργεί νέο failure mode και υψηλό intervention overhead.

Οι συγγραφείς προσθέτουν auxiliary reward ώστε η task policy να μαθαίνει να αποφεύγει ή να ανακάμπτει από high-risk regions, μειώνοντας τη σύγκρουση με τον recovery controller.

## Εμπειρικό evidence

Η μέθοδος αξιολογείται σε robot-navigation environment και συγκρίνεται κυρίως με unconstrained counterpart. Αναφέρεται βελτίωση σε reward και constraint violations, ενώ το auxiliary reward βελτιώνει το reward-to-cost ratio.

Το evidence είναι περιορισμένο σε scope και δεν θεμελιώνει γενική υπεροχή έναντι Recovery RL, shields ή detector-triggered reset.

## Εφαρμογή στη διπλωματική

Η πηγή δεν προσθέτει νέο βασικό agent. Προσθέτει controller diagnostics για οποιοδήποτε learned/local recovery mechanism:

- intervention boundary oscillation,
- consecutive intervention duration,
- task–recovery action disagreement,
- progress loss λόγω fallback,
- states με repeated controller hand-off.

Σε GridWorld μπορεί να εξεταστεί απλό fallback policy προς κοντινό safe state, μόνο ως safety ablation.

## Απαιτήσεις πρωτοκόλλου

- Log proposed task action και executed action.
- Log disagreement indicator μεταξύ task και fallback.
- Count intervention bursts, όχι μόνο συνολικό intervention count.
- Μετράται stuck/oscillation rate κοντά σε hazards.
- Αναφέρονται reward, violation count, severity και controller-induced delay χωριστά.
- Ίδιο risk threshold tuning protocol για όλες τις συγκρίσεις.

## Περιορισμοί

- Safe recovery controller δεν είναι environment-change detector.
- Η recovery αφορά επιστροφή σε safer state, όχι αποκατάσταση policy performance μετά από regime change.
- Η αξιολόγηση είναι περιορισμένη και η γλωσσική/τυπογραφική ποιότητα της εργασίας μέτρια.
- Απαιτεί pretraining της safety critic/recovery policy σε safety-oriented environment.
- Η auxiliary reward αλλάζει το learning objective και μπορεί να επηρεάσει task optimality.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται ειδικά για controller-conflict diagnostics και intervention-induced oscillation, όχι ως βασικό resilience algorithm.