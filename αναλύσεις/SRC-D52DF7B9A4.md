---
κωδικός: SRC-D52DF7B9A4
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Chapter 6 excerpt, Q-learning: Off-policy TD Control, pp. 131–135"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Q-learning: Off-policy TD Control

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Richard S. Sutton και Andrew G. Barto για το κεφάλαιο του εγχειριδίου· ο Q-learning αποδίδεται στον Christopher Watkins (1989)
- **Έτος:** 2018 για τη 2η έκδοση του εγχειριδίου / 1989 για την αρχική μέθοδο
- **Τύπος πηγής:** απόσπασμα ακαδημαϊκού εγχειριδίου, Chapter 6
- **DOI / arXiv / URL:** εκπαιδευτικό αντίγραφο κεφαλαίου στο Drake University
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-D52DF7B9A4.pdf`

## Σκοπός και ερευνητικό ερώτημα

Το απόσπασμα παρουσιάζει τον Q-learning ως off-policy temporal-difference control algorithm, τις βασικές συνθήκες σύγκλισης και τη διαφορά του από on-policy Sarsa. Το Cliff Walking παράδειγμα είναι ιδιαίτερα χρήσιμο για τη διπλωματική, επειδή δείχνει ότι η policy που είναι optimal ως προς το greedy target μπορεί να έχει χειρότερη online επίδοση όταν η behavior policy συνεχίζει να εξερευνά κοντά σε επικίνδυνες καταστάσεις.

Ο Q-learning είναι ισχυρός tabular baseline για controlled GridWorld. Δεν είναι εξ ορισμού resilient σε non-stationarity και η κλασική convergence guarantee αφορά stationary MDP με επαρκή visitation και κατάλληλα step sizes.

## Σύνοψη

Ο Q-learning ενημερώνει το state-action value προς το immediate reward συν το discounted maximum value της επόμενης κατάστασης. Επειδή ο target χρησιμοποιεί greedy next action ανεξάρτητα από την action που θα επιλεγεί πραγματικά, η μέθοδος είναι off-policy. Υπό συνεχή ενημέρωση όλων των state-action pairs και stochastic-approximation conditions, το Q προσεγγίζει το optimal action-value function σε stationary tabular setting.

Στο Cliff Walking, ο Q-learning μαθαίνει τη συντομότερη διαδρομή δίπλα στον γκρεμό, αλλά με ε-greedy behavior πέφτει περιστασιακά και έχει χειρότερο cumulative online reward από Sarsa. Η Sarsa μαθαίνει ασφαλέστερη μεγαλύτερη διαδρομή επειδή ο update target αντανακλά την exploratory behavior policy. Το κεφάλαιο παρουσιάζει επίσης maximization bias και Double Q-learning ως τρόπο αποσύνδεσης action selection από value estimation.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** tabular episodic GridWorld, Windy GridWorld exercises και Cliff Walking.
- **Μοντέλα / αλγόριθμοι:** Q-learning, Sarsa και Double Q-learning.
- **Baselines:** on-policy Sarsa έναντι off-policy Q-learning.
- **Μετρικές:** sum of rewards per episode, learned path και action-selection frequency στο maximization-bias example.
- **Πειραματική διαδικασία:** θεωρητική παρουσίαση updates και illustrative simulations.

## Κύρια ευρήματα

1. **Ο Q-learning είναι off-policy TD control.** Ο update target χρησιμοποιεί `max_a Q(S',a)` και προσεγγίζει optimal values ανεξάρτητα από την behavior policy, ενώ η behavior policy καθορίζει ποια pairs επισκέπτονται. Τεκμηρίωση: Section 6.5, pp. 131–132.
2. **Η σύγκλιση έχει συγκεκριμένες προϋποθέσεις.** Απαιτείται stationary tabular problem, συνεχιζόμενη ενημέρωση όλων των state-action pairs και κατάλληλη ακολουθία step sizes. Τεκμηρίωση: p. 131.
3. **Optimal target policy δεν συνεπάγεται καλύτερη online safety.** Στο Cliff Walking ο Q-learning μαθαίνει edge path αλλά η ε-greedy exploration προκαλεί πτώσεις· η Sarsa ενσωματώνει την behavior και μαθαίνει ασφαλέστερο path. Τεκμηρίωση: Example 6.6, pp. 132–134.
4. **Exploration schedule είναι μέρος του αποτελέσματος.** Αν το ε μειωθεί, η asymptotic behavior αλλάζει. Δίκαιη σύγκριση απαιτεί κοινό ή ρητά δικαιολογημένο exploration protocol. Τεκμηρίωση: Example 6.6.
5. **Το max operator δημιουργεί positive estimation bias σε noisy values.** Double learning χρησιμοποιεί ανεξάρτητες estimates για selection και evaluation και μειώνει τη μεροληψία. Τεκμηρίωση: Section 6.7 και Figure 6.5, p. 135.
6. **Η κλασική μέθοδος δεν ανιχνεύει environment changes.** Σε non-stationary GridWorld η learned Q-table μπορεί να γίνει παρωχημένη και απαιτεί continued updates, reset, forgetting ή explicit adaptation mechanism.

## Υποθέσεις και ορισμοί

Η state είναι πλήρως παρατηρήσιμη και το action set διακριτό. Ο tabular Q-learning αποθηκεύει value ανά state-action pair. Η behavior policy μπορεί να είναι ε-greedy, ενώ η target policy είναι greedy. Η κλασική convergence θεωρία δεν καλύπτει abrupt αλλαγές transition/reward κατά τη μάθηση.

Στη διπλωματική ο Q-learning πρέπει να αξιολογηθεί τουλάχιστον ως: fixed learned policy χωρίς update, συνεχώς ενημερούμενος baseline και πιθανώς baseline με reset/decay. Οι εκδοχές δεν πρέπει να συγχέονται.

## Περιορισμοί και απειλές εγκυρότητας

Το αρχείο είναι απόσπασμα κεφαλαίου και όχι η πλήρης πρωτογενής εργασία Watkins. Τα examples είναι μικρά και illustrative. Η σύγκλιση δεν μεταφέρεται σε function approximation ή non-stationary dynamics. Το Cliff Walking εξετάζει exploration risk, όχι unknown changepoint detection ή recovery. Reward και safety μπορεί να συμπίπτουν μόνο επειδή το cliff penalty έχει ενσωματωθεί στο reward.

## Σχέση με άλλες πηγές

Το `SRC-87C9BF9456` παρέχει γενικό MDP/model-uncertainty background. Το `SRC-FE2C0A3E00` χρησιμοποιεί Q-learning-related distinctions σε safety GridWorlds. Το `SRC-BE53B7970E` καλύπτει Double Q-learning σε deep setting. Το `SRC-95C9DAEE68` δείχνει γιατί stationary RL χρειάζεται detection/adaptation σε changing environments.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** RL background, baseline selection, GridWorld implementation, exploration protocol και threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** Q-learning είναι off-policy· stationary convergence έχει προϋποθέσεις· Sarsa/Q-learning μπορούν να διαφέρουν σε online risk· maximization bias δικαιολογεί Double Q baseline.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι Q-learning είναι resilient σε dynamic environments, ότι η ασφαλέστερη Sarsa συμπεριφορά είναι καθολική ή ότι convergence ισχύει μετά από repeated changes.
- **Ρόλος:** κύρια

## Απαιτούμενα αποσπάσματα

Καταγράφηκαν τεκμήρια για update/convergence, Cliff Walking, exploration dependence και maximization bias.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** να επιβεβαιωθεί στο κύριο repo αν θα συγκριθούν Q-learning, Sarsa και Double Q-learning ή μόνο δύο από αυτά.