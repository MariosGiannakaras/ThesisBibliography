# Επιστημονική ανάλυση — Παρτίδα 26

## Στόχος

Μαζική επεξεργασία δέκα πηγών με έμφαση σε:

1. RL-specific uncertainty/OOD detection,
2. robust-MDP sample complexity,
3. online robust policy learning,
4. uncertainty-set design και conservativeness,
5. policy selection ανάμεσα σε ισοδύναμες robust-optimal policies,
6. αποκλεισμό multi-agent, encyclopedic, commercial και application-survey records.

## Αποφάσεις

| Κωδικός | Πηγή | Ρόλος |
|---|---|---|
| `SRC-62996FD690` | Uncertainty-Based OOD Detection in Deep RL | Υποστηρικτική |
| `SRC-6E7AFA8AC0` | Theoretical Understandings of Robust MDPs | Υποστηρικτική |
| `SRC-D1B6BA711E` | Online Policy Optimization for Robust MDP | Υποστηρικτική |
| `SRC-9AF6281E67` | Policy-Conditioned Uncertainty Sets for RMDPs | Υποστηρικτική |
| `SRC-CC5B34C28C` | Best-Effort Policies for RMDPs | Υποστηρικτική |
| `SRC-27B5CE6877` | Multi-Agent/Multi-Robot Decision-Making | Απόρριψη: multi-agent scope |
| `SRC-EC7D639B07` | AI Security Resilience | Απόρριψη: commercial/security scope |
| `SRC-FFDA13CA36` | Multi-agent RL — Wikipedia | Απόρριψη: encyclopedia/MARL |
| `SRC-0490CF519D` | DRL for Autonomous Driving Survey | Απόρριψη: application/redundancy |
| `SRC-D0EDFCACAC` | Markov Decision Process — Wikipedia | Απόρριψη: generic encyclopedia |

## Κλειδωμένες επιστημονικές αποφάσεις

### Static OOD έναντι sequential change detection

- Static train/test OOD separation δεν ισοδυναμεί με online changepoint detection.
- Για detector arm απαιτούνται false-alarm rate, missed-change rate και detection delay πάνω σε trajectories.
- Uncertainty score/variance δεν ερμηνεύεται ως calibrated probability χωρίς calibration protocol.

### Robust-MDP assumptions

Καταγράφονται ρητά:

- uncertainty-set family,
- radius,
- (s,a)-rectangular / s-rectangular / non-rectangular structure,
- nominal model,
- data source και sample budget,
- model-free/model-based storage requirement.

### Δύο επίπεδα αβεβαιότητας

Σε online robust learning διαχωρίζονται:

1. statistical/epistemic uncertainty από περιορισμένα δεδομένα,
2. assumed ambiguity set για πιθανό deployment-model mismatch.

Κανένα από τα δύο δεν βαφτίζεται αυτόματα environmental changepoint.

### Conservativeness και policy selection

Worst-case return μόνο του δεν αρκεί. Για robust baselines αναφέρονται:

- clean/nominal return,
- worst-case return,
- typical/in-set return όπου είναι εφικτό,
- conservativeness gap,
- policy tie-breaking rule όταν υπάρχουν πολλαπλές robust-optimal policies.

### Uncertainty-set construction

Trajectory-level feature constraints μπορούν να μειώσουν την υπερβολική συντηρητικότητα rectangular sets, αλλά εισάγουν prior/modeling choices. Δηλώνονται:

- features,
- reference policy,
- reference-data budget,
- computational overhead.

## Baseline implications

Ο core πίνακας δεν αλλάζει:

1. continual tabular Q-learning,
2. recency/decay Q-learning,
3. full reset,
4. detector-triggered reset,
5. context recall.

Robust methods παραμένουν comparators/ablations και όχι υποκατάστατα online adaptation.

## Scope policy

- MARL/Dec-POMDP uncertainty δεν χρησιμοποιείται ως evidence για single-agent exogenous shifts.
- Wikipedia δεν χρησιμοποιείται για canonical definitions όταν υπάρχουν textbooks/primary sources.
- Commercial cyber/agentic-resilience άρθρα δεν στηρίζουν scientific claims.
- Application surveys δεν προστίθενται όταν δεν παρέχουν νέο controlled protocol.
- Καμία πηγή ή πρωτότυπο δεν διαγράφηκε.

## Generated layer

Το generated package παραμένει derived και δεν θεωρείται ενημερωμένο χωρίς πραγματική εκτέλεση exporter.