---
κωδικός: SRC-7EFBF9DA62
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Information Fusion 76 (2021), arXiv:2011.06225"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# A Review of Uncertainty Quantification in Deep Learning: Techniques, Applications and Challenges

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Moloud Abdar, Farhad Pourpanah, Sadiq Hussain, Dana Rezazadegan, Li Liu, Mohammad Ghavamzadeh, Paul Fieguth, Xiaochun Cao, Abbas Khosravi, U. Rajendra Acharya, Vladimir Makarenkov, Saeid Nahavandi
- **Έτος:** 2021
- **Τύπος πηγής:** εκτεταμένη επισκόπηση uncertainty quantification σε deep learning
- **Δημοσίευση:** Information Fusion 76, 243–297
- **arXiv:** 2011.06225
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-7EFBF9DA62.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία χαρτογραφεί τις κυριότερες τεχνικές uncertainty quantification (UQ) σε deep learning, με έμφαση σε Bayesian approximations, ensembles, calibration, prediction intervals και εφαρμογές. Κεντρικό ερώτημα είναι πώς ένα μοντέλο μπορεί να εκφράζει όχι μόνο μία πρόβλεψη αλλά και την αβεβαιότητα της πρόβλεψης με τρόπο χρήσιμο για αποφάσεις.

Για τη διπλωματική, η κύρια συνεισφορά της πηγής είναι η αυστηρή διάκριση ανάμεσα σε aleatoric και epistemic uncertainty. Το πρώτο αφορά εγγενή στοχαστικότητα ή θόρυβο των δεδομένων/περιβάλλοντος και δεν εξαφανίζεται απλώς με περισσότερα δεδομένα. Το δεύτερο αφορά ελλιπή γνώση του μοντέλου και μπορεί, υπό προϋποθέσεις, να μειωθεί με καλύτερη κάλυψη δεδομένων ή posterior learning. Η διάκριση εμποδίζει τη λανθασμένη αντιμετώπιση όλων των perturbations ως ενός ενιαίου «noise level».

## Σύνοψη

Η επισκόπηση παρουσιάζει την predictive uncertainty ως συνδυασμό epistemic και aleatoric συνιστωσών. Αναλύει Bayesian neural networks, variational inference, Monte Carlo dropout, deep ensembles, Gaussian processes, prediction intervals και calibration. Παράλληλα τονίζει ότι η ποιότητα UQ δεν κρίνεται μόνο από accuracy: μια confidence estimate πρέπει να είναι calibrated, να αντιδρά σε out-of-distribution inputs και να μην δημιουργεί ψευδή βεβαιότητα.

Στο RL, η uncertainty μπορεί να χρησιμοποιηθεί για exploration, model-based planning, risk-sensitive decision making, safe RL και detection distribution shift. Ωστόσο, η survey δεν πραγματοποιεί κοινό benchmark των RL μεθόδων και δεν καταλήγει σε μία βέλτιστη τεχνική. Μάλιστα δηλώνει ρητά ότι οι μέθοδοι εφαρμόζονται σε διαφορετικά datasets και tasks, άρα μια συνολική κατάταξη θα ήταν παραπλανητική.

Για την παρούσα εργασία, η πηγή υποστηρίζει ένα modular design: η αβεβαιότητα πρέπει να καταγράφεται ως diagnostic signal ή input του agent, ενώ η πραγματική resilience κρίνεται από το τι κάνει ο agent μετά τη μεταβολή — degradation, detection, adaptation και recovery. Μία υψηλή uncertainty score χωρίς αποτελεσματική απόκριση δεν αποτελεί ανθεκτικότητα.

## Μεθοδολογία

