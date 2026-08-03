> Source: https://github.com/SafeRL-Lab/Robust-Gymnasium

GitHub - SafeRL-Lab/Robust-Gymnasium: [ICLR 2025] Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning. · GitHub
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
Uh oh!
There was an error while loading. Please reload this page.
SafeRL-Lab / Robust-Gymnasium Public
Notifications You must be signed in to change notification settings
Fork 11
Star 101
Code
Issues 2
Pull requests 0
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
3 Branches 1 Tag  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
More items
Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning
Paper
· Website
· Code
· Tutorial
· Issue   
This benchmark aims to advance robust reinforcement learning (RL) for real-world applications and domain adaptation. The benchmark provides a comprehensive set of tasks that cover various robustness requirements in the face of uncertainty on state, action, reward and environmental dynamics, and span diverse applications including control, robot manipulations, dexterous hand, and so on (This repository is under actively development. We appreciate any constructive comments and suggestions).
🔥 Benchmark Features:
High Modularity: It is designed for flexible adaptation to a variety of research needs, featuring high modularity to support a wide range of experiments.
Task Coverage: It provides a comprehensive set of tasks to evaluate robustness across different RL scenarios (at least 170 tasks).
High Compatibility: It can be seamless and compatible with a wide range of existing environments.
Support Vectorized Environments: It can be useful to enable parallel processing of multiple environments for efficient experimentation.
Support for New Gym API: It fully supports the latest standards in Gym API, facilitating easy integration and expansion.
LLMs Guide Robust Learning: Leverage LLMs to set robust parameters (LLMs as adversary policies).
🔥 Benchmark Tasks:
Robust MuJoCo Tasks: Tackle complex simulations with enhanced robustness.
Robust Box2D Tasks: Engage with 2D physics environments designed for robustness evaluation.
Robust Robot Manipulation Tasks: Robust robotic manipulation with Kuka and Franka robots.
Robust Safety Tasks: Prioritize safety in robustness evaluation.
Robust Android Hand Tasks: Explore sophisticated hand manipulation challenges in robust settings.
Robust Dexterous Tasks: Advance the robust capabilities in dexterous robotics.
Robust Fetch Manipulation Tasks: Robust object manipulation with Fetch robots.
Robust Robot Kitchen Tasks: Robust manipulation in Kitchen environments with robots.
Robust Maze Tasks: Robust navigation robots.
Robust Humanoid Robot Tasks: Humanoid robot control with robust settings.
Robust Multi-Agent Tasks: Facilitate robust coordination among multiple agents.
Each of these robust tasks incorporates robust elements such as robust observations, actions, reward signals, and dynamics to evaluate the robustness of RL algorithms.
🔥 Our Vision: We hope this benchmark serves as a useful platform for pushing the boundaries of RL in real-world problems --- promoting robustness and domain adaptation ability!
Any suggestions and issues are welcome. If you have any questions, please propose an issue or pull request, or contact us directly via email at shangding.gu@berkeley.edu; we will respond to you in one week.
Content
Introduction
Environments and Tasks
Disruptor Module for Perturbations
Tutorials
Installation of the Environment
Quick start
Selected Demos
Robust MuJoCo Tasks
Robust MuJoCo Variant Tasks
Robust Robot Manipulation Tasks
Robust Dexterous Hand and Maze Tasks
Citation
Acknowledgments
Introduction
Reinforcement Learning against Uncertainty/Perturbation
Reinforcement learning (RL) problems is formulated as that an agent seeks a policy that optimizes the long-term expected return through interacting with an environment. While standard RL has been heavily investigated recently, its use can be significantly hampered in practice due to noise, malicious attacks, the sim-to-real gap, domain generalization requirements, or even a combination of those and more factors. Consequently, in addition to maximizing the cumulative rewards, robustness to unexpected uncertainty/perturbation emerges as another critical goal for RL, especially in high-stakes applications such as robotics, financial investments, autonomous driving, and so on. This leads to a surge of considerations of more robust RL algorithms for different problems, termed as robust RL, including but not limited to single-agent RL, safe RL, and multi-agent RL.
A Unified Robust Reinforcement Learning Framework: MDP with Disruption
Robust RL problems typically consists of three modules
An agent (a policy): tries to learn a strategy π (a policy) based on the observation from the environment to achieve optimal long-term return
An environment/task: a task that determine the agents' immediate reward r ( ⋅ | s , a ) and the physical or logical dynamics (transition function P t ( ⋅ | s , a ) )
The disruptor module: represents the uncertainty/perturbation events that happens during any parts of the interaction process between the agent and environment, with different modes, sources, and frequencies.
We illustrate the framework of robust RL for single-agent problems for instance: 
Robust-Gymnasium: A Unified Modular Benchmark
This benchmark support various 1) environments/tasks and 2) disruptors （perturbations to the interaction process). This allows users to design and evaluate different algorithms in different application scenarios when encountering diverse uncertainty issues. Switch to the sections below if you want to get a quick glance of which environments and perturbations that Robust-Gymnasium support.
Environments and Tasks
Disruptor Module for Perturbations
Environments and Tasks
Tasks: Random, Adversary, Semantic Tasks (Robot Manipulation Tasks).
Robust MuJoCo Tasks
Robust Boxd2d Tasks
Robust Robot Manipulation Tasks
Robust Safety Tasks
Robust Androit Hand Tasks
Robust Dexterous Tasks
Robust Fetch Manipulation Tasks
Robust Robot Kitchen Tasks
Robust Maze Tasks
Robust Multi-Agent Tasks
Robust Humanoid Tasks
Disruptor Module for Perturbations
Before introducing the disruptor module, we recall that RL problem can be formulated as a process involving several key concepts: an agent, state, action, reward, and an environment. Specifically, at each time t , the environment generate a state s t and a reward r t and send them to the agent, and the agent choose an action a t and send back to the environment to generate the next state s t + 1 conditioned on the current state s t and the action a t .
Considering this, in this benchmark, we consider extensive potential uncertainty/disturbance/generalizable events that happen in this process (including both training and testing phases) during any places, with any modes, and at any time, summarized in the following table.
Those perturbation events can be generally categorized from three different perspectives:
Sources: which component is perturbed/attacked.
Agent's observed state: The agent observes a noisy/attacked 'state' s ~ t (diverge from the real state s t ) and use it as the input of its policy to determine the action.
Agent's observed reward: The agent observes a noisy/attacked 'reward' r ~ t (differ from the real immediate reward ( r t ) obtained from the environment) and construct their policy according to it.
Action: The action a t chosen by the agent is contaminated before sent to the environment. Namely, a perturbed action a ~ t serves as the input of the environment for the next step.
Environment: an environment includes both immediate reward function r and dynamic function P t . An agent may interact with a shifted or unstationary environment.
Modes: what kind of perturbation is imposed on.
Random: the nominal variable will be added by some random noise following some distributions, such as Gaussian, or uniform distribution. This mode can be used to all perturbation sources.
Adversarial: an adversarial attacker will choose the perturbed output within some admissible set to degrade the agent's performance. This mode can be used to the perturbations towards observation and action.
Set arbitrarily: An environment can be set to any fixed one within some pre-scribed uncertainty set of the environments.
Semantic-domain-shifted: We offer some partially-similar environment/tasks while with some semantic diversity (such as different goals) for domain generalization or transfer learning tasks.
Frequency: when does the perturbation happen. Viewed through the lens of time, the perturbations can happen at different period during training and testing process, even with different frequency. We provide interactive modes that support step-wise varying interaction between disruptors, agents, and environments. So the user can choose to apply perturbations at any point in the dimension of time in any way.
💡 Tip
Not all environments support all kinds of disruptors (perturbations). Please refer to the above section (Environments and Tasks) for more information.
Tutorials
Here, we provide a step-by-step tutorial for users to create and use a domain-shifted/noisy task by choosing any environment/task combined with any uncertainty factor to perturb some original environment, see the link.
Installation of the Environments
Create an environment (requires Conda installation): We are currently developing our environments using a Linux system. The operating system version of our server is 20.04.3 LTS. Use the following command to create a new Conda environment named robustgymnasium with Python 3.11:
Activate the newly created environment:
Install dependency packages: Install the necessary packages using pip. Make sure you are in the project directory where the setup.py file is located:
(Optional) Install with uv If you prefer using uv for faster environment setup:
Testing the Tasks
To run the tests, navigate to the examples directory and Test. te the test script, e.g.,
Ensure you follow these steps to set up and test the environment properly. Adjust paths and versions as necessary based on your specific setup requirements.
If you met some issues, please check the existing solutions for the reported issues, which could help you address your issue.
Selected Demos
Robust MuJoCo Tasks
                                
