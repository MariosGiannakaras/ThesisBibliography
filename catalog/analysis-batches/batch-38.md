# Παρτίδα 38 — unknown changepoints και deep detection-adaptation

Ημερομηνία: 2026-08-01

## Selected

### `SRC-E5CA725A6C` — Zihe Liu, *Deep Reinforcement Learning in Non-stationary Environments* (PhD, UTS, 2024)
- **Ρόλος:** κύρια
- **Κατάσταση:** επαληθευμένη σε πλήρες converted thesis
- **Εξαγωγή:** ναι
- **Citation-ready excerpts:** ναι

Η διατριβή είναι από τις πιο άμεσες πηγές του corpus για το ερευνητικό αντικείμενο. Διατυπώνει RL σε ακολουθία MDPs με **unknown change points** και αναπτύσσει ρητά χωριστά modules για detection και adaptation.

### Κύρια επιστημονικά σημεία
- DARL: joint detection από state marginal + policy/conditional change και ξεχωριστή policy adaptation.
- Η διατήρηση όλων των προηγούμενων policies μπορεί να δημιουργήσει negative transfer· adaptation πρέπει να εξαρτάται από τη συνάφεια/απόσταση του νέου regime.
- Detector F1 και detection delay είναι διαφορετικές μεταβλητές. Στα reported experiments μπορεί detector με καλύτερο/ίσο F1 να έχει μεγαλύτερο delay.
- False alarms και missed changes έχουν διαφορετικά operational costs.
- Τα DARL experiments περιλαμβάνουν multiple change points σε CartPole, LunarLander, MiniGrid και VizDoom.
- FDA: Wasserstein functional surprise + Welch test, change-magnitude-aware preservation και bounded representative memory.
- Το FDA F1 ορίζει detection ως correct εντός 5 epochs από ground-truth change· η tolerance window είναι μέρος του metric definition.
- Βασική limitation: το κύριο formulation υποθέτει αρκετό χρόνο ώστε policy να συγκλίνει πριν την επόμενη αλλαγή.

## Exclusions
1. `SRC-BD5C631CA8` — SafeRL seminar YouTube playlist/index· discovery only.
2. `SRC-8E786113C3` — Stanford deep-RL course/video material.
3. `SRC-1550322156` — Stanford CS234 model-free policy-evaluation lecture.
4. `SRC-97178F6279` — educational GridWorld value/policy tutorial.
5. `SRC-D19D1DF801` — Sutton & Barto Gridworld C# implementation example.
6. `SRC-58DE790914` — LLM-agent prompting practitioner source.
7. `SRC-B1CC6687F0` — broad LLM/autonomous-agent architecture synthesis.
8. `SRC-C115B0240F` — legal essay on AI agents and liability.
9. `SRC-643DB6CBFE` — infrastructure/storage/business-continuity resilience, όχι policy resilience.
10. `SRC-A76BF5B717` — unrelated mathematical topology paper/import noise.
11. `SRC-7F30DDB0B2` — local-AI/agent guide.
12. `SRC-BFD3447AEF` — broad agentic-AI report.
13. `SRC-3174B1019C` — business/productivity AI-agents report.
14. `SRC-CA89A30F17` — MATLAB basic GridWorld example.
15. `SRC-1A15DFC70B` — MATLAB/Simulink GridWorld documentation.
16. `SRC-4C4598C8F4` — IBM introductory AI-agent taxonomy.
17. `SRC-8F03D3E086` — UAI 2024 YouTube conference playlist/index.
18. `SRC-F5CA634608` — duplicate of the same UAI playlist.
19. `SRC-8DDCC8572D` — practitioner AI-agents/LLM/expert architecture article.

## Νέες protocol αποφάσεις
1. **Detector scorecard και adapter scorecard χωριστά.**
2. Detector metrics: precision, recall, F1, detection delay, false alarms, misses και declared tolerance window.
3. Report **utility cost per false alarm**, όχι μόνο false-alarm count.
4. Report effect of missed/late detection on recovery.
5. No-transfer/scratch baseline υποχρεωτικό για να μετριέται negative-transfer gap.
6. Change magnitude πρέπει να είναι experimental factor επειδή επηρεάζει το σωστό retention/plasticity trade-off.
7. Multiple changes αναφέρονται ανά occurrence, όχι μόνο με τελικό aggregate return.
8. Προστίθεται **frequent-switch stress test** όπου η επόμενη αλλαγή μπορεί να συμβεί πριν από πλήρη convergence, ώστε να ελεγχθεί η limitation της βασικής DARL formulation.
9. Detector F1 μεταξύ papers δεν συγκρίνεται χωρίς να ελέγχεται το allowed detection window.
10. Joint/multi-signal detection μπορεί να εξεταστεί ως optional ablation, αλλά δεν θεωρείται εκ των προτέρων ανώτερο χωρίς calibration.

## Totals μετά την παρτίδα
Starting point Παρτίδα 37: 329 αποφασισμένες = 96 selected + 233 exclusions.

- Νέες αποφάσεις: 20
- Νέες selected: 1
- Νέες exclusions: 19
- Νέα citation-ready excerpt sets: 1
- Canonical σύνολο: **349 αποφασισμένες = 97 selected + 252 exclusions**
- Υπόλοιπη ουρά: **137 / 486 ενεργές πηγές**

## Infrastructure note
Τα totals βασίζονται στα canonical analyses/batch records. Το generated status και το curated export παραμένουν μη αξιόπιστα έως ασφαλή regeneration/sync.