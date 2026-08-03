> Source: https://gymnasium.farama.org/environments/toy_text/frozen_lake/

Frozen Lake - Gymnasium Documentation
Toggle site navigation sidebar
Light LogoDark Logo Gymnasium Documentation 
Farama Foundation logo Farama Foundation
Core Projects
Gymnasium logo Gymnasium
PettingZoo logo PettingZoo
Minari logo Minari
Mature Projects
Documentation
Gymnasium-Robotics logo Gymnasium-Robotics
MAgent2 logo MAgent2
Metaworld logo Metaworld
Minigrid logo Minigrid
MiniWoB++ logo MiniWoB++
MOMAland logo MOMAland
MO-Gymnasium logo MO-Gymnasium
Shimmy logo Shimmy
MPE2 logo MPE2
Stable-Retro logo Stable-Retro
ViZDoom logo ViZDoom
Repositories
Incubating Projects
Documentation
Arcade Learning Environment logo Arcade Learning Environment
HighwayEnv logo HighwayEnv
Repositories
Procgen2 logo Procgen2
Foundation
About logo About
Standards logo Standards
Donate logo Donate [-] [-]
Hide navigation sidebar
Hide table of contents sidebar
Light LogoDark Logo Gymnasium Documentation
Introduction
Basic Usage
Training an Agent
Create a Custom Environment
Recording Agents
Speeding Up Training
Gym Migration Guide
API
Env
Make and register
Spaces [-]  Toggle navigation of Spaces
Fundamental Spaces
Composite Spaces
Spaces Utils
Wrappers [-]  Toggle navigation of Wrappers
List of Wrappers
Misc Wrappers
Action Wrappers
Observation Wrappers
Reward Wrappers
Vectorize [-]  Toggle navigation of Vectorize
Wrappers
AsyncVectorEnv
SyncVectorEnv
Utility functions
Utility functions
Functional Env
Environments
Classic Control [-]  Toggle navigation of Classic Control
Acrobot
Cart Pole
Mountain Car Continuous
Mountain Car
Pendulum
Box2D [-]  Toggle navigation of Box2D
Bipedal Walker
Car Racing
Lunar Lander
Toy Text [x]  Toggle navigation of Toy Text
Blackjack
Taxi
Cliff Walking
Frozen Lake
MuJoCo [-]  Toggle navigation of MuJoCo
Ant
Half Cheetah
Hopper
Humanoid
Humanoid Standup
Inverted Double Pendulum
Inverted Pendulum
Pusher
Reacher
Swimmer
Walker2D
Atari
External Environments
Tutorials
Gymnasium Basics [-]  Toggle navigation of Gymnasium Basics
Make your own custom environment
Handling Time Limits
Implementing Custom Wrappers
Load custom quadruped robot environments
Training Agents [-]  Toggle navigation of Training Agents
Action Masking in the Taxi Environment
Running the Experiment
Visualizing Results
Results Analysis
Solving Blackjack with Tabular Q-Learning
Solving Frozenlake with Tabular Q-Learning
Training using REINFORCE for Mujoco
Speeding up A2C Training with Vector Envs
Third-Party Tutorials
Development
Github
Paper
Gymnasium Release Notes
Gym Release Notes
Contribute to the Docs
Back to top
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
Frozen Lake ¶
This environment is part of the Toy Text environments which contains general information about the environment.
Frozen lake involves crossing a frozen lake from start to goal without falling into any holes by walking over the frozen lake. The player may not always move in the intended direction due to the slippery nature of the frozen lake.
Description ¶
The game starts with the player at location [0,0] of the frozen lake grid world with the goal located at far extent of the world e.g. [3,3] for the 4x4 environment.
Holes in the ice are distributed in set locations when using a pre-determined map or in random locations when a random map is generated. Randomly generated worlds will always have a path to the goal.
The player makes moves until they reach the goal or fall in a hole.
The lake is slippery (unless disabled) so the player may move perpendicular to the intended direction sometimes (see is_slippery in Argument section).
Elf and stool from https://franuka.itch.io/rpg-snow-tileset. All other assets by Mel Tillery http://www.cyaneus.com/.
Action Space ¶
The action shape is (1,) in the range {0, 3} indicating which direction to move the player.
0: Move left
1: Move down
2: Move right
3: Move up
Observation Space ¶
The observation is a value representing the player's current position as current_row * ncols + current_col (where both the row and col start at 0). Therefore, the observation is returned as an integer.
For example, the goal position in the 4x4 map can be calculated as follows: 3 * 4 + 3 = 15. The number of possible observations is dependent on the size of the map.
Starting State ¶
The episode starts with the player in state [0] (location [0, 0]).
Rewards ¶
Default reward schedule:
Reach goal: +1
Reach hole: 0
Reach frozen: 0
See reward_schedule for reward customization in the Argument section.
Episode End ¶
The episode ends if the following happens:
Termination:
The player moves into a hole.
The player reaches the goal at max(nrow) * max(ncol) - 1 (location [max(nrow)-1, max(ncol)-1] ).
Truncation (using the time_limit wrapper):
The length of the episode is 100 for FrozenLake4x4, 200 for FrozenLake8x8.
Information ¶
step() and reset() return a dict with the following keys:
p : transition probability for the state which will be impacted by the is_slippery parameter.
Arguments ¶
FrozenLake has five parameters:
desc=None : Used to specify maps non-preloaded maps. If desc=None then map_name will be used. If both desc and map_name are None a random 8x8 map with 80% of locations frozen will be generated. To Specify a custom map - desc=["SFFF", "FHFH", "FFFH", "HFFG"] The tile letters denote:
“S” for Start tile
“G” for Goal tile
“F” for frozen tile
“H” for a tile with a hole A random generated map can be specified by calling the function generate_random_map .
map_name="4x4" - Helps load two predefined map names ( 4x4 and 8x8 )
is_slippery=True : If true the player will move in intended direction with probability specified by the success_rate else will move in either perpendicular direction with equal probability in both directions. For example, if action is left, is_slippery is True, and success_rate is 1/3, then:
P(move left)=1/3
P(move up)=1/3
P(move down)=1/3 If action is up, is_slippery is True, and success_rate is 3/4, then:
P(move up)=3/4
P(move left)=1/8
P(move right)=1/8
success_rate=1.0/3.0 : Used to specify the probability of moving in the intended direction when is_slippery=True
reward_schedule=(1, 0, 0) : Used to specify reward amounts for reaching certain tiles. The indices correspond to: Reach Goal, Reach Hole, Reach Frozen (includes Start), Respectively
Version History ¶
v1: Bug fixes to rewards (v1.3, added reward customization)
v0: Initial version release
Next MuJoCo
Previous Cliff Walking
Copyright © 2026 Farama Foundation 
On this page
Frozen Lake
Description
Action Space
Observation Space
Starting State
Rewards
Episode End
Information
Arguments
Version History
This page uses Google Analytics to collect statistics.
Deny Allow
v1.3.0 (latest)
Versions
main (unstable)
v1.3.0 (latest)
v1.2.3
v1.2.2
v1.2.1
v1.2.0
v1.1.1
v1.1.0
v1.0.0
v0.29.0
v0.28.1
v0.28.0
v0.27.1
v0.27.0
v0.26.3
v1.0.0a1
v1.0.0a2