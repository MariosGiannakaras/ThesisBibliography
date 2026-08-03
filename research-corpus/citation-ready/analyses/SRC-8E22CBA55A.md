# SRC-8E22CBA55A — Safe Model-based Reinforcement Learning with Stability Guarantees

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Felix Berkenkamp, Matteo Turchetta, Angela P. Schoellig, Andreas Krause
- **Έκδοση:** NeurIPS 2017
- **Τύπος:** primary safe model-based RL / control-theoretic method
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Αντικείμενο

Η εργασία συνδυάζει model-based RL, Gaussian-process uncertainty και Lyapunov stability ώστε να βελτιώνει policy ενώ διατηρεί high-probability safety guarantees. Η safety ορίζεται μέσω region of attraction και asymptotic stability, όχι απλώς μέσω expected cumulative constraint cost.

Ξεκινά από αρχική γνωστή safe policy και επεκτείνει προοδευτικά την εκτιμώμενη safe region συλλέγοντας informative data μόνο σε καταστάσεις που θεωρούνται ασφαλείς.

## Κύρια αποτελέσματα

- Η policy και η model uncertainty χρησιμοποιούνται για να πιστοποιηθεί region of attraction μέσω Lyapunov decrease conditions.
- Η exploration περιορίζεται ώστε να μην εγκαταλείπεται η πιστοποιημένη safe region.
- Με regularity assumptions και calibrated GP confidence intervals, η agent μπορεί να μάθει περισσότερα για τις dynamics και να επεκτείνει με ασφάλεια τη safe region.
- Η empirical επίδειξη γίνεται σε simulated inverted pendulum.

## Συνάφεια

Η εργασία είναι χρήσιμη για να διαχωριστούν τρεις έννοιες που συχνά συγχέονται:

1. **stability recovery**: επιστροφή προς equilibrium/region of attraction,
2. **safe exploration**: συλλογή νέων δεδομένων χωρίς έξοδο από certified safe set,
3. **environmental resilience**: προσαρμογή policy μετά από αλλαγή των dynamics/reward/observations.

Η πρώτη και η δεύτερη δεν αποδεικνύουν αυτόματα την τρίτη.

## Πρωτόκολλο που προκύπτει

Εάν χρησιμοποιηθεί safety-controller ή model-based safety arm, καταγράφονται:

- initial certified safe set,
- size/coverage της safe region ανά χρόνο,
- uncertainty/confidence level,
- unsafe-state violations,
- denied/intervened exploratory actions,
- performance loss από safety restrictions,
- whether a post-change state lies inside or outside the previously certified region.

Μετά από abrupt dynamics change πρέπει να ελέγχεται αν οι παλιές certificates παραμένουν valid. Δεν επιτρέπεται να θεωρηθεί δεδομένο ότι stability guarantee του pre-change model μεταφέρεται στο νέο model.

## Περιορισμοί

- Continuous deterministic dynamics και strong regularity assumptions.
- Απαιτεί initial safe policy και Lyapunov function/candidate.
- Η GP-based safe exploration έχει διαφορετικές απαιτήσεις από tabular Q-learning.
- Δεν παρέχει changepoint detector ούτε benchmark repeated non-stationarity.
- Το “recovery” της control theory αφορά equilibrium behavior, όχι απαραίτητα recovery της learned task performance μετά από concept/environment shift.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται για safety/stability boundaries, certification invalidation μετά από dynamics change και για σαφή διάκριση control-theoretic recovery από RL resilience.