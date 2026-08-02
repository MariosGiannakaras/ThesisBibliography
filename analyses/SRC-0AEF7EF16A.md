---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "UAI 2019 proceedings paper 228, PDF 11 σελίδων"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# A Bayesian Approach to Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Esther Derman, Daniel J. Mankowitz, Timothy A. Mann, Shie Mannor
- **Έτος:** 2019
- **Τύπος πηγής:** πρωτογενής ερευνητική εργασία robust και Bayesian reinforcement learning
- **Έκδοση / URL:** Proceedings of UAI 2019, paper 228 — https://www.auai.org/uai2019/proceedings/papers/228.pdf
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0AEF7EF16A.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς ένας robust-RL agent μπορεί να διατηρήσει προστασία απέναντι σε model misspecification χωρίς να παραμένει υπερβολικά συντηρητικός όταν τα νέα δεδομένα δείχνουν ότι το περιβάλλον είναι ευνοϊκότερο ή διαφορετικό από το αρχικό uncertainty set. Οι συγγραφείς συνδυάζουν Robust MDPs με Bayesian posterior uncertainty και εισάγουν την Uncertainty Robust Bellman Equation (URBE), καθώς και τη deep-RL υλοποίηση DQN-URBE.

Η πηγή είναι άμεσα σχετική με τη διπλωματική επειδή εξετάζει changing transition dynamics, online adaptation, robustness–performance trade-off και recovery μετά από γνωστή αλλαγή. Επιπλέον, δύο από τα τρία πειραματικά domains είναι μικρό MDP και 10×10 GridWorld, άρα η μεθοδολογική σύνδεση με ένα ελεγχόμενο GridWorld είναι σαφέστερη από ό,τι σε πολλά robotics benchmarks.

## Σύνοψη

Στα κλασικά Robust MDPs ο agent βελτιστοποιεί τη worst-case επίδοση πάνω σε ένα uncertainty set μεταβάσεων. Η προσέγγιση μπορεί να είναι ασφαλής αλλά υπερβολικά απαισιόδοξη, ιδίως όταν το set είναι μεγάλο ή rectangular και επιτρέπει στη “φύση” να επιλέγει ασύμβατα worst cases ανεξάρτητα για κάθε state–action pair.

Οι συγγραφείς ξεκινούν από Dirichlet priors για τις transitions και ενημερώνουν posterior uncertainty sets καθώς συλλέγονται observations. Η URBE υπολογίζει άνω φράγμα της posterior variance των robust Q-values μέσω Bellman-like recursion. Η variance χρησιμοποιείται ως exploration bonus, ώστε ο agent να εξερευνά state–action pairs όπου υπάρχει robust uncertainty και να προσαρμόζει έμμεσα το uncertainty set, αντί να δεσμεύεται μόνιμα σε fixed minimax policy.

Στη deep έκδοση, το DQN-URBE διαθέτει δύο output heads: robust Q-value και robust uncertainty. Συγκρίνεται με vanilla DQN, fixed robust DQN και DQN-UBE. Στο 10×10 Mars Rover, το fixed robust DQN αποφεύγει τον κίνδυνο αλλά δεν φτάνει στον στόχο, ενώ το DQN-UBE αποδίδει nominally αλλά είναι ευαίσθητο σε μεγαλύτερη failure probability. Το DQN-URBE επιτυγχάνει καλύτερο trade-off. Στο Cartpole, μετά από αλλαγή pole length κατά το training, το DQN-URBE ανακάμπτει γρηγορότερα από το robust DQN, το οποίο δεν επιστρέφει στη βέλτιστη reward.

## Μεθοδολογία

- **Τυπικό πλαίσιο:** finite-horizon Robust MDP με bounded rewards και state–action rectangular uncertainty set για transition probabilities.
- **Bayesian model:** ανεξάρτητα Dirichlet priors ανά state–action transition distribution και posterior update από observed history.
- **Posterior uncertainty sets:** L1 balls γύρω από posterior mean transitions με fixed confidence radius ανά state–action pair.
- **URBE:** Bellman recursion για άνω φράγμα της posterior variance των robust Q-values.
- **Deep architecture:** robust-DQN head για robust Q-values και δεύτερο head για robust local uncertainty· Gaussian exploration bonus με coefficient β.
- **Baselines:** vanilla DQN, fixed robust DQN και DQN-UBE.
- **Domains:** 7-state adversarial MDP, 10×10 Mars Rover GridWorld και Cartpole.
- **Changing dynamics:** διαδοχικές αλλαγές adversarial transition probability στο toy MDP και μεταβολή pole length από 0.75 σε 1.25 κατά το Cartpole training.
- **Επαναλήψεις/αξιολόγηση:** toy-MDP curves averaged over 10 runs για UBE/URBE· 100 testing episodes για Mars Rover trajectories· 200 testing episodes ανά Cartpole length.

