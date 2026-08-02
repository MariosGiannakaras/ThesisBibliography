> Source: https://github.com/sparisi/gym_gridworlds

GitHub - sparisi/gym_gridworlds · GitHub
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
sparisi / gym_gridworlds Public
Notifications You must be signed in to change notification settings
Fork 10
Star 9
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
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
CC-BY-4.0 license
More items
Overview
Minimalistic implementation of gridworlds based on Gymnasium, useful for quickly testing and prototyping reinforcement learning algorithms (both tabular and with function approximation).
The default class Gridworld implements a "go-to-goal" task where the agent has five actions (left, right, up, down, stay) and default transition function (e.g., doing "stay" in goal states ends the episode).
You can change actions and transition function by implementing more classes. For example, in RiverSwim there are only two actions and no terminal state, or in Taxi the agent can pick up passengers and drive them to the goal.
Basic gridworlds are defined in gridworld.py and are presented below. Harder gridworlds are defined in separate files in gym_gridworlds and are not discussed here (but are fully documented).
You can find a list of all environments here.
Install and Examples
To install the environments run
Run python and then
to render the Penalty-3x3-v0 gridworld (left figure),
to render the Full-4x5-v0 gridworld (middle figure), and
to render the DangerMaze-5x6-v0 gridworld (right figure).
  
