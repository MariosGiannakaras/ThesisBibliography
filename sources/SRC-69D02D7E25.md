> Source: https://proceedings.mlr.press/v80/pardo18a.html

# Time Limits in Reinforcement Learning

Fabio Pardo, Arash Tavakoli, Vitaly Levdik, Petar Kormushev

Proceedings of the 35th International Conference on Machine Learning, PMLR 80:4045-4054, 2018.

Canonical article page: https://proceedings.mlr.press/v80/pardo18a.html

Protocol-v2 closure relevance: distinguishes finite-horizon termination from administrative time-limit truncation. For genuine finite-horizon objectives, remaining time must be part of the state to preserve the Markov property; for time-unlimited tasks with artificial episode cutoffs, value-based learning should bootstrap across the truncation. This source is needed to resolve the thesis GridWorld `max_steps` semantics and document the historical v1.x `bootstrap_on_truncation=False` limitation without rewriting frozen evidence.