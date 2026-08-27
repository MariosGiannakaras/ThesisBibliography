---
κωδικός: SRC-8D4F62D85D
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI-18 / arXiv:1709.06560"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Deep Reinforcement Learning That Matters

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, David Meger
- **Έτος:** 2018
- **Τύπος:** peer-reviewed empirical/reproducibility study
- **Δημοσίευση:** AAAI-18

## Σκοπός και συνάφεια

Η εργασία εξετάζει γιατί αποτελέσματα deep RL μπορούν να αλλάξουν αισθητά με random seeds, hyperparameters, implementation details, architectures και reporting choices. Για το protocol-v2 είναι κυρίως evidence κατά μιας ασύμμετρης σύγκρισης όπου οι tabular μέθοδοι είναι ώριμα tuned ενώ DQN/PPO/A2C εκτελούνται με library defaults ή λίγα ευνοϊκά seeds.

## Κύρια σημεία που υποστηρίζονται άμεσα

1. **Random seeds και intrinsic variance μπορούν να αλλάξουν εμφανώς το reported αποτέλεσμα.** Μία ή λίγες επιλεγμένες εκτελέσεις δεν επαρκούν για claim υπεροχής.
2. **Hyperparameter και implementation sensitivity είναι ουσιαστικό μέρος της deep-RL σύγκρισης.** Αλλαγές σε architecture, reward scaling ή codebase μπορούν να επηρεάσουν το αποτέλεσμα.
3. **Η αναφορά μόνο των καλύτερων runs δημιουργεί υπεραισιόδοξη εικόνα.** Η κατανομή των stochastic runs και uncertainty πρέπει να διατηρούνται.
4. **Η reproducibility απαιτεί ακριβή reporting του experimental setup.** Algorithm name μόνο του δεν προσδιορίζει μία αναπαραγώγιμη deep-RL υλοποίηση.

## Τι δεν αποδεικνύει

- Δεν αποδεικνύει ότι DQN/PPO/A2C είναι ακατάλληλα για μικρό GridWorld.
- Δεν επιβάλλει ίδια hyperparameters μεταξύ διαφορετικών algorithms.
- Δεν ορίζει ένα μοναδικό δίκαιο tuning budget ή τον τελικό αριθμό roots.
- Δεν εξετάζει ειδικά abrupt environment-change resilience ή Frozen/Continual branches.

## Εφαρμογή στο protocol-v2

- Κάθε deep method πρέπει να έχει version-pinned implementation, πλήρες resolved config, architecture, optimizer/update semantics και seed provenance.
- Η tuning opportunity πρέπει να είναι συγκρίσιμη με τις άλλες μεθόδους και να μη βασίζεται σε “default = neutral”.
- Τα final results πρέπει να περιλαμβάνουν independent roots, uncertainty/effect sizes και failed/unstable runs.
- Οι algorithm adapters πρέπει να αποθηκεύουν ακριβές scientific state για reproducible continuation, όχι απλώς inference weights όταν το Continual regime απαιτεί resume training.

## Περιορισμοί

Η εργασία προέρχεται από παλαιότερη γενιά deep-RL benchmarks και δεν καθορίζει τις σύγχρονες library APIs. Χρησιμοποιείται για empirical-design/reproducibility principles, όχι ως απόδειξη για την επίδοση συγκεκριμένου SB3 version ή για τη συμπεριφορά στο thesis GridWorld.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Μεθοδολογία, Deep RL implementation, Αναπαραγωγιμότητα, Threats to validity.
- **Ρόλος:** κύρια/υποστηρικτική μεθοδολογική πηγή.
- **Ισχυρισμοί:** sensitivity σε seeds/hyperparameters/implementation και ανάγκη standardized reporting.
- **Μη ισχυρισμοί:** algorithm superiority ή resilience guarantee.
