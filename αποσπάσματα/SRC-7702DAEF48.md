## SRC-7702DAEF48 — Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

- **Ρόλος:** υποστηρικτική
- **Κατάσταση:** επαληθευμένη

### Citation-ready τεκμήρια

1. **Η task επίδοση και η constraint satisfaction μπορούν να ανατεθούν σε διαφορετικές policies.** Η task policy βελτιστοποιεί reward, ενώ μια recovery policy αναλαμβάνει όταν ένας safety critic προβλέπει αυξημένο κίνδυνο παραβίασης.

2. **Ο safety critic εκτιμά discounted μελλοντική πιθανότητα constraint violation** και ενεργοποιεί recovery όταν η εκτίμηση υπερβεί προκαθορισμένο threshold.

3. **Offline unsafe transitions μπορούν να μειώσουν το αναγκαίο επικίνδυνο exploration.** Δεν απαιτούνται demonstrations επιτυχίας του task· αρκούν παραδείγματα constraint-violating συμπεριφοράς.

4. **Η recovery policy λειτουργεί ως approximate local reset**, οδηγώντας τον agent προς κοντινή ασφαλή περιοχή αντί να επιβάλλει πλήρη επιστροφή στην αρχική κατάσταση.

5. **Η μέθοδος δεν αποτελεί formal safety guarantee χωρίς πρόσθετες assumptions.** Η αξιοπιστία εξαρτάται από calibration του safety critic, threshold και επάρκεια της recovery policy.

### Χρήση στη διπλωματική

- Pattern `task policy + risk monitor + learned fallback`.
- Χωριστή αναφορά interventions, violations και utility.
- Feasibility baseline για GridWorld hazards, όχι change detector ή πλήρες resilience mechanism.