> Source: https://www.mathworks.com/help/reinforcement-learning/ug/train-q-learning-agent-to-solve-basic-grid-world.html

Train Reinforcement Learning Agent in Basic Grid World - MATLAB & Simulink
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
Training and Simulation
Reinforcement Learning Toolbox
Get Started with Reinforcement Learning Toolbox
Train Reinforcement Learning Agent in Basic Grid World
On this page
Create Grid World Environment
Create Q-Learning Agent
Train Q-Learning Agent
Validate Q-Learning Results
Create and Train SARSA Agent
Validate SARSA Training
See Also
Documentation
Examples
Functions
Blocks
Apps
Videos
Answers
Main Content
Train Reinforcement Learning Agent in Basic Grid World
Open in MATLAB Online
Copy Code Copy Command
This example shows how to solve a grid world environment using reinforcement learning by training Q-learning and SARSA agents. For more information on these agents, see Q-Learning Agent and SARSA Agent.
Fix Random Number Stream for Reproducibility
The example code might involve computation of random numbers at several stages. Fixing the random number stream at the beginning of some sections in the example code preserves the random number sequence in the section every time you run it, which increases the likelihood of reproducing the results. For more information, see Results Reproducibility.
Fix the random number stream with seed 0 and random number algorithm Mersenne twister. For more information on controlling the seed used for random number generation, see rng .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
The output previousRngState is a structure that contains information about the previous state of the stream. You will restore the state at the end of the example.
This grid world environment has the following configuration and rules:
The grid world is 5-by-5 and bounded by borders, with four possible actions (North = 1, South = 2, East = 3, West = 4).
The agent begins from cell [2,1] (second row, first column).
The agent receives a reward +10 if it reaches the terminal state at cell [5,5] (blue).
The environment contains a special jump from cell [2,4] to cell [4,4] with a reward of +5.
The agent is blocked by obstacles (black cells).
All other actions result in –1 reward.  
Create Grid World Environment
Create the basic grid world environment.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
To specify that the initial state of the agent is always [2,1], create a reset function that returns the state number for the initial agent state. This function is called at the start of each training episode and simulation. States are numbered starting at position [1,1]. The state number increases as you move down the first column and then down each subsequent column. Therefore, create an anonymous function handle that sets the initial state to 2 .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Use the getActionInfo and getObservationInfo functions to extract the action and observation specification objects from the environment.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Create Q-Learning Agent
To create a Q-learning agent, first create a Q table using the observation and action specifications from the grid world environment. Set the learning rate of the optimizer to 0.01 .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
To approximate the Q-value function within the agent, create a rlQValueFunction approximator object, using the table and the environment information.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Next, create a Q-learning agent using the Q-value function.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Configure agent options such as the epsilon-greedy exploration and the learning rate for the function approximator.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
For more information on creating Q-learning agents, see rlQAgent and rlQAgentOptions .
Train Q-Learning Agent
To train the agent, first specify the training options. For this example, use the following options:
Train for a maximum of 200 episodes. Specify that each episode lasts for most 50 time steps.
Stop the training when the agent receives an average cumulative reward of 11 over 30 consecutive episodes.
For more information on training options, see rlTrainingOptions .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Fix the random stream for reproducibility.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Train the Q-learning agent using the train function. Training can take several minutes to complete. To save time while running this example, load a pretrained agent by setting doTraining to false . To train the agent yourself, set doTraining to true .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
The Reinforcement Learning Training Monitor window opens and displays the training progress. 
Validate Q-Learning Results
Fix the random stream for reproducibility.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
By default, the agent uses a greedy (hence deterministic) policy in simulation. To use the exploratory policy instead, set the UseExplorationPolicy agent property to true .
Before running the simulation, visualize the environment, configure the visualization to maintain a trace of the agent states, and clear any previously existing trace.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Simulate the agent in the environment using the sim function.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
The agent trace shows that the agent successfully finds the jump from cell [2,4] to cell [4,4].
Create and Train SARSA Agent
To create a SARSA agent, use the same Q value function and epsilon-greedy configuration as for the Q-learning agent. For more information on creating SARSA agents, see rlSARSAAgent and rlSARSAAgentOptions .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Train the SARSA agent using the train function. Training can take several minutes to complete. To save time while running this example, load a pretrained agent by setting doTraining to false . To train the agent yourself, set doTraining to true .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Validate SARSA Training
Fix the random stream for reproducibility.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
By default, the agent uses a greedy (hence deterministic) policy in simulation. To use the exploratory policy instead, set the UseExplorationPolicy agent property to true .
Before running the simulation, visualize the environment and configure the visualization to maintain a trace of the agent states.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
Simulate the agent in the environment.
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
The SARSA agent finds the same grid world solution as the Q-learning agent.
Restore the random number stream using the information stored in previousRngState .
Get
Copy Code Block
Copy openExample Command Paste command in MATLAB to download and open example files openExample("rl/BasicGridWorldExample") Copy
Open in MATLAB Online
See Also
Functions
createGridWorld | sim | train
Objects
rlSARSAAgentOptions | rlSARSAAgent | rlMDPEnv | rlTrainingOptions | rlQAgent | rlQAgentOptions
Topics
Train Reinforcement Learning Agent in MDP Environment
Q-Learning Agent
SARSA Agent
Reinforcement Learning Agents
Train Reinforcement Learning Agents
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