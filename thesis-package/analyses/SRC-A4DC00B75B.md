# SRC-A4DC00B75B — Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Maxime Chevalier-Boisvert, Bolun Dai, Mark Towers, Rodrigo de Lazcano, Lucas Willems, Salem Lahlou, Suman Pal, Pablo Samuel Castro, Jordan Terry
- **Έτος:** 2023
- **Τύπος:** environment/library paper με case studies
- **Ρόλος στη διπλωματική:** κύρια πηγή πειραματικού περιβάλλοντος

## Συνεισφορά

Η εργασία περιγράφει τις MiniGrid και MiniWorld βιβλιοθήκες, τη σχεδιαστική τους φιλοσοφία, τις observation/action/reward interfaces και τον τρόπο δημιουργίας custom environments. Το MiniGrid παρέχει 2D tile-based GridWorlds με discrete actions, sparse rewards, partial observations και προγραμματιστικά ελεγχόμενη generation λογική.

Η συνεισφορά της πηγής στη διπλωματική δεν είναι αλγοριθμική υπεροχή. Είναι η τεκμηρίωση ότι ένα modular GridWorld μπορεί να χρησιμοποιηθεί ως reproducible diagnostic testbed με ελεγχόμενες αλλαγές σε:

- layout και walls,
- objects και goals,
- mission/instruction,
- observation extent,
- stochastic action wrappers,
- reward function.

## Σχεδιαστικές ιδιότητες χρήσιμες για το πρωτόκολλο

- Κοινό Gymnasium-compatible API.
- Εύκολη δημιουργία νέων layouts και wrappers.
- Discrete action space με σαφή semantics.
- Sparse reward ως default, αλλά δυνατότητα override.
- Partial ή full observations.
- Deterministic default transitions, με δυνατότητα stochastic extensions.
- Seedable resets και εύκολη οπτικοποίηση της policy συμπεριφοράς.

## Case-study evidence

Η εργασία περιλαμβάνει transfer-learning case study μεταξύ MiniGrid και MiniWorld και χρησιμοποιεί AUC learning curves για να συγκρίνει transferred initialization με scratch learning. Τα αποτελέσματα δείχνουν ότι η μεταφορά ορισμένων components μπορεί να βοηθήσει, ενώ η μεταφορά actor weights μπορεί να προκαλέσει αρνητικό transfer. Αυτό υποστηρίζει την ανάγκη component-level transfer/reset ablations.

## Εφαρμογή στη διπλωματική

Το MiniGrid μπορεί να αποτελέσει reproducible implementation substrate για:

- abrupt wall insertion/removal,
- goal relocation,
- action failure/slip,
- reward remapping,
- observation masking/noise,
- repeated regime schedules,
- hidden versus explicit context variants.

Κάθε perturbation πρέπει να υλοποιείται ως ανεξάρτητο wrapper ή versioned environment configuration, όχι ως ad hoc αλλαγή μέσα στον agent.

## Πρωτόκολλο που κλειδώνει

- Καταγραφή exact environment ID/version.
- Καταγραφή map/configuration seed χωριστά από agent seed.
- Αποθήκευση serialized layout ή deterministic generator arguments.
- Solvability validation μετά από κάθε structural perturbation.
- Ίδιο action/observation contract για όλους τους agents.
- Χωριστή επισήμανση partial observability και transition stochasticity.
- Compatibility tests για Gymnasium termination/truncation semantics.

## Περιορισμοί

- Η βιβλιοθήκη δεν είναι από μόνη της benchmark για resilience.
- Τα default tasks είναι stationary και απαιτούν custom schedule layer για online changes.
- Η wide adoption δεν αποτελεί evidence για algorithm performance.
- Οι transfer case studies δεν είναι repeated non-stationarity experiments.
- MiniGrid και MiniWorld έχουν διαφορετικά observation modalities· cross-library transfer δεν πρέπει να συγχέεται με within-environment recovery.

## Απόφαση

**Επιλογή ως κύρια environment source.** Θα χρησιμοποιείται για την τεχνική περιγραφή του GridWorld implementation και της reproducibility architecture, όχι για claims αλγοριθμικής ανθεκτικότητας.