> Source: https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/

Make your own custom environment - Gymnasium Documentation
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
Toy Text [-]  Toggle navigation of Toy Text
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
Gymnasium Basics [x]  Toggle navigation of Gymnasium Basics
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
Edit this page
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
Note
This tutorial is compatible with Gymnasium version 1.3.0.
Make your own custom environment ¶
This tutorial shows how to create new environment and links to relevant useful wrappers, utilities and tests included in Gymnasium.
Setup ¶
Recommended solution ¶
Install pipx following the pipx documentation.
Then install Copier:
Alternative solutions ¶
Install Copier with Pip or Conda:
or
Generate your environment ¶
You can check that Copier has been correctly installed by running the following command, which should output a version number:
Then you can just run the following command and replace the string path/to/directory by the path to the directory where you want to create your new project.
Answer the questions, and when it's finished you should get a project structure like the following:
Subclassing gymnasium.Env ¶
Before learning how to create your own environment you should check out the documentation of Gymnasium's API.
To illustrate the process of subclassing gymnasium.Env , we will implement a very simplistic game, called GridWorldEnv . We will write the code for our custom environment in gymnasium_env/envs/grid_world.py . The environment consists of a 2-dimensional square grid of fixed size (specified via the size parameter during construction). The agent can move vertically or horizontally between grid cells in each timestep. The goal of the agent is to navigate to a target on the grid that has been placed randomly at the beginning of the episode.
Observations provide the location of the target and agent.
There are 4 actions in our environment, corresponding to the movements “right”, “up”, “left”, and “down”.
A done signal is issued as soon as the agent has navigated to the grid cell where the target is located.
Rewards are binary and sparse, meaning that the immediate reward is always zero, unless the agent has reached the target, then it is 1.
An episode in this environment (with size=5 ) might look like this:
where the blue dot is the agent and the red square represents the target.
Let us look at the source code of GridWorldEnv piece by piece:
Declaration and Initialization ¶
Our custom environment will inherit from the abstract class gymnasium.Env . You shouldn't forget to add the metadata attribute to your class. There, you should specify the render-modes that are supported by your environment (e.g., "human" , "rgb_array" , "ansi" ) and the framerate at which your environment should be rendered. Every environment should support None as render-mode; you don't need to add it in the metadata. In GridWorldEnv , we will support the modes “rgb_array” and “human” and render at 4 FPS.
The __init__ method of our environment will accept the integer size , that determines the size of the square grid. We will set up some variables for rendering and define self.observation_space and self.action_space . In our case, observations should provide information about the location of the agent and target on the 2-dimensional grid. We will choose to represent observations in the form of dictionaries with keys "agent" and "target" . An observation may look like {"agent": array([1, 0]), "target": array([0, 3])} . Since we have 4 actions in our environment (“right”, “up”, “left”, “down”), we will use Discrete(4) as an action space. Here is the declaration of GridWorldEnv and the implementation of __init__ :
Constructing Observations From Environment States ¶
Since we will need to compute observations both in reset and step , it is often convenient to have a (private) method _get_obs that translates the environment's state into an observation. However, this is not mandatory and you may as well compute observations in reset and step separately:
We can also implement a similar method for the auxiliary information that is returned by step and reset . In our case, we would like to provide the manhattan distance between the agent and the target:
Oftentimes, info will also contain some data that is only available inside the step method (e.g., individual reward terms). In that case, we would have to update the dictionary that is returned by _get_info in step .
Reset ¶
The reset method will be called to initiate a new episode. You may assume that the step method will not be called before reset has been called. Moreover, reset should be called whenever a done signal has been issued. Users may pass the seed keyword to reset to initialize any random number generator that is used by the environment to a deterministic state. It is recommended to use the random number generator self.np_random that is provided by the environment's base class, gymnasium.Env . If you only use this RNG, you do not need to worry much about seeding, but you need to remember to call super().reset(seed=seed) to make sure that gymnasium.Env correctly seeds the RNG. Once this is done, we can randomly set the state of our environment. In our case, we randomly choose the agent's location and the random sample target positions, until it does not coincide with the agent's position.
The reset method should return a tuple of the initial observation and some auxiliary information. We can use the methods _get_obs and _get_info that we implemented earlier for that:
Step ¶
The step method usually contains most of the logic of your environment. It accepts an action , computes the state of the environment after applying that action and returns the 5-tuple (observation, reward, terminated, truncated, info) . See gymnasium.Env.step() . Once the new state of the environment has been computed, we can check whether it is a terminal state and we set done accordingly. Since we are using sparse binary rewards in GridWorldEnv , computing reward is trivial once we know done .To gather observation and info , we can again make use of _get_obs and _get_info :
Rendering ¶
Here, we are using PyGame for rendering. A similar approach to rendering is used in many environments that are included with Gymnasium and you can use it as a skeleton for your own environments:
Close ¶
The close method should close any open resources that were used by the environment. In many cases, you don't actually have to bother to implement this method. However, in our example render_mode may be "human" and we might need to close the window that has been opened:
In other environments close might also close files that were opened or release other resources. You shouldn't interact with the environment after having called close .
Registering Envs ¶
In order for the custom environments to be detected by Gymnasium, they must be registered as follows. We will choose to put this code in gymnasium_env/__init__.py .
The environment ID consists of three components, two of which are optional: an optional namespace (here: gymnasium_env ), a mandatory name (here: GridWorld ) and an optional but recommended version (here: v0). It might have also been registered as GridWorld-v0 (the recommended approach), GridWorld or gymnasium_env/GridWorld , and the appropriate ID should then be used during environment creation.
The keyword argument max_episode_steps=300 will ensure that GridWorld environments that are instantiated via gymnasium.make will be wrapped in a TimeLimit wrapper (see the wrapper documentation for more information). A done signal will then be produced if the agent has reached the target or 300 steps have been executed in the current episode. To distinguish truncation and termination, you can check info["TimeLimit.truncated"] .
Apart from id and entrypoint , you may pass the following additional keyword arguments to register :
Most of these keywords (except for max_episode_steps , order_enforce and kwargs ) do not alter the behavior of environment instances but merely provide some extra information about your environment. After registration, our custom GridWorldEnv environment can be created with env = gymnasium.make('gymnasium_env/GridWorld-v0') . gymnasium_env/envs/__init__.py should have:
If your environment is not registered, you may optionally pass a module to import, that would register your environment before creating it like this - env = gymnasium.make('module:Env-v0') , where module contains the registration code. For the GridWorld env, the registration code is run by importing gymnasium_env so if it were not possible to import gymnasium_env explicitly, you could register while making by env = gymnasium.make('gymnasium_env:gymnasium_env/GridWorld-v0') . This is especially useful when you're allowed to pass only the environment ID into a third-party codebase (eg. learning library). This lets you register your environment without needing to edit the library's source code.
Creating a Package ¶
The last step is to structure our code as a Python package. This involves configuring pyproject.toml . A minimal example of how to do so is as follows:
Creating Environment Instances ¶
Now you can install your package locally with:
And you can create an instance of the environment via:
You can also pass keyword arguments of your environment's constructor to gymnasium.make to customize the environment. In our case, we could do:
Sometimes, you may find it more convenient to skip registration and call the environment's constructor yourself. Some may find this approach more pythonic and environments that are instantiated like this are also perfectly fine (but remember to add wrappers as well!).
Using Wrappers ¶
Oftentimes, we want to use different variants of a custom environment, or we want to modify the behavior of an environment that is provided by Gymnasium or some other party. Wrappers allow us to do this without changing the environment implementation or adding any boilerplate code. Check out the wrapper documentation for details on how to use wrappers and instructions for implementing your own. In our example, observations cannot be used directly in learning code because they are dictionaries. However, we don't actually need to touch our environment implementation to fix this! We can simply add a wrapper on top of environment instances to flatten observations into a single array:
Wrappers have the big advantage that they make environments highly modular. For instance, instead of flattening the observations from GridWorld, you might only want to look at the relative position of the target and the agent. In the section on ObservationWrappers we have implemented a wrapper that does this job. This wrapper is also available in gymnasium_env/wrappers/relative_position.py :
Download Python source code: environment_creation.py
Download Jupyter notebook: environment_creation.ipynb
Next Handling Time Limits
Previous Gymnasium Basics
Copyright © 2026 Farama Foundation 
On this page
Make your own custom environment
Setup
Recommended solution
Alternative solutions
Generate your environment
Subclassing gymnasium.Env
Declaration and Initialization
Constructing Observations From Environment States
Reset
Step
Rendering
Close
Registering Envs
Creating a Package
Creating Environment Instances
Using Wrappers
This page uses Google Analytics to collect statistics.
Deny Allow
Versions