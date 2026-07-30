> Source: https://github.com/Unity-Technologies/ml-agents

GitHub - Unity-Technologies/ml-agents: The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source project that enables games and simulations to serve as environments for training intelligent agents using deep reinforcement learning and imitation learning. · GitHub
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
Unity-Technologies / ml-agents Public
Notifications You must be signed in to change notification settings
Fork 4.5k
Star 19.6k
Code
Issues 1
Pull requests 15
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
477 Branches 145 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Code of conduct
License
More items
Unity ML-Agents Toolkit
( latest release) ( all releases)
The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source project that enables games and simulations to serve as environments for training intelligent agents. We provide implementations (based on PyTorch) of state-of-the-art algorithms to enable game developers and hobbyists to easily train intelligent agents for 2D, 3D and VR/AR games. Researchers can also use the provided simple-to-use Python API to train Agents using reinforcement learning, imitation learning, neuroevolution, or any other methods. These trained agents can be used for multiple purposes, including controlling NPC behavior (in a variety of settings such as multi-agent and adversarial), automated testing of game builds and evaluating different game design decisions pre-release. The ML-Agents Toolkit is mutually beneficial for both game developers and AI researchers as it provides a central platform where advances in AI can be evaluated on Unity's rich environments and then made accessible to the wider research and game developer communities.
Features
17+ example Unity environments
Support for multiple environment configurations and training scenarios
Flexible Unity SDK that can be integrated into your game or custom Unity scene
Support for training single-agent, multi-agent cooperative, and multi-agent competitive scenarios via several Deep Reinforcement Learning algorithms (PPO, SAC, MA-POCA, self-play).
Support for learning from demonstrations through two Imitation Learning algorithms (BC and GAIL).
Quickly and easily add your own custom training algorithm and/or components.
Easily definable Curriculum Learning scenarios for complex tasks
Train robust agents using environment randomization
Flexible agent control with On Demand Decision Making
Train using multiple concurrent Unity environment instances
Utilizes the Inference Engine to provide native cross-platform support
Unity environment control from Python
Wrap Unity learning environments as a gym environment
Wrap Unity learning environments as a PettingZoo environment
Releases & Documentation
⚠ Documentation Migration Notice We have moved to Unity Package documentation as the primary developer documentation and have deprecated the maintenance of web docs. Please use the Unity Package documentation for the most up-to-date information.
The table below shows our latest release, including our develop branch which is under active development and may be unstable. A few helpful guidelines:
The Versioning page overviews how we manage our GitHub releases and the versioning process for each of the ML-Agents components.
The Releases page contains details of the changes between releases.
The Migration page contains details on how to upgrade from earlier releases of the ML-Agents Toolkit.
The com.unity.ml-agents package is verified for Unity 2020.1 and later. Verified packages releases are numbered 1.0.x.
If you are a researcher interested in a discussion of Unity as an AI platform, see a pre-print of our reference paper on Unity and the ML-Agents Toolkit.
If you use Unity or the ML-Agents Toolkit to conduct research, we ask that you cite the following paper as a reference:
Additionally, if you use the MA-POCA trainer in your research, we ask that you cite the following paper as a reference:
Additional Resources
Unity Discussions
ML-Agents tutorials by CodeMonkeyUnity
Introduction to ML-Agents by Huggingface
Community created ML-Agents projects
ML-Agents models on Huggingface
Blog posts
Discord
Community and Feedback
The ML-Agents Toolkit is an open-source project and we encourage and welcome contributions. If you wish to contribute, be sure to review our contribution guidelines and code of conduct.
For problems with the installation and setup of the ML-Agents Toolkit, or discussions about how to best setup or train your agents, please create a new thread on the Unity ML-Agents discussion forum. Be sure to include as many details as possible to help others assist you effectively. If you run into any other problems using the ML-Agents Toolkit or have a specific feature request, please submit a GitHub issue.
Please tell us which samples you would like to see shipped with the ML-Agents Unity package by replying to this discussion thread.
Privacy
In order to improve the developer experience for Unity ML-Agents Toolkit, we have added in-editor analytics. Please refer to "Information that is passively collected by Unity" in the Unity Privacy Policy.
About
The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source project that enables games and simulations to serve as environments for training intelligent agents using deep reinforcement learning and imitation learning.
unity.com/products/machine-learning-agents
Topics
deep-learning deep-reinforcement-learning machine-learning neural-networks reinforcement-learning unity unity3d
Resources
Readme
License
Code of conduct
Code of conduct
Activity
Custom properties
Stars
19.6k stars
Watchers
553 watching
Forks
4.5k forks
Report repository
Releases 63 (63)
ML-Agents Release 23 Latest 11 months ago
+ 62 releases
Contributors 176 (176)
+ 162 contributors
Languages
C# 54.7%
Python 40.3%
Jupyter Notebook 4.5%
ShaderLab 0.2%
Shell 0.2%
Batchfile 0.1%
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