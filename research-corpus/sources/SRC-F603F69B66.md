> Source: https://github.com/taodav/pobax

GitHub - taodav/pobax: Partially Observable Benchmarks in JAX · GitHub
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
taodav / pobax Public
Notifications You must be signed in to change notification settings
Fork 7
Star 25
Code
Issues 6
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
4 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Apache-2.0 license
More items
POBAX: Partially Observable Benchmarks in JAX
POBAX is a reinforcement learning benchmark that tests all forms of partial observability.
POBAX has been accepted to RLC 2025. Check out our paper!
The benchmark is entirely written in JAX, allowing for fast, GPU-scalable experimentation.
Environments
POBAX includes environments (as well as recommended hyperparameter settings) across diverse forms of partial observability. We list our environments from smallest to largest (in terms of neural network size requirements for PPO RNN):
Experimental results on memory-based deep reinforcement learning algorithms are shown here and in our work.
Basic Usage
Installation
The latest pobax version can be installed via PyPI:
To develop for the pobax package, create a fork and clone the repo:
Installing Madrona_MJX (Optional)
POBAX's pixel-based continuous control environments ( ant-pixels , halfcheetah-pixels , hopper-pixels , walker2d-pixels ) require the Madrona_MJX renderer for GPU-accelerated rendering.
Installation:
Requirements:
CUDA 12.6.3 or compatible versions
GPU support
Note: Madrona_MJX currently does not support jax.vmap , so experiments must run with a single seed at a time. See scripts/hyperparams/visual_mujoco/ant/best/ant_ppo_madrona_best.py for an example configuration.
Compilation: The first time you run a Madrona_MJX environment, the renderer will compile (takes ~4 minutes on an RTX 3090). You'll see outputs like this:
Here's an example of how to run a pixel-based Madrona_MJX ant environment:
Agents
POBAX includes algorithms loosely based on the PureJAXRL framework, with algorithms based on proximal policy optimization (PPO). These include:
Recurrent PPO,
λ-discrepancy,
GTrXL.
Memoryless versions of the recurrent PPO algorithm is also included with the --memoryless flag.
Here's an example script of how to run a recurrent PPO agent on T-Maze:
Here's a small example of how to sweep hyperparameters using recurrent PPO agent in RockSample(11, 11):
This script will run an experiment over 5 seeds over 5M steps on CPU with entropy coefficient = 0.2 , GAE lambda = 0.7 and 16 parallel environments for each run, while sweeping learning rate = 0.0025, 0.00025 . For more information on running experiments with POBAX, check out the EXPERIMENTS.md file.
Hyperparameters and their descriptions can be found in pobax/config.py . Any hyperparameter that has a list type can be swept.
Citation
About
Partially Observable Benchmarks in JAX
Resources
Readme
Apache-2.0 license
Activity
Stars
25 stars
Watchers
2 watching
Forks
7 forks
Report repository
Releases
No releases published
Contributors 3 (3)
 taodav David Tao
 KevinGuo27 Kaicheng Guo
 noahfarr Noah Farr
Languages
Python 99.1%
Shell 0.9%
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