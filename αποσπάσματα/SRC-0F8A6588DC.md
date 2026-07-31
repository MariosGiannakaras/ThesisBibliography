---
κωδικός: SRC-0F8A6588DC
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — NovGrid

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** Introduction και *An Ontology of Novelty for Sequential Decision Making*, Table 1
- **Ισχυρισμός:** Η novelty στο NovGrid παραγοντοποιείται σε object/action αλλαγές, unary/non-unary σχέσεις και barrier/delta/shortcut επιδράσεις στη λύση.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο· Πειραματικό περιβάλλον
- **Θέματα:** novelty taxonomy; object changes; action changes; solution distribution
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η εργασία ταξινομεί τις αλλαγές ανάλογα με το αν επηρεάζουν objects ή action mechanics, αν αφορούν ιδιότητα ενός στοιχείου ή σχέση πολλών στοιχείων και αν η νέα βέλτιστη λύση γίνεται δυσκολότερη, ισοδύναμη σε μήκος ή ευκολότερη.

### Συμφραζόμενα

Η ontology σχεδιάστηκε για sequential decision-making και υλοποιείται με ενδεικτικές MiniGrid novelties.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν αποτελεί εξαντλητική taxonomy κάθε μορφής uncertainty ή distribution shift.

### Προτεινόμενη χρήση

Σχεδιασμός μικρού, παραγοντοποιημένου matrix αλλαγών χωρίς αυθαίρετη ανάμειξη πολλών μηχανισμών.

### Παραπομπή

Balloch et al., *Introduction* και *An Ontology of Novelty for Sequential Decision Making*, Table 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** *An Ontology of Novelty for Sequential Decision Making* και *Novelty MiniGrid*
- **Ισχυρισμός:** Το NovGrid κρατά σταθερό το observation/action interface, αλλά επιτρέπει να αλλάξουν τα effects ενεργειών, οι ιδιότητες αντικειμένων και οι reachable states.
- **Κεφάλαιο:** Μεθοδολογία
- **Θέματα:** controlled change; interface invariants; transition dynamics
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Πριν και μετά τη novelty το πλήθος και το σχήμα observations και actions παραμένουν συμβατά. Μπορούν όμως να εμφανιστούν νέες καταστάσεις ή μία ίδια action να αποκτήσει διαφορετικό αποτέλεσμα, επιτρέποντας ελεγχόμενη before/after αξιολόγηση.

### Συμφραζόμενα

Ο wrapper αλλάζει τις post-novelty reset και grid-generation λειτουργίες όταν φτάσει το episode εισαγωγής της αλλαγής.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η σταθερότητα του interface δεν σημαίνει stationarity του MDP ούτε ισοδύναμη δυσκολία πριν και μετά.

### Προτεινόμενη χρήση

Ορισμός environment invariants και validation tests για μεταβαλλόμενους κανόνες.

### Παραπομπή

Balloch et al., *An Ontology of Novelty for Sequential Decision Making* και *Novelty MiniGrid*.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** *Evaluation and Baseline*, Figure 2
- **Ισχυρισμός:** Η αξιολόγηση novelty adaptation απαιτεί χωριστή μέτρηση άμεσης ανθεκτικότητας, τελικής post-change επίδοσης, χρόνου/αλληλεπιδράσεων ανάκαμψης και one-shot επίδοσης.
- **Κεφάλαιο:** Μετρικές
- **Θέματα:** resilience; adaptive efficiency; asymptotic performance; one-shot adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το NovGrid ορίζει resilience ως την post-change επίδοση της pre-novelty policy σε σχέση με random baseline, asymptotic adaptive performance ως την τελική συγκλίνουσα επίδοση, adaptive efficiency ως τις αλληλεπιδράσεις μέχρι σύγκλιση και one-shot adaptive performance ως την επίδοση μετά από ένα post-change episode.

### Συμφραζόμενα

Οι μετρικές περιγράφουν διαφορετικά τμήματα της performance curve και δεν πρέπει να συμπτύσσονται άκριτα σε ένα score.

### Περιορισμοί και κίνδυνος παρερμηνείας

Ο ειδικός ορισμός resilience της εργασίας δεν είναι καθολικός και πρέπει να συγκριθεί με curve-based definitions άλλων πηγών.

### Προτεινόμενη χρήση

Αιτιολόγηση χωριστών primary και secondary recovery metrics στη διπλωματική.

### Παραπομπή

Balloch et al., *Evaluation and Baseline*, Figure 2.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** *Evaluation and Baseline*, Figure 3
- **Ισχυρισμός:** Ένα agent που απλώς συνεχίζει να μαθαίνει μετά την αλλαγή είναι χρήσιμο baseline, αλλά δεν ισοδυναμεί με ειδικό novelty-adaptation mechanism.
- **Κεφάλαιο:** Baselines· Πειραματικό πρωτόκολλο
- **Θέματα:** continued learning; PPO; lower-bound baseline; recovery
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο DoorKeyChange experiment ο PPO δεν διαθέτει εξειδικευμένο μηχανισμό novelty adaptation. Μετά την αλλαγή συνεχίζει την RL εκπαίδευση από extrinsic reward, ώστε η καμπύλη του να λειτουργεί ως απλό σημείο αναφοράς για πιο στοχευμένες μεθόδους.

### Συμφραζόμενα

Η αλλαγή εισάγεται στα 500k timesteps και η εκπαίδευση συνεχίζεται για άλλα 500k.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η εργασία το χαρακτηρίζει lower-bound, αλλά αυτό δεν αποδεικνύει ότι θα είναι κάτω από κάθε πιθανό method σε κάθε περιβάλλον.

### Προτεινόμενη χρήση

Καθιέρωση `continue-learning` baseline δίπλα σε frozen-policy και reset/retrain baselines.

### Παραπομπή

Balloch et al., *Evaluation and Baseline*, Figure 3.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** *Evaluation and Baseline*, Figure 3
- **Ισχυρισμός:** Η ενδεικτική PPO καμπύλη παρουσιάζει χαμηλή άμεση resilience και αργή, ατελή ανάκαμψη μετά το DoorKeyChange.
- **Κεφάλαιο:** Σχετικές εργασίες· Μετρικές
- **Θέματα:** performance drop; adaptation time; asymptotic gap
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο συγκεκριμένο setup αναφέρονται resilience 0.0531 και one-shot performance 0.22. Η post-novelty καμπύλη συγκλίνει περίπου 300k timesteps μετά την αλλαγή και σε χαμηλότερη reward περίπου 0.8.

### Συμφραζόμενα

Οι τιμές αφορούν 6×6 DoorKeyChange με συγκεκριμένο PPO setup και reward scale.

### Περιορισμοί και κίνδυνος παρερμηνείας

Οι αριθμοί είναι illustrative και δεν αποτελούν target ή αναμενόμενο αποτέλεσμα της δικής μας υλοποίησης.

### Προτεινόμενη χρήση

Παράδειγμα του γιατί η τελική επίδοση από μόνη της αποκρύπτει το adaptation cost.

### Παραπομπή

Balloch et al., *Evaluation and Baseline*, Figure 3.