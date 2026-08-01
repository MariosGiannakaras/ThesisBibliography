---
κωδικός: SRC-A4DC00B75B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# SRC-A4DC00B75B — Επαληθευμένα τεκμήρια

## 1. Modular GridWorld substrate

Το MiniGrid παρέχει 2D tile-based environments με προγραμματιστικά ελεγχόμενα layouts, discrete actions, sparse rewards και partial observations. Αυτό το καθιστά κατάλληλο για versioned, controlled perturbation scenarios.

## 2. Environment και agent seeds

Η Gymnasium-compatible χρήση επιτρέπει deterministic reset seeds. Για αναπαραγωγιμότητα πρέπει να αποθηκεύονται χωριστά map/configuration seed και agent/training seed.

## 3. Structural customization

Walls, goals, objects, mission strings, reward function και observation space μπορούν να αλλάξουν μέσω environment generation και wrappers. Οι αλλαγές πρέπει να καταγράφονται ως environment configuration, όχι να κρύβονται στον agent.

## 4. Solvability και contract checks

Η δυνατότητα εύκολης generation δεν εγγυάται ότι κάθε custom perturbation παραμένει επιλύσιμη. Κάθε structural scenario απαιτεί reachability/solvability check και κοινό action–observation contract για όλους τους agents.

## 5. Transfer caveat

Στα case studies, διαφορετικά transferred components έχουν διαφορετική επίδραση και η μεταφορά actor weights μπορεί να είναι επιβλαβής. Αυτό υποστηρίζει component-level reset/transfer ablations και explicit negative-transfer measurement.

## Προτεινόμενη χρήση

- Πειραματικό περιβάλλον και reproducibility section.
- Τεκμηρίωση partial observability, sparse reward και custom wrappers.
- Justification για serialized maps, environment versioning και solvability tests.