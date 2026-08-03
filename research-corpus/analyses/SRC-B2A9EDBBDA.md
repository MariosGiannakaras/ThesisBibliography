---
κωδικός: SRC-B2A9EDBBDA
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Preprints.org v1, 2026"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Forgetting as Control: A Theoretical Framework for Selective Behavioral Erasure in Post-Deployment Reinforcement Learning Agents

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Mehdi Samieiyeganeh, Parisa Bahraminikoo, Soobia Saeed, Saraswathy Gunasekaran, Saadat Ahmed
- **Έτος:** 2026
- **Τύπος πηγής:** μη αξιολογημένο θεωρητικό preprint / conceptual framework
- **DOI / URL:** 10.20944/preprints202606.0911.v1
- **Κατάσταση δημοσίευσης:** ρητά μη peer reviewed

## Σκοπός

Η εργασία προτείνει ένα conceptual “Forgetting Systems” framework για post-deployment suppression ανεπιθύμητων συμπεριφορών. Ο trigger συνδυάζει αρνητική ανταμοιβή, απόκλιση από στόχο και επανάληψη συμπεριφοράς, ενώ η suppression περιγράφεται μέσω exponential decay και δυνατότητας relearning.

## Κριτική αξιολόγηση

Η ιδέα είναι θεματικά γειτονική με controlled forgetting, αλλά δεν αποτελεί επαρκές evidence για τη διπλωματική:

1. **Δεν παρέχει υλοποιημένο RL algorithm.** Οι triggers, decay και relearning mechanisms παραμένουν υψηλού επιπέδου και δεν συνδέονται με σαφή update equations για standard agent architecture.
2. **Δεν παρουσιάζει experiments ή benchmark.** Δεν υπάρχουν συγκρίσεις, seeds, recovery curves, safety metrics ή ablations.
3. **Δεν αποδεικνύει ότι ο trigger διαχωρίζει πραγματική αλλαγή περιβάλλοντος από stochastic negative outcomes.** Αρνητικό reward και επανάληψη μπορούν να εμφανιστούν σε έγκυρη exploration ή σε noisy MDP.
4. **Η “goal deviation” προϋποθέτει εξωτερικά διαθέσιμο και μετρήσιμο intended goal.** Αυτό δεν ισχύει γενικά σε RL και δημιουργεί πιθανό oracle leakage.
5. **Η λήθη συμπεριφοράς συγχέεται εν μέρει με reward shaping, action suppression, machine unlearning και runtime safety intervention.** Δεν παρέχεται operational comparison που να αποδεικνύει ξεχωριστή αλγοριθμική κατηγορία.
6. **Η εργασία είναι πρόσφατο μη peer-reviewed preprint.** Δεν μπορεί να στηρίξει κεντρικούς ισχυρισμούς ή agent selection χωρίς ανεξάρτητη πρωτογενή επιβεβαίωση.

## Χρήσιμη μόνο ως προειδοποίηση σχεδιασμού

Η πηγή μπορεί να υπενθυμίσει ότι forgetting intervention πρέπει να είναι αναστρέψιμο και ότι persistent harmful behavior ίσως απαιτεί fallback/termination. Αυτά όμως καλύπτονται ισχυρότερα από τις ήδη επιλεγμένες πηγές continual learning, runtime assurance και safe RL.

## Απόφαση

- **Ρόλος:** απόρριψη
- **Εξαγωγή:** όχι
- **Αρχείο αποσπασμάτων:** όχι
- **Αιτιολογία:** speculative non-peer-reviewed framework χωρίς algorithmic ή empirical validation

## Σχέση με το πρωτόκολλο

Η εργασία δεν αλλάζει το baseline matrix. Exponential recency, partial reset και detector-triggered interventions θα παραμείνουν ορισμένα από ισχυρότερη non-stationary RL βιβλιογραφία. Negative reward δεν θα χρησιμοποιηθεί μόνο του ως forgetting trigger.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη ως προς την απόφαση απόρριψης
- **Ελέγχθηκε το διαθέσιμο πλήρες κείμενο:** ναι
- **Ανοιχτά ζητήματα:** επανεξέταση μόνο αν εμφανιστεί peer-reviewed έκδοση με reproducible experiments.
