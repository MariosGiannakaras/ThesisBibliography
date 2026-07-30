> Source: https://gymnasium.farama.org/environments/toy_text/cliff_walking/

Cliff Walking - Gymnasium Documentation
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
Cliff Walking ¶
This environment is part of the Toy Text environments which contains general information about the environment.
Cliff walking involves crossing a gridworld from start to goal while avoiding falling off a cliff.
Description ¶
The game starts with the player at location [3, 0] of the 4x12 grid world with the goal located at [3, 11]. If the player reaches the goal the episode ends.
A cliff runs along [3, 1..10]. If the player moves to a cliff location it returns to the start location.
The player makes moves until they reach the goal.
Adapted from Example 6.6 (page 132) from Reinforcement Learning: An Introduction by Sutton and Barto [ 1].
The cliff can be chosen to be slippery (disabled by default) so the player may move perpendicular to the intended direction sometimes (see is_slippery ).
With inspiration from: https://github.com/dennybritz/reinforcement-learning/blob/master/lib/envs/cliff_walking.py
Action Space ¶
The action shape is (1,) in the range {0, 3} indicating which direction to move the player.
0: Move up
1: Move right
2: Move down
3: Move left
Observation Space ¶
There are 3 x 12 + 1 possible states. The player cannot be at the cliff, nor at the goal as the latter results in the end of the episode. What remains are all the positions of the first 3 rows plus the bottom-left cell.
The observation is a value representing the player's current position as current_row * ncols + current_col (where both the row and col start at 0).
For example, the starting position can be calculated as follows: 3 * 12 + 0 = 36.
The observation is returned as an int() .
Starting State ¶
The episode starts with the player in state [36] (location [3, 0]).
Reward ¶
Each time step incurs -1 reward, unless the player stepped into the cliff, which incurs -100 reward.
Episode End ¶
The episode terminates when the player enters state [47] (location [3, 11]).
Information ¶
step() and reset() return a dict with the following keys:
“p” - transition proability for the state.
As cliff walking is not stochastic, the transition probability returned always 1.0.
Arguments ¶
References ¶
[1] R. Sutton and A. Barto, “Reinforcement Learning: An Introduction” 2020. [Online]. Available: http://www.incompleteideas.net/book/RLbook2020.pdf
Version History ¶
v1: Add slippery version of cliffwalking
v0: Initial version release
Next Frozen Lake
Previous Taxi
Copyright © 2026 Farama Foundation 
On this page
Cliff Walking
Description
Action Space
Observation Space
Starting State
Reward
Episode End
Information
Arguments
References
Version History
This page uses Google Analytics to collect statistics.
Deny Allow
Versions