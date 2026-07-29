> Source: https://github.com/prasenjit52282/GridWorld

GitHub - prasenjit52282/GridWorld: Gridworld environment creator for testing RL algorithms · GitHub
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
prasenjit52282 / GridWorld Public
Notifications You must be signed in to change notification settings
Fork 10
Star 37
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
5 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
More items
GridWorld
Gridworld is a tool for easily producing custom grid environments to test model-based and model-free classical/DRL Reinforcement Learning algorithms. The package provides an uniform way of defining a grid-world and place agent, goal state, and risky regions. Further, it builds the transition probability matrix (P_sas) and the reward matrix (R_sa) from the defined environment to test planning algorithms. Moreover, for model-free algorithms, the package provides a openai-gym like interface to interact with the environment and explore.
Installation
To install the package in your python(>=3.9) environment you need to run the below commands:
Model-based
See how we define the custom-grid world "a" being agents location, "g" being the goal, "o" being holes, and "w" being walls to obstruct the agent. For a model-based setup we can access the transition and reward dynamics "P_sas" and "R_sa" as shown below.
The policy is shown below:
Model-Free
See how we define the custom-grid world "a" being agents location, "g" being the goal, "o" being holes, and "w" being walls to obstruct the agent. For a model-free setup we can interact with the environment with a openai-gym like interface and observe the <S,A,R,S'> tuples as shown below.
State Transitions are printed:
  
Examples
To elaborate the usage of the package, examples folder contains several classical and Deep Reinforcement Learning algorithms that is tested on this platform. The algorithms are as follow:
Policy Evaluation python examples/policy_eval.py
Policy Iteration python examples/policy_itr.py
Value Iteration python examples/value_itr.py
Safe Monti-Carlo python examples/safe_mc.py
Safe SARSA python examples/safe_sarsa.py
Deep Q Network python examples/dqn.py
Natural Policy Gradient python examples/npg.py
Trust Region Policy Optimization python examples/trpo.py
Proximal Policy Optimization python examples/ppo.py
Testing DRL algorithms
To test any of the above DRL algorithms in the gridworld environment use the following code
The underlined gridworld environment object is defined in "examples/gridenv.py", and the logs of each algorithm is getting stored in the "logs" folder.
File Structure
If you want to have your own agent and goal along with differnt objects to represent the wall and normal states, you can change the respective images in "/gridworld/modules/images"
Contact Me
This is Assignment I & II of CS60077: Reinforcement Learning course in IIT Kharagpur, taught by Dr. Aritra Hazra. I hope that the gridworld tool will be useful in your RL-journey. For questions and general feedback, contact Prasenjit Karmakar.
About
Gridworld environment creator for testing RL algorithms
prasenjit52282.github.io/news/gridworld.html
Topics
custom-environments grid-world q-learning reinforcement-learning-environments
Resources
Readme
MIT license
Activity
Stars
37 stars
Watchers
1 watching
Forks
10 forks
Report repository
Contributors 1 (1)
 prasenjit52282 Prasenjit
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