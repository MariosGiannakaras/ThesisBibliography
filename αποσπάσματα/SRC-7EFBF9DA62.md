---
κωδικός: SRC-7EFBF9DA62
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — A Review of Uncertainty Quantification in Deep Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 1–3, Introduction και Figure 1
- **Ισχυρισμός:** Η aleatoric uncertainty προέρχεται από εγγενή μεταβλητότητα των δεδομένων, ενώ η epistemic uncertainty από ανεπαρκή γνώση ή κάλυψη του μοντέλου.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο; Μοντέλο αβεβαιότητας
- **Θέματα:** aleatoric uncertainty; epistemic uncertainty; noise; model uncertainty
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η πηγή διακρίνει δύο κύριες πηγές αβεβαιότητας. Η aleatoric uncertainty είναι ιδιότητα της στοχαστικότητας ή του θορύβου του data-generating process και θεωρείται μη αναγώγιμη μόνο με περισσότερα παρόμοια δεδομένα. Η epistemic uncertainty οφείλεται σε ελλιπή γνώση, περιορισμένη κάλυψη ή αβεβαιότητα για τις παραμέτρους του μοντέλου και μπορεί να μειωθεί με κατάλληλη πληροφορία.

### Συμφραζόμενα

Η διάκριση εισάγεται ως εννοιολογική βάση για τις τεχνικές UQ που ακολουθούν.

### Περιορισμοί και κίνδυνος παρερμηνείας

Στην πράξη η decomposition εξαρτάται από το μοντέλο. Δεν είναι πάντοτε δυνατό να αποδοθεί κάθε observed variance αποκλειστικά στη μία κατηγορία.

### Προτεινόμενη χρήση

Να χρησιμοποιηθεί για να ταξινομηθούν ξεχωριστά stochastic action/reward noise και uncertainty από unseen regimes.

### Παραπομπή

Abdar et al., Introduction and Figure 1, PDF σελ. 1–3.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 4–6, Section 2.2, Equations (4)–(12)
- **Ισχυρισμός:** Η predictive uncertainty συντίθεται από aleatoric και epistemic συνιστώσες και η Bayesian προσέγγιση χρησιμοποιεί posterior distribution πάνω στις παραμέτρους.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο; Μεθοδολογία
- **Θέματα:** predictive uncertainty; posterior predictive; variational inference; MC dropout
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η Section 2.2 γράφει την predictive uncertainty ως άθροισμα epistemic και aleatoric uncertainty. Για την epistemic συνιστώσα, η Bayesian formulation τοποθετεί distribution πάνω στις παραμέτρους και ολοκληρώνει την likelihood ως προς το posterior. Επειδή το ακριβές posterior συνήθως δεν είναι tractable, χρησιμοποιούνται approximations όπως variational inference και dropout-based inference.

### Συμφραζόμενα

Οι εξισώσεις παρουσιάζουν γενικό supervised predictive setting και όχι ειδικά MDP ή RL policy.

### Περιορισμοί και κίνδυνος παρερμηνείας

Approximate posterior δεν είναι ground-truth uncertainty. Η ποιότητα εξαρτάται από prior, variational family, optimization και data coverage.

### Προτεινόμενη χρήση

Να θεμελιώσει γιατί uncertainty-aware agent χρειάζεται σαφή estimator specification και validation.

### Παραπομπή

Abdar et al., Section 2.2, Equations (4)–(12), PDF σελ. 4–6.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 3–4, Section 1.1, Research Objectives and Outline
- **Ισχυρισμός:** Δεν είναι επιστημονικά έγκυρη μια καθολική κατάταξη UQ methods όταν έχουν σχεδιαστεί για διαφορετικά datasets και tasks.
- **Κεφάλαιο:** Σχετικές εργασίες; Threats to validity
- **Θέματα:** method comparison; task dependence; evidence limits
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς δηλώνουν ότι ο στόχος της review δεν είναι να συγκρίνει συνολικά την απόδοση όλων των UQ methods, επειδή οι τεχνικές έχουν προταθεί για διαφορετικά δεδομένα και ειδικές εργασίες. Η εργασία οργανώνει το πεδίο και τα κενά, αλλά δεν παρέχει universal winner.

### Συμφραζόμενα

Το σημείο αποτελεί ρητό scope limitation της ίδιας της survey.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν μπορεί να χρησιμοποιηθεί για επιλογή MC dropout, ensemble ή Bayesian network χωρίς task-specific pilot.

### Προτεινόμενη χρήση

Να δικαιολογήσει feasibility comparison μικρού αριθμού uncertainty estimators στο συγκεκριμένο environment.

### Παραπομπή

Abdar et al., Section 1.1, PDF σελ. 3–4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 2–3, Introduction; Section 9.1, Future Directions
- **Ισχυρισμός:** Η αξιοπιστία UQ περιορίζεται από ανεπαρκή θεωρία, imperfect data, calibration και computational cost.
- **Κεφάλαιο:** Περιορισμοί; Threats to validity
- **Θέματα:** calibration; imperfect data; computational overhead; theory gap
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η review αναγνωρίζει ως επαναλαμβανόμενες δυσκολίες την απουσία πλήρους θεωρίας και causal models, την ευαισθησία σε ατελή δεδομένα και το υπολογιστικό κόστος. Στις future directions επισημαίνει την ανάγκη για calibration, πιο ανθεκτική inference, sampling-free ή αποδοτικές προσεγγίσεις και καλύτερο OOD behavior.

### Συμφραζόμενα

Οι παρατηρήσεις καλύπτουν πολλά πεδία εφαρμογής και δεν είναι αποκλειστικά RL-specific.

### Περιορισμοί και κίνδυνος παρερμηνείας

Μια uncertainty method δεν πρέπει να κριθεί μόνο από runtime ή μόνο από in-distribution accuracy.

### Προτεινόμενη χρήση

Να συμπεριληφθούν calibration error, computational overhead και failure cases στην αξιολόγηση οποιουδήποτε uncertainty-aware baseline.

### Παραπομπή

Abdar et al., Introduction, PDF σελ. 2–3, και Section 9.1.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** RL-related synthesis και references 186–200; Section 9.1, Further directions
- **Ισχυρισμός:** Η uncertainty estimation μπορεί να υποστηρίξει exploration, risk-sensitive ή safe decision making, αλλά δεν αποτελεί από μόνη της adaptation ή resilience mechanism.
- **Κεφάλαιο:** Σχετικές εργασίες; Agent design
- **Θέματα:** uncertainty-aware RL; exploration; risk; adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η survey καταγράφει εφαρμογές uncertainty estimates σε Bayesian bandits, exploration, temporal-difference uncertainty, model-based RL, epistemic risk και safe RL. Στις future directions προτείνει περαιτέρω σύνδεση UQ με meta-RL και sequential decision making. Οι χρήσεις αυτές μετατρέπουν την uncertainty σε input για απόφαση· δεν αποδεικνύουν ότι το signal οδηγεί πάντα σε σωστή policy response.

### Συμφραζόμενα

Πρόκειται για βιβλιογραφική σύνθεση πολλών επιμέρους εργασιών, όχι ενιαίο πείραμα της survey.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η resilience πρέπει να μετρηθεί από performance/recovery μετά από shift. Υψηλή epistemic variance χωρίς αποτελεσματική δράση είναι μόνο diagnostic output.

### Προτεινόμενη χρήση

Να αιτιολογήσει uncertainty-aware baseline ως ξεχωριστή agent capability και όχι ως τελικό resilience score.

### Παραπομπή

Abdar et al., RL-related literature synthesis, references 186–200, και Section 9.1.
