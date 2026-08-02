---
κωδικός: SRC-3EA1176D3A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2410.06212v1, preprint 12 σελίδων"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Solving robust MDPs as a sequence of static RL problems

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Adil Zouitine, Matthieu Geist, Emmanuel Rachelson
- **Έτος:** 2024
- **Τύπος πηγής:** ερευνητικό preprint για robust MDPs
- **DOI / arXiv / URL:** arXiv:2410.06212
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-3EA1176D3A.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει αν ένα robust MDP μπορεί να λυθεί χωρίς να αντιμετωπίζεται αποκλειστικά ως συνεχές minimax παιχνίδι ανάμεσα σε policy και adversary. Εστιάζει στη διαφορά ανάμεσα στο dynamic uncertainty model, όπου η transition function μπορεί να αλλάζει σε κάθε timestep, και στο static model, όπου ένα transition model παραμένει σταθερό σε ολόκληρη την τροχιά. Προτείνει το IWOCS, μια διαδικασία που εντοπίζει σταδιακά δυσμενή static models και χρησιμοποιεί κλασικά RL subproblems για να robustify την policy.

Η πηγή είναι κεντρική για την ορολογία της διπλωματικής: διατυπώνει ρητά ότι robustness είναι η διατήρηση εγγυημένης επίδοσης χωρίς περαιτέρω εκπαίδευση, ενώ resilience είναι η ανάκαμψη μέσω συνεχιζόμενης μάθησης μετά από περιβαλλοντική αλλαγή. Αυτή η διάκριση επιβάλλει χωριστές κατηγορίες agents και metrics.

## Σύνοψη

Οι συγγραφείς επανεξετάζουν robust MDPs με uncertainty set πάνω στις transition functions. Υπό stationary policies και rectangular uncertainty sets, το dynamic και το static formulation μπορούν να συνδεθούν. Με πρόσθετη no-duality-gap συνθήκη, η αναζήτηση robust policy μπορεί να προσεγγιστεί ως ακολουθία static problems.

Το IWOCS ξεκινά με ένα transition model, λύνει το αντίστοιχο nominal MDP, κατασκευάζει pessimistic Q-function ως ελάχιστο πάνω στα ήδη ανακαλυφθέντα models και εντοπίζει το επόμενο worst-case model για την τρέχουσα candidate policy. Η διαδικασία επαναλαμβάνεται μέχρι η εκτιμώμενη worst-case value να συμφωνεί εντός tolerance με την pessimistic value. Παρουσιάζεται toy Windy Walk GridWorld και deep-RL εκδοχή σε continuous-control benchmarks.

Για τη διπλωματική, η μέθοδος δεν είναι απαραίτητα υποψήφιος τελικός agent λόγω πολυπλοκότητας. Είναι όμως πολύτιμη ως θεωρητική βάση για robust-oracle baseline, για τη διάκριση static έναντι within-episode αλλαγών και για την αποφυγή λανθασμένης χρήσης του όρου resilience για policies που δεν μαθαίνουν μετά τη μεταβολή.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** toy Windy Walk GridWorld με τρεις διαδρομές και transition uncertainty, καθώς και κλασικά continuous-control robust-RL benchmarks.
- **Μοντέλα / αλγόριθμοι:** robust value iteration, generic IWOCS, value iteration στο toy problem και deep IWOCS με off-policy policy optimisation.
- **Baselines:** robust value iteration και state-of-the-art deep robust-RL methods στο αντίστοιχο benchmark.
- **Μετρικές:** worst-case discounted return, απόσταση από robust value, αριθμός IWOCS iterations και benchmark return υπό διαφορετικά transition models.
- **Πειραματική διαδικασία:** επαναληπτική επέκταση πεπερασμένου uncertainty set. Σε κάθε iteration λύνεται νέο static MDP και αναζητείται transition model που ελαχιστοποιεί την επίδοση της candidate policy.

## Κύρια ευρήματα

