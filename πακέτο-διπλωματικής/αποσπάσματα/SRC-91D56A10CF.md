---
κωδικός: SRC-91D56A10CF
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Deep Reinforcement Learning amidst Continual Structured Non-Stationarity

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 1–3, Sections 1–2 και Figure 2
- **Ισχυρισμός:** Η structured non-stationarity μπορεί να μοντελοποιηθεί ως ακολουθία MDPs που συνδέονται μέσω κρυφών χρονικά εξελισσόμενων παραμέτρων.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο και μοντέλο περιβάλλοντος
- **Θέματα:** DP-MDP, latent context, structured non-stationarity
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το Dynamic Parameter MDP θεωρεί ότι κάθε episode αντιστοιχεί σε διαφορετικό MDP, του οποίου dynamics και reward προσδιορίζονται από latent parameter z. Σε αντίθεση με task distributions που δειγματοληπτούν i.i.d., τα διαδοχικά z συνδέονται από transition model. Αν το z ήταν γνωστό, η κατάσταση θα μπορούσε να επεκταθεί σε `(s, z)` και να λυθεί με standard RL. Η πρόκληση είναι η online inference και prediction του μη παρατηρούμενου context.

### Συμφραζόμενα

Αυτό το μοντέλο ταιριάζει σε περιοδική, σταδιακή ή επαναλαμβανόμενη αλλαγή. Δεν περιγράφει αυτόματα μοναδικό, εντελώς απρόβλεπτο rule switch.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η λέξη «dynamic» δεν αρκεί για να θεωρηθεί ένα scenario structured. Πρέπει να δηλωθεί ποια temporal regularity μπορεί να μάθει ο agent.

### Προτεινόμενη χρήση

Να ορίσει χωριστή κατηγορία πειραμάτων predictable/structured drift, διακριτή από abrupt unknown changepoints.

### Παραπομπή

Xie et al. (2021), σελ. 1–3, Sections 1–2 και Figure 2.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 4–6, Sections 3–6
- **Ισχυρισμός:** Ένας off-policy agent μπορεί να αξιοποιεί replay σε non-stationary περιβάλλον μόνο όταν η πολιτική και ο critic condition σε κατάλληλο context για το τρέχον MDP.
- **Κεφάλαιο:** Επιλογή και σχεδιασμός μοντέλων
- **Θέματα:** LILAC, off-policy replay, task inference
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το LILAC συνδυάζει variational latent model, learned temporal prior για τα task parameters και maximum-entropy actor-critic conditioned στο inferred z. Η representation loss και η RL loss εκπαιδεύονται από off-policy trajectories. Η context-conditioned πολιτική επιτρέπει διαφορετική συμπεριφορά ανά περιβαλλοντική φάση, αντί το replay buffer να ωθεί μια μοναδική policy σε μέσο συμβιβασμό μεταξύ ασύμβατων tasks.

### Συμφραζόμενα

Η πηγή δεν αποδεικνύει ότι κάθε replay algorithm χρειάζεται νευρωνικό latent model. Σε μικρό GridWorld μπορεί να εξεταστεί explicit context, task belief ή oracle label ως απλούστερη σύγκριση.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η επιτυχία εξαρτάται από την ποιότητα inference του z και του learned temporal model. Λανθασμένο context μπορεί να προκαλέσει αρνητική μεταφορά.

### Προτεινόμενη χρήση

Να αιτιολογήσει context-aware agent ή oracle-context upper bound έναντι context-free replay baseline.

### Παραπομπή

Xie et al. (2021), σελ. 4–6, Sections 3–6.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 6–7, Section 6, Figures 4–5
- **Ισχυρισμός:** Η αξιολόγηση adaptation πρέπει να περιλαμβάνει χωριστά reward shifts, dynamics shifts και ταυτόχρονες μεταβολές των δύο.
- **Κεφάλαιο:** Πειραματικά σενάρια
- **Θέματα:** reward shift, dynamics shift, continual adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η πειραματική σουίτα περιλαμβάνει Sawyer με μεταβαλλόμενο target, HalfCheetah με μεταβολές wind και target velocity, Minitaur με μεταβαλλόμενο payload και 2D Open World με non-stationary dynamics. Το HalfCheetah μεταβάλλει ταυτόχρονα dynamics και objective. Στο συγκεκριμένο protocol το LILAC παρουσιάζεται υψηλότερο και σταθερότερο από SAC, SLAC και PPO, ενώ τα baselines συχνά συγκλίνουν σε averaged behavior.

