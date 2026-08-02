# SRC-2C9FFED27E — Efficient Policy Optimization in Robust Constrained MDPs with Iteration Complexity Guarantees

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Sourav Ganguly, Kishan Panaganti, Arnob Ghosh, Adam Wierman
- **Έκδοση:** NeurIPS 2025, 39th Conference on Neural Information Processing Systems
- **Τύπος:** θεωρητική και εμπειρική εργασία robust constrained RL
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Πρόβλημα

Η εργασία εξετάζει Robust Constrained Markov Decision Processes (RCMDPs), όπου μία policy πρέπει ταυτόχρονα:

1. να βελτιστοποιεί τη worst-case cumulative objective,
2. να ικανοποιεί constraint thresholds υπό το worst-case transition model,
3. να παραμένει εφαρμόσιμη όταν το nominal simulator διαφέρει από το πραγματικό environment.

Η διατύπωση είναι αυστηρότερη από standard CMDP, επειδή ο worst-case transition model για την objective function μπορεί να διαφέρει από εκείνον για κάθε constraint function.

## Θεωρητική δυσκολία

Οι κλασικές primal–dual μέθοδοι CMDP δεν μεταφέρονται άμεσα, επειδή το RCMDP δεν διαθέτει γενικά strong duality και η occupancy measure δεν είναι πλέον convex ως προς την policy. Επίσης δεν είναι ορθό να εφαρμόζεται ένα ενιαίο robust value backup στη σύνθετη Lagrangian objective όταν οι worst-case models για reward και constraints διαφέρουν.

## Προτεινόμενη μέθοδος

Οι συγγραφείς προτείνουν Robust Natural Policy Gradient (RNPG), με objective που:

- μειώνει πρώτα τη μέγιστη constraint violation όταν κάποιος περιορισμός παραβιάζεται,
- βελτιστοποιεί τη robust task objective όταν όλοι οι περιορισμοί ικανοποιούνται,
- αποφεύγει binary search που απαιτούσαν προηγούμενες epigraph-based προσεγγίσεις,
- χρησιμοποιεί KL regularization.

Με γνωστό strict-feasibility margin, παρέχεται policy που είναι ε-feasible και ε-suboptimal μετά από iteration complexity της τάξης O(ξ^-2 ε^-2). Όταν το margin δεν είναι γνωστό, η εγγύηση χαλαρώνει και η complexity αυξάνει.

## Εμπειρική αξιολόγηση

Η εργασία αξιολογεί finite-state και function-approximation παραλλαγές σε constrained RiverSwim, Garnet, modified FrozenLake, garbage collection και CartPole. Αναφέρονται σημαντικές wall-clock βελτιώσεις έναντι EPIRC-PGS, ιδίως για μεγάλο discount factor, καθώς και feasibility με ανταγωνιστική robust reward.

## Συνάφεια με τη διπλωματική

Η πηγή τεκμηριώνει ότι safety under model mismatch δεν μπορεί να μετρηθεί μόνο με return ή με nominal constraints. Για οποιονδήποτε safe/robust comparator πρέπει να αναφέρονται χωριστά:

- worst-case ή disturbed utility,
- κάθε constraint cost,
- violation margin έναντι threshold,
- feasibility rate ανά seed,
- uncertainty-set assumptions,
- training και evaluation compute.

Η εργασία δεν αποτελεί online changepoint adaptation method. Το uncertainty set είναι στατικό mathematical object και δεν παρέχεται detector, reset logic ή repeated-regime recovery.

## Πρακτική επίπτωση

Ο πλήρης RNPG/RCAC δεν είναι απαραίτητος στο βασικό implementation matrix. Η πηγή χρησιμοποιείται κυρίως για:

- ορθή διατύπωση robust safety objectives,
- αποφυγή λανθασμένου single-Lagrangian simplification,
- computational-cost reporting,
- διάκριση nominal feasibility από robust feasibility.

## Περιορισμοί

- Απαιτεί robust policy evaluator και συγκεκριμένες uncertainty-set assumptions, όπως rectangularity.
- Η strict-feasibility παράμετρος μπορεί να είναι άγνωστη στην πράξη.
- Οι εγγυήσεις αφορούν static robust mismatch, όχι environment changes μέσα στη διάρκεια μάθησης.
- Η function-approximation επέκταση αυξάνει σημαντικά την πολυπλοκότητα και δεν ταιριάζει αναγκαστικά στο resource-aware GridWorld scope.
- Η καλύτερη wall-clock απόδοση έναντι συγκεκριμένου solver δεν συνεπάγεται καλύτερη resilience από tabular reset/recency baselines.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για robust-constraint formulation, feasibility metrics και computational trade-offs· όχι ως υποχρεωτική υλοποίηση.