> Source: https://www.baeldung.com/cs/goal-based-vs-utility-based-agents

Start Here
Guides  ▼ ▲ Core Concepts 
 Fundamental concepts in Computer Science 
 Operating Systems 
 Learn about the types of OSs used and the basic services they provide. 
 Neural Networks 
 Explore the theory behind neural networks and their architecture. 
 Graph Theory 
 Learn how GPS systems find the shortest routes, how engineers design integrated circuits and more real-world uses of graphs 
 Latex 
 A powerful preparation tool for creating high-quality document. 
Pricing
About  ▼ ▲ Full Archive 
 The high level overview of all the articles on the site. 
 About Baeldung 
 About Baeldung. 
Difference Between Goal-based and Utility-based Agents
Last updated:  June 29, 2024
 Written by: Subham Datta Reviewed by:  Michal Aibin Artificial Intelligence
Baeldung Pro – CS – NPI EA (cat = Baeldung on Computer Science)  
Learn through the super-clean Baeldung Pro experience:
>> Membership and Baeldung Pro.
No ads, dark-mode and 6 months free of IntelliJ Idea Ultimate to start with.
1. Overview
In this tutorial, we’ll discuss two types of artificial intelligent (AI) agents: goal-based and utility-based agents.
Finally, we’ll present the core differences between them.
2. Goal-Based Agent
A goal-based agent is an AI system designed to achieve a specific goal. The goal can be anything from navigating a maze to playing a game. Given a plan, a goal-based agent attempts to choose the best strategy to achieve it based on the environment. Furthermore, it uses search algorithms to find the most efficient path to the goal. Additionally, it also utilizes heuristics and AI techniques to improve its performance.
The goal-based agent is also known as a planning or goal-seeking agent. Additionally, we sometimes callit a rule-based agent as it follows a set of rules to achieve its goal. Furthermore, we can program the agents to take specific actions when facing certain conditions. Additionally, we can use goal-based agents in various applications, such as robotics, computer vision, and natural language processing.
Now, let’s take a look at the diagram, which summarizes the whole process of how a goal-based agent works:
Let’s take an example. Let’s assume we want to train an agent who can play the game Breakout:
Breakout is a classic arcade game in which the player controls a paddle at the bottom of the screen. The goal of the game is to use the paddle to hit a ball and prevent it from falling off the screen by bouncing it back into the play. Furthermore, the ball bounces off the walls as well as from the paddle. Additionally, the player can move the paddle left and right to try and hit the ball.
The game is over if the ball falls off the screen. Additionally, the player can earn points by hitting bricks at the top of the screen with the ball. However, the game gets progressively more difficult as the player progresses, and the ball moves faster.
In this game, the goal-based agent aims to destroy all the bricks in order to gain maximum reward. To achieve this goal, the agent must use its paddle to hit the ball and destroy all the bricks. Additionally, the agent needs to continuously evaluate its environment and take actions likely to lead it closer to its goal. Here, the agent learns by exploring the environment and setting rules for maximizing the reward.
3. Utility-Based Agent
A utility-based agent is an AI system designed to maximize a specific utility. Additionally, the utility can be anything from maximizing profits to minimizing energy consumption. Unlike a goal-based agent, a utility-based agent doesn’t have a particular goal. Instead, we design them to find the best solution based on a specific utility.
Furthermore, the utility-based agent uses optimization algorithms to find the best solution. Additionally, it also uses heuristics and AI techniques to improve its performance.
It makes decisions based on a set of predetermined criteria or a utility function. Furthermore, these criteria represent the goals or objectives of the agent. Additionally, we use the utility function to evaluate different actions or states regarding how well they achieve the given goals.
A typical utility function is to earn maximum points in a game. When presented with different possible actions, the utility-based agent chooses the one expected to optimize its utility according to its utility function.
Now, let’s take a look at the diagram, which summarizes the whole process of how a utility-based agent works:
Let’s take an example to understand how we can design a utility-based agent. Assume that we want to train an agent that can play the game Pacman. Pacman is a game where a player controls a character that can move around a maze and eat pellets. Furthermore, players can go to the next level if they collect enough pellets. However, while the player is collecting pellets, they’re vulnerable to being eaten by ghosts that enter the maze from the sides.
Additionally, if a ghost catches the player, they receive a negative reward, and the level restarts. We want to train an agent that can receive a reward for collecting pellets and a negative reward for being eaten by a ghost. For the agent to receive these rewards, we would have to embed a video of someone playing Pacman and have the agent take screengrabs of the relevant states.
These screengrabs would be what the agent uses to estimate its utility function. Additionally, the agent would try to learn patterns in the images it receives from Pacman and use these patterns to estimate the utility of different states. Furthermore, it receives information about the environment and the estimation value of the utility by taking a particular action in a given state.
Generally, utility-based agents will have a utility function as part of their model that depends upon the state, action, and reward received from a state. For example, the reward could be a profit obtained from a customer, some points received from winning a game, or the number of lives remaining in a game. Finally, the goal of the agent is to maximize the utility function.
4. Differences
We have discussed the basic concept of goal-based and utility-based agents. Now, let’s explore the core differences between them:
Goal-Based Agents   Utility-Based Agents   Goal-based agents may perform in a way that produces an unexpected outcome because their search space is limited   Utility-based agents are more reliable because they can learn from their environment and perform most efficiently   Makes decisions based on the goal and the available information   Makes decisions based on the utility and general information   Goal-based agents are easier to program   Implementing utility-based agents can be a complex task   Considers a set of possible actions before deciding whether the goal is achieved or not   Maps each state to an actual number to check how efficiently each step achieves its goals   Utilized in computer vision, robotics, and NLP   Used in GPS and tracking systems  
5. Conclusion
In this tutorial, we discussed two types of AI agents: goal-based and utility-based agents.
Finally, we presented the core differences between them.
Categories
Algorithms
Artificial Intelligence
Core Concepts
Data Structures
Latex
Networking
Security
Series
Graphs Tutorial
Neural Networks Series
LaTeX Series
About
About Baeldung
Baeldung All Access
The Full archive
Editors
Our Partners
Partner with Baeldung
eBooks
FAQ
Baeldung Pro
Terms of Service
Privacy Policy
Company Info
Contact