- **Μορφή μελέτης:** narrative/comprehensive review ευρέος πεδίου.
- **Βασική ταξινομία:** aleatoric έναντι epistemic uncertainty· homoscedastic έναντι heteroscedastic aleatoric uncertainty.
- **Μέθοδοι:** Bayesian neural networks, variational inference, MC dropout, ensembles, Gaussian processes, evidential/probabilistic models, calibration και prediction intervals.
- **Πεδία εφαρμογής:** computer vision, medical imaging, NLP, signal processing, reinforcement learning και άλλα.
- **Κριτήρια που συζητούνται:** uncertainty quality, calibration, reliability, OOD behavior, computational cost και data/code availability.
- **Όριο μελέτης:** δεν εκτελείται ενιαίο empirical comparison όλων των UQ methods.

## Κύρια ευρήματα

1. **Η aleatoric και η epistemic uncertainty έχουν διαφορετική αιτία και διαφορετική ερμηνεία.** Η aleatoric αποδίδεται στην εγγενή μεταβλητότητα/θόρυβο των δεδομένων, ενώ η epistemic σε ανεπαρκή γνώση, περιορισμένα δεδομένα ή model uncertainty. Τεκμηρίωση: PDF σελ. 1–3, Introduction και Figure 1.

2. **Η predictive uncertainty δεν είναι απλό confidence score.** Η Section 2.2 διατυπώνει την predictive uncertainty ως συνδυασμό epistemic και aleatoric συνιστωσών και συνδέει την epistemic uncertainty με posterior distribution πάνω στις παραμέτρους. Τεκμηρίωση: PDF σελ. 4–6, Section 2.2, Equations (4)–(12).

3. **Bayesian approximations και ensembles είναι δημοφιλή αλλά όχι δωρεάν.** MC dropout, variational inference και deep ensembles προσφέρουν πρακτικές προσεγγίσεις, με trade-offs σε computational overhead, memory, approximation quality και calibration. Τεκμηρίωση: Sections 2–7.

4. **Η confidence χρειάζεται calibration και OOD testing.** Υψηλή softmax πιθανότητα ή χαμηλή variance εντός training distribution δεν αποδεικνύει αξιόπιστη uncertainty σε shifted data. Η survey αναγνωρίζει calibration και OOD uncertainty ως ανοιχτές περιοχές. Τεκμηρίωση: Introduction, Sections 7 και 9.1.

5. **Η UQ μπορεί να βοηθήσει exploration, safe RL και adaptation, αλλά δεν είναι από μόνη της policy.** Η βιβλιογραφική σύνθεση περιλαμβάνει uncertainty-driven exploration, risk-sensitive RL, model uncertainty και safe RL, χωρίς να δείχνει ότι μία uncertainty estimate εγγυάται σωστή απόφαση. Τεκμηρίωση: RL-related discussion και references 186–200, καθώς και Section 9.1.

6. **Η ίδια η survey δεν δικαιολογεί καθολική κατάταξη μεθόδων.** Οι συγγραφείς δηλώνουν ότι η σύγκριση όλων των UQ methods είναι εκτός scope επειδή σχεδιάστηκαν για διαφορετικά δεδομένα και tasks. Τεκμηρίωση: PDF σελ. 3–4, Section 1.1.

7. **Θεωρία, causal modeling, imperfect data και computational cost παραμένουν βασικά κενά.** Η UQ μπορεί να παράγει παραπλανητική βεβαιότητα αν το posterior approximation, το data model ή το calibration protocol είναι ανεπαρκή. Τεκμηρίωση: PDF σελ. 2–3, Introduction, και Section 9.1.

## Υποθέσεις και ορισμοί

Για τη διπλωματική προτείνεται η ακόλουθη αντιστοίχιση:

- **Aleatoric uncertainty:** stochastic transition/action failure, reward noise, observation corruption ή άλλο randomness που παραμένει ακόμη και αν το μοντέλο είναι γνωστό.
- **Epistemic uncertainty:** άγνωστος νέος κανόνας, ανεπαρκής εμπειρία σε νέο regime, αβεβαιότητα για transition/reward parameters ή OOD state.
- **Predictive uncertainty:** συνολική αβεβαιότητα πρόβλεψης, η οποία μπορεί να περιλαμβάνει και τις δύο παραπάνω συνιστώσες.
- **Calibration:** αντιστοίχιση δηλωμένης confidence με εμπειρική συχνότητα ορθότητας ή κάλυψης.

