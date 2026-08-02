---
κωδικός: SRC-09DD20BA85
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "L4DC 2024 / PMLR 242:954–967 και arXiv:2209.15320v2"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Bounded Robustness in Reinforcement Learning via Lexicographic Objectives

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Daniel Jarne Ornia, Licio Romao, Lewis Hammond, Manuel Mazo Jr., Alessandro Abate
- **Έτος:** 2024
- **Τύπος πηγής:** peer-reviewed conference paper, Learning for Dynamics and Control, PMLR 242
- **DOI / arXiv / URL:** PMLR 242:954–967 · arXiv:2209.15320
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-09DD20BA85.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία μελετά πώς μπορεί να αυξηθεί η ανθεκτικότητα μιας RL policy σε άγνωστο observational noise χωρίς η robustification να θυσιάζει απεριόριστα την nominal utility ή να καταστρέφει τις θεωρητικές εγγυήσεις του βασικού policy-gradient algorithm. Το κεντρικό ερώτημα δεν είναι απλώς “πόσο robust είναι η policy;”, αλλά “πόση απόκλιση από τη nominal βέλτιστη επίδοση επιτρέπουμε ώστε να αυξηθεί η robustness;”.

Η πηγή καλύπτει άμεσα το “data noise” της επίσημης αίτησης, όταν αυτό ερμηνεύεται ως αλλοίωση της state observation. Παρέχει επίσης πολύτιμη αρχή αξιολόγησης: robustness δεν πρέπει να βελτιστοποιείται χωρίς αναφορά στο clean-performance cost. Δεν καλύπτει reward noise, action failure ή changing transition rules και δεν αποτελεί online recovery method.

## Σύνοψη

Οι συγγραφείς ορίζουν observationally disturbed MDP, στο οποίο ένας άγνωστος stochastic kernel μετασχηματίζει την πραγματική κατάσταση σε πιθανώς λανθασμένη παρατήρηση πριν εφαρμοστεί η policy. Η disturbance μπορεί να ιδωθεί ως averaging operator πάνω στην policy. Ορίζεται robustness regret που συγκρίνει την utility της αρχικής και της noise-altered policy και χαρακτηρίζονται maximally robust policies μέσω fixed-point και invariance ιδιοτήτων.

Στη συνέχεια προτείνεται Lexicographically Robust Policy Gradient (LRPG). Η nominal expected return παραμένει objective πρώτης προτεραιότητας μέχρι επιτρεπτή tolerance, και μόνο μέσα στο αποδεκτό σύνολο policies βελτιστοποιείται δεύτερο robustness objective. Έτσι η tolerance εκφράζει ρητά το utility–robustness trade-off. Η μέθοδος λειτουργεί ως meta-algorithm πάνω σε policy-gradient methods όπως PPO και A2C.

Τα πειράματα χρησιμοποιούν MiniGrid environments και διάφορα noise kernels. Τα LRPG variants εμφανίζουν βελτιωμένη ανθεκτικότητα σε αρκετές perturbations, ιδίως όπου μία λανθασμένη action επιλογή μπορεί να οδηγήσει σε terminal failure. Ωστόσο τα αποτελέσματα δεν δείχνουν καθολική κυριαρχία και ο ίδιος ο paper αναγνωρίζει ότι model-based filtering ή disturbance estimation μπορεί να είναι αποτελεσματικότερα όταν είναι διαθέσιμα.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** MiniGrid LavaGap, LavaCrossing και DynamicObstacles· η εκτεταμένη έκδοση περιλαμβάνει και continuous-control tasks.
- **Μοντέλα / αλγόριθμοι:** LRPG ως meta-algorithm πάνω σε PPO και A2C, με εναλλακτικά robustness proxy objectives.
- **Baselines:** PPO, A2C και SA-PPO ως observational-robust baseline.
- **Μετρικές:** expected reward σε clean και disturbed rollouts, robustness regret και nominal-utility tolerance.
- **Πειραματική διαδικασία:** 10 ανεξάρτητοι agents ανά algorithm· αναφορά του median agent σε 50 rollouts· testing σε clean, bounded uniform, Gaussian και state-adversarial noise configurations.

## Κύρια ευρήματα

