---
κωδικός: SRC-0AEF7EF16A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "UAI 2019 proceedings, paper 228"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# A Bayesian Approach to Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Esther Derman, Daniel Mankowitz, Timothy Mann, Shie Mannor
- **Έτος:** 2019
- **Τύπος πηγής:** πρωτογενής θεωρητική και πειραματική εργασία συνεδρίου
- **DOI / arXiv / URL:** UAI 2019, paper 228 — https://www.auai.org/uai2019/proceedings/papers/228.pdf
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0AEF7EF16A.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς ένας robust-RL agent μπορεί να παραμένει προστατευμένος απέναντι σε σφάλμα μοντέλου, χωρίς να εγκλωβίζεται σε υπερβολικά συντηρητική πολιτική και χωρίς να θεωρεί ότι το uncertainty set παραμένει σταθερό. Το ερευνητικό ερώτημα είναι αν η αβεβαιότητα πάνω στις robust Q-values μπορεί να χρησιμοποιηθεί για ασφαλέστερη εξερεύνηση και online προσαρμογή του επιπέδου robustness όταν οι δυναμικές του περιβάλλοντος μεταβάλλονται.

Η συνάφεια με την επίσημη αίτηση είναι άμεση. Η αίτηση απαιτεί σύγκριση ανθεκτικών πρακτόρων σε περιβάλλον με δυναμικές αλλαγές και αξιολόγηση της ανάκαμψης. Η πηγή διαχωρίζει τη στατική worst-case προστασία με fixed uncertainty set από την online προσαρμογή της εκτίμησης αβεβαιότητας μέσω νέων παρατηρήσεων.

## Σύνοψη

Οι συγγραφείς ξεκινούν από το Robust MDP, όπου η transition model θεωρείται μέλος state-action rectangular uncertainty set και η policy βελτιστοποιεί τη worst-case απόδοση. Αυτή η προσέγγιση μπορεί να γίνει υπερβολικά απαισιόδοξη, επειδή μεγάλα ή rectangular sets επιτρέπουν ασύμβατες worst-case μεταβάσεις ανεξάρτητα ανά state-action pair.

Προτείνουν την Uncertainty Robust Bellman Equation (URBE), η οποία δίνει άνω φράγμα στην posterior variance των robust Q-values. Η variance χρησιμοποιείται ως bonus εξερεύνησης, ώστε ο agent να συλλέγει πληροφορία σε αβέβαιες περιοχές και να ενημερώνει το posterior uncertainty set. Η deep εκδοχή DQN-URBE συνδυάζει robust Q-network με uncertainty network.

Η αξιολόγηση περιλαμβάνει μικρό MDP με χαρακτηριστικά GridWorld, Mars Rover και CartPole. Συγκρίνονται vanilla DQN, robust DQN με fixed uncertainty set, DQN-UBE και DQN-URBE. Ο fixed robust agent μπορεί να αποφεύγει υπερβολικά την εξερεύνηση, ενώ η UBE χωρίς robust criterion είναι ευάλωτη σε misspecification. Η DQN-URBE στοχεύει σε ενδιάμεσο σημείο μεταξύ προστασίας και προσαρμογής.

## Μεθοδολογία

- **Τυπικό μοντέλο:** finite-horizon robust MDP με rectangular transition uncertainty sets και Dirichlet posterior ανά state-action pair.
- **Κύρια συμβολή:** upper bound της posterior variance των robust Q-values με Bellman-style recursion.
- **Αλγόριθμοι:** tabular URBE και DQN-URBE.
- **Baselines:** vanilla DQN, robust DQN και DQN-UBE.
- **Περιβάλλοντα:** 7-state toy MDP, Mars Rover και CartPole.
- **Μεταβολές:** αλλαγές transition probabilities ή pole length μετά/εκτός nominal training.
- **Αξιολόγηση:** testing reward, state visitation, nominal performance, misspecification performance και learning curve μετά από change point.

## Κύρια ευρήματα

