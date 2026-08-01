---
κωδικός: SRC-CA06A28C0B
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI-20, Open-World Learning for Radically Autonomous Agents"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επιστημονική ανάλυση — SRC-CA06A28C0B

## Βιβλιογραφική ταυτότητα
Pat Langley, **Open-World Learning for Radically Autonomous Agents**, Proceedings of the AAAI Conference on Artificial Intelligence, AAAI-20, 2020.

- **Ρόλος στη διπλωματική:** υποστηρικτική

## Σκοπός και ερευνητικό πρόβλημα
Η εργασία διατυπώνει το open-world learning ως πρόβλημα όπου ένας autonomous agent διαθέτει επαρκή αρχική expertise, αλλά συναντά **αιφνίδιες, μη ανακοινωμένες και μακρόχρονες αλλαγές** που υποβαθμίζουν την επίδοσή του. Ο agent πρέπει, με περιορισμένη νέα εμπειρία, να εντοπίσει πότε άλλαξε το περιβάλλον και να αναθεωρήσει την expertise του αρκετά γρήγορα ώστε να επαναφέρει αποδεκτή λειτουργία.

Η διατύπωση είναι ευρύτερη από reinforcement learning και δεν προτείνει έναν συγκεκριμένο RL algorithm. Παρ' όλα αυτά είναι εξαιρετικά συμβατή με το thesis protocol επειδή χωρίζει ρητά monitoring/change detection, diagnosis και repair/adaptation.

## Αρχιτεκτονική διάκριση
Η εργασία περιγράφει τέσσερις λειτουργίες:
1. **performance element** που εκτελεί την τρέχουσα expertise,
2. **monitoring element** που συγκρίνει observations με expectations και εντοπίζει anomalies,
3. **diagnostic element** που απομονώνει πιθανές αιτίες της αποτυχίας,
4. **repair element** που αναθεωρεί την υπεύθυνη expertise.

Αυτό παρέχει ισχυρό conceptual support για το ήδη κλειδωμένο thesis boundary **detector ≠ adapter**. Η monitoring evidence δεν αποτελεί από μόνη της policy recovery και η repair quality δεν πρέπει να συγχέεται με detection accuracy.

## Taxonomy περιβαλλοντικών αλλαγών
Η εργασία προτείνει framework μετασχηματισμών που μπορούν να αλλάζουν:
- χωρικά/χρονικά fields και παραμέτρους,
- object categories και attributes,
- physical/control/perceptual processes,
- constraints, goals και values.

Για το GridWorld αυτό δικαιολογεί να μην αντιμετωπίζονται όλες οι novelties ως ένας ενιαίος scalar perturbation. Reward semantics, transition dynamics, action capabilities, observation process και structural constraints είναι διαφορετικές κατηγορίες αλλαγής.

## Evaluation design
Ιδιαίτερα χρήσιμη είναι η πρόταση για **novelty response curves**: performance plotted over time με σημειωμένα novelty events, ώστε να φαίνεται η πτώση μετά την αλλαγή και η επακόλουθη recovery/adaptation. Η εργασία υπογραμμίζει επίσης ότι detection time και rate of performance improvement after detection πρέπει να μετρώνται ξεχωριστά.

Προτείνει ακόμη ως experimental variables:
- τύπο novelty,
- συχνότητα εισαγωγής novelty,
- αριθμό αλλαγών,
- randomized novelty timing ώστε ο agent να μην μπορεί να προβλέψει το changepoint.

## Σχέση με τη διπλωματική
Η πηγή προσθέτει άμεσα methodological support για:
- unannounced changepoints,
- detector/diagnosis/repair separation,
- multiple shift families,
- recovery curves,
- detection delay χωριστά από adaptation rate,
- randomization του changepoint timing,
- repeated changes χωρίς full relearning from scratch.

Δεν απαιτείται να υλοποιηθεί η πλήρης symbolic/open-world architecture της εργασίας.

## Περιορισμοί και απειλές εγκυρότητας
- Position/framework paper και όχι matched empirical RL benchmark.
- Δεν δίνει συγκεκριμένο learning algorithm ή quantitative detector baseline.
- Η expertise μπορεί να είναι symbolic/model-based και όχι value-function policy.
- Οι προτεινόμενες novelty κατηγορίες είναι ευρύτερες από το resource-aware GridWorld scope.
- Δεν τεκμηριώνει ότι monitoring/diagnosis architecture υπερέχει ενός απλού statistical changepoint detector.

## Χρήση στη διπλωματική
Χρησιμοποιείται ως **υποστηρικτική πηγή για problem formulation και evaluation protocol**, ειδικά για τη διάκριση detection–repair και για novelty-response curves. Δεν χρησιμοποιείται για να αποδοθεί algorithmic superiority σε συγκεκριμένο agent.

## Απόφαση
**Επιλογή ως υποστηρικτική πηγή.**
