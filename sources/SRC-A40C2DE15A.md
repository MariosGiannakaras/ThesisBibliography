> Source: https://github.com/SuReLI/RRLS

GitHub - SuReLI/RRLS: Robust Reinforcement Learning Suite · GitHub
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
SuReLI / RRLS Public
Notifications You must be signed in to change notification settings
Fork 2
Star 37
Code
Issues 1
Pull requests 0
Discussions
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Projects
Security and quality
Insights 
main
3 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
AdilZouitine
Update README.md
2 years ago
0c43dc9
· 2 years ago
History
117 Commits
Open commit details 
117 Commits
.github/ workflows
.github/ workflows
Fix env var
3 years ago
media
media
Change interface
3 years ago
rrls
rrls
chore: Update RobustHopper environment in evaluate.py
2 years ago
test
test
Fix default parameters in envs for consistent get_param return
2 years ago
.gitignore
.gitignore
Add RARL force envs (#2)
3 years ago
.pre-commit-config.yaml
.pre-commit-config.yaml
Add RARL force envs (#2)
3 years ago
CITATION.bib
CITATION.bib
Add citation bib
3 years ago
LICENSE
LICENSE
Update LICENSE
2 years ago
README.md
README.md
Update README.md
2 years ago
pyproject.toml
pyproject.toml
add gymnasium 1.0
2 years ago
setup.py
setup.py
fix ci
3 years ago
View all files
Repository files navigation
README
MIT license
More items
  
Robust Reinforcement Learning Suite (rrls)
Goal
The goal of rrls is to standardize robust reinforcement learning benchmarks, ensuring that experiments are reproducible and comparable. rrls is designed to follow the gymnasium API.
📦 Installation
From source:
Available when Gymasium 1.0 is released
Via pip:
Prerequisites:
Ensure you have MuJoCo installed on your machine. The environments provided by rrls require the MuJoCo physics engine from Deepmind. For detailed installation instructions, please refer to the MuJoCo website and the MuJoCo Github repository.
We have tested and support Python versions 3.9, 3.10, and 3.11 on both Linux and macOS.
🤖 Environments
The package offers the following environments:
Environment Name
id
Ant robust-ant-v0
HalfCheetah robust-halfcheetah-v0
Hopper robust-hopper-v0
HumanoidStandup robust-humanoidstandup-v0
InvertedPendulum robust-invertedpendulum-v0
Walker2d robust-walker2d-v0
And lot more ... if you want to get a full list of the environments, you can use the following code:
Example of usage:
🌯 Wrappers
The package provides the following wrappers:
Domain randomization: rrls.wrappers.DomainRandomization
Probabilistic action robustness: rrls.wrappers.ProbabilisticActionRobust
Adversarial dynamics: rrls.wrappers.DynamicAdversarial
👝 Uncertainty sets
For each environment, we offer a set of uncertainty sets for use. For instance:
This Enum includes three variants: 1D, 2D, and 3D uncertainty sets, as referenced from the M2TD3 paper. For instance, the 2D uncertainty set for the Ant environment is defined as follows:
Also you can get the uncertainty set provided by the RARL paper
🤓 Evaluate
If you want benchmark worst-case performance using our extensive suite. For every uncertainty set, we provide a corresponding set of evaluation environments. These environments are created by equally partitioning (into 10 segments) each dimension of the uncertainty set.
If you wish to construct your own custom set of environments, you can utilize the code below:
📖 Project Maintainers
Adil Zouitine - IRT Saint-Exupery, ISAE Supaero, & Sureli Team
David Bertoin - IRT Saint-Exupery, INSA Toulouse, ISAE Supaero, & Sureli Team
Emmanuel Rachelson - ISAE Supaero & Sureli Team
Pierre Clavier - Ecole polytechnique and Inria Paris
🙏 Acknowledgments
This project is part of the ENVIA initiative, aiming to develop next-gen reinforcement learning controllers for airship transportation of heavy loads. We are grateful to our supporters:
Sureli Team
Isae Supaero
IRT Saint Exupéry
Thales
About
Robust Reinforcement Learning Suite
Resources
Readme
MIT license
Activity
Custom properties
Stars
37 stars
Watchers
5 watching
Forks
2 forks
Report repository
Releases
No releases published
Contributors 2 (2)
 AdilZouitine Adil Zouitine
 DavidBert David Bertoin
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