---
κωδικός: SRC-0A4AFAC8E9
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "NeurIPS 2021, arXiv:2108.13264"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-30"
---

# Deep Reinforcement Learning at the Edge of the Statistical Precipice

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc G. Bellemare
- **Έτος:** 2021
- **Τύπος πηγής:** πρωτογενής μεθοδολογική και μετα-εμπειρική εργασία για RL evaluation
- **DOI / arXiv / URL:** arXiv:2108.13264 — NeurIPS 2021 Outstanding Paper
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0A4AFAC8E9.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς μπορούν να γίνουν αξιόπιστες συγκρίσεις deep-RL algorithms όταν το υπολογιστικό κόστος επιτρέπει μόνο λίγα independent runs. Το κεντρικό ερώτημα είναι αν τα συνηθισμένα point estimates, όπως mean ή median score, αρκούν για να υποστηρίξουν ισχυρισμούς υπεροχής και ποιες εναλλακτικές στατιστικές αναφορές μειώνουν την πιθανότητα παραπλανητικών συμπερασμάτων.

Η πηγή είναι κεντρική για το πειραματικό πρωτόκολλο της διπλωματικής. Η σύγκριση resilience algorithms θα περιλαμβάνει stochastic training, διαφορετικά seeds, πολλαπλές perturbation conditions και πιθανώς μικρό αριθμό runs λόγω hardware. Επομένως πρέπει να αναφέρονται uncertainty intervals και effect sizes, όχι μόνο μία μέση καμπύλη ή ένα καλύτερο run.

## Σύνοψη

Οι συγγραφείς επανεξετάζουν δημοσιευμένες συγκρίσεις στα Atari 100k, ALE, Procgen και DeepMind Control Suite. Δείχνουν ότι μικρά samples runs, heavy-tailed distributions, outliers και ασυνεπείς evaluation protocols μπορούν να αντιστρέψουν ή να αποδυναμώσουν ισχυρισμούς για state-of-the-art performance. Προτείνουν stratified bootstrap confidence intervals, performance profiles, interquartile mean (IQM), probability of improvement και optimality gap.

Η βασική αρχή είναι ότι κάθε aggregate score από πεπερασμένο αριθμό runs είναι random variable. Η στατιστική αβεβαιότητα πρέπει να εμφανίζεται ρητά, ενώ τα raw per-run results πρέπει να διατηρούνται ώστε να μπορούν να επανεξεταστούν. Η εργασία αποθαρρύνει dichotomous significance testing και προτιμά confidence intervals και πρακτικά effect sizes.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** δημοσιευμένα και επανεκτελεσμένα αποτελέσματα από Atari 100k, ALE 200M, Procgen και DeepMind Control Suite.
- **Μοντέλα / αλγόριθμοι:** πολλοί υφιστάμενοι deep-RL algorithms· η πηγή δεν προτείνει agent αλλά evaluation toolkit.
- **Baselines:** published point estimates και μη τυποποιημένα protocols συγκρίνονται με bootstrap-based reanalysis.
- **Μετρικές:** stratified bootstrap CIs, IQM, median/mean, performance profiles, probability of improvement, optimality gap και rank distributions.
- **Πειραματική διαδικασία:** resampling πραγματικών per-run scores, subsampling διαφορετικού αριθμού runs, σύγκριση evaluation protocols και ανακατασκευή uncertainty-aware rankings.

## Κύρια ευρήματα

