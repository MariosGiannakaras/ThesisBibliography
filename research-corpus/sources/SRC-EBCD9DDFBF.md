> Source: https://aaltodoc.aalto.fi/bitstreams/20230aa7-e046-437e-bb26-56c0fbc7109a/download

Master’s programme in Master’s Programme in ICT Innovation 
Safe Reinforcement Learning for Real Robots 
Bridging the simulation to reality gap using Domain Randomization 
Juan Pablo Valdivia 
Master’s Thesis 2023
© 2023 
This work is licensed under a Creative Commons “Attribution-NonCommercial-ShareAlike 4.0 Interna-tional” license.
Author Juan Pablo Valdivia Title Safe Reinforcement Learning for Real Robots — Bridging the simulation to 
reality gap using Domain Randomization Degree programme Master’s Programme in ICT Innovation Major Autonomous Systems Supervisor Prof. Joni Pajarinen Advisors Alberto Hata, Ahmad Terra Collaborative partner Ericsson Date 3 September 2023 Number of pages 69 Language English 
Abstract This thesis explores the field of Safe Reinforcement Learning (SRL), a subset of reinforcement learning that emphasizes the safety of the agent during the learning process, focusing on its application in robotics implementing Trust Region Conditional Value at Risk (TRC) algorithm for SRL. The primary objectives are to teach an SRL model to navigate safely in a complex environment and to effectively bridge the sim-to-real gap, allowing for a smooth transfer from computer simulations to real-world environments. The main challenge in SRL is ensuring the agent’s safety throughout the learning process, which requires maintaining optimal performance despite the uncertainties and dynamic variables present in real-world environments. For the simulated training, the SafetyGym simulator was used, which is built on the MuJoCo physics engine. When it came to real-world tests, the Robot Operating System (ROS) was the chosen platform, using TurtleBot 2i, a versatile mobile robot platform equipped with a range of sensors, including the SICK TIM551 LiDAR, which has the capability to accurately measure distances for perception purposes. Different methods were explored to address the objectives, with Domain Randomization (DR) emerging as the top choice, a technique that involves randomizing the parameters of the simulation environment during training to help the model generalize better to the real-world. Interestingly, while the model without DR learned three times faster in simulations, it struggled in real-world tests. In the toughest test, it did not succeed even once. In contrast, the model trained with domain randomization passed every time. This model was further refined with real-world training, showing significant improvement in challenging situations. Ultimately, this research highlights the value of DR in ensuring that robots can use what they learn in simulations in the real-world, especially in situations where safety is crucial. 
Keywords Artificial Intelligence, Robotics, Reinforcement Learning, Safety, Domain Randomization, Transfer Learning, Autonomous Systems.
Preface 
First and foremost, I extend my deepest gratitude to my family, especially my parents Juan and Marion for their unconditional support throughout every decision I’ve made in my life. I am profoundly thankful to Alberto Hata and Ahmad Terra, my academic supervisors at Ericsson, for their support during my work, the help to use Ericsson’s resources, their recommendations, and their knowledge, and I look forward to the possibility of collaborating again in the future. Also, thanks to Joni Pajarinen, my academic supervisor for the guidance and the helpful tips in my thesis. Finally, of course, thanks to all my friends from Chile, los Tripode, los Jakis and the amazing people that I have met in Sweden and Finland, and a special affection to Paloma, whose presence has been truly special in my life. 
Otaniemi, 3 September 2023 
Juan Pablo Valdivia 
4
Contents 
Abstract 3 
Preface 4 
Contents 5 
Symbols and abbreviations 7 
1 Introduction 8 1.1 Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.2 Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 
2 Literature Review 11 2.1 Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . 11 2.2 Deep Q-learning . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2.3 Safe Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . 14 
2.3.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.3.2 Constrained Policy Optimization . . . . . . . . . . . . . . . 17 2.3.3 Conditional Value at Risk . . . . . . . . . . . . . . . . . . 18 2.3.4 Trust Region Conditional Value at Risk . . . . . . . . . . . 18 
2.4 Sim-to-Real Transfer . . . . . . . . . . . . . . . . . . . . . . . . . 20 2.4.1 Zero-shot and One-shot Transfer . . . . . . . . . . . . . . . 20 2.4.2 System Identification . . . . . . . . . . . . . . . . . . . . . 21 2.4.3 Domain Randomization Methods . . . . . . . . . . . . . . 21 2.4.4 Domain Adaptation Methods . . . . . . . . . . . . . . . . . 22 2.4.5 Learning with Disturbances . . . . . . . . . . . . . . . . . 24 
2.5 Real-world training . . . . . . . . . . . . . . . . . . . . . . . . . . 24 2.6 Simulation tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 2.7 Turtlebot 2i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 2.8 Robot Operating System (ROS) . . . . . . . . . . . . . . . . . . . . 29 
3 Method 31 3.1 Simulated Environment . . . . . . . . . . . . . . . . . . . . . . . . 31 3.2 TRC implementation . . . . . . . . . . . . . . . . . . . . . . . . . 34 3.3 State Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 3.4 Action Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 3.5 Domain Randomization . . . . . . . . . . . . . . . . . . . . . . . . 38 3.6 Fine-tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 
4 Experiments 41 4.1 Hardware and Software Specifications . . . . . . . . . . . . . . . . 41 
4.1.1 Notebook Hardware . . . . . . . . . . . . . . . . . . . . . 41 4.1.2 Robot NUC Hardware . . . . . . . . . . . . . . . . . . . . 41 4.1.3 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 
5
4.2 Simulation Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 4.2.1 Simple Environment . . . . . . . . . . . . . . . . . . . . . 42 4.2.2 Randomized Environment . . . . . . . . . . . . . . . . . . 43 
4.3 Real-world Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . 45 
5 Results 50 5.1 Simulation results . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 5.2 Real-world testing results . . . . . . . . . . . . . . . . . . . . . . . 54 
6 Conclusions 60 6.1 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 6.2 Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61 
6
Symbols and abbreviations 
Symbols 𝑉 value function 𝑄 state-action value function 𝜋 reinforcement learning policy function 
Operators ∇ × A curl of vector in A d d𝑡 
derivative with respect to variable 𝑡 
𝜕 
𝜕𝑡 partial derivative with respect to variable 𝑡∑︁ 
𝑖 sum over index 𝑖 A · B dot product of vectors A and B 
Abbreviations AI Artificial Intelligence ML Machine Learning ANN Artificial Neural Network MDP Markov Decision Process CMDP Constrained Markov Decision Process RL Reinforcement Learning SRL Safe Reinforcement Learning CV Constraint Violation DR Domain Randomization TRPO Trust-Region Policy Optimization CPO Constrained Policy Optimization TRC Trust Region Conditional Value 
7
1 Introduction 
Reinforcement learning (RL) is a branch of machine learning that aims to train machines to perform tasks autonomously using techniques inspired by animal behavior. This approach is particularly fascinating as it seeks to mimic the evolution and behavior of animals in a machine, combining knowledge from various scientific areas [69]. RL algorithms enable an agent to learn from its environment by interacting with it and receiving feedback in the form of rewards or punishments. This methodology has been successfully applied in various domains, including robotics [17]. However, implementing RL algorithms in real-world robots presents significant challenges due to the potential risk of causing damage to the robot, humans, or the surrounding environment during the interaction process [40, 82]. This risk is particularly high because the training of the RL model is usually performed in a simulation, which can generate unsafe behavior of the agent when deployed in the real-world. Therefore, Safe Reinforcement Learning (SRL) has become a crucial research area to ensure the safe and reliable deployment of RL in robotics. 
Simulated training is commonly preferred for several reasons. Firstly, it is costeffective as it negates the risk of physical damage to the robot or its surroundings. Second, it facilitates the collection of a large amount of data in a relatively short time since simulations can be executed much faster than real-time and concurrently. Lastly, it allows the agent to be tested in a variety of scenarios and conditions that may be challenging or impossible to replicate in the real-world. However, simulation environments often fail to accurately reflect the real-world, resulting in a ’simulation-to-reality gap.’ This gap can lead the agent to display unsafe behaviors that were not encountered or adequately addressed during simulation training. Consequently, most studies in this field have been conducted in simulated environments to minimize these risks. Simulations offer a controlled environment where the potential for harm is significantly reduced and the cost of interactions is minimal. Nonetheless, the use of simulations also presents challenges, especially when transferring what the robot has learned in the simulation to the real-world. This issue, known as the ’sim-to-real’ gap, is a major hurdle in the field of RL [39]. Therefore, methods to improve the deployment of RL algorithms, such as Transfer Learning [45] in combination with SRL, have become crucial research areas to reduce the sim-to-real gap and ensure the safe and reliable deployment of RL in robotics. 
SRL is a critical area of study in the field of robotics, particularly in environments that are uncertain, harmful, or require extensive exploration. The main challenge in SRL is to find the optimum balance for exploration to learn new tasks with the safety to prevent harm or damage to the robot or the environment. This balance is especially important in real-world applications, where the consequences of unsafe actions can be severe. An approach to this challenge is proposed in the work of Thananjeyan [72], where they introduce a method called Recovery RL. This method splits the goals of improving task performance and ensuring safety into two different policies: 
 Task policy that focuses only on optimizing the task rewards obtained from the
environment. 
 Recovery policy that guides the agent to safety states when there is a likelihood of constraint violation or possible danger. 
This approach allows the agent to have more effective navigation dealing with the trade-off between exploration and safety, which is one of the main challenges in SRL, improving performance in both simulated and real-world environments. 
Previous research has also investigated the field of SRL such as [1, 32, 28, 31, 80]. These studies have shown the potential of SRL algorithms to improve the safety and reliability of robotic systems, particularly in scenarios where humans and robots collaborate. In RL or SRL, typically a huge number of iterations with the environment is necessary to learn an optimal policy. In real-world settings, this process can be both time-consuming and resource-consuming. Moreover, each interaction carries a potential risk of causing harm if the robot’s actions are not safe [44]. 
Factors contributing to this gap include incorrect modeled dynamics, incorrect simulation parameters, and numerical errors. The sim-to-real gap becomes even more pronounced in locomotion tasks, where a robot’s agile motion and frequent changes in contact with the environment can fragment the control space. Even minor discrepancies in the model can lead to significant differences in outcomes, making the task of overcoming the gap a challenging one [70]. The concept of sim-to-real transfer is a solution to this problem, intending to bridge the gap between the simulated and real-world environments. It involves training a model in a simulated environment, where it can safely learn through trial and error without any harm, and after that transferring the learned knowledge to the real-world. This method allows the model to train without the risk of causing damage or consuming excessive resources. 
Despite these challenges, there have been attempts to bridge the sim-to-real gap. For instance, [28] successfully deployed and compared multiple methods on real robots, demonstrating their practical applicability in real-world scenarios. However, there is still room for further exploration and improvement, particularly in knowledge transfer between different simulators and robotic platforms. 
1.1 Objective The primary objective of this master’s thesis is to explore and improve the knowledge transfer capabilities in SRL algorithms, specifically in the context of mobile robots, while ensuring the preservation of safety policies. The exploration involves studying different Transfer Learning methods with the specific aim of enhancing the adaptability of SRL models during their transition from simulated to real-world environments. Thus, the SRL models will be capable of maintaining the safety policies learned during simulation training while improving their performance in real-world scenarios. The specific mobile robot for this work is Turtlebot 2i [73], a differential robot equipped 
9
with a range of sensors and actuators, which is an ideal robot system for this research due to its ability to navigate through diverse environments easily. Additionally, real-world training will be implemented to increase the performance of the Turtlebot in a real-world environment. This will allow a beneficial comparison with the model trained in the simulation. This work will then assess the need for real-world training and determine whether training only in a simulation environment is sufficiently effective. The objectives outlined in this master’s thesis are designed to address a main research question: 
 How can Transfer Learning enhance the adaptability and safety of reinforcement learning models when transitioning from simulated to real-world robotic environments? 
The relevance of this research question lies in the critical need to ensure the safety and adaptability of RL models when applied to real-world environments. As it was mentioned before the majority of RL models are trained in simulated environments due to the reduced risks and costs associated with this approach. However, the transition from simulated to real-world environments often results in a simulation-to-reality gap, where the model exhibits unsafe or unpredictable behaviors that were not encountered or adequately addressed during simulation training. This gap represents a significant obstacle to the safe and reliable deployment of RL models in real-world applications. Therefore, investigating the role of Transfer Learning to enhance the adaptability and safety of RL models is crucial for the successful operation of robotic systems in dynamic and unpredictable environments. 
1.2 Structure The following parts of the thesis are organized as follows: 
 Section 2 provides a comprehensive review of the existing literature in SRL, focusing on the algorithm TRC, the use of simulators, and the applications to mobile robots. 
 Section 3 gives an in-depth explanation of the methods used in the thesis, including the use of OpenAI gym simulation environments, Domain Randomization algorithm, and the real-world training of the mobile robot. 
 Section 4 shows a detailed description of the implementation of the different methods and the configurations performed within the simulated environments and real-world scenarios. 
 Section 5 presents, analyses, and compares the different results obtained from the experiments. 
 Section 6 provides the summary of the research findings, their implications, and finally the suggestions for future research based on the findings of the thesis. 
10
2 Literature Review 
In this section, a comprehensive review of the relevant literature is presented. The discussion delves into the foundational concepts, methodologies, and recent advancements in the field of Safe Reinforcement Learning (SRL). Additionally, the literature on transfer learning in the context of robotics is explored, along with an examination of tools used for both simulation and real-world robot training. This background will help set the stage for the specific research and findings presented later in the thesis. 
2.1 Reinforcement Learning Reinforcement learning (RL) is a popular method in robotics for training an agent to make decisions and act in an environment to maximize a reward signal. RL has been applied to a variety of robotic tasks such as manipulation, grasping, navigation, and autonomous flying, among others. In RL, an agent learns through trial and error by taking actions in the environment and receiving feedback in the form of rewards or penalties as can be seen in Figure 1. The problems in RL can be viewed as a Markov Decision Process (MDP) with unknown transition probabilities and reachable states [37]. An MDP is defined as a tuple (𝑆, 𝐴, 𝑃, 𝛾, 𝑅), where: 
 𝑆 is a finite set of states 
 𝐴 is a finite set of actions 
 𝑃 denotes the probability of state transition from state 𝑠 to 𝑠′ after taking action 𝑎 represented as: 
