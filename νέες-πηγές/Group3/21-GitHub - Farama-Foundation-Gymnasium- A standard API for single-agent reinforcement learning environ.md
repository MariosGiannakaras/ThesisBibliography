> Source: https://github.com/Farama-Foundation/Gymnasium

GitHub - Farama-Foundation/Gymnasium: A standard API for single-agent reinforcement learning environments, with popular reference environments and related utilities (formerly Gym) · GitHub
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
Farama-Foundation / Gymnasium Public
Sponsor
Notifications You must be signed in to change notification settings
Fork 1.4k
Star 12.2k
Code
Issues 66
Pull requests 18
Discussions
Actions
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Security and quality
Insights 
main
7 Branches 20 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Contributing
MIT license
More items
      
Gymnasium is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. This is a fork of OpenAI's Gym library by its maintainers (OpenAI handed over maintenance a few years ago to an outside team), and is where future maintenance will occur going forward.
The documentation website is at gymnasium.farama.org, and we have a public discord server (which we also use to coordinate development work) that you can join here: https://discord.gg/bnJ6kubTg6
Environments
Gymnasium includes the following families of environments along with a wide variety of third-party environments
Classic Control - These are classic reinforcement learning based on real-world problems and physics.
Box2D - These environments all involve toy games based around physics control, using box2d based physics and PyGame-based rendering
Toy Text - These environments are designed to be extremely simple, with small discrete state and action spaces, and hence easy to learn. As a result, they are suitable for debugging implementations of reinforcement learning algorithms.
MuJoCo - A physics engine based environments with multi-joint control which are more complex than the Box2D environments.
Atari - Emulator of Atari 2600 ROMs simulated that have a high range of complexity for agents to learn.
Third-party - A number of environments have been created that are compatible with the Gymnasium API. Be aware of the version that the software was created for and use the apply_env_compatibility in gymnasium.make if necessary.
Installation
To install the base Gymnasium library, use pip install gymnasium
This does not include dependencies for all families of environments (there's a massive number, and some can be problematic to install on certain systems). You can install these dependencies for one family like pip install "gymnasium[atari]" or use pip install "gymnasium[all]" to install all dependencies.
We support and test for Python 3.10, 3.11, 3.12, 3.13 and 3.14 on Linux and macOS. We will accept PRs related to Windows, but do not officially support it.
API
The Gymnasium API models environments as simple Python env classes. Creating environment instances and interacting with them is very simple- here's an example using the "CartPole-v1" environment:
Notable Related Libraries
Please note that this is an incomplete list, and just includes libraries that the maintainers most commonly point newcomers to when asked for recommendations.
CleanRL is a learning library based on the Gymnasium API. It is designed to cater to newer people in the field and provides very good reference implementations.
PettingZoo is a multi-agent version of Gymnasium with a number of implemented environments, for example, multi-agent Atari environments.
The Farama Foundation also has a collection of many other environments that are maintained by the same team as Gymnasium and use the Gymnasium API.
Environment Versioning
Gymnasium keeps strict versioning for reproducibility reasons. All environments end in a suffix like "-v0". When changes are made to environments that might impact learning results, the number is increased by one to prevent potential confusion. These were inherited from Gym.
Contributing
We welcome contributions from the community! Please see our CONTRIBUTING.md for details on how to get started.
Support Gymnasium's Development
If you are financially able to do so and would like to support the development of Gymnasium, please join others in the community in donating to us.
Citation
You can cite Gymnasium using our related paper ( https://arxiv.org/abs/2407.17032) as:
About
A standard API for single-agent reinforcement learning environments, with popular reference environments and related utilities (formerly Gym)
gymnasium.farama.org
Topics
api gym reinforcement-learning
Resources
Readme
MIT license
Contributing
Contributing
Cite this repository
Activity
Custom properties
Stars
12.2k stars
Watchers
64 watching
Forks
1.4k forks
Report repository
Releases 20 (20)
v1.3.0 Latest 3 months ago
+ 19 releases
Sponsor this project
 Farama-Foundation Farama Foundation  Sponsor @Farama-Foundation
Learn more about GitHub Sponsors
Used by 22K (22K)
@Billow-Labs@FDSVM@XAGI-Lab@CarlosGIbanez@LoveDoLove-Forked-Projects + 21,878
Contributors 505 (505)
+ 491 contributors
Languages
Python 99.9%
Other 0.1%
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