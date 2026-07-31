---
κωδικός: SRC-09DD20BA85
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2209.15320v2, 11 December 2023"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Bounded Robustness in Reinforcement Learning via Lexicographic Objectives

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Daniel Jarne Ornia, Licio Romao, Lewis Hammond, Manuel Mazo Jr., Alessandro Abate
- **Έτος:** 2023 (v2· αρχική υποβολή 2022)
- **Τύπος πηγής:** πρωτογενής θεωρητική και πειραματική εργασία
- **DOI / arXiv / URL:** arXiv:2209.15320
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-09DD20BA85.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία μελετά robustness απέναντι σε άγνωστο θόρυβο παρατήρησης. Το βασικό ερώτημα είναι πώς μπορεί μια policy να γίνει λιγότερο ευαίσθητη σε λανθασμένες state measurements χωρίς να θυσιάζεται ανεξέλεγκτα η απόδοσή της στο καθαρό περιβάλλον. Οι συγγραφείς επιδιώκουν ρητό, ποσοτικοποιήσιμο και θεωρητικά ελεγχόμενο utility–robustness trade-off αντί για αδιαφανή regularization.

Η πηγή συνδέεται άμεσα με τον όρο «θόρυβος δεδομένων» της επίσημης αίτησης. Προσφέρει έναν συγκεκριμένο τρόπο να οριστεί το observation noise: η πραγματική κατάσταση είναι x, αλλά ο agent παρατηρεί y σύμφωνα με stochastic kernel T(y|x). Αυτό διαφέρει από transition noise και action-execution failure, άρα πρέπει να αποτελεί χωριστή οικογένεια perturbation στο πειραματικό πρωτόκολλο.

## Σύνοψη

Οι συγγραφείς ορίζουν το observationally-disturbed MDP (DOMDP), μια POMDP-like κατασκευή όπου η δυναμική του περιβάλλοντος παραμένει ίδια, αλλά η policy λαμβάνει διαταραγμένη state observation. Ο noise kernel T μετασχηματίζει την αρχική policy σε disturbed policy. Ως robustness regret ορίζεται η διαφορά μεταξύ expected return της policy χωρίς θόρυβο και expected return της policy όταν οι αποφάσεις λαμβάνονται πάνω στις διαταραγμένες παρατηρήσεις.

Η θεωρητική ανάλυση χαρακτηρίζει σύνολα policies που είναι fixed points ή παρουσιάζουν μηδενικό noise disadvantage. Στη συνέχεια προτείνεται το Lexicographically Robust Policy Gradient (LRPG), meta-algorithm που θέτει ως κύριο objective την expected utility και ως δευτερεύον objective τη robustness. Μια ανοχή ε καθορίζει πόσο μπορεί να υποχωρήσει η primary utility ώστε να αυξηθεί η robustness.

Η εμπειρική αξιολόγηση εφαρμόζει LR-PPO και LR-A2C σε MiniGrid LavaGap, LavaCrossing και DynamicObstacles, με uniform, Gaussian και adversarial observation disturbances. Οι μέθοδοι συγκρίνονται με vanilla algorithms και SA-PPO. Τα αποτελέσματα υποστηρίζουν ότι η lexicographic regularization μπορεί να μειώσει το robustness regret, αλλά η αποτελεσματικότητα εξαρτάται από base algorithm, robustness objective και noise regime.

## Μεθοδολογία

- **Μοντέλο αβεβαιότητας:** DOMDP με stochastic observation kernel T(y|x), που αλλάζει μόνο την πληροφορία που εισέρχεται στην policy.
- **Κύρια μετρική:** robustness regret ρ(π,T)=J(π)−J(⟨π,T⟩), δηλαδή απώλεια utility λόγω θορύβου παρατήρησης.
- **Optimization:** lexicographic multi-objective update, με primary expected-return objective και secondary robustness objective.
- **Design parameter:** ανοχή ε που περιορίζει την επιτρεπόμενη απόκλιση από την optimal utility.
- **Algorithms:** LR-PPO και LR-A2C, καθώς και objective βασισμένο σε noise disadvantage όταν υπάρχει critic.
- **Περιβάλλοντα:** MiniGrid LavaGap, LavaCrossing και DynamicObstacles· discrete actions, safety-sensitive navigation, πλήρης ή μερική παρατηρησιμότητα.
- **Baselines:** PPO, A2C και SA-PPO.
- **Evaluation:** 10 independently trained agents ανά algorithm, median agent, 50 roll-outs, noiseless, uniform, Gaussian και bounded adversarial observation disturbances.

## Κύρια ευρήματα

