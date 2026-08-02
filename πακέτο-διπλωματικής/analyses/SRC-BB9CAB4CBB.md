# Επαληθευμένη ανάλυση — SRC-BB9CAB4CBB

## Βιβλιογραφική ταυτότητα

- **Τίτλος:** Decision-making under uncertainty: beyond probabilities — Challenges and perspectives
- **Συγγραφείς:** Thom Badings, Thiago D. Simão, Marnix Suilen, Nils Jansen
- **Έτος:** 2023
- **Τύπος:** peer-reviewed position/review paper
- **Πηγή:** International Journal on Software Tools for Technology Transfer
- **DOI:** 10.1007/s10009-023-00704-3

## Ερευνητικό αντικείμενο

Η εργασία οργανώνει μοντέλα λήψης αποφάσεων υπό αβεβαιότητα γύρω από τη διάκριση aleatoric και epistemic uncertainty. Εξετάζει MDP/POMDP, robust ή uncertain MDPs, Bayesian RL, constrained/safe RL και formal methods. Περιλαμβάνει ειδική συζήτηση για προσαρμογή σε drifting ή abrupt αλλαγές κατανομών.

## Κύρια ευρήματα και έννοιες

1. Η aleatoric uncertainty είναι εγγενής στο περιβάλλον και συνήθως μοντελοποιείται με πιθανότητες μεταβάσεων ή παρατηρήσεων.
2. Η epistemic uncertainty αφορά έλλειψη γνώσης και μπορεί να μειωθεί με περισσότερα δεδομένα ή αλληλεπίδραση.
3. Ένα uncertain/robust MDP μπορεί να εκφράσει epistemic uncertainty πάνω στις πιθανότητες ενός υποκείμενου MDP μέσω uncertainty sets.
4. Worst-case robust objectives μπορούν να προσφέρουν εγγυήσεις, αλλά ενδέχεται να οδηγήσουν σε υπερβολικά συντηρητικές πολιτικές.
5. Σε online RL, η διερεύνηση μπορεί να μειώσει epistemic uncertainty· αντίθετα, aleatoric variability δεν εξαφανίζεται με περισσότερα samples.
6. Για changing distributions, κρίσιμο πρόβλημα είναι να αποφασιστεί πότε μια απίθανη τροχιά αποτελεί φυσιολογική στοχαστικότητα και πότε ένδειξη πραγματικής αλλαγής dynamics.

## Σχέση με τη διπλωματική

Η πηγή ενισχύει το μοντέλο αβεβαιότητας της διπλωματικής και αποτρέπει τρεις συγχύσεις:

- observation/action stochasticity δεν ταυτίζεται με model uncertainty,
- uncertainty score δεν ταυτίζεται αυτόματα με calibrated change detector,
- robust policy πριν από την αλλαγή δεν ταυτίζεται με online resilience μετά την αλλαγή.

Στο GridWorld, οι perturbation probabilities που είναι γνωστές και σταθερές θα καταγράφονται ως aleatoric uncertainty. Άγνωστες αλλαγές στον κανόνα, στη μετάβαση ή στη σοβαρότητα θα αντιμετωπίζονται ως epistemic/model uncertainty μέχρι να ανιχνευθούν ή να εκτιμηθούν.

## Επιπτώσεις στον πειραματικό σχεδιασμό

- Κάθε scenario πρέπει να δηλώνει αν η αβεβαιότητα είναι γνωστή, εκτιμώμενη ή άγνωστη στον agent.
- Θα διαχωρίζονται `environment_stochasticity` και `model_uncertainty`.
- Αύξηση prediction error μετά από change θα θεωρείται change evidence, όχι από μόνη της απόδειξη αλλαγής.
- Robust baselines θα αξιολογούνται ταυτόχρονα σε nominal return και disturbed return, ώστε να μετράται conservativeness.
- Η προσαρμογή θα αξιολογείται μετά από πραγματικό change onset, ανεξάρτητα από το αν ο agent χρησιμοποιεί explicit uncertainty set.

## Περιορισμοί

- Είναι position/review paper και όχι ενιαία πρωτογενής πειραματική σύγκριση.
- Καλύπτει ευρύτερο πεδίο formal verification, control και RL, άρα δεν επιλέγει συγκεκριμένο GridWorld algorithm.
- Πολλά formal uncertainty models έχουν assumptions και computational costs που δεν μεταφέρονται αυτούσια στη μικρή εμπειρική μελέτη.

## Απόφαση

- **Κατάσταση:** επαληθευμένη
- **Ρόλος:** υποστηρικτική
- **Εξαγωγή:** ναι
- **Χρήση:** uncertainty taxonomy, detector interpretation, robust-versus-adaptive boundaries και threats to validity.
