---
κωδικός: SRC-F0A9C5D77B
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "institutional repository record, 2023"
ελεγχθέν-πρωτότυπο: όχι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Πειραματική σύγκριση αλγορίθμων ενισχυτικής μάθησης βασισμένης σε μοντέλα

## Αξιολόγηση
Η διπλωματική συγκρίνει neural-network και Gaussian-process dynamics models σε model-based policy search για ρομποτικά προβλήματα. Είναι χρήσιμη εφαρμοστικά για model learning και predictive uncertainty, αλλά το διαθέσιμο record είναι κυρίως metadata/abstract και δεν τεκμηριώνει controlled environmental changepoints, detector-triggered adaptation, repeated regimes ή post-change recovery metrics.

## Σχέση με τη διπλωματική
Το ερώτημα «ποιο learned dynamics model είναι καλύτερο» είναι διαφορετικό από το «ποιος agent ανακάμπτει γρηγορότερα μετά από αλλαγή MDP». Η uncertainty των Gaussian processes δεν πρέπει να ερμηνευθεί αυτομάτως ως calibrated change detector.

## Απόφαση
**Απόρριψη από την curated επιλογή.** Διατηρείται ως application/model-based RL record· μπορεί να επανεξεταστεί μόνο αν απαιτηθεί ειδικό model-based uncertainty baseline και ελεγχθεί το πλήρες PDF.