𝑃𝑎 𝑠𝑠 
′ = 𝑃(𝑠, 𝑎, 𝑠 ′) = P[𝑠′| (𝑠, 𝑎)] 
 𝛾 is the discount factor, which is a value between 0 and 1 
 𝑅 is the reward function 
11
Figure 1: Basic Reinforcement Learning Diagram. 
At each time step 𝑡, the agent selects and performs an action 𝑎𝑡 , which results in a transition to a new state 𝑠𝑡+1 and a reward or penalty 𝑟𝑡 = 𝑅(𝑠𝑡 , 𝑎𝑡) associated with that action. The agent uses this information to update its understanding of the environment. The agent’s goal is to maximize the return 𝐺 defined as: 
𝐺 𝑡 = 𝑟𝑡+1 + 𝛾𝑟𝑡+2 + · · · = ∞∑︁ 𝑘=0 
𝛾𝑘𝑟𝑡+𝑘+1 (1) 
Learning the optimal policy of the environment, either through an existing model of the environment (model-based) or through sampling experience (model-free). The return𝐺 𝑡 is calculated as the sum of discounted future rewards starting from time-step 𝑡. 
Two important aspects of RL in robotics are the continuous state and action space, which require sophisticated algorithms to efficiently learn from experience. A common approach to handling this is to use function approximators, such as neural networks, to estimate the value function or policy as in [18]. This has led to the development of deep reinforcement learning algorithms, which have demonstrated impressive results in robotics. 
Furthermore, the trade-off between exploration and exploitation is also critical in RL for robotics, as it determines the balance between exploring the state space to gather more information and exploiting learned knowledge to maximize the reward signal. The choice of exploration strategy is task-dependent and can greatly affect the performance of the agent [81]. For example, consider a scenario where a mobile robot is learning how to reach the end of a maze. In the early stages of learning, the agent might adopt a high variance Gaussian distribution for its actions, indicating a high level of exploration in discovering all the different paths. This could involve trying out a wide range of strategies, even those that seem risky or inefficient, to gather information about the maze. As the agent learns more about the maze and its strategy 
12
improves, the variance of the Gaussian distribution might decrease, indicating a shift toward exploitation. The agent now focuses more on using the strategies that it has found to be effective, rather than trying out new ones. 
Although reinforcement learning has proven to be a powerful tool for solving robotic problems and has the potential to further revolutionize the field of robotics, it still faces many challenges, such as sample efficiency, robustness, and generalization, that need to be addressed to make it more applicable to real-world robotics which is the main objective in this thesis. 
2.2 Deep Q-learning Q-learning is a popular method in reinforcement learning, a type of machine learning algorithm in which an agent learns to make decisions by interacting with an environment. In Q-learning, the agent learns the value of taking certain actions in specific states. This is done by estimating the expected rewards for each action in each state, which are stored in a table called the Q-table. Over time, as the agent explores its environment and receives feedback in the form of rewards or penalties, it updates the Q-table values. The goal is to find the best action to take in each state to maximize the total reward over time. 
Deep Q-learning is a variant of the Q-learning algorithm that uses deep neural networks to represent the action value function or the Q-table. This approach is particularly well suited to robotic applications, where the state space is often highdimensional and the dynamics of the system are complex. By using this approach, the algorithm can efficiently manage vast state spaces and intricate dynamics. This adaptability is essential in robotics, where the state can encompass various data such as images, joint positions, and various sensor outputs. 
In the process of choosing actions, the agent typically chooses the one with the highest value for the current state [84]. After taking an action, the agent updates its value table using the Bellman Expectation Equation for the State-Action Value Function (Q-Function) for a given policy 𝜋: 
𝑄𝜋 (𝑠, 𝑎) = E𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝑟𝑡+1 |𝑠0 = 𝑠, 𝑎0 = 𝑎 
]︄ (2) 
This equation states that the quality of a state-action pair (𝑄𝜋 (𝑠, 𝑎)) is determined by the immediate reward and the discounted future quality over all possible states and actions. The MDP is solved once the agent finds the optimal Q-function (𝑄∗(𝑠, 𝑎)) over all the possible policies, where: 
𝑄∗(𝑠, 𝑎) = max 𝜋 𝑄𝜋 (𝑠, 𝑎) 
The goal of RL is to find the optimal policy, which is done by updating the quality values until 𝑄𝜋 (𝑠, 𝑎) = 𝑄∗(𝑠, 𝑎). This is accomplished through the Q-value update, which is given by the equation: 
13
𝑄𝜋 (𝑠, 𝑎) = (1 − 𝛼)𝑄𝜋 (𝑠, 𝑎) + 𝛼[𝑟𝑡+1 + 𝛾max 𝑎′∈𝐴 
𝑄𝜋 (𝑠′, 𝑎′) −𝑄𝜋 (𝑠, 𝑎)] 
In this equation, the learning rate 𝛼 determines the impact of new observations on the updated Q-value. In the early stages of training, a high learning rate is preferred, but its value should gradually decrease over time to prevent large updates later on. 
A common exploration strategy used in deep Q-learning is epsilon-greedy [37]. The basic idea is that with probability 𝜖 , the agent will select a random action, rather than the action with the highest estimated value. This exploration allows the agent to explore new actions and states, rather than getting stuck in a local optimum. With probability 1 − 𝜖 , the agent will select the action with the highest estimated value, which is called greedy policy, following the equation: 
𝑎𝑡 = 
⎧⎪⎪⎨⎪⎪⎩ argmax 
𝑎 
𝑄(𝑠, 𝑎) with probability 1 − 𝜖 
random action otherwise 
The Q-learning technique gained popularity with advancements in computing power and was popularized by the work of [36], where they used Deep Q-Networks (DQN) to teach an RL agent to play Atari games at a level comparable to that of a professional human player. There are two common methods to improve DQN: experience replay and use of a target network. 
The experience replay method involves recording recent transitions, consisting of state, action, reward, and next state, in a tuple. During training, the agent randomly selects from this collection of transitions to learn from previous experiences. The target network is a copy of the primary Artificial Neural Network (ANN) with fixed weights. During training, its weights are periodically updated from the primary network. This approach is used for loss computation to prevent unstable training, as using a separate, fixed ANN helps to avoid sudden changes in weights during training. 
2.3 Safe Reinforcement Learning In recent decades, RL has been applied to solve complex tasks in robotics [1, 6, 9, 13, 19, 21, 25, 29, 30, 34, 42, 47, 48, 53]. Despite the success of RL in these fields, ensuring safety in real-world RL applications remains a significant challenge. Catastrophic consequences can arise if safety is not adequately considered in RL applications. For instance, robots that interact with humans must not cause harm, and recommendation systems should not recommend false or discriminatory information. For instance, in the context of self-driving cars, safety is even more important and must be ensured while carrying out tasks in real-world environments [20]. Before going deeper into this subject it is essential to define a clear understanding of the term "safety." Drawing from the Oxford Dictionary [49], "safety" is interpreted to mean “the condition of being protected from or unlikely to cause danger, risk, or injury.” Building 
14
on this, in the world of RL as mentioned in [5], "Safety in AI systems, particularly in RL, refers to the challenges associated with ensuring that AI agents behave in ways that are aligned with human values, avoid unintended negative consequences, and can be robustly controlled even as they learn and improve their capabilities." This understanding will guide our talk about safety in this study. 
In the practical application of RL, safety is a significant concern that remains unsolved and is considered one of the key issues in AI safety. Although this problem has gained attention in the field of RL, it still poses a challenge. Additionally, research has shown that safe RL techniques such as minus variance and percentile optimization are typically NP-hard problems making them computationally challenging to solve [77]. In some cases, ensuring the safety of the agent is more important than maximizing its reward. This is particularly true in real-world scenarios where safety is imperative, such as when operating near humans. As data and learning-based robot control methods improve constantly, researchers must understand when and how to best leverage them in real-world scenarios [13]. 
2.3.1 Background 
The concept of SRL is typically modeled as a Constrained Markov Decision Process (CMDP) [1], which involves maximizing agent reward and at the same time the agent is satisfying the safety constraints. Previous research has extensively examined CMDP problems in both tabular and linear cases [4, 7, 8, 27, 59, 60, 61]. However, the application of deep-safe RL to high-dimensional and continuous CMDP optimization problems is a relatively new field that has emerged in recent years. Neural networks are used to represent proximal optimal values that represent safe states or actions. This section provides an overview of the deep safe RL problem formulation in terms of the objective functions of safe RL. 
In SRL, the objective of an optimal policy 𝜋 is to maximize the reward and minimize the cost by selecting an action 𝑎, where Π𝑆 is the policy set, and 𝑇 ∼ 𝜋 is a trajectory defined as 𝑇 = (𝑠0, 𝑎0, 𝑠1, ...). The trajectory depends on the initial state distribution 𝜌0(·) and the policy 𝜋. The state distribution function is defined as 𝑑 𝑠0 𝜋 (𝑠) = (1 − 𝛾)∑︁∞ 
𝑡=0 𝛾 𝑡P𝜋 (𝑠𝑡 = 𝑠 |𝑠0), which represents the discounted state distribu-
tion starting at 𝑠0. The expected state distribution starting from 𝜌0(·) is presented as 𝑑 𝜌0 𝜋 (𝑠) = E𝑠0∼𝜌0 (·) [𝑑 
𝑠0 𝜋 (𝑠)]. 
The state-value function and state-action value function are defined as: 
𝑉𝜋 (𝑠) = E𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝑟𝑡+1 |𝑠0 = 𝑠 
]︄ 𝑄𝜋 (𝑠, 𝑎) = E𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝑟𝑡+1 |𝑠0 = 𝑠, 𝑎0 = 𝑎 
]︄ 
15
respectively. The advantage function 𝐴𝜋 (𝑠, 𝑎) = 𝑄𝜋 (𝑠, 𝑎) − 𝑉𝜋 (𝑠) is defined as the difference between the state-action value function and the state value function. The expected return function 𝐽 (𝜋) is defined as: 
𝐽 (𝜋) = E𝑠∼𝜌0 (·) [𝑉𝜋 (𝑠)] . A CMDP extends an MDP by including an additional constraint set C = 
{(𝑐𝑖, 𝑏𝑖)}𝑚𝑖=1, where 𝑐𝑖 is the cost function, 𝑏𝑖 is the safety constraint bound and 𝑚 the total number of sets. The cost value functions 𝑉 𝑐𝑖𝜋 are defined as 𝑉 𝑐𝑖𝜋 (𝑠) = 
E𝜋 [ ∑︁∞ 𝑡=0 𝛾 
𝑡𝑐𝑖 (𝑠𝑡 , 𝑎𝑡) |𝑠0 = 𝑠]. Similarly, 𝑄𝑐𝑖𝜋 and 𝐴𝑐𝑖𝜋 can be defined in the same way. The feasible policy set ΠC consists of policies that satisfy all safety constraints, i.e., 
ΠC = ∩𝑚𝑖=1{𝜋 ∈ ΠS and 𝐶𝑖 (𝜋) ≤ 𝑏𝑖} The goal of safe RL is to find an optimal policy that maximizes the reward 
performance while minimizing the cost and ensuring the safety constraints are satisfied. Mathematically, this can be expressed as: 
max 𝜋∈ΠC 
𝐽 (𝜋), subject to 𝐶𝑖 (𝜋) ≤ 𝑏𝑖 for all 𝑖 ∈ [1, 𝑚] (3) 
where 𝐽 (𝜋) is the expected cumulative reward of following policy 𝜋 and 𝐶𝑖 (𝜋) is the expected cumulative cost of following policy 𝜋 while satisfying the safety constraint 𝐶𝑖 ≤ 𝑏𝑖. The solution to this problem provides the optimal policy that maximizes the reward while minimizing the cost and ensuring that the safety constraints are satisfied. 
Safe RL methods that account for cumulative constraints introduce three types of constraints. The first is the discounted cumulative constraint: 
𝐽 𝜋𝜃 𝐶𝑖 
= E𝜏∼𝜋𝜃 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝐶𝑖 (𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ]︄ ≤ 𝑏𝑖 (4) 
The second is the mean valued constraint: 
𝐽 𝜋𝜃 𝐶𝑖 
= E𝜏∼𝜋𝜃 
[︄ 1 𝑁 
𝑇−1∑︁ 𝑡=0 
𝛾𝑡𝐶𝑖 (𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ]︄ ≤ 𝑏𝑖 (5) 
The third is the probabilistic constraint, which enforces that the probability of exceeding a certain cost threshold 𝜂: 
𝐽 𝜋𝜃 𝐶𝑖 
= 𝑃 
(︄∑︁ 𝑡 
𝐶𝑖 (𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ≥ 𝜂 )︄ ≤ 𝑏𝑖 (6) 
Instantaneous constraints, on the other hand, can be either explicit or implicit. Explicit constraints have a closed-form expression, which can be numerically checked, such as the cost incurred by the agent at each time step. Implicit constraints do not have a closed-form expression, such as the probability of an agent crashing into an unsafe area at each time step. 
16
Most Constrained Markov Decision Process (CMDP) methods focus on cumulative cost optimization. However, some CMDP methods optimize performance by considering immediate costs [52]. It is more natural to evaluate the cost of a whole trajectory rather than at the level of individual states or actions [14]. In the context of CMDPs, the focus on immediate costs versus cumulative costs can have significant implications for the agent’s behavior and the overall system performance. While cumulative cost optimization provides a holistic view of the agent’s trajectory, optimizing for immediate costs allows for more fine-grained control and adaptability in dynamic environments [4]. This is particularly useful in scenarios where the agent may encounter rapidly changing conditions or where long-term planning is less feasible. Immediate cost optimization can also be beneficial for handling explicit and implicit instantaneous constraints, as it allows the system to make real-time adjustments to ensure safety or other critical performance metrics. Therefore, the choice between focusing on immediate or cumulative costs should be carefully considered based on the specific requirements and constraints of the application at hand [17]. 
2.3.2 Constrained Policy Optimization 
Constrained Policy Optimization (CPO) [1] is a trust region-based method to solve an expectation-constrained RL problem and the problem is written as follows: 
maximize 𝜌,𝜋 
E𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝑅(𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ]︄ 
s.t. E 𝜌,𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝐶 (𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ]︄ ≤ 𝑑 
1 − 𝛾 
where 𝑑 is a limit value for the safety constraint and 𝜌 is the initial state distribution. Achiam et al. [1] derive the following subproblem to update policy 𝜋′ within the trust region of policy 𝜋. 
maximize 𝜋′ 
E 𝑠∼𝑑 𝜋 𝑎∼𝜋 
[︃ 𝜋′(𝑎 |𝑠) 𝜋(𝑎 |𝑠) 𝐴 
𝜋 (𝑠, 𝑎) ]︃ 
(7) 
s.t. 
⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩ E 𝑠∼𝜌 
[𝑉𝜋 𝐶 (𝑠)] + 1 
1−𝛾 E 𝑠∼𝑑 𝜋 𝑎∼𝜋 
[︂ 𝜋′ (𝑎 |𝑠) 𝜋(𝑎 |𝑠) 𝐴 
𝜋 𝐶 (𝑠, 𝑎) 
]︂ ≤ 𝑑 
1−𝛾 
E 𝑠∼𝑑 𝜋 
[𝐷𝐾𝐿 (𝜋 | |𝜋′) [𝑠]] ≤ 𝛿 
(8) 
where 𝐷𝐾𝐿 is the Kullback-Leibler divergence, which is a measure of how one probability distribution diverges from a second, 𝑑𝜋 (𝑠) := (1 − 𝛾)∑︁∞ 
𝑡=0 𝛾 𝑡P𝜋 (𝑠𝑡 = 𝑠) is 
the discounted state distribution. Then, a suboptimal policy is obtained by iteratively solving the subproblem in 7 with linear approximations on the objective and the safety constraint and quadratic approximations on the KL divergence term. 
17
2.3.3 Conditional Value at Risk 
Before presenting the primary method, it is crucial to introduce the concepts and definitions of Conditional Value at Risk (CVaR), which is one of the representative risk measures used to analyze the tails of distributions in financial portfolios [41] as well as in SRL is also used as a risk metric. Given the cumulative density function (CDF) on a variable 𝑋 , CVaR is obtained by calculating the expectation only for the region where the CDF value is above a specific risk level 𝛼. 
CVaR𝛼 (𝑋) = E [𝑋 |𝑋 ≥ ICDF(1 − 𝛼)] where ICDF is the inverse cumulative density function. If the variable 𝑋 follows a 
Gaussian distribution N(𝜇, 𝜎), CVaR can be expressed in a simple closed-form as follows: 
CVaR𝛼 (𝑋) = 𝜇 + 𝜙(Φ−1(𝛼)) 
𝛼 𝜎 (9) 
where 𝜙(𝑥) = 1√ 2𝜋 
exp(− 𝑥2 
2 ) and Φ(𝑥) = 1 2 (1 + erf( 𝑥√ 
2 )) [24]. For general distri-
bution, CVaR can be estimated from sampling, which is computationally expensive. Therefore, to provide a practical method, we assume that 𝐶𝜋 follows a Gaussian distribution to utilize the closed-form in 9 as commonly used in [3, 6]. To get the mean and variance of the distribution over 𝐶𝜋, the cost square function 𝑆𝜋 
𝐶 is defined 
as follows: 
𝑆𝜋𝐶 (𝑠) := E𝜋 [︁ 𝐶2 𝜋 |𝑠0 = 𝑠 
]︁ 𝑆𝜋𝐶 (𝑠, 𝑎) := E𝜋 
[︁ 𝐶2 𝜋 |𝑠0 = 𝑠, 𝑎0 = 𝑎 
]︁ Additionally, the cost square advantage function is definedas 𝐴𝜋 
𝐶 (𝑠, 𝑎) := 𝑆𝜋 
𝐶 (𝑠, 𝑎)− 
𝑆𝜋 𝐶 (𝑠). The expectation of the discounted cost sum𝐶𝜋 and square of the discounted cost 
sum𝐶2 𝜋 are denoted as 𝐽𝐶 (𝜋) := E𝑠∼𝜌 [𝑉𝜋𝐶 (𝑠)] and 𝐽𝑆 (𝜋) := E𝑠∼𝜌 [𝑆𝜋𝐶 (𝑠)], respectively. 
Then, the discounted cost sum can be expressed as 𝐶𝜋 ∼ N(𝐽𝐶 (𝜋), 𝐽𝑆 (𝜋) − 𝐽𝐶 (𝜋)2). Finally, the CVaR of 𝐶𝜋 can be approximated as follows [6]: 
CVaR𝛼 (𝐶𝜋) ≈ 𝐽𝐶 (𝜋) + 𝜙(Φ−1(𝛼)) 
𝛼 
√︁ 𝐽𝑆 (𝜋) − 𝐽𝐶 (𝜋)2 
2.3.4 Trust Region Conditional Value at Risk 
In real-world robotics applications, the implementation of SRL methods is still a challenging task. This is primarily due to the necessity for ensuring safety during training and maintaining stability in the learned policies. A comprehensive framework that can effectively evaluate the performance of SRL methods is also a crucial requirement. 
To this end, Trust Region Conditional Value at Risk (TRC) [28] approach is being considered. TRC follows the Constrained Policy Optimization (CPO) Section 2.3.2 structure and is based on the risk measure Conditional Value at Risk (CVaR) 
18
Section 2.3.3, which was also mentioned in the survey [20]. The use of TRC is expected to provide additional insights into the safety and stability of safe RL methods in real-world robotics applications. 
TRC is a trust region-based method, which aims to solve the problem of constrained reinforcement learning (CRL) by maximizing the discounted reward sum while limiting the CVaR of the discounted cost sum to a given value. This task poses a challenge as estimating the CVaR of any policy within the trust region in a differentiable form is difficult. 
To address this challenge, the authors of the work [28] derived an upper bound on the CVaR and replaced the CVaR constraint with the upper bound. Assuming that the discounted cost sum follows a Gaussian distribution and formulating the CVaR in a closed form as previously established in [87, 71]. Then they derive an upper bound on the square of the discounted cost sum and extend it to obtain the upper bound on the CVaR, which can be approximated in a differentiable form within a trust region. This approximation is then used to construct a CVaR-constrained subproblem, which is solved iteratively with Linearly Constrained Quadratic Convex Linear Programming (LQCLP) as previously outlined in [1]. Moreover, the method employs generalized advantage estimations (GAEs) [63] to reduce the variance of the policy gradient estimate. By utilizing TRC, they aim to provide a more effective and efficient method for solving CVaR-constrained RL problems, which can be used in various real-world applications. 
The proposed method utilizes the trust region approach and addresses a safe RL problem with CVaR constraints, which are more conservative than the expectation of discounted cost sums in that CVaR focuses on the tail of the distribution. The CVaR-constrained problem is formulated as: 
maximize 𝜌,𝜋 
E𝜋 
[︄ ∞∑︁ 𝑡=0 
𝛾𝑡𝑅(𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) ]︄ 
s.t. CVaR𝛼 (𝐶𝜋) ≤ 𝑑 
1 − 𝛾 (10) 
The first line of the equation is the objective function. It is trying to maximize the expected cumulative discounted reward over an infinite horizon which represents the length of the episode. Here, 𝜋 represents the policy that the agent is following, 𝑅(𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1) is the reward function, 𝛾 is the discount factor, and 𝑡 is the time step. The expectation is taken over all possible trajectories 𝜏 that can be generated by following policy 𝜋. 
The second line of the equation is the CVaR constraint of the discounted cost sum. In this context, 𝐶𝜋 represents the cost incurred by following policy 𝜋. This constraint establishes that the CVaR of the cost, at a certain risk level 𝛼, should be less than or equal to a certain value 𝑑, which represents the maximum acceptable risk 
19
level for the policy, divided by 1 − 𝛾. This constraint ensures that the policy does not incur too much risk, as measured by the CVaR of the cost. 
2.4 Sim-to-Real Transfer Sim-to-real transfer is an emerging research area that aims to bridge the gap between simulation and the real-world. This technique has gained significant attention in recent years because of its potential to enable robots to learn complex tasks in a simulated environment and then transfer that knowledge to the real-world. However, this is a challenging process due to the "sim-to-real gap", a common problem not just in robotics, but in any system that uses simulated data to represent the real-world. In the context of RL sim-to-real gap is defined as the difference between the value function of the learned policy 𝜋 and the value function of an optimal policy 𝜋∗𝑤 for the real-world: 
Gap(𝜋) = 𝑉𝜋∗𝑤 (𝑠) −𝑉𝜋 (𝑠) (11) 
This gap refers to the differences that exist between a simulated environment and the real-world. Simulations, by their very nature, are simplifications and approximations of the real-world. They do not capture all the complexities or unpredictability of real-world environments such as physical properties like friction, lighting, and material properties can be extremely difficult to model accurately in a simulation. 
Additionally, simulations are commonly deterministic, which means that given the same initial states, conditions, and actions, the simulation’s output will be always the same. On the other hand, the real-world is stochastic, with a degree of randomness and unpredictability. This discrepancy can lead to a model that performs well in the simulation but fails when transferred to the real-world. These factors contribute to the sim-to-real gap, making it a crucial challenge in the field of robotics and machine learning. 
Research on sim-to-real transfer has seen a significant increase, with a considerably larger number of publications on the topic. This surge in interest has led to the pursuit of various research directions, and in this section, a summary of the most notable and representative methods according to the work [88], are presented. 
2.4.1 Zero-shot and One-shot Transfer 
One straightforward approach to transferring what an agent has learned in simulation to the real-world is through zero-shot transfer. This method involves either creating a highly accurate simulation or extensively training the agent in the simulation such that it can be directly deployed in a real-world environment without further adaptation. In contrast, there is the one-shot transfer technique, which emphasizes constructing detailed models of the real-world and often leverages domain randomization to bridge the gap between simulation and reality [46]. 
20
2.4.2 System Identification 
System identification focuses on creating an accurate mathematical model of a physical system, especially in the realm of robotics. The primary objective is to bridge the gap between simulation and reality, ensuring that behaviors developed in simulation are transferable and effective in real-world scenarios. To enhance the realism of the simulator, meticulous calibration is imperative. This involves refining the physics simulator with real-world data, modeling the physics of contact, and even simulating tactile outputs based on simulated contact forces at the robot’s end effector [66]. 
2.4.3 Domain Randomization Methods 
Domain randomization (DR) has been identified as the most widely adopted method for increasing the realism of the simulation and better preparation for the real-world according to [88]. This technique is used to train models in simulated environments with the goal of transferring the learned knowledge to real-world scenarios. Instead of meticulously modeling all the parameters of the real-world, this approach introduces randomness into key parameters within the simulator. This strategy aims to create a broader distribution of simulated data that covers real-world data, thereby mitigating the sim-to-real gap and biases between the simulation and reality. Figure 2 illustrates the paradigm of DR, which involves randomizing various components of the simulator. 
Figure 2: DR data distribution expanding the simulated data to reach the real-world data [88]. 
Furthermore, depending on the components to be randomized, two types of randomization methods are identified: 
 Visual randomization: This type is related to vision tasks such as object localization [74], object detection [76], pose estimation [91], and semantic segmentation [38], the training data from simulator always have different textures, lighting, and camera positions from the realistic environments. Therefore, visual DR aims to provide enough simulated variability of the visual parameters at 
21
training time such that at test time the model is able to generalize to real-world data. 
 Dynamics randomization: Adding randomization to the visual input is complemented by dynamics randomization that also helps to acquire a robust policy particularly where the controlling policy is needed. For instance, to learn dexterous in-hand manipulation policies for a physical five-fingered hand, [50] randomizes various physical parameters in the simulator, such as object dimensions, objects and robot link masses, surface friction coefficients, robot joint damping coefficients, and actuator force gains. 
To extend the concept of DR, the environment with complete accessibility was designated as the "source domain," which, in this instance, corresponds to the simulated environment. On the other hand, the environment to which the model is intended to be transferred is defined as the "target domain" in this case the physical world. The training process happens inside the source domain. Within this domain, there is a set of randomization parameters N that can be controlled. These parameters are configured based on samples drawn from a designated randomization space, Ξ ⊂ R𝑁 . For each parameter a random variable 𝜉𝑖, {𝑖 = 1, ..., 𝑁} is defined which are sampled using Gaussian distribution N(𝜇, 𝜎2). 
Data from each episode is derived from the source domain with applied randomization. Consequently, the policy is exposed to a variety of environments, facilitating its learning and generalization capabilities. The policy parameter 𝜃 is trained to maximize the expected reward 𝑅(.) across a distribution of configurations: 
𝜃∗ = argmax 𝜃 
E𝜉∼Ξ [E𝜏∼𝑒 𝜉 [𝑅(𝜏)]] (12) 
where 𝜏 is the collected trajectory in the source domain 𝑒𝜉 randomized by 𝜉 [85]. The variance of the Gaussian distribution is applied based on the nature of the parameters to be randomized. 
This approach is aligned with the successful sim-to-real transfer experiments that demonstrate the potent impact of DR. [26] not only typically randomizes the simulated data to cover the real-world data distribution but also offers an intriguing alternative approach. They suggest translating the randomized simulated images and real-world images into canonical sim images. This sim-to-real approach, demonstrated by training a vision-based robotic manipulation system, not only bridges the gap between simulation and reality but also enhances the robot’s ability to generalize its learning to new, unseen environments, thereby improving its overall performance and adaptability. 
2.4.4 Domain Adaptation Methods 
Domain adaptation techniques are utilized to improve the performance of a learned model on a target domain with less available data by using data from the source domain. Since the feature spaces in the source and target domains are often different, 
22
making them unified is crucial for effective knowledge transfer. Domain adaptation has been extensively studied in vision-based tasks, including image classification [83] and semantic segmentation [24]. However, this research focuses on RL and its applications in robotics. In such scenarios, domain adaptation is used as priors for building RL agents or other controlling tasks [26, 10, 86], following pure vision-related tasks. There are also works on image-to-policy that use domain adaptation to generalize the policies learned from synthetic data or accelerate learning on real-world robots [10]. Sometimes, domain adaptation is directly used to tackle domain shift problems in RL tasks [23]. 
Based on the definition of MDP Section 2.1, the formalization of the domain adaptation in a RL setting is defined as: 
𝐷𝑆 ≡ (𝑆𝑆, 𝐴𝑆, 𝑃𝑆, 𝑅𝑆) for the source domain 
𝐷𝑇 ≡ (𝑆𝑇 , 𝐴𝑇 , 𝑃𝑇 , 𝑅𝑇 ) for the target domain Due to the perceptual-reality gap [62], in RL scenarios the source and target may 
differ significantly, then (𝑆𝑆 ≠ 𝑆𝑇 ). However, both domains share the same action spaces and transitions P(𝐴𝑆 ≈ 𝐴𝑇 , 𝑃𝑆 ≈ 𝑃𝑇 ), and their reward functions R have similar structures (𝑅𝑆 ≈ 𝑅𝑇 ). 
The survey paper on simulation-to-real transfer [88] summarizes three domain adaptation methods that can be applied to various tasks, including vision tasks and RL-based control tasks. These methods provide different views to unify features from different domains and are as follows: 
1. Discrepancy-based: these methods measure the feature distance between source and target domains by calculating pre-defined statistical metrics, in order to align their feature spaces [79, 33, 68]. 
2. Adversarial-based: these methods build a domain classifier to distinguish whether the features come from the source domain or target domain. After being trained, the extractor could produce invariant features from both the source domain and target domain [16, 78, 11]. 
3. Reconstruction-based: methods also aim to find the invariant or shared features between domains. However, they realize this goal by constructing one auxiliary reconstruction task and employing the shared feature to recover the original input [12]. In this way, the shared feature should be invariant and independent of the domains. 
In the context of RL, domain adaptation is used during the training phase to bridge the perceptual-reality gap, which arises due to significant differences between the source (simulation) and target (real-world) domains. For instance, the adversarial-based method, builds a domain classifier to distinguish whether the features come from the source or target domain. After training, the extractor can produce invariant features from both domains, as detailed in [16]. 
23
2.4.5 Learning with Disturbances 
The methods of DR and dynamics randomization focus on adding changes to the simulated environment to make agents less affected by the differences between simulation and reality. This idea has been applied in other works, including the use of noisy rewards in [82], which can better simulate real-world agent training, also environmental perturbations were considered in [89] and [90], which affect agents differently during parallel learning. When training multiple real agents with a common policy, this is an important factor to consider. Although not directly related to sim-to-real transfer, these techniques can increase the robustness of the agents. 
2.5 Real-world training In the context of SRL for real robots, the question of whether to train in the real-world or simulations is a critical consideration. While real-world training provides the most accurate and comprehensive data for training RL algorithms, it also presents significant challenges in terms of safety and resource consumption. On the other hand, simulations offer a safe and controlled environment for training, but they may not fully capture the complexity and unpredictability of the real-world [43]. 
However, it is important to note that it is not always necessary to train in the real-world to achieve a good performance. With advanced simulation techniques and effective knowledge transfer methods, it is possible to train robust and effective RL algorithms in simulated environments. These algorithms can then be transferred to real-world robots, where they can perform effectively without the need for extensive real-world training. 
In this thesis, the SRL algorithms will initially be trained in a simulated environment that accurately models the real-world. The data collected during these simulations will be used to update the algorithms, to improve their performance and safety. The trained algorithms will then be transferred to the Turtlebot 2i for testing in the real-world. 
In addition to this, a pre-trained model will be used as a starting point for realworld training as in [67]. This approach aims to leverage the advantages of both simulation-based training and real-world training, providing the algorithms with a solid foundation of knowledge from the simulations, while also allowing them to adapt and fine-tune their performance in the real-world. By exploring these different training approaches, this research will provide a comprehensive comparison of their effectiveness and efficiency for real-world robotics applications. 
2.6 Simulation tools Simulations are computer programs that imitate the behavior and dynamics of realworld systems, including robots. These tools play a crucial role in the development, testing, and deployment of robots by providing a safe, cost-effective, and time-efficient 
24
alternative to real-world experiments. 
One of the main benefits of robotic simulations is that they enable designers and engineers to test the behavior of a robot in a virtual environment. This allows them to identify and resolve any issues that might arise during the development process before the robot is physically built. Additionally, simulations allow designers to perform experiments that would be difficult or impossible to conduct in the real-world, such as testing robots in extreme conditions or hazardous environments. 
Another advantage of simulation tools is that they allow designers to evaluate the performance of robots in a variety of scenarios. For instance, simulations can be used to test the ability of robots to navigate complex environments, perform tasks, and interact with other robots or objects. This information can be used to refine the design of the robot and improve its overall performance [22]. 
Some of the most popular simulators for robots include Gazebo, V-REP, Webots, Mujoco, and CARLA. These tools provide a range of features, including physics engines, motion planning algorithms, and robot control interfaces, to support the development and testing of robots. 
On the other hand, there are RL suites which are software packages to create simulated environments that provide a comprehensive set of tools for designing, implementing, and evaluating RL algorithms. These suites provide a user-friendly interface for designing, testing, and executing RL models, which makes them useful for both researchers and practitioners. Some popular RL suites include OpenAI Gym, RLLib, and TensorForce. These suites come with pre-built environments and tools to help researchers quickly test and evaluate their algorithms, saving time and effort in the development process. Additionally, they also provide visualization tools to help understand and analyze the results of the RL models [51]. 
Mujoco is particularly well-suited for robotics applications and was created specifically to test and develop RL algorithms. Additionally, OpenAI has developed Safety Gym, a suite of environments and tools specifically designed for safe reinforcement learning research. Safety Gym provides multiple environments that simulate different safety scenarios to experiment with various strategies for managing and mitigating risks, which aligns perfectly with the main focus of this work. This simulator also provides the flexibility to work with three distinct agents, depending on the requirements of the research. These agents, as depicted in Figure 3, each brings unique capabilities and characteristics. 
25
Figure 3: From left to right: Point, a simple 2D robot that can turn and move; Car, a wheeled robot with differential drive control; and Doggo, a quadrupedal robot with bilateral symmetry [51]. 
In addition, the simulator offers a variety of configurable features, as depicted in Figure 4. These features allow for the representation of diverse types of hazards or obstacles within the environment. 
Figure 4: From left to right: Hazards, dangerous areas; Vases, fragile objects; Buttons, sometimes should not be pressed; Pillars, large fixed obstacles; Gremlins, moving obstacles [51]. 
2.7 Turtlebot 2i The Turtlebot 2i, shown in Figure 5 is a mobile robot known for its robust features and adaptability, and will be the platform for conducting the real-world experiments in this thesis. The Turtlebot’s mobility and comprehensive sensor capabilities make it an ideal tool for creating a wide array of complex tasks and scenarios. These features will be leveraged to provide a rich learning environment for the SRL algorithm in investigation. Moreover, the real-world operation of the Turtlebot 2i will provide a more challenging and realistic environment than a simulated one, thereby offering a more rigorous test of the SRL algorithm’s effectiveness and robustness [73]. 
This robot developed by Interbotix Labs was designed with a modular structure, allowing for easy customization and expansion to suit various research needs [55]. The key physical components and features of the Turtlebot 2i are: 
 Mobile base: Features a Kobuki mobile base that provides the robot with mobility. The base is equipped with drive wheels and casters that allow the robot to move smoothly in different directions and turn on the spot. 
 Sensors: The Turtlebot 2i is equipped with a variety of sensors that enable it to perceive its environment. The most notable sensor is the 3D Depth Camera -Orbbec Astra Pro, which provides high-resolution depth and RGB data. The 
26
robot also includes a 9 DOF IMU for tracking the orientation of the robot. Finally, it also has Edge Detection and Bumper Sensors. 
 Manipulator Arm: The Turtlebot 2i comes with a 6 DOF (Degrees of Freedom) Pincher MK3 arm. This arm allows the robot to interact with its environment in a more sophisticated way, such as picking up and moving objects. 
 CPU: It is recommended to include a CPU for the robot for example the most used is an INTEL NUC, 8GB RAM memory, 120GB or better SSD, 802.11AC WiFi / Bluetooth 4.0, Ubuntu 16.04/ ROS Kinetic. 
 Features: The robot has a maximum translational velocity: of 70 cm/s, maximum rotational velocity: of 180 deg/s (>110 deg/s gyro performance will degrade), payload: of 2kg (without arm), 1kg (with arm), can drive off a cliff with a depth lower than 5cm, climbs thresholds of 12 mm or lower, expected operating time between 4-6 hours depending on the load and charging time 2-3 hours. 
Figure 5: Turtlebot 2i with camera sensors and manipulator arm [55]. 
The core sensor for the research conducted in this thesis is a 2D LIDAR which is a system that uses lasers to measure distances. This sensor will be externally mounted on the Turtlebot as it is not included in the standard Turtlebot package. Specifically, the model chosen for this task is the Sick TIM551 [2] shown in the Figure 6. 
27
Figure 6: Lidar Sick TIM551 with 270° FoV that can be used to detect obstacles around the robot [2]. 
The Sick TIM551 is a state-of-the-art laser scanner that is highly effective for mapping and navigation systems. With its precise scanning capabilities and robust design, it is particularly well-suited for applications in SRL. The TIM551’s ability to generate detailed and accurate environmental data will be instrumental in training and testing the RL algorithms under investigation in this thesis. 
The main features of the SICK lidar are: 
 Measurement principle: HDDM+ 
 Light source: Infrared (850 nm) 
 Aperture angle: 270 degrees 
 Scanning frequency: 15 Hz 
 Angular resolution: 1 degree 
 Working range: 0.05m ... 10m 
 Scanning range: 8m 
The Turtlebot 2i’s compatibility with the Robot Operating System (ROS) is one great advantage because it allows for easy programming and control of the robot. ROS provides a standardized interface for interacting with the Turtlebot’s hardware and sensors, which simplifies the process of writing software for the robot. This makes it easier to focus on the high-level tasks of designing and implementing RL algorithms, rather than getting bogged down in the details of hardware control [58]. 
In addition, SICK TIM551 LIDAR sensor is fully compatible with ROS which means that the sensor’s data can be easily integrated into the ROS ecosystem. This allows for the use of existing ROS tools and libraries for processing and visualizing the LIDAR data, which can greatly simplify the task of developing mapping and navigation systems. 
28
2.8 Robot Operating System (ROS) Robot Operating System or ROS, is a software platform for building and programming robots. The most fundamental concept of ROS is its modularity, which makes it highly usable for developers and researchers. ROS is designed to provide a common set of tools and libraries that can be used to build and operate robots, regardless of the hardware being used. It uses a message-passing system to allow different parts of the robot software to communicate and interact with each other and provides a set of standard interfaces for accessing the hardware, sensors, and actuators on the robot, its fundamental concepts are: 
 Nodes: In ROS, individual processes are referred to as nodes. Nodes can publish or subscribe to topics, provide or call services, and interact with each other through these communication mechanisms. 
 Master: The ROS Master provides naming and registration services to the rest of the nodes in the ROS system. It tracks publishers and subscribers to topics as well as services. The role of the Master is to enable individual ROS nodes to locate one another [56]. 
 Messages: Communication between two nodes works via messages, a strictly typed data structure. A message can either consist of primitive types (integers, booleans, floating points, etc.) or other nested messages. 
 Topics: In ROS, nodes can publish data to topics or subscribe to receive data from topics. The ROS Master will check if any other nodes are subscribed to the same topic, and if so, it will share the node details of the publisher to the subscriber node. The two nodes then interconnect using the TCPROS protocol, which is based on TCP/IP sockets [35]. 
 Services: In ROS, nodes can provide services, which other nodes can call. Services are similar to topics, but they use a request-response model, rather than a publish-subscribe model. Services are used for more complex interactions between nodes. 
It’s possible to run ROS across multiple machines, for example, a robot computer and a laptop. In this case, ROS_IP environment variable should be set to the IP address of each machine [57]. 
This modular design makes it easy for developers to create, test, and refine individual parts of a robot’s software, and then integrate them into a cohesive system. Additionally, ROS provides a large and active community of developers and users, making it easy to find help and resources, as well as to share your developments with others. Overall, the modularity and usability of ROS make it an essential tool for building and programming robots, and it is widely used in both academia and industry. 
29
Every operation performed by the Turtlebot in this study uses multiple ROS services and connections. These services are essentially the building blocks of a ROS system, providing a means to encapsulate the functionality of nodes into a callable service. This allows for a more structured interaction with the robot, enabling the execution of specific tasks upon request. 
Moreover, multiple different ROS topics are utilized to access the robot’s information and to control the robot. Topics serve as a pipe for data flow, allowing nodes to communicate by publishing messages to topics and subscribing to topics to receive published messages. In essence, the use of ROS services and topics forms the backbone of the Turtlebot’s operation in this thesis. They enable a seamless flow of information between the various components of the robot system, thereby facilitating the control and command of the robot in a structured and efficient manner. This contributes to the overall robustness and reliability of the robot’s operation in the real-world environment. 
30
3 Method 
This section presents the methodologies employed clearly. It starts by explaining the simulated environments chosen for the study. Then, it dives into the specifics of the algorithm that was implemented. The section also defines the MDP spaces and presents in detail the parameters used in DR. By the end of this section, readers will have a clear understanding of the tools and techniques that drove the research. 
3.1 Simulated Environment There are several different simulation platforms available as it was mentioned in Section 2.6, each with its strengths and weaknesses. For example, MuJoCo is well-known for the accuracy of its contact, friction simulations, and computational speed [75], but it lacks integration with other tools such as ROS or OpenCV commonly used by roboticists. Coppelia Sim [54] and Gazebo [15] are both popular simulation platforms within the robotics community, and they offer a range of features that make them well-suited for different types of applications. Another reason for Gazebo’s popularity is due to its community support, a vast library of robots and sensors, and integration with ROS. However, it is not as accurate as MuJoCo, and it can be slower for running simulations. 
Based on the requirements and the specific focus of this study, the decision was made to utilize the Mujoco simulator in conjunction with OpenAI Gym. The specific simulation environment that was used in this study is the Safety Gym suite, which is a collection of environments that have been specifically designed for SRL research. Safety Gym provides multiple environments that simulate different safety scenarios, which allows for the experimentation of various strategies for managing and mitigating risks. The following Table 1 summarizes the main features of the simulation platforms that were considered for this study: 
Table 1: Comparison table among simulators. 
The simulated robot used in this study was created by modifying the Car agent in Safety Gym. The Car agent is a wheeled robot with differential drive control, and it is the most similar to the Turtlebot 2i in the Safety Gym suite. The geometry of the Car agent was modified to be as close as possible to the Turtlebot 2i, as shown in Figure 7. The two inputs to the agent are the linear speed and the angular speed of the robot, which have the following range of values: 
31
𝑣𝑥 [𝑚/𝑠] → [0, 1] ∈ R 𝜔[𝑟𝑎𝑑/𝑠] → [−1, 1] ∈ R 
(13) 
The linear speed controls the forward movement of the robot in the x-axis with respect to the robot’s coordinate frame in meters per second, while the angular speed controls the rotation of the robot in radians per second. 
Figure 7: Simulated Turtlebot base in Safety Gym simulator. 
The Lidar sensor in SafetyGym is a simulated laser sensor that provides measurements of the environment to the agent. This simulated sensor returns the distance to objects, the position and orientation of objects, and the type of objects. As a result, it serves as a valuable tool for accurately representing a real sensor, making it ideal for developing RL agents that rely on this sensor. 
The Lidar sensor in the simulation has to be as similar as possible to the realworld Lidar. For that reason, in this simulation, the sensor will be only used to measure distances and with the following configuration: 
 Distance to object: returns a value of the distance from the sensor to an object up to 10 meters. 
 Angle range: the range of the Lidar sensor is set from −120◦ to 120◦, as shown in Figure 8. 
 Angle resolution: the resolution of the scan is set to 1 degree, which means that it can measure distance from objects every 1 degree. 
32
Figure 8: Visualization of simulated Lidar, displaying seven example scans across the complete 240-degree field of view. 
The information provided by the Lidar sensor is essential for the agent to make informed decisions about its actions. This information can be used to avoid collisions, navigate through cluttered environments, and plan its movements. The Lidar sensor in this thesis is essentially the robot’s perception, providing it with a view of the environment around it. 
The Safety Gym environment has multiple objects that can be used to represent different types of obstacles. In this thesis, three different environments were created to train different agents and represent a real environment. All of the environments will have the same goal: to reach a translucent green cylinder and return to the initial position of the robot without colliding with any obstacle. These three environments will be described in detail in Section 4. 
In these environments, different types of obstacles will be added, such as static obstacles, dynamic obstacles, and walls. This will allow us to train a robust agent that can handle a variety of obstacles. The different elements in the environments are shown in Figure 9. 
33
Figure 9: Simulation environment with static (blue) and dynamic (orange) obstacles where the robot should navigate towards the goal (green). 
 Goal: This represents the coordinates where the robot has to reach. Is it shown as a green cylinder. 
 Static obstacles: These obstacles do not move. They are shown in blue and have different shapes and sizes. 
 Dynamic obstacles: These obstacles move. They are shown as orange cylinders in the figure with different sizes. They move in a circular pattern. 
 Walls: These obstacles prevent the agent from moving outside of the environment. They are shown in gray in the figure. 
3.2 TRC implementation The Trust Region Conditional Value at Risk (TRC) algorithm [28] as mentioned in Section 2.3.4 is a safe reinforcement learning algorithm that can be used to train policies that satisfy safety constraints. The algorithm works by maintaining a trust region around the current policy, and only exploring states and actions within the trust region. This ensures that the policy is unlikely to violate safety constraints during training. 
In this study, the TRC algorithm was implemented to train a policy for a simulated turtlebot. The ultimate objective is to enable the turtlebot to successfully navigate through a cluttered environment, reaching its designated goal without colliding with any obstacles. To achieve this, the following components were implemented: 
1. Reward Function: The reward function is structured to incentivize the turtlebot to progress toward its goal while circumventing any obstacles. The function 
34
assigns positive rewards for actions that decrease the distance between the turtlebot and its goal. This is mathematically represented as: 
𝑅(𝑠, 𝑎, 𝑠′) = 𝑑𝑔 (𝑠) − 𝑑𝑔 (𝑠′) 
In this equation, 𝑑𝑔 (𝑠) denotes the distance from the robot to the goal in state 𝑠. If the robot successfully reaches the goal, i.e., when 𝑑𝑔 (𝑠) < 𝛿 (where 𝛿 is a predefined goal distance threshold signifying goal achievement), the reward assigned is: 
𝑅(𝑠, 𝑎, 𝑠′) = 1 
2. Cost Function: In addition to the reward function, the cost function is also defined to quantify the undesired outcomes, such as colliding with obstacles. The cost function is similar to a penalty in a reward function, but it specifically focuses on the negative consequences of the robot’s actions. 
In the context of the TRC algorithm, the cost function is used to calculate the CVaR of the advantage function, which represents the expected cost in the worst-case scenarios. The CVaR is then used as a constraint in the policy update to discourage the policy from taking actions that could lead to high costs. This cost function is defined as: 
𝐶 (𝑠, 𝑎, 𝑠′) = 𝑆𝑖𝑔𝑚𝑜𝑖𝑑 [𝑤𝑐 (𝑑𝑙 − 𝑑ℎ (𝑠))] 
Where 𝑤𝑐 is the weight cost, 𝑑𝑙 is the distance limit to the obstacles and 𝑑ℎ is the minimum distance between the robot and the obstacle. By incorporating the cost function into the TRC algorithm, the policy training not only maximizes the rewards but also minimizes the costs, leading to a more balanced and safer behavior of the robot. 
3. Constraint Violations: Safety constraints are defined to prevent the turtlebot from colliding with obstacles. A constraint violation occurs when the turtlebot hits an obstacle or gets closer than a distance threshold. The severity of the violation is quantified by the nature of the violation, for instance, a crash is more serious than getting near an obstacle. The TRC algorithm incorporates these constraints into the policy update by adding a constraint on the CVaR of the advantage function, which discourages the policy from taking actions that could lead to a constraint violation. In this implementation, a violation is registered every time the robot comes within a distance of 0.35 meters from an obstacle. Moreover, if the robot collides with an obstacle, a more substantial violation count is assigned. This count is proportional to the remaining time steps in the episode, ensuring that early crashes are penalized more heavily. Specifically, the CV is determined using the equation below: 
𝐶𝑉 = Max time steps − Current time step (14) 
35
4. Hyperparameters: The TRC algorithm is characterized by several key hyperparameters that significantly influence its performance. Some of these hyperparameters are common to standard RL algorithms, while others are specifically designed to balance risk and performance in the context of the TRC algorithm, the primary parameters that most influence this algorithm are: 
 Discount Factor (𝛾): This determines the importance of future rewards in the cumulative reward calculation. A high 𝛾 encourages long-term strategy. 
 Generalized Advantage Estimation (GAE) [65] Parameter (𝜆): This controls the trade-off between bias and variance in the advantage estimation. A high 𝜆 reduces bias but increases variance. 
 Learning Rate (𝜂): This is the step size in the gradient descent optimization. A high 𝜂 can speed up the learning but might also cause instability. 
 Batch Size: This is the number of experiences collected before each policy update. A large batch size can improve the stability of the learning but also increase the computational cost. 
 Number of Iterations: This is the number of policy updates. The learning can continue until a stopping criterion is met, such as a maximum number of iterations or a minimum improvement in the performance. 
 Number of steps: This number determines the number of steps to be collected from the environment before each update or training iteration of the algorithm. This can influence the balance between exploration and exploitation during the learning process. 
 CVaR Level (𝛼): This determines the level of risk aversion in the policy. A low 𝛼 makes the policy more risk-averse. 
 Trust Region Size (𝛿): This is the maximum allowed change in the policy at each training update. A small 𝛿 can ensure safety but might slow down the learning. 
These hyperparameters were carefully tuned to align with the specific requirements and constraints of the task, more details of the values will be seen in Section 4. 
3.3 State Space The state space in this thesis is a multi-dimensional representation capturing useful information about the robot’s environment and its dynamics. Specifically, the state space is composed of the following dimensions: 
 Goal Vector Direction (2 dimensions): This captures the direction vector pointing towards the goal. It provides the robot with a sense of direction in which it needs to move to reach its destination. 
36
 Goal Distance (1 dimension): Represents the Euclidean distance from the robot’s current position to the goal. It indicates how far the robot is from its target. 
 Robot’s Speed (2 dimensions): Represents the linear and angular speed of the robot in [𝑚/𝑠] and [𝑟𝑎𝑑/𝑠] respectively. This provides information about the robot’s current movement dynamics. 
 Linear Acceleration (1 dimension): Captures the robot’s linear acceleration in [𝑚/𝑠2], indicating any changes in its speed. 
 LidarScan (48 dimensions): Represents the distances to obstacles as detected by the lidar sensor. The lidar operates with a resolution of 1 degree, scanning every degree within its range. In the state space, each dimension captures the minimum distance value over an array of 5 degrees, effectively aggregating the shortest distance from 5 individual 1-degree scans. This provides a comprehensive view of the robot’s surroundings, scanning from -120 to 120 degrees, aiding in navigation and obstacle avoidance. 
In total, the state space includes 54 dimensions, offering a comprehensive view of both the robot’s internal dynamics and its external environment. By providing the model with such detailed information, it is better equipped to make informed and optimal decisions in diverse scenarios. 
3.4 Action Space The action space in this thesis defines the set of possible actions the robot can take at any given state. Specifically, the action space consists of 2 dimensions that are: 
 Linear Speed ([0, 1] m/s): Represents the forward movement speed of the robot. The robot is restricted to move only forward, within a speed range of 0 to 1 m/s, to ensure it does not venture into areas not covered by the lidar’s field of view. This limitation enhances safety by preventing the robot from moving into unseen obstacles. 
 Angular Speed ([-1, 1] rad/s): Denotes the rotational speed of the robot around its axis. The robot can turn either left or right within a range of -1 to 1 radians per second, enabling it to navigate through turns, avoid obstacles, and orient itself towards the goal. 
Together, these two dimensions of the action space provide the robot with the necessary mobility and agility to navigate complex environments and achieve its objectives, while also ensuring safe operation. 
37
3.5 Domain Randomization Domain randomization was selected for this thesis due to its simplicity, intuitiveness, and effectiveness in bridging the sim-to-real gap. It exposes the agent to diverse training conditions, preventing overfitting to the simulation and enhancing real-world adaptability. Unlike more labor-intensive methods, DR is easy to implement and has become one of the most popular techniques for sim-to-real transfer, especially in scenarios with unpredictable environments. 
As discussed in Section 2.4.3, the primary objective of DR is to expose the agent to a wide range of environmental conditions during training, thereby ensuring that the learned policy is robust and adaptable. In the context of the TRC algorithm and the Safety Gym environment, DR is applied by varying several parameters of the simulation. In this thesis, the parameters are: 
1. Robot’s initial position: To prevent the robot from memorizing its starting point, it is initialized at a random location within the environment for each episode. 
2. Robot’s orientation: Randomizing the robot’s initial orientation enhances its adaptability and ensures it does not overfit to a specific direction. 
3. Obstacles position: Obstacles are placed randomly in each episode, offering a dynamic environment and simulating a variety of challenges. 
4. Obstacles shape and size: By varying both the shape and size of obstacles, the environment ensures a diverse set of challenges, preparing the robot for different real-world scenarios. 
5. Robot’s speed: Introducing a Gaussian noise to the control signals of the wheels’ speed ensures the robot learns to operate effectively across a range of velocities. 
6. Robot’s localization: The robot’s perceived position is adjusted with Gaussian noise, simulating the uncertainties of real-world localization. 
7. Lidar’s reading: To replicate real-world sensor inaccuracies, Gaussian noise is added to the lidar readings. 
The Gaussian noise for parameters 5, 6, and 7 is modeled as a normal distribution, represented as N(𝜇, 𝜎2), where 𝜇 is the mean and 𝜎2 is the variance. Given the reality gap, certain parameters may exhibit different degrees of accuracy. For instance, while the SICK TIM lidar sensor boasts a high accuracy of ±60[𝑚𝑚], there is a more pronounced discrepancy between the simulated and real-world robot’s speed. Consequently, the variance for the lidar’s reading noise is set lower than that for the robot’s speed and localization mainly because of the environment’s surface or wheel’s friction. Specifically, these variances are defined as: 
38
Robot’s speed → N(0, 0.15) (15) 
Robot’s localization → N(0, 0.15) (16) 
Lidar’s reading → N(0, 0.05) (17) 
This implies that for parameters 5, 6, and 7, a random value of ±15%, ±15%, and ±5%, respectively of the signal value will be added. Incorporating DR into various parameters, especially the robot’s speed, localization, and lidar readings, equips the agent with the ability to handle uncertainties inherent in real-world scenarios. This intentional perturbation ensures that the model remains robust, preparing the robot to navigate reducing the reality gap, and tackling unforeseen challenges or anomalies that might arise in actual environments. 
3.6 Fine-tuning Fine-tuning is a training method where a pre-trained model, which has already learned certain features from a large dataset (in this case the simulated environment), is further trained (typically on a smaller dataset) to refine or adapt to a specific task. In this thesis, fine-tuning is used to train the final layer of the neural networks to adapt the model pre-trained in a simulated environment to the specific dynamics and variations of our real-world robot environment. As it was mentioned in Section 2.5, this approach is particularly beneficial as training a model from scratch in the real-world requires significant time and computational resources. By leveraging the knowledge already captured in the simulation-trained model and focusing on fine-tuning the last layer, we can achieve better adaptability to the unique challenges presented by the real-world deployment of our robot. 
For consistency and effective transfer learning, the data dimensions from the real-world training must align with those from the pre-trained model obtained in the simulation. To ensure this uniformity across both domains, various state parameters were adjusted. Specifically, the lidar’s angle range was configured to -120 to 120 degrees, and offsets were set for the lidar sensor’s distance measurements on the robot. This ensures that the data representations from both the simulated and real-world environments are congruent, facilitating a smoother fine-tuning process. 
In this thesis, the fine-tuning process begins with a model that has been comprehensively trained in the simulated environment, as detailed in Section 3.1. Once this model is transferred to the real Turtlebot, all neural network weights are frozen, except the final layer, which is subjected to fine-tuning, this can be visually represented in Figure 10. 
39
Figure 10: Neural network in fine-tuning process. 
The subsequent real-world training is conducted over a specific number of episodes, as described in Section 4. This number is notably smaller than the episodes in the simulated environment due to the logistical complexities inherent to real-world training. For instance, each episode needs to reposition the robot and rearrange obstacles to create a fresh environment. To compensate for the reduced number of episodes, the learning rate is elevated, enabling more substantial gradient updates. This ensures that, even with limited episodes, the final layers of the network effectively adapt, capturing the distinct characteristics of the real-world domain. 
40
4 Experiments 
4.1 Hardware and Software Specifications In the experiments conducted for this study, two different hardware setups were employed. The first is a dedicated notebook, optimized for high computational tasks, which was used for training the model in a simulated environment using GPU. The second hardware setup corresponds to the onboard computer of the robot (NUC), responsible for real-time processing and decision-making during real-world deployments. Both setups, with their respective software configurations, are crucial to the research as they provide the computational backbone for the simulation, training, and deployment phases. The following sections detail the specifications of each hardware setup and the software environments. 
4.1.1 Notebook Hardware 
 Processor: Intel Core i7-10750H 6-Core Processor (up to 5.0 GHz) 
 Memory: 16GB DDR4 2933MHz RAM 
 Storage: 512GB PCIe NVMe SSD 
 Graphics: NVIDIA GeForce RTX 3080 Ti 
 Display: 15.6" Full HD 144Hz, 100% sRGB color range 
 Operating System: Ubuntu 20.04 LTS 
4.1.2 Robot NUC Hardware 
 Robot Platform: Turtlebot 2i 
 NUC Model: Intel NUC 11 Pro Kit - NUC11TNHi7 
 Processor: Intel Core i7-1185G7 Processor 12M Cache 
 Graphics: Integrated Intel Iris Xe Graphics 
 Memory: Supports up to 64GB DDR4 3200 MHz SO-DIMM 
 Connectivity: Intel Wi-Fi 6 AX201 + Bluetooth 5.2 
 Ports: 2x Thunderbolt 4, 4x USB 3.1 Gen2, HDMI 2.0b, Gigabit Ethernet 
 Lidar Sensor: SICK TIM561 
 Operating System: Ubuntu 20.04 LTS 
41
4.1.3 Software 
 Operating System: Ubuntu 20.04 LTS 
 Robot Operating System (ROS): Noetic 
 Simulation Platform: Safety Gym via Mujoco 
 Simulation library: Mujoco-py 2.0.2.7 
 Deep Learning Framework: Pytorch 1.10 
 Reinforcement Learning Framework: Stable Baselines 3 
 Programming Language: Python 3.8 
4.2 Simulation Setup In our experiments, two distinct simulation environments were set up to evaluate and compare the performance and robustness of the trained model under varying conditions. 
4.2.1 Simple Environment 
The first environment shown in Figure 11, referred to as the "Simple Environment", is characterized by its static nature. In this setup: 
 The robot always starts from a predefined initial position and orientation at the beginning of each episode. 
 The environment contains only static obstacles, all of which are of the same shape. 
 The primary objective for the robot is to navigate to a goal represented by a green cylinder and return to its starting position without colliding with any obstacles. 
 The goal’s location is not fixed but can be one of three possible positions, represented by green crosses or a green cylinder in Figure 11. 
42
Figure 11: Simple Environment Simulation with static obstacles (red, orange, and cyan) and with crosses the possible goal positions. 
4.2.2 Randomized Environment 
The second environment visible in Figure 12 implements DR, to introduce variability and complexity. Features of this environment include: 
 The robot’s starting position and orientation are randomized at the beginning of each episode. 
 Obstacles of various shapes, as defined in Section 3.1, are placed randomly within the environment. A constraint ensures that these obstacles maintain a minimum distance of 1 meter from each other and the robot’s starting position. 
 Moving obstacles, represented by orange cylinders, simulate moving people in a real-world scenario. These obstacles move in circular patterns. 
 The robot’s task remains consistent: navigate to a goal, represented by a green cylinder, and return to its starting position without colliding with any obstacles. 
43
Figure 12: Randomized Environment Simulation, with multiple boxes as static obstacles and orange cylinders as moving obstacles. 
In both simulation environments, each episode is constrained to a maximum of 15000 time steps. If this limit is reached, the episode concludes automatically. Each time step in the simulation corresponds to 0.002 seconds, indicating that the robot executes an action at this interval. It is also worth noting that any collision by the robot with an obstacle or wall results in the immediate termination of the episode, emphasizing the importance of safe navigation. 
To ensure the robustness and adaptability of the models, specific hyperparameters were chosen during the simulation training phase. The chosen values were based on a combination of empirical testing and literature recommendations from [28, 64] to achieve optimal results in the given environments. 
Table 2 presents a comprehensive list of the hyperparameters used for each model during the simulation training: 
44
Hyperparameter Value Learning Rate (𝜂) 0.0002 Discount Factor (𝛾) 0.99 GAE Parameter (𝜆) 0.97 Epochs 64 Number of Episodes 35000 Number of Steps for training 3000 CVaR Level (𝛼) 0.125 Trust Region Size (𝛿) 0.025 Max KL divergence 0.001 Policy Network hidden layers 2 Policy Network neurons 512 Policy Network activation function ReLU Policy Network output activation function Tanh Value function Network hidden layers 2 Value function Network neurons 512 Value function Network activation function ReLU Value function Network output activation function ReLU 
Table 2: Hyperparameters used for simulation training 
Both environments are designed to test the adaptability and performance of the model under different conditions, from a more controlled setting in the Simple Environment to a dynamic and unpredictable setting in the Randomized Environment. This design approach is specifically intended to provide a thorough evaluation of how effectively DR bridges the ’sim to real’ gap. This assessment becomes particularly crucial when the model is subsequently deployed in a real-world environment. 
4.3 Real-world Setup For the real-world setup, a spacious area within Ericsson’s offices was used to simulate a challenging environment for the robot. Large obstacles and numerous chairs were strategically placed to emulate intricate navigation scenarios. During the real-world training phase, the positions of all obstacles were manually altered for each episode, with one such configuration depicted in Figure 13. Both the starting position and the goal for the robot were marked on the floor using distinct signs. This real-world setup mirrors the conditions of the simulation in several key aspects: 
 The robot’s starting position is randomized at the beginning of each episode. 
 Obstacles are placed randomly within the environment. As before ensure at least maintain a minimum distance of 1 meter from each other and the robot’s starting position. 
 Moving obstacles are simulated by an individual walking at a regular pace in a straight trajectory. 
45
 The robot’s task remains the same: navigate to a goal and return to its starting position without colliding with any obstacles. 
Figure 13: Example Real Environment with chairs as obstacles. 
To evaluate the efficacy of DR in real-world scenarios, three distinct environments of escalating complexity were established. For a comprehensive perspective, alongside images of the real environments, their simulated perspective is presented on the right. The environments are as follows: 
1. The first test environment is relatively simple, featuring only two static obstacles. This setup can be observed in Figure 14. 
46
Figure 14: Testing Real Environment 1, with two simple obstacles. 
2. The second test environment is more intricate, comprising multiple static obstacles of varying shapes, spaced generously apart. This configuration is depicted in Figure 15. 
Figure 15: Testing Real Environment 2, with multiple static obstacles. 
3. The third and most challenging test environment consists of numerous static obstacles of different shapes, positioned closely to one another. Additionally, it includes two dynamic obstacles, represented by individuals. One person moves in a straight line as the robot approaches the goal, while the other does so as the 
47
robot returns to its starting point. Their respective trajectories are indicated by red arrows in the simulated representation, as shown in Figure 16. 
Figure 16: Testing Real Environment 3, with multiple static obstacles and people as moving obstacles. 
Finally, a particularly challenging environment configuration was selected to rigorously evaluate the robot’s performance in both pre and post real-world training. This test setup is illustrated in Figure 17. It is crucial to note that this specific configuration was intentionally excluded from the training sessions to ensure unbiased testing conditions. In the next section, the results of these different environments will be presented. 
Figure 17: Real-world training testing environment, with chairs and flower pots as obstacles. 
48
The hyperparameters for the real-world setup differ slightly from those used in the simulation training. The specific values are in the Table 3 below: 
Hyperparameter Value Learning Rate (𝜂) 0.01 Discount Factor (𝛾) 0.99 GAE Parameter (𝜆) 0.97 Epochs 64 Number of Episodes 150 Number of Steps for training 1000 CVaR Level (𝛼) 0.125 Trust Region Size (𝛿) 0.025 Max KL divergence 0.001 Policy Network hidden layers 2 Policy Network neurons 512 Policy Network activation function ReLU Policy Network output activation function Tanh Value function Network hidden layers 2 Value function Network neurons 512 Value function Network activation function ReLU Value function Network output activation function ReLU 
Table 3: Hyperparameters used for real-world training 
49
5 Results 
In this section, the results of the experiments will be detailed, highlighting the performance of various models under different training conditions. These results provide insight into the effectiveness of the methodologies employed, particularly the impact of domain randomization on bridging the sim-to-real gap. By comparing the performance of models trained under varying conditions, this study aims to identify the most promising strategies for SRL in real-world robotic applications. 
5.1 Simulation results The simulation phase of the experiments involved training three distinct models, each subjected to different environmental conditions and levels of DR. The performance of each model was gauged based on the rewards and constraint violations obtained during training, which serve as a proxy for the model’s ability to navigate safely and efficiently. 
 Simple Environment Model: This model was trained in a straightforward environment devoid of any randomization, as detailed in Section 4.2.1. The primary objective was to establish a baseline model to compare performances. 
 Basic Domain Randomization Model: Building on the previous model, this variant incorporated basic DR techniques. Specifically, the robot’s initial position and orientation were randomized at the start of each episode, in addition to the main features of this environment detailed in Section 4.2.2 which introduces an element of unpredictability to the training process. 
 Domain Randomization Model: This is the most advanced of the three models. In addition to the randomizations introduced in the Basic DR Model, this model also incorporated randomizations in three key parameters: the robot’s speed, its localization, and the lidar readings. These additional randomizations, as defined in Section 3.5, aimed to further challenge the model and enhance its adaptability to diverse real-world scenarios. 
In the subsequent plots, the reward trajectories of each model are presented, providing a comprehensive view of their learning progressions and highlighting the advantages and limitations of each approach. The reward function utilized for this purpose has been elaborated on in Section 3.2. The graphical representation of these rewards can be observed in Figure 18. 
50
Figure 18: Reward obtained in simulated environments, using the average of three random seeds 
From the Figure 18, it can be seen that the Simple Env Model consistently achieved higher rewards, reaching its peak earlier than the randomized models in only 10 thousand episodes. This is three times faster than the other two models, which took 35 thousand episodes to reach their maximum rewards. The reward curves of all three models eventually converged to values greater than 10, indicating that the robot successfully navigated the environment, reached the goal and returned to its starting point. This outcome aligns with expectations, given the relatively straightforward nature of its environment. On the other hand, the DR Env Model, represented by the red curve, exhibited a prolonged initial training phase, attributable to the extensive random components present in its environment. 
Subsequently, the constraint violations observed for each model are presented, as illustrated in Figure 19. The specific criteria for what constitutes a ’Constraint Violation’ is detailed in Section 3.2. 
51
Figure 19: Constraint Violations obtained in simulated environments, using the average of three random seeds. 
The graph in Figure 19 has been smoothed to enhance clarity. From the plot, it can be seen that the Simple Env Model exhibited exemplary performance, registering no constraint violations (0 CVs). This indicates that the model consistently navigated to the goal and returned without ever approaching closer than 0.35 meters to any obstacle. In contrast, the other two models, due to their training in the more intricate randomized environments, displayed a higher number of constraint violations, averaging around 16 CVs by the end of their training sessions. 
For a more quantitative evaluation, standard error values for the reward and constraint violations of each model are presented in the Tables 4 and 5 below. These values indicate the variability and stability of the models’ performances during their training. 
Table 4: Standard Error of Reward Obtained 
Model Standard Error Simple Env Model 0.079 
Basic DR Env Model 0.083 DR Env Model 0.096 
This error was calculated using the following formula being 𝜎 the standard deviation: 
𝑆𝐸 = 𝜎 √ 𝑛 
52
Table 5: Standard Error of Constraint Violations 
Model Standard Error Simple Env Model 0.122 
Basic DR Env Model 0.267 DR Env Model 0.259 
Referring to Tables 4 and 5, it becomes evident that the Simple Env Model exhibits the smallest standard error. This observation aligns with expectations, given that this model was trained in an environment devoid of any randomization, but the goal position over 3 option. Moreover, when considering the CV table 5, by excluding the initial 4000 episodes from the error calculation, the standard error (SE) reduces significantly to 0.005. 
To conclude the training, it is beneficial to visually evaluate the robot’s behavior within its environment. This is because the rewards obtained do not always correlate directly with the CVs. For instance, a robot that does not move might register a minimal reward of 0, yet exhibit no CVs. Thus, a comprehensive evaluation that goes beyond mere numerical metrics is essential for a comprehensive understanding of the robot’s performance in SRL. 
Test runs were conducted in the Randomized Environment to observe the DR model’s policy in action. The robot successfully achieved its primary objective, maintaining a reasonably safe distance from static and dynamic obstacles as it navigated to the target and returned. This trajectory can be observed in Figure 20, where the black arrow indicates the initial path and the red arrow denotes the return route. 
53
Figure 20: Testing DR Model, with a black arrow indicating the initial path and a red arrow as the return path. 
5.2 Real-world testing results In this subsection, the study examines the real-world performance of the models previously introduced and trained. After being refined within the simulation, these models were deployed onto the actual Turtlebot to navigate the challenges of the real-world. The testing was conducted in the three distinct environments described in Section 4.3. Each environment, with its unique complexities, acted as a benchmark, assessing the models’ adaptability and effectiveness when transitioning from a simulated to a real-world context. 
The subsequent results are derived from tests conducted in the three real-world environments defined in Section 4.3. For each environment, four distinct runs were executed, with obstacle positions varied as randomly as possible to ensure a comprehensive assessment. The performance of the models was measured using the following metrics: 
 Reward: This metric evaluates whether the robot successfully reached its goal and returned to its starting position, as detailed in Section 5.1. 
 CVs (Constraint Violations): Constraint violations increase whenever the robot comes within 0.35 meters of an obstacle or makes direct contact with one. This metric is further elaborated upon in Section 5.1. 
 Lidar Min Scan: To monitor the robot’s proximity to obstacles during each time step of an episode, the average of the minimum distances from any obstacle is 
54
calculated. This provides insights into how safely the robot navigates around obstacles. 
 Total distance: This straightforward metric measures the cumulative distance, in meters, that the robot traverses within the environment. The results for the first metric are shown in Figure 21. On the x-axis, the three different tests are represented, corresponding to Figure 14, 15, and 16. The y-axis displays the average value obtained over the four runs. 
Test 1 Test 2 Test 3 
0 
1 
2 
3 
4 
5 
M ea 
n Re 
wa rd 
5.2 5.2 
0.8 
5.2 5.2 
3.5 
5.2 5.2 5.2 
Average Reward from Four Runs 
Simple Env Basic DR Env DR Env 
Figure 21: Average Reward obtained over four runs of the three models for each real-world test. 
From Figure 21, it can be seen that in the first two tests, all three models achieved high reward values, indicating successful task completion. However, in the most challenging test, only the DR model managed to reach the goal, while the Simple model without DR exhibited the worst performance over the three models. 
55
Test 1 Test 2 Test 3 
0 
50 
100 
150 
200 
250 
300 
350 
400 
M 
ea n 
CV s 
0.3 13.0 
397.8 
5.5 4.3 
245.5 
0.5 1.5 
43.3 
Average CVs from Four Runs 
Simple Env Basic DR Env DR Env 
Figure 22: Average CVs obtained over four runs of the three models for each real-world test. 
Analyzing now the CVs results in Figure 22, it is clear that in the first test, all models performed without significant violations. However, by the second test, the Simple Model began to exhibit challenges. In the third test, the Simple model incurred numerous violations, while the DR model had only a few. 
Test 1 Test 2 Test 3 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
1.2 
1.4 
M ea 
n Lid 
ar  m 
in  S 
ca n 
1.38 
1.05 
0.78 
1.28 
1.07 
0.8 
1.23 
1.09 
0.92 
Average Lidar min Scan from Four Runs 
Simple Env Basic DR Env DR Env 
Figure 23: Average Lidar minimum scan distance obtained over four runs of the three models for each real-world test. 
From Figure 23, it can be seen that the minimum distances to obstacles were quite consistent across the models. However, in the third test, the DR model stands out with the greatest distance, indicating that it maintained a "safer" distance from obstacles compared to the other models. 
56
Test 1 Test 2 Test 3 
0 
5 
10 
15 
20 
25 
M ea 
n Di 
st an 
ce 
16.37 
18.4 
0.0 
14.13 
18.45 
23.78 
14.09 
18.55 
23.88 
Average Distance from Four Runs 
Simple Env Basic DR Env DR Env 
Figure 24: Average traveled distance obtained over four runs of the three models for each real-world test. 
In Figure 24, which illustrates the total distance traveled by the Turtlebot, during test 1 it is evident that the simple model opted for longer trajectories compared to the other models. Notably, in test 3, the simple model’s data is not even presented, as it failed to complete any episode. 
The subsequent tables provide detailed data from each run in the three tests. The results of Test 1 are presented in Table 6, the results of Test 2 in Table 7, and the results of Test 3 in Table 8. A white cell indicates a successful completion of the run, while a red cell means that the robot either crashed or got stuck. 
Table 6: Testing Environment 1 detailed results. 
In this first test, all three models successfully solved the environment achieving the maximum reward. As observed from the rewards in Table 6, they did so without any major issues. 
57
Table 7: Testing Environment 2 detailed results. 
In the second test, which was slightly more challenging, the Simple Env model registered more CVs compared to the others. However, the three models successfully solved the environment, obtaining the maximum reward indicated in Table 7. 
Table 8: Testing Environment 3 detailed results (red cells are runs that the robot crashed or got stuck). 
In Tests 1 and 2, all three models demonstrated notable performance. However, a closer examination of Test 3, as presented in Table 8, reveals a clear distinction among the models. The Simple model failed to complete any of the four episodes. The Basic DR model did better, successfully completing two out of the four episodes. In contrast, the DR model stood out, completing all four runs without any collisions or instances of getting stuck, and maintaining a reasonable count of violations throughout each run. 
Concluding the evaluations, the DR model, having demonstrated superior performance across all testing environments, was chosen as the pre-trained model for real-world training. This training primarily involved fine-tuning, as elaborated in Section 3.6. The specific environment configuration employed is detailed in Figure 17. 
The testing environment for the real-world was deliberately selected based on its observed challenges for the DR model. Among the various combinations of environments tested, this particular setup posed some difficulties for the DR model, making it an ideal candidate to assess improvements before and after real-world training. After conducting 150 training episodes, none of which included the testing environment, the results were compiled and presented in Table 9. 
Table 9: Testing Real Environment from Figure 17. 
The results clearly indicate a significant improvement after performing real-world training, even with just 150 episodes. While the DR model successfully completed 
58
only 2 out of 4 runs, the model trained in the real-world accomplished all 4 runs. However, both of them did register a considerable number of violations, suggesting that there were instances during the episode where the robot neared potentially hazardous situations. 
59
6 Conclusions 
In this section, the key findings of the research are synthesized and discussed, focusing on the training and deployment of SRL models in robotic environments. Performance metrics, especially in challenging environments, are highlighted to underscore the efficacy of the proposed approach. Additionally, the importance of real-world finetuning post extensive simulation training is discussed. Finally, possible improvements and recommendations for future research are proposed. 
6.1 Summary The primary objectives of this master’s thesis are to train an SRL model capable of navigating a robotic environment while maintaining safe actions and to bridge the simulation-to-reality gap in deploying RL agents in real robotic environments. A series of experiments were conducted in both simulated and real-world environments. These experiments provided valuable insights into the effectiveness of various training strategies and their implications for real-world deployment. Despite the challenges posed by the complexity of the environments and the logistical complexities inherent to real-world training, the study successfully demonstrated the potential of the proposed approach (defined in Section 3.2) in addressing these challenges and contributing to the field of SRL for real robots. 
In the simulation phase, three distinct models were trained, each subjected to different environmental conditions and levels of DR. The results showed clearly in Figure 18 that the model without DR (Simple env model) is superior in solving the environment in only 8000 episodes while the other 2 models had to train for 30000 episodes, which was expected due to the complexity of the environments. 
However, real-world testing further validated the theory of DR. When deployed on a Turtlebot, the DR Model consistently outperformed its counterparts. This was particularly visible in the most challenging environment, as shown in Table 8. Here, the Simple env model did not solve the environment in any of the four runs, while the DR model succeeded in all four. This highlights the importance of incorporating DR techniques in training to achieve better generalization in real-world scenarios. Additionally, the results showed that the DR model’s policy consistently opted for safer actions, maintaining 15% and 17% more distance from obstacles compared to the other models in the most challenging environment. 
Furthermore, the study emphasized the significance of fine-tuning in the real-world, even after extensive simulation training. The real-world training phase illustrated that even a modest number of episodes in the actual environment could lead to significant improvements in the model’s performance. Specifically, the model was able to successfully complete all four runs in a selected environment where the DR model initially encountered difficulties, managing to solve only 50% of the runs visible in Table 9. This emphasizes the necessity of real-world fine-tuning to optimize the 
60
model’s performance and adaptability, highlighting that simulation training, while valuable, may not fully capture the complexities of real-world environments. 
In conclusion, this thesis reaffirms the potential of DR as a viable strategy to address the sim-to-real gap in RL for robotics. By leveraging both simulation and real-world training, it is possible to develop models that are not only efficient in navigating diverse environments but also safe and reliable in real-world scenarios. 
6.2 Future work While this study has provided valuable insights, there is still room for further exploration. Future research could focus on developing a method for selecting parameters to perturb during DR, as the parameters in this study were chosen based on intuition. Ad-ditionally, creating a more advanced technique for constructing training environments during real-world training could eliminate the need for biased human intervention. It would also be interesting to compare a model trained from scratch in the real-world with the fine-tuned model developed in this study. Lastly, a comparison of the results obtained with methods using local or global planners could provide valuable insights into the effectiveness of different approaches. 
61
References 
[1] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. Constrained policy 
optimization. In Proceedings of International Conference on Machine Learning (ICML), volume 70, pages 22–31, 2017. 
[2] SICK AG. 2d lidar sensors: Tim551-2050001. https://www.sick.com/br/ en/lidar-sensors/2d-lidar-sensors/tim/tim551-2050001/p/p34 3045, 2023. Accessed: 2023-07-12. 
[3] Alekh Agarwal, Sham M Kakade, Jason D Lee, and Gaurav Mahajan. On the theory of policy gradient methods: Optimality, approximation, and distribution shift. Journal of Machine Learning Research, 22(98):1–76, 2021. 
[4] Eitan Altman. Constrained Markov decision processes. CRC Press, 1999. 
[5] Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. arXiv preprint arXiv:1606.06565, 2016. 
[6] Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, et al. Learning dexterous in-hand manipulation. The International Journal of Robotics Research, 39(1):3–20, 2020. 
[7] Frederick J Beutler and Keith W Ross. Optimal policies for controlled markov chains with a constraint. Journal of mathematical analysis and applications, 112(1):236–252, 1985. 
[8] Frederick J Beutler and Keith W Ross. Time-average optimal constrained semimarkov decision processes. Advances in Applied Probability, 18(2):341–359, 1986. 
[9] Kenneth Bogert and Prashant Doshi. Multi-robot inverse reinforcement learning under occlusion with estimation of state transitions. Artificial Intelligence, 263:46–73, 2018. 
[10] Konstantinos Bousmalis, Alex Irpan, Paul Wohlhart, Yunfei Bai, Matthew Kelcey, Mrinal Kalakrishnan, Laura Downs, Julian Ibarz, Peter Pastor, Kurt Konolige, et al. Using simulation and domain adaptation to improve efficiency of deep robotic grasping. In ICRA, 2018. 
[11] Konstantinos Bousmalis, Nathan Silberman, David Dohan, Dumitru Erhan, and Dilip Krishnan. Unsupervised pixel-level domain adaptation with generative adversarial networks. In CVPR, 2017. 
[12] Konstantinos Bousmalis, George Trigeorgis, Nathan Silberman, Dilip Krishnan, and Dumitru Erhan. Domain separation networks. In Advances in neural information processing systems, 2016. 
62
[13] Lukas Brunke, Melissa Greeff, Adam W Hall, Zhaocong Yuan, Siqi Zhou, Jacopo Panerati, and Angela P Schoellig. Safe learning in robotics: From learning-based control to safe reinforcement learning. Annual Review of Control, Robotics, and Autonomous Systems, 5, 2021. 
[14] Yinlam Chow, Ofir Nachum, Edgar Duenez-Guzman, and Mohammad Ghavamzadeh. A lyapunov-based approach to safe reinforcement learning. In Advances in Neural Information Processing Systems (NeurIPS), 2018. 
[15] Open Source Robotics Foundation. Gazebo. https://gazebosim.org/home. Accessed: 2023-07-10. 
[16] Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario Marchand, and Victor Lempitsky. Domain-adversarial training of neural networks. The Journal of Machine Learning Research, 17(1), 2016. 
[17] Javier Garcia and Fernando Fernandez. A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research, 16:1437–1480, 2015. 
[18] M. Geist and O. Pietquin. Algorithmic survey of parametric value function approximation. IEEE Transactions on Neural Networks and Learning Systems, 24(10):1543–1562, 2013. 
[19] Shangding Gu, Jakub Grudzien Kuba, Munning Wen, Ruiqing Chen, Ziyan Wang, Zheng Tian, Jun Wang, Alois Knoll, and Yaodong Yang. Multi-agent constrained policy optimisation. arXiv preprint arXiv:2110.02793, 2021. 
[20] Shangding Gu, Long Yang, Yali Du, Guang Chen, Florian Walter, Jun Wang, Yaodong Yang, and Alois Knoll. A review of safe reinforcement learning: Methods, theory and applications. 5 2022. 
[21] Shixiang Gu, Ethan Holly, Timothy Lillicrap, and Sergey Levine. Deep reinforcement learning for robotic manipulation with asynchronous off-policy updates. In 2017 IEEE international conference on robotics and automation (ICRA), pages 3389–3396. IEEE, 2017. 
[22] Carlos Gómez-Huélamo, Javier Del Egido, L. M. Bergasa, R. Barea, Elena López-Guillén, Felipe Arango, Javier Araluce, and Joaquín López. Train here, drive there: Ros based end-to-end autonomous-driving pipeline validation in carla simulator using the nhtsa typology. Multimedia Tools and Applications, 2021. 
[23] Irina Higgins, Arka Pal, Andrei A Rusu, Loic Matthey, Christopher P Burgess, Alexander Pritzel, Matthew Botvinick, Charles Blundell, and Alexander Lerchner. Darla: Improving zero-shot transfer in reinforcement learning. arXiv preprint arXiv:1707.08475, 2017. 
63
[24] Judy Hoffman, Eric Tzeng, Taesung Park, Jun-Yan Zhu, Phillip Isola, Kate Saenko, Alexei Efros, and Trevor Darrell. Cycada: Cycle-consistent adversarial domain adaptation. In ICML, 2018. 
[25] Junyan Hu, Hanlin Niu, Joaquin Carrasco, Barry Lennox, and Farshad Arvin. Voronoi-based multi-robot autonomous exploration in unknown environments via deep reinforcement learning. IEEE Transactions on Vehicular Technology, 69(12):14413–14423, 2020. 
[26] Stephen James, Paul Wohlhart, Mrinal Kalakrishnan, Dmitry Kalashnikov, Alex Irpan, Julian Ibarz, Sergey Levine, Raia Hadsell, and Konstantinos Bousmalis. Sim-to-real via sim-to-sim: Data-efficient robotic grasping via randomized-to-canonical adaptation networks. In CVPR, 2019. 
[27] Lodewĳk Kallenberg. Linear programming and finite Markovian control problems, volume 148. 1983. 
[28] Dohyeong Kim and Songhwai Oh. Trc: Trust region conditional value at risk for safe reinforcement learning. IEEE Robotics and Automation Letters, 7:2621–2628, April 2022. 
[29] Jens Kober, J Andrew Bagnell, and Jan Peters. Reinforcement learning in robotics: A survey. The International Journal of Robotics Research, 32(11):1238–1274, 2013. 
[30] David L Leottau, Javier Ruiz-del Solar, and Robert Babuška. Decentralized reinforcement learning of robot behaviors. Artificial Intelligence, 256:130–159, 2018. 
[31] Zuxin Liu, Zhepeng Cen, Vladislav Isenbaev, Wei Liu, Zhiwei Steven Wu, Bo Li, and Ding Zhao. Constrained variational policy optimization for safe reinforcement learning. 1 2022. 
[32] Zuxin Liu, Hongyi Zhou, Baiming Chen, Sicheng Zhong, and Ding Zhao. Safe model-based reinforcement learning with robust cross-entropy method, 2021. 
[33] Mingsheng Long, Yue Cao, Jianmin Wang, and Michael Jordan. Learning transferable features with deep adaptation networks. In ICML, 2015. 
[34] Zoran Miljković, Marko Mitić, Mihailo Lazarević, and Bojan Babić. Neural network reinforcement learning for visual control of robot manipulators. Expert Systems with Applications, 40(5):1721–1736, 2013. 
[35] MIT. Ros 101. https://vnav.mit.edu/labs/lab2/ros101.html. Accessed: 2023-06-29. 
[36] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, and et al. Human-level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015. 
64
[37] P.Read Montague. Reinforcement learning: An introduction, by sutton, r.s. and barto, a.g. Trends in Cognitive Sciences, 1999. 
[38] Igor Mordatch, Kendall Lowrey, Galen Andrew, Ilya Popov, Oriol Vinyals, and Marcin Andrychowicz. Domain randomization and pyramid consistency: Simulation-to-real generalization without accessing target domain data. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019. 
[39] Fabio Muratore, Fabio Ramos, Greg Turk, Wenhao Yu, Michael Gienger, and Jan Peters. Robot learning from randomized simulations: A review. Frontiers in Robotics and AI, 9:1–19, 2022. 
[40] T. Nguyen, Ngoc Duy Nguyen, and S. Nahavandi. Deep reinforcement learning for multiagent systems: A review of challenges, solutions, and applications. IEEE Transactions on Cybernetics, 50(5):2190–2203, 2020. 
[41] Matthew Norton, V. Khokhlov, and S. Uryasev. Calculating cvar and bpoe for common probability distributions with application to portfolio optimization and density estimation. Annals of Operations Research, 2019. 
[42] Masahiro Ono, Marco Pavone, Yoshiaki Kuwata, and J Balaram. Chance-constrained dynamic programming with application to risk-aware robotic space exploration. Autonomous Robots, 39(4):555–571, 2015. 
[43] Blazej Osinski, Sergey Levine, Chelsea Finn, and Pieter Abbeel. Simulation-based reinforcement learning for real-world autonomous driving. arXiv preprint arXiv:2005.02215, 2020. 
[44] Cosmin Paduraru, D. Mankowitz, Gabriel Dulac-Arnold, J. Li, Nir Levine, Sven Gowal, and Todd Hester. Challenges of real-world reinforcement learning: definitions, benchmarks and analysis. Machine Learning, 110(6):1367–1401, 2021. 
[45] Sinno Jialin Pan and Qiang Yang. A survey on transfer learning. IEEE Transactions on Knowledge and Data Engineering, 22(10):1345–1359, 2010. 
[46] Sinno Jialin Pan and Qiang Yang. A comprehensive survey on transfer learning. arXiv preprint arXiv:1911.02685, 2019. 
[47] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel van de Panne. Deepmimic: Example-guided deep reinforcement learning of physics-based character skills. ACM Transactions on Graphics (TOG), 37(4):1–14, 2018. 
[48] Tu-Hoa Pham, Giovanni De Magistris, and Ryuki Tachibana. Optlayer-practical constrained optimization for deep reinforcement learning in the real world. In 2018 IEEE International Conference on Robotics and Automation (ICRA), pages 6236–6243. IEEE, 2018. 
65
[49] Oxford University Press. Oxford English Dictionary. Oxford University Press, Oxford, UK, 2019. 
[50] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, John Schulman, Emanuel Todorov, and Sergey Levine. Learning dexterous in-hand manipulation. The International Journal of Robotics Research, 39(1):3–20, 2020. 
[51] Alex Ray, Joshua Achiam, and Dario Amodei. Benchmarking safe exploration in deep reinforcement learning. arXiv preprint, pages S. 1–6, 2019. 
[52] Kevin Regan and Craig Boutilier. Regret-based reward elicitation for markov decision processes. In Proceedings of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence, pages 444–451, 2009. 
[53] Florian Richter, Ryan K Orosco, and Michael C Yip. Open-sourced reinforcement learning environments for surgical robotics. arXiv preprint arXiv:1903.02090, 2019. 
[54] Coppelia Robotics. Coppelia robotics. https://www.coppeliarobotics.c om/. Accessed: 2023-07-10. 
[55] Trossen Robotics. Interbotix turtlebot 2i mobile ros platform. https: //www.trossenrobotics.com/interbotix-turtlebot-2i-mobile-r os-platform.aspx, 2023. Accessed: 2023-07-12. 
[56] ROS. Master. http://wiki.ros.org/Master. Accessed: 2023-06-29. 
[57] ROS. Running ros across multiple machines. http://wiki.ros.org/ROS/T utorials/MultipleMachines. Accessed: 2023-06-29. 
[58] ROS. Turtlebot. http://wiki.ros.org/Robots/TurtleBot, 2023. Accessed: 2023-07-12. 
[59] Keith W Ross. Randomized and past-dependent policies for markov decision processes with multiple constraints. Operations Research, 37(3):474–477, 1989. 
[60] Keith W Ross and Ravi Varadarajan. Markov decision processes with sample path constraints: the communicating case. Operations Research, 37(5):780–790, 1989. 
[61] Keith W Ross and Ravi Varadarajan. Multichain markov decision processes with a sample path constraint: A decomposition approach. Mathematics of Operations Research, 16(1):195–207, 1991. 
[62] Andrei A Rusu, Matej Večerík, Thomas Rothörl, Nicolas Heess, Razvan Pascanu, and Raia Hadsell. Sim-to-real robot learning from pixels with progressive nets. In Conference on Robot Learning, 2017. 
66
[63] J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel. High-dimensional continuous control using generalized advantage estimation. arXiv preprint arXiv:1506.02438v6, 2018. 
[64] John Schulman, Sergey Levine, Philipp Moritz, Michael I Jordan, and Pieter Abbeel. Trust region policy optimization. arXiv preprint arXiv:1502.05477, 2015. 
[65] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. arXiv preprint arXiv:1506.02438, 2016. 
[66] Z. Si, Z. Zhu, A. Agarwal, S. Anderson, and W. Yuan. Grasp stability prediction with sim-to-real transfer from tactile sensing. In IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2022. 
[67] Laura Smith, James Kew, Xue Bin Peng, Sehoon Ha, Jie Tan, and Sergey Levine. Legged robots that keep on learning: Fine-tuning locomotion policies in the real world. In IEEE International Conference on Robotics and Automation (ICRA), 2022. 
[68] Baochen Sun, Jiashi Feng, and Kate Saenko. Return of frustratingly easy domain adaptation. arXiv preprint arXiv:1511.05547, 2015. 
[69] Richard S Sutton and Andrew G Barto. Reinforcement Learning: An Introduction. MIT press Cambridge, 2018. 
[70] Jie Tan, Tingnan Zhang, Erwin Coumans, Atil Iscen, Yunfei Bai, Danĳar Hafner, Steven Bohez, and Vincent Vanhoucke. Sim-to-real: Learning agile locomotion for quadruped robots. Robotics: Science and Systems XIV, 2018. 
[71] Y. C. Tang, J. Zhang, and R. Salakhutdinov. Worst cases policy gradients. In Proc. Conf. Robot Learn., pages 1078–1093, 2020. 
[72] Brĳen Thananjeyan, A. Balakrishna, Suraj Nair, Michael Luo, K. Srinivasan, M. Hwang, Joseph E. Gonzalez, Julian Ibarz, Chelsea Finn, and Ken Goldberg. Recovery rl: Safe reinforcement learning with learned recovery zones. IEEE Robotics and Automation Letters, 6(3):5426–5433, 2021. 
[73] Gian Diego Tipaldi. Hands-on your turtlebot 2. https://web2.qatar.cmu .edu/~gdicaro/16311-Fall17/slides/start-with-turtlebot.pdf. Accessed: 2023-05-07. 
[74] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. IEEE International Conference on Intelligent Robots and Systems, 2017-Septe:23–30, 2017. 
67
[75] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 5026–5033, 2012. 
[76] Jonathan Tremblay, Aayush Prakash, David Acuna, M. Brophy, V. Jampani, Cem Anil, Thang To, Eric Cameracci, Shaad Boochoon, and Stan Birchfield. Training deep networks with synthetic data: Bridging the reality gap by domain randomization. In 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), 2018. 
[77] Matteo Turchetta, Felix Berkenkamp, and Andreas Krause. Safe exploration in finite markov decision processes with gaussian processes. In Advances in Neural Information Processing Systems, 2016. 
[78] Eric Tzeng, Judy Hoffman, Trevor Darrell, and Kate Saenko. Simultaneous deep transfer across domains and tasks. In ICCV, 2015. 
[79] Eric Tzeng, Judy Hoffman, Ning Zhang, Kate Saenko, and Trevor Darrell. Deep domain confusion: Maximizing for domain invariance. arXiv preprint arXiv:1412.3474, 2014. 
[80] Lukas Vordemann. Safe reinforcement learning for human- robot collaboration, 2022. 
[81] Haoran Wang, T. Zariphopoulou, and X. Zhou. Exploration versus exploitation in reinforcement learning: A stochastic control approach. arXiv preprint arXiv:1812.01552, 2018. 
[82] Jingkang Wang, Yang Liu, and Bo Li. Reinforcement learning with perturbed rewards. AAAI 2020 - 34th AAAI Conference on Artificial Intelligence, pages 6202–6209, 2020. 
[83] Mei Wang and Weihong Deng. Deep visual domain adaptation: A survey. Neurocomputing, 312, 2018. 
[84] Christopher J. C. H. Watkins and P. Dayan. Q-learning. Machine Learning, 8(3-4):279–292, 1992. 
[85] Lilian Weng. Domain randomization for sim2real transfer. lilianweng.github.io, 2019. 
[86] Mengyuan Yan, Iuri Frosio, Stephen Tyree, and Jan Kautz. Sim-to-real transfer of accurate grasping with eye-in-hand observations and continuous control. arXiv preprint arXiv:1712.03303, 2017. 
[87] Q. Yang, T. D. Simão, S. H. Tindemans, and M. T. Spaan. Wcsac: Worst-case soft actor critic for safety-constrained reinforcement learning. In Proc. AAAI Conf. Artif. Intell., pages 10639–10646, 2021. 
68
[88] Wenshuai Zhao, Jorge Peña Queralta, and Tomi Westerlund. Sim-to-real transfer in deep reinforcement learning for robotics: a survey. arXiv preprint arXiv:2009.13303, 2020. 
[89] Wenshuai Zhao, Jorge Peña Queralta, Li Qingqing, and Tomi Westerlund. To-wards closing the sim-to-real gap in collaborative multi-robot deep reinforcement learning, 2020. 
[90] Wenshuai Zhao, Jorge Peña Queralta, Li Qingqing, and Tomi Westerlund. Ubiquitous distributed deep reinforcement learning at the edge: Analyzing byzantine agents in discrete action spaces. Procedia Computer Science, 177:324– 329, 2020. The 11th International Conference on Emerging Ubiquitous Systems and Pervasive Networks (EUSPN 2020) / The 10th International Conference on Current and Future Trends of Information and Communication Technologies in Healthcare (ICTH 2020) / Affiliated Workshops. 
[91] Yilun Zhou, Conner Barnes, Xiangyang Jing, Brian Taylor, and Peter Goldfeder. Implicit 3d orientation learning for 6d object detection from rgb images. Pro-ceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019. 
69