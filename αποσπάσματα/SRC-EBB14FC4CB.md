---
κωδικός: SRC-EBB14FC4CB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Αποσπάσματα — Reinforcement Learning for Non-Stationary MDPs: The Blessing of (More) Optimism

## Τεκμήριο E1
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract και §1
- **Ισχυρισμός:** Rewards και transitions μπορούν να driftάρουν χωριστά υπό variation budgets.
- **Κατάσταση:** επαληθευμένο

Η εργασία μοντελοποιεί χρονικά μεταβαλλόμενα reward means και transition distributions, με συνολική μεταβολή περιορισμένη από διαφορετικά budgets.

**Χρήση:** χωριστοί άξονες reward και transition drift.

**Παραπομπή:** Cheung et al., 2020, Abstract και §1.

## Τεκμήριο E2
- **Τύπος:** πιστή παράφραση
- **Θέση:** §1.1 και algorithm formulation
- **Ισχυρισμός:** Το SWUCRL2-CW συνδυάζει sliding-window forgetting με confidence widening.
- **Κατάσταση:** επαληθευμένο

Η μέθοδος χρησιμοποιεί πρόσφατα observations και διευρύνει εσκεμμένα τα transition confidence regions αντί να επιδιώκει το στενότερο δυνατό set.

**Περιορισμός:** απαιτεί variation-budget knowledge για την προτεινόμενη ρύθμιση.

**Παραπομπή:** Cheung et al., 2020, §1.1.

## Τεκμήριο E3
- **Τύπος:** πιστή παράφραση
- **Θέση:** Sections 4 και 6
- **Ισχυρισμός:** Tight confidence sets μπορεί να έχουν δυσμενή MDP diameter και regret.
- **Κατάσταση:** επαληθευμένο

Στο non-stationary RL, η συμβατική λογική του ελάχιστου optimism μπορεί να επιλέξει plausible MDPs με πολύ μεγάλο diameter· το confidence widening αντιμετωπίζει αυτό το ειδικό RL πρόβλημα.

**Χρήση:** μη ταύτιση “μικρότερου uncertainty set” με “καλύτερη adaptation”.

**Παραπομπή:** Cheung et al., 2020, §§4, 6.

## Τεκμήριο E4
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract, §1.1 και §7
- **Ισχυρισμός:** Ο BORL αφαιρεί την ανάγκη γνώσης variation budgets.
- **Κατάσταση:** επαληθευμένο

Ο BORL προσαρμόζει τις παραμέτρους του base learner μέσω bandit-over-RL διαδικασίας και διατηρεί το ίδιο order dynamic-regret guarantee χωρίς budget input.

**Περιορισμός:** parameter-free ως προς budgets δεν σημαίνει χωρίς hyperparameters ή computation.

**Παραπομπή:** Cheung et al., 2020, Abstract, §1.1, §7.

## Τεκμήριο E5
- **Τύπος:** πιστή παράφραση
- **Θέση:** §2.2
- **Ισχυρισμός:** Η αξιολόγηση είναι dynamic regret έναντι time-indexed stationary optima.
- **Κατάσταση:** επαληθευμένο

Το cumulative deficit συγκρίνει κάθε χρονική στιγμή με τη long-run average reward του MDP που ορίζεται από τις τρέχουσες rewards και transitions.

**Περιορισμός:** δεν ισοδυναμεί με detection delay ή recovery-time metric.

**Παραπομπή:** Cheung et al., 2020, §2.2.

## Τεκμήριο E6
- **Τύπος:** πιστή παράφραση
- **Θέση:** §7
- **Ισχυρισμός:** Η συνεισφορά είναι θεωρητική και δεν αποδεικνύει empirical ordering στο GridWorld.
- **Κατάσταση:** επαληθευμένο

Η conclusion συνοψίζει regret guarantees και confidence widening, χωρίς empirical benchmark section.

**Χρήση:** θεωρητική αιτιολόγηση recency/adaptive tuning, όχι algorithm-ranking claim.

**Παραπομπή:** Cheung et al., 2020, §7.
