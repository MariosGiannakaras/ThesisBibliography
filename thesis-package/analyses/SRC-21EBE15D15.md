---
κωδικός: SRC-21EBE15D15
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Journal of Artificial Intelligence Research 76 (2023), arXiv:2111.09794"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# A Survey of Zero-shot Generalisation in Deep Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Robert Kirk, Amy Zhang, Edward Grefenstette, Tim Rocktäschel
- **Έτος:** 2023
- **Τύπος πηγής:** εκτεταμένη επισκόπηση zero-shot generalisation σε deep reinforcement learning
- **Δημοσίευση:** Journal of Artificial Intelligence Research, τόμος 76, σελ. 201–264
- **arXiv:** 2111.09794
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-21EBE15D15.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η πηγή μελετά πώς μια πολιτική deep RL μπορεί να λειτουργεί σε περιβαλλοντικές καταστάσεις ή instances που δεν εμφανίστηκαν κατά την εκπαίδευση, χωρίς να λάβει επιπλέον training data ή gradient updates από τα test instances. Οι συγγραφείς επιδιώκουν να ενοποιήσουν την ορολογία, να δείξουν ότι η zero-shot generalisation (ZSG) είναι οικογένεια προβλημάτων και όχι μία ενιαία ιδιότητα, και να οργανώσουν benchmarks, evaluation protocols και μεθόδους.

Για τη διπλωματική, η πηγή είναι κρίσιμη επειδή διαχωρίζει τρία διαφορετικά ερωτήματα που συχνά συγχέονται:

1. αν η policy αντέχει άμεσα σε άγνωστη μεταβολή χωρίς ενημέρωση,
2. αν αναγνωρίζει τη μεταβολή και προσαρμόζεται online,
3. αν ανακαλεί ή ξαναμαθαίνει προηγούμενο context.

Μόνο το πρώτο είναι αυστηρά zero-shot. Τα άλλα δύο είναι adaptation/recovery και πρέπει να μετρώνται σε διαφορετικό protocol.

## Σύνοψη

Η survey διατυπώνει τα ZSG προβλήματα μέσω contextual MDPs και distributions πάνω σε environment contexts. Η training και η testing distribution μπορεί να είναι ίδια με διαφορετικά samples, να διαφέρουν με interpolation ή extrapolation, ή να περιλαμβάνουν νέους συνδυασμούς παραγόντων. Επομένως, ο ισχυρισμός «βελτιώνει τη γενίκευση» είναι ανεπαρκής χωρίς σαφή περιγραφή του context space, του train/test split, του policy class και του επιτρεπόμενου test-time interaction.

Οι συγγραφείς διαχωρίζουν το environment από το evaluation protocol. Ένα benchmark δεν είναι απλώς ένας simulator ή ένα GridWorld· προκύπτει από τον συνδυασμό environment, context set, train/test context sets, sampling restrictions και interaction budget. Το ίδιο environment μπορεί να χρησιμοποιηθεί για ασθενή held-out-seed evaluation, για controlled interpolation, για extrapolation ή για combinatorial generalization.

Η εργασία ασκεί κριτική στα purely black-box procedural content generation (PCG) environments. Όταν ο ερευνητής ελέγχει μόνο random seeds και όχι τους πραγματικούς παράγοντες μεταβολής, είναι δύσκολο να απομονώσει γιατί μια policy επιτυγχάνει ή αποτυγχάνει. Η προτεινόμενη ισορροπία είναι να συνδυάζονται procedural variety και controllable factors. Αυτό ταιριάζει άμεσα σε ένα GridWorld όπου οι θέσεις obstacles μπορούν να τυχαιοποιούνται, ενώ reward noise, action failure rate, action costs και rule changes ορίζονται ρητά και ανεξάρτητα.

## Μεθοδολογία

