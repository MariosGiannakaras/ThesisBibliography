---
κωδικός: SRC-E5CA725A6C
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια — Deep Reinforcement Learning in Non-stationary Environments

## 1. Unknown change points ως ξεχωριστό RL πρόβλημα
- Τύπος: πιστή παράφραση
- Θέση: Abstract; Chapter 3, Sections 3.1–3.2
- Ισχυρισμός: Η διατριβή διατυπώνει ρητά RL σε ακολουθία MDPs όταν οι πραγματικές χρονικές στιγμές αλλαγής δεν είναι γνωστές στον agent.
- Κεφάλαιο: Θεωρητικό πλαίσιο / Non-stationarity
- Θέματα: changepoint; piecewise-stationary MDP; online adaptation
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Στο unknown-change-point setting ο agent αλληλεπιδρά διαδοχικά με διαφορετικά MDPs, ενώ οι πραγματικές αλλαγές σε reward/transition distributions δεν παρέχονται ως oracle signal. Ο agent πρέπει να παράγει δικές του detected change times και να προσαρμόζει την policy μετά την ανίχνευση.

### Συμφραζόμενα
Η formulation κρατά ίδιες τις διαστάσεις state/action spaces μεταξύ regimes και επιτρέπει να αλλάζουν οι υποκείμενες reward και transition distributions.

### Περιορισμοί και κίνδυνος παρερμηνείας
Unknown changepoint δεν σημαίνει ότι δεν υπάρχει controlled ground truth για evaluation· ο evaluator γνωρίζει τα πραγματικά change points ώστε να μετρήσει detector performance.

### Προτεινόμενη χρήση
Για τον επίσημο ορισμό του non-oracle detection setting της διπλωματικής.

### Παραπομπή
Liu, PhD thesis, 2024, Chapter 3.

## 2. Detector και adapter είναι διαφορετικά υποσυστήματα
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Section 3.3
- Ισχυρισμός: Το DARL χωρίζει ρητά environment change detection από detection-boosted policy adaptation.
- Κεφάλαιο: Μεθοδολογία
- Θέματα: detector; adapter; DARL
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Το model-free DARL ανιχνεύει αλλαγή από στοιχεία της joint state-action distribution και, αφού σημάνει αλλαγή, χρησιμοποιεί ξεχωριστό gradient-constrained adaptation μηχανισμό για μεταφορά χρήσιμης προηγούμενης γνώσης.

### Συμφραζόμενα
Το detection εξετάζει τόσο state-marginal όσο και policy/conditional αλλαγές. Η adaptation δεν θεωρεί όλες τις προηγούμενες policies εξίσου χρήσιμες.

### Περιορισμοί και κίνδυνος παρερμηνείας
Καλό detector δεν συνεπάγεται καλό adapter και αντίστροφα.

### Προτεινόμενη χρήση
Για να δικαιολογηθεί ξεχωριστό detector scorecard και adapter/recovery scorecard.

### Παραπομπή
Liu, 2024, Sections 3.3.1–3.3.2.

## 3. F1 δεν αντικαθιστά το detection delay
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Tables 3.3 και 3.5
- Ισχυρισμός: Η ίδια αξιολόγηση δείχνει ότι detector με υψηλότερο/ίσο F1 μπορεί να ανιχνεύει αργότερα από άλλον detector.
- Κεφάλαιο: Πειραματικό πρωτόκολλο / Detection
- Θέματα: F1; detection delay; precision; recall
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Στο CartPole το DARL και το CRL-Unsup αναφέρονται με F1 1.0, αλλά για πραγματικές αλλαγές στα 500 και 1000 episodes τα παραδείγματα detections είναι περίπου 508/1021 για DARL και 502/1003 για CRL-Unsup. Παρόμοια, στο LunarLander το DARL έχει καλύτερο F1 στο reported table αλλά τα συγκεκριμένα detections εμφανίζονται αργότερα.

### Συμφραζόμενα
Οι αριθμοί αφορούν τα συγκεκριμένα experiments και δεν αποτελούν γενική κατάταξη των detectors.

