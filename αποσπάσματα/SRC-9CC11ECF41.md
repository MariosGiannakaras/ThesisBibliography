---
κωδικός: SRC-9CC11ECF41
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επαληθευμένα τεκμήρια — SRC-9CC11ECF41

## 1. Epistemic uncertainty από άγνωστες MDP παραμέτρους
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Introduction, Section 2
- **Ισχυρισμός:** Άγνωστες transition/cost parameters που εκτιμώνται από περιορισμένα δεδομένα δημιουργούν epistemic uncertainty διαφορετική από την inherent stochasticity του MDP.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο
- **Θέματα:** epistemic uncertainty; MDP parameters; posterior
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η αβεβαιότητα για το ποιο transition/cost model ισχύει προέρχεται από περιορισμένη γνώση και μπορεί να ενημερώνεται καθώς συλλέγονται δεδομένα.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν ισοδυναμεί με aleatoric transition randomness ούτε με απόδειξη environmental changepoint.

### Προτεινόμενη χρήση
Διάκριση stochasticity, epistemic model uncertainty και non-stationarity.

## 2. Worst-case robustness και conservativeness
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Introduction
- **Ισχυρισμός:** Distributionally robust approaches μπορούν να είναι υπερβολικά συντηρητικές επειδή βελτιστοποιούν ως προς την πιο δυσμενή distribution μέσα στο ambiguity set.
- **Κεφάλαιο:** Robust baselines / Trade-offs
- **Θέματα:** robust MDP; conservativeness; ambiguity set
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Strict worst-case optimization μπορεί να θυσιάσει performance σε πιο πιθανά scenarios, άρα robust score πρέπει να συνοδεύεται από nominal utility.

### Προτεινόμενη χρήση
Clean return + disturbed/tail return + conservativeness gap.

## 3. Posterior-dependent risk-sensitive policy
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 2.2–2.3
- **Ισχυρισμός:** Στο BR-MDP η policy εξαρτάται από physical state και posterior distribution και χρησιμοποιεί nested convex risk measure για την uncertainty των άγνωστων parameters.
- **Κεφάλαιο:** Bayesian agents / Risk
- **Θέματα:** posterior update; CVaR; risk measure; belief
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η risk preference και η posterior belief είναι δύο χωριστά στοιχεία: το posterior περιγράφει τι θεωρεί πιθανό ο agent, ενώ το risk measure καθορίζει πώς αξιολογεί τις πιθανές outcomes.

### Περιορισμοί και κίνδυνος παρερμηνείας
Risk sensitivity δεν αποτελεί detector και χαμηλό-tail optimization δεν συνεπάγεται ταχύτερη recovery.

## 4. Learning reduces parameter uncertainty under model assumptions
- **Τύπος:** πιστή παράφραση
- **Θέση:** Section 2.2
- **Ισχυρισμός:** Με αυξανόμενο dataset, υπό τις assumptions του parametric Bayesian model, το posterior συγκεντρώνεται προς την true parameter και το BR-MDP πλησιάζει το true-MDP problem.
- **Κεφάλαιο:** Uncertainty / Threats to validity
- **Θέματα:** Bayesian learning; posterior concentration; model assumptions
- **Κατάσταση:** επαληθευμένο

### Προτεινόμενη χρήση
Να δηλώνεται αν το true regime ανήκει στην assumed model family και να υπάρχει misspecification/out-of-family test.

## 5. Scope boundary: offline planning ≠ online changepoint adaptation
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, Contributions, Sections 3–4
- **Ισχυρισμός:** Η εργασία επιλύει infinite-horizon Bayesian-risk planning μέσω approximate bilevel DCP· δεν προτείνει sequential changepoint detector ή repeated-regime recovery algorithm.
- **Κεφάλαιο:** Threats to validity
- **Θέματα:** offline planning; computational cost; changepoint boundary
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η posterior ενημέρωση σε ένα άγνωστο model δεν πρέπει να παρουσιάζεται ως empirical evidence ανθεκτικότητας σε abrupt repeated changes.

### Προτεινόμενη χρήση
Υποστηρικτική θεωρητική πηγή, όχι ranking ή υποχρεωτικός implementation candidate.

### Παραπομπή
Lin & Zhou, AAAI-25, *Approximate Bilevel Difference Convex Programming for Bayesian Risk Markov Decision Processes*.