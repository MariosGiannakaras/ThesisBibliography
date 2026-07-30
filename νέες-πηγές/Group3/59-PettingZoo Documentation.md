> Source: https://pettingzoo.farama.org/

PettingZoo Documentation
Toggle site navigation sidebar
Light LogoDark Logo PettingZoo Documentation 
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
Light LogoDark Logo PettingZoo Documentation
Introduction
Basic Usage
Environment Creation
Testing Environments
API
AEC API
Parallel API
Wrappers [-]  Toggle navigation of Wrappers
PettingZoo Wrappers
Supersuit Wrappers
Shimmy Compatibility Wrappers
Utils
Environments
Atari [-]  Toggle navigation of Atari
Basketball Pong
Boxing
Combat: Plane
Combat: Tank
Double Dunk
Emtombed: Competitive
Emtombed: Cooperative
Flag Capture
Foozpong
Ice Hockey
Joust
Mario Bros
Maze Craze
Othello
Pong
Quadrapong
Space Invaders
Space War
Surround
Tennis
Video Checkers
Volleyball Pong
Warlords
Wizard of Wor
Butterfly [-]  Toggle navigation of Butterfly
Cooperative Pong
Knights Archers Zombies ('KAZ')
Pistonball
Classic [-]  Toggle navigation of Classic
Chess
Connect Four
Gin Rummy
Go
Hanabi
Leduc Hold'em
Rock Paper Scissors
Texas Hold'em No Limit
Texas Hold'em
Tic Tac Toe
SISL [-]  Toggle navigation of SISL
Multiwalker
Pursuit
Third-Party Environments
Tutorials
Custom Environment Tutorial [-]  Toggle navigation of Custom Environment Tutorial
Tutorial: Repository Structure
Tutorial: Environment Logic
Tutorial: Action Masking
Tutorial: Testing Your Environment
CleanRL Tutorial [-]  Toggle navigation of CleanRL Tutorial
CleanRL: Implementing PPO
CleanRL: Advanced PPO
Tianshou Tutorial [-]  Toggle navigation of Tianshou Tutorial
Tianshou: Basic API Usage
Tianshou: Training Agents
Tianshou: CLI and Logging
Ray RLlib Tutorial [-]  Toggle navigation of Ray RLlib Tutorial
RLlib: PPO for Pistonball
RLlib: DQN for Simple Poker
LangChain Tutorial [-]  Toggle navigation of LangChain Tutorial
LangChain: Creating LLM agents
Stable-Baselines3 Tutorial [-]  Toggle navigation of Stable-Baselines3 Tutorial
SB3: PPO for Knights-Archers-Zombies
SB3: Action Masked PPO for Connect Four
AgileRL Tutorial [-]  Toggle navigation of AgileRL Tutorial
AgileRL: Implementing DQN - Curriculum Learning and Self-play
AgileRL: Implementing MADDPG
AgileRL: Implementing MATD3
Development
Github
Release Notes
Contribute to the Docs
Back to top
Edit this page
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar 
An API standard for multi-agent reinforcement learning.
PettingZoo is a simple, pythonic interface capable of representing general multi-agent reinforcement learning (MARL) problems. PettingZoo includes a wide variety of reference environments, helpful utilities, and tools for creating your own custom environments.
The AEC API supports sequential turn based environments, while the Parallel API supports environments with simultaneous actions.
Environments can be interacted with using a similar interface to Gymnasium:
Copyright © 2023 Farama Foundation 
This page uses Google Analytics to collect statistics.
Deny Allow
1.26.1 (latest)
Versions
main (unstable)
1.26.1 (latest)
1.26.0
1.25.0
1.24.3
1.24.2
1.24.1
1.24.0
1.23.1
1.23.0
1.22.4
1.22.3