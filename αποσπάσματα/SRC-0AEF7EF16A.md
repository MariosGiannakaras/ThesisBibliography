---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — A Bayesian Approach to Robust Reinforcement Learning

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 1–2, Abstract και Section 1
- **Ισχυρισμός:** Ένα fixed worst-case uncertainty set μπορεί να παράγει σταθερή αλλά υπερβολικά συντηρητική πολιτική, επομένως η robustness πρέπει να αξιολογείται μαζί με τη nominal utility.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο — robust MDPs
- **Θέματα:** conservativeness, worst-case policy, uncertainty set
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στα Robust MDPs η πολιτική βελτιστοποιείται ως προς το χειρότερο transition model μέσα σε γνωστό uncertainty set. Η tractable state–action rectangularity και η δυσκολία κατασκευής ακριβούς uncertainty set μπορούν να κάνουν τη λύση υπερβολικά απαισιόδοξη: ο agent προστατεύεται από συνδυασμούς worst-case transitions που μπορεί να μην εμφανίζονται μαζί στην πράξη και θυσιάζει σημαντική επίδοση ακόμη και στο nominal environment.

### Συμφραζόμενα

Η εργασία δεν απορρίπτει τη robust optimization· επιχειρεί να μάθει και να προσαρμόζει το επίπεδο uncertainty από δεδομένα, διατηρώντας robust Q-values.

### Περιορισμοί και κίνδυνος παρερμηνείας

Χαμηλή μεταβολή του score μετά από disruption μπορεί να είναι τεχνητά καλή όταν το pre-change score είναι ήδη χαμηλό. Απαιτούνται normalized degradation και absolute nominal performance.

### Προτεινόμενη χρήση

Να στηρίξει metric pair “nominal utility + robustness/recovery” και να αποτρέψει ranking μόνο με worst-case stability.

### Παραπομπή

Derman et al. (2019), σελ. 1–2, Abstract και Section 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–5, Sections 4–6 και Algorithm 1
- **Ισχυρισμός:** Η posterior variance των robust Q-values μπορεί να χρησιμοποιηθεί ως uncertainty-guided exploration signal για online προσαρμογή robust policy.
- **Κεφάλαιο:** Μοντέλα και αλγόριθμοι
- **Θέματα:** Bayesian uncertainty, URBE, safe exploration, online adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι transitions έχουν Dirichlet priors και ενημερώνονται από observed history. Γύρω από την posterior mean κατασκευάζονται uncertainty sets και η URBE παρέχει Bellman recursion για άνω φράγμα της posterior variance των robust Q-values. Στο DQN-URBE, ξεχωριστό network head προσεγγίζει αυτή την uncertainty και προστίθεται ως exploration bonus στο robust Q-value. Ο agent εξερευνά περισσότερο όπου υπάρχει robust uncertainty και ανανεώνει την posterior γνώση του αντί να χρησιμοποιεί αμετάβλητο minimax model.

### Συμφραζόμενα

Το uncertainty signal δεν είναι explicit changepoint detector. Λειτουργεί ως μηχανισμός exploration και έμμεσης προσαρμογής των posterior uncertainty sets.

### Περιορισμοί και κίνδυνος παρερμηνείας

Στη deep έκδοση παραβιάζονται assumptions της θεωρητικής derivation: το transition graph δεν είναι κατ’ ανάγκη acyclic, η policy δεν παραμένει fixed και η URBE προσεγγίζεται από network. Οι θεωρητικές εγγυήσεις δεν μεταφέρονται αυτούσιες στο DQN experiment.

### Προτεινόμενη χρήση

Να παρουσιάσει uncertainty-aware adaptive robustness και να ορίσει diagnostic logging της uncertainty γύρω από perturbation events.

### Παραπομπή

Derman et al. (2019), σελ. 3–5, Sections 4–6, Algorithm 1 και Figure 1.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 5–7, Sections 7.1–7.2, Figures 2–4
- **Ισχυρισμός:** Σε GridWorld με uncertain transition failures, μία fixed robust policy μπορεί να αποφεύγει την αποτυχία αλλά να μην ολοκληρώνει ποτέ τον στόχο, ενώ uncertainty-aware robust exploration μπορεί να διατηρεί καλύτερο robustness–performance trade-off.
- **Κεφάλαιο:** Σχετικές εργασίες και επιλογή μοντέλων
- **Θέματα:** GridWorld, transition failure, robust exploration, task completion
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο 10×10 Mars Rover, η πιθανότητα μετάβασης σε failure terminal state αυξάνεται όταν ο agent κινείται προς τον στόχο. Το fixed robust DQN δεν καταλήγει στη failure state, αλλά αποφεύγει ουσιαστικά την πρόοδο και δεν φτάνει στον στόχο ούτε στο nominal model. Το DQN-UBE αποδίδει nominally αλλά υποβαθμίζεται έντονα με μεγαλύτερη failure probability. Το DQN-URBE φτάνει στον στόχο στο nominal model και εμφανίζει μικρότερη ευαισθησία σε transition misspecification.

