# SRC-E8CAAF02BE — Planning and Acting in Partially Observable Stochastic Domains

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Leslie Pack Kaelbling, Michael L. Littman, Anthony R. Cassandra
- **Έκδοση:** Artificial Intelligence 101 (1998), 99–134
- **Τύπος:** θεμελιώδης POMDP εργασία
- **Ρόλος στη διπλωματική:** κύρια θεωρητική πηγή για partial observability/context uncertainty

## Αντικείμενο

Η εργασία θεμελιώνει τον σχεδιασμό και τη δράση όταν ο agent δεν παρατηρεί άμεσα το πραγματικό state. Το ιστορικό actions/observations συνοψίζεται σε belief state, δηλαδή probability distribution πάνω στα πιθανά underlying states.

Σε αντίθεση με πλήρως observable MDP, η σωστή policy δεν πρέπει να ενεργεί απλώς πάνω στην πιο πιθανή κατάσταση. Μπορεί να χρειάζεται actions που θυσιάζουν άμεσο reward για να αποκτήσουν πληροφορία.

## Κύρια σημεία

- Το belief state αποτελεί sufficient statistic του observable history για το POMDP formulation.
- Actions μπορούν ταυτόχρονα να αλλάζουν το περιβάλλον και να παρέχουν πληροφορία.
- Η policy ορίζεται πάνω στο belief space και όχι απαραίτητα πάνω στο raw observation.
- Partial observability δημιουργεί διαφορετικό πρόβλημα από stochastic transitions: ο agent είναι αβέβαιος για το current latent state/context.
- Exact POMDP planning είναι υπολογιστικά δύσκολο, άρα finite-memory ή approximate controllers είναι πρακτικές επιλογές.

## Συνάφεια με τη διπλωματική

Η εργασία παρέχει το σωστό theoretical boundary για scenarios όπου ο agent βλέπει corrupted/noisy observations ή όπου το active regime/context δεν δηλώνεται άμεσα.

Πρέπει να διαχωρίζονται:

1. **state observation noise** — η τρέχουσα πραγματική κατάσταση είναι αβέβαιη,
2. **latent regime/context** — η dynamics/reward model identity είναι αβέβαιη,
3. **environmental changepoint** — το underlying model αλλάζει πραγματικά με τον χρόνο.

Ένα belief/context estimator μπορεί να βοηθήσει στα 1–2, αλλά η ύπαρξή του δεν αποδεικνύει από μόνη της detection ή adaptation στο 3.

## Πρωτόκολλο που προκύπτει

Για partially observable scenarios καταγράφονται:

- true state/context όταν είναι διαθέσιμο μόνο στον evaluator,
- agent observation,
- belief/context posterior,
- belief entropy,
- posterior mass στο true state/context,
- information-gathering action count/cost,
- decision quality conditioned on belief accuracy.

Σε changepoint scenario πρέπει να δηλώνεται εάν ο agent γνωρίζει ότι υπάρχουν πολλαπλά candidate contexts ή εάν το νέο regime είναι εκτός της prior model family.

## Περιορισμοί

- Η εργασία αφορά planning με γνωστό model structure και όχι online learning άγνωστων dynamics.
- Exact belief-space methods δεν είναι απαραίτητα κατάλληλοι ως implementation baseline για μικρή resource-aware διπλωματική.
- POMDP uncertainty δεν ισοδυναμεί με non-stationarity.
- Το belief update μπορεί να είναι oracle-like εάν χρησιμοποιεί ακριβή transition/observation models που οι άλλοι agents δεν διαθέτουν.

## Απόφαση

**Επιλογή ως κύρια θεωρητική πηγή.** Χρησιμοποιείται για partial observability, belief-state/context semantics και για fairness controls όταν κάποιος agent διαθέτει explicit probabilistic context model.