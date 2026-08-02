---
κωδικός: SRC-6F4B8E8DCE
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "NeurIPS 2023"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms

## Βιβλιογραφική ταυτότητα
Akifumi Wachi, Wataru Hashimoto, Xun Shen, Kazumune Hashimoto. NeurIPS 2023.

## Σκοπός και ερευνητικό ερώτημα
Ενοποιεί διαφορετικές αυστηρές safe-exploration formulations και προτείνει meta-algorithm που συνδυάζει unconstrained RL με uncertainty quantification και emergency-stop authority.

## Σύνοψη
Η εργασία διατυπώνει Generalized Safe Exploration (GSE) με instantaneous time-varying safety thresholds και δείχνει πώς κοινές cumulative/state/instantaneous safety formulations μπορούν να μετασχηματιστούν σε αυτή. Το MASE χρησιμοποιεί confidence bounds για safety cost και emergency-stop/reset όταν δεν υπάρχει επαρκώς ασφαλής action.

## Μεθοδολογία
- episodic CMDP,
- generalized safe exploration constraints,
- uncertainty quantifier για safety cost,
- emergency stop action,
- GLM variant με theoretical guarantees,
- GP + deep RL variant,
- GridWorld και Safety Gym experiments.

## Κύρια ευρήματα
1. Διαφορετικές αυστηρές safety formulations δεν είναι ισοδύναμες με expected-cost CMDP constraints.
2. Η during-training safety απαιτεί explicit assumptions και external capability όπως emergency stop/reset.
3. Uncertainty quantifier χρησιμοποιείται για upper-confidence safety screening πριν εκτελεστεί action.
4. Safety guarantee δεν συνεπάγεται environmental adaptation ή task-performance recovery.

## Υποθέσεις και ορισμοί
Υποθέτει safety margin, uncertainty quantifier με high-probability coverage και emergency-stop action που επιστρέφει στο initial state όταν δεν υπάρχει ασφαλής επιλογή.

## Περιορισμοί και απειλές εγκυρότητας
- ισχυρή emergency-stop/reset δυνατότητα,
- safety model regularity/calibration assumptions,
- fully observable states στο βασικό formulation,
- safe-exploration objective, όχι changepoint detector,
- deep/GP variant μεγαλύτερου implementation cost.

## Σχέση με άλλες πηγές
Συμπληρώνει `SRC-91D94DB95B`/CPO, `SRC-6126015212`/returnability και `SRC-73C145D523`/recovery. Σε αντίθεση με expected CMDP safety, απαιτεί αυστηρότερη during-training constraint handling.

## Χρήση στη διπλωματική
Υποστηρικτική πηγή για safety protocol. Πρέπει να δηλώνονται:
- guarantee type: expected / chance / instantaneous / high-probability,
- emergency-stop ή reset authority,
- intervention/reset count,
- safety-model confidence/calibration,
- utility cost από interventions.

Emergency stop είναι prior capability και δεν μετρά ως learned resilience.

## Απαιτούμενα αποσπάσματα
1. GSE ενοποιεί πολλές αυστηρές safety formulations αλλά όχι κάθε CMDP formulation.
2. Emergency stop/reset είναι ουσιώδης assumption.
3. Confidence bounds μπορούν να μπλοκάρουν action πριν από violation.
4. Safety guarantee και task recovery πρέπει να αναφέρονται χωριστά.

## Κατάσταση επαλήθευσης
Επαληθεύτηκε στο πλήρες NeurIPS paper. Επιλέγεται ως υποστηρικτική.