> Source: https://github.com/google-deepmind/bsuite

GitHub - google-deepmind/bsuite: bsuite is a collection of carefully-designed experiments that investigate core capabilities of a reinforcement learning (RL) agent · GitHub
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
google-deepmind / bsuite Public
Notifications You must be signed in to change notification settings
Fork 186
Star 1.6k
Code
Issues 7
Pull requests 12
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
2 Branches 9 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
Contributing
Apache-2.0 license
More items
Behaviour Suite for Reinforcement Learning ( bsuite )
  
Introduction
bsuite is a collection of carefully-designed experiments that investigate core capabilities of a reinforcement learning (RL) agent with two main objectives.
To collect clear, informative and scalable problems that capture key issues in the design of efficient and general learning algorithms.
To study agent behavior through their performance on these shared benchmarks.
This library automates evaluation and analysis of any agent on these benchmarks. It serves to facilitate reproducible, and accessible, research on the core issues in RL, and ultimately the design of superior learning algorithms.
Going forward, we hope to incorporate more excellent experiments from the research community, and commit to a periodic review of the experiments from a committee of prominent researchers.
For a more comprehensive overview, see the accompanying paper.
Technical overview
bsuite is a collection of experiments, defined in the experiments subdirectory. Each subdirectory corresponds to one experiment and contains:
A file defining an RL environment, which may be configurable to provide different levels of difficulty or different random seeds (for example).
A sequence of keyword arguments for this environment, defined in the SETTINGS variable found in the experiment's sweep.py file.
A file analysis.py defining plots used in the provided Jupyter notebook. bsuite works by logging results from "within" each environment, when loading environment via a load_and_record* function. This means any experiment will automatically output data in the correct format for analysis using the notebook, without any constraints on the structure of agents or algorithms.
We collate all of the results and analysis in a pre-made jupyter notebook bit.ly/bsuite-colab.
Getting started
If you are new to bsuite you can get started in our colab tutorial. This Jupyter notebook is hosted with a free cloud server, so you can start coding right away without installing anything on your machine. After this, you can follow the instructions below to get bsuite running on your local machine.
Installation
We have tested bsuite on Python 3.6 & 3.7. To install the dependencies:
Optional: We recommend using a Python virtual environment to manage your dependencies, so as not to clobber your system installation:
Install bsuite directly from PyPI:
Optional: To also install dependencies for the baselines examples (excluding OpenAI and Dopamine examples), run:
Environments
Complete descriptions of each environment and their corresponding experiments are found in the analysis/results.ipynb Jupyter notebook.
These environments all have small observation sizes, allowing for reasonable performance with a small network on a CPU.
Loading an environment
Environments are specified by a bsuite_id string, for example "deep_sea/7" . This string denotes the experiment and the (index of the) environment settings to use, as described in the technical overview section.
For a full description of each environment and its corresponding experiment settings, see the paper.
The sequence of bsuite_id s required to run all experiments can be accessed programmatically via:
This module also contains bsuite_id s for each experiment individually via uppercase constants corresponding to the experiment name, for example:
In addition, sequences of bsuite_id s with the same tag can be loaded via:
The TAGS variable groups bsuite environments together by their underlying tag, so all the basic tasks or scale tasks can be loaded with:
Loading an environment with logging included
We include one implementation of automatic logging, available via:
bsuite.load_and_record_to_csv . This outputs one CSV file per bsuite_id , so is suitable for running a set of bsuite experiments split over multiple machines. The implementation is in logging/csv_logging.py
Note, older versions of bsuite included an SQLite logger. If you would like to use this, please contact us and we can update and reinstate it.
We also include a terminal logger in logging/terminal_logging.py , exposed via bsuite.load_and_record_to_terminal .
It is easy to write your own logging mechanism, if you need to save results to a different storage system. See the CSV implementation for the simplest reference.
Interacting with an environment
Our environments implement the Python interface defined in dm_env .
More specifically, all our environments accept a discrete, zero-based integer action (or equivalently, a scalar numpy array with shape () ).
To determine the number of actions for a specific environment, use
Each environment returns observations in the form of a numpy array.
We also expose a bsuite_num_episodes property for each environment in bsuite. This allows users to run exactly the number of episodes required for bsuite's analysis, which may vary between environments used in different experiments.
Example run loop for a hypothetical agent with a step() method.
Using bsuite in 'OpenAI Gym' format
To use bsuite with a codebase that uses the OpenAI Gym interface, use the GymFromDMEnv class in utils/gym_wrapper.py :
Note that bsuite does not include Gym in its default dependencies, so you may need to pip install it separately.
Baseline agents
We include implementations of several common agents in the [ baselines/ ] subdirectory, along with a minimal run-loop.
See the installation section for how to include the required dependencies at install time. These dependencies are not installed by default, since bsuite does not require users to use any specific machine learning library.
Running the entire suite of experiments
Each of the agents in the baselines folder contains a run script which serves as an example which can run against a single environment or against the entire suite of experiments, by passing the --bsuite_id=SWEEP flags; this will start a pool of processes with which to run as many experiments in parallel as the host machine allows. On a 12 core machine, this will complete overnight for most agents. Alternatively, it is possible to run on Google Compute Platform using run_on_gcp.sh , steps of which are outlined below.
Running experiments on Google Cloud Platform
run_on_gcp.sh does the following in order:
Create an instance with specified specs (by default 64-core CPU optimized).
git clone s bsuite and installs it together with other dependencies.
Runs the specified agent (currently limited to /baselines ) on a specified environment.
Copies the resulting SQLite file to /tmp/bsuite.db from the remote instance to you local machine.
Shuts down the created instance.
In order to run the script, you first need to create a billing account. Then follow the instructions here to setup and initialize Cloud SDK. After completing gcloud init , you are ready to run bsuite on Google Cloud.
For this make run_on_gcp.sh executable and run it:
After the instance is created, the instance name will be printed. Then you can ssh into the instance by selecting Compute Engine -> Instances and clicking SSH . Note that this is not necessary, as the result will be copied to your local machine once it is ready. However, ssh ing might be convenient if you want to make local changes to agent and environments. In this case, after ssh ing, do
to activate the virtual environment. Then you can run agents via
for instance.
Analysis
bsuite comes with a ready-made analysis Jupyter notebook included in analysis/results.ipynb . This notebook loads and processes logged data, and produces the scores and plots for each experiment. We recommend using this notebook in conjunction with Colaboratory.
We provide an example of a such bsuite report here.
bsuite Report
You can use bsuite to generate an automated 1-page appendix, that summarizes the core capabilities of your RL algorithm. This appendix is compatible with most major ML conference formats. For example output run,
More examples of bsuite reports can be found in the reports/ subdirectory.
Citing
If you use bsuite in your work, please cite the accompanying paper:
About
bsuite is a collection of carefully-designed experiments that investigate core capabilities of a reinforcement learning (RL) agent
Resources
Readme
Apache-2.0 license
Contributing
Contributing
Activity
Custom properties
Stars
1.6k stars
Watchers
55 watching
Forks
186 forks
Report repository
Releases 8 (8)
0.3.6 Latest 2 months ago
+ 7 releases
Used by 150 (150)
@ParamThakkar123@c6ai@runjerry@montrealrobotics@JamesRudd-Jones + 142
Contributors 17 (17)
+ 3 contributors
Languages
Python 52.8%
TeX 28.4%
Jupyter Notebook 11.9%
BibTeX Style 6.6%
Shell 0.3%
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