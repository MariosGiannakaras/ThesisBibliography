> Source: https://github.com/Farama-Foundation/HighwayEnv

GitHub - Farama-Foundation/HighwayEnv: A collection of environments for autonomous driving and tactical decision-making tasks · GitHub
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
Farama-Foundation / HighwayEnv Public
Notifications You must be signed in to change notification settings
Fork 885
Star 3.3k
Code
Issues 38
Pull requests 5
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
8 Branches 19 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Contributing
MIT license
More items
        
An episode of one of the environments available in HighwayEnv.
A collection of environments for autonomous driving and tactical decision-making tasks. Originally developed by Edouard Leurent and currently maintained by Jin Huang.
The documentation website is at highway-env.farama.org, and we have a public discord server (which we also use to coordinate development work) that you can join here: https://discord.gg/bnJ6kubTg6
Installation
To install HighwayEnv, use:
or with uv:
We support Linux and macOS primarily, with Windows support maintained on a best-effort basis.
Environments
HighwayEnv includes 10 driving scenario families: highway , intersection , exit , lane-keeping , merge , parking , racetrack , roundabout , two-way , and u-turn , with several environments also offering fast, continuous-control, connected-lane, multi-agent, generic, large, or oval variants. The full list with descriptions and configuration options is available in the documentation.
Previews
Usage
See the documentation for more examples including how to train agents with Stable Baselines3 and Google Colab notebooks. For examples of trained agents (DQN, DDPG, Value Iteration, MCTS), see the Agent Examples page.
Documentation
Read the documentation online.
Development Roadmap
Here is the roadmap for future development work.
Citating
If you use HighwayEnv in your work, please consider citing it with:
Publications
A list of publications using HighwayEnv can be found in the documentation.
About
A collection of environments for autonomous driving and tactical decision-making tasks
highway-env.farama.org/
Topics
autonomous-driving gymnasium-environment reinforcement-learning
Resources
Readme
MIT license
Contributing
Contributing
Cite this repository
Activity
Custom properties
Stars
3.3k stars
Watchers
27 watching
Forks
885 forks
Report repository
Releases 19 (19)
Vehicle behaviour fix, generic merge env, Gymnasium-compliant render behaviour, and docs refresh Latest 3 weeks ago
+ 18 releases
Used by 300 (300)
@AFIT-AI-TREC@rkoonireddy@learnwithallen@Gallimore-Software@pierriccardo + 294
Contributors 54 (54)
+ 40 contributors
Languages
Python 92.5%
Jupyter Notebook 7.3%
Just 0.2%
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