These demonstrations are from version 4 of the MuJoCo tasks with robust settings.
Robust MuJoCo Variant Tasks
                                
These demonstrations are Robust MuJoCo variant tasks with robust settings.
Robust Robot Manipulation Tasks
                                            
These demonstrations are from robot manipulation tasks with robust settings.
Robust Dexterous Hand and Maze Tasks
                                      
These demonstrations are from dexterous hand and maze tasks with robust settings.
LunarLander Experiments with Robust Gymnasium
This repository contains a focused set of reinforcement learning experiments on LunarLander-v3 using the Robust Gymnasium interface.
It is designed as a practical benchmark to compare classic and modern RL methods under:
standard training (no perturbation),
perturbation-based robustness tests,
delayed/sparse reward settings,
value-estimation bias analysis.
What is included
Algorithms
DQN
Double DQN
Dueling Double DQN (+ PER)
PPO
A2C (value critic and Q critic variants)
REINFORCE
Experiment themes
Baseline learning on LunarLander-v3
Robustness to perturbations (state noise / reward noise)
Delayed reward credit assignment
Q-value overestimation bias (DQN vs Double DQN)
Value-Advantage decomposition analysis (Dueling architecture)
Project structure (LunarLander v3-Discrete)
Quick start
Run experiments
From repository root:
Notes on Robust Gymnasium interface
The scripts use Robust Gymnasium's dict-based step input:
Set perturbations with fields in robust_config (for example noise_factor , noise_type , noise_sigma ).
Typical outputs
Depending on script, outputs include:
training curves ( .png ),
saved models ( .pth / .pt ),
evaluation logs ( .csv / .json ),
rollout visualizations ( .gif / .mp4 ),
experiment summaries ( .txt ).
Citation
If you find the repository useful, please cite the study
Acknowledgments
We thank the contributors from MuJoCo, Gymnasium, Humanoid-bench and Robosuite.
About
[ICLR 2025] Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning.
robust-gym.github.io
Topics
benchmark manipulation multi-agent-reinforcement-learning multi-agent-systems real-world-applications reinforcement-learning robot-learning robotics robust-reinforcement-learning robustness safe-reinforcement-learning safety
Resources
Readme
MIT license
Activity
Custom properties
Stars
101 stars
Watchers
2 watching
Forks
11 forks
Report repository
Releases
1 tag
Contributors 7 (7)
Languages
Python 100%
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