1. **Robustness και resilience δεν είναι συνώνυμα.** Robust policy διατηρεί επίδοση χωρίς further training, ενώ resilient agent ανακάμπτει μέσω continued learning. Τεκμηρίωση: Ενότητα 1, πρώτη παράγραφος.
2. **Το static και το dynamic uncertainty model απαντούν διαφορετικά πρακτικά ερωτήματα.** Το dynamic model επιτρέπει αλλαγή transition function ανά βήμα, ενώ το static model κρατά ένα model σε ολόκληρη την τροχιά. Τεκμηρίωση: Ενότητα 2, υποενότητες “Robust MDPs” και “The static model”.
3. **Worst-case robustness μπορεί να είναι υπερβολικά συντηρητική.** Μεγάλα rectangular uncertainty sets επιτρέπουν adversarial συνδυασμούς που μπορεί να μην αντιστοιχούν σε ρεαλιστικές συνεκτικές μεταβολές. Τεκμηρίωση: Ενότητα 2, “Robust Value Iteration”.
4. **Το IWOCS διαχωρίζει policy optimisation από την αναζήτηση adversarial transition model.** Αυτό επιτρέπει αξιοποίηση standard RL solvers σε ακολουθία static προβλημάτων. Τεκμηρίωση: Ενότητα 4 και Algorithm 1.
5. **Η σύγκλιση της pessimistic sequence δεν εγγυάται κατ’ ανάγκη σύγκλιση στο ακριβές robust optimum.** Η επιλογή του επόμενου model είναι heuristic και premature stopping παραμένει πιθανό. Τεκμηρίωση: Ενότητα 4, “Choosing T_{i+1}”.
6. **Ένα μικρό GridWorld μπορεί να απομονώσει transition uncertainty και να επαληθεύσει τον μηχανισμό.** Στο Windy Walk, η πιθανότητα οπισθοδρόμησης ελέγχεται από μία παράμετρο και επιτρέπει άμεση σύγκριση IWOCS με robust value iteration. Τεκμηρίωση: Ενότητα 4, “Illustration”, Σχήμα 1.

## Υποθέσεις και ορισμοί

Η βασική robust objective είναι max-policy/min-transition-model worst-case return πάνω σε uncertainty set. Η equivalence που χρησιμοποιείται αφορά stationary policies και rectangular sets· δεν ισχύει χωρίς προϋποθέσεις για κάθε static problem. Η no-duality-gap ιδιότητα αποτελεί επίσης ουσιαστική συνθήκη της ανάλυσης.

Στο δικό μας πείραμα πρέπει να ξεχωρίσουμε: (α) fixed-but-unknown environment per episode, (β) abrupt change ανάμεσα σε φάσεις ή επεισόδια και (γ) within-episode non-stationarity. Ένας robust baseline μπορεί να εκπαιδευτεί σε γνωστό uncertainty set και να αξιολογηθεί χωρίς online update. Ένας resilient/adaptive agent πρέπει να συνεχίζει να ενημερώνεται και να μετράται η πορεία ανάκαμψης.

## Περιορισμοί και απειλές εγκυρότητας

Η εργασία είναι preprint 12 σελίδων και η δημοσιευτική της κατάσταση δεν πρέπει να παρουσιαστεί ως peer-reviewed acceptance. Η θεωρία βασίζεται σε stationary policies, rectangularity και saddle-point/no-duality assumptions. Η αναζήτηση worst-case transition model μπορεί να είναι δύσκολη και heuristic. Η monotonically decreasing sequence των approximate robust values έχει κάτω φράγμα αλλά δεν εγγυάται από μόνη της convergence στο exact robust optimum. Το toy GridWorld αποδεικνύει λειτουργία σε ελεγχόμενο παράδειγμα, όχι scalability ή sample efficiency σε κάθε domain. Τέλος, το framework αξιολογεί κυρίως pre-trained robustness και όχι online recovery.

## Σχέση με άλλες πηγές

Το `SRC-81A15E6905` ορίζει action-level robust MDPs. Το `SRC-A3D907D882` παρέχει ευρύτερη perturbation taxonomy. Το `SRC-95C9DAEE68` καλύπτει detection και continued adaptation, δηλαδή την πλευρά της resilience. Το `SRC-0882A9B2B0` διαχωρίζει interpolation και extrapolation evaluation.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** ορισμοί, robust MDPs, σχετικές εργασίες, κατηγορίες agents, πειραματικά scenarios.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** robustness χωρίς further training διαφέρει από resilience μέσω continued learning· static και dynamic uncertainty πρέπει να δηλώνονται χωριστά· worst-case baselines μπορεί να είναι συντηρητικά.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι IWOCS έχει αποδεδειγμένα exact convergence σε όλες τις περιπτώσεις, ότι είναι ο βέλτιστος agent για τη διπλωματική ή ότι static robustness ισοδυναμεί με ταχεία recovery.
- **Ρόλος:** κύρια

## Απαιτούμενα αποσπάσματα

Απαιτούνται τεκμήρια για τη robustness–resilience διάκριση, το static/dynamic model και τη χρήση του Windy Walk ως minimal transition-uncertainty testbed.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** η πηγή θα αναφέρεται ως arXiv preprint· η καταλληλότητα IWOCS ως υλοποιήσιμου baseline θα αποφασιστεί μόνο μετά από complexity assessment.