- **Μορφή μελέτης:** επισκόπηση και εννοιολογική ενοποίηση του πεδίου ZSG σε deep RL.
- **Τυπικό πλαίσιο:** contextual MDPs, context distributions και policy classes με observed ή unobserved context.
- **Ταξινομία μεταβολών:** state/initial-state variation, dynamics variation, observation variation, reward variation και συνδυασμοί τους.
- **Τύποι split:** IID held-out contexts, interpolation, extrapolation, combinatorial interpolation και ισχυρότερα OOD regimes.
- **Benchmark analysis:** 55 environments, PCG και controllable context sets, discrete/ordinal/continuous factors.
- **Evaluation protocol:** training context set, testing context set, context-efficiency, sample budget και απαγόρευση test-time training στο αυστηρό ZSG setting.
- **Methods taxonomy:** data augmentation/domain randomization, regularization, representation learning, meta-RL-related methods, architectures, model-based approaches και environment generation.
- **Φύση τεκμηρίων:** survey και critical synthesis· δεν αποτελεί νέο ενιαίο benchmark experiment ή meta-analysis.

## Κύρια ευρήματα

1. **Zero-shot σημαίνει χωρίς επιπλέον training στο test instance.** Η policy αξιολογείται σε διαφορετικά environment instances χωρίς πρόσθετα δεδομένα ή updates από αυτά. Domain adaptation και πολλές meta-RL μέθοδοι ανήκουν σε διαφορετικό regime. Τεκμηρίωση: PDF σελ. 202–204, Introduction και Scope.

2. **Η ZSG είναι κλάση προβλημάτων, όχι μία scalar ιδιότητα.** Η επίδοση εξαρτάται από το τι αλλάζει, αν το context παρατηρείται, πόσο απέχει το test distribution και αν πρόκειται για interpolation, extrapolation ή νέο συνδυασμό παραγόντων. Τεκμηρίωση: PDF σελ. 202–205, Sections 1 και 3.

3. **Benchmark = environment + evaluation protocol.** Το environment μόνο του δεν καθορίζει τι εξετάζεται· απαιτούνται explicit training/testing context sets, budgets και sampling restrictions. Τεκμηρίωση: PDF σελ. 216–220, Sections 4.1–4.2.

4. **Τα controllable factors επιτρέπουν αιτιολογικά καθαρότερα πειράματα.** Purely PCG environments παρέχουν ποικιλία, αλλά δεν επιτρέπουν εύκολη απομόνωση συγκεκριμένων παραγόντων. Ο συνδυασμός PCG και researcher-controlled variation προτείνεται ως καλύτερος σχεδιασμός. Τεκμηρίωση: PDF σελ. 216–223, Sections 4.1–4.3.

5. **Held-out random seeds αποτελούν συχνά ασθενή μορφή generalization test.** Μπορούν να ελέγξουν memorization και robust optimization, αλλά δεν επαρκούν για ισχυρισμούς σχετικά με συγκεκριμένο dynamics ή reward shift. Τεκμηρίωση: PDF σελ. 219–220, Section 4.2.

6. **Reward και dynamics variation είναι υποεκπροσωπημένα σε σχέση με state/observation variation.** Η survey εντοπίζει ότι πολλά benchmarks μεταβάλλουν layout ή rendering, ενώ λιγότερα απομονώνουν dynamics και reward. Τεκμηρίωση: PDF σελ. 217–219, Section 4.1.1.

7. **Η online adaptation είναι συμπληρωματική αλλά όχι zero-shot.** Οι συγγραφείς προτείνουν fast online adaptation ως σημαντική μελλοντική κατεύθυνση για ισχυρότερες μεταβολές, αναγνωρίζοντας ότι χαλαρώνει την zero-shot υπόθεση. Τεκμηρίωση: PDF σελ. 242–243, Sections 6.5–6.6 και Conclusion.

8. **Η γενίκευση χρειάζεται πολλαπλές μετρικές και σαφή protocol reporting.** Test performance, generalization gap, context-efficiency και multidimensional evaluation έχουν διαφορετικό νόημα. Τεκμηρίωση: Sections 3.1, 4.2 και 6.3.

## Υποθέσεις και ορισμοί

Για τη διπλωματική προτείνονται τρία ρητά regimes:

- **Frozen-policy zero-shot robustness:** μετά το training, τα weights και η internal memory επαναφέρονται σε προκαθορισμένη κατάσταση και δεν γίνονται learning updates στο shifted test regime.
- **Online adaptation:** ο agent συνεχίζει να ενημερώνει policy, value function, model ή context representation μετά τη μεταβολή.
- **Recurring-context recall:** το περιβάλλον επιστρέφει σε προηγούμενο context και μετράται εάν η policy ανακαλεί γνώση ή χρειάζεται relearning.

Το evaluation protocol πρέπει επίσης να δηλώνει:

