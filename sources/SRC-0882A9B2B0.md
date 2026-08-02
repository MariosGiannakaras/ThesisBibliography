> Source: https://arxiv.org/pdf/1810.12282

Assessing Generalization in Deep Reinforcement Learning 
Charles Packer * 1 Katelyn Gao * 2 Jernej Kos 3 Philipp Krähenbühl 4 Vladlen Koltun 2 Dawn Song 1 
Abstract Deep reinforcement learning (RL) has achieved breakthrough results on many tasks, but agents often fail to generalize beyond the environment they were trained in. As a result, deep RL algorithms that promote generalization are receiving increasing attention. However, works in this area use a wide variety of tasks and experimental setups for evaluation. The literature lacks a controlled assessment of the merits of different generalization schemes. Our aim is to catalyze communitywide progress on generalization in deep RL. To this end, we present a benchmark and experimental protocol, and conduct a systematic empirical study. Our framework contains a diverse set of environments, our methodology covers both indistribution and out-of-distribution generalization, and our evaluation includes deep RL algorithms that specifically tackle generalization. Our key finding is that “vanilla” deep RL algorithms generalize better than specialized schemes that were proposed specifically to tackle generalization. 
1. Introduction Deep reinforcement learning (RL) has emerged as an important family of techniques that may support the development of intelligent systems that learn to accomplish goals in a variety of complex real-world environments (Mnih et al., 2015; Arulkumaran et al., 2017). A desirable characteristic of such intelligent systems is the ability to function in diverse environments, including ones that have never been encountered before. Yet deep RL algorithms are commonly trained and evaluated on a fixed environment. That is, the algorithms are evaluated in terms of their ability to optimize a policy in a complex environment, rather than their ability to learn a representation that generalizes to previously unseen circum-
*Equal contribution 1University of California Berkeley, Berke-ley, California, USA 2Intel Labs, Santa Clara, California, USA 3National University of Singapore, Singapore 4University of Texas Austin, Austin, Texas, USA. Correspondence to: Charles Packer <cpacker@berkeley.edu>, Katelyn Gao <kate-lyn.gao@intel.com>. 
stances. The dangers of overfitting to a specific environment have been noted in the literature (Whiteson et al., 2011) and the sensitivity of deep RL to even subtle changes in the environment has been noted in recent work (Rajeswaran et al., 2017b; Henderson et al., 2018; Zhang et al., 2018). 
Generalization is often regarded as an essential characteristic of advanced intelligent systems and a central issue in AI research (Lake et al., 2017; Marcus, 2018; Dietterich, 2017). It includes both interpolation to environments similar to those seen during training and extrapolation outside the training distribution. The latter is particularly challenging but is crucial to the deployment of systems in the real world as they must be able to handle unforseen situations. 
Generalization in deep RL has been recognized as an important problem and is under active investigation (Wang et al., 2016; Duan et al., 2016b; Rajeswaran et al., 2017a; Pinto et al., 2017; Finn et al., 2017; Kansky et al., 2017; Yu et al., 2017; Sung et al., 2017; Leike et al., 2017; Al-Shedivat et al., 2018; Clavera et al., 2018; Sæmundsson et al., 2018). How-ever, each work uses a different set of environments, variations, and experimental protocols. For example, Kansky et al. (2017) propose a graphical model architecture, evaluating on variations of the Atari game Breakout where the positions of the paddle, balls, and obstacles (if any) change. Rajeswaran et al. (2017a) propose training on a distribution of environments in a risk-averse manner and evaluate on two robot locomotion environments where variations in the robot body are considered. Duan et al. (2016b) aim to learn a policy that automatically adapts to the environment dynamics and evaluate on bandits, tabular Markov decision processes, and maze navigation environments where the goal position changes. Finn et al. (2017) train a policy that at test time can be quickly updated to the test environment and evaluate on navigation and locomotion. 
What appears to be missing is a systematic empirical study of generalization in deep RL with a clearly defined set of environments, metrics, and baselines. In fact, there is no common testbed for evaluating generalization in deep RL. Such testbeds have proven to be effective catalysts of concerted community-wide progress in other fields (Donoho, 2015). Only by conducting systematic evaluations on reliable testbeds can we fairly compare and contrast the merits of different algorithms and accurately assess progress. 
 
 
 
 
 
 
 
 
 
 
 
