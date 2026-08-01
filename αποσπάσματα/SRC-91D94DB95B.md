---
κωδικός: SRC-91D94DB95B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-91D94DB95B — verified excerpts

## CMDP formulation

Η εργασία ορίζει constrained MDP ως MDP με auxiliary cost functions και limits. Η policy βελτιστοποιεί το κύριο return μόνο μέσα στο feasible set που ικανοποιεί τα cost constraints.

**Χρήση:** σαφής διάκριση task reward και safety/constraint cost.

## Safety during learning

Το CPO σχεδιάστηκε ώστε οι διαδοχικές policy updates να ελέγχουν constraint satisfaction κατά τη διαδικασία μάθησης, όχι μόνο στην τελική policy.

**Protocol implication:** στη διπλωματική οι violations καταγράφονται σε ολόκληρη τη post-change recovery trajectory.

## Reward και cost ως διαφορετικές καμπύλες

Η constrained formulation επιτρέπει να μετρηθούν ανεξάρτητα expected task return και expected cumulative auxiliary costs.

**Thesis-ready claim:** επιστροφή του reward στο nominal επίπεδο δεν συνεπάγεται ότι έχει αποκατασταθεί και η safety performance.

## Expected-cost guarantee boundary

Το CMDP constraint είναι expectation-based. Δεν ισοδυναμεί από μόνο του με pointwise, instantaneous ή almost-sure safety guarantee.

**Χρήση:** κάθε safety result πρέπει να δηλώνει ακριβώς το είδος constraint/guarantee.

## Scope boundary

Το CPO δεν είναι change detector ούτε non-stationary adaptation algorithm. Η εργασία δεν μελετά abrupt environment switches.

**Μη επιτρεπτός ισχυρισμός:** ότι CPO αποδεικνύει resilience σε changing GridWorlds.

## Πειραματικές συνέπειες

Μετά από αλλαγή περιβάλλοντος αναφέρονται χωριστά:

- return recovery time,
- cumulative safety cost,
- violation count/rate,
- time until the constraint is satisfied again,
- nominal-performance penalty από safety enforcement.