- ποιοι παράγοντες μεταβάλλονται,
- ποιοι συνδυασμοί εμφανίζονται στο training,
- εάν το test είναι interpolation ή extrapolation,
- εάν ο context identifier είναι observable,
- το interaction και update budget μετά τη μεταβολή,
- εάν τα random seeds είναι διαφορετικά από τα train seeds.

## Περιορισμοί και απειλές εγκυρότητας

- Πρόκειται για survey και όχι για empirical proof ότι μία μέθοδος ή benchmark είναι ανώτερο.
- Η zero-shot υπόθεση μπορεί να είναι υπερβολικά αυστηρή για πραγματικά adaptive agents· παραμένει όμως χρήσιμη ως ξεχωριστή baseline capability.
- Το contextual-MDP formalism απαιτεί να οριστεί context space. Σε πραγματικές εφαρμογές οι factors μπορεί να είναι άγνωστοι ή μη παρατηρήσιμοι.
- Η taxonomy δεν εγγυάται ότι ένας συγκεκριμένος train/test split είναι αρκετά δύσκολος.
- Pure PCG μπορεί να είναι χρήσιμο για diversity, αλλά ακατάλληλο για συγκεκριμένους αιτιώδεις ισχυρισμούς.
- Controlled GridWorld factors αυξάνουν την εσωτερική εγκυρότητα, όχι αυτόματα την εξωτερική.
- Generalization gap χωρίς απόλυτο test performance μπορεί να είναι παραπλανητικό: τυχαία κακή policy μπορεί να έχει μικρό gap.
- Η εργασία δεν καλύπτει σε βάθος multi-agent generalization ούτε θεωρητικά bounds.

## Σχέση με άλλες πηγές

- Συμπληρώνει το `SRC-0882A9B2B0`, το οποίο δείχνει empirical overfitting σε training environments. Η παρούσα survey παρέχει ευρύτερη taxonomy και protocol language.
- Περιορίζει την ερμηνεία των `SRC-95C9DAEE68`, `SRC-D14764616F`, `SRC-91D56A10CF` και `SRC-153C917DE1`: οι μέθοδοι αυτές περιλαμβάνουν detection/adaptation/context learning και δεν πρέπει να περιγράφονται ως pure zero-shot.
- Ενισχύει το controlled design που προκύπτει από `SRC-FE2C0A3E00` και `SRC-A3D907D882`: κάθε perturbation πρέπει να είναι ανεξάρτητος factor, όχι απλώς διαφορετικό seed.
- Συνδέεται με το `SRC-0A594EACC0`: recovery curves αφορούν online response και πρέπει να παρουσιάζονται χωριστά από frozen-policy test performance.
- Συμπληρώνει το `SRC-F909CABDEB`, το οποίο καλύπτει continual learning, forgetting και transfer μετά από διαδοχικές αλλαγές.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Θεωρητικό υπόβαθρο, Σχετικές εργασίες, Πειραματικό περιβάλλον, Train/test protocol, Μετρικές, Threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** zero-shot και online adaptation είναι διαφορετικά regimes· benchmark απαιτεί environment και explicit protocol· controllable factors είναι καταλληλότεροι για στοχευμένη scientific evaluation· held-out seeds μόνοι τους δεν τεκμηριώνουν συγκεκριμένη OOD ικανότητα.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι zero-shot είναι η μόνη έγκυρη μορφή robustness· ότι GridWorld εγγυάται real-world generalization· ότι ένα method generalizes γενικά επειδή πέτυχε σε έναν split.
- **Ρόλος:** κύρια μεθοδολογική πηγή.

## Απαιτούμενα αποσπάσματα

1. Αυστηρός ορισμός zero-shot χωρίς test-time training.
2. ZSG ως κλάση προβλημάτων και ανάγκη explicit assumptions.
3. Benchmark ως environment συν evaluation protocol.
4. Pure PCG limitations και πλεονέκτημα controllable factors.
5. Διάκριση held-out seeds από targeted interpolation/extrapolation.
6. Online adaptation ως διαφορετικό, συμπληρωματικό regime.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** το τελικό πειραματικό protocol πρέπει να προεγγράψει frozen-policy και adaptive phases χωριστά και να ορίσει εάν κάθε shift είναι interpolation, extrapolation ή novel combination.