Η ταξινομία αφορά την πηγή της αβεβαιότητας, όχι αυτόματα το είδος της resilience mechanism. Το ίδιο perturbation μπορεί να είναι aleatoric για έναν agent που γνωρίζει το distribution και epistemic για agent που δεν το γνωρίζει.

## Περιορισμοί και απειλές εγκυρότητας

- Η survey καλύπτει εξαιρετικά ετερογενή πεδία, άρα πολλά συμπεράσματα είναι ταξινομικά και όχι task-specific.
- Η RL κάλυψη είναι μικρότερο μέρος της συνολικής εργασίας και δεν συνιστά systematic RL benchmark.
- Οι όροι uncertainty, confidence, risk και OOD score δεν είναι εναλλάξιμοι.
- MC dropout ή ensemble disagreement δεν αποτελεί ground truth epistemic uncertainty.
- Η decomposition σε aleatoric/epistemic εξαρτάται από το μοντέλο και μπορεί να μην είναι identifiable στην πράξη.
- UQ quality πρέπει να αξιολογηθεί με calibration ή decision utility, όχι μόνο με visually plausible uncertainty maps.
- Η εργασία προηγείται αρκετών νεότερων UQ methods· χρησιμοποιείται για θεμελιώδη ταξινομία, όχι για ισχυρισμό state of the art το 2026.

## Σχέση με άλλες πηγές

- Ερμηνεύει τις perturbation categories του `SRC-A3D907D882`: observation/reward/action noise είναι κυρίως aleatoric test factors, ενώ unseen rule/dynamics shifts δημιουργούν epistemic uncertainty.
- Συμπληρώνει το `SRC-3856071502`, όπου η posterior distribution του run length είναι συγκεκριμένη μορφή uncertainty για change detection.
- Συνδέεται με το `SRC-0AEF7EF16A`, το οποίο χρησιμοποιεί Bayesian uncertainty σε robust RL.
- Περιορίζει το `SRC-95C9DAEE68`: η ανίχνευση change point και η policy adaptation δεν πρέπει να αξιολογούνται μόνο από ένα uncertainty signal αλλά και από detection accuracy και recovery.
- Συμπληρώνει το `SRC-153C917DE1`, όπου contextual signals προσαρμόζουν exploration, αλλά δεν εγγυώνται calibrated epistemic uncertainty.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Θεωρητικό υπόβαθρο, Μοντέλο αβεβαιότητας, Σχετικές εργασίες, Πειραματικό πρωτόκολλο, Threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** aleatoric και epistemic uncertainty είναι διακριτές· uncertainty estimates χρειάζονται calibration/OOD evaluation· Bayesian approximations και ensembles έχουν πρακτικά trade-offs· uncertainty signal δεν ισοδυναμεί με resilience.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι MC dropout ή ensembles είναι η καλύτερη λύση για το συγκεκριμένο GridWorld· ότι η decomposition είναι πάντα ακριβής· ότι μία υψηλή uncertainty score αποδεικνύει detection ή recovery.
- **Ρόλος:** υποστηρικτική θεωρητική πηγή.

## Απαιτούμενα αποσπάσματα

1. Ορισμός aleatoric και epistemic uncertainty.
2. Predictive uncertainty decomposition και Bayesian posterior predictive.
3. Περιορισμός καθολικής σύγκρισης UQ methods.
4. Calibration/OOD και computational challenges.
5. Χρήση UQ σε sequential decision making χωρίς ταύτιση με policy quality.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** η τελική υλοποίηση uncertainty-aware baseline πρέπει να επιλεγεί μετά από feasibility pilot και να συνοδεύεται από calibration/decision-quality test, όχι μόνο από raw variance.
