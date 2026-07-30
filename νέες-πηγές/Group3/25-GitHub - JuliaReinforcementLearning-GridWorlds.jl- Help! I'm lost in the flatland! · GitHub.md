> Source: https://github.com/JuliaReinforcementLearning/GridWorlds.jl

GitHub - JuliaReinforcementLearning/GridWorlds.jl: Help! I'm lost in the flatland! · GitHub
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
JuliaReinforcementLearning / GridWorlds.jl Public
Notifications You must be signed in to change notification settings
Fork 9
Star 46
Code
Issues 9
Pull requests 4
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
master
6 Branches 7 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
More items
GridWorlds
A package for creating grid world environments for reinforcement learning in Julia. This package is designed to be lightweight and fast.
This package is inspired by gym-minigrid. In order to cite this package, please refer to the file CITATION.bib . Starring the repository on GitHub is also appreciated. For benchmarks, refer to benchmarks/benchmarks.md .
Table of contents:
Getting Started
Notes
List of Environments
SingleRoomUndirected
SingleRoomDirected
GridRoomsUndirected
GridRoomsDirected
SequentialRoomsUndirected
SequentialRoomsDirected
MazeUndirected
MazeDirected
GoToTargetUndirected
GoToTargetDirected
DoorKeyUndirected
DoorKeyDirected
CollectGemsUndirected
CollectGemsDirected
CollectGemsMultiAgentUndirected
DynamicObstaclesUndirected
DynamicObstaclesDirected
SokobanUndirected
SokobanDirected
Snake
Catcher
TransportUndirected
TransportDirected
Getting Started
Notes
Reinforcement Learning
This package does not intend to reinvent a fully usable reinforcement learning API. Instead, all the games in this package provide the bare minimum of what is needed to for the game logic, which is the ability to reset an environment using GW.reset!(env) and to perform actions in the environment using GW.act!(env, action) . In order to utilize such a game for reinforcement learning, you would probably be using a higher level reinforcement learning API like the one offered by the ReinforcementLearning.jl package ( RLBase API), for example. As of this writing, all the environments provide a default implementation for the RLBase API, which means that you can easily wrap a game from GridWorlds.jl and use it directly with the rest of the ReinforcementLearning.jl ecosystem.
1.
States
There are a few possible options for representing the state/observation for an environment. You can use the entire tile map. You can also augment that with other environment specific information like the agent's direction, target (in GoToTargetUndirected ) etc. In several games, you can also use the GW.get_sub_tile_map! function to get a partial view of the tile map to be used as the observation. All environemnts provide a default implementation of the RLBase.state function. It is recommended that before performing reinforcement learning experiments using an environment, you carefully understand the information contained in the state representation for that environment. 2.
Actions
As of this writing, all actions in all environments are discrete. And so, to keep things simple and consistent, they are represented by elements of Base.OneTo(NUM_ACTIONS) (basically integers going from 1 to NUM_ACTIONS). In order to know which action does what, you can call GW.get_action_names(env) to get a list of names which gives a better description. For example:
The order of elements in this list corresponds to that of the actions. 3.
Rewards and Termination
As mentioned before, in order to use these for reinforcement learning experiments, you would mostly be using a higher level API like RLBase , which should already provide a way to get these values. For example, in RLBase, rewards can be accessed using RLBase.reward(env) and checking whether an environment has terminated or not can by done by calling RLBase.is_terminated(env) . In case you are using some other API and need more direct control, it is better to take a look at the implementation for that environment to access things like reward and check for termination.
Tile Map
Each environment contains a tile map, which is a BitArray{3} that encodes information about the presence or absence of objects in the grid world. It is of size (num_objects, height, width) . The second and third dimensions correspond to positions along the height and width of the tile map. The first dimension corresponds to the presence or absence of objects at a particular position using a multi-hot encoding along the first dimension. You can get the name and ordering of objects along the first dimension of the tile map by using the following method:
Navigation
Several environments contain the word Undirected or Directed within their name. This refers to the navigation style of the agent. Undirected means that the agent has no direction associated with it, and navigates around by directly moving up, down, left, or right on the tile map. Directed means that the agent has a direction associated with it, and it navigates around by moving forward or backward along its current direction, or it could also turn left or right with respect to its current direction. There are 4 directions - UP , DOWN , LEFT , and RIGHT .
Interactive Playing and Recording
All the environments can be played directly inside the REPL. These interactive sessions can also be recorded in plain text files and replayed in the terminal. There are two ways to replay a recording:
The default way is to manually step through each recorded frame. This allows you to move through the frames one by one at your own pace using keyboard inputs.
The second way is to replay the frames at a given frame rate. This would loop through all the frames once and then (and only then) exit the replay.
Here is an example:   
Programmatic Recording of Agent's Behavior
In order to programmatically record the behavior of an agent during an episode, you can simply log the string representation of the environment at each step prefixed with a delimiter. You can also log other arbitrary information if you want, like the total reward so far, for example. You can then use the GW.replay functiton to replay the recording inside the terminal. The string representation of an environment can be obtained using repr(MIME"text/plain"(), env) . Here is an example:
In ReinforcementLearning.jl , you can create a hook for recording the agent's behavior at any point during training.
List of Environments
1.
SingleRoomUndirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     2.
SingleRoomDirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     3.
GridRoomsUndirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     4.
GridRoomsDirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     5.
SequentialRoomsUndirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     6.
SequentialRoomsDirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     7.
MazeUndirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     8.
MazeDirected
The objective of the agent is to navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates.     9.
GoToTargetUndirected
The objective of the agent is to navigate its way to the desired target. When the agent reaches the desired target, it receives a reward of 1. When the agent reaches the other target, it receives a reward of -1. In either case, the environment terminates upon reaching a target.     10.
GoToTargetDirected
The objective of the agent is to navigate its way to the desired target. When the agent reaches the desired target, it receives a reward of 1. When the agent reaches the other target, it receives a reward of -1. In either case, the environment terminates upon reaching a target.     11.
DoorKeyUndirected
The objective of the agent is to collect the key and navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates. Without picking up the key, the agent will not be able to pass through the door that separtes the agent and goal.     12.
DoorKeyDirected
The objective of the agent is to collect the key and navigate its way to the goal. When the agent reaches the goal, it receives a reward of 1 and the environment terminates. Without picking up the key, the agent will not be able to pass through the door that separtes the agent and goal.     13.
CollectGemsUndirected
The objective of the agent is to collect all the randomly scattered gems. When the agent collects a gem, it receives a reward of 1. The environment terminates when the agent has collected all the gems.     14.
CollectGemsDirected
The objective of the agent is to collect all the randomly scattered gems. When the agent collects a gem, it receives a reward of 1. The environment terminates when the agent has collected all the gems.     15.
CollectGemsMultiAgentUndirected
The objective of the agents is to collect all the randomly scattered gems. The agents take turns for performing actions. When an agent collects a gem, the environment gives a reward of 1. The environment terminates when the agents have collected all the gems.     16.
DynamicObstaclesUndirected
The objective of the agent is to navigate its way to the goal while avoiding collision with obstacles. When the agent reaches the goal, it receives a reward of 1 and the environment terminates. If the agent collides with an obstacle, the agent receives a reward of -1 and the environment terminates.     17.
DynamicObstaclesDirected
The objective of the agent is to navigate its way to the goal while avoiding collision with obstacles. When the agent reaches the goal, it receives a reward of 1 and the environment terminates. If the agent collides with an obstacle, the agent receives a reward of -1 and the environment terminates.     18.
SokobanUndirected
The agent needs to push the boxes onto the target positions. The levels are taken from https://github.com/deepmind/boxoban-levels. Upon each reset, a level is randomly selected from https://github.com/deepmind/boxoban-levels/blob/master/medium/train/000.txt. The level dataset can be dynamically swapped during runtime in case more levels are needed. One way to achieve this while using ReinforcementLearning.jl is with the help of hooks.     19.
SokobanDirected
The agent needs to push the boxes onto the target positions. The levels are taken from https://github.com/deepmind/boxoban-levels. Upon each reset, a level is randomly selected from https://github.com/deepmind/boxoban-levels/blob/master/medium/train/000.txt. The level dataset can be dynamically swapped during runtime in case more levels are needed. One way to achieve this while using ReinforcementLearning.jl is with the help of hooks.     20.
Snake
The objective of the agent is to eat as many food pellets as possible. As soon as the agent eats a food pellet, the length of its body incrases by one and it receives a reward of 1. When the agent tries to move into a wall or into its body, it receives a reward of - tile_map_height * tile_map_width and the environment terminates. When the agent collects all the food pellets possible, it receives a reward of tile_map_height * tile_map_width + 1 (for the last food pellet it ate).     21.
Catcher
The objective of the agent is to keep catching the falling gems for as long as possible. It receives a reward of 1 when it catches a gem and a new gem gets spawned in the next step. When the agent misses catching a gem, it receives a reward of -1 and the environment terminates.     22.
TransportUndirected
The objective of the agent is to pick up the gem and drop it to the target location. When the agent drops the gem at the target location, it receives a reward of 1 and the environment terminates.     23.
TransportDirected
The objective of the agent is to pick up the gem and drop it to the target location. When the agent drops the gem at the target location, it receives a reward of 1 and the environment terminates.    
About
Help! I'm lost in the flatland!
Topics
grid-world gridworld gridworld-environment hacktoberfest julia makie reinforcement-learning
Resources
Readme
MIT license
Cite this repository
Activity
Custom properties
Stars
46 stars
Watchers
7 watching
Forks
9 forks
Report repository
Releases 7 (7)
v0.5.0 Latest 5 years ago
+ 6 releases
Contributors 7 (7)
Languages
Julia 100%
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