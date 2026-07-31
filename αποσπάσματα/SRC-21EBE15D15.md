---
κωδικός: SRC-21EBE15D15
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — A Survey of Zero-shot Generalisation in Deep Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 202–204, Introduction και Scope
- **Ισχυρισμός:** Στο αυστηρό zero-shot regime δεν επιτρέπεται πρόσθετη εκπαίδευση ή χρήση δεδομένων από τα test environment instances.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο; Πειραματικό πρωτόκολλο
- **Θέματα:** zero-shot generalization; frozen policy; test-time learning
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η survey ορίζει το zero-shot setting ως αξιολόγηση μιας policy σε environment instances διαφορετικά από εκείνα της εκπαίδευσης, χωρίς πρόσθετη εκπαίδευση ή δεδομένα από τα test instances. Μέθοδοι που ενημερώνονται πάνω στο target environment, όπως domain adaptation και πολλές meta-RL προσεγγίσεις, ανήκουν σε διαφορετικό evaluation regime.

### Συμφραζόμενα

Ο περιορισμός επιλέγεται ώστε να μετρηθεί η άμεση ικανότητα transfer/generalization πριν από οποιαδήποτε online learning response.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το zero-shot δεν είναι πάντοτε το καταλληλότερο deployment model. Ένας resilient agent μπορεί να χρειάζεται online adaptation, η οποία όμως πρέπει να αναφέρεται χωριστά.

### Προτεινόμενη χρήση

Να οριστεί frozen-policy test πριν από την adaptive phase και να αποτραπεί η παρουσίαση post-update recovery ως zero-shot generalization.

### Παραπομπή

Kirk et al., Introduction and Scope, JAIR 76, PDF σελ. 202–204.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 202–205, Introduction και Section 3
- **Ισχυρισμός:** Η zero-shot generalization είναι κλάση προβλημάτων και κάθε ισχυρισμός απαιτεί ρητή περιγραφή του context και του train/test distribution shift.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο; Ερευνητικά ερωτήματα
- **Θέματα:** contextual MDP; interpolation; extrapolation; assumptions
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς τονίζουν ότι δεν υπάρχει μία ενιαία, γενική ιδιότητα «generalization». Τα προβλήματα διαφέρουν ως προς τον παράγοντα μεταβολής, την παρατηρησιμότητα του context, τη σχέση training και testing distributions και το αν το test απαιτεί interpolation, extrapolation ή νέο συνδυασμό γνωστών παραγόντων.

### Συμφραζόμενα

Η survey χρησιμοποιεί contextual MDP formalism για να ενοποιήσει διαφορετικές γραμμές βιβλιογραφίας.

### Περιορισμοί και κίνδυνος παρερμηνείας

Βελτίωση σε έναν τύπο shift μπορεί να βλάπτει άλλον. Δεν επιτρέπεται καθολικός ισχυρισμός generalization από ένα μόνο scenario.

### Προτεινόμενη χρήση

Κάθε πείραμα να επισημαίνεται ως IID held-out, interpolation, extrapolation ή combinatorial test.

### Παραπομπή

Kirk et al., Introduction και Section 3, PDF σελ. 202–205.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 216–220, Sections 4.1–4.2
- **Ισχυρισμός:** Ένα RL benchmark ορίζεται από τον συνδυασμό environment και evaluation protocol, όχι από τον simulator μόνο.
- **Κεφάλαιο:** Πειραματικό περιβάλλον; Μεθοδολογία
- **Θέματα:** benchmark design; context sets; train-test split; budget
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η πηγή διαχωρίζει το environment, το οποίο παρέχει ένα σύνολο context-MDPs, από το evaluation protocol, το οποίο καθορίζει training και testing context sets, sampling restrictions, αριθμό training contexts και διαθέσιμο interaction budget. Το ίδιο environment μπορεί συνεπώς να υποστηρίζει διαφορετικά benchmarks.

### Συμφραζόμενα

Η taxonomy χρησιμοποιείται για να συγκριθούν υπάρχοντα ZSG environments και protocols.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η αναφορά «χρησιμοποιήθηκε GridWorld» δεν αρκεί για αναπαραγωγιμότητα. Απαιτείται πλήρης περιγραφή των splits και των update rules.

### Προτεινόμενη χρήση

Να καταγραφούν σε config και αποτελέσματα οι train/test factors, seeds, severity levels και επιτρεπόμενα updates.

### Παραπομπή

