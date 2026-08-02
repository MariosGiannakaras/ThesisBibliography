---
κωδικός: SRC-1B40F8B37A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Reinforcement Learning Journal 2025"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Collaboration Promotes Group Resilience in Multi-Agent RL

## Βιβλιογραφική ταυτότητα
Ilai Shraga, Guy Azran, Matthias Gerstgrasser, Ofir Abu, Jeffrey S. Rosenschein, Sarah Keren. Reinforcement Learning Journal, 2025.

## Σκοπός και ερευνητικό ερώτημα
Η εργασία εισάγει formal notion of **group resilience** για MARL και εξετάζει εάν η collaboration βοηθά ομάδες agents να ανακτούν performance μετά από unexpected bounded environmental perturbations.

Παρότι το algorithmic mechanism είναι multi-agent collaboration και άρα εκτός του βασικού single-agent implementation scope της διπλωματικής, η formalization της resilience είναι αρκετά γενική ώστε να προσθέτει ανεξάρτητη αξία στο experimental protocol.

## Μεθοδολογία και ορισμοί
Η εργασία θεωρεί reference MDP `M` και perturbed MDP `M'`, μαζί με distance measure `δ(M,M')` και bound `K` για τη severity της perturbation.

Δίνει τρεις σχετικές formulations:

1. **Relative-to-optimum resilience**: η normalized utility στο perturbed environment πρέπει να διατηρεί τουλάχιστον συγκεκριμένο κλάσμα της normalized utility στο original environment.
2. **Relative-to-origin resilience**: η utility στο perturbed environment συγκρίνεται απευθείας με την utility του ίδιου group στο original environment.
3. **Resilience in expectation**: το performance guarantee ορίζεται κατά μέσο όρο πάνω σε distribution από perturbed MDPs μέσα σε bounded distance.

Η εργασία επίσης αποσυνθέτει perturbations σε atomic αλλαγές transition function, reward function και initial state.

## Κύρια ευρήματα χρήσιμα για τη διπλωματική
### 1. Resilience χρειάζεται explicit perturbation severity
Η resilience δεν ορίζεται σε κενό: συνδέεται με ένα `K` που περιορίζει το μέγεθος της αλλαγής. Αυτό ενισχύει την ανάγκη της διπλωματικής να αναφέρει performance ως function of shift severity και όχι ένα ενιαίο “robustness score”.

### 2. Relative recovery metric μπορεί να είναι παραπλανητικό
Η εργασία επισημαίνει ότι ένα group/policy με ήδη πολύ χαμηλή original performance —π.χ. no-op policy— μπορεί να φαίνεται τεχνητά highly resilient επειδή δεν έχει πολύ performance να χάσει.

Αυτό είναι κρίσιμο για το thesis protocol: **resilience ratio / retained-performance fraction δεν πρέπει ποτέ να αναφέρεται χωρίς absolute pre-change και post-change utility**.

### 3. Perturbation type πρέπει να δηλώνεται
Transition, reward και initial-state perturbations έχουν διαφορετική causal semantics. Δεν πρέπει να συγχωνεύονται σε έναν γενικό όρο “environment change”.

### 4. Recovery/generalization distinction
Η εργασία διαχωρίζει resilience από standard generalization/transfer framing: ενδιαφέρεται για performance degradation/recovery μετά από perturbation και όχι μόνο final score σε unseen test task.

## Πειραματικό αντικείμενο
Η empirical contribution είναι MARL: collaboration protocols συγκρίνονται σε multi-agent benchmarks και η εργασία αναφέρει ότι collaborative variants εμφανίζουν υψηλότερη group resilience από non-collaborative counterparts στα συγκεκριμένα experiments.

Η empirical superiority της collaboration **δεν μεταφέρεται** στο single-agent thesis benchmark.

## Υποθέσεις και περιορισμοί
- Multi-agent Markov-game setting, όχι single-agent MDP benchmark.
- Group utility και collaboration μπορούν να δημιουργούν agent-induced non-stationarity που δεν υπάρχει στο thesis core.
- Η resilience formulation εξαρτάται από την επιλογή distance metric `δ` και perturbation bound `K`.
- Relative-to-origin score μπορεί να επιβραβεύσει κακή baseline performance αν δεν αναφέρεται absolute utility.
- Expected resilience εξαρτάται από τη distribution `Ψ` των perturbations και επομένως από το benchmark sampling design.

## Σχέση με άλλες πηγές
Συμπληρώνει τις resilience/recovery πηγές του corpus επειδή προσθέτει:
- explicit perturbation-distance parameter,
- relative-to-origin / relative-to-optimum distinction,
- formal warning για no-op/low-baseline pathology.

Δεν αντικαθιστά τις single-agent non-stationarity πηγές όπως `SRC-E5CA725A6C` και δεν δικαιολογεί MARL implementation.

## Χρήση στη διπλωματική
**Υποστηρικτική πηγή για metrics/protocol, όχι για agent mechanism.**

Κλειδώνει τις ακόλουθες απαιτήσεις:
1. Κάθε resilience ratio συνοδεύεται από absolute pre/post-change return.
2. Shift severity `K` ή ισοδύναμη domain-specific severity measure δηλώνεται ρητά.
3. Performance-vs-severity curve προτιμάται από ένα μόνο aggregate resilience score.
4. Initial-state, reward και transition perturbations αναφέρονται χωριστά.
5. Αν χρησιμοποιηθεί normalized-to-optimum score, δηλώνεται πώς προσεγγίζεται/υπολογίζεται το regime-specific optimum.
6. Expected resilience αναφέρει τη distribution των perturbations/seeds από την οποία υπολογίζεται.

## Απαιτούμενα αποσπάσματα
1. Resilience ως retained performance υπό bounded MDP perturbation.
2. Relative-to-optimum έναντι relative-to-origin normalization.
3. Low-performing/no-op policies μπορούν να φαίνονται ψευδώς resilient σε relative metric.
4. Transition/reward/initial-state perturbations είναι διακριτοί τύποι αλλαγής.

## Κατάσταση επαλήθευσης
Ελέγχθηκε το πλήρες stored RLJ 2025 paper. **Επιλέγεται ως υποστηρικτική metric source με ρητό MARL caveat.**