## Κύρια ευρήματα

1. **Η worst-case robustness μπορεί να καταλήξει σε λειτουργική αδράνεια.** Στο Mars Rover, το fixed robust DQN αποφεύγει τη failure state αλλά δεν φτάνει στον στόχο ούτε στο nominal model. Η σταθερή αλλά χαμηλή reward δεν πρέπει να ερμηνεύεται ως επιτυχής resilience. Τεκμηρίωση: σελ. 5–7, Sections 7.1–7.2, Figures 2–4.
2. **Η nominal exploration χωρίς robust model είναι ευάλωτη.** Το DQN-UBE αποδίδει καλά στο nominal Mars Rover αλλά υποβαθμίζεται έντονα όσο αυξάνεται η probability of failure και γίνεται χειρότερο από το fixed robust baseline πάνω από συγκεκριμένη περιοχή. Τεκμηρίωση: σελ. 6, Section 7.2 και Figure 3.
3. **Το DQN-URBE ισορροπεί nominal performance και robustness.** Στο Mars Rover φτάνει τον στόχο στο nominal model και παραμένει λιγότερο ευαίσθητο σε model misspecification από vanilla DQN/UBE. Τεκμηρίωση: σελ. 6–7, Figures 3–4.
4. **Η posterior uncertainty μπορεί να ενεργοποιήσει online προσαρμογή.** Στο Cartpole, μετά την αλλαγή pole length από 0.75 σε 1.25, το URBE converges πιο αργά αρχικά αλλά ανακάμπτει πολύ γρηγορότερα και επιστρέφει σε maximal reward, ενώ το fixed robust DQN δεν ανακάμπτει στη βέλτιστη επίδοση. Τεκμηρίωση: σελ. 7–8, Figure 6(c).
5. **Το robustness–conservativeness trade-off πρέπει να μετριέται ρητά.** Ένας agent μπορεί να έχει μικρή επιπλέον degradation υπό shift επειδή ήδη αποδίδει χαμηλά στο nominal environment. Η σύγκριση απαιτεί nominal score, worst/shifted score, degradation ratio και recovery. Τεκμηρίωση: Sections 1, 7.2–7.3 και Conclusion.
6. **Η θεωρητική URBE και η deep approximation δεν έχουν τις ίδιες εγγυήσεις.** Στη deep υλοποίηση παραβιάζονται assumptions όπως acyclic transition graph, fixed policy και exact solution της URBE. Οι συγγραφείς χαρακτηρίζουν την εφαρμογή heuristic που λειτουργεί εμπειρικά. Τεκμηρίωση: σελ. 4–5, πριν από Section 7.
7. **Η εργασία δεν λύνει πλήρως τη μέτρηση resilience.** Δείχνει recovery σε training curves, αλλά δεν ορίζει standardized recovery threshold, confidence interval ή multiple-change metric. Αυτό πρέπει να συμπληρωθεί από τις πηγές resilience και statistical evaluation.

## Υποθέσεις και ορισμοί

Η θεωρία βασίζεται σε finite horizon, bounded rewards, rectangular transition uncertainty, ανεξάρτητα Dirichlet priors και, για το variance bound, directed acyclic graph υπό worst-case transition και fixed policy. Τα confidence radii των posterior uncertainty sets παραμένουν fixed αντί να βελτιστοποιούνται online.

Η deep έκδοση χρησιμοποιεί function approximation και approximated uncertainty head, οπότε τα θεωρητικά assumptions δεν ισχύουν πλήρως. Ο exploration coefficient β και το uncertainty-set construction αποτελούν κρίσιμα hyperparameters. Model misspecification ορίζεται ως perturbation των dynamics, όχι ως observation noise, reward corruption ή action substitution.