1. **Το fixed worst-case robustness μπορεί να είναι υπερβολικά συντηρητικό.** Με μεγάλο ή rectangular uncertainty set, ο agent μπορεί να συμπεριφέρεται σαν να συμβαίνει η χειρότερη μετάβαση σε κάθε state-action pair. Αυτό μειώνει nominal απόδοση και εξερεύνηση. Τεκμηρίωση: σελίδες 1–2, Introduction.
2. **Η epistemic uncertainty μπορεί να ενημερώνεται online.** Η URBE μετατρέπει posterior uncertainty σε recursion και exploration bonus, ώστε το επίπεδο προστασίας να μην παραμένει παγωμένο. Τεκμηρίωση: Sections 4–6.
3. **Robustness και exploration μπορούν να σχεδιαστούν από κοινού.** Η DQN-URBE εξερευνά αβέβαιες αλλά δυνητικά χρήσιμες περιοχές ενώ αξιολογεί worst-case transitions. Τεκμηρίωση: Sections 6–7.
4. **Απαιτούνται nominal και misspecified tests.** Στο Mars Rover, ο robust DQN δεν φτάνει στον goal ακόμη και στο nominal model, ενώ η DQN-URBE επισκέπτεται συχνότερα το winning state και παραμένει λειτουργική σε μεγαλύτερη failure probability. Τεκμηρίωση: σελίδες 6–7, Section 7.2, Figures 3–4.
5. **Η recovery speed είναι διαφορετική από static robustness.** Μετά την αλλαγή pole length από 0.75 σε 1.25, η DQN-URBE ανακτά γρηγορότερα μέγιστη reward, ενώ ο robust DQN δεν ανακάμπτει στο ίδιο window. Τεκμηρίωση: σελίδες 7–8, Section 7.3, Figure 6(c).
6. **Το uncertainty-aware robustness εξαρτάται από assumptions.** Posterior approximation, uncertainty radii και deep approximation περιορίζουν τη γενίκευση. Τεκμηρίωση: Sections 4, 7 και Conclusion.

## Υποθέσεις και ορισμοί

Η πηγή διακρίνει:

- **aleatoric uncertainty:** γνωστή stochasticity των transitions,
- **epistemic/model uncertainty:** ανεπαρκής γνώση του transition kernel,
- **non-stationarity:** πραγματική αλλαγή του kernel με τον χρόνο.

Ένας fixed robust baseline προστατεύεται έναντι προκαθορισμένου set, ενώ adaptive agent χρησιμοποιεί νέα δεδομένα για detection ή/και αναθεώρηση policy. Η URBE εκτιμά αβεβαιότητα αλλά δεν αποτελεί από μόνη της explicit change-point detector.

## Περιορισμοί και απειλές εγκυρότητας

Τα theoretical αποτελέσματα αφορούν finite-horizon RMDPs και ειδικές posterior/graph assumptions. Η deep εκδοχή δεν κληρονομεί αυτομάτως όλες τις tabular εγγυήσεις. Τα πειράματα είναι λίγα, ενώ priors και uncertainty radii επηρεάζουν το αποτέλεσμα. Η CartPole αλλαγή αφορά ένα change point και μία φυσική παράμετρο. Η μέθοδος είναι επίσης βαρύτερη από tabular baselines και δεν επιβάλλεται ως υλοποίηση της διπλωματικής.

Η πηγή χρησιμοποιείται για να αιτιολογήσει adaptive-versus-fixed robust comparison, conservativeness trade-off και recovery curves, όχι για να επιβάλει DQN-URBE ως υποχρεωτικό μοντέλο.

## Σχέση με άλλες πηγές

Το `SRC-81A15E6905` ορίζει action perturbations. Το `SRC-95C9DAEE68` διαχωρίζει detection και adaptation. Το `SRC-3856071502` παρέχει Bayesian change detection χωρίς control policy. Το `SRC-0A4AFAC8E9` απαιτεί πολλαπλά seeds και aggregate uncertainty analysis.

## Χρήση στη διπλωματική

- **Κεφάλαια:** robust/adaptive RL, μοντέλο αβεβαιότητας, related work, πειραματικό πρωτόκολλο και threats to validity.
- **Υποστηριζόμενοι ισχυρισμοί:** fixed robustness μπορεί να έχει nominal cost· online uncertainty learning μπορεί να επιταχύνει adaptation· recovery trajectory πρέπει να μετράται χωριστά.
- **Πειραματική συνέπεια:** fixed/non-adaptive robust baseline και agent που συνεχίζει update μετά τη μεταβολή· pre-change baseline, degradation, recovery και post-change plateau.
- **Μη επιτρεπτός ισχυρισμός:** ότι URBE είναι καθολικά καλύτερη ή ότι ένα uncertainty bonus αποτελεί πλήρη change detector.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη.
- **Έλεγχος πρωτοτύπου:** επίσημο UAI 2019 PDF, Abstract, Sections 1, 3–7, Figures 2–6 και Conclusion.
- **Απόφαση:** κύρια πηγή για static robustness, exploration και online adaptation σε changing dynamics.
