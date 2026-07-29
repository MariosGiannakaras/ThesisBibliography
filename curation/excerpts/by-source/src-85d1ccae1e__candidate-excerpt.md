## SRC-85D1CCAE1E — Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without

- **Priority:** P1-core
- **Topics:** robust-rl, resilience-recovery, transition-uncertainty
- **Source:** https://arxiv.org/abs/2508.17448
- **Markdown:** `sources/markdown/SRC-85D1CCAE1E__rectified-robust-policy-optimization-for-model-uncertain-constrained-rei.md`
- **Review status:** machine-selected; full-text verification pending

> or (s, a)-rectangular set (Wiesemann et al., 2013; Kumar et al., 2023) P := ×(s,a)∈S×AP(s,a). Here, instead of assuming a specific type of uncertainty set as in many existing literature (Wang & Zou, 2021; Wang et al., 2022), we work on general uncertainty sets but simply assume that the robust value function over these uncertainty set is computationally available. Notably, for many well-known uncertainty sets, such as the p-norm (Kumar et al., 2023), IPM (Zhou et al., 2024), and R-contamination (Wang & Zou, 2021) uncertainty set, the robust value function can be efficiently calculated without hurting the sample complexity. Let the policy π : S → ∆(A) map each state to a probability distribution over actions. In robust RL, the robust value function V π(s) under policy π starting from state s is defined as the worst-case expected discounted cumulative reward: V π(s) = inf P ∈P Eπ,P [ ∞∑ t=…
