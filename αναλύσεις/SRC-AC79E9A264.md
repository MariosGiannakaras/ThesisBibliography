# Επιστημονική ανάλυση — SRC-AC79E9A264

## Βιβλιογραφική ταυτότητα

- **Τίτλος:** Robust Policy Learning over Multiple Uncertainty Sets
- **Συγγραφείς:** Annie Xie, Shagun Sodhani, Chelsea Finn, Joelle Pineau, Amy Zhang
- **Δημοσίευση:** ICML 2022, PMLR 162
- **Προτεινόμενος ρόλος:** υποστηρικτική πηγή

## Ερευνητικό πρόβλημα

Η εργασία εξετάζει μεταφορά πολιτικής σε νέο περιβάλλον όταν το ακριβές latent context δεν είναι γνωστό και η αβεβαιότητα δεν περιγράφεται από ένα μοναδικό, σταθερό uncertainty set. Η απλή robust RL μπορεί να γίνει υπερβολικά συντηρητική, ενώ η απλή system identification αποτυγχάνει όταν ορισμένες παράμετροι δεν είναι ταχέως αναγνωρίσιμες.

## Μέθοδος

Η SIRSA συνδυάζει:

1. πιθανοτικό system-identification model από σύντομο ιστορικό αλληλεπίδρασης,
2. uncertainty-set-conditioned policy,
3. risk-sensitive/CVaR objective για την υπολειπόμενη μη αναγνωρίσιμη αβεβαιότητα.

Έτσι η agent μειώνει την αβεβαιότητα όπου υπάρχουν πληροφοριακές ενδείξεις και ενεργεί robustly ως προς ό,τι παραμένει αβέβαιο.

## Κύρια ευρήματα

- Η πολιτική γενικεύει σε νέα uncertainty sets καλύτερα από robust RL ή system identification μεμονωμένα.
- Η εργασία αναφέρει μεταφορά σε misspecified priors και σε non-stationary dynamics.
- Η identifiability αντιμετωπίζεται ως δομικός περιορισμός: λίγες αλληλεπιδράσεις δεν αρκούν πάντα για point identification.
- Το CVaR επιτρέπει συνεχή έλεγχο της συντηρητικότητας, αντί για αποκλειστικά expected-return ή strict max-min στόχο.

## Σχέση με τη διπλωματική

Η πηγή στηρίζει έναν καθαρό διαχωρισμό μεταξύ:

- **context inference** από πρόσφατες μεταβάσεις,
- **robust action selection** όταν το context δεν αναγνωρίζεται πλήρως,
- **online adaptation** μετά από αλλαγή δυναμικής.

Για resource-aware GridWorld δεν απαιτείται υλοποίηση της πλήρους SIRSA. Η πρακτική αφαίρεση είναι ένας baseline που διατηρεί belief/σύνολο πιθανών regimes και επιλέγει συντηρητική ενέργεια όταν η confidence είναι χαμηλή.

## Πειραματικές επιπτώσεις

Για αντίστοιχη αξιολόγηση πρέπει να καταγράφονται:

- χρόνος/βήματα μέχρι context identification,
- posterior ή candidate-set size,
- performance πριν και μετά την identification,
- worst-tail return ή χαμηλό quantile,
- nominal-performance cost της συντηρητικότητας,
- misspecified-prior scenario,
- μη αναγνωρίσιμα context pairs.

## Περιορισμοί

- Η μέθοδος αφορά continuous-control και family of parameterized tasks, όχι arbitrary structural GridWorld changes.
- Χρησιμοποιεί observed context labels κατά την εκπαίδευση του identification model.
- Απαιτεί εκπαιδευτική κατανομή uncertainty sets και δεν εγγυάται arbitrary OOD transfer.
- Η non-stationary αξιολόγηση δεν ισοδυναμεί με πλήρες repeated-changepoint benchmark.

## Απόφαση

**Επαληθευμένη — εξαγωγή ναι, ως υποστηρικτική πηγή.** Χρησιμοποιείται για hybrid inference-plus-robustness architecture και για identifiability/conservativeness trade-offs, όχι ως υποχρεωτική υλοποίηση.