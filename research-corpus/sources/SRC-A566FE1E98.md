> Source: https://github.com/google-research/rliable

GitHub - google-research/rliable: [NeurIPS'21 Outstanding Paper] Library for reliable evaluation on RL and ML benchmarks, even with only a handful of seeds. · GitHub
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
This repository was archived by the owner on Oct 15, 2025. It is now read-only.
google-research / rliable Public archive
Notifications You must be signed in to change notification settings
Fork 49
Star 880
Code
Issues 5
Pull requests 0
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
master
1 Branch 1 Tag  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Contributing
Apache-2.0 license
More items
  
rliable is an open-source Python library for reliable evaluation, even with a handful of runs, on reinforcement learning and machine learnings benchmarks.
Stratified Bootstrap Confidence Intervals (CIs)
Performance Profiles (with plotting functions)
Aggregate metrics
Interquartile Mean (IQM) across all runs
Optimality Gap
Probability of Improvement 
Interactive colab
We provide a colab at bit.ly/statistical_precipice_colab, which shows how to use the library with examples of published algorithms on widely used benchmarks including Atari 100k, ALE, DM Control and Procgen.
Data for individual runs on Atari 100k, ALE, DM Control and Procgen
You can access the data for individual runs using the public GCP bucket here (you might need to sign in with your gmail account to use Gcloud) : https://console.cloud.google.com/storage/browser/rl-benchmark-data. The interactive colab above also allows you to access the data programatically.
Paper
For more details, refer to the accompanying NeurIPS 2021 paper ( Outstanding Paper Award): Deep Reinforcement Learning at the Edge of the Statistical Precipice.
Installation
To install rliable , run:
To install latest version of rliable as a package, run:
To import rliable , we suggest:
Aggregate metrics with 95% Stratified Bootstrap CIs
IQM, Optimality Gap, Median, Mean
Probability of Improvement
Sample Efficiency Curve
 
Performance Profiles
 
The above profile can also be plotted with non-linear scaling as follows:
Dependencies
The code was tested under Python>=3.7 and uses these packages:
arch == 5.3.0
scipy >= 1.7.0
numpy >= 0.9.0
absl-py >= 1.16.4
seaborn >= 0.11.2
Citing
If you find this open source release useful, please reference in your paper:
Disclaimer: This is not an official Google product.
About
[NeurIPS'21 Outstanding Paper] Library for reliable evaluation on RL and ML benchmarks, even with only a handful of seeds.
agarwl.github.io/rliable
Topics
benchmarking evaluation-metrics google machine-learning reinforcement-learning rl
Resources
Readme
Apache-2.0 license
Contributing
Contributing
Cite this repository
Activity
Custom properties
Stars
880 stars
Watchers
0 watching
Forks
49 forks
Report repository
Contributors 9 (9)
Languages
Jupyter Notebook 97.3%
Python 2.7%
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