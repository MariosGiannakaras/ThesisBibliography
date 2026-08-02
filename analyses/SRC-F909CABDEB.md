---
κωδικός: SRC-F909CABDEB
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2506.21872, survey preprint"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-30"
---

# A Survey of Continual Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Chaofan Pan, Xin Yang, Yanhua Li, Wei Wei, Tianrui Li, Bo An, Jiye Liang
- **Έτος:** 2025
- **Τύπος πηγής:** πρόσφατη survey/preprint εργασία
- **DOI / arXiv / URL:** arXiv:2506.21872
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-F909CABDEB.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η survey οργανώνει το πεδίο continual reinforcement learning (CRL), όπου ένας persistent agent αντιμετωπίζει ακολουθία σχετικών μη στάσιμων tasks χωρίς restart από το μηδέν. Εξετάζει challenges, scenario settings, metrics, benchmarks και method taxonomy με βάση το είδος γνώσης που αποθηκεύεται ή μεταφέρεται.

Για τη διπλωματική, η βασική αξία της είναι η αποσαφήνιση ότι adaptation σε νέο περιβάλλον δεν αρκεί: πρέπει να εξετάζεται ταυτόχρονα η διατήρηση προηγούμενης γνώσης, η απόκτηση νέας συμπεριφοράς και το resource cost. Ωστόσο η επίσημη εργασία μας μπορεί να είναι στενότερη από πλήρες CRL, ιδίως αν αξιολογεί ένα task με perturbations και όχι μεγάλη ακολουθία διακριτών tasks.

## Σύνοψη

Η survey περιγράφει την τριγωνική ισορροπία stability–plasticity–scalability. Stability είναι η διατήρηση επίδοσης σε παλαιότερα tasks, plasticity η μάθηση και μεταφορά σε νέα tasks, και scalability η δυνατότητα να συνεχίζεται η διαδικασία με περιορισμένη μνήμη και υπολογισμό. Κατηγοριοποιεί scenarios σε lifelong adaptation, non-stationarity learning, task-incremental learning και task-agnostic learning, ανάλογα με το τι αλλάζει και αν task identities/boundaries είναι ορατά.

Παρουσιάζει standardized sequence-level metrics: average performance, forgetting, forward transfer, backward transfer και resource proxies. Η taxonomy των methods βασίζεται στο τι αποθηκεύεται ή μεταφέρεται: policy, experience, dynamics ή reward. Τονίζει ότι δεν υπάρχει ενιαίο benchmark ή καθολική scalability metric και ότι οι definitions/metrics εξαρτώνται από το scenario protocol.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** βιβλιογραφική ανασκόπηση CRL methods και benchmarks όπως Continual World, CRL Maze, Lifelong Hanabi, L2Explorer, CORA και COOM.
- **Μοντέλα / αλγόριθμοι:** policy-focused, experience-focused, dynamics-focused και reward-focused οικογένειες.
- **Baselines:** single-task training, fine-tuning/restart και benchmark-native continual baselines, ανάλογα με το examined work.
- **Μετρικές:** average performance A_N, forgetting FG, forward transfer FT μέσω AUC σε σχέση με single-task baseline, backward transfer BWT, sample efficiency, memory/model size και compute overhead.
- **Πειραματική διαδικασία:** δεν εκτελεί ενιαίο νέο benchmark· συνθέτει definitions, scenarios, metrics και reported evidence από τη βιβλιογραφία.

## Κύρια ευρήματα

