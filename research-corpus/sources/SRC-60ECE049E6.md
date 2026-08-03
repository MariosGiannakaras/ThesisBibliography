> Source: https://arxiv.org/html/2603.08956v3

A Survey of Reinforcement Learning For Economics
Report GitHub Issue
×
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub 
arXiv is now an independent nonprofit! Learn more ×
arXiv logo Back to arXiv
Why HTML? Report Issue Back to Abstract Download PDF  
Abstract
1 Introduction
2 Two Cultures of Sequential Decision-Making
2.1 Core Distinctions
2.2 Overlapping Terminology
2.3 Structural Equivalences
2.4 Notation
3 A Brief History of Reinforcement Learning
3.1 Animal Psychology
3.2 Board Games
3.3 Optimal Control
4 Reinforcement Learning Algorithms
4.1 The Classical Synthesis
4.1.1 Monte Carlo Estimation
4.1.2 Sutton (1988)
4.1.3 Watkins (1989)
4.1.4 Williams (1992)
4.1.5 Tesauro (1994)
4.1.6 SARSA (1994)
4.1.7 Baird (1995)
4.1.8 Actor-Critic Methods (2000)
4.1.9 Natural Policy Gradient (2001)
4.1.10 Fitted Value Iteration and Fitted Q-Iteration (2005)
4.2 The Deep Learning Era
4.2.1 Deep Q-Networks (2015)
4.2.2 TRPO and PPO (2015, 2017)
4.2.3 Soft Actor-Critic (2018)
4.2.4 AlphaGo Zero (2017)
5 The Theory of Reinforcement Learning
5.1 The Geometry of Dynamic Programming
5.1.1 Value Iteration as Picard Iteration
5.1.2 Policy Iteration as Newton's Method
5.1.3 Simulation Study: The Brock–Mirman Economy
5.2 Value Learning Methods
5.2.1 Stochastic Approximation Foundations
5.2.2 Q-Learning and SARSA
5.2.3 Multi-Step Returns and TD( λ \lambda )
5.2.4 Simulation Study: Credit Assignment in a Corridor
5.2.5 Finite-Sample Theory of Fitted Methods
5.2.6 Simulation Study: Fitted Methods on Linear-Quadratic Control
5.2.7 Simulation Study: Basis Representability on the Brock–Mirman Economy
5.2.8 Rollout, Lookahead, and AlphaZero
5.3 The Central Challenge: The Deadly Triad
5.3.1 The Projected Bellman Operator
5.3.2 Why Off-Policy Learning Diverges
5.3.3 Resolutions
5.4 Policy Learning Methods
5.4.1 The Policy Gradient Theorem
5.4.2 REINFORCE and Variance Reduction
5.4.3 Natural Policy Gradient and Gradient Domination
5.4.4 Trust Region Methods
5.5 Hybrid Methods
5.5.1 Actor-Critic Architecture and Two-Timescale Convergence
5.5.2 Entropy Regularization and Soft Actor-Critic
5.5.3 Error Amplification Under Approximate Value Functions
5.5.4 Sample Complexity of Planning
5.6 Fundamental Tradeoffs
5.7 Conclusion
6 The Empirics of Deep Reinforcement Learning
6.1 The Moving Target Problem
6.2 The Reproducibility Crisis and Sensitivity to Random Seeds
6.3 Value Overestimation and Spikes
6.4 Plasticity Loss and Primacy Bias
6.5 Implementation Dominates Algorithmic Innovation
6.6 Replay Buffer Pathologies and Reward Scaling
6.7 Simulation Study: Bellman Error and Value Error in Offline Policy Evaluation
6.8 Discussion and Recommendations
7 Reinforcement Learning for Optimal Control
7.1 Ride-Hailing Dispatch
7.2 Hotel Revenue Management
7.3 E-Commerce Dynamic Pricing
7.4 Financial Order Execution
7.5 Supply Chain Inventory Management
7.6 Real-Time Bidding
7.7 Simulation Study: Bus Engine Replacement
8 Structural Estimation with Reinforcement Learning
8.0.1 Adusumilli and Eckardt (2022): TD Learning for CCP Estimation
8.0.2 Hu and Yang (2025): Policy Gradient for DDC Estimation
8.1 Dynamic Oligopoly and Strategic Interaction
8.1.1 Asker, Fershtman, Jeon, and Pakes (2020): Q-Learning in Dynamic Procurement Auctions
8.1.2 Hollenbeck (2019): TD Learning for Merger Analysis with Innovation
8.2 Auction Equilibria and Mechanism Design
8.2.1 Brero, Eden, Gerstgrasser, Parkes, and Rheingans-Yoo (2021): RL for Sequential Price Mechanisms
8.2.2 Ravindranath, Feng, Wang, Zaheer, Mehta, and Parkes (2024): Fitted Policy Iteration for Combinatorial Auctions
8.3 Macroeconomic Models
8.4 Optimal Policy Design
8.5 Simulation Study: DDC Estimation at Scale
9 Reinforcement Learning in Games
9.1 Stochastic Games and Equilibrium Learning
9.1.1 The Stochastic Game Framework
9.1.2 Minimax-Q Learning
9.1.3 Nash-Q Learning
9.1.4 The Convergence Problem
9.1.5 Simulation Study: Cournot and Bertrand Duopoly
9.2 Counterfactual Regret Minimization
9.3 Neural Extensions
9.3.1 Deep CFR
9.3.2 Neural Fictitious Self-Play
9.3.3 Poker Results
9.4 The Coase Conjecture
9.4.1 Model
9.4.2 Equilibrium Analysis
9.4.3 Computational Results
9.5 Discussion
10 Bandits and Dynamic Pricing
10.1 Foundations
10.1.1 No Structure on Demand
10.1.2 Parametric Demand
10.1.3 High-Dimensional Features with Sparsity
10.2 Revealed Preference and Partial Identification
10.3 The Value of Knowing the Noise Distribution
10.4 Strategic Buyers
10.5 Comparison of Regret Rates
10.6 Applications
10.6.1 Joint Assortment and Pricing at Scale
10.7 Simulation Study: The Knowledge Ladder
11 Offline Reinforcement Learning and Human Feedback
11.1 The Pessimism Principle
11.1.1 Concentrability and Coverage
11.1.2 Impossibility Results
11.2 Algorithms
11.2.1 Fitted Q-Iteration
11.2.2 Conservative Q-Learning
11.2.3 Implicit Q-Learning
11.2.4 Batch-Constrained Q-Learning
11.3 Simulation: Offline RL for Dynamic Pricing
11.4 From Offline RL to Human Feedback
11.5 Learning Rewards from Preferences
11.6 The RLHF Pipeline and Direct Optimization
11.7 Recent Developments
11.8 Simulation Study: Preference Learning in Job Search
12 Reinforcement Learning and Causal Inference
12.1 From Partial Observability to Causal Structure
12.2 The Confounded MDP
12.3 Backdoor-Adjusted Off-Policy Evaluation
12.4 Alternative Identification Strategies
12.4.1 Front-Door Criterion
12.4.2 Instrumental Variables
12.4.3 Proximal Causal Inference
12.5 The Broader Causal RL Landscape
12.6 Simulation Study: Confounded Retail Pricing MDP
13 Discussion
13.1 How Economics Improves Reinforcement Learning
13.2 How Reinforcement Learning Advances Economics
13.3 Open Challenges
13.4 Conclusion
References
A Glossary of Acronyms and Terms
License: CC BY 4.0
arXiv:2603.08956v3 [econ.GN] 17 Mar 2026
A Survey of Reinforcement Learning For Economics
Pranjal Rawat, Georgetown University
( March 2026)
This survey (re)introduces reinforcement learning methods to economists. The curse of dimensionality limits how far exact dynamic programming can be effectively applied, forcing us to rely on suitably “small” problems or our ability to convert “big” problems into smaller ones. While this reduction has been sufficient for many classical applications, a growing class of economic models resists such reduction. Reinforcement learning algorithms offer a natural, sample-based extension of dynamic programming, extending tractability to problems with high-dimensional states, continuous actions, and strategic interactions. I review the theory connecting classical planning to modern learning algorithms and demonstrate their mechanics through simulated examples in pricing, inventory control, strategic games, and preference elicitation. I also examine the practical vulnerabilities of these algorithms, noting their brittleness, sample inefficiency, sensitivity to hyperparameters, and the absence of global convergence guarantees outside of tabular settings. The successes of reinforcement learning remain strictly bounded by these constraints, as well as a reliance on accurate simulators. That said, when guided by economic structure, reinforcement learning provides a flexible and innovative framework. It stands as an imperfect, but promising, addition to the computational economist's toolkit. A companion survey (Rust and Rawat, 2026b) covers the inverse problem of inferring preferences from observed behavior. All simulation code is publicly available. 1 1 1 https://github.com/rawatpranjal/survey-of-reinforcement-learning-in-economics
Keywords: Reinforcement Learning, Economics, Structural Estimation, Inverse Reinforcement Learning, Multi-Agent, Bandits, RLHF
Contents
1 Introduction
2 Two Cultures of Sequential Decision-Making
2.1 Core Distinctions
2.2 Overlapping Terminology
2.3 Structural Equivalences
2.4 Notation
3 A Brief History of Reinforcement Learning
3.1 Animal Psychology
3.2 Board Games
3.3 Optimal Control
4 Reinforcement Learning Algorithms
4.1 The Classical Synthesis
4.1.1 Monte Carlo Estimation
4.1.2 Sutton (1988)
4.1.3 Watkins (1989)
4.1.4 Williams (1992)
4.1.5 Tesauro (1994)
4.1.6 SARSA (1994)
4.1.7 Baird (1995)
4.1.8 Actor-Critic Methods (2000)
4.1.9 Natural Policy Gradient (2001)
4.1.10 Fitted Value Iteration and Fitted Q-Iteration (2005)
4.2 The Deep Learning Era
4.2.1 Deep Q-Networks (2015)
4.2.2 TRPO and PPO (2015, 2017)
4.2.3 Soft Actor-Critic (2018)
4.2.4 AlphaGo Zero (2017)
5 The Theory of Reinforcement Learning
5.1 The Geometry of Dynamic Programming
5.1.1 Value Iteration as Picard Iteration
5.1.2 Policy Iteration as Newton's Method
5.1.3 Simulation Study: The Brock–Mirman Economy
5.2 Value Learning Methods
5.2.1 Stochastic Approximation Foundations
5.2.2 Q-Learning and SARSA
5.2.3 Multi-Step Returns and TD( λ \lambda )
5.2.4 Simulation Study: Credit Assignment in a Corridor
5.2.5 Finite-Sample Theory of Fitted Methods
5.2.6 Simulation Study: Fitted Methods on Linear-Quadratic Control
5.2.7 Simulation Study: Basis Representability on the Brock–Mirman Economy
5.2.8 Rollout, Lookahead, and AlphaZero
5.3 The Central Challenge: The Deadly Triad
5.3.1 The Projected Bellman Operator
5.3.2 Why Off-Policy Learning Diverges
5.3.3 Resolutions
5.4 Policy Learning Methods
5.4.1 The Policy Gradient Theorem
5.4.2 REINFORCE and Variance Reduction
5.4.3 Natural Policy Gradient and Gradient Domination
5.4.4 Trust Region Methods
5.5 Hybrid Methods
5.5.1 Actor-Critic Architecture and Two-Timescale Convergence
5.5.2 Entropy Regularization and Soft Actor-Critic
5.5.3 Error Amplification Under Approximate Value Functions
5.5.4 Sample Complexity of Planning
5.6 Fundamental Tradeoffs
5.7 Conclusion
6 The Empirics of Deep Reinforcement Learning
6.1 The Moving Target Problem
6.2 The Reproducibility Crisis and Sensitivity to Random Seeds
6.3 Value Overestimation and Spikes
6.4 Plasticity Loss and Primacy Bias
6.5 Implementation Dominates Algorithmic Innovation
6.6 Replay Buffer Pathologies and Reward Scaling
6.7 Simulation Study: Bellman Error and Value Error in Offline Policy Evaluation
6.8 Discussion and Recommendations
7 Reinforcement Learning for Optimal Control
7.1 Ride-Hailing Dispatch
7.2 Hotel Revenue Management
7.3 E-Commerce Dynamic Pricing
7.4 Financial Order Execution
7.5 Supply Chain Inventory Management
7.6 Real-Time Bidding
7.7 Simulation Study: Bus Engine Replacement
8 Structural Estimation with Reinforcement Learning
8.0.1 Adusumilli and Eckardt (2022): TD Learning for CCP Estimation
8.0.2 Hu and Yang (2025): Policy Gradient for DDC Estimation
8.1 Dynamic Oligopoly and Strategic Interaction
8.1.1 Asker, Fershtman, Jeon, and Pakes (2020): Q-Learning in Dynamic Procurement Auctions
8.1.2 Hollenbeck (2019): TD Learning for Merger Analysis with Innovation
8.2 Auction Equilibria and Mechanism Design
8.2.1 Brero, Eden, Gerstgrasser, Parkes, and Rheingans-Yoo (2021): RL for Sequential Price Mechanisms
8.2.2 Ravindranath, Feng, Wang, Zaheer, Mehta, and Parkes (2024): Fitted Policy Iteration for Combinatorial Auctions
8.3 Macroeconomic Models
8.4 Optimal Policy Design
8.5 Simulation Study: DDC Estimation at Scale
9 Reinforcement Learning in Games
9.1 Stochastic Games and Equilibrium Learning
9.1.1 The Stochastic Game Framework
9.1.2 Minimax-Q Learning
9.1.3 Nash-Q Learning
9.1.4 The Convergence Problem
9.1.5 Simulation Study: Cournot and Bertrand Duopoly
9.2 Counterfactual Regret Minimization
9.3 Neural Extensions
9.3.1 Deep CFR
9.3.2 Neural Fictitious Self-Play
9.3.3 Poker Results
9.4 The Coase Conjecture
9.4.1 Model
9.4.2 Equilibrium Analysis
9.4.3 Computational Results
9.5 Discussion
10 Bandits and Dynamic Pricing
10.1 Foundations
10.1.1 No Structure on Demand
10.1.2 Parametric Demand
10.1.3 High-Dimensional Features with Sparsity
10.2 Revealed Preference and Partial Identification
10.3 The Value of Knowing the Noise Distribution
10.4 Strategic Buyers
10.5 Comparison of Regret Rates
10.6 Applications
10.6.1 Joint Assortment and Pricing at Scale
10.7 Simulation Study: The Knowledge Ladder
11 Offline Reinforcement Learning and Human Feedback
11.1 The Pessimism Principle
11.1.1 Concentrability and Coverage
11.1.2 Impossibility Results
11.2 Algorithms
11.2.1 Fitted Q-Iteration
11.2.2 Conservative Q-Learning
11.2.3 Implicit Q-Learning
11.2.4 Batch-Constrained Q-Learning
11.3 Simulation: Offline RL for Dynamic Pricing
11.4 From Offline RL to Human Feedback
11.5 Learning Rewards from Preferences
11.6 The RLHF Pipeline and Direct Optimization
11.7 Recent Developments
11.8 Simulation Study: Preference Learning in Job Search
12 Reinforcement Learning and Causal Inference
12.1 From Partial Observability to Causal Structure
12.2 The Confounded MDP
12.3 Backdoor-Adjusted Off-Policy Evaluation
12.4 Alternative Identification Strategies
12.4.1 Front-Door Criterion
12.4.2 Instrumental Variables
12.4.3 Proximal Causal Inference
12.5 The Broader Causal RL Landscape
12.6 Simulation Study: Confounded Retail Pricing MDP
13 Discussion
13.1 How Economics Improves Reinforcement Learning
13.2 How Reinforcement Learning Advances Economics
13.3 Open Challenges
13.4 Conclusion
References
A Glossary of Acronyms and Terms
1 Introduction
This survey (re)introduces reinforcement learning to economists. I review the theoretical connections between dynamic programming and reinforcement learning, demonstrating how value iteration, Q-learning, and policy gradient methods are common solution methods to the same class of optimization problems. I then examine applications across several domains, including control problems including pricing and inventory management; structural economic models with high-dimensional state spaces; strategic games in which multi-agent algorithms compute equilibria under imperfect information; bandit problems in which economic structure yields tighter regret bounds; and preference learning. The exposition combines formal theory, practical applications and computational illustration.
Both dynamic programming and reinforcement learning solve the Bellman equation; they differ in the information requirements and the way in which the solution is refined. First, dynamic programming requires knowledge of the transition in the environment and the reward function which allows the reduction of the average Bellman error, reinforcement learning estimates value functions only from sampled transitions (observed sets of state, action, reward, next-state) which only allows reduction of the sampled Bellman error at that state-action pair. This allows us to improve policies in domains where it is easier to build a simulator than specify the model of the environment and rewards e.g. board games, physics simulators for robots. Second, dynamic programming makes a “breadth-first” (accross all states and actions) update of the solution at each sweep, while reinforcement learning makes a “incremental” (only for the current state and action) update; this greatly reduces the computational burden and enhances scalability.
Reduction of average Bellman errors gives dynamic programming a geometric rate of convergence to the optimal solution, while the incremental updates and reduction of sampled Bellman errors, when combined with “sufficient exploration” of the state-action space, gives reinforcement learning only sublinear convergence guarantees. This is however, quite sufficient in practise, the scalability attained by only sampling transitions and making incremental updates more than makes up for the slower rates of convergence (and brittleness). These approximation methods sacrifice theoretical guarantees. RL algorithms lack the convergence assurances of exact dynamic programming. They exhibit sensitivity to hyperparameters and initialization. They can converge to suboptimal policies without diagnostic indication. This survey presents reinforcement learning as a computationally flexible framework while acknowledging its methodological limitations.
Theory in reinforcement learning trails empirical success, often by years; convergence guarantees, sample complexity bounds, and approximation error characterizations typically arrive after practitioners have demonstrated that an algorithm works. The theoretical insights that eventually follow tend to be deep and structural, and the empirical frontier is itself a productive research frontier. Experiments are brittle, conducted on benchmark environments that are stylized approximations of deployment settings. These benchmarks nonetheless serve a critical coordination function, aligning research effort, enabling reproducible comparison, and exposing failure modes that motivate new theory. Details matter disproportionately in reinforcement learning; small implementation choices can determine whether an algorithm converges or diverges, and the practice of releasing code and documenting hyperparameters, seeds, and preprocessing has proven essential to progress.
This survey focuses on less-surveyed intersections between reinforcement learning and economics, including the shared theoretical foundations, structural estimation, strategic interaction, bandit problems with economic structure, preference learning, and causal inference. Algorithmic collusion, in which independent pricing algorithms learn to sustain supra-competitive prices (Calvano et al., 2020) , is treated in a companion thesis chapter (Rawat, 2026) and omitted here. Reinforcement learning and deep learning methods for solving macroeconomic models with heterogeneous agents constitute a growing literature with dedicated methodological treatments (Atashbar and Shi, 2022) , (Maliar et al., 2021) , and (Fernández-Villaverde et al., 2024) . Portfolio optimization, optimal execution, and asset pricing via reinforcement learning form a large body of work surveyed comprehensively elsewhere (Hambly et al., 2023) . The inverse problem of inferring preferences from observed behavior using inverse reinforcement learning and structural estimation is treated in a companion survey (Rust and Rawat, 2026) .
The survey addresses the forward problem, that is, computing optimal policies given a known or simulated environment. Chapter 1 traces the parallel historical development of dynamic programming and reinforcement learning. Chapter 2 develops unified theory connecting planning and learning. Chapters 3 and 4 apply reinforcement learning to control problems and economic models. Chapter 5 examines strategic games. Chapter 6 addresses bandit problems. Chapter 7 discusses reinforcement learning from human feedback. Chapter 8 connects reinforcement learning to causal inference. Chapter 9 concludes.
2 Two Cultures of Sequential Decision-Making
Economics and reinforcement learning both study sequential decision-making under uncertainty, but they descend from different intellectual traditions. Economics is fundamentally an inference culture. Its central task is to understand the world. An economist's “model” is a specification of preferences, beliefs, constraints, and an equilibrium concept. The RL tradition is instead a control culture. Its central task is to act in the world. An RL researcher's “model” is a transition kernel P  ( s ′ | s , a ) P(s^{\prime}|s,a) and a reward function r  ( s , a ) r(s,a) . These are different mathematical objects serving fundamentally different scientific purposes.
The two cultures maintain different relationships with data. Economists work primarily with observational data, and endogeneity is the central obstacle. Identification is its defining challenge which involves dealing with functional forms, equilibrium definitions, instrumental variables, regression discontinuities, and natural experiments. RL researchers have traditionally enjoyed what might be called simulator omnipotence. They often own the data-generating process and can create the variation in their data and fit any manner of nonparametric functions through millions of simulated samples. They face computational rather than statistical constraints. This difference shapes the cultures, from algorithm design to what counts as a valid result and what is the standard of evidence.
The two fields also differ in their treatment of human agency. To an economist, the human (or firm) is the optimizer, a rational or boundedly rational agent solving her own dynamic program, whose revealed choices are the data to be explained. To an RL researcher, the algorithm is the optimizer and the human is part of the environment. A customer's purchasing decision is not modeled as utility maximization but as a stochastic reward signal from which the algorithm learns. Even the word “learning” itself carries different meaning across the divide. In economic theory, learning means Bayesian updating of beliefs about unknown parameters. In reinforcement learning, learning means executing a recursive stochastic approximation algorithm to find the fixed point of the Bellman operator.
The two cultures have a closely related and shared vocabulary but with divergent meanings. And this creates persistent confusion for researchers crossing from one field to the other. This chapter attempts to provide a systematic translation and notes common sources of confusion.
2.1 Core Distinctions
RL organizes its core problems along axes that do not map directly onto well known categories. In RL, Prediction refers to estimating V π  ( s ) V^{\pi}(s) or Q π  ( s , a ) Q^{\pi}(s,a) for a fixed policy π \pi (policy evaluation), not forecasting observable variables. Control refers to finding the policy π ∗ \pi^{*} that maximizes expected discounted return (policy optimization), not the inclusion of regressors. Because prediction concerns evaluating a specific policy, a closely related question is whether the data was generated by the policy being studied. On-policy methods evaluate and improve the same policy that generates the data. Off-policy methods learn about a target policy π \pi from data generated by a different behavioral policy μ \mu . This distinction is central to causal inference (Section 12), where off-policy evaluation is precisely counterfactual policy evaluation. 2 2 2“Counterfactual” here is used in the interventional sense, asking “what would happen if we deployed policy π \pi instead of μ \mu ?” This is distinct from the structural counterfactual in Oberst and Sontag ( 2019) , which conditions on the specific realized trajectory and asks what would have happened to this individual under a different action, requiring a fully specified structural causal model rather than just the observational distribution under μ \mu .
A separate question concerns how the algorithm accesses experience. Online RL learns while interacting with the environment, collecting new data as a consequence of its own actions. Offline RL (also called batch RL) learns exclusively from a fixed dataset of previously collected transitions, with no ability to gather additional samples. The offline setting is closer to standard empirical work, where the dataset is given and the analyst cannot run new experiments; the online setting corresponds more closely to adaptive experimental design or sequential decision problems. Note that “online” in RL carries no timing constraint; it means only that the agent generates fresh experience. Real-time RL, by contrast, imposes hard deadlines on the perception-action loop, as in robotics or mechatronics. Every real-time RL system is online, but most online RL (games, recommender systems) are not real-time.
Aside from data access is the question of what the algorithm does with that data. In RL, the word model refers strictly to the environment's dynamics, the transition kernel P  ( s ′ | s , a ) P(s^{\prime}|s,a) and reward function r  ( s , a ) r(s,a) . A model-based RL algorithm explicitly constructs or is given a mathematical representation of P P and r r , then computes a policy by planning through that representation (for example, using a simulator or the known rules of a game, as in AlphaZero). A model-free algorithm computes the value function or policy directly from experienced transitions without ever building an explicit representation of the transition probabilities. Crucially, “model-free” need not mean the algorithm lacks complete access to any model of the environment. A model-free algorithm could interact with a simulator that internally implements a complete computerized model of the environment; the distinction is that the algorithm never extracts or plans through the transition probabilities, treating the simulator as a black box that merely returns sample transitions. In some sense, usually when we use “model-free” learning we are saying that while we do have access to some model, for some reason we do not or simply can not use it to find an optimal policy directly and instead find it easier to “sample transitions and rewards” from it. So an agent may have access to a complete simulation model of the world (e.g., a chess engine), but if its algorithm learns purely from sampled trajectories rather than using the known rules of the game to plan, it is considered model-free learning. However, it is possible that a “model-free” algorithm could also be implimented “in-field” where there is genuinely no access to a “model” of the environment but only direct access to the environment itself (for reasons discussed later, this is rarely done).
One might believe that an analog to “model-free” RL algorithms might be reduced-form or a statistical model that only requires a few assumptions (exogeneity, etc.) to make inference on parameters of interest. But this is a false analogy, as regardless of “model-free” or “model-based” we are talking about learning optimal policies within a MDP (this itself demands a certain structure on the problem including the Markovian assumption that the state contains all relevant information). One could believe that “model-based” algorithms are analogous to structural estimation, which involves the specification of preferences, technology, beliefs, and an equilibrium concept, all of which give rise to specific transition dynamics and reward functions. This is also a false analogy. In RL terminology, for an algorithm to be “model-based”, the conditions very precise, all we need is a given representation of P P and r r (regardless of whether you do or don't make any structural economic assumptions about human or firm behavior or their interactions). All this to say, in RL, the model generally only refers to transition matrices P P and rewards r r within an MDP; wheras in economics it refers to a set of agents, preferences, exclusion restrictions, and equilibrium concepts. Therefore, it is possible to do structural estimation of an “economic model” with a lot of structure but by using a “model-free” RL algorithm as a computational tool to find the equilibrium, as in Section 8. 3 3 3 The closer analog to structural estimation in the RL taxonomy is inverse reinforcement learning (IRL), which takes observed behavior as data and recovers the reward function that rationalizes it. This is the subject of the companion survey (Rust and Rawat, 2026) .
Every RL system passes through two phases. In the training phase, the agent interacts with an environment (simulated or real) and updates its parameters. In the execution phase (also called the deployment phase), the policy is frozen and used to make decisions without further updates. This distinction is critical for interpreting “online.” Online training in RL almost always takes place inside a simulator (and not in the “real world”). AlphaGo Zero trained online through millions of self-play games; when it faced Lee Sedol, its weights were frozen and it was purely executing its trained policy. Some deployed systems in Section 7 followed this pattern cleanly; DiDi's dispatch system trained a value function from historical trip data, then deployed with fixed weights. Others blur the boundary. The hotel revenue management system in Section 7.2 updated Q-values from realized returns after each completed episode during live operation, making it an in-field learner rather than a frozen executor. 4 4 4“In-field” is not standard RL vocabulary. We introduce it here to distinguish live-market online learning, where exploration has real economic cost, from the far more common case of online learning inside a simulator. Bandit algorithms (Section 10) also learn in-field by design, updating demand estimates from real customer responses during deployment. The term in-field is useful here; it denotes online learning where the environment is a live market with real economic consequences, as opposed to online learning inside a simulator where exploration is free, cheap and safe. While industry practitioners use terms like 'operational phase', 'live', and 'inference-time' interchangeably to describe any post-training system, this survey reserves the term in-field to specifically denote online learning in a live market where exploration carries real economic consequences.
A related terminological hazard concerns the word inference. In machine learning, “inference” refers to executing a frozen model, a forward pass producing outputs from inputs. In economics, “inference” means statistical inference, the construction of standard errors, confidence intervals, and hypothesis tests. This survey uses “inference” exclusively in the econometric sense and “execution” or “deployment” when referring to applying a trained model (whether in a computer or in field). Established terms such as “Bayesian inference” and “variational inference,” which refer to inference about parameters or distributions, are used where appropriate. The key takeaway is that most RL convergence results and sample complexity guarantees refer to the training phase, and interpreting them as claims about deployed performance requires additional argument. Table 1 summarizes these distinctions.
Table 1: The reinforcement learning lifecycle grid. Most RL research operates in the top-left cell. When economists hear “online,” they typically picture the bottom-left.
A typical economic RL pipeline moves through the grid sequentially, from pre-training on historical logs (middle-left) to refinement in a simulator (top-left) to deployment with frozen weights (bottom-right). Bandits illustrate this fluidity; even a bandit algorithm that will ultimately learn in-field is typically calibrated in simulation and tuned on historical logs before any live deployment, because in-field exploration incurs real financial cost. The systems that do operate in-field arrive with exploration parameters, initial policies, and demand priors shaped by extensive offline preparation.
The Tmall e-commerce pricing project of Liu et al. ( 2019) (Section 7.3) illustrates this migration concretely. The team pre-trained a DQN from logged specialist pricing decisions (historical data, training), then ran offline evaluation of the candidate policy on held-out transaction logs before any live deployment (historical data, execution). The evaluated policy was deployed for 15 to 30 day field experiments on live Tmall traffic, with the agent receiving reward and observation signals from the market environment (live market, execution and training). Liu et al. ( 2019) note that no accurate simulator exists for e-commerce pricing, so the project skipped the simulator row entirely, jumping from historical pre-training directly to live deployment. Not every application traverses all six cells of Table 1, but the grid clarifies which cells a given project could be working on.
2.2 Overlapping Terminology
In RL the environment is a formal object encompassing everything outside the agent (the DGP, other agents, market clearing conditions), whereas in economics “environment” refers more loosely to market structure or institutional rules. 5 5 5 A source of confusion is generative model. In machine learning broadly, this means a model of the joint distribution P  ( X , Y ) P(X,Y) or a synthetic data generator (GANs, diffusion models). In RL theory, a generative model is a simulator oracle that, given any ( s , a ) (s,a) , returns a sample s ′ ∼ P ( ⋅ | s , a ) s^{\prime}\sim P(\cdot|s,a) and reward r  ( s , a ) r(s,a) ; the usage implies random-access simulation, stronger than sequential online interaction but weaker than knowing P P analytically.
In RL, the return G t = ∑ k = 0 ∞ γ k  r t + k + 1 G_{t}=\sum_{k=0}^{\infty}\gamma^{k}r_{t+k+1} is the discounted sum of future rewards from time t t onward, the random variable whose expectation defines the value function. The RL usage is closer to what economists call the “present discounted value” of a stream of payoffs. A single complete sequence of interactions from an initial state to termination, ( s 0 , a 0 , r 1 , s 1 , … , s T ) (s_{0},a_{0},r_{1},s_{1},\ldots,s_{T}) , is called an episode (synonymously, trajectory or rollout). 6 6 6 The closest econometric analogs are a single panel unit's time series, a realization of a stochastic process, or one “history” in a dynamic model. Where an econometrician speaks of the outcome, meaning the dependent variable Y Y in a regression, RL has no single analog: the reward r t r_{t} is the per-period outcome, the return G t G_{t} is the cumulative outcome, and the value function V π  ( s ) V^{\pi}(s) is the expected cumulative outcome conditional on state.
Bootstrapping in econometrics refers to Efron's resampling method (Efron, 1979) ; in RL, it means updating a value estimate using another value estimate rather than a complete realized return, as when a TD algorithm uses the target r t + 1 + γ  V  ( s t + 1 ) r_{t+1}+\gamma V(s_{t+1}) that depends on the current, uncertain estimate V  ( s t + 1 ) V(s_{t+1}) (Sutton, 1988) .
Learning carries at least four distinct meanings in this survey. In economic theory (Bayesian learning, adaptive expectations), learning refers to agents forming and refining beliefs about unknown parameters of their environment. In supervised machine learning, learning means statistical estimation, fitting the weights of a parameterized model to minimize a loss function over data. In reinforcement learning, “learning” is primarily computation. When an RL agent “learns” a Q-function, it is executing a recursive stochastic approximation algorithm to find the fixed point of the Bellman operator. We say the algorithm is “learning” because it improves its policy iteratively through simulated or real experience, but mathematically it is solving a fixed-point problem. In many applications throughout this survey, particularly Section 8, the RL algorithm is simply a numerical method for solving the Bellman equation; no actual human-like learning from experience is taking place. Finally, while RL draws inspiration from animal psychology (Section 3.1), it is a drastic simplification of biological learning. Tabula rasa RL algorithms require millions of iterations of trial and error to discover policies that animals acquire rapidly. Real-world animal learning relies on innate priors, basic physical knowledge, and parental nurturing and should be distinct from RL-style “learning”.
Function approximation in RL refers to representing value functions or policies using parameterized function classes (linear combinations of basis functions, kernel methods, or neural networks), which econometricians will recognize as sieve estimation or nonparametric series estimation, the approximation of an unknown function by projection onto a finite-dimensional basis.
The term bandit itself carries different mathematical content across disciplines. The classical multi-armed bandit in statistics and economics (Thompson, 1933; Rothschild, 1974; Gittins, 1979) is a Bayesian sequential allocation problem. The state is the agent's posterior belief over the unknown arm distributions, and the solution is the Gittins index, an optimal allocation rule derived from the theory of optimal stopping. In the RL and computer science literature, bandits are instead framed as frequentist regret-minimization problems. Algorithms such as UCB provide worst-case bounds on cumulative regret ∑ t = 1 T ( μ ∗ − μ A t ) \sum_{t=1}^{T}(\mu^{*}-\mu_{A_{t}}) without requiring Bayesian priors. The two traditions ask fundamentally different questions, Bayesian optimality of the full sequential problem versus minimax regret rates over adversarial or stochastic environments, and their answers are not directly comparable. Section 10 adopts the regret framework because it connects more naturally to the sample complexity concerns that arise in economic field experiments.
The term contextual bandit is especially liable to misreading by economists. To an economist, the “context” is simply the state variable x t x_{t} , and a contextual bandit looks like an MDP with an unknown reward parameter. What the RL literature signals by “context” is a specific structural restriction on transitions, the agent's action has no causal effect on the next context, so that P  ( x t + 1 ∣ x t , a t ) = P  ( x t + 1 ) P(x_{t+1}\mid x_{t},a_{t})=P(x_{t+1}) . This exogeneity assumption separates the exploration problem (learning which arm is best given the current context) from the planning problem (choosing actions that influence future states). When contexts evolve exogenously, there is no long-horizon credit assignment, and the problem reduces to repeated one-period optimization under uncertainty. The term “contextual” therefore flags a modeling assumption about dynamics, not merely the presence of observable covariates.
A concrete example clarifies how the two culture see a common problem. The RL literature frames some recommender systems as contextual bandits, where user covariates are the context, the recommendation is the arm, and a click or rating is the reward. An economist might instead view movie recommendation as a two-sided learning problem in which the platform learns user preferences while users simultaneously explore the catalog and update their own tastes. The bandit formulation absorbs the user's utility maximization into the environment's reward signal and treats user arrivals as exogenous. This is a modeling choice, not a fact about the world. Also, the object called a “bandit” in this formulation, a one-step decision under exogenous context, is a slightly different mathematical object than the Bayesian sequential allocation problem of Gittins ( 1979) , even though both carry the same name and are related. 7 7 7 Lattimore ( 2016) proves that the Gittins index with a flat Gaussian prior achieves finite-time regret of the same order as UCB, and that the index decomposes as posterior mean plus an exploration bonus that shrinks toward zero near the horizon, structurally resembling but differing from the UCB confidence bound. As apparant, the RL view often abstracts away from a lot of complexity in the world (human learning, human interaction) to squash the problem into the straightforward language of optimal control ( p  i pi , V V , P , r P,r ), while the economics literature prefers to allow for much more complex models of human-firm interaction.
2.3 Structural Equivalences
Beyond terminological differences, several formal objects in RL and economics are mathematically identical. The softmax (or Boltzmann) policy used throughout RL is the multinomial logit model of McFadden ( 1974) . The RL softmax policy selects actions according to
π  ( a ∣ s ) = exp  ( Q  ( s , a ) / τ ) ∑ a ′ ∈ 𝒜 exp  ( Q  ( s , a ′ ) / τ ) , \pi(a\mid s)=\frac{\exp(Q(s,a)/\tau)}{\sum_{a^{\prime}\in\mathcal{A}}\exp(Q(s,a^{\prime})/\tau)},
(1)
where τ > 0 \tau>0 is a temperature parameter. In the discrete choice framework, Q  ( s , a ) Q(s,a) plays the role of the deterministic component of utility v  ( a ∣ x ) v(a\mid x) , and τ \tau is the scale parameter of the Type I extreme value (Gumbel) taste shocks ε a \varepsilon_{a} . As τ → 0 \tau\to 0 , the policy converges to the greedy (deterministic) policy, just as the logit choice probability concentrates on the utility-maximizing alternative as the variance of taste shocks vanishes.
The entropy regularization commonly added to RL objectives is the inclusive value (or log-sum-exp) from the discrete choice literature. The soft value function
V soft  ( s ) = τ  log  ∑ a ∈ 𝒜 exp  ( Q  ( s , a ) / τ ) V^{\text{soft}}(s)=\tau\log\sum_{a\in\mathcal{A}}\exp(Q(s,a)/\tau)
(2)
is identical to the McFadden surplus function W  ( x ) = τ  log  ∑ a exp  ( v  ( a | x ) / τ ) + C W(x)=\tau\log\sum_{a}\exp(v(a|x)/\tau)+C , where C C is Euler's constant. In the structural estimation literature, this object appears as the Emax function in dynamic discrete choice models following Rust ( 1987) .
The advantage function A π  ( s , a ) = Q π  ( s , a ) − V π  ( s ) A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s) measures how much better action a a is compared to the average action under π \pi . In the discrete choice framework, this is precisely the choice-specific value function net of the ex-ante value function, a quantity that appears in the Hotz and Miller ( 1993) CCP estimator for dynamic discrete choice models.
2.4 Notation
Table 2 maps the notation used throughout this survey to the most common econometric equivalents.
Table 2: Notation mapping between reinforcement learning and economics.
RL Term
Symbol
Economics Equivalent
Symbol
State
s ∈ 𝒮 s\in\mathcal{S}
State variable, covariate
x t x_{t} , Ω t \Omega_{t}
Action
a ∈ 𝒜 a\in\mathcal{A}
Choice, control variable
d t d_{t} , u t u_{t} 8 8 8 The letter u u appears twice in the economics column with different meanings: u t u_{t} denotes the control variable (action), while u  ( x , d ) u(x,d) denotes per-period utility (reward). Context usually disambiguates, but readers should note the collision.
Reward
r  ( s , a ) r(s,a)
Per-period utility, payoff
u  ( x , d ) u(x,d)
Discount factor
γ \gamma 9 9 9 RL permits γ = 0 \gamma=0 (myopic, one-step) and γ = 1 \gamma=1 (undiscounted, episodic tasks with guaranteed termination). Economics requires β ∈ ( 0 , 1 ) \beta\in(0,1) strictly; the contraction mapping argument for the Bellman operator relies on β < 1 \beta<1 .
Discount factor
β \beta
Policy
π  ( a | s ) \pi(a|s)
Decision rule, CCP
P  ( d | x ) P(d|x)
Value function
V π  ( s ) V^{\pi}(s)
Ex-ante value function
V ¯ θ  ( x ) \bar{V}_{\theta}(x)
Q-function
Q π  ( s , a ) Q^{\pi}(s,a)
Choice-specific value function
v θ  ( x , d ) v_{\theta}(x,d)
Return
G t G_{t}
Present discounted value
∑ k = 0 ∞ β k  u t + k \sum_{k=0}^{\infty}\beta^{k}u_{t+k}
Transition
P  ( s ′ | s , a ) P(s^{\prime}|s,a)
State transition law
f  ( x t + 1 | x t , d t ) f(x_{t+1}|x_{t},d_{t})
Learning rate
α \alpha
Step size
α n \alpha_{n}
TD error
δ t \delta_{t} 10 10 10 The TD error δ t = r t + 1 + γ  V  ( s t + 1 ) − V  ( s t ) \delta_{t}=r_{t+1}+\gamma V(s_{t+1})-V(s_{t}) is a stochastic, sample-based quantity. The “Bellman residual” in numerical methods and economics is the population object ‖ V − 𝒯  V ‖ |V-\mathcal{T}V| , measuring how far a candidate V V is from satisfying the Bellman equation exactly. Bellman residual minimization (BRM), which directly minimizes 𝔼  [ ( r + γ  V  ( s ′ ) − V  ( s ) ) 2 ] \mathbb{E}[(r+\gamma V(s^{\prime})-V(s))^{2}] , is a distinct estimation method from TD learning.
Bellman residual at sample
–
3 A Brief History of Reinforcement Learning
Reinforcement learning draws on animal psychology, game-playing programs, and optimal control theory in roughly equal measure. Thorndike's law of effect and behaviourist trial-and-error learning provided the notion of “reinforcement” as formalized by Rescorla-Wagner. Chess and checkers programs of Shannon and Samuel from the 1950s onward gave researchers concrete problems on which to test ideas about machine learning. The Bellman-Howard-Blackwell dynamic programming framework provided the recursive structure and language.
3.1 Animal Psychology
Controlled experiments on rats, cats, and dogs inspired the “gridworld” environments still used today, and shaped how the field conceptualizes “training” agents through “reward signals”. Thorndike ( 1898) placed cats in puzzle boxes with latched doors and food visible outside. Across 15 different box configurations, the cats initially engaged in undirected behavior such as clawing at the walls, pushing against the bars, reaching through openings. The first cat to escape the simplest box required 160 seconds of random activity before accidentally pressing the latch. By the 24th trial, the same cat pressed the latch directly within 6 seconds. The learning curves showed gradual, continuous improvement rather than sudden insight. From these experiments the Law of Effect was formulated: responses (actions) followed by satisfaction (positive rewards) are “stamped in” and more likely to recur, while those followed by discomfort (negative rewards) are “stamped out.”
Pavlov ( 1927) noted that dogs salivated not only at food itself but at the sight of an empty food bowl, the sound of footsteps, and other stimuli that preceded feeding (i.e. the state). To measure these “psychic secretions” precisely, he surgically implanted fistulas (tubes allowing external collection) to collect saliva. In the canonical experiment, a metronome sounded before food delivery. After 20–40 pairings, the metronome alone elicited salivation. The response followed not from the stimulus itself but from what it ”predicted”. In reinforcement learning terms, the conditioned stimulus is a state s s , and the learned expectation of food is the value function V  ( s ) V(s) .
Kamin ( 1969) demonstrated that learning requires more than mere co-occurrence in time. In Phase I of his blocking experiment, rats learned that a noise predicted a shock and developed a conditioned fear response to the noise alone. In Phase II, a compound stimulus of noise plus light was paired with the same shock. When the light was subsequently presented alone, no fear response occurred. The light was “blocked” (ignored) because the noise already predicted the shock perfectly. There was no prediction error (or “surprise”) to drive learning about the light. Once the noise was established as a predictor, the light added no new information and thus no new learning occurred.
Rescorla and Wagner ( 1972) formalized the blocking phenomenon as a prediction-error learning rule. Translating to RL notation: 11 11 11 The original notation used V i V_{i} for associative strength of stimulus i i , α i \alpha_{i} for stimulus salience (noticeability), β j \beta_{j} for learning rate, λ j \lambda_{j} for maximum conditioning (1 if reward present, 0 otherwise), and V tot = ∑ k V k V_{\text{tot}}=\sum_{k}V_{k} for total prediction. The correspondence is: V i → V  ( s ) V_{i}\to V(s) , α i  β j → α \alpha_{i}\beta_{j}\to\alpha , λ j → r \lambda_{j}\to r , V tot → V  ( s ) V_{\text{tot}}\to V(s) . See Sutton and Barto ( 1990) for details.
V  ( s ) ← V  ( s ) + α  δ , where  δ = r − V  ( s ) V(s)\leftarrow V(s)+\alpha,\delta,\quad\text{where }\delta=r-V(s)
(3)
This is temporal difference learning with γ = 0 \gamma=0 , without discounting of future rewards. Each stimulus s s begins with V  ( s ) = 0 V(s)=0 . On each trial, the organism observes the stimuli present, receives outcome r ∈ { 0 , 1 } r\in{0,1} , and updates values according to δ \delta . The model is purely predictive; there are no actions, only learned expectations about reward. 12 12 12 The Rescorla-Wagner update is mathematically identical to the Widrow-Hoff least mean squares rule. The model's power lay in prediction, not just explanation. It correctly predicted overexpectation, whereby two separately conditioned stimuli combined and reinforced together each lose value because their summed prediction exceeds r r .
3.2 Board Games
Chess and checkers are sequential decision problems. The board position is a state s ∈ 𝒮 s\in\mathcal{S} , a legal move is an action a ∈ 𝒜  ( s ) a\in\mathcal{A}(s) , and the resulting position is a successor state s ′ = T  ( s , a ) s^{\prime}=T(s,a) determined by the rules of the game. The game outcome provides a terminal reward r ∈ { + 1 , 0 , − 1 } r\in{+1,0,-1} for win, draw, or loss. An evaluation function f  ( P ) f(P) that scores a position corresponds to a value function V  ( s ) V(s) estimating expected outcome. These games are deterministic (no chance moves in chess), fully observable (both players see the entire board), and zero-sum (one player's gain is the other's loss). The adversarial structure introduces a second player whose actions a ′ a^{\prime} must be anticipated.
Shannon ( 1950) posed the fundamental question: can we program a general-purpose computer to play chess, and if so, what principles should guide the design? The challenge is computational. A chess game averages 40 moves per player with roughly 30 legal moves available at each position. Shannon estimated that exhaustive search through all possible games would require examining approximately 30 80 ≈ 10 120 30^{80}\approx 10^{120} positions, a number exceeding the atoms in the observable universe. This is the curse of dimensionality applied to games, where state space size grows exponentially with the number of sequential decisions. Shannon calculated that brute-force enumeration would require 10 90 10^{90} years at any foreseeable computing speed. The curse intensifies with game complexity. Chess has approximately 10 47 10^{47} legal positions, shogi 10 71 10^{71} , and Go 10 171 10^{171} . 13 13 13 State space estimates from Igami ( 2020) .
Shannon distinguished two approaches. Type A strategies search all continuations to a fixed depth H H , building a complete game tree and evaluating every leaf (“rote-learning”). Type B strategies search selectively, examining only variations deemed important by some criterion (“generalization”). Either approach requires an evaluation function f  ( P ) f(P) to score positions where search terminates. Shannon proposed linear evaluation:
f  ( P ) = ∑ i w i  ϕ i  ( P ) f(P)=\sum_{i}w_{i}\phi_{i}(P)
(4)
with features ϕ i \phi_{i} for material, mobility, pawn structure, and king safety. Weights w i w_{i} were hand-tuned. The minimax principle governs adversarial search. In a two-player zero-sum game, the value of a position satisfies
V  ( s ) = max a ∈ 𝒜  ( s )  min a ′ ∈ 𝒜 ′  ( s ′ )  V  ( T  ( s , a , a ′ ) ) V(s)=\max_{a\in\mathcal{A}(s)}\min_{a^{\prime}\in\mathcal{A}^{\prime}(s^{\prime})}V(T(s,a,a^{\prime}))
(5)
where the maximizing player moves first and the minimizing opponent responds optimally. This is model-based planning, since the transition function T T is known exactly from the game rules. The computational problem is how to use limited search resources effectively given the exponential tree.
Both Type A and Type B strategies truncate the game tree at depth H H and substitute the evaluation function for exact continuation values. This is approximate dynamic programming. The true value V ∗  ( s ) V^{*}(s) satisfies a recursive equation, but computing it exactly is infeasible, so the recursion is truncated and terminal values approximated. Deeper lookahead ( H H -step search) builds larger trees; rollout policies extend search by simulating play to the end using a fast base policy. 14 14 14 Monte Carlo tree search, developed later, samples rollouts rather than enumerating all branches, enabling deeper effective lookahead in games with large branching factors. The evaluation function serves as a heuristic substitute for exact computation. Shannon did not implement a chess program; the 1950 paper is theoretical, outlining the architecture that shaped fifty years of game engines.
Samuel ( 1959) built a checkers program for the IBM 704 that could improve through experience. The program played against itself, generating virtually unlimited training data at no cost. It parameterized the value function as a linear combination of hand-crafted features (piece advantage, mobility, king safety):
V  ( s ; 𝐰 ) = ∑ i w i  ϕ i  ( s ) V(s;\mathbf{w})=\sum_{i}w_{i}\phi_{i}(s)
(6)
After each move from s t s_{t} to s t + 1 s_{t+1} , weights were updated by temporal difference:
𝐰 ← 𝐰 + α  [ V  ( s t + 1 ; 𝐰 ) − V  ( s t ; 𝐰 ) ]  ∇ 𝐰 V  ( s t ; 𝐰 ) \mathbf{w}\leftarrow\mathbf{w}+\alpha\left[V(s_{t+1};\mathbf{w})-V(s_{t};\mathbf{w})\right]\nabla_{\mathbf{w}}V(s_{t};\mathbf{w})
(7)
In a 1965 match, World Champion W.F. Hellman won all four games played by mail, but was played to a draw in one game. After learning from 173,989 book moves, the program agreed with the book-recommended move (or rated only 1 move higher) 64% of the time without lookahead. With lookahead and minimaxing, it followed book moves ”a much higher fraction of the time.”
The linear parameterization compresses the value function from 10 20 10^{20} table entries to dozens of weights, the essential response to the curse of dimensionality. Samuel's architecture, minimax search to depth H H with the learned evaluation function scoring leaves, is an early instance of rollout, where tree search simulates forward, truncating at H H and substituting V  ( s ) V(s) for exact continuation values. 15 15 15 Bertsekas ( 2021) interprets this as approximate dynamic programming, where offline training (learning V V ) combined with online planning (tree search) implements a Newton-like step for the Bellman equation. The conceptual apparatus of modern game-playing AI (self-play, evaluation learning, tree search, and function approximation) was present in the 1950s.
3.3 Optimal Control
Bellman ( 1957) considered multi-stage decision processes in which a system occupies state s ∈ 𝒮 s\in\mathcal{S} , the decision-maker chooses action a ∈ 𝒜 a\in\mathcal{A} , the system transitions to s ′ ∼ P ( ⋅ | s , a ) s^{\prime}\sim P(\cdot|s,a) , and a reward r  ( s , a , s ′ ) r(s,a,s^{\prime}) accrues. The objective is to maximize cumulative reward over a finite or infinite horizon. The classical approach treats an N N -stage process as a single N N -dimensional optimization. Bellman calculated the consequence. A 10-stage process with 10 grid points per variable requires 10 10 10^{10} function evaluations; at one evaluation per second, 10 10 10^{10} evaluations require 2.77 million hours. He called this exponential growth the curse of dimensionality. His solution was the principle of optimality, namely that an optimal policy has the property that, whatever the initial state and initial decision, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision. This principle yields the Bellman equation:
V ∗  ( s ) = max a ∈ 𝒜  [ r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V ∗  ( s ′ ) ] V^{}(s)=\max_{a\in\mathcal{A}}\left[r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a),V^{}(s^{\prime})\right]
(8)
The equation reduces an N N -dimensional problem to a sequence of N N one-dimensional problems. Value iteration computes V ∗ V^{*} by iterating V k + 1  ( s ) = max a  [ r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V k  ( s ′ ) ] V_{k+1}(s)=\max_{a}[r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a)V_{k}(s^{\prime})] . The monograph applied the method to resource allocation, inventory control, bottleneck scheduling, gold mining under uncertainty, and multi-stage games. 16 16 16 Chapter IX shows how dynamic programming derives classical variational conditions from the functional equation. The continuous-time analogue is the Hamilton-Jacobi-Bellman equation.
Howard ( 1960) observed that value iteration converges slowly for problems of indefinite duration. His alternative, policy iteration, solves for the value function of a fixed policy and then improves the policy directly. Given policy π \pi , policy evaluation computes the gain g g (average reward per period) and relative values v i v_{i} by solving the linear system g + v i = q i + ∑ j p i  j  v j g+v_{i}=q_{i}+\sum_{j}p_{ij}v_{j} for i = 1 , … , N i=1,\ldots,N , where q i q_{i} is the expected immediate reward in state i i and p i  j p_{ij} is the transition probability under π \pi . Policy improvement then selects, for each state i i , the action k k maximizing q i k + ∑ j p i  j k  v j q_{i}^{k}+\sum_{j}p_{ij}^{k}v_{j} . Howard proved that each iteration strictly increases the gain unless the policy is already optimal, and the algorithm terminates in finitely many steps. For a problem with 50 states and 50 actions per state, exhaustive enumeration must consider 50 50 ≈ 10 85 50^{50}\approx 10^{85} policies; policy iteration finds the optimum in a handful of iterations. Howard demonstrated the method on a toymaker's production problem, taxicab dispatch in three city zones, and automobile replacement timing.
Blackwell ( 1965) established the measure-theoretic foundations for discounted dynamic programming with general state and action spaces. He proved that the Bellman operator T T defined by T  u  ( s ) = sup a [ r  ( s , a ) + γ  ∫ u  ( s ′ )  P  ( d  s ′ | s , a ) ] Tu(s)=\sup_{a}[r(s,a)+\gamma\int u(s^{\prime})P(ds^{\prime}|s,a)] is a contraction with modulus γ \gamma : ‖ T  u − T  v ‖ ∞ ≤ γ  ‖ u − v ‖ ∞ |Tu-Tv|{\infty}\leq\gamma|u-v|{\infty} . Banach's fixed-point theorem then guarantees a unique bounded solution V ∗ V^{} to the Bellman equation, with ‖ V k − V ∗ ‖ ∞ ≤ γ k  ‖ V 0 − V ∗ ‖ ∞ |V_{k}-V^{}|{\infty}\leq\gamma^{k}|V{0}-V^{*}|_{\infty} under value iteration. The central result concerns stationary policies, which use the same decision rule f : 𝒮 → 𝒜 f:\mathcal{S}\to\mathcal{A} at every period regardless of history. Blackwell proved that if the action space is finite, there exists an optimal stationary policy. For countable action spaces, ϵ \epsilon -optimal stationary policies exist for every ϵ > 0 \epsilon>0 . These results justify the focus on memoryless policies, since optimal behavior depends only on the current state, not on the history of past states and actions. The Bellman equation, Howard's policy iteration, and Blackwell's existence theorems constitute the planning framework. Given complete knowledge of P P and r r , these methods compute optimal policies exactly. The challenge of learning without such knowledge is the central problem of reinforcement learning. 17 17 17 For comprehensive treatments of dynamic programming in economics, including numerical methods, computational complexity, and the curse of dimensionality, see Rust ( 2008) and Rust ( 1996) .
4 Reinforcement Learning Algorithms
4.1 The Classical Synthesis
4.1.1 Monte Carlo Estimation
When P  ( s ′ | s , a ) P(s^{\prime}|s,a) and r  ( s , a ) r(s,a) are unknown, the obvious approach is to use Monte Carlo (MC) to approximate them. These methods estimate value functions from sampled episodes ( s 0 , a 0 , r 1 , s 1 , a 1 , r 2 , … , s T ) (s_{0},a_{0},r_{1},s_{1},a_{1},r_{2},\ldots,s_{T}) . The realized return from state s t s_{t} is
G t = ∑ k = 0 T − t − 1 γ k  r t + k + 1 G_{t}=\sum_{k=0}^{T-t-1}\gamma^{k}r_{t+k+1}
(9)
First-visit MC prediction averages G t G_{t} over episodes for each state s s , counting only its first occurrence per episode. Each first-visit return is an independent draw from the return distribution, so the sample mean converges almost surely to V π  ( s ) V^{\pi}(s) by the strong law of large numbers (Sutton and Barto, 2018) . An incremental update is,
V  ( s ) ← V  ( s ) + α  [ G t − V  ( s ) ] V(s)\leftarrow V(s)+\alpha[G_{t}-V(s)]
For MC control, we can estimate action-values Q  ( s , a ) Q(s,a) by averaging first-visit returns from each state-action pair, then improve the policy greedily: π  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a Q  ( s , a ) \pi(s)=\mathop{\it argmax}{a}Q(s,a) . Under exploring starts (every ( s , a ) (s,a) pair begins an episode infinitely often), this alternation converges to Q ∗ Q^{} . 18 18 18 Tsitsiklis ( 2002) proved convergence even when the policy improves after every episode rather than waiting for complete evaluation. In practice, exploring starts is infeasible, so on-policy variants use ε \varepsilon -greedy exploration instead. These converge to Q ∗ Q^{} provided the exploration schedule satisfies the greedy-in-the-limit with infinite exploration (GLIE) condition: every state-action pair is visited infinitely often, and ε t → 0 \varepsilon{t}\to 0 so the policy converges to greedy in the limit.
4.1.2 Sutton (1988)
Monte Carlo has two limitations. The agent must wait for episode termination to compute G t G_{t} , ruling out continuing tasks. And G t G_{t} is unbiased ( 𝔼  [ G t ∣ S t = s ] = V π  ( s ) \mathbb{E}[G_{t}\mid S_{t}=s]=V^{\pi}(s) ) but high-variance, because it sums random rewards over the entire trajectory.
Sutton ( 1988) proposed temporal difference (TD) learning to fix both problems. TD(0) replaces the full return G t G_{t} with a one-step target:
V  ( s t ) ← V  ( s t ) + α  [ r t + 1 + γ  V  ( s t + 1 ) − V  ( s t ) ] V(s_{t})\leftarrow V(s_{t})+\alpha\left[r_{t+1}+\gamma V(s_{t+1})-V(s_{t})\right]
(10)
The target r t + 1 + γ  V  ( s t + 1 ) r_{t+1}+\gamma V(s_{t+1}) depends on one random reward and one random transition, so its variance is low. The cost is bias. The bootstrap target V  ( s t + 1 ) V(s_{t+1}) is the agent's current estimate, not the true value. This is “ bootstrapping”. 19 19 19 See Section 2 for the distinction between RL bootstrapping and Efron's resampling procedure. As V V improves, the bias shrinks; the low variance persists regardless. Sutton demonstrated this tradeoff on a five-state random walk where TD(0) converged faster than Monte Carlo with less data.
The general TD( λ \lambda ) update interpolates between these extremes through an eligibility trace. 20 20 20 The eligibility trace records which states were recently visited, allowing credit assignment to propagate backward in time. States visited more recently receive stronger updates when the TD error is observed.
V  ( s t ) ← V  ( s t ) + α  δ t  e t  ( s ) V(s_{t})\leftarrow V(s_{t})+\alpha,\delta_{t},e_{t}(s)
(11)
where δ t = r t + 1 + γ  V  ( s t + 1 ) − V  ( s t ) \delta_{t}=r_{t+1}+\gamma V(s_{t+1})-V(s_{t}) is the TD error and e t  ( s ) = γ  λ  e t − 1  ( s ) + 𝟙  { s = s t } e_{t}(s)=\gamma\lambda,e_{t-1}(s)+\mathbbm{1}{s=s_{t}} is the eligibility trace for state s s . Setting λ = 0 \lambda=0 yields TD(0); setting λ = 1 \lambda=1 recovers Monte Carlo returns. Intermediate λ \lambda trades off variance against bias. 21 21 21 Dayan ( 1992) proved convergence of TD( λ \lambda ) for general λ \lambda in the tabular case; Jaakkola et al. ( 1994) gave a unified stochastic approximation proof covering both TD and Q-learning; Tsitsiklis and Van Roy ( 1997) extended the analysis to linear function approximation.
4.1.3 Watkins (1989)
TD(0) learns value functions V  ( s ) V(s) , but converting these to actions (the control problem) still requires knowing transition probabilities. Given V  ( s ′ ) V(s^{\prime}) for all successor states, the agent needs to know which action leads to which successor.
Watkins and Dayan ( 1992) , formalizing Watkins's 1989 PhD thesis, provided the solution. Instead of learning V  ( s ′ ) V(s^{\prime}) learn Q  ( s , a ) Q(s,a) (the action value function or the “quality” of actions function) directly, the expected return from taking action a a in state s s and then behaving optimally. The optimal policy is then π ∗  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a Q ∗  ( s , a ) \pi^{}(s)=\mathop{\it argmax}_{a}Q^{}(s,a) , requiring no model to act. The Bellman optimality equation provides the fixed-point condition:
Q ∗  ( s , a ) = 𝔼  [ r + γ  max a ′  Q ∗  ( s ′ , a ′ ) ∣ s , a ] Q^{}(s,a)=\mathbb{E}\left[r+\gamma\max_{a^{\prime}}Q^{}(s^{\prime},a^{\prime})\mid s,a\right]
(12)
Q-learning achieves this via the update
Q  ( s t , a t ) ← Q  ( s t , a t ) + α  [ r t + 1 + γ  max a ′  Q  ( s t + 1 , a ′ ) − Q  ( s t , a t ) ] Q(s_{t},a_{t})\leftarrow Q(s_{t},a_{t})+\alpha\left[r_{t+1}+\gamma\max_{a^{\prime}}Q(s_{t+1},a^{\prime})-Q(s_{t},a_{t})\right]
(13)
Q-learning converges to Q ∗ Q^{} under standard regularity conditions (Section 5.2). The maximization over a ′ a^{\prime} makes Q-learning off-policy: 22 22 22 See Section 2 for the on-policy/off-policy distinction. Q-learning learns about the greedy policy π ∗  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a Q  ( s , a ) \pi^{}(s)=\mathop{\it argmax}_{a}Q(s,a) while collecting data with an exploratory policy. This exploratory policy needs only to be sufficiently “exploratory” and admits a wide range of policies; including a fully random policy. the update target uses the greedy action at the next state regardless of the action actually taken. Therefore the agent can follow an ε \varepsilon -greedy exploration strategy or even a fully random policy, while learning about the optimal policy directly.
4.1.4 Williams (1992)
Value-based methods learn an action-value function and derive a policy from it. Williams ( 1992) derived an alternative, policy gradients, that optimize the policy directly by gradient ascent on expected return
∇ θ J  ( θ ) = 𝔼 π θ  [ ∑ t = 0 T ∇ θ log  π θ  ( a t | s t )  G t ] \nabla_{\theta}J(\theta)=\mathbb{E}{\pi{\theta}}\left[\sum_{t=0}^{T}\nabla_{\theta}\log\pi_{\theta}(a_{t}|s_{t}),G_{t}\right]
(14)
where G t = ∑ k = 0 T − t γ k  r t + k + 1 G_{t}=\sum_{k=0}^{T-t}\gamma^{k}r_{t+k+1} is the discounted return from time t t . The log-derivative trick allows the gradient to be estimated from sampled trajectories without differentiating through the environment dynamics.
Consider a robot arm that must apply a continuous torque a ∈ ℝ a\in\mathbb{R} to reach a target angle. Q-learning requires computing max a  Q  ( s , a ) \max_{a}Q(s,a) at every update, which becomes a nested optimization problem 23 23 23 In continuous action spaces, max a  Q  ( s , a ) \max_{a}Q(s,a) has no closed-form solution in general and must be solved numerically at every Bellman update. Discretizing a d d -dimensional action space on a grid of m m points per dimension costs O  ( m d ) O(m^{d}) evaluations per update step. when the action space is continuous. A policy gradient method sidesteps the issue. Parameterize the policy as a Gaussian π θ  ( a | s ) = 𝒩  ( μ θ  ( s ) , σ θ 2  ( s ) ) \pi_{\theta}(a|s)=\mathcal{N}(\mu_{\theta}(s),,\sigma_{\theta}^{2}(s)) , 24 24 24 The Gaussian distribution 𝒩  ( μ , σ 2 ) \mathcal{N}(\mu,\sigma^{2}) has density ( 2  π  σ 2 ) − 1 / 2  exp  ( − ( a − μ ) 2 / 2  σ 2 ) (2\pi\sigma^{2})^{-1/2}\exp(-(a-\mu)^{2}/2\sigma^{2}) . Here μ θ  ( s ) \mu_{\theta}(s) and σ θ  ( s ) \sigma_{\theta}(s) are neural network outputs parameterizing the policy mean and standard deviation. sample an action, observe the return, and update θ \theta by REINFORCE. Virtually all continuous-control results in reinforcement learning descend from the policy gradient framework for this reason.
4.1.5 Tesauro (1994)
Tesauro ( 1994) 's TD-Gammon demonstrated that temporal difference learning with neural network function approximation could achieve expert-level play in a domain with approximately 10 20 10^{20} legal positions 25 25 25 The state 𝐱  ( s ) \mathbf{x}(s) was a 198-dimensional binary encoding of the raw board (four units per board point per player indicating checker counts, plus bar and borne-off counts). The output was a four-component vector estimating probabilities of each game outcome (White/Black × \times normal win/gammon), and the move maximizing expected outcome among all legal moves was selected at each step..
Backgammon was far beyond tabular methods, yet TD-Gammon trained a feedforward neural network to estimate the probability of winning from any board position. A hidden layer 26 26 26 A feedforward neural network stacks an input layer, one or more hidden layers, and an output layer; each unit in a hidden layer computes a weighted sum of its inputs and applies a nonlinear activation, here the logistic sigmoid σ  ( x ) = 1 / ( 1 + e − x ) \sigma(x)=1/(1+e^{-x}) , which maps any real number to ( 0 , 1 ) (0,1) and is identical to the binary logit link function. of 80 sigmoid units fed a single sigmoid output.
V ^  ( s ) = σ  ( 𝐰 ⊤  σ  ( W  𝐱  ( s ) + 𝐛 ) + c ) \hat{V}(s)=\sigma!\bigl(\mathbf{w}^{\top}\sigma(W\mathbf{x}(s)+\mathbf{b})+c\bigr)
(15)
where σ \sigma is the logistic sigmoid, W W is the input-to-hidden weight matrix, and 𝐰 \mathbf{w} is the hidden-to-output weight vector. The network was trained by self-play using TD( λ \lambda ) with λ = 0.7 \lambda=0.7 . After each move from position s t s_{t} to s t + 1 s_{t+1} , the weights 𝜽 \boldsymbol{\theta} 27 27 27 𝜽 \boldsymbol{\theta} denotes the full vector of network weights and biases, generalizing the scalar θ \theta used for policy parameters in earlier sections. were updated by
𝜽 ← 𝜽 + α  [ V ^  ( s t + 1 ) − V ^  ( s t ) ]  𝐞 t \boldsymbol{\theta}\leftarrow\boldsymbol{\theta}+\alpha\bigl[\hat{V}(s_{t+1})-\hat{V}(s_{t})\bigr],\mathbf{e}_{t}
(16)
where α \alpha 28 28 28 The learning rate α \alpha controls the step size of each parameter update. TD learning uses a semi-gradient step rather than true gradient descent, but α \alpha plays the same role: too large and updates overshoot; too small and convergence is slow. is the step size, and the eligibility trace 𝐞 t = ∑ k = 1 t λ t − k  ∇ 𝜽 V ^  ( s k ) \mathbf{e}{t}=\sum{k=1}^{t}\lambda^{t-k}\nabla_{\boldsymbol{\theta}}\hat{V}(s_{k}) accumulates exponentially decayed gradients of past predictions. 29 29 29 In the neural network case, the eligibility trace 𝐞 t ∈ ℝ | 𝜽 | \mathbf{e}{t}\in\mathbb{R}^{|\boldsymbol{\theta}|} is a vector accumulating exponentially-weighted gradients, extending the scalar state-based trace to parameter space. At game's end, V ^  ( s t + 1 ) \hat{V}(s{t+1}) is replaced by the outcome z ∈ { 0 , 1 } z\in{0,1} .
A single neural network V ^ \hat{V} serves as the evaluation function for both players. At each turn, the current player selects the legal move maximizing V ^  ( s ′ ) \hat{V}(s^{\prime}) from its own perspective. As the network improves, it generates stronger play on both sides, producing harder training games that drive further improvement. The dice rolls ensure diverse board positions without requiring an explicit exploration mechanism. 30 30 30 Version 2.1, trained on 1,500,000 games with 2-ply search, achieved near-parity with former world champion Bill Robertie and discovered novel positional strategies subsequently adopted by the human backgammon community.
4.1.6 SARSA (1994)
Q-learning learns the optimal action-value function regardless of the policy generating experience. This off-policy property is useful but introduces complications when combined with function approximation. Rummery and Niranjan ( 1994) introduced SARSA as an on-policy 31 31 31 See Section 2 for the on-policy/off-policy distinction. alternative that learns the value of the policy actually being followed. The name derives from the quintuple ( s t , a t , r t + 1 , s t + 1 , a t + 1 ) (s_{t},a_{t},r_{t+1},s_{t+1},a_{t+1}) used in each update:
Q  ( s t , a t ) ← Q  ( s t , a t ) + α  [ r t + 1 + γ  Q  ( s t + 1 , a t + 1 ) − Q  ( s t , a t ) ] Q(s_{t},a_{t})\leftarrow Q(s_{t},a_{t})+\alpha\left[r_{t+1}+\gamma Q(s_{t+1},a_{t+1})-Q(s_{t},a_{t})\right]
(17)
The key difference from Q-learning is that SARSA bootstraps from the action a t + 1 a_{t+1} actually taken at the next state, rather than the greedy action 𝑎𝑟𝑔𝑚𝑎𝑥 a ′ Q  ( s t + 1 , a ′ ) \mathop{\it argmax}{a^{\prime}}Q(s{t+1},a^{\prime}) . This makes the algorithm on-policy, since the target depends on the behavior policy generating the data.
If the agent follows an ε \varepsilon -greedy policy, SARSA converges to Q ε  -greedy Q^{\varepsilon\text{-greedy}} , not Q ∗ Q^{} 32 32 32 SARSA converges to Q ∗ Q^{} under GLIE (greedy in the limit with infinite exploration)A GLIE schedule explores all state-action pairs infinitely often but converges to the greedy policy asymptotically. The standard ε \varepsilon -greedy policy with ε t → 0 \varepsilon_{t}\to 0 is one such schedule. policies and standard step-size conditions (Section 5.2). This distinction matters when exploration is costly. Consider the cliff-walking problem, where an agent must traverse a gridworld with a cliff along one edge. The optimal path runs along the cliff edge (shortest route), but the ε \varepsilon -greedy policy occasionally falls off. Q-learning learns the optimal path because it evaluates the greedy policy; the agent falls off during learning but the Q-values reflect the optimal route. SARSA learns a safer path further from the cliff because it evaluates the actual exploratory policy; it accounts for the fact that exploration sometimes leads to catastrophic states.
4.1.7 Baird (1995)
Baird ( 1995) constructed a six-state star MDP demonstrating divergence of Q-learning with linear function approximation. The MDP has five outer states that all transition to a single inner state under the target policy. The off-policy behavior samples states uniformly. With linear function approximation, the weights grow without bound under repeated Q-learning updates. The source of instability is the interaction of three components, namely bootstrapping (updating from estimated values rather than observed returns), off-policy learning (training on data from a different policy than the target), and function approximation (representing the value function with a parameterized model). Sutton and Barto ( 2018) later named this the deadly triad. Any two components can be combined safely; all three together permit divergence. The mechanism underlying this instability is analyzed in Section 5.3.
This result explains the asymmetry between Tesauro's success and Baird's failure. TD-Gammon used bootstrapping and function approximation but was on-policy, with training data coming from the same self-play policy whose value was being estimated. Baird's counterexample used all three components and diverged. Baird also proposed a constructive solution, namely residual gradient algorithms that perform gradient descent on the mean-squared Bellman residual, guaranteeing convergence at the cost of a different fixed point.
4.1.8 Actor-Critic Methods (2000)
The idea of maintaining both a policy ( actor) and a value function ( critic) dates to Barto et al. ( 1983) , who used a two-component system to solve the pole-balancing task. Actor-critic methods address the high variance of REINFORCE by replacing Monte Carlo returns with bootstrapped TD targets as the learning signal. The critic learns a value function V  ( s ) V(s) by TD updates.
V  ( s t ) ← V  ( s t ) + α c  δ t , δ t = r t + 1 + γ  V  ( s t + 1 ) − V  ( s t ) V(s_{t})\leftarrow V(s_{t})+\alpha_{c},\delta_{t},\quad\delta_{t}=r_{t+1}+\gamma V(s_{t+1})-V(s_{t})
(18)
The actor updates the policy using the TD error as a sample of the advantage.
θ ← θ + α a  ∇ θ log  π θ  ( a t | s t )  δ t \theta\leftarrow\theta+\alpha_{a}\nabla_{\theta}\log\pi_{\theta}(a_{t}|s_{t}),\delta_{t}
(19)
The TD error δ t \delta_{t} estimates A π  ( s t , a t ) = Q π  ( s t , a t ) − V π  ( s t ) A^{\pi}(s_{t},a_{t})=Q^{\pi}(s_{t},a_{t})-V^{\pi}(s_{t}) , the advantage of action a t a_{t} over the average action. 33 33 33 That δ t \delta_{t} is an unbiased estimate of the advantage follows from the policy gradient theorem (Sutton et al., 2000) . Positive advantages indicate the action was better than expected; negative advantages indicate it was worse.
Konda and Tsitsiklis ( 2000) provided the first convergence proof for actor-critic algorithms with function approximation, showing convergence to a stationary point under two-timescale learning rates ( α c ≫ α a \alpha_{c}\gg\alpha_{a} ) and a compatibility condition on the critic architecture (Section 5.5).
4.1.9 Natural Policy Gradient (2001)
Standard gradient descent treats all parameter directions equally, but policy parameters define probability distributions whose natural geometry is not Euclidean. Kakade ( 2001) introduced the natural policy gradient, which measures progress in distribution space rather than parameter space. The update uses the Fisher information matrix F  ( θ ) F(\theta) :
F  ( θ ) = 𝔼 s ∼ d π , a ∼ π θ  [ ∇ θ log  π θ  ( a | s )  ∇ θ log  π θ  ( a | s ) ⊤ ] F(\theta)=\mathbb{E}{s\sim d^{\pi},a\sim\pi{\theta}}\left[\nabla_{\theta}\log\pi_{\theta}(a|s)\nabla_{\theta}\log\pi_{\theta}(a|s)^{\top}\right]
(20)
The natural gradient is
∇ ~ θ  J  ( θ ) = F  ( θ ) − 1  ∇ θ J  ( θ ) \tilde{\nabla}{\theta}J(\theta)=F(\theta)^{-1}\nabla{\theta}J(\theta)
(21)
This direction is invariant to reparameterization of the policy. In the tabular softmax 34 34 34 The softmax function maps a vector 𝐳 \mathbf{z} to a probability distribution: softmax  ( z i ) = exp  ( z i ) / ∑ j exp  ( z j ) \text{softmax}(z_{i})=\exp(z_{i})/\sum_{j}\exp(z_{j}) . A softmax policy parameterizes action probabilities as π θ  ( a | s ) = softmax  ( θ s , a ) \pi_{\theta}(a|s)=\text{softmax}(\theta_{s,a}) . case, a single natural gradient step with unit step size recovers one step of exact policy iteration (Section 5.4).
The computational bottleneck is inverting F  ( θ ) ∈ ℝ d × d F(\theta)\in\mathbb{R}^{d\times d} . Practical implementations use conjugate gradient methods to solve F  ( θ )  x = ∇ θ J  ( θ ) F(\theta)x=\nabla_{\theta}J(\theta) without forming F F explicitly. This approach was later scaled to deep neural networks by TRPO and PPO.
4.1.10 Fitted Value Iteration and Fitted Q-Iteration (2005)
Tabular Q-learning maintains a separate entry for every state-action pair. When | 𝒮 | |\mathcal{S}| is large or the state space is continuous, as in most economic applications, this is infeasible. Fitted Q-Iteration (FQI) (Ernst et al., 2005) replaces the tabular update with a supervised regression step: given a batch of transitions, fit a function approximator to the Bellman targets.
Let ℱ \mathcal{F} be a function class mapping 𝒮 × 𝒜 → ℝ \mathcal{S}\times\mathcal{A}\to\mathbb{R} . Initialize Q 0 ≡ 0 Q_{0}\equiv 0 . At each iteration k = 0 , 1 , … , K − 1 k=0,1,\ldots,K-1 : (i) draw N N transitions ( s i , a i , r i , s i ′ ) (s_{i},a_{i},r_{i},s_{i}^{\prime}) from a generative model; (ii) construct regression targets y i ( k ) = r i + γ  max a ′  Q k  ( s i ′ , a ′ ) y_{i}^{(k)}=r_{i}+\gamma\max_{a^{\prime}}Q_{k}(s_{i}^{\prime},a^{\prime}) ; (iii) set Q k + 1 ← arg  min f ∈ ℱ  1 N  ∑ i = 1 N ( f  ( s i , a i ) − y i ( k ) ) 2 Q_{k+1}\leftarrow\arg\min_{f\in\mathcal{F}}\frac{1}{N}\sum_{i=1}^{N}\bigl(f(s_{i},a_{i})-y_{i}^{(k)}\bigr)^{2} . The output is the greedy policy π K  ( s ) = arg  max a  Q K  ( s , a ) \pi_{K}(s)=\arg\max_{a}Q_{K}(s,a) .
The regression step replaces the exact Bellman application with a projection onto ℱ \mathcal{F} : Q k + 1 = Π ℱ  𝒯  Q k Q_{k+1}=\Pi_{\mathcal{F}}\mathcal{T}Q_{k} , where 𝒯 \mathcal{T} is the Bellman optimality operator and Π ℱ \Pi_{\mathcal{F}} is the L 2 L^{2} -projection under the sample distribution. Fitted Value Iteration (FVI) (Munos and Szepesvári, 2008) applies the same idea to the value function directly: V k + 1 = Π ℱ  𝒯 ∗  V k V_{k+1}=\Pi_{\mathcal{F}}\mathcal{T}^{}V_{k} , where ( 𝒯 ∗  V )  ( s ) = max a  { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V  ( s ′ ) } (\mathcal{T}^{}V)(s)=\max_{a}{r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a)V(s^{\prime})} .
With feature matrix Φ ∈ ℝ | 𝒮 | × d \Phi\in\mathbb{R}^{|\mathcal{S}|\times d} (rows ϕ  ( s ) ⊤ \phi(s)^{\top} ) and per-action weight vectors θ a ∈ ℝ d \theta_{a}\in\mathbb{R}^{d} , each FQI regression step for action a a reduces to the normal equations:
θ a ( k + 1 ) = ( Φ ⊤  Φ ) − 1  Φ ⊤  y a ( k ) , \theta_{a}^{(k+1)}=\bigl(\Phi^{\top}\Phi\bigr)^{-1}\Phi^{\top}y_{a}^{(k)},
(22)
where y a ( k )  ( s ) = r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  max a ′  ϕ  ( s ′ ) ⊤  θ a ′ ( k ) y_{a}^{(k)}(s)=r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a)\max_{a^{\prime}}\phi(s^{\prime})^{\top}\theta_{a^{\prime}}^{(k)} . Computation is O  ( d 2  | 𝒮 | + d 3 ) O(d^{2}|\mathcal{S}|+d^{3}) per action per iteration. The FVI update takes the same form with a single weight vector θ V \theta_{V} :
θ V ( k + 1 ) = ( Φ ⊤  Φ ) − 1  Φ ⊤  V target ( k ) , \theta_{V}^{(k+1)}=\bigl(\Phi^{\top}\Phi\bigr)^{-1}\Phi^{\top}V_{\mathrm{target}}^{(k)},
(23)
where V target ( k )  ( s ) = max a  { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  ϕ  ( s ′ ) ⊤  θ V ( k ) } V_{\mathrm{target}}^{(k)}(s)=\max_{a}\bigl{r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a)\phi(s^{\prime})^{\top}\theta_{V}^{(k)}\bigr} . The finite-sample error theory for these methods is developed in Section 5.2.5.
4.2 The Deep Learning Era
4.2.1 Deep Q-Networks (2015)
Mnih et al. ( 2015) trained a single convolutional neural network 35 35 35 A convolutional neural network applies learned spatial filters to detect local patterns in grid-structured data, commonly used for image inputs. to play 49 Atari 2600 games directly from pixel inputs ( 210 × 160 × 3 210\times 160\times 3 ) and a scalar score, using no game-specific features.
The architecture processed four consecutive frames through three convolutional layers and a fully connected layer. 36 36 36 A fully connected layer computes y = W  x + b y=Wx+b where every input unit is connected to every output unit with learned weights W W and biases b b ; it is the affine transformation familiar from linear regression, followed by a nonlinear activation. The network Q  ( s , a ; θ ) Q(s,a;\theta) was trained to minimize the squared temporal difference error
L  ( θ ) = 𝔼 ( s , a , r , s ′ ) ∼ 𝒟  [ ( r + γ  max a ′  Q  ( s ′ , a ′ ; θ − ) − Q  ( s , a ; θ ) ) 2 ] L(\theta)=\mathbb{E}{(s,a,r,s^{\prime})\sim\mathcal{D}}\left[\left(r+\gamma\max{a^{\prime}}Q(s^{\prime},a^{\prime};\theta^{-})-Q(s,a;\theta)\right)^{2}\right]
(24)
Two innovations stabilized learning. Experience replay (Lin, 1992) stored transitions ( s , a , r , s ′ ) (s,a,r,s^{\prime}) in a buffer 𝒟 \mathcal{D} and sampled uniformly for training, breaking the temporal correlation between consecutive updates. A target network used a frozen copy of parameters θ − \theta^{-} , updated periodically, 37 37 37 The buffer held 10 6 10^{6} transitions; the target network θ − \theta^{-} was synchronized to θ \theta every C = 10 , 000 C=10{,}000 steps. so the regression target does not shift with each gradient step.
DQN exceeded human-level performance on 29 of 49 games using a single architecture and hyperparameters. 38 38 38 Hyperparameters are design choices fixed before training begins, such as network depth, learning rate, and replay buffer size; they are not estimated by gradient descent and are analogous to tuning parameters in nonparametric estimation (bandwidth, penalty weights). Games requiring long-horizon planning or sparse rewards, such as Montezuma's Revenge, remained difficult.
4.2.2 TRPO and PPO (2015, 2017)
Policy gradient methods suffer from a practical instability: a single large gradient step can move the policy into a region where performance collapses and recovery is slow.
Schulman et al. ( 2015) addressed this with Trust Region Policy Optimization (TRPO). TRPO solves the constrained optimization problem
max θ  L θ old  ( θ ) subject to D ¯ KL  ( θ old , θ ) ≤ δ \max_{\theta};L_{\theta_{\text{old}}}(\theta)\quad\text{subject to}\quad\bar{D}{\mathrm{KL}}(\theta{\text{old}},\theta)\leq\delta
(25)
where L L is a surrogate objective based on the advantage function A π  ( s , a ) = Q π  ( s , a ) − V π  ( s ) A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s) . 39 39 39 The Kullback-Leibler divergence D KL  ( p ∥ q ) = ∑ x p  ( x )  log  ( p  ( x ) / q  ( x ) ) D_{\mathrm{KL}}(p|q)=\sum_{x}p(x)\log(p(x)/q(x)) measures statistical distance between distributions. The bar denotes expectation over states: D ¯ KL = 𝔼 s [ D KL ( π θ old ( ⋅ | s ) ∥ π θ ( ⋅ | s ) ) ] \bar{D}{\mathrm{KL}}=\mathbb{E}{s}[D_{\mathrm{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s)|\pi_{\theta}(\cdot|s))] .
Schulman et al. ( 2017) proposed Proximal Policy Optimization (PPO) as a simpler alternative. PPO replaces the KL constraint with a clipped surrogate objective:
L CLIP  ( θ ) = 𝔼 t  [ min  ( r t  ( θ )  A ^ t , clip  ( r t  ( θ ) , 1 − ε , 1 + ε )  A ^ t ) ] L^{\text{CLIP}}(\theta)=\mathbb{E}{t}\left[\min!\left(r{t}(\theta)\hat{A}{t},;\text{clip}(r{t}(\theta),1-\varepsilon,1+\varepsilon)\hat{A}_{t}\right)\right]
(26)
where r t  ( θ ) = π θ  ( a t | s t ) / π θ old  ( a t | s t ) r_{t}(\theta)=\pi_{\theta}(a_{t}|s_{t})/\pi_{\theta_{\text{old}}}(a_{t}|s_{t}) is the probability ratio. The clipping removes the incentive for r t  ( θ ) r_{t}(\theta) to move outside the interval [ 1 − ε , 1 + ε ] [1-\varepsilon,1+\varepsilon] , penalizing large policy updates without explicitly computing a divergence measure.
PPO outperformed A2C, TRPO, and the cross-entropy method on continuous control benchmarks and achieved the highest average reward on 30 of 49 Atari games among the methods tested. PPO became the default policy optimization algorithm for large-scale RL applications, demonstrating that constraining the magnitude of policy updates is essential for stable optimization.
4.2.3 Soft Actor-Critic (2018)
Haarnoja et al. ( 2018) introduced Soft Actor-Critic (SAC), which adds entropy regularization to the actor-critic framework. The agent maximizes expected return plus an entropy bonus:
J ( θ ) = 𝔼 π θ [ ∑ t = 0 ∞ γ t ( r t + τ ℋ ( π θ ( ⋅ | s t ) ) ) ] J(\theta)=\mathbb{E}{\pi{\theta}}\left[\sum_{t=0}^{\infty}\gamma^{t}\left(r_{t}+\tau\mathcal{H}(\pi_{\theta}(\cdot|s_{t}))\right)\right]
(27)
where ℋ  ( π ) = − ∑ a π  ( a )  log  π  ( a ) \mathcal{H}(\pi)=-\sum_{a}\pi(a)\log\pi(a) is the entropy and τ > 0 \tau>0 is a temperature parameter. The entropy bonus encourages exploration by penalizing deterministic policies. The optimal policy under this objective is softmax in the Q-values: π ∗  ( a | s ) ∝ exp  ( Q ∗  ( s , a ) / τ ) \pi^{}(a|s)\propto\exp(Q^{}(s,a)/\tau) , connecting to discrete choice models in econometrics.
SAC maintains two Q-networks (to reduce overestimation bias) and a policy network. The soft Bellman operator for the critic is:
( T π  Q )  ( s , a ) = r  ( s , a ) + γ  𝔼 s ′  [ V  ( s ′ ) ] , V  ( s ) = 𝔼 a ∼ π  [ Q  ( s , a ) − τ  log  π  ( a | s ) ] (T^{\pi}Q)(s,a)=r(s,a)+\gamma\mathbb{E}{s^{\prime}}\left[V(s^{\prime})\right],\quad V(s)=\mathbb{E}{a\sim\pi}[Q(s,a)-\tau\log\pi(a|s)]
(28)
SAC is off-policy (using experience replay), handles continuous actions naturally, and achieves state-of-the-art sample efficiency on continuous control benchmarks. The entropy regularization provides automatic exploration without ε \varepsilon -greedy schedules. 
Figure 1: Architecture comparison of the three fundamental algorithm families. (a) DQN maps states to Q-values for all actions, selecting the argmax. (b) REINFORCE maps states to a probability distribution over actions, then samples. (c) Actor-Critic maintains separate policy and value networks; the critic's TD error δ t \delta_{t} provides a low-variance learning signal to the actor.
4.2.4 AlphaGo Zero (2017)
The game of Go has approximately 10 170 10^{170} legal positions and a branching factor of roughly 250, far beyond the reach of brute-force search. Hand-crafted evaluation functions, which had succeeded in chess, failed here because positional concepts like influence, territory, and group viability are holistic and contextual. Monte Carlo tree search (MCTS) had achieved amateur-level play by using random simulations to estimate position values, but progress had stalled below professional strength. Silver et al. ( 2016) broke through by combining supervised learning from 30 million human expert positions, reinforcement learning via self-play, and MCTS with learned value and policy networks; the resulting system defeated Lee Sedol four games to one in March 2016. A year later, Silver et al. ( 2017) showed that none of the human data was necessary.
AlphaGo Zero uses a single convolutional neural network f θ  ( s ) = ( 𝐩 , v ) f_{\theta}(s)=(\mathbf{p},v) that takes a board position s s and outputs both a policy vector 𝐩 \mathbf{p} over legal moves and a scalar value v v estimating the probability of winning. The input representation consists of 17 binary planes on the 19 × 19 19\times 19 board encoding the raw game state without hand-crafted features. 40 40 40 Eight planes for Black's stone positions over the last eight moves, eight for White's, and one indicating which color plays next. The history planes allow the network to detect ko situations and infer the trajectory of play. The architecture uses residual blocks, 41 41 41 A residual block computes 𝐱 + g  ( 𝐱 ) \mathbf{x}+g(\mathbf{x}) rather than just g  ( 𝐱 ) g(\mathbf{x}) , where g g is a learned transformation. The skip connection allows gradients to flow through very deep networks without vanishing. AlphaGo Zero's 40-block architecture has 79 parameterized layers. which allow training of very deep networks.
During play, each move is selected by running MCTS, which conducts 1,600 simulated games from the current position to estimate move quality. Each simulation proceeds in four phases, illustrated in Figure 2. In the selection phase, the algorithm starts from the current position and traverses the partially built search tree by choosing at each node the action that maximizes Q  ( s , a ) + c puct ⋅ P  ( s , a ) ⋅ ∑ b N  ( s , b ) / ( 1 + N  ( s , a ) ) Q(s,a)+c_{\text{puct}}\cdot P(s,a)\cdot\sqrt{\sum_{b}N(s,b)},/,(1+N(s,a)) , where Q  ( s , a ) Q(s,a) is the current average value of action a a , P  ( s , a ) P(s,a) is the prior probability from the neural network, and N  ( s , a ) N(s,a) is the visit count. 42 42 42 The constant c puct c_{\text{puct}} controls exploration. Actions visited often have well-estimated Q Q values but a shrinking exploration bonus; rarely visited actions have uncertain values but a large bonus. This is a continuous analogue of the upper confidence bound (UCB) strategy from bandit theory. In the expansion and evaluation phase, when the traversal reaches a position not yet in the tree, the neural network evaluates it in a single forward pass, producing a policy vector 𝐩 \mathbf{p} and a value estimate v v ; the policy initializes prior probabilities P  ( s ′ , a ) = p a P(s^{\prime},a)=p_{a} for each child edge. In the backup phase, the value v v propagates back up the traversed path, incrementing each edge's visit count N  ( s , a ) N(s,a) and updating its mean value Q  ( s , a ) Q(s,a) . After all 1,600 simulations, the algorithm selects the move with the highest visit count at the root.
(a) Selection (b) Expansion f θ f_{\theta} ( 𝐩 , v ) (\mathbf{p},v) (c) Evaluation v v (d) Backup Figure 2: The four phases of a single MCTS simulation in AlphaGo Zero. (a) Selection traverses the tree from the root, choosing at each node the action maximizing a UCB-like score balancing exploitation ( Q Q ) and exploration ( P / N P/N ). (b) Expansion adds a new leaf node when the traversal reaches an unexplored position. (c) The neural network f θ f_{\theta} evaluates the new position, producing move priors 𝐩 \mathbf{p} and a value estimate v v . (d) Backup propagates v v along the traversed path, updating mean values Q  ( s , a ) Q(s,a) and visit counts N  ( s , a ) N(s,a) at each edge.
The training loop generates self-play games. At each board position s t s_{t} during a game, the program runs MCTS to produce improved move probabilities 𝝅 t \boldsymbol{\pi}{t} , where π t  ( a ) ∝ N  ( s t , a ) 1 / τ \pi{t}(a)\propto N(s_{t},a)^{1/\tau} and τ \tau is a temperature parameter controlling exploration. 43 43 43 Early in the game ( t ≤ 30 t\leq 30 ), τ = 1 \tau=1 so moves are sampled proportionally to visit counts, encouraging diverse openings. Later, τ → 0 \tau\to 0 and the most-visited move is selected deterministically. Dirichlet noise is also added to root priors, P  ( s , a ) = ( 1 − ε )  p a + ε  η a P(s,a)=(1-\varepsilon)p_{a}+\varepsilon\eta_{a} with η ∼ Dir  ( 0.03 ) \eta\sim\text{Dir}(0.03) , ensuring all legal moves can be explored despite strong network priors. A move a t a_{t} is sampled from 𝝅 t \boldsymbol{\pi}{t} and played. At game end, the outcome z ∈ { − 1 , + 1 } z\in{-1,+1} is recorded. Each position becomes a training triple ( s t , 𝝅 t , z ) (s{t},\boldsymbol{\pi}_{t},z) , and the network parameters are updated to minimize
ℓ  ( θ ) = ( z − v ) 2 − 𝝅 ⊤  log  𝐩 + c  ‖ θ ‖ 2 \ell(\theta)=(z-v)^{2}-\boldsymbol{\pi}^{\top}\log\mathbf{p}+c|\theta|^{2}
(29)
where the first term is a value prediction loss, the second is a policy cross-entropy loss, 44 44 44 The cross-entropy loss − 𝝅 ⊤  log  𝐩 -\boldsymbol{\pi}^{\top}\log\mathbf{p} measures how well the predicted distribution 𝐩 \mathbf{p} matches the target 𝝅 \boldsymbol{\pi} ; it equals zero when the distributions are identical. and the third is L 2 L_{2} regularization. 45 45 45 L 2 L_{2} regularization penalizes the squared magnitude of parameters, c  ‖ θ ‖ 2 c|\theta|^{2} , analogous to ridge regression in econometrics. The key mechanism is a virtuous cycle. MCTS serves as a policy improvement operator, since the search probabilities 𝝅 \boldsymbol{\pi} are stronger than the raw network outputs 𝐩 \mathbf{p} . Training the network to match 𝝅 \boldsymbol{\pi} distills the search improvements back into the network, and the improved network in turn produces better MCTS. After 72 hours of self-play on 4 TPUs, AlphaGo Zero surpassed all previous versions, including the one that defeated Lee Sedol, and discovered novel strategies not previously seen in human play. 46 46 46 The system that defeated Lee Sedol in March 2016 used fixed network weights throughout the match; no parameter updates occurred between or during games. This illustrates the training-execution distinction (Section 2): the months of self-play constituted the training phase, while the five-game match was purely execution.
Go was well-suited to this architecture. Its fixed 19 × 19 19\times 19 board maps naturally to convolutional networks, its perfect information and deterministic transitions make MCTS's tree structure exact, and the binary game outcome provides an unambiguous training signal. Igami ( 2020) interprets the architecture in econometric terms, where the policy network is a conditional choice probability (CCP) estimator, the value network is a conditional value function (CVF) estimator, and the system performs CCP estimation and forward simulation jointly, connecting to the approach of Hotz and Miller ( 1993) in dynamic discrete choice.
5 The Theory of Reinforcement Learning
5.1 The Geometry of Dynamic Programming
Value iteration (VI) and policy iteration (PI) are the workhorses of dynamic programming. VI applies the Bellman operator repeatedly until convergence; PI alternates between policy evaluation (solving a linear system) and policy improvement (taking the greedy action). PI converges faster. Why? The answer reveals a connection between dynamic programming and numerical optimization. Policy iteration is Newton's method applied to the Bellman equation.
5.1.1 Value Iteration as Picard Iteration
Consider the Bellman optimality operator T T acting on value functions.
( T  V )  ( s ) = max a ∈ 𝒜  { r  ( s , a ) + γ  ∑ s ′ ∈ 𝒮 P  ( s ′ | s , a )  V  ( s ′ ) } . (TV)(s)=\max_{a\in\mathcal{A}}\left{r(s,a)+\gamma\sum_{s^{\prime}\in\mathcal{S}}P(s^{\prime}|s,a)V(s^{\prime})\right}.
(30)
This operator is nonlinear due to the max \max . Value iteration applies T T repeatedly: V k + 1 = T  V k V_{k+1}=TV_{k} . Since T T is a γ \gamma -contraction in the supremum norm (Denardo, 1967) , Banach's fixed-point theorem guarantees ‖ V k − V ∗ ‖ ∞ ≤ γ k  ‖ V 0 − V ∗ ‖ ∞ |V_{k}-V^{}|{\infty}\leq\gamma^{k}|V{0}-V^{}|{\infty} . 47 47 47 This is the Contraction Mapping Theorem. The identical mathematical structure governs convergence of value function iteration in consumption-savings models, competitive equilibrium computation, and Bellman equation solution. This is Picard iteration, with linear convergence at rate γ \gamma . 48 48 48 Picard iteration is x k + 1 = f  ( x k ) x{k+1}=f(x_{k}) for finding roots of x = f  ( x ) x=f(x) . When f f is a contraction, convergence is geometric. The rate γ \gamma means each iteration reduces the error by a fixed proportion; more patient agents (higher γ \gamma ) face slower convergence because the operator contracts less per step. The iteration count to reduce error by a factor of δ \delta is k = log  ( δ ) / log  ( 1 / γ ) k=\log(\delta)/\log(1/\gamma) (Bertsekas, 1996) .
5.1.2 Policy Iteration as Newton's Method
Policy iteration takes a different approach. At the current value estimate V ~ \tilde{V} , define the greedy policy π ~  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V ~  ( s ′ ) } \tilde{\pi}(s)=\mathop{\it argmax}{a}{r(s,a)+\gamma\sum{s^{\prime}}P(s^{\prime}|s,a)\tilde{V}(s^{\prime})} . The policy evaluation step solves the linear fixed-point equation V = T π ~  V V=T^{\tilde{\pi}}V exactly, where T π ~ T^{\tilde{\pi}} is the policy-specific Bellman operator
( T π ~  V )  ( s ) = r  ( s , π ~  ( s ) ) + γ  ∑ s ′ P  ( s ′ | s , π ~  ( s ) )  V  ( s ′ ) . (T^{\tilde{\pi}}V)(s)=r(s,\tilde{\pi}(s))+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,\tilde{\pi}(s))V(s^{\prime}).
(31)
The geometric structure, formalized by Puterman and Brumelle ( 1979) , is as follows: the linear operator T π ~ T^{\tilde{\pi}} is a supporting hyperplane to the nonlinear operator T T at the current iterate. 49 49 49 A supporting hyperplane to a convex function at x 0 x_{0} is a linear function ℓ \ell with ℓ  ( x 0 ) = f  ( x 0 ) \ell(x_{0})=f(x_{0}) and ℓ  ( x ) ≤ f  ( x ) \ell(x)\leq f(x) everywhere. In plainer terms: T π ~ T^{\tilde{\pi}} is the tangent-line approximation to T T from elementary calculus, extended to function spaces. The policy operator T π ~ T^{\tilde{\pi}} plays this role for the Bellman operator. Specifically, the operators satisfy tangency: T π ~  V ~ = T  V ~ T^{\tilde{\pi}}\tilde{V}=T\tilde{V} , so the linearization agrees with the nonlinear operator at the current iterate. They also satisfy support: T π ~  V ≤ T  V T^{\tilde{\pi}}V\leq TV for all V V , meaning the linear operator lies weakly below the nonlinear one everywhere, just as a tangent line lies below a convex function. Policy evaluation solves for the fixed point of this linearization exactly. This is precisely the structure of Newton's method; linearize the nonlinear equation at the current point, solve the linearized system, and iterate. 50 50 50 The Newton interpretation of policy iteration has precursors in Kleinman ( 1968) for Riccati equations in linear-quadratic control and Pollatschek and Avi-Itzhak ( 1969) for stochastic games. 51 51 51 Algebraically: consider finding the root of G  ( V ) = V − T  V = 0 G(V)=V-TV=0 . The Bellman operator T T is piecewise affine, not smooth: T T is affine on each region where the greedy policy is constant, with kinks at boundaries where the optimal action switches. This makes G G a semismooth function in the sense of Qi and Sun ( 1993) . At any iterate V k V_{k} where the greedy policy π ~ \tilde{\pi} is unique (a generic condition), T T is locally affine: T  V = r π ~ + γ  P π ~  V TV=r^{\tilde{\pi}}+\gamma P^{\tilde{\pi}}V , so G ′  ( V k ) = I − γ  P π ~ G^{\prime}(V_{k})=I-\gamma P^{\tilde{\pi}} . The Newton step V k + 1 = V k − [ G ′  ( V k ) ] − 1  G  ( V k ) = ( I − γ  P π ~ ) − 1  r π ~ V_{k+1}=V_{k}-[G^{\prime}(V_{k})]^{-1}G(V_{k})=(I-\gamma P^{\tilde{\pi}})^{-1}r^{\tilde{\pi}} is exactly the policy evaluation solution. At the non-smooth boundary points where two actions tie, any element of the B-subdifferential yields the same iterate because the two candidate linearizations produce the same fixed point.
Theorem 1 (Policy Improvement, Howard ( 1960) ).
Let π k \pi_{k} be the current policy with value V π k V^{\pi_{k}} , and let π k + 1 \pi_{k+1} be the greedy policy with respect to V π k V^{\pi_{k}} :
π k + 1  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a ∈ 𝒜 { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V π k  ( s ′ ) } . \pi_{k+1}(s)=\mathop{\it argmax}{a\in\mathcal{A}}\left{r(s,a)+\gamma\sum{s^{\prime}}P(s^{\prime}|s,a),V^{\pi_{k}}(s^{\prime})\right}.
(32)
Then V π k + 1  ( s ) ≥ V π k  ( s ) V^{\pi_{k+1}}(s)\geq V^{\pi_{k}}(s) for all s ∈ 𝒮 s\in\mathcal{S} , with strict inequality at some state unless π k \pi_{k} is already optimal.
The consequence is finite termination. Since there are at most | 𝒜 | | 𝒮 | |\mathcal{A}|^{|\mathcal{S}|} deterministic policies and each PI step strictly improves the value function (Theorem 1), PI reaches the exact optimum in finitely many iterations. While VI requires k = log  ( 100 ) / log  ( 1 / γ ) k=\log(100)/\log(1/\gamma) iterations to reduce error by a factor of 100 (Bertsekas, 1996) , PI typically converges in 5–10 iterations regardless of γ \gamma . 52 52 52 Ye ( 2011) proves PI is strongly polynomial with iteration count O  ( | 𝒮 |  | 𝒜 | 1 − γ  log  | 𝒮 | 1 − γ ) O!\left(\frac{|\mathcal{S}||\mathcal{A}|}{1-\gamma}\log\frac{|\mathcal{S}|}{1-\gamma}\right) , resolving a long-standing conjecture. This bound is for fixed γ \gamma ; Fearnley ( 2010) constructs examples requiring exponentially many iterations when γ \gamma is allowed to vary with | 𝒮 | |\mathcal{S}| . 53 53 53 For continuous-state problems discretized on a grid (the norm in economics), the finite-termination argument still applies to the discretized problem, but the number of grid points n n enters the bound. Santos and Rust ( 2004) establish a three-tier convergence result for PI applied to discretized dynamic programs: order ≈ 1.5 \approx 1.5 globally for general interpolation schemes, quadratic convergence locally when the value function approximation is concave and piecewise linear, and superlinear convergence for general smooth interpolation. The formal error constants C  ( h ) C(h) in their quadratic bound degrade as the grid mesh h → 0 h\to 0 , but the iteration count is empirically independent of grid size. At γ = 0.90 \gamma=0.90 , VI needs 44 iterations while PI needs only 5–8; at γ = 0.95 \gamma=0.95 , VI requires 90 versus 5–8; at γ = 0.99 \gamma=0.99 , VI needs 459 iterations while PI still converges in 5–10.
Bertsekas ( 2022b) extends this interpretation to a broad class of dynamic programming problems. The Newton structure applies whenever the Bellman operator can be written as a pointwise maximum over linear operators: T = max π  T π T=\max_{\pi}T^{\pi} . This includes not only infinite horizon problems with discounting but also optimal stopping problems (job search, option exercise), average cost optimization (inventory, queueing), and minimax formulations for adversarial settings. 54 54 54 Rust ( 1996) surveys successive approximation and policy iteration methods for economic models, comparing their performance on the bus engine replacement problem. Zhang ( 2023) extends randomized policy iteration to multi-agent problems where the control is m m -dimensional, reducing per-iteration complexity from exponential to linear in m m . 55 55 55 These problems appear under different names such as “stochastic shortest path” for optimal stopping, “average-cost MDP” for long-run average optimization, and “model predictive control” (or receding-horizon control) for finite-horizon replanning. The practical implication is that algorithms with policy-improvement structure (evaluate a policy exactly or approximately, then improve) inherit Newton-like convergence behavior, while pure value-iteration methods (apply T T directly) are limited to linear convergence. 56 56 56 Blackwell ( 1965) proves that for discounted MDPs with finite state and action spaces, a stationary deterministic policy π : 𝒮 → 𝒜 \pi:\mathcal{S}\to\mathcal{A} exists that is optimal for all initial states simultaneously. This “uniform optimality” has three implications: (1) the search space reduces from history-dependent or stochastic policies to static maps, justifying neural networks that condition only on current state; (2) the optimal policy is independent of the initial distribution d 0 d_{0} , so changing where episodes start does not require retraining; (3) PI and VI are guaranteed to converge to the same globally optimal policy regardless of initialization.
5.1.3 Simulation Study: The Brock–Mirman Economy
The Brock and Mirman ( 1972) optimal growth model provides a concrete demonstration. A planner chooses capital k ′ k^{\prime} to maximize ∑ t = 0 ∞ β t  log  ( c t ) \sum_{t=0}^{\infty}\beta^{t}\log(c_{t}) subject to the resource constraint c t + k t + 1 = z t  k t α c_{t}+k_{t+1}=z_{t}k_{t}^{\alpha} , where productivity z t ∈ { 0.9 , 1.1 } z_{t}\in{0.9,1.1} follows a Markov chain with persistence 0.8. I set α = 0.36 \alpha=0.36 , β = 0.96 \beta=0.96 , and discretize capital on a 500-point grid covering two productivity states (1,000 states). This model admits the closed-form policy k ′  ( k , z ) = α  β  z  k α k^{\prime}(k,z)=\alpha\beta zk^{\alpha} , providing an exact benchmark.
The discretized model makes the PI–Newton equivalence concrete. Define the Bellman residual G  ( V ) = V − T  V G(V)=V-TV on ℝ n \mathbb{R}^{n} where n = 1 , 000 n=1{,}000 (500 capital grid points × \times 2 productivity states). At iterate V k V_{k} , let π k \pi_{k} denote the greedy policy. Since π k \pi_{k} is unique at V k V_{k} (generically), T T is locally affine: T  V = r π k + γ  P π k  V TV=r^{\pi_{k}}+\gamma P^{\pi_{k}}V , so the residual becomes G  ( V ) = ( I − γ  P π k )  V − r π k G(V)=(I-\gamma P^{\pi_{k}})V-r^{\pi_{k}} with Jacobian G ′  ( V k ) = I − γ  P π k G^{\prime}(V_{k})=I-\gamma P^{\pi_{k}} . The Newton update is
V k + 1 = V k − [ G ′  ( V k ) ] − 1  G  ( V k ) = ( I − γ  P π k ) − 1  r π k , V_{k+1}=V_{k}-[G^{\prime}(V_{k})]^{-1},G(V_{k})=(I-\gamma P^{\pi_{k}})^{-1},r^{\pi_{k}},
(33)
which is exactly the policy evaluation step: solving V = r π k + γ  P π k  V V=r^{\pi_{k}}+\gamma P^{\pi_{k}}V for V V . Each PI iteration is one Newton step on the Bellman residual, explaining the 11-iteration convergence on a 1,000-state problem. 57 57 57 Santos and Rust ( 2004) is the definitive reference on PI convergence for discretized economic models of precisely this type. Their analysis of the Brock–Mirman growth model establishes that PI iteration counts are empirically independent of grid resolution (7–11 iterations across all grid sizes in Table 3), consistent with the Newton interpretation: Newton's method converges in a number of steps determined by the nonlinearity of the operator, not the dimension of the discretization.
The VI iteration count follows from the contraction bound: each iteration reduces the Bellman residual by the factor β = 0.96 \beta=0.96 , requiring k = ⌈ log  ( ϵ / ‖ T  V 0 − V 0 ‖ ∞ ) / log  β ⌉ = 567 k=\lceil\log(\epsilon/|TV_{0}-V_{0}|_{\infty})/\log\beta\rceil=567 iterations for tolerance ϵ = 10 − 10 \epsilon=10^{-10} . 58 58 58 At β = 0.99 \beta=0.99 , the weaker contraction yields approximately four times as many iterations, since log  ( 0.96 ) / log  ( 0.99 ) ≈ 4 \log(0.96)/\log(0.99)\approx 4 .
Figure 3(a)–(b) provide a geometric interpretation for a scalar Bellman equation with three policies. Each policy operator T π i  V = r π i + γ i  V T^{\pi_{i}}V=r^{\pi_{i}}+\gamma_{i}V is affine; the Bellman operator T = max i  T π i T=\max_{i}T^{\pi_{i}} is their upper envelope, a convex piecewise-linear function. Panel (a) shows VI: the staircase iterates V k + 1 = T  V k V_{k+1}=TV_{k} by alternating between the T T curve and the 45 ∘ 45^{\circ} line, converging at the linear rate γ \gamma . Panel (b) shows PI: at each iterate, the algorithm identifies the active policy operator and solves for its fixed point on the 45 ∘ 45^{\circ} line, jumping directly to the intersection. This is a Newton step, where each T π k T^{\pi_{k}} is a supporting hyperplane to T T at V k V_{k} , and the fixed point of the linearization is the Newton iterate. The scalar picture extends to ℝ n \mathbb{R}^{n} : the affine operator T π k  V = r π k + γ  P π k  V T^{\pi_{k}}V=r^{\pi_{k}}+\gamma P^{\pi_{k}}V supports T T at V k V_{k} , and its fixed point ( I − γ  P π k ) − 1  r π k (I-\gamma P^{\pi_{k}})^{-1}r^{\pi_{k}} is the Newton iterate from equation ( 33). Finite termination follows because T T has finitely many affine pieces; the iteration count depends on the number of policy switches, not the state-space dimension.
Table 3 and Figure 3 confirm the theory. VI requires 567 iterations at rate β n = 0.96 n \beta^{n}=0.96^{n} ; PI converges in 11, a 50 × 50\times reduction predicted by the Newton interpretation. The Manne ( 1960) LP recovers the same value function to solver precision ( ‖ V LP − V VI ‖ ∞ < 10 − 8 |V_{\text{LP}}-V_{\text{VI}}|{\infty}<10^{-8} ). 59 59 59 PI wall-clock time scales favorably: at n k = 200 n{k}=200 , PI is roughly 50 × 50\times faster than VI (Table 3), because the O  ( n 3 ) O(n^{3}) per-iteration cost of policy evaluation is offset by 7–10 total iterations versus 567. 
Figure 3: The Brock–Mirman economy ( α = 0.36 \alpha=0.36 , β = 0.96 \beta=0.96 , 1,000 states). (a) Value iteration on a scalar Bellman equation. The staircase iterates V k + 1 = T  V k V_{k+1}=TV_{k} , converging at the linear rate γ \gamma . (b) Policy iteration as Newton's method. Each step solves for the fixed point of the active policy operator T π k T^{\pi_{k}} , jumping to the tangent line's intersection with the diagonal. (c) Sup-norm error ‖ V k − V ∗ ‖ ∞ |V_{k}-V^{*}|_{\infty} for the discretized model; VI requires 567 iterations, PI converges in 11. Table 3: Brock–Mirman Economy: VI vs PI vs LP
5.2 Value Learning Methods
5.2.1 Stochastic Approximation Foundations
When P P is unknown, a single sampled transition ( s , a , r , s ′ ) (s,a,r,s^{\prime}) can replace the expectation 𝔼 s ′ ∼ P ( ⋅ | s , a )  [ V  ( s ′ ) ] \mathbb{E}_{s^{\prime}\sim P(\cdot|s,a)}[V(s^{\prime})] . The mathematical foundation is stochastic approximation, developed by Robbins ( 1952) . 60 60 60 The modern theory of stochastic approximation, including convergence rates and the ODE (ordinary differential equation) method for analyzing iterates, is developed in Kushner and Clark ( 1978) and Borkar and Meyn ( 2000) . The ODE method shows that the expected trajectory of the stochastic iterates tracks the solution of a deterministic differential equation x ˙ = − g  ( x ) \dot{x}=-g(x) , providing stability conditions via Lyapunov theory. Consider the problem of finding x ∗ x^{} such that g  ( x ∗ ) = 0 g(x^{})=0 , where g g cannot be evaluated directly but one can observe noisy samples g  ( x ) + ϵ g(x)+\epsilon . The Robbins-Monro iteration is:
x t + 1 = x t − α t  [ g  ( x t ) + ϵ t ] , x_{t+1}=x_{t}-\alpha_{t}[g(x_{t})+\epsilon_{t}],
(34)
where ϵ t \epsilon_{t} is zero-mean noise. Under two conditions on the step sizes, this converges to x ∗ x^{*} with probability one. The conditions are ∑ t = 0 ∞ α t = ∞ \sum_{t=0}^{\infty}\alpha_{t}=\infty (sufficient exploration, ensuring that learning never ceases) and ∑ t = 0 ∞ α t 2 < ∞ \sum_{t=0}^{\infty}\alpha_{t}^{2}<\infty (diminishing noise, ensuring the variance of cumulative updates is finite). The canonical choice α t = 1 / ( t + 1 ) \alpha_{t}=1/(t+1) satisfies both conditions.
5.2.2 Q-Learning and SARSA
Q-learning (Watkins and Dayan, 1992) is Robbins-Monro applied to the Bellman equation for action-value functions. 61 61 61 The “Q” in Q-learning stands for “quality,” following Watkins and Dayan ( 1992) , who used Q  ( s , a ) Q(s,a) to denote the quality (expected return) of taking action a a in state s s . The term “Q-factor” is used interchangeably with “action-value function” throughout the RL literature. Define the Q-factor Bellman operator:
( F  Q )  ( s , a ) = r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  max a ′  Q  ( s ′ , a ′ ) . (FQ)(s,a)=r(s,a)+\gamma\sum_{s^{\prime}}P(s^{\prime}|s,a)\max_{a^{\prime}}Q(s^{\prime},a^{\prime}).
(35)
The Q-learning update, upon observing transition ( s t , a t , r t , s t + 1 ) (s_{t},a_{t},r_{t},s_{t+1}) , is
Q  ( s t , a t ) ← Q  ( s t , a t ) + α t  [ r t + γ  max a ′  Q  ( s t + 1 , a ′ ) − Q  ( s t , a t ) ] . Q(s_{t},a_{t})\leftarrow Q(s_{t},a_{t})+\alpha_{t}\left[r_{t}+\gamma\max_{a^{\prime}}Q(s_{t+1},a^{\prime})-Q(s_{t},a_{t})\right].
(36)
The logic of Q-learning is best understood as a Monte Carlo approximation of the Bellman contraction. The true Bellman operator involves an integral over the transition distribution, ( F  Q )  ( s , a ) = r + γ  ∫ max a ′  Q  ( s ′ , a ′ )  𝑑 P  ( s ′ | s , a ) (FQ)(s,a)=r+\gamma\int\max_{a^{\prime}}Q(s^{\prime},a^{\prime}),dP(s^{\prime}|s,a) . Since P P is unknown, this integral cannot be computed analytically. However, a sample transition ( s , a , r , s ′ ) (s,a,r,s^{\prime}) acts as a single-point Monte Carlo estimate of this integral. The Q-learning update is simply an exponential moving average (with weight α t \alpha_{t} ) between the current estimate and this noisy Monte Carlo target. Because F F is a γ \gamma -contraction in the supremum norm, the expected update drives the estimate toward the fixed point Q ∗ Q^{*} , provided the noise in the Monte Carlo sample averages out over time (which the Robbins-Monro conditions ensure) (Tsitsiklis, 1994) . 62 62 62 Q-learning can be viewed as root-finding for the expected Bellman residual: the goal is to find parameters such that 𝔼 ( s , a , r , s ′ )  [ δ t ] = 0 \mathbb{E}{(s,a,r,s^{\prime})}[\delta{t}]=0 , where δ t = r + γ  max a ′  Q  ( s ′ , a ′ ) − Q  ( s , a ) \delta_{t}=r+\gamma\max_{a^{\prime}}Q(s^{\prime},a^{\prime})-Q(s,a) is the temporal difference error. The update is a stochastic gradient step on the mean-squared Bellman error, but with a critical distinction: the gradient is “semi-gradient” because the target max a ′  Q  ( s ′ , a ′ ) \max_{a^{\prime}}Q(s^{\prime},a^{\prime}) is treated as a fixed constant rather than a function of the parameters being updated. This simplifies computation but disconnects the update from true gradient descent, requiring the specific stability conditions of Tsitsiklis ( 1994) .
Convergence requires two conditions. Exploration (visiting all state-action pairs infinitely often) ensures identification. The Robbins-Monro step-size conditions ( ∑ t α t = ∞ \sum_{t}\alpha_{t}=\infty , ∑ t α t 2 < ∞ \sum_{t}\alpha_{t}^{2}<\infty ) balance tracking versus noise suppression. Watkins and Dayan ( 1992) and Jaakkola et al. ( 1994) formalize these; Tsitsiklis ( 1994) provides the general framework.
The choice of step-size schedule has quantitative consequences: Even-Dar and Mansour ( 2003) show that polynomial schedules α t = 1 / t ω \alpha_{t}=1/t^{\omega} with ω ∈ ( 1 / 2 , 1 ) \omega\in(1/2,1) achieve convergence rate O  ( 1 / t 1 − ω ) O(1/t^{1-\omega}) , creating an explicit tradeoff between speed and stability. Recent work by Li et al. ( 2024a) establishes that Q-learning with variance-reduced updates achieves minimax-optimal sample complexity O ~  ( | 𝒮 |  | 𝒜 | / ( 1 − γ ) 3  ϵ 2 ) \tilde{O}(|\mathcal{S}||\mathcal{A}|/(1-\gamma)^{3}\epsilon^{2}) , matching information-theoretic lower bounds. 63 63 63 Vanilla Q-learning (without variance reduction) has tight complexity Θ ~  ( | 𝒮 |  | 𝒜 | / ( 1 − γ ) 4  ϵ 2 ) \tilde{\Theta}(|\mathcal{S}||\mathcal{A}|/(1-\gamma)^{4}\epsilon^{2}) , worse by a factor of 1 / ( 1 − γ ) 1/(1-\gamma) due to maximization bias inflating variance. The optimal cubic rate requires variance-reduced updates (Wainwright, 2019; Sidford et al., 2018) . By contrast, naive model-based RL (estimate P ^ \hat{P} from samples, then solve by planning) achieves the optimal ( 1 − γ ) − 3 (1-\gamma)^{-3} rate with no special tricks (Agarwal et al., 2020b) , illustrating the statistical cost of discarding transition structure. Model-free learning is possible. The optimal value function can be found without ever estimating the transition probabilities. 64 64 64 Model-free methods are essential when (a) the environment is a physical system with dynamics too complex to write down, or (b) the agent learns directly from interaction. Note that “model-free” does not mean “atheoretical.” The agent does not store P  ( s ′ | s , a ) P(s^{\prime}|s,a) explicitly, but the Q-function serves as an implicit model encoding long-run consequences.
SARSA provides an on-policy variant. 65 65 65 SARSA is named for the quintuple ( S t , A t , R t , S t + 1 , A t + 1 ) (S_{t},A_{t},R_{t},S_{t+1},A_{t+1}) used in each update (Rummery and Niranjan, 1994) . Convergence requires the GLIE (Greedy in the Limit with Infinite Exploration) condition: the behavior policy must explore all actions infinitely often while converging to a greedy policy. ε \varepsilon -greedy with ε t → 0 \varepsilon_{t}\to 0 satisfies this. Instead of taking the maximum over next actions, SARSA uses the action actually taken:
Q  ( s t , a t ) ← Q  ( s t , a t ) + α t  [ r t + γ  Q  ( s t + 1 , a t + 1 ) − Q  ( s t , a t ) ] . Q(s_{t},a_{t})\leftarrow Q(s_{t},a_{t})+\alpha_{t}\left[r_{t}+\gamma Q(s_{t+1},a_{t+1})-Q(s_{t},a_{t})\right].
(37)
This solves for the value function of the behavior policy π \pi rather than the optimal policy. Singh et al. ( 2000) prove convergence under the same step-size conditions, provided the behavior policy converges to a stationary distribution. Q-learning is noisy value iteration on Q-factors; SARSA is noisy policy evaluation. 66 66 66 Bhandari et al. ( 2021) provide finite-time analysis of TD learning, showing that the convergence rate depends on the mixing time of the Markov chain under the behavior policy. Faster mixing (less serial correlation in the state sequence) yields faster convergence. The Robbins-Monro conditions ensure that the noise averages out faster than the signal decays, allowing asymptotic convergence despite using only single-sample estimates.
5.2.3 Multi-Step Returns and TD( λ \lambda )
The updates in ( 36) bootstrap from a single successor state. More generally, one can bootstrap from n n steps ahead. The n n -step return is
G t ( n ) = ∑ k = 0 n − 1 γ k  R t + k + 1 + γ n  V  ( S t + n ) . G_{t}^{(n)}=\sum_{k=0}^{n-1}\gamma^{k}R_{t+k+1}+\gamma^{n}V(S_{t+n}).
(38)
Setting n = 1 n=1 recovers the TD(0) target; letting n → ∞ n\to\infty (or reaching a terminal state) gives the Monte Carlo return.
The λ \lambda -return (Sutton, 1988) averages all n n -step returns with geometrically decaying weights:
G t λ = ( 1 − λ )  ∑ n = 1 ∞ λ n − 1  G t ( n ) , λ ∈ [ 0 , 1 ] . G_{t}^{\lambda}=(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}G_{t}^{(n)},\qquad\lambda\in[0,1].
(39)
This is the forward view: at time t t , look forward at all possible truncation horizons and take a weighted average. The parameter λ \lambda controls a bias-variance tradeoff: lower λ \lambda gives higher bias (more bootstrapping) but lower variance; higher λ \lambda gives lower bias but higher variance, since more of the update relies on stochastic returns rather than value estimates.
The forward view requires waiting until the end of the episode to compute G t λ G_{t}^{\lambda} . The backward view computes the same total update incrementally. At each step, compute one TD error δ t = R t + 1 + γ  V  ( S t + 1 ) − V  ( S t ) \delta_{t}=R_{t+1}+\gamma V(S_{t+1})-V(S_{t}) and distribute it to all states via an eligibility trace:
e t  ( s ) = γ  λ  e t − 1  ( s ) + 𝟙  { s = S t } , V  ( s ) ← V  ( s ) + α  δ t  e t  ( s ) . e_{t}(s)=\gamma\lambda,e_{t-1}(s)+\mathbbm{1}{s=S_{t}},\qquad V(s)\leftarrow V(s)+\alpha,\delta_{t},e_{t}(s).
(40)
The trace e t  ( s ) e_{t}(s) acts as a fading memory of recently visited states: it spikes when s s is visited and decays by γ  λ \gamma\lambda per step. Each TD error δ t \delta_{t} updates every state in proportion to its current trace, enabling O  ( | 𝒮 | ) O(|\mathcal{S}|) per-step credit assignment without storing trajectories. 67 67 67 The forward and backward views produce identical total weight changes over a complete episode (Sutton, 1988) . The backward view is preferred in practice because it operates online (updating after each transition) rather than requiring the full episode to be stored. Practical variants include replacing traces ( e t  ( s ) = 1 e_{t}(s)=1 when s = S t s=S_{t} , capping the trace at 1 instead of accumulating), Dutch traces (van Seijen et al., 2016) , and off-policy extensions such as Retrace( λ \lambda ) (Munos et al., 2016) and V-trace (Espeholt et al., 2018) . The historical development of eligibility traces is discussed in Section 3.
Under linear function approximation, TD( λ \lambda ) converges to a unique fixed point with approximation error bounded by 1 − λ  γ 1 − γ 2 \frac{1-\lambda\gamma}{\sqrt{1-\gamma^{2}}} times the best-in-class error (Equation 46 and the bound in Section 5.3; Tsitsiklis and Van Roy, 1997 ). Higher λ \lambda tightens this bound, approaching the projection of V π V^{\pi} as λ → 1 \lambda\to 1 .
5.2.4 Simulation Study: Credit Assignment in a Corridor
A 20-state deterministic corridor ( s ∈ { 0 , … , 19 } s\in{0,\ldots,19} , action: move right, reward + 1 +1 only at the terminal state s = 19 s=19 , γ = 0.99 \gamma=0.99 ) isolates the credit-assignment mechanism. The true value function is V ∗  ( s ) = γ 19 − s V^{*}(s)=\gamma^{19-s} . TD( λ \lambda ) performs policy evaluation for four values of λ \lambda across 20 seeds and 200 episodes.
Table 4 and Figure 4 show that higher λ \lambda propagates the sparse terminal reward signal backward through the corridor faster: TD( λ = 1 \lambda=1 ) reaches RMSVE < 0.05 <0.05 in fewer episodes than TD(0), which must wait for many episodes before the reward signal diffuses back to early states through one-step bootstrapping alone. 
Figure 4: RMSVE vs. episodes for TD( λ \lambda ) on the 20-state corridor. Shaded regions show ± 1 \pm 1 SE over 20 seeds. Higher λ \lambda propagates the terminal reward faster. Table 4: TD( λ \lambda ) on 20-state corridor. Mean ± \pm SE over 20 seeds, 200 episodes, γ = 0.99 \gamma=0.99 , α = 0.05 \alpha=0.05 .
5.2.5 Finite-Sample Theory of Fitted Methods
Fitted Q-Iteration and Fitted Value Iteration (Definition 4.1.10, Section 4.1.10) replace exact Bellman applications with projected regression steps. The projection introduces approximation error that compounds across iterations.
Define the inherent Bellman approximation error
ε approx = inf f ∈ ℱ ‖ 𝒯  f − f ‖ p , μ , \varepsilon_{\mathrm{approx}}=\inf_{f\in\mathcal{F}}|\mathcal{T}f-f|_{p,\mu},
(41)
the smallest residual achievable when the Bellman operator maps any element of ℱ \mathcal{F} back to itself. Munos and Szepesvári ( 2008) show that after K K iterations with N N i.i.d. samples per iteration,
‖ V K − V ∗ ‖ p , ρ ≤ C ρ , μ  [ γ K  ‖ V 0 − V ∗ ‖ p , ρ + ε approx ( 1 − γ ) 2 + O  ( 1 N ) ] , |V_{K}-V^{}|{p,\rho};\leq;C{\rho,\mu}\left[\gamma^{K}|V_{0}-V^{}|{p,\rho}+\frac{\varepsilon{\mathrm{approx}}}{(1-\gamma)^{2}}+O!\left(\frac{1}{\sqrt{N}}\right)\right],
(42)
where C ρ , μ C_{\rho,\mu} is a concentrability coefficient bounding the ratio of future-state distributions under the evaluation distribution ρ \rho relative to the data distribution μ \mu . 68 68 68 The concentrability coefficient C ρ , μ C_{\rho,\mu} measures how well the data distribution μ \mu covers future states reachable under optimal policies from ρ \rho . When μ \mu is the state-action distribution of the optimal policy itself, C ρ , μ = 1 C_{\rho,\mu}=1 . Distribution mismatch, common when batch data comes from a sub-optimal behavior policy, inflates C ρ , μ C_{\rho,\mu} and worsens the bound. Antos et al. ( 2008) extend these results to continuous action spaces and single-trajectory data. Three terms drive the error: the geometric decay γ K \gamma^{K} (initialization bias), the approximation error ( 1 − γ ) − 2  ε approx (1-\gamma)^{-2}\varepsilon_{\mathrm{approx}} (bias from function class), and the estimation error O  ( 1 / N ) O(1/\sqrt{N}) (variance from finite samples). When ℱ \mathcal{F} contains V ∗ V^{*} exactly, ε approx = 0 \varepsilon_{\mathrm{approx}}=0 and the bound recovers exact convergence as K → ∞ K\to\infty . The ( 1 − γ ) − 2 (1-\gamma)^{-2} amplification, one factor of ( 1 − γ ) − 1 (1-\gamma)^{-1} more than in tabular Q-learning, reflects error accumulation across approximate DP steps: each regression step introduces bias, and this bias compounds over K K iterations.
Both algorithms solve projected Bellman equations. When V ∗ ∈ span  ( Φ ) V^{}\in\mathrm{span}(\Phi) exactly, FVI converges to V ∗ V^{} in a single projected iteration, since the normal equations ( 23) recover θ V ∗ \theta_{V}^{} satisfying Φ  θ V ∗ = V ∗ \Phi\theta_{V}^{}=V^{} . For FQI, the per-action Q-functions satisfy Q ∗  ( s , a ∗  ( s ) ) = V ∗  ( s ) Q^{}(s,a^{}(s))=V^{}(s) at the optimal action a ∗  ( s ) a^{}(s) , so when Q ∗  ( ⋅ , a ) Q^{}(\cdot,a) is also representable in span  ( Φ ) \mathrm{span}(\Phi) for each a a , FQI recovers consistent value estimates ϕ  ( s ) ⊤  θ a ∗  ( s ) ∗ = ϕ  ( s ) ⊤  θ V ∗ \phi(s)^{\top}\theta_{a^{}(s)}^{}=\phi(s)^{\top}\theta_{V}^{} at convergence. Whether FQI succeeds therefore depends on the geometry of the problem: when Q ∗  ( ⋅ , a ) ∉ span  ( Φ ) Q^{}(\cdot,a)\notin\mathrm{span}(\Phi) , as on the Brock–Mirman economy, where the per-action Q-function requires fractional-power terms k − n  α k^{-n\alpha} outside the log-polynomial span, FQI stalls at error 1.65 while FVI converges to 0.001; when Q ∗  ( x , u ) Q^{}(x,u) is exactly quadratic in ( x , u ) (x,u) , as on the linear-quadratic control problem (Section 5.2.6), both FVI and FQI converge to near-zero error. Section 5.2.7 shows that replacing the linear basis with a nonlinear parametric model that matches the log-Cobb–Douglas structure of Q ∗ Q^{} restores FQI convergence on the Brock–Mirman economy.
5.2.6 Simulation Study: Fitted Methods on Linear-Quadratic Control
Linear-quadratic control (LQC) is a setting where both V ∗ V^{} and Q ∗ Q^{} are quadratic polynomials, so the fitted method comparison is analytically transparent. The model has scalar state x ∈ [ − 4 , 4 ] x\in[-4,4] and action u ∈ [ − 2 , 2 ] u\in[-2,2] , deterministic dynamics x ′ = a  x + b  u x^{\prime}=ax+bu with a = 0.5 a=0.5 , b = 1.0 b=1.0 , reward r  ( x , u ) = − ( x 2 + u 2 ) r(x,u)=-(x^{2}+u^{2}) , and discount γ = 0.95 \gamma=0.95 . The parameters are chosen so that x ′ = 0.5  x + u ∈ [ − 4 , 4 ] x^{\prime}=0.5x+u\in[-4,4] whenever ( x , u ) ∈ [ − 4 , 4 ] × [ − 2 , 2 ] (x,u)\in[-4,4]\times[-2,2] , making the grid strictly invariant. The optimal value function satisfies V ∗  ( x ) = − P  x 2 V^{}(x)=-Px^{2} , where P P solves γ  b 2  P 2 + P  ( 1 − γ  ( a 2 + b 2 ) ) − 1 = 0 \gamma b^{2}P^{2}+P(1-\gamma(a^{2}+b^{2}))-1=0 , yielding P ≈ 1.129 P\approx 1.129 . The optimal Q-function is Q ∗  ( x , u ) = − ( 1 + γ  P  a 2 )  x 2 − 2  γ  P  a  b  x  u − ( 1 + γ  P  b 2 )  u 2 ≈ − 1.268  x 2 − 1.073  x  u − 2.073  u 2 Q^{}(x,u)=-(1+\gamma Pa^{2})x^{2}-2\gamma Pab,xu-(1+\gamma Pb^{2})u^{2}\approx-1.268x^{2}-1.073xu-2.073u^{2} , which lies exactly in span  { x 2 , x  u , u 2 } ⊂ span  { x , x 2 , u , u 2 , x  u } \mathrm{span}{x^{2},xu,u^{2}}\subset\mathrm{span}{x,x^{2},u,u^{2},xu} . FVI uses state features ϕ V  ( x ) = [ x , x 2 ] ⊤ ∈ ℝ 2 \phi_{V}(x)=[x,x^{2}]^{\top}\in\mathbb{R}^{2} (no intercept, since V ∗  ( 0 ) = 0 V^{*}(0)=0 ); FQI uses state-action features ϕ Q  ( x , u ) = [ x , x 2 , u , u 2 , x  u ] ⊤ ∈ ℝ 5 \phi_{Q}(x,u)=[x,x^{2},u,u^{2},xu]^{\top}\in\mathbb{R}^{5} . Both use a 301-point state grid and 201-point action grid. DQN uses a two-layer network of 64 units per layer with ReLU activations, an experience replay buffer of 50,000 transitions, a hard target-network update every 500 gradient steps, and rewards scaled by a factor of 1 / 20 1/20 to stabilize training.
Both methods recover the analytical solution to machine precision (Table 5, Figure 5): FVI and FQI converge in under 10 iterations with errors below 10 − 3 10^{-3} , matching the known polynomial structure of Q ∗ Q^{} . DQN also converges (error 5.6 × 10 − 1 5.6\times 10^{-1} after 100,000 gradient steps) with no prior knowledge of the feature basis. The contrast with Brock–Mirman is exact: FQI succeeds here because Q ∗  ( x , u ) ∈ span  ( Φ Q ) Q^{}(x,u)\in\mathrm{span}(\Phi_{Q}) , while it fails on Brock–Mirman because Q ∗  ( ⋅ , a ) ∉ span  ( Φ ) Q^{*}(\cdot,a)\notin\mathrm{span}(\Phi) .
Table 5: Fitted weights and convergence metrics for FVI, FQI, and DQN on linear-quadratic control. The FVI x 2 x^{2} coefficient recovers the Riccati solution P ≈ 1.129 P\approx 1.129 . The FQI quadratic coefficients match the analytical Q ∗ Q^{} to four decimal places. FVI and FQI achieve max error below 10 − 3 10^{-3} against the analytical V ∗ V^{} ; DQN achieves error 5.6 × 10 − 1 5.6\times 10^{-1} after 100,000 gradient steps with no feature basis specified. 
Figure 5: LQC convergence of FVI and FQI (left), DQN learning curve (middle), and value function recovery for all three methods (right). FVI and FQI reduce ‖ V k − V ∗ ‖ ∞ |V_{k}-V^{}|_{\infty} to near-zero in under 10 iterations, exploiting the known polynomial structure of Q ∗ Q^{} . DQN declines from error 6.7 to 0.56 over 100,000 gradient steps with no feature basis specified.
5.2.7 Simulation Study: Basis Representability on the Brock–Mirman Economy
The Brock–Mirman stochastic growth model (Brock and Mirman, 1972) provides the negative case. The economy has | 𝒮 | = 100 |\mathcal{S}|=100 states ( N K = 50 N_{K}=50 capital grid points, N Z = 2 N_{Z}=2 productivity levels) and | 𝒜 | = 50 |\mathcal{A}|=50 actions. We use the same log-polynomial basis ϕ  ( k , z ) = [ 1 , log  k , k / k ¯ , ( k / k ¯ ) 2 , ( k / k ¯ ) 3 ] ⊗ [ 𝟙 z = z ℓ , 1 z = z h ] \phi(k,z)=[1,,\log k,,k/\bar{k},,(k/\bar{k})^{2},,(k/\bar{k})^{3}]\otimes[\mathbbm{1}{z=z{\ell}},,\mathbbm{1}{z=z{h}}] from the theory discussion above, which contains V ∗ V^{} up to residual ‖ Π Φ  V ∗ − V ∗ ‖ ∞ = 0.0002 |\Pi_{\Phi}V^{}-V^{*}|{\infty}=0.0002 . To test whether the failure is inherent to FQI or to the basis, we add two methods that use the structurally correct per-action feature log  ( z  k α − k ′ ) \log(zk^{\alpha}-k^{\prime}) , the log-consumption implied by the Cobb–Douglas technology. Oracle-FQI treats α = 0.36 \alpha=0.36 as known and runs standard OLS per action with three parameters [ 𝟙 z = z ℓ , 1 z = z h , log  ( z  k α − k ′ ) ] [\mathbbm{1}{z=z_{\ell}},,\mathbbm{1}{z=z{h}},,\log(zk^{\alpha}-k^{\prime})] . NLLS-FQI estimates α \alpha jointly via concentrated least squares: for each candidate α \alpha , it solves conditional OLS for intercepts and slope, then optimizes α \alpha to minimize total residual sum of squares, initialized at the deliberately wrong value α 0 = 0.5 \alpha_{0}=0.5 . 69 69 69 Observations where z  k α − k ′ ≤ 0 zk^{\alpha}-k^{\prime}\leq 0 (infeasible consumption) contribute a penalty equal to the mean squared target, preventing the optimizer from improving RSS by shrinking the feasible set.
Table 6 and Figure 6 confirm the diagnosis: basis representability, not algorithmic failure. FVI converges near the projection floor of the log-polynomial basis; linear FQI stalls at error 1.65, confirming Q ∗  ( ⋅ , a ) ∉ span  ( Φ ) Q^{}(\cdot,a)\notin\mathrm{span}(\Phi) . Oracle-FQI and NLLS-FQI, using the structurally correct log-consumption feature, match exact VI with error below 10 − 4 10^{-4} . NLLS-FQI recovers α ^ = 0.3600 \hat{\alpha}=0.3600 in a single iteration, demonstrating that the same FQI algorithm succeeds when the function class contains Q ∗ Q^{} .
Table 6: Convergence metrics for five methods on the Brock–Mirman economy ( N K = 50 N_{K}=50 , N Z = 2 N_{Z}=2 , γ = 0.96 \gamma=0.96 ). Policy agreement is measured against the closed-form optimal policy k ′ = α  β  z  k α k^{\prime}=\alpha\beta zk^{\alpha} . 
Figure 6: Left: convergence of ‖ V k − V ∗ ‖ ∞ |V_{k}-V^{*}|{\infty} for FVI, linear FQI, Oracle-FQI, and NLLS-FQI on the Brock–Mirman economy. Right: NLLS-FQI estimated α \alpha trajectory, converging from α 0 = 0.5 \alpha{0}=0.5 to the true α = 0.36 \alpha=0.36 in one iteration.
5.2.8 Rollout, Lookahead, and AlphaZero
Two constructions bridge the Newton interpretation of Section 5.1 to practical algorithms. Given a base policy μ \mu with value function V μ V^{\mu} , the rollout policy selects
μ R  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a ∈ 𝒜 { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V μ  ( s ′ ) } . \mu_{R}(s)=\mathop{\it argmax}{a\in\mathcal{A}}\left{r(s,a)+\gamma\sum{s^{\prime}}P(s^{\prime}|s,a),V^{\mu}(s^{\prime})\right}.
(43)
This is one step of policy iteration starting from μ \mu : the Policy Improvement Theorem (Theorem 1) guarantees V μ R  ( s ) ≥ V μ  ( s ) V^{\mu_{R}}(s)\geq V^{\mu}(s) for all s s , with strict inequality unless μ \mu is already optimal (Bertsekas, 2021) . 70 70 70 Bertsekas uses cost-minimization notation throughout his work, writing min \min where standard RL uses max \max and defining value as accumulated cost rather than reward. I translate to the reward-maximization convention used elsewhere in this chapter; the mathematics are equivalent with reversed inequalities. Given an arbitrary approximate value function V ~ \tilde{V} (not necessarily the value of any policy), the one-step lookahead policy selects
π ~  ( s ) = 𝑎𝑟𝑔𝑚𝑎𝑥 a ∈ 𝒜 { r  ( s , a ) + γ  ∑ s ′ P  ( s ′ | s , a )  V ~  ( s ′ ) } . \tilde{\pi}(s)=\mathop{\it argmax}{a\in\mathcal{A}}\left{r(s,a)+\gamma\sum{s^{\prime}}P(s^{\prime}|s,a),\tilde{V}(s^{\prime})\right}.
(44)
When V ~ = V μ \tilde{V}=V^{\mu} , lookahead and rollout coincide. The distinction matters because rollout inherits the monotone improvement guarantee (it starts from the value of a policy), while lookahead from an arbitrary V ~ \tilde{V} has no such monotonicity. The Newton interpretation from Section 5.1 explains why lookahead nevertheless helps: both constructions solve the linearized Bellman equation at the current iterate. 71 71 71 Rollout requires a simulator (generative model) that can be queried from arbitrary states, a stronger assumption than the trajectory-based access of Q-learning and SARSA.
An ℓ \ell -step lookahead extends this by applying ( ℓ − 1 ) (\ell-1) steps of value iteration before the final greedy selection. The first ( ℓ − 1 ) (\ell-1) steps are ordinary Bellman contractions, each shrinking the approximation error by a factor of γ \gamma . Only the final step, the greedy policy improvement, constitutes the Newton step. 72 72 72 Bertsekas ( 2021) states this explicitly: “whatever follows the first step of the lookahead is preparation for the Newton step.” The preceding value iteration steps have linear convergence at rate γ \gamma ; only the terminal improvement step has superlinear character. The resulting error bound is
‖ V π ~ − V ∗ ‖ ∞ ≤ γ ℓ  ‖ V ~ − V ∗ ‖ ∞ , |V^{\tilde{\pi}}-V^{}|_{\infty}\leq\gamma^{\ell},|\tilde{V}-V^{}|_{\infty},
(45)
where the γ ℓ \gamma^{\ell} factor reflects ℓ \ell total contractions (Bertsekas, 2022a, Prop. 2.3.1) . Deep lookahead compensates for poor approximation through repeated contraction, not through repeated Newton steps.
Recall the AlphaGo Zero system from Section 4.2.4, where a neural network f θ  ( s ) = ( 𝐩 , v ) f_{\theta}(s)=(\mathbf{p},v) outputs a prior policy 𝐩 \mathbf{p} and a value estimate v v for any board position s s . During play, the network does not act alone: Monte Carlo Tree Search runs simulated games from the current position, using v v to evaluate leaf nodes and 𝐩 \mathbf{p} to guide which branches to explore. 73 73 73 AlphaGo Zero uses 1,600 MCTS simulations per move for Go; the generalized AlphaZero algorithm uses 800 simulations per move across chess, shogi, and Go (Silver et al., 2018, Table S3) . The network provides V ~ \tilde{V} ; MCTS applies multi-step lookahead through selective tree expansion. Table 7 makes the correspondence explicit.
Table 7: Policy iteration and AlphaZero follow the same evaluate-improve loop. The network provides approximate policy evaluation; MCTS provides approximate policy improvement via selective tree search.
The gap between network-only play and network-plus-search is the contraction factor γ H \gamma^{H} , where H H is the effective search depth. The network provides a rough starting point V ~ \tilde{V} ; MCTS applies the Bellman operator through deep lookahead, shrinking the approximation error by γ \gamma per level of search. 74 74 74 MCTS adds UCB exploration and selective tree expansion beyond the literal lookahead framework. The Newton interpretation explains why lookahead helps at all, namely, the final greedy selection over the search tree is a policy improvement step. It does not explain the specific mechanisms (upper confidence bounds, progressive widening) that make MCTS computationally efficient.
5.3 The Central Challenge: The Deadly Triad
State spaces are too large for lookup tables (Go has 10 170 10^{170} states; most economic models have continuous state variables). Practitioners must combine three ingredients: function approximation (to handle large state spaces), bootstrapping (to learn from single transitions rather than complete episodes), and off-policy learning (to learn about the optimal policy while exploring, or to reuse old data). Each is desirable in isolation. Their interaction, known as the deadly triad (Sutton and Barto, 2018, Ch. 11) , is the central open problem in reinforcement learning theory.
Off-policy learning is preferred for three reasons. First, sample efficiency: transitions collected under any behavioral policy can be reused to evaluate or improve a different target policy, amortizing the cost of data collection. Discarding data because it was generated by a superseded policy is wasteful. Second, exploration and exploitation separate cleanly: the agent can follow an exploratory policy (e.g., ε \varepsilon -greedy) to ensure adequate state-space coverage while simultaneously learning the optimal deterministic policy. On-policy methods such as SARSA entangle the two, learning the value of the exploratory policy rather than the optimal one. Third, off-policy evaluation answers “what would have happened under policy π \pi ?” from data generated by policy μ \mu , the counterfactual question at the heart of policy comparison.
5.3.1 The Projected Bellman Operator
With function approximation V  ( s ) ≈ ϕ  ( s ) ⊤  θ V(s)\approx\phi(s)^{\top}\theta , the parameter vector θ \theta is shared across states. Updating θ \theta to improve the value estimate at one state simultaneously changes the estimate at every other state. The algorithm can no longer apply the Bellman operator T π T^{\pi} to each state independently; instead, it applies T π T^{\pi} to compute a target, then projects the result back onto the function space (the span of the features ϕ \phi ). The composed operator is Π  T π \Pi T^{\pi} , the projected Bellman operator, where Π \Pi denotes this projection (Tsitsiklis and Van Roy, 1997) . Convergence of the approximate iteration θ k + 1 = Π  T π  θ k \theta_{k+1}=\Pi T^{\pi}\theta_{k} requires Π  T π \Pi T^{\pi} to be a contraction.
In the on-policy setting, Π \Pi minimizes squared error weighted by d π d^{\pi} , the stationary distribution of the policy being evaluated, so Π  V = arg  min V ^ ∈ span  ( Φ )  ‖ V − V ^ ‖ d π \Pi V=\arg\min_{\hat{V}\in\text{span}(\Phi)}|V-\hat{V}|{d^{\pi}} , where ‖ V ‖ d π 2 = ∑ s d π  ( s )  V  ( s ) 2 |V|{d^{\pi}}^{2}=\sum_{s}d^{\pi}(s)V(s)^{2} . The Bellman operator T π T^{\pi} is a γ \gamma -contraction in the same d π d^{\pi} -norm. Because both operators use the same norm, the projection Π \Pi is orthogonal, meaning the residual V − Π  V V-\Pi V is perpendicular to the approximation subspace. The Pythagorean theorem then gives ‖ Π  V ‖ d π 2 + ‖ V − Π  V ‖ d π 2 = ‖ V ‖ d π 2 |\Pi V|{d^{\pi}}^{2}+|V-\Pi V|{d^{\pi}}^{2}=|V|{d^{\pi}}^{2} , so ‖ Π  V ‖ d π ≤ ‖ V ‖ d π |\Pi V|{d^{\pi}}\leq|V|_{d^{\pi}} . 75 75 75 The same argument holds in ℝ n \mathbb{R}^{n} . Projecting a vector onto a subspace never makes it longer. This is the geometric content of the Cauchy-Schwarz inequality. In the function-approximation setting, the “vector” is a value function, the “subspace” is the span of features, and “length” is the d π d^{\pi} -weighted L 2 L^{2} norm. The projection cannot expand distances. The composition therefore contracts:
‖ Π  T π  V 1 − Π  T π  V 2 ‖ d π ≤ ‖ Π ‖ ⏟ ≤ 1 ⋅ ‖ T π  V 1 − T π  V 2 ‖ d π ⏟ ≤ γ  ‖ V 1 − V 2 ‖ d π < ‖ V 1 − V 2 ‖ d π . |\Pi T^{\pi}V_{1}-\Pi T^{\pi}V_{2}|{d^{\pi}}\leq\underbrace{|\Pi|}{\leq,1}\cdot\underbrace{|T^{\pi}V_{1}-T^{\pi}V_{2}|{d^{\pi}}}{\leq,\gamma|V_{1}-V_{2}|{d^{\pi}}}<|V{1}-V_{2}|_{d^{\pi}}.
(46)
A unique fixed point Φ  θ ∗ \Phi\theta^{} exists, and TD( λ \lambda ) converges to it with probability one. The resulting approximation error satisfies ‖ Φ  θ ∗ − V π ‖ d π ≤ 1 − λ  γ 1 − γ 2  ‖ Π  V π − V π ‖ d π |\Phi\theta^{}-V^{\pi}|{d^{\pi}}\leq\frac{1-\lambda\gamma}{\sqrt{1-\gamma^{2}}}|\Pi V^{\pi}-V^{\pi}|{d^{\pi}} , bounding the TD solution's error by a multiple of the best possible approximation error (Tsitsiklis and Van Roy, 1997, Theorem 1) .
5.3.2 Why Off-Policy Learning Diverges
In the off-policy setting, samples come from a behavior distribution μ ≠ d π \mu\neq d^{\pi} . The projection now minimizes error under μ \mu , but the Bellman operator T π T^{\pi} still contracts in the d π d^{\pi} -norm. The two operators measure distance in different norms. The projection is no longer orthogonal in the d π d^{\pi} -norm; it is oblique. Unlike orthogonal projections, oblique projections can expand distances, with ‖ Π μ ‖ d π |\Pi_{\mu}|{d^{\pi}} exceeding 1 in the worst case. If ‖ Π μ ‖ d π > 1 / γ |\Pi{\mu}|_{d^{\pi}}>1/\gamma , the expansion from projection overwhelms the γ \gamma -contraction from the Bellman operator, and the fixed-point iteration diverges.
This divergence is not overfitting. Overfitting occurs when the approximator memorizes training data at the expense of generalization; collecting more data helps. Divergence means the parameter vector θ \theta grows without bound, producing arbitrarily large value estimates that bear no relation to the true values. More data does not help; the algorithm itself is unstable. The distinction matters because the remedies are entirely different. Regularization and early stopping address overfitting, while the deadly triad requires structural changes to the algorithm.
Baird ( 1995) constructed a six-state star MDP that makes this failure concrete. All rewards are zero, so the true value is V ∗  ( s ) = 0 V^{*}(s)=0 for every state. A lookup table learns this immediately. The MDP has a star topology: states 1 through 5 each transition to state 6, and state 6 transitions to itself. Linear function approximation uses a shared weight w 1 w_{1} across all states plus a state-specific weight, with V  ( s ) = 2  w 1 + w s V(s)=2w_{1}+w_{s} for s ∈ { 1 , … , 5 } s\in{1,\ldots,5} and V  ( 6 ) = 2  w 1 − w 6 V(6)=2w_{1}-w_{6} . Training samples all transitions equally often (uniform distribution, not d π d^{\pi} ). The dynamics are as follows. 76 76 76 Baird ( 1995) also presents an MDP variant with two actions per state, demonstrating that Q-learning diverges under the same mechanism. The key insight is identical: shared parameters create cross-state coupling that uniform sampling cannot counterbalance. When V  ( 6 ) V(6) is large and positive, the TD target γ  V  ( 6 ) \gamma V(6) exceeds V  ( s ) V(s) for states 1 through 5, producing positive TD errors that push w 1 w_{1} upward. At state 6, the TD target is γ  V  ( 6 ) < V  ( 6 ) \gamma V(6)<V(6) , producing a negative TD error that pushes w 1 w_{1} downward. But states 1 through 5 are each visited as often as state 6, so w 1 w_{1} receives five upward pushes for every one downward push. The shared weight diverges to + ∞ +\infty . The on-policy distribution would concentrate mass on state 6 (the absorbing state), counterbalancing the upward pressure; uniform sampling destroys this balance. 77 77 77 The gradient of ‖ Q − T  Q ‖ 2 |Q-TQ|^{2} requires two independent next-state samples from the same ( s , a ) (s,a) , since ∇ 𝔼  [ ( Q − 𝔼  [ r + γ  V  ( s ′ ) ] ) 2 ] \nabla\mathbb{E}[(Q-\mathbb{E}[r+\gamma V(s^{\prime})])^{2}] involves 𝔼  [ ⋅ ] ⋅ ∇ 𝔼  [ ⋅ ] \mathbb{E}[\cdot]\cdot\nabla\mathbb{E}[\cdot] and 𝔼  [ X  Y ] ≠ 𝔼  [ X ]  𝔼  [ Y ] \mathbb{E}[XY]\neq\mathbb{E}[X]\mathbb{E}[Y] . This “double-sampling” requirement is impractical (Baird, 1995) , so practitioners use semi-gradient TD, treating the bootstrap target as a constant. This semi-gradient structure makes off-policy TD vulnerable to projection mismatch.
Each element of the triad is individually necessary for divergence. Without function approximation (tabular), the projection is the identity and Q-learning's contraction applies directly. Without bootstrapping (Monte Carlo returns), targets are independent of current value estimates and the problem reduces to supervised regression. Without off-policy learning, samples come from d π d^{\pi} , the projection is orthogonal, and the Tsitsiklis-Van Roy convergence guarantee holds. 
Figure 7: Geometry of the projected Bellman operator in ℝ 2 \mathbb{R}^{2} . The gray line is the function approximation subspace span( Φ \Phi ); the blue arrow is T  V TV , the Bellman update. (a) On-policy: the orthogonal projection Π μ \Pi_{\mu} drops T  V TV perpendicularly onto the subspace, preserving the contraction. (b) Off-policy: the oblique projection Π ν \Pi_{\nu} (under the behavior distribution) reaches a point further from the origin than T  V TV itself, causing expansion.
5.3.3 Resolutions
Three classes of algorithms restore convergence, each neutralizing a different component of the triad.
Target networks weaken bootstrapping. Instead of updating toward r + γ  Q  ( s ′ ; θ ) r+\gamma Q(s^{\prime};\theta) , where the target moves with each parameter update, DQN (Mnih et al., 2015) updates toward r + γ  Q  ( s ′ ; θ − ) r+\gamma Q(s^{\prime};\theta^{-}) , where θ − \theta^{-} is a slowly-updated copy of the parameters. 78 78 78 Experience replay (Lin, 1992) complements target networks by breaking temporal correlation in the training data. The two mechanisms address different sources of instability: target networks stabilize the bootstrap target, while replay stabilizes the sampling distribution. The regression target becomes quasi-static, converting the coupled fixed-point problem into a sequence of supervised learning problems. Zhang et al. ( 2021) prove that this two-timescale scheme converges to a regularized TD fixed point with linear function approximation. Fellows et al. ( 2023) show that target networks recondition the Jacobian of the TD update: the spectral radius of the composed update operator depends on the target network update frequency k k , and for sufficiently large k k the spectral radius drops below 1 even in off-policy settings with nonlinear function approximation.
Gradient TD methods fix the projection mismatch. Sutton et al. ( 2009) reformulate the projected Bellman error as a saddle-point problem min θ  max y  L  ( θ , y ) \min_{\theta}\max_{y}L(\theta,y) , yielding algorithms (GTD, GTD2, TDC) that perform true stochastic gradient descent on the mean-squared projected Bellman error. 79 79 79 The saddle-point formulation introduces auxiliary variables y y of the same dimension as θ \theta , doubling the parameter count and requiring a second learning rate. Bhandari et al. ( 2021) provide finite-time convergence rates for these two-timescale algorithms. These methods converge off-policy with linear function approximation because they eliminate the semi-gradient approximation that causes the norm mismatch.
Regularization shrinks the projection operator. Lim and Lee ( 2024) add an ℓ 2 \ell_{2} penalty − η  θ -\eta\theta to the Q-learning update. This changes the projection from Π = X  ( X ⊤  D  X ) − 1  X ⊤  D \Pi=X(X^{\top}DX)^{-1}X^{\top}D to Π η = X  ( X ⊤  D  X + η  I ) − 1  X ⊤  D \Pi_{\eta}=X(X^{\top}DX+\eta I)^{-1}X^{\top}D . As the regularization strength η \eta increases, the projection “shrinks” toward the origin. For sufficiently large η \eta , γ  ‖ Π η ‖ < 1 \gamma|\Pi_{\eta}|<1 , restoring the contraction property. The algorithm converges to a biased but stable fixed point, with the bias controlled by η \eta .
5.4 Policy Learning Methods
Value-based methods find fixed points of the Bellman operator. Policy-based methods parameterize the policy directly as π θ  ( a | s ) \pi_{\theta}(a|s) and maximize expected return J  ( θ ) = 𝔼 π θ  [ ∑ t = 0 ∞ γ t  R t ] J(\theta)=\mathbb{E}{\pi{\theta}}[\sum_{t=0}^{\infty}\gamma^{t}R_{t}] by gradient ascent. This formulation sidesteps the Bellman equation entirely and frames reinforcement learning as constrained optimization.
5.4.1 The Policy Gradient Theorem
The policy gradient theorem, proved independently by Williams ( 1992) for the episodic case and Sutton et al. ( 2000) for the general discounted setting, provides a tractable expression for the gradient:
∇ θ J  ( θ ) = 𝔼 s ∼ d π θ , a ∼ π θ  [ ∇ θ log  π θ  ( a | s )  Q π θ  ( s , a ) ] , \nabla_{\theta}J(\theta)=\mathbb{E}{s\sim d^{\pi{\theta}},a\sim\pi_{\theta}}\left[\nabla_{\theta}\log\pi_{\theta}(a|s),Q^{\pi_{\theta}}(s,a)\right],
(47)
where d π θ  ( s ) = ( 1 − γ )  ∑ t = 0 ∞ γ t  ℙ  ( s t = s | π θ ) d^{\pi_{\theta}}(s)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\mathbb{P}(s_{t}=s|\pi_{\theta}) is the discounted state visitation distribution. The fundamental econometric challenge in optimizing J  ( θ ) J(\theta) is that this distribution depends on θ \theta through the environment's dynamics. A naive derivative would require ∇ θ d π θ  ( s ) \nabla_{\theta}d^{\pi_{\theta}}(s) , which implies differentiating the unknown transition matrix P  ( s ′ | s , a ) P(s^{\prime}|s,a) .
The policy gradient theorem sidesteps this entirely via a likelihood ratio (or score function) trick. 80 80 80 The score function ∇ θ log  π θ  ( a | s ) \nabla_{\theta}\log\pi_{\theta}(a|s) is the same mathematical object that appears in the Cramér-Rao bound and the score test in maximum likelihood estimation. The policy gradient is a covariance, ∇ J = Cov d π θ × π θ  ( ∇ log  π θ , Q π θ ) \nabla J=\text{Cov}{d^{\pi{\theta}}\times\pi_{\theta}}(\nabla\log\pi_{\theta},Q^{\pi_{\theta}}) , measuring how sensitive the log-likelihood of the policy is to parameter changes, weighted by action quality. The theorem transforms a sensitivity analysis problem (how does the system evolve?) into a simpler expectation problem (what is the correlation between the score ∇ log  π \nabla\log\pi and the value Q Q ?). The gradient can be written as an expectation under the current policy, weighted by action-values, without requiring ∇ θ d π θ \nabla_{\theta}d^{\pi_{\theta}} . The transition dynamics P  ( s ′ | s , a ) P(s^{\prime}|s,a) do not appear; the gradient is estimable via sample averages from trajectories alone.
5.4.2 REINFORCE and Variance Reduction
REINFORCE (Williams, 1992) is the simplest policy gradient algorithm. Sample a trajectory ( s 0 , a 0 , r 0 , s 1 , … ) (s_{0},a_{0},r_{0},s_{1},\ldots) , compute the return G t = ∑ k = 0 ∞ γ k  r t + k G_{t}=\sum_{k=0}^{\infty}\gamma^{k}r_{t+k} from each time step, and update:
θ ← θ + α  ∑ t ∇ θ log  π θ  ( a t | s t )  G t . \theta\leftarrow\theta+\alpha\sum_{t}\nabla_{\theta}\log\pi_{\theta}(a_{t}|s_{t}),G_{t}.
(48)
This is an unbiased estimator of ∇ θ J  ( θ ) \nabla_{\theta}J(\theta) , but its variance is high because a single trajectory provides a noisy estimate of Q π θ Q^{\pi_{\theta}} . Despite high variance, REINFORCE converges to a globally optimal policy in the tabular setting. 81 81 81 The baseline b  ( s ) b(s) subtracted from G t G_{t} reduces variance while preserving unbiasedness, since 𝔼  [ ∇ θ log  π θ  ( a | s )  b  ( s ) ] = 0 \mathbb{E}[\nabla_{\theta}\log\pi_{\theta}(a|s)b(s)]=0 for any baseline independent of a a .
5.4.3 Natural Policy Gradient and Gradient Domination
Standard gradient descent treats all parameter directions equally. But small changes in θ \theta can cause large changes in the policy distribution π θ \pi_{\theta} . The natural policy gradient (Kakade, 2001) , building on the natural gradient framework of Amari ( 1998) , accounts for this curvature by preconditioning with the Fisher information matrix. 82 82 82 The Fisher information F  ( θ ) = 𝔼  [ ∇ log  p  ∇ log  p ⊤ ] F(\theta)=\mathbb{E}[\nabla\log p\nabla\log p^{\top}] measures curvature of the log-likelihood and appears in the Cramér-Rao bound. Here it measures how policy distributions change with parameters. The relationship between NPG and standard PG parallels that between Fisher scoring and gradient ascent in MLE. Both precondition with the inverse Fisher information matrix F  ( θ ) − 1 F(\theta)^{-1} , achieving parameterization invariance and quadratic convergence near the optimum.
∇ ~ θ  J  ( θ ) = F  ( θ ) − 1  ∇ θ J  ( θ ) , F  ( θ ) = 𝔼 s , a  [ ∇ θ log  π θ  ( a | s )  ∇ θ log  π θ  ( a | s ) ⊤ ] . \tilde{\nabla}{\theta}J(\theta)=F(\theta)^{-1}\nabla{\theta}J(\theta),\quad F(\theta)=\mathbb{E}{s,a}\left[\nabla{\theta}\log\pi_{\theta}(a|s)\nabla_{\theta}\log\pi_{\theta}(a|s)^{\top}\right].
(49)
Why does NPG recover policy iteration? Standard gradient ascent is sensitive to parameterization: it takes the steepest step in Euclidean parameter space, where units depend on how the policy is parameterized. NPG takes the steepest step in distribution space (measured by KL-divergence), which is invariant to reparameterization. In the tabular case, Kakade ( 2001, Theorem 2) proves that this geometric correction aligns the gradient exactly with the greedy policy π ~ \tilde{\pi} from policy iteration. With step size 1 (and exact estimation), NPG performs one full Newton step; with smaller step sizes, it performs damped Newton updates. This explains its rapid convergence: NPG approximates the quadratic convergence of finding a fixed point rather than the linear convergence of hill-climbing.
The RL objective J  ( θ ) J(\theta) is non-convex in θ \theta . For economists trained to distrust gradient methods on non-convex objectives, the natural concern is convergence to spurious local optima. For tabular softmax policies (one free parameter per state-action pair), this concern is unfounded. The landscape is “benign” in a precise sense. Agarwal et al. ( 2021a) prove that J  ( θ ) J(\theta) satisfies a gradient domination condition (also called Polyak-Łojasiewicz, or PL). The PL condition has the same functional form as the strong convexity condition for guaranteeing linear convergence of gradient descent, but it applies to non-convex functions: whenever ‖ ∇ J  ( θ ) ‖ |\nabla J(\theta)| is small, the policy must be near-optimal. Formally, the sub-optimality J  ( π ∗ ) − J  ( π θ ) J(\pi^{*})-J(\pi_{\theta}) is bounded by a constant times ‖ ∇ J  ( θ ) ‖ 2 |\nabla J(\theta)|^{2} . The implication is immediate: any point where the gradient vanishes is globally optimal. The non-convex landscape has no false peaks, no spurious local maxima. Gradient ascent cannot get trapped.
Mei et al. ( 2020) sharpen this result for softmax parameterization, proving explicit convergence rates. These guarantees are specific to the tabular parameterization. With function approximation, the PL condition does not hold. Agarwal et al. ( 2021a, Theorem 6.2) show that NPG with log-linear or smooth policy classes (including neural networks) converges to a neighborhood of the optimum whose radius depends on the approximation error of the policy class, not to the global optimum itself. 83 83 83 However, “no spurious local optima” does not imply “easy optimization.” The landscape is dominated by vast plateaus (saddle points) where gradients vanish. Without sufficient exploration, the probability of visiting relevant states decays exponentially with the horizon, rendering the gradient exponentially small. Global convergence requires the starting distribution to have adequate coverage relative to the optimal policy's visitation distribution, formalized as the “distribution mismatch coefficient” by Agarwal et al. ( 2021a) . The Natural Policy Gradient addresses this by preconditioning with the Fisher Information Matrix, making the update direction covariant: invariant to invertible linear transformations of the parameter space. This standardizes units across parameters, preventing stalling on plateaus caused by poor parameter scaling. Li et al. ( 2022) make this quantitatively precise: vanilla softmax policy gradient requires iterations doubly exponential in the effective horizon 1 / ( 1 − γ ) 1/(1-\gamma) because score functions are exponentially small in directions corresponding to suboptimal actions.
In the tabular setting, NPG achieves more: dimension-free convergence. Standard gradient ascent on J  ( θ ) J(\theta) has a convergence rate that depends on the smoothness constant, which scales with | 𝒮 | |\mathcal{S}| . NPG circumvents this by preconditioning with the Fisher information matrix F  ( θ ) − 1 F(\theta)^{-1} . The mechanism is that the state-visitation distribution d π θ  ( s ) d^{\pi_{\theta}}(s) appears in both ∇ J  ( θ ) \nabla J(\theta) and F  ( θ ) F(\theta) ; when computing F − 1  ∇ J F^{-1}\nabla J , these terms cancel analytically. The resulting update rule is equivalent to soft policy iteration and converges at rate O  ( 1 / ( 1 − γ ) 2  ϵ ) O(1/(1-\gamma)^{2}\epsilon) , independent of | 𝒮 | |\mathcal{S}| and | 𝒜 | |\mathcal{A}| (Xiao, 2022) .
5.4.4 Trust Region Methods
NPG requires computing and inverting the Fisher information matrix F  ( θ ) F(\theta) , which scales as O  ( d 2 ) O(d^{2}) in parameters and is impractical for neural networks. TRPO (Schulman et al., 2015) approximates the natural gradient using conjugate gradient methods 84 84 84 Conjugate gradient is an iterative method for solving linear systems A  x = b Ax=b without forming A A explicitly, requiring only matrix-vector products A  v Av . With k k iterations it costs O  ( k  d ) O(kd) versus O  ( d 3 ) O(d^{3}) for direct inversion, making it feasible for neural networks with millions of parameters. without forming F F explicitly, and enforces trust regions via line search. 85 85 85 Trust region methods build on the performance difference lemma: for any two policies π \pi and π ′ \pi^{\prime} , J  ( π ′ ) − J  ( π ) = 1 1 − γ  𝔼 s ∼ d π ′  [ ∑ a π ′  ( a | s )  A π  ( s , a ) ] J(\pi^{\prime})-J(\pi)=\frac{1}{1-\gamma}\mathbb{E}{s\sim d^{\pi^{\prime}}}[\sum{a}\pi^{\prime}(a|s)A^{\pi}(s,a)] , where A π  ( s , a ) = Q π  ( s , a ) − V π  ( s ) A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s) is the advantage function. This identity bounds how much policy improvement is possible and motivates constraining updates to regions where advantage estimates remain accurate (Kakade, 2002) . Shani et al. ( 2020) prove convergence for adaptive trust region methods that adjust the constraint radius dynamically. PPO (Schulman et al., 2017) simplifies further by replacing the hard KL constraint with a clipped surrogate objective, trading theoretical guarantees for computational simplicity. The geometric foundation of trust region methods lies in information geometry. The space of policies { π θ : θ ∈ ℝ d } {\pi_{\theta}:\theta\in\mathbb{R}^{d}} forms a statistical manifold, and the natural distance between two nearby policies is the KL divergence, not the Euclidean distance between their parameters (Amari, 1998) . To second order, KL  ( π θ ∥ π θ + Δ  θ ) ≈ 1 2  Δ  θ ⊤  F  ( θ )  Δ  θ \mathrm{KL}(\pi_{\theta}|\pi_{\theta+\Delta\theta})\approx\frac{1}{2}\Delta\theta^{\top}F(\theta)\Delta\theta , where F  ( θ ) F(\theta) is the Fisher information matrix. Two parameter vectors θ \theta and θ ′ \theta^{\prime} that are far apart in Euclidean distance may correspond to nearly identical distributions, while nearby parameters may produce radically different policies. The natural gradient corrects for this by measuring steepest ascent in KL-divergence rather than Euclidean norm. Figure 8 illustrates the distinction: on the policy manifold, the Euclidean gradient ∇ θ J \nabla_{\theta}J points in a direction that ignores curvature, while the natural gradient F − 1  ∇ θ J F^{-1}\nabla_{\theta}J follows the manifold's intrinsic geometry toward the optimum. 
Figure 8: Information geometry of the natural policy gradient. Left: the policy manifold ℳ \mathcal{M} with Euclidean gradient ∇ θ J \nabla_{\theta}J (red) and natural gradient F − 1  ∇ θ J F^{-1}\nabla_{\theta}J (green) from the current iterate π θ old \pi_{\theta_{\mathrm{old}}} toward the optimal policy π ∗ \pi^{*} . Right: tangent plane at θ old \theta_{\mathrm{old}} showing the Euclidean unit ball ‖ Δ  θ ‖ 2 ≤ ε |\Delta\theta|_{2}\leq\varepsilon (red) and the KL unit ball Δ  θ ⊤  F  Δ  θ ≤ δ \Delta\theta^{\top}F\Delta\theta\leq\delta (green), with the respective steepest-ascent directions.
TRPO formalizes this insight as a constrained optimization problem. At each iteration, TRPO maximizes the importance-weighted surrogate
max θ  L  ( θ ) = 𝔼 s ∼ d π θ old  [ ∑ a π θ  ( a | s ) π θ old  ( a | s )  A π θ old  ( s , a ) ] s.t. KL  ( π θ old ∥ π θ ) ≤ δ , \max_{\theta};L(\theta)=\mathbb{E}{s\sim d^{\pi{\theta_{\mathrm{old}}}}}\left[\sum_{a}\frac{\pi_{\theta}(a|s)}{\pi_{\theta_{\mathrm{old}}}(a|s)}A^{\pi_{\theta_{\mathrm{old}}}}(s,a)\right]\quad\text{s.t.}\quad\mathrm{KL}(\pi_{\theta_{\mathrm{old}}}|\pi_{\theta})\leq\delta,
(50)
where A π  ( s , a ) = Q π  ( s , a ) − V π  ( s ) A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s) is the advantage function. Linearizing L  ( θ ) L(\theta) around θ old \theta_{\mathrm{old}} and applying the quadratic KL approximation yields a Lagrangian whose closed-form solution is
θ new = θ old + 2  δ g ⊤  F − 1  g  F − 1  g , g = ∇ θ L  ( θ ) | θ old . \theta_{\mathrm{new}}=\theta_{\mathrm{old}}+\sqrt{\frac{2\delta}{g^{\top}F^{-1}g}},F^{-1}g,\qquad g=\nabla_{\theta}L(\theta)\big|{\theta{\mathrm{old}}}.
(51)
This is precisely the natural gradient direction, scaled so that the step saturates the KL budget δ \delta . The step size is determined entirely by the trust region geometry, not by a learning rate hyperparameter. In practice, TRPO solves the linear system F  v = g Fv=g via conjugate gradient and performs a backtracking line search to enforce the KL constraint exactly. 86 86 86 Conjugate gradient solves F  v = g Fv=g iteratively using only matrix-vector products F  v Fv , which can be computed via automatic differentiation without forming F F explicitly. With k k iterations it costs O  ( k  d ) O(kd) versus O  ( d 3 ) O(d^{3}) for direct inversion, making it feasible for neural networks with millions of parameters.
The theoretical guarantee underlying TRPO is a majorization-minimization (MM) argument. The surrogate L  ( θ ) L(\theta) is a local lower bound on J  ( θ ) J(\theta) that is tight at θ old \theta_{\mathrm{old}} : L  ( θ old ) = J  ( θ old ) L(\theta_{\mathrm{old}})=J(\theta_{\mathrm{old}}) and L  ( θ ) ≤ J  ( θ ) L(\theta)\leq J(\theta) within the trust region. 87 87 87 The bound follows from the performance difference lemma: J  ( π ′ ) − J  ( π ) = 1 1 − γ  𝔼 s ∼ d π ′  [ ∑ a π ′  ( a | s )  A π  ( s , a ) ] J(\pi^{\prime})-J(\pi)=\frac{1}{1-\gamma}\mathbb{E}{s\sim d^{\pi^{\prime}}}[\sum{a}\pi^{\prime}(a|s)A^{\pi}(s,a)] . Replacing d π ′ d^{\pi^{\prime}} with d π d^{\pi} introduces error controlled by the KL divergence between the two policies (Kakade, 2002) . Maximizing L L within the trust region therefore guarantees monotonic improvement: J  ( θ new ) ≥ L  ( θ new ) ≥ L  ( θ old ) = J  ( θ old ) J(\theta_{\mathrm{new}})\geq L(\theta_{\mathrm{new}})\geq L(\theta_{\mathrm{old}})=J(\theta_{\mathrm{old}}) . This is the same pattern as the EM algorithm in statistics, where the E-step constructs a surrogate (the ELBO) and the M-step maximizes it. 88 88 88 In EM, Q  ( θ | θ ( t ) ) Q(\theta|\theta^{(t)}) lower-bounds the log-likelihood and is tight at θ ( t ) \theta^{(t)} . Each M-step guarantees ℓ  ( θ ( t + 1 ) ) ≥ Q  ( θ ( t + 1 ) | θ ( t ) ) ≥ Q  ( θ ( t ) | θ ( t ) ) = ℓ  ( θ ( t ) ) \ell(\theta^{(t+1)})\geq Q(\theta^{(t+1)}|\theta^{(t)})\geq Q(\theta^{(t)}|\theta^{(t)})=\ell(\theta^{(t)}) . The TRPO bound has the same structure with L L playing the role of Q Q and J J playing the role of ℓ \ell . Shani et al. ( 2020) prove convergence for adaptive trust region methods that adjust δ \delta dynamically. Figure 9 illustrates this mechanism: each surrogate is a lower bound that touches J J at the current iterate, and sequential maximization produces monotonically improving iterates converging to θ ∗ \theta^{*} . 
Figure 9: Majorization-minimization interpretation of trust region updates. Left: the surrogate L  ( θ | θ old ) L(\theta|\theta_{\mathrm{old}}) (dashed) lower-bounds J  ( θ ) J(\theta) (solid) and is tight at θ old \theta_{\mathrm{old}} ; the trust region (shaded) constrains the step. The gap between L  ( θ new ) L(\theta_{\mathrm{new}}) and J  ( θ new ) J(\theta_{\mathrm{new}}) is the guaranteed improvement. Right: iterative MM convergence from θ 0 \theta_{0} through four surrogates (dashed, colored by iteration) to θ ∗ \theta^{*} .
PPO (Schulman et al., 2017) replaces the hard KL constraint with a clipped surrogate objective. Let r t  ( θ ) = π θ  ( a t | s t ) / π θ old  ( a t | s t ) r_{t}(\theta)=\pi_{\theta}(a_{t}|s_{t})/\pi_{\theta_{\mathrm{old}}}(a_{t}|s_{t}) denote the importance ratio. PPO maximizes
L clip  ( θ ) = 𝔼 t  [ min  ( r t  ( θ )  A t , clip  ( r t  ( θ ) , 1 − ε , 1 + ε )  A t ) ] , L^{\mathrm{clip}}(\theta)=\mathbb{E}{t}\left[\min!\big(r{t}(\theta)A_{t},;\mathrm{clip}(r_{t}(\theta),1-\varepsilon,1+\varepsilon)A_{t}\big)\right],
(52)
where ε \varepsilon (typically 0.1–0.2) bounds the ratio. When A t > 0 A_{t}>0 , clipping prevents r t r_{t} from exceeding 1 + ε 1+\varepsilon ; when A t < 0 A_{t}<0 , it prevents r t r_{t} from falling below 1 − ε 1-\varepsilon . The resulting feasible region is not an ellipsoid in parameter space but rather a non-convex set determined by the ratio constraint at each sampled state-action pair. PPO requires no Fisher information computation and uses only first-order gradients, making it the dominant method in large-scale applications including RLHF (Section 11.4). Figure 10 illustrates all three mechanisms in the LQC monetary policy setting, where the non-ellipsoidal PPO feasible region is visible in contrast to TRPO's KL ellipse.
The trust region framework connects naturally to econometric optimization. The Levenberg-Marquardt algorithm for nonlinear least squares uses a similar trust region mechanism, interpolating between gradient descent and Gauss-Newton steps. 89 89 89 Levenberg-Marquardt solves min θ  ‖ r  ( θ ) ‖ 2 \min_{\theta}|r(\theta)|^{2} by adding a damping term λ  I \lambda I to the Gauss-Newton Hessian approximation J ⊤  J J^{\top}J , which is equivalent to constraining the step to a trust region whose radius decreases with λ \lambda . TRPO replaces J ⊤  J J^{\top}J with the Fisher information matrix F  ( θ ) F(\theta) . More broadly, the Fisher information matrix that defines TRPO's trust region is the same object that appears in the Cramér-Rao bound: it measures the statistical precision of the policy parameterization. The natural gradient adapts step sizes to this precision, taking large steps in well-identified directions and small steps where the data provide little information about the policy. 
Figure 10: Trust region methods in the LQC monetary policy setting. A central bank learns a Taylor rule u t = − ( θ 1  x 1  t + θ 2  x 2  t ) u_{t}=-(\theta_{1}x_{1t}+\theta_{2}x_{2t}) mapping output gap x 1 x_{1} and inflation gap x 2 x_{2} to an interest rate instrument. Left: policy contour lines in state space for the current iterate θ old \theta_{\mathrm{old}} , optimal weights θ ∗ \theta^{*} , and the unconstrained gradient step θ bad \theta_{\mathrm{bad}} , with phase arrows showing closed-loop dynamics under θ old \theta_{\mathrm{old}} . Center: expected return J  ( θ 1 , θ 2 ) J(\theta_{1},\theta_{2}) in parameter space; hatching marks the unstable region. The KL trust region ellipse bounds the TRPO step; the unconstrained gradient step overshoots into the unstable region. Right: TRPO feasible region (KL ellipse) and PPO feasible region (50% ratio-clip band over 200 sampled state-action pairs) overlaid on J  ( θ ) J(\theta) , with the respective constrained steps marked.
5.5 Hybrid Methods
REINFORCE estimates policy gradients from sample returns (unbiased, high variance); TD methods use bootstrapped targets r + γ  V  ( s ′ ) r+\gamma V(s^{\prime}) (lower variance, biased when V V is approximate). Actor-critic methods combine both. The critic estimates the value function, the actor updates the policy using the critic's estimates.
5.5.1 Actor-Critic Architecture and Two-Timescale Convergence
The theoretical foundation is two-timescale stochastic approximation (Konda and Tsitsiklis, 2000) , building on the two-timescale ODE convergence theory of Borkar ( 1997) . 90 90 90 The original analysis of Konda and Tsitsiklis ( 2000) uses the average-cost formulation with TD error δ t = c  ( X t , U t ) − Λ + V  ( X t + 1 ) − V  ( X t ) \delta_{t}=c(X_{t},U_{t})-\Lambda+V(X_{t+1})-V(X_{t}) , where Λ \Lambda is the average cost. The discounted variant presented here follows by replacing the average-cost baseline with γ  V  ( s ′ ) \gamma V(s^{\prime}) . A related but distinct ODE stability framework for single-timescale stochastic approximation, including Q-learning and TD learning, appears in Borkar and Meyn ( 2000) . Run two concurrent learning processes:
where δ t = r t + γ  V ^  ( s t + 1 ; θ t ) − V ^  ( s t ; θ t ) \delta_{t}=r_{t}+\gamma\hat{V}(s_{t+1};\theta_{t})-\hat{V}(s_{t};\theta_{t}) is the TD error. The critic updates the value function parameters θ \theta ; the actor updates the policy parameters ω \omega .
Convergence requires the critic to learn faster than the actor.
lim t → ∞ α t ( a ) α t ( c ) = 0 , with both satisfying Robbins-Monro conditions. \lim_{t\to\infty}\frac{\alpha_{t}^{(a)}}{\alpha_{t}^{(c)}}=0,\quad\text{with both satisfying Robbins-Monro conditions.}
(55)
Under this separation, the actor sees a quasi-stationary critic: from the actor's perspective, the critic provides approximately correct value estimates at each step. 91 91 91 The two-timescale structure is analogous to nested optimization in structural estimation, where an inner loop solves for equilibrium given parameters and an outer loop searches over parameters. The critic's inner loop (policy evaluation) must converge before the actor's outer loop (policy improvement) takes a step. Wu et al. ( 2020) provide finite-time convergence rates ( O ~  ( ϵ − 2.5 ) \tilde{O}(\epsilon^{-2.5}) sample complexity) for two-timescale actor-critic with linear approximation, and Tian et al. ( 2023) establish analogous rates for single-timescale actor-critic with multi-layer neural networks. The actor's updates are then approximately unbiased policy gradient steps. Konda and Tsitsiklis ( 2000) prove convergence to a stationary point of J  ( ω ) J(\omega) (i.e., ∇ J  ( ω ) → 0 \nabla J(\omega)\to 0 ).
Convergence requires a structural condition on the critic. The critic's feature vectors must span the actor's score functions ∇ ω log  π ω  ( a | s ) \nabla_{\omega}\log\pi_{\omega}(a|s) , so that the critic's approximation error lies orthogonal to the policy gradient direction. Under this compatibility condition, the critic's projection error does not bias the actor's gradient estimates. 92 92 92 The compatible function approximation theorem first appears in Sutton et al. ( 2000) and is the key structural requirement in Konda and Tsitsiklis ( 2000) . It constrains the critic architecture to be “compatible” with the actor parameterization, the same condition that makes the natural policy gradient equal to the critic's weight vector in Kakade ( 2002) .
A2C (Advantage Actor-Critic) is the synchronous variant: collect a batch of transitions, compute TD errors, and update both networks. A3C (Mnih et al., 2016) parallelizes this across multiple workers updating a shared parameter server asynchronously. 93 93 93 Parallel workers decorrelate gradient estimates by exploring different parts of the state space simultaneously, removing the need for an experience replay buffer. Rigorous convergence theory for A3C's lock-free asynchronous parameter updates remains an open problem; existing analyses of asynchronous stochastic approximation (Qu and Wierman, 2020) address classical asynchrony (different state-action pairs updated at different times on a single trajectory), not the parallel-worker gradient setting.
5.5.2 Entropy Regularization and Soft Actor-Critic
SAC (Soft Actor-Critic) (Haarnoja et al., 2018) extends the actor-critic framework with entropy regularization, building on the soft Q-learning algorithm of Haarnoja et al. ( 2017) . The agent maximizes the entropy-augmented objective:
J τ ( θ ) = 𝔼 π θ [ ∑ t = 0 ∞ γ t ( R t + τ ℋ ( π θ ( ⋅ | s t ) ) ) ] , J_{\tau}(\theta)=\mathbb{E}{\pi{\theta}}\left[\sum_{t=0}^{\infty}\gamma^{t}\left(R_{t}+\tau\mathcal{H}(\pi_{\theta}(\cdot|s_{t}))\right)\right],
(56)
where ℋ  ( π ) = − ∑ a π  ( a )  log  π  ( a ) \mathcal{H}(\pi)=-\sum_{a}\pi(a)\log\pi(a) is the entropy and τ > 0 \tau>0 is the temperature parameter. Geist et al. ( 2019) later provided the unifying theoretical framework, showing that entropy regularization converts the Bellman optimality operator's non-smooth hard max into a smooth log-sum-exp, and that the resulting soft Bellman operator remains a γ \gamma -contraction, preserving the convergence guarantees of standard dynamic programming. 94 94 94 The optimal policy under entropy regularization is π ∗  ( a | s ) ∝ exp  ( Q ∗  ( s , a ) / τ ) \pi^{}(a|s)\propto\exp(Q^{}(s,a)/\tau) , which is precisely the McFadden ( 1974) logit choice probability with systematic utility Q ∗  ( s , a ) Q^{*}(s,a) and scale parameter τ \tau . The entropy-regularized value function is the log-sum-exp of Q-values, corresponding to the inclusive value (log-sum) operator in nested logit models. This equivalence between the soft-control framework and dynamic discrete choice models with EV1 taste shocks is developed formally in Rust and Rawat ( 2026) , Appendix A.
Entropy regularization also addresses the deadly triad directly. By maintaining policy stochasticity, the behavior policy used for data collection remains close to the target policy being optimized. This reduces the distribution mismatch between the stationary distribution under the behavior policy and the update targets, mitigating the off-policy instability leg of the triad. Cen et al. ( 2022) formalize a second benefit: entropy regularization accelerates convergence of the natural policy gradient from O  ( 1 / ϵ ) O(1/\epsilon) to O  ( log  ( 1 / ϵ ) ) O(\log(1/\epsilon)) , providing a precise sense in which smoothing the policy landscape aids optimization. The actor-critic structure separates identification from optimization: the critic solves a regression problem (estimate V π V^{\pi} from data), while the actor solves an optimization problem (improve π \pi using the estimated values).
5.5.3 Error Amplification Under Approximate Value Functions
Two questions remain important: how does approximation error propagate to policy quality, and how does computational complexity scale with problem size? Singh and Yee ( 1994) bound the policy degradation from value function errors (an independent derivation appears in Bertsekas and Tsitsiklis 1996 , Proposition 6.1). If V ^ \hat{V} approximates V ∗ V^{} with error ‖ V ^ − V ∗ ‖ ∞ ≤ ϵ |\hat{V}-V^{}|_{\infty}\leq\epsilon , and π ^ \hat{\pi} is the greedy policy with respect to V ^ \hat{V} , then:
‖ V ∗ − V π ^ ‖ ∞ ≤ 2  γ 1 − γ  ϵ . |V^{*}-V^{\hat{\pi}}|_{\infty}\leq\frac{2\gamma}{1-\gamma}\epsilon.
(57)
At γ = 0.99 \gamma=0.99 , the amplification factor is 2 ⋅ 0.99 / 0.01 = 198 2\cdot 0.99/0.01=198 . A 1% error in value function approximation yields at most 198% error in policy value. 95 95 95 The Singh-Yee bound is worst-case and not tight in general; massoud Farahmand et al. ( 2010) derive tighter bounds under smoothness assumptions on the MDP. The amplification factor 2  γ / ( 1 − γ ) 2\gamma/(1-\gamma) is a sensitivity analysis: it quantifies how errors in the “inputs” (value estimates) propagate to “outputs” (policy quality), analogous to errors-in-variables bias in regression. The discount factor γ \gamma controls sensitivity; more patient agents face larger amplification. This bound is pessimistic but finite: approximate value functions do not cause unbounded policy degradation.
5.5.4 Sample Complexity of Planning
Classical dynamic programming complexity scales with the state space size | 𝒮 | |\mathcal{S}| . For problems like Go, where | 𝒮 | ≈ 10 170 |\mathcal{S}|\approx 10^{170} , exact computation is impossible. Kearns et al. ( 2002) prove that with access to a generative model 96 96 96 A “generative model” in RL is a simulator that, given any state-action pair ( s , a ) (s,a) , returns a sampled next state s ′ ∼ P ( ⋅ | s , a ) s^{\prime}\sim P(\cdot|s,a) and reward r r . This is unrelated to “generative models” in machine learning (GANs, diffusion models) or “generative processes” in Bayesian econometrics. The distinction matters: planning with a generative model is strictly easier than learning from a single trajectory, because the agent can query arbitrary states rather than following a sequential path. (a simulator that samples transitions from any state-action pair), near-optimal planning is possible with no dependence on | 𝒮 | |\mathcal{S}| . The cost is exponential dependence on the effective horizon H = log  ( R max / ( ϵ  ( 1 − γ ) ) ) / log  ( 1 / γ ) H=\log(R_{\max}/(\epsilon(1-\gamma)))/\log(1/\gamma) : the sparse sampling algorithm requires O  ( ( | 𝒜 | / ϵ ) H ) O((|\mathcal{A}|/\epsilon)^{H}) simulator calls. 97 97 97 The sparse sampling algorithm builds a random tree of depth H H from the current state, sampling C C successor states per action at each node, then estimates values by averaging leaf rewards back up the tree. Its running time is O  ( ( C  | 𝒜 | ) H ) O((C|\mathcal{A}|)^{H}) , which is exponential in H H but entirely independent of | 𝒮 | |\mathcal{S}| . Kearns et al. ( 2002) also prove a lower bound of Ω  ( 2 H ) \Omega(2^{H}) generative model calls for any planning algorithm, so exponential horizon dependence is unavoidable in the worst case. For γ \gamma near 1, H ≈ ( 1 − γ ) − 1  log  ( R max / ϵ ) H\approx(1-\gamma)^{-1}\log(R_{\max}/\epsilon) , so the method is practical only for short effective horizons or moderate discount factors. The key insight is the tradeoff: classical DP scales linearly in | 𝒮 | |\mathcal{S}| but polynomially in H H ; sparse sampling eliminates state-space dependence at the cost of exponential horizon dependence. This explains why MCTS succeeds in large state spaces with bounded lookahead.
The minimax-optimal sample complexity for planning with a generative model, when queries to arbitrary state-action pairs are permitted, is Θ  ( | 𝒮 |  | 𝒜 | / ( ( 1 − γ ) 3  ϵ 2 ) ) \Theta(|\mathcal{S}||\mathcal{A}|/((1-\gamma)^{3}\epsilon^{2})) (Azar et al., 2013) . This bound scales linearly in | 𝒮 | |\mathcal{S}| but polynomially in 1 / ( 1 − γ ) 1/(1-\gamma) , the opposite regime from sparse sampling. Agarwal et al. ( 2020a) show that the plug-in model-based approach (learn P ^ \hat{P} from samples, then plan with P ^ \hat{P} ) achieves this minimax rate, establishing that model-based RL is statistically optimal. Li et al. ( 2024b) further tighten this result by breaking the | 𝒮 |  | 𝒜 | / ( 1 − γ ) 2 |\mathcal{S}||\mathcal{A}|/(1-\gamma)^{2} sample-size barrier, showing that the minimax rate is achievable with total sample size as low as | 𝒮 |  | 𝒜 | / ( 1 − γ ) |\mathcal{S}||\mathcal{A}|/(1-\gamma) . 98 98 98 Recent extensions push these results beyond standard MDPs. Clavier et al. ( 2024) study the robust MDP setting where the agent must plan under model uncertainty with sa-rectangular or s-rectangular uncertainty sets, establishing minimax rates for robust policy optimization. Wang et al. ( 2025) extend the analysis to risk-sensitive objectives under the iterated CVaR criterion.
5.6 Fundamental Tradeoffs
The choice between methods involves distinct tradeoffs rooted in DP structure. Value-based methods target Q ∗ Q^{*} via the Bellman contraction (Szepesvári, 2010) . In the tabular case convergence is guaranteed, but function approximation introduces the deadly triad. Policy-based methods optimize π θ \pi_{\theta} directly. Modern theory (Agarwal et al., 2021a) establishes global convergence for softmax policies, with high variance as the practical weakness rather than local traps. Actor-critic methods combine both (Konda and Tsitsiklis, 2000) , using the critic for low-variance value estimates while the actor inherits policy gradient's global convergence. Each family traces to DP foundations.
Four additional trade-offs pervade reinforcement learning. First, exploration versus exploitation: should the agent act on its current best estimate or gather information to improve future decisions? Lai and Robbins ( 1985) establish the fundamental lower bound: any consistent policy must incur regret at least logarithmic in the number of periods. Naive exploration ( ε \varepsilon -greedy) requires samples exponential in the horizon; strategic exploration (UCB, optimism in the face of uncertainty) reduces this to polynomial (Auer et al., 2002a) , formalizing the value of targeted experimentation. 99 99 99 The exploration-exploitation tradeoff is the subject of the bandits chapter, where the multi-armed bandit framework provides the sharpest analysis. In full MDPs, exploration is harder because the agent must learn not just reward distributions but also transition dynamics, compounding the information requirement.
Second, model-based versus model-free: model-based methods learn a transition model P ^  ( s ′ | s , a ) \hat{P}(s^{\prime}|s,a) and plan with it (Sutton, 1990) ; model-free methods learn value functions or policies directly from transitions. The Dyna architecture (Sutton, 1990) bridges these by generating simulated experience from the learned model to supplement real transitions. Model-based methods are sample-efficient (each transition updates the entire model, which improves value estimates for all states) but suffer asymptotic bias if the model class is misspecified; model-free methods are asymptotically unbiased but sample-inefficient, using each transition for a single gradient step. 100 100 100 Model misspecification in RL is the analog of omitted variable bias in econometrics: if the learned model omits relevant state variables or misspecifies the functional form of transitions, the resulting policy is biased regardless of sample size. Moerland et al. ( 2023) provide a comprehensive survey of model-based RL, analyzing the model-bias versus sample-efficiency tradeoff across method families.
Third, on-policy versus off-policy (Sutton and Barto, 2018, Ch. 5–7) : on-policy methods (SARSA, REINFORCE) learn from data generated by the current policy, ensuring stability but discarding past experience; off-policy methods (Q-learning, DQN) reuse stored experience via replay buffers, gaining sample efficiency but risking the instabilities of the deadly triad.
Fourth, bias versus variance in advantage estimation: REINFORCE uses the full Monte Carlo return (unbiased but high variance); actor-critic methods (Konda and Tsitsiklis, 2000) use bootstrapped TD targets (low variance but biased by the critic's approximation error). Generalized Advantage Estimation in PPO (Schulman et al., 2015) interpolates between these extremes via a parameter λ ∈ [ 0 , 1 ] \lambda\in[0,1] , where λ = 1 \lambda=1 recovers Monte Carlo returns and λ = 0 \lambda=0 recovers one-step TD. The value function baseline is the variance-minimizing choice, motivating the actor-critic architecture as a bias-variance compromise.
5.7 Conclusion
The central insight is that RL algorithms are not mysterious. They are asymptotic approximations to classical dynamic programming operators, justified by the mathematics of contractions, stochastic approximation, and gradient domination. Value iteration becomes Q-learning (Watkins and Dayan, 1992; Tsitsiklis, 1994) when expectations are replaced by single samples. Policy iteration becomes the natural policy gradient (Kakade, 2001; Agarwal et al., 2021a) when the greedy improvement step is approximated by gradient ascent, and NPG recovers PI exactly in the tabular case. The stochastic approximation framework, from the foundational work of Robbins ( 1952) through the ODE method of Borkar and Meyn ( 2000) , guarantees that under appropriate step-size conditions, noisy iterates converge to the same fixed points as their deterministic counterparts. Reinforcement learning is not a departure from dynamic programming but an extension of it. Tabular RL and RL with linear function approximation rest on solid theoretical foundations. Deep RL lacks comparable guarantees: convergence remains an open problem, and empirical successes remain case-specific.
6 The Empirics of Deep Reinforcement Learning
I review the empirical pathologies of deep reinforcement learning, their causes, and the diagnostic tools that expose them.
6.1 The Moving Target Problem
In supervised learning, the loss function is a fixed function of the training data and model parameters. Deep reinforcement learning does not enjoy this property. Each gradient step moves both the current value estimates and the targets simultaneously, creating a “nonstationary” optimization landscape. The target network heuristic introduced by Mnih et al. ( 2015) slows target drift by periodically freezing a copy of the network, but does not eliminate it. Therefore Bellman residual is a poor proxy for the accuracy of the value function.
Fujimoto et al. ( 2022) formalize this observation. Let Q π Q^{\pi} denote the true value function for policy π \pi , let Δ  ( s , a ) = Q  ( s , a ) − Q π  ( s , a ) \Delta(s,a)=Q(s,a)-Q^{\pi}(s,a) denote the value error, and let ε  ( s , a ) = Q  ( s , a ) − ( r + γ  𝔼 s ′ , a ′  [ Q  ( s ′ , a ′ ) ] ) \varepsilon(s,a)=Q(s,a)-(r+\gamma\mathbb{E}{s^{\prime},a^{\prime}}[Q(s^{\prime},a^{\prime})]) denote the Bellman error. Substituting the definition of Q π Q^{\pi} yields the key identity: ε  ( s , a ) = Δ  ( s , a ) − γ  𝔼 s ′ , a ′  [ Δ  ( s ′ , a ′ ) ] \varepsilon(s,a)=\Delta(s,a)-\gamma\mathbb{E}{s^{\prime},a^{\prime}}[\Delta(s^{\prime},a^{\prime})] . The Bellman error is a difference of value errors at consecutive states, not the value error itself. If the errors Δ  ( s , a ) \Delta(s,a) and Δ  ( s ′ , a ′ ) \Delta(s^{\prime},a^{\prime}) are correlated across time—the network is wrong in the same direction at successive state-action pairs—they cancel in the difference and the Bellman error is small regardless of how large the individual errors are. 101 101 101 In the extreme case, shifting all Q-values by the constant c / ( 1 − γ ) c/(1-\gamma) leaves the Bellman error unchanged at zero while increasing value error by c / ( 1 − γ ) c/(1-\gamma) .
The second failure mode is specific to finite datasets: Fujimoto et al. ( 2022, Corollary 1) show that over an incomplete dataset, zero Bellman error is consistent with arbitrarily large value error, because the network can fit unobserved successor pairs to whatever values make the observed residuals vanish. 102 102 102 The Bellman equation uniquely identifies Q π Q^{\pi} when enforced over the entire MDP, but over an incomplete dataset it admits infinitely many solutions. Whenever a transition ( s ′ , a ′ ) (s^{\prime},a^{\prime}) that is reachable from the dataset is not itself in the dataset, the network is free to set Q  ( s ′ , a ′ ) Q(s^{\prime},a^{\prime}) at unobserved pairs to whatever value makes the residual vanish on the observed ones, unconstrained by any loss. A network can thus reach near-zero training loss while the value function remains arbitrarily inaccurate over the full state space.
The dual failure mode appears in policy gradient methods: Ilyas et al. ( 2020) find that even when PPO's surrogate objective improves monotonically, episode return can plateau or decline, because the surrogate gradient is poorly aligned with the gradient of the true return. 103 103 103 Ilyas et al. ( 2020) examine the surrogate objective used in Proximal Policy Optimization (Schulman et al., 2017) . The PPO clipping mechanism is designed to keep policy updates within a trust region by bounding the probability ratio π θ  ( a | s ) / π θ old  ( a | s ) \pi_{\theta}(a|s)/\pi_{\theta_{\text{old}}}(a|s) . The gradient of the surrogate is poorly aligned with the gradient of the true return, particularly in later training phases where the policy has diverged from the behavior policy used to collect the replay data. The loss metric that practitioners monitor throughout training is measuring something other than what they care about.
6.2 The Reproducibility Crisis and Sensitivity to Random Seeds
Henderson et al. ( 2018) trained five leading policy gradient algorithms (PPO, TRPO, DDPG, TD3, SAC) on six MuJoCo benchmark environments, holding all hyperparameters fixed and varying only the random seed. The resulting learning curves from different seeds were non-overlapping: a seed that performed well under one algorithm performed comparably to a different algorithm's best seeds, making cross-algorithm comparison unreliable. 104 104 104 Differences as large as 2,000 points in final episode return arose from seed variation alone. Agarwal et al. ( 2021b) quantify the damage: comparing point estimates from 5 runs per task on Atari 100k yields Type I error exceeding 50%, meaning a random noise injection appears beneficial in half of all comparisons.
Agarwal et al. ( 2021b) propose the interquartile mean (IQM) as a replacement for mean and median when comparing algorithms. The IQM discards the top and bottom 25% of runs before averaging, reducing sensitivity to outlier seeds. Using these tools and stratified bootstrap confidence intervals, Agarwal et al. ( 2021b) find that several widely-cited algorithmic improvements on Atari 100k vanish or reverse when statistical uncertainty is accounted for. 105 105 105 They also introduce performance profiles, which plot the fraction of tasks and seeds where an algorithm achieves performance above a threshold τ \tau , as τ \tau varies from 0 to the maximum. Performance profiles reveal the full shape of the score distribution rather than collapsing it to a single statistic. 106 106 106 The fragility extends to hyperparameters. Eimer et al. ( 2023) conduct a systematic study of hyperparameter sensitivity across 6 algorithms and 17 environments, finding that default hyperparameters from published papers perform competitively in the specific environments used in those papers but generalize poorly across environments. Patterson et al. ( 2024) synthesize these findings into an empirical design handbook, recommending at minimum 10 seeds per configuration, IQM-based comparisons, and preregistration of hyperparameter search protocols.
6.3 Value Overestimation and Spikes
Q-learning uses the Bellman optimality update
Q  ( s , a ) ← r + γ  max a ′  Q  ( s ′ , a ′ ) , Q(s,a)\leftarrow r+\gamma\max_{a^{\prime}}Q(s^{\prime},a^{\prime}),
(58)
where the maximum is taken over the estimated Q-values of all actions at the successor state. Thrun and Schwartz ( 1993) identify a positive bias intrinsic to this update: if the Q-value estimates contain noise with mean zero, the maximum over noisy estimates is biased upward by Jensen's inequality. An agent that uses a single network for both action selection ( arg  max \arg\max ) and value estimation ( max  Q \max Q ) systematically overestimates the values of every state it visits, biasing the Bellman target upward at every update step. The bias compounds through bootstrapping: overestimated targets produce overestimated updates, which produce further overestimated targets.
van Hasselt ( 2010) propose double Q-learning as a remedy: maintain two independent Q-networks Q A Q_{A} and Q B Q_{B} . Use Q A Q_{A} to select the greedy action at s ′ s^{\prime} , but use Q B Q_{B} to evaluate that action. Because the two networks are trained on different data, their errors are approximately independent, and the positive bias largely cancels. van Hasselt et al. ( 2016b) implement this as Double DQN, using the online network for action selection and the periodically-frozen target network for evaluation. On 49 Atari games, Double DQN reduces overestimation by a factor of 3–5 and improves median performance by 20% relative to DQN.
Fujimoto et al. ( 2018) observe that Double DQN's correction is incomplete in continuous-action settings, where the target network and online network remain correlated through shared updates. They propose Clipped Double Q-learning: compute two Q-value estimates Q 1 , Q 2 Q_{1},Q_{2} with separate networks trained on the same data, and use y = r + γ  min  ( Q 1  ( s ′ , a ′ ) , Q 2  ( s ′ , a ′ ) ) y=r+\gamma\min(Q_{1}(s^{\prime},a^{\prime}),Q_{2}(s^{\prime},a^{\prime})) as the Bellman target. The minimum operator introduces pessimistic underestimation, which is conservative but avoids the explosive positive bias. 107 107 107 Ciosek et al. ( 2019) note that clipped double Q can cause excessive pessimism under high uncertainty, proposing optimistic actor-critic as a counterweight. 
Figure 11: Overestimation bias from Jensen's inequality with n = 2 n=2 actions. Blue: density of individual Q ^  ( s , a i ) ∼ 𝒩  ( μ , σ 2 ) \hat{Q}(s,a_{i})\sim\mathcal{N}(\mu,\sigma^{2}) . Red: density of max i  Q ^  ( s , a i ) \max_{i}\hat{Q}(s,a_{i}) , shifted right by σ / π ≈ 0.56 \sigma/\sqrt{\pi}\approx 0.56 . The shaded gap is the bias. With n = 100 n=100 actions the bias exceeds 2.5  σ 2.5\sigma .
DQN prevents outright divergence, but van Hasselt et al. ( 2018) find that soft divergence, defined as a temporary spike in value estimates by more than 10% followed by recovery, occurs in the majority of DQN training runs across 57 Atari games. 108 108 108 Larger networks diverge more frequently than smaller ones, counter to the usual intuition that more expressive models should generalize better. The deadly triad does not announce itself as a training failure: the value estimates may spike and recover, leaving no visible trace in the loss curve while corrupting the policy.
Kumar et al. ( 2021) describe a continuous manifestation of the deadly triad: implicit under-parameterization. 109 109 109 Neural networks trained with bootstrapped TD objectives progressively lose their effective rank, with fewer and fewer neurons contributing distinct directions in the representation. This rank collapse is silent (training loss continues to decrease) but the network's ability to represent new information degrades over time, a form of capacity loss distinct from but related to plasticity loss.
6.4 Plasticity Loss and Primacy Bias
A network that trains well at step t = 100 t=100 may be incapable of learning at step t = 100 , 000 t=100{,}000 , even if the data quality at the later step is higher. Lyle et al. ( 2022) call this capacity loss: the network's ability to update its own weights degrades progressively during training, measured by the fraction of effective parameters and the network's ability to fit new random labels. Lyle et al. ( 2023) extend this to plasticity loss, identifying dead ReLU neurons, weight norm growth, and feature rank collapse as three distinct mechanisms, not all of which co-occur.
Nikishin et al. ( 2022) identify primacy bias as a specific cause. Because the replay buffer is filled incrementally, early transitions are oversampled relative to later ones, and the network over-fits to early environment transitions, corrupting representations throughout the remainder of training. 110 110 110 Nikishin et al. ( 2022) show that 100 initial “priming” steps of excessive gradient updates degrade a SAC agent's performance for hundreds of thousands of subsequent steps. Sokar et al. ( 2023) measure the fraction of dormant neurons (units with near-zero activation across the replay buffer) accumulating monotonically during training. Dohare et al. ( 2024) find that standard deep networks lose all plasticity within a few million gradient steps in continual learning tasks.
The proposed remedies fall into three categories: periodic resets, continual backpropagation, and architectural interventions. 111 111 111 Periodic resets reinitialize the last layers of the network while retaining the replay buffer, allowing the agent to forget overfit representations without discarding experience (Nikishin et al., 2022; D'Oro et al., 2023) . Continual backpropagation replaces neurons with near-zero utility at each gradient step rather than waiting for a global reset (Dohare et al., 2024) . Architectural interventions—layer normalization (Lyle et al., 2025) , orthogonal initialization, spectral normalization—reduce the rate at which plasticity is lost by stabilizing gradient magnitudes and preventing weight norm growth.
6.5 Implementation Dominates Algorithmic Innovation
Engstrom et al. ( 2020) find that PPO with the clipping mechanism disabled performs indistinguishably from the full algorithm; TRPO (Schulman et al., 2015) with the same code-level additions matches PPO. 112 112 112 The non-clipping components that suffice are: observation normalization, reward normalization, value function clipping, global gradient norm clipping, orthogonal weight initialization, and the Adam optimizer. Andrychowicz et al. ( 2021) identify observation normalization, orthogonal initialization, and learning rate annealing as the three choices accounting for most variance across 250,000 agents and 250 hyperparameter configurations. Huang et al. ( 2022) catalog 37 implementation details required to reproduce PPO on Atari; 113 113 113 These include reward clipping to [ − 1 , 1 ] [-1,1] , frame stacking to 4 frames, a specific episode termination convention, and a numerically stable normalization of the advantage estimate. omitting any produces materially different results.
The most consequential implementation detail is the distinction between termination and truncation (Pardo et al., 2018) . In reinforcement learning, an episode can end for two distinct reasons: termination, where the environment reaches a natural absorbing state (the pole falls in CartPole, the robot falls in locomotion tasks), and truncation, where the episode is cut short by an external time limit. At a termination, the value of the successor state is zero: V  ( s term ) = 0 V(s_{\text{term}})=0 . At a truncation, the episode is merely paused and the successor state has non-zero value: V  ( s trunc ) ≠ 0 V(s_{\text{trunc}})\neq 0 . Treating truncated transitions as terminated substitutes zero for a non-zero bootstrap value at every time limit boundary, corrupting every Bellman update in the vicinity of episode boundaries. Pardo et al. ( 2018) show that this conflation degrades performance by 20–40% on standard MuJoCo benchmarks. 114 114 114 The Gymnasium API (Towers et al., 2024) enforces the distinction by returning separate terminated and truncated flags, but most pre-2022 codebases conflate them in the done flag.
6.6 Replay Buffer Pathologies and Reward Scaling
Experience replay (Lin, 1992) decouples the data collection and learning processes, allowing a single transition to be used for multiple gradient updates. The replay ratio (the number of gradient updates per environment step) governs the trade-off between sample efficiency and data staleness. Zhang and Sutton ( 2017) show that increasing the replay ratio beyond a modest threshold degrades performance. 115 115 115 At high replay ratios, the distribution shift between the current policy and the behavior policy that generated the stored data grows large enough to violate the off-policy assumptions of Q-learning. The relationship is non-monotone and environment-dependent, making replay buffer size a sensitive hyperparameter with no universal default.
Schaul et al. ( 2016) propose prioritized experience replay (PER). 116 116 116 PER samples transitions with probability proportional to the magnitude of their TD error, on the argument that high-error transitions are the most informative. Fedus et al. ( 2020) revisit PER on large-scale Atari experiments and find that uniform sampling from a large enough buffer matches or outperforms PER, while being simpler to implement and tune.
Reward scaling introduces a separate class of failure modes. Standard DQN (Mnih et al., 2015) clips rewards to [ − 1 , + 1 ] [-1,+1] across all environments to stabilize training. van Hasselt et al. ( 2016a) observe that reward clipping changes the objective: clipped rewards make all positive events equivalent regardless of magnitude, so the agent learns to maximize the frequency of positive events rather than their cumulative value. This substitution can produce policies that are locally rational under the clipped reward but qualitatively suboptimal under the true reward. van Hasselt et al. ( 2016a) propose PopArt as a remedy. 117 117 117 PopArt normalizes targets to have unit variance while adjusting the output layer so that the policy remains invariant to the normalization. PopArt allows consistent learning across reward scales spanning several orders of magnitude without reward clipping.
Skalse et al. ( 2022) formalize reward hacking and show that any non-constant proxy reward can in principle be exploited by a sufficiently capable optimizer. 118 118 118 Skalse et al. ( 2022) define a proxy as unhackable if increasing expected proxy return cannot decrease expected true return. Their main result states that for the set of all stochastic policies, two reward functions are unhackable only if one of them is constant. For deterministic policies and finite policy sets, non-trivial unhackable pairs exist, but the conditions are stringent.
6.7 Simulation Study: Bellman Error and Value Error in Offline Policy Evaluation
The MDP uses s = ( k , z ) s=(k,z) with k k on a 50-point log-spaced capital grid and z ∈ { 0.9 , 1.1 } z\in{0.9,1.1} following a Markov chain with persistence 0.8. Actions are next-period capital choices on the same grid. Reward is log  ( z  k α − k ′ ) \log(zk^{\alpha}-k^{\prime}) with α = 0.36 \alpha=0.36 , β = 0.96 \beta=0.96 . Rewards are shifted by − r ¯ -\bar{r} (mean reward over feasible pairs) to center Q ∗ Q^{} near zero, which avoids initialization issues without altering the optimal policy. The offline dataset 𝒟 \mathcal{D} consists of T = 2 , 000 T=2{,}000 transitions simulated from the closed-form optimal policy k ∗  ( k , z ) = α  β  z  k α k^{}(k,z)=\alpha\beta zk^{\alpha} . Since the optimal policy concentrates capital near its steady state, 𝒟 \mathcal{D} covers only 11 of the 4,795 feasible ( s , a ) (s,a) pairs—0.2% coverage—the distribution mismatch condition in Fujimoto et al. ( 2022, Corollary 1) .
Two algorithms are trained on 𝒟 \mathcal{D} . 119 119 119 50,000 gradient steps per seed, 3 seeds; two-layer MLP with 64 hidden units, Adam at 5 × 10 − 4 5\times 10^{-4} ; target network updated every 500 steps. BRM minimizes 𝔼 𝒟  [ ( Q  ( s , a ) − ( r + γ  max a ′  Q  ( s ′ , a ′ ) ) ) 2 ] \mathbb{E}{\mathcal{D}}[(Q(s,a)-(r+\gamma\max{a^{\prime}}Q(s^{\prime},a^{\prime})))^{2}] where both Q  ( s , a ) Q(s,a) and Q  ( s ′ , a ′ ) Q(s^{\prime},a^{\prime}) use the current network; gradients flow through both sides simultaneously. The key consequence is that the network can zero the residual at an observed pair ( s , a ) (s,a) by co-moving Q  ( s , a ) Q(s,a) and Q  ( s ′ , a ′ ) Q(s^{\prime},a^{\prime}) together, rather than moving either toward Q ∗ Q^{} . This is the opposite of supervised learning, where labels are fixed external targets that do not move with the model weights. FQE prevents this by using a frozen target network for Q  ( s ′ , a ′ ) Q(s^{\prime},a^{\prime}) ; the network must reduce Q  ( s , a ) Q(s,a) toward a target that does not respond to its own gradient steps. Every 500 steps we record the Bellman error on 𝒟 \mathcal{D} (current network on both sides) and the value error 1 | ℱ |  ∑ ( s , a ) ∈ ℱ | Q θ  ( s , a ) − Q ∗  ( s , a ) | \frac{1}{|\mathcal{F}|}\sum_{(s,a)\in\mathcal{F}}|Q_{\theta}(s,a)-Q^{}(s,a)| over all 4,795 feasible pairs. As a supervised baseline, OLS regression of log  c \log c on log  k \log k and log  z \log z is estimated on expanding windows. 120 120 120 Noise σ = 0.30 \sigma=0.30 ; windows from n = 10 n=10 to 2 , 000 2{,}000 ; held-out test set of 500 transitions.
The OLS baseline shows tight coupling between training and test loss (Pearson r = − 1.000 r=-1.000 ; Table 8). The RL results reproduce Fujimoto et al. ( 2022) in the economic model: BRM achieves Bellman error 816 × 816\times lower than FQE, yet both methods have nearly identical value error over the full MDP, yielding a VE/BE ratio three orders of magnitude higher for BRM. Both mechanisms from Section 6.1 operate: error cancellation on the 11 observed pairs and unconstrained Q  ( s ′ , a ′ ) Q(s^{\prime},a^{\prime}) at the 4,784 unobserved pairs.
Table 8: Bellman error on dataset 𝒟 \mathcal{D} and value error on the full MDP for BRM and FQE trained on offline Brock–Mirman data. BE is mean squared Bellman error evaluated with the current network on both sides; VE is mean absolute deviation from Q ∗ Q^{*} over all 4,795 feasible state-action pairs. 
Figure 12: Left: OLS regression of log consumption on log capital and log productivity, estimated on expanding windows from the Brock–Mirman optimal policy. Out-of-sample MSE (left axis, red) and out-of-sample R 2 R^{2} (right axis, blue) track each other with Pearson r = − 1.000 r=-1.000 . Right: BRM (orange) and FQE (blue) trained on offline Brock–Mirman data 𝒟 \mathcal{D} ( T = 2 , 000 T=2{,}000 transitions, 0.2% state-space coverage); note the log scale on the y y -axis. Solid lines show Bellman error on 𝒟 \mathcal{D} (current network both sides); dashed lines show mean absolute value error against Q ∗ Q^{*} over all 4,795 feasible state-action pairs; shaded bands are ± 1 \pm 1 SE over 3 seeds.
6.8 Discussion and Recommendations
Track episode return and policy entropy alongside training loss; entropy collapse and stagnating return are early warning signs of plasticity loss (Section 6.4). Use PPO or SAC as default baselines before implementing custom algorithms. Report at least 10 seeds per configuration with IQM-based comparisons (Section 6.2).
7 Reinforcement Learning for Optimal Control
A handful of organizations have deployed reinforcement learning beyond simulation, achieving measurable gains on specific large-scale problems. Each deployment required substantial domain engineering and scientific tuning; these remain exceptional cases rather than standard practice. I review the most prominent field deployments, including ride-hailing dispatch at DiDi, data center cooling at Google, hotel revenue management, and financial order execution, before concluding with a simulation study on the bus engine replacement problem. In each case, the RL agent's parameters were updated during a training phase conducted in simulation or on historical data, and the resulting policy was deployed with fixed weights (Section 2).
7.1 Ride-Hailing Dispatch
Each driver-passenger assignment changes the spatial distribution of available drivers, making ride-hailing dispatch a sequential optimization problem at a scale (tens of millions of daily rides at DiDi) where exact dynamic programming is intractable.
Qin et al. ( 2021) formalized DiDi's order dispatching as a semi-Markov decision process 121 121 121 A semi-Markov decision process generalizes the standard MDP by allowing variable time between decisions. The discount factor γ τ k \gamma^{\tau_{k}} depends on the actual time elapsed τ k \tau_{k} rather than applying a fixed per-step discount. where each driver is an independent agent. The state of a driver consists of location (discretized into hexagonal zones) and time (bucketed into intervals). The action is the order assigned to the driver, with the option to remain idle. The reward is the trip fare. State transitions are determined by trip destinations, as completing an order transports the driver from origin to destination, changing their spatial state. The stochasticity arises from future demand, which determines the available actions at each state. The per-driver value function V π  ( s ) V^{\pi}(s) represents the expected cumulative fare a driver can earn from state s s under dispatching policy π \pi :
V π  ( s ) = 𝔼  [ ∑ k = 0 ∞ γ τ k  r k ∣ s 0 = s , π ] , V^{\pi}(s)=\mathbb{E}\left[\sum_{k=0}^{\infty}\gamma^{\tau_{k}}r_{k}\mid s_{0}=s,\pi\right],
(59)
where τ k \tau_{k} is the time to complete the k k -th trip and r k r_{k} is the corresponding fare. The platform's objective is to maximize total driver income across the fleet, which decomposes into the sum of individual driver value functions.
Each dispatching window (a few seconds), the platform collects open orders and available drivers, constructs a bipartite graph, and solves a linear assignment problem. The edge weights are computed as the advantage of each driver-order match relative to the driver's current state value.
w i  j = r ^ i + γ τ ^ i  V  ( s j ′ ) − V  ( s j ) , w_{ij}=\hat{r}{i}+\gamma^{\hat{\tau}{i}}V(s_{j}^{\prime})-V(s_{j}),
(60)
where r ^ i \hat{r}{i} is the predicted fare for order i i , τ ^ i \hat{\tau}{i} is the estimated trip duration, and s j ′ s_{j}^{\prime} is the destination state. The value function is learned via temporal-difference methods from historical trip data. DiDi's Cerebellar Value Network (CVNet; Tang et al., 2019) uses hierarchical coarse-coding 122 122 122 Coarse-coding represents a value function as a weighted sum over overlapping rectangular or hexagonal tiles that partition the state space (Sutton and Barto, 2018) ; each state activates the tiles that contain it, and a hierarchical variant stacks tiles at multiple resolutions to allow both coarse and fine generalization simultaneously. with a multi-resolution hexagonal grid, enabling transfer learning 123 123 123 Transfer learning initializes a model for a new task (a new city) with parameters trained on related tasks (existing cities), on the assumption that learned representations of traffic and demand patterns generalize across contexts and require less data to reach good performance in the new setting. across cities and robustness to data sparsity in low-traffic zones.
Production deployment across more than 20 Chinese cities demonstrated modest but consistent improvements of 0.5–2% on key metrics, gains that required the full CVNet infrastructure (hierarchical coarse-coding, multi-resolution grids, transfer learning across cities) to achieve. Table 9 summarizes the reported gains from A/B tests using time-slice rotation, where algorithms alternate control of the platform in 3-hour blocks to avoid interference effects.
Table 9: DiDi dispatch deployment results from Qin et al. ( 2021) and Tang et al. ( 2019) .
Li et al. ( 2019) addressed the coordination challenge using mean-field multi-agent RL. With thousands of drivers making simultaneous decisions, the full multi-agent state space is intractable. The mean-field approximation replaces individual driver states with an aggregate distribution, allowing each driver to condition on the density of nearby drivers rather than their exact locations. Experiments on DiDi data showed improved fleet utilization compared to single-agent baselines.
Han et al. ( 2022) reported complementary results from Lyft, where the dispatching system optimizes driver assignment and repositioning jointly. Their value decomposition architecture 124 124 124 Value decomposition decomposes the platform's global matching objective into individual driver value functions, each estimable via temporal-difference learning. The global optimum is recovered by optimizing the sum of individual values. assigns credit to individual driver decisions within the global objective. The production system demonstrated improvements in rider wait times and driver utilization, providing a second data point suggesting that similar approaches may transfer across platforms.
At DiDi's volume, even 1% gains represent hundreds of thousands of additional completed rides per day, because dispatching is fundamentally a fleet positioning problem: today's assignments determine tomorrow's driver distribution.
7.2 Hotel Revenue Management
Budget hotel chains face a capacity allocation problem: how to dynamically distribute rooms across rate segments defined by discount level, with booking channels such as direct platforms and online travel agencies mapped to segments offering discounts ranging from less than 15% to over 40%. Demand is uncertain, cancellations are difficult to forecast, and hotel managers resist black-box optimization systems that override their judgment. Chen et al. ( 2023) deployed reinforcement learning at China Lodging Group (CLG), a budget hotel chain operating approximately 2,000 hotels across China, and conducted field experiments measuring the impact of RL-based capacity allocation on actual hotel revenue.
Their system uses a two-step design. The RL agent observes the state ( t , s ) (t,s) , where t t indexes the booking period within a T = 10 T=10 -period episode and s s is the average revenue per room sold to date, and selects an average discount level a ∈ { 10 % , 20 % , 30 % } a\in{10%,20%,30%} . A linear program then converts this scalar recommendation into a feasible capacity allocation across rate segments, accounting for each hotel's channel preferences. 125 125 125 The RL component uses a modified on-policy Monte Carlo method with ε \varepsilon -greedy exploration, updating Q-values from realized returns after each completed episode. Training on real operational data rather than simulated environments means the method adapts to demand non-stationarity without requiring an explicit demand model. This decomposition addresses practitioner acceptance, since managers understand a single discount recommendation, and circumvents the need to explicitly model demand arrivals or cancellation rates.
The field experiment randomly assigned five Hanting-brand hotels in Shanghai to the treatment group from ten candidates, with 271 additional Shanghai hotels serving as a donor pool for synthetic control estimation. 126 126 126 Synthetic control constructs a weighted combination of untreated hotels whose pre-treatment trend matches each treated hotel, avoiding the selection bias of simple before-after comparisons. Table 10 reports the average treatment effects over the pilot period (March–June 2015).
Table 10: Field experiment results from Chen et al. ( 2023) , measured via synthetic control.
The RevPAR gain is heterogeneous across treatment hotels; some improved primarily via higher occupancy rates, others via higher average daily rates, and others via both channels simultaneously.
7.3 E-Commerce Dynamic Pricing
E-commerce platforms face a pricing problem at a scale that defeats human specialists. Alibaba's Tmall.com lists millions of SKUs across thousands of product categories, each requiring daily price adjustments that account for demand elasticity, competitor behavior, inventory levels, and promotional calendars. Liu et al. ( 2019) deployed deep reinforcement learning agents for automated pricing on Tmall.com beginning July 2018, conducting field experiments on thousands of SKUs over several months.
The pricing MDP for product i i has state s i , t ∈ ℝ m s_{i,t}\in\mathbb{R}^{m} comprising four feature groups: price features (current and historical prices, price-to-cost ratio), sales features (units sold, conversion rate), customer traffic features (unique visitors uv i , t \text{uv}{i,t} , page views), and competitiveness features (price rank among similar products). The pricing period is d = 1 d=1 day. Actions are either discrete, a i , t ∈ { 1 , … , K } a{i,t}\in{1,\ldots,K} indexing price bins uniformly spaced between product-specific bounds [ P i , min , P i , max ] [P_{i,\min},P_{i,\max}] , or continuous, a i , t ∈ ℝ a_{i,t}\in\mathbb{R} . The reward is the difference of revenue conversion rates (DRCR):
r i , t = revenue i , t uv i , t − revenue i , t − τ uv i , t − τ , r_{i,t}=\frac{\text{revenue}{i,t}}{\text{uv}{i,t}}-\frac{\text{revenue}{i,t-\tau}}{\text{uv}{i,t-\tau}},
(61)
where uv i , t \text{uv}_{i,t} is unique visitors in period t t and τ \tau is a reference lag. 127 127 127 DRCR normalizes revenue by traffic to remove demand fluctuations unrelated to pricing. The differencing further removes product-specific level effects, yielding a reward signal that is more concave than raw revenue and improves convergence stability.
Two algorithms are deployed: DQN for the discrete action formulation and DDPG for continuous actions. Both are pre-trained from demonstrations using historical specialist pricing actions (DQfD, DDPGfD) to address cold-start. 128 128 128 Standard A/B testing is infeasible because Chinese e-commerce regulations prohibit displaying different prices to different customers for the same product simultaneously. Liu et al. ( 2019) instead evaluate using difference-in-differences against “simi-products” (similar products not subject to algorithmic pricing) as controls.
Table 11: Field experiment results from Liu et al. ( 2019) on Tmall.com. DRCR improvement is relative to the simi-product control group.
DDPG with continuous action space outperformed DQN with discrete bins across all daily pricing experiments, and both substantially outperformed manual expert pricing.
7.4 Financial Order Execution
The theoretical benchmark for optimal execution is the Almgren-Chriss framework (Almgren and Chriss, 2001) , which derives optimal deterministic schedules under linear impact assumptions. A trader liquidating Q Q shares over T T periods faces a tradeoff between timing risk and market impact. With risk-aversion parameter λ \lambda , price volatility σ \sigma , and temporary impact coefficient η \eta , the optimal remaining inventory at time t t follows the hyperbolic sine schedule:
x ∗  ( t ) = Q ⋅ sinh  ( κ  ( T − t ) ) sinh  ( κ  T ) , κ = λ  σ 2 η . x^{*}(t)=Q\cdot\frac{\sinh!\bigl(\kappa(T-t)\bigr)}{\sinh(\kappa T)},\quad\kappa=\sqrt{\frac{\lambda\sigma^{2}}{\eta}}.
(62)
This deterministic trajectory is the benchmark any adaptive method must beat. It prescribes front-loading or back-loading depending on the risk-impact balance, but cannot respond to realized order flow or spread dynamics.
Nevmyvaka et al. ( 2006) applied tabular Q-learning to execution on real limit order book data from NASDAQ stocks. 129 129 129 The dataset covers 500 trading days of millisecond-level limit order book snapshots for AMZN, QCOM, and NVDA. The state space contains approximately 10,000 states; the horizon is T = 60 T=60 seconds with discount γ = 1 \gamma=1 . The state at time t t is s t = ( t , q t , ψ t , Δ t ) s_{t}=(t,q_{t},\psi_{t},\Delta_{t}) , where t ∈ { 1 , … , T } t\in{1,\ldots,T} is time remaining, q t ∈ { 0 , 1 , … , Q } q_{t}\in{0,1,\ldots,Q} is inventory remaining, ψ t \psi_{t} is the discretized bid-ask spread, and Δ t \Delta_{t} is the discretized signed volume imbalance. 130 130 130 Signed volume imbalance is the difference between buy and sell order volume near the best prices, normalized by total volume; positive imbalance typically predicts short-term price increases. Actions a t ∈ { 0 , δ , 2  δ , … , q t } a_{t}\in{0,\delta,2\delta,\ldots,q_{t}} specify shares to execute in the current interval. The reward is the negative per-period slippage contribution:
r t = − a t  ( p t exec − p 0 ) , r_{t}=-a_{t}\bigl(p_{t}^{\text{exec}}-p_{0}\bigr),
(63)
where p 0 p_{0} is the mid-quote at order arrival and p t exec p_{t}^{\text{exec}} is the average execution price. Total implementation shortfall is I  S = − ∑ t = 1 T r t / Q IS=-\sum_{t=1}^{T}r_{t}/Q . 131 131 131 Implementation shortfall measures the total cost of executing a trade relative to the benchmark mid-quote at arrival. It captures market impact, timing cost, and opportunity cost of unexecuted shares. Because the objective is cost minimization, the Q-learning update uses min \min over next-period actions:
Q  ( s t , a t ) ← Q  ( s t , a t ) + α  [ r t + γ  min a ′  Q  ( s t + 1 , a ′ ) − Q  ( s t , a t ) ] . Q(s_{t},a_{t})\leftarrow Q(s_{t},a_{t})+\alpha\Bigl[r_{t}+\gamma\min_{a^{\prime}}Q(s_{t+1},a^{\prime})-Q(s_{t},a_{t})\Bigr].
(64)
The agent learns to condition on market microstructure signals: trading aggressively when spreads are narrow, waiting when order flow predicts favorable price movement, and accelerating near the deadline.
Table 12: Execution results from Nevmyvaka et al. ( 2006) on NASDAQ stocks. TWAP is the time-weighted average price baseline (equal-sized trades at uniform intervals).
The RL agent reduces execution costs by 12–19% over Almgren-Chriss. These results informed subsequent work on adaptive execution, though independently verified production deployments remain scarce in the public literature.
7.5 Supply Chain Inventory Management
Multi-echelon inventory systems coordinate ordering decisions across supply chain stages, where each stage's order becomes the next stage's incoming shipment. A retailer orders from a warehouse, which orders from a distribution center, which orders from a factory. The sequential nature creates complex dependencies, since an order placed upstream today affects downstream availability many periods later. The state space grows exponentially in the number of echelons, with K K stages each having M M possible inventory levels yielding M K M^{K} states. Classical inventory theory provides elegant solutions for special cases, most notably the echelon base-stock policy of Clark and Scarf ( 1960) .
The state s = ( I 1 , … , I K ) s=(I_{1},\ldots,I_{K}) records on-hand inventory at each stage, where stage 1 faces customer demand and stage K K is the most upstream. The action q ∈ { 0 , 1 , … , Q max } q\in{0,1,\ldots,Q_{\max}} is the order quantity placed at stage K K . Demand D t ∼ F D D_{t}\sim F_{D} arrives at stage 1 each period; unfilled demand is backordered. Shipments flow downstream, with stage k k receiving what stage k + 1 k+1 shipped in the previous period. The per-period cost combines holding, backorder, and ordering components.
c t = h  ∑ k = 1 K I k + + b ⋅ ( D t − I 1 ) + + c o ⋅ q t , c_{t}=h\sum_{k=1}^{K}I_{k}^{+}+b\cdot(D_{t}-I_{1})^{+}+c_{o}\cdot q_{t},
(65)
where I k + = max  ( 0 , I k ) I_{k}^{+}=\max(0,I_{k}) is on-hand inventory, ( x ) + = max  ( 0 , x ) (x)^{+}=\max(0,x) , h h is holding cost per unit, b b is backorder cost per unit, and c o c_{o} is ordering cost. The objective is to minimize expected discounted total cost.
Gijsbrechts et al. ( 2022) conducted a systematic evaluation of deep RL against classical base-stock policies across lost sales, dual sourcing, and multi-echelon configurations. The classical benchmark is the echelon base-stock policy, in which each stage k k maintains an echelon inventory position and orders to bring this position to a target level S k S_{k} . 132 132 132 Formally, the echelon inventory position at stage k k equals on-hand inventory at k k plus all inventory at downstream stages 1 , … , k − 1 1,\ldots,k-1 plus in-transit inventory, minus backorders. The echelon base-stock policy of Clark and Scarf ( 1960) is optimal for serial systems with linear costs and backorders. For single-echelon systems with backorders, the optimal base-stock level is given by the newsvendor critical fractile S ∗ = F D − 1  ( b / ( b + h ) ) S^{*}=F_{D}^{-1}(b/(b+h)) . Table 13 summarizes results from their multi-echelon experiments.
Table 13: Multi-echelon inventory results from Gijsbrechts et al. ( 2022) .
Where classical solutions exist, RL underperforms: the base-stock policy remains highly competitive when properly calibrated, and DRL required millions of training transitions to approach performance levels achievable through closed-form calculation. RL struggles particularly with multi-echelon coupling, where upstream orders affect downstream costs many periods later. 133 133 133 Credit assignment refers to the difficulty of determining which past actions caused a delayed reward or cost. In multi-echelon systems, an upstream ordering decision today may not affect customer-facing costs for many periods, making it difficult for RL to learn the causal connection. The value proposition for RL lies in problems where analytical solutions are unavailable: non-stationary demand, complex operational constraints, or cost structures that do not admit tractable decomposition. Even in these settings, successful deployment remains rare and requires extensive simulation infrastructure, domain expertise, and careful calibration against classical baselines.
7.6 Real-Time Bidding
Real-time bidding for display advertising presents a budget pacing problem: an advertiser must allocate a fixed budget B 0 B_{0} across a campaign of T T auctions to maximize total conversions. Each impression is a second-price auction; the advertiser submits a bid and pays the second-highest bid if they win. The challenge is that bidding aggressively depletes budget early, while conservative bidding leaves value on the table.
Wu et al. ( 2018) formalized this as an MDP with state s t = ( B t , t , w t ) s_{t}=(B_{t},t,w_{t}) , where B t B_{t} is remaining budget, t t is auctions remaining, and w t w_{t} is the recent win rate. The action is a bid multiplier λ t ∈ [ λ min , λ max ] \lambda_{t}\in[\lambda_{\min},\lambda_{\max}] , so the actual bid is b t = λ t ⋅ b ¯ b_{t}=\lambda_{t}\cdot\bar{b} , where b ¯ \bar{b} is a base bid calibrated to the estimated value-per-impression. The clearing price c t c_{t} is drawn from a distribution F c F_{c} estimated from historical data; the advertiser wins if b t ≥ c t b_{t}\geq c_{t} . The per-auction reward is:
r t = 𝟙  { b t ≥ c t } ⋅ cvr t , r_{t}=\mathbbm{1}{b_{t}\geq c_{t}}\cdot\mathrm{cvr}_{t},
(66)
where cvr t ∈ { 0 , 1 } \mathrm{cvr}{t}\in{0,1} is the conversion indicator. Budget evolves as B t + 1 = B t − 𝟙  { b t ≥ c t } ⋅ c t B{t+1}=B_{t}-\mathbbm{1}{b_{t}\geq c_{t}}\cdot c_{t} , and the episode terminates when B t ≤ 0 B_{t}\leq 0 or t = 0 t=0 . 134 134 134 The state space is discretized into budget bins and time bins. Wu et al. ( 2018) augment the state with bid landscape features derived from historical clearing price distributions, giving the agent information about current market competitiveness.
The agent is a deep Q-network trained on a simulator calibrated to production RTB data. Table 14 reports performance relative to rule-based pacing baselines. The DQN agent improves total conversions by conserving budget during high-competition periods and bidding aggressively when clearing prices are low, a pattern the rule-based approaches cannot learn.
Table 14: Real-time bidding results from Wu et al. ( 2018) . Performance is relative to linear pacing on a simulator calibrated to production data.
7.7 Simulation Study: Bus Engine Replacement
I conclude with a simulation demonstrating that RL matches dynamic programming on a classical economics benchmark. The bus engine replacement problem, introduced by Rust ( 1987) , models a fleet manager's monthly decision whether to replace engines based on accumulated mileage. Replacement incurs a fixed cost but resets mileage to zero; continued operation incurs maintenance costs increasing in mileage.
I extend the single-engine problem to a fleet of N N engines with a capacity constraint limiting replacements per period. The state s = ( m 1 , … , m N ) s=(m_{1},\ldots,m_{N}) records discretized mileage for each engine. Actions are subsets of engines to replace, subject to the capacity constraint. The per-period cost is c  ( s , a ) = α  ∑ i m i + β  | a | c(s,a)=\alpha\sum_{i}m_{i}+\beta|a| , where α \alpha is the operating cost per unit mileage and β \beta is the replacement cost. 135 135 135 The mileage-dependent operating cost α  ∑ i m i \alpha\sum_{i}m_{i} follows Rust's original specification c  ( x , θ 1 ) = θ 11  x c(x,\theta_{1})=\theta_{11}x , creating a non-trivial threshold replacement policy. The fleet extension uses deterministic mileage increments to isolate the combinatorial scaling challenge that arises from the joint state of multiple engines. Mileage evolves deterministically; replaced engines reset to m = 0 m=0 ; others increment by one bin. 136 136 136 With M = 6 M=6 mileage bins, the state space is 6 N 6^{N} : 1,296 states at N = 4 N=4 , 7,776 at N = 5 N=5 , 46,656 at N = 6 N=6 . Value iteration is feasible for N ≤ 5 N\leq 5 .
Figure 13 compares dynamic programming, DQN, and heuristic baselines across fleet sizes. 
Figure 13: Bus engine replacement benchmark. Left: computation time vs. fleet size (log scale). Right: discounted return vs. fleet size for DP, DQN, and heuristic baselines. At N = 6 N=6 (46,656 states), DP is infeasible (no data point).
For N = 1 N=1 through 5 5 where both methods are computable, DQN matches DP within 1% of the optimal discounted return. At N = 6 N=6 (46,656 states), DP is infeasible but DQN produces a policy. The threshold heuristic, which replaces engines above a mileage cutoff, provides a reasonable baseline but cannot account for capacity constraints or the joint state of multiple engines. The never-replace heuristic performs poorly due to accumulated mileage costs, confirming that the cost structure creates a non-trivial replacement decision.
8 Structural Estimation with Reinforcement Learning
Several recent papers have used RL training loops, 137 137 137 Throughout this chapter, the RL training loop runs entirely inside the econometrician's computational model; the agent never interacts with real economic agents or markets but serves as a numerical method for solving the Bellman equation within a structural estimation procedure (Section 2). There is no execution phase in the usual sense. namely Q-learning, temporal-difference learning, policy gradient, and actor-critic methods, to solve structural economic models at scales where conventional dynamic programming fails. 138 138 138 I exclude papers that use neural network function approximation without an RL training mechanism. Inverse reinforcement learning is treated in the sister survey (Rust and Rawat, 2026) . Throughout this chapter I adopt a unified notation. An MDP is a tuple ( 𝒮 , 𝒜 , P , r , γ ) (\mathcal{S},\mathcal{A},P,r,\gamma) where 𝒮 \mathcal{S} is the state space, 𝒜 \mathcal{A} is the action space, P  ( s ′ | s , a ) P(s^{\prime}|s,a) is the transition kernel, r  ( s , a ) r(s,a) is the per-period reward, and γ ∈ [ 0 , 1 ) \gamma\in[0,1) is the discount factor. 139 139 139 Several of the papers reviewed here use β \beta for the discount factor, following economics convention. I translate all results to γ \gamma for consistency with the RL literature and the rest of this survey. A policy π : 𝒮 → Δ  ( 𝒜 ) \pi:\mathcal{S}\to\Delta(\mathcal{A}) maps states to distributions over actions. The value function under π \pi is V π  ( s ) = 𝔼 π  [ ∑ t = 0 ∞ γ t  r  ( s t , a t ) ∣ s 0 = s ] V^{\pi}(s)=\mathbb{E}{\pi}\left[\sum{t=0}^{\infty}\gamma^{t}r(s_{t},a_{t})\mid s_{0}=s\right] , and the action-value function is Q π  ( s , a ) = r  ( s , a ) + γ  𝔼 s ′ ∼ P ( ⋅ | s , a )  [ V π  ( s ′ ) ] Q^{\pi}(s,a)=r(s,a)+\gamma\mathbb{E}{s^{\prime}\sim P(\cdot|s,a)}[V^{\pi}(s^{\prime})] . The optimal value function satisfies V ∗  ( s ) = max a ∈ 𝒜  Q ∗  ( s , a ) V^{*}(s)=\max{a\in\mathcal{A}}Q^{*}(s,a) .
The canonical structural estimation framework for MDPs was formulated by Rust ( 1994) , whose nested fixed-point (NFXP) algorithm embeds the Bellman equation inside a maximum likelihood estimator. The methods reviewed in this chapter replace the inner fixed-point computation with RL-based approximations. 
Figure 14: NFXP versus RL-based structural estimation. Top: the nested fixed-point algorithm evaluates the likelihood by solving the Bellman equation to convergence inside each optimizer step. Bottom: single-loop stochastic approximation updates structural parameters θ \theta and value/policy weights ω \omega simultaneously from data batches. The NFXP algorithm is due to Rust ( 1987) .
8.0.1 Adusumilli and Eckardt (2022): TD Learning for CCP Estimation
Adusumilli et al. ( 2022) adapt temporal-difference (TD) learning to estimate the recursive terms that arise in CCP-based estimation, entirely avoiding specification or estimation of transition densities.
The CCP approach requires computing two functions h : 𝒜 × 𝒮 → ℝ d h:\mathcal{A}\times\mathcal{S}\to\mathbb{R}^{d} and g : 𝒜 × 𝒮 → ℝ g:\mathcal{A}\times\mathcal{S}\to\mathbb{R} that solve the recursive equations
where e  ( a , s ) = γ E − ln  P  ( a | s ) e(a,s)=\gamma_{\text{E}}-\ln P(a|s) under logit errors ( γ E \gamma_{\text{E}} denoting the Euler constant), and the expectation is over the next-period state-action pair ( s ′ , a ′ ) (s^{\prime},a^{\prime}) given the transition kernel P  ( s ′ | s , a ) P(s^{\prime}|s,a) and the observed policy P  ( a | s ) P(a|s) . Both h h and g g satisfy a Bellman-like recursion under the observed (data-generating) policy, not the optimal policy, so standard TD learning applies directly. Adusumilli et al. ( 2022) propose two methods.
The first is the linear semi-gradient method. 140 140 140 The method is called “semi-gradient” because it computes the gradient of only the prediction ϕ  ( a , s ) ⊤  w \phi(a,s)^{\top}w with respect to w w , not the full TD error including the bootstrap target ϕ  ( a ′ , s ′ ) ⊤  w \phi(a^{\prime},s^{\prime})^{\top}w . This avoids differentiating through the target but sacrifices guaranteed convergence in some settings. Approximate h  ( a , s ) ≈ ϕ  ( a , s ) ⊤  w h(a,s)\approx\phi(a,s)^{\top}w where ϕ : 𝒜 × 𝒮 → ℝ p \phi:\mathcal{A}\times\mathcal{S}\to\mathbb{R}^{p} is a vector of basis functions (e.g., polynomials in state variables) and w ∈ ℝ p w\in\mathbb{R}^{p} are the weights to be estimated. The TD(0) fixed-point equation is
𝔼  [ ϕ  ( a , s )  ( ϕ  ( a , s ) − γ  ϕ  ( a ′ , s ′ ) ) ⊤ ]  w = 𝔼  [ ϕ  ( a , s )  z  ( s , a ) ] . \mathbb{E}\left[\phi(a,s)\left(\phi(a,s)-\gamma\phi(a^{\prime},s^{\prime})\right)^{\top}\right]w=\mathbb{E}\left[\phi(a,s),z(s,a)\right].
(69)
The sample analog replaces population expectations with averages over the observed panel.
w ^ = ( 1 n  ( T − 1 )  ∑ i = 1 n ∑ t = 1 T − 1 ϕ i  t  ( ϕ i  t − γ  ϕ i , t + 1 ) ⊤ ) − 1  ( 1 n  ( T − 1 )  ∑ i = 1 n ∑ t = 1 T − 1 ϕ i  t  z i  t ) , \hat{w}=\left(\frac{1}{n(T-1)}\sum_{i=1}^{n}\sum_{t=1}^{T-1}\phi_{it}\left(\phi_{it}-\gamma\phi_{i,t+1}\right)^{\top}\right)^{-1}\left(\frac{1}{n(T-1)}\sum_{i=1}^{n}\sum_{t=1}^{T-1}\phi_{it},z_{it}\right),
(70)
where ϕ i  t = ϕ  ( a i  t , s i  t ) \phi_{it}=\phi(a_{it},s_{it}) and z i  t = z  ( s i  t , a i  t ) z_{it}=z(s_{it},a_{it}) . This requires inverting a p × p p\times p matrix, where p p is the number of basis functions, making computation trivial in most settings. No transition density estimation is needed, since the method uses only observed sequences of current and next-period state-action pairs.
The second method is approximate value iteration (AVI), which iterates the Bellman-like operator using nonparametric regression. At iteration k k , one constructs pseudo-outcomes
Y i  t ( k ) = z i  t + γ  h ^ ( k − 1 )  ( a i , t + 1 , s i , t + 1 ) Y_{it}^{(k)}=z_{it}+\gamma,\hat{h}^{(k-1)}(a_{i,t+1},s_{i,t+1})
(71)
and then fits h ^ ( k ) \hat{h}^{(k)} by regressing Y i  t ( k ) Y_{it}^{(k)} on ( a i  t , s i  t ) (a_{it},s_{it}) using any machine learning method, including LASSO, random forests, or neural networks. 141 141 141 LASSO (Tibshirani, 1996) adds an ℓ 1 \ell_{1} penalty to a regression loss, shrinking many coefficients to zero for sparse solutions; random forests average many decision trees fit to random subsamples and feature subsets for nonparametric estimation; neural networks compose affine transformations with elementwise nonlinearities across multiple layers. This is the first DDC estimator compatible with arbitrary ML prediction methods, enabling application to very high-dimensional state spaces.
With h ^ \hat{h} and g ^ \hat{g} in hand, structural parameters are recovered by pseudo-maximum likelihood estimation (PMLE). For continuous state spaces, Adusumilli et al. ( 2022) derive a locally robust correction to the PMLE criterion that accounts for the nonparametric first-stage estimation of value terms, restoring n \sqrt{n} -convergence of θ ^ \hat{\theta} . 142 142 142 An estimator has n \sqrt{n} -convergence if its error shrinks at rate n − 1 / 2 n^{-1/2} where n n is the sample size. This is the standard parametric rate; slower rates (e.g., n − 1 / 4 n^{-1/4} ) indicate efficiency loss from nonparametric first stages. The PMLE score is m  ( a , s ; θ , h , g ) = ∂ θ ln  π  ( a , s ; θ , h , g ) m(a,s;\theta,h,g)=\partial_{\theta}\ln\pi(a,s;\theta,h,g) , where π \pi is the logit choice probability with continuation value V  ( a , s ) = h  ( a , s ) ⊤  θ + g  ( a , s ) V(a,s)=h(a,s)^{\top}\theta+g(a,s) . The naive estimator solves 𝔼 n  [ m  ( a , s ; θ , h ^ , g ^ ) ] = 0 \mathbb{E}_{n}[m(a,s;\theta,\hat{h},\hat{g})]=0 , but with continuous states this moment condition is not orthogonal to the first-stage estimates and converges slower than n \sqrt{n} . The locally robust moment adds a debiasing correction:
ζ = m  ( a , s ; θ , h , g ) − λ  ( a , s ; θ )  { z  ( s , a ) ⊤  θ + γ  e  ( a ′ , s ′ ) + γ  V  ( a ′ , s ′ ) − V  ( a , s ) } , \zeta=m(a,s;\theta,h,g)-\lambda(a,s;\theta)\left{z(s,a)^{\top}\theta+\gamma,e(a^{\prime},s^{\prime})+\gamma,V(a^{\prime},s^{\prime})-V(a,s)\right},
(72)
where λ  ( a , s ; θ ) \lambda(a,s;\theta) solves a backward recursion that propagates the influence of estimation error through the dynamic structure. 143 143 143 The term in braces is the temporal-difference error of the continuation value V V . The adjoint λ \lambda weights this TD error by its marginal impact on the PMLE score. See Online Appendix B.3 of Adusumilli et al. ( 2022) for the derivation. The corrected estimator θ ^ L  R \hat{\theta}{LR} solves 𝔼 n  [ ζ n ] = 0 \mathbb{E}{n}[\zeta_{n}]=0 and is computationally no harder than the naive PMLE, since the correction is constant in θ \theta .
Theorem 2 ( Adusumilli et al. ( 2022) , Theorem 1).
Under regularity conditions, the linear semi-gradient estimator h ^ \hat{h} satisfies ‖ h ^ − h ‖ 2 = O P  ( n − 1 / 2  ( T − 1 ) − 1 / 2 ) |\hat{h}-h|{2}=O{P}(n^{-1/2}(T-1)^{-1/2}) , where ∥ ⋅ ∥ 2 |\cdot|{2} denotes the L 2  ( P ) L^{2}(P) norm. 144 144 144 The L 2  ( P ) L^{2}(P) norm is ‖ f ‖ 2 = ( ∫ f  ( x ) 2  𝑑 P  ( x ) ) 1 / 2 |f|{2}=(\int f(x)^{2},dP(x))^{1/2} , measuring average squared deviation under the probability measure P P . This is the natural norm for mean-squared-error analysis.
Theorem 3 ( Adusumilli et al. ( 2022) , Theorem 5).
Under regularity conditions on the ML method used in AVI, the locally robust PMLE estimator θ ^ L  R \hat{\theta}{LR} satisfies n  ( θ ^ L  R − θ ∗ ) → 𝑑 𝒩  ( 0 , Σ ) \sqrt{n}(\hat{\theta}{LR}-\theta^{*})\xrightarrow{d}\mathcal{N}(0,\Sigma) for an explicit variance Σ \Sigma , even when the state space is continuous.
Monte Carlo experiments on a dynamic firm entry model with seven structural parameters and five continuous state variables show that the TD-based estimators achieve a 4- to 11-fold reduction in mean squared error compared to CCP estimators using state-space discretization.
For dynamic discrete games, the method extends naturally. Standard CCP-based estimation of games requires integrating out other players' actions, which becomes intractable with many players or continuous states. TD learning avoids this entirely, since it works directly with the joint empirical distribution of states and their successors. The “integrating out” is done implicitly within sample expectations.
8.0.2 Hu and Yang (2025): Policy Gradient for DDC Estimation
Hu and Yang ( 2025) combine policy gradient methods with the Simulated Method of Moments (SMM) to estimate DDCs, with particular focus on models with unobserved state variables.
The outer loop is SMM. 145 145 145 SMM (Gourieroux et al., 1993) estimates structural parameters by matching moments from simulated data to moments from observed data, avoiding direct evaluation of the likelihood function. Define a vector of data moments 𝐌 d \mathbf{M}{d} computed from the observed panel. For candidate structural parameters θ \theta and transition parameters ξ \xi , simulate the model to produce simulated moments 𝐌 s  ( θ , ξ ) \mathbf{M}{s}(\theta,\xi) . The estimator minimizes
( θ ^ , ξ ^ ) = arg min θ , ξ ( 𝐌 d − 𝐌 s ( θ , ξ ) ) ⊤ 𝐖 ( 𝐌 d − 𝐌 s ( θ , ξ ) ) , (\hat{\theta},\hat{\xi})=\arg\min_{\theta,\xi}\left(\mathbf{M}{d}-\mathbf{M}{s}(\theta,\xi)\right)^{\top}\mathbf{W}\left(\mathbf{M}{d}-\mathbf{M}{s}(\theta,\xi)\right),
(73)
where 𝐖 \mathbf{W} is a positive definite weight matrix. Computing 𝐌 s  ( θ , ξ ) \mathbf{M}_{s}(\theta,\xi) requires solving for the optimal policy under ( θ , ξ ) (\theta,\xi) , which is the inner-loop problem.
The inner loop parametrizes the choice probability directly as a logistic function of state variables. For a binary choice J t ∈ { 0 , 1 } J_{t}\in{0,1} , the general form is Pr  ( J t = 1 ∣ 𝑿 t ; 𝜸  ( θ ) ) = logistic  ( 𝑿 t  𝜸  ( θ ) ) \Pr(J_{t}=1\mid\boldsymbol{X}{t};\boldsymbol{\gamma}(\theta))=\text{logistic}(\boldsymbol{X}{t}\boldsymbol{\gamma}(\theta)) , where 𝜸  ( θ ) \boldsymbol{\gamma}(\theta) are policy parameters that depend on the structural parameters. 146 146 146 The linear index can be replaced by higher-order terms of 𝑿 t \boldsymbol{X}{t} or deep neural networks; the method requires only that the gradient ∇ 𝜸 log  π 𝜸 \nabla{\boldsymbol{\gamma}}\log\pi_{\boldsymbol{\gamma}} has a closed form. In their application to a Rust bus engine model with unobserved bus condition S t ∗ S_{t}^{*} , this takes the form
Pr  ( J t = 1 ∣ X t , S t ∗ , t ; 𝜸 ) = exp  ( γ 0 + γ 1  t + γ 2  X t + γ 3  S t ∗ ) 1 + exp  ( γ 0 + γ 1  t + γ 2  X t + γ 3  S t ∗ ) , \Pr(J_{t}=1\mid X_{t},S_{t}^{},t;\boldsymbol{\gamma})=\frac{\exp(\gamma_{0}+\gamma_{1}t+\gamma_{2}X_{t}+\gamma_{3}S_{t}^{})}{1+\exp(\gamma_{0}+\gamma_{1}t+\gamma_{2}X_{t}+\gamma_{3}S_{t}^{*})},
(74)
where t t enters the index directly to capture time-varying replacement incentives. The policy parameters are updated by REINFORCE-style gradient ascent, applying the policy gradient theorem (Sutton et al., 1999) :
∇ 𝜸 V  ( 𝜸 ) = 𝔼  [ ∑ t = 0 T ∇ 𝜸 log  π 𝜸  ( J t ∣ X t , S t ∗ , t )  Q π 𝜸  ( X t , S t ∗ , J t ) ] , \nabla_{\boldsymbol{\gamma}}V(\boldsymbol{\gamma})=\mathbb{E}\left[\sum_{t=0}^{T}\nabla_{\boldsymbol{\gamma}}\log\pi_{\boldsymbol{\gamma}}(J_{t}\mid X_{t},S_{t}^{},t),Q^{\pi_{\boldsymbol{\gamma}}}(X_{t},S_{t}^{},J_{t})\right],
(75)
where Q π 𝜸 Q^{\pi_{\boldsymbol{\gamma}}} is the action-value function under the current policy, estimated by Monte Carlo returns from forward-simulated trajectories.
The main contribution is handling unobserved state variables. When state variables are only partially observed, the policy in ( 74) is parametrized as a function of both X t X_{t} and S t ∗ S_{t}^{*} , and the algorithm forward-simulates trajectories of both observed and unobserved variables.
Building on the nonparametric identification results of Hu and Shum ( 2012) , the outer-loop SMM targets moments from five consecutive periods of observed data, which suffice to separately identify the structural parameters θ \theta and transition parameters ξ \xi without requiring the econometrician to observe S t ∗ S_{t}^{*} . No discretization of continuous unobserved states is needed; the same algorithm handles both discrete and continuous unobserved heterogeneity.
For each candidate ( θ , ξ ) (\theta,\xi) in the outer minimization ( 73), the inner loop runs policy gradient until convergence, producing optimal policy parameters 𝜸 ∗  ( θ , ξ ) \boldsymbol{\gamma}^{*}(\theta,\xi) . These are used to simulate data and compute 𝐌 s  ( θ , ξ ) \mathbf{M}_{s}(\theta,\xi) .
On an extended Rust bus engine model with a continuous unobserved bus condition following an AR(1) process, estimates of seven structural parameters are centered around their true values across 400 simulations. On a discrete-unobservable variant, the method matches the precision of Arcidiacono and Miller ( 2011) 's two-step EM algorithm at comparable computation times, though the advantage diminishes as more inner-loop iterations are used for precision.
8.1 Dynamic Oligopoly and Strategic Interaction
Dynamic oligopoly models combine game theory and dynamic programming: firms choose actions strategically while anticipating competitors' strategies, and the state space grows combinatorially in the number of firms.
8.1.1 Asker, Fershtman, Jeon, and Pakes (2020): Q-Learning in Dynamic Procurement Auctions
Asker et al. ( 2020) develop a computational framework for analyzing dynamic procurement auctions with serially correlated asymmetric information. Their approach builds on the Experience-Based Equilibrium (EBE) concept of Fershtman and Pakes ( 2012) , which computes equilibria by simulating industry trajectories and updating strategies toward best responses. EBE evaluates values only on recurrently visited states rather than the full state space, making it feasible for large state spaces. While Fershtman and Pakes ( 2012) use a stochastic approximation algorithm to update continuation values from simulated industry trajectories, Asker et al. ( 2020) add explicit value-function updates via stochastic approximation.
The model is a repeated first-price sealed-bid auction with two firms. Each firm i i maintains a private inventory state ω i , t \omega_{i,t} (stock of unharvested timber, in their application). The state evolves endogenously, as winning an auction increases inventory while harvesting depletes it. Each firm's private state is not observed by its competitor except at periodic revelation events.
The key computational innovation is the use of Q-learning to compute equilibrium strategies. Each firm i i maintains a Q-function Q i : 𝒮 i × 𝒜 i → ℝ Q_{i}:\mathcal{S}{i}\times\mathcal{A}{i}\to\mathbb{R} , where 𝒮 i \mathcal{S}{i} encodes firm i i 's information set (its own inventory, beliefs about the competitor's inventory, public history) and 𝒜 i \mathcal{A}{i} is its action set (participation decision and bid level). The Q-function satisfies
Q i ( s , a ) = 𝔼 [ r i ( s , a , a − i ) + γ max a ′ ∈ 𝒜 i Q i ( s ′ , a ′ ) | s , a ] , Q_{i}(s,a)=\mathbb{E}\left[r_{i}(s,a,a_{-i})+\gamma\max_{a^{\prime}\in\mathcal{A}{i}}Q{i}(s^{\prime},a^{\prime});\middle|;s,a\right],
(76)
where r i  ( s , a , a − i ) r_{i}(s,a,a_{-i}) is firm i i 's per-period profit given the state, its own action a a , and the competitor's action a − i a_{-i} , and the expectation is taken over the competitor's strategy and the stochastic transitions.
Firms update Q-values using sample averaging.
Q i  ( s , a ) ← Q i  ( s , a ) + 1 h k  ( s , a )  [ r i + γ  max a ′ ∈ 𝒜 i  Q i  ( s ′ , a ′ ) − Q i  ( s , a ) ] , Q_{i}(s,a)\leftarrow Q_{i}(s,a)+\frac{1}{h_{k}(s,a)}\left[r_{i}+\gamma\max_{a^{\prime}\in\mathcal{A}{i}}Q{i}(s^{\prime},a^{\prime})-Q_{i}(s,a)\right],
(77)
where h k  ( s , a ) h_{k}(s,a) is the number of times state-action pair ( s , a ) (s,a) has been visited. 147 147 147 This sample-averaging rule ( α k = 1 / h k \alpha_{k}=1/h_{k} ) is equivalent to maintaining the running mean of observed returns, as distinct from fixed- α \alpha Q-learning which gives exponentially decaying weight to older observations. The update is applied for all actions, including counterfactual actions not taken, using the observed state transition. The equilibrium computation proceeds iteratively, with firms simultaneously updating their Q-functions based on simulated play against each other's current strategies. Strategies are derived from Q-values using an ε \varepsilon -greedy rule or Boltzmann exploration. 148 148 148 ε \varepsilon -greedy selects the greedy action 𝑎𝑟𝑔𝑚𝑎𝑥 a Q  ( s , a ) \mathop{\it argmax}_{a}Q(s,a) with probability 1 − ε 1-\varepsilon and a uniformly random action otherwise. Boltzmann exploration selects action a a with probability ∝ exp  ( Q  ( s , a ) / τ ) \propto\exp(Q(s,a)/\tau) where τ > 0 \tau>0 is a temperature parameter.
Asker et al. ( 2020) add a boundary consistency condition to the EBE concept that restricts behavior at the boundary of the recurrent state class, reducing the multiplicity of equilibria. Their numerical analysis reveals that information sharing between firms can, through increased precision of beliefs about competitor states, induce firms to spend more time in states where competition is less intense. The dynamic RL-computed equilibrium yields qualitatively different predictions from both static analysis and myopic ( γ = 0 \gamma=0 ) benchmarks. With dynamics, information sharing decreases average bids and increases average profits, while the myopic benchmark shows negligible effects.
The limitation of this approach is the tabular representation; the Q-function is stored as a lookup table over discretized states and actions, restricting applicability to models with moderate state-space dimension.
8.1.2 Hollenbeck (2019): TD Learning for Merger Analysis with Innovation
Hollenbeck ( 2019) uses RL to solve a dynamic oligopoly model with endogenous mergers, entry, exit, and quality investment. The model extends the Ericson-Pakes framework to study how horizontal mergers affect innovation incentives.
The industry state is Ω = ( ω 1 , … , ω n ) \Omega=(\omega_{1},\ldots,\omega_{n}) where ω i ∈ { 1 , … , ω max } \omega_{i}\in{1,\ldots,\omega_{\max}} is firm i i 's product quality. Firms produce differentiated goods and compete in prices (Bertrand competition with logit demand). In each period, firms simultaneously choose investment levels, entry/exit decisions, and potentially initiate merger negotiations.
Each firm i i computes its continuation value V i  ( Ω ) V_{i}(\Omega) from the industry state. Because the state space is the product of all firms' quality levels plus industry structure (number of active firms, recent mergers), exact dynamic programming is infeasible for industries with more than two or three firms. Hollenbeck ( 2019) instead uses temporal-difference learning to estimate values from simulated industry trajectories.
The value function update for firm i i is 149 149 149 This stochastic approximation update, introduced by Pakes and McGuire ( 1994) for dynamic oligopoly computation, is closely related to temporal-difference learning in the RL literature. The original algorithm uses visit-count averaging ( α k = 1 / k \alpha_{k}=1/k where k k counts visits to each state) rather than a fixed learning rate.
V i  ( Ω ) ← V i  ( Ω ) + α  [ Π i  ( Ω , 𝐚 ) + γ  V i  ( Ω ′ ) − V i  ( Ω ) ] , V_{i}(\Omega)\leftarrow V_{i}(\Omega)+\alpha\left[\Pi_{i}(\Omega,\mathbf{a})+\gamma V_{i}(\Omega^{\prime})-V_{i}(\Omega)\right],
(78)
where Π i  ( Ω , 𝐚 ) \Pi_{i}(\Omega,\mathbf{a}) denotes firm i i 's per-period profit given industry state Ω \Omega and the joint action profile 𝐚 \mathbf{a} (investment, entry/exit, merger decisions), 150 150 150 I use Π i \Pi_{i} for firm i i 's per-period profit to avoid confusion with policy π \pi . γ \gamma is the discount factor, and Ω ′ \Omega^{\prime} is the realized next-period state. The algorithm uses ε \varepsilon -decreasing exploration to prevent convergence to locally suboptimal equilibria.
The equilibrium computation follows the Pakes-McGuire iterative scheme. 151 151 151 The Pakes-McGuire algorithm (Pakes and McGuire, 1994) computes Markov perfect equilibria by iterating: (1) given current value functions, compute best-response strategies; (2) given strategies, update value functions via simulation. Convergence is not guaranteed but works well in practice. The algorithm simulates long industry histories, updates each firm's value function via ( 78), re-derives best-response strategies from updated values, and repeats.
The central finding is that horizontal mergers, while reducing static consumer surplus in the short run, create a strong incentive for entry and investment. Firms enter with negative static profits because the prospect of a lucrative buyout justifies the initial investment. The result is substantially higher long-run innovation and consumer welfare with mergers than without. This finding reverses the standard static antitrust prediction and can only emerge in a dynamic model where firms are forward-looking.
Two related papers merit brief mention. Lomys and Magnolfi ( 2024) develop structural estimation methods for strategic settings where agents use learning algorithms (specifically regret-minimizing rules) rather than playing a fixed equilibrium. They impose an “asymptotic no-regret” condition as a minimal rationality requirement and derive identification results for payoff parameters. Covarrubias ( 2022) uses deep RL to study oligopolistic pricing in a New Keynesian framework, representing firms' pricing policies as neural networks π ϕ  ( a | s ) \pi_{\phi}(a|s) . The method uncovers multiple equilibria ranging from competitive to collusive pricing. 152 152 152 The most prominent example of algorithmic collusion is Calvano et al. ( 2020) , who showed that independent Q-learning agents in a repeated Bertrand pricing game learn to sustain supra-competitive prices and punish deviators without explicit communication. This result and its implications for competition policy are treated in the companion thesis chapter (Rawat, 2026) .
8.2 Auction Equilibria and Mechanism Design
Closed-form equilibrium bidding strategies exist only for narrow families of valuation distributions and auction formats, and numerical methods scale poorly with the number of bidders and items.
8.2.1 Brero, Eden, Gerstgrasser, Parkes, and Rheingans-Yoo (2021): RL for Sequential Price Mechanisms
Brero et al. ( 2021) use RL to design optimal sequential price mechanisms (SPMs), a class of indirect auction mechanisms where agents are approached in sequence and offered menus of items at posted prices. SPMs generalize both serial dictatorship and posted-price mechanisms and essentially characterize all strongly obviously strategyproof (SOSP) mechanisms (Pycia and Troyan, 2023) . 153 153 153 A mechanism is strategyproof if truthful reporting is a dominant strategy. It is obviously strategyproof if this dominance is apparent even to boundedly rational agents; strongly obviously strategyproof (SOSP) adds that dominance holds at every information set (Pycia and Troyan, 2023) .
The mechanism design problem is formulated as a partially observable Markov decision process (POMDP). 154 154 154 In a POMDP, the agent cannot directly observe the full state. It maintains a belief distribution over possible states, updated via Bayes' rule as new observations arrive. This captures the mechanism designer's uncertainty about bidder valuations. The state at round t t includes the set of remaining items ρ t items ⊆ [ m ] \rho_{t}^{\text{items}}\subseteq[m] , remaining agents ρ t agents ⊆ [ n ] \rho_{t}^{\text{agents}}\subseteq[n] , the partial allocation 𝐱 t \mathbf{x}{t} , and the agents' (unobserved) valuation functions. The action a t = ( i t , { p j t } j ∈ ρ t − 1 items ) a{t}=(i_{t},{p_{j}^{t}}{j\in\rho{t-1}^{\text{items}}}) specifies which agent to visit next and what prices to offer. The observation is the agent's purchase decision, from which the mechanism can update beliefs about valuations. The reward is the objective function evaluated at the final allocation:
r = g  ( 𝐱 T , 𝝉 T ; 𝐯 ) , r=g(\mathbf{x}{T},\boldsymbol{\tau}{T};\mathbf{v}),
(79)
where g g can be social welfare ∑ i v i  ( x i ) \sum_{i}v_{i}(x_{i}) , revenue ∑ i τ i \sum_{i}\tau_{i} , or max-min fairness min i  v i  ( x i ) \min_{i}v_{i}(x_{i}) .
A key theoretical result establishes when adaptive mechanisms outperform static ones.
Theorem 4 ( Brero et al. ( 2021) , Propositions 1–4, informal).
Each feature of adaptive mechanisms is necessary for welfare optimality, even in simple settings. Personalized prices are needed with one item and two i.i.d. agents (Proposition 1); adaptive prices are needed with two identical items and three i.i.d. agents (Proposition 2); adaptive ordering is needed with six agents whose valuations are correlated (Proposition 3); both adaptive prices and ordering are needed with four agents whose valuations are independently but non-identically distributed (Proposition 4).
The policy maps from a sufficient statistic of the observation history to actions. Brero et al. ( 2021) show that this statistic can be represented compactly. The set of remaining items and agents suffices for independent valuations, while the full allocation matrix is needed for correlated valuations. They train the mechanism policy using Proximal Policy Optimization (PPO), 155 155 155 Proximal Policy Optimization (Schulman et al., 2017) is a policy gradient algorithm that constrains each update to a trust region, preventing large destabilizing policy changes. It is described in Chapter 2. which handles the discrete action space (agent selection) and continuous action space (price setting) of the POMDP.
Experimental results show that the learned SPMs achieve near-optimal welfare across settings with up to 20 agents and 5 items (with similar results noted for up to 30 of each), significantly outperforming static pricing benchmarks. The improvement is largest when agent valuations are correlated, since adaptive prices allow the mechanism to infer information about remaining agents from earlier purchases.
The limitation is that the POMDP formulation requires knowledge of the prior distribution over valuations, which in practice must be estimated from data. The method also does not scale easily to very large numbers of items due to the combinatorial action space.
8.2.2 Ravindranath, Feng, Wang, Zaheer, Mehta, and Parkes (2024): Fitted Policy Iteration for Combinatorial Auctions
Ravindranath et al. ( 2024) address revenue-maximizing mechanism design for combinatorial auctions with multiple items and strategic bidders. Their innovation is integrating differentiable auction structure into a fitted policy iteration framework, enabling analytical gradient computation where standard RL methods struggle with high variance.
The mechanism visits agents one at a time in sequence. Each agent i i , upon being visited, selects a bundle of items from those still available, given posted prices. Valuations are drawn once from distributions V i V_{i} and remain fixed throughout the mechanism. Complementarities arise from the structure of the valuation function over bundles, not from dynamic evolution. The MDP state at step t t is s t = ( i t , S t ) s_{t}=(i_{t},S_{t}) , where i t i_{t} is the current bidder and S t S_{t} is the set of remaining items.
The mechanism's policy maps from state to a price vector over available items. The key technical contribution is making the auction clearing differentiable. In a standard auction, the allocation is an argmax over bids (non-differentiable), and payments depend discontinuously on the allocation. Ravindranath et al. ( 2024) replace the hard bundle selection with a softmax relaxation, 156 156 156 The softmax relaxation replaces the hard allocation 𝑎𝑟𝑔𝑚𝑎𝑥 i b i \mathop{\it argmax}{i}b{i} with a soft allocation exp  ( b i / τ ) / ∑ j exp  ( b j / τ ) \exp(b_{i}/\tau)/\sum_{j}\exp(b_{j}/\tau) , which is differentiable and approaches the hard allocation as τ → 0 \tau\to 0 . enabling analytical gradient computation through the mechanism. The actor loss is the negative expected revenue, and gradients flow directly through the softmax-relaxed allocation and payment rules. The paper explicitly avoids REINFORCE-style estimators, noting that analytical gradients overcome the sample inefficiency and high variance of score-function methods.
The method follows fitted policy iteration (Bertsekas and Tsitsiklis, 1996) , alternating between evaluating the current policy (computing expected revenue) and improving it via gradient ascent on the actor loss. This differs from model-free RL approaches (PPO, SAC) that the paper uses as baselines.
Experiments on settings with additive and combinatorial valuations show that the learned mechanisms achieve up to 13% higher revenue than item-wise Myerson optimal auctions, with the largest gains in combinatorial settings where bundle complementarities make item-wise pricing suboptimal. Standard RL baselines (PPO, SAC) are also outperformed, confirming the advantage of exploiting differentiable structure. 157 157 157 DDPG was also tested but found to be unstable. DQN is not applicable to continuous price-setting.
8.3 Macroeconomic Models
Reinforcement learning and deep learning are increasingly used to solve high-dimensional macroeconomic models where grid-based dynamic programming is infeasible. Heterogeneous agent models, in which a distribution of agents with different wealth levels, productivities, or beliefs interact through markets, generate state spaces that grow with the number of agent types and asset positions. Maliar et al. ( 2021) demonstrate that deep neural networks can approximate policy and value functions in dynamic economic models, achieving accuracy comparable to established projection methods while scaling to problems with dozens of state variables. Fernández-Villaverde et al. ( 2023) solve a model with financial frictions and an endogenous wealth distribution using deep learning, obtaining global solutions to a problem where perturbation methods fail due to strong nonlinearities. Fernández-Villaverde et al. ( 2024) provide a systematic treatment of deep learning methods for high-dimensional dynamic programming problems in economics, covering both single-agent and equilibrium settings. Atashbar and Shi ( 2023) apply deep deterministic policy gradient (DDPG) 158 158 158 DDPG extends Q-learning to continuous action spaces by learning a deterministic policy network alongside a Q-function critic. to a real business cycle model, demonstrating that model-free RL can recover near-optimal consumption and investment policies without deriving optimality conditions such as the Euler equation. Moll ( 2025) argues that rational expectations equilibria in heterogeneous agent models are computationally intractable and proposes reinforcement learning as a more tractable alternative for modeling how agents form beliefs and make decisions; see also the textbook treatment in Zhao ( 2025) . This is a rapidly growing area; readers seeking a comprehensive methodological treatment are directed to the cited papers and the references therein.
8.4 Optimal Policy Design
Zheng et al. ( 2022) introduce the AI Economist, a two-level multi-agent reinforcement learning framework for automated tax policy design. In their environment, a population of AI worker agents learn to work, trade, and build in a spatial-economic simulation, while a government RL agent simultaneously learns tax brackets that optimize a social welfare objective. The worker agents are trained with PPO to maximize individual post-tax utility, and the government agent is trained with PPO to maximize a weighted combination of equality (measured by the Gini index) and productivity (total output). The two-level structure produces a Stackelberg game between the government (leader) and the workers (followers), where the government must anticipate how tax policy changes affect worker behavior. The learned tax policies achieve equality-productivity tradeoffs that Pareto-dominate several analytical baselines, including the Saez tax formula. This framework extends the mechanism design perspective of the preceding subsection from auctions to fiscal policy, using multi-agent RL to jointly solve for optimal mechanisms and equilibrium responses.
8.5 Simulation Study: DDC Estimation at Scale
The test bed is a multi-component extension of the Rust ( 1987) bus engine replacement model. In the original formulation a maintenance superintendent observes discretized mileage m ∈ { 0 , … , M − 1 } m\in{0,\ldots,M{-}1} and makes a binary keep-or-replace decision, facing running cost c  ( s ; θ ) = θ 1  x + θ 2  x 2 c(s;\theta)=\theta_{1}x+\theta_{2}x^{2} with x = m / M x=m/M , replacement cost R  C RC , and Type I extreme value additive errors that yield logit conditional choice probabilities. We extend the model to K K independent wear components, each evolving in { 0 , … , M − 1 } {0,\ldots,M{-}1} , with aggregate normalized wear x  ( s ) = ∑ k m k / M x(s)=\sum_{k}m_{k}/M entering the same cost function. The state space is | 𝒮 | = M K |\mathcal{S}|=M^{K} , so increasing K K produces a controlled scaling experiment in which the data-generating process is identical across scales but the computational burden grows exponentially.
We compare four estimation methods on a multi-component bus engine replacement problem (Rust, 1987) with K ∈ { 1 , 2 , 3 , 4 } K\in{1,2,3,4} independent wear components, producing state spaces from 20 to 160,000 states. Panel data consist of N = 500 N=500 agents observed for T = 100 T=100 periods. The four methods are NFXP (nested fixed-point MLE), CCP (Hotz-Miller inversion), TD-CCP Linear (semi-gradient TD with polynomial basis), and TD-CCP Neural (approximate value iteration with a two-layer MLP), where the two TD-CCP variants follow Adusumilli et al. ( 2022) . Each configuration is replicated across 5 seeds; Table 15 and Figure 15 report means.
Table 15: DDC estimation results across state-space scales. Rows show method, number of components K K , state-space size | 𝒮 | |\mathcal{S}| , mean wall-clock time (seconds), RC bias, and root mean squared error for each structural parameter. Averages over 5 seeds; dashes indicate method failure (sparse state coverage).
Figure 15: Wall-clock estimation time versus state-space scale for the four DDC estimators. Vertical axis is log-scaled. Each point is the mean over 5 seeds.
NFXP scales from 0.2s at K = 1 K{=}1 ( | 𝒮 | = 20 |\mathcal{S}|{=}20 ) to 179s at K = 4 K{=}4 ( | 𝒮 | = 160 , 000 |\mathcal{S}|{=}160{,}000 ), reflecting the cost of repeated value iteration inside each likelihood evaluation. CCP becomes infeasible beyond K = 2 K{=}2 due to sparse state coverage in the panel data. TD-CCP Neural maintains near-constant runtime ( ∼ 28 {\sim}28 – 44 44 s) across all K K levels with competitive accuracy (RC RMSE 0.077 at K = 4 K{=}4 ), validating the AVI approach of Adusumilli et al. ( 2022) . TD-CCP Linear runs in under 0.3s at all scales but suffers from basis misspecification at higher K K (RC RMSE 0.337 at K = 4 K{=}4 ); see Table 15 and Figure 15.
9 Reinforcement Learning in Games
With multiple agents adapting simultaneously, each agent's environment includes the others' changing policies, so the stationary-transition assumption behind single-agent convergence results fails. Shoham et al. ( 2007) enumerate five desiderata for multi-agent learning: (1) convergence to a stationary strategy in self-play; (2) rationality (best-responding against stationary opponents); (3) equilibrium attainment; (4) safety (guaranteeing at least the Nash-value payoff); (5) social welfare. No existing algorithm satisfies all five in general games.
Two paradigms emerged. Value-based methods generalize the Bellman operator to games, replacing the max \max with game-theoretic solution concepts (minimax, Nash), targeting stochastic games with simultaneous moves and observable payoffs. Regret-based methods (CFR) accumulate counterfactual regrets and let the time-averaged strategy converge, targeting extensive-form games with sequential moves and private information. Computing Nash equilibria is PPAD-complete (Daskalakis et al., 2009) , so neither approach escapes the fundamental hardness, but both achieve convergence in the game classes they target.
9.1 Stochastic Games and Equilibrium Learning
9.1.1 The Stochastic Game Framework
An n n -player stochastic game Γ = ( n , 𝒮 , 𝒜 1 , … , 𝒜 n , P , r 1 , … , r n , γ ) \Gamma=(n,\mathcal{S},\mathcal{A}{1},\ldots,\mathcal{A}{n},P,r_{1},\ldots,r_{n},\gamma) consists of a finite state space 𝒮 \mathcal{S} ; finite action sets 𝒜 i \mathcal{A}{i} for each player i i ; a transition function P : 𝒮 × 𝒜 1 × ⋯ × 𝒜 n → Δ  ( 𝒮 ) P:\mathcal{S}\times\mathcal{A}{1}\times\cdots\times\mathcal{A}{n}\to\Delta(\mathcal{S}) ; reward functions r i : 𝒮 × 𝒜 1 × ⋯ × 𝒜 n → ℝ r{i}:\mathcal{S}\times\mathcal{A}{1}\times\cdots\times\mathcal{A}{n}\to\mathbb{R} ; and a common discount factor γ ∈ [ 0 , 1 ) \gamma\in[0,1) . At each stage, all players simultaneously choose actions, receive individual rewards, and the game transitions to a new state. 159 159 159 Shapley ( 1953) introduced stochastic games in 1953 for the two-player zero-sum case, proving existence of the value via a contraction argument on the Bellman operator. The general-sum extension to n n players is due to Fink (1964) and Takahashi (1964).
A Markov decision process is a stochastic game with n = 1 n=1 ; a matrix game is a stochastic game with | 𝒮 | = 1 |\mathcal{S}|=1 . Each player i i seeks a policy π i : 𝒮 → Δ  ( 𝒜 i ) \pi_{i}:\mathcal{S}\to\Delta(\mathcal{A}{i}) maximizing discounted return 𝔼  [ ∑ t = 0 ∞ γ t  r i  ( s t , a 1 , t , … , a n , t ) ] \mathbb{E}[\sum{t=0}^{\infty}\gamma^{t}r_{i}(s_{t},a_{1,t},\ldots,a_{n,t})] .
Standard Q-learning convergence (Watkins and Dayan, 1992) requires stationary transition and reward dynamics; with multiple learners, this assumption fails. Bowling and Veloso ( 2002) formalized two properties a learning algorithm should satisfy. It is rational if, when all other players converge to stationary policies, it converges to a best response; it is convergent if, in self-play, it converges to a stationary policy.
If all players use rational, convergent algorithms, the resulting profile is a Nash equilibrium by construction. The challenge is achieving both properties simultaneously.
9.1.2 Minimax-Q Learning
Littman ( 1994) proposed the first Q-learning algorithm for stochastic games, targeting two-player zero-sum games. The key modification replaces the max \max operator in the standard Q-learning backup with a minimax operator. Each agent maintains Q i  ( s , a i , a − i ) Q_{i}(s,a_{i},a_{-i}) over the joint action space. The update rule is
Q i  ( s , a i , a − i ) ← ( 1 − α )  Q i  ( s , a i , a − i ) + α  [ r i + γ  V i  ( s ′ ) ] , Q_{i}(s,a_{i},a_{-i})\leftarrow(1-\alpha),Q_{i}(s,a_{i},a_{-i})+\alpha\left[r_{i}+\gamma,V_{i}(s^{\prime})\right],
(80)
where the value backup solves a linear program:
V i  ( s ) = max π i ∈ Δ  ( 𝒜 i )  min a − i ∈ 𝒜 − i  ∑ a i ∈ 𝒜 i π i  ( a i )  Q i  ( s , a i , a − i ) . V_{i}(s)=\max_{\pi_{i}\in\Delta(\mathcal{A}{i})}\min{a_{-i}\in\mathcal{A}{-i}}\sum{a_{i}\in\mathcal{A}{i}}\pi{i}(a_{i}),Q_{i}(s,a_{i},a_{-i}).
(81)
This is the RL analogue of Shapley's value iteration for zero-sum stochastic games (Shapley, 1964) . The resulting policy π i  ( s ) \pi_{i}(s) is generally a mixed strategy, since deterministic policies are exploitable in adversarial settings.
Minimax-Q converges to the minimax Q-values under Robbins-Monro learning rates ( ∑ t α t = ∞ \sum_{t}\alpha_{t}=\infty , ∑ t α t 2 < ∞ \sum_{t}\alpha_{t}^{2}<\infty ) and infinite exploration of all state-action tuples. 160 160 160 The convergence proof extends the contraction argument for standard Q-learning. Because the zero-sum minimax operator is a contraction with modulus γ \gamma under the ℓ ∞ \ell^{\infty} norm, the stochastic approximation converges to the fixed point. See Littman ( 1994) and the general treatment in Szepesvári and Littman (1999). However, the algorithm sacrifices rationality: it plays the equilibrium strategy even against exploitable opponents. 161 161 161 In the soccer game of Littman ( 1994) , minimax-Q won 53.7% against a hand-built opponent versus 26.1% for Q-learning. Against an adversarial challenger, Q-learning won 0% (its deterministic policy was fully predictable); minimax-Q won 37.5% through mixed strategies.
9.1.3 Nash-Q Learning
Hu and Wellman ( 2003) extended the framework to general-sum stochastic games, where players may have aligned, opposed, or mixed incentives. Each agent i i maintains a Q-function over the joint action space Q i  ( s , a 1 , … , a n ) Q_{i}(s,a_{1},\ldots,a_{n}) and updates via
Q i  ( s , 𝐚 ) ← ( 1 − α )  Q i  ( s , 𝐚 ) + α  [ r i + γ  Nash i  ( Q 1  ( s ′ ) , … , Q n  ( s ′ ) ) ] , Q_{i}(s,\mathbf{a})\leftarrow(1-\alpha),Q_{i}(s,\mathbf{a})+\alpha\left[r_{i}+\gamma,\text{Nash}{i}\bigl(Q{1}(s^{\prime}),\ldots,Q_{n}(s^{\prime})\bigr)\right],
(82)
where Nash i  ( ⋅ ) \text{Nash}{i}(\cdot) denotes player i i 's payoff under a Nash equilibrium of the stage game defined by the current Q-values ( Q 1  ( s ′ ) , … , Q n  ( s ′ ) ) (Q{1}(s^{\prime}),\ldots,Q_{n}(s^{\prime})) . At each backup, the algorithm treats the Q-values as payoff matrices, computes a Nash equilibrium of this matrix game, and uses the equilibrium payoffs for the value estimate.
Theorem 5 ( Hu and Wellman ( 2003) ).
Nash-Q converges to Nash Q-values under Robbins-Monro learning rates and infinite exploration, provided every stage game encountered during learning has either (a) a global optimal point (all agents receive their highest payoff at the same joint action) or (b) a unique saddle-point Nash equilibrium.
These conditions are restrictive. When stage games have multiple Nash equilibria, agents may select different equilibria for their backups, causing divergence. 162 162 162 In the experiments of Hu and Wellman ( 2003) , a grid game with a unique equilibrium Q-function converged in 100% of trials under Nash-Q versus 20% under independent Q-learning; a game with three equilibrium Q-functions converged in only 68–90% of trials. Nash-Q requires each agent to observe all other agents' rewards and to maintain Q-values over the joint action space 𝒜 1 × ⋯ × 𝒜 n \mathcal{A}{1}\times\cdots\times\mathcal{A}{n} , with storage O  ( n  | 𝒮 |  ∏ i | 𝒜 i | ) O(n|\mathcal{S}|\prod_{i}|\mathcal{A}_{i}|) , exponential in the number of players. Nash-Q reduces to standard Q-learning in the single-agent case.
9.1.4 The Convergence Problem
Table 16 summarizes the trade-offs. No single algorithm achieves both rationality and convergence in general games.
Table 16: Multi-agent Q-learning algorithms: convergence and information requirements
WoLF-PHC (Win or Learn Fast, Policy Hill-Climbing) of Bowling and Veloso ( 2002) maintains a policy π i  ( a | s ) \pi_{i}(a|s) and a running average policy π ¯ i  ( a | s ) \bar{\pi}_{i}(a|s) , updating Q-values as in standard Q-learning. The policy moves toward the greedy action at a variable rate:
δ = { δ l if  ∑ a π i  ( a | s )  Q i  ( s , a ) < ∑ a π ¯ i  ( a | s )  Q i  ( s , a ) (losing) δ w otherwise (winning) \delta=\begin{cases}\delta_{l}&\text{if }\sum_{a}\pi_{i}(a|s),Q_{i}(s,a)<\sum_{a}\bar{\pi}{i}(a|s),Q{i}(s,a)\quad\text{(losing)}\ \delta_{w}&\text{otherwise}\quad\text{(winning)}\end{cases}
(83)
with δ l > δ w \delta_{l}>\delta_{w} . When the current policy underperforms the historical average (losing), the agent adapts quickly; when outperforming (winning), it adapts slowly to avoid destabilizing the opponent. Bowling and Veloso ( 2002) proved that WoLF-IGA (the infinitesimal gradient ascent variant) converges to Nash equilibrium in all two-player, two-action games. The trajectory traces piecewise ellipses around the equilibrium, shrinking by a factor of ℓ 4 < 1 \ell^{4}<1 per orbit, where ℓ = δ w / δ l \ell=\sqrt{\delta_{w}/\delta_{l}} . WoLF-PHC requires only own-reward observations, the same information as independent Q-learning.
Two further algorithms deserve mention. Friend-or-Foe Q-learning (Littman, 2001) decomposes agents as cooperative (friend) or adversarial (foe), using max \max for friends and minimax for foes; it always converges but requires knowing the relationship type a priori. 163 163 163 Correlated-Q learning (Greenwald and Hall, 2003) generalizes both Nash-Q and Minimax-Q by using correlated equilibrium, a probability distribution over joint actions enforced by a correlating device. The set of correlated equilibria contains all Nash equilibria. Correlated-Q converges under conditions analogous to Nash-Q. The evolutionary perspective of Börgers and Sarin ( 1997) provides a deeper lens: reinforcement learning dynamics in matrix games converge to the replicator equation from evolutionary game theory. The cycling of Q-learning in games such as matching pennies is structurally identical to the cycling of replicator dynamics in Rock-Paper-Scissors games.
9.1.5 Simulation Study: Cournot and Bertrand Duopoly
Two canonical games from industrial organization serve as benchmarks. In Cournot duopoly, two firms choose quantities q i ∈ { 0 , 1 , … , 9 } q_{i}\in{0,1,\ldots,9} with inverse demand P  ( Q ) = 10 − Q P(Q)=10-Q and marginal cost c = 1 c=1 ; the unique Nash equilibrium is q ∗ = 3 q^{}=3 with profit π ∗ = 9 \pi^{}=9 . In Bertrand duopoly with differentiated products, two firms choose prices p i ∈ { 0 , 1 , … , 9 } p_{i}\in{0,1,\ldots,9} with demand d i = 10 − 2  p i + p j d_{i}=10-2p_{i}+p_{j} and marginal cost c = 1 c=1 ; the continuous Nash equilibrium is p ∗ ≈ 4.33 p^{}\approx 4.33 , which discretizes to p ∗ = 4 p^{}=4 with profit π ∗ = 18 \pi^{*}=18 . Both games have unique Nash equilibria in pure strategies. 164 164 164 Each configuration runs for 50,000 iterations across 20 seeds. Three algorithms compete: independent Q-learning (IQL), Nash-Q, and WoLF-PHC.
Table 17: Convergence to Nash equilibrium in Cournot and Bertrand duopoly
Notes: Action and Profit report mean ± \pm standard error across 20 seeds over the final 5,000 iterations. | a − a ∗ | |a-a^{*}| is the mean distance from Nash. Conv. iter is the first iteration where the smoothed average action enters a 0.5 0.5 -neighborhood of Nash.
Table 17 and Figure 16 report the results. All three algorithms converge to Nash in both games within the first 5,000 iterations. IQL, which lacks any game-theoretic computation, matches the game-aware methods in these well-structured games with unique pure-strategy equilibria. The advantage of Nash-Q and WoLF-PHC emerges in games requiring mixed strategies, where IQL's deterministic policy limit prevents convergence. 
Figure 16: Convergence of expected actions to Nash equilibrium. Left: Cournot duopoly. Right: Bertrand duopoly. Smoothed over 1,000-iteration windows, averaged across 20 seeds.
9.2 Counterfactual Regret Minimization
Extensive-form games require a different approach. CFR bypasses equilibrium selection: instead of computing Nash equilibria at each step, it minimizes cumulative regret and lets the time-averaged strategy converge to equilibrium.
An extensive-form game consists of a game tree with information sets ℐ i \mathcal{I}{i} partitioning player i i 's decision nodes. An information set groups nodes where the player cannot distinguish between them due to hidden opponent actions or private information. A behavioral strategy σ i : ℐ i → Δ  ( 𝒜 ) \sigma{i}:\mathcal{I}_{i}\to\Delta(\mathcal{A}) assigns action probabilities at each information set.
The counterfactual value of action a a at information set I I is
v i σ  ( I , a ) = ∑ h ∈ I π − i σ  ( h )  ∑ z ⊒ h  a π σ  ( h  a , z )  u i  ( z ) v^{\sigma}{i}(I,a)=\sum{h\in I}\pi^{\sigma}{-i}(h)\sum{z\sqsupseteq ha}\pi^{\sigma}(ha,z)u_{i}(z)
(84)
where π − i σ  ( h ) \pi^{\sigma}{-i}(h) is the probability opponents reach h h , and π σ  ( h  a , z ) \pi^{\sigma}(ha,z) is the probability of reaching terminal z z from h  a ha . The counterfactual formulation weights by opponent reach π − i σ  ( h ) \pi^{\sigma}{-i}(h) rather than joint reach π σ  ( h ) \pi^{\sigma}(h) , ensuring non-zero updates even at rarely-visited information sets. Cumulative regret for action a a is R T  ( I , a ) = ∑ t = 1 T [ v σ t  ( I , a ) − v σ t  ( I ) ] R^{T}(I,a)=\sum_{t=1}^{T}[v^{\sigma^{t}}(I,a)-v^{\sigma^{t}}(I)] . CFR updates via regret matching: 165 165 165 Regret matching is an action selection rule where the probability of choosing action a a is proportional to the cumulative regret for not having chosen a a in the past (truncated at zero). Actions with high regret receive higher probability; actions with negative regret (having performed worse than average) receive zero probability.
σ T + 1  ( I , a ) = [ R T  ( I , a ) ] + ∑ a ′ [ R T  ( I , a ′ ) ] + , [ x ] + = max  ( x , 0 ) . \sigma^{T+1}(I,a)=\frac{[R^{T}(I,a)]^{+}}{\sum_{a^{\prime}}[R^{T}(I,a^{\prime})]^{+}},\quad[x]^{+}=\max(x,0).
(85)
The average strategy σ ¯ T \bar{\sigma}^{T} converges to ε \varepsilon -Nash with ε = O  ( | ℐ |  | 𝒜 |  Δ / T ) \varepsilon=O(|\mathcal{I}|\sqrt{|\mathcal{A}|}\Delta/\sqrt{T}) , where Δ \Delta is the range of payoffs (Zinkevich et al., 2008) . 166 166 166 An ε \varepsilon -Nash equilibrium is a strategy profile where no player can improve her expected payoff by more than ε \varepsilon through unilateral deviation. As ε → 0 \varepsilon\to 0 , this converges to an exact Nash equilibrium.
CFR+ (Tammelin, 2014) replaces standard regret matching with Regret Matching+, which truncates cumulative regrets to zero after each update rather than only at action selection. The update becomes R T + 1  ( I , a ) = max  ( R T  ( I , a ) + r T + 1  ( I , a ) , 0 ) R^{T+1}(I,a)=\max(R^{T}(I,a)+r^{T+1}(I,a),,0) , where r T + 1  ( I , a ) = v σ T + 1  ( I , a ) − v σ T + 1  ( I ) r^{T+1}(I,a)=v^{\sigma^{T+1}}(I,a)-v^{\sigma^{T+1}}(I) is the instantaneous counterfactual regret. CFR+ also weights iteration t t by t t when computing the average strategy. While vanilla CFR converges at O  ( 1 / T ) O(1/\sqrt{T}) , CFR+ empirically converges at O  ( 1 / T ) O(1/T) . 167 167 167 The O  ( 1 / T ) O(1/T) rate for CFR+ is empirically observed but not yet proven in full generality. Tammelin ( 2014) conjectured this rate based on extensive experiments across poker variants. CFR+ enabled Bowling et al. ( 2015) to essentially solve heads-up limit Texas hold'em, a game with 3.16 × 10 17 3.16\times 10^{17} states, the first non-trivial imperfect-information game played competitively by humans to be essentially solved. Their program Cepheus achieved exploitability below 1 mbb/g (milli-big-blind per game).
9.3 Neural Extensions
Tabular CFR stores regrets at every information set, infeasible when | ℐ | > 10 14 |\mathcal{I}|>10^{14} . Two neural approaches scale to large games.
9.3.1 Deep CFR
Brown et al. ( 2019) approximate cumulative regrets with a neural network V θ : ℐ × 𝒜 → ℝ V_{\theta}:\mathcal{I}\times\mathcal{A}\to\mathbb{R} trained on sampled (information set, iteration, regret) tuples:
L V  ( θ ) = 𝔼 ( I , t ′ , r ) ∼ ℳ  [ t ′ ⋅ ( V θ  ( I , a ) − r ) 2 ] . L_{V}(\theta)=\mathbb{E}{(I,t^{\prime},r)\sim\mathcal{M}}\left[t^{\prime}\cdot(V{\theta}(I,a)-r)^{2}\right].
(86)
Weighting by iteration index t ′ t^{\prime} gives more recent regret estimates higher importance. A separate network Π ϕ \Pi_{\phi} approximates the average strategy, trained via weighted MSE on strategy samples with the same iteration weighting. The current strategy derives from regret matching, with σ  ( I , a ) ∝ [ V θ  ( I , a ) ] + \sigma(I,a)\propto[V_{\theta}(I,a)]^{+} .
9.3.2 Neural Fictitious Self-Play
NFSP (Heinrich and Silver, 2016) combines fictitious play 168 168 168 Fictitious play (Brown, 1951) is a classical learning rule where each player best-responds to the empirical distribution of opponents' past actions. Under certain conditions (e.g., two-player zero-sum games), the time-average strategies converge to Nash equilibrium. (Brown, 1951) with deep Q-learning. 169 169 169 Deep Q-Network (DQN) (Mnih et al., 2015) approximates the Q-function with a neural network, using experience replay and a target network to stabilize training. The target network θ − \theta^{-} in the loss function is a delayed copy of the main network, updated periodically. Each player maintains two networks: a best-response network Q θ Q_{\theta} trained via DQN, and an average strategy network π ¯ ϕ \bar{\pi}_{\phi} trained via supervised learning on the best-response actions:
L RL  ( θ ) = 𝔼  [ ( r + γ  max a ′  Q θ −  ( I ′ , a ′ ) − Q θ  ( I , a ) ) 2 ] , L SL  ( ϕ ) = 𝔼  [ − log  π ¯ ϕ  ( a | I ) ] . L_{\text{RL}}(\theta)=\mathbb{E}\left[\left(r+\gamma\max_{a^{\prime}}Q_{\theta^{-}}(I^{\prime},a^{\prime})-Q_{\theta}(I,a)\right)^{2}\right],\quad L_{\text{SL}}(\phi)=\mathbb{E}\left[-\log\bar{\pi}_{\phi}(a|I)\right].
(87)
During play, agents follow π ¯ ϕ \bar{\pi}{\phi} with probability 1 − η 1-\eta and Q θ Q{\theta} with probability η \eta .
9.3.3 Poker Results
These methods achieved superhuman performance in poker. Deep CFR attained exploitability of 37 mbb/g 170 170 170 Exploitability measures how far a strategy is from Nash equilibrium, defined as the maximum expected gain an adversary could achieve by best-responding. Zero exploitability means the strategy is unexploitable (Nash). In poker, exploitability is measured in milli-big-blinds per game (mbb/g). in heads-up flop hold'em (Brown et al., 2019) . Libratus defeated top human professionals in heads-up no-limit hold'em using nested subgame solving with CFR (Brown and Sandholm, 2018) . Pluribus extended to six-player no-limit hold'em (Brown and Sandholm, 2019) . The game tree of heads-up no-limit hold'em contains ∼ 10 161 \sim 10^{161} states; these results demonstrate that CFR-based methods scale to economically relevant game sizes.
9.4 The Coase Conjecture
The durable goods monopoly is a canonical extensive-form bargaining problem with private information: the seller does not know the buyer's valuation.
Coase ( 1972) conjectured that a durable goods monopolist 171 171 171 A durable good provides utility over multiple periods (e.g., a car, appliance, or software license) rather than being consumed immediately. Unlike non-durable goods, durable goods create intertemporal competition, as the seller at time t t competes with her own future self at t + 1 t+1 . loses market power when buyers are patient. Unable to commit to future prices, the seller competes with her future self, eroding rents. As the inter-offer interval shrinks ( δ → 1 \delta\to 1 ), price collapses to marginal cost and all surplus is extracted by buyers. Gul et al. ( 1986) formalized this for the gap case, where the seller's cost is strictly below all buyer valuations, guaranteeing trade and a unique stationary equilibrium. 172 172 172 Stokey ( 1981) showed that a monopolist facing rational consumers cannot price discriminate intertemporally; Bulow ( 1982) proved that in the no-gap case, the monopolist prefers renting to selling. The no-gap case admits multiple equilibria with more complex dynamics.
9.4.1 Model
A seller with zero cost faces a buyer with private valuation v ∈ { v L , v H } v\in{v_{L},v_{H}} , where Pr  ( v = v H ) = π \Pr(v=v_{H})=\pi . In each period t = 1 , 2 , … t=1,2,\ldots , the seller posts price p t p_{t} ; the buyer accepts or rejects. Upon acceptance at t t , the seller receives δ t − 1  p t \delta^{t-1}p_{t} and the buyer receives δ t − 1  ( v − p t ) \delta^{t-1}(v-p_{t}) , where δ ∈ ( 0 , 1 ) \delta\in(0,1) is the common discount factor. The game ends upon acceptance or after T T periods. Parameters: v L = 100 v_{L}=100 , v H = 200 v_{H}=200 , T = 2 T=2 periods.
9.4.2 Equilibrium Analysis
The screening price P ∗  ( δ ) P^{*}(\delta) makes the high-type buyer indifferent between accepting now and waiting.
v H − P ∗ = δ  ( v H − v L ) ⟹ P ∗  ( δ ) = v H − δ  ( v H − v L ) . v_{H}-P^{}=\delta(v_{H}-v_{L})\implies P^{}(\delta)=v_{H}-\delta(v_{H}-v_{L}).
(88)
The seller's optimal strategy depends on π \pi . Let Π screen = π  P ∗ + ( 1 − π )  δ  v L \Pi_{\text{screen}}=\pi P^{*}+(1-\pi)\delta v_{L} and Π pool = v L \Pi_{\text{pool}}=v_{L} . The seller screens if Π screen > Π pool \Pi_{\text{screen}}>\Pi_{\text{pool}} , yielding threshold
π ∗ = v L  ( 1 − δ ) P ∗ − δ  v L = 1 2 when  v H = 2  v L . \pi^{}=\frac{v_{L}(1-\delta)}{P^{}-\delta v_{L}}=\frac{1}{2}\quad\text{when }v_{H}=2v_{L}.
(89)
For π < π ∗ \pi<\pi^{} , the seller pools (offers v L v_{L} immediately). For π > π ∗ \pi>\pi^{} , the seller screens (offers P ∗ P^{} , then v L v_{L} if rejected). 173 173 173 In a screening equilibrium, the seller uses price to separate buyer types: high-value buyers accept immediately at a high price, while low-value buyers reject and receive a lower offer. In a pooling equilibrium, the seller offers a single price that all types accept. The gap case ( 0 = c < v L 0=c<v_{L} ) guarantees trade in equilibrium. The Coase conjecture manifests as δ → 1 \delta\to 1 , where P ∗  ( δ ) → v L P^{}(\delta)\to v_{L} and the seller cannot extract surplus from high types.
9.4.3 Computational Results
I model the bargaining game as an extensive-form game and apply CFR. 174 174 174 The game tree has two information sets for the seller (indexed by rejection history) and two for the buyer (indexed by private type). CFR runs for 5,000 iterations per parameter configuration; NashConv (sum of exploitabilities) measures convergence.
Table 18: CFR Equilibrium vs. Theory: π \pi -sweep at δ = 0.5 \delta=0.5
Notes: P(Screen) is the probability the seller offers P ∗ = 150 P^{*}=150 in period 1. Theory column gives the predicted probability (0 for pooling, 1 for screening).
Table 18 reports results from varying π \pi at fixed δ = 0.5 \delta=0.5 . CFR recovers the sharp phase transition at π ∗ = 0.5 \pi^{}=0.5 : pooling below, screening above. A δ \delta -sweep at π = 0.7 \pi=0.7 confirms the screening price formula P ∗  ( δ ) = 200 − 100  δ P^{}(\delta)=200-100\delta with zero error across δ ∈ [ 0.1 , 0.9 ] \delta\in[0.1,0.9] ; at δ ≈ 0.75 \delta\approx 0.75 , the seller switches to pooling as patient buyers erode the screening premium, consistent with the Coase conjecture. 175 175 175 Four stress tests were conducted: (1) awkward primes ( v L , v H ) = ( 37 , 83 ) (v_{L},v_{H})=(37,83) , converging to P ∗ = 55 P^{*}=55 (theory: 55.4); (2) information leak with a single seller information set at the root; (3) grid shift with 150 removed, recovering 145 (99.4%); (4) 3-period game, finding P 1 = 120 P_{1}=120 versus theoretical 136. The 3-period result reflects a tie-breaking equilibrium: at P 1 = 136 P_{1}=136 the high buyer is exactly indifferent, so the seller prefers P 1 = 120 P_{1}=120 (revenue 108 versus 86.4 if rejected).
9.5 Discussion
Stochastic-game Q-learning and CFR target complementary game classes: simultaneous-move games with observable payoffs and extensive-form games with private information, respectively. The simulations confirm convergence to known equilibria in both settings without encoding economic structure into the algorithms.
10 Bandits and Dynamic Pricing
This chapter focuses on online reinforcement learning (Section 2), where, unlike the simulator-based training of preceding chapters, the agent learns directly from interactions with real customers and exploration is a real cost that must be balanced against exploitation. A seller faces T T customers in sequence, setting a price for each and observing only whether the customer bought. 176 176 176 Rothschild ( 1974) posed pricing under demand uncertainty as a two-armed bandit problem. His insight was that a myopic seller can get stuck at a suboptimal price forever, because exploiting the currently best-looking price generates no information about alternatives. The seller does not observe the customer's willingness to pay. Regret, the total revenue gap between the seller's policy and the best fixed price in hindsight, is the central measure: if the optimal fixed price earns r ∗ r^{} per customer, a policy with regret R  ( T ) R(T) earns T  r ∗ − R  ( T ) Tr^{}-R(T) in total. The central question is how fast R  ( T ) R(T) shrinks as the seller accumulates purchase data, and how structural assumptions about demand affect this rate.
10.1 Foundations
10.1.1 No Structure on Demand
Kleinberg and Leighton ( 2003) study the simplest version of the problem. Customers arrive with valuations drawn i.i.d. from an unknown distribution on [ 0 , 1 ] [0,1] , and the seller posts a price from a continuous set. The demand curve D  ( p ) = Pr  ( v ≥ p ) D(p)=\Pr(v\geq p) is unknown; the only feedback is whether each customer bought. The seller's goal is to minimize regret against the single price p ∗ p^{} that maximizes p ⋅ D  ( p ) p\cdot D(p) . Kleinberg and Leighton prove that the minimax regret is Θ  ( T ) \Theta(\sqrt{T}) . 177 177 177 The upper bound, O  ( T  log  T ) O(\sqrt{T\log T}) , discretizes [ 0 , 1 ] [0,1] into K = ⌈ ( T / log  T ) 1 / 4 ⌉ K=\lceil(T/\log T)^{1/4}\rceil prices and runs the UCB1 algorithm of Auer et al. ( 2002a) . The lower bound, Ω  ( T ) \Omega(\sqrt{T}) , constructs a family of demand curves parameterized by the location of the optimal price p ∗ ∈ [ 0.3 , 0.4 ] p^{}\in[0.3,0.4] . The key tension: posting prices far from p ∗ p^{} is informative about demand but costly in revenue; posting prices near p ∗ p^{} is cheap but uninformative. Resolving this tension costs at least Ω  ( T ) \Omega(\sqrt{T}) in cumulative revenue. UCB1 (Auer et al., 2002a) selects the price maximizing μ ^ p k  ( t ) + 2  ln  t / N p k  ( t ) \hat{\mu}{p{k}}(t)+\sqrt{2\ln t/N_{p_{k}}(t)} , where μ ^ p k  ( t ) \hat{\mu}{p{k}}(t) is the empirical mean profit and N p k  ( t ) N_{p_{k}}(t) the number of trials; the second term is an exploration bonus that shrinks as a price is tried more, implementing the principle of optimism in the face of uncertainty. In concrete terms, after 10,000 customers the seller loses roughly 100 customers' worth of revenue to the uncertainty in demand. No algorithm can do better without imposing structure on D D . For adversarial valuations (chosen by a worst-case opponent rather than drawn from a fixed distribution), the minimax regret rises to Θ  ( T 2 / 3 ) \Theta(T^{2/3}) , achieved by the Exp3 algorithm 178 178 178 Exp3 (Auer et al., 2002b) maintains a weight w k  ( t ) w_{k}(t) for each price, selecting p k p_{k} with probability proportional to w k  ( t ) w_{k}(t) and updating the chosen price's weight by exp  ( η  r ^ k , t ) \exp(\eta\hat{r}{k,t}) where r ^ k , t \hat{r}{k,t} is the revenue importance-weighted by the selection probability; because no model of demand is assumed, the guarantee holds against an adversary who chooses valuations after observing the algorithm. on a discretized price grid. I focus on the stochastic setting throughout this chapter.
10.1.2 Parametric Demand
Broder and Rusmevichientong ( 2012) consider a parametric demand model d  ( p ; z ) = Pr  ( V ≥ p ) d(p;z)=\Pr(V\geq p) , where z ∈ ℝ n z\in\mathbb{R}^{n} is an unknown parameter governing the demand curve. The seller observes binary purchase decisions and updates a maximum likelihood estimate of z z . Under standard regularity conditions (bounded demand, unique optimal price, smooth revenue function), the minimax regret is again Θ  ( T ) \Theta(\sqrt{T}) . 179 179 179 The lower bound (Theorem 3.1 of Broder and Rusmevichientong ( 2012) ) constructs a linear demand family where all demand curves pass through the same point at the optimal price p ∗  ( z 0 ) p^{*}(z_{0}) . Observing purchases at this price provides no information about z z . An MLE-Cycle policy that interleaves dedicated exploration rounds with greedy pricing achieves the matching upper bound O  ( T ) O(\sqrt{T}) (Theorem 3.6). Parametric structure alone does not break the T \sqrt{T} barrier.
The picture changes under a “well-separated” condition requiring that every price in the feasible set is informative about the demand parameter. Formally, the Fisher information I  ( p , z ) I(p,z) is bounded below by c f > 0 c_{f}>0 for all prices p p and parameters z z . 180 180 180 This means no two demand curves d  ( p ; z ) d(p;z) and d  ( p ; z ′ ) d(p;z^{\prime}) cross on the pricing interval, so every purchase observation distinguishes the two hypotheses. In the lower-bound family of Theorem 3.1, the curves all cross at p = 1 p=1 , which is why the T \sqrt{T} floor emerges. Under well-separation, a pure greedy policy (MLE-Greedy, pricing at p ∗  ( z ^ t ) p^{*}(\hat{z}_{t}) each period) achieves O  ( log  T ) O(\log T) regret (Theorem 4.8), because every price is informative and dedicated exploration rounds become unnecessary. 
Figure 17: Revenue curves r  ( p ) = r ∗ − k  ( p − p ∗ ) 2 r(p)=r^{}-k(p-p^{})^{2} for four demand curvatures k ∈ { 0.5 , 1.0 , 2.0 , 3.5 } k\in{0.5,1.0,2.0,3.5} . All models agree at the optimal price p ∗ = 5 p^{}=5 . Within the shaded exploration zone, the curves are nearly indistinguishable, so playing prices near p ∗ p^{} is uninformative about the demand parameter.
10.1.3 High-Dimensional Features with Sparsity
Javanmard and Nazerzadeh ( 2019) extend the setting to products described by d d -dimensional feature vectors x t x_{t} . The market value is v t = x t ⊤  θ 0 + z t v_{t}=x_{t}^{\top}\theta_{0}+z_{t} , where θ 0 ∈ ℝ d \theta_{0}\in\mathbb{R}^{d} is unknown and z t z_{t} is i.i.d. noise from a known log-concave distribution F F . 181 181 181 Log-concavity of F F and 1 − F 1-F is satisfied by the normal, logistic, uniform, Laplace, and exponential distributions. It ensures that expected revenue p ⋅ [ 1 − F  ( p − x t ⊤  θ 0 ) ] p\cdot[1-F(p-x_{t}^{\top}\theta_{0})] is strictly quasi-concave in p p , giving a unique optimal price. Only s 0 s_{0} of the d d coordinates of θ 0 \theta_{0} are nonzero, but the seller does not know which ones.
Their RMLP algorithm (Regularized Maximum Likelihood Pricing) operates in episodes whose lengths double (1, 2, 4, 8, …). At each episode boundary, the seller fits a LASSO-penalized maximum likelihood estimate of θ 0 \theta_{0} using data from the previous episode, then prices greedily throughout the current episode. The regret is O  ( s 0  log  d ⋅ log  T ) O(s_{0}\log d\cdot\log T) (Theorem 4.1), with a matching lower bound of Ω  ( s 0  ( log  d + log  T ) ) \Omega(s_{0}(\log d+\log T)) (Theorem 5.1). The reason this beats T \sqrt{T} connects back to the Broder lower bound. In the parametric model of Section 10.1.2, all demand curves can cross at the optimal price, making that price uninformative. Here, customer features vary across periods, so the aggregate demand function at any fixed price changes in proportion to the estimation error in θ 0 \theta_{0} . Every price is informative, and dedicated exploration rounds become unnecessary. 182 182 182 If some feature directions are rarely observed, the seller cannot learn all coordinates of θ 0 \theta_{0} quickly, and regret degrades to O  ( log  ( d ) ⋅ T ) O(\sqrt{\log(d)\cdot T}) (Theorem 4.2). If the noise distribution belongs to a known parametric family but its scale parameter is unknown, regret reverts to Ω  ( T ) \Omega(\sqrt{T}) (Theorem 7.1), foreshadowing the result of Xu and Wang ( 2021) discussed in Section 10.3. Even with hundreds of features, if only a handful matter, learning is fast.
10.2 Revealed Preference and Partial Identification
Misra et al. ( 2019) bring economic theory into the bandit pricing framework. Their model has K K discrete prices, S S consumer segments (segment membership observed, but valuations unknown), and within-segment heterogeneity δ \delta . A consumer in segment s s has valuation v i = v s + n i v_{i}=v_{s}+n_{i} , where v s v_{s} is the segment midpoint and n i ∈ [ − δ , δ ] n_{i}\in[-\delta,\delta] is idiosyncratic noise. The key structural assumption is WARP (Weak Axiom of Revealed Preference): if a consumer buys at price p p , she would buy at any lower price p ′ < p p^{\prime}<p .
WARP enables partial identification of each segment's valuation. Suppose the seller has offered several prices to segment s s . Define p s min = max  { p k : all customers purchased } p_{s}^{\min}=\max{p_{k}:\text{all customers purchased}} and p s max = min  { p k : no customer purchased } p_{s}^{\max}=\min{p_{k}:\text{no customer purchased}} . Then the segment midpoint lies in [ p s min , p s max ] [p_{s}^{\min},p_{s}^{\max}] , and within-segment heterogeneity satisfies δ ^ s ≤ ( p s max − p s min ) / 2 \hat{\delta}{s}\leq(p{s}^{\max}-p_{s}^{\min})/2 . These bounds propagate to aggregate demand: for each price p k p_{k} , the seller constructs upper and lower bounds on total profit π  ( p k ) = p k ⋅ D  ( p k ) \pi(p_{k})=p_{k}\cdot D(p_{k}) . When the profit upper bound at some price falls below the best profit lower bound across all prices, that price is dominated and permanently eliminated from consideration.
The UCB-PI algorithm combines dominance elimination with a price-scaled exploration bonus:
I p k  ( t ) = μ ^ p k  ( t ) + p k  2  ln  t N p k  ( t ) I_{p_{k}}(t)=\hat{\mu}{p{k}}(t)+p_{k}\sqrt{\frac{2\ln t}{N_{p_{k}}(t)}}
(90)
if p k p_{k} is not dominated, and I p k  ( t ) = 0 I_{p_{k}}(t)=0 otherwise, where μ ^ p k  ( t ) \hat{\mu}{p{k}}(t) is the average profit observed at price p k p_{k} and N p k  ( t ) N_{p_{k}}(t) is the number of trials. 183 183 183 Standard UCB1 uses an exploration bonus of 2  ln  t / N p k  ( t ) \sqrt{2\ln t/N_{p_{k}}(t)} , which assumes rewards in [ 0 , 1 ] [0,1] . Since profit at price p k p_{k} is bounded by p k p_{k} , scaling the bonus by p k p_{k} tightens exploration for cheap prices that cannot contribute much profit regardless. Two innovations drive the improvement over standard UCB1. First, dominance elimination reduces the effective number of arms the algorithm must explore. Second, the p k p_{k} scaling focuses exploration on prices where uncertainty actually matters for profit. Together, these yield O  ( log  T ) O(\log T) regret.
𝔼  [ R T  ( UCB-PI ) ] ≤ ∑ k ≠ k ∗ 8  p k  log  T Δ k + ( 1 + π 2 3 )  ∑ k = 1 K Δ k \mathbb{E}[R_{T}(\text{UCB-PI})]\leq\sum_{k\neq k^{*}}\frac{8p_{k}\log T}{\Delta_{k}}+\left(1+\frac{\pi^{2}}{3}\right)\sum_{k=1}^{K}\Delta_{k}
(91)
where Δ k = μ k ∗ − μ k \Delta_{k}=\mu_{k^{*}}-\mu_{k} is the gap between arm k k and the optimal arm. 184 184 184 The first sum is the leading term, scaling as O  ( log  T ) O(\log T) . The second sum is a constant that does not grow with T T . Replacing p k p_{k} with 1 recovers the standard UCB1 bound, which is looser.
Misra et al. ( 2019) calibrate the model to a field experiment at ZipRecruiter, a B2B online recruiting platform. With 7,870 customers per month, 1,000 segments, and 10 price points from $19 to $399, UCB-PI achieves 98% of oracle profit and produces 43% higher profits during the first month of testing compared to a learn-then-earn alternative. The algorithm has both higher mean profit and lower variance, reflecting the value of eliminating dominated prices early. 185 185 185 For multi-product settings, Mueller et al. ( 2019) impose low-rank structure on the price-sensitivity matrix, achieving regret O  ( T 3 / 4  d ) O(T^{3/4}\sqrt{d}) that scales with the latent demand dimension d d rather than the number of products. Badanidiyuru et al. ( 2013) extend the bandit framework to handle inventory constraints (“bandits with knapsacks”), relevant when the seller faces limited stock alongside the pricing decision.
10.3 The Value of Knowing the Noise Distribution
Xu and Wang ( 2021) ask how much it helps to know the shape of demand uncertainty. In their model, a feature vector x t ∈ ℝ d x_{t}\in\mathbb{R}^{d} describes each sales session, the customer's valuation is w t = x t ⊤  θ ∗ + N t w_{t}=x_{t}^{\top}\theta^{}+N_{t} where θ ∗ \theta^{} is unknown and N t N_{t} is zero-mean i.i.d. noise with CDF F F , and the seller observes only whether the customer bought at the posted price. The answer depends on whether F F is known. 186 186 186 The regret benchmark here differs from Section 10.1.1. Kleinberg and Leighton ( 2003) and Broder and Rusmevichientong ( 2012) measure regret against the best fixed price; Xu and Wang ( 2021) and Liu et al. ( 2024) measure regret against the clairvoyant contextual policy that sets the optimal price p t ∗ p_{t}^{*} for each customer's features x t x_{t} . The contextual benchmark is harder, which makes the O  ( d  log  T ) O(d\log T) rate more impressive.
If F F is known (the seller knows that demand shocks are, say, normally distributed with known variance), the EMLP algorithm (Epoch-based Maximum Likelihood Pricing) achieves regret O  ( d  log  T ) O(d\log T) (Theorem 3). 187 187 187 EMLP runs in doubling epochs of length τ k = 2 k − 1 \tau_{k}=2^{k-1} . At each epoch boundary, the seller fits a maximum likelihood estimate θ ^ k \hat{\theta}{k} using data from the previous epoch, then prices greedily at p t = J  ( x t ⊤  θ ^ k ) p{t}=J(x_{t}^{\top}\hat{\theta}{k}) throughout the epoch, where J  ( u ) = arg  max v  v  [ 1 − F  ( v − u ) ] J(u)=\arg\max{v},v[1-F(v-u)] is the revenue-maximizing price function. The key technical insight is that the negative log-likelihood is strongly convex (Lemma 7 of Xu and Wang ( 2021) ), so MLE concentrates at rate O  ( d / τ k ) O(d/\tau_{k}) . Since regret is quadratic in the parameter estimation error (Lemma 5) and there are O  ( log  T ) O(\log T) epochs, the total regret is O  ( d  log  T ) O(d\log T) . After 10,000 customers with d = 5 d=5 features, the revenue loss is roughly 50 customers' worth, an improvement over the T ≈ 100 \sqrt{T}\approx 100 customers' worth that Kleinberg's lower bound imposes without structural knowledge.
If F F is unknown (even if only the variance of a Gaussian is unknown, with everything else known), the regret is at least Ω  ( T ) \Omega(\sqrt{T}) (Theorem 12). 188 188 188 The lower bound constructs two noise variances σ 1 = 1 \sigma_{1}=1 and σ 2 = 1 − T − 1 / 4 \sigma_{2}=1-T^{-1/4} . Any algorithm that performs well under both must spend Ω  ( T ) \Omega(\sqrt{T}) revenue distinguishing the two cases. This extends the “uninformative price” phenomenon of Broder and Rusmevichientong ( 2012) : when the seller does not know F F , there exist prices at which observed purchase behavior is nearly identical under different demand parameters. The seller is back to the Kleinberg baseline, with no algorithm able to achieve sublinear improvement regardless of how many features are available.
The gap between O  ( d  log  T ) O(d\log T) and Ω  ( T ) \Omega(\sqrt{T}) is super-polynomial in T T , not merely a constant factor. When an economist specifies a logit or probit demand model, the assumed noise distribution purchases a qualitative improvement in learning rate. Semiparametric approaches that leave the error distribution unspecified pay a concrete cost, reverting from logarithmic to polynomial regret. 189 189 189 Tullii et al. ( 2024) establish the tightest known bound under minimal distributional assumptions: if the noise distribution (c.d.f.) is merely Lipschitz continuous, the minimax regret is Θ  ( T 2 / 3 ) \Theta(T^{2/3}) , strictly between the log  T \log T rate with known F F and the T \sqrt{T} rate with unknown F F . Fan et al. ( 2024) consider a semiparametric setting where the noise density is smooth and connect the pricing problem to the econometrics of semiparametric estimation.
10.4 Strategic Buyers
Liu et al. ( 2024) introduce buyer manipulation into contextual dynamic pricing. At time t t , a buyer arrives with true covariates x t 0 ∈ ℝ d x_{t}^{0}\in\mathbb{R}^{d} and valuation v t = θ 0 ⊤  x t 0 + z t v_{t}=\theta_{0}^{\top}x_{t}^{0}+z_{t} . The seller announces a pricing rule p t = g  ( θ ^ k ⊤  x t ) p_{t}=g(\hat{\theta}{k}^{\top}x{t}) , where θ ^ k \hat{\theta}_{k} is the current parameter estimate. Crucially, the buyer observes this rule and can distort her reported features. She solves a cost-minimization problem:
min x ~  ( p − v t ) + 1 2  ( x ~ − x t 0 ) ⊤  A  ( x ~ − x t 0 ) \min_{\tilde{x}};(p-v_{t})+\frac{1}{2}(\tilde{x}-x_{t}^{0})^{\top}A(\tilde{x}-x_{t}^{0})
(92)
where A A is a positive definite matrix governing manipulation costs. 190 190 190 The matrix A A captures how costly it is for the buyer to distort each feature dimension. High eigenvalues of A A mean manipulation is expensive. This is the standard model of strategic classification (Hardt et al., 2016) , adapted to pricing. The first-order condition yields a systematic bias: the buyer shifts her features to make the seller's model predict a lower valuation, securing a lower price. The seller observes only the distorted features x ~ t \tilde{x}{t} , not the true x t 0 x{t}^{0} .
Theorem 6 (Theorem 1 of Liu et al. ( 2024) ).
Under standard regularity conditions, any pricing policy that treats reported features as truthful accumulates regret Ω  ( T ) \Omega(T) .
The regret is linear in T T : every standard dynamic pricing algorithm, including EMLP and RMLP, systematically underprices because it bases decisions on manipulated features, and the bias does not shrink with more data because the manipulation is endogenous to the pricing rule.
The fix is to jointly estimate demand parameters and manipulation behavior. Liu et al. ( 2024) propose an episodic algorithm with two phases per episode. During the exploration phase, the seller posts uniform random prices that do not depend on features. Since the price is independent of x ~ t \tilde{x}{t} , buyers have no incentive to manipulate, and the seller observes true features x t 0 x{t}^{0} . During the exploitation phase, the seller uses the corrected pricing rule that anticipates the manipulation:
p t = g  ( θ ^ k ⊤  x t + β ^ k ⊤  A − 1  β ^ k ⋅ g ′  ( θ ^ k ⊤  x t ) ) p_{t}=g\left(\hat{\theta}{k}^{\top}x{t}+\hat{\beta}{k}^{\top}A^{-1}\hat{\beta}{k}\cdot g^{\prime}(\hat{\theta}{k}^{\top}x{t})\right)
(93)
where β ^ k \hat{\beta}_{k} is the estimated coefficient on the manipulable features and g g is the optimal pricing function. This correction adds a markup that offsets the anticipated feature distortion.
Theorem 7 (Theorem 2 of Liu et al. ( 2024) ).
With known manipulation cost matrix A A , the strategic pricing algorithm achieves regret O  ( d  T ) O(d\sqrt{T}) .
When A A is unknown, the seller can still recover O  ( d  T / τ ) O(d\sqrt{T/\tau}) regret by tracking repeat buyers across exploration and exploitation phases, where τ \tau is the fraction of buyers who appear in both phases (Theorem 3). Higher repeat rates mean more matched pairs for estimating manipulation behavior.
Incentive compatibility matters even in settings where the seller is “just” learning demand. 191 191 191 Agrawal and Tang ( 2024) document a related phenomenon in pricing with reference effects. If consumers anchor on past prices, a static pricing policy that ignores reference dependence accumulates linear regret Ω  ( T ) \Omega(T) . Chen et al. ( 2025) show that imposing fairness constraints (requiring similar prices for similar customers) raises the regret floor to Θ  ( T 2 / 3 ) \Theta(T^{2/3}) , a social cost of equitable treatment.
10.5 Comparison of Regret Rates
Table 19 collects regret rates ordered from weakest to strongest structural assumptions. The dominant pattern is that stronger assumptions yield faster learning, with the gap between log  T \log T and T \sqrt{T} being super-polynomial in T T , not merely a constant factor. Strategic behavior is the outlier: it produces linear regret that no amount of data can overcome without explicit correction. Figure 18 plots each rate on a log-log scale.
Table 19: Regret rates in dynamic pricing under progressively stronger assumptions. T T is the number of customers, d d the feature dimension, s 0 s_{0} the sparsity level. The last column translates asymptotic rates into concrete terms for T = 10 , 000 T=10{,}000 with d = 5 d=5 , setting constants to 1.
Figure 18: Theoretical regret rate functions at constants equal to 1, d = 5 d=5 . Two cases for the s 0  log  d  log  T s_{0}\log d\log T rate are shown: s 0 = 1 s_{0}=1 (very sparse, ≈ 15 \approx 15 lost at T = 10 , 000 T=10{,}000 ) and s 0 = 5 s_{0}=5 (moderate sparsity, ≈ 74 \approx 74 lost). The vertical line marks T = 10 , 000 T=10{,}000 , matching the “Per 10K” column of Table 19.
10.6 Applications
10.6.1 Joint Assortment and Pricing at Scale
Cai et al. ( 2023) tackle the joint assortment-pricing problem, where a retailer must simultaneously choose which products to display and at what prices. With a large catalog and limited shelf space, the number of possible assortments is combinatorially vast; for a Chinese instant noodle producer with 176 products and 30 display slots, there are ( 176 30 ) ≈ 6.4 × 10 33 \binom{176}{30}\approx 6.4\times 10^{33} possible assortments before prices are even set. Customer demand also depends on market context such as region and season. In each period t t , the retailer selects an assortment-pricing vector a t ∈ ℝ d a a_{t}\in\mathbb{R}^{d_{a}} (encoding which products to display and at what prices), observes a context vector x t ∈ ℝ d x x_{t}\in\mathbb{R}^{d_{x}} (encoding customer demographics and market conditions), and earns revenue Y t Y_{t} . Cai et al. model expected revenue as 𝔼  [ Y t ∣ x t , a t ] = a t ⊤  Θ ∗  x t \mathbb{E}[Y_{t}\mid x_{t},a_{t}]=a_{t}^{\top}\Theta^{}x_{t} , where Θ ∗ ∈ ℝ d a × d x \Theta^{}\in\mathbb{R}^{d_{a}\times d_{x}} is an unknown matrix assumed to have low rank r ≪ min  { d a , d x } r\ll\min{d_{a},d_{x}} . The low-rank assumption is the demand-side analogue of factor models in asset pricing; a small number of latent dimensions (flavor preferences, seasonal effects, price sensitivity) explain most of the variation in purchasing behavior.
Their Hi-CCAB algorithm estimates Θ ∗ \Theta^{*} via penalized least squares, where the penalty is the nuclear norm (the sum of singular values) of Θ \Theta . This penalty encourages low-rank solutions, playing the same role for matrices that the LASSO penalty plays for sparse vectors. The time-averaged regret is O ~  ( T − 1 / 6 ) \tilde{O}(T^{-1/6}) with dimension dependence r  ( d a + d x ) r(d_{a}+d_{x}) rather than d a ⋅ d x d_{a}\cdot d_{x} , so the effective parameter count scales with the number of latent factors, not the full product-by-context matrix. In simulation, Hi-CCAB achieves nearly four times the cumulative sales of the noodle producer's historical assortment strategies, averaged over 100 replications.
Ganti et al. ( 2018) deploy Thompson Sampling for dynamic pricing at Walmart.com. Their MAX-REV-TS algorithm models demand for each item i i on day t t via a constant-elasticity function d i , t  ( p ) = f i , t  ( p / p i , t − 1 ) γ i ∗ d_{i,t}(p)=f_{i,t}(p/p_{i,t-1})^{\gamma_{i}^{}} , where d i , t  ( p ) d_{i,t}(p) is unit sales at price p p , f i , t f_{i,t} is a baseline demand forecast at the previous day's price p i , t − 1 p_{i,t-1} , and γ i ∗ < − 1 \gamma_{i}^{}<-1 is the unknown price elasticity. The structural assumption, that demand responds to price through a single elasticity parameter per item, reduces the learning problem from estimating a full demand curve to estimating one scalar per item. MAX-REV-TS places a Gaussian prior over the elasticity vector γ ∗ \gamma^{*} and draws posterior samples at each period to solve a constrained revenue maximization problem. In a five-week field experiment on a basket of roughly 5,000 items, Thompson Sampling produced a statistically significant increase in per-item revenue relative to the passive pricing baseline.
10.7 Simulation Study: The Knowledge Ladder
I run six algorithms on the Misra et al. ( 2019) demand environment to trace how cumulative regret responds to increasing structural knowledge. 192 192 192 The environment has K = 100 K=100 prices on a grid from $0.01 to $1.00, S = 1 , 000 S=1{,}000 consumer segments with equal weights, within-segment heterogeneity δ = 0.1 \delta=0.1 , and segment midpoints v s ∼ Uniform  ( 0.1 , 0.9 ) v_{s}\sim\mathrm{Uniform}(0.1,0.9) . A consumer purchases if and only if v i ≥ p v_{i}\geq p (WARP). Each algorithm runs across 10 seeds with T = 200 , 000 T=200{,}000 rounds. The six algorithms, ordered by the structural knowledge they exploit, are: (0) ε \varepsilon -greedy with ε = 0.1 \varepsilon=0.1 , which never adapts its exploration rate; (1) Learn-Then-Earn (LTE), which explores uniformly for the first 5% of rounds and then commits to the empirical best price; (2) UCB1 (Auer et al., 2002a) , which adapts exploration via confidence bounds but ignores demand structure; (3) Thompson Sampling (Thompson, 1933) , which maintains a Bayesian posterior over purchase rates 193 193 193 At each period the algorithm draws one sample μ ~ k \tilde{\mu}{k} from each arm's posterior over its purchase rate and selects the arm with the highest sampled expected profit p k  μ ~ k p{k}\tilde{\mu}_{k} ; arms with uncertain posteriors have high-variance draws and are selected frequently, while well-estimated arms are selected in proportion to how likely they are optimal.; (4) UCB-PI (Misra et al., 2019) , which uses WARP to eliminate dominated prices and scales the exploration bonus by the price level; and (5) UCB-PI-tuned, which adds a variance-based refinement to the exploration bonus.
Figure 19 reports cumulative regret at four checkpoints. The results confirm the theoretical progression from Table 19: ε \varepsilon -greedy grows linearly, UCB1 and Thompson Sampling grow as T \sqrt{T} , and UCB-PI-tuned achieves the lowest regret at every checkpoint past T = 10 , 000 T=10{,}000 . The untuned UCB-PI variant overexplores, scaling as T \sqrt{T} rather than the theoretical log  T \log T , illustrating that WARP-based elimination alone is insufficient without variance-calibrated exploration bonuses. 
Figure 19: Cumulative regret on log-log axes ( K = 100 K=100 , S = 1 , 000 S=1{,}000 , 10 seeds). Each algorithm's legend entry includes its theoretical regret rate. Dashed lines show Θ  ( T ) \Theta(T) , O  ( T ) O(\sqrt{T}) , and O  ( log  T ) O(\log T) reference rates. Shaded regions are ± 2 \pm 2 standard errors.
11 Offline Reinforcement Learning and Human Feedback
In the preceding chapters, the agent interacts with its environment while learning: it tries a price, observes a purchase, and updates its belief. Online learning is natural in digital markets where experimentation is cheap and feedback is instant. In many economically important settings, however, experimentation is impossible or prohibitively costly. A hospital cannot randomly assign treatments to learn optimal dosing. A central bank cannot experiment with interest rate schedules to discover optimal monetary policy. A firm inheriting a decade of transaction logs wants to improve its pricing rule without conducting new experiments during the transition. In each case, the agent has access to a fixed dataset of past decisions and outcomes, collected under some historical policy, and must learn the best possible new policy from this data alone.
This is the problem of offline reinforcement learning, also called batch reinforcement learning. 194 194 194 The term “batch RL” was standard in the earlier literature (Ernst et al., 2005; Lange et al., 2012) . “Offline RL” became dominant after Levine et al. ( 2020) , who distinguished it from off-policy RL (which still collects new data, just under a different policy than the target). I use “offline RL” throughout. The agent never queries the environment. All learning happens from a fixed dataset 𝒟 = { ( s i , a i , r i , s i ′ ) } i = 1 n \mathcal{D}={(s_{i},a_{i},r_{i},s_{i}^{\prime})}{i=1}^{n} collected by some behavioral policy π b \pi{b} . The goal is to find a policy π ^ \hat{\pi} whose value V π ^ V^{\hat{\pi}} is as close to the optimal V ∗ V^{*} as possible.
Online RL algorithms (Q-learning, SARSA, policy gradient methods from Section 4) can in principle be applied to offline data by treating the dataset as a replay buffer. In practice, this fails catastrophically. The reason is distributional shift: the learned policy π ^ \hat{\pi} inevitably queries state-action pairs that the behavioral policy π b \pi_{b} never visited, and the Q-function at these unseen pairs is pure extrapolation. Because the Bellman backup propagates these extrapolation errors through the max operator, errors compound geometrically across the planning horizon, producing arbitrarily poor policies. 195 195 195 This failure mode was first demonstrated empirically by Fujimoto et al. ( 2019) , who showed that standard off-policy algorithms (DDPG, SAC) trained purely from a static dataset performed worse than the behavioral policy itself, even when that behavioral policy was a partially-trained, mediocre agent. The gap widened with dataset size, the opposite of what one expects from more data.
11.1 The Pessimism Principle
The overestimation failure has a clean theoretical characterization. Consider tabular Q-learning with a fixed dataset. At any state-action pair ( s , a ) (s,a) not in the dataset, the empirical Bellman backup is undefined, but the max in max a ′  Q ^  ( s ′ , a ′ ) \max_{a^{\prime}}\hat{Q}(s^{\prime},a^{\prime}) may still select it if the randomly-initialized Q-value happens to be high. With function approximation, the problem is subtler but identical in spirit: the function approximator can assign high values to out-of-distribution inputs without any corrective signal.
The solution, established simultaneously by several groups, is the pessimism principle: construct a lower confidence bound on the Q-function and optimize against it. Formally, given a dataset 𝒟 \mathcal{D} and a confidence parameter δ \delta , construct a penalty function Γ  ( s , a ) \Gamma(s,a) that is large where data coverage is poor, and define the pessimistic Q-function
Q ~  ( s , a ) = Q ^  ( s , a ) − Γ  ( s , a ) \tilde{Q}(s,a)=\hat{Q}(s,a)-\Gamma(s,a)
(94)
where Q ^ \hat{Q} is the standard empirical Bellman solution. The policy π ^  ( s ) = arg  max a  Q ~  ( s , a ) \hat{\pi}(s)=\arg\max_{a}\tilde{Q}(s,a) selects actions that are both high-value and well-supported by data.
Definition D1 (Pessimistic Value Iteration, PEVI (Jin et al., 2021) ).
Given dataset 𝒟 \mathcal{D} , penalty function Γ h  ( s , a ) \Gamma_{h}(s,a) for each stage h h , and horizon H H , PEVI computes
where P ^ h \hat{P}_{h} is the empirical transition operator estimated from 𝒟 \mathcal{D} .
Jin et al. ( 2021) show that with Γ h  ( s , a ) = c ⋅ H 3 / N h  ( s , a ) \Gamma_{h}(s,a)=c\cdot\sqrt{H^{3}/N_{h}(s,a)} , where N h  ( s , a ) N_{h}(s,a) counts visits to ( s , a ) (s,a) at stage h h and c c is an absolute constant, PEVI achieves
V ∗ − V π ^ ≤ O ~  ( ∑ h = 1 H 𝔼 π ∗  [ 1 N h  ( s h , a h ) ] ) V^{}-V^{\hat{\pi}}\leq\tilde{O}\left(\sum_{h=1}^{H}\mathbb{E}_{\pi^{}}\left[\sqrt{\frac{1}{N_{h}(s_{h},a_{h})}}\right]\right)
(98)
with high probability. The bound depends on the data coverage at states and actions visited by the optimal policy π ∗ \pi^{*} , not the full state-action space. This is the key advantage of pessimism over uniform coverage requirements.
11.1.1 Concentrability and Coverage
The bound in ( 98) is instance-dependent, scaling with how well π b \pi_{b} covers π ∗ \pi^{*} . The classical way to formalize this is through concentrability coefficients (Munos and Szepesvári, 2008) .
Definition D2 (Single-policy concentrability).
The single-policy concentrability coefficient of π ∗ \pi^{*} with respect to π b \pi_{b} is
C ∗ = max h ∈ [ H ]  ‖ d h π ∗ d h π b ‖ ∞ C^{}=\max_{h\in[H]}\left|\frac{d_{h}^{\pi^{}}}{d_{h}^{\pi_{b}}}\right|_{\infty}
(99)
where d h π  ( s , a ) d_{h}^{\pi}(s,a) is the state-action occupancy measure of π \pi at stage h h .
When C ∗ C^{} is finite, the optimal policy visits only states and actions that π b \pi_{b} also visits with non-negligible probability, and the 1 / N h  ( s h , a h ) 1/\sqrt{N_{h}(s_{h},a_{h})} terms in ( 98) remain controlled. Rashidinejad et al. ( 2021) prove that single-policy concentrability is both necessary and sufficient for offline learning: if C ∗ < ∞ C^{}<\infty , then O  ( | 𝒮 |  H 2  C ∗ / ϵ 2 ) O(|\mathcal{S}|H^{2}C^{}/\epsilon^{2}) samples suffice for an ϵ \epsilon -optimal policy; if C ∗ = ∞ C^{}=\infty , no algorithm can guarantee suboptimality better than the behavioral policy.
11.1.2 Impossibility Results
Zanette ( 2021) establish fundamental limits on offline RL by showing that it can be exponentially harder than online RL. Specifically, there exist MDPs with S S states and horizon H H where online RL finds an ϵ \epsilon -optimal policy in poly  ( S , H , 1 / ϵ ) \text{poly}(S,H,1/\epsilon) episodes, but any offline algorithm requires Ω  ( 2 H ) \Omega(2^{H}) samples unless the dataset covers all reachable states. The construction uses a binary tree MDP where the optimal path visits a unique leaf, and any dataset that misses this leaf provides no information about the optimal action at the root.
The practical implication is that offline RL is not a universal replacement for online experimentation. When the behavioral policy is far from optimal, especially in long-horizon problems, offline methods provably cannot recover the optimal policy without exponentially large datasets. Pessimistic algorithms are the best one can do, but they are still fundamentally constrained by what the data contains.
11.2 Algorithms
I present four practical algorithms that instantiate different approaches to the distributional shift problem. All four can be understood as modifications of standard Q-learning (Section 4) that prevent the agent from overvaluing actions outside the data support.
11.2.1 Fitted Q-Iteration
Fitted Q-Iteration (FQI, Ernst et al., 2005) is the simplest offline RL algorithm, predating the modern pessimism framework. FQI applies the standard Bellman backup iteratively using supervised regression on the fixed dataset, as described in Section 4. It does not include any explicit pessimism mechanism. When state-action coverage is poor, the max in the Bellman backup selects the highest Q-value among all actions at s ′ s^{\prime} , including actions never observed in the data. If the function approximator generalizes poorly at these unseen actions, targets become noisy and biased upward, causing the overestimation cascade. FQI works well when coverage is good but degrades as coverage gaps grow. 196 196 196 Munos and Szepesvári ( 2008) prove finite-time error bounds for FQI under approximate Bellman completeness and all-policy concentrability. Both assumptions are strong, and violation of either leads to divergence in practice.
11.2.2 Conservative Q-Learning
Conservative Q-Learning (CQL, Kumar et al., 2020) adds an explicit penalty that pushes down Q-values at actions not well-represented in the data. The key idea is to add a regularizer to the Bellman error objective that minimizes Q-values under a broad distribution over actions while maximizing Q-values at the actions actually taken in the dataset.
Definition D3 (Conservative Q-Learning).
CQL modifies the standard Bellman error objective by adding a conservative regularizer. At each iteration, CQL solves
Q ^ k + 1 = arg  min Q  α  ( 𝔼 s ∼ 𝒟  [ log  ∑ a exp  Q  ( s , a ) ] − 𝔼 ( s , a ) ∼ 𝒟  [ Q  ( s , a ) ] ) + 1 2  𝔼 𝒟  [ ( Q  ( s , a ) − ℬ ^ π k  Q ^ k  ( s , a ) ) 2 ] \hat{Q}{k+1}=\arg\min{Q};\alpha\left(\mathbb{E}{s\sim\mathcal{D}}\left[\log\sum{a}\exp Q(s,a)\right]-\mathbb{E}{(s,a)\sim\mathcal{D}}[Q(s,a)]\right)+\frac{1}{2}\mathbb{E}{\mathcal{D}}\left[(Q(s,a)-\hat{\mathcal{B}}^{\pi_{k}}\hat{Q}_{k}(s,a))^{2}\right]
(100)
where α > 0 \alpha>0 is a hyperparameter controlling the degree of conservatism, and ℬ ^ π k \hat{\mathcal{B}}^{\pi_{k}} is the empirical Bellman operator.
The first term in the regularizer, log  ∑ a exp  Q  ( s , a ) \log\sum_{a}\exp Q(s,a) , is a soft maximum over all actions, pushing down Q-values uniformly. The second term, 𝔼 𝒟  [ Q  ( s , a ) ] \mathbb{E}_{\mathcal{D}}[Q(s,a)] , pulls Q-values back up at the data actions. The net effect is a penalty on Q-values for actions that appear infrequently relative to their softmax contribution. Kumar et al. ( 2020) prove that the resulting Q-function is a pointwise lower bound on the true Q-function (Theorem 3.2), making it a concrete instantiation of the pessimism principle from ( 94) with an implicit, data-adaptive penalty Γ \Gamma .
11.2.3 Implicit Q-Learning
Implicit Q-Learning (IQL, Kostrikov et al., 2022) avoids querying Q-values at unseen actions entirely. Instead of computing max a ′  Q  ( s ′ , a ′ ) \max_{a^{\prime}}Q(s^{\prime},a^{\prime}) in the Bellman backup (which requires evaluating Q Q at potentially out-of-distribution actions), IQL learns a separate value function V  ( s ) V(s) that approximates the in-sample maximum through expectile regression.
Definition D4 (Implicit Q-Learning).
IQL maintains three functions: Q θ  ( s , a ) Q_{\theta}(s,a) , V ψ  ( s ) V_{\psi}(s) , and a policy π ϕ  ( a | s ) \pi_{\phi}(a|s) . The value function is trained via expectile regression
L V  ( ψ ) = 𝔼 ( s , a ) ∼ 𝒟  [ L 2 τ  ( Q θ ¯  ( s , a ) − V ψ  ( s ) ) ] L_{V}(\psi)=\mathbb{E}{(s,a)\sim\mathcal{D}}\left[L{2}^{\tau}(Q_{\bar{\theta}}(s,a)-V_{\psi}(s))\right]
(101)
where L 2 τ  ( u ) = | τ − 𝟙  { u < 0 } | ⋅ u 2 L_{2}^{\tau}(u)=|\tau-\mathbbm{1}{u<0}|\cdot u^{2} is the asymmetric squared loss with expectile parameter τ ∈ ( 0.5 , 1 ) \tau\in(0.5,1) , and Q θ ¯ Q_{\bar{\theta}} uses a target network. The Q-function is trained with V ψ V_{\psi} as the continuation value
L Q  ( θ ) = 𝔼 ( s , a , r , s ′ ) ∼ 𝒟  [ ( r + γ  V ψ  ( s ′ ) − Q θ  ( s , a ) ) 2 ] L_{Q}(\theta)=\mathbb{E}{(s,a,r,s^{\prime})\sim\mathcal{D}}\left[(r+\gamma V{\psi}(s^{\prime})-Q_{\theta}(s,a))^{2}\right]
(102)
The expectile parameter τ \tau controls the degree of optimism within the data support. As τ → 1 \tau\to 1 , the expectile converges to the in-sample maximum; as τ → 0.5 \tau\to 0.5 , it converges to the in-sample mean. Setting τ = 0.7 \tau=0.7 balances exploiting the best observed actions against the noise in finite samples. The critical property is that the Q-function is never evaluated at actions outside the dataset: the max \max operation is implicit in the expectile regression of V V .
11.2.4 Batch-Constrained Q-Learning
Batch-Constrained Q-Learning (BCQ, Fujimoto et al., 2019) takes a different approach: rather than modifying the Q-function objective, it restricts the policy to actions similar to those in the dataset. BCQ first learns a generative model G ω  ( s ) G_{\omega}(s) of the behavioral policy, then constrains the policy to only select actions with high likelihood under G ω G_{\omega} .
Definition D5 (Batch-Constrained Q-Learning).
BCQ learns a behavioral model G ω  ( a | s ) G_{\omega}(a|s) from the dataset via maximum likelihood, and constrains action selection
π ^  ( s ) = arg  max a : G ω  ( a | s ) ≥ τ ⋅ max a ′  G ω  ( a ′ | s )  Q θ  ( s , a ) \hat{\pi}(s)=\arg\max_{a:G_{\omega}(a|s)\geq\tau\cdot\max_{a^{\prime}}G_{\omega}(a^{\prime}|s)}Q_{\theta}(s,a)
(103)
where τ ∈ ( 0 , 1 ] \tau\in(0,1] is a threshold parameter. The Q-function is trained with standard Bellman backups, but the max in the target computation is also constrained to the feasible action set.
BCQ's constraint is hard rather than soft: actions with behavioral probability below τ \tau times the most likely action are simply excluded from consideration. This prevents the Q-function from ever being queried at truly out-of-distribution actions, addressing the distributional shift problem at the policy level rather than the value function level. The tradeoff is that BCQ's performance is bounded by the quality of actions in the dataset. If the behavioral policy never takes the optimal action at some state, BCQ cannot discover it regardless of sample size.
11.3 Simulation: Offline RL for Dynamic Pricing
The simulation study evaluates the four offline RL algorithms on a perishable inventory pricing problem with demand regime switching. A retailer with I max = 30 I_{\max}=30 units of perishable inventory must set prices over H = 20 H=20 periods. The state ( i , d , t ) (i,d,t) consists of current inventory i ∈ { 0 , … , 30 } i\in{0,\ldots,30} , demand regime d ∈ { 1 , 2 , 3 , 4 } d\in{1,2,3,4} , and time remaining t ∈ { 1 , … , 20 } t\in{1,\ldots,20} . The action is a price p ∈ { 1 , … , 10 } p\in{1,\ldots,10} . Demand follows Q ∼ Poisson  ( λ 0  [ d ] ⋅ e − 0.15  p ) Q\sim\text{Poisson}(\lambda_{0}[d]\cdot e^{-0.15p}) with base rates λ 0 = ( 1.5 , 3.0 , 5.0 , 8.0 ) \lambda_{0}=(1.5,3.0,5.0,8.0) , and the reward is r = p ⋅ min  ( Q , i ) r=p\cdot\min(Q,i) . Demand regimes follow a 4-state Markov chain with diagonal persistence 0.6. Unsold inventory at the terminal period incurs a spoilage cost of $2.00 per unit, making clearance pricing valuable near the deadline. 197 197 197 The spoilage penalty creates distributional shift. The optimal policy adapts prices to inventory level and time remaining, using lower prices near the deadline when inventory is high. The behavioral policy ignores these state variables and prices at the maximum, so the Q-function at state-adapted pricing actions is extrapolation from sparse data. The $2.00 penalty is a deliberate design choice: under harsher penalties (e.g., $10 per unit), all methods collapse to 48–53% of optimal regardless of algorithmic sophistication, confirming that no offline correction can overcome severe distributional shift when the penalty regime amplifies consequences of the behavioral policy's suboptimality. The behavioral policy represents a conservative pricing team that always sets the maximum price ( p = 10 p=10 ) regardless of demand regime, inventory, or time remaining, with probability 0.85 and randomizes uniformly over all prices with probability 0.15. 198 198 198 With 500 episodes (10,000 transitions) on a state-action space of 24,800 pairs, the 85% concentration at price 10 ensures that the behavioral state-action occupancy diverges significantly from the optimal policy's occupancy, while the 15% uniform component provides sparse off-policy coverage. All episodes start at full inventory ( i = 30 i=30 ). All offline methods train on 500 episodes and are evaluated over 1,000 episodes against the DP optimal policy computed by backward induction. 199 199 199 FQI uses the standard Bellman backup with max a ′  Q  ( s ′ , a ′ ) \max_{a^{\prime}}Q(s^{\prime},a^{\prime}) , deliberately without a target network, to isolate the overestimation cascade as a pedagogical baseline. Adding target networks to FQI mitigates but does not eliminate extrapolation error. CQL and IQL include target networks following their original implementations (Kumar et al., 2020; Kostrikov et al., 2022) ; for CQL, target networks proved essential, as the conservative penalty amplifies bootstrap instability without them. Results are averaged over 20 independent seeds.
Table 20: Policy value for each offline RL method, expressed as mean return and percentage of the DP optimal. Standard errors computed over 20 seeds.
FQI achieves 81.2% of the DP optimal, substantially below the behavioral cloning baseline of 88.0% (Table 20). Without any mechanism to control extrapolation error, the max a ′  Q  ( s ′ , a ′ ) \max_{a^{\prime}}Q(s^{\prime},a^{\prime}) operator in FQI's Bellman backup selects overestimated Q-values at out-of-distribution actions, and these overestimates compound across 200 iterations of fitted Q-iteration. CQL and IQL both exceed the behavioral baseline, achieving 91.9% and 92.0% respectively. 200 200 200 CQL uses α = 0.1 \alpha=0.1 , the result of a search over α ∈ { 5.0 , 2.0 , 0.5 , 0.1 } \alpha\in{5.0,2.0,0.5,0.1} . Larger values push Q-values down too aggressively, collapsing the learned policy to the behavioral action at most states; the right α \alpha is problem-specific and can vary by orders of magnitude. CQL's conservative penalty suppresses Q-values at actions not well-represented in the data while preserving relative ordering among data-supported actions, allowing the policy to discover lower prices that clear inventory near the deadline. IQL achieves the same improvement through a different mechanism: by replacing max a ′  Q  ( s ′ , a ′ ) \max_{a^{\prime}}Q(s^{\prime},a^{\prime}) with the expectile-regressed value function V  ( s ′ ) V(s^{\prime}) as the Bellman continuation, IQL avoids querying Q at unseen actions during training while still extracting a policy that improves on the behavioral at states where the 15% noise component revealed better pricing actions. BCQ matches the behavioral at 88.0%; its action constraint restricts the policy to prices near 10, preventing both overestimation and improvement. 201 201 201 When the behavioral policy concentrates 85% probability at a single action, BCQ's threshold constraint permits only that action at most states, effectively reducing BCQ to behavioral cloning regardless of the learned Q-values.
These results validate several theoretical predictions from the preceding sections. FQI's degradation below the behavioral baseline (81.2% versus 88.0%) demonstrates the overestimation cascade described in Section 11.2: without pessimism, the max a ′ \max_{a^{\prime}} operator selects overestimated Q-values at out-of-distribution actions, and 200 iterations of bootstrapping compound these errors geometrically (Fujimoto et al., 2019) . CQL and IQL both exceeding BC confirms the pessimism principle (Section 11.1): CQL's conservative penalty produces a pointwise lower bound on the true Q-function (Definition D3, Theorem 3.2 of Kumar et al. 2020 ), while IQL's expectile regression (Definition D4) avoids querying Q at unseen actions entirely (Kostrikov et al., 2022) . BCQ matching BC exactly illustrates the action-constraint tradeoff formalized in Definition D5: performance is bounded by the quality of actions in the data, and when the behavioral policy concentrates on a single action, no amount of Q-learning can overcome the constraint. 
Figure 20: Policy value (as % of DP optimal) versus behavioral policy randomness ϵ b \epsilon_{b} for four offline RL methods and the behavioral cloning baseline (BC). Higher ϵ b \epsilon_{b} increases data coverage. FQI peaks at moderate coverage ( ϵ b = 0.3 \epsilon_{b}=0.3 ) and collapses at both extremes. BCQ degrades at high ϵ b \epsilon_{b} as its behavioral constraint becomes vacuous.
Figure 20 varies the behavioral noise parameter ϵ b ∈ { 0.05 , 0.3 , 0.9 } \epsilon_{b}\in{0.05,0.3,0.9} . CQL and IQL remain above the BC baseline across all coverage levels, confirming that both pessimism mechanisms provide robustness to the data distribution. FQI exhibits non-monotone behavior: it peaks at moderate coverage ( ϵ b = 0.3 \epsilon_{b}=0.3 ) where partial exploration controls the overestimation cascade, but collapses at both extremes. 202 202 202 At high ϵ b \epsilon_{b} , the near-uniform behavioral policy provides Q-function targets across all actions, giving the unconstrained max a ′ \max_{a^{\prime}} operator more opportunities to select overestimated values rather than fewer. BCQ collapses at ϵ b = 0.9 \epsilon_{b}=0.9 because a nearly uniform behavioral policy renders the action constraint vacuous, reducing BCQ to unconstrained FQI. These coverage patterns connect directly to the concentrability framework (Definition D2): as ϵ b \epsilon_{b} decreases, the concentrability coefficient C ∗ C^{*} grows because the optimal policy's state-action occupancy diverges from the behavioral policy's, and the 1 / N h  ( s h , a h ) 1/\sqrt{N_{h}(s_{h},a_{h})} terms in ( 98) become large at states the optimal policy visits. CQL and IQL remain robust because their conservative adjustments scale with data sparsity, while FQI lacks this adaptive correction.
11.4 From Offline RL to Human Feedback
The offline RL algorithms above assume access to a scalar reward signal in the dataset. When rewards are observed, the problem reduces to learning a good policy from fixed data. In many domains, however, the reward itself is unknown and must be learned from human judgments. Reinforcement Learning from Human Feedback (RLHF) combines offline preference data with the policy optimization tools of offline RL: the agent never interacts with the environment during training, and all learning proceeds from a static dataset of human comparisons. The methods below extend the offline RL framework from learning policies given rewards to learning rewards given preferences, and then optimizing policies against those learned rewards.
Every chapter so far assumes access to a scalar reward signal: dynamic programming requires r  ( s , a ) r(s,a) , model-free RL observes r t r_{t} after each transition, and the Bellman optimality equation presupposes that rewards are known or observable. When they are neither, the DP/RL machinery cannot be applied directly.
In many domains, scalar rewards are unavailable but ordinal preferences over trajectories are easy to elicit. A human evaluator cannot assign a meaningful numerical score to a paragraph of text, but can reliably say “response A is better than response B.” The raw data is a set of trajectory pairs with binary preference labels. RLHF uses these ordinal comparisons to learn a proxy reward function r θ r_{\theta} , which then serves as the scalar signal for standard RL optimization. This is not an inverse problem in the IRL sense; the goal is not to rationalize observed behavior, but rather a two-stage forward problem in which the analyst first learns a reward from human judgments and then solves the resulting MDP. Christiano et al. ( 2017) demonstrated that this approach could train agents without an explicit reward function. RLHF has since become the predominant method for aligning large language models.
11.5 Learning Rewards from Preferences
The canonical RLHF framework is built on a formal model of human preference. The observed data consists of tuples ( s , y w , y l ) (s,y_{w},y_{l}) , where s s is a context, and y w y_{w} and y l y_{l} are two outputs, with y w y_{w} being the “winner” preferred by a human. Assuming preferences follow a latent utility model, the Bradley-Terry model (Bradley and Terry, 1952) gives the probability that y w y_{w} is preferred: P  ( y w ≻ y l | s ) = σ  ( r θ  ( s , y w ) − r θ  ( s , y l ) ) P(y_{w}\succ y_{l}|s)=\sigma(r_{\theta}(s,y_{w})-r_{\theta}(s,y_{l})) , where r θ : 𝒮 × 𝒴 → ℝ r_{\theta}:\mathcal{S}\times\mathcal{Y}\to\mathbb{R} is a learned reward model parameterized by θ \theta , trained to approximate human preferences (not the ground-truth reward, which is unobserved), and σ  ( ⋅ ) \sigma(\cdot) is the logistic function. This formulation is a binary logit model (Section 2, Equation 1). 203 203 203 Iskhakov et al. ( 2020) discuss the contrasts and synergies between machine learning and structural econometrics, including the shared reliance on logit-based choice models that underlies both RLHF and dynamic discrete choice estimation. The reward model parameters θ \theta are estimated by minimizing the negative log-likelihood of the observed human choices:
ℒ  ( θ ) = − 𝔼 ( s , y w , y l ) ∼ 𝒟  [ log  σ  ( r θ  ( s , y w ) − r θ  ( s , y l ) ) ] , \mathcal{L}(\theta)=-\mathbb{E}{(s,y{w},y_{l})\sim\mathcal{D}}\left[\log\sigma\left(r_{\theta}(s,y_{w})-r_{\theta}(s,y_{l})\right)\right],
(104)
In the LLM setting, the “outputs” y w y_{w} and y l y_{l} are token sequences, i.e., trajectories of the autoregressive policy 204 204 204 An autoregressive language model generates text token by token: at each step it outputs a distribution over the vocabulary conditioned on all preceding tokens, then samples the next token; the full response is therefore a trajectory in token space and the model acts as a sequential policy over a vocabulary-sized action set., so preferences are over trajectories rather than single actions. The preference loss in Equation ( 104) is MLE of a choice model where the “alternatives” are trajectory segments and the “choice” is the human-preferred one.
11.6 The RLHF Pipeline and Direct Optimization
The learned r θ r_{\theta} then serves as a proxy objective for policy optimization. Building on the reward-learning and RL fine-tuning framework of Ziegler et al. ( 2019) and Stiennon et al. ( 2020) , the canonical three-stage pipeline was formalized by Ouyang et al. ( 2022) . First, a base pretrained model is initialized via supervised fine-tuning (SFT) 205 205 205 Pretraining optimizes a language model to predict the next token across a massive text corpus, producing broad linguistic knowledge with no behavioral objective. Supervised fine-tuning (SFT) continues training on a small curated dataset of (prompt, ideal-response) pairs to specialize the model toward the desired task and establish the reference policy π S  F  T \pi^{SFT} from which the KL penalty is measured. on a small dataset of high-quality demonstrations, yielding an initial policy π S  F  T \pi^{SFT} . This grounds the model in the desired style and format. The second step is the reward model training as described, using preference data generated from this π S  F  T \pi^{SFT} .
In the third step, the SFT policy π ϕ \pi_{\phi} is fine-tuned via PPO (Section 5.5) to maximize the frozen reward model r θ r_{\theta} , 206 206 206 After fine-tuning concludes, the resulting LLM is deployed with frozen weights. Each user interaction is a forward pass in the execution phase (Section 2); the model does not update its parameters from conversations. Periodic retraining on new preference data constitutes a separate training phase. with a KL-divergence penalty preventing the policy from drifting into regions where r θ r_{\theta} is unreliable. The objective is
J ( ϕ ) = 𝔼 s ∼ 𝒟 , y ∼ π ϕ ( ⋅ | s ) [ r θ ( s , y ) ] − λ K  L 𝔼 s ∼ 𝒟 [ D K  L ( π ϕ ( ⋅ | s ) | | π S  F  T ( ⋅ | s ) ) ] , J(\phi)=\mathbb{E}{s\sim\mathcal{D},y\sim\pi{\phi}(\cdot|s)}[r_{\theta}(s,y)]-\lambda_{KL}\mathbb{E}{s\sim\mathcal{D}}[D{KL}(\pi_{\phi}(\cdot|s),||,\pi^{SFT}(\cdot|s))],
(105)
where D K  L D_{KL} is the Kullback-Leibler divergence and λ K  L \lambda_{KL} controls the penalty strength. 207 207 207 λ K  L \lambda_{KL} denotes the KL penalty weight, reserving β \beta for model parameters and γ \gamma for discount factors. The standard RLHF literature, including Rafailov et al. ( 2023) , uses β \beta for this parameter. Without this constraint, the policy exploits inaccuracies in r θ r_{\theta} to achieve high proxy scores with degenerate behavior (“reward hacking”), the RLHF analogue of divergence under function approximation (Section 5.3).
The KL-regularized objective in Equation ( 105) admits a Bayesian interpretation (Korbak et al., 2022) . In this view, the reference policy π S  F  T \pi^{SFT} acts as a prior distribution over plausible responses. The reward model r θ r_{\theta} provides evidence, specifying which responses are more desirable. The goal of alignment is to find the posterior distribution π ∗ \pi^{*} that optimally combines the prior with this evidence. This ideal posterior policy takes the form of Equation ( 106):
π ∗  ( y | s ) ∝ π S  F  T  ( y | s )  exp  ( r θ  ( s , y ) λ K  L ) . \pi^{*}(y|s)\propto\pi^{SFT}(y|s)\exp\left(\frac{r_{\theta}(s,y)}{\lambda_{KL}}\right).
(106)
The reward function scaled by λ K  L \lambda_{KL} defines the log-likelihood, so the KL-regularized objective J  ( ϕ ) J(\phi) is equivalent (up to an additive constant) to the Evidence Lower Bound (ELBO) for this Bayesian inference problem. Maximizing the RLHF objective via PPO is therefore variational inference: finding the policy π ϕ \pi_{\phi} that minimizes KL divergence to π ∗ \pi^{*} . This reframes the KL penalty as a structural component of the inference problem rather than an ad-hoc regularizer.
Despite this closed-form characterization, the three-stage RLHF pipeline is complex to implement, requiring training multiple large models and a computationally expensive RL loop. Direct Preference Optimization (DPO), introduced by Rafailov et al. ( 2023) , collapses the pipeline into a single supervised learning objective by reparameterizing the reward function in terms of π ∗ \pi^{*} and π S  F  T \pi^{SFT} , as in Equation ( 107):
r  ( s , y ) = λ K  L  log  ( π ∗  ( y | s ) π S  F  T  ( y | s ) ) + λ K  L  log  Z  ( s ) . r(s,y)=\lambda_{KL}\log\left(\frac{\pi^{*}(y|s)}{\pi^{SFT}(y|s)}\right)+\lambda_{KL}\log Z(s).
(107)
When this analytical expression for the reward is substituted into the Bradley-Terry preference loss from Equation ( 104), the unknown partition function Z  ( s ) Z(s) cancels out. This yields a loss function that depends only on the policy π ϕ \pi_{\phi} being optimized and the fixed reference policy π S  F  T \pi^{SFT} . The DPO objective, given in Equation ( 108), is thus a simple binary cross-entropy loss over policy likelihoods:
ℒ D  P  O  ( ϕ ; π S  F  T ) = − 𝔼 ( s , y w , y l ) ∼ 𝒟  [ log  σ  ( λ K  L  log  π ϕ  ( y w | s ) π S  F  T  ( y w | s ) − λ K  L  log  π ϕ  ( y l | s ) π S  F  T  ( y l | s ) ) ] . \mathcal{L}{DPO}(\phi;\pi^{SFT})=-\mathbb{E}{(s,y_{w},y_{l})\sim\mathcal{D}}\left[\log\sigma\left(\lambda_{KL}\log\frac{\pi_{\phi}(y_{w}|s)}{\pi^{SFT}(y_{w}|s)}-\lambda_{KL}\log\frac{\pi_{\phi}(y_{l}|s)}{\pi^{SFT}(y_{l}|s)}\right)\right].
(108)
This objective is optimized on ϕ \phi using standard supervised learning with a static preference dataset. The gradient increases the likelihood of preferred responses y w y_{w} and decreases the likelihood of dispreferred responses y l y_{l} , relative to the reference policy. 
Figure 21: RLHF versus DPO pipelines. Top row: the three-stage RLHF pipeline trains a reward model from human preferences, then uses PPO to fine-tune the policy with a KL penalty. Bottom row: DPO collapses the pipeline into a single supervised learning objective over preference pairs, eliminating the explicit reward model (ghosted box).
11.7 Recent Developments
A subsequent innovation leverages DPO to create an iterative self-improvement loop, reducing reliance on static, human-annotated data (Yuan et al., 2024) . In this paradigm, dubbed Self-Rewarding Language Models, a single language model acts as both the instruction-following agent and its own reward model. The process begins with a base model fine-tuned to have both instruction-following and evaluation capabilities (“LLM-as-a-Judge”). In each subsequent iteration, the current model generates a new preference dataset for itself by producing multiple responses to a set of prompts and then evaluating its own outputs to assign scores. These scores are used to construct preference pairs ( y w , y l ) (y_{w},y_{l}) , which form an AI-generated feedback dataset. The model is then fine-tuned on this new data using the DPO loss. This iterative process creates a feedback loop where enhancements in instruction-following ability lead to better reward modeling, which in turn fuels the next round of policy optimization.
While RLHF and its successors have proven effective at aligning model behavior with human preferences, several open issues remain. The framework does not aim to solve the identification problem in the strict econometric sense; the learned reward model r θ r_{\theta} (whether explicit or implicit in DPO) is a proxy for preference, not necessarily the uniquely identified “true” utility function required for welfare analysis. 208 208 208 The identification problem in preference learning mirrors that in discrete choice. The reward function is identified only up to an additive constant and requires a location normalization. Furthermore, the notion of “human feedback” is a significant simplification, as the preferences being optimized are those of a small, non-representative group of paid labelers, raising important questions about whose values are being embedded in these systems. Finally, the fine-tuning process can lead to degraded performance on standard academic benchmarks, a phenomenon called the alignment tax (Ouyang et al., 2022) . 209 209 209 The alignment tax, as described by Ouyang et al. ( 2022) , refers to performance regressions on public NLP benchmarks (SQuAD, DROP, HellaSwag) that result from RLHF fine-tuning. Mitigating these challenges while scaling alignment beyond the limits of human data collection remains a key frontier for the field.
11.8 Simulation Study: Preference Learning in Job Search
A worker searches for jobs in a labor market with compensating differentials, following a McCall (1970)-style search model. Each job is characterized by a wage w ∈ { 20 , 28 , 38 , 50 , 65 , 82 , 100 , 125 } w\in{20,28,38,50,65,82,100,125} (thousands) and an amenity level z ∈ { 0 , 1 , … , 6 } z\in{0,1,\ldots,6} capturing commute quality, flexibility, and job security. The state space has 112 states: 56 searching states in which the worker observes a pending offer ( w i , z j ) (w_{i},z_{j}) and decides to accept or reject, plus 56 employed states ( w i , z j ) (w_{i},z_{j}) in which the worker decides to stay or quit. The offer distribution exhibits compensating differentials, with wage rank and amenity rank negatively correlated ( ρ = − 0.74 \rho=-0.74 ): high-wage offers cluster with low amenities and vice versa. The worker's true per-period utility is u  ( w , z ) = α  log  ( w ) + ( 1 − α )  z u(w,z)=\alpha\log(w)+(1-\alpha)z with α = 0.6 \alpha=0.6 , but this function is unobserved; the worker can only compare career trajectories (“I prefer path A to path B”), exactly as in stated-preference surveys in labor economics. While searching, the worker receives the unemployment benefit u b = α  log  ( b ) u_{b}=\alpha\log(b) where b = 28 b=28 . Layoffs occur with probability p = 0.05 p=0.05 per period, and the discount factor is γ = 0.95 \gamma=0.95 . Dynamic programming gives V ∗  ( s 0 ) = 74.13 V^{*}(s_{0})=74.13 ; the optimal policy accepts 25 of 56 offer types and stays employed at 25 of 56 job types. Preference data is generated by rolling out a uniform random policy from a random searching state. Each rollout produces a career segment of L = 15 L=15 periods recording states and actions. For each of K K comparisons, two independent career segments are generated; the segment with higher cumulative discounted utility under the true (unobserved) utility function is labeled as preferred via the Bradley-Terry model. Figure 22 shows the optimal accept/reject and stay/quit boundaries. 
Figure 22: Left: the optimal accept/reject boundary for searching states in wage-amenity space. Right: the optimal stay/quit boundary for employed states. Both boundaries cut diagonally, reflecting the tradeoff between wage and amenity quality under compensating differentials.
Six methods are compared across K ∈ { 25 , 50 , 100 , 200 , 500 , 1 , 000 , 2 , 000 , 5 , 000 } K\in{25,50,100,200,500,1{,}000,2{,}000,5{,}000} , averaged over 30 seeds. The neural network RLHF reward model is a two-layer MLP trained by Bradley-Terry MLE on the K K segment pairs; per-transition rewards are discount-weighted and summed to obtain a segment score, and the resulting 112-state reward table is solved by value iteration. 210 210 210 The neural network has 4 inputs (normalized log-wage, normalized amenity, employment indicator, action), 32 hidden units per layer, and ∼ \sim 1,200 parameters. The logistic loss from Equation ( 104) is applied to discount-weighted segment reward sums. The correctly specified structural model parameterizes utility as u ^ = α ^  log  ( w ) + ( 1 − α ^ )  z \hat{u}=\hat{\alpha}\log(w)+(1-\hat{\alpha})z , estimating the single parameter α ^ \hat{\alpha} via Bradley-Terry MLE, then solves the MDP. The misspecified model uses u ^ = α ^  log  ( w ) + ( 1 − α ^ )  z ¯ \hat{u}=\hat{\alpha}\log(w)+(1-\hat{\alpha})\bar{z} , where z ¯ = 3 \bar{z}=3 is the mean amenity level; this model ignores amenity variation across jobs, treating all amenities as identical. DPO trains a tabular softmax policy directly from trajectory comparisons, bypassing reward modeling entirely. 211 211 211 DPO uses 112 logit parameters ϕ s \phi_{s} , one per state, trained via the DPO loss (Equation 108) with Adam optimization over a sweep of λ K  L ∈ { 0.01 , 0.05 , 0.1 , 0.5 , 1.0 , 5.0 } \lambda_{KL}\in{0.01,0.05,0.1,0.5,1.0,5.0} , selecting the λ K  L \lambda_{KL} that minimizes training loss. The reference policy is uniform: π S  F  T  ( a | s ) = 0.5 \pi^{SFT}(a|s)=0.5 . To match the LLM setup where both completions condition on the same prompt, DPO comparison pairs start from the same initial state. Tabular Q-learning ( 10 , 000 10{,}000 episodes, ε = 0.15 \varepsilon=0.15 , learning rate 0.1 0.1 ) and exact DP provide scalar-reward baselines. All four preference methods receive identical comparison data per seed; DPO receives a same-state variant generated from the same seed. 
Figure 23: Policy value V π  ( s 0 ) V^{\pi}(s_{0}) versus number of preference comparisons K K for all six methods (30 seeds, L = 15 L=15 ). The right axis shows the percentage of DP-optimal value.
Figure 23 reports the main results. Three findings stand out. First, the correctly specified structural model dominates: even at K = 25 K=25 it achieves 99.9% of DP-optimal, illustrating the power of correct specification when the model has a single free parameter. Second, the neural network converges more slowly but reaches 99.9% by K = 5 , 000 K=5{,}000 , reflecting the higher sample complexity of a flexible model relative to a one-parameter structural specification. Third, DPO plateaus at approximately 95% by K = 500 K=500 and does not improve further. 212 212 212 DPO learns only from ( s , a ) (s,a) pairs visited in training trajectories generated by the random behavioral policy. It cannot propagate value to undervisited states the way value iteration does after learning a reward model, so states poorly covered by the behavioral policy remain suboptimal regardless of K K . This plateau is qualitatively different from the gridworld failure ( − 118 % -118% ): DPO recovers a reasonable policy, but the gap does not close with additional data. 213 213 213 DPO fails catastrophically in gridworld because transitions are stochastic (10% slip probability) and rewards are transition-dependent. The same ( s , a ) (s,a) pair yields different rewards depending on whether the agent slipped, so the DPO loss conflates policy quality with transition luck. In the job search model, accept/reject deterministically changes employment status, and only the 5% layoff probability introduces stochastic transitions. The misspecified constant-amenity model plateaus at 91% regardless of K K , because additional preference data cannot correct the omitted variable.
Table 21: Diagnostics at K = 5 , 000 K=5{,}000 (single seed): policy agreement with π ∗ \pi^{*} , value-function correlation, and mean accepted wage and amenity for each method.
Table 21 provides state-level diagnostics at K = 5 , 000 K=5{,}000 . The structural model and neural network achieve near-perfect policy agreement with π ∗ \pi^{*} (100% and 96% respectively). DPO agrees on only 57% of states with value-function correlation 0.78, systematically underselecting on both wage and amenity dimensions. 214 214 214 DPO's mean accepted amenity of 3.4 parallels the misspecified structural model's 3.0, though the mechanisms differ: the misspecified model ignores amenity variation by construction, while DPO underweights amenities because the random behavioral policy underrepresents high-amenity employed states in the training data. The misspecified model agrees on 50%, with disagreements concentrated where amenity variation matters. 215 215 215 An online versus offline ablation for the neural network at K = 1 , 000 K=1{,}000 (20 seeds) shows comparable performance: online 73.92 ± 0.05 73.92\pm 0.05 , offline 73.99 ± 0.03 73.99\pm 0.03 ( p = 0.09 p=0.09 ). The random behavioral policy already provides diverse career trajectories covering the full wage-amenity space. 
Figure 24: Policy value V π  ( s 0 ) V^{\pi}(s_{0}) versus segment length L L at K = 2 , 000 K=2{,}000 for the neural network and DPO (20 seeds). The right axis shows the percentage of DP-optimal value.
Figure 24 reports the segment length ablation at K = 2 , 000 K=2{,}000 . At L = 1 L=1 , both methods perform poorly because single-step comparisons carry minimal information about long-run value. The neural network recovers rapidly (by L = 3 L=3 ) because the reward model aggregates per-transition estimates over longer segments and value iteration propagates them through the full transition structure; DPO improves monotonically but plateaus at its ∼ \sim 95% ceiling, as it must learn the policy directly from trajectory comparisons without access to the transition model.
Two-stage RLHF separates preference estimation (a static econometric problem) from dynamic programming (which exploits the known transition model); DPO conflates the two and forfeits the transition structure that economists typically have access to. 216 216 216 This advantage is specific to settings where the transition model is known or estimable; in domains without a tractable transition model, DPO's single-stage approach avoids compounding errors from reward model estimation.
12 Reinforcement Learning and Causal Inference
Reinforcement learning algorithms solve Markov decision processes by estimating value functions or optimizing policies from sampled transitions. Two assumptions underlie the standard formulation. First, the agent's action at time t t is determined solely by the observed state s t s_{t} and the agent's policy π  ( a ∣ s t ) \pi(a\mid s_{t}) ; there is no unobserved variable (confounder) simultaneously influencing both the action and the reward or state transition. 217 217 217 See Section 2 for the terminological mapping between “outcome” in causal inference and the corresponding RL quantities. Throughout this chapter, I reserve “outcome” for its causal inference meaning and use the specific RL quantity (reward, state, return, value) elsewhere. Second, the observed state s t s_{t} is sufficient for prediction, so that conditioning on s t s_{t} renders future states independent of past history. Both assumptions are the Markov property restated in causal language. Both fail routinely in economic applications.
The preceding chapters operated under a third assumption that was so natural it required no mention: the analyst controls data collection. In the tabular algorithms of Section 4 and the gridworld study of Section 6, each method generated its own trajectories by executing actions in a simulator and observing the consequences. The bandit algorithms of Section 10 chose arms and observed payoffs in real time. Even when exploration was limited, the data-generating process was known because the agent's own policy produced it. This chapter drops that assumption entirely. The analyst receives a fixed log of decisions made by someone else, a behavioral policy μ \mu whose functional form may be unknown and whose action choices may depend on variables the analyst cannot observe. The data are observational in the econometric sense: the analyst had no role in generating them and cannot rerun the experiment under a different policy. Identification, not optimization, becomes the central problem.
Unobserved demand shocks that affect both a retailer's pricing algorithm and consumer demand create endogeneity. The observed correlation between price and demand conflates the causal effect with the confounding effect. An RL agent trained on such observational data converges to a biased policy that systematically overestimates the revenue from high prices.
This chapter formalizes the confounded MDP, develops four identification strategies for recovering interventional quantities from observational data (backdoor adjustment, front-door adjustment, instrumental variables, and proximal causal inference), and demonstrates their practical consequences through a unified simulation study. For comprehensive surveys of the rapidly growing causal RL literature, including causal representation learning, counterfactual policy optimization, transfer, and fairness, I refer readers to Deng et al. ( 2023) and da Costa Cunha et al. ( 2025) .
12.1 From Partial Observability to Causal Structure
Before formalizing confounded MDPs, it is useful to distinguish partial observability from confounding, since both involve hidden variables but create fundamentally different challenges. A partially observable MDP (POMDP) augments the standard MDP with an observation function. The POMDP is defined by the tuple ( 𝒮 , 𝒜 , 𝒪 , P , O , r , γ ) (\mathcal{S},\mathcal{A},\mathcal{O},P,O,r,\gamma) , where 𝒪 \mathcal{O} is a finite observation space and O O is the observation function.
O ( o ∣ s ′ , a ) = P ( O t = o ∣ S t = s ′ , A t − 1 = a ) . O(o\mid s^{\prime},a)=P(O_{t}=o\mid S_{t}=s^{\prime},A_{t-1}=a).
(109)
The agent does not observe s t s_{t} directly but instead receives o t ∼ O ( ⋅ ∣ s t , a t − 1 ) o_{t}\sim O(\cdot\mid s_{t},a_{t-1}) and maintains a belief state b t ∈ Δ  ( 𝒮 ) b_{t}\in\Delta(\mathcal{S})
b t  ( s ) = P  ( S t = s ∣ o 1 , a 1 , … , o t ) , b_{t}(s)=P(S_{t}=s\mid o_{1},a_{1},\ldots,o_{t}),
(110)
which is updated via Bayesian filtering at each step. The belief MDP, whose state space is Δ  ( 𝒮 ) \Delta(\mathcal{S}) , is itself a fully observable (continuous-state) MDP, so standard value iteration applies in principle, though computation is intractable in general.
da Costa Cunha et al. ( 2025) organize sequential decision problems with hidden variables into a hierarchy: standard MDP (full observability, no confounding), POMDP (partial observability, no confounding), confounded MDP (full observability, confounding), and causal POMDP (both). The key distinction is epistemic versus identificational. In a POMDP, the hidden state is a modeling challenge: the agent acknowledges incomplete information and plans accordingly via the belief state, analogous to Kalman or Hamilton filtering in econometrics. In a confounded MDP, the hidden variable is an identification challenge: standard estimators silently produce biased results, analogous to endogeneity and omitted variable bias.
12.2 The Confounded MDP
When unobserved confounders influence both the behavioral policy and the transitions or rewards, the MDP is confounded. This formalization, developed by Zhang and Bareinboim ( 2019) , Zhang and Bareinboim ( 2020) , and Kallus and Zhou ( 2020) , provides the foundation for causal reasoning in sequential decision problems. The key tool is Pearl's do-operator. The interventional distribution P  ( Y ∣ do  ( X = x ) ) P(Y\mid\operatorname{do}(X=x)) is the distribution that arises when X X is set externally rather than observed passively, severing all incoming causal influences on X X while leaving the remaining data-generating process intact. 218 218 218 The do-operator is formalized within the structural causal model (SCM) framework of Pearl ( 2009) . An SCM specifies endogenous variables 𝐕 \mathbf{V} , exogenous variables 𝐔 \mathbf{U} , structural equations V i = f i  ( pa  ( V i ) , U i ) V_{i}=f_{i}(\text{pa}(V_{i}),U_{i}) , and a distribution P  ( 𝐔 ) P(\mathbf{U}) . The intervention do  ( X = x ) \operatorname{do}(X=x) replaces the structural equation for X X with a constant, producing the interventional distribution. See Pearl ( 2009) for the complete framework, including the causal hierarchy (association, intervention, counterfactual) and general identification theory.
Definition D6 (Confounded MDP (Zhang and Bareinboim, 2020) ).
A confounded MDP is a tuple ( 𝒮 , 𝒜 , 𝒰 , P , r , γ ) (\mathcal{S},\mathcal{A},\mathcal{U},P,r,\gamma) where 𝒮 \mathcal{S} is a finite state space, 𝒜 \mathcal{A} is a finite action space, 𝒰 \mathcal{U} is a space of unobserved confounders, γ ∈ [ 0 , 1 ) \gamma\in[0,1) is a discount factor, and the dynamics are governed by structural equations
The behavioral (logging) policy μ \mu depends on the unobserved confounder U t U_{t} through Equation ( 112). An evaluation policy π  ( a ∣ s ) \pi(a\mid s) depends only on the observed state.
Unlike the online algorithms of Sections 4– 6, where behavior and target policies were identical or related by a known exploration mechanism, here μ \mu is an unknown function of unobserved variables.
Because μ \mu depends on U t U_{t} , conditioning on { A t = a } {A_{t}=a} carries information about the confounder, so the observational and interventional transitions diverge:
P  ( s ′ ∣ s , a ) ≠ P  ( s ′ ∣ s , do  ( a ) ) . P(s^{\prime}\mid s,a)\neq P(s^{\prime}\mid s,\operatorname{do}(a)).
(115)
The Bellman equation for policy evaluation must use interventional, not observational, transition probabilities. Define the causal Bellman operator for a target policy π \pi :
Definition D7 (Causal Bellman Operator (Zhang and Bareinboim, 2020) ).
The causal Bellman operator 𝒯 c π \mathcal{T}_{c}^{\pi} for policy π \pi in a confounded MDP is
( 𝒯 c π  V )  ( s ) = ∑ a ∈ 𝒜 π  ( a ∣ s )  ∑ s ′ ∈ 𝒮 P  ( s ′ ∣ s , do  ( a ) )  [ r  ( s , a ) + γ  V  ( s ′ ) ] , (\mathcal{T}{c}^{\pi}V)(s)=\sum{a\in\mathcal{A}}\pi(a\mid s)\sum_{s^{\prime}\in\mathcal{S}}P(s^{\prime}\mid s,\operatorname{do}(a))\bigl[r(s,a)+\gamma V(s^{\prime})\bigr],
(116)
where r  ( s , a ) = 𝔼  [ R t ∣ S t = s , do  ( A t = a ) ] r(s,a)=\mathbb{E}[R_{t}\mid S_{t}=s,\operatorname{do}(A_{t}=a)] is the interventional expected reward.
Lemma L1 (Bias of Naive Off-Policy Evaluation (Kallus and Zhou, 2020) ).
Let V ^ naive π \hat{V}^{\pi}_{\text{naive}} denote the value function obtained by solving the Bellman equation with observational transitions P  ( s ′ ∣ s , a ) P(s^{\prime}\mid s,a) , and let V π V^{\pi} denote the true value function under interventional transitions P  ( s ′ ∣ s , do  ( a ) ) P(s^{\prime}\mid s,\operatorname{do}(a)) . In a confounded MDP where P  ( s ′ ∣ s , a ) ≠ P  ( s ′ ∣ s , do  ( a ) ) P(s^{\prime}\mid s,a)\neq P(s^{\prime}\mid s,\operatorname{do}(a)) for some ( s , a , s ′ ) (s,a,s^{\prime}) , the naive estimator is biased.
V ^ naive π  ( s ) ≠ V π  ( s ) . \hat{V}^{\pi}_{\text{naive}}(s)\neq V^{\pi}(s).
(117)
The importance-sampling estimator V ^ IS π = 1 N  ∑ i = 1 N ∏ t = 0 T π  ( a t ( i ) ∣ s t ( i ) ) μ  ( a t ( i ) ∣ s t ( i ) )  G ( i ) \hat{V}^{\pi}{\text{IS}}=\frac{1}{N}\sum{i=1}^{N}\prod_{t=0}^{T}\frac{\pi(a_{t}^{(i)}\mid s_{t}^{(i)})}{\mu(a_{t}^{(i)}\mid s_{t}^{(i)})}G^{(i)} , where G ( i ) = ∑ t = 0 T γ t  R t ( i ) G^{(i)}=\sum_{t=0}^{T}\gamma^{t}R_{t}^{(i)} is the discounted return of trajectory i i and T T is the trajectory length, is also biased because the propensity μ  ( a ∣ s ) \mu(a\mid s) is not the true behavioral propensity μ  ( a ∣ s , u ) \mu(a\mid s,u) . 219 219 219 This is the sequential analogue of the omitted variable bias in linear regression. In the static case, regressing Y Y on X X without controlling for a confounder U U yields a biased coefficient. In the sequential case, the bias propagates through the Bellman recursion and can amplify over the horizon.
The backdoor criterion (Pearl, 2009) provides a path to identification. Zhang and Bareinboim ( 2020) apply it to the confounded MDP setting.
Theorem 8 (Backdoor Identification in Confounded MDPs (Pearl, 2009; Zhang and Bareinboim, 2020) ).
Suppose a set of observed variables 𝐙 t \mathbf{Z}{t} satisfies the backdoor criterion relative to ( A t , S t + 1 ) (A{t},S_{t+1}) in the causal graph of the confounded MDP, meaning that 𝐙 t \mathbf{Z}{t} blocks all backdoor paths from A t A{t} to
S
t
1
S_{t+1}
and no element of
𝐙
t
\mathbf{Z}_{t}
is a descendant of
A
t
A_{t}
. 220 220
220
A backdoor path from
A
t
A_{t}
to
S
t
1
S_{t+1}
is any path in the causal graph that begins with an arrow into
A
t
A_{t}
(i.e., a non-causal path). In the confounded MDP,
A
t
←
U
t
→
S
t
1
A_{t}\leftarrow U_{t}\rightarrow S_{t+1}
is a backdoor path:
U
t
U_{t}
causes both
A
t
A_{t}
and
S
t
1
S_{t+1}
, creating a spurious association. Blocking all such paths by conditioning on appropriate variables eliminates the confounding bias. See
Pearl
(
2009
)
, Chapter 3.
Then the interventional transition probability is identified:
P
(
s
′
∣
s
,
do
(
a
)
)
=
∑
𝐳
P
(
s
′
∣
s
,
a
,
𝐳
)
P
(
𝐳
∣
s
)
.
P(s^{\prime}\mid s,\operatorname{do}(a))=\sum_{\mathbf{z}}P(s^{\prime}\mid s,a,\mathbf{z}),P(\mathbf{z}\mid s).
(118)
Substituting Equation (
118
) into the causal Bellman operator (Equation
116
) yields an identified, consistent estimator of
V
π
V^{\pi}
.
12.3 Backdoor-Adjusted Off-Policy Evaluation
Off-policy evaluation under confounding is an average treatment effect estimation problem in a dynamic setting
(Bannon et al.,
2020
)
:
μ
\mu
is the treatment assignment mechanism,
π
\pi
the counterfactual regime, importance sampling corresponds to inverse probability weighting, and doubly robust OPE corresponds to the AIPW estimator of
Robins et al. (
1994
)
.
Theorem
8
yields a concrete estimation procedure. Given logged data
{
(
s
t
,
a
t
,
z
t
,
r
t
,
s
t
1
)
}
t
=
1
N
{(s_{t},a_{t},z_{t},r_{t},s_{t+1})}_{t=1}^{N}
collected under behavioral policy
μ
\mu
, where
z
t
z_{t}
is an observed proxy for the confounder.
Estimate the conditional transition model P ^  ( s ′ ∣ s , a , z ) \hat{P}(s^{\prime}\mid s,a,z) and the proxy distribution P ^  ( z ∣ s ) \hat{P}(z\mid s) from the logged data.
Compute interventional transitions via the backdoor adjustment: P ^  ( s ′ ∣ s , do  ( a ) ) = ∑ z P ^  ( s ′ ∣ s , a , z )  P ^  ( z ∣ s ) . \hat{P}(s^{\prime}\mid s,\operatorname{do}(a))=\sum_{z}\hat{P}(s^{\prime}\mid s,a,z),\hat{P}(z\mid s). (119)
Solve the causal Bellman equation (Definition D7 ) using the estimated interventional transitions to obtain V ^ π \hat{V}^{\pi} .
The doubly robust variant combines the fitted action-value function
Q
^
(
s
,
a
)
\hat{Q}(s,a)
(the RL analogue of the econometric outcome model) with backdoor-adjusted propensities, achieving consistency if either
Q
^
\hat{Q}
or the propensity model is correctly specified.
12.4 Alternative Identification Strategies
When no backdoor variable is available, three alternative identification strategies apply, each with a direct econometric analogue. Figure
25
displays the causal graph for each. 
Figure 25:
Causal graphs for three identification strategies in confounded MDPs. Gray dashed nodes are unobserved; dashed edges involve unobserved variables. (a) Front-door criterion with mediator
M
t
M_{t}
. (b) Instrumental variables with exogenous instrument
Z
t
Z_{t}
. (c) Proximal causal inference with proxies
W
t
(
1
)
,
W
t
(
2
)
W_{t}^{(1)},W_{t}^{(2)}
.
12.4.1 Front-Door Criterion
The front-door criterion applies when
A
t
A_{t}
affects
S
t
1
S_{t+1}
only through an observed mediator
M
t
M_{t}
. Three conditions are required: (i)
M
t
M_{t}
intercepts all directed paths from
A
t
A_{t}
to
S
t
1
S_{t+1}
, (ii) no unblocked backdoor path exists from
A
t
A_{t}
to
M
t
M_{t}
, and (iii)
A
t
A_{t}
blocks all backdoor paths from
M
t
M_{t}
to
S
t
1
S_{t+1}
. When satisfied
(Pearl,
2009
)
:
P
(
s
′
∣
s
,
do
(
a
)
)
=
∑
m
P
(
m
∣
a
)
∑
a
′
P
(
s
′
∣
s
,
m
,
a
′
)
P
(
a
′
∣
s
)
.
P(s^{\prime}\mid s,\operatorname{do}(a))=\sum_{m}P(m\mid a)\sum_{a^{\prime}}P(s^{\prime}\mid s,m,a^{\prime}),P(a^{\prime}\mid s).
(120)
The first factor is unconfounded; the inner sum adjusts for confounding on the
M
t
→
S
t
1
M_{t}\to S_{t+1}
link by averaging over the observational action distribution. This is the sequential analogue of mediation analysis
(da Costa Cunha et al.,
2025
)
.
The causal RL survey of
da Costa Cunha et al. (
2025
)
illustrates the front-door criterion with a mobile wellness intervention. A health app (action
A
t
A_{t}
) aims to reduce patient cortisol levels (outcome
S
t
1
S_{t+1}
), but unobserved health consciousness
U
t
U_{t}
confounds the relationship because health-conscious individuals are both more likely to adopt the app and more likely to have low cortisol regardless. The app affects cortisol only through an observed mediator, supplement adherence
M
t
M_{t}
. Applying Equation (
120
) recovers the causal effect without observing health consciousness.
12.4.2 Instrumental Variables
When neither backdoor nor front-door variables are available, instrumental variable methods can identify causal effects. An instrument
Z
t
Z_{t}
must satisfy two conditions: it affects the action
A
t
A_{t}
(relevance) and its effect on
S
t
1
S_{t+1}
is channeled entirely through
A
t
A_{t}
(exclusion restriction).
Liao et al. (
2024
)
formalize this as a Confounded MDP with Instrumental Variables (CMDP-IV), where transitions take the form
S
t
1
=
F
∗
(
S
t
,
A
t
)
ϵ
t
S_{t+1}=F^{*}(S_{t},A_{t})+\epsilon_{t}
with unobserved confounders
ϵ
t
\epsilon_{t}
affecting both the behavior policy and transitions. The transition function
F
∗
F^{*}
is recovered from a conditional moment restriction:
𝔼
[
S
t
1
−
F
∗
(
S
t
,
A
t
)
∣
Z
t
,
S
t
]
=
0
.
\mathbb{E}[S_{t+1}-F^{*}(S_{t},A_{t})\mid Z_{t},S_{t}]=0.
(121)
For a binary action and binary instrument, the Wald estimator provides a closed-form solution. Let
β
\beta
denote the causal effect of promoting (action
a
=
0
a=0
) on the transition probability.
β
=
P
(
s
′
∣
s
,
Z
=
1
)
−
P
(
s
′
∣
s
,
Z
=
0
)
P
(
A
=
0
∣
s
,
Z
=
1
)
−
P
(
A
=
0
∣
s
,
Z
=
0
)
,
\beta=\frac{P(s^{\prime}\mid s,Z{=}1)-P(s^{\prime}\mid s,Z{=}0)}{P(A{=}0\mid s,Z{=}1)-P(A{=}0\mid s,Z{=}0)},
(122)
where the numerator is the reduced-form effect of the instrument on the transition and the denominator is the first-stage effect on treatment uptake. The interventional transition is then recovered from any instrument value
z
z
via
P
(
s
′
∣
s
,
do
(
a
=
0
)
)
=
P
(
s
′
∣
s
,
Z
=
z
)
β
⋅
(
1
−
P
(
A
=
0
∣
s
,
Z
=
z
)
)
P(s^{\prime}\mid s,\operatorname{do}(a{=}0))=P(s^{\prime}\mid s,Z{=}z)+\beta\cdot(1-P(A{=}0\mid s,Z{=}z))
. Their IV-aided Value Iteration algorithm applies this moment restriction at each state to estimate
F
∗
F^{*}
, then runs standard value iteration on the estimated model.
Liao et al. (
2024
)
illustrate with neonatal intensive care unit (NICU) assignment. A hospital must decide whether to admit each newborn to the NICU (action
A
t
A_{t}
), and this decision is confounded by unobserved severity indicators that affect both the admission decision and the infant's health trajectory. Differential travel time from the hospital to a specialty care provider serves as an instrument
Z
t
Z_{t}
. Relevance holds because longer travel times discourage NICU referrals, shifting the admission probability. The exclusion restriction holds because travel time affects infant health outcomes only through the admission decision, not directly. The conditional moment restriction (Equation
121
) uses variation in travel time across hospitals to trace out the causal effect of NICU admission on health transitions, recovering the transition function
F
∗
F^{*}
that standard regression conflates with the unobserved confounder.
12.4.3 Proximal Causal Inference
When confounders are truly latent but proxy variables, noisy correlates of the confounder, are available, proximal causal inference provides identification.
Bennett and Kallus (
2021
)
adapt this to sequential settings. The analyst observes two proxies: a treatment-side proxy
W
t
(
1
)
W_{t}^{(1)}
and an outcome-side proxy
W
t
(
2
)
W_{t}^{(2)}
, both conditionally independent given the latent confounder
U
t
U_{t}
. Identification proceeds through a bridge function
h
h
that solves a conditional moment equation linking the two proxies to the interventional quantity:
𝔼
[
V
(
S
t
1
)
∣
W
t
(
1
)
,
S
t
,
A
t
]
=
𝔼
[
h
(
W
t
(
2
)
,
S
t
,
A
t
)
∣
W
t
(
1
)
,
S
t
,
A
t
]
.
\mathbb{E}[V(S_{t+1})\mid W_{t}^{(1)},S_{t},A_{t}]=\mathbb{E}[h(W_{t}^{(2)},S_{t},A_{t})\mid W_{t}^{(1)},S_{t},A_{t}].
(123)
The bridge function
h
h
is estimated by solving this integral equation (which reduces to a linear system in the discrete case), and the causal effect is recovered by marginalizing over the outcome proxy distribution.
P
(
s
′
∣
s
,
do
(
a
)
)
=
∑
w
2
h
(
w
2
,
s
,
a
)
P
(
W
(
2
)
=
w
2
∣
s
)
.
P(s^{\prime}\mid s,\operatorname{do}(a))=\sum_{w_{2}}h(w_{2},s,a),P(W^{(2)}{=}w_{2}\mid s).
(124)
Two bridge functions, analogous to inverse propensity scores and Q-functions, yield a doubly robust estimator of the policy value that is
n
\sqrt{n}
-consistent without ever observing
U
t
U_{t}
.
Bennett and Kallus (
2021
)
demonstrate with a sepsis management simulator in which physicians choose among fluids, vasopressors, and antibiotics at each decision point. The patient's diabetes status is the latent confounder, partially censored in the medical record so that 20% of diabetic patients appear as non-diabetic in the data. Because the physician observes the true diabetes status when prescribing but the analyst's dataset contains the censored version, the behavioral policy depends on a variable the analyst cannot fully recover. Previous clinical observations
O
t
−
1
O_{t-1}
(prior lab values and vitals) serve as the treatment-side proxy
W
t
(
1
)
W_{t}^{(1)}
because they correlate with diabetes status and influence the physician's current prescribing. Current clinical observations
O
t
O_{t}
serve as the outcome-side proxy
W
t
(
2
)
W_{t}^{(2)}
because they reflect diabetes status and predict future health transitions. In their experiments, the proximal estimator correctly identified which evaluation policy improved over the behavioral policy in 82–100% of test cases, while naive estimators that ignored confounding and standard MDP estimators that assumed full observability both achieved 0% accuracy.
12.5 The Broader Causal RL Landscape
Three active research directions beyond confounded MDPs illustrate the broader scope of causal RL.
Causal representation learning for RL seeks state representations
ϕ
(
s
)
\phi(s)
that capture causal mechanisms rather than spurious correlations
(Schölkopf et al.,
2021
)
.
da Costa Cunha et al. (
2025
)
formalize this as invariant policy optimization within a multi-environment MDP framework. In sim-to-real robotics, training across multiple visually distinct simulators (same physics, different rendering) forces the representation to discard renderer-specific features and retain only causally relevant ones like object pose and joint angles.
Counterfactual policy optimization uses structural causal models to generate “what-if” trajectories for credit assignment and data augmentation.
Buesing et al. (
2019
)
introduce Gumbel-Max SCMs that produce counterfactual rollouts from a single observed trajectory via Pearl's Abduction-Action-Prediction procedure
(Pearl,
2009
)
: infer the exogenous noise explaining the observed trajectory, replace the logged action, and propagate through the structural equations. By replaying a trajectory with one action changed while holding the environment's randomness fixed, any difference in reward is attributable to that action, solving long-horizon credit assignment without importance sampling.
Oberst and Sontag (
2019
)
extend this to healthcare settings, while
Forney et al. (
2017
)
use counterfactual data-fusion to augment online exploration.
Causal transfer in RL applies the transportability theory of
Pearl and Bareinboim (
2014
)
and
Bareinboim and Pearl (
2016
)
to policy transfer across domains. Selection diagrams identify which mechanisms are shared across environments and which differ, enabling targeted recalibration rather than wholesale domain adaptation. In sim-to-real autonomous driving, physical dynamics transfer directly while visual rendering requires recalibration with scarce real-world data
(Bareinboim and Pearl,
2016
)
.
12.6 Simulation Study: Confounded Retail Pricing MDP
I construct a 5-state engagement funnel
𝒮
=
{
0
,
1
,
2
,
3
,
4
}
\mathcal{S}={0,1,2,3,4}
with two actions (promote, hold price) and an absorbing conversion state at
s
=
4
s=4
. A retailer manages customers through engagement stages, deciding whether to offer a promotional discount. The data-generating process embeds four distinct sources of causal variation, enabling simultaneous validation of all four identification strategies from a single DGP.
Figure
26
displays the complete causal graph. Market conditions
Z
t
∼
Bernoulli
(
0.5
)
Z_{t}\sim\text{Bernoulli}(0.5)
are observed and affect both the latent confounder and transitions. Consumer sentiment
U
t
U_{t}
is an unobserved confounder strongly correlated with
Z
t
Z_{t}
. 221 221
221
P
(
U
t
=
1
∣
Z
t
=
1
)
=
0.9
P(U_{t}{=}1\mid Z_{t}{=}1)=0.9
and
P
(
U
t
=
1
∣
Z
t
=
0
)
=
0.1
P(U_{t}{=}1\mid Z_{t}{=}0)=0.1
.
An independent cost shock
IV
t
∼
Bernoulli
(
0.5
)
\text{IV}_{t}\sim\text{Bernoulli}(0.5)
serves as an instrument. The behavioral pricing policy depends on both
U
t
U_{t}
and
IV
t
\text{IV}_{t}
:
μ
(
promote
∣
s
,
U
t
,
IV
t
)
=
0.55
ρ
⋅
0.25
⋅
(
2
U
t
−
1
)
0.15
⋅
(
IV
t
−
0.5
)
\mu(\text{promote}\mid s,U_{t},\text{IV}{t})=0.55+\rho\cdot 0.25\cdot(2U{t}-1)+0.15\cdot(\text{IV}_{t}-0.5)
, where
ρ
∈
{
0
,
0.2
,
…
,
1.0
}
\rho\in{0,0.2,\ldots,1.0}
controls confounding strength. Promotions trigger marketing follow-ups with
M
t
M_{t}
serving as a mediator. 222 222
222
M
t
∼
Bernoulli
(
0.8
)
M_{t}\sim\text{Bernoulli}(0.8)
when the retailer promotes and
Bernoulli
(
0.2
)
\text{Bernoulli}(0.2)
otherwise.
Two noisy proxies of
U
t
U_{t}
are available: a CRM score
W
t
(
1
)
W_{t}^{(1)}
and browsing behavior
W
t
(
2
)
W_{t}^{(2)}
. 223 223
223
W
t
(
1
)
∼
Bernoulli
(
0.85
⋅
U
t
0.15
⋅
(
1
−
U
t
)
)
W_{t}^{(1)}\sim\text{Bernoulli}(0.85\cdot U_{t}+0.15\cdot(1-U_{t}))
and
W
t
(
2
)
∼
Bernoulli
(
0.75
⋅
U
t
0.25
⋅
(
1
−
U
t
)
)
W_{t}^{(2)}\sim\text{Bernoulli}(0.75\cdot U_{t}+0.25\cdot(1-U_{t}))
. 
Figure 26:
Complete causal graph of the simulation DGP. Gray dashed node (
U
t
U_{t}
) is unobserved; dashed edges involve
U
t
U_{t}
.
The action affects the next state only through the mediator:
P
(
s
1
∣
s
,
M
t
,
Z
t
)
P(s{+}1\mid s,M_{t},Z_{t})
depends on
M
t
M_{t}
and
Z
t
Z_{t}
but not on
A
t
A_{t}
or
U
t
U_{t}
directly. This enables all four identification strategies simultaneously:
Z
t
Z_{t}
satisfies the backdoor criterion,
M
t
M_{t}
satisfies the front-door criterion,
IV
t
\text{IV}_{t}
satisfies relevance and exclusion, and
W
t
(
1
)
,
W
t
(
2
)
W_{t}^{(1)},W_{t}^{(2)}
satisfy the proximal conditions. 224 224
224
Rewards are
r
(
s
,
a
)
=
−
1
r(s,a)=-1
for
s
<
4
s<4
,
γ
=
0.9
\gamma=0.9
. The target policy always promotes. The true interventional transition probability is
P
(
s
1
∣
s
,
do
(
promote
)
)
=
0.615
P(s{+}1\mid s,\operatorname{do}(\text{promote}))=0.615
.
I compare six estimators: oracle, naive (biased per Lemma
L1
), backdoor (Equation
119
), front-door (Equation
120
), Wald IV (Equation
122
), and proximal (Equations
123
–
124
). 225 225
225
Each configuration uses 2,000 trajectories averaged over 20 seeds.
Figure
27
reports bias and RMSE across confounding strengths (20 seeds, 2,000 trajectories per seed). The naive estimator's bias grows monotonically with
ρ
\rho
because observational transitions overestimate promotion success: the promote action is more likely when
U
t
=
1
U_{t}=1
, which correlates with favorable conditions, so
P
^
obs
\hat{P}_{\text{obs}}
exceeds the true interventional probability, and this per-step bias compounds through the Bellman recursion. The backdoor and front-door estimators eliminate bias at all
ρ
\rho
, validating Theorem
8
and Equation (
120
). The IV estimator maintains low bias but higher variance due to the Wald ratio's sensitivity to instrument strength; panel (c) illustrates this classic bias-variance tradeoff. The proximal estimator achieves low bias with moderate variance, confirming that bridge functions recover causal effects from noisy proxies. 
Figure 27:
(a) Bias of five OPE estimators as a function of confounding strength
ρ
\rho
. (b) RMSE of five estimators as a function of
ρ
\rho
. (c) IV estimator bias distribution vs. instrument strength at
ρ
=
1
\rho=1
; dashed red line is naive estimator bias.
13 Discussion
This concluding section develops concrete research agendas at the intersection of reinforcement learning and economics as well as lists the bottlenecks and open challenges.
13.1 How Economics Improves Reinforcement Learning
Reinforcement learning's most celebrated successes, from Atari to Go to protein folding, share a common ingredient: a cheap, fast, and accurate simulator that generates unlimited training data. Economics largely lacks this ingredient. Every application in Section
7
demanded a custom environment, and the engineering cost of building these environments often dominated the cost of training the RL agent itself. Economics is, however, uniquely positioned to fill this gap. Economic models encode variable selection, causal structure, and institutional constraints that determine how agents respond to interventions. The Lucas critique warns that correlational simulators, trained on observational data without structural assumptions, will break under policy changes (Section
12
). Building economic simulators that respect causal identification and correctly model agent responses to rule changes is an important problem.
A recurring theme across the survey is that economic structure, when available, can dramatically reduce the sample complexity of learning. The knowledge ladder in Section
10
shows that imposing demand structure on a pricing problem can reduce cumulative regret from
Θ
(
T
)
\Theta(T)
to
O
(
log
T
)
O(\log T)
. The pattern extends beyond bandits: structural assumptions yield similar gains in dynamic estimation (Section
8
) and preference learning (Section
11
). These reflect the difference between learning in an unstructured space and learning in one shaped by economic theory. Formalizing this intuition, identifying which structural assumptions yield which complexity reductions and under what conditions, is an active research frontier.
The RLHF and DPO frameworks studied in Section
11
rely on the Bradley-Terry model, one of the simplest members of the discrete choice family. Economics offers a rich toolkit for moving beyond it. Mixed logit models accommodate heterogeneous preferences across annotators. Revealed preference theory provides axiomatic consistency constraints, such as GARP and stochastic transitivity, that can serve as regularizers on learned reward models. The preference learning simulation in Section
11
illustrates the cost of misspecification (Figure
23
). Integrating econometric tools for preference elicitation, model selection, and specification testing into the RLHF pipeline is a natural direction.
13.2 How Reinforcement Learning Advances Economics
Dynamic programming has always offered economics a prescriptive capability: given a model, compute the optimal policy. In practice, this capability has been limited by the curse of dimensionality to models with small, discrete state spaces. RL relaxes this constraint. TD-based methods make structural models tractable at state-space scales where NFXP is infeasible (Section
8
), and real-world deployments confirm that RL can compute policies of practical value (Section
7
). These results suggest a prescriptive role for RL in economics: not merely estimating model parameters (the traditional econometric task), but computing the policies those parameters imply.
Social science and policy research work with vast quantities of observational data from settings where controlled experimentation is impossible or unethical. Offline RL, which learns policies from logged data without further interaction, is a natural fit. The simulation in Section
11
illustrates both the promise and the limits: algorithms with distributional shift correction exceed the behavioral baseline, while those without it degrade below it, and performance depends critically on data support (Table
20
, Figure
20
). This means that offline RL is not a black box that extracts optimal policies from any observational dataset. It is a framework with clearly delineated conditions under which learning is possible, conditions that connect directly to familiar econometric concepts like overlap and common support. Developing standardized benchmarks and digital twins for economic offline RL can enable firms and policy-makers to design optimal policies from data generated under old ones.
RL also offers a descriptive model of how boundedly rational agents learn in economic environments. The simulations in Section
9
demonstrate that independent Q-learning agents converge to Nash equilibrium through trial and error, providing “as-if” microfoundations for equilibrium concepts: the equilibrium arises not from common knowledge of rationality, but from a simple adaptive process.
When RL-trained agents are actually deployed in markets, they become economic actors subject to empirical scrutiny. Algorithmic pricing agents, for instance, have been shown to sustain supra-competitive prices through reward-based learning without explicit communication. This is not a speculative concern; competition authorities in the EU, US, and UK are actively investigating whether algorithmic coordination constitutes tacit collusion. 226 226
226
The companion thesis
(Rawat,
2026
)
develops a framework for evaluating algorithmic inefficiency and collusion risk in algorithmically mediated markets, combining simulators with factorial experimental designs.
As algorithmic agents proliferate in pricing, trading, content recommendation, and resource allocation, the empirical study of machine behavior using economic tools becomes an increasingly important research program.
13.3 Open Challenges
For researchers accustomed to estimators with well-characterized asymptotic properties, the deadly triad represents a significant barrier to adoption. Deep RL algorithms exhibit seed sensitivity, overestimation cascades, and plasticity loss that make reproducibility difficult even in controlled settings (Section
6
).
Multi-agent RL faces fundamental problems (Section
9
). Computing Nash equilibria is PPAD-complete, and RL does not escape this hardness. In economic games with multiple equilibria, agents performing Bellman backups may select different equilibria for different states, causing value iteration to cycle or diverge. The literature on equilibrium refinement, focal points, and coordination mechanisms may offer partial resolutions, but a general solution remains open.
The absence of standardized economic simulators is part of a broader infrastructure gap. Industrial RL deployments require dedicated engineering teams, GPU clusters, and months of hyperparameter tuning (Section
7
, Section
6
). Reducing these barriers through shared simulation environments and accessible software libraries would accelerate adoption.
13.4 Conclusion
Reinforcement learning is a welcome addition to the economist's toolkit but is not a replacement for existing methods. It extends the reach of dynamic programming to problems that were previously intractable, and it connects naturally to econometric frameworks through shared mathematical foundations. The research agendas outlined above, from building economic simulators to formalizing the role of structural assumptions in sample complexity to developing inference procedures for learned policies, are concrete and tractable. Progress on them will require sustained collaboration between the two fields, drawing on economics for “structure” and institutional context and on RL for computation.
References
Adusumilli et al. (2022) S. Adusumilli, M. Eckardt, and G. Tate. Estimation of dynamic discrete choice models with differentiable temporal-difference learning. arXiv preprint arXiv:2209.15174 , 2022.
Agarwal et al. (2020a) Alekh Agarwal, Sham Kakade, and Lin F. Yang. Model-based reinforcement learning with a generative model is minimax optimal. In Conference on Learning Theory (COLT) , 2020a.
Agarwal et al. (2021a) Alekh Agarwal, Sham M. Kakade, Jason D. Lee, and Gaurav Mahajan. On the theory of policy gradient methods: Optimality, approximation, and distribution shift. Journal of Machine Learning Research , 22(98), 2021a.
Agarwal et al. (2020b) Rishabh Agarwal, Dale Schuurmans, and Mohammad Norouzi. An optimistic perspective on offline reinforcement learning. In International Conference on Machine Learning (ICML) , 2020b.
Agarwal et al. (2021b) Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, and Marc G. Bellemare. Deep reinforcement learning at the edge of the statistical precipice. In Advances in Neural Information Processing Systems , volume 34, 2021b.
Agrawal and Tang (2024) Shipra Agrawal and Wei Tang. Dynamic pricing with reference price effects. arXiv preprint arXiv:2301.02497 , 2024.
Almgren and Chriss (2001) Robert Almgren and Neil Chriss. Optimal execution of portfolio transactions. Journal of Risk , 3(2):5–40, 2001.
Amari (1998) Shun-ichi Amari. Natural gradient works efficiently in learning. Neural Computation , 10(2):251–276, 1998.
Andrychowicz et al. (2021) Marcin Andrychowicz, Anton Raichuk, Piotr Stańczyk, Manu Orsini, Sertan Girgin, Raphael Marinier, Leonard Hussenot, Matthieu Geist, Olivier Pietquin, Marcin Michalski, Sylvain Gelly, and Olivier Bachem. What matters for on-policy deep actor-critic methods? a large-scale study. In Proceedings of the International Conference on Learning Representations (ICLR) , 2021.
Antos et al. (2008) András Antos, Csaba Szepesvári, and Rémi Munos. Learning near-optimal policies with Bellman-residual minimization based fitted policy iteration and a single sample path. Machine Learning , 71(1):89–129, 2008. doi: 10.1007/s10994-007-5038-2 .
Arcidiacono and Miller (2011) Peter Arcidiacono and Robert A. Miller. Conditional choice probability estimation of dynamic discrete choice models with unobserved heterogeneity. Econometrica , 79(6):1823–1867, 2011.
Asker et al. (2020) John Asker, Chaim Fershtman, Jihye Jeon, and Ariel Pakes. A computational framework for analyzing dynamic auctions: The market impact of information sharing. The RAND Journal of Economics , 51(3):805–839, 2020.
Atashbar and Shi (2022) Tohid Atashbar and Rui Aruhan Shi. Deep reinforcement learning: Emerging trends in macroeconomics and future prospects. Working Paper 2022/259, International Monetary Fund, 2022.
Atashbar and Shi (2023) Tohid Atashbar and Shuping Shi. Solving macroeconomic models with deep reinforcement learning. Journal of Economic Dynamics and Control , 2023.
Auer et al. (2002a) Peter Auer, Nicolo Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit problem. Machine Learning , 47(2):235–256, 2002a.
Auer et al. (2002b) Peter Auer, Nicolò Cesa-Bianchi, Yoav Freund, and Robert E. Schapire. The nonstochastic multiarmed bandit problem. SIAM Journal on Computing , 32(1):48–77, 2002b.
Azar et al. (2013) Mohammad Gheshlaghi Azar, Rémi Munos, and Hilbert J Kappen. Minimax pac bounds on the sample complexity of reinforcement learning with a generative model. Machine Learning , 91(1):7–32, 2013.
Badanidiyuru et al. (2013) Ashwinkumar Badanidiyuru, Robert Kleinberg, and Aleksandrs Slivkins. Bandits with knapsacks. IEEE 54th Annual Symposium on Foundations of Computer Science , pages 207–216, 2013.
Baird (1995) Leemon Baird. Residual algorithms: Reinforcement learning with function approximation. In Proceedings of the Twelfth International Conference on Machine Learning , pages 30–37. Morgan Kaufmann, 1995.
Bannon et al. (2020) James Bannon, Brad Langlois, Raimundo Fernandez, and Danielle Maddix. Causality and batch reinforcement learning: Complementary approaches to planning in unknown domains. In NeurIPS Workshop on Causal Discovery and Causality-Inspired Machine Learning , 2020.
Bareinboim and Pearl (2016) Elias Bareinboim and Judea Pearl. Causal inference and the data-fusion problem. Proceedings of the National Academy of Sciences , 113(27):7345–7352, 2016.
Barto et al. (1983) Andrew G. Barto, Richard S. Sutton, and Charles W. Anderson. Neuronlike adaptive elements that can solve difficult learning control problems. IEEE Transactions on Systems, Man, and Cybernetics , SMC-13(5):834–846, 1983.
Bellman (1957) Richard Bellman. Dynamic Programming . Princeton University Press, 1957.
Bennett and Kallus (2021) Andrew Bennett and Nathan Kallus. Proximal reinforcement learning: Efficient off-policy evaluation in partially observed Markov decision processes. Operations Research , 2021.
Bertsekas (1996) Dimitri P. Bertsekas. Dynamic Programming and Optimal Control . Athena Scientific, 1996.
Bertsekas (2021) Dimitri P. Bertsekas. Lessons from AlphaZero for optimal, model predictive, and adaptive control. Athena Scientific Reports , 2021.
Bertsekas (2022a) Dimitri P. Bertsekas. Abstract Dynamic Programming . Athena Scientific, Belmont, MA, 3rd edition, 2022a.
Bertsekas (2022b) Dimitri P. Bertsekas. Newton's method for reinforcement learning and model predictive control. Results in Control and Optimization , 7:100121, 2022b.
Bertsekas and Tsitsiklis (1996) Dimitri P. Bertsekas and John N. Tsitsiklis. Neuro-Dynamic Programming . Athena Scientific, Belmont, MA, 1996.
Bhandari et al. (2021) Jalaj Bhandari, Daniel Russo, and Raghav Singal. A finite time analysis of temporal difference learning with linear function approximation. Operations Research , 69(3), 2021.
Blackwell (1965) David Blackwell. Discounted dynamic programming. Annals of Mathematical Statistics , 36(1):226–235, 1965.
Börgers and Sarin (1997) Tilman Börgers and Rajiv Sarin. Learning through reinforcement and replicator dynamics. Journal of Economic Theory , 77(1):1–14, 1997.
Borkar (1997) Vivek S. Borkar. Stochastic approximation with two time scales. Systems & Control Letters , 29(5):291–294, 1997.
Borkar and Meyn (2000) Vivek S. Borkar and Sean P. Meyn. The ODE method for convergence of stochastic approximation and reinforcement learning. SIAM Journal on Control and Optimization , 38(2):447–469, 2000.
Bowling and Veloso (2002) Michael Bowling and Manuela Veloso. Multiagent learning using a variable learning rate. Artificial Intelligence , 136(2):215–250, 2002.
Bowling et al. (2015) Michael Bowling, Neil Burch, Michael Johanson, and Oskari Tammelin. Heads-up limit hold'em poker is solved. Science , 347(6218):145–149, 2015.
Bradley and Terry (1952) Ralph Allan Bradley and Milton E. Terry. Rank analysis of incomplete block designs: I. The method of paired comparisons. Biometrika , 39(3/4):324–345, 1952.
Brero et al. (2021) Gianluca Brero, Alon Eden, Matthias Gerstgrasser, David C. Parkes, and Duncan Rheingans-Yoo. Reinforcement learning of sequential price mechanisms. In Proceedings of the AAAI Conference on Artificial Intelligence , volume 35, pages 13662–13670, 2021.
Brock and Mirman (1972) William A. Brock and Leonard J. Mirman. Optimal economic growth and uncertainty: The discounted case. Journal of Economic Theory , 4(3):479–513, 1972.
Broder and Rusmevichientong (2012) Josef Broder and Paat Rusmevichientong. Dynamic pricing under a general parametric choice model. Operations Research , 60(4):965–980, 2012.
Brown (1951) George W. Brown. Iterative solution of games by fictitious play, 1951.
Brown and Sandholm (2018) Noam Brown and Tuomas Sandholm. Superhuman ai for heads-up no-limit poker: Libratus beats top professionals. Science , 359(6374):418–424, 2018.
Brown and Sandholm (2019) Noam Brown and Tuomas Sandholm. Superhuman ai for multiplayer poker. Science , 365(6456):885–890, 2019.
Brown et al. (2019) Noam Brown, Adam Lerer, Sam Gross, and Tuomas Sandholm. Deep counterfactual regret minimization. In Proceedings of the 36th International Conference on Machine Learning (ICML) , volume 97, pages 793–802. PMLR, 2019.
Buesing et al. (2019) Lars Buesing, Theophane Weber, Yori Zwols, Sebastien Racaniere, Arthur Guez, Jean-Baptiste Lespiau, and Nicolas Heess. Woulda, coulda, shoulda: Counterfactually-guided policy search. In International Conference on Learning Representations , 2019.
Bulow (1982) Jeremy I. Bulow. Durable-goods monopolists. Journal of Political Economy , 90(2):314–332, 1982.
Cai et al. (2023) Junhui Cai, Ran Chen, Martin J. Wainwright, and Linda Zhao. Doubly high-dimensional contextual bandits: An interpretable model for joint assortment-pricing. arXiv preprint arXiv:2309.07956 , 2023.
Calvano et al. (2020) Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolò, and Sergio Pastorello. Artificial intelligence, algorithmic pricing, and collusion. American Economic Review , 110(10):3267–3297, 2020.
Cen et al. (2022) Shicong Cen, Chen Cheng, Yuxin Chen, Yuting Wei, and Yuejie Chi. Fast global convergence of natural policy gradient methods with entropy regularization. Operations Research , 70(4), 2022.
Chen et al. (2023) Ji Chen, Yifan Xu, Peiwen Yu, and Jun Zhang. A reinforcement learning approach for hotel revenue management with evidence from field experiments. Journal of Operations Management , 69(7):1176–1201, 2023. doi: 10.1002/joom.1246 .
Chen et al. (2025) Yuxin Chen, Jieming Mao, and Rui Miao. Dynamic pricing with fairness constraints. arXiv preprint arXiv:2402.07834 , 2025.
Christiano et al. (2017) Paul F. Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. In Advances in Neural Information Processing Systems , volume 30, 2017.
Ciosek et al. (2019) Kamil Ciosek, Quan Vuong, Robert Lierowski, and Katja Hofmann. Better exploration with optimistic actor-critic. In Advances in Neural Information Processing Systems , volume 32, 2019.
Clark and Scarf (1960) Andrew J. Clark and Herbert Scarf. Optimal policies for a multi-echelon inventory problem. Management Science , 6(4):475–490, 1960.
Clavier et al. (2024) Pierre Clavier, Erwan Le Pennec, and Matthieu Geist. Towards minimax optimality of model-based robust reinforcement learning. In Conference on Uncertainty in Artificial Intelligence (UAI) , 2024.
Coase (1972) Ronald H. Coase. Durability and monopoly. Journal of Law and Economics , 15(1):143–149, 1972.
Covarrubias (2022) Matias Covarrubias. Dynamic oligopoly and monetary policy: A deep reinforcement learning approach. Job Market Paper, New York University, 2022.
da Costa Cunha et al. (2025) Cristiano da Costa Cunha, Wei Liu, Tim French, and Ajmal Mian. Unifying causal reinforcement learning: Survey, taxonomy, algorithms and applications. arXiv preprint arXiv:2512.18135 , 2025.
Daskalakis et al. (2009) Constantinos Daskalakis, Paul W. Goldberg, and Christos H. Papadimitriou. The complexity of computing a nash equilibrium. SIAM Journal on Computing , 39(1):195–259, 2009.
Dayan (1992) Peter Dayan. The convergence of TD( λ \lambda ) for general λ \lambda . Machine Learning , 8(3–4):341–362, 1992.
Denardo (1967) Eric V. Denardo. Contraction mappings in the theory underlying dynamic programming. SIAM Review , 9(2):165–177, 1967.
Deng et al. (2023) Zhihong Deng, Jing Jiang, Guodong Long, and Chengqi Zhang. Causal reinforcement learning: A survey. Transactions on Machine Learning Research , 2023.
Dohare et al. (2024) Shibhansh Dohare, J. Fernando Hernandez-Garcia, Qingfeng Lan, Parash Rahman, A. Mahmoud, and Richard S. Sutton. Loss of plasticity in deep continual learning. Nature , 632:768–774, 2024.
D'Oro et al. (2023) Pierluca D'Oro, Max Schwarzer, Evgenii Nikishin, Pierre-Luc Bacon, Marc G. Bellemare, and Aaron Courville. Sample-efficient reinforcement learning by breaking the replay ratio barrier. In Proceedings of the International Conference on Learning Representations (ICLR) , 2023.
Efron (1979) Bradley Efron. Bootstrap methods: Another look at the jackknife. The Annals of Statistics , 7(1):1–26, 1979.
Eimer et al. (2023) Theresa Eimer, Marius Lindauer, and Roberta Raileanu. Hyperparameters in reinforcement learning and how to tune them. In Proceedings of the 40th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2023.
Engstrom et al. (2020) Logan Engstrom, Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, and Aleksander Madry. Implementation matters in deep RL: A case study on PPO and TRPO. In Proceedings of the International Conference on Learning Representations (ICLR) , 2020.
Ernst et al. (2005) Damien Ernst, Pierre Geurts, and Louis Wehenkel. Tree-based batch mode reinforcement learning. Journal of Machine Learning Research , 6:503–556, 2005.
Espeholt et al. (2018) Lasse Espeholt, Hubert Soyer, Rémi Munos, Karen Simonyan, Volodymyr Mnih, Tom Ward, Yotam Doron, Vlad Firoiu, Tim Harley, Iain Dunning, Shane Legg, and Koray Kavukcuoglu. IMPALA: Scalable distributed deep-RL with importance weighted actor-learner architectures. In International Conference on Machine Learning , 2018.
Even-Dar and Mansour (2003) Eyal Even-Dar and Yishay Mansour. Learning rates for q-learning. Journal of Machine Learning Research , 5:1–25, 2003.
Fan et al. (2024) Jianqing Fan, Yongyi Guo, and Mengxin Yu. Semiparametric dynamic pricing. arXiv preprint arXiv:2401.01136 , 2024.
Fearnley (2010) John Fearnley. Exponential lower bounds for policy iteration. In International Colloquium on Automata, Languages, and Programming (ICALP) , pages 551–562, 2010.
Fedus et al. (2020) William Fedus, Prajit Ramachandran, Rishabh Agarwal, Yoshua Bengio, Hugo Larochelle, Mark Rowland, and Marc G. Bellemare. Revisiting fundamentals of experience replay. In Proceedings of the 37th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2020.
Fellows et al. (2023) Mattie Fellows, Matthew J. A. Smith, and Shimon Whiteson. Why target networks stabilise temporal difference methods. In Proceedings of the 40th International Conference on Machine Learning , volume 202 of Proceedings of Machine Learning Research , pages 9886–9909. PMLR, 2023.
Fernández-Villaverde et al. (2023) Jesús Fernández-Villaverde, Samuel Hurtado, and Galo Nuño. Financial frictions and the wealth distribution. Econometrica , 91(3):869–901, 2023.
Fernández-Villaverde et al. (2024) Jesús Fernández-Villaverde, Galo Nuño, and Jesse Perla. Taming the curse of dimensionality: Quantitative economics with deep learning. Working Paper 33117, National Bureau of Economic Research, 2024.
Fershtman and Pakes (2012) Chaim Fershtman and Ariel Pakes. Dynamic games with asymmetric information: A framework for empirical work. The Quarterly Journal of Economics , 127(4):1611–1661, 2012.
Forney et al. (2017) Andrew Forney, Judea Pearl, and Elias Bareinboim. Counterfactual data-fusion for online reinforcement learners. In Proceedings of the 34th International Conference on Machine Learning , pages 1156–1164, 2017.
Fujimoto et al. (2018) Scott Fujimoto, Herke van Hoof, and David Meger. Addressing function approximation error in actor-critic methods. In Proceedings of the 35th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2018.
Fujimoto et al. (2019) Scott Fujimoto, David Meger, and Doina Precup. Off-policy deep reinforcement learning without exploration. In Proceedings of the 36th International Conference on Machine Learning , volume 97 of Proceedings of Machine Learning Research , pages 2052–2062. PMLR, 2019.
Fujimoto et al. (2022) Scott Fujimoto, David Meger, Doina Precup, Ofir Nachum, and Shixiang Shane Gu. Why should I trust you, Bellman? the Bellman error is a poor replacement for value error. In Proceedings of the 39th International Conference on Machine Learning , volume 162 of Proceedings of Machine Learning Research , 2022.
Ganti et al. (2018) Ravi Ganti, Matyas Sustik, Quoc Tran, and Brian Seaman. Thompson sampling for dynamic pricing. arXiv preprint arXiv:1802.03050 , 2018.
Geist et al. (2019) Matthieu Geist, Bruno Scherrer, and Olivier Pietquin. A theory of regularized Markov decision processes. In International Conference on Machine Learning (ICML) , 2019.
Gijsbrechts et al. (2022) Joren Gijsbrechts, Robert N. Boute, Jan A. Van Mieghem, and Dennis J. Zhang. Can deep reinforcement learning improve inventory management? Performance on dual sourcing, lost sales, and multi-echelon problems. Manufacturing & Service Operations Management , 24(3):1349–1368, 2022.
Gittins (1979) John C. Gittins. Bandit processes and dynamic allocation indices. Journal of the Royal Statistical Society: Series B (Methodological) , 41(2):148–164, 1979.
Gourieroux et al. (1993) Christian Gourieroux, Alain Monfort, and Eric Renault. Indirect inference. Journal of Applied Econometrics , 8(S1):S85–S118, 1993.
Greenwald and Hall (2003) Amy Greenwald and Keith Hall. Correlated q-learning. In Proceedings of the 20th International Conference on Machine Learning , pages 242–249, 2003.
Gul et al. (1986) Faruk Gul, Hugo Sonnenschein, and Robert Wilson. Foundations of dynamic monopoly and the Coase conjecture. Journal of Economic Theory , 39(1):155–190, 1986.
Haarnoja et al. (2017) Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. Reinforcement learning with deep energy-based policies. In Proceedings of the 34th International Conference on Machine Learning , 2017.
Haarnoja et al. (2018) Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. Proceedings of the 35th International Conference on Machine Learning , pages 1861–1870, 2018.
Hambly et al. (2023) Ben Hambly, Renyuan Xu, and Huining Yang. Recent advances in reinforcement learning in finance. Mathematical Finance , 33(3):437–503, 2023.
Han et al. (2022) Xiao Han, Weijian Zhang, Jiaxin Wang, Fan Zhang, and Jieping Ye. A better match for drivers and riders: Reinforcement learning at Lyft. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining , pages 2927–2936, 2022.
Hardt et al. (2016) Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. Strategic classification. In Proceedings of the 2016 ACM Conference on Innovations in Theoretical Computer Science (ITCS) , pages 111–122, 2016.
Heinrich and Silver (2016) Johannes Heinrich and David Silver. Deep reinforcement learning from self-play in imperfect-information games. arXiv preprint arXiv:1603.01121 , 2016.
Henderson et al. (2018) Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger. Deep reinforcement learning that matters. In Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence , 2018.
Hollenbeck (2019) Brett Hollenbeck. Horizontal mergers and innovation in concentrated industries. Quantitative Marketing and Economics , 2019.
Hotz and Miller (1993) V. Joseph Hotz and Robert A. Miller. Conditional choice probabilities and the estimation of dynamic models. The Review of Economic Studies , 60(3):497–529, 1993.
Howard (1960) Ronald A. Howard. Dynamic Programming and Markov Processes . The Technology Press of M.I.T. and John Wiley and Sons, New York, NY, 1960.
Hu and Wellman (2003) Junling Hu and Michael P Wellman. Nash q-learning for general-sum stochastic games. Journal of Machine Learning Research , 4(Nov):1039–1069, 2003.
Hu and Shum (2012) Yingyao Hu and Matthew Shum. Nonparametric identification of dynamic models with unobserved state variables. Journal of Econometrics , 171(1):32–44, 2012.
Hu and Yang (2025) Yingyao Hu and Fangzhu Yang. Estimation of dynamic discrete choice models with unobserved state variables using reinforcement learning. Working Paper, Johns Hopkins University , 2025.
Huang et al. (2022) Shengyi Huang, Rousslan Fernand Julien Dossa, Antonin Raffin, Anssi Kanervisto, and Weng Wang. The 37 implementation details of proximal policy optimization. ICLR Blog Track , 2022.
Igami (2020) Mitsuru Igami. Artificial intelligence as structural estimation: Deep blue, bonanza, and alphago. The Econometrics Journal , 23(3):S1–S24, 2020.
Ilyas et al. (2020) Andrew Ilyas, Logan Engstrom, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, and Aleksander Madry. A closer look at deep policy gradients. In Proceedings of the International Conference on Learning Representations (ICLR) , 2020.
Iskhakov et al. (2020) Fedor Iskhakov, John Rust, and Bertel Schjerning. Machine learning and structural econometrics: Contrasts and synergies. The Econometrics Journal , 23(S1):S81–S124, 2020.
Jaakkola et al. (1994) Tommi Jaakkola, Michael I. Jordan, and Satinder P. Singh. On the convergence of stochastic iterative dynamic programming algorithms. In Advances in Neural Information Processing Systems 6 , pages 703–710. Morgan Kaufmann, 1994.
Javanmard and Nazerzadeh (2019) Adel Javanmard and Hamid Nazerzadeh. Dynamic pricing in high-dimensions. Journal of Machine Learning Research , 20(9):1–49, 2019.
Jin et al. (2021) Ying Jin, Zhuoran Yang, and Zhaoran Wang. Is pessimism provably efficient for offline RL? In Proceedings of the 38th International Conference on Machine Learning , volume 139 of Proceedings of Machine Learning Research , pages 5084–5096. PMLR, 2021.
Kakade (2001) Sham M. Kakade. A natural policy gradient. Advances in Neural Information Processing Systems , 14, 2001.
Kakade (2002) Sham M. Kakade. A Natural Policy Gradient . PhD thesis, University College London, 2002.
Kallus and Zhou (2020) Nathan Kallus and Angela Zhou. Confounding-robust policy evaluation in infinite-horizon reinforcement learning. In Advances in Neural Information Processing Systems , volume 33, 2020.
Kamin (1969) Leon J. Kamin. Predictability, surprise, attention and conditioning. In Byron A. Campbell and Russell M. Church, editors, Punishment and Aversive Behavior , pages 279–296. Appleton-Century-Crofts, 1969.
Kearns et al. (2002) Michael Kearns, Yishay Mansour, and Andrew Y. Ng. A sparse sampling algorithm for near-optimal planning in large Markov decision processes. Machine Learning , 49(2–3):193–208, 2002.
Kleinberg and Leighton (2003) Robert Kleinberg and Tom Leighton. The value of knowing a demand curve: Bounds on regret for online posted-price auctions. In Proceedings of the 44th Annual IEEE Symposium on Foundations of Computer Science (FOCS) , pages 594–605, 2003.
Kleinman (1968) David L. Kleinman. On an iterative technique for Riccati equation computations. IEEE Transactions on Automatic Control , 13(1):114–115, 1968.
Konda and Tsitsiklis (2000) Vijay R. Konda and John N. Tsitsiklis. Actor-critic algorithms. In Advances in Neural Information Processing Systems 12 , pages 1008–1014. MIT Press, 2000.
Korbak et al. (2022) Tomasz Korbak, Ethan Perez, and Christopher L. Buckley. RL with KL penalties is better viewed as Bayesian inference. arXiv preprint arXiv:2205.11275 , 2022.
Kostrikov et al. (2022) Ilya Kostrikov, Ashvin Nair, and Sergey Levine. Offline reinforcement learning with implicit Q-Learning. In International Conference on Learning Representations , 2022.
Kumar et al. (2020) Aviral Kumar, Aurick Zhou, George Tucker, and Sergey Levine. Conservative Q-Learning for offline reinforcement learning. In Advances in Neural Information Processing Systems , volume 33, 2020.
Kumar et al. (2021) Aviral Kumar, Rishabh Agarwal, Dibya Ghosh, and Sergey Levine. Implicit under-parameterization inhibits data-efficient deep reinforcement learning. In Proceedings of the International Conference on Learning Representations (ICLR) , 2021.
Kushner and Clark (1978) Harold J. Kushner and Dean S. Clark. Stochastic Approximation Methods for Constrained and Unconstrained Systems . Springer-Verlag, New York, 1978.
Lai and Robbins (1985) Tze Leung Lai and Herbert Robbins. Asymptotically efficient adaptive allocation rules. Advances in Applied Mathematics , 6(1):4–22, 1985.
Lange et al. (2012) Sascha Lange, Thomas Gabel, and Martin Riedmiller. Batch reinforcement learning. Reinforcement Learning: State-of-the-Art , pages 45–73, 2012.
Lattimore (2016) Tor Lattimore. Regret analysis of the finite-horizon Gittins index strategy for multi-armed bandits. In Proceedings of the 29th Conference on Learning Theory (COLT) , pages 1214–1245, 2016.
Levine et al. (2020) Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu. Offline reinforcement learning: Tutorial, review, and perspectives on open problems. arXiv preprint arXiv:2005.01643 , 2020.
Li et al. (2022) Gen Li, Yuting Wei, Yuejie Chi, and Yuxin Chen. Softmax policy gradient methods can take exponential time to converge. Mathematical Programming , 196:579–632, 2022.
Li et al. (2024a) Gen Li, Laixi Shi, Yuxin Chen, Yuting Wei, and Yuejie Chi. Is q-learning minimax optimal? a tight sample complexity analysis. Operations Research , 72(1), 2024a.
Li et al. (2024b) Gen Li, Yuting Wei, Yuejie Chi, Yuantao Gu, and Yuxin Chen. Breaking the sample size barrier in model-based reinforcement learning with a generative model. Operations Research , 72(1), 2024b.
Li et al. (2019) Minne Li, Zhiwei Qin, Yan Jiao, Yaodong Yang, Zheng Gong, Jun Wang, Changjie Wang, Gauge Wu, and Jieping Ye. Efficient ridesharing order dispatching with mean field multi-agent reinforcement learning. In Proceedings of the 2019 World Wide Web Conference (WWW) , pages 983–994, 2019.
Liao et al. (2024) Luofeng Liao, Zuyue Fu, Zhuoran Yang, Yixin Wang, Dingli Ma, Mladen Kolar, and Zhaoran Wang. Instrumental variable value iteration for causal offline reinforcement learning. Journal of Machine Learning Research , 25(303):1–56, 2024.
Lim and Lee (2024) Han-Dong Lim and Donghwan Lee. Regularized q-learning. In Advances in Neural Information Processing Systems (NeurIPS) , 2024.
Lin (1992) Long-Ji Lin. Self-Improving Reactive Agents Based on Reinforcement Learning, Planning and Teaching . PhD thesis, Carnegie Mellon University, 1992. Also published in Machine Learning , 8(3–4):293–321, 1992.
Littman (1994) Michael L Littman. Markov games as a framework for multi-agent reinforcement learning. In Machine Learning Proceedings 1994 , pages 157–163. Morgan Kaufmann, 1994.
Littman (2001) Michael L. Littman. Friend-or-foe q-learning in general-sum games. In Proceedings of the 18th International Conference on Machine Learning , pages 322–328, 2001.
Liu et al. (2024) Allen Liu, Jingwen Yang, Yining Wang, and Jianghao Sun. Contextual dynamic pricing with strategic buyers. arXiv preprint arXiv:2307.04055 , 2024.
Liu et al. (2019) Jiaxi Liu, Xiaoqing Wang, Yuming Deng, Xingyu Wu, and Yidong Zhang. Dynamic pricing on E-commerce platform with deep reinforcement learning: A field experiment. arXiv preprint arXiv:1912.02572 , 2019.
Lomys and Magnolfi (2024) Nikolay Lomys and Luca Magnolfi. Estimation of games under no regret: Structural econometrics for ai. Working Paper NET Institute Working Paper No. 24-05, Social Science Research Network (SSRN), 2024. Available at SSRN: https://ssrn.com/abstract=4717195 or http://dx.doi.org/10.2139/ssrn.4717195.
Lyle et al. (2022) Clare Lyle, Mark Rowland, and Will Dabney. Understanding and preventing capacity loss in reinforcement learning. In Proceedings of the International Conference on Learning Representations (ICLR) , 2022.
Lyle et al. (2023) Clare Lyle, Mark Rowland, Will Dabney, Marta Kwiatkowska, and Yarin Gal. Understanding plasticity in neural networks. In Proceedings of the 40th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2023.
Lyle et al. (2025) Clare Lyle, Zeyu Zheng, Evgenii Nikishin, Bernardo Avila Pires, Razvan Pascanu, and Will Dabney. Disentangling causes of plasticity loss in neural networks. In Proceedings of the International Conference on Learning Representations (ICLR) , 2025.
Maliar et al. (2021) Lilia Maliar, Serguei Maliar, and Pablo Winant. Deep learning for solving dynamic economic models. Journal of Monetary Economics , 122:76–101, 2021.
Manne (1960) Alan S. Manne. Linear programming and sequential decisions. Management Science , 6(3):259–267, 1960.
massoud Farahmand et al. (2010) Amir massoud Farahmand, Rémi Munos, and Csaba Szepesvári. Error propagation for approximate policy and value iteration. In Advances in Neural Information Processing Systems 22 (NeurIPS) , pages 568–576, 2010.
McFadden (1974) Daniel McFadden. Conditional logit analysis of qualitative choice behavior. Frontiers in Econometrics , pages 105–142, 1974.
Mei et al. (2020) Jincheng Mei, Chenjun Xiao, Csaba Szepesvari, and Dale Schuurmans. On the global convergence rates of softmax policy gradient methods. In International Conference on Machine Learning , 2020.
Misra et al. (2019) Kanishka Misra, Eric M. Schwartz, and Jacob Abernethy. Dynamic online pricing with incomplete information using multiarmed bandit experiments. Marketing Science , 38(2):226–252, 2019.
Mnih et al. (2015) Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level control through deep reinforcement learning. Nature , 518:529–533, 2015.
Mnih et al. (2016) Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. Asynchronous methods for deep reinforcement learning. In Proceedings of the 33rd International Conference on Machine Learning , pages 1928–1937. PMLR, 2016.
Moerland et al. (2023) Thomas M. Moerland, Joost Broekens, Aske Plaat, and Catholijn M. Jonker. Model-based reinforcement learning: A survey. Foundations and Trends in Machine Learning , 2023.
Moll (2025) Benjamin Moll. The trouble with rational expectations in heterogeneous agent models: A challenge for macroeconomics. The Economic Journal , 2025. doi: 10.1093/ej/ueaf104 .
Mueller et al. (2019) Jonas Mueller, Vasilis Syrgkanis, and Matt Taddy. Low-rank bandit methods for high-dimensional dynamic pricing. In Advances in Neural Information Processing Systems , volume 32, 2019.
Munos and Szepesvári (2008) Rémi Munos and Csaba Szepesvári. Finite-time bounds for fitted value iteration. Journal of Machine Learning Research , 9:815–857, 2008.
Munos and Szepesvári (2008) Rémi Munos and Csaba Szepesvári. Finite-time bounds for fitted value iteration. Journal of Machine Learning Research , 9(27):815–857, 2008.
Munos et al. (2016) Rémi Munos, Tom Stepleton, Anna Harutyunyan, and Marc G. Bellemare. Safe and efficient off-policy reinforcement learning. In Advances in Neural Information Processing Systems , volume 29, 2016.
Nevmyvaka et al. (2006) Yuriy Nevmyvaka, Yi Feng, and Michael Kearns. Reinforcement learning for optimized trade execution. In Proceedings of the 23rd International Conference on Machine Learning (ICML) , pages 673–680, 2006.
Nikishin et al. (2022) Evgenii Nikishin, Max Schwarzer, Pierluca D'Oro, Pierre-Luc Bacon, and Aaron Courville. The primacy bias in deep reinforcement learning. In Proceedings of the 39th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2022.
Oberst and Sontag (2019) Michael Oberst and David Sontag. Counterfactual off-policy evaluation with Gumbel-Max structural causal models. In Proceedings of the 36th International Conference on Machine Learning , pages 4923–4932, 2019.
Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems , volume 35, pages 27730–27744, 2022.
Pakes and McGuire (1994) Ariel Pakes and Paul McGuire. Computing Markov-perfect Nash equilibria: Numerical implications of a dynamic differentiated product model. RAND Journal of Economics , 25(4):555–589, 1994.
Pardo et al. (2018) Fabio Pardo, Arash Tavakoli, Vitaly Levdik, and Petar Kormushev. Time limits in reinforcement learning. In Proceedings of the 35th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2018.
Patterson et al. (2024) Andrew Patterson, Samuel Neumann, Martha White, and Adam White. Empirical design in reinforcement learning. In arXiv preprint arXiv:2304.01315 , 2024.
Pavlov (1927) Ivan P. Pavlov. Conditioned Reflexes: An Investigation of the Physiological Activity of the Cerebral Cortex . Oxford University Press, 1927.
Pearl (2009) Judea Pearl. Causality: Models, Reasoning, and Inference . Cambridge University Press, Cambridge, 2nd edition, 2009.
Pearl and Bareinboim (2014) Judea Pearl and Elias Bareinboim. External validity: From do-calculus to transportability across populations. Statistical Science , 29(4):579–595, 2014.
Pollatschek and Avi-Itzhak (1969) Moshe A. Pollatschek and Benjamin Avi-Itzhak. Algorithms for stochastic games with geometrical interpretation. Management Science , 15(7):399–415, 1969.
Puterman and Brumelle (1979) Martin L. Puterman and Shelby L. Brumelle. On the convergence of policy iteration in stationary dynamic programming. Mathematics of Operations Research , 4(1):60–69, 1979.
Pycia and Troyan (2023) Marek Pycia and Peter Troyan. A theory of simplicity in games and mechanism design. Econometrica , 91(4):1495–1526, 2023.
Qi and Sun (1993) Liqun Qi and Jie Sun. A nonsmooth version of Newton's method. Mathematical Programming , 58(1–3):353–367, 1993.
Qin et al. (2021) Zhiwei Qin, Xiaocheng Tang, Yan Jiao, Fan Zhang, Zhe Xu, Hongtu Zhu, and Jieping Ye. Ride-hailing order dispatching at DiDi via reinforcement learning. INFORMS Journal on Applied Analytics , 51(3):272–286, 2021.
Qu and Wierman (2020) Guannan Qu and Adam Wierman. Finite-time analysis of asynchronous stochastic approximation and q-learning. Journal of Machine Learning Research , 21(1):1–28, 2020.
Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances in Neural Information Processing Systems , volume 36, 2023.
Rashidinejad et al. (2021) Paria Rashidinejad, Banghua Zhu, Cong Ma, Jiantao Jiao, and Stuart Russell. Bridging offline reinforcement learning and imitation learning: A tale of pessimism. In Advances in Neural Information Processing Systems , volume 34, 2021.
Ravindranath et al. (2024) Sai Srivatsa Ravindranath, Zhe Feng, Di Wang, Manzil Zaheer, Aranyak Mehta, and David C. Parkes. Deep reinforcement learning for sequential combinatorial auctions. Submitted to ICLR 2025, 2024. Available at https://openreview.net/forum?id=SVd9Ffcdp8 .
Rawat (2026) Pranjal Rawat. Designing auctions when algorithms learn to bid. Working Paper , 2026.
Rescorla and Wagner (1972) Robert A. Rescorla and Allan R. Wagner. A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In Abraham H. Black and William F. Prokasy, editors, Classical Conditioning II: Current Research and Theory , pages 64–99. Appleton-Century-Crofts, 1972.
Robbins (1952) Herbert Robbins. Some aspects of the sequential design of experiments. Bulletin of the American Mathematical Society , 58(5):527–535, 1952.
Robins et al. (1994) James M. Robins, Andrea Rotnitzky, and Lue Ping Zhao. Estimation of regression coefficients when some regressors are not always observed. Journal of the American Statistical Association , 89(427):846–866, 1994.
Rothschild (1974) Michael Rothschild. A two-armed bandit theory of market pricing. Journal of Economic Theory , 9(2):185–202, 1974.
Rummery and Niranjan (1994) G. A. Rummery and M. Niranjan. On-line q-learning using connectionist systems. Technical report, Cambridge University, 1994.
Rust (1987) John Rust. Optimal replacement of gmc bus engines: An empirical model of harold zurcher. Econometrica , 55(5):999–1033, 1987.
Rust (1994) John Rust. Structural estimation of Markov decision processes. In Robert F. Engle and Daniel McFadden, editors, Handbook of Econometrics , volume 4, chapter 51, pages 3081–3143. Elsevier, 1994.
Rust (1996) John Rust. Numerical dynamic programming in economics. In Hans M. Amman, David A. Kendrick, and John Rust, editors, Handbook of Computational Economics , volume 1, pages 619–729. Elsevier, 1996.
Rust (2008) John Rust. Dynamic programming. In The New Palgrave Dictionary of Economics . Palgrave Macmillan, London, 2nd edition, 2008.
Rust and Rawat (2026) John Rust and Pranjal Rawat. Structural econometrics and inverse reinforcement learning: Inferring preferences and beliefs from human behavior. Working Paper, Georgetown University, 2026.
Samuel (1959) Arthur L. Samuel. Some studies in machine learning using the game of checkers. IBM Journal of Research and Development , 3(3):210–229, 1959.
Santos and Rust (2004) Manuel S. Santos and John Rust. Convergence properties of policy iteration. SIAM Journal on Control and Optimization , 42(6):2094–2115, 2004.
Schaul et al. (2016) Tom Schaul, John Quan, Ioannis Antonoglou, and David Silver. Prioritized experience replay. In Proceedings of the International Conference on Learning Representations (ICLR) , 2016.
Schölkopf et al. (2021) Bernhard Schölkopf, Francesco Locatello, Stefan Bauer, Nan Rosemary Ke, Nal Kalchbrenner, Anirudh Goyal, and Yoshua Bengio. Toward causal representation learning. Proceedings of the IEEE , 109(5):612–634, 2021.
Schulman et al. (2015) John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust region policy optimization. Proceedings of the 32nd International Conference on Machine Learning , pages 1889–1897, 2015.
Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.
Shani et al. (2020) Lior Shani, Yonathan Efroni, and Shie Mannor. Adaptive trust region policy optimization: Global convergence and faster rates for regularized MDPs. In AAAI Conference on Artificial Intelligence , 2020.
Shannon (1950) Claude E. Shannon. Programming a computer for playing chess. Philosophical Magazine , 41(314):256–275, 1950.
Shapley (1953) Lloyd S. Shapley. Stochastic games. Proceedings of the National Academy of Sciences , 39(10):1095–1100, 1953.
Shapley (1964) Lloyd S. Shapley. Some topics in two-person games. In M. Dresher, L. S. Shapley, and A. W. Tucker, editors, Advances in Game Theory , pages 1–28. Princeton University Press, 1964.
Shoham et al. (2007) Yoav Shoham, Rob Powers, and Trond Grenager. If multi-agent learning is the answer, what is the question? Artificial Intelligence , 171(7):365–377, 2007.
Sidford et al. (2018) Aaron Sidford, Mengdi Wang, Xian Wu, Lin F. Yang, and Yinyu Ye. Near-optimal time and sample complexities for solving Markov decision processes with a generative model. In Advances in Neural Information Processing Systems , 2018.
Silver et al. (2016) David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis. Mastering the game of go with deep neural networks and tree search. Nature , 529(7587):484–489, 2016.
Silver et al. (2017) David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel, and Demis Hassabis. Mastering the game of go without human knowledge. Nature , 550(7676):354–359, 2017.
Silver et al. (2018) David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, and Demis Hassabis. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. Science , 362(6419):1140–1144, 2018.
Singh et al. (2000) Satinder Singh, Tommi Jaakkola, Michael L Littman, and Csaba Szepesvári. Convergence results for single-step on-policy reinforcement-learning algorithms. Machine learning , 38:287–308, 2000.
Singh and Yee (1994) Satinder P. Singh and Richard C. Yee. An upper bound on the loss from approximate optimal-value functions. Machine Learning , 16(3):227–233, 1994.
Skalse et al. (2022) Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, and David Krueger. Defining and characterizing reward hacking. In Advances in Neural Information Processing Systems , volume 35, 2022.
Sokar et al. (2023) Ghada Sokar, Rishabh Agarwal, Pablo Samuel Castro, and Utku Evci. The dormant neuron phenomenon in deep reinforcement learning. In Proceedings of the 40th International Conference on Machine Learning , Proceedings of Machine Learning Research, 2023.
Stiennon et al. (2020) Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul F. Christiano. Learning to summarize with human feedback. In Advances in Neural Information Processing Systems , volume 33, pages 3008–3021, 2020.
Stokey (1981) Nancy L. Stokey. Rational expectations and durable goods pricing. Bell Journal of Economics , 12(1):112–128, 1981.
Sutton (1988) Richard S. Sutton. Learning to predict by the methods of temporal differences. Machine Learning , 3(1):9–44, 1988. doi: 10.1023/A:1022633531479 .
Sutton (1990) Richard S. Sutton. Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In Proceedings of the Seventh International Conference on Machine Learning , pages 216–224. Morgan Kaufmann, 1990.
Sutton and Barto (1990) Richard S. Sutton and Andrew G. Barto. Time-derivative models of Pavlovian reinforcement. In Michael Gabriel and John Moore, editors, Learning and Computational Neuroscience: Foundations of Adaptive Networks , pages 497–537. MIT Press, 1990.
Sutton and Barto (2018) Richard S. Sutton and Andrew G. Barto. Reinforcement Learning: An Introduction . The MIT Press, 2nd edition, 2018.
Sutton et al. (1999) Richard S. Sutton, David A. McAllester, Satinder P. Singh, and Yishay Mansour. Policy gradient methods for reinforcement learning with function approximation. Advances in Neural Information Processing Systems , 12, 1999.
Sutton et al. (2000) Richard S. Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradient methods for reinforcement learning with function approximation. In Advances in Neural Information Processing Systems , volume 12. MIT Press, 2000.
Sutton et al. (2009) Richard S. Sutton, Hamid Reza Maei, Doina Precup, Shalabh Bhatnagar, David Silver, Csaba Szepesvári, and Eric Wiewiora. Fast gradient-descent methods for temporal-difference learning with linear function approximation. In Proceedings of the 26th International Conference on Machine Learning , pages 993–1000. ACM, 2009.
Szepesvári (2010) Csaba Szepesvári. Algorithms for Reinforcement Learning . Synthesis Lectures on Artificial Intelligence and Machine Learning. Morgan & Claypool Publishers, 2010.
Tammelin (2014) Oskari Tammelin. Solving large imperfect information games using cfr+. arXiv preprint arXiv:1407.5042 , 2014.
Tang et al. (2019) Xiaocheng Tang, Zhiwei Qin, Fan Zhang, Zhaodong Wang, Zhe Xu, Yintai Ma, Hongtu Zhu, and Jieping Ye. A deep value-network based approach for multi-driver order dispatching. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining , pages 1780–1790, 2019.
Tesauro (1994) Gerald Tesauro. Td-gammon, a self-teaching backgammon program, achieves master-level play. Neural Computation , 6(2):215–219, 1994.
Thompson (1933) William R. Thompson. On the likelihood that one unknown probability exceeds another in view of the evidence of two samples. Biometrika , 25(3–4):285–294, 1933.
Thorndike (1898) Edward L. Thorndike. Animal Intelligence: An Experimental Study of the Associative Processes in Animals . Macmillan, 1898. Psychological Review Monograph Supplements, No. 8.
Thrun and Schwartz (1993) Sebastian Thrun and Anton Schwartz. Issues in using function approximation for reinforcement learning. In Proceedings of the Fourth Connectionist Models Summer School , 1993.
Tian et al. (2023) Haoxing Tian, Ioannis Ch. Paschalidis, and Alex Olshevsky. Convergence of actor-critic methods with multi-layer neural networks. In The Eleventh International Conference on Learning Representations (ICLR) , 2023.
Tibshirani (1996) Robert Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society, Series B , 58(1):267–288, 1996.
Towers et al. (2024) Mark Towers, Ariel Kwiatkowski, Jordan K. Terry, John U. Balis, Gianluca De Cola, Tristan Deleu, Manuel Goulao, Andreas Kallinteris, Markus Krimmel, Arjun KG, Rodrigo Perez-Vicente, Andrea Pierré, Sander Schulhoff, Jun Jet Tai, Hannah Tze, and Omar G. Younis. Gymnasium: A standard interface for reinforcement learning environments. In arXiv preprint arXiv:2407.17032 , 2024.
Tsitsiklis (1994) John N. Tsitsiklis. Asynchronous stochastic approximation and q-learning. Machine Learning , 16(3):185–202, 1994. doi: 10.1007/bf00993306 .
Tsitsiklis (2002) John N. Tsitsiklis. On the convergence of optimistic policy iteration. Journal of Machine Learning Research , 3:59–72, 2002.
Tsitsiklis and Van Roy (1997) John N. Tsitsiklis and Benjamin Van Roy. Analysis of temporal-difference learning with function approximation. In Advances in Neural Information Processing Systems 9 (NIPS) , 1997.
Tullii et al. (2024) Daniele Tullii, Adel Javanmard, Matteo Pirotta, and Pierre Lezaud. Contextual dynamic pricing with strategic buyers under unknown valuations. arXiv preprint arXiv:2307.04895 , 2024.
van Hasselt (2010) Hado van Hasselt. Double q-learning. In Advances in Neural Information Processing Systems , volume 23, 2010.
van Hasselt et al. (2016a) Hado van Hasselt, Arthur Guez, Matteo Hessel, Volodymyr Mnih, and David Silver. Learning values across many orders of magnitude. In Advances in Neural Information Processing Systems , volume 29, 2016a.
van Hasselt et al. (2016b) Hado van Hasselt, Arthur Guez, and David Silver. Deep reinforcement learning with double Q-Learning. In Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence , 2016b.
van Hasselt et al. (2018) Hado van Hasselt, Yotam Doron, Florian Strub, Matteo Hessel, Nicolas Sonnerat, and Joseph Modayil. Deep reinforcement learning and the deadly triad. In arXiv preprint arXiv:1812.02648 , 2018.
van Seijen et al. (2016) Harm van Seijen, A. Rupam Mahmood, Patrick M. Pilarski, Marlos C. Machado, and Richard S. Sutton. True online temporal-difference learning. Journal of Machine Learning Research , 17(145):1–40, 2016.
Wainwright (2019) Martin J. Wainwright. Stochastic approximation with cone-contractive operators: Sharp ℓ ∞ \ell_{\infty} -bounds for Q-learning. Annals of Statistics , 47(6):3168–3197, 2019.
Wang et al. (2025) Yue Wang, Tomasz Żak, and Csaba Szepesvári. Near-optimal sample complexity for iterated CVaR reinforcement learning with a generative model. arXiv preprint arXiv:2503.08934 , 2025.
Watkins and Dayan (1992) Christopher J. C. H. Watkins and Peter Dayan. Q-learning. Machine Learning , 8(3–4):279–292, 1992.
Williams (1992) Ronald J. Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. Machine Learning , 8:229–256, 1992.
Wu et al. (2018) Di Wu, Xiujun Chen, Xun Yang, Hao Wang, Qing Tan, Xiaoxun Zhang, Jian Xu, and Kun Gai. Budget constrained bidding by model-free reinforcement learning in display advertising. In Proceedings of the 27th ACM International Conference on Information and Knowledge Management (CIKM) , pages 1443–1451, 2018.
Wu et al. (2020) Yue Wu, Weitong Zhang, Pan Xu, and Quanquan Gu. A finite-time analysis of two time-scale actor-critic methods. In Advances in Neural Information Processing Systems (NeurIPS) , 2020.
Xiao (2022) Lin Xiao. On the convergence rates of policy gradient methods. Journal of Machine Learning Research , 23, 2022.
Xu and Wang (2021) Jianyu Xu and Yu-Xiang Wang. Logarithmic regret in feature-based dynamic pricing. In Advances in Neural Information Processing Systems , volume 34, 2021.
Ye (2011) Yinyu Ye. The simplex and policy-iteration methods are strongly polynomial for the Markov decision problem with a fixed discount rate. Mathematics of Operations Research , 36(4):593–603, 2011.
Yuan et al. (2024) Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston. Self-rewarding language models. arXiv preprint arXiv:2401.10020 , 2024.
Zanette (2021) Andrea Zanette. Exponential lower bounds for batch reinforcement learning: Batch RL can be exponentially harder than online RL. In Proceedings of the 38th International Conference on Machine Learning , volume 139 of Proceedings of Machine Learning Research . PMLR, 2021.
Zhang and Bareinboim (2019) Junzhe Zhang and Elias Bareinboim. Near-optimal reinforcement learning in dynamic treatment regimes. In Advances in Neural Information Processing Systems , volume 32, 2019.
Zhang and Bareinboim (2020) Junzhe Zhang and Elias Bareinboim. Designing optimal dynamic treatment regimes: A causal reinforcement learning approach. In Proceedings of the 37th International Conference on Machine Learning , pages 11012–11022, 2020.
Zhang and Sutton (2017) Shangtong Zhang and Richard S. Sutton. A deeper look at experience replay. In arXiv preprint arXiv:1712.01275 , 2017.
Zhang et al. (2021) Shangtong Zhang, Hengshuai Yao, and Shimon Whiteson. Breaking the deadly triad with a target network. In International Conference on Machine Learning (ICML) , 2021.
Zhang (2023) Weipeng Zhang. Distributed randomized multiagent policy iteration in reinforcement learning. Results in Control and Optimization , 12:100255, 2023.
Zhao (2025) Shiyu Zhao. Mathematical Foundations of Reinforcement Learning . Springer, 2025. doi: 10.1007/978-981-97-3944-8 .
Zheng et al. (2022) Stephan Zheng, Alexander Trott, Sunil Srinivasa, David C. Parkes, and Richard Socher. The AI economist: Taxation policy design via two-level deep multiagent reinforcement learning. Science Advances , 8(18):eabk2607, 2022.
Ziegler et al. (2019) Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences. arXiv preprint arXiv:1909.08593 , 2019.
Zinkevich et al. (2008) Martin Zinkevich, Michael Johanson, Michael Bowling, and Carmelo Piccione. Regret minimization in games with incomplete information. In Advances in Neural Information Processing Systems , volume 20, 2008.
Appendix A Glossary of Acronyms and Terms
Acronyms
Experimental support, please
view the build logs
for errors. Generated by
L A T E xml[LOGO]
.
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" ( ) button, located in the page header.
Tip:
You can select the relevant text first, to include it in your report.
Our team has already identified
the following issues
. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a
list of packages that need conversion
, and welcome
developer contributions
.
We gratefully acknowledge support from our
major funders
,
member institutions
,
, and all contributors.
About
·
Help
·
Contact
·
Subscribe
·
Copyright
·
Privacy
·
Accessibility
·
Operational Status (opens in new tab)
Major funding support from
 