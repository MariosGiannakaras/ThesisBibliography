> Source: https://github.com/PKU-Alignment/omnisafe

GitHub - PKU-Alignment/omnisafe: JMLR: OmniSafe is an infrastructural framework for accelerating SafeRL research. · GitHub
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
PKU-Alignment / omnisafe Public
Notifications You must be signed in to change notification settings
Fork 161
Star 1.1k
Code
Issues 23
Pull requests 7
Discussions
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Projects
Security and quality
Insights 
main
1 Branch 7 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Code of conduct
Contributing
Apache-2.0 license
More items 
         
Documentation | Implemented Algorithms | Installation | Getting Started | License
OmniSafe is an infrastructural framework designed to accelerate safe reinforcement learning (RL) research. It provides a comprehensive and reliable benchmark for safe RL algorithms, and also an out-of-box modular toolkit for researchers. SafeRL intends to develop algorithms that minimize the risk of unintended harm or unsafe behavior.
OmniSafe stands as the inaugural unified learning framework in the realm of safe reinforcement learning, aiming to foster the Growth of SafeRL Learning Community. The key features of OmniSafe:
Highly Modular Framework. OmniSafe presents a highly modular framework, incorporating an extensive collection of tens of algorithms tailored for safe reinforcement learning across diverse domains. This framework is versatile due to its abstraction of various algorithm types and well-designed API, using the Adapter and Wrapper design components to bridge gaps and enable seamless interactions between different components. This design allows for easy extension and customization, making it a powerful tool for developers working with different types of algorithms.
High-performance parallel computing acceleration. By harnessing the capabilities of torch.distributed , OmniSafe accelerates the learning process of algorithms with process parallelism. This enables OmniSafe not only to support environment-level asynchronous parallelism but also incorporates agent asynchronous learning. This methodology bolsters training stability and expedites the training process via the deployment of a parallel exploration mechanism. The integration of agent asynchronous learning in OmniSafe underscores its commitment to providing a versatile and robust platform for advancing SafeRL research.
Out-of-box toolkits. OmniSafe offers customizable toolkits for tasks like training, benchmarking, analyzing, and rendering. Tutorials and user-friendly APIs make it easy for beginners and average users, while advanced researchers can enhance their efficiency without complex code.
  
