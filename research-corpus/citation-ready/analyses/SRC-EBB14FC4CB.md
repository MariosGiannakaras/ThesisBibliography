---
κωδικός: SRC-EBB14FC4CB
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PMLR 119, ICML 2020"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Reinforcement Learning for Non-Stationary Markov Decision Processes: The Blessing of (More) Optimism

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Wang Chi Cheung, David Simchi-Levi, Ruihao Zhu
- **Έτος:** 2020
- **Έκδοση:** Proceedings of Machine Learning Research 119, ICML 2020
- **Τύπος:** πρωτογενής θεωρητική εργασία για drifting non-stationary tabular MDPs
- **Πρωτότυπο:** `πηγές/SRC-EBB14FC4CB.md`

## Σκοπός

Η εργασία μελετά online reinforcement learning όταν reward means και transition distributions μεταβάλλονται εξωγενώς με τον χρόνο, χωρίς να υπερβαίνουν συνολικά variation budgets. Το ζητούμενο είναι χαμηλό dynamic regret έναντι του optimal stationary policy του τρέχοντος MDP σε κάθε χρονική στιγμή.

## Προτεινόμενες μέθοδοι

### SWUCRL2-CW

Ο Sliding-Window UCRL2 with Confidence Widening:

- χρησιμοποιεί μόνο πρόσφατα samples,
- κατασκευάζει confidence regions για rewards και transitions,
- διευρύνει σκόπιμα το transition confidence set,
- απαιτεί γνώση των συνολικών variation budgets για τη θεωρητικά ρυθμισμένη επιλογή window και widening.

### BORL

Ο Bandit-over-Reinforcement-Learning wrapper επιλέγει adaptively τις βασικές παραμέτρους του SWUCRL2-CW και επιτυγχάνει το ίδιο order dynamic-regret bound χωρίς να γνωρίζει εκ των προτέρων τα variation budgets.

## Κύρια θεωρητικά ευρήματα

1. **Stale data απαιτούν forgetting.** Όταν rewards και transitions drift, estimators που χρησιμοποιούν όλη την ιστορία αποκτούν bias προς παλιότερα MDPs.
2. **Το sliding window μόνο του δεν αρκεί.** Στο non-stationary RL, τα tight confidence sets μπορούν να περιλαμβάνουν optimistic MDPs με πολύ μεγάλο diameter, προκαλώντας δυσμενή regret dependence.
3. **Confidence widening εισάγει “extra optimism”.** Η εσκεμμένη διεύρυνση του transition set επιτρέπει την επιλογή μοντέλων με ελεγχόμενο diameter και είναι κεντρική για το bound.
4. **Known-budget και parameter-free settings πρέπει να διακρίνονται.** Το SWUCRL2-CW χρησιμοποιεί variation-budget knowledge, ενώ το BORL αφαιρεί αυτή την oracle-like απαίτηση μέσω online model selection.
5. **Η μετρική είναι dynamic regret, όχι recovery time.** Η ανάλυση είναι cumulative και δεν παρέχει απευθείας changepoint delay ή per-change recovery curves.
6. **Η πηγή είναι θεωρητική.** Δεν παρέχει empirical GridWorld benchmark που να αποδεικνύει πρακτική υπεροχή στις συνθήκες της διπλωματικής.

## Μοντέλο και υποθέσεις

- finite state/action spaces,
- undiscounted communicating MDPs,
- bounded maximum diameter,
- arbitrary drift υπό συνολικά reward και transition variation budgets,
- unknown instantaneous changes,
- partial/bandit feedback από τις επισκέψεις του agent,
- dynamic-regret oracle που χρησιμοποιεί το current stationary MDP.

## Σχέση με τη διπλωματική

Η εργασία παρέχει ισχυρή θεωρητική βάση για:

- recency/sliding-window baselines,
- χωριστή καταγραφή reward και transition variation,
- διάκριση known-budget από adaptive parameter-free tuning,
- αποφυγή του ισχυρισμού ότι “λιγότερη αβεβαιότητα” ή στενότερο confidence set είναι πάντα καλύτερο,
- evaluation gradual drift χωρίς τεχνητά discrete changepoints.

Δεν προτείνεται η πλήρης υλοποίηση SWUCRL2-CW ή BORL, επειδή απαιτούν optimistic planning σε confidence sets και είναι δυσανάλογα σύνθετα για το βασικό resource-aware GridWorld matrix.

## Πρακτικές απαιτήσεις πρωτοκόλλου

- `reward_variation_budget` και `transition_variation_budget` χωριστά,
- `variation_budget_known_to_agent`: yes/no,
- gradual drift χωριστά από piecewise abrupt changes,
- memory/window hyperparameters χωρίς test leakage,
- parameter-free/adaptive tuning χωριστά από oracle tuning,
- dynamic cumulative deficit μαζί με local recovery metrics,
- reporting του effective planning/model-selection overhead.

## Περιορισμοί

Τα regret bounds βασίζονται σε communicating MDPs, finite tabular spaces και diameter quantities. Το theoretical dynamic regret δεν μεταφράζεται αυτόματα σε superior average return ή safety. Η BORL αφαιρεί τη γνώση budgets αλλά προσθέτει meta-bandit complexity. Η confidence-widening ιδέα είναι mechanism evidence και όχι υποχρεωτικό implementation requirement.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Non-stationarity, Adaptive baselines, Exploration under drift, Μετρικές, Threats to validity.
- **Υποστηριζόμενοι ισχυρισμοί:** recent-memory estimation είναι principled για drifting MDPs· known variation budgets αποτελούν πρόσθετη πληροφορία· tight confidence regions δεν εγγυώνται καλό non-stationary RL behavior.
- **Μη υποστηριζόμενοι ισχυρισμοί:** ότι ένα συγκεκριμένο window είναι βέλτιστο στο GridWorld· ότι η μέθοδος ανιχνεύει changepoints· ότι το regret ordering θα αναπαραχθεί εμπειρικά.
- **Ρόλος:** κύρια

## Κατάσταση επαλήθευσης

- πλήρες κείμενο: ελέγχθηκε
- theorem/conclusion scope: ελέγχθηκε
- empirical evidence: δεν παρέχεται
- citation-ready excerpts: δημιουργήθηκαν
