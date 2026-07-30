> Source: https://github.com/zaiyan-x/RFQI

GitHub - zaiyan-x/RFQI: Implementation of Robust Reinforcement Learning using Offline Data [NeurIPS'22] · GitHub
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
zaiyan-x / RFQI Public
Notifications You must be signed in to change notification settings
Fork 4
Star 25
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
Robust Reinforcement Learning using Offline Data
Implementation of the algorithm Robust Fitted Q-Iteration (RFQI). RFQI is introduced in our paper Robust Reinforcement Learning using Offline Data (NeurIPS'22). This implementation of RFQI is based on the implementation of BCQ and the implementation of PQL.
Our method is tested in OpenAI gym discrete control task, CartPole, and two MuJoCo continuous control tasks, Hopper and HalfCheetah, using the D4RL benchmark. Thus it is required that MuJoCo and D4RL are both installed prior to using this repo.
Setup
Install requirements:
Next, you need to properly register the perturbed Gym environments which are placed under the folder perturbed_env. A recommended way to do this: first, place cartpole_perturbed.py under gym/envs/classic_control, hopper_perturbed.py and half_cheetah_perturbed.py under gym/envs/mujoco. Then add the following to_init_ **.py under gym/envs:
You can test this by running:
After installing MuJoCo and D4RL, you can run the following script to download D4RL offline data and make it conform to our format, or you can directly go to TL;DR section below:
Training and Testing of MuJoCo Infographics: Robust MuJoCo Gym
The nominal stochastic probability transition model on which we train our policies is the vanilla MuJoCo setup inducing transition stochasticity using traditional action randomizations from BCQ and PQL implementations. Finally, we evaluate the trained policies deployed on physics-informed perturbed MuJoCo environments.
TL;DR
Here you can find shell scripts that take you directly from offline data generation to evaluation results.
To get all data, run
To get all results, run
To evaluate all pre-trained models, run
Detailed instructions
To generate the epsilon-greedy dataset for CartPole-v0 with epsilon=0.3 , run the following:
To generate the mixed dataset specified in Appendix E.1, run the following:
To train an RFQI policy on Hopper-v3 with d4rl-hopper-medium-v0 and uncertainty hyperparameter rho=0.5 , please run:
You can also train an RFQI policy on Hopper-v3 with mixed dataset and uncertainty hyperparameter rho=0.5 by running
Miscellaneous
If you are using a remote machine to run this repo, please remember to assign a display/virtual display for the evaluation suite to properly generate gifs.
Citation
Please consider citing our repository and paper if you find it useful in your research directions.
About
Implementation of Robust Reinforcement Learning using Offline Data [NeurIPS'22]
Topics
offline-reinforcement-learning reinforcement-learning
Resources
Readme
MIT license
Activity
Stars
25 stars
Watchers
1 watching
Forks
4 forks
Report repository
Releases
No releases published
Contributors 1 (1)
 zaiyan-x Zaiyan Xu
Languages
Python 99.2%
Shell 0.8%
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