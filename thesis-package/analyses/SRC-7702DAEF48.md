# Επιστημονική ανάλυση — SRC-7702DAEF48

## Βιβλιογραφική ταυτότητα

- **Τίτλος:** Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones
- **Συγγραφείς:** Brijen Thananjeyan et al.
- **Δημοσίευση:** IEEE Robotics and Automation Letters, 2021
- **Προτεινόμενος ρόλος:** υποστηρικτική πηγή

## Ερευνητικό πρόβλημα

Η εργασία αντιμετωπίζει το conflict ανάμεσα σε task-directed exploration και περιορισμό constraint violations. Αντί να αναμιγνύει reward και safety σε ένα ενιαίο objective, διαχωρίζει την επίδοση του task από τη λειτουργία ανάκαμψης.

## Αρχιτεκτονική

Η Recovery RL χρησιμοποιεί:

1. **task policy**, που βελτιστοποιεί αποκλειστικά το task reward,
2. **safety critic**, που εκτιμά discounted μελλοντική πιθανότητα constraint violation,
3. **recovery policy**, που αναλαμβάνει όταν το estimated risk υπερβαίνει threshold,
4. offline data με παραδείγματα unsafe transitions για αρχικοποίηση πριν από online exploration.

Η composite policy εκτελεί είτε την task είτε τη recovery policy ανά βήμα.

## Κύρια ευρήματα

- Στα εξεταζόμενα simulation και robotic domains, η μέθοδος πετυχαίνει ευνοϊκότερο trade-off task success/constraint violation από συγκρινόμενες safe-RL baselines.
- Η learned recovery mechanism μπορεί να λειτουργήσει ως approximate local reset προς κοντινή safe state, χωρίς να απαιτεί πλήρη επαναφορά στην αρχική κατάσταση.
- Ο safety critic ενημερώνεται online και μπορεί να αξιοποιήσει offline unsafe data.
- Το safety threshold ελέγχει τη συχνότητα παρέμβασης και την πιθανή συντηρητικότητα.

## Σχέση με τη διπλωματική

Η πηγή δεν αποτελεί non-stationarity detector. Παρέχει όμως ισχυρό architectural pattern για ανθεκτικό agent:

- primary learner,
- risk monitor,
- learned fallback/recovery controller,
- explicit intervention logging.

Σε GridWorld μπορεί να υλοποιηθεί απλουστευμένα ως Q-learning task policy και recovery table/policy που απομακρύνει τον agent από hazard states όταν η εκτιμώμενη violation probability υπερβεί threshold.

## Πειραματικό πρωτόκολλο που προκύπτει

Πρέπει να αναφέρονται χωριστά:

- task return και success rate,
- violation count και violation probability,
- αριθμός/διάρκεια recovery interventions,
- false ή unnecessary interventions,
- performance under shield/recovery έναντι unassisted agent,
- recovery-controller failures,
- offline unsafe-data budget.

## Περιορισμοί

- Η safety critic δεν παρέχει από μόνη της formal guarantee όταν οι dynamics και constraints είναι άγνωστες.
- Η μέθοδος υποθέτει διαθέσιμα labels για constraint violation και offline examples.
- Τα experiments εστιάζουν safety during learning, όχι repeated environmental regime shifts.
- Η επίδοση εξαρτάται από threshold calibration και την ποιότητα της recovery policy.

## Απόφαση

**Επαληθευμένη — εξαγωγή ναι, ως υποστηρικτική πηγή.** Χρησιμοποιείται για learned recovery/fallback architecture και intervention metrics, όχι ως change-detection ή resilience algorithm από μόνη της.