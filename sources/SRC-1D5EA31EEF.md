> Source: https://github.com/google-deepmind/ai-safety-gridworlds

GitHub - google-deepmind/ai-safety-gridworlds: This is a suite of reinforcement learning environments illustrating various safety properties of intelligent agents. · GitHub
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
This repository was archived by the owner on Jul 21, 2023. It is now read-only.
google-deepmind / ai-safety-gridworlds Public archive
Notifications You must be signed in to change notification settings
Fork 126
Star 636
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
Contributing
Apache-2.0 license
More items
AI safety gridworlds
This is a suite of reinforcement learning environments illustrating various safety properties of intelligent agents. These environments are implemented in pycolab, a highly-customisable gridworld game engine with some batteries included.
For more information, see the accompanying research paper.
For the latest list of changes, see CHANGES.md.
Instructions
Open a new terminal window ( iterm2 on Mac, gnome-terminal or xterm on linux work best, avoid tmux / screen ).
Set the terminal colours to xterm-256color by running export TERM=xterm-256color .
Clone the repository using git clone https://github.com/deepmind/ai-safety-gridworlds.git .
Choose an environment from the list below and run it by typing PYTHONPATH=. python -B ai_safety_gridworlds/environments/ENVIRONMENT_NAME.py .
Dependencies
Python 2 (with enum34 support) or Python 3. We tested it with all the commonly used Python minor versions (2.7, 3.4, 3.5, 3.6). Note that the version 2.7.15 might have curses rendering issues in a terminal.
Pycolab which is the gridworlds game engine we use.
Numpy. Our version is 1.14.5. Note that the higher versions don't work with pip tensorflow at the moment.
Abseil Python common libraries.
If you intend to contribute and run the test suite, you will also need Tensorflow, as pycolab relies on it for testing.
We also recommend using a virtual environment. Under the assumption that you have the virtualenv package installed, the setup is as follows.
For python2:
For python3:
Environments
Our suite includes the following environments.
Safe interruptibility: We want to be able to interrupt an agent and override its actions at any time. How can we prevent the agent from learning to avoid interruptions? safe_interruptibility.py
Avoiding side effects: How can we incentivize agents to minimize effects unrelated to their main objectives, especially those that are irreversible or difficult to reverse? side_effects_sokoban.py and conveyor_belt.py
Absent supervisor: How can we ensure that the agent does not behave differently depending on whether it is being supervised? absent_supervisor.py
Reward gaming: How can we design agents that are robust to misspecified reward functions, for example by modeling their uncertainty about the reward function? boat_race.py and tomato_watering.py
Self-modification: Can agents be robust to limited self-modifications, for example if they can increase their exploration rate? whisky-gold.py
Distributional shift: How can we detect and adapt to a data distribution that is different from the training distribution? distributional_shift.py
Robustness to adversaries: How can we ensure the agent's performance does not degrade in the presence of adversaries? friend_foe.py
Safe exploration: How can we ensure satisfying a safety constraint under unknown environment dynamics? island_navigation.py
Our environments are Markov Decision Processes. All environments use a grid of size at most 10x10. Each cell in the grid can be empty, or contain a wall or other objects. These objects are specific to each environment and are explained in the corresponding section in the paper. The agent is located in one cell on the grid and in every step the agent takes one of the actions from the action set A = {left, right, up, down}. Each action modifies the agent's position to the next cell in the corresponding direction unless that cell is a wall or another impassable object, in which case the agent stays put.
The agent interacts with the environment in an episodic setting: at the start of each episode, the environment is reset to its starting configuration (which is possibly randomized). The agent then interacts with the environment until the episode ends, which is specific to each environment. We fix the maximal episode length to 100 steps. Several environments contain a goal cell, depicted as G. If the agent enters the goal cell, it receives a reward of +50 and the episode ends. We also provide a default reward of −1 in every time-step to encourage finishing the episode sooner than later, and use no discounting in the environment.
In the classical reinforcement learning framework, the agent's objective is to maximize the cumulative (visible) reward signal. While this is an important part of the agent's objective, in some problems this does not capture everything that we care about. Instead of the reward function, we evaluate the agent on the performance function that is not observed by the agent. The performance function might or might not be identical to the reward function. In real-world examples, the performance function would only be implicitly defined by the desired behavior the human designer wishes to achieve, but is inaccessible to the agent and the human designer.
About
This is a suite of reinforcement learning environments illustrating various safety properties of intelligent agents.
Resources
Readme
Apache-2.0 license
Contributing
Contributing
Activity
Custom properties
Stars
636 stars
Watchers
2 watching
Forks
126 forks
Report repository
Releases
No releases published
Contributors 5 (5)
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