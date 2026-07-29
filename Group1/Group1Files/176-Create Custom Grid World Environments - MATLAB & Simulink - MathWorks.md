> Source: https://www.mathworks.com/help/reinforcement-learning/ug/create-custom-grid-world-environments.html

Create Custom Grid World Environments - MATLAB & Simulink
Skip to content
MATLAB Help Center
Search or ask a question
MATLAB Help Center
Community
Learning
Get MATLAB MATLAB
Sign In
My Account
My Community Profile
Link License
Sign Out
Contact MathWorks Support
Visit mathworks.com
MATLAB MATLAB
Help Center Help Center
MathWorks MathWorks
MATLAB Answers MATLAB Answers
File Exchange File Exchange
Videos Videos
Online Training Online Training
Blogs Blogs
Cody Cody
MATLAB Drive MATLAB Drive
ThingSpeak ThingSpeak
Bug Reports Bug Reports
Community Community
Off-Canvas Navigation Menu Toggle Contents
Documentation Home
Control Systems
Reinforcement Learning Toolbox
Environments
Create Custom Grid World Environments
On this page
Create Grid World Object
Configure Grid World Object
Create Grid World Environment from Grid World Object
Environment Visualization
Actions
Observations
Grid World Dynamics
Rewards
Reset Function
Create a Default Agent for this Environment
Step Function
References
See Also
Documentation
Examples
Functions
Blocks
Apps
Videos
Answers
Main Content
Create Custom Grid World Environments
A custom grid world environment is a MATLAB ® environment featuring a generic two-dimensional grid with actions, observations, rewards, dynamics, and optional obstacles and terminal states that are mostly left for you to define. As in any grid world environment, the goal of the agent is to move in a way to maximize its expected discounted cumulative long-term reward.
Grid world environments are a special case of Markov Decision Process (MDP) environments. An MDP is a discrete time stochastic control process. It provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of the decision maker. In a grid world environment, the state represents a position in a two-dimensional grid, while the action represents a move from the current position to the next, which an agent might attempt. To create a custom MDP environment, see Markov Decision Process (MDP) Environments, createMDP , and rlMDPEnv . 
You can use a custom grid world environment to analyze the behavior of different discrete-time agents on custom grid worlds, and to explore reinforcement learning concepts. For example, many common benchmark reinforcement learning problems are grid world problems, and you can study them with Reinforcement Learning Toolbox™ by creating a custom grid world environments.
To create a custom grid world environment:
Create the grid world object.
Configure the grid world object.
Use the grid world object to create your environment.
To load a grid world environment with predefined actions, observations, rewards, and dynamics, see Use Predefined Grid World Environments.
Create Grid World Object
You can create your own grid world model using the createGridWorld function. Specify the grid size when creating the GridWorld object.
For example, at the MATLAB command line, type:
Note
The grid world model GW is a GridWorld object, not an environment object. You must later create an rlMDPEnv environment object from GW .
The GridWorld object has these properties.
Property
Read-Only
Description GridSize
Yes
Dimensions of the grid world, displayed as a row vector containing two positive integers. The first integer m is the number of rows in the grid, and the second integer n is the number of columns in the grid. CurrentState
No
Name of the current state of the environment. This name corresponds to the current agent position in the grid, and it is specified as a string or character vector such as "[a,b]" . Here, a and b are two positive integers less than m and n , respectively, that indicate the row (a) and the column (b) corresponding to the agent position on the grid. Specifying this property in any other format results in an error when the environment step function is executed on an environment built using GW . By default, this property is set to the string "[1,1]" .
You can use this property to set the initial state of the environment. For example, the command GW.CurrentState = "[2,4]"; sets the current position of the agent in the cell located in the second row and the fourth column of the grid. On an 8-by-7 grid this position is encoded as environment state number 26, using the formula 8*(4-1) + 2 = 26 .
If you call the step function on an environment built using GW , the environment executes the function from the state indicated by CurrentState . Note that every time the environment reset function is called, the environment state is reset according to the specific code in the reset function. For more information on step and reset functions, see Create Custom Environment Using Step and Reset Functions. States
Yes
A string vector containing the state names of the grid world, as specified in the CurrentState property. For example, for a 2-by-2 grid world model GW , you can specify the state names as follows.
You can use the state2idx function to obtain the state index associated with a state name. Actions
Yes
A string vector containing the list of possible actions that the agent can execute in the grid world environment. You can set the actions when you create the grid world model by using the moves argument.
For example, at the MATLAB command line, type:
Here, m and n are integers as specified in GridSize , and moves is a string that can be either "Standard" or "Kings" . moves GW.Actions "Standard" ["N";"S";"E";"W"] , indicates that the agent can attempt to move north, south, east, and west from its current grid position. The step function of the environment built using GW encodes these moves using integers from 1 to 4. For example, step(env,3) indicates that the agent attempts to move east from its current position. "Kings" ["N";"S";"E";"W";"NE";"NW";"SE";"SW"] indicating that the agent can attempt to move north, south, east, west, northeast, northwest, southeast and southwest, respectively, from its current grid position. The step function of the environment built using GW encodes these moves using integers from 1 to 8, so that, for example, step(env,8) indicates that the agent attempts to move southwest from its current position.
You can use the action2idx function to obtain the action index associated with a state name. T
No
State transition matrix, specified as a 3-D array in which every row of each page contains nonnegative numbers that must add up to one.
The state transition matrix T is a probability matrix in which each entry indicates the likelihood of the agent moving from the current state s to any possible next state s' by performing action a .  T can be denoted as
T ( s , s ' , a ) = p r o b a b i l i t y ( s ' | s , a ) T is:
A K -by- K -by-4 array, if moves is specified as "Standard" . Here, K = m * n .
A K -by- K -by-8 array, if moves is specified as "Kings" .
When you create a grid world object, the default transition matrix contains standard deterministic transitions corresponding to the four or eight actions that the agent can execute. Specifically, the default transition matrix is such that any attempted move in any direction results in the agent moving one cell in that direction with probability of one, except for any attempted move outside the grid, which results in the agent keeping its current position.
For example, consider a 5-by-5 deterministic grid world object GW with the agent in cell [3,1] . View the state transition matrix for the north direction.
Here, the number 1 in the last dimension encodes the attempted move north, as specified in the Actions property. 
In this figure, the value of northStateTransition(3,2) is 1. This value indicates that when the agent is in the position [3,1] , following the action 'N' , the agent moves to the position [2,1] with a probability of 1 (and with a probability of 0 to the other cells specified in the same row).
Note
Because each number in a row represents the probability of moving from the cell indexed by the column into the cell indexed by the row, all the numbers along a row must always add to either one or zero (within the tolerance specified in ProbabilityTolerance ). To set transition probabilities, first, set an entire row to zero, then set the non-zero probabilities all at once. For an example, see createGridWorld or createMDP . Alternatively, copy the transition matrix into a variable, modify the variable, and then assign it back as transition matrix of your grid world object.
To index specific states and actions in the transition matrix, you can use the state2idx and action2idx functions. For example:
For an example on how to set the transition matrix, see createGridWorld . R
No
Reward transition matrix, specified as a 3-D array. R determines how much reward the agent receives after performing an action in the environment.
Each entry of the reward transition matrix specifies the reward that the agent obtains when moving from the current state s to any possible next state s' by performing action a :
r = R ( s , s ' , a ) . R has the same shape and size as the state transition matrix T . Specifically, R is:
A K -by- K -by-4 array, if moves is specified as "Standard" . Here, K = m * n .
A K -by- K -by-8 array, if moves is specified as "Kings" .
When you create a grid world object, the reward matrix is zero.
Set up R so that there is a reward to the agent after every action. For example, you can set up a positive reward if the agent transitions over obstacle states and when it reaches the terminal state. You can also set up a reward of –1 for any action the agent takes, independent of the current state and next state.
To index specific states and actions in the reward matrix, you can use the state2idx and action2idx functions. For example:
For an example on how to set the reward matrix, see createGridWorld . ObstacleStates
No ObstacleStates are states that cannot be reached in the grid world, specified as a string vector. Consider this 5-by-5 grid world object GW . 
This syntax specifies the obstacle states, represented by black squares in the figure.
When you set obstacle states, the transition matrix T automatically updates so that if the agent attempts to move into an obstacle, its resulting position is the same as its current position, with a probability of one.
For an example on how to set obstacles, see createGridWorld . TerminalStates
No TerminalStates are the final states in the grid world, specified as a string vector. Consider the picture of the previous 5-by-5 grid world model GW . The blue cell is the terminal state and you can specify it with this command.
When you set terminal states, the transition and reward matrices of GW automatically update so that both the probability of moving out of the terminal state and the reward for staying in the terminal state is zero. Additionally, for any environment env created from GW , the step function returns an is-done value of true as its third output argument when the agent moves in a terminal state. As a result, when you use the train or sim functions, the training or simulation episode stops when the agent reaches the terminal state.
For an example on how to set terminal states, see createGridWorld . ProbabilityTolerance
No
This property is the tolerance for the sum of probabilities along a row of the transition matrix.
Because the sum of numbers along a row of the transition matrix represents the probability of moving into the state indexed by the row number, all the numbers along a row must add to either one or zero, within the tolerance specified in ProbabilityTolerance . If this condition is not verified, an error is thrown.
To set transition probabilities, first, set an entire row to zero, then set the non-zero probabilities all at once. For an example, see createGridWorld or createMDP . Alternatively, copy the transition matrix into a variable, modify the variable, and then assign it back as transition matrix of your grid world object.
Configure Grid World Object
After creating your GridWorld object, you need to configure its transition matrix, to make sure it represents your desired dynamics. You also need to configure its reward matrix to make sure the agent gets the appropriate rewards for its moves.
Because each row of each page of the transition matrix must always sum to one, you cannot modify the transition matrix entries in place one at a time. Instead, assign the default matrix to a temporary variable, in the workspace, modify the variable entries appropriately, and then reassign the modified variable to the transition matrix of your GridWorld object.
For example, create a GridWorld object with five rows and five columns.
Extract the default transition matrix, which already contains the standard transition dynamics.
Modify the temporary matrix so that from state 6 any action leads to state 10.
Update the transition matrix of your GridWorld object.
Create Grid World Environment from Grid World Object
After configuring your GridWorld object, use it to create an MDP environment using rlMDPEnv . This step is necessary because the GridWorld object is not an environment object.
For example, if you have the GridWorld object gw in the MATLAB workspace, at the command line, type:
This command creates the environment env that contains your GridWorld object.
If necessary, you can set your own reset function. For example, to make sure the agent always starts from state number 2, set the ResetFcn environment property to the handle of an anonymous function that always returns 2.
For more information on the reset function, see Reset Function.
Environment Visualization
As with other grid world environments, you can visualize the environment using the plot function. A red circle represents the current agent position, that is, the environment state. If present, the terminal locations and obstacles are represented by blue and black squares, respectively.
Note
Visualizing the environment during training can provide insight, but it tends to increase training time. For faster training, keep the environment plot closed during training.
Actions
Depending on the Actions property of the underlying GridWorld model, the action channel carries a scalar integer ranging from either 1 to 4 or 1 to 8.
When Actions is set to "Standard" , the integer indicates an (attempted) move in the directions north, south, east, or west, respectively.
When Actions is set to "Kings" , the integer indicates an (attempted) move in the directions north, south, east, west, northeast, northwest, southeast and southwest, respectively.
For more information, see Create Grid World Object.
In either case, the action specification is an rlFiniteSetSpec object. To extract the action specification, use the getActionInfo function.
Observations
As in all grid world environments, the environment observation has a single channel carrying a scalar integer from 1 to the number of environment states. The observation indicates the current agent location (that is, the environment state) in column-wise fashion. So, the observation specification is an rlFiniteSetSpec object. To extract the observation specification, use the getObservationInfo function.
Grid World Dynamics
As for all grid world environments, the transition matrix property T of the underlying GridWorld object determines the dynamics.
The default transition matrix is such that any attempted move in any direction results in the agent moving one cell in that direction with a probability of one, except for any attempted move outside the grid, which results in the agent maintaining its current position.
For more information, see Create Grid World Object and Configure Grid World Object.
Rewards
As for all grid world environments, the reward matrix property R of the underlying GridWorld object determines the reward.
The default reward matrix contains only zeroes.
For more information, see Create Grid World Object and Configure Grid World Object.
Reset Function
The state of a custom grid world environment is initially set to 1 , which is equivalent to the string "[1,1]" , representing the most northwestern position of the grid. The default reset function for a custom grid world environment then sets the initial environment state (that is, the initial position of the agent on the grid), randomly.
You can write your own reset function to specify a different initial state. For example, to specify that the initial state of the environment is always 5, create a reset function that always returns 3 , and set the ResetFcn property to the handle of the function.
A training or simulation function automatically calls the reset function at the beginning of each training or simulation episode.
Create a Default Agent for this Environment
The environment observation and action specifications allow you to create an agent (with discrete action space) that works with your environment. For example, create a default AC agent.
If needed, modify the agent options using dot notation.
You can now use both the environment and the agent as arguments for the built-in functions train and sim , which train or simulate the agent within the environment.
You can also create and train agents for this environment interactively using the Reinforcement Learning Designer app. For an example, see Design and Train Agent Using Reinforcement Learning Designer.
For more information on creating agents, see Reinforcement Learning Agents.
Step Function
As in other MATLAB environments, you can also call the environment step function to return the next observation, reward, and an is-done scalar indicating whether the environment reaches a final state.
For example, call the step function with an action input of 2 to move the agent south.
The environment step and reset functions allow you to create a custom training or simulation loop. For more information on custom training loops, see Train Reinforcement Learning Policy Using Custom Training Loop.
References
[1] Sutton, Richard S., and Andrew G. Barto. Reinforcement Learning: An Introduction. Second edition. Adaptive Computation and Machine Learning. Cambridge, Mass: The MIT Press, 2018.
See Also
Functions
createMDP | createGridWorld | rlPredefinedEnv | getObservationInfo | getActionInfo | train | sim
Objects
rlMDPEnv | rlNumericSpec | rlFiniteSetSpec | rlFunctionEnv | rlMultiAgentFunctionEnv | rlTurnBasedFunctionEnv | SimulinkEnvWithAgent
Topics
Train Reinforcement Learning Agent in Basic Grid World
Reinforcement Learning Environments
Thank you for your feedback!
Why did you choose this rating?
Submit
How useful was this information? [x]
Unrated [-] 1 1 star [-] 2 2 stars [-] 3 3 stars [-] 4 4 stars [-] 5 5 stars
MATLAB Command
You clicked a link that corresponds to this MATLAB command:
Run the command by entering it in the MATLAB Command Window. Web browsers do not support MATLAB commands.
Close  
Select a Web Site
Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: United States.
United States
United States (English)
United States (Deutsch)
United States (Français)
United States（简体中文）
United States (English)
You can also select a web site from the following list
How to Get Best Site Performance
Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.
Americas
América Latina (Español)
Canada (English)
United States (English)
Europe
Belgium (English)
Denmark (English)
Deutschland (Deutsch)
España (Español)
Finland (English)
France (Français)
Ireland (English)
Italia (Italiano)
Luxembourg (English)
Netherlands (English)
Norway (English)
Österreich (Deutsch)
Portugal (English)
Sweden (English)
Switzerland
Deutsch
English
Français
United Kingdom (English)
Asia Pacific
Australia (English)
India (English)
New Zealand (English)
中国
简体中文
English
日本 (日本語)
한국 (한국어)
Contact your local office
Trust Center
Trademarks
Privacy Policy
Preventing Piracy
Application Status
Contact Us
Your Privacy Choices
© 1994-2026 The MathWorks, Inc.
Select a Web Site United States