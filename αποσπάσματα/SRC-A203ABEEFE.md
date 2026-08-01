---
κωδικός: SRC-A203ABEEFE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-A203ABEEFE — verified excerpts

## Replay memory

Experience replay αποθηκεύει transitions και τα επαναχρησιμοποιεί, μειώνοντας temporal correlation και επιτρέποντας πολλαπλά updates από σπάνια experiences.

**Non-stationary implication:** μετά από changepoint το ίδιο buffer μπορεί να περιέχει data από διαφορετικά regimes.

## TD-error prioritization

Το prioritized replay χρησιμοποιεί συνήθως το μέγεθος του TD error ως proxy για το πόσο σημαντικό ή surprising είναι ένα transition.

**Boundary:** surprise/TD error δεν είναι calibrated evidence περιβαλλοντικής αλλαγής.

## Diversity και noise

Pure greedy prioritization μπορεί να μειώσει diversity και να υπερεστιάσει σε noise spikes ή transitions με επίμονα approximation errors.

**Protocol implication:** αναφορά priority distribution και regime/age composition των replayed samples.

## Sampling bias

Non-uniform replay αλλάζει την sampling distribution και εισάγει bias· η εργασία χρησιμοποιεί importance-sampling correction.

**Χρήση:** replay-based baseline πρέπει να αναφέρει prioritization και correction parameters.

## Changepoint ablations

Για τη διπλωματική είναι χρήσιμο να συγκριθούν uniform/PER με no replay, oracle buffer flush και detector-triggered flush.

**Μη επιτρεπτός ισχυρισμός:** ότι PER είναι change detector ή εγγυημένα επιταχύνει recovery σε non-stationary MDP.