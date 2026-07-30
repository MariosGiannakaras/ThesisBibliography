> Source: https://github.com/marekpetrik/RAAM

GitHub - marekpetrik/RAAM: Robust and Approximate Markov Decision Processes · GitHub
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
marekpetrik / RAAM Public
Notifications You must be signed in to change notification settings
Fork 5
Star 12
Code
Issues 0
Pull requests 0
Actions
Projects
Wiki
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Wiki
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
MIT license
More items 
RAAM: Robust and Approximate Markov Decision Processes
A simple and easy to use Python library to solve Markov decision processes and robust Markov decision processes. The library includes mostly helper functions for the CRAAM python interface. In particular, it contains basic simulation routines, approximate dynamic programming through state aggregation, and the construction of MDPs from simulation.
The library supports standard finite or infinite horizon discounted MDPs [Puterman2005]. The library assumes maximization over actions. The states and actions must be finite.
The robust model extends the regular MDPs [Iyengar2005]. The library allows to model uncertainty in both the transition and rewards, unlike some published papers on this topic. This is modeled by adding an outcome to each action. The outcome is assumed to be minimized by nature, similar to [Filar1997].
In summary, the robust MDP problem being solved is:
Here, \mathcal{S} are the states, \mathcal{A} are the actions, \mathcal{O} are the outcomes.
The included algorithms are value iteration and modified policy iteration. The library support both the plain worst-case outcome method and a worst case with respect to a base distribution. The precise algorithms are implemented in C++ in CRAAM; see the project website for a detailed description.
The algorithms that approximate MDPs though robust state aggregation are described in [Petrik2014]. The robust algorithm generalizes standard state aggregation by capturing the introduced model error through robust models.
Installation
Requirements:
craam 1.0+ C++ implementation of methods for solving MDPs
Python 3.5+ (Python 2 is NOT supported)
Setuptools 7.0
Numpy 1.8+
Scipy 0.13
Cython 0.21+
The package has been tested only on Linux.
Optional dependencies:
Matplotlib 1.0+ for plotting support
To install, run (use --user to install locally):
To install in a development mode, execute:
The development installation will not copy project files to site-packages ---any changes to the Python code will be reflected without the need to reinstall.
To test the installation, run the following python code:
It is also possible to run the tests from the command line as:
Structure
The project consists of the following main modules:
raam.robust - a pure python implementation of selected robust optimization methods
raam.simulator - framework code for implementing a simulation-based MDP formulation and optimization
raam.samples - methods for handling samples
raam.features - methods for defining state features
raam.plotting - basic plotting support
raam.examples - example MDP domains
raam.test - code unit tests
Methods for solving robust MDPs are provided by craam.robust .
First Steps
Solving a Simple MDP
See library CRAAM for a simple example.
Solving a Sample-based MDP (reinforcement learning)
First, define a simulator for a simple MDP chain and sample from it.
The next step is to generate samples as follows:
These samples use the raw state and action representation. The state is in integer in this case, but it could be in principle any python object. So to formulate an MDP, we need to assign unique indices to the states as follows:
And finally, the following code will actually solve the MDP.
Note that it is important to map the value function and policy in the last two lines. This is because the sampled robust MDP uses an internal representation that separates decision and expectation states in order to improve computational efficiency.
More examples are provided in the subdirectory examples .
References
[Filar1997]
Filar, J., & Vrieze, K. (1997). Competitive Markov decision processes. Springer.
[Puterman2005]
Puterman, M. L. (2005). Markov decision processes: Discrete stochastic dynamic programming. Handbooks in operations research and management …. John Wiley & Sons, Inc.
[Iyengar2005]
Iyengar, G. N. G. (2005). Robust dynamic programming. Mathematics of Operations Research, 30(2), 1–29.
[Petrik2014]
Petrik, M., & Subramanian, D. (2014). RAAM : The benefits of robustness in approximating aggregated MDPs in reinforcement learning. In Neural Information Processing Systems (NIPS).
About
Robust and Approximate Markov Decision Processes
Resources
Readme
MIT license
Activity
Stars
12 stars
Watchers
2 watching
Forks
5 forks
Report repository
Releases
No releases published
Contributors 1 (1)
 marekpetrik Marek Petrik
Languages
Python 99.5%
Shell 0.5%
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