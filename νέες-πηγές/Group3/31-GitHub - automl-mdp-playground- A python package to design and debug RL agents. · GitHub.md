> Source: https://github.com/automl/mdp-playground

GitHub - automl/mdp-playground: A python package to design and debug RL agents. · GitHub
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
automl / mdp-playground Public
Notifications You must be signed in to change notification settings
Fork 7
Star 34
Code
Issues 0
Pull requests 3
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
master
13 Branches 2 Tags  
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
RaghuSpaceRajan
Update .toml extras; fixed tests; added changelog; removed old setup.py;
failure
3 months ago
2ca8a01
· 3 months ago
History
820 Commits
Open commit details 
820 Commits
.github/ workflows
.github/ workflows
Add setuptools to combat Gym/distutils failure
2 years ago
docs
docs
Improved naming of function to get and set underlying Markov states i…
9 months ago
experiments
experiments
formatted using black
4 years ago
mdp_playground
mdp_playground
Update .toml extras; fixed tests; added changelog; removed old setup.py;
3 months ago
misc
misc
Add sample CSV data
4 years ago
tests
tests
Improved naming of function to get and set underlying Markov states i…
9 months ago
.coveragerc
.coveragerc
Update .coveragerc
5 years ago
.gitignore
.gitignore
reward_every_n_steps updated to work with continuous and grid envs (a…
2 years ago
.pep8
.pep8
Code formatted with black and autopep8
5 years ago
CHANGELOG.md
CHANGELOG.md
Update .toml extras; fixed tests; added changelog; removed old setup.py;
3 months ago
CONTRIBUTING.md
CONTRIBUTING.md
updated readmes
5 years ago
LICENSE
LICENSE
Update LICENSE
5 years ago
README.md
README.md
Update .toml extras; fixed tests; added changelog; removed old setup.py;
3 months ago
README_CONFIGS.md
README_CONFIGS.md
Replace meta-feature with dimension of hardness
4 years ago
codecov.yml
codecov.yml
Add exceptions codecov.yml
4 years ago
default_config.py
default_config.py
Code formatted with black and autopep8
5 years ago
example.py
example.py
Improved naming of function to get and set underlying Markov states i…
9 months ago
plot_experiments.ipynb
plot_experiments.ipynb
Replace meta-feature with dimension of hardness
4 years ago
plot_experiments_multiple.ipynb
plot_experiments_multiple.ipynb
Replace meta-feature with dimension of hardness
4 years ago
poetry.lock
poetry.lock
updated poetry lock
5 years ago
py36_toy_rl.yml
py36_toy_rl.yml
Updated conda env YAML
7 years ago
pyproject.toml
pyproject.toml
Update .toml extras; fixed tests; added changelog; removed old setup.py;
3 months ago
requirements.txt
requirements.txt
Fix README to work.
5 years ago
run_experiments.py
run_experiments.py
Fixed failing tests. Added run_experiments.py to root dir
5 years ago
uv.lock
uv.lock
Update .toml extras; fixed tests; added changelog; removed old setup.py;
3 months ago
View all files
Repository files navigation
README
Contributing
Apache-2.0 license
More items
    
MDP Playground
A python package to inject low-level dimensions of hardness in RL environments. There are toy environments to design and debug RL agents. And complex environment wrappers for Gym environments (inclduing Atari and Mujoco) to test robustness to these dimensions in complex environments.
Quick Start
Example to inject hardness (reward delay and reward noise) into 2 Gymnasium environments: a toy environment and using the Gymnasium wrapper for an Atari environment:
Important Note
We are moving to package management with uv and away from using Ray Rllib, so some experiment / agent running functionality might break. The wrappers and toy environment should still work fine though.
Getting started
There are 4 parts to the package:
Toy Environments: The base toy Environment in mdp_playground/envs/rl_toy_env.py implements the toy environment functionality, including discrete and continuous environments, and is parameterised by a config dict which contains all the information needed to instantiate the required toy MDP. Please see example.py for some simple examples of how to use these. For further details, please refer to the documentation in mdp_playground/envs/rl_toy_env.py .
Complex Environment Wrappers: Similar to the toy environment, this is parameterised by a config dict which contains all the information needed to inject the dimensions into Gym environments (tested with Atari, Mujoco and ProcGen). Please see example.py for some simple examples of how to use these. The generic Gym wrapper (for Atari, ProcGen, etc.) is in mdp_playground/envs/gym_env_wrapper.py and the Mujoco specific wrapper is in mdp_playground/envs/mujoco_env_wrapper.py .
Experiments: Experiments are launched using run_experiments.py . Config files for experiments are located inside the experiments directory. Please read the instructions below for details on how to launch experiments.
Analysis: plot_experiments.ipynb contains code to plot the standard plots from the paper.
Running experiments from the main paper
For reproducing experiments from the main paper, please continue reading.
For general install and usage instructions, please see here.
Installation for running experiments from the main paper
We recommend using conda environments to manage virtual Python environments to run the experiments. Unfortunately, you will have to maintain 2 environments - 1 for the "older" discrete toy experiments and 1 for the "newer" continuous and complex experiments from the paper. As mentioned in Appendix section Tuned Hyperparameters in the paper, this is because of issues with Ray, the library that we used for our baseline agents.
Please follow the following commands to install for the discrete toy experiments:
Please follow the following commands to install for the continuous and complex experiments. IMPORTANT: In case, you do not have MuJoCo, please ignore any mujoco related installation errors below:
We list here how the commands for the experiments from the main paper look like:
For plotting, please follow the instructions here.
Installation
For reproducing experiments from the main paper, please see here.
For continued usage of MDP Playground as it is in development, please continue reading.
Production use
We recommend using conda to manage environments. After setup of the environment, you can install MDP Playground in two ways:
Manual
To install MDP Playground manually (this might be the preferred way if you want easy access to the included experiments), clone the repository and run:
From PyPI
Alternatively, MDP Playground can also be installed from PyPI. Just run:
Running experiments
You can run experiments using:
The exp_name is a prefix for the filenames of CSV files where stats for the experiments are recorded. The CSV stats files will be saved to the current directory.
The command line arguments also usually have defaults. Please refer to the documentation inside run_experiments.py for further details on the command line arguments. (Or run it with the -h flag to bring up help.)
The config files for experiments from the paper are in the experiments directory.
The name of the file corresponding to an experiment is formed as: <algorithm_name>_<dimension_names>.py for the toy environments
And as: <algorithm_name>_<env>_<dimension_names>.py for the complex environments
Some sample algorithm_name s are: dqn , rainbow , a3c , ddpg , td3 and sac
Some sample dimension_name s are: seq_del (for delay and sequence length varied together), p_r_noises (for P and R noises varied together), target_radius (for varying target radius) and time_unit (for varying time unit)
For example, for algorithm DQN when varying dimensions delay and sequence length, the corresponding experiment file is dqn_seq_del.py
The CSV stats files will be saved to the current directory and can be analysed in plot_experiments.ipynb .
Plotting
To plot results from experiments, please be sure that you installed MDP Playground for production use manually (please see here) and then run jupyter-notebook and open plot_experiments.ipynb in Jupyter. There are instructions within each of the cells on how to generate and save plots.
Documentation
The documentation can be found at: https://automl.github.io/mdp-playground/
Toy Environments
Complex Environment Wrappers:
Gym
Mujoco
Please see example.py for some simple examples of how to use all of these.
Citing
If you use MDP Playground in your work, please cite the following paper:
About
A python package to design and debug RL agents.
automl.github.io/mdp-playground/
Topics
benchmark benchmarking reinforcement-learning testbed
Resources
Readme
Apache-2.0 license
Contributing
Contributing
Activity
Custom properties
Stars
34 stars
Watchers
7 watching
Forks
7 forks
Report repository
Releases 2 (2)
v1.0.0 - Gymnasium Migration, new numpy RNG & uv Package Management Latest 3 months ago
+ 1 release
Contributors 5 (5)
Languages
Python 97.8%
Jupyter Notebook 1.5%
Shell 0.7%
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