1. **Observational noise μετατρέπει την πραγματική policy σε διαφορετική effective policy.** Η policy δρα πάνω σε πιθανώς λανθασμένη κατάσταση, άρα η robustness μπορεί να μετρηθεί ως απόκλιση utility μεταξύ nominal και disturbed εκτέλεσης. Τεκμηρίωση: Ενότητα 2, Definitions 2.1–2.2.
2. **Η robustness έχει κόστος και πρέπει να είναι bounded.** Η επιτρεπτή απόκλιση από την nominal optimum κωδικοποιείται ως tolerance πρώτου lexicographic objective. Τεκμηρίωση: Εισαγωγή, Problem 2.3 και Ενότητα 4.
3. **Μπορούν να χαρακτηριστούν policy invariances ως προς noise kernels.** Fixed points του disturbance operator αποτελούν υποσύνολο maximally robust policies, αλλά η χρησιμότητα αυτών των sets εξαρτάται από το MDP και τη reward structure. Τεκμηρίωση: Ενότητα 3, Proposition 3.1 και Theorem 3.3.
4. **Το LRPG μπορεί να προστεθεί σε policy-gradient algorithm χωρίς να αγνοείται η nominal objective.** Υπό τις δηλωμένες assumptions, η lexicographic διαδικασία διατηρεί convergence/sub-optimality guarantees του underlying method μέσα σε tolerance. Τεκμηρίωση: Ενότητα 4.1, Theorem 4.1.
5. **Η choice του training noise generator έχει σημασία, αλλά δεν απαιτεί γνώση του ακριβούς deployment kernel.** Uniform ή Gaussian design kernels με κατάλληλες reachability ιδιότητες μπορούν να κατευθύνουν την policy προς invariant sets. Τεκμηρίωση: Ενότητα 5, Corollary 5.1.
6. **Τα MiniGrid αποτελέσματα δείχνουν trade-off, όχι καθολική υπεροχή.** LRPG συχνά διατηρεί καλύτερη disturbed performance, ενώ η clean utility και η αποτελεσματικότητα αλλάζουν ανά task, base algorithm και noise. Τεκμηρίωση: Ενότητα 6, Table 1 και Ενότητα 7.

## Υποθέσεις και ορισμοί

Το DOMDP θεωρεί finite state/action spaces στην κύρια θεωρητική διατύπωση και unknown stochastic observation kernel που δρα μόνο πάνω στην state observation. Οι policies είναι memoryless stochastic kernels. Η εργασία υποθέτει ergodicity/άπειρες επισκέψεις καταστάσεων για κρίσιμα αποτελέσματα και convergence του underlying policy-gradient method. Η tolerance της lexicographic objective είναι σχεδιαστική παράμετρος και όχι εμπειρικά δεδομένη σταθερά.

Στο δικό μας GridWorld, observation noise μπορεί να υλοποιηθεί ως state corruption kernel με ελεγχόμενο confusion pattern. Η nominal utility loss και η disturbed utility πρέπει να αναφέρονται μαζί. Αν χρησιμοποιηθεί partial observability, πρέπει να διαχωριστεί από corruption: το πρώτο αφαιρεί πληροφορία δομικά, ενώ το δεύτερο αλλοιώνει διαθέσιμη πληροφορία στο deployment.

## Περιορισμοί και απειλές εγκυρότητας

Η θεωρία αφορά observational disturbances και δεν γενικεύεται απευθείας σε reward corruption, failed actions ή transition changes. Οι memoryless policies και ergodicity assumptions μπορεί να μην ισχύουν σε κάθε episodic GridWorld. Η robustness proxy βασίζεται σε invariance προς design kernel, όχι σε estimation του πραγματικού noise process. Η πειραματική αναφορά median agent από 10 trainings και 50 rollouts δεν αντικαθιστά πλήρη aggregate uncertainty analysis όλων των runs. Τα tasks είναι μικρά και safety-sensitive, με sparse rewards, επομένως η σχετική επίδοση μπορεί να αλλάξει σε διαφορετική reward structure. Ο paper επίσης αναγνωρίζει ότι model-based filtering ή explicit disturbance rejection μπορεί να υπερέχει όταν υπάρχει αξιόπιστο noise model.

## Σχέση με άλλες πηγές

Το `SRC-A3D907D882` εντάσσει το observation noise σε γενική taxonomy state/reward/action/environment disruption. Το `SRC-FE2C0A3E00` δείχνει γιατί hidden performance indicators είναι απαραίτητοι σε safety GridWorlds. Το `SRC-0A4AFAC8E9` απαιτεί aggregate reporting όλων των runs αντί επιλογής representative seed. Το `SRC-3EA1176D3A` διαχωρίζει robustness χωρίς update από resilience μέσω continued learning.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** uncertainty model, observation noise, robust baselines, metrics και trade-offs.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** robustness σε observational noise πρέπει να αξιολογείται μαζί με nominal utility· state corruption μπορεί να μοντελοποιηθεί ως stochastic kernel· η robustification χρειάζεται ρητή tolerance ή Pareto/lexicographic αναφορά.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι LRPG αντιμετωπίζει changing rules ή action failures, ότι εγγυάται online recovery ή ότι τα MiniGrid αποτελέσματα αποδεικνύουν καθολική υπεροχή.
- **Ρόλος:** κύρια

## Απαιτούμενα αποσπάσματα

Απαιτούνται τεκμήρια για το DOMDP, τη bounded utility–robustness trade-off και τους πειραματικούς περιορισμούς της σύγκρισης.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** η υλοποίηση LRPG ως baseline θα εξεταστεί μόνο εφόσον το complexity και η διαθεσιμότητα αξιόπιστου implementation είναι συμβατά με το scope.
