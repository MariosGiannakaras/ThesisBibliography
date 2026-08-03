---
κωδικός: SRC-0F8A6588DC
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2203.12117v1"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# NovGrid: A Flexible Grid World for Evaluating Agent Response to Novelty

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Jonathan Balloch, Zhiyu Lin, Mustafa Hussain, Aarun Srinivas, Robert Wright, Xiangyu Peng, Julia Kim, Mark Riedl
- **Έτος:** 2022
- **Τύπος πηγής:** επιστημονική εργασία / benchmark framework
- **DOI / arXiv / URL:** arXiv:2203.12117
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0F8A6588DC.pdf` και `πηγές/SRC-0F8A6588DC.md`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς μπορεί να οριστεί, να εισαχθεί και να αξιολογηθεί ελεγχόμενα η **novelty** σε προβλήματα sequential decision-making. Το βασικό ερώτημα είναι πώς ένα benchmark μπορεί να απομονώνει διαφορετικές αλλαγές στις ιδιότητες ή στους μηχανισμούς ενός περιβάλλοντος και να μετρά όχι μόνο την τελική απόδοση, αλλά και την πτώση και την ταχύτητα ανάκαμψης ενός agent μετά την αλλαγή.

## Σύνοψη

Το NovGrid επεκτείνει το MiniGrid με wrapper εισαγωγής novelty, έντεκα ενδεικτικές μεταβολές και μία ontology που διαχωρίζει αλλαγές σε objects από αλλαγές σε actions, unary από non-unary αλλαγές και barrier, delta ή shortcut αλλαγές ως προς τη μεταβολή της βέλτιστης λύσης. Προτείνει τέσσερις χωριστές μετρικές για τη συμπεριφορά μετά τη novelty: resilience, asymptotic adaptive performance, adaptive efficiency και one-shot adaptive performance. Ένα PPO baseline σε DoorKeyChange χρησιμοποιείται ως ενδεικτική επίδειξη και όχι ως πλήρης συγκριτική μελέτη.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** MiniGrid-compatible GridWorld, με wrapper που αλλάζει world generation και reset behavior μετά από προκαθορισμένο episode εισαγωγής novelty.
- **Μοντέλα / αλγόριθμοι:** PPO με convolutional feature extractor και χωριστά value/policy outputs στην ενδεικτική baseline εκτέλεση.
- **Baselines:** random agent και PPO που μετά την αλλαγή συνεχίζει απλώς την κανονική RL εκπαίδευση χωρίς ειδικό adaptation mechanism.
- **Μετρικές:** resilience, asymptotic adaptive performance, adaptive efficiency, one-shot adaptive performance.
- **Πειραματική διαδικασία:** 6×6 DoorKeyChange περιβάλλον με δύο κλειδιά και μία πόρτα· 500k timesteps πριν από την αλλαγή και επιπλέον 500k timesteps μετά την αλλαγή.

## Κύρια ευρήματα

1. **Η novelty δεν ταυτίζεται με outlier detection, continual learning, domain adaptation ή γενικό transfer learning.** Η εργασία την ορίζει ως αιφνίδια μεταβολή στις ιδιότητες ή στους μηχανισμούς του ίδιου σχετιζόμενου task και αξιολογεί την online απόκριση μετά τη μεταβολή. Τεκμηρίωση: ενότητα *Novelty Background and Related Work*.
2. **Η ontology επιτρέπει ελεγχόμενη παραγοντοποίηση των αλλαγών.** Οι αλλαγές ταξινομούνται σε object/action, unary/non-unary και barrier/delta/shortcut. Τεκμηρίωση: ενότητα *An Ontology of Novelty for Sequential Decision Making* και Table 1.
3. **Το benchmark διατηρεί σταθερά observation και action spaces, αλλά αλλάζει τη σημασία ή τα effects συγκεκριμένων στοιχείων.** Αυτό επιτρέπει πριν/μετά συγκρίσεις χωρίς ασυμβατότητα διαστάσεων. Τεκμηρίωση: ενότητα ontology και ενότητα *Novelty MiniGrid*.
4. **Η αξιολόγηση πρέπει να διαχωρίζει την άμεση υποβάθμιση από την τελική προσαρμογή και το κόστος προσαρμογής.** Οι τέσσερις μετρικές καταγράφουν διαφορετικές ιδιότητες της post-change curve. Τεκμηρίωση: ενότητα *Evaluation and Baseline* και Figure 2.
5. **Το ενδεικτικό PPO baseline παρουσιάζει μεγάλη πτώση και αργή ανάκαμψη.** Αναφέρεται resilience 0.0531, one-shot performance 0.22, σύγκλιση περίπου 300k timesteps μετά την αλλαγή και χαμηλότερη asymptotic reward περίπου 0.8. Τεκμηρίωση: ενότητα *Evaluation and Baseline* και Figure 3.

## Υποθέσεις και ορισμοί

- Η novelty είναι αλλαγή του περιβάλλοντος και όχι αλλαγή του decision-making model του agent.
- Η αποστολή και η εξωτερική reward structure διατηρούνται σταθερές πριν και μετά τη novelty.
- Τα observation και action spaces διατηρούν ίδιο μέγεθος και σχήμα, παρότι οι effects ή οι εμφανιζόμενες καταστάσεις μπορούν να αλλάξουν.
- Barrier novelty δυσκολεύει τη βέλτιστη λύση, shortcut novelty τη διευκολύνει και delta novelty αλλάζει τη λύση χωρίς να αλλάζει το βέλτιστο μήκος της.
- Η resilience metric του NovGrid είναι ειδικός κανονικοποιημένος ορισμός της εργασίας και δεν πρέπει να παρουσιάζεται ως καθολικός ορισμός resilience.

## Περιορισμοί και απειλές εγκυρότητας

- Το πείραμα PPO είναι μία ενδεικτική baseline περίπτωση DoorKeyChange, όχι εκτεταμένη σύγκριση πολλών agents και novelties.
- Οι αριθμητικές τιμές δεν πρέπει να μεταφερθούν ως αναμενόμενη επίδοση σε διαφορετικό GridWorld, reward scale ή training budget.
- Η ontology δεν καλύπτει πλήρως local έναντι global novelty ούτε population/multi-agent διαστάσεις, όπως αναγνωρίζεται στην ενότητα *Future Work*.
- Η εργασία δεν αποδεικνύει ότι η υιοθέτηση ολόκληρου του NovGrid codebase είναι καλύτερη από μία μικρή custom υλοποίηση.
- Η συνέχιση της εκπαίδευσης μετά τη μεταβολή είναι baseline adaptation process, όχι ειδικός resilience algorithm.

## Σχέση με άλλες πηγές

- Συμπληρώνει το `SRC-FE2C0A3E00` (AI Safety Gridworlds) με ελεγχόμενη εισαγωγή dynamic changes και post-change metrics.
- Συνδέεται με `SRC-95C9DAEE68` και `SRC-0A594EACC0`, τα οποία διαχωρίζουν detection, degradation και recovery curves.
- Συμπληρώνει το `SRC-A3D907D882` παρέχοντας GridWorld-specific novelty templates, ενώ το Robust Gymnasium προσφέρει γενικότερη perturbation taxonomy.
- Διαφέρει από το `SRC-3F84F52F97` (CARL): το NovGrid εστιάζει σε αιφνίδια αλλαγή κατά τη διάρκεια της μάθησης, ενώ το CARL κυρίως σε ελεγχόμενες distributions στατικών context instances και generalization.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Σχετικές εργασίες· Πειραματικό περιβάλλον· Taxonomy αβεβαιότητας/μεταβολών· Μετρικές· Μεθοδολογία· Threats to validity
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** ότι ένα μικρό GridWorld μπορεί να φιλοξενήσει ελεγχόμενες object/action και dynamics changes· ότι η post-change αξιολόγηση χρειάζεται χωριστές μετρικές άμεσης πτώσης, ανάκαμψης, τελικής απόδοσης και sample efficiency· ότι η ίδια task interface μπορεί να διατηρηθεί ενώ αλλάζουν οι μηχανισμοί.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι το NovGrid είναι υποχρεωτικό για τη διπλωματική· ότι οι τέσσερις μετρικές είναι οι μοναδικές ή καθολικά αποδεκτές resilience metrics· ότι το PPO ή το NovGrid αποδεικνύουν υπεροχή κάποιου agent.
- **Ρόλος:** κύρια

## Απαιτούμενα αποσπάσματα

- Ontology object/action και barrier/delta/shortcut.
- Σταθερότητα observation/action spaces και μεταβολή effects.
- Τέσσερις post-novelty metrics.
- PPO baseline protocol και περιορισμένη ερμηνεία.
- Αναγνωρισμένα κενά της ontology.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** Να αξιολογηθεί αργότερα η τρέχουσα συντήρηση, άδεια, API συμβατότητα, determinism και κόστος ενσωμάτωσης του actual NovGrid repository πριν ληφθεί απόφαση reuse/adapt/custom.