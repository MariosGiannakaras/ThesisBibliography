> Source: https://arxiv.org/pdf/2306.11217

Autonomous Driving with Deep Reinforcement Learning in CARLA Simulation 
Jumman Hossain Department of Information Systems 
University of Maryland, Baltimore County (UMBC) jumman.hossain@umbc.edu 
Abstract—Nowadays, autonomous vehicles are gaining traction due to their numerous potential applications in resolving a variety of other real-world challenges. However, developing autonomous vehicles need huge amount of training and testing before deploying it to real world. While the field of reinforcement learning (RL) has evolved into a powerful learning framework to the development of deep representation learning, and it is now capable of learning complicated policies in high-dimensional environments like in autonomous vehicles. In this regard, we make an effort, using Deep Q-Learning, to discover a method by which an autonomous car may maintain its lane at top speed while avoiding other vehicles. After that, we used CARLA simulation environment to test and verify our newly acquired policy based on the problem formulation. 
I. INTRODUCTION 
The development of learning-based methodologies, the proliferation of low-cost sensors, and the availability of enormous amounts of driving data have all contributed to the substantial progress that has been made in the field of autonomous driving over the course of the past few decades. In recent years, there has been an increase in the popularity of end-to-end approaches, which are methods that attempt to learn driving judgments directly from sensory inputs. This rise can be attributed to the rise of deep learning. Instead of first learning an exact representation of the data and then making judgments based on that information, the system will learn an intermediate representation in this fashion, which has the potential to produce superior results. 
The navigation problem for AVs entails finding the best course of action to get the vehicle from one location to another without crashing into any of the moving obstacles or other vehicles along the way. Because AVs are supposed to maintain a safe distance from other vehicles while simultaneously making driving more fuel- and time-efficient, safety is a crucial part of navigation. Autonomous driving relies heavily on navigation, a topic that has been intensively researched in the fields of motion planning and mobile robotics. 
In an autonomous navigation tasks, the goal of utilizing a RL algorithm is to identify the best strategy for directing the robot to its destination point through interaction with the environment. Many well-known RL algorithms have been adapted to create a RL-based navigation system, including DQN, DDPG, PPO, and their variants. These methods model the navigation process as an MDP using sensor observation as the state and the goal of maximizing the action’s predicted 
revenue. RL-based navigation has the advantages of being mapless, having a good learning ability, and having a low reliance on sensor accuracy. Because RL is a trial-and-error learning system, the physical training process will ultimately result in the robot colliding with external impediments. 
Since autonomous driving is a situation in which an agent makes decisions based on what it senses, the problem can be turned into a Markov Decision Process (MDP), making it an ideal candidate for the application of Reinforcement Learning. While Deep Q Networks (DQNs) demonstrated superhuman performance in Atari games [1], [2], and AlphaGo achieved widespread success [3], the use of Deep Reinforcement Learning for control-oriented tasks has experienced explosive growth. 
The authors [4] make use of RL in order to get experience in racing in a virtual setting. There have also been several research published that demonstrate the application of inverse reinforcement learning (IRL) [5], [6]to the task of autonomous driving. [7] Describe a system that can learn costmaps for autonomous driving utilizing IRL data directly from sensors. [8] Demonstrate a strategy that would be used in real life in a straightforward case of highway driving on a specialized simulator. 
In a manner analogous to that described above, we learn from unprocessed sensory data in a simulated setting. We make an effort to discover, through Deep Q-Learning, a method that would enable an autonomous car to maintain its lane at the highest potential speed while simultaneously avoiding collisions with other vehicles. 
II. RELATED WORK 
B-GAP [9] : Presented a navigation scheme that is based on deep reinforcement learning and considers driver behavior to perform behaviorally-guided navigation. Their DRL based policy implicitly models the interactions between traffic agents and computes safe trajectories for the ego-vehicle accounting for aggressive driver maneuvers such as overtaking, overspeeding, weaving, and sudden lane changes. 
Overtaking Maneuvers [10] : Presented a Deep Deter-ministic Policy Gradients (DDPG) based approach to learn overtaking maneuvers for a car, in presence of multiple other cars, in a simulated highway scenario. Their training strategy resembles a curriculum learning approach that ables to learn smooth maneuvers, largely collision free, wherein the agent 
 
 
 
 
 
 
 
 
 
 
overtakes all other cars, independent of the track and number of cars in the scene. 
[11] approaches for predicting the behaviors of human drivers based on the trajectories of their vehicles. They are using graph-theoretic tools to extract features from the trajectories and machine learning to learn a computational mapping between the trajectories and the driver behaviors. Their approach is similar to how humans implicitly interpret the behaviors of drivers on the road, by only observing the trajectories of their vehicles. By using machine learning to model this process, it may be possible to enable autonomous vehicles to better understand and predict the behaviors of human drivers, which can be useful for a variety of applications, including autonomous navigation. 
In contrast, our objective is to implement Deep Q-Networks, which are capable of resolving the issue of driving autonomous vehicles in a highway environment as quickly as possible while simultaneously avoiding crashes. 
III. PRELIMINARIES 
A. Reinforcement Learning 
There are two primary components that fall under the umbrella of generalized reinforcement learning: an agent and an environment. At a certain moment in time t, the agent lies in a state st of the environment; it then takes an action, moving from the state st to a new state st+1, and receives a reward rt from the environment. The goal of the agent is to learn a policy π that maximizes the cumulative reward over time. The standard agent-environment interaction in reinforcement learning [12] is depicted in Figure 1. 
Fig. 1: Agent-Environment Interaction in Reinforcement learning 
Typically, we can model an RL problem with decisions by formulating it as a Markov Decision Process (MDP). An MDP is often described as a tuple consisting of: 
 A state space S: which is the set of spaces in which an agent can find himself along the process. 
 An action state A: which is the set of actions available for the agent. 
 A transition probability function that represents the probability to move from one state to another by choosing a certain action. 
 A reward function Rt(st, At) which is the reward obtained by choosing a certain action in a certain state. 
