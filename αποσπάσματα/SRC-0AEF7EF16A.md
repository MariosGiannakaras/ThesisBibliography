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
- **Ισχυρισμός:** Ένα fixed robust MDP μπορεί να παράγει υπερβολικά συντηρητική policy όταν το uncertainty set είναι μεγάλο ή rectangular.
- **Κεφάλαιο:** Robust-RL limitations
- **Θέματα:** robust MDP, uncertainty set, conservativeness
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Το robust MDP βελτιστοποιεί worst-case performance μέσα σε επιτρεπτό σύνολο transition models. Η tractability συνήθως απαιτεί ανεξάρτητη worst-case επιλογή ανά state-action pair. Με μεγάλο uncertainty set αυτό μπορεί να συνθέσει υπερβολικά απαισιόδοξα scenarios, να μειώσει την clean απόδοση και να αποθαρρύνει χρήσιμη εξερεύνηση.

### Συμφραζόμενα

Η κριτική αφορά συγκεκριμένα robust formulations και λειτουργεί ως κίνητρο για online Bayesian ενημέρωση.

### Περιορισμοί και κίνδυνος παρερμηνείας

Worst-case baselines παραμένουν χρήσιμα, αλλά πρέπει να αναφέρεται το nominal cost τους.

### Προτεινόμενη χρήση

Να αιτιολογήσει fixed robust baseline και ξεχωριστή μέτρηση clean-performance loss.

### Παραπομπή

Derman et al. (2019), σελ. 1, Abstract και Introduction.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–6, Sections 4–6
- **Ισχυρισμός:** Posterior uncertainty των robust Q-values μπορεί να χρησιμοποιηθεί για safe exploration και online ενημέρωση του uncertainty set.
- **Κεφάλαιο:** Adaptive robust RL
- **Θέματα:** URBE, posterior variance, epistemic uncertainty
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η URBE παρέχει upper bound στην posterior variance των robust Q-values. Η variance λειτουργεί ως exploration bonus προς state-action pairs με περιορισμένη γνώση. Καθώς συλλέγονται νέες transitions, ενημερώνονται posterior και uncertainty estimates, αντί να παραμένει fixed το αρχικό επίπεδο robustness.

### Συμφραζόμενα

Η construction βασίζεται σε Bayesian transition posteriors. Δεν δηλώνει ρητά change point.

### Περιορισμοί και κίνδυνος παρερμηνείας

Υψηλή uncertainty μπορεί να οφείλεται σε περιορισμένο visitation και όχι σε πραγματική non-stationarity.

### Προτεινόμενη χρήση

Να στηρίξει adaptive uncertainty-aware agent category και logging uncertainty estimates μαζί με reward curves.

### Παραπομπή

Derman et al. (2019), σελ. 3–6, Sections 4–6.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 6–7, Sections 7.1–7.2 και Figures 2–4
- **Ισχυρισμός:** Robustness evaluation πρέπει να περιλαμβάνει nominal και misspecified transitions, επειδή fixed robust policy μπορεί να αποφεύγει τον goal ακόμη και σε ευνοϊκές συνθήκες.
- **Κεφάλαιο:** Πειραματικό πρωτόκολλο
- **Θέματα:** nominal performance, transition misspecification, visitation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο toy MDP και το Mars Rover, ο robust DQN μπορεί να παραμένει σε ασφαλή αλλά μη αποδοτική συμπεριφορά και να μη φτάνει στον goal στο nominal model. Η DQN-URBE επισκέπτεται συχνότερα το winning state και παραμένει λειτουργική όταν αυξάνεται η probability of failure, ενώ DQN-UBE είναι πιο ευάλωτη στη misspecification.

### Συμφραζόμενα

Η γενικεύσιμη αρχή είναι η ανάγκη πολλαπλών test regimes και visitation diagnostics, όχι καθολική υπεροχή συγκεκριμένου algorithm.

### Περιορισμοί και κίνδυνος παρερμηνείας

Heatmaps δεν αντικαθιστούν confidence intervals ή πολλαπλά seeds.

### Προτεινόμενη χρήση

Να αιτιολογήσει nominal return, stressed return, success rate και path/visitation diagnostics ανά severity.

### Παραπομπή

Derman et al. (2019), σελ. 6–7, Sections 7.1–7.2 και Figures 2–4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 7–9, Section 7.3, Figure 6(c) και Conclusion
- **Ισχυρισμός:** Static robustness και recovery speed μετά από αλλαγή δυναμικής είναι διαφορετικές ιδιότητες.
- **Κεφάλαιο:** Μετρικές ανθεκτικότητας
- **Θέματα:** change point, recovery speed, post-change plateau
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Μετά convergence στο CartPole, το pole length αλλάζει από 0.75 σε 1.25. Η DQN-URBE επανέρχεται γρηγορότερα σε maximal reward, ενώ ο fixed robust DQN δεν ανακάμπτει στο ίδιο training window. Η post-change trajectory παρέχει πληροφορία που χάνεται σε έναν συνολικό μέσο όρο.

### Συμφραζόμενα

Πρόκειται για ένα change point σε continuous-control domain και όχι γενική recovery guarantee.

### Περιορισμοί και κίνδυνος παρερμηνείας

Απαιτούνται προκαθορισμένο recovery threshold, uncertainty intervals και πολλαπλά seeds/change points.

### Προτεινόμενη χρήση

Να θεμελιώσει degradation depth, time-to-recovery και post-change steady-state performance.

### Παραπομπή

Derman et al. (2019), σελ. 7–9, Section 7.3, Figure 6(c) και Conclusion.
