---
κωδικός: SRC-CBA29E303A
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PMLR 119, ICML 2020 official article page/abstract"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# Revisiting Fundamentals of Experience Replay

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** William Fedus, Prajit Ramachandran, Rishabh Agarwal, Yoshua Bengio, Hugo Larochelle, Mark Rowland, Will Dabney
- **Έτος:** 2020
- **Τύπος:** peer-reviewed πρωτογενής εμπειρική εργασία deep RL
- **Δημοσίευση:** Proceedings of the 37th International Conference on Machine Learning, PMLR 119:3061–3071

## Σκοπός και συνάφεια

Η εργασία μελετά συστηματικά δύο βασικές ιδιότητες του experience replay σε off-policy Q-learning methods: replay capacity και replay ratio, δηλαδή τον λόγο learning updates προς collected experience. Είναι άμεσα σχετική με το protocol-v2 DQN adapter, επειδή αυτές οι επιλογές επηρεάζουν το learning system και δεν πρέπει να κρύβονται ως αόρατα library defaults.

## Κύρια σημεία που υποστηρίζονται άμεσα

1. **Replay capacity μπορεί να αλλάξει performance.** Η μελέτη βρίσκει ότι μεγαλύτερη capacity βελτιώνει ουσιαστικά ορισμένους algorithms ενώ άλλους τους αφήνει σχεδόν ανεπηρέαστους.
2. **Replay ratio είναι consequential experimental quantity.** Οι συγγραφείς ελέγχουν άμεσα τον αριθμό learning updates σε σχέση με τη νέα environment experience και δείχνουν ότι αποτελεί σημαντικό παράγοντα σε διαφορετικούς deep-RL algorithms.
3. **Το replay δεν είναι απλή αποθήκευση.** Capacity και update-to-experience cadence αποτελούν μέρος της πραγματικής learning dynamics του off-policy system.

## Εφαρμογή στο protocol-v2

Για DQN πρέπει να είναι ρητά resolved/frozen και persisted:

- replay-buffer capacity;
- logical size/cursor και πλήρες buffer content στο scientific checkpoint;
- replay sampling RNG/policy;
- warm-up / `learning_starts`;
- batch size;
- train frequency και gradient/update count, από τα οποία προκύπτει το πραγματικό replay/update ratio;
- target-network update cadence;
- interaction counter που αποτελεί την common scientific budget authority.

Replay reset, clearing old data, recency weighting ή αλλαγή replay ratio μετά το changepoint είναι ξεχωριστές interventions και δεν επιτρέπεται να εμφανίζονται ως implementation convenience στο default Adaptive branch.

## Περιορισμοί

Η εργασία δεν καθορίζει τη βέλτιστη buffer capacity ή replay ratio για το thesis GridWorld και δεν αφορά ειδικά resilience μετά από action remapping. Τα environment-specific empirical findings δεν μεταφέρονται ως αναμενόμενη κατάταξη. Η πηγή υποστηρίζει ότι replay configuration/state είναι scientifically consequential, όχι ποια ακριβώς τιμή πρέπει να επιλεγεί.

## Χρήση στη διπλωματική

- **Κεφάλαια:** DQN/background, μεθοδολογία, fair configuration, checkpoint/provenance, threats to validity.
- **Ρόλος:** κύρια μεθοδολογική πηγή για DQN replay identity.
- **Ισχυρισμοί:** replay capacity/replay ratio matter and require explicit control/reporting.
- **Μη ισχυρισμοί:** συγκεκριμένη final buffer size/ratio ή post-change replay intervention.
