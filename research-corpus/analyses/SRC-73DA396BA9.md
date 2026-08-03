# SRC-73DA396BA9 — Online MDP with Transition Prototypes: A Robust Adaptive Approach

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Shuo Sun, Meng Qi, Zuo-Jun Max Shen
- **Έκδοση που αναλύθηκε:** arXiv:2412.14075v2, 19 Δεκεμβρίου 2024
- **Τύπος:** θεωρητική και αριθμητική εργασία για online robust MDPs
- **Ρόλος στη διπλωματική:** κύρια

## Ερευνητικό πρόβλημα

Η εργασία εξετάζει online MDP όπου ο αληθινός transition kernel δεν είναι γνωστός, αλλά θεωρείται ότι ανήκει σε ένα πεπερασμένο σύνολο γνωστών transition prototypes. Ο πράκτορας πρέπει ταυτόχρονα:

1. να λαμβάνει αποφάσεις με λίγα δεδομένα,
2. να προστατεύεται από λάθος επιλογή prototype,
3. να συλλέγει evidence για τον αληθινό kernel,
4. να συρρικνώνει προοδευτικά το ambiguity set.

Αυτό διαφέρει από κλασικό robust RL με σταθερό uncertainty ball: εδώ υπάρχει ένας αληθινός ονομαστικός kernel και η αβεβαιότητα μειώνεται online.

## Μέθοδος

Η RPO-AAS διατηρεί ενεργό σύνολο candidate prototypes και υπολογίζει robust policy ως προς όσα δεν έχουν ακόμη αποκλειστεί. Με νέα trajectories ενημερώνει τα empirical transition statistics και απομακρύνει prototypes που δεν είναι συμβατά με τα δεδομένα. Περιλαμβάνει early-stopping μηχανισμό όταν υπάρχει επαρκές evidence για μοναδικό candidate.

Η εργασία συγκρίνει επίσης μη robust επιλογή του πλησιέστερου empirical prototype. Η σύγκριση είναι χρήσιμη επειδή απομονώνει το κόστος και το όφελος της worst-case policy κατά την περίοδο αβεβαιότητας.

## Θεωρητικά και εμπειρικά αποτελέσματα

- Παρέχεται sublinear regret ως προς την optimal policy του αληθινού prototype υπό τις δηλωμένες assumptions.
- Παρέχεται episode-level lower bound για την απόδοση της robust policy.
- Το early stopping μπορεί να τερματίσει την robust φάση όταν το prototype ταυτοποιηθεί με αρκετή βεβαιότητα.
- Στα αριθμητικά πειράματα η robust adaptive μέθοδος εμφανίζει πλεονέκτημα κυρίως στα πρώτα επεισόδια, όπου τα δεδομένα είναι περιορισμένα.

## Συνάφεια με τη διπλωματική

Η εργασία αποτελεί άμεσο formal reference για context/model libraries όπου κάθε αποθηκευμένο regime περιέχει transition model. Υποστηρίζει ένα controlled comparator με:

- finite library γνωστών regimes,
- belief ή active candidate set,
- robust fallback όσο η ταυτοποίηση είναι αβέβαιη,
- μετάβαση σε regime-specific policy όταν η confidence περάσει threshold.

Για GridWorld μπορεί να υλοποιηθεί απλούστερη tabular εκδοχή χωρίς να αναπαραχθεί ο πλήρης RPO-AAS.

## Πειραματικές απαιτήσεις που προκύπτουν

- Αναφορά του πραγματικού αριθμού candidate prototypes.
- Καταγραφή χρόνου μέχρι μοναδική ταυτοποίηση.
- False elimination rate: πόσο συχνά απορρίπτεται το αληθινό regime.
- Ambiguity-set size ανά βήμα ή επεισόδιο.
- Σύγκριση robust candidate-set policy με hard nearest-prototype selection.
- Υποχρεωτικό stress test όπου ο αληθινός kernel απουσιάζει από τη library.
- Χωριστή μέτρηση early-stage utility και τελικής asymptotic utility.

## Περιορισμοί

- Προϋποθέτει πεπερασμένο, γνωστό σύνολο transition prototypes.
- Η αληθινή δυναμική θεωρείται ένα από τα prototypes· η out-of-library περίπτωση δεν καλύπτεται από το βασικό guarantee.
- Το μοντέλο είναι loop-free finite-horizon MDP και δεν μεταφέρεται αυτόματα σε κάθε continuing task.
- Πρόκειται για arXiv εργασία και όχι για τεκμήριο υπεροχής σε γενικά non-stationary RL benchmarks.
- Η μέθοδος αφορά identification υπό model ambiguity και όχι αυθαίρετα repeated changepoints χωρίς structural prior.

## Απόφαση

**Επιλογή ως κύρια πηγή.** Χρησιμοποιείται για model-library adaptation, active prototype elimination και robust-to-specialized switching. Δεν καθιστά υποχρεωτική την πλήρη υλοποίηση RPO-AAS.