1. **CRL απαιτεί ισορροπία stability, plasticity και scalability.** Αποκλειστική βελτιστοποίηση adaptation μπορεί να προκαλέσει forgetting, ενώ πλήρης αποθήκευση όλων των policies/data παραβιάζει resource constraints. Τεκμηρίωση: Section III-B και Figure 3.
2. **Το scenario definition καθορίζει τι πρέπει να μετρηθεί.** Non-stationarity learning, task-incremental και task-agnostic settings διαφέρουν ως προς changes και task-boundary availability. Τεκμηρίωση: Section III-E και Table III.
3. **Average performance δεν αρκεί.** Forgetting, forward transfer και backward transfer αποκαλύπτουν αν μια μέθοδος διατηρεί παλιές ικανότητες ή επιταχύνει τη μάθηση νέων tasks. Τεκμηρίωση: Section III-C, Equations 7–10.
4. **Forward transfer πρέπει να συγκρίνεται με single-task baseline.** Η AUC-based metric εξετάζει αν prior knowledge επιταχύνει τη μάθηση, όχι μόνο αν το τελικό score είναι υψηλό. Τεκμηρίωση: Section III-C, Equation 9.
5. **Η resource χρήση είναι μέρος της αξιολόγησης.** Model size, replay memory, environment interactions, wall-clock cost και per-step overhead είναι αναγκαία context για scalability claims. Τεκμηρίωση: Section III-C.
6. **Δεν υπάρχει ένα ιδανικό benchmark ή ενιαία metric suite.** Task order, sequence length, observation type και task-boundary assumptions διαφοροποιούν τα benchmarks. Τεκμηρίωση: Sections III-D–III-E.

## Υποθέσεις και ορισμοί

Η survey χρησιμοποιεί γενική time-indexed CRL formulation όπου state/action/reward/transition/observation components μπορούν να αλλάζουν, αλλά πολλά practical benchmarks είναι piecewise-stationary task sequences. Το p_i,j εκφράζει normalized performance στο task j μετά από training έως task i. Forgetting συγκρίνει προηγούμενη με τελική επίδοση, ενώ forward transfer συγκρίνει learning AUC με single-task-from-scratch baseline.

Στη διπλωματική, repeated configurations του ίδιου GridWorld μπορούν να θεωρηθούν non-stationarity stream. Αν δεν επανεξετάζονται παλιές configurations, δεν πρέπει να ισχυριστούμε πλήρες continual learning· θα πρόκειται κυρίως για lifelong adaptation ή non-stationary RL.

## Περιορισμοί και απειλές εγκυρότητας

Η πηγή είναι survey preprint και περιλαμβάνει πολύ πρόσφατες εργασίες με ετερογενή peer-review status. Δεν παρέχει κοινή reimplementation ή meta-analysis effect sizes. Οι taxonomy categories αλληλεπικαλύπτονται και οι reported metrics δεν χρησιμοποιούνται ομοιόμορφα. Η έννοια task μπορεί να είναι τεχνητή όταν οι boundaries είναι άγνωστες ή οι changes gradual. Το πλήρες CRL evaluation μπορεί να υπερβεί το scope/hardware της διπλωματικής. Τέλος, retention σε παλιότερα tasks δεν είναι ταυτόσημο με άμεση recovery μετά από perturbation, παρότι οι δύο έννοιες σχετίζονται.

## Σχέση με άλλες πηγές

Το `SRC-95C9DAEE68` παρέχει συγκεκριμένα detection–adaptation algorithms και repeated-change experiments. Η παρούσα survey δίνει ευρύτερη taxonomy και retention/transfer metrics. Το `SRC-0A4AFAC8E9` προσθέτει uncertainty-aware statistical reporting, ενώ το `SRC-0882A9B2B0` διαχωρίζει interpolation και extrapolation.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** θεωρητικό υπόβαθρο, σχετικές εργασίες, μετρικές, επιλογή models και limitations.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** adaptation πρέπει να εξετάζεται μαζί με stability και resource cost· repeated task streams χρειάζονται forgetting/transfer metrics· task-boundary availability είναι κρίσιμη experimental assumption.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι η διπλωματική υλοποιεί πλήρες CRL αν δεν αξιολογεί retention σε task sequence, ότι μία taxonomy είναι οριστική ή ότι όλες οι surveyed methods είναι peer-reviewed και ισοδύναμα τεκμηριωμένες.
- **Ρόλος:** υποστηρικτική

## Απαιτούμενα αποσπάσματα

Καταγράφηκαν τεκμήρια για stability–plasticity–scalability, scenario taxonomy, forgetting/transfer metrics, resource reporting και scope boundaries.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** να αποφασιστεί αν το final protocol θα επανεξετάζει προηγούμενες environment configurations, ώστε να δικαιολογούνται forgetting και backward-transfer metrics.