> Source: https://researchportal.hkust.edu.hk/en/studentTheses/reinforcement-learning-in-nonstationary-environments

Skip to main navigationSkip to searchSkip to main contentThe Hong Kong University of Science and Technology Research Portal Home  
Reinforcement learning in nonstationary environments
Ping-Man Choi
Department of Computer Science and Engineering
Student thesis :  Doctoral thesis
Abstract
Learning to act optimally in the complex world has long been a major goal in artificial intelligence research. Reinforcement learning (RL) is an active research area that attempts to achieve this goal. In the past, studies on RL have been focused mainly on stationary environments, in which the underlying dynamics do not change over time. This assumption, however, is often unrealistic for real-world tasks. Previous works on nonstationary RL typically assume that nonstationary environments change slowly enough for adaptation to take place. The dominating approach thus far is to employ online learning techniques to give higher emphasis on recent experience in order to cope with environmental changes. This online learning approach is memoryless in the sense that even if the environment does ever revert to its previous dynamics, the learning agent must still need to re-learn the environment model. This dissertation focuses on the nonstationary environments that repeat their dynamics in certain ways. Several forms of memory mechanism are employed to allow a rapid adaptation to take place. In the first part of the dissertation, a formal model is proposed for the nonstationary environments in which environmental changes are confined to a fixed number of hidden modes. Each hidden mode specifies a Markov decision process and is itself governed by another Markov process. The relationship between the proposed model and the partially observable Markov decision processes (POMDPs) is then discussed. Two efficient model learning algorithms and a policy learning algorithm are subsequently developed. Empirical results show that the new model is computationally more tractable than POMDPs. A heuristic algorithm that works on a variant of the model is also studied. In the second part of the dissertation, I propose a memory-based RL algorithm for navigation-type nonstationary problems. The algorithm extends the idea of exploration bonuses proposed by Sutton, and can be implemented in a distributed manner. It has been applied to the network routing domain with encouraging results. Empirical studies show that the new algorithm outperforms a previous approach as the network traffic load varies over time. Keywords: Markov decision processes, reinforcement learning, partially observable Markov decision processes, nonstationary environments, Baum-Welch algorithm, network routing. Date of Award 2000 Original language English Awarding Institution
The Hong Kong University of Science and Technology
Cite this
 Standard 
Reinforcement learning in nonstationary environments Choi, P. (Author).  2000
Student thesis :  Doctoral thesis
Links
https://doi.org/10.14711/thesis-b655883
Log in to Pure   Link opens in a new tab
The Hong Kong University of Science and Technology Research Portal data protection policy   Link opens in a new tab
About web accessibility   Link opens in a new tab
Report vulnerability   Link opens in a new tab
 '