In reinforcement learning, an agent interacts with an environment in a sequence of steps, with the goal of maximizing a reward signal. At each time step, the agent receives an observation of the environment and takes action based on this observation. The action leads to a new observation and a reward, and the process repeats. 
The goal of the agent is to learn a policy that maps observations to actions in a way that maximizes the expected sum of rewards over time. This can be formalized using the following components: 
State: A state is a representation of the environment at a given time step. It can include information about the agent’s current location, the objects and obstacles in the environment, and any other relevant information. 
Action: An action is a choice made by the agent at each time step. It can be a discrete decision, such as moving left or right, or a continuous decision, such as adjusting the speed of a robot. 
Reward: A reward is a scalar value that is provided to the agent after each action. It reflects the quality of the action taken by the agent and is used to guide the learning process. 
Policy: A policy is a function that maps states to actions. It determines the action that the agent should take at each time step based on the current state. The goal of the agent is to learn a policy that maximizes the expected sum of rewards. 
The process of reinforcement learning can be summarized by the following equation: 
π∗(s) = argmax π 
E[ ∞∑ t=0 
γtrt|s0 = s, π] 
Here, π(s) is the optimal policy for a given state s, π is a policy being evaluated, E[·] is the expected value operator, γ is a discount factor that determines the importance of future rewards, and rt is the reward received at time step t. The sum is over all time steps starting at t = 0 and going to infinity. The goal is to find the policy π(s) that maximizes the expected sum of rewards. 
B. Q-learning 
The mind of the agent in Q-learning is a table with the rows as the State or Observation of the agent from the environment and the columns as the actions to take. Each of the cells of the table will be filled with a value called Q-value which is the value that an action brings considering the state it is in. let’s call this table Q-table. The Q-table is actually the brain of the agent. 
The agent starts taking an action in the environment and starts a Q-table initialized with zeros in all the cells. Then, the agent gets to a new state or observation (state is the information of the environment that an agent is in and observation is an actual image that the agent sees. Depending on the environment an agent gets state or observation as an input) by doing an action from the table. The state is a row in the table containing Q-values for each action and the highest value
Fig. 2: Q-table. 
in the row will be the action that the agent takes (the column with the highest value in that specific row). 
In Q-learning, the expected future reward for a given action at a given time step is referred to as the action-value function or Q-value. The Q-value for an action at a time step is calculated using the following formula: 
Q(st, at) = E[Rt+1 + γmax a 
Q(st+1, a)|st, at] 
Here, Q(st, at) is the Q-value for taking action at at state st, E[·] is the expected value operator, Rt+1 is the reward received at the next time step, γ is the discount factor that determines the importance of future rewards, and st+1 is the state at the next time step. The term maxa Q(st+1, a) is the maximum Q-value over all actions at the next time step. 
The Q-learning algorithm involves iteratively updating the Q-values using the above formula and a learning rate parameter α. The Q-values are initially set to a random value and are updated using the following update rule: 
Q(st, at)← (1− α)Q(st, at) + α(Rt+1 + γmax a 
Q(st+1, a)) 
This update rule involves a combination of the current Q-value and the new estimate of the Q-value, with the learning rate α determining the relative importance of these two terms. The Q-learning algorithm is run for a fixed number of iterations or until the Q-values converge to a stable value. 
Once the Q-learning algorithm has completed, the optimal policy can be obtained by choosing the action with the highest Q-value at each state. The Q-table is a data structure that stores the Q-values for all states and actions, and can be used to look up the optimal action for a given state. 
The agent gets a reward by doing the action. The reward has a meaning. the higher the value the better, but sometimes the lower value could mean that the agent has taken the better action. The reward comes from the environment and the environment defines which of the lower or higher reward is better. The environment gives the agent the reward for taking an action in a specific state. 
The agent keeps doing steps 1 to 3 and gathers information in its “memory”. The memory contains tuples of state, next state, action, reward, and a Boolean value for indicating the termination of the agent. These steps keep on going and the agent memorizes the info until the termination happens. 
After the termination of the agent which could mean completing the task or failing, the agent starts replaying the experiences it gathered in its memory. A batch of a particular 
size will be chosen from the memory and the task of training will be performed on it. Basically, this means that the Q-table starts filling up. This is called Experience Replay 
Basically, Q-value is the reward obtained from the current state plus the maximum Q-value from the next state. So, that means the agent has to get the reward and the next state from its experience in the memory and add the reward to the highest Q-value derived from the row of the next state in the Q-table and the result will go into the row of the current state and the column of the action, both obtained from the experience in the memory. 
C. Deep Q-Learning 
The only difference between Q-learning and DQN is the agent’s brain. The agent’s brain in Q-learning is the Q-table, but in DQN the agent’s brain is a deep neural network. 
DQN uses a neural network (Fig. 3) to represent the value function, which is trained using a variant of the Q-learning algorithm. The input to the neural network is the state or observation, and the output is the Q-value for each possible action. The neural network is trained using a loss function that measures the difference between the predicted Q-values and the target Q-values, which are updated using the Bellman equation. 
Overall, the main difference between Q-learning and DQN is the way that the value function is represented and updated. Q-learning uses a tabular representation, while DQN uses a neural network representation. Both algorithms can be effective for learning policies in different types of environments, but DQN may be better suited for problems with large or continuous action and observation spaces. Taking all of this into account, DQN might be an appropriate option for an autonomous driving situation which includes: 
Real-time performance: DQN can learn policies in realtime, which is important for applications like autonomous driving where decisions need to be made quickly and accurately. 
Generalization: DQN can learn policies that generalize well to different scenarios and environments, which is important for autonomous driving, where the vehicle may need to operate in a range of different conditions. 
Scalability: DQN can scale to large action and observation spaces, which is often the case in autonomous driving, where the vehicle may need to consider a wide range of possible actions and observations. 
Robustness: DQN can learn robust policies that are resistant to noise and uncertainty, which is important for autonomous driving, where the environment may be highly dynamic and unpredictable. 
IV. PROBLEM FORMULATION 
We formulate the problem with observation space, action space, and reward structure throughout the environment interactions by agents. 
Observation Space: The Observation space for each agent is a 5 by 5 array that has a list of five vehicles that are located in close proximity to one another and is described by a set of
Fig. 3: Q-learning vs Deep Q-learning. 
characteristics including Position (x, y) and Velocity (Vx, Vy). In order to accomplish the goals of multi-agent learning, we create a tuple by concatenating the observation of the number of agents that are now active. 
Action Space: Our Action Space is a Discrete space that consists of Lateral movement and Longitudinal movement. 
0 : LANELEFT , 1 : IDLE, 2 : LANERIGHT , 3 : FASTER, 4 : SLOWER Reward Formulation: On the highway, which is quite 
straight and has numerous lanes, the driver of the vehicle receives a reward for maintaining a high speed, staying in the lanes to the right of the center, and avoiding collisions. 
RIGHTLANEREWARD = 0.1 HIGHSPEEDREWARD = 0.4 LANECHANGEREWARD = 0 Within our learning policy, we take the mean of the reward 
values that were acquired by each agent. The episode is over when it reaches a maximum of 50 seconds in length or when the agents come into physical contact with one another. 
V. METHODOLOGY 
In a multi-agent problem with partially observed data, it can be challenging to design effective reinforcement learning algorithms that can make long-term strategies over thousands of steps in a large action space. One approach that may be useful in this scenario is to use multi-agent reinforcement learning algorithms. 
Multi-agent reinforcement learning algorithms are designed specifically to address problems involving multiple agents interacting with each other and the environment. These algorithms typically involve the use of various techniques to handle the complexity of multi-agent systems, such as decentralized control, cooperative and competitive behavior, and communication between agents. 
There are several different approaches to multi-agent reinforcement learning, including centralised training with decentralised execution, independent learning, and cooperative learning. Each of these approaches has its own benefits and 
limitations, and the choice of which approach to use will depend on the specific characteristics of the problem being addressed. 
It is also important to note that in order to effectively solve a multi-agent problem with partially observed data, it may be necessary to incorporate additional techniques such as partially observable Markov decision processes (POMDPs) or belief state representations. These techniques can help the agents to reason about the uncertainty in their observations and make more informed decisions. 
In the Q-learning algorithm, the action-value function Q(s, a) is used to estimate the expected future reward of taking a particular action a in a particular state s, and to select the action that will maximize this expected reward. This expected reward is also known as the ”utility” of the action, and it takes into account the immediate reward of taking the action as well as the future rewards that may be obtained by following a particular policy. 
The action-value function Q(s, a) is typically represented as a table or a function approximator, such as a neural network. It is updated using the Bellman equation, which expresses the relationship between the expected utility of an action and the expected utility of the subsequent state that the action leads to. The Bellman equation is used to update the actionvalue function Q(s, a) in an iterative fashion, as the agent explores the environment and learns about the consequences of its actions. 
In the example you provided of a chess game, the actionvalue function Q(s, a) could be used to measure how beneficial it is to move a particular pawn forward in a particular game state. The action-value function would take into account the immediate reward of making the move (e.g., capturing an opponent’s piece) as well as the potential future rewards that may be obtained by following a particular strategy (e.g., setting up a winning position). 
For the sake of this project, the Q assesses how well one is able to decide whether to speed up, slow down, or switch lanes at any given time and in any given setting. As the agent examines the present state of the environment and chooses an action, the environment transitions into a new state while simultaneously returning a reward to signal the result of the action that was chosen. Because of Q-learning, the agent is equipped with a cheat sheet that details the Q-values present in each scenario along with the actions that should be taken in response to them. On the other hand, the Q-learning agent does not have the ability to make value estimates for states that have not yet been encountered. If the Q-learning agent has never been exposed to a state before, it will be completely clueless regarding the appropriate next steps to take. 
In order to acquire knowledge about Q values via a Multi-Layer Perceptron Model, we make use of a DQN technique. The actions are selected by the policy based on which ones have the highest possible Q value for the current condition. While the DQN algorithm works by using a neural network to predict the expected reward for taking a particular action in a given state. The neural network is trained using a variant of
Vehicle Position Velocity X Y Vx Vy 
Ego-Vehicle 0.04 0.05 0.72 0 Vehicle 1 -0.12 0 -0.16 0 Vehicle 2 0.09 0.03 -0.072 0 Vehicle 3 0.06 0.02 -0.65 0 Vehicle 4 0.28 0.18 0.20 0.025 
Value Action 0 LANE LEFT 1 IDLE 2 LANE RIGHT 3 FASTER 4 SLOWER 
Action Reward RIGHT LANE 0.1 HIGH SPEED 0.4 LANE CHANGE 0 
(a) Observation Space (b) Action Space (c) Reward Space 
TABLE I: Problem formulation with (a) observation space: Position and velocity of different vehicles, (b): Action space with 5 scenarios, and (c) reward values of three actions. 
Fig. 4: Multi-Layer Perceptron Model. 
stochastic gradient descent called Q-learning, which updates the network’s weights based on the difference between the predicted reward and the actual reward received after taking the action. We employ the DQN method to learn Q values through a Multi-Layer Perceptron Model. The actions are chosen by the policy with maximum Q value for a given state. RIGHT_LANE_REWARD, HIGH_SPEED_REWARD, and 
LANE_CHANGE_REWARD are variables that define the reward values for certain actions taken by the autonomous vehicle (AV) during training. RIGHT_LANE_REWARD is a positive value that rewards the 
AV for staying on the rightmost lanes. This reward encourages the AV to drive in a safe and efficient manner. HIGH_SPEED_REWARD is a positive value that rewards the 
AV for driving at a high speed. This reward encourages the AV to drive efficiently and reach its destination quickly. LANE_CHANGE_REWARD is a value that rewards or penal-
izes the AV for changing lanes. If LANE_CHANGE_REWARD is positive, it will encourage the AV to change lanes. If LANE_CHANGE_REWARD is negative, it will discourage the AV from changing lanes. If LANE_CHANGE_REWARD is set to zero, the AV will not be specifically rewarded or penalized for lane changes. 
These reward values are used in the reward formulation of the DQN algorithm 1 to train the AV to perform a particular task, such as driving on a highway. The AV will receive rewards or penalties based on the values of RIGHT_LANE_REWARD, HIGH_SPEED_REWARD, and LANE_CHANGE_REWARD after taking actions in different states, and will use this information to learn the best actions 
to take in different situations. In this formulation, the neural network Q is used to ap-
proximate the optimal action-value function, which determines the best action to take in a given state. The replay memory D is used to store transitions and sample minibatches for training the network. The ϵ-greedy policy is used to balance exploration (trying new actions) and exploitation (choosing the action with the highest predicted reward). The discount factor γ determines the importance of future rewards in the actionvalue function. And the loss function L is used to update the weights of the neural network to better approximate the optimal action-value function. 
Algorithm 1 DQN Algorithm for AV Driving 
1: Initialize the neural network with random weights: W . 2: Initialize the replay memory D to capacity N . 3: for each step t = 1, 2, 3, . . . do 4: Receive the current state s of the AV. 5: Select an action a using an ϵ-greedy policy based 
on the current estimate of the action-value function: Q(s, a;W ). 
6: Execute action a in the environment. 7: Observe the reward r and the next state s′. 8: Store the transition (s, a, r, s′) in the replay memory 
D. 9: Sample a minibatch of transitions (si, ai, ri, s 
′ i) from 
the replay memory D. 10: if episode terminates at step i+ 1 then 11: yi ← ri 12: else 13: yi ← ri + γmaxa′ Q(s′i, a 
′;W ) 14: end if 15: Update the weights of the neural network using gra-
dient descent to minimize the loss function: 16: Li(W )← (yi −Q(si, ai;W ))2 
17: end for 
VI. RESULTS 
Across all of CARLA [13]’s towns, under a variety of climatic circumstances, and in three distinct traffic patterns, we put our agent through a rigorous test, evaluating it based on four key parameters.
Metric/Town Town01 Town02 Town03 Town04 Town05 Town06 Town07 Town10 Total 
Collision rate S U 
0.78 0.98 
0.85 0.98 
0.72 0.99 
0.81 0.99 
0.38 0.95 
0.4 0.92 
0.77 0.89 
0.58 0.90 
68% 96% 
Speed S U 
8.60 5.98 
8.22 5.7 
8.43 5.99 
9.05 6.02 
9.26 6.25 
9.23 6.45 
7.54 5.68 
8.64 6.31 
8.71 km/h 6.10 km/h 
Timesteps S U 
315 190 
329 208 
365 235 
371 209 
420 250 
473 323 
272 214 
341 270 
373 241 
Total Reward S U 
2165 510 
2026 498 
1995 591 
1789 562 
2188 486 
2010 694 
1485 354 
1902 514 
1954 513 
TABLE II: Performance of our agents: standard (S), and untrained (U).The results have been aggregated over the two weather sets (soft and hard), and three traffic scenarios (no, regular, and dense). 
Fig. 5: CARLA Highway Environment (Town04). 
 Metrics: collision rate, speed, total reward, and timesteps (i.e. the number of steps without any infraction or collision). 
 Towns: Every town in CARLA has certain distinguishing characteristics all its own. Town04 (Fig. 5) served as the platform for our agent’s training, and subsequent towns—including Town01, Town02, Town03, Town04, Town05, Town06, Town07, and Town10—were used to assess its performance. 
 Weather: Our evaluation is based on two separate sets of weather presets: easy and difficult. The first set, which is just utilized for training , and the second set, which is completely new to the agent, are as follows: WetCloudyNoon, CloudySunset, WetCloudySunset, HardRainNoon. 
 Traffic: Our agent is evaluated using three distinct types of traffic: no traffic, regular traffic, and dense traffic. 
