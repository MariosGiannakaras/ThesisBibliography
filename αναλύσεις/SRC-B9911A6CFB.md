---
κωδικός: SRC-B9911A6CFB
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI 2023"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Safe Reinforcement Learning via Shielding under Partial Observability

## Βιβλιογραφική ταυτότητα
Steven Carr, Sebastian Junges, Nils Jansen, Ufuk Topcu. AAAI 2023.

## Σκοπός και ερευνητικό ερώτημα
Μελετά πώς ενσωματώνεται formal shielding σε deep RL όταν ο agent δεν παρατηρεί πλήρως την πραγματική κατάσταση και πρέπει να βασίζεται σε observation histories/belief support.

## Σύνοψη
Η εργασία συνδυάζει state estimator και shield για POMDPs. Το shield χρησιμοποιεί partial model knowledge —ιδίως το graph/support των δυνατών transitions— ώστε να περιορίζει actions σε εκείνα που διατηρούν reach-avoid safety. Εξετάζεται επίσης gradual phase-out του shield μετά από αρχική shielded εκπαίδευση.

## Μεθοδολογία
- finite POMDPs,
- belief-support state estimation,
- reach-avoid specifications,
- permissive shield,
- partial graph-preserving model,
- deep RL empirical evaluation,
- shield phase-out/bootstrapping experiments.

## Κύρια ευρήματα
1. State estimation μόνο του δεν εγγυάται safety· το shield παρεμβαίνει ρητά στο action set.
2. Shielding μπορεί να επιταχύνει convergence αποφεύγοντας unsafe exploration σε συγκεκριμένα experiments.
3. Η safety guarantee βασίζεται σε prior knowledge του transition-support graph και specification.
4. Shield μπορεί να γίνει σταδιακά λιγότερο ενεργό, αλλά αυτό είναι ξεχωριστή intervention policy και όχι environmental adaptation.

## Υποθέσεις και ορισμοί
Το partial model μπορεί να μην γνωρίζει ακριβείς probabilities/rewards αλλά πρέπει να διατηρεί το support των δυνατών transitions. Η safety ορίζεται μέσω reach-avoid specification.

## Περιορισμοί και απειλές εγκυρότητας
- απαιτεί formal specification και transition-support knowledge,
- partial-observability POMDP setting με διαφορετικό computational burden από tabular GridWorld,
- shield μπορεί να είναι conservative,
- δεν ανιχνεύει dynamics changepoints,
- αν structural change μεταβάλλει το support graph, το παλιό shield μπορεί να μην παραμένει valid.

## Σχέση με άλλες πηγές
Συμπληρώνει `SRC-23A2C07D09` για runtime assurance, `SRC-E8CAAF02BE` για POMDP beliefs και `SRC-8718299821` για foundational shielding.

## Χρήση στη διπλωματική
Υποστηρικτική πηγή για partial-observability/safety arm. Κλειδώνει:
- prior graph/model support δηλώνεται ως information advantage,
- shield interventions και blocked actions καταγράφονται,
- state-estimation error και safety violations αναφέρονται χωριστά,
- μετά από structural shift γίνεται shield/model revalidation,
- phase-out schedule δηλώνεται ρητά.

## Απαιτούμενα αποσπάσματα
1. Belief-support estimator και shield είναι διαφορετικές knowledge interfaces.
2. Shield guarantee χρησιμοποιεί partial transition-support model.
3. Structural support change απαιτεί επανέλεγχο του shield.
4. Shield phase-out δεν ισοδυναμεί με learned resilience.

## Κατάσταση επαλήθευσης
Επαληθεύτηκε στο πλήρες AAAI paper. Επιλέγεται ως υποστηρικτική.