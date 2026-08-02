---
κωδικός: SRC-9DCA1F02C1
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PMLR 119, ICML 2020"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Leveraging Procedural Generation to Benchmark Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Karl Cobbe, Christopher Hesse, Jacob Hilton, John Schulman
- **Έτος:** 2020
- **Έκδοση:** PMLR 119, ICML 2020
- **Τύπος:** πρωτογενής benchmark/protocol εργασία

## Σκοπός

Η εργασία εισάγει το Procgen Benchmark, 16 procedurally generated environments για μέτρηση sample efficiency και generalization. Το κεντρικό πρόβλημα είναι ότι agents μπορούν να υπερπροσαρμόζονται ακόμη και σε μεγάλα fixed level sets, ενώ η training performance μπορεί να δίνει ψευδή εικόνα πραγματικής δεξιότητας.

## Benchmark design

Τα environments παρέχουν:

- σχεδόν απεριόριστη level distribution μέσω seeds,
- disjoint train/test levels,
- κοινό observation/action interface,
- easy/hard distributions,
- tunable exploration και memory demands,
- γρήγορη simulation throughput,
- προσπάθεια διασφάλισης level solvability.

## Κύρια ευρήματα

1. **Η diversity του training distribution είναι κρίσιμη.** Μικρά level sets προκαλούν μεγάλο generalization gap και σε αρκετά environments απαιτούνται έως και χιλιάδες levels για να περιοριστεί η υπερπροσαρμογή.
2. **Fixed deterministic sequences μπορούν να δημιουργούν ψευδαίσθηση προόδου.** Agents μαθαίνουν τα πρώτα training levels αλλά αποδίδουν ελάχιστα όταν η test sequence τυχαιοποιείται.
3. **Sample efficiency και generalization είναι διαφορετικές μετρικές.** Full-distribution train/test μετρά sample efficiency, ενώ finite training set και unseen level distribution μετρά zero-shot generalization.
4. **Το recommended protocol χρησιμοποιεί held-out levels.** Η εργασία προτείνει 500 training levels για hard generalization benchmark και average performance σε unseen levels.
5. **Μεγάλα models βελτιώνουν γενικά training και test performance, αλλά με σημαντικό compute cost.** Αυτό δεν αποτελεί resource-neutral ordering.
6. **PPO και Rainbow εμφανίζουν environment-dependent ordering.** PPO είναι πιο συνεπές συνολικά, ενώ Rainbow υπερέχει σε ορισμένα environments· δεν προκύπτει universal ranking.

## Σχέση με τη διπλωματική

Η πηγή υποστηρίζει το protocol για procedural GridWorld layouts:

- διαχωρισμένα training, validation και test seeds,
- held-out layouts για zero-shot evaluation,
- διαφορετική αξιολόγηση sample efficiency και adaptation,
- αποφυγή fixed map/trajectory memorization,
- reporting ανά scenario και όχι μόνο aggregate score.

Το Procgen benchmark δεν είναι online non-stationarity: κάθε level μπορεί να αλλάζει ανά episode, αλλά το train/test evaluation αφορά frozen-policy generalization σε distribution και όχι recovery μετά από changepoint.

## Πρακτικές απαιτήσεις

- `level_seed` και `split` καταγεγραμμένα,
- disjoint train/validation/test generators,
- solvability verification,
- train και test returns μαζί,
- generalization gap,
- unseen-level zero-shot test πριν από adaptation,
- fixed-sequence ablation,
- resource-normalized compute budget,
- per-environment results πριν από aggregate normalized score.

## Περιορισμοί

Το Procgen είναι visual deep-RL benchmark με υψηλό compute και δεν μεταφέρεται αυτούσιο σε tabular GridWorld. Ορισμένα levels μπορεί να μην είναι επιλύσιμα και η solvability δεν είναι mathematically guaranteed. Οι baseline experiments χρησιμοποιούν λίγα seeds σε αρκετές συγκρίσεις. Το normalized aggregate score εξαρτάται από chosen normalization constants.

## Χρήση στη διπλωματική

- **Κεφάλαια:** Benchmark design, Generalization, Train-test protocol, Metrics, Reproducibility.
- **Ισχυρισμοί:** fixed levels μπορεί να κρύβουν overfitting· procedural diversity και held-out seeds είναι ουσιώδη· sample efficiency και generalization πρέπει να μετρώνται χωριστά.
- **Μη ισχυρισμοί:** ότι Procgen level changes ισοδυναμούν με online environmental drift· ότι PPO είναι καθολικά καλύτερο από Rainbow.
- **Ρόλος:** κύρια

## Κατάσταση επαλήθευσης

- πλήρες κείμενο και protocols: ελέγχθηκαν
- experiments: ελέγχθηκαν
- citation-ready excerpts: δημιουργήθηκαν
