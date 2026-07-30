> Source: https://github.com/Farama-Foundation/PettingZoo

GitHub - Farama-Foundation/PettingZoo: A standard API for multi-agent reinforcement learning environments, with popular reference environments and related utilities · GitHub
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
Farama-Foundation / PettingZoo Public
Sponsor
Notifications You must be signed in to change notification settings
Fork 511
Star 3.5k
Code
Issues 21
Pull requests 8
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
24 Branches 44 Tags  
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
 
nightly
and
virgilt
Add [RecordVideo](https://github.com/Farama-Foundation/PettingZoo/commit/a735a654566a856ebd45be790646c02f3372b986) wrappers (#1306)
Open commit details success
last week
a735a65
· last week
History
4,679 Commits
Open commit details 
4,679 Commits
.github
.github
Potential fix for code scanning alert no. 1: Workflow does not contai…
2 weeks ago
docs
docs
Add [RecordVideo](https://github.com/Farama-Foundation/PettingZoo/commit/a735a654566a856ebd45be790646c02f3372b986) wrappers (#1306)
last week
pettingzoo
pettingzoo
Add [RecordVideo](https://github.com/Farama-Foundation/PettingZoo/commit/a735a654566a856ebd45be790646c02f3372b986) wrappers (#1306)
last week
test
test
Add [RecordVideo](https://github.com/Farama-Foundation/PettingZoo/commit/a735a654566a856ebd45be790646c02f3372b986) wrappers (#1306)
last week
tutorials
tutorials
docs: update docs & tutorials to use env registry (#1404)
last week
.gitignore
.gitignore
Migrate type checking from pyright to ty (#1344)
last month
.pre-commit-config.yaml
.pre-commit-config.yaml
Replace black + isort with ruff for linting and formatting (#1371)
last month
CITATION.cff
CITATION.cff
Create CITATION.cff (#990)
3 years ago
CODE_OF_CONDUCT.rst
CODE_OF_CONDUCT.rst
Make pre-commit match Gymnasium (add many more pre-commit hook checks) (
3 years ago
CONTRIBUTING.md
CONTRIBUTING.md
1261 proposal modify readme to include yjhan96 to the contact list (#…
last year
LICENSE
LICENSE
Make pre-commit match Gymnasium (add many more pre-commit hook checks) (
3 years ago
MANIFEST.in
MANIFEST.in
Update README with Project Maintainers section (#929)
3 years ago
Makefile
Makefile
refactor: renaming for test auto discovery
4 years ago
README.md
README.md
docs: update docs & tutorials to use env registry (#1404)
last week
conftest.py
conftest.py
Wrappers doctests (#1083)
3 years ago
pettingzoo-text.png
pettingzoo-text.png
Add files via upload
4 years ago
pyproject.toml
pyproject.toml
Add [RecordVideo](https://github.com/Farama-Foundation/PettingZoo/commit/a735a654566a856ebd45be790646c02f3372b986) wrappers (#1306)
last week
setup.py
setup.py
Replace [setup.py](https://github.com/Farama-Foundation/PettingZoo/commit/bd86a472d42f0f01bfa7c14b5b3d8379ee319fdb) with [pyproject.toml](https://github.com/Farama-Foundation/PettingZoo/commit/bd86a472d42f0f01bfa7c14b5b3d8379ee319fdb) (#875)
4 years ago
View all files
Repository files navigation
README
Contributing
License
More items
   
PettingZoo is a Python library for conducting research in multi-agent reinforcement learning, akin to a multi-agent version of Gymnasium.
The documentation website is at pettingzoo.farama.org and we have a public discord server (which we also use to coordinate development work) that you can join here: https://discord.gg/nhvKkYa6qX
Environments
PettingZoo includes the following families of environments:
Atari: Multi-player Atari 2600 games (cooperative, competitive and mixed sum)
Butterfly: Cooperative graphical games developed by us, requiring a high degree of coordination
Classic: Classical games including card games, board games, etc.
SISL: 2 cooperative environments, originally from https://github.com/sisl/MADRL
Installation
To install the base PettingZoo library: pip install pettingzoo .
This does not include dependencies for all families of environments (some environments can be problematic to install on certain systems).
To install the dependencies for one family, use pip install 'pettingzoo[atari]' , or use pip install 'pettingzoo[all]' to install all dependencies.
We support and maintain PettingZoo for Linux and macOS. We will accept PRs related to Windows, but do not officially support it.
Getting started
For an introduction to PettingZoo, see Basic Usage. To create a new environment, see our Environment Creation Tutorial and Custom Environment Examples. For examples of training RL models using PettingZoo see our tutorials:
CleanRL: Implementing PPO: train multiple PPO agents in the Pistonball environment.
Tianshou: Training Agents: train DQN agents in the Tic-Tac-Toe environment.
AgileRL: Training, Curriculums and Self-play: train agents with curriculum learning and self-play in the Connect Four environment.
API
PettingZoo model environments as Agent Environment Cycle (AEC) games, in order to be able to cleanly support all types of multi-agent RL environments under one API and to minimize the potential for certain classes of common bugs.
Using environments in PettingZoo is very similar to Gymnasium, i.e. you initialize an environment via:
Environments can be interacted with in a manner very similar to Gymnasium:
For the complete API documentation, please see https://pettingzoo.farama.org/api/aec/
Parallel API
In certain environments, it's a valid to assume that agents take their actions at the same time. For these games, we offer a secondary API to allow for parallel actions, documented at https://pettingzoo.farama.org/api/parallel/
SuperSuit
SuperSuit is a library that includes all commonly used wrappers in RL (frame stacking, observation, normalization, etc.) for PettingZoo and Gymnasium environments with a nice API. We developed it in lieu of wrappers built into PettingZoo. https://github.com/Farama-Foundation/SuperSuit
Environment Versioning
PettingZoo keeps strict versioning for reproducibility reasons. All environments end in a suffix like "_v0". When changes are made to environments that might impact learning results, the number is increased by one to prevent potential confusion.
Citation
To cite this project in publication, please use
Project Maintainers
Project Manager: Travis Virgil - travis@farama.org
Maintenance for this project is also contributed by the broader Farama team: farama.org/team.
About
A standard API for multi-agent reinforcement learning environments, with popular reference environments and related utilities
pettingzoo.farama.org
Topics
api gymnasium multi-agent-reinforcement-learning multiagent-reinforcement-learning reinforcement-learning
Resources
Readme
License
Contributing
Contributing
Cite this repository
Activity
Custom properties
Stars
3.5k stars
Watchers
16 watching
Forks
511 forks
Report repository
Releases 41 (41)
PettingZoo 1.26.1 Latest 3 months ago
+ 40 releases
Sponsor this project
 Farama-Foundation Farama Foundation  Sponsor @Farama-Foundation
Learn more about GitHub Sponsors
Used by 3.2K (3.2K)
@amais23@fccoelho@pateldivyesh1323@fork-the-planet@perfloop + 3,173
Contributors 135 (135)
+ 121 contributors
Languages
Python 99.9%
Makefile 0.1%
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