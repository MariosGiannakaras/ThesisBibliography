---
κωδικός: SRC-702F9AB94C
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PMLR 168, Learning for Dynamics and Control 2022, επίσημο PDF 16 σελίδων"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Block Contextual MDPs for Continual Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Shagun Sodhani, Franziska Meier, Joelle Pineau, Amy Zhang
- **Έτος:** 2022
- **Τύπος πηγής:** πρωτογενής θεωρητική και εμπειρική εργασία continual reinforcement learning
- **DOI / arXiv / URL:** https://proceedings.mlr.press/v168/sodhani22a.html
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-702F9AB94C.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία προτείνει το Block Contextual MDP ως πλαίσιο για non-stationary RL με πλούσιες observations και hidden context. Εξετάζει αν ένα learned context representation, ομαλό ως προς τις μεταβολές rewards και dynamics, μπορεί να επιτρέψει zero-shot adaptation σε unseen tasks χωρίς gradient updates κατά την αξιολόγηση.

## Σύνοψη

Οι συγγραφείς συνδυάζουν την block-MDP υπόθεση για rich observations με contextual MDPs και εισάγουν Lipschitz BC-MDPs. Ορίζουν task metric που εξαρτάται από reward differences και Wasserstein distance μεταξύ transition kernels, παρουσιάζουν bounds για value/generalization και προτείνουν το `ZeUS` (Zero-shot adaptation to Unknown Systems).

Το ZeUS χρησιμοποιεί observation encoder, history-based context encoder, learned dynamics model και reward model. Κατά την εκτέλεση συμπεραίνει context από τα τελευταία `k` interactions και conditionάρει την policy χωρίς parameter update. Αξιολογείται σε families continuous-control tasks με μεταβαλλόμενες physical dynamics ή reward parameters.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** DM Control/MuJoCo Cheetah, Walker και Finger tasks· Sawyer-Peg για varying goal/reward.
- **Μοντέλα / αλγόριθμοι:** ZeUS representation learning μαζί με SAC-AE policy optimization.
- **Baselines:** UP-OSI, CaDM, HyperDynamics, ZeUS χωρίς context loss και Meld στα reward-shift experiments.
- **Μετρικές:** episodic return σε training, interpolation και extrapolation contexts· mean και standard error σε 10 seeds· correlation learned και ground-truth context distances.
- **Πειραματική διαδικασία:** predefined context ranges· held-out interpolation/extrapolation για dynamics· test reward parameters από το training range· online context inference χωρίς gradient updates.

## Κύρια ευρήματα

1. **Reward και dynamics variation μπορούν να μοντελοποιηθούν ως latent context μόνο όταν οι tasks μοιράζονται επαρκή δομή.** Το BC-MDP χαρτογραφεί context σε reward, transition και observation components. Τεκμηρίωση: Ενότητες 1 και 3, Definitions 1–3.
2. **Η theoretical generalization εξαρτάται από smoothness και identifiability.** Το νέο context πρέπει να μπορεί να συναχθεί από περιορισμένο αριθμό transitions και να βρίσκεται κοντά σε γνωστά contexts σύμφωνα με το learned metric. Τεκμηρίωση: Ενότητα 4, Assumption 1 και Theorems 1–2.
3. **Το ZeUS εκτελεί zero-shot online context inference και όχι post-change learning.** Η policy δέχεται context encoding από πρόσφατο interaction history, χωρίς gradient update κατά το test. Τεκμηρίωση: Ενότητα 5 και Figure 1.
4. **Στα reported held-out dynamics experiments, το ZeUS υπερέχει των συγκρινόμενων context/system-identification baselines.** Το context-loss ablation αποδίδει χειρότερα, υποδεικνύοντας ότι η δομή του context representation συνεισφέρει. Τεκμηρίωση: Ενότητα 6.3 και Figure 2.
5. **Στα varying-reward tasks, το ZeUS επίσης αναφέρεται ως καλύτερο από τις επιλεγμένες baselines.** Η σύγκριση όμως υποθέτει πρόσβαση στη reward function και test rewards από το training range. Τεκμηρίωση: Ενότητες 6.1, 6.3 και Figure 3.
6. **Το learned context space αποτυπώνει μέρος της task geometry.** Η rank correlation με την πραγματική ordering των contexts είναι `0.60` με context loss έναντι `0.23` χωρίς αυτό. Τεκμηρίωση: Ενότητα 6.4 και Figure 4.
7. **Η επίδοση υποβαθμίζεται όσο το evaluation context απομακρύνεται από την training distribution.** Το paper το αναγνωρίζει ρητά και δείχνει degradation σε target velocities εκτός γνωστής περιοχής. Τεκμηρίωση: Ενότητα 7 και Figure 5.
8. **Dense reward αποτελεί ουσιώδη empirical assumption.** Η διάκριση tasks μέσω reward model δυσκολεύεται σε sparse-reward environments. Τεκμηρίωση: Ενότητα 7.

