> Source: https://icml.cc/virtual/2025/poster/44177

ICML Poster Online Robust Reinforcement Learning Through Monte-Carlo Planning
Skip to yearly menu bar Skip to main content
Main Navigation
ICML
Help/FAQ
Contact ICML
Create Profile
Code of Conduct
Privacy Policy
Press
Journal To Conference Track
Careers
Downloads
Inclusion
Future Meetings
My Stuff
Login
Select Year: (2025)
2026
2025
2024
2023
2022
2021
2020
2019
2018
2017
2016
2015
2014
2013
2012
2011
2010
2009
2008
2007
2006
2005
2004
2002
1996
IMLS Archives
Getting Started
Schedule
Tutorials
Main Conference
Invited Talks
Orals
Awards
Test of Time Award
Papers
Spotlight Posters
Workshops
Community
Socials
Exhibitors
Exhibitors
Expo
Organizers
Help
FAQ
RocketChat Help
RocketChat Desktop Client
Poster
Online Robust Reinforcement Learning Through Monte-Carlo Planning
Tuan Dam ⋅ Kishan Panaganti ⋅ Brahim Driss ⋅ Adam Wierman
2025 Poster
[ Poster] [ OpenReview]
Abstract
Monte Carlo Tree Search (MCTS) is a powerful framework for solving complex decision-making problems, yet it often relies on the assumption that the simulator and the real-world dynamics are identical. Although this assumption helps achieve the success of MCTS in games like Chess, Go, and Shogi, the real-world scenarios incur ambiguity due to their modeling mismatches in low-fidelity simulators. In this work, we present a new robust variant of MCTS that mitigates dynamical model ambiguities. Our algorithm addresses transition dynamics and reward distribution ambiguities to bridge the gap between simulation-based planning and real-world deployment. We incorporate a robust power mean backup operator and carefully designed exploration bonuses to ensure finite-sample convergence at every node in the search tree. We show that our algorithm achieves a convergence rate of O ( n − 1 / 2 ) for the value estimation at the root node, comparable to that of standard MCTS. Finally, we provide empirical evidence that our method achieves robust performance in planning problems even under significant ambiguity in the underlying reward distribution and transition dynamics.
Show more
Lay Summary
Imagine you're learning to play a video game by practicing on a simulator, but when you finally play the real game, the physics are slightly different—maybe the character jumps a bit lower or moves a bit slower than in the simulator. This gap between practice and reality is a major challenge in artificial intelligence, where computer programs often train in simplified virtual environments before being deployed in the messy real world. This paper tackles this "simulation-to-reality gap" by making AI planning algorithms more robust—meaning they work well even when the real world differs from their training environment. The researchers focus on a popular AI technique called Monte Carlo Tree Search (MCTS), which is like playing out thousands of possible future scenarios in your head before making a decision. Think of MCTS like a chess player who considers many possible moves and counter-moves before choosing their next play. The difference here is that instead of assuming the game rules are perfectly known, the algorithm plans for uncertainty—it considers that the "rules" of the real world might be somewhat different from what it learned in simulation. The key innovation is building uncertainty directly into the decision-making process. Instead of assuming the best-case scenario, the algorithm prepares for reasonable worst-case scenarios. It's like a cautious driver who plans their route assuming there might be unexpected traffic, rather than optimistically assuming clear roads. The algorithm does this by considering multiple possible versions of how the world might behave, making decisions that work well across all these possibilities, and balancing between being too cautious and being too optimistic. This research is important because it helps bridge the gap between AI systems that work perfectly in labs and AI systems that work reliably in the real world. Applications could include autonomous vehicles that can handle unexpected road conditions, medical treatment planning that accounts for patient variability, financial trading systems that remain stable during market volatility, and robotics that can adapt when the real environment differs from simulations. The researchers proved mathematically that their robust algorithm maintains the same learning speed as traditional methods while being much more reliable when faced with unexpected conditions. They tested this in several scenarios, including gambling problems and navigation tasks, showing that the robust approach maintains steady performance even when the real environment differs significantly from what was expected. This work represents a step toward AI systems that are not just smart, but also reliable and trustworthy in real-world deployment. By explicitly planning for uncertainty rather than ignoring it, we can build AI that performs consistently across the messy, unpredictable conditions of the real world.
Show more
Video
Chat is not available.
bytez 
Online Robust Reinforcement Learning Through Monte-Carlo Planning
2025
·
ICML
Paper
Abstract
Monte Carlo Tree Search (MCTS) is a powerful framework for solving complex decision-making problems, yet it often relies on the assumption that the simulator and the real-world dynamics are identical. Although this assumption helps achieve the success of MCTS in games like Chess, Go, and Shogi, the real-world scenarios incur ambiguity due to their modeling mismatches in low-fidelity simulators. In this work, we present a new robust variant of MCTS that mitigates dynamical model ambiguities. Our algorithm addresses transition dynamics and reward distribution ambiguities to bridge the gap between simulation-based planning and real-world deployment. We incorporate a robust power mean backup operator and carefully designed exploration bonuses to ensure finite-sample convergence at every node in the search tree. We show that our algorithm achieves a convergence rate of 
for the value estimation at the root node, comparable to that of standard MCTS. Finally, we provide empirical evidence that our method achieves robust performance in planning problems even under significant ambiguity in the underlying reward distribution and transition dynamics.
1. Introduction
Reinforcement learning (RL) provides a statistical machine learning framework to interact with the environments—such as autonomous vehicles, agile robots, and network systems—sequentially and learn to take control actions to achieve the desired objective. Monte Carlo Tree Search (MCTS) algorithm, in conjunction with deep learning methods, solve complex decision-making problems in high-dimensional environments. Its celebrated success stories include autonomous RL decision-making agents playing board games Chess, Go, Shogi (Silver et al., 2016; Schrittwieser et al., 2020), Poker (Brown and Sandholm, 2018; Keshavarzi and Navidi, 2025), and solving various real-world challenging tasks like robotics and autonomous systems (Hoel et al., 2019; Kartal et al., 2019; Dam et al., 2022). MCTS offers a principled way to balance exploration and exploitation by using combinatorial search mechanisms derived from online simulated trajectories. As a result, MCTS can effectively promote the exploration of promising regions of the environment with only partial modeling information of the environment.
However, most of these successes are limited to structured or simulated environments. As successful as RL algorithms are, an issue in applying them to real-world dynamical systems is the unavoidable discrepancy between the simulators and the actual real-world system dynamics. In traditional RL approaches (Kaelbling et al., 1996; Salvato et al., 2021), transition models are often learned from data collected by interacting with simulator models to avoid unsafe interactions with real-world systems, and reward models may be subject to stochasticity, hacked rewards, or unmodeled external factors. Such ambiguities arise from a variety of sources: limited training data, non-stationary environments, adversarial conditions, partial observability, or simply modeling simplifications. These factors can lead to a so-called simulation-to-reality gap, where the policy or value function that appears optimal in the simulated environment may perform poorly when deployed in the real world. A natural approach to addressing these challenges is to incorporate robustness against simulation-to-reality gaps directly into the planning algorithm.
RL agents making decisions under the framework of Robust Markov Decision Processes (RMDPs) (Iyengar, 2005; Nilim and El Ghaoui, 2005) offer a principled mechanism to conceptualize robustness against transition model and reward model mismatches raised by simulation-to-reality gaps. These robust RL agents explore policies that maximize expected returns under the worst-case model within a prescribed ambiguity set. The ambiguity set is typically constructed as a ball around the simulator dynamics or re-
ward model, with the design choice of the ball size covering the real-world ground truth model descriptors. Recent works demonstrate their potential to achieve robust decision-making performance when faced with perturbations in transition dynamics and reward function models. However, while value iteration and policy optimization methods have been introduced and analyzed for robust RL, MCTS-based planning algorithms have not been explored, as per the authors' knowledge. We discuss more detailed related works in Section 2.
In this work, we propose a novel robust MCTS algorithm equipped with non-asymptotic performance guarantees under model ambiguity set. Importantly, we incorporate both reward and transition ambiguity robustness, similar to recent works (Zhou et al., 2021; Wang et al., 2024b) in robust RL. In particular, our work resolves the following questions:
Can we use a search-based planning approach like MCTS to balance exploitation and exploration for the robust RL problem? What theoretical guarantee can we provide? Can we show robust performance against standard algorithms under the simulation-to-reality issue?
Our approach embeds the distributionally robust optimization (Rahimian and Mehrotra, 2019) mathematical principle into the MCTS framework, ensuring that the value estimates and action selections are robust to transitions and rewards drawn from the ambiguity sets. More precisely, we conceptualize a robust backup operator and design exploration bonuses that accommodate ambiguity sets defined using total variation, Kullback-Leibler, chi-squared, or Wasserstein measures. This allows MCTS to simultaneously use a tree search mechanism to solve for robust value estimates by trading off exploitation and exploration while achieving robust policies that work uniformly well across different models in the ambiguity set.
One of the key contributions of this work is the establishment of finite-sample bounds on the convergence rates of our robust MCTS algorithm. Viewing each node in the MCTS tree as a non-stationary bandit problem sheds light on the nontrivial challenges of controlling the interaction between ambiguity sets and exploration bonuses. More specifically, coming up with exploration bonuses (thereby robust value approximations) is nontrivial based on the non-linear backup operator due to the formalization of robustness. We overcome these challenges by building on a sequence of technical lemmas and applying concentration inequalities to the robust backup operator, we show that our method attains a convergence rate of order 
for robust value estimation at the root node, where n is the number of states visited while exploring the environment. This convergence rate also matches the best-known results for standard, non-robust MCTS, thereby demonstrating that introducing robustness need not change the convergence speed in terms of the number of samples.
Contributions. In this work, to the best of our knowledge, we are the first to propose an MCTS-based algorithm for the robust RL problem. Our contributions are threefold:
•
Robust MCTS Algorithm: We solve the online robust RL problem–accounting for model ambiguity in both transitions and rewards–using a planning algorithm enabled by MCTS. This fundamental first step paves the way for future applications in large-scale dynamical systems.
•
Non-Asymptotic Guarantees: We provide rigorous finite-sample performance bounds, ensuring that the robust MCTS converges with a known rate, on par with standard MCTS. Our analysis leads to novel exploration bonuses that arise from careful analyses of robust backup operators and the tree search mechanism by recasting robust MCTS for different ambiguity sets as a collection of non-stationary multi-armed bandit problems.
•
Robust Empirical Performance: We conduct experiments in two environments (Gambler's Problem and Frozen Lake) to evaluate our robust algorithm, demonstrating that it achieves superior robust performance to model mismatches than the standard MCTS algorithm baseline.
2. Related Works
Robust RL. Robust RL agents make decisions to alleviate environmental ambiguities under the RMDP framework introduced by Iyengar (2005); Nilim and El Ghaoui (2005) considers distributional robust optimization (Rahimian and Mehrotra, 2019) mathematical formularization. Many recent works extensively study the robust RL problem, addressing multiple aspects of the challenges of decision-making learning algorithms. Panaganti and Kalathil (2021); Zhou et al. (2021); Panaganti and Kalathil (2022); Shi and Chi (2024) propose model-based dynamic programming algorithms to solve the robust RL problem for finite state-action environments, and Dong et al. (2022); Pana- ganti et al. (2025) extend to the online and offline settings, respectively. These works focus on addressing the sample complexity—minimal samples needed from the simulator model (leading to the construction of an approximate model) for every state-action pair to obtain an approximate value estimation—issue. Panaganti and Kalathil (2021); Panaganti et al. (2022); Zhang et al. (2023) propose model-free value function approximation-based robust RL algorithms utilizing special structures in the Bellman backups arising due to specific forms of ambiguity sets. Different from these approaches, our algorithm is inspired by MCTS to solve the robust RL problem. MCTS scales well (Silver et al., 2016) for large problems by embedding strong search mechanisms into model-based planning approaches in RL.
MCTS for non-robust RL. AlphaGo-like (Silver et al., 2016) agents are powered by tree search mechanisms such as MCTS in traditional dynamic programming planning for standard RL. Kocsis and Szepesv´ari (2006); Shah et al. (2020); Dam et al. (2024b) provide theoretical guarantees for such heuristic search-based deep RL algorithms. Recently, the adoption of MCTS (´ Swiechowski et al., 2023) in other learning settings has seen scaling advantages. For instance, in non-standard RL settings, like supervised learning systems (Guez et al., 2018; Wang et al., 2024a), constrained dynamical systems (Parthasarathy et al., 2023; Kureˇcka et al., 2024) to promote safe decision-making choices, and partially observable and constrained dynamical systems (Lee et al., 2018; Dam et al., 2022; 2020). In bandits, like agents taking decisions in the space of contexts (Ontan´on, 2013; Mao et al., 2020). In applications, like autonomous vehicles and robots, (Kartal et al., 2019; Yin et al., 2022) where the imitation of expert decisions plays a critical role. Alternative approaches include entropy regularization methods like MENTS (Xiao et al., 2019), RENTS and TENTS (Dam et al., 2021; 2024a), and Boltzmann-based approaches (Painter et al., 2023), though these rely on temperature parameters that may impede convergence to true optimal values. Inspired by such adoption of MCTS, we enable MCTS-based planning for the first time to the robust RL problem—equipped with theoretical guarantees—that accounts for mitigating dynamical model ambiguities.
Search-based planning for online robust RL. This line of research is closest to ours in terms of search-inspired algorithms. (Liu et al., 2022; Wang et al., 2023; Wang, 2024) introduces the Multi-Level Monte Carlo (MLMC) method (Heinrich, 2001; Giles, 2008) to approximate the robust Bellman backups. MLMC is another powerful statistical sampling method from the family of Monte Carlo estimators. However, they have the drawback of requiring random sampling procedures in each iteration of the robust RL planning stages for every state-action pair. By avoiding these pitfalls, MCTS adapts to the online sampling procedure by enabling search from a tree node—states and actions in dynamical systems—up to some constant depth in the tree. Other works introduce sampling-based Q-learning (Zhou et al., 2021; Liu et al., 2022; Wang et al., 2024b) and policy iteration (Panaganti and Kalathil, 2021; Kumar et al., 2023; Badrinath, 2023) inspired approaches. These are popular methods in standard online RL enabling trajectory-based updates—at current states, actions, and next states sampled with an updated policy—to approximate the Bellman backups. However, these require algorithmic and theoretical innovations–for e.g., function approximation architectures–for scaling up to high-dimensional dynamical systems (Panaganti et al., 2022; Zhang et al., 2023; Panaganti et al., 2024; Liu and Xu, 2024). The incorporation of the strong sampling procedure by MCTS avoids this issue.
3. Preliminaries
A Markov Decision Process (MDP) specified by the tuple ( S, A, P, R), where 
is the (potentially large) state space, A is a discrete action space, 
is the transition model mapping each state–action pair to a probability distribution over next states, and 
R is the (possibly uncertain) reward function assumed to be supported on a bounded interval 
. A stationary policy 
is defined as 
, meaning that at each discrete time step t, the agent observes a state 
, samples an action 
, collects a reward 
, and transitions to 
. We mention detailed notations used in this work in Table 3.
3.1. Value Functions and Policies
We adopt a discounted formulation with discount factor 
. The state-value and state–action value functions of a policy 
are given by 
The optimal state-value function is defined as  
By definition and existence of deterministic optimal actions, the optimal state–action value function 
satisfies 
for each 
3.2. Conceptualization of Robustness
A key challenge in real-world RL is that both transitions P and rewards R may be partially unknown or even timevarying. Let 
and 
denote the nominal transition probabilities and reward distributions, respectively, with each reward 
. These nominal models can be either factory-set approximations or a simulator of real-world systems. Following Wang et al. (2024b); Zhou et al. (2021); Liu et al. (2022), we allow the environment to deviate from 
within a robustness budget 
respectively. This leads to a robust MDP that accounts for uncertainties in both transitions and rewards.
Ambiguity Sets. We model transitions in an ambiguity set 
where each 
contains all plausi- ble distributions over next states from ( s, a). Analogously, an ambiguity set 
captures deviations in the reward distributions r( s, a). Here, with a chosen metric 
, 
Different choices of D lead to distinct ambiguity sets, such as total-variation balls ( 
), chi-squared neighborhoods ( 
), or Wasserstein sets ( 
). For notational convenience, we denote the reward distributions 
also as their probability densities in the context of measuring distances 
.
4. Main Problem Formulation
This section establishes how Monte Carlo Tree Search (MCTS) can be adapted to account for model ambiguity in a robust Markov Decision Process (MDP). Our goal is twofold: first, to clarify the root assumptions behind the robust planning framework, and second, to describe how MCTS is modified so that each node's value estimate incorporates worst-case rewards and transitions.
Robust MDP. We consider a robust MDP M = ( S, A, P, R) in which the state space S may be large or partially continuous, the action space A is discrete, and the unknown reward r( s, a) and transition model 
can lie within an ambiguity set R and P (described in Section 3). At each step t, the agent observes a state 
, selects an action 
, receives reward 
, and transitions to a new state 
. The robust state-value and state-action value functions of a policy 
are given by 
and 
respectively. A pol- icy 
that maximizes the value function is an optimal robust policy with corresponding optimal robust value functions 
and 
. Hence, both transitions and rewards may be adversarially perturbed, ensuring the agent plans robustly for worst-case scenarios within these sets.
Robust Bellman Operator. In the robust MDP, the worst-case expected value arises from an adversarial choice of both transition and reward distributions within their respective ambiguity sets. From the robust MDP literature (Iyengar, 2005; Liu et al., 2022), by the construction of P and R ambiguity sets, 
is known to be computable, and thereby 
.
Let us define for any set B and a vector  
Robust dynamic programming, given by 
and 
where 
, and 
captures the worst-case expected reward at ( s, a) and value of V over 
, converges to optimal robust value functions 
and 
respectively.
MCTS in a Robust MDP. In Monte Carlo Tree Search, we approximate a 
-discounted solution by simulating trajectories down a growing search tree. Each node corresponds to a state 
, with h indicating the depth in the tree (distance from the root). From 
, the algorithm either expands a child node for the next state 
or performs a rollout using a simpler policy 
if h reaches the maximum search depth H. Trajectories terminate upon reaching depth H or a terminal state.
Performance Measure. A canonical metric for MCTS algorithms is the convergence rate r( t), where t indexes the number of simulated trajectories (rollouts). Informally, r( t) bounds how quickly the MCTS estimates approach the true optimal values at the root node. For instance, one may require that 
or 
where 
is the action chosen at the root after t rollouts, and 
approximates 
.
Recursive Value Estimation Under Ambiguity. To capture the robust (worst-case) aspect of the MDP, we define a recursive estimation scheme at each node that accounts for 
of reward and 
transitions. Let 
be a node at depth h. We assign a robust value 
and a robust action-value 
such that 
At a leaf node ( h = H), we approximate the value with a simple rollout policy 
, yielding 
.
Goal of MCTS. Since finite sample sizes introduce noise, each node's robust value 
is estimated from rollouts. The ultimate objective is to identify an action 
at the root state 
within n simulated trajectories, where 
represents the robust-optimal action value. Intuitively, we want: 
with small statistical error. In Section 5, we describe how Robust-Power-UCT achieves this via specially designed backup operators and action-selection rules. Section 6 establishes finite-sample guarantees, showing that robustness in MCTS need not degrade convergence speed compared to its non-robust counterpart.
5. Algorithm Description
Robust-Power-UCT algorithm, focusing on the value backup and action selection strategies. Other details, such as the main loop and rollout procedure, are standard MCTS routines and hence only briefly mentioned.
Table 1: Key Conditions for Algorithmic Constants ( 
[0, H]) 
Value Backup. To estimate the value function at each node, we use a power mean backup operator. When node 
is expanded in the tree, we define inductively for all t, 
where 
. This power mean backup places more emphasis on actions that have high current value estimates (when p > 1), but still captures the contributions of other actions. Meanwhile 
, or simply 
as the root is 
, itself is updated via 
where 
is an empirical ro- bust reward at 
, and 
is a robust operator cap- turing worst-case transitions for ambiguity sets governed by empirical estimates of nominal reward and transition models: 
and 
Action Selection. At each node 
in the search tree,
Robust-Power-UCT selects an action a according to an optimistic rule that balances exploration and exploitation. 
Specifically, we maintain an empirical estimate 
for each action and add an exploration bonus of the form: 
where 
is the total number of visits to 
up to time t, and 
is how often action a has been taken from 
. The exponents 
and 
control how aggressively the algorithm explores, while C is a user-chosen constant. At the end of training (greedy mode), the action with the highest 
is chosen.
Main Loop and Rollout. As in standard MCTS, the algorithm repeatedly simulates from the root state 
, selecting actions according to the above scheme. When reaching a leaf node (unexpanded or maximum depth), a rollout policy approximates the return from that leaf. These routines are routine and can be implemented similarly to classical MCTS methods.
By combining an optimistic action selection mechanism with a power mean and robust operator for value backup, Robust-Power-UCT systematically balances exploration of uncertain actions and exploitation of promising ones, all under model ambiguity.
6. Theoretical Results
In robust MCTS planning, each internal node of the search tree can be viewed as a non-stationary multi-armed bandit due to ongoing updates of the node's reward and transition ambiguity estimates. At each step, the empirical evaluations shift, reflecting how robust exploration is balanced against uncertainty in the model. To handle this dynamic process, we begin by studying a non-stationary multi- armed bandit problem—focusing on how the power-mean backup operator concentrates around its robust-optimal value. We then leverage these results to prove convergence properties of our robust MCTS algorithm, showing that it systematically discards suboptimal branches under model uncertainty while maintaining sample efficiency.
6.1. Non-Stationary Bandit Perspective
We first analyze Robust-Power-UCT in a simpler non-stationary multi-armed bandit setting. Here, actions are selected optimistically, and the power mean backup operator is used at the root node.
6.1.1. PROBLEM DESCRIPTION AND KEY DEFINITIONS
We consider a class of non-stationary multi-armed bandit (MAB) problems with 
actions (arms) with the reward 
. Define a sequence of estimator 
(in this 
paper is the robustness estimation of the mean value of arm a) such that 
We are interested in sequence of estimators that satisfy a suitable concentration property:
Definition 1 (Concentration). A sequence of estimators 
concentrates at rate 
toward a limit Y , writing as 
, if there is a constant c > 0 such that 
ε > n 
c n 
ε 
.
Assumption 1 (Non-Stationary Rewards). For each arm 
, the sequence 
concentrates at rate 
toward a value 
, i.e. 
. Let  
, assumed to be unique with a strict gap from suboptimal 
.
6.1.2. OPTIMISTIC ACTION SELECTION AND POWER MEAN BACKUP
Under Assumption 1, we use an optimistic exploration rule similar to Robust-Power-UCT. Let 
be the number of times arm a is pulled before time n. The algorithm pulls each arm once initially. For n > K:   
By applying Theorem 1 of
Dam et al. (2024b), we get 
where  
, and 
.
Connecting Back to MCTS. This bandit analysis underpins how Robust-Power-UCT handles exploration and the power mean backup. In an MCTS context, each node's local bandit analysis is augmented by worst-case backups, but the principle is similar: the algorithm discards suboptimal branches with high probability, causing the robust estimates to concentrate around the best actions.
6.1.3. MAIN CONVERGENCE RESULTS
Before presenting the main result (Theorem 3), we first show an important lemma used for our MCTS algorithm. 
Lemma 17. For 
, let 
be a sequence of estimator satisfying 
, and there exists a constant L such that 
. Let 
be an iid sequence from a distribution 
with mean 
and 
be an iid sequence from a distribution 
sup- ported on { 1, ... , M}. Introducing the random variables 
. Define a model estimate of p as 
. We define an estimate of 
as 
Recall 
w.r.t 
and 
w.r.t 
. We define
the sequence of estimators 
Then with 
β, β > 1, 
R 
γσ 
.
Remark 1. This non-asymptotic convergence result shows that, for suitable parameters 
, the estimator 
will concentrate around the limiting quantity 
with high probability. Importantly, we do not claim these 
are in any sense optimal; rather, we only need the existence of such parameters that guarantee the concentration at the prescribed rate. Moreover, our analysis uses covering number generalization to handle continuous reward distributions. Furthermore, the constant c implicit in the notation 
can depend on problem-dependent factors (e.g., size of the action set A, number of states S, etc.), reflecting the stochastic process complexity.
6.2. Tree-Level Convergence
The above non-stationary bandit analysis is critical for proving the subsequent tree-level theorems. In particular, Theorem 2 (restated below) shows that under appropriate parameter settings (Table 1), the estimated node values 
and 
converge at a known rate:
Theorem 2. When applying Robust-Power-UCT with parameters 
satisfying Table 1: 
(ii) For any node 
at depth 
, 
Proof. (Sketch) The argument proceeds by induction on the tree depth H. For H = 1, we handle the root node using Lemma 17 plus the concentration assumptions on leaf nodes. For general H, we note that descending into a child node effectively reduces the depth by one, thus the induction hypothesis applies. By carefully controlling exploration (Section 5) and using robust backups, each node's 
and 
estimates concentrate at the specified rates.
Finally, Theorem 3 establishes that under optimal parameter tuning, the expected payoff at the root converges at 
.
Theorem 3. (Convergence of Expected Payoff) At the root node 
, there is a choice of parameters yielding  
Robust-Power-UCT and standard (non-robust) MCTS achieve the same 
rate for value estimation at the root node, which implies that robustness need not affect convergence speed, which is order-optimal. While we achieve this rate, the exact dependence on various problem-dependent factors (e.g., number of actions A, number of states S, tree search depth H, etc.) is not decodable (thereby not comparable to other online robust RL results (Dong et al., 2022)) due to our analysis limitations.
7. Experiments
We evaluate Robust-Power-UCT in three distinct environments designed to test different aspects of robust planning: the Gambler's Problem, Frozen Lake, and American Option Pricing. For each environment, we compare: Stochastic-Power-UCT (Dam et al., 2024b) (baseline) and Robust-Power-UCT with Total Variation, Chi-squared, and Wasserstein ambiguity sets.
While several robust reinforcement learning methods exist (c.f.Section 2), to the best of our knowledge, this is the first work to incorporate ambiguity sets directly into MCTS, making Stochastic-Power-UCT our primary baseline. All experiments are done over 100 seeds, using 
and robustness budget 
, with these values showing consistent performance across preliminary experiments with different parameter settings. For concise presentation, we only experiment with transition model ambiguity just as prior robust RL works.
Full experimental details, environment descriptions and hyperparameter configurations are provided in Appendix.E.1, along with an additional analysis of the robustness budget. We also provide our code at https://github.com/ brahimdriss/RobustMCTS.
Remark 3. While the robust Bellman operator involves solving a minimization problem over probability distributions, we can leverage dual reformulations to make its computation tractable. Many prior works (Iyengar, 2005; Nilim and El Ghaoui, 2005; Xu et al., 2023) show, for a value function V and nominal distribution 
, the robust value under all ambiguity balls with radius 
can be computed in at most O( S log( S)) time. Thus requiring only marginally more computation than standard Bellman operators O( S). This computational efficiency is crucial for practical implementations, particularly in online planning settings like MCTS with frequent Bellman updates.
7.1. Gambler's Problem Robustness Results
The Gambler's Problem provides an ideal testbed for evaluating robustness to model misspecification. An agent must reach a target capital through a series of bets, with each 
Figure 1: Success rates in the Gambler's Problem under model mismatch. Results show planning with fixed probabilities 
while executing across different probabilities. Shaded area demonstrates how robust methods maintain more consistent performance under model mismatch compared to Stochastic-Power-UCT.
bet winning with probability 
. This enables precise control of the planning-execution mismatch through a single parameter.
Figure 1 illustrates the performance of different PowerUCT variants under model mismatch in the Gambler's Problem. The behavior of Stochastic-Power-UCT reveals a fundamental vulnerability: when 
, there exist multiple optimal policies that achieve winning ratios close to the true environment probability. However, when planning with 
, the algorithm converges to an aggressive single-bet strategy that fails catastrophically when the true probability is lower than assumed.
The superior performance of robust variants stems from their conservative betting strategies. While Stochastic-Power-UCT often makes large single bets, robust variants tend to make smaller, sequential bets that preserve capital for future opportunities.
7.2. Frozen Lake Robustness Results
The Frozen Lake environment tests robustness in a different complex setting where uncertainties compound over multiple steps. The agent must navigate to a goal while avoiding hazards, with actions potentially failing with probability 
.
Table 2 provides detailed success rates across different planning and execution probabilities. With matching conditions (4000 rollouts and 
case), our results closely match those reported in the original paper (Dam et al., 2024b) even with slightly different dynamics. The Wasserstein uncertainty set exhibits superior performance in scenarios with lower execution probabilities, achieving the highest success rates (bold) across multiple conditions. For example, with 
, it achieves 58% success when 
, significantly outperforming other ap-
proaches.
Both Wasserstein and Chi-squared variants outperform the baseline Stochastic-Power-UCT and Total Variation approaches. Interestingly, when planning and execution probabilities align (underlined values), both robust variants maintain superior performance compared to standard approaches. This suggests that explicitly accounting for uncertainty in the planning process provides benefits even without model mismatch, possible by encouraging more conservative and reliable decision-making strategies.
These results on Gambler's Problem and Frozen Lake demonstrate that explicitly accounting for model ambiguity during planning can significantly improve reliability when deployment conditions differ from simulation assumptions. The choice of ambiguity set provides a mechanism for balancing conservatism against nominal performance.
7.3. American Option Robustness Results
The American Option environment provides a financial domain to test reward robustness under model uncertainty. In this setting, the agent must decide when to exercise an option to maximize expected returns, with the key uncertain parameter being the probability 
of price increases at each time step.
Figure 2 demonstrates the reward robustness of different Power-UCT variants under model mismatch in option pricing scenarios. We examine two planning scenarios: training with 
(left panel) and 
(right panel), then testing across execution probabilities from 0.4 to 0.8.
The results reveal that robust variants maintain significantly more stable performance compared to standard PowerUCT. When planning with 
, the standard approach shows dramatic performance degradation as the test probability deviates from the planning assumption, dropping 
Figure 2: Reward robustness comparison in American Option pricing under model mismatch. Results show planning with fixed price-up probabilities 
while testing across different probabilities. Robust variants maintain significantly more stable performance compared to standard Power-UCT, demonstrating consistent risk-averse behavior that is particularly valuable in financial decision-making contexts where reliability is crucial. 
Table 2: Success rates (%) for planning with Power-UCT variants. Methods: Stochastic-Power-UCT (Sp), Robust version with Total Variation (Tv), Chi-squared (Cs), and Wasserstein (Ws) ambiguity sets. Underlined values indicate matching planning and execution 
. Bold indicates highest success rate per planning scenario.
from approximately 5 to near 0 when 
. In contrast, robust variants maintain consistent performance across the entire range.
When planning with 
, standard Power-UCT exhibits extreme sensitivity with dramatically varying performance. The robust variants demonstrate desired risk-averse behavior: achieving conservative but stable returns across all conditions. This stability is especially valuable in financial contexts where consistent performance is preferred over potentially high but unreliable returns.
The Wasserstein and Chi-squared ambiguity sets show particularly strong performance, maintaining steady rewards even under significant model mismatch, demonstrating that explicitly accounting for uncertainty leads to policies inherently more robust to different deployment conditions.
8. Conclusions
We have developed a robust variant of Monte Carlo Tree Search (MCTS) that addresses dynamical model and reward distribution ambiguities, bridging the gap between simulation-based planning and real-world deployment. The dependence of MCTS-based algorithms' convergence rates on parameters (states S, actions A, depth H) remains underexplored in standard RL. We will address this gap for both robust and non-robust setups in the future. As our formulation follows an overly conservative mathematical framework, in the future, we will explore alternative robust formulations that are more permeable to less conservative solutions to address the simulation-to-reality gap.
Impact Statement
This paper presents a novel algorithm for the robust reinforcement learning field using the Monte Carlo Tree Search planning mechanism. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.
Acknowledgments
Tuan Dam was funded by Hanoi University of Science and Technology (HUST) under Project No. T2024-TD-024. K. Panaganti acknowledges support from the Resnick Institute and the 'PIMCO Postdoctoral Fellow in Data Science' fellowship at Caltech. B. Driss was funded by the project ANR-23-CE23-0006. A. Wierman acknowledges support by the NSF through CNS-2146814, CPS-2136197, CNS-2106403, and NGSDI-2105648. This work was granted access to the HPC resources of IDRIS under the allocation 2024-AD011015599 made by GENCI.
References
Kishan Panaganti Badrinath. Robust Reinforcement Learning: Theory and Algorithms. PhD thesis, Texas A&M University, 2023.
Noam Brown and Tuomas Sandholm. Superhuman ai for heads-up no-limit poker: Libratus beats top professionals. Science, 359(6374):418–424, 2018.
Imre Csisz´ar. Eine informationstheoretische ungleichung und ihre anwendung auf den beweis der ergodizit¨at von markoffschen ketten. A Magyar Tudom´anyos Akad´emia Matematikai Kutat´o Int´ezet´enek K¨ozlem´enyei, 8(1-2):85– 108, 1963.
Tuan Dam, Pascal Klink, Carlo D'Eramo, Jan Peters, and Joni Pajarinen. Generalized mean estimation in monte-carlo tree search. In Christian Bessiere, editor, Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, IJCAI-20, pages 2397– 2404. International Joint Conferences on Artificial Intelligence Organization, 7 2020. doi: 10.24963/ijcai.2020/ 332. URL https://doi.org/10.24963/ijcai. 2020/332. Main track.
Tuan Dam, Georgia Chalvatzaki, Jan Peters, and Joni Pa- jarinen. Monte-carlo robot path planning. IEEE Robotics and Automation Letters, 7(4):11213–11220, 2022.
Tuan Dam, Carlo D'Eramo, Jan Peters, and Joni Pajari- nen. A unified perspective on value backup and exploration in monte-carlo tree search. Journal of Artificial Intelligence Research, 81:511–577, 2024a.
Tuan Dam, Odalric-Ambrym Maillard, and Emilie Kaufmann. Power mean estimation in stochastic monte-carlo tree search. In Negar Kiyavash and Joris M. Mooij, editors, Proceedings of the Fortieth Conference on Uncertainty in Artificial Intelligence, volume 244 of Proceedings of Machine Learning Research, pages 894–918. PMLR, 15–19 Jul 2024b. URL https://proceedings.mlr. press/v244/dam24a.html.
Tuan Q Dam, Carlo D'Eramo, Jan Peters, and Joni Pajarinen. Convex regularization in monte-carlo tree search. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th International Conference on Machine Learning, volume 139 of Proceedings of Machine Learning Research, pages 2365–2375. PMLR, 18–24 Jul 2021. URL https://proceedings.mlr.press/ v139/dam21a.html.
Jing Dong, Jingwei Li, Baoxiang Wang, and Jingzhao Zhang. Online policy optimization for robust mdp. arXiv preprint arXiv:2209.13841, 2022.
Nicolas Fournier and Arnaud Guillin. On the rate of con- vergence in wasserstein distance of the empirical measure. Probability theory and related fields, 162(3):707– 738, 2015.
Rui Gao and Anton Kleywegt. Distributionally robust stochastic optimization with wasserstein distance. Mathematics of Operations Research, 48(2):603–655, 2023.
Michael B Giles. Multilevel monte carlo path simulation. Operations research, 56(3):607–617, 2008.
Arthur Guez, Th´eophane Weber, Ioannis Antonoglou, Karen Simonyan, Oriol Vinyals, Daan Wierstra, R´emi Munos, and David Silver. Learning to search with mctsnets. In International conference on machine learning, pages 1822–1831. PMLR, 2018.
Stefan Heinrich. Multilevel monte carlo methods. In Large-Scale Scientific Computing: Third International Conference, LSSC 2001 Sozopol, Bulgaria, June 6–10, 2001 Revised Papers 3, pages 58–67. Springer, 2001.
Carl-Johan Hoel, Katherine Driggs-Campbell, Krister Wolff, Leo Laine, and Mykel J Kochenderfer. Combining planning and deep reinforcement learning in tactical decision making for autonomous driving. IEEE transactions on intelligent vehicles, 5(2):294–305, 2019.
Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005.
Leslie Pack Kaelbling, Michael L Littman, and Andrew W Moore. Reinforcement learning: A survey. Journal of artificial intelligence research, 4:237–285, 1996.
Bilal Kartal, Pablo Hernandez-Leal, and Matthew E Tay- lor. Action guidance with mcts for deep reinforcement learning. In Proceedings of the AAAI conference on artificial intelligence and interactive digital entertainment, volume 15, pages 153–159, 2019.
Behbod Keshavarzi and Hamidreza Navidi. Comparative analysis of extensive form zero sum game algorithms for poker like games. Scientific Reports, 15(1):2917, 2025.
Levente Kocsis and Csaba Szepesv´ari. Bandit based monte-carlo planning. In European conference on machine learning, pages 282–293. Springer, 2006.
Navdeep Kumar, Esther Derman, Matthieu Geist, Kfir Y Levy, and Shie Mannor. Policy gradient for rectangular robust markov decision processes. Advances in Neural Information Processing Systems, 36:59477–59501, 2023.
Martin Kureˇcka, V´aclav Nevyhoˇstˇeny, Petr Novotny, and V´ıt Unˇcovsk`y. Threshold uct: Cost-constrained monte carlo tree search with pareto curves. arXiv preprint arXiv:2412.13962, 2024.
Jongmin Lee, Geon-Hyeong Kim, Pascal Poupart, and Kee-Eung Kim. Monte-carlo tree search for constrained pomdps. Advances in Neural Information Processing Systems, 31, 2018.
Edouard Leurent. rl-agents: Implementations of reinforcement learning algorithms. https://github. com/eleurent/rl-agents, 2018.
Zhishuai Liu and Pan Xu. Distributionally robust offdynamics reinforcement learning: Provable efficiency with linear function approximation. In International Conference on Artificial Intelligence and Statistics, pages 2719–2727. PMLR, 2024.
Zijian Liu, Qinxun Bai, Jose Blanchet, Perry Dong, Wei Xu, Zhengqing Zhou, and Zhengyuan Zhou. Distributionally robust q-learning. In International Conference on Machine Learning, pages 13623–13643. PMLR, 2022.
Weichao Mao, Kaiqing Zhang, Qiaomin Xie, and Tamer Basar. Poly-hoot: Monte-carlo planning in continuous space mdps with non-asymptotic analysis. Advances in Neural Information Processing Systems, 33:4549–4559, 2020.
Arnab Nilim and Laurent El Ghaoui. Robust control of markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005.
Santiago Ontan´on. The combinatorial multi-armed bandit problem and its application to real-time strategy games. In Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, volume 9, pages 58–64, 2013.
Michael Painter, Mohamed Baioumy, Nick Hawes, and Bruno Lacerda. Monte carlo tree search with boltzmann exploration. Advances in Neural Information Processing Systems, 36:78181–78192, 2023.
Kishan Panaganti and Dileep Kalathil. Robust reinforce- ment learning using least squares policy iteration with
provable performance guarantees. In International Conference on Machine Learning, pages 511–520. PMLR, 2021.
Kishan Panaganti and Dileep Kalathil. Sample complex- ity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics, pages 9582–9602. PMLR, 2022.
Kishan Panaganti, Zaiyan Xu, Dileep Kalathil, and Mo- hammad Ghavamzadeh. Robust reinforcement learning using offline data. Advances in Neural Information Processing Systems (NeurIPS), 2022.
Kishan Panaganti, Adam Wierman, and Eric Mazumdar. Model-free robust 
-divergence reinforcement learning using both offline and online data. ICML, arXiv preprint arXiv:2405.05468, 2024.
Kishan Panaganti, Zaiyan Xu, Dileep Kalathil, and Mo- hammad Ghavamzadeh. Bridging distributionally robust learning and offline rl: An approach to mitigate distribution shift and partial data coverage. Learning for Dynamics and Control Conference, 2025.
Dinesh Parthasarathy, Georgios Kontes, Axel Plinge, and Christopher Mutschler. C-mcts: Safe planning with monte carlo tree search. arXiv preprint arXiv:2305.16209, 2023.
Hamed Rahimian and Sanjay Mehrotra. Distributionally robust optimization: A review. arXiv preprint arXiv:1908.05659, 2019.
Erica Salvato, Gianfranco Fenu, Eric Medvet, and Fe- lice Andrea Pellegrino. Crossing the reality gap: A survey on sim-to-real transferability of robot controllers in reinforcement learning. IEEE Access, 9:153171–153187, 2021.
Julian Schrittwieser, Ioannis Antonoglou, Thomas Hu- bert, Karen Simonyan, Laurent Sifre, Simon Schmitt, Arthur Guez, Edward Lockhart, Demis Hassabis, Thore Graepel, et al. Mastering atari, go, chess and shogi by planning with a learned model. Nature, 588(7839):604– 609, 2020.
Devavrat Shah, Qiaomin Xie, and Zhi Xu. Nonasymptotic analysis of monte carlo tree search. In Abstracts of the 2020 SIGMETRICS/Performance Joint International Conference on Measurement and Modeling of Computer Systems, pages 31–32, 2020.
Laixi Shi and Yuejie Chi. Distributionally robust model- based offline reinforcement learning with near-optimal sample complexity. Journal of Machine Learning Research, 25(200):1–91, 2024.
David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of go with deep neural networks and tree search. nature, 529(7587):484, 2016.
Richard S Sutton and Andrew G Barto. Reinforcement learning: an introduction, 2nd edn. adaptive computation and machine learning, 2018.
Maciej ´Swiechowski, Konrad Godlewski, Bartosz Sawicki, and Jacek Ma´ndziuk. Monte carlo tree search: A review of recent modifications and applications. Artificial Intelligence Review, 56(3):2497–2562, 2023.
Mark Towers, Ariel Kwiatkowski, Jordan Terry, John U Balis, Gianluca De Cola, Tristan Deleu, Manuel Goul˜ao, Andreas Kallinteris, Markus Krimmel, Arjun KG, et al. Gymnasium: A standard interface for reinforcement learning environments. arXiv preprint arXiv:2407.17032, 2024.
Jie Wang, Rui Gao, and Yao Xie. Regularization for adversarial robust learning. arXiv preprint arXiv:2408.09672, 2024a.
Shengbo Wang, Nian Si, Jose Blanchet, and Zhengyuan Zhou. A finite sample complexity bound for distributionally robust q-learning. In International Conference on Artificial Intelligence and Statistics, pages 3370–3398. PMLR, 2023.
Shengbo Wang, Nian Si, Jose Blanchet, and Zhengyuan Zhou. Sample complexity of variance-reduced distributionally robust q-learning. Journal of Machine Learning Research, 25(341):1–77, 2024b.
Yudan Wang. Model-free robust reinforcement learning with sample complexity analysis. Master's thesis, State University of New York at Buffalo, 2024.
Chenjun Xiao, Ruitong Huang, Jincheng Mei, Dale Schuurmans, and Martin M¨uller. Maximum entropy monte-carlo planning. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alch´e-Buc, E. Fox, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019. URL https://proceedings.neurips. cc/paper_files/paper/2019/file/
7ffb4e0ece07869880d51662a2234143-Paper. pdf.
Zaiyan Xu, Kishan Panaganti, and Dileep Kalathil. Im- proved sample complexity bounds for distributionally robust reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 9728–9754. PMLR, 2023.
Zhao-Heng Yin, Weirui Ye, Qifeng Chen, and Yang Gao. Planning for sample efficient imitation learning. Advances in Neural Information Processing Systems, 35: 2577–2589, 2022.
Runyu Zhang, Yang Hu, and Na Li. Regularized robust mdps and risk-sensitive mdps: Equivalence, policy gradient, and sample complexity. arXiv preprint arXiv:2306.11626, 2023.
Zhengqing Zhou, Zhengyuan Zhou, Qinxun Bai, Linhai Qiu, Jose Blanchet, and Peter Glynn. Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 3331–3339. PMLR, 2021.
A. Notations
Table 3: Key Notations Used in the Appendix. Symbols and definitions for uncertainty sets (TV, 
, Wasserstein), reward distributions, and the main variables in robust MDP analysis.
B. Useful technical results
Lemma 1. (Lemma 1 (Panaganti and Kalathil, 2022)) For any 
and for any 
, we have 
and 
Lemma 2. (Proposition 2 (Xu et al., 2023)) Fix any 
. For any 
, we have with the probability of at least 
From Lemma 2, we have 
so that
Lemma 3. (Proposition 4 (Xu et al., 2023)) Fix any 
. For any 
, we have with the probability of at least 
Then we have 
Set 
with   
, then 
Lemma 4. (Proposition 9 (Xu et al., 2023)) Fix any 
. For any 
, we have with the
probability of at least  
Similarly, Set 
with   
ρ p θδ  
, then 
so that
Lemma 5. (Lemma 2 (Fournier and Guillin, 2015), Concentration inequality for Wasserstein distance ). For 
, we consider an i.i.d. sequence 
of 
-distributed random variables and, for all 
, the empirical measure 
Assume that there exists 
such that 
. Then for all 
, all x > 0, 
where the Wasserstein distance 
is defined by
and the positive constant C and c depends only on 
and 
.
Lemma 6. (Lemma 4 (Zhou et al., 2021)). Let 
be a random variable with 
, and 
denotes its empirical distribution of sample size n. For 
, for any 
(1) 
. Furthermore, assume that the support of X is finite. Then there exists a constant 
, such that 
, with probability at least 
, we have 
(2) 
. Then there exists a constant 
, such that for any 
, with probability at least 
, there exists a 
such that 
, where 
is independent of n and 
.
The Total Variation, Chi-square, and Kullback-Liebler uncertainty sets are constructed with the f-divergence. The f divergence between the distributions P and 
is defined as 
where f is a convex function (Csisz´ar, 1963). We obtain different divergences for different forms of the function f, including some well-known divergences. For example, 
gives Total Variation, 
gives chi-square, and f( t) = t log( t) gives Kullback-Liebler.
Lemma 7. (Lemma 5 (Panaganti et al., 2022)) Let 
be as defined in equation 18 with 
corresponding to the TV uncertainty set. Then, 
Lemma 8. (Covering number (TV)). Given a reward function 
, let 
. Fix any 
. Denote 
where 
. Then 
is a 
-cover for 
with respect to 
, and its cardinality is bounded as  
. Furthermore, for any 
, we have 
.
Proof. First, 
is the minimal number of subintervals of length 
needed to cover 
. Denote  ![(i − 1)θ, iθ)
to be the i-th subinterval, 
. Fix some 
. Then 
. Without loss of generality, assume this particular 
. Let 
. Now, for any 
, 
where (a) follows from 
and the fact that 
, if x > y. Taking maximum with respect to s, a on both sides, we get 
. Since 
, this suggests 
is a 
-cover for 
. The cardinality bound directly follows from 
where the last inequality is due to 
. Now, for any 
, we can establish the following 
where the inequality is element-wise.
Lemma 9. Fix any 
. Fix any reward function 
. Let 
be the 
-cover of  
as described in Lemma 8 . We then have 
Proof. For any 
, there exists 
such that 
. Now for such particular 
and r, we have 
Taking maximum over 
on both sides, we get 
Now note that by the definition of 
, we have 
The desired result directly follows.
Lemma 10. Consider the total-variation uncertainty set
Let 
and 
be the robust rewards defined using the empirical estimate 
and 
and respectively. Then there exists a constant 
such that for all 
(i.e. a sufficiently large number of reward samples at ( s, a), the following holds with probability at least 
: 
Proof. Following similar analyses as in Proposition 2 (Xu et al., 2023) (Lemma.2), we get 
where ( a) follows from the fact that 
. For (b), recall that 
for any 
. Hence, the term 
is always non-negative for 
, which cancels out by linearity of the expectation. (c) follows from applying Lemma 9 to the first term. Recall that all 
is upper bounded by 
. Now we can apply Hoeffding's inequality to the first term in equation 26:  
and recall that 
from Lemma 8. We have 
Applying a union bound over 
, we get
with probability at least 
. Now we can also apply Hoeffding's inequality to the second term in equation 26. Recall that any reward function is bounded by 
. We have 
with probability at least 
. Combining equation 26 - equation 28 completes the proof. 
From Lemma 10, we have 
so that
Lemma 11. (Lemma 9 (Panaganti et al., 2022)) Let 
be defined as in equation 18 with the convex function f( t) = 
corresponding to the Chi-square uncertainty set. Then 
Lemma 12. Fix any 
. For any 
and 
, we have, with probability at least 
, we can find a constant 
such that 
, we have 
Proof. Similar to Lemma 10, the result is direct by applying the results of Lemma 9, Lemma 11 and the law of total probability.
From the results of Lemma 12, Then we have 
Set 
with   
, then 
Lemma 13. Consider an MDP with the Wasserstein distance 
. Fix any 
, we can derive 
Proof. Fix any 
. We have
where ( a) follows from ((Gao and Kleywegt, 2023) Theorem 1). For ( b), let us first denote any optimizer in ( a) to be 
. Observe that since R is non-negative, it follows that 
where in the last inequality we use that the distance metric satisfies d( R, R) = 0, for any 
. 
Lemma 14. (Covering number (Wasserstein)). Consider the following set of 
vectors: 
Let
where 
and 
. Then 
is a 
-cover of 
with respect to 
,
and its cardinality is bounded as 
. Furthermore, for any 
, we have  
Proof. Fix any 
. First note that 
is the minimal number of subintervals of length 
needed to cover 
. Denote   
. Fix some 
. Then 
must takes the form 
for some 
. Without loss of generality, assume 
. Now we pick 
Fix any 
and 
, we have 
where ( a) is due to 
. Taking maximum over 
on both sides, we get 
. Since 
, this suggests that 
is a 
-cover for 
. To bound the cardinality of 
, we consider two cases. If 
, then 
and 
On the other hand, if 
, then since 
, we have
Hence, we have 
. Now we prove the last claim. Fix any 
. Note that for any 
, 
The result then follows from taking maximum over 
on both sides.
Lemma 15. Fix any 
. Let 
be the 
-cover of the set 
as described in Lemma 14. We then have 
Proof. The proof is identical to the proof of Lemma 9.
Lemma 16. Fix any 
. For any 
and 
, we have the following inequality with probability at least  
Proof. From Lemma 13 , we have 
Now it follows that
where ( a) follows from 
. (b) follows from Lemma 15. Recall that all 
is bounded by 
. Now we can apply Hoeffding's inequality: 
Now recall that 
and choose 
We then have 
Finally, applying a union bound over 
, we get
with probability at least 
. Combining the above and equation 41 completes the proof. 
Similarly, Set 
with  
, then 
= 
2 
2 
(42) 
4 (2 
2 
exp 
so that
C. Convergence of Robust-Power-UCT Multi-armed bandits
Lemma 17. For 
, let 
be a sequence of estimator satisfying 
, and there exists a constant L such that 
. Let 
be an iid sequence from a distribution 
with mean 
and 
be an iid sequence from a distribution 
supported on { 1, ... , M}. Introducing the random variables  
. Let us study a random vector 
. We define an estimate of 
as 
where 
is a point mass at 
. And define 
w.r.t 
and 
w.r.t 
. We define the sequence of estimator 
Then with 
β, β > 1, 
R 
γσ 
.
Proof. Let 
where 
is the 
-dimensional simplex. Without loss of generality, we assume that 
for all m. Let us define 
. Let  
is the number of times that population i was observed. We have  
. Therefore, 
To upper bound A, 
To upper bound B, let us consider 
. Then, 
By applying results from Lemma 2 and Equation 8, we obtain
For 
, as the result from Lemma 1, we have 
Therefore, 
Therefore, 
In both three cases, that leads to 
with 
depends on 
. Here we need
to argue that 
. Therefore, with 
, 
Furthermore,
so that, lim 
This means 
which concludes the proof.
D. Convergence of Robust-Power-UCT n Monte-Carlo Tree Search
Theorem 1. (Theorem 1 of Dam et al. (2024b)) For each arm 
, let 
and define 
. Suppose arms are selected according to equation 4 with parameters 
, and let ![p ∈ 1, ∞)
. If 
, and α 
, or p > 2, 0 < α 
< 1,
and α 
b < α,
then there exists a suitable constant C (depending on 
) such that 
where ∆ 
), 
1) 
, and 
1).
Theorem 2. When applying Robust-Power-UCT with parameters 
, and 
satisfying Table 1:
(i) For any node 
at depth 
, 
(ii) For any node 
at depth 
,
Proof. We follow the proof technique of Dam et al. (2024b, Theorem 2).
Base Case ( H = 1). Consider the root node 
. Each time we visit 
, we collect:
•
A reward sample 
from the reward distribution 
, which then leads to evaluating 
and  
, thus approximates the worst-case reward at 
.
•
A next state 
from 
possible states (denote such states as 
). This then leads to 
, and captures the worst-case value from the transition ambiguity set 
.
By definition of the robust Bellman backup, recall
Since H = 1, the next state 
is treated as a leaf. We approximate 
, i.i.d. rollout returns under the policy 
. By standard concentration bounds (e.g., Hoeffding), we obtain for all child nodes 
: 
Next, recall by equation 3: 
Here 
is the estimated value at all child nodes 
. By Lemma 17 and equation 77, it follows that 
Since 
is the root node, we perform the power-mean backup on 
: 
Under Theorem 1 (from Dam et al. (2024b) for robust settings), we conclude 
This establishes both points (i) and (ii) at depth 0 and confirms the result for H = 1.
Inductive Step ( H > 1). Assume the theorem holds for all search trees up to depth 
. We now add one more level to create a tree of depth H. Let 
be a child of the new root 
. Then 
itself is a root of a subtree with depth 
. By the inductive hypothesis: 
At the new root 
, we repeat the argument used in the base case:
•
Observing rewards 
from 
.
•
Transitioning under 
to state 
.
Hence, Lemma 17 again implies 
and the power-mean operator at 
yields 
Thus, depth H inherits the same concentration property from depth 
. This completes the inductive argument, establishing statements (i) and (ii) for any node at any depth 
. 
Theorem 3. (Convergence of Expected Payoff) At the root node 
, there is a choice of parameters yielding 
Proof. By Jensen's inequality (convexity of | x|), we obtain 
=   
Next, we split this integral at 
. Using the concentration property 
, we have 
for 
. Hence,
Because 
(see Theorem 1), the dominant term is 
. Thus, 
E. Experimental setup and Parameters selection
E.1. Experimental setup
All experiments are done over 100 seeds, using 
and robustness budget 
, with these values showing consistent performance across preliminary experiments with different parameter settings. We use 2000 rollouts for The Gambler's Problem and 4000 rollouts for Frozen Lake.
We implement our robust MCTS framework by extending a base Monte Carlo Tree Search implementation from (Leurent, 2018). Our codebase adds Stochastic Power UCT and introduces new robust backup operators for handling different uncertainty sets (Total Variation, Chi-squared, and Wasserstein), while maintaining the core MCTS selection and expansion strategies. We also provide our code at https://github.com/brahimdriss/RobustMCTS.
E.2. Environments
The Gambler's Problem (Sutton and Barto, 2018): a classic casino-inspired reinforcement learning environment where an agent starts with an initial capital and aims to reach a specific goal amount through a series of betting decisions. In our implementation, the agent begins with 50 units of capital and must reach a goal of 100 units to win. At each step, the agent can bet any amount up to its current capital. The environment has a win probability 
for each bet, where the agent either wins the wagered amount with probability 
or loses it with probability 
. The state space consists of all possible integer capital amounts from 0 to 100, with 0 and 100 being terminal states. The action space at each state includes all possible integer bets up to the current capital. This environment is particularly suitable for studying decision-making under uncertainty as it combines both risk management and optimal stopping aspects.
In our experiments, to reduce computational complexity while maintaining the same fundamental dynamics and challenges, we scaled down the problem to use a starting capital of 5 units and a goal of 10 units. This smaller scale version preserves all the essential characteristics and decision-making complexity of the original problem.
Frozen Lake(Towers et al., 2024): This environment presents a gridworld navigation challenge where an agent must traverse a 4x4 frozen surface from a starting position to a goal while avoiding holes. The surface is slippery, introducing stochastic dynamics where the agent's intended actions may result in sliding to adjacent states with some probability. The state space consists of 16 discrete states representing different positions on the grid, with some states marked as holes (H) and one goal state (G). The action space includes four possible movements: left, right, up, and down. When the agent executes an action, it moves in the intended direction with probability 1/3 and slides perpendicular to the intended direction (left or right) with probability 2/3, making the environment highly stochastic. This environment is particularly valuable for evaluating robust policies as it combines both navigational planning and uncertainty in action outcomes.
In our experiments, we define 
as the probability that the executed action differs from the agent's selected action. When a slip occurs, the actual executed action is sampled uniformly at random, effectively modeling the uncertain dynamics of the frozen surface.
E.3. Robust Performance Results
We investigate the impact of uncertainty budgets on agent performance in a modified gambler's problem. In this experiment, we fix the planning probability 
at 0. 6 , the ambiguity set at Wasserstein. The agent's robustness is evaluated across different uncertainty budgets 
0.1, 0.3, 0.5, 0.7, 0.9}, where higher values of 
correspond to more conservative policies. For each uncertainty budget, we assess the agent's performance by varying the execution probability from 0.2 to 0.8, thus testing the policy's robustness to model misspecification. This experimental design allows us to analyze how different levels of conservatism (controlled by the uncertainty budget) affect the agent's ability to maintain performance when faced with discrepancies between planning and execution environments.
Figure 3 demonstrate a clear trade-off between performance and robustness across different uncertainty budgets. Agents with lower uncertainty budgets ( 
ceeds the planning probability, but their success rate drops significantly in misspecified environments. In contrast, higher uncertainty budgets ( 
maintaining better success rates when the execution probability is lower than the planning probability. This suggests that while conservative policies might not achieve optimal performance in well-specified environments, they provide better robustness to model misspecification. The moderate uncertainty budget ( 
0.5) appears to offer a balanced trade-off, maintaining reasonable performance across both regimes.
We now investigate a wide range of transition model ambiguities for the Frozen Lake environment. Table 4 provides an extended version of Table 2 with detailed success rates across different planning and execution probabilities. We observe that the performance of Stochastic-Power-UCT algorithm degrades faster for increased noise injection for slipping probabilities 
. We again see Wasserstein robust MCTS does well across all planning versus execution phases. All robust MCTS variants outperform the baseline.
Finally, our experiments reveal that the Wasserstein robust MCTS algorithm showcases the most robust performance across all variants. It might be of independent interest for future research to give a theoretical understanding of this phenomenon. 
Figure 3: Performance comparison across different uncertainty budgets ( 
). Planning probability is fixed at 
(vertical dashed line), while execution probability varies from 0.2 to 0.8. Higher uncertainty budgets lead to more conservative policies, showing improved robustness when 
but potentially reduced performance when 
. 
Table 4: Success rates (%) for planning with Power-UCT variants. Methods: Stochastic-Power-UCT (Sp), Robust version with Total Variation (Tv), Chi-squared (Cs), and Wasserstein (Ws) ambiguity sets. Underlined values indicate matching planning and execution 
. Bold indicates highest success rate per planning scenario.
Bytez.com - Designed for Accessibility and to further Open Science Send feedback
0cAFcWeA7fkwj0zxQHOO6qfzuL-1iGdDr2kyk7aPUFZfNcHxFO_LvyPsAwiqtSaAaSktCBGFFYAnSEfPGyRLUwEEHPWVz0MKBEytx880WQKM9dfcirQtyN0UVrRLoHzC5qpich32HARt11ydd9sf75OMW_7aU6Tg5o9y0sEnje0BFAZeL0qROFZ9pVu9fbtLiI8bHAontYGg3SJWTAGNPGSthOklFeYbTy-0O9-hSL47A6tNPgqqQW8a5P2_TobefQ07eiF71WRVCDwHXKqtnURVtDp-iRKayyYdxTyMhtRrQlNRjME2sVQopeiBN7aP5Dz7wMeSITUE0BR3IvLG3tzcN14VwOIiZaPzHm5Spp4Pn_c20XF_dEExew7b0LfvGwsP5JqM9KDbvGCD0iri2VwXVbTDT_XvH25rfR8rSMyWj3SQ8vRBQF889-2oPzcJ22mtUb4WgyiwtoHOCtZD4TJ7w0t2UMYCzp8aUvx9bpaeU4CkxLjM4B4T3GxR2VjFFrYFksNPmeaOaMX0ApONYEGkaxfdKW1bQqMPJUsuS5ClBHwZk_FjoMGYXadNfBhAwQv4ctow_yST1TtC49a0sLuCHDqXwQepBqul2JqXD8au2bROe0zwXSpPDdyYWTgFc0WXh6tk9nWlDJ9iPH4_rG3m4LIoGZZC-_mJrnauQHJ7HVSrTVN6JMXgDi-kTllDcnPZn-fC2ZVvK37jXIAvoXVjEiK_zQMbZCe6N-dLEe_pD5oRlCcBDuJO6xaWOeH6Z_57GagNa3r52U5vBvr6pb5ZzA5KA6Sqk_asFycxUCYX4n13UDlY_tYnRce_QEWNuStFz8tGFfau4LhKGJ-WwsTai7IKDbzd1GfqS3kNkpVhsZuRvf4H0BZQPjiKWeXc6aE45vVOV6XNLeLf8p1jQH6QtZSoI1JDr2RYidoW9KoYOBTB-rZwbda1tlBOOoA0wgwVyAsPhvndo3Dod9VGThMbF1HOLl3zgTbW7-8p9ro1XAM0G_8n2ibm0x9lIw5mPtUTlOAyB-8OQCOYx2NBLNXxh5zdD8YdQ1HG7WzgWUQOeA2LZnlbil86Gs0nggA1LS5tL3tdh-B3TKUCv-L4GHyVx6f5TOce81TbaAducD4DGyoOOpf9pdQKfffLg1KxEnowRao-9vkmxFyIaWJ8vowIkkhgtxhofLYE5AFrRwJrl_p5Ko7Zeku25hPKFaZcELCSJkqmgk9UFgGuMb3q8x-46IlYfC4mpFHASxCzyZi6zQkmvHNpcghxISD6bgw1sj_qr21y3NFoQK1U7OMZYG82-H0YbGx1u6KaxuaJERN2A1phKQvcWBpEdlxfUYYHe0vP--RqmH392S77BirCuowYwE6vzbvjnjSvAZ8j6KRLWWBt6mvj9k6nQGNdsJCTsjxuHkfPn3B5Fd2uZjnAcSWXWXFwkPvuVbQCbQwutoiOhnmCvaUujvMhOrU1KCBw7hU3wUoLzI85wqevCfIyndbOduE8Kidz-iASSkucL1qiNXFlU5ShsUqpspE6-GdRtmGyNmF-q8_eMUgcyiIsrcty2rTZ2k3BQ9S5yu4ilcka4Pfaa7qU_ESDOvh5NBHJmRjt-OCyrfKfE6Mt6vtbXuWeGi5AaqXYdjCuxfztmBiy1uUl_ssTL7UNvIiC5CgEsjV2ag_mKskt9qERPej9VpzXFiWkCp3fKbsZAqSg7QR_YdUFe1oc71D8JSCYM1S7FP4Jq0Ll64CIk65JN2BViuKxQmu-ounr9g0mZjPsv4Yn8CcD3BxlIr0quXoTBlHak0y3bididqSMWsQqXTOHps4ukz2qyIat65KZAWZnmSAwTFjbQ_ARMsipHBvwP4gBEgoy3C2vYh9_ClDuSooz255w-5C1j5XlNGAD4iVpZo-H6BtRuULYY9fCVAiqOHj0Qe6wbBmZI4lVnI1wmBFU2ozYSI1kSFVvOLKg0CJ2jMVxAdymi24IPRzHVP4VDtqosBJoU8ft_Ol9Tc5FEc0RthE4-V_OG7THI8b9-gt2eoImrsMmxvJ2WWLRRFLLjpiJI82j4-o2M_ZWJQXQCSs-Xc9ZMGKzr9TeN8mTHtdgMVd9p4RnMUlOq7L1p-HzNjJ729jT9Wxc16pKXJoW9qHToflZ98bedNsWyGJF4syNzzvnCkCNltw6RmqzS1tU1X2otHvt2S005TNYjlgWgGyS6U7zGRYn4E9oULl1h4dWd68R4HoC_7NFTYQUuDPS-0BYc8uGkB7wtFAU2O   
Successful Page Load
ICML uses cookies for essential functions only. We do not sell your personal information. Our Privacy Policy »
Accept
The ICML Logo above may be used on presentations. Right-click and choose download. It is a vector graphic and may be used at any scale.
Useful links
About ICML
ICML Proceedings at PMLR
Code of Conduct
Contact
1269 Law Street, San Diego CA 92109
Email
ICML Proceedings at PMLR