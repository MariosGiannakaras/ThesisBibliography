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

Η συνάφεια με την επίσημη αίτηση είναι άμεση. Η αίτηση απαιτεί σύγκριση ανθεκτικών πρακτόρων σε περιβάλλον με δυναμικές αλλαγές και αξιολόγηση της ανάκαμψης. Η πηγή διαχωρίζει δύο δυνατότητες που δεν πρέπει να συγχέονται: στατική worst-case προστασία με fixed uncertainty set και online προσαρμογή της εκτίμησης αβεβαιότητας από νέες παρατηρήσεις.

## Σύνοψη

Οι συγγραφείς ξεκινούν από το Robust MDP, όπου η πραγματική transition model θεωρείται μέλος ενός state-action rectangular uncertainty set και η πολιτική βελτιστοποιεί τη worst-case αναμενόμενη απόδοση. Επισημαίνουν ότι αυτή η προσέγγιση συχνά γίνεται υπερβολικά απαισιόδοξη, επειδή τα uncertainty sets μπορεί να είναι μεγάλα ή να επιτρέπουν ασύμβατες worst-case μεταβάσεις ανεξάρτητα σε κάθε state-action pair.

Προτείνουν την Uncertainty Robust Bellman Equation (URBE), η οποία δίνει άνω φράγμα στην posterior variance των robust Q-values. Η variance χρησιμοποιείται ως bonus εξερεύνησης, ώστε ο agent να συλλέγει πληροφορία σε αβέβαιες περιοχές και να ενημερώνει το posterior uncertainty set. Η deep εκδοχή DQN-URBE συνδυάζει robust TD learning με δεύτερο δίκτυο που προσεγγίζει την αβεβαιότητα.

Η εμπειρική αξιολόγηση περιλαμβάνει ένα μικρό MDP με χαρακτηριστικά GridWorld, Mars Rover και CartPole. Συγκρίνονται vanilla DQN, robust DQN με fixed uncertainty set, DQN-UBE και DQN-URBE. Τα αποτελέσματα δείχνουν ότι η fixed robust πολιτική μπορεί να αποφύγει υπερβολικά την εξερεύνηση, ενώ η UBE χωρίς robust criterion μπορεί να είναι ευαίσθητη σε misspecification. Η DQN-URBE επιδιώκει ενδιάμεσο σημείο: προστασία απέναντι σε model error, αλλά και επαρκή εξερεύνηση ώστε να προσαρμόζεται όταν οι δυναμικές αλλάζουν.

## Μεθοδολογία

- **Τυπικό μοντέλο:** finite-horizon robust MDP με state-action rectangular transition uncertainty sets και Dirichlet posterior ανά state-action pair.
- **Κύρια θεωρητική συμβολή:** άνω φράγμα της posterior variance των robust Q-values που ικανοποιεί Bellman-style recursion, την URBE.
- **Αλγόριθμοι:** tabular URBE και scalable DQN-URBE με robust Q-network και uncertainty network.
- **Baselines:** vanilla DQN, robust DQN και DQN-UBE.
- **Περιβάλλοντα:** 7-state toy MDP που προσομοιώνει επιλογή ασφαλούς ή αβέβαιης διαδρομής προς reward state, Mars Rover grid-like navigation και CartPole με μεταβαλλόμενο pole length.
- **Μεταβολές:** αλλαγές στις transition probabilities ή σε φυσική παράμετρο της δυναμικής μετά/εκτός της nominal εκπαίδευσης.
- **Αξιολόγηση:** testing reward, visitation patterns, nominal performance, performance under misspecification και training curve μετά από change point.

## Κύρια ευρήματα

1. **Το fixed worst-case robustness μπορεί να είναι υπερβολικά συντηρητικό.** Με μεγάλο ή rectangular uncertainty set, ο agent μπορεί να συμπεριφέρεται σαν να συμβαίνει ανεξάρτητα η χειρότερη μετάβαση σε κάθε state-action pair. Αυτό μπορεί να μειώσει την nominal απόδοση και να εμποδίσει την εξερεύνηση. Τεκμηρίωση: σελίδες 1–2, Introduction.
2. **Η epistemic uncertainty πρέπει να ενημερώνεται από online δεδομένα.** Η URBE μετατρέπει την posterior uncertainty των robust values σε Bellman recursion και bonus εξερεύνησης. Έτσι, η προστασία δεν παραμένει απαραίτητα παγωμένη στο αρχικό uncertainty set. Τεκμηρίωση: Sections 4–6.
3. **Robustness και exploration δεν είναι αντίθετες έννοιες όταν σχεδιαστούν από κοινού.** Η DQN-URBE στοχεύει να εξερευνά αβέβαιες αλλά δυνητικά χρήσιμες περιοχές, ενώ εξακολουθεί να αξιολογεί worst-case transitions. Τεκμηρίωση: Sections 6–7.
4. **Η αξιολόγηση πρέπει να περιλαμβάνει nominal και misspecified dynamics.** Στο Mars Rover, ο fixed robust agent αποφεύγει τον goal ακόμη και στο nominal setting, ενώ η DQN-URBE φτάνει συχνότερα στο winning state και παραμένει λειτουργική όταν αυξάνεται η πιθανότητα failure. Τεκμηρίωση: σελίδες 6–7, Section 7.2 και Figures 3–4.
5. **Η recovery speed μετά από change point είναι ξεχωριστή από τη static robustness.** Στο CartPole, μετά την αλλαγή pole length από 0.75 σε 1.25, η DQN-URBE ανακτά γρηγορότερα τη μέγιστη απόδοση, ενώ ο robust DQN δεν ανακάμπτει στο ίδιο training window. Τεκμηρίωση: σελίδες 7–8, Section 7.3 και Figure 6(c).
6. **Το uncertainty-aware robustness έχει κόστος και assumptions.** Η μέθοδος βασίζεται σε posterior approximation, fixed radii για τα posterior uncertainty sets και ειδικές θεωρητικές παραδοχές. Το empirical πλεονέκτημα δεν αποτελεί γενική εγγύηση για κάθε non-stationary task. Τεκμηρίωση: Sections 4, 7 και Conclusion.

