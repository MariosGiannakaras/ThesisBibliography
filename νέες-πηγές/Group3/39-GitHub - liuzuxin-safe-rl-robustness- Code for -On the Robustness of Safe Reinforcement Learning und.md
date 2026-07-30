> Source: https://github.com/liuzuxin/safe-rl-robustness

GitHub - liuzuxin/safe-rl-robustness: Code for "On the Robustness of Safe Reinforcement Learning under Observational Perturbations" (ICLR 2023) · GitHub
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
liuzuxin / safe-rl-robustness Public
Notifications You must be signed in to change notification settings
Fork 5
Star 46
Code
Issues 0
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
1 Branch 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
More items
On the Robustness of Safe Reinforcement Learning under Observational Pertubrations
This project provides the open source implementation of the robust safe RL introduced in the ICLR 2023 paper: "On the Robustness of Safe Reinforcement Learning under Observational Pertubrations" (Liu, et al. 2023).
Safe RL trains a policy to maximize the reward while satisfying constraints. While prior works focus on the performance optimality, we find that the optimal solutions of many safe RL problems are not robust and safe against carefully designed observational perturbations. We propose two adversarial attacks - one maximizes the cost and the other maximizes the reward. One interesting and counter-intuitive finding is that the maximum reward attack is strong, as it can both induce unsafe behaviors and make the attack stealthy by maintaining the reward. We further propose a defense method based on adversarial training, which can make the agent stay safe under attacks. Video demos are available at the project webpage.
If you find this code useful, consider to cite:
Table of Contents
Environment setup
System requirements
Installation
How to run experiments
Pretrained weights
Acknowledgments
The structure of this repo is as follows:
Environment setup
System requirements
The repo is tested in Ubuntu 20.04 and should be fine with Ubuntu 18.04
We recommend to use Anaconda3 for python env management
Installation
Activate a python 3.7+ virtual anaconda env, then install the bullet_safety_gym simulation environment:
After switching back to the repo root folder, install the dependencies that are listed in requirement.txt and the rsrl library:
Then install pytorch based on your system configurations, see instructions here. For example, installing a cpu-only version pytorch via Anaconda3 by the following command:
The MAD attacker requires pysgmcmc library for optimization. Install it by:
How to run experiments
To run a single experiment:
To run multiple experiments in parallel:
To evaluate a trained model, run:
To evaluate multiple trained model in parallel:
The complete hyper-parameters can be found in script/config/config_robust_ppo.yaml .
In particular, PPO-Lagrangian has different robust training modes, which are specified by the rs_mode parameter. We detail the modes in the following table.
The proposed adversarial training methods correspond to the max_cost, max_reward modes.
For SA-PPOL series, the modes are kl, klmc, klmr . The SA-PPOL with the original MAD attacker is the kl mode, the SA-PPOL method with the MC and MR attackers are klmc and klmr respectively.
Note that FOCOPS also supports the adversarail training modes max_cost, max_reward and uniform, vanilla .
Pretrained weights
The pretrained weights are available at here.
Acknowledgments
Part of the code is based on several public repos:
https://github.com/SvenGronauer/Bullet-Safety-Gym, note that our BulletSafetyGym is modified based on the original one. The major modification is the simulation step where we increase it to reduce the total training time without sacrifacing too much accuracy.
https://github.com/openai/spinningup
About
Code for "On the Robustness of Safe Reinforcement Learning under Observational Perturbations" (ICLR 2023)
Resources
Readme
MIT license
Activity
Stars
46 stars
Watchers
1 watching
Forks
5 forks
Report repository
Releases
No releases published
Contributors 2 (2)
 Ja4822 Zijian Guo
 liuzuxin Zuxin
Languages
Python 97.5%
Jupyter Notebook 2.5%
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