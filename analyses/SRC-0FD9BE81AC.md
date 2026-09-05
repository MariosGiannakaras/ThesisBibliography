---
κωδικός: SRC-0FD9BE81AC
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "ICML 2025, PMLR 267:38397–38423; official PMLR/author manuscript"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-09-05"
---

# Continual Reinforcement Learning by Planning with Online World Models

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Zichen Liu, Guoji Fu, Chao Du, Wee Sun Lee, Min Lin
- **Έτος:** 2025
- **Έκδοση:** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, pp. 38397–38423
- **Τύπος:** peer-reviewed πρωτογενής εργασία continual/model-based reinforcement learning
- **Ρόλος:** υποστηρικτική
- **Επίσημη έκδοση που ελέγχθηκε:** PMLR publication/full paper και matching arXiv:2507.09177

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει continual reinforcement learning ως ακολουθία tasks που παρουσιάζονται διαδοχικά και όπου ο agent πρέπει να αποκτά νέες ικανότητες χωρίς να ξεχνά παλιές. Το βασικό πρόβλημα είναι catastrophic forgetting. Οι συγγραφείς προτείνουν να μεταφερθεί το persistent knowledge σε ένα online world model και η επιλογή ενεργειών να γίνεται με model predictive control, αντί η long-term ικανότητα να εξαρτάται αποκλειστικά από μια βαθιά task policy που ανανεώνεται διαδοχικά.

Για τη διπλωματική, η πηγή είναι χρήσιμη επειδή δίνει πρόσφατο peer-reviewed όριο για το τι σημαίνει πραγματικά model-based continual adaptation. Δεν αποτελεί όμως paper για tabular Dyna-Q+ ούτε αξιολογεί το ίδιο disturbance protocol. Η αξία της βρίσκεται στη σύγκριση μηχανισμών: online model maintenance, planning, forgetting, transfer και task-sequence evaluation.

## Μεθοδολογία

Οι συγγραφείς μαθαίνουν ένα shallow Follow-The-Leader online world model που ανανεώνεται από τις πραγματικές interactions και χρησιμοποιούν model predictive control με planning πάνω στο πιο πρόσφατο μοντέλο. Το resulting FTL Online Agent δεν αποθηκεύει task-specific policies ως κύριο persistence mechanism: η reusable γνώση βρίσκεται στη dynamics model και διαφορετικά tasks ορίζονται μέσω reward functions.

Η εργασία εισάγει επίσης το Continual Bench, ένα dedicated CRL benchmark με έξι manipulation tasks που μοιράζονται κοινό state/action representation και unified physical dynamics. Η αξιολόγηση εξετάζει τόσο acquisition νέων tasks όσο και retention προηγούμενων, δηλαδή forgetting/transfer αντί μόνο τελικής επίδοσης στο πιο πρόσφατο task. Τα experiments συγκρίνουν το Online Agent με deep world-model baselines και continual-learning mitigations υπό κοινό model-planning framework.

## Κύρια ευρήματα

1. **Catastrophic forgetting είναι ξεχωριστό evaluation axis από την ικανότητα να μάθει κανείς το επόμενο task.** Ένας continual agent πρέπει να αξιολογείται και σε προηγούμενες ικανότητες.
2. **Ένα online world model μπορεί να λειτουργήσει ως persistent shared knowledge component.** Η προτεινόμενη μέθοδος ενημερώνει σταδιακά dynamics knowledge και το planner χρησιμοποιεί το πιο πρόσφατο model για acting.
3. **Το model-based continual RL δεν ταυτίζεται με Dyna-style synthetic replay.** Η εργασία συζητά προηγούμενη Dyna-based προσέγγιση όπου synthetic model data ενημερώνουν model-free value/policy components και διαχωρίζει αυτή την αρχιτεκτονική από planning directly through the current world model.
4. **Benchmark design για CRL χρειάζεται retention και transfer.** Το Continual Bench περιλαμβάνει sequence of six tasks με κοινή dynamics structure ώστε να μπορούν να εξεταστούν forgetting και transfer.
5. **Η empirical claim της εργασίας είναι περιορισμένη στο δικό της benchmark/method family.** Δεν μεταφέρεται ως numerical ή ranking evidence για Q-learning, SARSA, DQN, PPO ή Dyna-Q+ στο thesis GridWorld.

