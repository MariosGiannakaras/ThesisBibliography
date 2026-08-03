> Source: https://minigrid.farama.org/

MiniGrid Documentation
Toggle site navigation sidebar
Light LogoDark Logo MiniGrid Documentation 
Farama Foundation logo Farama Foundation
Core Projects
Gymnasium logo Gymnasium
PettingZoo logo PettingZoo
Minari logo Minari
Foundation
About logo About
Standards logo Standards
Donate logo Donate
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
Incubating Projects
Documentation
Arcade Learning Environment logo Arcade Learning Environment
HighwayEnv logo HighwayEnv
Repositories
Procgen2 logo Procgen2 [-] [-]
Hide navigation sidebar
Hide table of contents sidebar
Light LogoDark Logo MiniGrid Documentation
Introduction
Basic Usage
Installation
List of Publications
Tutorial on Creating Environments
Training Minigrid Environments
Wrappers
Wrapper [-]  Toggle navigation of Wrapper
Action Bonus
Dict Observation Space
Direction Obs
FlatObs
Fully Obs
Image Observation
No Death
Observation
One Hot Partial Obs
Reseed
RGB Img Obs
RGB Partial Img Obs
Position Bonus
Stochastic Action
Symbolic Obs
View Size
Environments
Minigrid Environments [-]  Toggle navigation of Minigrid Environments
Blocked Unlock Pickup
Crossing
Dist Shift
Door Key
Dynamic Obstacles
Empty
Fetch
Four Rooms
Go To Door
Go To Object
Key Corridor
Lava Gap
Locked Room
Memory
Multi Room
Obstructed Maze Dlhb
Obstructed Maze Full
Playground
Put Near
Red Blue Door
Unlock
Unlock Pickup
BabyAI Environments [-]  Toggle navigation of BabyAI Environments
Go To Red Ball Grey
Go To Red Ball
Go To Red Ball No Dists
Go To Obj
Go To Local
Go To
Go To Imp Unlock
Go To Seq
Go To Red Blue Ball
Go To Door
Go To Obj Door
Open
Open Red Door
Open Door
Open Two Doors
Open Doors Order
Pickup
Unblock Pickup
Pickup Loc
Pickup Dist
Pickup Above
Put Next Local
Put Next
Unlock
Unlock Local
Key In Box
Unlock Pickup
Blocked Unlock Pickup
Unlock To Unlock
Action Obj Door
Find Obj S5
Key Corridor
One Room S8
Move Two Across
Synth
Synth Loc
Synth Seq
Mini Boss Level
Boss Level
Boss Level No Unlock
WFC Environments [-]  Toggle navigation of WFC Environments
WFC Maze Simple
WFC Dungeon Maze Scaled
WFC Rooms Fabric
WFC Obstacles Blackdots
WFC Obstacles Angular
WFC Obstacles Hogs3
WFC Maze Knot
WFC Maze Wall
WFC Rooms Office
WFC Obstacles Hogs2
WFC Skew2
WFC Maze
WFC Maze Spirals
WFC Maze Paths
WFC Mazelike
WFC Dungeon
WFC Dungeon Rooms
WFC Dungeon Less Rooms
WFC Dungeon Spirals
WFC Rooms Magic Office
WFC Skew Cave
WFC Skew Lake
Development
Release Notes
Github
Back to top
Edit this page
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar 
Minigrid contains simple and easily configurable grid world environments to conduct Reinforcement Learning research. This library was previously known as gym-minigrid.
This library contains a collection of 2D grid-world environments with goal-oriented tasks. The agent in these environments is a triangle-like agent with a discrete action space. The tasks involve solving different maze maps and interacting with different objects such as doors, keys, or boxes. The design of the library is meant to be simple, fast, and easily customizable.
In addition, the environments found in the BabyAI repository have been included in Minigrid and will be further maintained under this library.
The Gymnasium interface allows to initialize and interact with the Minigrid default environments as follows:
To cite this project please use:
Copyright © 2026 Farama Foundation 
This page uses Google Analytics to collect statistics.
Deny Allow
Versions