> Source: https://indico.cern.ch/event/828418/contributions/3582746/attachments/1920959/3177770/tutorial_RL.pdf

An Introduction to Reinforcement Learning 
Dr Ing. Gianluca Valentino 
Department of Communications and Computer Engineering 
University of Malta
Outline 
 What is Reinforcement Learning? 
 RL terminology: states, actions, reward, policy 
 Value function and Q-value function 
 Q-learning and neural networks 
 Python notebooks: Grid World and Cart Pole
What is Reinforcement Learning? 
 So far: Supervised Learning 
 Data: (X, y) 
 Goal: Learn a function to map X -> y 
 Examples: classification, regression, object detection etc 
Dog 
 So far: Unsupervised Learning 
 Data: X (no y) 
 Goal: Learn some underlying hidden structure in the data 
 Examples: clustering, dimensionality reduction, anomaly detection 
Abnormal 
Normal
What is Reinforcement Learning? 
 In Reinforcement Learning, an agent interacts with an environment to learn how to perform a particular task well. 
 How is it different to the other learning paradigms? 
 There is no supervisor, only a reward. 
 The agent’s actions affect the subsequent data it receives 
 Feedback is delayed, and may be received after several actions
Cat Agent 
State: Sitting 
Action: walk Come here! 
Reward 
Action: keep sitting 
Stay hungry.. 
Observable
Examples of Reinforcement Learning 
Fly a helicopter 
Make a robot walk 
Manage an investment portfolio 
Play Atari games better than humans
Rewards 
 The agent receives feedback from the environment through reward 
 A reward Rt is a scalar feedback signal 
 It is an indication of how well the agent is doing at step t 
 The agent’s job is to maximise cumulative reward 
 Examples: 
 Winning a game 
 Achieving design luminosity in a collider 
 Maintaining an inverted pendulum at the top
Sequential decision making 
 Goal: select actions to maximise total future reward 
 Actions may have long term consequences 
 Reward may be delayed 
 It may be better to sacrifice immediate reward to gain more longterm reward 
 Examples: 
 A financial investment (may take months to mature) 
 Blocking opponent moves (might help winning probability many moves from now)
States 
 State: what the agent is observing about the environment 
 Examples: 
 Pixels in an image (of a game, of a driverless car, etc) 
 Data from beam instrumentation in an accelerator 
 The position of all pieces in a game of chess
The agent and its environment 
Agent 
Environment 
Reward rt 
Next state st+1 
State st Action at 
Markov Decision Process (MDP) 
A0 
S0 
R1 
S1 S2 
R2 
A1 
 Markov property: current state 
completely characterizes state of the world. 
 Defined by: (S, A, R, P, γ) 
 S: set of possible states 
 A: set of possible actions 
 R: reward for a given (state, action) pair 
 P(st|st-1, at): transition probability 
 γ: Discount factor (usually close to 1)
Markov Decision Process (MDP) 
 At time step t = 0, environment samples initial state s0 ~ P(s0) 
 Then, for t = 0 until done: 
 Agent selects action at 
 Environment samples reward rt ~ R( . | st, at) 
 Environment samples next state st+1 ~ P( . | st, at) 
 Agent receives reward rt and next state st+1. 
 A policy π is a function which specifies what action to take by the agent in each state. 
 Objective: find a policy π* that maximizes cumulative discounted reward
A simple MDP: Grid World 
actions = { 
1. right 
2. left 
3. up 
4. down 
} 
Objective: reach one of the terminal states 
A simple MDP: Grid World 
Random Policy Optimal Policy
The optimal policy π* 
 Need to find the optimal policy π* that maximizes the sum of rewards. 
 To handle randomness (initial state, transition probability etc): 
 Maximize the expected sum of rewards
Definitions: Value function and Q-value function 
 Following a policy produces sample trajectories (or paths) s0, a0, r0, s1, a1, r1, … 
 How good is a state? 
 The value function at state s is the expected cumulative reward from following the 
policy from state s: 
 How good is a state-action pair? 
 The Q-value function at state s and action a, is the expected cumulative reward from 
taking action a in state s and then following the policy:
Bellman equation 
 The optimal Q-value function Q* is the maximum expected cumulative reward 
