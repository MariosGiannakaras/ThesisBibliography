## SRC-D6A6F6F96E — Reward shaping — Mastering Reinforcement Learning

- **Priority:** P2-supporting
- **Topics:** gridworld, reward-uncertainty, tabular-rl, deep-rl
- **Source:** https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html
- **Markdown:** `sources/markdown/SRC-D6A6F6F96E__reward-shaping-mastering-reinforcement-learning.md`
- **Review status:** machine-selected; full-text verification pending

> If we plot the average episode length during training, we see that reward shaping reduces the length of the early episodes because it has knowledge nudging it towards the goal: Example – A Bad Potential Function for GridWorld# This example is thanks to Dr Cathy Wu. Now, let's consider a poorly-designed potential function — one that gives a shaped reward that is the opposite of the earlier potential function for GridWorld: We again compare this to standard Q-learning without reward shaping, but using just the original 4x3 GridWorld (doing this on the larger GridWorld never terminated when I ran this):
