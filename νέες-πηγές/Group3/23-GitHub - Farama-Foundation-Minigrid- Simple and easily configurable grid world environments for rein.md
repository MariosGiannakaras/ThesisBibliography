> Source: https://github.com/Farama-Foundation/Minigrid

GitHub - Farama-Foundation/Minigrid: Simple and easily configurable grid world environments for reinforcement learning · GitHub
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
Farama-Foundation / Minigrid Public
Sponsor
Notifications You must be signed in to change notification settings
Fork 645
Star 2.5k
Code
Issues 17
Pull requests 9
Actions
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Security and quality
Insights 
main
23 Branches 15 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
License
More items
     
  
The Minigrid library contains a collection of discrete grid-world environments to conduct research on Reinforcement Learning. The environments follow the Gymnasium standard API and they are designed to be lightweight, fast, and easily customizable.
The documentation website is at minigrid.farama.org, and we have a public discord server (which we also use to coordinate development work) that you can join here: https://discord.gg/bnJ6kubTg6
Note that the library was previously known as gym-minigrid and it has been referenced in several publications. If your publication uses the Minigrid library and you wish for it to be included in the list of publications, please create an issue in the GitHub repository.
See the Project Roadmap for details regarding the long-term plans.
Installation
To install the Minigrid library use pip install minigrid .
We support Python 3.10+ on Linux and macOS. We will accept PRs related to Windows, but do not officially support it.
Environments
The included environments can be divided in two groups. The original Minigrid environments and the BabyAI environments.
Minigrid
The list of the environments that were included in the original Minigrid library can be found in the documentation. These environments have in common a triangle-like agent with a discrete action space that has to navigate a 2D map with different obstacles (Walls, Lava, Dynamic obstacles) depending on the environment. The task to be accomplished is described by a mission string returned by the observation of the agent. These mission tasks include different goal-oriented and hierarchical missions such as picking up boxes, opening doors with keys or navigating a maze to reach a goal location. Each environment provides one or more configurations registered with Gymansium. Each environment is also programmatically tunable in terms of size/complexity, which is useful for curriculum learning or to fine-tune difficulty.
BabyAI
These environments have been imported from the BabyAI project library and the list of environments can also be found in the documentation. The purpose of this collection of environments is to perform research on grounded language learning. The environments are derived from the Minigrid grid-world environments and include an additional functionality that generates synthetic natural-looking instructions (e.g. “put the red ball next to the box on your left”) that command the the agent to navigate the world (including unlocking doors) and move objects to specified locations in order to accomplish the task.
Training an Agent
The rl-starter-files is a repository with examples on how to train Minigrid environments with RL algorithms. This code has been tested and is known to work with this environment. The default hyper-parameters are also known to converge.
Citation
The original gym-minigrid environments were created as part of work done at Mila. The Dynamic obstacles environment were added as part of work done at IAS in TU Darmstadt and the University of Genoa for mobile robot navigation with dynamic obstacles.
To cite this project please use:
If using the BabyAI environments please also cite the following:
About
Simple and easily configurable grid world environments for reinforcement learning
minigrid.farama.org/
Topics
gridworld-environment gymnasium gymnasium-environment
Resources
Readme
License
Cite this repository
Activity
Custom properties
Stars
2.5k stars
Watchers
35 watching
Forks
645 forks
Report repository
Releases 14 (14)
Minigrid 3.1.0 Latest 2 months ago
+ 13 releases
Sponsor this project
 Farama-Foundation Farama Foundation  Sponsor @Farama-Foundation
Learn more about GitHub Sponsors
Used by 830 (830)
@xcoder-es@AFIT-AI-TREC@fork-the-planet@perfloop@Jahid11978 + 827
Contributors 100 (100)
+ 86 contributors
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