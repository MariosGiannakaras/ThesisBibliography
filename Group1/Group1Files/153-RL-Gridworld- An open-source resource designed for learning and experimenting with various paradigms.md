> Source: https://github.com/kitaird/rl-gridworld

GitHub - kitaird/rl-gridworld: RL-Gridworld: An open-source resource designed for learning and experimenting with various paradigms in reinforcement learning (RL) · GitHub
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
kitaird / rl-gridworld Public
Notifications You must be signed in to change notification settings
Fork 0
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
develop
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
More items
RL-Gridworld: A RL-Learning Environment
Welcome to the RL-Gridworld, an open-source resource designed for learning and experimenting with various paradigms in reinforcement learning (RL). This library provides a versatile gridworld environment that can be easily extended and customized, demonstrating how RL-Algorithms achieve their solutions.
All control approaches can be implemented in the respective file and can be selected in the GUI of the GridWorld example.
Features
Gymnasium Interface: The gridworld environment is designed to be compatible with the popular RL-interface Gymnasium, allowing users to transition their gained knowledge easily to more sophisticated DRL-libraries.
Extensible Gridworld Environment: At the core of this library is the gridworld environment, a simple yet powerful tool for demonstrating key concepts in RL. Users can easily modify and extend this environment to suit their learning and research needs.
Support for Multiple RL Paradigms: The library is built to demonstrate a variety of reinforcement learning techniques (see Sutton & Barto, Reinforcement Learning: An Introduction, 2018), including:
Dynamic Programming:
Policy Iteration
Value Iteration
Monte Carlo Methods:
On-Policy Monte-Carlo Control (w/o Exploring Starts)
Off-Policy Monte-Carlo Control
Temporal Difference Learning:
Sarsa
Expected Sarsa
Q-Learning
N-Step bootstrapping:
N-Step Sarsa
N-Step
N-Step Tree Backup
Off-Policy N-Step Sarsa
Off-Policy N-Step Q(sigma)
Environment dynamics
The environment acts the following way, but can be configured freely as described below:
Every move results in a reward of -1
Moving into the wall will also yield a reward of -1 , however the agent's position doesn't change
Moving out of the grid will also yield a reward of -1 , however the agent's position doesn't change
When being in a terminal state, no more action is possible
Configuration
The gridworld layout can be adjusted in the src/env/gridworld-config.yml file. Multiple terminal states are possible. Rewards and terminal states are decoupled. The dimensions of the grid are adjustable. One can try out multiple sizes and test each algorithm with it. It can be configured the following way:
Gridworld configuration
Horizon: The maximum number of steps the agent can take in the environment (defines truncation)
Action_space: The possible actions the agent can take (cardinal_moves: [North, South, East, West], queen_moves: [N, S, E, W, NE, NW, SE, SW])
Layout:
s : indicates the agent's starting position
w : indicates a wall
. : indicates an accessible state
t : indicates a terminal state
Rewards:
# : indicates a reward issued when entering that state (where # is any int or float, else the default reward is 0 )
Reward_per_step: The reward issued for every step the agent takes
Installing and running the program
All required packages are in resources/requirements.txt . To install the requirements, execute pip install -r resources/requirements.txt . Best practice is to create a 'venv' with python version 3.12, then install the resources/requirements.txt using the command above with the created venv.
Run the __main__.py file with python 3.12 to run the program!
For Mac users if there are issues with _tkinter , installing python-tk might be helpful.
Example images
Here are some examples of the project with implemented algorithms:
Empty Gridworld
Empty Gridworld with Agent starting position
Initialised Action Values
Example images using Sarsa
Converged Action Values
Optimal Policy
Episode Returns
References
The rl_board.py is based on the source code ot the python package game2dboard which uses the provided game2dboard-MIT-Licence under resources/game2dboard-LICENSE.txt . The initial board.py from mjbrusso/game2dboard was extended to contain additional buttons and logic for the purpose of this project.
License
This project is licensed under the MIT License - see the MIT-Licence file for details.
Citation
If you find this project helpful and use it, please cite it like so:
About
RL-Gridworld: An open-source resource designed for learning and experimenting with various paradigms in reinforcement learning (RL)
Resources
Readme
MIT license
Cite this repository
Activity
Stars
4 stars
Watchers
1 watching
Forks
0 forks
Report repository
Releases
No releases published
Contributors 1 (1)
 kitaird Adi
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