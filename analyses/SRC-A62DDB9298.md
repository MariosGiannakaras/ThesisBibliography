---
κωδικός: SRC-A62DDB9298
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "ECE 517 final project report, 17 σελίδες, 2019"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Avoiding Catastrophic Forgetting in Safety Gridworld

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Carl Edwards, Brandon Mathis
- **Έτος:** 2019
- **Τύπος πηγής:** μη δημοσιευμένη φοιτητική τελική εργασία μαθήματος
- **DOI / arXiv / URL:** https://cnedwards.com/files/Final_Project_Report_Edwards_Mathis.pdf
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-A62DDB9298.pdf`

## Σκοπός και ερευνητικό ερώτημα

Το report εξετάζει αν DQN με Elastic Weight Consolidation μπορεί να μάθει διαδοχικά δύο custom AI Safety Gridworld-inspired tasks χωρίς να ξεχάσει το πρώτο.

## Σύνοψη

Οι συγγραφείς κατασκευάζουν μικρά 4×4 Lava World και Interrupt World environments, εκπαιδεύουν DQN και προσθέτουν EWC. Η κύρια sequential-learning προσπάθεια αποτυγχάνει να διατηρήσει το task A ενώ μαθαίνει το task B. Δοκιμές network capacity, Fisher batch size, learning rate, EWC weight και minimum Fisher values δεν δίνουν σταθερή λύση. Ένα naive multitask protocol, όπου τα δύο environments δειγματοληπτούνται μαζί, μαθαίνει και τα δύο σε πέντε trials.

Η εργασία είναι θεματικά σχετική με GridWorld, catastrophic forgetting και knowledge preservation, αλλά δεν παρέχει επαρκές peer-reviewed ή στατιστικά ισχυρό evidence για citation-ready χρήση. Η αξία της περιορίζεται σε implementation warning: ένα discrete path μπορεί να αποτυγχάνει από μία λανθασμένη action και η EWC/DQN επιλογή χρειάζεται ισχυρό feasibility pilot.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** custom 4×4×7 one-hot Safety Gridworld-inspired Lava World και Interrupt World.
- **Μοντέλα / αλγόριθμοι:** DQN, Adam, replay memory και EWC.
- **Baselines:** DQN χωρίς EWC και naive simultaneous two-task sampling.
- **Μετρικές:** episode return, learned path και binary retain/learn outcome.
- **Πειραματική διαδικασία:** sequential task A→B training, περιορισμένο hyperparameter investigation και πέντε trials μόνο για το naive multitask protocol.

## Κύρια ευρήματα

1. Η κύρια EWC sequential-learning προσπάθεια απέτυχε να διατηρήσει task A μετά τη μάθηση task B. Τεκμηρίωση: §§6.3–6.4, PDF σελ. 10–14.
2. Οι συγγραφείς εντοπίζουν zero entries στην empirical Fisher diagonal ως πιθανό μηχανισμό ανεπαρκούς προστασίας σημαντικών weights. Τεκμηρίωση: §6.3, PDF σελ. 11.
3. Αλλαγές capacity, batch size, learning rate και EWC hyperparameters δεν έδωσαν σταθερή επιτυχία στο περιορισμένο search. Τεκμηρίωση: §6.4, PDF σελ. 11–14.
4. Το naive multitask sampling έμαθε και τα δύο tasks σε πέντε trials, δείχνοντας ότι το network είχε επαρκή capacity υπό διαφορετικό data schedule. Τεκμηρίωση: §6.5, PDF σελ. 14–15.
5. Οι συγγραφείς χαρακτηρίζουν το project συνολικά ανεπιτυχές και αναφέρουν time constraints. Τεκμηρίωση: §7, PDF σελ. 15.

## Υποθέσεις και ορισμοί

Το catastrophic forgetting operationalized ως αποτυχία του learned path στο task A μετά από sequential training στο task B. Η αξιολόγηση είναι εξαιρετικά discrete: μία λανθασμένη action μπορεί να οδηγήσει σε lava και πλήρη episode failure.

## Περιορισμοί και απειλές εγκυρότητας

Δεν είναι peer-reviewed publication αλλά course project. Τα environments είναι custom και μικρά, οι περισσότερες hyperparameter combinations δοκιμάστηκαν μία φορά, δεν αναφέρονται confidence intervals ή standardized forgetting/transfer metrics και δεν υπάρχει σύγκριση με σύγχρονες continual-RL baselines. Η διατύπωση «GridWorld may not be well-suited for DQN» είναι inference από αποτυχημένη συγκεκριμένη υλοποίηση και δεν αποτελεί γενικό αποτέλεσμα. Το report επίσης συγχέει σε σημεία EWC feasibility με naive multitask success.

## Σχέση με άλλες πηγές

- Αντλεί περιβάλλοντα και motivation από την ισχυρότερη primary πηγή AI Safety Gridworlds.
- Η continual-learning θέση καλύπτεται πληρέστερα από το `SRC-F909CABDEB`.
- Η knowledge-preservation και sudden-change αξιολόγηση καλύπτεται αυστηρότερα από `SRC-B88D51FA3F` και `SRC-0F8A6588DC`.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** κανένα ως citation-ready evidence.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** μόνο εσωτερικό implementation warning ότι EWC+DQN σε one-hot discrete GridWorld μπορεί να είναι εύθραυστο και απαιτεί pilot.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι EWC γενικά αποτυγχάνει· ότι tabular methods είναι ανώτερα· ότι GridWorld είναι ακατάλληλο για deep RL· ότι τα αποτελέσματα έχουν γενικευσιμότητα.
- **Ρόλος:** απόρριψη

## Απαιτούμενα αποσπάσματα

Δεν δημιουργείται αρχείο citation-ready αποσπασμάτων επειδή η πηγή απορρίπτεται από το thesis export gate. Τα χρήσιμα implementation warnings παραμένουν στην παρούσα ανάλυση.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** κανένα· διατηρείται εκτός εξαγωγής.