## Υποθέσεις και ορισμοί

Η πηγή χρησιμοποιεί τον όρο zero-shot adaptation για inference ενός latent context και άμεση επιλογή κατάλληλης behavior policy χωρίς parameter learning. Για τη διπλωματική πρέπει να διακρίνεται από:

- `frozen-policy generalization`, όπου δεν υπάρχει history-conditioned inference,
- `context inference`, όπου αλλάζει η condition της policy αλλά όχι τα parameters,
- `online learning`, όπου ενημερώνονται value/policy/model parameters,
- `recovery`, που περιγράφει την πραγματική performance trajectory μετά από αλλαγή.

Η απόσταση από την training context distribution πρέπει να καταγράφεται, επειδή η zero-shot επίδοση εξαρτάται άμεσα από αυτή.

## Περιορισμοί και απειλές εγκυρότητας

Το framework υποθέτει κοινή latent structure, smooth task family και context identifiability από μικρό history. Δεν καλύπτει arbitrary structural changes, νέες actions/states ή μη αναγνωρίσιμες αλλαγές. Τα reward experiments χρησιμοποιούν contexts από το training range και πρόσβαση στη reward function. Η μέθοδος βασίζεται σε dense rewards, deep representation learning και continuous-control benchmarks, άρα είναι υπερβολικά σύνθετη ως αρχικό GridWorld baseline.

Τα theoretical bounds δεν εγγυώνται ότι το learned representation ανακαλύπτει τις πραγματικές causal dynamics. Η επιλογή best hyperparameters με training performance και η απουσία explicit detection-delay/recovery metrics περιορίζουν την άμεση σύγκριση με detector-driven resilience methods.

## Σχέση με άλλες πηγές

- Συμπληρώνει το `SRC-3F84F52F97` με hidden rich-observation context και learned task metric.
- Είναι συγγενές με το `SRC-91D56A10CF`, αλλά εστιάζει σε smooth context inference και zero-shot transfer.
- Διαφέρει από το `SRC-7456165CEA`, το οποίο εντοπίζει arbitrary abrupt changepoints και κάνει restart/update.
- Διαφέρει από το `SRC-660560956D`, όπου η policy συνεχίζει να μαθαίνει και αυξάνει exploration μετά από prediction error.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Θεωρητικό υπόβαθρο, Contextual non-stationarity, Σχετικές εργασίες, Agent taxonomy, Train/test protocol, Threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** hidden context μπορεί να συνοψίζει structured reward/dynamics variation· zero-shot context inference είναι διαφορετικός adaptation mechanism· interpolation και extrapolation πρέπει να αναφέρονται χωριστά.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι ZeUS αντιμετωπίζει arbitrary sudden changes· ότι zero-shot inference ισοδυναμεί με online recovery· ότι χρειάζεται deep context encoder στο τελικό GridWorld.
- **Ρόλος:** υποστηρικτική

## Απαιτούμενα αποσπάσματα

Καταγράφηκαν επαληθευμένα τεκμήρια για BC-MDP assumptions, context identifiability, zero-shot inference, train/test context ranges, empirical comparisons και out-of-distribution degradation.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** χρήση ως taxonomy/related-work source· απλό context-conditioned tabular baseline μόνο αν τα pilots δείξουν επαναλαμβανόμενα και αναγνωρίσιμα regimes.
