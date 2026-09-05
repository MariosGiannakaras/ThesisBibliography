# Continual Reinforcement Learning by Planning with Online World Models

- Authors: Zichen Liu, Guoji Fu, Chao Du, Wee Sun Lee, Min Lin
- Year: 2025
- Venue: Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267, pages 38397–38423
- Publication page: https://proceedings.mlr.press/v267/liu25p.html
- Full paper: https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25p/liu25p.pdf

## Intake rationale

Recent peer-reviewed continual-RL work with particular relevance to the thesis's model-based Dyna-Q+ comparator and to the distinction between direct adaptation and retained/updated dynamics knowledge. The work proposes an online world model with planning and introduces Continual Bench for sequential continual-RL evaluation.

This is not evidence that Dyna-Q+ should outperform or underperform in the thesis GridWorld. Its value is conceptual and comparative: model-based continual adaptation can be framed around an online dynamics model; forgetting and adaptation are distinct concerns; and a planning-based method can be evaluated under a continual sequence rather than only on a fixed task.

## Claims to verify during analysis

1. The paper defines continual reinforcement learning as an agent repeatedly adapting through trial and error to sequentially presented tasks.
2. It identifies catastrophic forgetting as a central obstacle and proposes planning with an online world model as its main mechanism.
3. The proposed online model is updated incrementally and is used by a planner for task solving.
4. The paper introduces Continual Bench as a dedicated CRL environment and compares against alternative world-model/continual-learning baselines.
5. Any thesis use must preserve the methodological boundary: this paper's world-model/planning setup is not the same algorithm as tabular Dyna-Q+, and its empirical superiority does not transfer numerically to the thesis GridWorld.

## Candidate thesis use

- Related Work: recent model-based continual RL and world-model planning.
- Background/Discussion: model freshness, model retention, and adaptation under non-stationary sequences.
- Limitations/Future Work: richer model-based continual methods beyond tabular Dyna-Q+ and evaluation of forgetting across repeated task sequences.
