---
κωδικός: SRC-702F9AB94C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Block Contextual MDPs for Continual Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητες 1 και 3, Definitions 1–3
- **Ισχυρισμός:** Structured non-stationarity μπορεί να αναπαρασταθεί ως latent context που μεταβάλλει rewards, dynamics και observations σε κοινή task family.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο
- **Θέματα:** contextual MDP; hidden context; task family
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το BC-MDP ορίζει context που χαρτογραφείται σε reward function, transition kernel και observation space, ενώ η continual setting δεν παρέχει ρητά task boundaries όταν το context αλλάζει.

### Συμφραζόμενα

Η εργασία προσθέτει Lipschitz smoothness ώστε κοντινά contexts να αντιστοιχούν σε κοντινές task dynamics/rewards.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το πλαίσιο αφορά related tasks με κοινή δομή και όχι arbitrary αλλαγές state/action space.

### Προτεινόμενη χρήση

Ορισμός structured/latent-context non-stationarity.

### Παραπομπή

Sodhani et al., 2022, §§1, 3, Defs. 1–3.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 4, Assumption 1 και Theorem 2
- **Ισχυρισμός:** Η θεωρητική generalization απαιτεί νέο context που είναι αναγνωρίσιμο από περιορισμένο interaction history και κοντά σε known contexts.
- **Κεφάλαιο:** Υποθέσεις· Threats to validity
- **Θέματα:** identifiability; context distance; generalization bound
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Υποτίθεται ότι context encoder μπορεί, από `k` transition tuples, να παράγει εκτίμηση κοντά στο πραγματικό context· το policy-value error αυξάνεται με context approximation και task distance.

### Συμφραζόμενα

Η απόσταση ορίζεται μέσω reward differences και transition-distribution distances.

### Περιορισμοί και κίνδυνος παρερμηνείας

Μία αλλαγή που δεν επηρεάζει άμεσα τα παρατηρούμενα transitions ή δεν είναι identifiable δεν καλύπτεται από το guarantee.

### Προτεινόμενη χρήση

Ρητή καταγραφή assumptions για context-conditioned baselines.

### Παραπομπή

Sodhani et al., 2022, §4, Assumption 1, Theorem 2.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 5 και Figure 1
- **Ισχυρισμός:** Zero-shot adaptation του ZeUS είναι history-conditioned context inference χωρίς gradient update.
- **Κεφάλαιο:** Agent taxonomy· Πειραματικό πρωτόκολλο
- **Θέματα:** zero-shot adaptation; context inference; no parameter update
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Κατά την εκτέλεση, ο context encoder συνοψίζει τα τελευταία `k` interactions και η policy conditionάρεται στο inferred context, χωρίς ενημέρωση parameters στο νέο task.

### Συμφραζόμενα

Η representation και η policy έχουν εκπαιδευτεί προηγουμένως σε task family.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να παρουσιαστεί ως post-change learning ή ως απόδειξη ότι ο agent ανακτά μέσω νέας γνώσης.

### Προτεινόμενη χρήση

Διάκριση frozen policy, context inference και online updating.

### Παραπομπή

Sodhani et al., 2022, §5, Fig. 1.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητες 6.1–6.3, Figures 2–3
- **Ισχυρισμός:** Train/test context ranges και interpolation/extrapolation πρέπει να αναφέρονται χωριστά.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** interpolation; extrapolation; dynamics shift; reward shift
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Για dynamics, η εργασία αξιολογεί held-out contexts μέσα και έξω από το training parameter range· για rewards, τα test parameters προέρχονται από το ίδιο range με την εκπαίδευση.

### Συμφραζόμενα

Τα αποτελέσματα αναφέρονται σε 10 seeds με mean και standard error.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η επιτυχία στα reward experiments δεν αποτελεί evidence για reward extrapolation.

### Προτεινόμενη χρήση

Υποχρεωτική σήμανση `interpolation`, `extrapolation` και `novel structural change`.

### Παραπομπή

Sodhani et al., 2022, §§6.1–6.3, Figs. 2–3.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητες 6.3–6.4, Figures 2–4
- **Ισχυρισμός:** Το context-learning objective βελτιώνει τόσο reported return όσο και τη γεωμετρική οργάνωση των learned contexts.
- **Κεφάλαιο:** Σχετικές εργασίες
- **Θέματα:** context loss; representation; ablation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το ZeUS υπερέχει του no-context-loss ablation στα held-out tasks, ενώ η correlation learned και true context distances είναι `0.60` με context loss έναντι `0.23` χωρίς αυτό.

### Συμφραζόμενα

Η συσχέτιση αναφέρεται στο Cheetah torso-length task family.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η συγκεκριμένη correlation δεν αποδεικνύει causal representation ούτε γενικεύεται σε arbitrary environments.

### Προτεινόμενη χρήση

Evidence ότι context representations πρέπει να ελέγχονται με ablations και task geometry.

### Παραπομπή

Sodhani et al., 2022, §§6.3–6.4, Figs. 2–4.

## Τεκμήριο E6

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 7, Figure 5
- **Ισχυρισμός:** Ακόμη και structured context methods υποβαθμίζονται όταν το evaluation context απομακρύνεται από την training distribution.
- **Κεφάλαιο:** Threats to validity· Μετρικές
- **Θέματα:** OOD distance; degradation; dense reward
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η επίδοση του ZeUS μειώνεται καθώς το target velocity κινείται μακρύτερα από το training range, και η μέθοδος βασίζεται εμπειρικά σε dense reward για να διακρίνει tasks.

### Συμφραζόμενα

Το paper αναγνωρίζει ρητά ότι οι guarantees αφορούν contexts κοντά σε seen contexts.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν υποστηρίζει open-ended adaptation σε απεριόριστα ή structurally novel regimes.

### Προτεινόμενη χρήση

Αναφορά performance ως συνάρτηση context distance και reward observability.

### Παραπομπή

Sodhani et al., 2022, §7, Fig. 5.
