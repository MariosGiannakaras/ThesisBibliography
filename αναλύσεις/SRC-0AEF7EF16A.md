---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "UAI 2019 proceedings, paper 228"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# A Bayesian Approach to Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Esther Derman, Daniel Mankowitz, Timothy Mann, Shie Mannor
- **Έτος:** 2019
- **Τύπος πηγής:** πρωτογενής θεωρητική και πειραματική εργασία συνεδρίου
- **Δημοσίευση:** Conference on Uncertainty in Artificial Intelligence (UAI 2019)
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0AEF7EF16A.pdf`
- **Επίσημη έκδοση:** UAI proceedings, paper 228

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς ένα robust reinforcement-learning σύστημα μπορεί να παραμείνει προστατευμένο απέναντι σε λανθασμένο ή μεταβαλλόμενο μοντέλο μεταβάσεων χωρίς να καταλήγει σε υπερβολικά απαισιόδοξη πολιτική. Το βασικό πρόβλημα των κλασικών Robust MDPs είναι ότι η πολιτική βελτιστοποιείται για το χειρότερο μοντέλο μέσα σε ένα προκαθορισμένο uncertainty set. Όταν το σύνολο αυτό είναι υπερβολικά μεγάλο ή state-action rectangular, ο agent μπορεί να αποφεύγει χρήσιμη εξερεύνηση και να θυσιάζει μεγάλη ονομαστική απόδοση.

Οι συγγραφείς ρωτούν αν η αβεβαιότητα γύρω από τις robust Q-values μπορεί να ενημερώνεται Bayesian online και να χρησιμοποιείται ως exploration signal. Προτείνουν την Uncertainty Robust Bellman Equation (URBE) και την κλιμακούμενη εκδοχή DQN-URBE. Η συνάφεια με την αίτηση είναι υψηλή: η εργασία αφορά μεταβαλλόμενη δυναμική, model misspecification, συνέχιση μάθησης μετά τη μεταβολή και εμπειρική ταχύτητα ανάκαμψης. Δεν καλύπτει όμως γενικά κάθε μορφή resilience και δεν εξετάζει αλλαγές κανόνων ή reward functions ως ξεχωριστό κύριο πείραμα.

## Σύνοψη

Το πλαίσιο ξεκινά από ένα finite-horizon RMDP με σύνολο πιθανών transition matrices. Για κάθε state-action pair χρησιμοποιείται Dirichlet prior και, καθώς συσσωρεύονται παρατηρήσεις, κατασκευάζεται posterior uncertainty set γύρω από την posterior mean transition. Η robust Q-value παραμένει worst-case ως προς αυτό το σύνολο, αλλά η αβεβαιότητα της Q-value δεν θεωρείται σταθερή. Οι συγγραφείς αποδεικνύουν άνω φράγμα της posterior variance που ικανοποιεί Bellman-like recursion, την URBE.

Η πρακτική ιδέα είναι ότι υψηλή epistemic uncertainty σε μια state-action περιοχή δικαιολογεί ασφαλή εξερεύνηση ακόμη και μέσα σε robust planning. Στην deep εκδοχή, το DQN-URBE μαθαίνει robust Q-network και χωριστή εκτίμηση robust local uncertainty. Η συμπεριφορά επιλέγεται με βάση τη robust αξία συν exploration bonus. Με τον τρόπο αυτό ο agent δεν μένει εγκλωβισμένος στη στατική χειρότερη υπόθεση, αλλά προσαρμόζει έμμεσα το επίπεδο robustness καθώς αποκτά νέα δεδομένα.

## Μεθοδολογία

- **Θεωρητικό μοντέλο:** finite state/action RMDP, finite horizon, bounded rewards και state-action rectangular posterior uncertainty sets.
- **Bayesian υπόθεση:** ανεξάρτητα Dirichlet priors για τις transition distributions κάθε state-action pair.
- **Κύρια τεχνική:** άνω φράγμα της posterior variance των robust Q-values και μοναδική λύση της Uncertainty Robust Bellman Equation.
- **Αλγόριθμοι:** tabular URBE και DQN-URBE με robust Q-function, robust local uncertainty estimator και uncertainty-guided exploration.
- **Baselines:** vanilla DQN, fixed robust DQN και DQN-UBE χωρίς robust transition set.
- **Περιβάλλοντα:** επτακαταστατικό toy MDP, 10×10 Mars Rover gridworld και CartPole.
- **Μεταβολές:** διαδοχικές αλλαγές adversarial transition probability στο toy MDP, αυξημένη πιθανότητα αποτυχίας κίνησης στο Mars Rover και αλλαγή μήκους πόλου στο CartPole.
- **Αξιολόγηση:** cumulative reward ή testing reward, state-visitation heatmaps και training recovery curve μετά από αλλαγή dynamics.

Στο toy MDP οι πιθανότητες adversarial transition αλλάζουν διαδοχικά σε 0.001, 0.8, 0.1 και 0.9 και οι UBE/URBE καμπύλες μέσου cumulative reward βασίζονται σε δέκα runs. Στο Mars Rover η εκπαίδευση γίνεται με nominal failure probability 0.005 και η robustness δοκιμάζεται μεταξύ άλλων στο 0.2. Στο CartPole οι agents εκπαιδεύονται σε pole length 0.75, αξιολογούνται σε διαφορετικά μήκη και σε χωριστό training experiment το μήκος μεταβάλλεται σε 1.25 αφού έχει προηγηθεί σύγκλιση.

## Κύρια ευρήματα

1. **Το στατικό worst-case planning μπορεί να είναι υπερβολικά συντηρητικό.** Η rectangularity και ένα ευρύ uncertainty set επιτρέπουν στη φύση να επιλέγει ασύμβατα worst cases ανεξάρτητα ανά state-action pair. Αυτό μπορεί να δώσει ασφαλή αλλά πρακτικά άχρηστη πολιτική. Τεκμηρίωση: σελ. 1–2, Introduction και Background.

2. **Η αβεβαιότητα πρέπει να διαχωρίζεται από τη robust αξία.** Η URBE εκτιμά posterior variance των robust Q-values, όχι απλώς τη stochasticity του περιβάλλοντος. Έτσι το exploration bonus στοχεύει περιοχές όπου λείπει γνώση για το worst-case transition model. Τεκμηρίωση: σελ. 3–5, Sections 4–6.

3. **Online ενημέρωση μπορεί να μειώσει το κόστος conservatism.** Στο Mars Rover, ο fixed robust DQN αποφεύγει τη διαδρομή προς τον στόχο ακόμη και στο nominal model, ενώ το DQN-URBE εξερευνά και φτάνει στον στόχο. Σε υψηλότερη failure probability το URBE παραμένει πιο αποτελεσματικό από το μη robust UBE. Τεκμηρίωση: σελ. 6–7, Section 7.2 και Figures 3–4.

4. **Η recovery speed είναι ξεχωριστή από τη nominal και stressed απόδοση.** Μετά την αλλαγή pole length από 0.75 σε 1.25, η αναφερόμενη training curve δείχνει ότι το DQN-URBE ανακάμπτει γρηγορότερα και φτάνει ξανά το μέγιστο reward, ενώ ο fixed robust DQN δεν επανέρχεται στην προηγούμενη βέλτιστη επίδοση. Τεκμηρίωση: σελ. 7–9, Section 7.3 και Figure 6(c).

5. **Υπάρχει τριπλό trade-off robustness, exploration και nominal performance.** Περισσότερη robust προστασία δεν είναι αυτομάτως καλύτερη: μπορεί να εμποδίσει την επίτευξη του στόχου. Αντίστροφα, exploration χωρίς robust criterion μπορεί να αποτύχει υπό σοβαρό model misspecification. Τεκμηρίωση: σελ. 6–9, Sections 7–9.

6. **Οι εμπειρικές ενδείξεις δεν αποτελούν γενική εγγύηση convergence ή resilience.** Οι ίδιοι οι συγγραφείς αφήνουν ως μελλοντική εργασία την asymptotic συμπεριφορά και την επίδραση του μεγέθους του posterior uncertainty set. Τεκμηρίωση: σελ. 9, Conclusion.

## Υποθέσεις και ορισμοί

Η εργασία χρησιμοποιεί τον όρο model misspecification για perturbation της transition dynamics. Το robust objective είναι worst-case και δεν ισοδυναμεί με expected performance υπό γνωστή stochastic noise distribution. Η posterior αβεβαιότητα προέρχεται από έλλειψη γνώσης για τις μεταβάσεις, ενώ η εσωτερική stochasticity του MDP είναι διαφορετικό είδος αβεβαιότητας.

Για τη διπλωματική, αυτή η διάκριση είναι κρίσιμη. Ένα scenario με γνωστή πιθανότητα action failure αξιολογεί robustness σε aleatoric stochasticity. Ένα ξαφνικά μεταβαλλόμενο ή άγνωστο failure rate αξιολογεί detection και epistemic adaptation. Οι δύο περιπτώσεις δεν πρέπει να συγχωνευθούν σε μία μόνο καμπύλη.

## Περιορισμοί και απειλές εγκυρότητας

Το θεωρητικό μέρος εξαρτάται από finite spaces, bounded rewards, acyclic worst-case transition graph και rectangular uncertainty sets. Η ανεξαρτησία των Dirichlet priors ανά state-action pair μπορεί να είναι ισχυρή απλοποίηση. Το radius του posterior uncertainty set παραμένει πρακτικά fixed, άρα η μέθοδος δεν επιλύει πλήρως τη βαθμονόμηση του uncertainty set.

Η πειραματική τεκμηρίωση είναι περιορισμένη σε τρία domains και δεν παρουσιάζει ενιαίο σύγχρονο statistical protocol για όλα τα deep experiments. Το toy MDP αναφέρει δέκα runs, αλλά τα deep plots δεν τεκμηριώνουν εξίσου καθαρά seeds, confidence intervals ή hypothesis tests. Η recovery σύγκριση στο CartPole είναι χρήσιμη ως proof of concept, όχι ως ακριβής αριθμητική εκτίμηση γενικής recovery time. Επιπλέον, ο worst-case adversary μπορεί να είναι ισχυρότερος από τον τυχαίο θόρυβο που θα μοντελοποιηθεί στο GridWorld της διπλωματικής.

## Χρήση στη διπλωματική

Η πηγή πρέπει να χρησιμοποιηθεί ως κύρια θεωρητική και μεθοδολογική αναφορά για:

- τη διάκριση fixed robustness από online adaptation,
- το conservatism cost των worst-case πολιτικών,
- Bayesian uncertainty ως σήμα προσαρμοστικής εξερεύνησης,
- την ανάγκη χωριστών nominal, stressed και post-change μετρικών,
- τον ορισμό recovery speed ως δυναμικής καμπύλης μετά από γνωστό change point,
- ένα υποψήφιο robust/adaptive baseline ή σχεδιαστική αρχή, όχι κατ’ ανάγκη πιστή υλοποίηση DQN-URBE.

Στο απλό προσομοιωμένο περιβάλλον της αίτησης μπορεί να μεταφραστεί σε controlled changes της transition kernel ή του action-failure rate. Η εργασία αιτιολογεί γιατί ένα GridWorld μπορεί να είναι κατάλληλο testbed, αλλά δεν μετατρέπει το GridWorld σε επίσημη απαίτηση ούτε τεκμηριώνει real-world generalization.

## Σχέση με άλλες πηγές

- **SRC-81A15E6905:** μοντελοποιεί action perturbations με adversarial policy. Η παρούσα εργασία εστιάζει αντίθετα σε Bayesian uncertainty των transition models και online μείωση conservatism.
- **SRC-3856071502:** παρέχει explicit changepoint posterior. Το URBE δεν είναι καθαρός changepoint detector· προσαρμόζει συνεχώς uncertainty και exploration.
- **SRC-95C9DAEE68:** υποστηρίζει τη διάσπαση detection–adaptation και post-change metrics. Η παρούσα πηγή δίνει συγκεκριμένο robust-Bayesian μηχανισμό adaptation.
- **SRC-FE2C0A3E00:** αιτιολογεί controlled gridworld benchmarking και independent safety/performance functions. Η παρούσα πηγή προσθέτει συγκεκριμένο dynamic perturbation και recovery experiment.

## Επιτρεπτοί και μη επιτρεπτοί ισχυρισμοί

**Επιτρέπεται να υποστηριχθεί ότι:**

- fixed robust policies μπορεί να είναι υπερβολικά συντηρητικές,
- posterior uncertainty μπορεί να χρησιμοποιηθεί για safe exploration σε RMDPs,
- η πηγή παρουσιάζει εμπειρική ταχύτερη ανάκαμψη του DQN-URBE από fixed robust DQN στο συγκεκριμένο CartPole experiment,
- nominal performance, stressed performance και recovery πρέπει να εξετάζονται χωριστά.

**Δεν επιτρέπεται να υποστηριχθεί ότι:**

- το DQN-URBE είναι καθολικά καλύτερο από κάθε robust ή adaptive algorithm,
- τα αποτελέσματα αποδεικνύουν asymptotic convergence σε arbitrary non-stationarity,
- η μέθοδος καλύπτει άμεσα reward shifts, changing rules και action replacement με τον ίδιο τρόπο,
- οι αριθμητικές ρυθμίσεις του CartPole ή Mars Rover μεταφέρονται αυτούσιες σε άλλο GridWorld.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Έλεγχος πρωτοτύπου:** ολοκληρώθηκε στο επίσημο PDF των UAI proceedings.
- **Έλεγχος μεθόδου και πειραμάτων:** ολοκληρώθηκε στις Sections 3–7 και Appendix.
- **Έλεγχος περιορισμών:** ολοκληρώθηκε στις assumptions και στο Conclusion.
- **Απόφαση:** κύρια πηγή για robust Bayesian adaptation, uncertainty-guided exploration και recovery-versus-conservatism trade-off.
