---
κωδικός: SRC-0A4AFAC8E9
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-30"
---

# Αποσπάσματα — Deep Reinforcement Learning at the Edge of the Statistical Precipice

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 1–3, Abstract, Section 1 και Table 1
- **Ισχυρισμός:** Η σύγκριση stochastic RL algorithms με λίγα runs δεν πρέπει να βασίζεται μόνο σε mean ή median point estimates.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο και στατιστική ανάλυση
- **Θέματα:** few-run evaluation, uncertainty, reproducibility
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι aggregate επιδόσεις από πεπερασμένα independent runs είναι τυχαίες μεταβλητές. Στο deep RL, όπου 3–10 runs είναι συνηθισμένα και η διακύμανση συχνά μεγάλη, ένα point estimate μπορεί να υπερεκτιμά ή να υποεκτιμά ουσιαστικά την αναμενόμενη επίδοση. Οι συγγραφείς προτείνουν να συνοδεύονται οι συγκρίσεις από uncertainty intervals και distributions.

### Συμφραζόμενα

Το πρόβλημα αφορά ιδιαίτερα ακριβά benchmarks, αλλά ισχύει και σε μικρότερο GridWorld όταν οι learning curves, exploration και perturbations είναι stochastic.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν συνεπάγεται ότι λίγα runs είναι άχρηστα. Σημαίνει ότι τα συμπεράσματα πρέπει να είναι ανάλογα με το πλάτος της αβεβαιότητας.

### Προτεινόμενη χρήση

Να απαγορεύσει claims υπεροχής από ένα seed ή από μόνο μία μέση τιμή.

### Παραπομπή

Agarwal et al. (2021), σελ. 1–3, Abstract, Section 1 και Table 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 5–7, Section 4.1 και Table 1
- **Ισχυρισμός:** Τα aggregate scores πρέπει να συνοδεύονται από stratified bootstrap confidence intervals που resample tasks και runs με τρόπο συμβατό με τη δομή του benchmark.
- **Κεφάλαιο:** Στατιστική μεθοδολογία
- **Θέματα:** bootstrap confidence intervals, effect uncertainty
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η προτεινόμενη διαδικασία χρησιμοποιεί stratified bootstrap ώστε η resampling distribution να διατηρεί τη διάκριση μεταξύ tasks και runs. Το interval εκφράζει plausible values του aggregate performance και επιτρέπει πιο προσεκτική σύγκριση από μια μοναδική τιμή. Για διαφορές agents πρέπει να υπολογίζεται uncertainty της διαφοράς και όχι να ερμηνεύεται μηχανικά η επικάλυψη δύο ανεξάρτητων intervals.

### Συμφραζόμενα

Στη διπλωματική τα strata μπορούν να είναι perturbation scenarios ή severity levels, εφόσον οριστούν πριν από την ανάλυση.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το bootstrap προϋποθέτει κατάλληλη ανεξαρτησία και αντιπροσωπευτικότητα των runs. Δεν διορθώνει cherry-picking ή unequal tuning budgets.

### Προτεινόμενη χρήση

Να εφαρμοστεί σε primary outcome metrics και pairwise agent differences.

### Παραπομπή

Agarwal et al. (2021), σελ. 5–7, Section 4.1.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 2–3 και 6–8, Table 1 και Section 4.3
- **Ισχυρισμός:** Το interquartile mean είναι χρήσιμο robust aggregate επειδή περιορίζει την επίδραση outliers και είναι συχνά πιο στατιστικά αποδοτικό από τη median.
- **Κεφάλαιο:** Μετρικές και reporting
- **Θέματα:** IQM, aggregate metrics, outliers
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το IQM υπολογίζει τον μέσο όρο του μεσαίου 50% των pooled normalized scores. Σε benchmark comparisons είναι λιγότερο ευάλωτο σε λίγα εξαιρετικά tasks από τον mean και παρουσιάζει στενότερη sampling uncertainty από τη median στο few-run regime. Οι συγγραφείς το προτείνουν μαζί με άλλα summaries, όχι ως μοναδική περιγραφή.

### Συμφραζόμενα

Σε ένα configurable environment, IQM έχει νόημα μόνο αν τα scenario scores κανονικοποιηθούν συγκρίσιμα. Per-scenario medians και distributions παραμένουν απαραίτητα.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η απόρριψη tails μπορεί να κρύψει σπάνιες καταστροφικές αποτυχίες, οι οποίες είναι σημαντικές για resilience. Αυτές πρέπει να αναφέρονται χωριστά.

### Προτεινόμενη χρήση

Να χρησιμοποιηθεί ως secondary aggregate, μαζί με worst-case/tail και failure-rate metrics.

### Παραπομπή

Agarwal et al. (2021), Table 1 και Section 4.3.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδα 5, Section 3, συζήτηση evaluation protocols
- **Ισχυρισμός:** Αποτελέσματα από διαφορετικούς evaluation rules, όπως final performance και maximum performance during training, δεν είναι άμεσα συγκρίσιμα.
- **Κεφάλαιο:** Αναπαραγωγιμότητα και πρωτόκολλο
- **Θέματα:** protocol consistency, checkpoint selection, bias
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η εργασία δείχνει ότι η χρήση maximum score κατά την εκπαίδευση μπορεί να παράγει αισιόδοξες τιμές σε σχέση με την average final performance. Διαφορές protocol μεγαλύτερες από τις διαφορές algorithms μπορούν να ανατρέψουν ranking. Συνεπώς όλοι οι agents πρέπει να αξιολογούνται στα ίδια checkpoints, με ίδια episode budgets και ίδιο aggregation rule.

### Συμφραζόμενα

Η επιλογή «καλύτερου checkpoint» μπορεί να επιτρέπεται μόνο με κοινό validation procedure που δεν κοιτάζει το test result.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν υπάρχει ένας καθολικός σωστός checkpoint rule· απαιτείται συνέπεια και προεγγραφή.

### Προτεινόμενη χρήση

Να κλειδώσει το stopping/evaluation protocol πριν από τα τελικά runs.

### Παραπομπή

Agarwal et al. (2021), σελ. 5, Section 3.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 9–10, Sections 5–6
- **Ισχυρισμός:** Το fixing συγκεκριμένων seeds δεν αποδεικνύει ότι ένας agent θα αποδώσει καλά σε νέες τυχαίες συνθήκες.
- **Κεφάλαιο:** Αναπαραγωγιμότητα και limitations
- **Θέματα:** seeds, independent runs, generalizability of results
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς τονίζουν ότι fixed seeds μπορεί να ωφελούν άνισα διαφορετικούς algorithms και δεν απαντούν στο ερώτημα αν το αποτέλεσμα θα επαναληφθεί με νέες random conditions. Επιπλέον, ένα run μπορεί να περιλαμβάνει randomness που δεν ελέγχεται πλήρως από ένα seed, όπως framework ή hardware nondeterminism.

### Συμφραζόμενα

Για reproducibility πρέπει να αποθηκεύονται seeds και configurations, αλλά για statistical reliability χρειάζονται πολλαπλές ανεξάρτητες εκτελέσεις.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να εγκαταλειφθεί το seed logging. Είναι απαραίτητο για debugging και exact replay, αλλά όχι επαρκές για επιστημονική γενίκευση.

### Προτεινόμενη χρήση

Να τεκμηριώσει χωριστά deterministic replay και statistical replication.

### Παραπομπή

Agarwal et al. (2021), σελ. 9–10, Sections 5–6.