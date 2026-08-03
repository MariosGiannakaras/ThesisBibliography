> Source: https://github.com/google-deepmind/pycolab

GitHub - google-deepmind/pycolab: A highly-customisable gridworld game engine with some batteries included. Make your own gridworld games to test reinforcement learning agents! · GitHub
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
google-deepmind / pycolab Public
Notifications You must be signed in to change notification settings
Fork 123
Star 666
Code
Pull requests 0
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
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
The pycolab game engine.
A highly-customisable gridworld game engine with some batteries included. Make your own gridworld games to test reinforcement learning agents!
Play some games!
If you're new, why not try playing some games first? For the full colour experience on most UNIX-compatible systems:
crack open a nice, new, modern terminal (iterm2 on Mac, gnome-terminal or xterm on linux). (Avoid screen/tmux for now---just the terminal, please.)
set the terminal type to xterm-256color (usually, you do this by typing export TERM=xterm-256color at the command prompt).
run the example games! One easy way is to cd to just above the pycolab/ library directory (that is, cd to the root directory of the git repository or the distribution tarball, if you're using either of those) and run python with the appropriate PYTHONPATH environment variable. Example command line for bash -like shells: PYTHONPATH=. python -B pycolab/examples/scrolly_maze.py .
Okay, install some dependencies first.
If that didn't work, you may need to obtain the following software packages that pycolab depends on:
Python 2.7, or Python 3.4 and up. We've had success with 2.7.6, 3.4.3, and 3.6.3; other versions may work.
Numpy. Our version is 1.13.3, but 1.9 seems to have the necessary features.
Scipy, but only for running one of the examples. We have 0.13.3.
Overview
pycolab is extensively documented and commented, so the best ways to understand how to use it are:
check out examples in the examples/ subdirectory,
read docstrings in the .py files.
For docstring reading, the best order is probably this one---stopping whenever you like (the docs aren't going anywhere...):
the docstring for the Engine class in engine.py
the docstrings for the classes in things.py
Those two are probably the only bits of "required" reading in order to get an idea of what's going on in examples/ . From there, the following reading may be of interest:
plot.py : how do game components talk to one another---and how do I give the agent rewards and terminate episodes?
human_ui.py : how can I try my game out myself?
prefab_parts/sprites.py : useful Sprite subclasses, including MazeWalker , a pixel that can walk around but not through walls and obstacles.
cropping.py : how can I generate the illusion of top-down scrolling by cleverly cropping an observation around a particular moving game element? (This is a common way to build partial observability into a game.)
Don't forget that you can always read the tests, too. These can help demonstrate by example what all the various components do.
Disclaimer
This is not an official Google product.
We just thought you should know that.
About
A highly-customisable gridworld game engine with some batteries included. Make your own gridworld games to test reinforcement learning agents!
Resources
Readme
Apache-2.0 license
Contributing
Contributing
Activity
Custom properties
Stars
666 stars
Watchers
31 watching
Forks
123 forks
Report repository
Releases
No releases published
Used by 190 (190)
@sk-surya@EvoGenesis-AgentSheild@Leadership-Stock-LTD@cloudesize67-cmd@stevewithington + 186
Contributors 4 (4)
 stepleton Tom Stepleton
 odelalleau Olivier Delalleau
 GeorgOstrovski Georg Ostrovski
 wenkesj Sam Wenke
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