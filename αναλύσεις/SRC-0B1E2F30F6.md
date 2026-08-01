# SRC-0B1E2F30F6 — Hierarchical Reinforcement Learning for Playing a Dynamic Dungeon Crawler Game

## Απόφαση

**Απόρριψη από το core export.**

Η εργασία προτείνει dynamic hierarchical RL όπου κάθε hierarchical choice επανεξετάζεται σε κάθε time step, ώστε ο agent να αντιδρά σε αλλαγές μέσα στο game. Παρότι η λέξη “dynamic” είναι θεματικά ελκυστική, το πρόβλημα δεν είναι controlled non-stationary MDP benchmark με explicit changepoints.

## Αιτιολόγηση

- Η δυναμικότητα προέρχεται από game events/enemies και hierarchical action selection.
- Δεν υπάρχει formal pre-change/post-change regime protocol.
- Δεν μετρώνται detection delay, performance drop, recovery time ή forgetting.
- Η σύγκριση αφορά dHRL έναντι MaxQ σε game levels, όχι matched resilience baselines.
- Η hierarchical decomposition θα εισήγαγε νέο agent family χωρίς αναγκαία κάλυψη του κεντρικού research question.

Η πηγή διατηρείται ως related HRL/application evidence, αλλά δεν εξάγεται.