> Source: https://github.com/jlwu002/VSRL

GitHub - jlwu002/VSRL: [NeurIPS 2024] Verified Safe Reinforcement Learning for Neural Network Dynamic Models · GitHub
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
jlwu002 / VSRL Public
Notifications You must be signed in to change notification settings
Fork 1
Star 6
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
main
1 Branch 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
More items
Verified Safe Reinforcement Learning for Neural Network Dynamic Models (NeurIPS 2024)
Run generate_grid.py to generate the grid for verification.
Train a vanilla controller by setting Line 170 in moving_obs/train.py to False ( use_reachability = False ), and comment out Line 149 ( ppo_agent.load ) in train.py .
Train with bounds by setting Line 170 to True and loading the checkpoint from the vanilla controller ( ppo_agent.load ) .
The controller for each k-th step reachability safety will be stored in the outputs folder. If a controller is not fully verified for a given k, the filename will have the suffix _not_verified.pth .
If you observe a significant decrease in reward or reach the target verification step, stop training. Run check_collide.py to verify the safety of the desired input region.
Based on the results from check_collide.py (modify target_steps ), split the input region and continue from Step 3 for each input region cluster (load from a selected checkpoint).
Stop if all input regions are verified safe for the corresponding controller.
About
[NeurIPS 2024] Verified Safe Reinforcement Learning for Neural Network Dynamic Models
arxiv.org/pdf/2405.15994
Resources
Readme
Activity
Stars
6 stars
Watchers
2 watching
Forks
1 fork
Report repository
Releases
No releases published
Contributors 1 (1)
 jlwu002 Junlin Wu
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