### Περιορισμοί και κίνδυνος παρερμηνείας
F1 συμπυκνώνει correctness γύρω από change events αλλά δεν εκφράζει latency. Η μέτρηση delay χρειάζεται ανεξάρτητη αναφορά.

### Προτεινόμενη χρήση
Υποχρεωτικό protocol rule: `precision/recall/F1 + delay`, όχι ένα μόνο detector metric.

### Παραπομπή
Liu, 2024, Tables 3.3, 3.5.

## 4. Joint detection μειώνει false alarms έναντι ενός μόνο signal
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Ablation study, Table 3.4 / Figure 3.8
- Ισχυρισμός: Η συνδυαστική χρήση policy-change και episodic/state-distribution signals έδωσε καλύτερη detection fidelity από κάθε component μόνο του στο συγκεκριμένο benchmark.
- Κεφάλαιο: Detection ablations
- Θέματα: joint detector; state distribution; policy change; false alarm
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η διατριβή αναφέρει ότι neither policy-only nor episodic-only detection αναγνώριζε αξιόπιστα όλα τα πραγματικά change points, ενώ η κοινή απόφαση των δύο signals φιλτράριζε περισσότερες λανθασμένες ενδείξεις.

### Συμφραζόμενα
Το ακριβές implementation βασίζεται σε deep-policy distances και MMD-like state-distribution tests.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν συνεπάγεται ότι δύο signals είναι πάντα καλύτερα· απαιτείται calibration και matched validation.

### Προτεινόμενη χρήση
Για rationale ενός detector που συνδυάζει performance/statistical evidence αντί να ενεργοποιείται από ένα μόνο reward spike/drop.

### Παραπομπή
Liu, 2024, Section 3.4.3.

## 5. Negative transfer από προηγούμενα regimes
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Figures 3.6 και 3.10, adaptation discussion
- Ισχυρισμός: Η διατήρηση/μεταφορά προηγούμενων policies μπορεί να βλάψει adaptation όταν οι παλιές policies είναι άσχετες με το νέο regime.
- Κεφάλαιο: Adaptation / Transfer
- Θέματα: negative transfer; gradient constraints; no-transfer comparator
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η διατριβή εισάγει deliberately μια «bad» προηγούμενη policy και παρατηρεί ότι αυστηρότερα preservation constraints μπορούν να περιορίσουν έντονα την προσαρμογή καθώς προστίθενται regimes. Το DARL χαλαρώνει την επίδραση προηγούμενων policies ανάλογα με τη συνάφειά τους.

### Συμφραζόμενα
Η σύγκριση αφορά deep gradient-based adaptation.

### Περιορισμοί και κίνδυνος παρερμηνείας
Η επιτυχία ενός transfer mechanism σε συγκεκριμένα deep benchmarks δεν σημαίνει ότι το ίδιο mechanism πρέπει να υλοποιηθεί σε tabular GridWorld.

### Προτεινόμενη χρήση
Για να απαιτείται scratch/no-transfer comparator και explicit negative-transfer gap.

### Παραπομπή
Liu, 2024, Sections 3.4.3–3.4.4.

## 6. False alarm και missed change έχουν διαφορετικές συνέπειες
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Section 3.4.4
- Ισχυρισμός: Η εργασία εξετάζει ξεχωριστά το κόστος λανθασμένης ανίχνευσης και χαμένης αλλαγής.
- Κεφάλαιο: Detector failure analysis
- Θέματα: false positive; miss; adaptation cost; recovery
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Στο DARL ένα false detection μπορεί να ενεργοποιήσει περιττή adaptation και να προκαλέσει προσωρινό reward drop πριν η policy επανέλθει, ενώ ένα missed change μπορεί να επιβραδύνει την προσαρμογή επειδή δεν ενεργοποιείται εγκαίρως η κατάλληλη αλλαγή constraints/knowledge transfer.

### Συμφραζόμενα
Οι συνέπειες εξαρτώνται από τον συγκεκριμένο adapter.

### Περιορισμοί και κίνδυνος παρερμηνείας
False-alarm rate μόνο του δεν εκφράζει πόσο ακριβό είναι κάθε false alarm.

