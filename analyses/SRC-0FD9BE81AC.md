---
κωδικός: SRC-0FD9BE81AC
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "ICML 2025, PMLR 267:38397–38423; official PMLR/author manuscript"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-09-05"
---

# Ανάλυση — Continual Reinforcement Learning by Planning with Online World Models

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Zichen Liu, Guoji Fu, Chao Du, Wee Sun Lee, Min Lin
- **Έτος:** 2025
- **Έκδοση:** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, pp. 38397–38423; ICML 2025 Spotlight
- **Τύπος:** peer-reviewed πρωτογενής εργασία continual/model-based reinforcement learning
- **Επίσημη έκδοση που ελέγχθηκε:** official PMLR record/full paper, cross-checked with arXiv:2507.09177

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει continual reinforcement learning ως ακολουθία tasks που παρουσιάζονται διαδοχικά και όπου ο agent πρέπει να αποκτά νέες ικανότητες χωρίς να ξεχνά παλιές. Το βασικό πρόβλημα είναι catastrophic forgetting. Οι συγγραφείς προτείνουν να αποθηκεύεται reusable knowledge σε ένα online world-dynamics model και η συμπεριφορά να κατασκευάζεται με model predictive control, αντί να εξαρτάται αποκλειστικά από task-specific policy/value parameters που ανανεώνονται διαδοχικά.

Για τη διπλωματική η πηγή είναι χρήσιμη ως πρόσφατο primary example model-based continual RL. Δεν αποτελεί paper για tabular Dyna-Q+ ούτε αξιολογεί το frozen thesis disturbance protocol.

## Μεθοδολογία

- **World model:** shallow/wide Follow-The-Leader online model, updated incrementally from real state-action-transition data.
- **Planning:** model predictive control with cross-entropy method (CEM), replanning from the latest state through the current learned model.
- **Theoretical analysis:** Section 4.2 proves a regret bound for the sparse online model update under explicit assumptions.
- **Benchmark:** Continual Bench, six MuJoCo/Meta-World manipulation tasks with unified physical dynamics, common state/action structure and reward-defined task changes.
- **Evaluation:** average performance over all seen tasks and online regret; experiments compare model-based world-model agents under common CEM/MPC planning plus model-free continual-learning baselines.
- **Baselines:** fine-tuning, regularization/architecture/replay approaches and Perfect Memory variants as described in Section 6 and Appendix A.

## Κύρια ευρήματα με ακριβείς θέσεις

1. **CRL requires retention as well as acquisition.** Abstract and Section 1: continual tasks arrive sequentially and catastrophic forgetting is identified as a primary obstacle; evaluation therefore includes previously experienced tasks rather than only the newest task.
2. **Shared world dynamics is the proposed persistent knowledge component.** Section 3.2 and Sections 4.1/4.3: the agent learns dynamics online and forms actions by MPC/CEM planning; reward functions specify the active task while the dynamics model is reused.
3. **The theoretical guarantee is method-specific.** Section 4.2, Theorem 1, with proof in Appendix E.3.2: the sparse FTL world-model update has a sublinear regret bound under Assumptions 1–3 concerning feature behavior, bounded quantities and sparsity/update conditions.
4. **Continual Bench intentionally separates task objectives from shared dynamics.** Figure 3, Section 6.1 and Appendix B: six manipulation tasks share unified dynamics and common 26-dimensional state / 4-dimensional action structure; the reward changes on task switch.
5. **Task-boundary information is not universally hidden.** Section 6.1: reward change defines the switch and the world-model learner is not given task-boundary information unless a particular continual-learning baseline requires it. Appendix D further states that the benchmark is episodic with explicit task switches across episodes.
6. **OA retains earlier-task performance in the studied framework.** Sections 6.3–6.4, Figures 5–6 and Table 1: OA maintains high performance on prior tasks while several deep-model baselines forget to varying degrees. Table 1 reports OA AP 72.93% / regret 27.62%; model-based Perfect Memory AP 73.09% / regret 30.95%.
7. **The authors state important limitations.** Appendix D: moderate-dimensional state-based observations, no modeled world uncertainty, no explicit exploration in planning, and an episodic rather than reset-free continual benchmark.