1. **Τα λίγα runs μπορούν να παράγουν μεγάλη αβεβαιότητα ακόμη και σε aggregate metrics.** Στο Atari 100k η median μπορεί να παραμένει ασταθής ακόμη και με δεκάδες runs, ενώ 3–10 runs είναι συνηθισμένα λόγω κόστους. Τεκμηρίωση: σελ. 1–5, Sections 1–3 και Figures 1–4.
2. **Τα point estimates μπορούν να αλλάξουν το συμπέρασμα μιας σύγκρισης.** Δημοσιευμένες διαφορές συχνά δεν παραμένουν σαφείς όταν εμφανίζονται CIs ή score distributions. Τεκμηρίωση: σελ. 4–10, Sections 3–5.
3. **Το IQM είναι συχνά καταλληλότερο aggregate από mean ή median.** Αγνοεί το χαμηλότερο και υψηλότερο τεταρτημόριο, είναι ανθεκτικότερο σε outliers από mean και στατιστικά αποδοτικότερο από median στο few-run regime. Τεκμηρίωση: σελ. 2–3 και 6–7, Table 1 και Section 4.3.
4. **Η συνέπεια του evaluation protocol είναι απαραίτητη.** Τελική επίδοση, μέγιστη επίδοση κατά την εκπαίδευση και καλύτερο run δεν είναι άμεσα συγκρίσιμες ποσότητες. Τεκμηρίωση: σελ. 5, Section 3.
5. **Η πιθανότητα βελτίωσης είναι πιο ειλικρινής από δυαδικό claim υπεροχής.** Μπορεί να δείξει ότι μια δημοσιευμένη «βελτίωση» έχει μόνο οριακή πιθανότητα να επαναληφθεί σε νέα runs. Τεκμηρίωση: σελ. 8–10, Sections 4–5 και Figure 12.
6. **Το fixing seeds δεν λύνει την αναπαραγωγιμότητα.** Στόχος είναι η απόδοση σε νέες τυχαίες συνθήκες, όχι η αναπαραγωγή ενός ευνοϊκού συγκεκριμένου seed. Τεκμηρίωση: σελ. 10, Section 6.
7. **Τα p-values δεν πρέπει να αντικαθιστούν effect sizes και uncertainty.** Η εργασία προτείνει CIs για plausible effect sizes και αποφεύγει binary significance claims. Τεκμηρίωση: σελ. 3, Remark στη Section 2.

## Υποθέσεις και ορισμοί

Ένα run είναι ανεξάρτητη εκτέλεση του πλήρους training/evaluation pipeline και δεν ταυτίζεται κατ’ ανάγκη με απλή αλλαγή fixed seed, επειδή GPU/framework nondeterminism και άλλες πηγές τυχαιότητας μπορεί να παραμένουν. Τα normalized scores χρειάζονται κοινά reference points και το aggregation πρέπει να σέβεται τη δομή tasks × runs.

Για τη διπλωματική, κάθε combination agent × perturbation scenario × severity θα πρέπει να έχει προκαθορισμένα independent runs, raw results και κοινό evaluation checkpoint. Οι temporal resilience metrics μπορούν να αναλυθούν ανά run και να συνοψιστούν με bootstrap CIs, χωρίς να συμπιεστούν όλα σε έναν μη ερμηνεύσιμο scalar.

## Περιορισμοί και απειλές εγκυρότητας

Η εργασία επικεντρώνεται κυρίως σε benchmark suites με πολλά tasks, ενώ η διπλωματική πιθανόν να έχει ένα configurable GridWorld με πολλά scenarios. Το IQM across tasks δεν μεταφέρεται μηχανικά όταν υπάρχει μόνο ένα task· μπορεί όμως να εφαρμοστεί σε pooled standardized scenario-run scores με σαφή ορισμό ή να αντικατασταθεί από per-scenario distributions. Το bootstrap δεν διορθώνει biased design, dependent runs, cherry-picked hyperparameters ή data leakage. Τα proposed tools δεν καθορίζουν τον απαιτούμενο αριθμό runs για κάθε effect size· χρειάζεται pilot-based precision/power planning. Τέλος, CIs από πολύ μικρά samples μπορεί να είναι ευρέα ή ευαίσθητα στις assumptions του resampling.

## Σχέση με άλλες πηγές

Το `SRC-95C9DAEE68` προτείνει reward curves, F1 detection και multiple seeds σε non-stationary RL, ενώ η παρούσα πηγή καθορίζει πώς πρέπει να αναφέρεται η αβεβαιότητά τους. Το `SRC-0882A9B2B0` παρέχει controlled train/test generalization scenarios. Το `SRC-F909CABDEB` προσθέτει continual metrics όπως forgetting και forward transfer.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** πειραματικό πρωτόκολλο, στατιστική ανάλυση, αναπαραγωγιμότητα, threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** λίγα stochastic runs δεν δικαιολογούν point-estimate claims· πρέπει να αναφέρονται intervals και per-run distributions· evaluation protocols πρέπει να είναι ίδια για όλους τους agents.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι IQM είναι πάντοτε η μοναδική σωστή μετρική, ότι bootstrap λύνει όλες τις μορφές bias ή ότι συγκεκριμένος αριθμός seeds είναι καθολικά επαρκής.
- **Ρόλος:** κύρια

## Απαιτούμενα αποσπάσματα

Καταγράφηκαν τεκμήρια για few-run uncertainty, bootstrap CIs, IQM, protocol consistency, probability of improvement και seed limitations.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** μετά τα pilot runs να επιλεγεί αριθμός repetitions με βάση επιθυμητό CI width και να καθοριστεί αν aggregation θα γίνεται ανά scenario, severity ή συνολικό suite.