---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — A Bayesian Approach to Robust Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδα 1, Abstract και Introduction
- **Ισχυρισμός:** Ένα fixed robust MDP μπορεί να οδηγήσει σε υπερβολικά συντηρητική πολιτική, ιδιαίτερα όταν το uncertainty set είναι μεγάλο ή rectangular.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο και robust-RL limitations
- **Θέματα:** robust MDP, uncertainty set, conservativeness, worst case
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το robust MDP προστατεύει την πολιτική βελτιστοποιώντας τη χειρότερη απόδοση μέσα σε σύνολο επιτρεπτών transition models. Η υπολογιστική tractability συνήθως απαιτεί state-action rectangular uncertainty, δηλαδή ανεξάρτητη επιλογή worst-case transition ανά state-action pair. Μαζί με ένα υπερβολικά μεγάλο uncertainty set, αυτό μπορεί να συνθέτει πολύ απαισιόδοξα σενάρια και να παράγει πολιτικές που θυσιάζουν υπερβολικά τη nominal απόδοση ή αποφεύγουν χρήσιμη εξερεύνηση.

### Συμφραζόμενα

Η κριτική αφορά συγκεκριμένη οικογένεια robust formulations και όχι κάθε τεχνική robustness. Οι συγγραφείς χρησιμοποιούν το πρόβλημα ως κίνητρο για online Bayesian ενημέρωση της αβεβαιότητας.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να συμπεράνουμε ότι worst-case baselines είναι άχρηστα. Αποτελούν σημαντικό σημείο σύγκρισης, αλλά το nominal cost και η δυνατότητα προσαρμογής τους πρέπει να αναφέρονται.

### Προτεινόμενη χρήση

Να αιτιολογήσει baseline που είναι robust αλλά μη adaptive και ξεχωριστή μέτρηση της απώλειας nominal performance.

### Παραπομπή

Derman et al. (2019), σελ. 1, Abstract και Introduction.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–6, Sections 4–6
- **Ισχυρισμός:** Η posterior uncertainty των robust Q-values μπορεί να οργανωθεί σε Bellman-style recursion και να χρησιμοποιηθεί για safe exploration και online ενημέρωση του uncertainty set.
- **Κεφάλαιο:** Adaptive robust reinforcement learning
- **Θέματα:** URBE, posterior variance, epistemic uncertainty, exploration
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η Uncertainty Robust Bellman Equation παρέχει άνω φράγμα στην posterior variance των robust Q-values. Η εκτιμώμενη variance λειτουργεί ως uncertainty bonus που κατευθύνει τον agent προς state-action pairs όπου η γνώση του μοντέλου είναι περιορισμένη. Καθώς συλλέγονται νέες μεταβάσεις, ενημερώνεται το posterior και, έμμεσα, το επίπεδο robustness που απαιτείται. Η λογική είναι διαφορετική από ένα uncertainty set που καθορίζεται μία φορά και δεν αλλάζει.

### Συμφραζόμενα

Η κατασκευή βασίζεται σε Bayesian transition posteriors και συγκεκριμένες assumptions. Δεν είναι γενικός change-point detector και δεν δηλώνει ρητά πότε συνέβη αλλαγή.

### Περιορισμοί και κίνδυνος παρερμηνείας

Epistemic uncertainty μπορεί να αυξηθεί λόγω ανεπαρκούς visitation και όχι απαραίτητα λόγω non-stationarity. Στη διπλωματική πρέπει να διαχωριστεί η ένδειξη αβεβαιότητας από την επιβεβαιωμένη ανίχνευση αλλαγής.

### Προτεινόμενη χρήση

Να στηρίξει την κατηγορία adaptive uncertainty-aware agents και να αιτιολογήσει telemetry για uncertainty estimates μαζί με performance curves.

### Παραπομπή

Derman et al. (2019), σελ. 3–6, Sections 4–6.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 6–7, Sections 7.1–7.2, Figures 2–4
- **Ισχυρισμός:** Η robustness αξιολόγηση πρέπει να συγκρίνει nominal συμπεριφορά και συμπεριφορά υπό misspecified transitions, επειδή ένας fixed robust agent μπορεί να αποφεύγει τον στόχο ακόμη και όταν οι συνθήκες είναι ευνοϊκές.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** nominal performance, transition misspecification, Mars Rover, visitation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο μικρό MDP και στο Mars Rover, η εργασία συγκρίνει την πρόσβαση σε υψηλό reward υπό nominal και δυσμενείς transition probabilities. Τα visitation heatmaps δείχνουν ότι ο robust DQN μπορεί να παραμένει σε ασφαλή αλλά μη αποδοτική συμπεριφορά και να μη φτάνει στον goal, ενώ η DQN-URBE επισκέπτεται συχνότερα το winning state. Όταν αυξάνεται η πιθανότητα failure, η UBE χωρίς robust objective εμφανίζεται πιο ευάλωτη από την URBE.

### Συμφραζόμενα

Τα αποτελέσματα αφορούν τις συγκεκριμένες υλοποιήσεις και uncertainty sets. Η γενικεύσιμη αρχή είναι η ανάγκη πολλαπλών test regimes και state-visitation diagnostics.

### Περιορισμοί και κίνδυνος παρερμηνείας

Ένα heatmap δεν αντικαθιστά confidence intervals ή πολλαπλά seeds. Δεν επιτρέπεται να παρουσιαστεί η qualitative εικόνα ως καθολική υπεροχή της DQN-URBE.

### Προτεινόμενη χρήση

Να αιτιολογήσει nominal return, stressed return, success rate και visitation/path diagnostics ανά severity.

### Παραπομπή

Derman et al. (2019), σελ. 6–7, Sections 7.1–7.2 και Figures 2–4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 7–9, Section 7.3, Figure 6(c) και Conclusion
- **Ισχυρισμός:** Η static robustness και η recovery speed μετά από αλλαγή δυναμικής είναι διαφορετικές ιδιότητες και πρέπει να μετρώνται χωριστά.
- **Κεφάλαιο:** Μετρικές ανθεκτικότητας και ανάκαμψης
- **Θέματα:** change point, recovery speed, adaptation, post-change plateau
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Αφού οι agents συγκλίνουν στο CartPole, το pole length αλλάζει από 0.75 σε 1.25. Η DQN-URBE εμφανίζει αρχικά διαφορετική learning dynamics, αλλά μετά την αλλαγή ανακτά γρήγορα τη μέγιστη reward, ενώ ο fixed robust DQN δεν επανέρχεται στο ίδιο χρονικό παράθυρο. Το paper χρησιμοποιεί αυτή τη διαφορά για να υποστηρίξει ότι online ενημέρωση uncertainty μπορεί να βελτιώσει adaptation σε changing dynamics.

### Συμφραζόμενα

Πρόκειται για ένα change point και συγκεκριμένο continuous-control domain. Το εύρημα δεν ορίζει γενική recovery metric, αλλά δείχνει γιατί η post-change trajectory έχει πληροφορία που χάνεται σε έναν συνολικό μέσο όρο.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να μεταφερθούν αυτούσιες οι episode counts ή το pole-length setup. Η διπλωματική χρειάζεται προκαθορισμένο recovery threshold, uncertainty interval και επαναλήψεις σε πολλαπλά change points/severities.

### Προτεινόμενη χρήση

Να θεμελιώσει μετρικές degradation depth, time-to-recovery και post-change steady-state performance πέρα από το συνολικό return.

### Παραπομπή

Derman et al. (2019), σελ. 7–9, Section 7.3, Figure 6(c) και Conclusion.
