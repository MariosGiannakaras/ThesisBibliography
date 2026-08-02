---
κωδικός: SRC-91D56A10CF
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "ICML 2021, Proceedings of Machine Learning Research 139"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Deep Reinforcement Learning amidst Continual Structured Non-Stationarity

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Annie Xie, James Harrison, Chelsea Finn
- **Έτος:** 2021
- **Τύπος πηγής:** πρωτογενής θεωρητική και πειραματική εργασία συνεδρίου
- **Δημοσίευση:** Proceedings of the 38th International Conference on Machine Learning, PMLR 139
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-91D56A10CF.pdf`
- **Μέθοδος:** Lifelong Latent Actor-Critic (LILAC)

## Σκοπός και ερευνητικό ερώτημα

Η εργασία μελετά continual non-stationarity στην οποία η δυναμική ή/και η ανταμοιβή μεταβάλλονται διαρκώς, αλλά όχι αυθαίρετα: οι διαδοχικές καταστάσεις του περιβάλλοντος συνδέονται μέσω κρυφών παραμέτρων που ακολουθούν δική τους χρονική δυναμική. Το ερευνητικό ερώτημα είναι αν ένας off-policy agent μπορεί να χρησιμοποιήσει παλαιότερη εμπειρία χωρίς το replay buffer να τον παγιδεύει σε μια «μέση» πολιτική για όλες τις παλιές και νέες συνθήκες.

Οι συγγραφείς εισάγουν το Dynamic Parameter MDP (DP-MDP), όπου κάθε episode αντιστοιχεί σε MDP που προσδιορίζεται από latent variable z και τα z εξελίσσονται διαδοχικά. Το LILAC μαθαίνει ταυτόχρονα representation των latent task parameters, transition model μεταξύ τους και maximum-entropy policy/critic conditioned στο inferred context. Η εργασία είναι άμεσα συναφής με δυναμικά μεταβαλλόμενους κανόνες ή dynamics, αλλά η συνάφεια εξαρτάται από την ύπαρξη επαναλαμβανόμενης ή προβλέψιμης δομής στις αλλαγές.

## Σύνοψη

Τα standard episodic RL benchmarks θεωρούν ότι κάθε episode προέρχεται από το ίδιο MDP. Αντίθετα, το DP-MDP περιγράφει ακολουθία MDPs με unobserved continuous parameters. Οι παράμετροι δεν είναι i.i.d. αλλά ακολουθούν transition model. Εάν το z ήταν γνωστό, η επαυξημένη κατάσταση `(s, z)` θα επέτρεπε standard RL. Επειδή δεν είναι γνωστό, το LILAC χρησιμοποιεί variational inference ώστε να συμπεράνει z από trajectories και να προβλέψει το context του επόμενου episode.

Ο actor και ο critic condition στα inferred latent variables, ενώ η εκπαίδευση είναι off-policy και αξιοποιεί replay. Αυτό διαφέρει από απλό recurrent policy που προσπαθεί να αναγνωρίσει το τρέχον task μόνο μέσα στο episode: το LILAC μοντελοποιεί ρητά τη χρονική σχέση μεταξύ διαδοχικών tasks. Στα πειράματα, η μέθοδος συγκρίνεται με SAC, SLAC και PPO, καθώς και με goal-conditioned oracle όπου το true goal είναι διαθέσιμο.

## Μεθοδολογία

- **Τυπικό μοντέλο:** Dynamic Parameter MDP, ειδική δομημένη περίπτωση POMDP με latent parameters που επηρεάζουν transition dynamics και reward.
- **Representation:** inference network για approximate posterior του z από trajectory και learned prior/transition model για το επόμενο z.
- **RL πυρήνας:** maximum-entropy off-policy actor-critic, συγγενής με SAC, conditioned στο latent context.
- **Baselines:** SAC χωρίς latent variables, SLAC για partially observed dynamics, PPO ως on-policy baseline και goal-conditioned SAC oracle σε goal-reaching tasks.
- **Περιβάλλοντα:** Sawyer reaching με μη παρατηρούμενο κινούμενο target, HalfCheetah με μεταβαλλόμενο wind και target velocity, Minitaur με μεταβαλλόμενο payload/mass και 2D Open World με non-stationary dynamics.
- **Είδη μεταβολής:** reward shift, dynamics shift, ταυτόχρονα reward/dynamics shifts, διαφορετικές ταχύτητες αλλαγής, intra-episode smooth shift και extrapolating target trajectory.
- **Runs:** best hyperparameter setting με τρία random seeds για κάθε προσέγγιση, εκτός από SAC στο Minitaur που επεκτείνεται σε πέντε seeds μετά από significance analysis.
- **Reporting:** learning curves και 95% confidence intervals, με πρόσθετες ablations για rate, intra-episode representation και extrapolation.

## Κύρια ευρήματα

1. **Η μη στασιμότητα μπορεί να έχει εκμεταλλεύσιμη χρονική δομή.** Το DP-MDP δεν αντιμετωπίζει κάθε νέο task ως ανεξάρτητο. Το latent transition model επιτρέπει πρόβλεψη της επόμενης περιβαλλοντικής κατάστασης και άμεσο conditioning της πολιτικής. Τεκμηρίωση: σελ. 1–3, Sections 1–2.

2. **Το replay χωρίς context μπορεί να συγκλίνει σε συμβιβαστική μέση συμπεριφορά.** Στα πειράματα, το SAC συνδυάζει εμπειρίες από διαφορετικά MDPs στο ίδιο buffer και καταλήγει σε averaged behavior, ενώ το SLAC δεν μοντελοποιεί inter-episode non-stationarity. Τεκμηρίωση: σελ. 6–7, Section 6 και Figure 5.

3. **Latent context βοηθά όταν αλλάζουν ταυτόχρονα dynamics και reward.** Στο HalfCheetah με μεταβολές wind και target velocity, το LILAC διατηρεί υψηλότερη και σταθερότερη επίδοση από τα baselines στο συγκεκριμένο protocol. Τεκμηρίωση: σελ. 6–7, Figure 5.

4. **Η ταχύτητα αλλαγής είναι ανεξάρτητη πειραματική διάσταση.** Στο Sawyer, το goal κινείται με διαφορετικά angular step sizes και η αναφερόμενη επίδοση του LILAC παραμένει σχετικά σταθερή στις εξεταζόμενες τιμές, ενώ το stationary case προσεγγίζει το SAC. Τεκμηρίωση: σελ. 7, Section 6 και Figure 6(a).

5. **Η episode-boundary υπόθεση μπορεί να χαλαρώσει μόνο υπό συγκεκριμένες συνθήκες.** Σε smoothly varying Sawyer, το LILAC λειτουργεί με αλλαγή κάθε timestep, ιδιαίτερα όταν το timestep δίνεται ή μπορεί να συναχθεί. Αυτό δεν αποδεικνύει αντοχή σε arbitrary abrupt intra-episode change. Τεκμηρίωση: σελ. 7–8, Figure 6(b).

6. **Η extrapolation επιτυχία είναι task-structured, όχι γενική OOD εγγύηση.** Το LILAC παρακολουθεί target που κινείται κατά μήκος συνεχούς γραμμής πέρα από τις προηγούμενες θέσεις, επειδή η latent dynamics διαθέτει προβλέψιμη μορφή. Τεκμηρίωση: σελ. 7–8, Figure 6(c).

7. **Σπάνια και διακριτά απρόβλεπτα shifts μπορεί να απαιτούν explicit changepoint detection.** Οι συγγραφείς αναγνωρίζουν ότι το LILAC δεν είναι σχεδιασμένο για unobserved, infrequent abrupt changes και παραπέμπουν στη change-point literature. Τεκμηρίωση: σελ. 8, Conclusion.

## Υποθέσεις και ορισμοί

Η πηγή χρησιμοποιεί «structured non-stationarity» για αλλαγές των οποίων οι latent parameters ακολουθούν learnable temporal process. Αυτό διαφέρει από:

- **i.i.d. domain randomization**, όπου κάθε task είναι ανεξάρτητο δείγμα,
- **single abrupt changepoint**, όπου η αλλαγή μπορεί να μην επαναλαμβάνεται,
- **adversarial perturbation**, όπου η μετάβαση επιλέγεται worst-case,
- **stationary partial observability**, όπου το κρυφό state αλλάζει αλλά ο γενετικός μηχανισμός παραμένει σταθερός.

Για τη διπλωματική, ένα predictable cycle κανόνων, μια σταδιακή μετατόπιση failure rate ή επαναλαμβανόμενες περιβαλλοντικές φάσεις μπορούν να θεωρηθούν structured. Αντίθετα, ένα τυχαίο μοναδικό rule switch απαιτεί χωριστό detection/adaptation scenario.

## Περιορισμοί και απειλές εγκυρότητας

Η βασική DP-MDP διατύπωση θεωρεί ένα latent context ανά episode. Η επέκταση σε intra-episode αλλαγές βασίζεται σε timestep information ή σε approximate quantization, επομένως δεν καλύπτει αυτόματα ξαφνικές μη παρατηρούμενες μεταβολές. Η επιτυχία εξαρτάται από learnable regularity των latent dynamics και μπορεί να αποτύχει όταν οι αλλαγές δεν έχουν επαναλαμβανόμενη δομή.

Τα πειράματα είναι continuous-control ή continuous-navigation και απαιτούν σημαντικά πιο σύνθετη function approximation από ένα tabular GridWorld. Τα περισσότερα αποτελέσματα χρησιμοποιούν μόνο τρία seeds. Παρότι εμφανίζονται 95% intervals και συμπληρωματικός significance έλεγχος, η μικρή βάση runs περιορίζει την ακρίβεια σύγκρισης. Η hyperparameter tuning γίνεται για όλες τις μεθόδους, αλλά δεν τεκμηριώνεται εδώ ότι τα συνολικά tuning budgets είναι απολύτως ίσα.

Οι authors συγκρίνουν με ισχυρά baselines, όμως το goal-conditioned SAC oracle έχει πρόσβαση σε true task information που ο LILAC δεν διαθέτει και λειτουργεί κυρίως ως άνω σημείο αναφοράς. Τα reported claims πρέπει να παραμένουν εντός των συγκεκριμένων task families.

## Χρήση στη διπλωματική

Η πηγή πρέπει να χρησιμοποιηθεί ως κύρια αναφορά για:

- τον ορισμό structured non-stationarity,
- latent-context adaptation και task inference,
- τον κίνδυνο replay interference ή averaged policies,
- σενάρια με σταδιακή, περιοδική ή επαναλαμβανόμενη αλλαγή rules/dynamics,
- τη διάκριση μεταξύ predictable drift και abrupt changepoints,
- την ανάγκη να αξιολογείται ο ρυθμός αλλαγής ως experimental factor.

Δεν είναι απαραίτητο να υλοποιηθεί πλήρες LILAC. Για μικρό GridWorld μπορεί να λειτουργήσει ως θεωρητική αιτιολόγηση ενός context-aware baseline, ενός oracle-context upper bound ή μιας απλούστερης task-belief μέθοδου. Η υπολογιστική πολυπλοκότητα και τα continuous-control assumptions πρέπει να ληφθούν υπόψη στην επιλογή μοντέλων.

## Σχέση με άλλες πηγές

- **SRC-95C9DAEE68:** η διατριβή για non-stationary environments δίνει detection–adaptation decomposition και ευρύτερη taxonomy. Το LILAC είναι συγκεκριμένη latent predictive adaptation μέθοδος.
- **SRC-3856071502:** το Bayesian Online Changepoint Detection ταιριάζει καλύτερα σε abrupt, infrequent shifts. Το LILAC ταιριάζει σε persistent structured evolution.
- **SRC-F909CABDEB:** η continual-RL survey παρέχει stability, plasticity, forgetting και transfer metrics. Το LILAC αποτελεί συγκεκριμένο continual adaptation παράδειγμα.
- **SRC-0882A9B2B0:** η generalization εργασία διαχωρίζει interpolation και extrapolation. Το LILAC παρέχει task-specific extrapolating latent trajectory, όχι γενική zero-shot guarantee.

## Επιτρεπτοί και μη επιτρεπτοί ισχυρισμοί

**Επιτρέπεται να υποστηριχθεί ότι:**

- structured temporal context μπορεί να βελτιώσει off-policy adaptation σε διαδοχικά μεταβαλλόμενα MDPs,
- replay χωρίς task context μπορεί να οδηγήσει σε averaged behavior,
- το LILAC υπερέβη SAC, SLAC και PPO στα συγκεκριμένα continuous non-stationary benchmarks,
- ο ρυθμός και η προβλεψιμότητα των αλλαγών πρέπει να αποτελούν χωριστές experimental variables.

**Δεν επιτρέπεται να υποστηριχθεί ότι:**

- το LILAC χειρίζεται κάθε arbitrary ή adversarial non-stationarity,
- τρία seeds αρκούν γενικά για αξιόπιστη κατάταξη RL algorithms,
- η extrapolation επίδοση του Sawyer ισοδυναμεί με γενική OOD generalization,
- η μέθοδος είναι αναγκαία ή υπολογιστικά κατάλληλη για το τελικό GridWorld χωρίς pilot comparison.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Έλεγχος πρωτοτύπου:** ολοκληρώθηκε στο επίσημο ICML/PMLR PDF.
- **Έλεγχος μοντέλου:** ολοκληρώθηκε στις Sections 2–4.
- **Έλεγχος πειραμάτων:** ολοκληρώθηκε στη Section 6 και στα appendices για environments/seeds.
- **Έλεγχος περιορισμών:** ολοκληρώθηκε στη Section 7.
- **Απόφαση:** κύρια πηγή για structured non-stationarity, latent context και predictive adaptation· όχι γενική λύση για απρόβλεπτα changepoints.