## Σχέση με Dyna και το thesis experiment

Η πηγή είναι ιδιαίτερα χρήσιμη για να αποφευχθεί ένας υπεραπλουστευμένος ισχυρισμός ότι “model-based RL = Dyna-Q+”. Το Dyna-Q+ της διπλωματικής είναι tabular method που συνδυάζει direct updates, learned model, planning updates και exploration bonus. Το Liu et al. χρησιμοποιεί online world-model learning και MPC/CEM-style planning χωρίς να είναι η ίδια algorithmic family ή implementation. Συνεπώς η σύγκριση είναι conceptual: και τα δύο αξιοποιούν learned dynamics, αλλά διαφέρουν ως προς representation, planning interface, continual objective, retained state και evaluation regime.

Η πηγή ενισχύει επίσης το limitation ότι το thesis protocol εξετάζει adaptation/recovery μετά από ελεγχόμενη αλλαγή αλλά δεν αποτελεί πλήρες CRL benchmark: δεν επανεξετάζει μια μεγάλη ακολουθία παλιών tasks ώστε να μετρήσει forgetting, forward transfer και backward transfer ως primary outcomes.

## Περιορισμοί και απειλές εγκυρότητας

- Το Continual Bench είναι περιορισμένο σε episodic setting με explicit task switches μεταξύ episodes.
- Η proposed world model αφορά moderate-dimensional state-based observations και δεν μοντελοποιεί world uncertainty στην τρέχουσα μορφή.
- Το planning framework δεν ενσωματώνει explicit exploration ως μέρος της κύριας μεθόδου.
- Η unified-dynamics assumption και η αλλαγή reward-defined tasks διαφέρουν από persistent action-remap, no-op action failure και observation corruption.
- Τα αποτελέσματα σε robotic manipulation δεν τεκμηριώνουν ranking σε discrete GridWorld.
- Η no-forgetting theoretical property αφορά τη συγκεκριμένη FTL shallow-model construction και τις παραδοχές της, όχι κάθε world-model ή Dyna method.

## Χρήση στη διπλωματική

- **Κεφάλαιο 2 / Related Work:** πρόσφατη peer-reviewed model-based continual RL προσέγγιση και διάκριση online world models από Dyna-style synthetic planning.
- **Κεφάλαιο 3 / Scope:** αποσαφήνιση ότι το δικό μας post-change adaptation protocol δεν είναι πλήρες multi-task CRL evaluation.
- **Κεφάλαιο 6 / Discussion:** model retention, replay/model freshness, forgetting και transfer ως μηχανισμοί που δεν μετρώνται πλήρως από ένα μόνο post-change outcome.
- **Κεφάλαιο 7 / Future Work:** repeated task sequences, explicit forgetting/transfer metrics και richer online world-model comparators.

Δεν χρησιμοποιείται για να υποστηρίξει ότι το Dyna-Q+ της διπλωματικής είναι ισοδύναμο με OA, ότι τα αποτελέσματα του Continual Bench μεταφέρονται στο GridWorld ή ότι οποιαδήποτε model-based method είναι γενικά ανώτερη.

## Απόφαση

**Επαληθευμένη — εξαγωγή ναι ως υποστηρικτική πηγή.** Προσθέτει πρόσφατη peer-reviewed τεκμηρίωση για model-based continual adaptation, forgetting/transfer και online world-model persistence, με σαφή διάκριση από το thesis Dyna-Q+ και το frozen Phase-B protocol.
