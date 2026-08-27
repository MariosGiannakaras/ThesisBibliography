---
κωδικός: SRC-46CF36BC1E
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PMLR 162, ICML 2022 official article page/abstract"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# The Primacy Bias in Deep Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Evgenii Nikishin, Max Schwarzer, Pierluca D'Oro, Pierre-Luc Bacon, Aaron Courville
- **Έτος:** 2022
- **Τύπος:** peer-reviewed πρωτογενής εμπειρική εργασία deep RL
- **Δημοσίευση:** Proceedings of the 39th International Conference on Machine Learning, PMLR 162:16828–16847

## Σκοπός και συνάφεια

Η εργασία μελετά το `primacy bias`: την τάση deep-RL learners να βασίζονται δυσανάλογα σε πρώιμες interactions και να αξιοποιούν ανεπαρκώς χρήσιμη μεταγενέστερη εμπειρία. Αυτό είναι σχετικό με το protocol-v2 επειδή το Adaptive branch ζητά από έναν ήδη εκπαιδευμένο DQN/PPO learner να συνεχίσει ordinary method-native learning μετά από environmental change. Η πηγή υποστηρίζει ότι η αδυναμία προσαρμογής μπορεί να προέρχεται και από learning-history effects, όχι μόνο από το ίδιο το disturbance.

## Κύρια σημεία που υποστηρίζονται άμεσα

1. **Early experience μπορεί να έχει μακροχρόνια επιρροή.** Οι συγγραφείς περιγράφουν deep-RL agents που τείνουν να βασίζονται στις πρώτες interactions και να αγνοούν μεταγενέστερα χρήσιμα στοιχεία.
2. **Το φαινόμενο μπορεί να επηρεάζει τη μετέπειτα μάθηση.** Η progressively growing training experience μπορεί να οδηγήσει σε overfitting προς παλαιότερη εμπειρία και να βλάψει την υπόλοιπη learning process.
3. **Reset είναι intervention, όχι neutral continuation.** Η εργασία προτείνει περιοδικό partial reset ως μηχανισμό αντιμετώπισης και αναφέρει βελτιώσεις σε discrete και continuous-action experiments.

## Εφαρμογή στο protocol-v2

Η πηγή χρησιμοποιείται κυρίως ως threat/interpretation evidence:

- ordinary post-change continuation δεν θεωρείται εγγυημένα πλαστική ή αποτελεσματική·
- poor Adaptive DQN/PPO recovery δεν ερμηνεύεται αυτομάτως ως απόδειξη ότι «ο algorithm δεν μπορεί να προσαρμοστεί» γενικά·
- η πλήρης pre-change learning state διατηρείται ώστε το experiment να μετρά πραγματική συνέχεια του ίδιου learner;
- partial reset, optimizer reset, replay reset ή plasticity intervention **δεν** ενσωματώνεται στο default Adaptive branch.

Αν reset/plasticity mitigation εξεταστεί μελλοντικά, αποτελεί νέο predeclared experimental arm/RQ και όχι implementation fix μετά την παρατήρηση αποτελεσμάτων.

## Περιορισμοί

Η εργασία δεν μελετά το συγκεκριμένο thesis GridWorld/action remapping και δεν προβλέπει ότι DQN ή PPO θα εμφανίσουν primacy bias στο δικό μας bounded horizon. Η προτεινόμενη reset intervention δεν τεκμηριώνει ότι reset είναι η κατάλληλη λύση εδώ. Η πηγή υποστηρίζει πιθανό threat και μηχανιστική ερμηνεία, όχι προγνωστική κατάταξη.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Continual/adaptive learning background, Discussion, threats to validity.
- **Ρόλος:** υποστηρικτική μεθοδολογική/interpretation πηγή.
- **Ισχυρισμοί:** primacy bias as a possible deep-RL learning-history limitation; resets are substantive interventions.
- **Μη ισχυρισμοί:** ότι primacy bias θα εμφανιστεί υποχρεωτικά στο thesis experiment ή ότι reset πρέπει να εφαρμοστεί.
