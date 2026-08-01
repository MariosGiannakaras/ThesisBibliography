---
κωδικός: SRC-E8CAAF02BE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-E8CAAF02BE — verified excerpts

## Partial observability

Σε POMDP ο agent δεν γνωρίζει απευθείας το πραγματικό state και πρέπει να χρησιμοποιεί ιστορικό observations/actions για να διατηρεί εκτίμηση της κατάστασης.

**Χρήση:** observation uncertainty δεν πρέπει να μοντελοποιείται σαν απλό transition noise όταν το hidden state έχει σημασία για την απόφαση.

## Belief state

Το observable history μπορεί να συνοψιστεί σε belief state, δηλαδή distribution πάνω στα δυνατά underlying states, και η policy μπορεί να οριστεί πάνω σε αυτό το belief.

**Protocol implication:** όταν χρησιμοποιείται context/belief agent, αποθηκεύονται posterior mass στο true context και belief entropy.

## Information-gathering actions

Μια action μπορεί να έχει dual role: να αλλάζει το world state και να παρέχει πληροφορία. Η βέλτιστη action δεν είναι πάντα η action που είναι καλύτερη για το most-likely state.

**Μετρική:** information-gathering action count και reward/safety cost της active disambiguation.

## Three distinct uncertainties

Η partial observability πρέπει να διακρίνεται από latent regime uncertainty και από πραγματική χρονική αλλαγή του environment model.

**Thesis-ready claim:** belief-state reasoning δεν αποτελεί από μόνο του changepoint adaptation.

## Fairness boundary

Agent που διαθέτει ακριβές transition/observation model για Bayesian belief update έχει περισσότερο prior information από model-free Q-learning.

**Protocol rule:** δηλώνεται ρητά ποιο model/prior/context library είναι διαθέσιμο σε κάθε agent.