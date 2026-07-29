## SRC-AC79E9A264 — Robust Policy Learning over Multiple Uncertainty Sets

- **Priority:** P2-supporting
- **Topics:** robust-rl
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-AC79E9A264__robust-policy-learning-over-multiple-uncertainty-sets.md`
- **Review status:** machine-selected; full-text verification pending

> Abstract Reinforcement learning (RL) agents need to be robust to variations in safety-critical environments. While system identification methods provide a way to infer the variation from online experience, they can fail in settings where fast identification is not possible. Another dominant approach is robust RL which produces a policy that can handle worst-case scenarios, but these methods are generally designed to achieve robustness to a single uncertainty set that must be specified at train time. Towards a more general solution, we formulate the multi-set robustness problem to learn a policy robust to different perturbation sets. We then design an algorithm that enjoys the benefits of both system identification and robust RL: it reduces uncertainty where possible given a few interactions, but can still act robustly with respect to the remaining uncertainty. On a diverse set of control…
