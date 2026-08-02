# Reward shaping — Mastering Reinforcement Learning

- Reward shaping — Mastering Reinforcement Learning

- [Skip to main content](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#main-content)

- Back to top [-] [-] `Ctrl` + `K`

- [Logo imageLogo image](https://gibberblot.github.io/rl-notes/index.html)

- Search `Ctrl` + `K`

- [Contents](https://gibberblot.github.io/rl-notes/index.html)

- Introduction

- [Foreword](https://gibberblot.github.io/rl-notes/intro/foreword.html)

- [What is reinforcement learning?](https://gibberblot.github.io/rl-notes/intro/intro.html)

- [Getting started with a first example](https://gibberblot.github.io/rl-notes/intro/a-first-example.html)

- Single-agent Reinforcement Learning

- [Markov Decision Processes](https://gibberblot.github.io/rl-notes/single-agent/MDPs.html)

- [Value-based methods](https://gibberblot.github.io/rl-notes/single-agent/value-based.html) [x]

- [Value Iteration](https://gibberblot.github.io/rl-notes/single-agent/value-iteration.html)

- [Multi-armed bandits](https://gibberblot.github.io/rl-notes/single-agent/multi-armed-bandits.html)

- [Temporal difference reinforcement learning](https://gibberblot.github.io/rl-notes/single-agent/temporal-difference-learning.html)

- [n-step reinforcement learning](https://gibberblot.github.io/rl-notes/single-agent/n-step.html)

- [Monte-Carlo Tree Search (MCTS)](https://gibberblot.github.io/rl-notes/single-agent/mcts.html)

- [Q-function approximation](https://gibberblot.github.io/rl-notes/single-agent/function-approximation.html)

- [Reward shaping](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html)

- [Policy-based methods](https://gibberblot.github.io/rl-notes/single-agent/policy-based.html) [-]

- [Policy iteration](https://gibberblot.github.io/rl-notes/single-agent/policy-iteration.html)

- [Policy gradients](https://gibberblot.github.io/rl-notes/single-agent/policy-gradients.html)

- [Actor-critic methods](https://gibberblot.github.io/rl-notes/single-agent/actor-critic.html)

- [Modelling and abstraction for MDPs](https://gibberblot.github.io/rl-notes/single-agent/modelling-and-abstraction.html)

- Multi-agent Reinforcement Learning

- [Normal form games](https://gibberblot.github.io/rl-notes/multi-agent/normal-form.html)

- [Extensive form games](https://gibberblot.github.io/rl-notes/multi-agent/extensive-form.html) [-]

- [Backward induction](https://gibberblot.github.io/rl-notes/multi-agent/backward-induction.html)

- [Multi-agent reinforcement learning](https://gibberblot.github.io/rl-notes/multi-agent/multi-agent-rl.html)

- [Modelling and abstraction for multi-agent games](https://gibberblot.github.io/rl-notes/multi-agent/modelling-and-abstraction.html)

- Appendix

- [Introduction to basic probability theory](https://gibberblot.github.io/rl-notes/appendix/intro-to-probability-theory.html)

- [Repository](https://gibberblot.github.io/rl-notes/intro.html)

- [Open issue](https://gibberblot.github.io/rl-notes/intro.html/issues/new?title=Issue%20on%20page%20%2Fsingle-agent/reward-shaping.html&body=Your%20issue%20content%20here.)

- [.md](https://gibberblot.github.io/rl-notes/_sources/single-agent/reward-shaping.md)

- .pdf

# Reward shaping

## Contents

- [Overview](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#overview)

- [Reward shaping](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#id1)

- [Shaped Reward](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#shaped-reward)

- [Potential-based Reward Shaping](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#potential-based-reward-shaping)

- [Example – Potential Reward Shaping for GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-potential-reward-shaping-for-gridworld)

- [Implementation](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#implementation)

- [Example – A Bad Potential Function for GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-a-bad-potential-function-for-gridworld)

- [Q-value initialisation](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#q-value-initialisation)

- [Example – Q-value Initialisation in GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-q-value-initialisation-in-gridworld)

- [Takeaways](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#takeaways)

- [Related Reading](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#related-reading)

# Reward shaping[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#reward-shaping)

- Video byte: Introduction to reward shaping

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- Learning outcomes

- The learning outcomes of this chapter are:

- Explain how reward shaping can be used to help model-free reinforcement learning methods to converge.

- Manually apply reward shaping for a given potential function to solve small-scale MDP problems.

- Design and implement potential functions to solve medium-scale MDP problems automatically.

- Compare and contrast reward shaping with Q-value initialisation.

## Overview[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#overview)

- In the previous chapters, we looked at fundamental temporal difference (TD) methods for reinforcement learning. As noted, these methods have some weaknesses, including that rewards are sometimes **sparse**. This means that there are few state/actions that lead to non-zero rewards. This is problematic because initially, reinforcement learning algorithms behave entirely randomly and will struggle to find good rewards. Remember the example of a [UCT algorithm playing Freeway](https://gibberblot.github.io/rl-notes/single-agent/mcts.html#sec-mcts-demo).

- In this section, we look at two simple approaches that can improve temporal difference methods:

- **Reward shaping**: If rewards are sparse, we can modify/augment our reward function to reward behaviour that we think moves us closer to the solution.

- **Q-value Initialisation**: We can “guess” good Q-values at the start and initialise Q ( s , a ) to be this at the start, which will guide our learning algorithm.

## Reward shaping[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#id1)

- Video byte: Rewarding shaping — The problem

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- Definition – Reward sharping

- **Reward shaping** is the use of small intermediate 'fake' rewards given to the learning agent that help it converge more quickly.

- In many applications, you will have some idea of what a good solution should look like. For example, in our simple navigation task, it is clear that moving towards the reward of +1 and away from the reward of -1 are likely to be good solutions.

- Can we then speed up learning and/or improve our final solution by nudging our reinforcement learner towards this behaviour?

- The answer is: Yes! We can modify our reinforcement learning algorithm slightly to give the algorithm some information to help, while also guaranteeing optimality.

- This information is known as **domain knowledge** — that is, stuff about the domain that the human modeller knows about while constructing the model to be solved.

- Video byte: Reward shaping intuition

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- Exercise: Freeway What would be a good heuristic for the Freeway game to learn how to get the chicken across the freeway?

- Exercise: GridWorld What would be a good heuristic for GridWorld?

### Shaped Reward[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#shaped-reward)

- Video byte: Shaped reward updates

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- In TD learning methods, we update a Q-function when a reward is received. E.g, for 1-step Q-learning:

- Q ( s , a ) ← Q ( s , a ) + α [ r + γ max a ′ Q ( s ′ , a ′ ) − Q ( s , a ) ]

- The approach to reward shaping is not to modify the reward function or the received reward r , but to just give some additional reward for some actions:

- Q ( s , a ) ← Q ( s , a ) + α [ r + F ( s , s ′ ) ⏟ additional reward + γ max a ′ Q ( s ′ , a ′ ) − Q ( s , a ) ]

- The purpose of the function is to give an additional reward F ( s , s ′ ) when any action transitions from state s to state s ′ . The function F : S × S → R provides **heuristic domain knowledge** to the problem that is typically manually programmed.

- We say that r + F ( s , s ′ ) is the **shaped reward** for an action.

- Further, we say that G Φ = ∑ i = 0 ∞ γ i ( r i + F ( s i , s i + 1 ) ) is the shaped reward for the entire episode.

- If we define F ( s , s ′ ) > 0 for states s and s ′ , then this provides a small positive reward for transitioning from s to s ′ , thus encouraging actions that transition from s to s ′ in future exploitation. If we define F ( s , s ′ ) < 0 for states s and s ′ , then this provides a small *negative* reward for transitioning from s to s ′ , thus discouraging actions that transition like this in future exploitation.

### Potential-based Reward Shaping[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#potential-based-reward-shaping)

- Video byte: Potential-based reward shaping

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- **Potential-based** reward shaping is a particular type of reward shaping with nice theoretical guarantees. In potential-based reward shaping, F is of the form:

- F ( s , s ′ ) = γ Φ ( s ′ ) − Φ ( s )

- We call Φ the **potential function** and Φ ( s ) is the **potential** of state s .

- So, instead of defining F : S × S → R , we define Φ : S → R , which is some heuristic measure of the value of each state s ∈ S .

- **Theoretical guarantee**: this will still converge to the optimal policy under the assumption that all state-action pairs are sampled infinitely often.

- This is quite straightforward to show as follows. Consider an episode with shaped reward G Φ :

- G Φ = ∑ i = 0 ∞ γ i ( r i + F ( s i , s i + 1 ) ) = ∑ i = 0 ∞ γ i ( r i + γ Φ ( s i + 1 ) − Φ ( s i ) ) = ∑ i = 0 ∞ γ i r i + ∑ i = 0 ∞ γ i + 1 Φ ( s i + 1 ) − ∑ i = 0 ∞ γ i Φ ( s i ) = G + ∑ i = 0 ∞ γ i Φ ( s i ) − Φ ( s 0 ) − ∑ i = 0 ∞ γ i Φ ( s i ) = G − Φ ( s 0 )

- where G refers to the shaped reward for the episode, and s 0 is the starting state of the episode. What this says is that the shaped reward G Φ is just the unshaped reward G minus the potential of the initial state s 0 . However, because F does not depend on the actions and G Φ does not depend on shaped rewards beyond the initial state, the **shaped Q function**, which we refer to as Q Φ , can be defined as just Q Φ ( s , a ) = Q ( s , a ) + Φ ( s ) . Given this, any optimal policy extracted from Q Φ will be equivalent to any optimal policy extracted from Q .

- **However!** While it provides guarantees about the end result, potential-based reward shaping may either increase or decrease the time taken to learn. A well-designed potential function decrease the time to convergence.

### Example – Potential Reward Shaping for GridWorld[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-potential-reward-shaping-for-gridworld)

- Video byte: Example – Reward shaping in Q-learning

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- For Grid World, we use the Manhattan distance to define the potential function, normalised by the size of the grid:

- Φ ( s ) = 1 − | x ( g ) − x ( s ) | + | y ( g ) − y ( s ) | w i d t h + h e i g h t − 2

- in which x ( s ) and y ( s ) return the x and y coordinates of the agent respectively, g is the goal state. and w i d t h and h e i g h t are the width and height of the grid respectively. Note that the coordinates are indexed from 0, so we subtract 2 from the denominator.

- Even on the very first iteration, a greedy policy such as ϵ -greedy, will feedback those states closer to the +1 reward. From state (1,2) with γ = 0.9 if we go Right, we get:

- F ( ( 1 , 2 ) , ( 2 , 2 ) ) = γ Φ ( 2 , 2 ) − Φ ( 1 , 2 ) = 0.9 ⋅ ( 1 − 1 5 ) − ( 1 − 2 5 ) = 0.12

- We can compare the Q-values for these states for the four different possible moves that could have been taken from (1,2), using and α = 0.1 and γ = 0.9 :

- Action r F ( s , s ′ ) γ max a ′ Q ( s ′ , a ′ ) New Q ( s , a ) U p 0 0.9 ( 1 − 2 5 ) − ( 1 − 2 5 ) = − 0.06 0 − 0.006 D o w n 0 0.9 ( 1 − 2 5 ) − ( 1 − 2 5 ) = − 0.06 0 − 0.006 R i g h t 0 0.9 ( 1 − 1 5 ) − ( 1 − 2 5 ) = − 0.12 0 − 0.012 L e f t 0 0.9 ( 1 − 3 5 ) − ( 1 − 2 5 ) = − 0.24 0 − 0.024

- Thus, we can see that our potential reward function rewards actions that go towards the goal and penalises actions that go away from the goal. Recall that state (1,2) is in the top row, so action Up just leaves us in state (1,2) and Down similarly because we cannot go through the walls.

- But! It will not always work. Compare states (0,0) and (0,1). Our potential function will reward (0,1) because it is closer to the goal, but we know from from our value iteration example that (0,0) is a higher value state than (0,1). This is because our reward function does not consider the negative reward.

- In practice, it is non-trivial to derive a perfect reward function – it is the same problem as deriving the perfect search heuristic. If we could do this, we would not need to even use reinforcement learning – we could just do a greedy search over the reward function.

### Implementation[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#implementation)

- To implement potential-based reward shaping, we need to first implement a potential function. We implement potential functions as subclasses of `PotentialFunction` . For the GridWorld example, the potential function is 1 minus the normalised distance from the goal:

- Reward shaping for Q-learning is then a simple extension of the `QLearning` class, overriding the `get_delta` method:

- Video byte: Reward shaping in Super Gridworld

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- We can run this on a GridWorld example with more states, to make the problem harder::

- Now, we compare this with Q-learning without reward shaping:

- If we plot the average episode length during training, we see that reward shaping reduces the length of the early episodes because it has knowledge nudging it towards the goal:

### Example – A Bad Potential Function for GridWorld[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-a-bad-potential-function-for-gridworld)

- This example is thanks to [Dr Cathy Wu](http://www.wucathy.com/). Now, let's consider a poorly-designed potential function — one that gives a shaped reward that is the opposite of the earlier potential function for GridWorld:

- We again compare this to standard Q-learning without reward shaping, but using just the original 4x3 GridWorld (doing this on the larger GridWorld never terminated when I ran this):

- Plotting the episode length, we see that it shapes the reward quite poorly:

- Note that this is so poor that the difference between the standard Q-learning and reward-shaped Q-learning is barely visible on this new graph — and remember that the bad reward shaping example is run on the small 4x3 GridWorld example, not the larger 10x8 version, for which the results would be much worse.

- However, notice that because we use a potential function, it still converges to a (close-to) optimal policy! But in this case, the convergence takes longer because the potential function is misleading.

## Q-value initialisation[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#q-value-initialisation)

- Video byte: Q-value initialisation

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

- An approach related to reward shaping is **Q-value initialisation**. Recall that TD learning methods can start at any arbitrary Q-function. The closer our Q-values is to the optimal Q-values, the quicker it will converge.

- Imagine if we happened to initialise our Q-values to the optimal Q-value. It would converge in one step!

- Q-value initialisation is similar to reward shaping: we use heuristics to assign higher values to 'better' states. If we just define Φ ( s ) = V 0 ( s ) , then they are equivalent. In fact, if our potential function is **static** (the definition does not change during learning), then Q-value initialisation and reward shaping are equivalent[[ 1]](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#id3).

### Example – Q-value Initialisation in GridWorld[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-q-value-initialisation-in-gridworld)

- Using the idea of Manhattan distance for a potential function, we can define an initial Q-function as follows for state (1,2) using our potential function:

- Q ( ( 1 , 2 ) , U p ) = 0.9 ( 1 − 2 5 ) − ( 1 − 2 5 ) = − 0.06 Q ( ( 1 , 2 ) , D o w n ) = 0.9 ( 1 − 2 5 ) − ( 1 − 2 5 ) = − 0.06 Q ( ( 1 , 2 ) , R i g h t ) = 0.9 ( 1 − 1 5 ) − ( 1 − 2 5 ) = 0.12 Q ( ( 1 , 2 ) , L e f t ) = 0.9 ( 1 − 3 5 ) − ( 1 − 2 5 ) = − 0.24

- Once we start learning over episodes, we will select those actions with a higher heuristic value, and also we are already closer to the optimal Q-function, so will will converge faster. As with reward shaping though, this entirely depends on having a good potential function! A poor potential function will give an inaccurate initial Q-values, which may take longer to converge.

- Video byte: Summary

- Tap to unmute

- Your browser can't play this video.

- [Learn more](https://www.youtube.com/supported_browsers)

## Takeaways[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#takeaways)

- Takeaways

- A weakness of model-free methods is that they spend a lot of time exploring at the start of the learning. It is not until they find some rewards that the learning begins. This is particularly problematic when rewards are sparse.

- **Reward shaping** takes in some domain knowledge that “nudges” the learning algorithm towards more positive actions.

- **Q-value initialisation** is a “guess” of the initial Q-values to guide early exploration

- Reward sharping and Q-value initialisation are equivalent if our potential function is static.

- **Potential-based reward shaping** guarantees that the policy will converge to the same policy without reward shaping.

### Related Reading[#](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#related-reading)

- Chapter 9 (Approximate Solution Methods) of [Introduction to Reinforcement Learning, Sutton and Barto](http://incompleteideas.net/book/the-book-2nd.html)

- [ [1](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#id2)]

- Wiewiora, Eric. “Potential-based shaping and Q-value initialization are equivalent.” Journal of Artificial Intelligence Research 19 (2003): 205-208. [https://www.jair.org/index.php/jair/article/download/10338/24713/](https://www.jair.org/index.php/jair/article/download/10338/24713/)

- [previous Q-function approximation](https://gibberblot.github.io/rl-notes/single-agent/function-approximation.html)

- [next Policy-based methods](https://gibberblot.github.io/rl-notes/single-agent/policy-based.html)

- Contents

- [Overview](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#overview)

- [Reward shaping](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#id1)

- [Shaped Reward](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#shaped-reward)

- [Potential-based Reward Shaping](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#potential-based-reward-shaping)

- [Example – Potential Reward Shaping for GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-potential-reward-shaping-for-gridworld)

- [Implementation](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#implementation)

- [Example – A Bad Potential Function for GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-a-bad-potential-function-for-gridworld)

- [Q-value initialisation](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#q-value-initialisation)

- [Example – Q-value Initialisation in GridWorld](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#example-q-value-initialisation-in-gridworld)

- [Takeaways](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#takeaways)

- [Related Reading](https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html#related-reading)

- By Tim Miller, The University of Queensland

- © Copyright 2023.