---
κωδικός: SRC-6E7AFA8AC0
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Annals of Statistics 2022, DOI 10.1214/22-AOS2225"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Toward the Theoretical Understandings of Robust Markov Decision Processes: Sample Complexity and Asymptotics

## Βιβλιογραφική ταυτότητα
Wenhao Yang, Liangyu Zhang, Zhihua Zhang. Annals of Statistics, 2022.

## Σκοπός και ερευνητικό ερώτημα
Μελετά πόσα samples απαιτούνται για ακριβή robust policy/value estimation και πώς επηρεάζουν τα guarantees η γεωμετρία και η rectangularity του uncertainty set.

## Σύνοψη
Η εργασία παρέχει finite-sample και asymptotic ανάλυση για robust MDPs με L1, χ² και KL uncertainty sets, τόσο υπό (s,a)-rectangular όσο και s-rectangular υποθέσεις. Δείχνει ότι το κόστος εκτίμησης εξαρτάται ουσιαστικά από radius, discount factor, state/action cardinality και uncertainty-set structure.

## Μεθοδολογία
- tabular robust MDPs,
- model-based estimation από generative model ή offline occupancy data,
- robust value/policy estimation,
- finite-sample deviation bounds,
- asymptotic normality robust value estimators,
- experiments για empirical coverage.

## Κύρια ευρήματα
1. Robust MDPs δεν είναι κατ’ ανάγκη εκθετικά δυσκολότερα από nominal MDPs ως προς effective horizon.
2. s-rectangular sets συνήθως απαιτούν περισσότερα samples από (s,a)-rectangular sets.
3. Uncertainty-set radius και divergence family μεταβάλλουν sample requirements και conservativeness.
4. Statistical inference για robust value estimates είναι εφικτή υπό τις συγκεκριμένες υποθέσεις.

## Υποθέσεις και ορισμοί
Η εργασία αφορά uncertainty γύρω από model estimates και όχι piecewise-stationary online changepoints. Το uncertainty set θεωρείται μέρος της formulation και δεν ανιχνεύεται online ως αλλαγή regime.

## Περιορισμοί και απειλές εγκυρότητας
- ισχυρές rectangularity assumptions,
- tabular finite MDPs,
- generative/offline data settings κυρίως,
- δεν παρέχει recovery curves ή detector metrics,
- sample-complexity guarantees δεν μεταφράζονται αυτομάτως σε best practical agent.

## Σχέση με άλλες πηγές
Συμπληρώνει `SRC-52E62452B8` για robust-MDP semantics και `SRC-9D663D35D0` για model-free robust Q-learning. Σε σχέση με `SRC-D1B6BA711E`, αποτελεί περισσότερο statistical-estimation foundation παρά online exploration algorithm.

## Χρήση στη διπλωματική
Υποστηρικτική θεωρητική πηγή για:
- δήλωση uncertainty-set family/radius,
- sensitivity analysis του robustness radius,
- διάκριση (s,a)-rectangular και s-rectangular assumptions,
- resource accounting για samples/model storage,
- αποφυγή γενικών ισχυρισμών ότι robust RL είναι «δωρεάν» ή πάντα καλύτερο.

## Απαιτούμενα αποσπάσματα
1. Robust sample complexity εξαρτάται από uncertainty-set structure και radius.
2. s-rectangular formulation είναι γενικότερη αλλά μπορεί να είναι ακριβότερη.
3. Robustness formulation αντιμετωπίζει model mismatch, όχι κατ’ ανάγκη online change recovery.

## Κατάσταση επαλήθευσης
Επαληθεύτηκε στο πλήρες journal PDF. Επιλέγεται ως supporting theoretical evidence.