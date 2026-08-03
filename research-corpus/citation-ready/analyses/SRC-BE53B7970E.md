---
κωδικός: SRC-BE53B7970E
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "AAAI 2016 / arXiv:1509.06461"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επιστημονική ανάλυση — SRC-BE53B7970E

## Βιβλιογραφική ταυτότητα
- **Τίτλος:** Deep Reinforcement Learning with Double Q-learning
- **Συγγραφείς:** Hado van Hasselt, Arthur Guez, David Silver
- **Δημοσίευση:** AAAI 2016
- **Ρόλος:** υποστηρικτική / neural-baseline reference

## Σκοπός
Η εργασία εξετάζει το systematic overestimation που προκαλεί ο max operator του Q-learning όταν οι action-value estimates περιέχουν σφάλμα και μεταφέρει την ιδέα Double Q-learning στο DQN.

## Μεθοδολογία
Το DQN χρησιμοποιεί τις ίδιες estimated values για selection και evaluation του maximizing action. Το Double DQN αποσυνδέει αυτά τα δύο βήματα: το online network επιλέγει το action και το target network το αξιολογεί. Η εργασία αναλύει θεωρητικά το maximization bias και το αξιολογεί εμπειρικά σε Atari.

## Κύρια ευρήματα
1. Το DQN μπορεί να υπερεκτιμά σημαντικά action values ακόμη και σε deterministic environments.
2. Estimation error οποιασδήποτε προέλευσης μπορεί να τροφοδοτήσει maximization bias· η εργασία αναφέρει ρητά function approximation, noise και non-stationarity ως πιθανές πηγές ανακρίβειας.
3. Η αποσύνδεση selection/evaluation μειώνει τις υπερεκτιμήσεις.
4. Στα εξεταζόμενα Atari games, Double DQN βελτιώνει value accuracy και σε αρκετές περιπτώσεις performance.

## Σχέση με τη διπλωματική
Η πηγή δεν αποτελεί adaptation mechanism. Είναι όμως σημαντική για **baseline fairness** εάν προστεθεί neural value-based agent:
- plain DQN μπορεί να υποφέρει από maximization bias που δεν σχετίζεται με resilience,
- μετά από changepoint τα transient value errors μπορούν να αυξηθούν,
- άρα η σύγκριση resilience δεν πρέπει να αποδίδει σε adaptation mechanism μια αποτυχία που οφείλεται σε γνωστό Q-estimation bias.

## Πειραματικές επιπτώσεις
Εάν υπάρχει DQN-family comparator:
- προτιμάται Double DQN ως βασικός neural value-based baseline ή τουλάχιστον ως ablation,
- αναφέρονται mean/max Q estimates και realized returns,
- καταγράφεται overestimation gap πριν και μετά από changepoint,
- replay, target-network update interval και architecture κρατούνται κοινά,
- Double DQN δεν χαρακτηρίζεται resilient χωρίς ξεχωριστές recovery metrics.

## Περιορισμοί
- Atari, όχι controlled repeated GridWorld changepoints.
- Δεν ανιχνεύει αλλαγές και δεν αλλάζει memory/learning rate/context.
- Η βελτίωση αφορά Q-estimation bias, όχι continual learning ή forgetting.
- Δεν δικαιολογεί από μόνη της inclusion neural agents αν resource budget δεν το επιτρέπει.

## Απόφαση
**Επαληθευμένη — εξαγωγή ναι ως υποστηρικτική πηγή.** Χρησιμοποιείται για neural baseline design και overestimation diagnostics, όχι ως resilience algorithm.