### Συμφραζόμενα

Η διάκριση των shift types είναι σημαντικότερη από την αντιγραφή των συγκεκριμένων continuous-control domains. Στο απλό περιβάλλον μπορούν να αντιστοιχιστούν σε changing transition rules, changing goal/reward και combined scenario.

### Περιορισμοί και κίνδυνος παρερμηνείας

Τα περισσότερα settings αξιολογούνται με τρία seeds. Οι reported 95% intervals δεν εξαλείφουν την uncertainty από μικρό run count ούτε καθιστούν τις κατατάξεις καθολικές.

### Προτεινόμενη χρήση

Να ορίσει factorial scenario matrix: reward-only, dynamics-only και combined shift.

### Παραπομπή

Xie et al. (2021), σελ. 6–7, Section 6 και Figures 4–5.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 7–8, Section 6 και Figure 6
- **Ισχυρισμός:** Ο ρυθμός μεταβολής και η δυνατότητα extrapolation πρέπει να αξιολογούνται ως χωριστές ιδιότητες και όχι να συγχέονται με μία γενική έννοια robustness.
- **Κεφάλαιο:** Μετρικές και experimental factors
- **Θέματα:** change rate, intra-episode shift, extrapolation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο Sawyer οι authors μεταβάλλουν το angular step του στόχου για να ελέγξουν διαφορετικούς ρυθμούς non-stationarity. Εξετάζουν επίσης smoothly varying target μέσα στο episode και target που συνεχίζει σε νέες, μη προηγουμένως επισκεφθείσες θέσεις. Το LILAC διατηρεί υψηλή επίδοση στις συγκεκριμένες δομημένες τροχιές, σε αντίθεση με το SAC που υποβαθμίζεται στην extrapolating περίπτωση.

### Συμφραζόμενα

Τα πειράματα δείχνουν predictive tracking συγκεκριμένης latent dynamics. Δεν αποτελούν γενική απόδειξη OOD robustness σε άγνωστες μορφές αλλαγής.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η intra-episode επέκταση είναι ευκολότερη όταν το timestep παρέχεται ή μπορεί να συναχθεί. Ένα abrupt hidden switch χωρίς temporal cue είναι διαφορετικό πρόβλημα.

### Προτεινόμενη χρήση

Να συμπεριληφθούν τουλάχιστον δύο change rates και να αναφέρεται ρητά αν το pattern έχει εμφανιστεί στην εκπαίδευση.

### Παραπομπή

Xie et al. (2021), σελ. 7–8, Section 6 και Figure 6.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδα 8, Section 7 Conclusion
- **Ισχυρισμός:** Σπάνιες, μη παρατηρούμενες και διακριτές αλλαγές ενδέχεται να χρειάζονται explicit changepoint detection αντί για latent predictive adaptation μόνο.
- **Κεφάλαιο:** Περιορισμοί και σχεδιασμός agents
- **Θέματα:** changepoint detection, abrupt shifts, scope limitation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς αναγνωρίζουν ότι η episode-level latent formulation περιορίζει τη γενικότητα του DP-MDP. Για highly infrequent shifts παραπέμπουν ρητά σε change-point detection methods και σε προηγούμενες εργασίες sequential decision-making με unobserved changes. Επομένως το LILAC δεν πρέπει να παρουσιάζεται ως πλήρης αντικατάσταση μηχανισμού detection.

### Συμφραζόμενα

Η διάκριση ταιριάζει με την αρχιτεκτονική detection–adaptation: predictive latent model για structured drift, detector/reset mechanism για abrupt unknown change.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η παραπομπή σε changepoint methods είναι περιορισμός και ερευνητική κατεύθυνση, όχι πειραματική απόδειξη ότι ένας συγκεκριμένος hybrid agent θα λειτουργήσει.

### Προτεινόμενη χρήση

Να αιτιολογήσει χωριστά baselines ή scenarios για structured drift και abrupt changepoints.

### Παραπομπή

Xie et al. (2021), σελ. 8, Conclusion.
