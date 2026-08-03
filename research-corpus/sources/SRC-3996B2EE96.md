> Source: https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines

GitHub - chauncygu/Safe-Reinforcement-Learning-Baselines: The repository is for safe reinforcement learning baselines. · GitHub
Skip to content
Navigation Menu
Toggle navigation 
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot Write better code with AI
GitHub Copilot app Direct agents from issue to merge
MCP Registry Integrate external tools
DEVELOPER WORKFLOWS
Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
Code Quality Enforce quality at merge
APPLICATION SECURITY
GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners View all resources
Open Source
COMMUNITY
GitHub Sponsors Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously. [-]
Include my email address so I can be contacted
Cancel Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation.
Cancel Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
chauncygu / Safe-Reinforcement-Learning-Baselines Public
Notifications You must be signed in to change notification settings
Fork 104
Star 810
Code
Issues 0
Pull requests 1
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights 
main
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
More items
Safe-Reinforcement-Learning-Baselines
The repository is for Safe Reinforcement Learning (RL) research, in which we investigate various safe RL baselines and safe RL benchmarks, including single agent RL and multi-agent RL. If any authors do not want their paper to be listed here, please feel free to contact <gshangd[AT]foxmail.com>. (This repository is under actively development. We appreciate any constructive comments and suggestions)
You are more than welcome to update this list! If you find a paper about Safe RL which is not listed here, please
fork this repository, add it and merge back;
or report an issue here;
or email <gshangd[AT]foxmail.com>.
The README is organized as follows:
Safe-Reinforcement-Learning-Baselines
1. Environments Supported
1.1. Safe Single Agent RL benchmarks
1.2. Safe Multi-Agent RL benchmarks
2. Safe RL Baselines
2.1. Safe Single Agent RL Baselines
2.2. Safe Multi-Agent RL Baselines
3. Surveys
4. Theses
5. Book
6. Tutorials
7. Exercise
Publication
1. Environments Supported
1.1. Safe Single Agent RL benchmarks
AI Safety Gridworlds
Safety-Gym
Safety-Gymnasium
1.2. Safe Multi-Agent RL benchmarks
Safe Multi-Agent Mujoco
Safe Multi-Agent Isaac Gym
Safe Multi-Agent Robosuite
2. Safe RL Baselines
2.1. Safe Single Agent RL Baselines
Consideration of risk in reinforcement learning, Paper, Not Find Code, (Accepted by ICML 1994)
Multi-criteria Reinforcement Learning, Paper, Not Find Code, (Accepted by ICML 1998)
Lyapunov design for safe reinforcement learning, Paper, Not Find Code, (Accepted by ICML 2002)
Risk-sensitive reinforcement learning, Paper, Not Find Code, (Accepted by Machine Learning, 2002)
Risk-Sensitive Reinforcement Learning Applied to Control under Constraints, Paper, Not Find Code, (Accepted by Journal of Artificial Intelligence Research, 2005)
An actor-critic algorithm for constrained markov decision processes, Paper, Not Find Code, (Accepted by Systems & Control Letters, 2005)
Reinforcement learning for MDPs with constraints, Paper, Not Find Code, (Accepted by European Conference on Machine Learning 2006)
Discounted Markov decision processes with utility constraints, Paper, Not Find Code, (Accepted by Computers & Mathematics with Applications, 2006)
Constrained reinforcement learning from intrinsic and extrinsic rewards, Paper, Not Find Code, (Accepted by International Conference on Development and Learning 2007)
Safe exploration for reinforcement learning, Paper, Not Find Code, (Accepted by ESANN 2008)
Percentile optimization for Markov decision processes with parameter uncertainty, Paper, Not Find Code, (Accepted by Operations research, 2010)
Probabilistic goal Markov decision processes, Paper, Not Find Code, (Accepted by IJCAI 2011)
Safe reinforcement learning in high-risk tasks through policy improvement, Paper, Not Find Code, (Accepted by IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning (ADPRL) 2011)
Safe Exploration in Markov Decision Processes, Paper, Not Find Code, (Accepted by ICML 2012)
Policy gradients with variance related risk criteria, Paper, Not Find Code, (Accepted by ICML 2012)
Risk aversion in Markov decision processes via near optimal Chernoff bounds, Paper, Not Find Code, (Accepted by NeurIPS 2012)
Safe Exploration of State and Action Spaces in Reinforcement Learning, Paper, Not Find Code, (Accepted by Journal of Artificial Intelligence Research, 2012)
An Online Actor–Critic Algorithm with Function Approximation for Constrained Markov Decision Processes, Paper, Not Find Code, (Accepted by Journal of Optimization Theory and Applications, 2012)
Safe policy iteration, Paper, Not Find Code, (Accepted by ICML 2013)
Reachability-based safe learning with Gaussian processes, Paper, Not Find Code (Accepted by IEEE CDC 2014)
Safe Policy Search for Lifelong Reinforcement Learning with Sublinear Regret, Paper, Not Find Code, (Accepted by ICML 2015)
High-Confidence Off-Policy Evaluation, Paper, Code (Accepted by AAAI 2015)
Safe Exploration for Optimization with Gaussian Processes, Paper, Not Find Code (Accepted by ICML 2015)
Safe Exploration in Finite Markov Decision Processes with Gaussian Processes, Paper, Not Find Code (Accepted by NeurIPS 2016)
Safe and efficient off-policy reinforcement learning, Paper, Code (Accepted by NeurIPS 2016)
Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving, Paper, Not Find Code (only Arxiv, 2016, citation 530+)
Safe Learning of Regions of Attraction in Uncertain, Nonlinear Systems with Gaussian Processes, Paper, Code (Accepetd by CDC 2016)
Safety-constrained reinforcement learning for MDPs, Paper, Not Find Code (Accepted by InInternational Conference on Tools and Algorithms for the Construction and Analysis of Systems 2016)
Convex synthesis of randomized policies for controlled Markov chains with density safety upper bound constraints, Paper, Not Find Code (Accepted by American Control Conference 2016)
Combating Deep Reinforcement Learning's Sisyphean Curse with Intrinsic Fear, Paper, Not Find Code (only Openreview, 2016)
Combating reinforcement learning's sisyphean curse with intrinsic fear, Paper, Not Find Code (only Arxiv, 2016)
Constrained Policy Optimization (CPO), Paper, Code (Accepted by ICML 2017)
Risk-constrained reinforcement learning with percentile risk criteria, Paper, , Not Find Code (Accepted by The Journal of Machine Learning Research, 2017)
Probabilistically Safe Policy Transfer, Paper, Not Find Code (Accepted by ICRA 2017)
Accelerated primal-dual policy optimization for safe reinforcement learning, Paper, Not Find Code (Arxiv, 2017)
Stagewise safe bayesian optimization with gaussian processes, Paper, Not Find Code (Accepted by ICML 2018)
Leave no Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning, Paper, Code (Accepted by ICLR 2018)
Safe Model-based Reinforcement Learning with Stability Guarantees, Paper, Code (Accepted by NeurIPS 2018)
A Lyapunov-based Approach to Safe Reinforcement Learning, Paper, Not Find Code (Accepted by NeurIPS 2018)
Constrained Cross-Entropy Method for Safe Reinforcement Learning, Paper, Not Find Code (Accepted by NeurIPS 2018)
Safe Reinforcement Learning via Formal Methods, Paper, Not Find Code (Accepted by AAAI 2018)
Safe exploration and optimization of constrained mdps using gaussian processes, Paper, Not Find Code (Accepted by AAAI 2018)
Safe reinforcement learning via shielding, Paper, Code (Accepted by AAAI 2018)
Trial without Error: Towards Safe Reinforcement Learning via Human Intervention, Paper, Not Find Code (Accepted by AAMAS 2018)
Learning-based Model Predictive Control for Safe Exploration and Reinforcement Learning, Paper, Not Find Code (Accepted by CDC 2018)
The Lyapunov Neural Network: Adaptive Stability Certification for Safe Learning of Dynamical Systems, Paper, Code (Accepted by CoRL 2018)
OptLayer - Practical Constrained Optimization for Deep Reinforcement Learning in the Real World, Paper, Not Find Code (Accepted by ICRA 2018)
Safe learning of quadrotor dynamics using barrier certificates, Paper, Not Find Code (Accepted by ICRA 2018)
Safe reinforcement learning on autonomous vehicles, Paper, Not Find Code (Accepted by IROS 2018)
Trial without error: Towards safe reinforcement learning via human intervention, Paper, Code (Accepted by AAMAS 2018)
Safe reinforcement learning: Learning with supervision using a constraint-admissible set, Paper, Not Find Code (Accepted by Annual American Control Conference (ACC) 2018)
A General Safety Framework for Learning-Based Control in Uncertain Robotic Systems, Paper, Not Find Code (Accepted by IEEE Transactions on Automatic Control 2018)
Safe exploration algorithms for reinforcement learning controllers, Paper, Not Find Code (Accepted by IEEE transactions on neural networks and learning systems 2018)
Verification and repair of control policies for safe reinforcement learning, Paper, Not Find Code (Accepted by Applied Intelligence, 2018)
Safe Exploration in Continuous Action Spaces, Paper, Code, (only Arxiv, 2018, citation 200+)
Safe exploration of nonlinear dynamical systems: A predictive safety filter for reinforcement learning, Paper, Not Find Code (Arxiv, 2018, citation 40+)
Batch policy learning under constraints, Paper, Code (Accepted by ICML 2019)
Safe Policy Improvement with Baseline Bootstrapping, Paper, Not Find Code (Accepted by ICML 2019)
Convergent Policy Optimization for Safe Reinforcement Learning, Paper, Code (Accepted by NeurIPS 2019)
Constrained reinforcement learning has zero duality gap, Paper, Not Find Code (Accepted by NeurIPS 2019)
Reinforcement learning with convex constraints, Paper, Code (Accepted by NeurIPS 2019)
Reward constrained policy optimization, Paper, Not Find Code (Accepted by ICLR 2019)
Supervised policy update for deep reinforcement learning, Paper, Code, (Accepted by ICLR 2019)
End-to-end safe reinforcement learning through barrier functions for safety-critical continuous control tasks, Paper, Code (Accepted by AAAI 2019)
Lyapunov-based safe policy optimization for continuous control, Paper, Not Find Code (Accepted by ICML Workshop RL4RealLife 2019)
Safe reinforcement learning with model uncertainty estimates, Paper, Not Find Code (Accepted by ICRA 2019)
Safe reinforcement learning with scene decomposition for navigating complex urban environments, Paper, Code, (Accepted by IV 2019)
Verifiably safe off-model reinforcement learning, Paper, Code (Accepted by InInternational Conference on Tools and Algorithms for the Construction and Analysis of Systems 2019)
Probabilistic policy reuse for safe reinforcement learning, Paper, Not Find Code, (Accepted by ACM Transactions on Autonomous and Adaptive Systems (TAAS), 2019)
Projected stochastic primal-dual method for constrained online learning with kernels, Paper, Not Find Code, (Accepted by IEEE Transactions on Signal Processing, 2019)
Resource constrained deep reinforcement learning, Paper, Not Find Code, (Accepted by 29th International Conference on Automated Planning and Scheduling 2019)
Temporal logic guided safe reinforcement learning using control barrier functions, Paper, Not Find Code (Arxiv, Citation 25+, 2019)
Safe policies for reinforcement learning via primal-dual methods, Paper, Not Find Code (Arxiv, Citation 25+, 2019)
Value constrained model-free continuous control, Paper, Not Find Code (Arxiv, Citation 35+, 2019)
Safe Reinforcement Learning in Constrained Markov Decision Processes (SNO-MDP), Paper, Code (Accepted by ICML 2020)
Responsive Safety in Reinforcement Learning by PID Lagrangian Methods, Paper, Code (Accepted by ICML 2020)
Constrained markov decision processes via backward value functions, Paper, Code (Accepted by ICML 2020)
Projection-Based Constrained Policy Optimization (PCPO), Paper, Code (Accepted by ICLR 2020)
First order constrained optimization in policy space (FOCOPS), Paper, Code (Accepted by NeurIPS 2020)
Safe reinforcement learning via curriculum induction, Paper, Code (Accepted by NeurIPS 2020)
Constrained episodic reinforcement learning in concave-convex and knapsack settings, Paper, Code (Accepted by NeurIPS 2020)
Risk-sensitive reinforcement learning: Near-optimal risk-sample tradeoff in regret, Paper, Not Find Code (Accepted by NeurIPS 2020)
Upper confidence primal-dual reinforcement learning for CMDP with adversarial loss, Paper, Not Find Code (Accepted by NeurIPS 2020)
IPO: Interior-point Policy Optimization under Constraints, Paper, Not Find Code (Accepted by AAAI 2020)
Safe reinforcement learning using robust mpc, Paper, Not Find Code (IEEE Transactions on Automatic Control, 2020)
Safe reinforcement learning via projection on a safe set: How to achieve optimality? Paper, Not Find Code (Accepted by IFAC 2020)
Reinforcement learning for safety-critical control under model uncertainty, using control lyapunov functions and control barrier functions, Paper, Not Find Code (Accepted by RSS 2020)
Learning Transferable Domain Priors for Safe Exploration in Reinforcement Learning, Paper, Code, (Accepted by International Joint Conference on Neural Networks (IJCNN) 2020)
Safe reinforcement learning through meta-learned instincts, Paper, Not Find Code (Accepted by The Conference on Artificial Life 2020)
Learning safe policies with cost-sensitive advantage estimation, Paper, Not Find Code (Openreview 2020)
Safe reinforcement learning using probabilistic shields, Paper, Not Find Code (2020)
A constrained reinforcement learning based approach for network slicing, Paper, Not Find Code (Accepted by IEEE 28th International Conference on Network Protocols (ICNP) 2020)
Safe reinforcement learning: A control barrier function optimization approach, Paper, Not Find Code (Accepted by the International Journal of Robust and Nonlinear Control)
Exploration-exploitation in constrained mdps, Paper, Not Find Code (Arxiv, 2020)
Safe reinforcement learning using advantage-based intervention, Paper, Code (Accepted by ICML 2021)
Shortest-path constrained reinforcement learning for sparse reward tasks, Paper, Code, (Accepted by ICML 2021)
Density constrained reinforcement learning, Paper, Not Find Code (Accepted by ICML 2021)
CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee, Paper, Not Find Code (Accepted by ICML 2021)
Safe reinforcement learning with linear function approximation, Paper, Not Find Code (Accepted by ICML 2021)
Safe Reinforcement Learning by Imagining the Near Future (SMBPO), Paper, Code (Accepted by NeurIPS 2021)
Towards safe reinforcement learning with a safety editor policy, Paper, Code (Accepted by NeurIPS 2021)
Exponential Bellman Equation and Improved Regret Bounds for Risk-Sensitive Reinforcement Learning, Paper, Not Find Code (Accepted by NeurIPS 2021)
Risk-Sensitive Reinforcement Learning: Symmetry, Asymmetry, and Risk-Sample Tradeoff, Paper, Not Find Code (Accepted by NeurIPS 2021)
Safe reinforcement learning with natural language constraints, Paper, Code, (Accepted by NeurIPS 2021)
Learning policies with zero or bounded constraint violation for constrained mdps, Paper, Not Find Code (Accepted by NeurIPS 2021)
Conservative safety critics for exploration, Paper, Not Find Code (Accepted by ICLR 2021)
Wcsac: Worst-case soft actor critic for safety-constrained reinforcement learning, Paper, Not Find Code (Accepted by AAAI 2021)
Risk-averse trust region optimization for reward-volatility reduction, Paper, Not Find Code (Accepted by IJCAI 2021)
AlwaysSafe: Reinforcement Learning Without Safety Constraint Violations During Training, Paper, Code (Accepted by AAMAS 2021)
Safe Continuous Control with Constrained Model-Based Policy Optimization (CMBPO), Paper, Code (Accepted by IROS 2021)
Context-aware safe reinforcement learning for non-stationary environments, Paper, Code (Accepted by ICRA 2021)
Model-based Constrained Reinforcement Learning using Generalized Control Barrier Function, Paper, Code (Accepted by IROS 2021)
Robot Reinforcement Learning on the Constraint Manifold, Paper, Code (Accepted by CoRL 2021)
Provably efficient safe exploration via primal-dual policy optimization, Paper, Not Find Code (Accepted by the International Conference on Artificial Intelligence and Statistics 2021)
Safe model-based reinforcement learning with robust cross-entropy method, Paper, Code (Accepted by ICLR 2021 Workshop on Security and Safety in Machine Learning Systems)
MESA: Offline Meta-RL for Safe Adaptation and Fault Tolerance, Paper, Code (Accepted by Workshop on Safe and Robust Control of Uncertain Systems at NeurIPS 2021)
Safe Reinforcement Learning of Control-Affine Systems with Vertex Networks, Paper, Code (Accepted by Conference on Learning for Dynamics and Control 2021)
Can You Trust Your Autonomous Car? Interpretable and Verifiably Safe Reinforcement Learning, Paper, Not Find Code (Accepted by IV 2021)
Provably safe model-based meta reinforcement learning: An abstraction-based approach, Paper, Not Find Code (Accepted by CDC 2021)
Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones, Paper, Code, (Accepted by IEEE RAL, 2021)
Reinforcement learning control of constrained dynamic systems with uniformly ultimate boundedness stability guarantee, Paper, Not Find Code (Accepted by Automatica, 2021)
A predictive safety filter for learning-based control of constrained nonlinear dynamical systems, Paper, Not Find Code (Accepted by Automatica, 2021)
A simple reward-free approach to constrained reinforcement learning, Paper, Not Find Code (Arxiv, 2021)
State augmented constrained reinforcement learning: Overcoming the limitations of learning with rewards, Paper, Not Find Code (Arxiv, 2021)
DESTA: A Framework for Safe Reinforcement Learning with Markov Games of Intervention, Paper, Not Find Code (Arxiv, 2021)
Safe Exploration in Model-based Reinforcement Learning using Control Barrier Functions, Paper, Not Find Code (Arxiv, 2021)
Constrained Variational Policy Optimization for Safe Reinforcement Learning, Paper, Code (ICML 2022)
Provably efficient model-free constrained rl with linear function approximation, Paper, Not Find Code (NeurIPS 2022)
Constrained Policy Optimization via Bayesian World Models, Paper, Code (ICLR 2022)
Stability-Constrained Markov Decision Processes Using MPC, Paper, Not Find Code (Accepted by Automatica, 2022)
Constrained Reinforcement Learning for Vehicle Motion Planning with Topological Reachability Analysis, Paper, Not Find Code (Accepted by Robotics, 2022)
Triple-Q: A Model-Free Algorithm for Constrained Reinforcement Learning with Sublinear Regret and Zero Constraint Violation, Paper, Code (Accepted by AISTATS 2022)
Safe reinforcement learning using robust action governor, Paper, Not Find Code (Accepted by In Learning for Dynamics and Control, 2022)
A primal-dual approach to constrained markov decision processes, Paper, Not Find Code (Arxiv, 2022)
SAUTE RL: Almost Surely Safe Reinforcement Learning Using State Augmentation, Paper, Not Find Code (Arxiv, 2022)
Finding Safe Zones of policies Markov Decision Processes, Paper, Not Find Code (Arxiv, 2022)
CUP: A Conservative Update Policy Algorithm for Safe Reinforcement Learning, Paper, Code (Arxiv, 2022)
SAFER: Data-Efficient and Safe Reinforcement Learning via Skill Acquisition, Paper, Not Find Code (Arxiv, 2022)
Penalized Proximal Policy Optimization for Safe Reinforcement Learning, Paper, Not Find Code (Arxiv, 2022)
Mean-Semivariance Policy Optimization via Risk-Averse Reinforcement Learning, Paper, Not Find Code (Arxiv, 2022)
Convergence and sample complexity of natural policy gradient primal-dual methods for constrained MDPs, Paper, Not Find Code (Arxiv, 2022)
Guided Safe Shooting: model based reinforcement learning with safety constraints, Paper, Not Find Code (Arxiv, 2022)
Safe Reinforcement Learning via Confidence-Based Filters, Paper, Not Find Code (Arxiv, 2022)
TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning, Paper, Code (Accepted by IEEE RAL, 2022)
Efficient Off-Policy Safe Reinforcement Learning Using Trust Region Conditional Value at Risk, Paper, Not Find Code (Accepted by IEEE RAL, 2022)
Enhancing Safe Exploration Using Safety State Augmentation, Paper, Not Find Code (Arxiv, 2022)
Towards Safe Reinforcement Learning via Constraining Conditional Value-at-Risk, Paper, Not Find Code (Accepted by IJCAI 2022)
Safe reinforcement learning of dynamic high-dimensional robotic tasks: navigation, manipulation, interaction, Paper, Not Find Code (Arxiv, 2022)
Safe Exploration Method for Reinforcement Learning under Existence of Disturbance, Paper, Not Find Code (Arxiv, 2022)
Guiding Safe Exploration with Weakest Preconditions, Paper, Code (Arxiv, 2022)
Temporal logic guided safe model-based reinforcement learning: A hybrid systems approach, Paper, Not Find Code (Accepted by Nonlinear Analysis: Hybrid Systems, 2022)
Provably Safe Reinforcement Learning via Action Projection using Reachability Analysis and Polynomial Zonotopes, Paper, Not Find Code (Arxiv, 2022)
Model-based Safe Deep Reinforcement Learning via a Constrained Proximal Policy Optimization Algorithm, Paper, Code (Arxiv, 2022)
Safe Model-Based Reinforcement Learning with an Uncertainty-Aware Reachability Certificate, Paper, Not Find Code (Arxiv, 2022)
UNIFY: a Unified Policy Designing Framework for Solving Constrained Optimization Problems with Machine Learning, Paper, Not Find Code (Arxiv, 2022)
Enforcing Hard Constraints with Soft Barriers: Safe Reinforcement Learning in Unknown Stochastic Environments, Paper, Not Find Code (Arxiv, 2022)
Safe Reinforcement Learning Using Robust Control Barrier Functions, Paper, Not Find Code (Accepted by IEEE RAL, 2022)
Model-free Neural Lyapunov Control for Safe Robot Navigation, Paper, Code, Demo (Accepted by IROS 2022)
Safe Reinforcement Learning via Probabilistic Logic Shields, Paper, Code (Accepted by IJCAI 2023, Distinguished Paper Award)
Towards robust and safe reinforcement learning with benign off-policy data, Paper, Not Find Code (Accepted by ICML 2023)
Enforcing hard constraints with soft barriers: Safe reinforcement learning in unknown stochastic environments, Paper, Not Find Code (Accepted by ICML 2023)
Safe Exploration Incurs Nearly No Additional Sample Complexity for Reward-free RL, Paper, Not Find Code (Accepted by ICLR 2023)
A CMDP-within-online framework for Meta-Safe Reinforcement Learning, Paper, Not Find Code (Accepted by ICLR 2023)
Datasets and Benchmarks for Offline Safe Reinforcement Learning, Paper, Code, (Accepted by Journal of Data-centric Machine Learning Research)
SCPO: Safe Reinforcement Learning with Safety Critic Policy Optimization, Paper, Code (Arxiv, 2023)
Shielded Reinforcement Learning for Hybrid Systems, Paper (Arxiv), Code (AISOLA, 2023)
Adaptive primal-dual method for safe reinforcement learning, Paper, Not Find Code (Accepted by AAMAS 2024)
Probabilistic constraint for safety-critical reinforcement learning, Paper, Not Find Code (Accepted by TAC)
Generalized constraint for probabilistic safe reinforcement learning, Paper, Not Find Code (Accepted by DCC 2024)
Log Barriers for Safe Black-box Optimization with Application to Safe Reinforcement Learning, Paper, Code (JMLR, 2024)
Provably safe reinforcement learning with step-wise violation constraints, Paper, Not Find Code (Accepted by NeurIPS 2024)
Feasibility Consistent Representation Learning for Safe Reinforcement Learning, Paper, Code, (Accepted by ICML 2024)
Balance Reward and Safety Optimization for Safe Reinforcement Learning: A Perspective of Gradient Manipulation, Paper, Not Find Code (Accepted by AAAI 2024)
Safe Reinforcement Learning with Free-form Natural Language Constraints and Pre-Trained Language Models, Paper, Not Find Code (Accepted by AAMAS 2024)
Enhancing Efficiency of Safe Reinforcement Learning via Sample Manipulation, Paper, Not Find Code (Arxiv, 2024)
Safe and Balanced: A Framework for Constrained Multi-Objective Reinforcement Learning, Paper, Not Find Code (Arxiv, 2024)
Confident Natural Policy Gradient for Local Planning in qπ-realizable Constrained MDPs, Paper, Not Find Code (Arxiv, 2024)
Safe Exploration Using Bayesian World Models and Log-Barrier Optimization, Paper, Code (Arxiv, 2024)
Safe and Balanced: A Framework for Constrained Multi-Objective Reinforcement Learning, Paper, Code (Accepted by IEEE TPAMI 2025)
Reward-Safety Balance in Offline Safe RL via Diffusion Regularization, Paper, Not Find Code (Accepted by NeurIPS 2025)
2.2. Safe Multi-Agent RL Baselines
Multi-Agent Constrained Policy Optimisation (MACPO), Paper, Code (Arxiv, 2021)
MAPPO-Lagrangian, Paper, Code (Arxiv, 2021)
Decentralized policy gradient descent ascent for safe multi-agent reinforcement learning, Paper, Not Find Code (Accepted by AAAI 2021)
Safe multi-agent reinforcement learning via shielding, Paper, Not Find Code (Accepted by AAMAS 2021)
CMIX: Deep Multi-agent Reinforcement Learning with Peak and Average Constraints, Paper, Not Find Code (Accepted by Joint European Conference on Machine Learning and Knowledge Discovery in Databases 2021)
Safe multi-agent reinforcement learning through decentralized multiple control barrier functions, Paper, Not Find Code (Arxiv 2021)
CAMA: A New Framework for Safe Multi-Agent Reinforcement Learning Using Constraint Augmentation, Paper, Not Find Code (Openreview 2022)
Shield decentralization for safe multi-agent reinforcement learning, Paper, Not Find Code (NeurIPS 2022)
Solving Multi-Agent Safe Optimal Control with Distributed Epigraph Form MARL, Paper, Code (RSS 2025)
3. Surveys
A Review of Safe Reinforcement Learning: Methods, Theory and Applications, Paper (IEEE TPAMI, 2024)
State-wise Safe Reinforcement Learning: A Survey, Paper (Accepted by IJCAI 2023)
Policy learning with constraints in model-free reinforcement learning: A survey, Paper (Accepted by IJCAI 2021)
Safe learning in robotics: From learning-based control to safe reinforcement learning, Paper (Accepted by Annual Review of Control, Robotics, and Autonomous Systems, 2021)
Safe learning and optimization techniques: Towards a survey of the state of the art, Paper (Accepted by In International Workshop on the Foundations of Trustworthy AI Integrating Learning, Optimization and Reasoning, 2020)
A comprehensive survey on safe reinforcement learning, Paper (Accepted by Journal of Machine Learning Research, 2015)
4. Theses
Safe Reinforcement Learning to Make Decisions in Robotics, Thesis (PhD thesis, Shangding Gu, TU Munich, 2024)
Safe Exploration in Reinforcement Learning: Theory and Applications in Robotics, Thesis (PhD thesis, Felix Berkenkamp, ETH Zurich, 2019)
Safe reinforcement learning, Thesis (PhD thesis, Philip S. Thomas, University of Massachusetts Amherst, 2015)
5. Book
Constrained Markov decision processes: stochastic modeling, Book, (Eitan Altman, Routledge, 1999)
6. Tutorials
Safe Reinforcement Learning: Bridging Theory and Practice, tutorial, (Ming Jin & Shangding Gu, 2024)
Safe Reinforcement Learning for Smart Grid Control and Operations, tutorial, (Ming Jin & Shangding Gu, 2024)
Safe Reinforcement Learning, tutorial, (Felix Berkenkamp, 2023)
Primal-Dual Methods, tutorial, (Gergely Neu, 2023)
7. Exercise
Primal-Dual Reinforcement Learning, exercise code and exercise Colab, (Germano Gabbianelli, 2023)
Publication
If you find the repository useful, please cite the paper:
About
The repository is for safe reinforcement learning baselines.
Topics
baseline reinforcement-learning robotics safe-reinforcement-learning safe-robot-learning safety
Resources
Readme
Activity
Stars
810 stars
Watchers
9 watching
Forks
104 forks
Report repository
Releases
No releases published
Contributors 5 (5)
Languages
Jupyter Notebook 35.8%
C 35.8%
Julia 15.1%
Python 12.4%
TeX 0.5%
q 0.2%
Other 0.2%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can't perform that action at this time.