The advantages of DQN are also measured by contrasting the performance of the same agent with and without DQN; the former is denoted by the letter ”S” for Standard DQN, while the latter is denoted by the letter ”U” for the baseline performance of an agent with the same architecture and fixed random weights throughout the evaluation. Table 2 demonstrates our agents’ aggregate performance across both traffic scenarios and both weather sets. 
The formulation of the method has the ability to maximize the standard reward that is gained by all of the agents. It’s not uncommon for the reward signal to fluctuate or exhibit nonmonotonic behavior as the agent learns, and it can take some time for the reward to converge to a stable value or trend. It appears that after 3000 steps, the reward begins to converge 
with an upward trend. This suggests that the algorithm is learning a policy that is able to consistently achieve a high reward. 
Fig. 6: Policy learning with DQN. 
VII. LIMITATIONS 
There are several potential limitations of the proposed DQN approach. 
Sensors and perception: Depending on the sensors and perception capabilities of the agents, it has limited visibility or understanding of the environment, which could affect the ability to make informed decisions. 
Reward signal: The reward signal used in the simulation (i.e., the speed of the vehicles within the range of [20, 30]) may not capture all of the relevant factors that influence the agents’ performance, leading to suboptimal policies. 
Limited generalizability: The policies learned by the agents in this simulation may not generalize well to other environments or scenarios, meaning that they may not perform well when applied to different situations. 
VIII. CONCLUSION AND FUTURE WORK 
We have used reinforcement learning to learn a policy with a modified DQN algorithm to train autonomous vehicles to achieve maximum speed while avoiding collisions. We also designed our own observation, action, and reward structure. We have experimented with this problem formulation in CARLA simulation environment, and considering future work that involves applying other reinforcement learning algorithms, such as Deep Deterministic Policy Gradient (DDPG) [14], Soft Actor-Critic (SAC) [15], and possibly training the policy in
a decentralized manner using Proximal Policy Optimization (PPO) [16]. 
REFERENCES 
[1] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013. 
[2] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, An-dreas K Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. nature, 518(7540):529–533, 2015. 
[3] David Silver, Aja Huang, Christopher J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis. Mastering the game of go with deep neural networks and tree search. Nature, 529:484–503, 2016. 
[4] Larry D. Pyeatt and Adele E. Howe. Learning to race: Experiments with a simulated race car. In The Florida AI Research Society, 1998. 
[5] Yu Shen, Weizi Li, and Ming C Lin. Inverse reinforcement learning with hybrid-weight trust-region optimization and curriculum learning for autonomous maneuvering. Technical report, Technical report, Department of Computer Science, University of Maryland, 2022. 
[6] Tung Phan-Minh, Forbes Howington, Ting-Sheng Chu, Sang Uk Lee, Momchil S Tomov, Nanxiang Li, Caglayan Dicle, Samuel Findler, Francisco Suarez-Ruiz, Robert Beaudoin, et al. Driving in real life with inverse reinforcement learning. arXiv preprint arXiv:2206.03004, 2022. 
[7] Markus Wulfmeier, Dominic Zeng Wang, and Ingmar Posner. Watch this: Scalable cost-function learning for path planning in urban environments. In 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 2089–2095. IEEE, 2016. 
[8] Sahand Sharifzadeh, Ioannis Chiotellis, Rudolph Triebel, and Daniel Cremers. Learning to drive using inverse reinforcement learning and deep q-networks. arXiv preprint arXiv:1612.03653, 2016. 
[9] Angelos Mavrogiannis, Rohan Chandra, and Dinesh Manocha. B-gap: Behavior-guided action prediction and navigation for autonomous driving. arXiv preprint arXiv:2011.03748, 2020. 
[10] Meha Kaushik, Vignesh Prasad, K Madhava Krishna, and Balaraman Ravindran. Overtaking maneuvers in simulated highway driving using deep reinforcement learning. In 2018 IEEE Intelligent Vehicles Sympo-sium (IV), pages 1885–1890, 2018. 
[11] Rohan Chandra, Aniket Bera, and Dinesh Manocha. Using graphtheoretic machine learning to predict human driver behavior. IEEE Transactions on Intelligent Transportation Systems, 23(3):2572–2585, 2022. 
[12] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
[13] Alexey Dosovitskiy, German Ros, Felipe Codevilla, Antonio Lopez, and Vladlen Koltun. Carla: An open urban driving simulator. In Conference on robot learning, pages 1–16. PMLR, 2017. 
[14] Timothy P Lillicrap, Jonathan J Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971, 2015. 
[15] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning, pages 1861–1870. PMLR, 2018. 
[16] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.