---
κωδικός: SRC-90A20ED43A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2410.19852v1, 22 Οκτωβρίου 2024"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Survival of the Fittest: Evolutionary Adaptation of Policies for Environmental Shifts

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Sheryl Paul, Jyotirmoy V. Deshmukh
- **Έτος:** 2024
- **Τύπος πηγής:** πρωτογενής αλγοριθμική εργασία / arXiv preprint
- **URL:** https://arxiv.org/abs/2410.19852
- **Πρωτότυπο που ελέγχθηκε:** πλήρες arXiv κείμενο στο `πηγές/SRC-90A20ED43A.md`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς μπορεί μία ήδη εκπαιδευμένη policy να προσαρμοστεί γρήγορα όταν η δυναμική ή η γεωμετρία του περιβάλλοντος μεταβληθεί σημαντικά και η παλιά optimal policy γίνει υποβέλτιστη ή αποτύχει. Η έμφαση δεν βρίσκεται στη worst-case προστασία πριν από την αλλαγή, αλλά στη μεταγενέστερη, επαναληπτική αναπροσαρμογή της policy μέσα στο νέο περιβάλλον.

## Σύνοψη

Οι συγγραφείς προτείνουν τον Evolutionary Robust Policy Optimization (ERPO), έναν gradient-free μηχανισμό policy adaptation εμπνευσμένο από replicator dynamics της evolutionary game theory. Η training policy αποτελεί μεταβαλλόμενο μείγμα της παλιάς optimal policy και μιας νέας policy. Παράγονται batches trajectories στο μετατοπισμένο περιβάλλον και οι state–action πιθανότητες ενημερώνονται με μεγαλύτερο βάρος για trajectories των οποίων η απόδοση αποκλίνει ουσιαστικά από την απόδοση του batch. Καθώς η διαδικασία προχωρά, μειώνεται η προσκόλληση στην παλιά policy και αυξάνεται η επιρροή της νέας policy.

Η εργασία δίνει θεωρητικό convergence αποτέλεσμα υπό sparse-reward και sampling assumptions και συγκρίνει τον ERPO με PPO, PPO με domain randomization, DQN και A2C, τόσο με εκπαίδευση από την αρχή όσο και με warm start από μοντέλο του αρχικού περιβάλλοντος.

## Μεθοδολογία

- **Πρόβλημα:** finite-horizon MDP με διακριτά state και action spaces, sparse goal-oriented reward και μεγάλη μεταβολή της transition structure.
- **Adaptation mechanism:** weighted combination παλιάς και νέας policy, batch trajectories και replicator-style updates ανά state–action pair.
- **Baselines:** PPO, PPO-DR, DQN, A2C, με scratch και pretrained/warm-start παραλλαγές όπου εφαρμόζεται.
- **Περιβάλλοντα:** FrozenLake, Taxi, CliffWalking, MiniGrid DistributionShift και custom MiniGrid Walls&Lava με αυξανόμενα επίπεδα μετατόπισης.
- **Reported outcomes:** episode/sample efficiency, return, convergence behavior και computational time.
- **Θεωρία:** convergence προς optimal policy στο νέο περιβάλλον υπό τις δηλωμένες sparsity και sampling assumptions.

## Κύρια ευρήματα