Kirk et al., Sections 4.1–4.2, PDF σελ. 216–220.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 216–223, Sections 4.1–4.3
- **Ισχυρισμός:** Purely black-box PCG προσφέρει ποικιλία αλλά δεν επιτρέπει εύκολη απομόνωση συγκεκριμένων παραγόντων· προτιμάται συνδυασμός PCG και controllable variation.
- **Κεφάλαιο:** Πειραματικό περιβάλλον; Threats to validity
- **Θέματα:** PCG; controllable factors; GridWorld; causal attribution
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Σε purely PCG environments, ο ερευνητής συνήθως ελέγχει μόνο το seed και οι επιμέρους παράγοντες του context παραμένουν μπλεγμένοι. Αυτό δυσκολεύει τη στοχευμένη μελέτη συγκεκριμένης μορφής generalization. Η survey προτείνει environments που διατηρούν procedural diversity αλλά εκθέτουν controllable factors για ακριβή επιστημονικά πειράματα.

### Συμφραζόμενα

Η κριτική δεν απορρίπτει το PCG. Απορρίπτει τη χρήση του ως μοναδικού μηχανισμού όταν ζητούνται factor-specific claims.

### Περιορισμοί και κίνδυνος παρερμηνείας

Controlled factors δεν εγγυώνται realism. Αυξάνουν κυρίως την εσωτερική εγκυρότητα και την ερμηνευσιμότητα.

### Προτεινόμενη χρήση

Στο GridWorld να τυχαιοποιείται το layout, αλλά action failure, reward noise, obstacle changes και action costs να ελέγχονται ανεξάρτητα.

### Παραπομπή

Kirk et al., Sections 4.1–4.3, PDF σελ. 216–223.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 219–220, Section 4.2, PCG Evaluation Protocols
- **Ισχυρισμός:** Held-out random seeds ελέγχουν κυρίως memorization και robust optimization και δεν τεκμηριώνουν από μόνα τους targeted OOD generalization.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο; Μετρικές
- **Θέματα:** held-out seeds; weak ZSG; context efficiency; OOD
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η survey χαρακτηρίζει το protocol όπου σχεδόν όλο το seed space χρησιμοποιείται για training και λίγα seeds κρατούνται για testing ως ασθενή μορφή ZSG. Είναι καλύτερο από evaluation στο ίδιο ακριβώς environment, αλλά ελέγχει κυρίως εάν η policy αποφεύγει memorization και όχι εάν αντέχει σε συγκεκριμένη dynamics ή reward extrapolation.

### Συμφραζόμενα

Η παρατήρηση αφορά purely PCG context spaces όπου δεν υπάρχουν άξονες με ερμηνεύσιμη δομή.

### Περιορισμοί και κίνδυνος παρερμηνείας

Held-out seeds παραμένουν χρήσιμο secondary test. Απλώς δεν πρέπει να είναι το μοναδικό evidence για generalization.

### Προτεινόμενη χρήση

Να συνδυαστούν held-out layouts με explicit factor sweeps και unseen severity combinations.

### Παραπομπή

Kirk et al., Section 4.2, PDF σελ. 219–220.

## Τεκμήριο E6

- **Τύπος:** πιστή παράφραση
- **Θέση:** PDF σελ. 242–243, Sections 6.5–6.6 και Conclusion
- **Ισχυρισμός:** Η fast online adaptation είναι σημαντική για ισχυρότερα shifts, αλλά αποτελεί χαλάρωση της zero-shot υπόθεσης και πρέπει να αξιολογείται χωριστά.
- **Κεφάλαιο:** Σχετικές εργασίες; Agent design; Μετρικές
- **Θέματα:** online adaptation; recovery; zero-shot baseline; regime separation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς προτείνουν περισσότερη έρευνα σε policies που μαθαίνουν και προσαρμόζονται online, ιδιαίτερα για ισχυρές περιβαλλοντικές μεταβολές όπου η zero-shot transfer μπορεί να μην επαρκεί. Παράλληλα διατηρούν τη zero-shot αξιολόγηση ως χρήσιμη βασική ικανότητα πάνω στην οποία μπορούν να χτιστούν adaptive λύσεις.

### Συμφραζόμενα

Το σημείο βρίσκεται στις future directions και δεν αποδεικνύει συγκεκριμένο adaptation algorithm.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να συγκρίνονται frozen και adaptive agents χωρίς κοινό pre-change training budget και σαφές post-change update budget.

### Προτεινόμενη χρήση

Να παρουσιαστούν δύο σειρές αποτελεσμάτων: immediate zero-shot drop και adaptation/recovery curve μετά την ενεργοποίηση updates.

### Παραπομπή

Kirk et al., Sections 6.5–6.6 και Conclusion, PDF σελ. 242–243.
