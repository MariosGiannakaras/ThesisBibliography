> Source: https://proceedings.mlr.press/v199/steinparz22a/steinparz22a.pdf

# Reactive Exploration to Cope With Non-Stationarity in Lifelong Reinforcement Learning

Christian Alexander Steinparz, Thomas Schmied, Fabian Paischer, Marius-Constantin Dinu, Vihang Prakash Patil, Angela Bitto-Nemling, Hamid Eghbal-zadeh, Sepp Hochreiter

Proceedings of The 1st Conference on Lifelong Learning Agents (CoLLAs), PMLR 199:441-469, 2022.

arXiv:2207.05742

The paper studies reinforcement learning under environmental non-stationarity and compares exploration/adaptation behavior across value-based and policy-gradient approaches. Its experiments are directly relevant to protocol-v2 interpretation of ordinary continued training after change and to the scientific importance of replay-buffer allocation and stale experience for DQN-like agents. It does not justify resetting replay by default; rather, it supports treating replay management as part of the adaptation mechanism.
