---
κωδικός: SRC-8E22CBA55A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-8E22CBA55A — verified excerpts

## Safety as stability

Η εργασία ορίζει safety μέσω control-theoretic stability και region of attraction. Μια policy θεωρείται ασφαλής σε περιοχή όπου οι trajectories παραμένουν και συγκλίνουν προς equilibrium.

**Χρήση:** distinction από CMDP expected-cost safety.

## Safe exploration

Η agent συλλέγει νέα δεδομένα μόνο σε σημεία που μπορούν να πιστοποιηθούν ως ασφαλή με βάση model uncertainty και Lyapunov conditions.

**Protocol implication:** exploration coverage πρέπει να αναφέρεται μαζί με safety restrictions και denied/intervened actions.

## Initial safe policy

Η μέθοδος απαιτεί αρχική policy που είναι γνωστό ότι σταθεροποιεί το σύστημα τουλάχιστον σε μικρή περιοχή.

**Χρήση:** κάθε safe-learning baseline με pre-existing fallback πρέπει να δηλώνει ρητά το prior knowledge που διαθέτει.

## Model uncertainty και certificates

Οι guarantees εξαρτώνται από confidence intervals του learned dynamics model και regularity assumptions.

**Thesis-ready claim:** μετά από dynamics changepoint, pre-change safety certificate δεν πρέπει να θεωρείται αυτομάτως valid για το νέο regime.

## Recovery terminology boundary

Η “recovery” προς safe/equilibrium state είναι διαφορετική από recovery της task-policy performance μετά από environmental shift.

**Μη επιτρεπτός ισχυρισμός:** ότι Lyapunov stability guarantee συνεπάγεται γρήγορη adaptation ή relearning μετά από non-stationarity.

## Πειραματικές συνέπειες

- αναφορά certified-safe-region size,
- unsafe-state violations,
- intervention/denial frequency,
- nominal utility cost,
- in-certificate versus out-of-certificate post-change states,
- certificate revalidation latency μετά από αλλαγή dynamics.