## Περιορισμοί και απειλές εγκυρότητας

Τα πειράματα καλύπτουν μόνο τρία σχετικά μικρά domains και περιορισμένο σύνολο baselines. Δεν υπάρχει σύγκριση με σύγχρονες continual-RL, change-detection ή meta-RL methods. Ο αριθμός runs είναι μικρός στο toy MDP και δεν παρουσιάζονται σύγχρονα uncertainty intervals ή robust aggregate statistics. Η επιλογή των uncertainty sets και της prior επηρεάζει το πόσο conservative ή adaptive γίνεται ο agent.

Η claim της ταχύτερης adaptation στο Cartpole προκύπτει από ένα συγκεκριμένο abrupt change κατά το training. Δεν αποδεικνύει general recovery superiority σε observation noise, action failures, reward changes, repeated shifts ή unseen environments. Επίσης, το DQN-URBE έχει μεγαλύτερη αρχιτεκτονική και υπολογιστική πολυπλοκότητα από tabular baselines, γεγονός σημαντικό για resource-bounded διπλωματική.

Η εργασία δεν διαχωρίζει detection delay από policy adaptation: η posterior uncertainty αυξάνει exploration, αλλά δεν παράγει explicit changepoint alarm. Για να αποδοθεί επιστημονικά η recovery, χρειάζονται logs uncertainty, action policy και performance γύρω από το event.

## Σχέση με άλλες πηγές

- Το `SRC-3856071502` παρέχει explicit Bayesian changepoint detector, ενώ το URBE προσαρμόζει uncertainty online χωρίς ξεχωριστό alarm.
- Το `SRC-95C9DAEE68` διαχωρίζει detection και adaptation και εξετάζει πολλαπλές non-stationary changes.
- Το `SRC-81A15E6905` καλύπτει action robustness, κατηγορία που δεν μοντελοποιείται από transition-only URBE.
- Το `SRC-0A594EACC0` παρέχει failure/recovery profiles για να αξιολογηθεί η recovery curve του URBE.
- Το `SRC-0A4AFAC8E9` παρέχει στατιστικό protocol για πιο αξιόπιστη επανεκτέλεση της σύγκρισης.

## Χρήση στη διπλωματική

Η πηγή πρέπει να χρησιμοποιηθεί για:

- την παρουσίαση adaptive robust MDP methods και του κινδύνου υπερβολικής conservativeness,
- την επιλογή ενός robust/adaptive model family ως πιθανό πειραματικό candidate ή advanced baseline,
- τη σχεδίαση GridWorld scenario με stochastic/adversarial transition failures,
- τη μέτρηση nominal utility μαζί με perturbation robustness,
- την καταγραφή uncertainty signal ως πιθανό explanatory diagnostic,
- την αιτιολόγηση recovery curves μετά από abrupt dynamic change.

Η υλοποίηση DQN-URBE δεν πρέπει να θεωρηθεί δεδομένη. Πριν επιλεγεί ως τελικό model χρειάζεται feasibility prototype, έλεγχος διαθέσιμου κώδικα, υπολογιστικού κόστους και σύγκριση με απλούστερο tabular Bayesian/robust baseline. Σε μικρό GridWorld μπορεί να είναι επιστημονικά καθαρότερο να υλοποιηθεί tabular analogue ή περιορισμένη ablation αντί πλήρους deep architecture.

## Απόφαση ένταξης

- **Ρόλος:** κύρια πηγή μοντέλου και robust-adaptation trade-off.
- **Απόφαση:** ένταξη και εξαγωγή.
- **Αιτιολόγηση:** παρέχει άμεσο GridWorld/Cartpole evidence για changing dynamics και recovery, μαζί με σαφείς assumptions και failure mode της fixed robust policy. Δεν αποτελεί ακόμη τελική απόφαση υλοποίησης.

## Κατάσταση επαλήθευσης

Κατάσταση: επαληθευμένη. Ελέγχθηκε το πλήρες UAI proceedings PDF, οι URBE assumptions/equations, η DQN architecture, τα τρία experiments, οι figures, οι baselines, η conclusion και οι δηλωμένοι/συναγόμενοι περιορισμοί. Τα τεκμήρια καταγράφονται στο `αποσπάσματα/SRC-0AEF7EF16A.md`.