### Προτεινόμενη χρήση
Report και `false_alarm_count/rate` και `utility_cost_per_false_alarm`, μαζί με miss/delay effects.

### Παραπομπή
Liu, 2024, Section 3.4.4.

## 7. FDA: statistical decision, change magnitude και bounded memory
- Τύπος: πιστή παράφραση
- Θέση: Chapter 5, Sections 5.3–5.4
- Ισχυρισμός: Το FDA χρησιμοποιεί Wasserstein functional surprise, significance test και περιορισμένη representative memory για detection/adaptation.
- Κεφάλαιο: Advanced adaptation mechanisms
- Θέματα: Wasserstein surprise; Welch test; representative memory; plasticity
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Το FDA μετατρέπει functional surprise σε change decision μέσω Welch's t-test/significance level και ρυθμίζει το preservation της παλιάς policy σύμφωνα με το μέγεθος της αλλαγής. Για περιορισμό compute/storage κρατά representative trajectories αντί για όλο το ιστορικό.

### Συμφραζόμενα
Η representative-memory επιλογή ευνοεί trajectories κοντά σε decision boundaries και με υψηλό cumulative reward.

### Περιορισμοί και κίνδυνος παρερμηνείας
Το mechanism έχει σημαντικά υψηλότερη υπολογιστική πολυπλοκότητα από tabular recency/reset baselines.

### Προτεινόμενη χρήση
Ως rationale για bounded memory και change-magnitude-aware forgetting/retention, όχι ως υποχρεωτική υλοποίηση.

### Παραπομπή
Liu, 2024, Chapter 5.

## 8. Detection tolerance window είναι μέρος του protocol
- Τύπος: πιστή παράφραση
- Θέση: Chapter 5, Section 5.4.1 / Table 5.1
- Ισχυρισμός: Στα FDA experiments ένα detection μετρά ως correct όταν βρίσκεται μέσα σε συγκεκριμένο χρονικό παράθυρο από το ground-truth change point.
- Κεφάλαιο: Metrics / Reproducibility
- Θέματα: tolerance window; F1; detector evaluation
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Για τον υπολογισμό των detector F1 scores στη συγκεκριμένη αξιολόγηση, detections έως 5 epochs μετά το πραγματικό change point θεωρούνται correct. Η επιλογή αυτού του παραθύρου επηρεάζει άμεσα precision, recall και F1.

### Συμφραζόμενα
Η διατριβή αναφέρει FDA F1 μεγαλύτερο από τους συγκεκριμένους comparators στα τρία εξεταζόμενα VizDoom scenarios με αυτή τη definition.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν επιτρέπεται σύγκριση F1 μεταξύ papers αν χρησιμοποιούν διαφορετικά tolerance windows χωρίς normalization/σαφή αναφορά.

### Προτεινόμενη χρήση
Το detector tolerance window να οριστεί εκ των προτέρων και να αναφέρεται στο experimental protocol.

### Παραπομπή
Liu, 2024, Table 5.1.

## 9. Convergence-before-next-change assumption
- Τύπος: πιστή παράφραση
- Θέση: Chapter 3, Problem formulation
- Ισχυρισμός: Το βασικό DARL setting υποθέτει ότι κάθε regime διαρκεί αρκετά ώστε η policy να συγκλίνει πριν την επόμενη αλλαγή.
- Κεφάλαιο: Limitations / Stress tests
- Θέματα: change frequency; convergence; external validity
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Παρότι οι change points είναι άγνωστοι στον agent, η formulation υποθέτει αρκετά episodes ανά environment για policy convergence πριν από το επόμενο switch.

### Συμφραζόμενα
Η υπόθεση απλοποιεί τη διάκριση μεταξύ regimes και την αξιολόγηση adaptation.

### Περιορισμοί και κίνδυνος παρερμηνείας
Τα αποτελέσματα δεν πρέπει να μεταφερθούν αυτομάτως σε rapid drift/frequent switching.

### Προτεινόμενη χρήση
Να προστεθεί ξεχωριστό high-frequency-switch stress test στη διπλωματική, πέρα από το κύριο convergence-friendly schedule.

### Παραπομπή
Liu, 2024, Section 3.2.