If you find OmniSafe useful or use OmniSafe in your research, please cite it in your publications.
Table of Contents
Quick Start
Installation
Prerequisites
Install from source
Install from PyPI
Implemented Algorithms
Examples
Algorithms Registry
Supported Environments
Customizing your environment
Try with CLI
Getting Started
Important Hints
Quickstart: Colab on the Cloud
Changelog
Citing OmniSafe
Publications using OmniSafe
The OmniSafe Team
License
Quick Start
Installation
Prerequisites
OmniSafe requires Python 3.8+ and PyTorch 1.10+.
We support and test for Python 3.8, 3.9, 3.10 on Linux. Meanwhile, we also support M1 and M2 versions of macOS. We will accept PRs related to Windows, but do not officially support it.
Install from source
Install from PyPI
OmniSafe is hosted in
/
.
Implemented Algorithms
Latest SafeRL Papers
[AAAI 2023] Augmented Proximal Policy Optimization for Safe Reinforcement Learning (APPO)
[NeurIPS 2022] Constrained Update Projection Approach to Safe Policy Optimization (CUP)
[NeurIPS 2022] Effects of Safety State Augmentation on Safe Exploration (Simmer)
[NeurIPS 2022] Model-based Safe Deep Reinforcement Learning via a Constrained Proximal Policy Optimization Algorithm
[ICML 2022] Sauté RL: Almost Surely Safe Reinforcement Learning Using State Augmentation (SauteRL)
[IJCAI 2022] Penalized Proximal Policy Optimization for Safe Reinforcement Learning
[AAAI 2022] Conservative and Adaptive Penalty for Model-Based Safe Reinforcement Learning (CAP)
List of Algorithms On Policy SafeRL
[x] The Lagrange version of PPO (PPO-Lag) [x] The Lagrange version of TRPO (TRPO-Lag) [x] [ICML 2017] Constrained Policy Optimization (CPO) [x] [ICLR 2019] Reward Constrained Policy Optimization (RCPO) [x] [ICML 2020] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods (PID-Lag) [x] [NeurIPS 2020] First Order Constrained Optimization in Policy Space (FOCOPS) [x] [AAAI 2020] IPO: Interior-point Policy Optimization under Constraints (IPO) [x] [ICLR 2020] Projection-Based Constrained Policy Optimization (PCPO) [x] [ICML 2021] CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee [x] [IJCAI 2022] Penalized Proximal Policy Optimization for Safe Reinforcement Learning(P3O)
Off Policy SafeRL
[Preprint 2019] The Lagrangian version of DDPG (DDPGLag)
[Preprint 2019] The Lagrangian version of TD3 (TD3Lag)
[Preprint 2019] The Lagrangian version of SAC (SACLag)
[ICML 2020] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods (DDPGPID)
[ICML 2020] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods (TD3PID)
[ICML 2020] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods (SACPID)
Model-Based SafeRL
[-] [NeurIPS 2021] Safe Reinforcement Learning by Imagining the Near Future (SMBPO) [x] [CoRL 2021 (Oral)] Learning Off-Policy with Online Planning (SafeLOOP) [x] [AAAI 2022] Conservative and Adaptive Penalty for Model-Based Safe Reinforcement Learning (CAP) [x] [NeurIPS 2022] Model-based Safe Deep Reinforcement Learning via a Constrained Proximal Policy Optimization Algorithm [-] [ICLR 2022] Constrained Policy Optimization via Bayesian World Models (LA-MBDA) [x] [ICML 2022 Workshop] Constrained Model-based Reinforcement Learning with Robust Cross-Entropy Method (RCE) [x] [NeurIPS 2018] Constrained Cross-Entropy Method for Safe Reinforcement Learning (CCE)
Offline SafeRL
[x] The Lagrange version of BCQ (BCQ-Lag) [x] The Constrained version of CRR (C-CRR) [-] [AAAI 2022] Constraints Penalized Q-learning for Safe Offline Reinforcement Learning CPQ [x] [ICLR 2022 (Spotlight)] COptiDICE: Offline Constrained Reinforcement Learning via Stationary Distribution Correction Estimation [-] [ICML 2022] Constrained Offline Policy Optimization (COPO)
Others
[-] [RA-L 2021] Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones [x] [ICML 2022] Sauté RL: Almost Surely Safe Reinforcement Learning Using State Augmentation (SauteRL) [x] [NeurIPS 2022] Effects of Safety State Augmentation on Safe Exploration
Examples
Algorithms Registry
Supported Environments
Here is a list of environments that Safety-Gymnasium supports:
For more information about environments, please refer to Safety-Gymnasium.
Customizing your environment
We offer a flexible customized environment interface that allows users to achieve the following without modifying the OmniSafe source code:
Use OmniSafe to train algorithms on customized environments.
Create the the environment with specified personalized parameters.
Complete the recording of environment-specific information in Logger.
We provide step-by-step tutorials on Environment Customization From Scratch and Environment Customization From Community to give you a detailed introduction on how to use this extraordinary feature of OmniSafe.
Note: If you find trouble customizing your environment, please feel free to open an issue or discussion. Pull requests are also welcomed if you're willing to contribute the implementation of your environments interface.
Try with CLI
Getting Started
Important Hints
We have provided benchmark results for various algorithms, including on-policy, off-policy, model-based, and offline approaches, along with parameter tuning analysis. Please refer to the following:
On-Policy
Off-Policy
Model-based
Offline
Quickstart: Colab on the Cloud
Explore OmniSafe easily and quickly through a series of Google Colab notebooks:
Getting Started Introduce the basic usage of OmniSafe so that users can quickly hand it.
CLI Command Introduce how to use the CLI tool of OmniSafe.
We take great pleasure in collaborating with our users to create tutorials in various languages. Please refer to our list of currently supported languages. If you are interested in translating the tutorial into a new language or improving an existing version, kindly submit a PR to us.
Changelog
See CHANGELOG.md.
Publications using OmniSafe
We have compiled a list of papers that use OmniSafe for algorithm implementation or experimentation. If you are willing to include your work in this list, or if you wish to have your implementation officially integrated into OmniSafe, please feel free to contact us.
The OmniSafe Team
OmniSafe is mainly developed by the SafeRL research team directed by Prof. Yaodong Yang. Our SafeRL research team members include Borong Zhang, Jiayi Zhou, JTao Dai, Weidong Huang, Ruiyang Sun, Xuehai Pan and Jiaming Ji. If you have any questions in the process of using OmniSafe, don't hesitate to ask your questions on the GitHub issue page, we will reply to you in 2-3 working days.
License
OmniSafe is released under Apache License 2.0.
About
JMLR: OmniSafe is an infrastructural framework for accelerating SafeRL research.
omnisafe.readthedocs.io/en/latest/
Topics
benchmark constraint-rl constraint-satisfaction-problem deep-learning deep-reinforcement-learning machine-learning pytorch reinforcement-learning safe-reinforcement-learning safe-rl saferl safety-critical safety-gym safety-gymnasium
Resources
Readme
Apache-2.0 license
Code of conduct
Code of conduct
Contributing
Contributing
Activity
Custom properties
Stars
1.1k stars
Watchers
26 watching
Forks
161 forks
Report repository
Releases 7 (7)
v0.5.0 Latest 3 years ago
+ 6 releases
Contributors 16 (16)
+ 2 contributors
Languages
Python 99.3%
Other 0.7%
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