1. **Η post-shift adaptation είναι διαφορετική από τη static robustness.** Ο ERPO αρχίζει αφού είναι διαθέσιμο το μετατοπισμένο περιβάλλον και χρησιμοποιεί νέα trajectories για να ανακατασκευάσει την policy. Δεν είναι frozen robust policy ούτε μηχανισμός πρόληψης της πτώσης.
2. **Η παλιά policy λειτουργεί ως προσωρινό prior και όχι ως μόνιμος περιορισμός.** Το βάρος της μειώνεται καθώς αυξάνεται η εμπιστοσύνη στη νέα policy. Αυτό δημιουργεί σαφές stability–plasticity hyperparameter: υπερβολική προσκόλληση καθυστερεί την προσαρμογή, ενώ πολύ γρήγορη εγκατάλειψη χάνει χρήσιμη προηγούμενη γνώση.
3. **Η επιλογή informative trajectories αποτελεί τον πυρήνα της ενημέρωσης.** Σε αντίθεση με updates που αντιμετωπίζουν ομοιόμορφα τα samples ενός batch, ο ERPO δίνει έμφαση σε trajectories που υπεραποδίδουν ή υποαποδίδουν σε σχέση με το batch.
4. **Τα πειράματα καλύπτουν structural shifts σε navigation tasks.** Walls, lava, altered layouts και standard discrete navigation benchmarks είναι άμεσα συγγενή με τα ελεγχόμενα GridWorld scenarios της διπλωματικής.
5. **Οι συγγραφείς αναφέρουν ταχύτερη προσαρμογή και καλύτερη απόδοση από τα συγκεκριμένα baselines στα εξεταζόμενα settings.** Αυτό αποτελεί empirical evidence για τα συγκεκριμένα configurations, όχι καθολική κατάταξη ERPO έναντι PPO/DQN/A2C.
6. **Η εργασία περιορίζεται σε διακριτά state–action spaces και single-agent settings.** Η επέκταση σε continuous spaces και multi-agent learning παραμένει future work.
7. **Η εμπειρική αναπαραγωγιμότητα χρειάζεται προσοχή.** Στο διαθέσιμο κείμενο δεν εντοπίστηκε πλήρης standardised αναφορά seeds, confidence intervals και ενιαίου statistical test protocol για όλες τις συγκρίσεις. Τα αποτελέσματα δεν θα χρησιμοποιηθούν ως απόλυτη superiority claim.

## Σχέση με τη διπλωματική

Η πηγή είναι άμεσα χρήσιμη για severe post-change adaptation σε GridWorld, ιδίως όταν η αλλαγή επηρεάζει εμπόδια, hazardous cells ή paths και η παλιά policy περιέχει ακόμη μερικώς χρήσιμη πληροφορία. Συμπληρώνει:

- το detector-triggered reset του `SRC-7456165CEA`,
- το context recall του `SRC-D14764616F`,
- τη recent-memory λογική του `SRC-4B456A9363`,
- τη διάκριση negative transfer του `SRC-67AB8572A9`.

Ο ERPO δεν θα προστεθεί αυτόματα ως βασικός agent. Μπορεί να υλοποιηθεί ως προαιρετικό tabular policy-adaptation pilot μόνο εάν η πολυπλοκότητα παραμένει συμβατή με το τελικό scope.

## Απαιτήσεις πρωτοκόλλου που προκύπτουν

- χωριστές κατηγορίες `static_robustness` και `post_shift_retraining`,
- καταγραφή `old_policy_weight` ή αντίστοιχου adherence schedule,
- scratch, warm-start και no-transfer comparators,
- μέτρηση adaptation interactions και wall-clock/computational overhead,
- severe structural shifts χωριστά από μικρή bounded stochastic perturbation,
- clean nominal performance πριν από την αλλαγή και recovery μετά την αλλαγή,
- έλεγχος negative transfer όταν η παλιά policy είναι παραπλανητική.

## Περιορισμοί και απειλές εγκυρότητας

Η θεωρία βασίζεται σε sparse rewards και συγκεκριμένες sampling assumptions. Οι συγκρίσεις περιλαμβάνουν διαφορετικού τύπου αλγορίθμους και η εφαρμογή τους μπορεί να εξαρτάται από implementation και tuning choices. Η εργασία είναι arXiv preprint στην έκδοση που ελέγχθηκε. Τα discrete navigation results είναι συναφή, αλλά δεν αποδεικνύουν ότι η ίδια ordering θα ισχύσει σε κάθε stochastic GridWorld ή σε repeated, gradual και partially observable changes.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Σχετικές εργασίες, Agent architectures, Post-change adaptation, Πειραματικά scenarios, Μετρικές, Threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** warm-start policy adaptation μπορεί να είναι αποτελεσματική μετά από μεγάλες structural shifts· η προσκόλληση στην παλιά policy πρέπει να μειώνεται ελεγχόμενα· scratch και warm-start baselines πρέπει να συγκρίνονται χωριστά.
- **Τι δεν πρέπει να ισχυριστούμε:** ότι ο ERPO είναι καθολικά ανώτερος· ότι αποτελεί robust policy πριν από την αλλαγή· ότι οι theoretical assumptions ισχύουν αυτόματα στο τελικό GridWorld.
- **Ρόλος:** κύρια

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτό implementation ζήτημα:** feasibility pilot μόνο μετά την οριστικοποίηση του βασικού tabular baseline matrix.
