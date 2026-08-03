> Source: https://github.com/PKU-Alignment/safety-gymnasium

GitHub - PKU-Alignment/safety-gymnasium: NeurIPS 2023: Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark · GitHub
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
PKU-Alignment / safety-gymnasium Public
Notifications You must be signed in to change notification settings
Fork 81
Star 578
Code
Issues 13
Pull requests 3
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
6 Branches 12 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Code of conduct
Contributing
Apache-2.0 license
More items
Safety-Gymnasium
     
Why Safety-Gymnasium? | Documentation | Install guide | Customization | Video
Safety-Gymnasium is a highly scalable and customizable Safe Reinforcement Learning (SafeRL) library. It aims to deliver a good view of benchmarking SafeRL algorithms and a standardized set of environments. We provide a set of standard APIs which are compatible with information on constraints. Users can explore new insights via an elegant code framework and well-designed environments.
Citing Safety-Gymnasium
If you find Safety-Gymnasium useful, please cite it in your publications.
Note for v1.1.0 and v1.2.0❗❗❗
We have updated the environments for both the Safe Vision series and the Safe Isaac Gym series. However, due to package size constraints, we have not yet uploaded versions v1.1.0 and v1.2.0 to PyPI. As a result, users are required to manually download and install. We currently recommend using GitHub's Download zip feature to obtain our package and access the latest environments. In the future, we plan to deploy resources separately to a cloud service to accommodate PyPI. Stay tuned for further updates.
Python 3.11 is not supported for now, due to the incompatibility of pygame.
Why Safety-Gymnasium?
Here we provide a table for comparison of Safety-Gymnasium and existing SafeRL Environments libraries.
Environments
We designed a variety of safety-enhanced learning tasks and integrated the contributions from the RL community: safety-velocity , safety-run , safety-circle , safety-goal , safety-button , etc. We introduce a unified safety-enhanced learning benchmark environment library called Safety-Gymnasium.
Further, to facilitate the progress of community research, we redesigned Safety-Gym and removed the dependency on mujoco-py . We built it on top of MuJoCo and fixed some bugs, more specific bug reports can refer to Safety-Gym's BUG Report.
Here is a list of all the environments we support for now:
Here are some screenshots of the Safe Navigation tasks.
Agents
Point
Car
Racecar
Doggo
Ant
Tasks
Vision-based Safe RL
Vision-based SafeRL lacks realistic scenarios. Although the original Safety-Gym could minimally support visual input, the scenarios were too similar. To facilitate the validation of visual-based SafeRL algorithms, we have developed a set of realistic vision-based SafeRL tasks, which are currently being validated on the baseline.
For the appetizer, the images are as follows:
Environment Usage
Notes: We support explicitly expressing the cost based on Gymnasium APIs. The step method returns 6 items (next_obervation, reward, cost, terminated, truncated, info) with an extra cost field.
We also provide two convenience wrappers for converting the Safety-Gymnasium environment to the standard Gymnasium API and vice versa.
Users can apply Gymnasium wrappers easily with:
or
In addition, for all Safety-Gymnasium environments, we also provide corresponding Gymnasium environments with a suffix Gymnasium in the environment id. For example:
Installation
Install from PyPI
Install from source
Important Notes
If you failed to render on your server, you can try:
Debug with your keyboard
For simple agents, we offer the capability to control the robot's movement via the keyboard, facilitating debugging. Simply append a Debug suffix to the task name, such as SafetyCarGoal2Debug-v0 , and utilize the keys I , K , J , and L to guide the robot's movement.
For more intricate agents, you can also craft custom control logic based on specific peripherals. To achieve this, implement the debug method from the BaseAgent for the designated agent.
Customize your environments
We construct a highly expandable framework of code so that you can easily comprehend it and design your environments to facilitate your research with no more than 100 lines of code on average.
For details, please refer to our documentation. Here is a minimal example:
License
Safety-Gymnasium is released under Apache License 2.0.
About
NeurIPS 2023: Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark
safety-gymnasium.readthedocs.io/en/latest/
Topics
constraint-rl constraint-satisfaction-problem reinforcement-learning safe-policy-optimization safe-reinforcement-learning safe-reinforcement-learning-environments safety-critical safety-critical-systems
Resources
Readme
Apache-2.0 license
Code of conduct
Code of conduct
Contributing
Contributing
Cite this repository
Activity
Custom properties
Stars
578 stars
Watchers
7 watching
Forks
81 forks
Report repository
Releases 12 (12)
v1.2.0 Latest 3 years ago
+ 11 releases
Contributors 11 (11)
Languages
Python 98.1%
HTML 1.2%
Other 0.7%
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