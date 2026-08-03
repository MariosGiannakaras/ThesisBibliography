---
κωδικός: SRC-CC5B34C28C
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI-26"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Best-Effort Policies for Robust Markov Decision Processes

## Βιβλιογραφική ταυτότητα
Alessandro Abate, Thom Badings, Giuseppe De Giacomo, Francesco Fabiano. AAAI 2026.

## Σκοπός και ερευνητικό ερώτημα
Μελετά πώς επιλέγεται policy όταν περισσότερες από μία policies είναι ισοδύναμα βέλτιστες ως προς το worst-case robust objective αλλά διαφέρουν στην απόδοση για λιγότερο δυσμενείς transition models.

## Σύνοψη
Η εργασία εισάγει optimal robust best-effort (ORBE) policies: διατηρούν την optimal worst-case guarantee και ταυτόχρονα δεν κυριαρχούνται από άλλη policy σε ολόκληρο το uncertainty set. Πρόκειται για principled tie-breaker που περιορίζει άσκοπη συντηρητικότητα χωρίς να εγκαταλείπει το robust objective.

## Μεθοδολογία
- discounted finite RMDPs,
- s-rectangular uncertainty sets,
- dominance/best-effort ordering policies,
- characterization και algorithm για ORBE,
- numerical feasibility experiments.

## Κύρια ευρήματα
1. Ίση worst-case robust value δεν σημαίνει ίση απόδοση στα υπόλοιπα plausible models.
2. ORBE policy διατηρεί robust optimality και αποκλείει policies που είναι dominated σε όλο το uncertainty set.
3. Η επιλογή policy μέσα στο robust-optimal set είναι ξεχωριστή από την επιλογή ambiguity set.
4. Η μέθοδος δεν κάνει learning μετά από changepoint και δεν αποτελεί resilience mechanism.

## Υποθέσεις και ορισμοί
Η ανάλυση υποθέτει γνωστό s-rectangular uncertainty set και αξιολογεί όλες τις transition realizations μέσα σε αυτό. Best-effort εδώ είναι robust policy-selection notion, όχι «best effort recovery» μετά από αποτυχία.

## Περιορισμοί και απειλές εγκυρότητας
- πρόσφατη AAAI-26 εργασία,
- γνωστή robust-MDP formulation,
- δεν αντιμετωπίζει unknown out-of-set changes,
- δεν παρέχει detector/recovery metrics,
- πρόσθετο computational overhead έναντι standard robust value iteration.

## Σχέση με άλλες πηγές
Συμπληρώνει `SRC-52E62452B8` και `SRC-09DD20BA85` για conservativeness/nominal-utility trade-offs. Διαφέρει από `SRC-90A20ED43A`, όπου adaptation συμβαίνει μετά από structural shift.

## Χρήση στη διπλωματική
Υποστηρικτική πηγή για fairness και reporting robust baselines. Εάν robust baseline έχει πολλαπλές ισοδύναμες worst-case policies:
- δηλώνεται tie-breaking rule,
- αναφέρεται worst-case return,
- clean/nominal return,
- average/typical in-set return,
- conservativeness gap.

Δεν προστίθεται ORBE ως υποχρεωτικός agent· η ιδέα χρησιμοποιείται για ορθότερη επιλογή/αξιολόγηση robust policies.

## Απαιτούμενα αποσπάσματα
1. Πολλαπλές worst-case-optimal policies μπορούν να διαφέρουν εκτός του worst case.
2. Best-effort dominance προσφέρει principled tie-breaker χωρίς απώλεια robust optimality.
3. Worst-case score μόνο του δεν αρκεί για αξιολόγηση conservativeness.

## Κατάσταση επαλήθευσης
Επαληθεύτηκε στο πλήρες AAAI-26 paper. Επιλέγεται ως υποστηρικτική.