1. **Ο observation noise χρειάζεται ξεχωριστό formal model.** Στο DOMDP, η πραγματική κατάσταση x δεν αλλάζει, αλλά η policy ενεργεί πάνω σε observation y που παράγεται από T(y|x). Αυτό απομονώνει sensor/data corruption από transition stochasticity. Τεκμηρίωση: σελίδες 2–4, Definition 1 και Section 2.
2. **Η robustness μπορεί να μετρηθεί ως utility loss υπό disturbance.** Το robustness regret συγκρίνει την αναμενόμενη απόδοση της ίδιας policy πριν και μετά τον observation-kernel transformation. Τεκμηρίωση: σελίδες 3–4, Definition 2.
3. **Η απόλυτη robustness δεν πρέπει να επιδιώκεται χωρίς κόστος.** Policies που είναι αμετάβλητες σε κάθε observation μπορεί να γίνουν σχεδόν state-independent και να χάσουν χρήσιμη εξειδίκευση. Η ανοχή ε επιτρέπει ελεγχόμενη θυσία utility, όχι απεριόριστη regularization. Τεκμηρίωση: Abstract, Introduction και Sections 2–4.
4. **Το utility–robustness trade-off μπορεί να οριστεί ως lexicographic constraint.** Το LRPG αναζητά την πιο robust policy μέσα στο σύνολο των ε-optimal policies. Έτσι το primary task objective παραμένει ιεραρχικά ανώτερο. Τεκμηρίωση: σελίδες 3 και 6–8, Problem 1 και Theorem 6.
5. **Η robustness training πρέπει να δοκιμάζεται σε περισσότερα noise kernels από εκείνο της εκπαίδευσης.** Τα experiments αξιολογούν noiseless, uniform, Gaussian και adversarial disturbances, ώστε να διαχωριστεί memorization ενός noise pattern από broader invariance. Τεκμηρίωση: σελίδες 8–10 και Appendix C.
6. **Η βελτίωση δεν είναι καθολική ούτε ανεξάρτητη του base algorithm.** LRPG μειώνει robustness regret στα εξεταζόμενα tasks και διατηρεί guarantees υπό assumptions, αλλά A2C και PPO παρουσιάζουν διαφορετική ευαισθησία, ενώ SA-PPO είναι συχνά ισχυρότερο ειδικά στο adversarial regime για το οποίο εκπαιδεύτηκε. Τεκμηρίωση: σελίδες 9–10, Table 1, Discussion και Appendix C.

## Υποθέσεις και ορισμοί

Η πηγή υποθέτει finite state representation για το DOMDP και, για βασικά θεωρητικά αποτελέσματα, ergodicity/visitation και convergence properties του underlying policy-gradient algorithm. Η observational robustness αφορά την policy response σε corrupted observation, όχι αλλαγή στο transition kernel ή στο reward function.

Για το GridWorld της διπλωματικής μπορούν να οριστούν διαφορετικοί observation kernels:

- **location corruption:** με πιθανότητα p εμφανίζεται γειτονικό ή λάθος cell,
- **feature dropout:** αποκρύπτεται προσωρινά obstacle, hazard ή goal indicator,
- **symbol swap:** δύο observation labels ανταλλάσσονται,
- **bounded local corruption:** η παρατήρηση μετακινείται μόνο μέσα σε προκαθορισμένη ακτίνα.

Κάθε kernel πρέπει να έχει σαφή severity parameter, να εφαρμόζεται χωρίς να αλλάζει την πραγματική state transition και να αξιολογείται χωριστά από action failure.

## Περιορισμοί και απειλές εγκυρότητας

Η θεωρία εξαρτάται από assumptions όπως ergodicity και convergence του base policy-gradient method. Το design kernel που χρησιμοποιείται στην εκπαίδευση δεν ταυτίζεται αναγκαστικά με τον πραγματικό άγνωστο noise kernel. Η επιλεγμένη ανοχή ε επηρεάζει ουσιαστικά το αποτέλεσμα και δεν υπάρχει μία καθολική τιμή. Τα MiniGrid experiments είναι safety-sensitive αλλά περιορισμένα, ενώ το reported median-agent protocol δεν είναι τόσο πλήρες όσο η σύγχρονη aggregate evaluation με stratified bootstrap και performance profiles.

Η μέθοδος αφορά policy-gradient agents και δεν μεταφέρεται αυτούσια σε tabular Q-learning. Ωστόσο, το DOMDP και το robustness regret μπορούν να χρησιμοποιηθούν ανεξάρτητα από LRPG ως ορισμοί perturbation και metric. Επίσης, observation noise σε partially observable task μπορεί να αλληλεπιδρά με memory/history, οπότε απαιτείται προσοχή ώστε να μη συγκριθούν άνισα memoryless και recurrent agents.

## Σχέση με άλλες πηγές

Το `SRC-81A15E6905` αφορά action perturbations, ενώ η παρούσα πηγή αφορά observation corruption. Το `SRC-0882A9B2B0` οργανώνει in-distribution και out-of-distribution evaluation, που μπορεί να εφαρμοστεί σε unseen noise severities. Το `SRC-0A4AFAC8E9` παρέχει καταλληλότερο aggregate protocol από την επιλογή ενός median agent. Το `SRC-FE2C0A3E00` δείχνει ότι ένα minimal GridWorld επιτρέπει ελεγχόμενες, ερμηνεύσιμες perturbations.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** μοντέλο αβεβαιότητας, robust RL, experimental scenarios, metrics και threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** observation noise είναι διαφορετικό από action/transition noise· robustness πρέπει να αναφέρεται μαζί με nominal utility cost· unseen noise kernels/severities είναι χρήσιμη δοκιμή.
- **Πειραματική συνέπεια:** να υπάρχει καθαρό baseline, πολλαπλά observation-noise severities και μέτρηση τόσο του stressed return όσο και της διαφοράς από την clean performance. Για adaptive agents να καταγράφεται και recovery μετά την ενεργοποίηση ή αλλαγή του noise regime.
- **Τι δεν πρέπει να ισχυριστούμε:** ότι LRPG είναι αναγκαίο μοντέλο της διπλωματικής, ότι κάθε data noise ισοδυναμεί με state misobservation ή ότι θεωρητικές guarantees ισχύουν για οποιοδήποτε neural implementation.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη.
- **Έλεγχος πρωτοτύπου:** ελέγχθηκε το arXiv v2 PDF, με έμφαση σε Abstract, Sections 1–4, Definition 1–2, Theorem 6, Sections 6–7, Table 1 και Appendix C.
- **Απόφαση:** κύρια πηγή για το επίσημο σενάριο «θόρυβος δεδομένων», τον σαφή διαχωρισμό observational uncertainty και το bounded utility–robustness trade-off.
