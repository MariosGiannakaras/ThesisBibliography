---
κωδικός: SRC-09DD20BA85
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Bounded Robustness in Reinforcement Learning via Lexicographic Objectives

## Τεκμήριο E1 — Observation corruption ως διαφορετική effective policy

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 2, Definitions 2.1–2.2
- **Ισχυρισμός:** Ο θόρυβος δεδομένων στο GridWorld πρέπει να μοντελοποιείται ως ρητός observation kernel και να μετριέται η διαφορά ανάμεσα στην nominal και τη disturbed εκτέλεση.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο · Μοντέλο αβεβαιότητας
- **Θέματα:** observational noise; DOMDP; robustness regret
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Σε ένα observationally disturbed MDP, η πραγματική κατάσταση περνά από άγνωστο stochastic kernel πριν δοθεί στην policy. Επειδή η policy επιλέγει action με βάση την αλλοιωμένη observation, το αποτέλεσμα ισοδυναμεί με εφαρμογή μιας noise-altered effective policy στο πραγματικό MDP. Η εργασία ορίζει robustness με βάση τη utility difference ανάμεσα στην αρχική policy και την policy μετά την επίδραση του kernel.

### Συμφραζόμενα

Αυτό επιτρέπει στο πείραμα να ξεχωρίσει δύο ερωτήσεις: πόσο καλά λειτουργεί ο agent όταν βλέπει σωστά το state και πόσο χάνει όταν η ίδια υποκείμενη κατάσταση παρατηρείται λανθασμένα. Για reproducibility πρέπει να αποθηκεύονται true state, observed state και kernel parameters σε κάθε βήμα.

### Περιορισμοί και κίνδυνος παρερμηνείας

Το μοντέλο αφορά state-observation corruption και όχι κάθε μορφή “data noise”. Reward noise, missing observations και delayed observations μπορεί να χρειάζονται διαφορετικό operator ή POMDP formulation. Η robustness regret της πηγής δεν αποτελεί από μόνη της recovery metric.

### Προτεινόμενη χρήση

Να στηρίξει την ακριβή τυπική περιγραφή του observation-noise scenario και τη χωριστή clean/disturbed αξιολόγηση.

### Παραπομπή

Jarne Ornia et al. (2024), Section 2, Definitions 2.1–2.2.

---

## Τεκμήριο E2 — Bounded utility–robustness trade-off

- **Τύπος:** πιστή παράφραση
- **Θέση:** Problem 2.3· Ενότητα 4 και Section 4.1, Theorem 4.1
- **Ισχυρισμός:** Μια μέθοδος δεν πρέπει να χαρακτηρίζεται καλύτερη επειδή είναι robust, χωρίς να αναφέρεται πόση nominal επίδοση θυσιάζει.
- **Κεφάλαιο:** Μετρικές · Σύγκριση μοντέλων
- **Θέματα:** utility trade-off; lexicographic objectives; bounded sub-optimality
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η εργασία θέτει την nominal utility ως objective υψηλότερης προτεραιότητας και επιτρέπει απόκλιση μόνο έως συγκεκριμένη tolerance. Μέσα στο σύνολο policies που ικανοποιούν αυτή την απαίτηση, βελτιστοποιείται δεύτερο robustness objective. Το LRPG επομένως δεν αναζητεί robustness με οποιοδήποτε τίμημα, αλλά ελέγχει ρητά την υποβάθμιση της clean objective και συνδέει τη robustification με τις convergence assumptions του βασικού policy-gradient algorithm.

### Συμφραζόμενα

Στη διπλωματική πρέπει να παρουσιάζεται τουλάχιστον ζεύγος nominal return και performance-under-perturbation. Για κάθε robust ή adaptive agent χρειάζεται επίσης adaptation overhead ή training cost. Ένας agent που φαίνεται σταθερός επειδή έχει ήδη πολύ χαμηλή clean επίδοση δεν αποτελεί χρήσιμο robust αποτέλεσμα.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η tolerance δεν επιλέγεται αυτόματα από τη θεωρία. Είναι value judgment ή experimental design parameter. Η εγγύηση εξαρτάται από assumptions για policy representation, visitation και convergence του underlying algorithm. Δεν πρέπει να παρουσιαστεί ως model-free εγγύηση για κάθε neural implementation.

### Προτεινόμενη χρήση

Να αιτιολογήσει clean-performance guardrail, robustness–utility plots και αποφυγή ενός μονοδιάστατου ranking.

### Παραπομπή

Jarne Ornia et al. (2024), Problem 2.3; Sections 4–4.1, Theorem 4.1.

---

## Τεκμήριο E3 — MiniGrid πειράματα και όρια γενίκευσης

- **Τύπος:** πιστή παράφραση
- **Θέση:** Ενότητα 6, Table 1· Ενότητα 7
- **Ισχυρισμός:** Τα observational-robust methods πρέπει να συγκρίνονται σε clean, stochastic-noise και adversarial-noise conditions, αλλά τα αποτελέσματα χρειάζονται πολλαπλά runs και προσεκτική αναφορά.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο · Threats to validity
- **Θέματα:** MiniGrid; PPO; A2C; noise evaluation; reporting
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς εφαρμόζουν LRPG πάνω σε PPO και A2C στα LavaGap, LavaCrossing και DynamicObstacles. Αξιολογούν clean environment, bounded uniform noise, Gaussian noise και state-adversarial configurations. Τα LRPG variants συχνά διατηρούν υψηλότερη disturbed reward, αλλά η εικόνα αλλάζει ανά task, base algorithm και robustness proxy. Η συζήτηση αναγνωρίζει ότι model-based filtering ή disturbance rejection μπορεί να είναι καλύτερο όταν υπάρχει noise model.

### Συμφραζόμενα

Η πειραματική δομή είναι χρήσιμη για τη δική μας observation-noise axis, αλλά η στατιστική διαδικασία πρέπει να ενισχυθεί: αντί για median agent, θα αναφέρονται όλα τα seeds με bootstrap intervals, IQM και performance profiles όπου είναι κατάλληλο. Θα διατηρείται κοινό perturbation schedule ανά paired seed.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η αξιολόγηση βασίζεται σε 10 trained agents και scores του median agent σε 50 rollouts. Αυτό δεν αποτυπώνει πλήρως training uncertainty. Τα MiniGrid tasks είναι ευαίσθητα σε single-step catastrophic actions και μπορεί να ευνοούν συγκεκριμένες invariance strategies. Δεν πρέπει να μεταφερθεί η ποσοτική κατάταξη ως αναμενόμενο αποτέλεσμα της διπλωματικής.

### Προτεινόμενη χρήση

Να τεκμηριώσει τα noise conditions και να καταγράψει γιατί η δική μας στατιστική αναφορά πρέπει να είναι αυστηρότερη από representative-agent reporting.

### Παραπομπή

Jarne Ornia et al. (2024), Section 6, Table 1; Section 7.
