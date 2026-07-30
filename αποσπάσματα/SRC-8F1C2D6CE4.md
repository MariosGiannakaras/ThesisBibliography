## SRC-8F1C2D6CE4 — ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty - arXiv

- **Προτεραιότητα:** P1-core
- **Θέματα:** robust-rl, transition-uncertainty
- **Πηγή:** https://arxiv.org/abs/2510.11899
- **Αρχείο:** `πηγές/SRC-8F1C2D6CE4.md`
- **Κατάσταση ελέγχου:** αυτόματη επιλογή· εκκρεμεί έλεγχος του πλήρους κειμένου

> - Robust reinforcement learning (Robust RL) seeks to handle epistemic uncertainty in environment dynamics, but existing approaches often rely on nested min–max optimization, which is computationally expensive and yields overly conservative policies. We propose Adaptive Rank Representation (AdaRL), a bi-level optimization framework that improves robustness by aligning policy complexity with the intrinsic dimension of the task. At the lower level, AdaRL performs policy optimization under fixed-rank constraints with dynamics sampled from a Wasserstein ball around a centroid model. At the upper level, it adaptively adjusts the rank to balance the bias–variance trade-off, projecting policy parameters onto a low-rank manifold. This design avoids solving adversarial worst-case dynamics while ensuring robustness without over-parameterization. Empirical results on MuJoCo continuous control benchm…
