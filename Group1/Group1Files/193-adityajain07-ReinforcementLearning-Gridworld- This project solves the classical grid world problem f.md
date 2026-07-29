> Source: https://github.com/adityajain07/ReinforcementLearning-Gridworld

GitHub - adityajain07/ReinforcementLearning-Gridworld: This project solves the classical grid world problem first with DP methods of RL like Policy Iteration and Value Iteration. Q learning is implemented too. Q learning is then implemented with changing positions of obstacles in the grid. · GitHub
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
adityajain07 / ReinforcementLearning-Gridworld Public
Notifications You must be signed in to change notification settings
Fork 3
Star 2
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
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
More items
RL_Gridworld
Motivation
In a not so distant future, when we will have a connected network of autonomous cars on the roads, can we leverage the use of spatial and temporal information obtained from different vehicles to make better decisions regarding cruise speed, overtaking and lane-changing?
Problem Statement
With the above motivation, we are scaling down the problem to a grid-like environment where different cells represents their state (occupied/free of obstacle) and the agent has to travel from the start to the goal position (or cell) using RL techniques, thus maximizing the overall rewards. In addition to above:
Agent can query the state of (any/deterministic) k cells in the grid at each iteration and make decisions accordingly
Obstacles may also change their positions in the grid (just like cars on the road) at each iteration With the above scenario, can the agent cover the distance in the shortest time as well as maximize the total reward?
Methodology
This project solves the classical grid world problem with different scenarios. Note: All the experiments haven been performed on a 4x4 grid
We first implement Dynamic Programming methods of RL i.e. Policy Iteration and Value Iteration. The results are then compared with BFS.
We then place static obstacles deterministically in the grid and and run the above DP methods. We also run Q learning on the same.
Then we build a scenario in which the obstacles change their position in every episode (but drawn from the same distribution). We then run a modified version of Q learning on the same.
About
This project solves the classical grid world problem first with DP methods of RL like Policy Iteration and Value Iteration. Q learning is implemented too. Q learning is then implemented with changing positions of obstacles in the grid.
Resources
Readme
Activity
Stars
2 stars
Watchers
2 watching
Forks
3 forks
Report repository
Releases
No releases published
Contributors 2 (2)
 manasimalik Manasi Malik
 adityajain07 Aditya Jain
Languages
Jupyter Notebook 99.9%
MATLAB 0.1%
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