---
κωδικός: SRC-71F2ECA651
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "NeurIPS 13 / NIPS 2000 official proceedings PDF, 7 σελίδες"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Jun Morimoto, Kenji Doya
- **Έτος:** 2000 για το συνέδριο· συχνά αναφέρεται ως proceedings 2001
- **Τύπος πηγής:** θεμελιώδης πρωτογενής εργασία robust reinforcement learning
- **DOI / arXiv / URL:** https://proceedings.neurips.cc/paper/2000/hash/e8dfff4676a47048d6f0c4ef899593dd-Abstract.html
- **Πρωτότυπο που ελέγχθηκε:** επίσημο NeurIPS proceedings PDF

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εισάγει reinforcement-learning formulation που λαμβάνει ρητά υπόψη input disturbances και model mismatch. Το ερώτημα είναι αν online learning μπορεί να βρει control policy με καλύτερη worst-case επίδοση από standard RL όταν το πραγματικό σύστημα αποκλίνει από το μοντέλο εκπαίδευσης.

## Σύνοψη

Οι συγγραφείς αξιοποιούν ιδέες από `H∞` control και διατυπώνουν differential game μεταξύ actor και disturber. Ο actor επιλέγει control input, ενώ ο disturber επιλέγει worst-case disturbance. Η λύση είναι minimax value function που ισορροπεί output deviation και μέγεθος disturbance. Προτείνονται online learning rules για value function, worst disturbance και best control. Η μέθοδος ελέγχεται σε inverted pendulum, αρχικά σε linear setting και στη συνέχεια σε nonlinear swing-up με αλλαγές βάρους και τριβής.

Η πηγή είναι ιστορικά σημαντική επειδή δείχνει ότι robust RL δεν προέκυψε απλώς ως σύγχρονο adversarial-training trend: η βασική ιδέα της ρητής αντιπαράθεσης policy και disturbance υπάρχει ήδη στην πρώιμη βιβλιογραφία.

## Μεθοδολογία

- **Δεδομένα ή περιβάλλον:** linear και nonlinear inverted-pendulum control.
- **Μοντέλα / αλγόριθμοι:** robust RL με actor–disturber minimax formulation και standard RL comparator.
- **Baselines:** analytical linear `H∞` solution και conventional RL controller.
- **Μετρικές:** σταθερότητα/ποιότητα ελέγχου υπό αλλαγές μοντέλου, output deviation και disturbance penalty.
- **Πειραματική διαδικασία:** online learning της value function και των actor/disturber policies, έπειτα αξιολόγηση υπό μεταβολές βάρους και τριβής του pendulum.

## Κύρια ευρήματα

1. **Η robust objective πρέπει να δηλώνει ρητά τι θεωρεί disturbance και ποιο worst-case trade-off βελτιστοποιεί.** Τεκμηρίωση: Abstract και Ενότητα 1, PDF σελ. 1.
2. **Η robust policy μπορεί να διατυπωθεί ως minimax game actor–disturber.** Ο disturber αναζητά δυσμενή input perturbation και ο actor control που περιορίζει την απόκλιση. Τεκμηρίωση: formulation sections, PDF σελ. 2–4.
3. **Στο linear case, η learned λύση συμφωνεί με analytical `H∞` control.** Αυτό λειτουργεί ως validation against known solution. Τεκμηρίωση: experimental section, PDF σελ. 4–5.
4. **Στο nonlinear inverted pendulum, η robust policy αντέχει καλύτερα αλλαγές βάρους και friction από standard RL.** Τεκμηρίωση: results, PDF σελ. 5–7.
5. **Η εργασία μελετά robustness σε model mismatch, όχι detection και recovery από άγνωστη αλλαγή.** Η policy εκπαιδεύεται μέσα σε adversarial disturbance formulation και δεν περιγράφεται ξεχωριστό post-change adaptation phase.

## Υποθέσεις και ορισμοί

Η uncertainty αντιμετωπίζεται ως worst-case input/model disturbance. Η ανθεκτικότητα της policy αξιολογείται από τη διατήρηση control performance όταν μεταβάλλονται παράμετροι του συστήματος. Για την παρούσα διπλωματική, αυτή η formulation είναι ιστορικό/θεωρητικό υπόβαθρο για robust baselines, όχι πλήρης operational definition της resilience.

## Περιορισμοί και απειλές εγκυρότητας

Η εργασία είναι παλαιά, μικρής κλίμακας και επικεντρώνεται σε continuous-control pendulum. Οι assumptions και ο `H∞`-inspired objective δεν μεταφέρονται αυτούσια σε discrete GridWorld. Δεν αξιολογούνται πολλαπλοί τύποι uncertainty, recovery time, repeated disruptions ή catastrophic forgetting. Η robust policy μπορεί επίσης να είναι συντηρητική σε nominal conditions, κάτι που πρέπει να μετρηθεί ρητά στη δική μας εργασία.

## Σχέση με άλλες πηγές

- Ιστορικός πρόδρομος των robust-MDP και adversarial robust-RL formulations.
- Συμπληρώνει το `SRC-3EA1176D3A` ως foundational worst-case robustness reference.
- Διαχωρίζεται από το `SRC-B88D51FA3F`, το οποίο μελετά online adaptation μετά από novelty.
- Παρέχει γενικό minimax rationale, ενώ το `SRC-8E12FE2688` δίνει discrete action-failure formulation.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** Θεωρητικό υπόβαθρο, Ιστορική εξέλιξη robust RL, Σχετικές εργασίες, Περιορισμοί.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** πρώιμη formulation actor–disturber· model mismatch ως κίνητρο robust RL· διάκριση robust policy από standard nominal policy.
- **Τι δεν πρέπει να ισχυριστούμε από αυτή την πηγή:** ότι η μέθοδος είναι κατάλληλη executable GridWorld baseline· ότι αποδεικνύει recovery/adaptation· ότι υπερέχει σε σύγχρονα benchmarks.
- **Ρόλος:** υπόβαθρο

## Απαιτούμενα αποσπάσματα

Καταγράφηκαν επαληθευμένα τεκμήρια για το motivation, minimax actor–disturber formulation, analytical validation, nonlinear results και τα όρια σε σχέση με resilience.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη
- **Ελέγχθηκε το πλήρες κείμενο:** ναι
- **Ελέγχθηκαν οι θέσεις των αποσπασμάτων:** ναι
- **Ανοιχτά ζητήματα:** καμία ανάγκη υλοποίησης της μεθόδου στην πρώτη experimental design· χρησιμοποιείται ως θεωρητικό υπόβαθρο.
