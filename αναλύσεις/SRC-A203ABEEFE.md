# SRC-A203ABEEFE — Prioritized Experience Replay

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Tom Schaul, John Quan, Ioannis Antonoglou, David Silver
- **Έκδοση:** ICLR 2016 / arXiv:1511.05952
- **Τύπος:** primary deep RL replay method
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Αντικείμενο

Η εργασία μελετά ποια transitions από replay memory πρέπει να επαναχρησιμοποιούνται συχνότερα. Αντί για uniform replay, προτεραιοποιεί transitions με μεγάλο TD error ως proxy για learning progress/surprise, με stochastic prioritization και importance-sampling correction.

## Κύρια αποτελέσματα

- Replay memory σπάει temporal correlations και επιτρέπει reuse παλαιών/σπάνιων experiences.
- TD-error prioritization επιταχύνει learning σε σχέση με uniform replay σε benchmark settings της εργασίας.
- Pure greedy prioritization μπορεί να μειώσει diversity και να υπεραντιδρά σε noisy TD-error spikes.
- Stochastic prioritization διατηρεί non-zero probability για όλα τα transitions.
- Non-uniform replay εισάγει sampling bias, που αντιμετωπίζεται με importance-sampling weights.

## Συνάφεια με non-stationary RL

Η εργασία δεν μελετά environmental changepoints, αλλά είναι κρίσιμη για replay-based agents επειδή μετά από αλλαγή το replay buffer περιέχει mixture από **pre-change stale** και **post-change current** transitions.

Το μεγάλο TD error μετά από changepoint μπορεί να κάνει το prioritized replay να εστιάσει γρήγορα σε νέα samples, αλλά μπορεί επίσης να κρατά υψηλή προτεραιότητα σε παλιά inconsistent transitions. Επομένως δεν πρέπει να θεωρηθεί εκ των προτέρων ότι PER βοηθά adaptation.

## Πρωτόκολλο που προκύπτει

Για replay-based agents μετά από environmental change καταγράφονται:

- buffer size,
- age distribution των sampled transitions,
- fraction pre-change/post-change samples ανά minibatch,
- sampling priority ανά regime,
- TD-error distribution χωριστά για stale/current data,
- replay ratio,
- buffer reset/flush policy,
- importance-sampling parameters,
- memory και compute overhead.

Απαιτούνται ablations:

1. no replay,
2. uniform replay,
3. prioritized replay,
4. buffer reset at true changepoint — oracle upper bound,
5. detector-triggered buffer reset — non-oracle variant.

## Περιορισμοί

- Primary experiments αφορούν stationary Atari tasks.
- TD error είναι learning signal/surprise proxy, όχι calibrated change detector.
- High TD error μπορεί να προκύψει από stochastic rewards/noise και όχι regime change.
- Deep replay architecture δεν είναι αναγκαία για τον tabular core.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Χρησιμοποιείται κυρίως για replay-memory diagnostics και για να τεκμηριωθεί ότι sampling priority, stale data και replay bias αποτελούν ανεξάρτητους μηχανισμούς που πρέπει να ελέγχονται σε non-stationary experiments.