achievable from a given (state, action) pair: 
 Q* satisfies the Bellman equation: 
 Intuition: if the optimal state-action values for the next time-step Q*(s’,a’) are known, then the optimal strategy is to take the action that maximizes the expected value of 
 Optimal policy π* -> taking the best action in any state as specified by Q*.
Solving for the optimal policy 
 Value iteration algorithm: use the Bellman equation as an iterative update: 
 Qi will converge to Q* as i -> infinity.
Exploration vs Exploitation 
During training, we could e.g.: 30% of the time we choose a random action 
Grid world example 
End Reward: +1 
End Reward: -1 
Start 
 Agent starts at bottom left. 
 At each step, agent has 4 possible actions (up, down, left, right). 
 Black square: agent cannot move through it. 
 Assume each action is deterministic.
Grid world example 
 First, define the grid world parameters:
Grid world example 
 Define the reward:
Grid world example 
 Probabilistic result of taking an action:
Grid world example 
 Define how the state is updated when the action is taken by the agent. 
 Need to check that the next state is not the black box or else outside the grid.
Grid world example 
 Tradeoff between exploration (new info) and exploitation (greedy actions):
Grid world example 
 Define stopping condition:
Grid world example • Bring everything together:
Grid world example 
 Let’s have a look at test_gridworld_qlearning.ipynb 
 http://bit.ly/338nV5e 
 After running the notebook, change “DETERMINISTIC” from True to False. What do you notice?
Solving for the optimal policy: Q-learning 
 Value iteration algorithm: use the Bellman equation as an iterative update: 
 Qi will converge to Q* as i -> infinity. 
 What is the problem with this? 
 Not scalable: must compute Q(s, a) for every state-action pair. If state is e.g. current 
game state pixels, computationally infeasible to compute for entire state space! 
 Solution: use a function approximator to estimate Q(s,a). 
 A neural network! 
Solving for the optimal policy: Q-learning 
 Q-learning: use a function approximator to estimate the action-value function: 
Q(s, a; Θ) ≈ Q*(s, a) 
Where Θ are the neural network weights which need to be learned. 
 If the function approximator is a deep neural network -> deep q-learning (DQN)!
RL agent types 
 
Tries to learn a policy directly instead of learning the exact value of every (state, action) pair 
Combines Policy Gradients and Q-learning by training both an actor (the policy) and a critic (the Q-function) 
Cartpole Problem 
 Objective: Balance a pole on top of a movable cart 
 State: angle, angular speed, position, horizontal velocity 
 Action: horizontal force applied on the cart (or not) 
 Reward: +1 at each time step if the pole is upright 
(within some limits)
OpenAI Gym 
 In order to train an agent to perform a task, we need a suitable physical environment. 
 OpenAI gym provides a number of ready environments for common problems, e.g. Cart Pole, Atari Games, Mountain Car 
 However, you can also define your own environment following the OpenAI Gym framework (e.g. physical model of accelerator operation)
OpenAI Gym – Cart Pole Environment 
 Let’s have a look at the Cart Pole environment in cartpole.ipynb 
 Main component: step function 
 Updates state 
 Calculates reward 
 Also has rendering functionality
Implementation of a DQN agent 
 There are several ready implementations of RL agents 
 E.g. Keras RL 
 We first define the Q network architecture (in Keras fashion):
Implementation of a DQN agent 
 We can use a ready-made policy (BoltzmannQPolicy) 
 Builds a probability law on q-values and returns an action selected randomly according to this law. 
 We also define the number of actions, the learning rate and the number of steps that we want to train the agent for, trying to optimize some metric. 
 Memory: stores the agent’s experiences 
 Number of warmup steps: avoids early overfitting 
 Target Model update: how often are weights of target network updated
Rendering the training of the agent 
 Google Colaboratory does not support OpenGL through the browser 
 I had to: 
 modify rendering.ipynb to avoid using pyglet.gl 
 modify cartpole.ipynb to render via matplotlib 
 If you were to download the notebook on your laptop, you can do without the above two notebooks and directly pass the OpenAI gym environment name as a string.
Let’s try to train DQNAgent for Cart Pole!
Summary 
 Reinforcement Learning: an agent learns to perform a task from its interactions with its environment 
 Formulation as a Markov Decision Process 
 Definitions of state, reward, policy, action 
 Concepts of value function and Q-value function 
 Q-learning and DQN