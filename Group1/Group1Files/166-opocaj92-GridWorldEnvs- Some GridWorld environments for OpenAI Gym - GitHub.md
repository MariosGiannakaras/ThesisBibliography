> Source: https://github.com/opocaj92/GridWorldEnvs

GitHub - opocaj92/GridWorldEnvs: Some GridWorld environments for OpenAI Gym · GitHub
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
opocaj92 / GridWorldEnvs Public
Notifications You must be signed in to change notification settings
Fork 5
Star 4
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
master
1 Branch 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
More items
GridWorldEnvs
Some GridWorld environments for OpenAI Gym
Problem
GridWorld is a simple and famous benchmark problem in Reinforcement Learning. The environment presents a rectangular grid in which an agent, starting from a certain cell, has to reach another cell defined as a goal, observing only its actual position. The agent receives a certain reward when it reachs the goal while moving in the environment. There are a lot of variations to this problem, like having multiple goal cells, walls (cells that the agent cannot pass by), bombs (cells that give a big negative reward if stepped) or uncertainty in the actions' outcome.
Also multi-agent versions have been proposed, like the Pursers-Evaders problem, in which a set of pursuers (our agents) have to reach coordinately the location of the evaders in order to catch them, while also them are moving in the environment (in out environment they move at random, but they could also learn how to evade). The problem ends when all the evaders have been catched.
Overview
This little environment for OpenAI Gym allows to learn these problems. The files gym_gridworld/envs/GridWorld.py and gym_gridworld/envs/PursuersEvaders.py represent the two different problems respectively. They can simply be used as any other OpenAI Gym environment with env = gym.make("GridWorld-v0") and env = gym.make("PursuersEvaders-v0") . Custom maps can be made using text file similar to the provided examples (files named map#.txt are for the GridWorld environment, while files named mmap#.txt are for the PursuersEvaders one).
The two files q_learning.py and multiagent_q_learning.py are two example solvers for these two environments using the Q-Learning algorithm.
Author
Castellini Jacopo
About
Some GridWorld environments for OpenAI Gym
Topics
multi-agent-systems openai-gym reinforcement-learning
Resources
Readme
Activity
Stars
4 stars
Watchers
1 watching
Forks
5 forks
Report repository
Releases
No releases published
Contributors 3 (3)
 opocaj92 Jacopo Castellini
 dosssman Rousslan F.J. Dossa
 hassaanhashmi Hassaan Hashmi
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