### Συμφραζόμενα

Το αποτέλεσμα αφορά συγκεκριμένο reward design, uncertainty-set sampling και deep-DQN implementation. Η σημαντική γενική αρχή είναι η διάκριση ασφαλούς αδράνειας από λειτουργική resilience.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν αποδεικνύει υπεροχή σε observation noise, action substitution ή reward changes. Δεν παρουσιάζονται confidence intervals σύγχρονου τύπου ή μεγάλος αριθμός seeds.

### Προτεινόμενη χρήση

Να αιτιολογήσει transition-failure scenario σε GridWorld και metrics success rate, path efficiency, catastrophic failure rate και nominal–robust trade-off.

### Παραπομπή

Derman et al. (2019), σελ. 5–7, Sections 7.1–7.2, Figures 2–4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 7–8, Section 7.3, Figure 6(c) και Section 9
- **Ισχυρισμός:** Η recovery μετά από abrupt change πρέπει να αξιολογείται από την πλήρη post-change learning curve και όχι μόνο από μία τελική επίδοση.
- **Κεφάλαιο:** Μετρικές — recovery speed
- **Θέματα:** changing dynamics, recovery curve, adaptation speed
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Αφού robust DQN και DQN-URBE συγκλίνουν στο Cartpole, το pole length αλλάζει από 0.75 σε 1.25 και η εκπαίδευση συνεχίζεται. Η curve δείχνει ότι το URBE συγκλίνει αρχικά πιο αργά, αλλά μετά τη μεταβολή ανακάμπτει πολύ γρηγορότερα και φτάνει ξανά σε maximal reward. Το fixed robust DQN δεν ανακάμπτει στη βέλτιστη reward. Το αποτέλεσμα υποστηρίζει την παρατήρηση της χρονικής τροχιάς και του recovery delay.

### Συμφραζόμενα

Η perturbation είναι μία γνωστή abrupt change κατά το ongoing training. Η εργασία δεν ορίζει formal recovery threshold ή confidence interval για time-to-recovery.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η οπτική σύγκριση smoothed curves δεν αρκεί για γενική claim. Στη διπλωματική το recovery time πρέπει να υπολογιστεί ανά seed με προκαθορισμένο threshold και uncertainty interval.

### Προτεινόμενη χρήση

Να στηρίξει continued-learning scenarios και metric time-to-90%-of-new-reference, μαζί με area-under-recovery-deficit.

### Παραπομπή

Derman et al. (2019), σελ. 7–8, Section 7.3, Figure 6(c), και Section 9.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 4–5, παράγραφος πριν από Section 7, και σελίδα 8, Conclusion
- **Ισχυρισμός:** Η deep εφαρμογή ενός θεωρητικού uncertainty method πρέπει να παρουσιάζεται με σαφή διάκριση ανάμεσα στις formal assumptions και στην heuristic approximation.
- **Κεφάλαιο:** Threats to validity και reproducibility
- **Θέματα:** theoretical assumptions, function approximation, evidence strength
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς δηλώνουν ότι στο deep setting παραβιάζονται αρκετές assumptions της variance derivation: τα transition models δεν είναι acyclic, η policy δεν είναι fixed και η URBE δεν λύνεται ακριβώς αλλά προσεγγίζεται από sub-network. Παρότι η heuristic αποδίδει στα experiments, μελλοντική εργασία απαιτείται για asymptotic behavior και για την επίδραση του μεγέθους του posterior uncertainty set.

### Συμφραζόμενα

Η ειλικρινής αυτή διάκριση περιορίζει το είδος του claim που μπορεί να κάνει η διπλωματική αν επαναχρησιμοποιήσει ή προσαρμόσει την αρχιτεκτονική.

### Περιορισμοί και κίνδυνος παρερμηνείας

Empirical success σε τρία domains δεν μετατρέπει το deep heuristic σε method με πλήρεις theoretical guarantees.

### Προτεινόμενη χρήση

Να καταγραφεί ως απειλή εγκυρότητας και ως λόγος για μικρό pilot/ablation πριν από τελική επιλογή DQN-URBE.

### Παραπομπή

Derman et al. (2019), σελ. 4–5 και 8, πριν από Section 7 και Section 9.