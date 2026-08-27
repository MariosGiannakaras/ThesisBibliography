---
κωδικός: SRC-4ED8B918E3
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "JMLR 25(318), 2024"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Empirical Design in Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Andrew Patterson, Samuel Neumann, Martha White, Adam White
- **Έτος:** 2024
- **Τύπος:** peer-reviewed μεθοδολογική εργασία για empirical reinforcement learning
- **Δημοσίευση:** Journal of Machine Learning Research 25(318):1–63

## Σκοπός και συνάφεια

Η εργασία εξετάζει πώς πρέπει να σχεδιάζονται και να ερμηνεύονται εμπειρικά πειράματα RL όταν οι αλγόριθμοι έχουν στοχαστικότητα, διαφορετικές learning dynamics, πολλαπλές υπερπαραμέτρους και σημαντικό experimenter discretion. Είναι άμεσα σχετική με το protocol-v2 επειδή η διπλωματική συγκρίνει διαφορετικές οικογένειες RL και όχι απλώς δύο deployment regimes του ίδιου learner.

## Κύρια σημεία που υποστηρίζονται άμεσα

1. **Η σύγκριση learning curves πρέπει να ελέγχει την πραγματική εμπειρία.** Η μέτρηση έναντι steps/interactions είναι καταλληλότερη από episode count όταν τα episode lengths μπορούν να διαφέρουν, επειδή διαφορετικός αριθμός episodes μπορεί να συνεπάγεται διαφορετικό αριθμό agent–environment samples.
2. **Η tuning opportunity πρέπει να είναι συγκρίσιμη.** Η εργασία επισημαίνει ότι ένας αλγόριθμος δεν πρέπει να λαμβάνει πολύ μεγαλύτερο hyperparameter-search opportunity από έναν άλλο. Ως ελάχιστο fairness criterion αναφέρει ίδιο αριθμό δοκιμαζόμενων hyperparameter settings· για optimizer-based tuning προτείνει κοινό iteration/steps/seeds budget.
3. **Τα random runs είναι μέρος του estimand.** Seeds/independent repetitions δεν είναι υπερπαράμετροι προς επιλογή και δεν δικαιολογείται best-seed reporting ως κύριο αποτέλεσμα.
4. **Οι συγκρίσεις πολλών agents χρειάζονται προσεκτικό design.** Baseline construction, hyperparameter bias, variation και statistical assumptions πρέπει να δηλώνονται πριν από ισχυρισμούς υπεροχής.
5. **Το experimental design δεν διορθώνεται εκ των υστέρων από καλύτερη στατιστική.** Unequal tuning, biased environment choice ή post-hoc selection παραμένουν design defects.

## Τι δεν αποδεικνύει

- Δεν καθορίζει ποιος RL algorithm πρέπει να κερδίσει στο GridWorld της διπλωματικής.
- Δεν επιβάλλει συγκεκριμένο αριθμό roots, layouts ή timesteps για το protocol-v2.
- Δεν αποδεικνύει ότι ένα συγκεκριμένο bootstrap/test είναι σωστό για κάθε hierarchy.
- Δεν μετατρέπει ίσο interaction budget σε ίσο wall-clock/compute cost· το compute πρέπει να αναφέρεται χωριστά.

## Εφαρμογή στο protocol-v2

Η πηγή στηρίζει το ακόλουθο bounded fairness contract:

- principal cross-method training currency: **agent–environment interactions/timesteps**;
- method-specific hyperparameters με συγκρίσιμο, προδηλωμένο search opportunity· όχι κοινές ψεύτικες υπερπαράμετροι;
- κοινά tuning-only partitions/roots και κοινός selection rule πριν από final access;
- standardized no-learning evaluation checkpoints για να μην συγχέεται exploratory training return με policy quality;
- independent roots ως randomization units και paired blocking όπου το κοινό environment randomness είναι έγκυρο;
- πλήρης διατήρηση poor/failed runs και όχι επιλογή του καλύτερου seed.

## Περιορισμοί / απειλές μεταφοράς

Η εργασία είναι γενική methodological guidance και περιλαμβάνει παραδείγματα πολύ ευρύτερα από ένα μικρό single-testbed GridWorld. Οι προτάσεις της για multiple-agent comparisons χρειάζονται προσαρμογή στην πραγματική hierarchy `root × layout × condition`, όχι μηχανική αντιγραφή benchmark-suite aggregates.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Μεθοδολογία, πειραματικός σχεδιασμός, tuning, στατιστική ανάλυση, threats to validity.
- **Ρόλος:** κύρια μεθοδολογική πηγή.
- **Ισχυρισμοί:** fair tuning opportunity, interaction-based comparison, independent randomness, bias-aware multi-agent design.
- **Μη ισχυρισμοί:** superiority συγκεκριμένου agent ή καθολικός αριθμός seeds/budget.