## Υποθέσεις και ορισμοί

Η πηγή διακρίνει την εσωτερική στοχαστικότητα του MDP από την αβεβαιότητα για transition/reward parameters. Στο robust MDP, η δεύτερη αναπαρίσταται με σύνολο πιθανών μοντέλων και η πολιτική μεγιστοποιεί τη χειρότερη αναμενόμενη απόδοση. Η URBE προσθέτει Bayesian posterior uncertainty πάνω στις robust Q-values.

Για τη διπλωματική, αυτό υποδεικνύει ότι πρέπει να διαχωριστούν:

- **aleatoric uncertainty:** γνωστή stochasticity των transitions,
- **epistemic/model uncertainty:** ανεπαρκής γνώση του transition kernel,
- **non-stationarity:** πραγματική αλλαγή του kernel με τον χρόνο.

Ένας fixed robust baseline μπορεί να προστατεύεται έναντι ενός προκαθορισμένου uncertainty set, ενώ ένας adaptive agent πρέπει να χρησιμοποιεί νέα δεδομένα για detection ή/και αναθεώρηση της πολιτικής του.

## Περιορισμοί και απειλές εγκυρότητας

Τα theoretical αποτελέσματα αφορούν finite-horizon RMDPs, posterior assumptions και, σε σημεία, acyclic worst-case transition graphs. Η deep εκδοχή χρησιμοποιεί approximation και δεν κληρονομεί αυτομάτως όλες τις tabular εγγυήσεις. Τα πειράματα είναι λίγα και μικρής κλίμακας, ενώ η επιλογή uncertainty radii και priors επηρεάζει το αποτέλεσμα. Η CartPole αλλαγή αφορά μία φυσική παράμετρο και ένα change point· δεν αποδεικνύει robustness σε πολλαπλές ή άγνωστες αλλαγές. Επιπλέον, η DQN-URBE είναι βαρύτερη από έναν απλό tabular agent και πιθανόν υπερβολική ως υποχρεωτικό μοντέλο για το bounded GridWorld της διπλωματικής.

Η πηγή πρέπει συνεπώς να χρησιμοποιηθεί κυρίως για να αιτιολογήσει το adaptive-versus-fixed robust comparison, το conservativeness trade-off και τις time-resolved recovery curves. Δεν δικαιολογεί μόνη της την επιλογή DQN-URBE ως υλοποιημένου μοντέλου.

## Σχέση με άλλες πηγές

Το `SRC-81A15E6905` ορίζει action-level perturbations, ενώ η παρούσα πηγή αφορά κυρίως transition-model uncertainty και online αναθεώρηση robustness. Το `SRC-95C9DAEE68` διαχωρίζει detection από adaptation σε non-stationary environments. Το `SRC-3856071502` παρέχει ξεχωριστή Bayesian change-detection μέθοδο, χωρίς να προτείνει robust control policy. Το `SRC-0A4AFAC8E9` απαιτεί πολλαπλά seeds και uncertainty intervals για να αξιολογηθεί αν η ταχύτερη ανάκαμψη είναι στατιστικά αξιόπιστη.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** θεωρητικό υπόβαθρο, robust/adaptive RL, μοντέλο αβεβαιότητας, σχετικές εργασίες, πειραματικό πρωτόκολλο και threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** fixed worst-case robustness μπορεί να είναι υπερβολικά συντηρητικό· online uncertainty learning μπορεί να βελτιώσει adaptation· nominal performance και recovery after change πρέπει να μετρώνται χωριστά.
- **Πειραματική συνέπεια:** να υπάρχει τουλάχιστον ένας fixed/non-adaptive robust ή conservative baseline και ένας agent που συνεχίζει να ενημερώνεται μετά τη μεταβολή. Οι καμπύλες πρέπει να περιλαμβάνουν pre-change baseline, degradation, recovery trajectory και post-change plateau.
- **Τι δεν πρέπει να ισχυριστούμε:** ότι η URBE είναι η μοναδική ή καθολικά καλύτερη adaptive μέθοδος, ότι οι numerical τιμές του CartPole μεταφέρονται σε GridWorld ή ότι ένα Bayesian bonus αποτελεί από μόνο του πλήρη change detector.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη.
- **Έλεγχος πρωτοτύπου:** ελέγχθηκε το επίσημο UAI 2019 PDF και αντιπαραβλήθηκαν Abstract, Sections 1, 3–7, Figures 2–6 και Conclusion.
- **Απόφαση:** κύρια πηγή για το trade-off μεταξύ static robustness, exploration και online adaptation σε changing dynamics.
