---
κωδικός: SRC-3EA1176D3A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Solving robust MDPs as a sequence of static RL problems

## Τεκμήριο E1 — Robustness έναντι resilience

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 1, πρώτη παράγραφος
- **Ισχυρισμός:** Στη διπλωματική, robustness πρέπει να σημαίνει διατήρηση απόδοσης χωρίς περαιτέρω εκπαίδευση, ενώ resilience πρέπει να περιλαμβάνει ανάκαμψη μέσω συνεχιζόμενης μάθησης.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο · Ορισμοί · Ερευνητικά ερωτήματα
- **Θέματα:** robustness; resilience; continued learning; recovery
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς περιγράφουν ως robustness την ικανότητα μιας policy να κρατά εγγυημένο επίπεδο αποτελεσματικότητας σε διαφορετικό περιβάλλον χωρίς να εκπαιδευτεί ξανά. Αντίθετα, ονομάζουν resilience την ικανότητα ανάκαμψης από περιβαλλοντικές αλλαγές μέσω continued learning. Η διάκριση διαχωρίζει ένα εκ των προτέρων robust controller από έναν agent που ανιχνεύει ή βιώνει τη μεταβολή και μεταβάλλει την policy του μετά από αυτή.

### Συμφραζόμενα

Ο ορισμός εμφανίζεται στο πλαίσιο robust MDPs και worst-case transition uncertainty. Είναι ιδιαίτερα χρήσιμος για να οργανωθούν οι agents της διπλωματικής σε nominal, fixed robust και adaptive/resilient baselines. Οι δύο ιδιότητες μπορούν να συνυπάρχουν, αλλά δεν πρέπει να συγχωνευθούν σε ένα ασαφές score.

### Περιορισμοί και κίνδυνος παρερμηνείας

Πρόκειται για λειτουργική ορολογική διάκριση μέσα σε robust-RL paper, όχι για μοναδικό καθολικά αποδεκτό standard. Η τελική διατύπωση της διπλωματικής πρέπει να δηλώνεται ρητά και να συνδεθεί με measurable quantities: degradation για robustness και recovery trajectory για resilience.

### Προτεινόμενη χρήση

Να αποτελέσει τη βασική πηγή για τον διαχωρισμό των research questions “αντέχει χωρίς update;” και “ανακάμπτει όταν επιτρέπεται update;”.

### Παραπομπή

Zouitine, Geist, and Rachelson (2024), Section 1, opening paragraph.

---

## Τεκμήριο E2 — Static και dynamic transition uncertainty

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 2, υποενότητες “Robust MDPs” και “The static model”
- **Ισχυρισμός:** Το πειραματικό πρωτόκολλο πρέπει να δηλώνει αν οι κανόνες αλλάζουν ανά timestep, ανά episode ή παραμένουν σταθεροί μετά από change point.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο · Πειραματικά scenarios
- **Θέματα:** static uncertainty; dynamic uncertainty; transition model; non-stationarity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο dynamic uncertainty model, ένας adversarial μηχανισμός μπορεί να επιλέγει διαφορετική transition function σε κάθε βήμα. Στο static model επιλέγεται μία transition function από το uncertainty set και αυτή παραμένει ίδια σε ολόκληρη την trajectory. Υπό stationary policies και rectangular uncertainty sets υπάρχει συγκεκριμένη equivalence για την robust value, αλλά το γενικό static optimisation δεν γίνεται αυτόματα εύκολο και μπορεί να είναι υπολογιστικά δυσχερές.

### Συμφραζόμενα

Η διάκριση επηρεάζει άμεσα την έννοια “changing rules”. Άλλο πείραμα είναι ένα μόνιμο rule change στο επεισόδιο, άλλο μία τυχαία αστοχία transition σε κάθε βήμα και άλλο ένα μοναδικό άγνωστο change point μετά το οποίο ισχύει νέο καθεστώς. Αυτές οι περιπτώσεις δεν πρέπει να αναμειχθούν σε ένα κοινό label.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η static–dynamic equivalence που συζητά το paper προϋποθέτει stationary policies και rectangularity. Δεν δικαιολογεί την αντικατάσταση κάθε non-stationary experiment από static test. Στη διπλωματική θα χρησιμοποιηθεί ως taxonomy και baseline distinction, όχι ως απόδειξη ότι όλες οι αλλαγές είναι ισοδύναμες.

### Προτεινόμενη χρήση

Να αιτιολογήσει τρία ξεχωριστά scenario families: stochastic per-step failures, persistent episode-level variants και abrupt persistent regime changes.

### Παραπομπή

Zouitine, Geist, and Rachelson (2024), Section 2, “Robust MDPs” and “The static model”.

---

## Τεκμήριο E3 — Minimal GridWorld για transition uncertainty

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 4, “Illustration”, Algorithm 1 και Σχήμα 1
- **Ισχυρισμός:** Ένα μικρό GridWorld μπορεί να χρησιμοποιηθεί επιστημονικά για να απομονώσει uncertainty στη transition function και να ελέγξει robust-policy μηχανισμούς.
- **Κεφάλαιο:** Πειραματικό περιβάλλον · Baselines
- **Θέματα:** GridWorld; worst-case search; transition uncertainty; robust value
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο Windy Walk GridWorld, ο agent επιλέγει ανάμεσα σε τρεις διαδρομές προς τον στόχο. Η πιθανότητα να παρασυρθεί προς τα πίσω μεταβάλλεται ανά corridor μέσω μιας ελεγχόμενης παραμέτρου. Το uncertainty set περιλαμβάνει διακριτές τιμές αυτής της παραμέτρου. Το IWOCS λύνει επανειλημμένα static MDPs, κατασκευάζει pessimistic Q-values πάνω στα ήδη εντοπισμένα models και αναζητεί νέο worst-case model για την τρέχουσα policy.

### Συμφραζόμενα

Το παράδειγμα δείχνει πώς η απλότητα επιτρέπει γνωστό uncertainty set, brute-force worst-case evaluation και άμεση σύγκριση με robust value iteration. Αντίστοιχα, το δικό μας GridWorld μπορεί να διαθέτει ground-truth rule versions και ακριβή oracle evaluation, χωρίς να ισχυρίζεται ρεαλιστική προσομοίωση πραγματικού domain.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το Windy Walk είναι illustrative toy problem. Δεν τεκμηριώνει ότι το IWOCS θα είναι πρακτικό σε όλη τη δική μας experiment matrix ούτε ότι η μετάβαση σε deep agents είναι δωρεάν. Επίσης αξιολογεί worst-case robustness, όχι detection delay ή recovery speed.

### Προτεινόμενη χρήση

Να στηρίξει την επιλογή GridWorld ως instrumented minimal testbed και πιθανό μικρό robust-oracle baseline σε περιορισμένο uncertainty set.

### Παραπομπή

Zouitine, Geist, and Rachelson (2024), Section 4, Algorithm 1 and Figure 1.
