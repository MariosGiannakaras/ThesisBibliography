---
κωδικός: SRC-5D0E7E5BD7
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2005.12729 official record/abstract"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Logan Engstrom, Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, Aleksander Madry
- **Έτος:** 2020
- **Τύπος:** πρωτογενής εμπειρική/μεθοδολογική εργασία deep RL
- **Αναγνωριστικό:** arXiv:2005.12729

## Σκοπός και συνάφεια

Η εργασία εξετάζει κατά πόσο η φαινομενική αλγοριθμική πρόοδος σε PPO/TRPO οφείλεται στον core algorithm ή σε code-level optimizations/implementation augmentations που συχνά περιγράφονται ως δευτερεύουσες λεπτομέρειες. Είναι άμεσα σχετική με το protocol-v2 επειδή η σύγκριση ενός PPO adapter με Q-Learning/SARSA/DQN/Dyna-Q+ δεν είναι επιστημονικά επαρκής αν το PPO δηλώνεται μόνο ως όνομα χωρίς implementation identity και resolved configuration.

## Κύρια σημεία που υποστηρίζονται άμεσα

1. **Code-level optimizations μπορούν να έχουν μεγάλο effect.** Οι συγγραφείς βρίσκουν ότι implementation augmentations επηρεάζουν ουσιαστικά agent behavior και cumulative reward.
2. **Το algorithm label δεν είναι πλήρης scientific identity.** Στη συγκεκριμένη μελέτη, οι implementation choices εξηγούν μεγάλο μέρος της μετρούμενης διαφοράς PPO/TRPO και αλλάζουν τον τρόπο λειτουργίας των methods.
3. **Attribution χρειάζεται προσοχή.** Η παρατηρούμενη απόδοση δεν πρέπει να αποδίδεται αυτομάτως στην αφηρημένη algorithmic ιδέα όταν code-level choices διαφέρουν.

## Εφαρμογή στο protocol-v2

Για το retained PPO implementation πρέπει να παγώνονται και να αποθηκεύονται ως provenance/scientific configuration τουλάχιστον maintained-library και PyTorch versions, network/feature architecture, activation/initialization όπου παραμετροποιούνται, optimizer/LR schedule, rollout length, batch/update epochs, GAE/clipping/entropy/value settings και κάθε normalization/wrapper που επηρεάζει τη μάθηση.

Η ίδια αρχή εφαρμόζεται γενικά στους deep adapters: η thesis δεν συγκρίνει αφηρημένα ονόματα algorithms αλλά συγκεκριμένες, versioned, predeclared implementations του ίδιου task contract.

Η πηγή **δεν** χρησιμοποιείται για post-hoc tuning ούτε για να αντιγράψουμε settings από διαφορετικά benchmarks. Υποστηρίζει provenance/implementation transparency και την ανάγκη να μην αποδίδονται effects στον core algorithm χωρίς έλεγχο των implementation choices.

## Περιορισμοί

Η μελέτη είναι case study PPO/TRPO και δεν αποδεικνύει ότι κάθε code-level choice έχει το ίδιο effect στο thesis GridWorld. Δεν δίνει τη βέλτιστη PPO configuration για το project και δεν αποδεικνύει superiority/ inferiority PPO έναντι DQN ή tabular methods. Οι τελικές settings παραμένουν bounded tuning/pilot output.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Μεθοδολογία, reproducibility/provenance, deep-RL implementation, threats to validity.
- **Ρόλος:** κύρια μεθοδολογική πηγή για implementation sensitivity.
- **Ισχυρισμοί:** algorithm-label underspecification, importance of code-level choices, attribution risk.
- **Μη ισχυρισμοί:** συγκεκριμένη τελική PPO configuration ή cross-method ranking.