## Υποθέσεις και ορισμοί που πρέπει να διατηρηθούν

- Η key reuse assumption είναι **unified world dynamics** across tasks, ενώ reward functions αλλάζουν ανά task.
- Η no-regret statement αφορά το συγκεκριμένο sparse FTL world-model learning rule και τις stated assumptions, όχι οποιοδήποτε world model.
- Planning through the model με MPC/CEM δεν είναι το ίδιο mechanism με Dyna-style model-generated learning updates.
- Continual Bench μετρά multi-task retention/forgetting και transfer opportunities· το thesis protocol μετρά bounded post-change adaptation/recovery σε μία controlled task family.

## Περιορισμοί και threats to validity

- Η unified-dynamics/reward-switch non-stationarity διαφέρει ουσιωδώς από persistent action remap, stochastic no-op action failure και observation corruption.
- Τα robotic manipulation results δεν τεκμηριώνουν ranking σε discrete GridWorld.
- Η theoretical no-forgetting/no-regret reasoning δεν μεταφέρεται σε Dyna-Q+, DQN, PPO ή άλλα thesis agents.
- Η current OA δεν μοντελοποιεί world uncertainty και δεν περιλαμβάνει explicit exploration στο planner.
- Το benchmark είναι episodic με switches between episodes, όχι reset-free lifelong stream.
- Perfect Memory και οι λοιπές baselines είναι paper-specific implementations και δεν αποτελούν universal upper bounds.

## Σχέση και κατάταξη έναντι υπάρχουσας βιβλιογραφίας

- `SRC-39696F490F` (Khetarpal et al., JAIR 2022) παραμένει ισχυρότερη **core taxonomy/review** πηγή για continual-RL framing, scope/driver of non-stationarity, stability–plasticity και evaluation principles. Το Liu 2025 δεν την αντικαθιστά.
- `SRC-8025C139CE` (Padakandla) παραμένει πιο άμεσο broad survey evidence για dynamically varying environments και stationary/non-stationary assumption boundaries.
- `SRC-F6BD3A6B18` και το canonical Dyna evidence παραμένουν οι σωστές primary/foundational πηγές για Dyna/Dyna-Q+ mechanisms.
- `SRC-D38364B32C` (Alver et al., 2025) είναι closer-fit modern evidence για learned-model freshness/local adaptation and stale replay/model problems under environmental change.
- Το Liu 2025 **προσθέτει** κάτι διαφορετικό: recent primary evidence για online world-model persistence, direct MPC planning, multi-task forgetting/retention metrics και a shared-dynamics continual benchmark.

## Χρήση στη διπλωματική

- **Ρόλος:** υποστηρικτική
- **Προτεινόμενα κεφάλαια:** Related Work; Scope/Methodology boundaries; Discussion; Future Work
- **Επιτρεπτές χρήσεις:** recent model-based continual RL, distinction between online world-model planning and Dyna-style planning updates, catastrophic forgetting/retention, unified-dynamics task sequences, explicit limitations.
- **Μη επιτρεπτές χρήσεις:** claim ότι Dyna-Q+ = OA, ότι model-based agents είναι γενικά ανώτερα, ότι the regret theorem applies to thesis methods, ή ότι Continual Bench results predict thesis GridWorld recovery.

## Απόφαση

**Επιλογή ως υποστηρικτική citation-ready πηγή.** Είναι υψηλής ποιότητας recent primary work για ένα στενό model-based CRL claim, αλλά δεν αντικαθιστά τις foundational/review πηγές ούτε το closer-fit evidence για the thesis's specific non-stationarity and Dyna mechanisms.

Ρόλος: υποστηρικτική
Εξαγωγή: ναι

## Απαιτούμενα αποσπάσματα

Το `evidence/SRC-0FD9BE81AC.md` περιέχει verified evidence για CRL/forgetting, shared online world models and MPC planning, the method-specific regret result, Continual Bench assumptions, bounded empirical results and explicit limitations.
