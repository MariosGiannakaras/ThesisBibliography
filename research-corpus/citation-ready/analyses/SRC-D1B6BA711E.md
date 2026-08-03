---
κωδικός: SRC-D1B6BA711E
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2209.13841"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Online Policy Optimization for Robust MDP

## Βιβλιογραφική ταυτότητα
Jing Dong, Jingwei Li, Baoxiang Wang, Jingzhao Zhang. arXiv:2209.13841.

## Σκοπός και ερευνητικό ερώτημα
Μελετά αν robust policy optimization μπορεί να γίνει αποδοτικά σε online setting, χωρίς generative-model oracle, ενώ ο agent πρέπει ταυτόχρονα να εξερευνά και να μεγιστοποιεί worst-case performance.

## Σύνοψη
Η εργασία διατυπώνει episodic robust MDP γύρω από άγνωστο nominal kernel και rectangular uncertainty set. Προτείνει optimistic policy-optimization algorithm και αποδεικνύει sublinear regret για (s,a)-rectangular και s-rectangular uncertainty sets.

## Μεθοδολογία
- episodic finite-horizon robust MDP,
- online interaction με nominal environment,
- stochastic policy optimization,
- optimism bonus που συνδυάζει data uncertainty και robust-transition uncertainty,
- regret analysis και experiments.

## Κύρια ευρήματα
1. Robust learning μπορεί να συνδυαστεί με online exploration χωρίς generative-model access υπό συγκεκριμένες assumptions.
2. Η robust policy μπορεί να χρειάζεται stochasticity, ιδιαίτερα υπό s-rectangular uncertainty.
3. Η exploration uncertainty από περιορισμένα δεδομένα είναι διαφορετική από την ambiguity του robust MDP.
4. Sublinear regret αφορά worst-case robust objective και όχι adaptation μετά από πραγματικό changepoint.

## Υποθέσεις και ορισμοί
Το nominal dynamics θεωρείται σταθερό κατά τη learning διαδικασία και το deployment uncertainty βρίσκεται μέσα σε προκαθορισμένο ambiguity set. Δεν υπάρχει άγνωστη ακολουθία abrupt regimes.

## Περιορισμοί και απειλές εγκυρότητας
- finite tabular/episodic theory,
- known uncertainty-set form/radius,
- robust objective μπορεί να είναι conservative,
- δεν παρέχει detection delay/recovery-time metrics,
- το algorithmic complexity υπερβαίνει το βασικό resource-aware GridWorld baseline matrix.

## Σχέση με άλλες πηγές
Συμπληρώνει `SRC-9D663D35D0` (model-free robust MDP) και `SRC-6E7AFA8AC0` (sample complexity). Σε αντίθεση με `SRC-7456165CEA`, δεν ανιχνεύει changepoints ούτε κάνει restart.

## Χρήση στη διπλωματική
Υποστηρικτική θεωρητική/feasibility πηγή για online robust comparator. Επιβάλλει να δηλώνονται χωριστά:
- uncertainty από estimation/exploration,
- uncertainty set που εκφράζει deployment model ambiguity,
- clean return,
- robust/worst-case return,
- post-change recovery όταν επιτρέπονται updates.

Δεν προτείνεται ως default implementation.

## Απαιτούμενα αποσπάσματα
1. Online robust RL πρέπει να ισορροπεί exploration και worst-case optimization.
2. Robust MDP uncertainty και statistical uncertainty από limited data είναι διαφορετικές πηγές αβεβαιότητας.
3. Sublinear robust regret δεν ισοδυναμεί με resilience σε piecewise-stationary environment.

## Κατάσταση επαλήθευσης
Επαληθεύτηκε στο πλήρες preprint. Επιλέγεται ως υποστηρικτική.