Black tiles are empty,
White tiles are pits (walking on them yields a large negative reward and the episode ends),
Gray tiles are walls (the agent cannot step on them),
Black tiles with purple arrows are tiles where the agent can move only in one direction (other actions will fail),
Red tiles give negative rewards,
Green tiles give positive rewards (the brighter, the higher),
Yellow tiles are quicksand, where all actions will fail with 90% probability,
The agent is the blue circle,
The orange arrow denotes the agent's last action,
The orange dot denotes that the agent did not try to move with its last action. 
The smallest pre-built environment is Gym-Gridworlds/Empty-RandomStart-2x2-v0 (on the left): there are only 4 states, 5 actions, and the initial position is random. It is the simplest environment you can use to debug your algorithm.
Optional Features
➤ Noisy Transition and Reward Functions
This makes the environment take a random action (instead of the action passed by the agent) with 10% probability, and Gaussian noise with 0.05 standard deviation is added to the reward.
➤ POMDP
To turn the MDP into a POMDP and learn from partially-observable pixels, make the environment with view_radius=1 (or any integer). This way, only the tiles close to the agent (within the view radius) will be visible, while far away tiles will be masked by white noise. For example, this is the partially-observable version of the Full-4x5-v0 gridworld above.
➤ Noisy Observations
Make the environment with observation_noise=0.2 (or any float between 0 and 1). With default observations, the float represents the probability that the position observed by the agent is random. With RGB observations, it represents the probability that a pixel is white noise, as shown below.
➤ Random Goals
Make the environment with random_goals=True to randomize the position of positive rewards (positive only!) at every reset. To learn in this setting, you need to add the rewards position to the observation ( MatrixWithGoalWrapper ), or to learn from pixels.
➤ Action To Terminate
If you make the environment with action_to_terminate=True , the agent will have an additional action to terminate the episode immediately with reward 0.
Make Your Own Gridworld
Encode your grid following the above mapping, and save it as txt file in gym_gridworlds/grids . For example save the grid below as 5x5_wall.txt .
(IN PROGRESS) You can use map_editor.py to draw customized grids and save/load them to txt files. The current version supports only TravelField grids.
Register the environment in gym_gridworlds/__init__.py , for example
Try it
Playground
If you install with pip install -e .[playground] , you can use playground.py to test an environment. For example, run
You will be able to move the agent around the environment with the directional arrow keys, see the rewards received by the agent, and save gifs like the ones below.         
Default MDP ( Gridworld Class)
Action Space
The action is discrete in the range {0, 4} for {LEFT, RIGHT, DOWN, UP, STAY} . It is possible to remove the STAY action by making the environment with no_stay=True .
Diagonal actions {5, 8} for {UP_LEFT, DOWN_LEFT, DOWN_RIGHT, UP_RIGHT} are also supported but not used in the default MDP.
An extra action is appended to the action space if action_to_terminate=True . With it, the agent can terminate the episode immediately with reward 0.
Observation Space
➤ Default (True State)
The observation is discrete in the range {0, n_rows * n_cols - 1} . Each integer denotes the current location of the agent. For example, in a 3x3 grid the observations are
The true state is always passed with the info dictionary as info["state"] , to retrieve it even when wrappers are used. This makes debugging easier (e.g., it is possible to count state visits even when RGB wrappers are used).
The observation can be transformed to better fit function approximation (e.g., if you use DQN) using wrappers from observation_wrappers.py. For example
CoordinateWrapper returns matrix coordinates (row, col) . In the above example, obs = 3 becomes obs = (1, 0) .
MatrixWrapper returns a map of the environment with one 1 at the agent's position. In the above example, obs = 3 becomes
BirdEyeWrapper returns a partial map of the environment with characters corresponding to the tile contents. The map is centered on the agent's position and shows tiles within the specified radius. This makes our Gridworlds similar to Minigrid, except that we use a single text map instead of multiple layered integer maps. For example, with view_radius=1
A similar observation can be returned with render_mode=ansi and then retrieving obs = print(env.render()) . The ANSI rendering returns a string (not an array of chars) representing the whole map, with A where the agent is. In the example above: .XO\n.X.\n..A
ContinuousObservationWrapper returns continuous observations based on the agent's position with a random fixed offset (to cover all of the observation space), normalized in [-1, 1] . In the above example, obs = 3 becomes obs = [-0.70128391, -0.92455349] . Read the wrapper documentation for more info.
Learning with such observations can be difficult, because tiles with similar observations — e.g., (0.2, 0.495) and (0.2, 0.505) — are very close in the observation space, but may be significantly different (e.g., one may be a pit and the other the goal). We advise using sparse function approximation when this wrapper is used, such as Fuzzy Tiling.
➤ RGB
To use classic RGB pixel observations, make the environment with render_mode="rgb_array" and then wrap it with gymnasium.wrappers.AddRenderObservation .
➤ Partial RGB
Pixel observations can be made partial by making the environment with view_radius . For example, if view_radius=1 the rendering will show the content of only the tiles around the agent, while all other tiles will be filled with white noise.
➤ Noisy Observations
Make the environment with observation_noise=0.2 (or any float between 0 and 1). With default observations, the float represents the probability that the position observed by the agent is random. With RGB observations, it represents the probability that a pixel is white noise.
Starting State
By default, the episode starts with the agent at the top-left tile (0, 0) . You can manually select the starting position by making the environment with the argument start_pos , e.g., start_pos=[(3, 4)] . You can use the key "max" to automatically select the end of the grid, e.g., start_pos=[("max", 0)] will place the agent at the bottom-right corner. If you make the environment with start_pos=None , the starting position will be random. In both cases (fixed and random), the starting position cannot be a tile with a wall, a pit, or a positive reward.
Note that the starting position must be passed as a list of tuples. If more than one tuple is passed, the starting position will be randomly sampled from the list at every reset.
➤ More Control Over The Starting State
If you want some starting states to be more likely to be sampled, repeat them within the list. For example, with start_pos=[(3, 4), (1, 0), (1, 0)] the agent has 66% chance of starting in (1, 0) and 33% of starting in (3, 4) .
If you make the environment with loop_through_start_pos=True , the starting state will be different at every reset, following the order you passed with start_pos . This can be useful for testing environments with multiple starting states with only a few episodes. For example,
If you make the environment with non_uniform_start=True , then all starting positions are repeated 10 times except the last one. This is a quick a simple way to study environments where the initial position of the agent is not uniformly sampled. For example,
Transition
By default, the transition is deterministic except in quicksand tiles, where any action fails with 90% probability (the agent does not move).
Transition can be made stochastic everywhere by passing random_action_prob . This is the probability that the action will be random. For example, if random_action_prob=0.1 there is a 10% chance that the agent will do a random action instead of doing the one passed to self.step(action) .
Another way to add stochasticity is with slippery_prob , which is the probability that the agent slips and moves twice (similar to "sticky actions" in other environments).
➤ Random Resets
You can pass random_reset_prob to have a chance that the environment self-resets at any step. This doesn't change the terminal and truncated flags, but simply transitions the agent to an initial state (i.e., the next state will be the one returned by env.reset() ).
Useful to mimic episodic tasks in the infinite horizon setting (should not be used when there are terminal states).
➤ Noisy Tiles
In tiles defined by ? in their text map, there is a 50% chance that the action executed by the agent will be ignored, and a random one will be done instead. Visually, these tiles appear identical to empty tiles.
➤ Action To Terminate
If the environment is made with action_to_terminate=True , the agent can decide to terminate it at any time step. If so, the environment step returns reward = 0 and terminal = True .
Rewards
Doing STAY at the goal: +1
Doing STAY at a distracting goal: 0.1
Any action in penalty tiles: -10
Any action in small penalty tiles: -0.1
Walking on a pit tile: -100
Otherwise: 0
If the environment is made with no_stay=True , then the agent receives positive rewards for any action done in a goal state. Note that the reward still depends on the current state and not on the next state.
Positive rewards position can be randomized at every reset by making the environment with random_goals=True .
➤ Noisy Rewards
White noise can be added to all rewards by passing reward_noise_std , or only to nonzero rewards with nonzero_reward_noise_std .
➤ Auxiliary Rewards
Auxiliary rewards based on the Manhattan distance to the closest goal can be added by passing distance_reward=True or distance_difference_reward=True . The former is distance_at_current_state / max_distance , i.e., the distance from the current state scaled according to the size of the grid to be in the range [-1, 0]. The latter is distance_at_current_state - distance_at_next_state , thus it can be +1 (if the agent moves closer to the goal), 0 (if it does STAY), or -1 (if it moves further from the goal).
Episode End
By default, an episode ends if any of the following happens:
A positive reward is collected (termination),
Walking on a pit tile (termination),
The length of the episode is max_episode_steps (truncation).
It is possible to remove termination altogether by making the environment with infinite_horizon=True .
About
No description, website, or topics provided.
Resources
Readme
CC-BY-4.0 license
Cite this repository
Activity
Stars
9 stars
Watchers
2 watching
Forks
10 forks
Report repository
Releases
No releases published
Contributors 2 (2)
 sparisi Simone Parisi
 Hedgemon4 Seth Akins
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