Assessing Generalization in Deep Reinforcement Learning 
Our contribution is an empirical evaluation of the generalization performance of deep RL algorithms. In doing so, we also establish a reproducible framework for investigating generalization in deep RL with the hope that it will catalyze progress on this problem. Like Kansky et al. (2017), Rajeswaran et al. (2017a), and others, we focus on generalization to environmental changes that affect the system dynamics instead of the goal or rewards. We select a diverse set of environments that have been widely used in previous work on generalization in deep RL, comprising classic control problems and MuJoCo locomotion tasks, built on top of OpenAI Gym for ease of adoption. The environmental changes that affect the system dynamics are implemented by selecting degrees of freedom (parameters) along which the environment specifications can be varied. Significantly, we test generalization in two regimes: interpolation and extrapolation. Interpolation implies that agents should perform well in test environments where parameters are similar to those seen during training. Extrapolation requires agents to perform well in test environments where parameters are different from those seen during training. 
To provide the community with a set of clear baselines, we first evaluate two popular state-of-the-art deep RL algorithms under different combinations of training and testing regimes. We choose one algorithm from each of the two major families: A2C from the actor-critic family and PPO from the policy gradient family. Under the same experimental protocol, we also evaluate two recently-proposed schemes for tackling generalization in deep RL: EPOpt, which learns a policy that is robust to environment changes by maximizing expected reward over the most difficult of a distribution of environment parameters, and RL2, which learns a policy that can adapt to the environment at hand by learning environmental characteristics from the trajectory it sees on-the-fly. Because each scheme is constructed based on existing deep RL algorithms, our evaluation is of four algorithms: EPOpt-A2C, EPOpt-PPO, RL2-A2C, and RL2-PPO. We analyze the results, devising simple metrics for generalization in terms of both interpolation and extrapolation and drawing conclusions that can guide future work on generalization in deep RL. The experiments confirm that extrapolation is more difficult than interpolation. 
However, surprisingly, the vanilla deep RL algorithms, A2C and PPO, generalized better than their EPOpt and RL2 variants; they were able to interpolate fairly successfully. That is, simply training on a set of environments with variations can yield agents that can generalize to environments with similar variations. EPOpt was able to improve generalization (both interpolation and extrapolation) but only when combined with PPO on environments with continuous action spaces and only one of the two policy/value function architectures we consider. RL2-A2C and RL2-PPO proved to be difficult to train and were unable to reach the level of 
performance of the other algorithms given the same amount of training resources. We discuss lines of inquiry that are opened by these observations. 
2. Related work 
Generalization in RL. There are two main approaches to generalization in RL: learning policies that are robust to environment variations and learning policies that adapt to such variations. A popular approach to learn a robust policy is to maximize a risk-sensitive objective, such as the conditional value at risk (Tamar et al., 2015), over a distribution of environments. From a control theory perspective, Mori-moto & Doya (2001) maximize the minimum reward over possible disturbances to the system model, proposing robust versions of the actor-critic and value gradient methods. This maximin objective is utilized by others in the context where environment changes are modeled by uncertainties in the transition probability distribution function of a Markov decision process. Nilim & Ghaoui (2004) assume that the set of possible transition probability distribution functions are known, while Lim et al. (2013) and Roy et al. (2017) estimate it using sampled trajectories from the distribution of environments of interest. A recent representative of this approach applied to deep RL is the EPOpt algorithm (Ra-jeswaran et al., 2017a), which maximizes the conditional value at risk, i.e. expected reward over the subset of environments with lowest expected reward. EPOpt has the advantage that it can be used in conjunction with any RL algorithm. Adversarial training has also been proposed to learn a robust policy; for MuJoCo locomotion tasks, Pinto et al. (2017) train an adversary that tries to destabilize the agent while it trains. 
A robust policy may sacrifice performance on many environment variants in order to not fail on a few. Thus, an alternative, recently popular approach to generalization in RL is to learn an agent that can adapt to the environment at hand (Yu et al., 2017). To do so, a number of algorithms learn an embedding for each environment variant using trajectories sampled from that environment, which is utilized by the agent. Then, at test time, the current trajectory can be used to compute an embedding for the current environment, enabling automatic adaptation of the agent. Duan et al. (2016b), Wang et al. (2016), Sung et al. (2017), and Mishra et al. (2018), which differ mainly in the way embeddings are computed, consider model-free RL by letting the embedding be input into a policy and/or value function. Clavera et al. (2018) consider model-based RL, in which the embedding is input into a dynamics model and actions are selected using model predictive control. Under a similar setup, Sæmundsson et al. (2018) utilize probabilistic dynamics models and inference. 
The above approaches do not require updating the learned
Assessing Generalization in Deep Reinforcement Learning 
policy or model at test time, but there has also been work on generalization in RL that utilize such updates, primarily under the umbrellas of transfer learning, multi-task learning, and meta-learning. Taylor & Stone (2009) survey transfer learning in RL where a fixed test environment is considered, with Rusu et al. (2016) being an example of recent work on that problem using deep networks. Ruder (2017) provides a survey of multi-task learning in general, which, different from our problem of interest, considers a fixed finite population of tasks. Finn et al. (2017) present a meta-learning formulation of generalization in RL, training a policy that can be updated with good data efficiency for each test environment; Al-Shedivat et al. (2018) extend it for continuous adaptation in non-stationary environments. 
Empirical methodology in deep RL. Shared open-source software infrastructure, which enables reproducible experiments, has been crucial to the success of deep RL. The deep RL research community uses simulation frameworks, including OpenAI Gym (Brockman et al., 2016) (which we build upon), the Arcade Learning Environment (Bellemare et al., 2013; Machado et al., 2017), DeepMind Lab (Beattie et al., 2016), and VizDoom (Kempka et al., 2016). The MuJoCo physics simulator (Todorov et al., 2012) has been influential in standardizing a number of continuous control tasks. Leike et al. (2017) introduce a set of two-dimensional grid environments for RL, each designed to test specific safety properties of a trained agent, including in response to shifts in the distribution of test environments. Recently OpenAI released benchmarks for generalization in RL based on playing new levels of video games, both allowing finetuning at test time (Nichol et al., 2018) and not (Cobbe et al., 2018). Both Cobbe et al. (2018) and Justesen et al. (2018) (who also consider video games) use principled procedural generation of training and test levels based on difficulty. In contrast to the above works, we focus on control tasks with no visual input. 
Our work also follows in the footsteps of a number of empirical studies of reinforcement learning algorithms, which have primarily focused on the case where the agent is trained and tested on a fixed environment. Henderson et al. (2018) investigate reproducibility in deep RL and conclude that care must be taken not to overfit during training. On four MuJoCo tasks, the results of state-of-the-art algorithms may be quite sensitive to hyperparameter settings, initializations, random seeds, and other implementation details. The problem of overfitting in RL was recognized earlier by White-son et al. (2011), who propose an evaluation methodology based on training and testing on multiple environments sampled from some distribution and experiment with three classic control environments and a form of tabular Q-learning. Duan et al. (2016a) present a benchmark suite of continuous control tasks and conduct a systematic evaluation of reinforcement learning algorithms on those tasks; they consider 
interpolation performance on a subset of their tasks. Leike et al. (2017) test generalization to unseen environment configurations at test time (referred to as ‘distributional shift’) by varying the position of obstacles in a gridworld environment. In contrast to these works, we consider a greater variety of tasks, extrapolation as well as interpolation, and algorithms for generalization in deep RL. 
3. Notation In RL, environments are formulated in terms of Markov Decision Processes (MDPs) (Sutton & Barto, 2017). An MDP M is defined by the tuple (S,A, p, r, γ, ρ0, T ) where S is the set of possible states, A is the set of actions, p : S×A×S → R≥0 is the transition probability distribution function, r : S×A → R is the reward function, γ is the discount factor, ρ0 : S → R≥0 is the initial state distribution at the beginning of each episode, and T is the time horizon per episode. 
Let st and at be the state and action taken at time t. At the beginning of each episode, s0 ∼ ρ0(·). Under a policy π stochastically mapping a sequence of states to actions, at ∼ π(at | st, · · · , s0) and st+1 ∼ p(st+1 | at), giving a trajectory {st,at, r(st,at)}, t = 0, 1, · · ·. RL algorithms, taking the MDP as fixed, learn π to maximize the expected reward (per episode) JM (π) = Eπ 
[∑T t=0 γ 
trt 
] , where 
rt = r(st,at). They often utilize the concepts of a value function vπM (s), the expected reward conditional on s0 = s and a state-action value function QπM (s,a), the expected reward conditional on s0 = s and a0 = a. 
Algorithms that are designed to build RL agents that generalize often assume that there is a distribution of environments q(M). Then, they aim to learn a policy that maximizes the expected reward over the distribution, EπM∼q [JM (π)]. 
4. Algorithms We first evaluate two popular state-of-the-art vanilla deep RL algorithms from different families, A2C (Mnih et al., 2016) from the actor-critic family of algorithms and PPO (Schul-man et al., 2017) from the policy gradient family. 1 These algorithms are oblivious to changes in the environment. Second, we consider two recently-proposed algorithms designed to train agents that generalize to environment variations. We select one each from the two main types of approaches discussed in Section 2: EPOpt (Rajeswaran et al., 2017a) from the robust category of approaches and RL2 (Duan et al., 2016b) from the adaptive category. Both methods are built on top of vanilla deep RL algorithms, so for completeness we evaluate a Cartesian product of the 
1Preliminary experiments on other deep RL algorithms including A3C, TRPO, and ACKTR gave qualitatively similar results.
Assessing Generalization in Deep Reinforcement Learning 
algorithms for generalization and the vanilla algorithms: EPOpt-A2C, EPOpt-PPO, RL2-A2C, and RL2-PPO. Next we briefly summarize A2C, PPO, EPOpt, and RL2, using the notation in Section 3. 
Advantage Actor-Critic (A2C). A2C involves the interplay of two optimizations; a critic learns a parametric value function, while an actor utilizes that value function to learn a parametric policy that maximizes expected reward. At each iteration, trajectories are generated using the current policy, with the environment and hidden states of the value function and policy reset at the end of each episode. Then, the policy and value function parameters are updated using RMSProp (Hinton et al., 2012), with an entropy term added to the policy objective function in order to encourage exploration. We use an implementation from OpenAI Baselines (Dhariwal et al., 2017). 
Proximal Policy Optimization (PPO). PPO aims to learn a sequence of monotonically improving parametric policies by maximizing a surrogate for the expected reward via gradient ascent, cautiously bounding the improvement at each iteration. At iteration i, trajectories are generated using the current policy πθi , with the environment and hidden states of the policy reset at the end of each episode. The following objective is then maximized with respect to θ using Adam (Kingma & Ba, 2015): 
Es∼ρθi ,a∼πθi min [ `θ(a, s)Aπθi (s,a),mθ(a, s)Aπθi (s,a) 
] where ρθi are the expected visitation frequencies under πθi , `θ(a, s) = πθ(a | s)/πθi(a | s), mθ equals `θ(a, s) clipped to the interval [1 − δ, 1 + δ] with δ ∈ (0, 1), and Aπθi (s,a) = Q 
πθi M (s,a)− vπθiM (s). We use an implementa-
tion from OpenAI Baselines, PPO2. 
Ensemble Policy Optimization (EPOpt). In order to obtain a policy that is robust to possibly out-of-distribution environments, EPOpt maximizes the expected reward over the ε ∈ (0, 1] fraction of environments with worst expected reward: 
EπM∼q [JM (π) ≤ y] where PM∼q(JM (π) ≤ y) = ε. 
At each iteration, the algorithm generates L complete episodes according to the current policy, where at the end of each episode, a new environment is sampled from q and reset and the hidden states of the policy and value function are reset. It keeps the ε fraction of episodes with lowest reward and uses them to update the policy via a vanilla RL algorithm (TRPO (Schulman et al., 2015) in the paper). We use A2C and PPO, implementing EPOpt on top of them. 
RL2. In order to maximize the expected reward over a distribution of environments, RL2 tries to train an agent that can adapt to the dynamics of the environment at hand. RL2 
models the policy and value functions as a recurrent neural network (RNN) with the current trajectory as input, not just the sequence of states. The hidden states of the RNN may be viewed as an environment embedding. Specifically, for the RNN the inputs at time t are st, at−1, rt−1, and dt−1, where dt−1 is a Boolean variable indicating whether the episode ended after taking action at−1; the output is at and the hidden states are updated. Like the other algorithms, at each iteration trajectories are generated using the current policy with the environment state reset at the end of each episode. However, unlike the other algorithms, a new environment is sampled from q only at the end of every N episodes, which we call a trial. The generated trajectories are then input into a model-free RL algorithm, maximizing expected reward in a trial; the paper uses TRPO, while we use A2C and PPO. As with EPOpt, our implementation of RL2 is built on top of those of A2C and PPO. 
5. Environments Our environments are modified versions of four environments from the classic control problems in OpenAI Gym (Brockman et al., 2016) (CartPole, MountainCar, Ac-robot, and Pendulum) and two environments from OpenAI Roboschool (Schulman et al., 2017) (HalfCheetah and Hop-per) that are based on the corresponding MuJoCo (Todorov et al., 2012) environments. We alter the implementations to allow control of several environment parameters that affect the system dynamics, i.e. transition probability distribution functions of the corresponding MDPs. Similar environments have been used in experiments in the generalization for RL literature, see for instance (Rajeswaran et al., 2017a), (Pinto et al., 2017), and (Yu et al., 2017). Each of the six environments has three versions, with d parameters allowed to vary. Figure 1 is a schematic of the parameter ranges in D, R, and E when d = 2. 
1. Deterministic (D): The parameters of the environment are fixed at the default values in the implementations from Gym and Roboschool. That is, every time the environment is reset, only the state is reset. 
2. Random (R): Every time the environment is reset, the parameters are uniformly sampled from a d-dimensional box containing the default values. This is done by independently sampling each parameter uniformly from an interval containing the default value. 
3. Extreme (E): Every time the environment is reset, its parameters are uniformly sampled from 2d d-dimensional boxes anchored at the vertices of the box in R. This is done by independently sampling each parameter uniformly from the union of two intervals that straddle the corresponding interval in R.
Assessing Generalization in Deep Reinforcement Learning 
The structure of the three versions was designed to mirror the process of training an RL agent on a real-world task. D symbolizes the fixed environment used in the classic RL setting, and R represents the distribution of environments from which it is feasible and sensible to obtain training data. With more extreme parameters, E corresponds to edge cases, those unusual environments that are not seen during training but must be handled in deployment. 
Figure 1. Schematic of the three versions of an environment. 
CartPole (Barto et al., 1983). A pole is attached to a cart that moves on a frictionless track. For at most 200 time steps, the agent pushes the cart either left or right in order to keep the pole upright. There is a reward of 1 for each time step the pole is upright, with the episode ending when the angle of the pole from vertical is too large. Three environment parameters can be varied: (1) push force magnitude, (2) pole length, and (3) pole mass. 
MountainCar (Moore, 1990). The goal is to move a car to the top of a hill within 200 time steps. At each time step, the agent pushes a car left or right, with a reward of −1. Two environment parameters can be varied: (1) push force magnitude and (2) car mass. 
Acrobot (Sutton, 1995). The acrobot is a two-link pendulum attached to a bar with an actuator at the joint between the two links. For at most 500 time steps, the agent applies torque (to the left, to the right, or not at all) to the joint in order to swing the end of the second link above the bar to a height equal to the length of the link. The reward structure is the same as that of MountainCar. Three parameters of the links can be varied: (1) length, (2) mass, and (3) moment of inertia, which are the same for each link. 
Pendulum. The goal is to, for 200 time steps, apply a continuous-valued force to a pendulum in order to keep it at a vertical position. The reward at each time step is a decreasing function of the pendulum’s angle from vertical, the speed of the pendulum, and the magnitude of the applied force. Two environment parameters can be varied, the 
pendulum’s (1) length and (2) mass. 
HalfCheetah. The half-cheetah is a bipedal robot with eight links and six actuated joints corresponding to the thighs, shins, and feet. The goal is for the robot to learn to walk on a track without falling over by applying continuousvalued forces to its joints. The reward at each time step is a combination of the progress made and the costs of the movements, e.g., electricity and penalties for collisions, with a maximum of 1000 time steps. Three environment parameters can be varied: (1) power, a factor by which the forces are multiplied before application, (2) torso density, and (3) sliding friction of the joints. 
Hopper. The hopper is a monopod robot with four links arranged in a chain corresponding to a torso, thigh, shin, and foot and three actuated joints. The goal, reward structure, and varied parameters are the same as those of HalfCheetah. 
In all environments, the difficulty may depend on the values of the parameters; for example, in CartPole, a very light and long pole would be more difficult to balance. By sampling parameters from boxes surrounding the default values, R and E include environments of various difficulties. The actual ranges of the parameters for each environment, shown in Table 1, were chosen by hand so that a policy trained on D struggles in environments in R and fails in E. 
5.1. Performance metrics 
The traditional performance metric used in the RL literature is the average total reward achieved by the policy in an episode. In the spirit of the definition of an RL agent as goal-seeking (Sutton & Barto, 2017), we compute the percentage of episodes in which a certain goal is successfully completed, the success rate. We define the goals of each environment as follows: (1) CartPole: balance for at least 195 time steps, (2) MountainCar: get to the hilltop within 110 time steps, (3) Acrobot: swing the end of the second link to the desired height within 80 time steps, (4) Pendulum: keep the angle of the pendulum at most π/3 radians from vertical for the last 100 time steps of a trajectory with length 200, and (5) HalfCheetah and Hopper: walk for 20 meters. The goals for CartPole, MountainCar, and Acrobot are based on the definition of success for those environments given by OpenAI Gym. 
The binary success rate is clear and interpretable and has multiple advantages. First, it is independent of reward shaping, the common practice of modifying an environment’s reward functions to help an agent to learn desired behaviors. Moreover, separate implementations of the same environment, e.g. HalfCheetah in Roboschool and rllab (Duan et al., 2016a), may have different reward functions which are hidden in the code and not easily understood. Second, it allows fair comparisons across various environment param-
Assessing Generalization in Deep Reinforcement Learning 
Table 1. Ranges of parameters for each version of each environment, using set notation. 
Environment Parameter D R E 
CartPole Force 10 [5,15] [1,5]∪[15,20] Length 0.5 [0.25,0.75] [0.05,0.25]∪[0.75,1.0] Mass 0.1 [0.05,0.5] [0.01,0.05]∪[0.5,1.0] 
MountainCar Force 0.001 [0.0005,0.005] [0.0001,0.0005]∪[0.005,0.01] Mass 0.0025 [0.001,0.005] [0.0005,0.001]∪[0.005,0.01] 
Acrobot Length 1 [0.75,1.25] [0.5,0.75]∪[1.25,1.5] Mass 1 [0.75,1.25] [0.5,0.75]∪[1.25,1.5] MOI 1 [0.75,1.25] [0.5,0.75]∪[1.25,1.5] 
Pendulum Length 1 [0.75,1.25] [0.5,0.75]∪[1.25,1.5] Mass 1 [0.75,1.25] [0.5,0.75]∪[1.25,1.5] 
HalfCheetah Power 0.90 [0.70,1.10] [0.50,0.70]∪[1.10,1.30] Density 1000 [750,1250] [500,750]∪[1250,1500] Friction 0.8 [0.5,1.1] [0.2,0.5]∪[1.1,1.4] 
Hopper Power 0.75 [0.60,0.90] [0.40,0.60]∪[0.90,1.10] Density 1000 [750,1250] [500,750]∪[1250,1500] Friction 0.8 [0.5,1.1] [0.2,0.5]∪[1.1,1.4] 
eters. For example, a slightly heavier torso in HalfCheetah and Hopper would change the energy consumption of the robot and thus the reward function in Roboschool but would not change the definition of success in terms of walking a certain distance. 
6. Experimental methodology We benchmark six algorithms (A2C, PPO, EPOpt-A2C, EPOpt-PPO, RL2-A2C, RL2-PPO) and six environments (CartPole, MountainCar, Acrobot, Pendulum, HalfCheetah, Hopper). With each pair of algorithm and environment, we consider nine training-testing scenarios: training on D, R, and E and testing on D, R, and E. We refer to each scenario using the two-letter abbreviation of the training and testing environment versions, e.g., DR for training on D and testing on R. For A2C, PPO, EPOpt-A2C, and EPOpt-PPO, we train for 15000 episodes and test on 1000 episodes. For RL2-A2C and RL2-PPO, we train for 7500 trials of 2 episodes each, equivalent to 15000 episodes, and test on the last episodes of 1000 trials; this allows us to evaluate the ability of the policies to adapt to the environment in the current trial. Note that this is a fair protocol as policies without memory of previous episodes are expected to have the same performance in any episode of a trial. We do a thorough sweep of hyperparameters, and for the sake of fairness, we randomly generate random seeds and report results over several runs of the entire sweep. In the following paragraphs we describe the network architectures for the policy and value functions, our hyperparameter search, and the performance metrics we use for evaluation. 
Evaluation metrics. For each algorithm, architecture, and environment, we compute three numbers that distill the nine success rates into simple metrics for generalization performance: (1) Default: success percentage on DD, (2) Interpolation: success percentage on RR, and (3) Extrapo-lation: geometric mean of the success percentages on DR, DE, and RE. 
Default is the classic RL setting and thus provides a baseline for comparison. Because R represents the set of environments seen during training in a real-world RL problem, the success rate on RR, or Interpolation, measures the generalization performance to environments similar to those seen during training. In DR, DE, and RE the training distribution of environments does not overlap with the test distribution. Therefore, their success rates are combined to obtain Ex-trapolation, which measures the generalization performance to environments different from those seen during training. 
Policy and value function parameterization. To have equitable evaluations, we consider two network architectures for the policy and value functions for all algorithms and environments. In the first, following others in the literature including Henderson et al. (2018), the policy and value functions are multi-layer perceptrons (MLPs) with two hidden layers of 64 units each and hyperbolic tangent activations; there is no parameter sharing. We refer to this architecture as FF (feed-forward). In the second,2 the policy and value functions are the outputs of two separate fully-connected layers on top of a one-hidden-layer RNN with long short-
2Based on personal communication with authors of Duan et al. (2016b).
Assessing Generalization in Deep Reinforcement Learning 
term memory (LSTM) cells of 256 units. The RNN itself is on top of a MLP with two hidden layers of 256 units each, which we call the feature network. Again, hyperbolic tangent activations are used throughout; we refer to this architecture as RC (recurrent). For A2C, PPO, EPOpt-A2C, and EPOpt-PPO, we evaluate both architectures (where the inputs are the environment states), while for RL2-A2C and RL2-PPO, we evaluate only the second architecture (where the input is a tuple of states, actions, rewards, and Booleans as discussed in Section 4). In all cases, for discrete action spaces policies sample actions by taking a softmax function over the policy network output layer; for continuous action spaces actions are sampled from a Gaussian distribution with mean the policy network output and diagonal covariance matrix whose entries are learned along with the policy and value function network parameters. 
Hyperparameters. During training, for each algorithm and each version of each environment, we performed grid search over a set of hyperparameters used in the optimizers, and selected the value with the highest success probability when tested on the same version of the environment. That set of hyperparameters includes the learning rate for all algorithms and the length of the trajectory generated at each iteration for A2C, PPO, RL2-A2C, and RL2-PPO. They also include the coefficient of the policy entropy in the objective for A2C, EPOpt-A2C, and RL2-A2C and the coefficient of the KL divergence between the previous policy and current policy for RL2-PPO. The grid values are listed in the supplement. Other hyperparameters, such as the discount factor, were fixed at the default values in OpenAI Baselines, or in the case of EPOpt-A2C and EPOpt-PPO, L = 100 and ε = 1.0 for 100 iterations and then ε = 0.1. 
7. Results and discussion We highlight some of the key findings and present a summary of the experimental results in Table 2. The supplement contains analogous tables for each environment, which also informs the following discussion. 
A2C and PPO. We first consider the results under the FF architecture. The two vanilla deep RL algorithms are usually successful in the classic RL setting of training and testing on a fixed environment, as evidenced by the high values for Default in Table 2. However, when those agents trained on the fixed environment D are tested, we observed that they usually suffer from a significant drop in performance in R and an even further drop in E. Fortunately, based on the performance in RR, we see that simply training on a distribution of environments, without adding any special mechanism for generalization, results in agents that can perform fairly well in similar environments. 3 For example, PPO, for which 
3We have also found that sometimes the performance in RD is 
Default equals 78.22, has Interpolation equal to 70.57. Nev-ertheless, as expected in general they are less successful at extrapolation; PPO has Extrapolation equal to 48.37. With the RC architecture, A2C has similar behavior as with the FF architecture while PPO had difficulty training on the fixed environment D and did not generalize well. For example, on all the environments except CartPole and Pendulum the FF architecture was necessary for PPO to be successful even in the classic RL setting. 
The pattern of declining performance from Default to In-terpolation to Extrapolation also appears when looking at each environment individually. The magnitude of decrease depends on the combination of algorithm, architecture, and environment. For instance, on CartPole, A2C interpolates and extrapolates successfully, where Interpolation equals 100.00 and Extrapolation equals 93.63 with the FF architecture and 83.00 with the RC architecture; this behavior is also shown for PPO with the FF architecture. On the other hand, on Hopper, PPO with the FF architecture has 85.54% success rate in the classic RL setting but struggles to interpolate (Interpolation equals 39.68) and fails to extrapolate (Extrapolation equals 10.36). This indicates that our choices of environments and their parameter ranges lead to a variety of difficulty in generalization. 
EPOpt. Again, we start with the results under the FF architecture. Overall EPOpt-PPO improved both interpolation and extrapolation performance over PPO, as shown in Ta-ble 2. Looking at specific environments, on Hopper EPOpt-PPO has nearly twice the interpolation performance and significantly improved extrapolation performance compared to PPO. Such an improvement also appears for Pendulum and HalfCheetah. However, the generalization performance of EPOpt-PPO was worse than that of PPO on the other three environments. EPOpt did not demonstrate the same performance gains when combined with A2C; in fact, it generally failed to train even in the fixed environment D. With the RC architecture, EPOpt-PPO, like PPO, also had difficulties training on environment D. EPOpt-A2C was able to find limited success on CartPole but failed to learn a working policy in environment D for the other environments. The effectiveness of EPOpt when combined with PPO but not A2C and then only on Pendulum, Hopper, and HalfCheetah indicates that a continuous action space is important for its success. 
RL2. RL2-A2C and RL2-PPO proved to be difficult to train and data inefficient. On most environments, the Default numbers are low, indicating that a working policy was not found in the classic RL setting of training and testing on a fixed environment. As a result, they also have low In-
better than that in DD. That is, adding variation to a fixed environment can help to stabilize training enough that the algorithm finds a better policy for the original environment.
Assessing Generalization in Deep Reinforcement Learning 
Table 2. Generalization performance (in % success) of each algorithm, averaged over all environments (mean and standard deviation over five runs). 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 78.14± 6.07 76.63± 1.48 63.72± 2.08 RC 81.25± 3.48 72.22± 2.95 60.76± 2.80 
PPO FF 78.22± 1.53 70.57± 6.67 48.37± 3.21 RC 26.51± 9.71 41.03± 6.59 21.59± 10.08 
EPOpt-A2C FF 2.46± 2.86 7.68± 0.61 2.35± 1.59 RC 9.91± 1.12 20.89± 1.39 5.42± 0.24 
EPOpt-PPO FF 85.40± 8.05 85.15± 6.59 59.26± 5.81 RC 5.51± 5.74 15.40± 3.86 9.99± 7.39 
RL2-A2C RC 45.79± 6.67 46.32± 4.71 33.54± 4.64 
RL2-PPO RC 22.22± 4.46 29.93± 8.97 21.36± 4.41 
terpolation and Extrapolation numbers. This suggests that additional structure must be injected into the policy in order to learn useful environmental characteristics from the trajectories. The difficulty in training may also be partially due to the recurrent architecture, as PPO with the RC architecture does not find a successful policy in the classic RL setting as shown in Table 2. Thus, using a Temporal Convolution Network may offer improvements, as they have been shown to outperform RNNs in many sequence modeling tasks (Bai et al., 2018). The same qualitative observations also hold for other values of the number of episodes per trial; see the supplement for specifics. 
In a few environments, such as RL2-PPO on CartPole and RL2-A2C on HalfCheetah, a working policy was found in the classic RL setting, but the algorithm struggled to interpolate or extrapolate. The one success story is RL2-A2C on Pendulum, where we have nearly 100% success rate in DD, interpolate extremely well (Interpolation is 99.82), and extrapolate fairly well (Extrapolation is 81.79). We observed that the partial success of these algorithms on the environments appears to be dependent on two implementation choices: the feature network in the RC architecture and the nonzero coefficient of the KL divergence between the previous policy and current policy in RL2-PPO, which is intended to help stabilize training. 
8. Conclusion We presented an empirical study of generalization in deep RL. We evaluated two state-of-the-art deep RL algorithms, A2C and PPO, and two algorithms that explicitly tackle the problem of generalization in different ways: EPOpt, which aims to be robust to environment variations, and RL2, which aims to automatically adapt to them. In order to do this, we introduced a new testbed and experimental protocol to measure the ability of RL algorithms to generalize to 
environments both similar to and different from those seen during training. A common testbed and protocol, which were missing from previous work, enable us to compare the relative merits of algorithms for building generalizable RL agents. Our code is available online 4 and we hope that it will support future research on generalization in deep RL. 
Overall, the vanilla deep RL algorithms have better generalization performance than their more complex counterparts, being able to interpolate quite well with some extrapolation success. In other words, vanilla deep RL algorithms trained with environmental stochasticity may be more effective for generalization than specialized algorithms; the same conclusion was also suggested by the results of the OpenAI Retro contest (Nichol et al., 2018) and the CoinRun benchmark (Cobbe et al., 2018) in environments with visual input. When combined with PPO under the FF architecture, EPOpt is able to outperform PPO, in particular for the environments with continuous action spaces; however, it does not generalize in the other cases and often fails to train even on the Default environments. RL2 is difficult to train, and in its success cases provides no clear generalization advantage over the vanilla deep RL algorithms or EPOpt. 
The sensitivity of the effectiveness of EPOpt and RL2 to the base algorithm, architecture, and environment presents an avenue for future work, as EPOpt and RL2 were presented as general-purpose techniques. We have considered model-free RL algorithms in our evaluation; another direction for future work is to further investigate model-based RL algorithms, such as the recent work of Sæmundsson et al. (2018) and Clavera et al. (2018). Because model-based RL explicitly learns the system dynamics and is generally more data efficient, it could be better leveraged by adaptive techniques for generalization. 
4http://www.github.com/sunblaze-ucb/rl-generalization
Assessing Generalization in Deep Reinforcement Learning 
References Al-Shedivat, M., Bansal, T., Burda, Y., Sutskever, I., Mor-
datch, I., and Abbeel, P. Continuous adaptation via metalearning in nonstationary and competitive environments. In International Conference on Learning Representations (ICLR), 2018. 
Arulkumaran, K., Deisenroth, M. P., Brundage, M., and Bharath, A. A. Deep reinforcement learning: A brief survey. IEEE Signal Processing Magazine, 34(6), 2017. 
Bai, S., Kolter, J. Z., and Koltun, V. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling. arXiv:1803.01271, 2018. 
Barto, A. G., Sutton, R. S., and Anderson, C. W. Neuronlike adaptive elements that can solve difficult learning control problems. IEEE Transactions on Systems, Man, and Cybernetics, 13(5), 1983. 
Beattie, C., Leibo, J. Z., Teplyashin, D., Ward, T., Wain-wright, M., Küttler, H., Lefrancq, A., Green, S., et al. DeepMind Lab. arXiv:1612.03801, 2016. 
Bellemare, M. G., Naddaf, Y., Veness, J., and Bowling, M. The arcade learning environment: An evaluation platform for general agents. Journal of Artificial Intelligence Research (JAIR), 47, 2013. 
Brockman, G., Cheung, V., Pettersson, L., Schneider, J., Schulman, J., Tang, J., and Zaremba, W. OpenAI Gym. arXiv:1606.01540, 2016. 
Clavera, I., Nagabandi, A., Fearing, R. S., Abbeel, P., Levine, S., and Finn, C. Learning to adapt: Meta-learning for model-based control. arXiv:1803.11347, 2018. 
Cobbe, K., Klimov, O., Hesse, C., Kim, T., and Schulman, J. Quantifying generalization in reinforcement learning. arXiv:1812.02341, 2018. 
Dhariwal, P., Hesse, C., Plappert, M., Radford, A., Schul-man, J., Sidor, S., and Wu, Y. OpenAI Baselines. https: //github.com/openai/baselines, 2017. 
Dietterich, T. G. Steps toward robust artificial intelligence. AI Magazine, 38(3), 2017. 
Donoho, D. 50 years of data science. In Tukey Centennial Workshop, 2015. 
Duan, Y., Chen, X., Houthooft, R., Schulman, J., and Abbeel, P. Benchmarking deep reinforcement learning for continuous control. In International Conference on Machine Learning (ICML), 2016a. 
Duan, Y., Schulman, J., Chen, X., Bartlett, P. L., Sutskever, I., and Abbeel, P. RL2: Fast reinforcement learning via slow reinforcement learning. arXiv:1611.02779, 2016b. 
Finn, C., Abbeel, P., and Levine, S. Model-agnostic metalearning for fast adaptation of deep networks. In Interna-tional Conference on Machine Learning (ICML), 2017. 
Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., and Meger, D. Deep reinforcement learning that matters. In AAAI Conference on Artificial Intelligence (AAAI), 2018. 
Hinton, G., Srivastava, N., and Swersky, K. Neu-ral networks for machine learning lecture 6. https://www.cs.toronto.edu/˜tijmen/ csc321/slides/lecture_slides_lec6.pdf, 2012. 
Justesen, N., Torrado, R. R., Bontrager, P., Khalifa, A., Togelius, J., and Risi, S. Procedural level generation improves generality of deep reinforcement learning. arXiv:1806.10729, 2018. 
Kansky, K., Silver, T., Mély, D. A., Eldawy, M., Lázaro-Gredilla, M., Lou, X., Dorfman, N., Sidor, S., Phoenix, D. S., and George, D. Schema networks: Zero-shot transfer with a generative causal model of intuitive physics. In International Conference on Machine Learning (ICML), 2017. 
Kempka, M., Wydmuch, M., Runc, G., Toczek, J., and Jaśkowski, W. ViZDoom: A Doom-based AI research platform for visual reinforcement learning. In IEEE Con-ference on Computational Intelligence and Games, 2016. 
Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. In International Conference on Learning Representations (ICLR), 2015. 
Lake, B. M., Ullman, T. D., Tenenbaum, J. B., and Gersh-man, S. J. Building machines that learn and think like people. Behavioral and Brain Sciences, 40, 2017. 
Leike, J., Martic, M., Krakovna, V., Ortega, P. A., Everitt, T., Lefrancq, A., Orseau, L., and Legg, S. Ai safety gridworlds. arXiv:1711.09883, 2017. 
Lim, S. H., Xu, H., and Mannor, S. Reinforcement learning in robust Markov decision processes. In Neural Informa-tion Processing Systems (NIPS), 2013. 
Machado, M. C., Bellemare, M. G., Talvitie, E., Veness, J., Hausknecht, M. J., and Bowling, M. Revisiting the arcade learning environment: Evaluation protocols and open problems for general agents. arXiv:1709.06009, 2017. 
Marcus, G. Deep learning: A critical appraisal. arXiv:1801.00631, 2018.
Assessing Generalization in Deep Reinforcement Learning 
Mishra, N., Rohaninejad, M., Chen, X., and Abbeel, P. A simple neural attentive meta-learner. In International Conference on Learning Representations (ICLR), 2018. 
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Ve-ness, J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., et al. Human-level control through deep reinforcement learning. Nature, 518(7540), 2015. 
Mnih, V., Badia, A. P., Mirza, M., Graves, A., Lillicrap, T. P., Harley, T., Silver, D., and Kavukcuoglu, K. Asyn-chronous methods for deep reinforcement learning. In International Conference on Machine Learning (ICML), 2016. 
Moore, A. W. Efficient memory-based learning for robot control. Technical report, University of Cambridge Com-puter Laboratory, 1990. 
Morimoto, J. and Doya, K. Robust reinforcement learning. In Neural Information Processing Systems (NIPS), 2001. 
Nichol, A., Pfau, V., Hesse, C., Klimov, O., and Schulman, J. Gotta learn fast: A new benchmark for generalization in RL. arXiv:1804.03720, 2018. 
Nilim, A. and Ghaoui, L. E. Robustness in Markov decision problems with uncertain transition matrices. In Neural Information Processing Systems (NIPS), 2004. 
Pinto, L., Davidson, J., Sukthankar, R., and Gupta, A. Ro-bust adversarial reinforcement learning. In International Conference on Machine Learning (ICML), 2017. 
Rajeswaran, A., Ghotra, S., Ravindran, B., and Levine, S. EPOpt: Learning robust neural network policies using model ensembles. In International Conference on Learn-ing Representations (ICLR), 2017a. 
Rajeswaran, A., Lowrey, K., Todorov, E. V., and Kakade, S. M. Towards generalization and simplicity in continuous control. In Neural Information Processing Systems (NIPS), 2017b. 
Roy, A., Xu, H., and Pokutta, S. Reinforcement learning under model mismatch. In Neural Information Processing Systems (NIPS), 2017. 
Ruder, S. An overview of multi-task learning in deep neural networks. arXiv:1706.05098, 2017. 
Rusu, A. A., Rabinowitz, N. C., Desjardins, G., Soyer, H., Kirkpatrick, J., Kavukcuoglu, K., Pascanu, R., and Had-sell, R. Progressive neural networks. arXiv:1606.04671, 2016. 
Sæmundsson, S., Hofmann, K., and Deisenroth, M. P. Meta reinforcement learning with latent variable Gaussian processes. In Conference on Uncertainty in Artificial Intelli-gence (UAI), 2018. 
Schulman, J., Levine, S., Abbeel, P., Jordan, M. I., and Moritz, P. Trust region policy optimization. In Interna-tional Conference on Machine Learning (ICML), 2015. 
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. arXiv:1707.06347, 2017. 
Sung, F., Zhang, L., Xiang, T., Hospedales, T., and Yang, Y. Learning to learn: Meta-critic networks for sample efficient learning. arXiv:1706.09529, 2017. 
Sutton, R. S. Generalization in reinforcement learning: Suc-cessful examples using sparse coarse coding. In Neural Information Processing Systems (NIPS), 1995. 
Sutton, R. S. and Barto, A. G. Reinforcement Learning: An Introduction. MIT Press, 2nd edition, 2017. 
Tamar, A., Glassner, Y., and Mannor, S. Optimizing the CVaR via sampling. In AAAI Conference on Artificial Intelligence (AAAI), 2015. 
Taylor, M. E. and Stone, P. Transfer learning for reinforcement learning domains: A survey. Journal of Machine Learning Research (JMLR), 10, 2009. 
Todorov, E., Erez, T., and Tassa, Y. MuJoCo: A physics engine for model-based control. In Intelligent Robots and Systems (IROS), 2012. 
Wang, J. X., Kurth-Nelson, Z., Tirumala, D., Soyer, H., Leibo, J. Z., Munos, R., Blundell, C., Kumaran, D., and Botvinick, M. Learning to reinforcement learn. arXiv:1611.05763, 2016. 
Whiteson, S., Tanner, B., Taylor, M. E., and Stone, P. Pro-tecting against evaluation overfitting in empirical reinforcement learning. In IEEE Symposium on Adaptive Dy-namic Programming And Reinforcement Learning, 2011. 
Yu, W., Tan, J., Liu, C. K., and Turk, G. Preparing for the unknown: Learning a universal policy with online system identification. In Robotics: Science and Systems (RSS), 2017. 
Zhang, A., Ballas, N., and Pineau, J. A dissection of overfitting and generalization in continuous reinforcement learning. arXiv:1806.07937, 2018.
Assessing Generalization in Deep Reinforcement Learning 
Acknowledgments This material is in part based upon work supported by the National Science Foundation under Grant No. TWC-1409915, DARPA under FA8750-17-2-0091, and Berkeley Deep Drive. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation. 
A. Training Hyperparameters The grid values we search over for each hyperparameter and each algorithm are listed below. In sum, the search space contains 183 unique hyperparameter configurations for all algorithms on a single training environment (3, 294 training configurations), and each trained agent is evaluated on 3 test settings (9, 882 total train/test configurations). We report results for 5 runs of the full grid search, a total of 49, 410 experiments. 
 Learning rate: 
– A2C, EPOpt-A2C with RC architecture, and RL2-A2C: [7e−3, 7e−4, 7e−5] 
– EPOpt-A2C with FF architecture: [7e−2, 7e−3, 7e−4] 
– PPO, EPOpt-PPO with RC architecture: [3e−3, 3e−4, 3e−5] 
– EPOpt-PPO with FF architecture: [3e−2, 3e−3, 3e−4] 
– RL2-PPO: [3e−4, 3e−5, 3e−6] 
 Length of the trajectory generated at each iteration: 
– A2C and RL2-A2C: [5, 10, 15] – PPO and RL2-PPO: [128, 256, 512] 
 Policy entropy coefficient: [1e−2, 1e−3, 1e−4, 1e−5] 
 KL divergence coefficient: [0.3, 0.2, 0.0] 
B. Detailed Experimental Results In order to elucidate the generalization behavior of each algorithm, here we present the quantities in Table 1 of the paper for each environment. 
C. Behavior of MountainCar On MountainCar, several of the algorithms, including A2C with both architectures and PPO with the FF architecture, have greater success on Extrapolation than Interpolation, which is itself sometimes greater than Default (see Table 5). At first glance, this is unexpected because Extrapolation 
combines the success rates of DR, DE, and RE, with E containing more extreme parameter settings, while Interpolation is the success rate of RR. To explain this phenomenon, we hypothesize that compared to R, E is dominated by easy parameter settings, e.g., those where the car is light but the force of the push is strong, allowing the agent to reach the top of the hill in only a few steps. In order to test this hypothesis, we create heatmaps of the rewards achieved by A2C with both architectures and PPO with the FF architecture trained on D and tested on R and E. We show only the heatmap for A2C with the FF architecture, in Figure 2; the other two are qualitatively similar. Referring to the description of the environments in the main paper, we see that the reward achieved by the policy is higher in the regions corresponding to E. Indeed, it appears that the largest regions of E are those with a large force, which enables the trained policy to push the car up the hill in much less than 110 time steps, achieving the goal defined in Section 6 of the paper. (Note that the reward is the negative of the number of time steps taken to push the car up the hill.) 
On the other hand, Figure 3 shows a similar heatmap for A2C with the FF architecture on Pendulum, in which In-terpolation is greater than Extrapolation. In this case, the policy trained on D struggles more on environments from E than on those from R. This special case demonstrates the importance of considering a wide variety of environments when assessing the generalization performance of an algorithm; each environment may have idiosyncrasies that cause performance to be correlated with parameters. 
0.000 0.002 0.004 0.006 0.008 0.010 force 
0.002 
0.004 
0.006 
0.008 
0.010 
m as s 
−200 
−175 
−150 
−125 
−100 
−75 
−50 
−25 
Figure 2. MountainCar: heatmap of the rewards achieved by A2C with the FF architecture on DR and DE. The axes are the two environment parameters varied in R and E.
Assessing Generalization in Deep Reinforcement Learning 
Table 3. Mean and standard deviation over five runs of generalization performance (in % success) on Acrobot. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 88.52± 1.32 72.88± 0.74 66.56± 0.52 RC 88.24± 1.53 73.46± 1.11 67.94± 1.06 
PPO FF 87.20± 1.11 72.78± 0.44 64.93± 1.05 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
EPOpt-A2C FF 0.0± 0.0 0.0± 0.0 0.0± 0.0 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
EPOpt-PPO FF 79.60± 5.86 69.20± 1.64 65.05± 2.16 RC 3.10± 3.14 6.40± 3.65 15.57± 5.59 
RL2-A2C RC 65.70± 8.68 57.70± 2.40 57.01± 2.70 
RL2-PPO RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
Table 4. Mean and standard deviation over five runs of generalization performance (in % success) on CartPole. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 100.00± 0.0 100.00± 0.0 93.63± 9.30 RC 100.00± 0.0 100.00± 0.0 83.00± 11.65 
PPO FF 100.00± 0.0 100.00± 0.0 86.20± 12.60 RC 65.58± 27.81 70.80± 21.02 45.00± 18.06 
EPOpt-A2C FF 14.74± 17.14 43.06± 3.48 10.48± 9.41 RC 57.00± 4.50 55.88± 3.97 32.53± 1.47 
EPOpt-PPO FF 99.98± 0.04 99.46± 0.79 73.58± 12.19 RC 29.94± 31.58 20.22± 17.83 14.55± 20.09 
RL2-A2C RC 20.78± 39.62 0.06± 0.12 0.12± 0.23 
RL2-PPO RC 87.20± 12.95 54.22± 34.85 51.00± 14.60 
Table 5. Mean and standard deviation over five runs of generalization performance (in % success) on MountainCar. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 79.78± 11.38 84.10± 1.25 89.72± 0.65 RC 95.88± 4.10 74.84± 6.82 89.77± 0.76 
PPO FF 99.96± 0.08 84.12± 0.84 90.21± 0.37 RC 0.0± 0.0 63.36± 0.74 15.86± 31.71 
EPOpt-A2C FF 0.0± 0.0 3.04± 0.19 3.63± 0.49 RC 0.0± 0.0 62.46± 0.80 0.0± 0.0 
EPOpt-PPO FF 74.42± 37.93 84.86± 1.09 87.42± 5.11 RC 0.0± 0.0 65.74± 4.88 29.82± 27.30 
RL2-A2C RC 0.32± 0.64 57.86± 2.97 21.56± 30.35 
RL2-PPO RC 0.0± 0.0 60.10± 0.91 31.27± 26.24
Assessing Generalization in Deep Reinforcement Learning 
Table 6. Mean and standard deviation over five runs of generalization performance (in % success) on Pendulum. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 100.00± 0.0 99.86± 0.14 90.27± 3.07 RC 100.00± 0.0 99.96± 0.05 79.58± 6.41 
PPO FF 0.0± 0.0 31.80± 40.11 0.0± 0.0 RC 73.28± 36.80 90.94± 7.79 61.11± 31.08 
EPOpt-A2C FF 0.0± 0.0 0.0± 0.0 0.0± 0.0 RC 2.48± 4.96 7.00± 10.81 0.0± 0.0 
EPOpt-PPO FF 100.00± 0.0 77.34± 38.85 54.72± 27.57 RC 0.0± 0.0 0.04± 0.08 0.0± 0.0 
RL2-A2C RC 100.00± 0.0 99.82± 0.31 81.79± 3.88 
RL2-PPO RC 46.14± 17.67 65.22± 21.78 45.76± 8.38 
Table 7. Mean and standard deviation over five runs of generalization performance (in % success) on HalfCheetah. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 85.06± 19.68 91.96± 8.60 40.54± 8.34 RC 88.06± 12.26 74.70± 13.49 42.96± 7.79 
PPO FF 96.62± 3.84 95.02± 2.96 38.51± 15.13 RC 20.22± 17.01 21.08± 26.04 7.55± 5.04 
EPOpt-A2C FF 0.0± 0.0 0.0± 0.0 0.0± 0.0 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
EPOpt-PPO FF 99.76± 0.08 99.28± 0.87 53.41± 9.41 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
RL2-A2C RC 87.96± 4.21 62.48± 29.18 40.78± 5.99 
RL2-PPO RC 0.0± 0.0 0.0± 0.0 0.16± 0.32 
Table 8. Mean and standard deviation over five runs of generalization performance (in % success) on Hopper. 
Algorithm Architecture Default Interpolation Extrapolation 
A2C FF 15.46± 7.58 11.00± 7.01 1.63± 2.77 RC 15.34± 8.82 10.38± 15.14 1.31± 1.23 
PPO FF 85.54± 6.96 39.68± 16.69 10.36± 6.79 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
EPOpt-A2C FF 0.0± 0.0 0.0± 0.0 0.0± 0.0 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
EPOpt-PPO FF 58.62± 47.51 80.78± 29.18 21.39± 16.62 RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
RL2-A2C RC 0.0± 0.0 0.0± 0.0 0.0± 0.0 
RL2-PPO RC 0.0± 0.0 0.02± 0.04 0.0± 0.0
Assessing Generalization in Deep Reinforcement Learning 
0.6 0.8 1.0 1.2 1.4 length 
0.6 
0.8 
1.0 
1.2 
1.4 
m as s 
−1200 
−1000 
−800 
−600 
−400 
−200 
Figure 3. Pendulum: heatmap of the rewards achieved by A2C with the FF architecture on DR and DE. The axes are the two environment parameters varied in R and E. 
D. Varying N in RL2 
We test the sensitivity of the results for RL2-A2C and RL2-PPO to the hyperparameter of the number of episodes per trial, N . We consider N = 1 and N = 5, to determine whether it was too difficult to train a RNN over trajectories of N = 2 episodes or more episodes were needed for adaptation. Table 9 contains the results for N = 1 on each environment (and averaged); Table 10 is a similar table for N = 5. 
It appears that increasing N usually degrades generalization performance, indicating that the increasing trajectory length does make training more difficult. Nevertheless, there are two special cases where generalization performance improves as N increases, on Acrobot with RL2-A2C and Pendulum with RL2-PPO. 
Note that when N = 1, RL2-A2C is the same as A2C with the RC architecture but with the actions, rewards, and done flags input in addition to the states; the same is true of RL2-PPO and PPO with the RC architecture. However, on average its generalization performance is not as good; for example Interpolation is 66.83 for RL2-A2C but 72.22 for A2C with the RC architecture. This suggests that RL2 is unable to effectively utilize the information contained in the trajectories to learn about the environment dynamics and a different policy architecture from a simple RNN is needed. 
E. Training Curves To investigate the effect of EPOpt and RL2 and the different environment versions on training, we plotted the training curves for PPO, EPOpt-PPO, and RL2-PPO on 
each version of each environment, averaged over the five experiment runs and showing error bands based on the standard deviation over the runs. Training curves for all algorithms and environments are available at the following link: https://drive.google.com/drive/folders/1H5aBv-Lex6WQzKI-a LCgJUER-UQzKF4. We observe that in the majority of cases training appears to be stabilized by the increased randomness in the environments in R and E, including situations where successful policies are found. This behavior is particularly apparent for CartPole, whose training curves are shown in Figure 4 and in which all algorithms above are able to find at least partial success. We see that especially towards the end of the training period, the error bands for training on E are narrower than those for training on D or R. Except for EPOpt-PPO with the FF architecture, the error bands for training on D appear to be the widest. In particular, RL2-PPO is very unstable when trained on D, possibly because the more expressive policy network overfits to the generated trajectories. 
F. Videos of trained agents The above link also contains videos of the trained agents of one run of the experiments for all environments and algorithms. Using HalfCheetah as a case study, we describe some particularly interesting behavior we see. 
A trend we noticed across several algorithms were similar changes in the cheetah’s gait that seem to be correlated with the difficulty of the environment. The cheetah’s gait became forward-leaning when trained on the Random and Extreme environments, and remained relatively flat in the agents trained on the Deterministic environment (see figures 5 and 6). We hypothesize that the forward-leaning gait developed to counteract conditions in the R and E settings. The agents with the forward-learning gait were able to recover from face planting (as seen in the second row of figure 5), as well as maintain balance after violent leaps likely caused by settings with unexpectedly high power. In addition to becoming increasingly forward-leaning, the agents’ gait also tended to become stiffer in the more extreme settings, developing a much shorter, twitching stride. Though it reduces the agents’ speed, a shorter, stiffer stride appears to make the agent more resistant to adverse settings that would cause an agent with a longer stride to fall. This example illustrates how training on a range of different environment configurations may encourage policies that are more robust to changes in system dynamics at test time.
Assessing Generalization in Deep Reinforcement Learning 
Table 9. Mean and standard deviation over five runs of generalization performance (in % success) for RL2-A2C and RL2-PPO when N = 1. 
Environment Algorithm Default Interpolation Extrapolation 
Average RL2-A2C 66.83± 7.32 65.19± 2.86 55.76± 4.41 RL2-PPO 27.01± 8.20 34.02± 5.92 17.59± 6.27 
Acrobot RL2-A2C 30.54± 17.06 20.10± 16.10 33.95± 9.43 RL2-PPO 0.0± 0.0 0.0± 0.0 0.0± 0.0 
CartPole RL2-A2C 99.90± 0.20 100.0± 0.0 87.50± 3.81 RL2-PPO 81.76± 22.33 86.62± 9.47 59.10± 21.36 
MountainCar RL2-A2C 88.94± 5.30 81.84± 0.78 86.82± 2.62 RL2-PPO 0.0± 0.0 55.02± 0.89 11.11± 22.23 
Pendulum RL2-A2C 100.0± 0.0 99.98± 0.04 87.81± 2.74 RL2-PPO 42.58± 34.73 48.80± 21.42 34.10± 24.76 
HalfCheetah RL2-A2C 80.54± 30.70 82.50± 14.23 35.24± 21.03 RL2-PPO 37.70± 30.62 13.68± 15.81 1.20± 1.49 
Hopper RL2-A2C 1.04± 1.23 6.74± 5.71 3.26± 3.75 RL2-PPO 0.0± 0.0 0.0± 0.0 0.0± 0.0 
Table 10. Mean and standard deviation over five runs of generalization performance (in % success) for RL2-A2C and RL2-PPO when N = 5. 
Environment Algorithm Default Interpolation Extrapolation 
Average RL2-A2C 41.08± 4.66 41.11± 2.82 27.97± 2.37 RL2-PPO 12.77± 2.94 21.16± 1.27 15.59± 5.39 
Acrobot RL2-A2C 79.02± 2.67 69.86± 0.90 64.59± 0.72 RL2-PPO 0.0± 0.0 0.0± 0.0 0.0± 0.0 
CartPole RL2-A2C 0.0± 0.0 0.0± 0.0 0.0± 0.0 RL2-PPO 1.04± 1.63 1.04± 1.51 0.16± 0.31 
MountainCar RL2-A2C 0.0± 0.0 56.60± 2.59 4.39± 2.26 RL2-PPO 0.0± 0.0 62.32± 1.24 31.33± 27.67 
Pendulum RL2-A2C 99.98± 0.04 99.68± 0.35 82.67± 3.64 RL2-PPO 75.58± 19.00 63.60± 9.27 62.07± 5.68 
HalfCheetah RL2-A2C 67.50± 29.37 20.50± 17.01 16.16± 11.05 RL2-PPO 0.0± 0.0 0.0± 0.0 0.0± 0.0 
Hopper RL2-A2C 0.0± 0.0 0.0± 0.0 0.0± 0.0 RL2-PPO 0.0± 0.0 0.0± 0.0 0.0± 0.0
Assessing Generalization in Deep Reinforcement Learning 
0 2000 4000 6000 8000 10000 12000 14000 Total Episodes 
0 
50 
100 
150 
200 
M ea 
n Ep 
iso de 
 R ew 
ar d 
CartPole-E CartPole-R CartPole-D 
(a) PPO with FF architecture 
0 2000 4000 6000 8000 10000 12000 14000 Total Episodes 
25 
50 
75 
100 
125 
150 
175 
200 
225 
M ea 
n Ep 
iso de 
 R ew 
ar d 
CartPole-E CartPole-R CartPole-D 
(b) PPO with RC architecture 
0 2000 4000 6000 8000 10000 12000 14000 Total Episodes 
25 
50 
75 
100 
125 
150 
175 
200 
225 
M ea 
n Ep 
iso de 
 R ew 
ar d 
CartPole-E CartPole-R CartPole-D 
(c) EPOpt-PPO with FF architecture 
0 2000 4000 6000 8000 10000 12000 14000 Total Episodes 
0 
50 
100 
150 
200 M ea 
n Ep 
iso de 
 R ew 
ar d 
CartPole-E CartPole-R CartPole-D 
(d) EPOpt-PPO with RC architecture 
0 2000 4000 6000 8000 10000 12000 14000 Total Episodes 
25 
50 
75 
100 
125 
150 
175 
200 
225 
M ea 
n Ep 
iso de 
 R ew 
ar d 
CartPole-E CartPole-R CartPole-D 
(e) RL2-PPO 
Figure 4. Training curves for the PPO-based algorithms on CartPole, all three environment versions. Note that the decrease in mean episode reward at 10000 episodes in the two EPOpt-PPO plots is due to the fact that it transitions from being computed using all generated episodes (ε = 1) to only the 10% with lowest reward (ε = 0.1).
Assessing Generalization in Deep Reinforcement Learning 
Figure 5. Video frames of agents trained with A2C on HalfCheetah, trained in the Deterministic (D), Random (R), and Extreme (E) settings (from top to bottom). All agents evaluated in the D setting. 
Figure 6. Video frames of agents trained with PPO on HalfCheetah, trained in the Deterministic (D), Random (R), and Extreme (E) settings (from top to bottom). All agents evaluated in the D setting.