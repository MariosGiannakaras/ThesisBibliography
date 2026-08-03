> Source: https://dione.lib.unipi.gr/xmlui/bitstream/handle/unipi/18088/Tsilifonis_mtn2323.pdf

Multi-agent Reinforcement Learning with Diffusion Models 
by 
Aris Tsilifonis 
Submitted 
in partial fulfilment of the requirements for the degree of 
Master of Artificial Intelligence 
at the 
UNIVERSITY OF PIRAEUS 
June 2025 
University of Piraeus, NCSR “Demokritos”. All rights reserved.
Author: Aris Tsilifonis 
II-MSc “Artificial Intelligence” June 01, 2025 
Certified by 
Georgios Vouros Professor 
Thesis Supervisor 
Certified by 
Georgios Bouritsas Researcher 
Member of Examination Committee 
Certified by 
Maria Dagioglou Researcher 
Member of Examination Committee 
2
Multi-Agent Reinforcement Learning with Diffusion Models 
By 
Aris Tsilifonis 
Submitted to the II-MSc “Artificial Intelligence” on June 01, 2025, 
in partial fulfillment of the requirements for the MSc degree 
Abstract Diffusion models have been increasingly applied to Reinforcement Learning (RL) 
in order to deal with complex decision-making tasks. However, their effectiveness in learning multi-agent policies have not been thoroughly studied in the literature. This thesis explores how these models can enhance Multi-Agent RL (MARL) techniques in complex multi-agent environments under the celebrated CTDE schema. We present a MARL method, dubbed Q-Diffuser, which aims at inferring imaginative communication messages among agents, and further using meaningful inferred information to enhance the estimation of the Q-value function building upon the most premier MARL algorithm, called QMIX. The approach leverages a wide array of state-of-the-art techniques, including Denoising Diffusion Probabilistic Models (DDPM), transformer architectures, and the individual-global-max (IGM) property. Experimentally, we evaluate Q-Diffuser on the widely used StarCraft Multi-Agent Challenge (SMAC) benchmark and demonstrate superior performance over vanilla QMIX on a diverse set of challenging tasks, including Hard and Super-Hard maps. 
Thesis Supervisor: Georgios Vouros Title: Multi-Αgent Reinforcement Learning with Diffusion Models 
3
Acknowledgments 
This thesis required a great deal of hardwork anddedication, but Iwas fortunate to have some truly important people supporting me throughout the journey. First, I would like to sincerely thank my supervisor, Prof. Georgios Vouros, for introducing me to this exciting topic in AI. He consistently made time to meet with me each week to discuss ideas and progress. Thanks to his guidance, the work became not only productive but also genuinely enjoyable. I’m also deeply grateful to my close friends, Andreas and Nikos, for their mentorship and technical insights. Their support played a significant role in shaping the quality of this thesis. A heartfelt thank you goes to my parents for always being there for me. Their encouragement kept me going. Also, I want to thank my brother, who was always willing to make time for me whenever I needed it most. Last but not least, I want to thank my band for helping me relax and feel good during this time. 
4
Contents 
Acknowledgments 4 
List of Figures 7 
List of Tables 8 
1 Introduction 9 1.1 General Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.2 Thesis structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 1.3 Introduction to Multi-Agent Systems . . . . . . . . . . . . . . . . . . . . 11 1.4 Introduction to Multi-Agent Reinforcement Learning . . . . . . . . . . . 13 
1.4.1 Computational Complexity . . . . . . . . . . . . . . . . . . . . . . 14 1.4.2 Non-stationarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 1.4.3 Partial-observability . . . . . . . . . . . . . . . . . . . . . . . . . . 15 1.4.4 Credit Assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 
1.5 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 1.5.1 The CTDE schema . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 1.5.2 Agent Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 1.5.3 (Multi-Agent) Reinforcement Learning with Diffusion Models . . 19 1.5.4 Further Related Work . . . . . . . . . . . . . . . . . . . . . . . . . 21 
1.6 Main objectives of this thesis . . . . . . . . . . . . . . . . . . . . . . . . . 21 
2 Preliminaries and Background 24 2.1 Markov Decision Process . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 2.2 Multi-agent Reinforcement-Learning . . . . . . . . . . . . . . . . . . . . 25 
2.2.1 DEC-POMDPs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 2.2.2 Designing MARL algorithms . . . . . . . . . . . . . . . . . . . . . 26 2.2.3 Value Decomposition Networks and QMIX . . . . . . . . . . . . . 26 
2.3 Denoising Diffusion Probabilistic Models (DDPMs) . . . . . . . . . . . . 31 
3 Evaluated Framework 35 3.1 Problem Statement and Motivation . . . . . . . . . . . . . . . . . . . . . 35 3.2 Q-Diffuser: A Framework for Empowering Multi-agent Reinforcement 
Learning with Diffusion Models . . . . . . . . . . . . . . . . . . . . . . . 36 
4 Evaluation 42 4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 4.2 StarCraft Multi-Agent Challenge (SMAC) . . . . . . . . . . . . . . . . . . 42 4.3 Results on SMAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 4.4 Ablation Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 
5
4.4.1 Impact of the λ Parameter on Q-Diffuser Performance . . . . . . . 64 4.4.2 Impact of the batch size on Q-Diffuser Performance . . . . . . . . 67 4.4.3 Impact of the mixing embedding dimension and hyper-net em-
bedding dimension on Q-Diffuser Performance . . . . . . . . . . 68 4.4.4 Impact of Batch Size on the Performance of QMIX . . . . . . . . . 69 4.4.5 Impact of loss type on the performance of Q-Diffuser . . . . . . . 70 4.4.6 Impact of exploration on the performance of Q-Diffuser . . . . . . 72 
5 Conclusions and Further Discussion 73 
6 Appendix 75 6.1 Installation instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75 6.2 QMIX and Q-Diffuser Configuration files . . . . . . . . . . . . . . . . . . 76 6.3 Hardware and versions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 
6
List of Figures 
1 Multi-agent system schematic representation. . . . . . . . . . . . . . . . 12 2 Multi-agent Reinforcement Learning challenges . . . . . . . . . . . . . . 17 3 Multi-agent Reinforcement Learning Training Methods . . . . . . . . . . 18 4 Agent modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 5 VDN architecture [29] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 6 QMIX architecture [60, 29] . . . . . . . . . . . . . . . . . . . . . . . . . . 30 7 Diffusion forward and reverse processes as described in [19] . . . . . . . 31 8 A graphical representation of the reparameterization trick used to derive 
the Equation 18 [16] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 9 Q-Diffuser architecture [19] . . . . . . . . . . . . . . . . . . . . . . . . . . 36 10 Denoising Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 11 2c vs 64zg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 12 3s vs 5z . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 13 Corridor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 14 MMM2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 15 6h vs 8z . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 16 3s5z vs 3s6z . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 17 2s vs 1sc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 18 5m vs 6m . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 19 Q-MIX vs Q-Diffuser Win-ratio comparison(4) . . . . . . . . . . . . . . . 57 20 QMIX vs Q-Diffuser Performance comparison . . . . . . . . . . . . . . . 63 21 (0.1 vs 0) lambda coefficient . . . . . . . . . . . . . . . . . . . . . . . . . 64 22 (0.1 vs 0.5) lambda coefficient . . . . . . . . . . . . . . . . . . . . . . . . 65 23 (0.1 vs 1) lambda coefficient . . . . . . . . . . . . . . . . . . . . . . . . . . 66 24 Ablation Study on the Batch Size of the Diffuser . . . . . . . . . . . . . . 67 25 Mixing and hyper-network embed dimension comparison . . . . . . . . . 68 26 Ablation Study on the Batch Size of the Qmix . . . . . . . . . . . . . . . . 69 27 Effect of Huber Diffuser’s Loss on the 3s_vs_5z Scenario . . . . . . . . . 70 28 Effect of L2 Diffuser’s Loss on the 3s_vs_5z Scenario . . . . . . . . . . . 71 29 Effect of exploration (epsilon annealing) . . . . . . . . . . . . . . . . . . 72 
7
List of Tables 
1 SMAC Scenarios (1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 2 SMAC Scenarios (2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47 3 Installation Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75 4 Reinstall PyTorch packages for GPU compatibility . . . . . . . . . . . . . 75 5 Install smac and more environments . . . . . . . . . . . . . . . . . . . . . 75 6 QMIX configuration file . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 7 Q-Diffuser configuration file . . . . . . . . . . . . . . . . . . . . . . . . . 77 8 System Configuration and SMAC Version . . . . . . . . . . . . . . . . . . 78 
8
1 Introduction 
1.1 General Discussion 
In the rapidly evolving technological landscape, the interplay between Artificial Intel-ligence (AI), Multi-Agent Systems (MAS), and Machine Learning (ML) has become a cornerstone in the development of intelligent systems. This introductory chapter sets the groundwork for exploring the intricate relationships among these fields and examines their combined potential to address complex challenges across diverse domains. 
Artificial Intelligence serves as the overarching domain that encompasses a variety of methodologies designed to endow machines with human-like cognitive capabilities. Techniques such as knowledge representation, natural language processing, computer vision, and robotics are integral to AI, enabling systems to perform tasks that typically require human intelligence. Within this broad field, Machine Learning has emerged as a crucial subdomain, focusing on algorithmic models that facilitate the autonomous learning of patterns and insights from data, thereby supporting data-driven predictions and decision-making. 
Multi-Agent Systems consist of multiple autonomous agents—software entities, robots, or even humans—that interact to achieve specific objectives. These interactions may be cooperative, competitive, or mixed, and MAS are particularly useful in modeling and solving complex, real-world problems that are beyond the scope of single-agent systems. 
The integration of Machine Learning into AI has significantly improved the adaptability and performance of intelligent systems. ML allows AI models to learn from data, adapt to dynamic environments, and improve iteratively over time. Prominent AI applications, such as self-driving vehicles [8], traffic control systems [34, 30], healthcare technologies [14, 7], image and video editing [56, 44, 68], and web systems [61, 32], have leveraged ML to achieve remarkable levels of precision and robustness. Further-more, when ML techniques are embedded into Multi-Agent Systems, agents gain the ability to learn, adapt, and optimize their actions. This leads tomore responsive and intelligent collective behaviors, such as in supply chain optimization, where agents make data-driven decisions based on both historical patterns and real-time updates. 
The convergence of AI, ML, and MAS is particularly evident in complex, real-world applications. For example, AI-powered chatbots [69] utilize ML to understand and re-
9
spond to user input, and as agents within amulti-agent framework, they can collaborate with other systems to resolve multifaceted issues. These scenarios highlight the synergistic potential of combining AI, ML, and MAS. 
In this context, the integration of Reinforcement Learning (RL) into Multi-Agent Sys-tems has attracted growing interest. Reinforcement learning, a branch of ML, enables agents to learn optimal behaviors through interactions with their environment. Un-like traditional supervised learning, RL is based on trial-and-error, where agents adjust their strategies according to the rewards or penalties received for their actions. This mechanism equips agents to make informed decisions, adapt to uncertainty, and continuously refine their policies in dynamic settings. 
WhenRL is incorporated intoMulti-Agent Systems, it opens the door to a highly emerging research area knownasMulti-AgentReinforcement Learning (MARL) [2]. InMARL, agents learn not only from their own experience, but also through their interactions with other agents. This fosters the development of advanced behaviors and coordination strategies that surpass those achievable by traditional methods. MARL holds significant promise for solving complex tasks that involve coordination, competition, and efficient resource management among autonomous agents. 
1.2 Thesis structure 
The structure of the thesis is as follows: 
 In the first chapter, we outline the scope and main objectives of our research and provide a broad overviewofMulti-Agent Systems andMulti-AgentReinforcement Learning. The latter part of the chapter explores key challenges such as computational complexity, partial observability, and credit assignment. A comprehensive survey of related work covers topics including centralized training, agent modeling, representation learning, and exploration strategies 
 In the second chapter, we present the theoretical background, beginning with the fundamentals of Decentralized Partially Observable Markov Decision Processes and proceeding to essential concepts in reinforcement learning, with special focus on common practices in theMARL setting. Special attention is given to the QMIX algorithm, which serves as the foundation for the framework studied. 
 In the third chapter, we describe the examined framework in detail. It begins with the problem statement and motivation and then proceeds to a complete presentation of the methodology. 
10
 The fourth chapter focuses on evaluation, starting with the experimental setup based on the SMAC benchmark. The chapter then presents the empirical results and includes an ablation study that provides further insights into the system’s behavior. 
 Finally, the fifth chapter offers a discussion of the findings, reflecting on their broader implications, and outlines directions for future research. 
1.3 Introduction to Multi-Agent Systems 
Multi-Agent systems (MAS) is a growing field in computer science research. MAS involves many autonomous agents that act on behalf of a user or a system. Instead of acting with some predefined plan, they develop strategies to achieve their goal. To operate in a coordinated way, they typically exchange messages with each other through a communication network. Consequently, they demonstrate a high level of cooperation, comparable to that of humans working in teams[80]. 
There is a tight coupling betweenMulti-AgentReinforcement Learning andMulti-Agent Systems. While classic RL focused on the optimization of the single agent scenario, MARL extends this scope by introducingmultiple agents to it. InMARL settings, agents learn through interaction with the environment, receiving rewards based on the quality of their actions. The aggregate reward of all agents serves as a key performance indicator, demonstrating that the learned behaviors are effective and that the agents have successfully coordinated within the environment. 
When transitioning from a single agent to a multi-agent setting, complexity increases significantly as agents collaborate and rely on each other. Despite these difficulties, MARL provides solutions to real-world problems where single-agent approaches are not productive. 
The diagram below depicts a Multi-Agent System. Inside it, two agents act within the environment and receive a corresponding observation from it. Each agent has its own goals, action set, and domain knowledge. A detailed diagram of each component [4] is provided below in Figure 1. 
Environments have several very unique characteristics. They can be either stochastic or deterministic. The former are known about creating outcomes with some level of uncertainty, while the latter yield definite results. Additionally, they can be classified as accessible or inaccessible, depending on whether agents have complete access to the environment’s state information. When environments are static, only the agent’s efficiency is changing. The agent’s policy can be conditioned on its history of observations if the environment is not accessible to estimate the underlying true state. Real-world 
11
Figure 1: Multi-agent system schematic representation. 
environments are typically dynamic. An agent’s action can be discrete or continuous. Discrete environments have a closed set of possible actions, whereas continuous ones offer a range of choices. 
Agents are intelligent systems that have a perception about the state of the environment and act directly inside it. They can have prior information about it, a set of possible states, and the effect of any action on any specific state. Agent’s are goal-oriented since they act to achieve their goals. These objectives are typically formulated as the maximization of a reward or utility function. In the SMAC setting exercised in our study, these goals are represented by a reward function, a scalar signal that quantifies the quality of an agent’s action in a given state or trajectory. Agents select their actions according to a policy function, which may be either probabilistic or deterministic. 
In multi-agent systems, agents can cooperate to achieve their goal. In such settings, agents coordinate their actions to reach a common goal through aligned strategies. When agents have conflicting objectives, they compete with each other. A mixed scenario may arise, involving both cooperative and competitive strategies, which can lead to increased complexity in the environment’s dynamics. 
There aremany areas inMARL that are promising for research, such as the design of action optimization methods to reach a specific goal[64]. Another field rich in research is how tomotivate agents to adopt a strategy, how to share information among agents[24], and how a hierarchy can be applied to them [66]. 
12
1.4 Introduction to Multi-Agent Reinforcement Learning 
Reinforcement learning is the field of Machine Learning that aims to teach a set of agents an optimal policy. Optimality is achieved by maximizing the cumulative reward of the multi-agent system. More specifically, we examine the interactions of the agents in the environment over time. If the agent’s behavior yields an increasing total reward, that showcases our system is learning effectively. Agents discover this policy more frequently through trial and error. They have two choices during learning, exploration, and exploitation. Since rewards are often scarce in the early stages of training, agents face a fundamental trade-off between exploitation and exploration. They must choose whether to exploit actions that currently yield high estimated returns in a given state or to explore alternative actions, either within the same state or across different states, that may lead to improved long-term performance. Exploration and exploitation are crucial for the learning of agents, since prioritizing one of them can lead to different outcomes depending on the problem. RL algorithms face the problem of the curse of dimensionality, as the state and action space can be very large in complex environments (e.g. see [57]). 
Deep neural networks, when integrated with reinforcement learning, alleviate the challenges of high-dimensional inputs by automatically extractingmeaningful feature spaces. These latent representations simplify the input data, qualifying the RL agent to learn faster and converge on an optimal policy. This allows agents tomake very complex decisions effectively, increasing their abilities in very difficult tasks, such as the robotic arm [5] and robot navigation [51]. Recent advances in single-agent reinforcement learning have motivated researchers to extend these algorithms to multi-agent settings. In these scenarios, agents aim to maximize a shared cumulative reward through repeated interactions with the environment and policy updates informed by prior experience. 
In the multi-agent scenario, each agent performs its own action. The set of actions that agents execute simultaneously at a givenmoment is called a joint action. This representation can lead to a change in the state of the environment in response to its dynamics. As this change is processed by the environment, the agents receive their rewards and observations accordingly. This procedure happens repeatedly until a terminal state is reached. The runtime duration from initial to terminal state is called an episode. Those episodes, which contain rewards, observations, and actions, provide trajectories that agents are learning to train their policy. In the context of this thesis, we specifically resort to observations and observation histories to train our model. In our setting, agents receive identical rewards at each time step of an episode, reinforcing the need for coordinated behavior to achieve shared objectives. 
Although this process might seem productive, there are some very significant obstacles on this occasion. The fact that future rewards are dependent on the joint-actions of sev-
13
eral agents can constitute the system substantiallymore complicated. Not only does the inherent uncertainty of the environment pose challenges, but potential conflicts, such as an improvement in the reward of one agent leading to deterioration of another, can further escalate the complexity of the MARL system. This problem is called the moving target, since the optimization of one’s policy can lead to the decline of others. More commonly, rewards anddynamics change in themulti-agent setting, and the state space increases with the number of agents. There are some countermeasures that agents can take to mitigate those issues. For example, they can communicate and inform other agents about their knowledge, imitate other agents, or have knowledge of the global state. 
Several challenges can occur when trying to incorporate the multi-agent methodology instead of a single agent into a system. Themost important ones are credit assignment, high computational complexity, partial observability, and non-stationarity. Those issues could happen simultaneously during run-time, which can create great risks in our model’s efficiency. For example, the demand to scale an MARL system by increasing the number of agents can lead to great complexity and computationally costly execution. Regarding non-stationarity, it can happen when agents continuously alter their plan based on what other agents do at a specific time. When agents lack adequate information on the environment, it can be difficult for them to distinguish the impact of their individual contribution on the overall performance of the group. 
1.4.1 Computational Complexity 
Reinforcement learning (RL) systems frequently exhibit high computational complexity, as the time required to process each training example can be substantial. In multiagent reinforcement learning (MARL), this challenge is amplified: complex interactions amongmultiple agents necessitate rich state representations and lead to extremely high-dimensional joint action–observation spaces, which strain parallel frameworks and make it difficult to integrate with deep learning generative techniques such as denoising diffusion probabilistic models (DDPMs). 
To alleviateMARL training bottlenecks, parallel learning frameworks can leveragemulticore CPU and GPU architectures to process multiple environment interactions concurrently. However, communication and synchronization among parallel workers introduce additional overhead, which can reduce sample efficiency and increase the number of training iterations needed for convergence. Recent approaches such as Q-Scalable [59] and SADMA [77] aim to optimize computational complexity and accelerate convergence, ultimately enhancing the scalability of large-scale MARL deployments. 
14
1.4.2 Non-stationarity 
Non-stationarity characterizes the continuous change of agents’ policies throughout the learning process. This may lead to a moving target problem because each agent adheres to the other agents policy. Their actions also change in the same pattern, thereby causing system instability. This can be attributed to the dependence of the environment state on the joint action of the agents instead of each individual agent’s action. Many MARL algorithms use methods such as Centralized Training with Decentralized Execution (CTDE) or information sharing to downgrade the uncertainty caused by the multiple agents in the system. In a multi-agent setting, training agents independently leads each one to optimize its own objective in isolation, effectively behaving selfishly without accounting for the presence or adaptation of others. As a result, each agent experiences an unpredictably changing environment due to the simultaneous learning and behavioral shifts of other agents, making it difficult to learn stable and reliable strategies. Other approaches can include agent modeling and policy planning to address these problems. 
1.4.3 Partial-observability 
When the environment is partially observable, agents receive incomplete observations without knowing the full state. Partial observability is often inherent by the nature of the multi-agent systems and the non-stationarity of the multi-agent environment. It is commonly encountered in decentralized partially observable Markov decision processes (Dec-POMDPs), where a groupof agents seeks tomaximize shared return through joint actions. Training multi-agent systems in such settings poses significant challenges, as limited individual observations restrict agents’ capacity to coordinate and cooperate effectively toward a shared objective. To mitigate this issue, approaches such as inter-agent communication and centralized training with decentralized execution (CTDE) are frequently applied to facilitate improved coordination among agents. This thesis investigates a partially observable environment, namely the StarCraftMulti-Agent Challenge (SMAC), which requires effective cooperation among agents to enable optimal decision-making in a dynamic setting. 
1.4.4 Credit Assignment 
This issue is presented when agents are unable to discern their individual contributions to the joint reward in amulti-agent reinforcement learning (MARL) system. Since agents act simultaneously, it becomes difficult to identify which agent’s past actions had a greater impact on the total reward. As a result, agents can learn suboptimal policies 
15
because they cannot determine which actions were responsible for the improvements in global reward. A potential solution is to assign each agent a local reward instead of a shared global reward. However, this may lead to poor collaboration, as agents may behave selfishly. An effective alternative, as proposed in [46], is to combine local and global rewards. 
The problem of lazy agents [39] can also arise when credit is not properly assigned. If one agent contributes significantly while others remain idle, the inaction of those agents may be unintentionally reinforced, since they are not penalized. The idea of avoiding harm to the system’s productivity can lead to widespread inactivity, which is detrimental in MARL. One method to discourage such laziness is to use counterfactual reasoning [11], where each agent receives feedback based on the difference between the actual joint outcome and the outcome that would have occurred had the agent taken a different action, allowing a more precise credit assignment. 
1.5 RelatedWork 
1.5.1 The CTDE schema 
Various frameworks can be used to train multi-agent learning systems. The most important ones are illustrated in Figure 3. The independent learners method involves agents being trained independently. It is the least effective approach because agents will not coordinate their actions to collectively make decisions to reach nontrivial goals, thus following an suboptimal policy in a multi-agent setting. An improved method necessitates a centralized controller that outputs the policy that each agent will abide to. To do that, it requires the observations and actions of every individual agent. Unfortu-nately, centralized training cannot be scaled for a larger multi-agent system due to the fact that complexity increases with the number of agents and possible actions. 
A more robust training schema is essential for the MARL algorithm to perform effectively in a complex and large-scale multi-agent environment. In this thesis, we focus on the celebrated Centralized Training and Decentralized Execution [40] schema. Ac-cording to Kraemer and Banerjee [33], multi-agent systems can benefit from the CTDE framework because the model has available information from all the agents of the environment such as rewards, observation, and other parameters during training. This can create amore rich representation for themodel to learn. During testing, each agent acts on the basis of its own local observations. This approach helps eliminate challenges such as non-stationarity, as centralized information leads to more stable learning. Furthermore, incomplete observations are not present during training, allowing the model to teach the agent more efficiently in that phase. [79]. When using a value-
16
Figure 2: Multi-agent Reinforcement Learning challenges 
based method, cooperating agents are expected to optimize a shared value function. Research efforts focus on identifying effective strategies to decompose and optimize this joint value function. We will refer to such challenges in the next chapter of this thesis. 
1.5.2 Agent Modeling 
Agent modeling, also known as opponent modeling, is about creating models to replicate other agents behavior. An agent model can make predictions about the actions, observations, or a specific long-term target of other agents. In partially observable settings, agents may infer the beliefs of other agents about the global state in order to reconstruct it fully. To this end, an agent model can leverage observation histories, joint actions, or a combination of a subset of them. 
Agent Modeling (AM) has been introduced as a means to infer either the policies of 
17
Figure 3: Multi-agent Reinforcement Learning Training Methods 
Figure 4: Agent modeling 
other agents or hidden components of the environment [3]. Several works employ Bayesian inference to capture probabilistic beliefs [91, 45, 85], while others incorporate elements inspired by theory of mind [48, 45, 22]. LIAM [54] and SMPE [31], for instance, leverage an encoder-decoder (ED) architecture to generate agent embeddings by reconstructing local information, which are then used as auxiliary inputs for policy learning. 
Moreover, most AM methods assume a single learning agent interacting with fixed, non-adaptive co-players [17, 53, 54, 47, 12]. Some further rely on strong prior knowledge about observation features [72, 47], or require access to other agents’ internal information at execution time [84, 21, 22, 12]. Otherworks are limited to fully cooperative team-based settings [70]. 
A model for each agent is needed to represent the behaviors of different agents. The concepts of best-response and policy reconstruction are fundamental in agent modeling. An approach to policy reconstruction involves the use of generative models. These models can improve an agent’s decision-making process by mitigating issues related to non-stationarity and partial observability, since they model the intentions of other agents. This enables them to discover what others are thinking, helping them to act proactively and improving their policies long-term. 
A paper that combines CTDE, Communication, and Agent-Modeling in MARL settings 
18
is Multi-Agent Incentive Communication (MAIC) [84], a framework where agents generate targeted incentive messages that directly influence the value function of teammates for explicit coordination. MAIC learns teammate models to tailor messages and uses a novel regularization to promote efficient communication. It is compatible with various MARL algorithms and value factorization methods. Experiments proved that MAIC significantly outperforms baselines in several cooperative tasks. It uses QMIX as the backbone algorithm. 
1.5.3 (Multi-Agent) Reinforcement Learning with Diffusion Models 
Single-Agent RL with DMs Several important papers are related to MARL with diffusionmodels in the online setting. Regarding single agent RL, one of the first papers that emerged in this field is the DIPO algorithm (Diffusion Policy)[82]. The primary source of instability in actor–critic methods is the backpropagation of value-function approximation errors into the policy network. DIPO circumvents this by using the learned Q-function to relabel each stored action via a single gradient-ascent step on the Q-value with respect to the action, thereby generating higher value action targets. These relabeled actions serve as reliable supervised targets for the diffusion policy’s state-conditioned denoising (score matching) objective, effectively converting unstable approximation errors into stable training data. It can be considered an on-policy algorithm, as the agent learns from data generated by current policy. 
Another important breakthrough in the fieldwas theConsistencyPolicywithQ-Learning (CPQL) method[9]. It is an efficient off-policy single agent methodology suitable for both online and offline continuous tasks. Instead of sampling through multiple steps, it takes advantage of a consistency model to generate actions by a single step in combination with Q learning. This significantly improves inference time by approximately 45 times in comparison to previous diffusion-based such methods. Single-step testing was used as RL policies, providing exploration and exploitation efficiency. 
The previous papers introduced model-free solutions. A model-based algorithm was proposed by Rigter et al[62]. It uses a diffusion process to model the dynamics of a worldmodel. It does not generates trajectories in an autoregressive manner, but it produces full trajectorieswith a single diffusion update. The innovation is that the diffusion model is adapted to produce on-policy data that guarantees action-state consistency with the policy. This approach was tested in continuous online RL environments, such as MuJoco, with significant results. 
The diffusionmodel inRL first appeared in Janner et al. [25]. It belongs tomodel-based approaches, since it generates trajectories for planning. Also, it is an off-policy algorithm, as it uses static offline data. Rather than generating actions one step at a time, 
19
the model iteratively denoises and refines entire trajectories at once. Conducts guided sampling to shift the agent’s behavior towards higher reward regions. Another promising algorithm in the same research fields is MaDiff [90]. This paper extends diffusion-based offline RL to cooperative offline MARL in CTDE framework. The method adds an attention module to the diffusion model for better multi-agent coordination during centralized training. It showed high scores in some important benchmarks, namely MPE and SMAC. 
Finally, an actor critic method has illustrated impressive results in single agent benchmarks. This paper presents MaxEntDP[10], a novel online reinforcement learning algorithm that seamlessly incorporates diffusion models within the maximum entropy framework. To bolster policy improvement, MaxEntDP introduces a Q-weighted noise estimation technique, thus enabling more informed and effective action sampling. For policy evaluation, themethod employs numerical integration to accurately estimate the action probabilities under the diffusion policy. It can perform well in complex multigoal RL environments, like MuJoco. 
Multi-Agent RL with DMs It is noteworthy how diffusion models have demonstrated potential in addressing more complex reinforcement learning scenarios, such as those found in multi-agent settings. A particularly notable contribution in this area is the SiDiff algorithm [81]. Many MARLmethods exploit only local observations, thus significantly limiting their overall performance. This novel method proposes state inference with Diffusion Models. It is based on an image outpainting technique to reconstruct full global state using a U-Net, utilizing a State Generator and State Extrac-tor to infer the full global state. Also, it uses the CTDE schema and manages to extract most important information from the images that it processes with a vision transformer. Then, it administers an improved state to the agents. Designed for compatibility, SIDIFF can be effortlessly integrated into existingmulti-agent reinforcement learning (MARL) algorithms to enhance their performance, as it uses QMIX as a backbone algorithm. However, the generator and extractor can present significant computational overhead so that agents can acquire meaningful information, without compensating significantly on improved performance over standard baselines, such as QMIX. 
A recent advancement in multi-agent reinforcement learning (MARL) utilizing diffusion models is presented in [58]. Prior approaches predominantly utilized the global state representation during training, while relying on reconstructed dimensional-wise states that emphasized selected features during execution. This discrepancy led to a bias in the attention of agents towards isolated features, thereby neglecting critical interagent dependencies and relational information. By contrast, the method proposed in [58] reconstructs an agent-wise state representation that inherently captures richer inter-agent relationships. 
20
1.5.4 Further RelatedWork 
Many MARLmethods (e.g., [71, 60, 67]) approximate the joint state-action value function by leveraging individual agent models trained using the global reward signal. To enhance cooperation and coordination among agents, attention mechanisms [75] have been increasingly incorporated into MARL frameworks. These modules have been utilized for various purposes: to foster agent-centric cooperation [65], to estimate value functions that promote exploratory interactions [43], to design more effective experience replay strategies [83], to facilitate more accurate credit assignment [86], and to support the learning of robust policies [42, 78, 87]. 
In sparse rewards settings,MARLexploration strategies often encompass density-based [73, 88, 27], curiosity-driven [89, 36], and information-theoretic [35, 26] approaches. 
1.6 Main objectives of this thesis 
TL;DR. This thesis successfully extends current generative AI techniques to effectively addressmulti-agent problems. The approach is evaluated onwidely usedMARL testbeds and demonstrated improved performance over the standard baseline MARL algorithm QMIX. 
Motivation in the context of relatedwork. This thesis ismotivated by the absence of Multi-Agent Reinforcement Learning (MARL) methods grounded in diffusion models, as discussed in the related work section. The approach builds upon the ideas introduced by Xu et al. [81], aiming to address several limitations of their framework. First, the method presented in [81] is tailored exclusively for image-based environments, which are relatively uncommon in the evaluation ofMARL algorithms [55, 52]. Second, their architectural design is notably complex and unintuitive, while also demonstrating limited performance in standard benchmarks—such as the image-based version of the StarCraftMulti-Agent Challenge (SMAC) [63]—when compared to conventionalMARL baselines. 
Objectives of this thesis The primary objectives of this thesis are the following: 
 To study and evaluate amethod, referred to asQ-Diffuser, whichwas presented in a Python codebase[13]. This approach is built upon PyMARL [55], a widely used modular framework for developing and benchmarkingmulti-agent reinforcement learning (MARL) algorithms. It combined the QMIX algorithm [60] and De-noising Diffusion Probabilistic Models [18], within the paradigms of Centralized Training with Decentralized Execution (CTDE) and Agent Modeling (AM). 
21
 To learn how to generate novel local views for agents, enabling them to predict future outcomes of the game. Additionally, infer the global state from partial agent observations in order to enhance collaboration within a multi-agent setting. 
 Integration of a diffusion-based component into the QMIX framework to significantly enhance the modeling of inter-agent dependencies and improve coordinated decision making. Diffusion models approximate the complex multimodal conditional distribution over joint observations by learning to reverse a structured noising process, thereby generating diverse context embeddings. In SMAC’s challenging scenarios, this capacity allows the term Qbias to represent multiple plausible coordination patterns between agents, something that a single-pass MLP cannot achieve. 
 Address the partial observability and non-stationarity challenges inherent in online cooperative environments such as SMAC. In this setting, a standalone DDPM cannot converge: its target distribution shifts continuously as the joint policy evolves. By embedding the diffusion component within a backbone algorithm such as QMIX, we obtain stable supervision signals and high-quality context embeddings, enabling the diffusion model to generate realistic terms that enhance coordinated decision-making. 
 Apply attention mechanisms to the diffusion model’s output, allowing each agent to focus on themost relevant teammates whenmaking decisions. This is achieved by weighting the hidden states of the agents’ RNNs using attention scores derived from each agent’s predictions about the behavior of its teammates. 
 To demonstrate that the studied model outperforms QMIX in established MARL benchmarks, including theHard andSuper-HardStarCraftMulti AgentChallenge (SMAC) [76] scenarios. 
 To show that diffusion models can be efficiently leveraged as an Agent Modeling component to significantly enhance MARL performance, without relying on very complex architectures, for example, as in [81]. 
Outline Since QMIX demonstrates the best overall performance in all SMAC scenarios[63], it was selected as the backbone algorithm for the adopted method. The core idea is to refine the Q-value of each agent by incorporating an additional term, denoted Qbias, which provides contextual information on the relevance of other agents in the judgment of individual agents. Each agent performs modeling of its teammates by generating both their hidden states and observable data, conditioned on its own observations via a diffusion model. This enhancement allows agents to more accurately 
22
model their teammates’ behaviors, thereby supporting better informed and better coordination among the agents. We conducted an extensive ablation study of the analyzed method, offering valuable insight into key design choices such as batch size selection, reconstruction loss behavior, and the impact of parallel training environments. This ablation study, together with the integration of additional Gym environments and systematic debugging improvements, constitutes the primary contribution of this thesis to the original codebase. 
23
2 Preliminaries and Background 
2.1 Markov Decision Process 
Before delving into reinforcement learning (RL) algorithms, it is essential to introduce the concept of a Markov Decision Process (MDP) [20], which provides a mathematical framework for modeling sequential decision-making problems in single-agent decision making settings. An MDP is typically represented by the tuple ⟨S,A,P , r, γ, µ⟩ [1], where: 
 S denotes a finite set of states, 
 A represents a finite set of actions, 
 P : S × A → ∆(S) is the transition probability function, where ∆(S) denotes the space of probability distributions over S. The term P (s′ | s, a) specifies the probability of transitioning to state s′ when action a is taken in state s, 
 r : S × A → [0, 1] is the reward function, which assigns a scalar feedback for executing action a in state s, 
 γ ∈ [0, 1) is the discount factor, which determines the importance of future rewards in continuous tasks without a terminal state, thereby balancing short- and long-term returns, 
 µ ∈ ∆(S) is the initial state distribution, fromwhich the starting state s0 is drawn. 
At the beginning of each episode, the agent starts at an initial state s0 ∼ µ. At each time step t, the agent selects an action at ∈ A according to its decision-making strategy. The environment then responds by providing a reward rt+1 and transitioning to a new state st+1 ∼ P(· | st, at). This repeated interaction results in a trajectory τ = (s0, a0, r1, s1, . . . , st, at, rt+1). 
The agent’s behavior is guided by a stationary policy π : S → ∆(A), whichmaps states to probability distributions over actions. In this case, actions are sampled as at ∼ π(· | st). If the policy is deterministic, it reduces to a mapping π : S → A. The objective of the agent is to maximize the expected discounted return: 
Gt = rt+1 + γrt+2 + γ2rt+3 + · · · = ∞∑ k=0 
γkrt+k+1 (1) 
24
To evaluate a given policy π, we define the state-value function Vπ : S → R, which gives the expected return when starting from state s and following π thereafter: 
Vπ(s) = Eπ[Gt | St = s] 
= Eπ[rt+1 + γGt+1 | St = s] 
= ∑ a 
π(a | s) ∑ s′ 
∑ r 
P(s′, r | s, a) [r + γEπ[Gt+1 | St+1 = s′]] 
= ∑ a 
π(a | s) ∑ s′ 
∑ r 
P(s′, r | s, a) [r + γVπ(s ′)] 
(2) 
The expectations are taken over the randomness of the transition dynamics P and the stochasticity of the policy π. Since the reward is bounded in [0, 1], the value function is bounded by 0 ≤ Vπ(s) ≤ 1 
1−γ . The goal of the agent is to find a policy π that maximizes 
this value function, i.e., maxπ Vπ(s). 
Additionally, we define the **action-value function**Qπ : S ×A → R, which expresses the expected return from state swhen taking action a and following policy π thereafter: 
Qπ(s, a) = Eπ[Gt | St = s, At = a] 
= ∑ s′ 
P(s, a, s′) [r + γVπ(s ′)] 
= ∑ s′ 
P(s, a, s′) 
[ r + γ 
∑ a′ 
π(a′ | s′)Qπ(s ′, a′) 
] (3) 
As with Vπ, the action-value function is also bounded by 1 1−γ 
. 
2.2 Multi-agent Reinforcement-Learning 
2.2.1 DEC-POMDPs 
A Dec-POMDP [50] for an N-agent cooperative task is a tuple (S,A, P, r, F,O,N, γ), where S is the state space, A is the joint action space A = A1 × · · · × AN , where Ai is the action space of agent i, P (s′ | s, a) : S × A → [0, 1] is the state transition function, r(s, a) : S×A→ R is the reward function and γ ∈ [0, 1) is the discount factor. Assuming partial observability, each agent at time step t does not have access to the full state, yet it samples observations oit ∈ Oi according to the observation function Fi(s) : S → Oi. Agents’ joint observations are denoted by o ∈ O and are sampled according to F =∏ 
i Fi. The action-observation history for agent i at time t is denoted by hi t ∈ Hi, which 
25
includes action-observation pairs until t-1 and oit, on which the agent can condition its individual stochastic policy πi 
θi (ait | hi 
t) : Hi×Ai → [0, 1], parameterised by θi. The joint action of all agents other than i is denoted by a−i, and we use a similar convention for the policies, i.e., π−i 
θ . The joint policy is denoted by πθ, with parameters θ ∈ Θ. 
The objective is to find an optimal joint policy which satisfies the optimal value function V ∗ = maxθ Ea∼πθ,s′∼P (·|s,a),o∼F (s) [ 
∑∞ t=0 γ 
trt]. 
2.2.2 Designing MARL algorithms 
To addressmulti-agent problems, single-agent reinforcement learning algorithmsmust be extended to the multi-agent setting. Our analysis follows the framework presented in [4]. For notational consistency, we use ϕ to denote the parameters of value functions and θ for policy parameters. Throughout this work, we adopt the Centralized Training with Decentralized Execution (CTDE) paradigm: during training, agents may leverage joint observations or global state information, while during execution they rely solely on their individual local observations. 
We present the multi-agent reinforcement learning (MARL) algorithms using notation suitable for partially observable environments. Let ht 
i = (o0i , o 1 i , . . . , o 
t i) represent the 
local observation history of agent i up to time t, and let ht = (o0, o1, . . . , ot) denote the joint observation history. When relevant, we distinguish these from the global state st 
at time t. In settings where the full state is not accessible due to partial observability, it is common to approximate it with the joint observation history, i.e., st ≈ ht. Conversely, in fully observable environments, agents can condition directly on st rather than individual or joint observation histories. 
To enable policies and value functions to condition on past observations, we employ recurrent neural networks (RNNs), as described in [15]. RNNs maintain a hidden state that summarizes the entire observation history, allowing the network to update its internal state incrementally at each time step. As a result, value and policy functions can effectively condition on either the full history or solely the most recent observation, depending on the design. 
2.2.3 Value Decomposition Networks and QMIX 
The primary difficulty arises from the exponential growth of the joint action space as the number of agents increases. To address this issue, a key direction inMARL research focuses on factorizing the action-value function to make its learning more tractable. 
Before delving into methods that enable effective factorization, it is useful to recall that 
26
the centralized action-value function can be expressed as: 
Q(st, at;ϕ) = E 
[ ∞∑ τ=t 
γτ−trτs | st, at ] 
(4) 
where rτs represents the common reward for all agents at time step τ . 
The easiest way to solve the decomposition problem is to assume that the common reward can be linearly decomposed into individual utilities for each agent: 
rts = r̄t1 + · · ·+ r̄tn (5) 
where we define each individual reward of agent i at time step t as r̄ti , while the bar denotes that the reward is obtained by the decomposition and not by the environment itself. Then the action-value function can be decomposed as: 
Q(st, at;ϕ) = Eπ 
[ ∞∑ τ=t 
γτ−trτs | st, at ] 
= Eπ 
[ ∞∑ τ=t 
γτ−t 
(∑ i∈I 
rτi 
) | st, at 
] 
= ∑ i∈I 
Eπ 
[ ∞∑ τ=t 
γτ−trτi | st, at ] 
= ∑ i∈I 
Q(ht i, a 
t i;ϕi) 
(6) 
The Value Decomposition Networks (VDN) method [71] was proposed as a computationally efficient approach for optimizing individual utility functions while enabling the learning of decentralized policies. VDN operates using off-policy learning and employs a replay bufferD that stores the joint experiences of all agents. The objective is to minimize the loss defined in Equation 7, which serves as an approximation of the centralized action-value function across all agents. 
L(ϕ) = 1 
B 
∑ (ht,at,rts,h 
t+1)∈B 
( rts + γmax 
a Q(ht+1, a; ϕ̄)−Q(ht, at;ϕ) 
)2 (7) 
where Q(ht, at;ϕ) = 
∑ i∈I 
Q(ht i, a 
t i;ϕi) 
and max 
a Q(ht+1, a; ϕ̄) = 
∑ i∈I 
max ai 
Q(ht+1 i , ai; ϕ̄i) 
27
The architecture of VDN is illustrated in Figure 5 
Figure 5: VDN architecture [29] 
Although VDN offers a viable solution to the value decomposition problem, its reliance on a linear decomposition structure can be limiting, as the assumption of linearity may not always hold in practice. In such cases, a non-linear approach can bemore appropriate. One of the most prominent methods for non-linear value decomposition is QMIX [60]. 
To introduceQMIX,we frame the decomposition problemas learning individual actionvalue functions Q(hi, ai;ϕi) for each agent i, conditioned solely on the agent’s own observation history and action. However, these individual value functions are not trained to estimate each agent’s individual expected return. Instead, they are optimized to approximate a centralized action-value function for the entire team. Importantly, this approximation must satisfy the so-called individual-global-max (IGM) property with respect to the centralized action-value function: 
argmax a=(a1,...,an) 
Q(st, a;ϕ) = 
 argmaxa1 Q(ht 1, 1;ϕ1) 
... argmaxan Q(ht 
n, n;ϕn) 
 (8) 
The introduction of the Individual-Global-Max (IGM) property ensures that when each agent selects its action greedily according to its own action-value function, the resulting joint action is also greedy with respect to the centralized action-value function. In other 
28
words, the individual action-value functions effectively factorize the centralized actionvalue function [67]. 
QMIX enforces the IGM property by imposing a monotonicity constraint: the centralized action-value function must be monotonically increasing with respect to each individual agent’s action-value. Formally, this means that the partial derivative of the centralized action-value function with respect to each agent’s action-value function must be non-negative: 
∀i ∈ I, ∀a ∈ A : ∂Q(s, a;ϕ) 
∂Q(hi, ai;ϕi) ≥ 0 (9) 
This condition implies that if agent i increases its estimated value for a specific observation hi and action ai, then the centralized action-value should not decrease for any joint action a′ = ⟨a′−i, ai⟩, where agent i selects action ai and the other agents choose arbitrary actions a′−i. In other words, increasing the individual value estimate should not negatively impact the overall joint action-value. 
Similar to VDN, QMIX employs an individual action-value network (i.e., a deep Q-network) for each agent. To achievemonotonic value decomposition, QMIX introduces amixing network, denoted as fmix, which is a feedforward neural network that combines the individual agent Q-values to approximate the centralized action-value function: 
Q(st, at, ϕ) = fmix 
( Q(ht 
1, a t 1, ϕ1), . . . , Q(ht 
n, a t n, ϕn);ϕmix 
) (10) 
The mixing network guarantees that the monotonicity constraint in Equation 9 is satisfied if the weight matrices ϕmix contain only positive values; this restriction does not apply to the bias vectors within ϕmix. To ensure the weights remain positive, QMIX employs a separate network known as the hypernetwork, denoted by fhyper. Parameterized by ϕhyper, the hypernetwork takes the full state s as input and outputs the parameters ϕmix required by the mixing network. 
To preserve monotonicity, the hypernetwork applies an element-wise absolute value function to the outputs corresponding to the mixing network’s weight matrices, ensuring these weights are strictly non-negative. When computing the centralized actionvalue Q(s, a;ϕ), the individual values Q(h1, a1;ϕ1), . . . , Q(hn, an;ϕn) are first calculated independently. Simultaneously, the state s is fed into the hypernetwork to generate the mixing network parameters ϕmix. The mixing network then combines the individual utilities into the centralized value Q(s, a;ϕ) using these parameters. 
During training, all parametersϕof the decentralized action-value function—comprising the individual utility networks ϕ1, . . . , ϕn and the hypernetwork parameters ϕhyper—are 
29
jointly optimized by minimizing the value loss: 
L(ϕ) = 1 
B 
∑ (st,at,rts,s 
t+1)∈B 
( rts + γmax 
a Q(st+1, a; ϕ̄)−Q(st, at;ϕ) 
)2 (11) 
where batchB is sampled from the replay buffer, while the centrilized action-value function and its target value are given by equation 10 with parameters ϕ and ϕ̄ respectively. The parameters of the mixing network are not directly optimized via gradient-based methods; instead, they are generated dynamically as outputs from the optimized hypernetwork. QMIX’s training procedure largely follows the same structure as the VDN algorithm but extends it by including the initialization and optimization of both the mixing network and the hypernetwork. The value loss minimized during training is given by Equation 11. 
It is also important to note that, unlikeVDN,QMIX’s replay buffer stores the full state st, which encompasses the individual observation histories (ht 
1, . . . , h t n) of all agents. This 
comprehensive state information is essential for enforcing the monotonic mixing property, as the hypernetwork fhyper conditions on the complete environment state during parameter generation. The QMIX architecture is depicted in Figure 6. 
Figure 6: QMIX architecture [60, 29] 
30
2.3 Denoising Diffusion Probabilistic Models (DDPMs) 
DDPMs [19] model the data generation process as a Markov chain that progressively denoises a sample over multiple timesteps. Specifically, starting from an initial clean data x0 Gaussian noise is gradually added to derive a completely noisy sample xT , forming a sequence of noisy data {x1, ..., xT}. This forward diffusion process is defined by a series of Gaussian transitions as follows: 
q(xt | xt−1) = N (xt; √ αtxt−1, (1− αt)I) (12) 
where each αt is a part of a predefined noise schedule and t ∈ {1, ..., T}. The joint distribution over all noisy samples given the clean data x0 can be expressed as: 
q(x1:T | x0) = T∏ t=1 
q(xt | xt−1) (13) 
To generate novel samples, we need to reverse the process described in 12, starting from pure noise xT ∼ N (0, I). Since the quantity q(xt−1 | xt) is intractable, we must learn a model pθ to approximate the reverse conditional distributions using parameterized Gaussian transitions: 
pθ(xt−1 | xt) = N (xt−1;µθ(xt, t), σθ(xt, t)) (14) 
pθ(x0:T ) = p(xT ) T∏ t=1 
pθ(xt−1 | xt) (15) 
Figure 7: Diffusion forward and reverse processes as described in [19] 
As described in [19], under the reparameterization trick [28], samples xt ∼ q(xt | xt−1) can be obtained as follows: 
31
xt = √ αtxt−1 + 
√ 1− αt ϵ with ϵ ∼ N (0, I) (16) 
Similarly, samples xt−1 ∼ q(xt−1 | xt−2) are expressed as: 
xt−1 = √ αt−1xt−2 + 
√ 1− αt−1 ϵ, with ϵ ∼ N (0, I) (17) 
The expression for q(xt | x0) can be derived recursively through repeated application of the reparameterization trick. Thus, at any timestep t, the noisy sample xt can be obtained using the following closed-form expression: 
Figure 8: A graphical representation of the reparameterization trick used to derive the Equation 18 [16] 
xt = √ ᾱtx0 + 
√ 1− ᾱt ϵ 
∼ N ( xt; √ ᾱtx0, (1− ᾱt)I 
) (18) 
where ϵ ∼ N (0, I) and ᾱt := ∏t 
s=1 αs. 
The training goal is to learn the parameters θ thatmaximize the data likelihood log pθ(x0). This is typically achieved by optimizing an Evidence Lower Bound (ELBO) on the loglikelihood, which simplifies to a KL divergence between the learned reverse process pθ and the true forward process q. It is proved in [41] that the ELBO objective for diffusion models can be simplified into the following optimization objective: 
argmin θ 
1 
2σ2 q (t) 
[ ∥µθ(xt, t)− µq(xt, x0)∥22 
] (19) 
, 
whereσ2 q (t) = 
(1−αt)(1−ᾱt−1) 1−ᾱt 
, andµθ(xt, t) is a neural network that approximatesµq(xt, x0), the mean of the tractable reverse process q(xt−1 | xt, x0). 
32
Asdescribed in [41], by applying the reparameterization trick, bothµq(xt, x0) andµθ(xt, t) can be written as: 
µq(xt, x0) = 1 √ αt 
xt − 1− αt√ 1− ᾱt 
√ αt 
ϵ (20) 
µθ(xt, t) = 1 √ αt 
xt − 1− αt√ 1− ᾱt 
√ αt 
ϵθ(xt, t) (21) 
where ϵ ∼ N (0, I) and ϵθ(xt, t) is a noise prediction network. Therefore, as shown in [19, 41], by substituting 20 and 21 into 19, the diffusion surrogate objective can be expressed as: 
L = Ex, ϵ∼N (0,I), t∼U{1,T} 
[∥∥ϵ− ϵθ (√ 
ᾱtx0 + √ 1− ᾱt ϵ, t 
)∥∥2] (22) 
where t is sampled uniformly from all diffusion steps to ensure robustness across the entire diffusion trajectory. In practice, training is performed by teaching a denoising neural network ϵθ(xt, t) to estimate the noise ϵ that was added during the forward process. 
To generate novel data using the trained denoising network ϵθ(xt, t), we iteratively apply the following updating rule [19]: 
xt−1 = 1 √ αt 
( xt − 
1− αt√ 1− ᾱt 
ϵθ(xt, t) 
) + σtz (23) 
where z ∼ N (0, I). 
Below, we present the training and sampling algorithms as described in [19]. 
Algorithm 1 Training 
1: repeat 2: x0 ∼ q(x0) 
3: t ∼ Uniform({1, . . . , T}) 4: ϵ ∼ N (0, I) 
5: Take gradient descent step on: 
∇θ 
∥∥ϵ− ϵθ (√ 
ᾱtx0 + √ 1− ᾱt ϵ, t 
)∥∥2 6: until converged 
33
Algorithm 2 Sampling 
1: xT ∼ N (0, I) 
2: for t = T, . . . , 1 do 3: z ∼ N (0, I) if t > 1, else z = 0 
4: xt−1 = 1√ αt 
( xt − 1−αt√ 
1−ᾱt ϵθ(xt, t) 
) + σtz 
5: end for 6: return x0 
34
3 Evaluated Framework 
3.1 Problem Statement and Motivation 
As discussed previously, the challenges of partial observability, non-stationarity, and computational complexity can significantly hinder the performance of a MARL algorithm. To address these limitations, we provide a novel method, called Q-Diffuser. This algorithm fully embraces the CTDE paradigmwhile explicitly avoiding inter-agent communication during execution, which may otherwise impair generalization by making agents overly dependent on suchmechanisms. This work adopts the CTDE scheme, given its strong performance in benchmark tasks, as reported in the literature. The environment is modeled using the Decentralized Partially Observable Markov Decision Process (DecPOMDP) framework. In particular, as we will see later in this thesis, Q-Diffuser achieves strong results across all maps in SMAC, the most popular MARL environment. 
The core idea of the studied method is to refine the Q values of individual agents with an additional term, which we denote by Qbias, providing contextual information on the relevance of fellow agents in each agent’s individual decision-making process. In the diffusion-based framework, called Diffuser in Figure 9, each team member performs modeling of its teammates by generating both their hidden states and observable data, conditioned on its own observations. This process captures an individual agent’s internal belief in what its teammates perceive through their observations, as well as the intentions inferred from their latent representations. For each agent, themodel treats the rest of the team as targets to be predicted, allowing it to simulate what those teammates might perceive and how they are likely to think and act. This modeling procedure is executed independently for every agent in the team, with Diffuser learning to produce refined internal representations that enhance the agents’ ability to anticipate future game dynamics more accurately. Although the original QMIX architecture models agents using recurrent neural networks (RNNs), the approach extends this design to construct more sophisticated agents. This enhancement allows agents to more accurately model their teammates’ behaviors, thereby supporting better informed and better coordination among the agents. An attention mechanism is used to weight the contributions of the predictions of other agents in the decision-making process of each individual agent, allowing more informed and context-aware action selection. This allows each agent to make decisions based not only on its own observations but also on the inferred perspectives and intentions of its teammates. In essence, the method serves as a technique for approximating global state inference using only the partial observations of the agents. 
35
3.2 Q-Diffuser: A Framework for Empowering Multi-agent Reinforcement Learning with Diffusion Models 
Figure 9: Q-Diffuser architecture [19] 
The core idea behind our algorithm is illustrated in the figure above. It involves two primary components: the Agent and the Diffuser, which together enable enhanced learning performance. Specifically, we augment a standard RNN-based agent architecture by integrating an Attention Module and a diffusion-based Teammate Model. Operat-ing under the Centralized Training with Decentralized Execution (CTDE) paradigm, we construct a centralized information structure during training while maintaining decentralized input for execution. 
Centralized Agent Information To train the Teammate Model (Agent Modeling component) effectively, we leverage all available information from the agents at each 
36
timestep during training. For this purpose, we infer amessage for agent i (agentmodeling) via Diffuser, by predicting local information of all other agents j ̸= i. Each inferred message is designed to predict local observation otj and the hidden state h 
t j of the agent 
j. The values of j range from 1 to the number of agents in the ally team. Formally, the message corresponding to agent j is as follows: 
mj,i = {otj, ht j} (24) 
In this way, agent i’s Diffuser aims to generate the concatenated messages corresponding to all other agents j. 
Training of the diffusion model The Diffuser model is trained using the structured messages described above. During training, we use the complete set of agent information at each time step of an episode. Diffuser uses a DDPM as a backbone, which applies a forward diffusion process, inwhich eachmessage is progressively transformed into a noisy representation, following the noise formulation presented in Equation 17. This process incrementally perturbs the input data towards a Gaussian distribution. 
Subsequently, a Multi-Layer Perceptron (MLP)—as illustrated in Figure 10—receives the noisy message and attempts to predict the exact noise that was applied to the original input. This prediction task is guided by the standard DDPM loss function, which minimizes the difference between the predicted and actual noise components. The model parameters, denoted by ωi, are updated through gradient descent to optimize this loss. 
The primary goal of the Diffuser is to model the underlying distribution of inter-agent messages. As illustrated in Figure 10, each blue block corresponds to a linear transformation layer. The architecture comprises nine linear layers, each intermediate output (excluding the final layer) followed by a ReLU activation function. Furthermore, each layer is conditioned on a timestep embedding that encodes the denoising step index t. These timestep embeddings enable the model to adjust its predictions based on the current noise level, which is critical to accurately reverse the diffusion process and generate coherent samples. During execution, when complete agent information is no longer accessible, the trained diffuser generates high-quality syntheticmessages. These messages are then used to improve the decisionmaking of the agents in a decentralized manner. During the inference phase of the diffuser, each agent relies solely on its own local observation to infer the relevant contextual information, enabling autonomous decision-making without requiring access to the hidden states or observations of the other agents. The Q-Diffuser framework follows the decentralized execution paradigm by introducing noise to the hidden states and observations of all other agents in the 
37
Figure 10: Denoising Network 
team during training, thus preventing the reliance on exact centralized information. The diffuser must infer the noised representations of the information of other agents to produce enriched contextual representations that assist each agent inmaking decisions. 
The loss of Diffuser is as follows: 
LMSE(ω) = Eϵ,tDM 
[∥∥ϵ− ϵω ( {mj,i,tDM 
}j ̸=i, o t i, tDM 
)∥∥2 2 
] (25) 
where tDM denotes the diffusion time step, ϵ ∼ N(0, I) and tDM ∼ U(0, TDM) (where TDM denotes the total number of diffusion steps). As highlighted above, we condition the diffusion model by concatenating oti, which is used as an additional input to the denoising network. 
To generate a novel messagemj, we apply the iterative DDPM update rule as described in Algorithm 2 in the previous section. 
mj,tDM−1 = 1 
√ αtDM 
( mj,i,tDM 
− 1− αtDM√ 1− ᾱtDM 
ϵω(mj,i,tDM , oti, tDM) 
) + σtDM 
z (26) 
where z ∼ N(0, I). 
Attention module As illustrated in Figure 9, attention is applied between the hidden state hi and themessage m̂j generated by the diffusionmodel, which represents the information inferred from the other agents on the same team. The objective of the attentionmechanism is to quantify the relative importance of each teammatewith respect to the hidden state of the agent i, thus influencing its decision-making process. 
38
The attention module enables each agent to selectively focus on the most relevant messages from its teammates whenmaking decisions. Specifically, each agent imaintains a hidden state hi that encodes its local observation and task-relevant information. Mean-while, other agents j ̸= i provide inferred messages m̂j, which represent their highlevel intentions generated by a diffusion-based model. The attention mechanism evaluates the relevance of each teammate’s message m̂j to agent i by comparing it with hi. This allows agent i to dynamically assign higher importance to the messages that are most informative or useful for its own decision-making, enablingmore coordinated and context-aware behavior across the team. 
Here, we define the dimensionalities as follows: 
 dh: dimension of the agent’s hidden state hi, 
 dm: dimension of the message m̂j,i generated by the diffusion model, 
 dattn: dimension of the query/key space in the attention mechanism, 
 A: number of discrete actions. 
For each agent j ̸= i, we describe the calculation of the attention mechanism: 
vij =MLP([hi, m̂j,i]) ∈ RA, [hi, m̂j,i] ∈ Rdh+dm (27) 
qi = Wqhi ∈ Rdattn , Wq ∈ Rdattn×dh (28) 
kij = Wkm̂j,i ∈ Rdattn , Wq ∈ Rdattn×dm (29) 
whereMLP denotes amulti-layer perceptron network, andWq,Wk are learnable linear projection matrices. 
The attention scores can be expressed as: 
αij = q⊤ i kij√ dattn 
∈ R (30) 
We apply a softmax operation over the attention scores to obtain normalized attention weights. Specifically, for each agent i, the weight assigned to agent j is given by: 
α̃ij = exp(αij)∑ 
j′ ̸=i 
exp(αij′) (31) 
39
The softmax ensures that the resulting weights α̃ij ∈ [0, 1] sum to 1 across j ̸= i, forming a valid probability distribution over teammates. 
To compute the influence of other agents on agent i’s action values, we aggregate the value vectors vij using attention weights derived from the softmax-normalized scores α̃ij . Specifically, the bias term Qbias 
i ∈ RA is defined as a weighted sum over all teammates j ̸= i: 
Qbias i = 
∑ j ̸=i 
α̃ij · vij ∈ RA (32) 
This operation produces an action-wise correction to agent i’s Q-values, allowing it to incorporate the most relevant information from its teammates. The attention weights ensure thatmore influence is given to those teammateswhosemessages aremost aligned with agent i’s current state and goals. As a result, this mechanism enables more informed and coordinated decision-making within the agent team. 
Refinement of Q-values The attention module outputs refined Q-values by incorporating information from teammates, enablingmore informed action selection. These are combined using a mixing network to produce a more accurate joint Q-value. Here, the Q-values are parameterized by the agent-specific parameters θ, which are distinct from the diffusion model parameters ω. 
Q′ i = Qi(hi, ai; θ) + λ ·Qbias 
i (hi, ai; θ̃). (33) 
Let θ̃ denote the parameters of the Qbias network, and let λ represent the weight of the modeling component. The Qbias network, shown in Figure 9 as the Attention Module, consists of amulti-layer perceptron (MLP) that computes value embeddings, alongwith two fully connected layers that generate query and key embeddings. These components are jointly optimized to enable attention-based coordination among agents by modulating the original Q-values. In practice, we use λ = 0.1, as it works well in all of our experiments. Finally, we train Q′ 
i using the standard Qmix loss, described in the previous section. 
40
Algorithm 3 Q-Diffuser Algorithm 
1: Initialize agent network parameters θi, θ̃i, mixer parameters ϕi, DM ωi 
2: Initialize target networks: θ′i ← θi, ϕ′ i ← ϕi, θ̃′i ← θ̃i 
3: Initialize replay buffer D 4: for each episode do 5: Reset environment; observe state s0 and observations {oi0}ni=1 
6: for t = 0 to T − 1 do 7: for each agent i do 8: Sample messages m̂ji ∼ Diffuser using 26 9: Sample action ait ∼ ϵ-greedy(Q′ 
i(o t i, h 
t i, {m̂j,i}j ̸=i; θi)) using 33 
10: end for 11: Execute joint action at = (at1, . . . , a 
t n) 
12: Observe reward rt, next state st+1, and observations {ot+1 i }ni=1 
13: Store (st, {oti}, at, rt, st+1, {ot+1 i }) in D 
14: end for 15: if train: run Train 16: end for 17: 
18: Routine Train 19: Sample a batch of episodes from D 20: for each timestep t in the batch do 21: for each agent i do 22: Sample messages m̂ji ∼ Diffuser using 26 23: Compute Qi(h 
i t, a 
i t; θ) 
24: Compute Qbias i (hi 
t, a i t; θ̃) using 32 
25: Compute Q′ i(h 
i t, a 
i t) using 33 
26: end for 27: Compute total centralized Q-value: Qtot = Mixer({Qi}, st;ϕ) using : 28: for each agent i do 29: ai∗t+1 = argmaxa Q′ 
i(h i t+1, a; θ 
′, θ̃′) 
30: Compute Target Q′ i = Q′ 
i(h i t+1, a 
i∗ t+1; θ 
′, θ̃′) 31: end for 32: Compute target total value: Q′ 
tot = Mixer({Q′ i}, st;ϕ′) 
33: TD target: yt = rt + γQ′ tot 
34: TD loss: Lt = (Qtot − yt) 2 
35: end for 36: Update θ, θ̃ and ϕ by minimizing total loss L = 
∑ t Lt 
37: for epoch in DM_epochs do 38: for eachmj,i do 39: Update ω using 25 40: end for 41: end for 42: if episode mod C = 0 then 43: Update target networks: θ′i ← θi, θ̃′i ← θ̃i, ϕ′ 
i ← ϕi 
44: end if 
41
4 Evaluation 
4.1 Experimental Setup 
4.2 StarCraft Multi-Agent Challenge (SMAC) 
Single-agent benchmarks, such asALEandMuJoco, offer testing environments ranging from trivial scenarios to gridworlds. However, a benchmark capable of effectively evaluating cooperation in multi-agent systems did not exist, making it difficult to measure performance appropriately. To address this gap, SMAC was proposed to the computer science community. It is based on the popular Blizzard company’s game, StarCraftII [63]. In a regular game, one or more humans will compete against each other or an AI bot enemy to fight units, gather items, and construct buildings. 
Typically, there are two game modes in StarCraftII, micro- and macro-game-play. The latter refers to high-level considerations, such as long-term strategy (e.g., splitting an army into two parts). In contrast, the micro tactic involves the control of individual units, which can kite or engage in close-range (melee) combat depending on the type of enemy they are facing. The SMAC benchmark was specifically developed to focus on micromanagement. It is amodified version of the original game, designed to combine a multi-agent structurewith decentralized control. In SMAC, each unit is controlled by an independent agent that operates on the basis of its own local observations. Since each agent has a limited, self-centered field of view, this creates challenging and complex combat scenarios within the multi-agent reinforcement learning (MARL) setting. The centralized control of the enemy AI is very difficult to defeat on many occasions. 
Effective microtactics aim to maximize the reward of each individual agent while minimizing the damage received fromenemyunits, often utilizing a variety of strategic skills. An important tactic is focused fire, in which agents collectively target a specific enemy unit to eliminate it efficiently, without dealing excess damage. Other effective techniques include grouping high-armor units together to attract enemy attacks, thereby protecting more vulnerable allies. In addition, units can maneuver through the terrain to gain positional advantages ormaintain distance from enemies, minimizing incoming damage using mechanics such as kiting. 
Each combat has a scripted strategy that evaluates coordination. Combat ends when one of the two armies has been completely eliminated or the specified time limit has been reached. The goal is tomaximize win ratio, the games won compared to the games played. The battle begins with the AI of the enemy attacking the spawning point of the agent to accelerate the learning. 
42
The game scenarios are categorized into three distinct difficulty levels: easy, hard, and super-hard. The easiest battles are typically symmetric, as both sides possess the same units. The simplest type of symmetric team is homogeneous, characterized by the use of identical unit types across all agents. A more difficult scenario exists when the teams consist of more than one kind of unit (MMM2). There are situations where one type of unit is particularly strong against another, a phenomenon known as countering. In such cases, it is up to the agent to determine an optimal strategy to respond effectively. One possible approach is to protect the most vulnerable units from enemy attacks. Asym-metric scenarios occur when one team is outnumbered by the other. Finally, SMAC includes a collection of engaging microtrick scenarios that require a high level of coordination and precise micromanagement techniques to overcome the enemy. The complete list of challenges is presented in Table 1 and Table 2 below. The sight and shooting range valuesmay differ from the default values of the units in the original game because it enables efficient testing of decentralized policies. 
SMAC benchmark has a discrete set of actions. They can move north, south, west, and east. Also, dead agents can take no-op action, while the alive agent must perform an action. They can attack an enemy using their ID or stop dealing damage to them. The maximum number of actions an agent can take is minimum 7 and maximum 70, with the number varying according to the individual scenario. Healer units must use this ability instead of attacking. The agent can attack only within their shooting range, thus ensuring decentralization. The range of shooting is shorter than the range of sight, requiring agents to use other commands before attacking. 
SMAC environment provides observations without graphical elements. The observation contains useful information such as the agent’s health and the position of units on the map. The raw API allows the user to send an action command to a specific unit based on their ID. Although this does not happen in the original game, it is helpful to develop decentralized agents. The benchmark’s games are shorter than the ones in the original game. Thus, restarting the game after every episode is computationally expensive. So, the units are respawned in the initial place with an efficient debug command. In addition, automatic attacks by allied agents have been disabled to enforce explicit decision making. This is achieved by setting the allied agents’ combat behavior parameters—specifically, the Default Acquire Level is set to Passive (preventing automatic targeting), and the Response Behavior is set to NoResponse (disabling automatic retaliation). The enemy AI, however, retains its default behavior settings. 
Regarding rewards, there is an option to include sparse ones by assigning +1 to win and -1 to lose. The overall goal is to maximize the cumulative reward to improve the total win ratio between episodes. A shaped reward based on hit point damage dealt and received is provided, with positive or negative gains for killing enemy or allied units, and bonuses for winning or losing the battle. However, the creators discourage tuning 
43
the reward function for different battle scenarios. 
Finally, at each timestep, agents receive observations limited to their field of view, which is defined by a fixed sight radius centered on each unit. The environment becomes partially observable for every agent due to it. Agents have knowledge about what happens in their field of view and they are agnostic to out-of-sight events, such as the ally’s death in the fog of war [63]. The observation is a feature vector with the following attributes for both allied and enemy units: distance, relative x, relative y, health, shield, and unit type. This vector contains information only for the units within their radius of sight. In some scenarios, agents are protected by a shield layer that must be depleted before they can take direct damage to their health [63]. This mechanic adds an additional layer of defense and prolongs agent survivability. Agents also receive information on themost recent actions of allied units within their sight area. It is possible to observe key characteristics of the terrain, such as walkability and latitude. This can be accomplished by examining the values at eight equidistant points positioned along the cardinal and intercardinal directions (i.e., North, Northeast, East, Southeast, South, Southwest, West, and Northwest) at a fixed radius. This approach is substantiated by the get_surrounding_points function in the original SMAC environment, in which binary features representing walkability, along with the latitude of the eight fixed points, are explicitly included in the observation space[49, 63]. The environment supports centralized training by acquiring information about all units in the map during that stage. This state vector includes the coordinates of every agent, measured from the center of the map terrain combined with the observation’s features. The last action of every agent is added to that state. Reset of the ability of the allied units(cooldown), which is included in that state,is used to determine the delay between attacks and energy relevant to healing. The field of view is set to 9 for all agents. All features, whether part of the global state or seen by individual agents, are scaled relative to their maximum possible values to ensure consistency in representation. 
It is worth discussing some of the hardest game modes in the SMAC benchmark. Ob-serving some screenshots from the game played helps us understand the structure of each battle and potential strategies that the applied RL-algorithm might develop. In SMAC, units originate from one of three canonical StarCraft II races—Protoss, Terran, or Zerg—whichdefine their visual appearance, lore, shielding properties and other combat characteristics. However, for practical purposes within micromanagement scenarios, units are more effectively categorized by combat role into long-range, close-range (melee), and healer classes. The Protoss Colossi is a long-range unit: a towering mechanical walker equipped with dual thermal lances that deliver powerful area-of-effect damage in linear trajectories. Colossis are capable of traversing terrain elevations, including stepping up or down cliffs, which allows them to reposition strategically. Fur-thermore, when a Colossi moves to higher ground, enemy units positioned below mo-
44
mentarily gain vision of it, thereby limiting the extent to which terrain elevation can be exploited for tactical advantage[37]. Zerglings are fast melee units characterized by exceptionally high movement speed and extremely short attack cooldowns. While individually fragile, they become highly effective when deployed in large numbers, capable of overwhelming targets through coordinated swarming and sustained damage output upon contact. However, their low durability makes them particularly vulnerable to area-of-effect (splash) damage. 
One of the hard scenarios, 2c_vs_64zg (shown in Figure 11), features two Colossi facing sixty-four Zerglings. In this configuration, the enemy Zerglings outnumber the allied Colossi, constituting the largest unit contingent in the benchmark. However, the allies’ units are significantly stronger than the enemies. Colossis need to master positioning and kiting to survive close ranged units. They have long-range splash damage. In addition, they can hug the walls to avoid being surrounded by enemies. As you can see in Figure 11 they kill a lot of low health enemy units simultaneously to quickly limit incoming damage. 
Another interesting super-Hard benchmark is the corridor one. This battle involves 6 Zealots that fight 24 enemy Zerlings. Zealots are melee warriors of the Protoss race. They are relatively fast compared to other Protoss units and possess high health and damage output for a basic unit, making themwell-suited for front-line roles in a variety of combat scenarios [38]. The solution to the Corridor scenario (Figure 13) is to exploit the terrain that contains two zones connected by a corridor to limit the incoming damage from the enemies[6]. Even though Zealots are stronger individually they are significantly outnumbered and can lose the battle when swarmed by the larger enemy in an open space. 
In the Figure 18, the 5m_vs_6m scenario—classified as Hard—features five allied Ter-ran Marines facing six enemy Marines, with no melee or support units on either side. Marines are ranged infantry with moderate fire rate and limited durability, rendering them vulnerable to area-of-effect damage and numerical superiority. Outnumbered, the five allied agents must concentrate their fire on individual enemy units to rapidly reduce the volume of incoming damage. Simultaneously, they must employ kiting— withdrawing during weapon cooldowns to preserve health—and coordinate their volleys to maximize damage output before the larger enemy force can mount an effective counterattack [74]. 
45
Name Ally Units Enemy Units Type 
3m (Easy) 3 Marines 3 Marines homogeneous & symmetric 
8m (Easy) 8 Marines 8 Marines homogeneous & symmetric 
25m (Hard) 25 Marines 25 Marines homogeneous & symmetric 
2s3z (Easy) 2 Stalkers & 3 Zealots 
2 Stalkers & 3 Zealots 
heterogeneous & symmetric 
3s5z (Easy) 3 Stalkers & 5 Zealots 
3 Stalkers & 5 Zealots 
heterogeneous & symmetric 
MMM (Easy) 1 Medivac, 2 Marauders & 7 Marines 
1 Medivac, 2 Marauders & 7 Marines 
heterogeneous & symmetric 
5m vs 6m (Hard) 5 Marines 6 Marines homogeneous & asymmetric 
8m vs 9m (Hard) 8 Marines 9 Marines homogeneous & asymmetric 
10m vs 11m (Easy) 10 Marines 11 Marines homogeneous & asymmetric 
27m vs 30m (Super-Hard) 
27 Marines 30 Marines homogeneous & asymmetric 
Table 1: SMAC Scenarios (1) 
46
Name Ally Units Enemy Units Type 
3s5z vs 3s6z (Super-Hard) 
3 Stalkers &5 Zealots 
3 Stalkers & 6 Zealots 
heterogeneous & asymmetric 
MMM2 (Super-Hard) 
1 Medivac, 2 Marauders & 7 Marines 
1 Medivac, 3 Marauders & 8 Marines 
heterogeneous & asymmetric 
2m vs 1z (Easy) 2 Marines 1 Zealot micro-trick: alternating fire 
2s vs 1sc (Easy) 2 Stalkers 1 Spine Crawler micro-trick: alternating fire 
3s vs 3z (Easy) 3 Stalkers 3 Zealots micro-trick: kiting 
3s vs 4z (Easy) 3 Stalkers 4 Zealots micro-trick: kiting 
3s vs 5z (Hard) 3 Stalkers 5 Zealots micro-trick: kiting 
6h vs 8z (Super-Hard) 
6 Hydralisks 8 Zealots micro-trick: focus fire 
corridor (Super-Hard) 
6 Zealots 24 Zerglings micro-trick: wall off 
bane vs bane (Hard) 20 Zerglings & 4 Banelings 
20 Zerglings & 4 Banelings 
micro-trick: positioning 
so many banelings (Easy) 
7 Zealots 32 Banelings micro-trick: positioning 
2c vs 64zg (Hard) 2 Colossi 64 Zerglings micro-trick: positioning 
1c3s5z (Easy) 1 Colossi, 3 Stalkers & 5 Zealots 
1 Colossi, 3 Stalkers & 5 Zealots 
heterogeneous & symmetric 
Table 2: SMAC Scenarios (2) 
47
Figure 11: 2c vs 64zg 
Figure 12: 3s vs 5z 
48
Figure 13: Corridor 
Figure 14: MMM2 
49
Figure 15: 6h vs 8z 
Figure 16: 3s5z vs 3s6z 
50
Figure 17: 2s vs 1sc 
Figure 18: 5m vs 6m 
51
4.3 Results on SMAC 
In this section, we present the results of the analyzed Q-Diffuser method evaluated on the StarCraft Multi-Agent Challenge benchmark. Our algorithm demonstrates strong and consistent performance across a wide range of map scenarios. The Figure 19 below compares the win rate of the Q-Diffuser with QMIX, which serves as the foundational baseline for our approach. In the first plot, the horizontal axis represents the number of timesteps elapsed in the 3s_vs_3z scenario (Figure 19(a)), while the vertical axis shows the win rate achieved by the allied agent team against the built-in AI during evaluation. The bold line represents the average win rate across multiple environment seeds, and the shaded area denotes the interquartile range (25th to 75th percentile) over those seeds. 
Lower shaded bound = mean−NORMAL_IQR_FACTOR× std (34) 
Upper shaded bound = mean+NORMAL_IQR_FACTOR× std (35) 
NORMAL_IQR_FACTOR = 0.6745 (for 25–75% range) (36) 
Interquartile Range = [mean−0.6745 ∗ std,mean+ 0.6745 ∗ std] (37) 
The number of simulated steps tested ranges from 1.5 million for simpler maps such as 2s_vs_1sc, up to 14 million for more difficult scenarios. All environments were evaluated using EPyMARL episode runner, with the exception of the maps corridor and 6h_vs_8z. These two more demanding environments were executed using the parallel runner, with 4 and 8 parallel environments, respectively, to reduce training time and improve sampling efficiency. In addition to win rates, we also report the average return during both training and evaluation episodes to provide a comprehensive view of the learning dynamics of our method. 
With regard to the parameters used in our experiments, most of them were adopted directly from EPyMARL. The primary additions include the output dimension of the attention mechanism’s linear layers for keys and values, which was set to 32, and the hidden dimension of the MLP used for value estimation, which was set to 64. Further-more, for the MMM2 scenario, the batch size was adjusted to 16 for both algorithms. All algorithms were evaluated over 3 to 4 different random seeds before averaging the results. The total number of training steps for the experiments was selected on the basis of relevant benchmarks and results reported in the literature. 
As discussed previously, the SMAC benchmark includes environments of varying difficulty, categorized as easy, hard, and super hard. In Figure 19(a,b), the diagrams shown correspond to easier environments. In particular, for the 2s_vs_1sc map, as shown in Figure 19(b), Q-Diffuser exhibits consistently lower variance in win rate compared to QMIX up to convergence, and significantly outperforms QMIX in the range of 0.5 million to 0.8 million environment steps. The difficulty in SMAC is set to the high-
52
est non-cheating level, corresponding to difficulty level 7, which represents the hardest setting without enabling any unfair advantages for the enemy units. 
Increasing the difficulty to the hard setting highlighted the significant performance gap between QMIX and Q-Diffuser. An illustrative example is the 2c_vs_64zg scenario (Figure 19(c)), where the Q-Diffuser consistently outperforms QMIX, maintaining a higher performance line with notably low variance. This indicates greater consistency in the results compared to QMIX. Q-Diffuser appears to converge much earlier, around 1.25million steps, whereas QMIX reaches a similar optimum, approximately 92%, only around 2 million steps. 
The 3s_vs_5zmap (Figure 19(d)), which is equally challenging due to the need for stalkers to kite zealots to survive, further demonstrates this trend. The average win ratio of Q-Diffuser remains consistently at or above that of QMIX up to 2 million steps, with lower variance. Beyond 2.1 million steps, the performance gap widens, providing evidence that the Q-Diffuser attains a better optimum after additional training. 
Two additional challenging maps in SMAC are 5m_vs_6m and 8m_vs_9m, which feature homogeneous unit compositions but place the ally team at a numerical disadvantage. The low ally-to-enemy ratio increases the difficulty of these scenarios, requiring agents to learn effective coordination strategies—such as focusing fire on the same enemy unit—to survive. Neither QMIX nor Q-Diffuser fully solves these tasks. In Figure 19(e), QMIX initially performs better; however, after approximately 0.5 million environment steps, Q-Diffuser surpasses QMIX by a noticeable margin, maintaining a 5% to 10% higher win rate. Additionally, the win-ratio variance of Q-Diffuser remains consistently lower than that of QMIX. The algorithm demonstrates superior performance for themajority of the testing process, as indicated by the greater area between the lines when Q-Diffuser is above QMIX compared to when it is below. Eventually, both lines converge at around 93%, but Q-Diffuser exhibits more robust learning throughout. 
This pattern persists in Figure 19(f), where the mean win rate of our algorithm generally remains above that of QMIX. Additionally, the minimum win rates achieved by Q-Diffuser are consistently higher than those of QMIX up to approximately 1 million steps. After that point, the performance of both algorithms converges to a similar optimum of around 72%. 
In the transition to Super Hard environments, both algorithms struggle to solve the game in scenario 3s5z_vs_3s6z (Figure 19(g)), requiring significantly more training steps and exhibiting minimal performance differences. In Figure 19(h), corresponding to the MMM2 scenario, the Q-Diffuser outperforms QMIX on average up to approximately 1.5 million steps, after which their performances converge. Specifically, Q-Diffuser shows better performance than QMIX between 0.5 and 0.8 million steps, with occasional performance peaks observed between 1.0 and 1.5 million steps. 
53
In SMAC’s most challenging benchmark, 6h_vs_8z (Figure 19(i)), Q-Diffuser manages to outperformQMIX. The difficulty of this scenario is evident in the fact that, even after 1.4 million parallel training steps, the peak win ratio remains below 20%. Despite fluctuations, Q-Diffuser consistently performs above QMIX from 0.5 million steps—when the win ratio first becomes non-zero—until 1.4 million steps. Additionally, Q-Diffuser exhibits significantly lower variance compared toQMIX, indicating greater stability and less uncertainty in performance. After 1.4million steps, both algorithms appear to converge at a win ratio of around 20%. 
(a) 3s_vs_3z 
(b) 2s_vs_1sc 
Figure 19: Q-MIX vs Q-Diffuser Win-ratio comparison (1) 
54
(c) 2c_vs_64zg 
(d) 3s_vs_5z 
(e) 8m_vs_9m 
Figure 19: Q-MIX vs Q-Diffuser Win-ratio comparison(2) 
55
(f) 5m_vs_6m 
(g) 3s5z_vs_3s6z 
(h) MMM2 
Figure 19: Q-MIX vs Q-Diffuser Win-ratio comparison(3) 
56
(i) 6h_vs_8z 
Figure 19: Q-MIX vs Q-Diffuser Win-ratio comparison(4) 
In addition to the test battle win ratio, several other key metrics provide valuable insight into algorithm performance, including the training return mean, the testing return mean, and the training battle win ratio. These indicators help establish the relationship between training and testing performance and offer a more comprehensive view of generalization capabilities. The train_return_mean refers to the average return (i.e., the sum of common rewards) obtained during training episodes, while the test_return_mean corresponds to the same quantitymeasured during evaluation. Dur-ing training, the current policy of each algorithm was evaluated by conducting 100 test episodes at every 2000 training steps. During these evaluation phases, we recorded the episode returns—i.e., the accumulated common rewards obtained in each test episode— and computed the average return as 1 
N 
∑N i=1 Rt,i,j , where N = 100 is the number of test 
episodes, t denotes the current training timestep, and Rt,i,j is the return of the i-th test episode in the j-th experimental run. This metric, logged as test_return_mean in EPy-MARL, provides a reliable measure of policy performance and generalization across independent evaluations. The train_return_mean is calculated by averaging the cumulative returns over all training episodes that occurred within each logging interval (every 2000 steps)[52]. 
Furthermore, the battle_won_mean metric is used to quantify team success. For each episode, a win is attributed to the team that completely eliminates the opposing team. If the enemy is completely defeated before the episode ends, the winning team receives a value of 1 and the losing team receives 0. The battle_won_mean is then computed as the ratio of won episodes to the total number of episodes within the corresponding 
57
training or testing interval. Those are depicted in Figure 20 below. 
In Figure 20 (a,d,g), corresponding to the 3s_vs_3z, 3s_vs_5z, and 3s5z_vs_3s6z scenarios, both algorithms perform comparably across all metrics. Although the training average win rate in 3s_vs_5z (Figure 20 (d)) , slightly favors our algorithm, the advantage is not as pronounced as it is in the test mean win rate. In Figure 20(b) (2s_vs_1sc), a similar trend is observed—when the test win ratio of Q-Diffuser improves at certain intervals, the improvement is mirrored across all other metrics in those same regions, indicating consistency and reliability in performance gains. Fig-ure 20(c) (2c_vs_64zg) shows a clear advantage for our algorithm, which outperforms QMIX across all metrics until convergence, where both reach similar optimum values. In Figure 20(f) (5m_vs_6m), training and testing return means, as well as test win ratio, follow highly similar trajectories. However, the test win ratio reveals larger performance gaps in favor of Q-Diffuser. 
Figure 20(e) (8m_vs_9m) highlights even more pronounced gaps in training win ratio in favor of our algorithm compared to test win ratio, though our method outperforms in both. Notably, the training return mean consistently exceeds the testing return mean, suggesting strong training performance that translates reasonably well to generalization. In Figure 20(h) (MMM2), all metrics—except for test win ratio—follow nearly identical patterns across both algorithms, indicating stable learning dynamics with slightly better testing performance by Q-Diffuser. Lastly, in the most challenging scenario, Figure 20(i) (6h_vs_8z), our algorithm significantly outperforms QMIX after approximately 400.000 steps and maintains this advantage throughout the remainder of training. Here, the train and test returnmeans show even greater differences in favor of Q-Diffuser than the corresponding win ratios, reinforcing the strength and consistency of our approach across multiple evaluation dimensions. 
Overall, the studied strategy of dynamically weighting the influence of other agents’ predicted observations and behaviors—i.e., what they perceive and how they act—on a specific agent proves to be highly effective. When this influence is deemed significant, the Q-values of the contributing agents are biased toward actions that promote greater coordination. This mechanism, combined with diffusion models and attention within the Centralized Training with Decentralized Execution (CTDE) paradigm, demonstrates strong generalization, even in complex and high-difficulty environments. The Diffuser, through its generative capabilities, may produce agent-level representations that encourage proactive decision-making across the team. Our results validate that this approach fosters more efficient agent coordination and accelerates the resolution of challenging multi-agent tasks. 
58
(a) 3s_vs_3z 
(b) 2s_vs_1sc 
59
(c) 2c_vs_64zg 
(d) 3s_vs_5z 
60
(e) 8m_vs_9m 
(f) 5m_vs_6m 
61
(g) 3s5z_vs_3s6z 
(h) MMM2 
62
(i) 6h_vs_8z 
Figure 20: QMIX vs Q-Diffuser Performance comparison 
63
4.4 Ablation Study 
4.4.1 Impact of the λ Parameter on Q-Diffuser Performance 
We observe that the parameter λ has a significant impact on the performance of Q-Diffuser. Specifically, setting λ to 0.1 consistently yields stronger results compared to setting it to 0, as demonstrated across the entire experiment on the 2s_vs_1sc scenario. This performance trend is not limited to test win ratios; similar patterns are also evident in training win ratios and both training and test mean returns. Notably, with λ set to 0.1, Q-Diffuser converges more quickly. In contrast, setting λ to 0 effectively disables the Q-bias mechanism, which diminishes the algorithm’s learning efficiency. 
Figure 21: (0.1 vs 0) lambda coefficient 
64
Increasing the λ parameter to 0.5 yields performance that is largely consistent with the baseline value 0.1 used in our main experiments. While λ = 0.5 appears to provide more stability during the initial training phase—avoiding the sharper drop observed in test and training mean returns with lower λ values—both configurations ultimately converge around the same point. Minor fluctuations occur where one occasionally outperforms the other, but these are infrequent and not statistically significant. Overall, the results suggest that both settings produce comparable performance, making it difficult to definitively favor one over the other. 
Figure 22: (0.1 vs 0.5) lambda coefficient 
65
When λ is further increased to 1, the performance of Q-Diffuser deteriorates significantly. The gap between training and testing metrics becomes notably larger, with the most pronounced discrepancy observed in win ratio, though mean returns also reflect a substantial decline. As shown in Figure 23, Q-Diffuser with λ = 0.1 successfully converges to an optimal solution—achieving a 100% win ratio by 1.5 million steps. In contrast, the λ = 1 configuration plateaus at approximately 20%, indicating that excessive weighting of the Q-bias term hinders the model’s ability to learn an effective policy. 
Figure 23: (0.1 vs 1) lambda coefficient 
66
4.4.2 Impact of the batch size on Q-Diffuser Performance 
The default batch size used in our experiments was 32, consistent with the parameters of EPyMARL. We observe that this configuration yields better overall performance compared to a reduced batch size of 16. Specifically, the batch size of 32 leads to convergence at approximately 100%win ratio, while the run with batch size 16 stabilizes at around 80% over the same number of steps. Although a temporary decline is visible in the test mean return and training return curves for the batch size 32 setting—lasting for roughly 100,000 steps—this drop does not affect the win ratio and quickly recovers. As previously noted, such drops are typically reflected only in return-based metrics, while win ratio remains stable. In fact, during this period, Q-Diffuser still outperforms QMIX in terms of win ratio. 
Figure 24: Ablation Study on the Batch Size of the Diffuser 
67
4.4.3 Impact of the mixing embedding dimension and hyper-net embedding dimension on Q-Diffuser Performance 
Weevaluateddifferent combinations of parameters related to theQMIXbackbonewithin Q-Diffuser, focusing on the embedding dimensions of the hypernetworks and mixing networks. Specifically, we compared a configuration with a hypernetwork embedding dimension of 32 and a mixing embedding dimension of 64 against a smaller setup with values of 16 and 32, respectively. Our results indicate that the higher-dimensional configuration consistently outperforms the smaller one. While both configurations follow similar performance trends up to approximately 1.2 million steps, the smaller setup experiences a sharp decline thereafter and fails to recover to the same performance level. It is important to note that this experiment was conducted on the 3s_vs_3z environment, which typically requires more steps—around 2.5 million—for the algorithm to reach optimal performance. 
Figure 25: Mixing and hyper-network embed dimension comparison 
68
4.4.4 Impact of Batch Size on the Performance of QMIX 
Although we tested the batch size in Q-Diffuser, we aimed to explicitly examine the effect of batch size on the backboneQMIXalgorithm. The observedpattern is consistent with previous findings: a batch size of 32 consistently outperforms a batch size of 16 throughout the experiment. Furthermore, the model with batch size 32 converges to a better optimum. Specifically, while the batch size of 16 converges to approximately a 75% win ratio, the batch size of 32 achieves complete task resolution at around 1.5 million training steps. 
Figure 26: Ablation Study on the Batch Size of the Qmix 
69
4.4.5 Impact of loss type on the performance of Q-Diffuser 
We tested both the L2 norm and Huber loss for reconstructing the original samples, as described in the baseline framework. The Huber loss function integrates the L1 and L2 
loss functions through a piecewise formulation, providing robustness to outliers while maintaining sensitivity to small errors. The L2 norm significantly improved the win ratio in highly competitive environments such as 3s_vs_5z. In these environments, Q-Diffuser exhibits a more rapid increase in win ratio, with performance improvements becoming apparent around 1 million training steps. In contrast, experiments using the Huber loss show the win ratio increasing only after approximately 1.7 million steps. Additionally, theL2 loss achieves a higher win ratio optimumof around 60%, compared to only 30–40% for theHuber loss. It is worth noting that theHuber loss was employed for the 5m_vs_6m, 8m_vs_9m, and 3s_vs_3z environments, where it achieved better average results compared to the L2 loss. For the remaining environments, the L2 loss demonstrated superior performance. Therefore, we conclude that the choice of loss function for diffuser training depends on the specific environment setting. 
Figure 27: Effect of Huber Diffuser’s Loss on the 3s_vs_5z Scenario 
70
Figure 28: Effect of L2 Diffuser’s Loss on the 3s_vs_5z Scenario 
Although L2 loss is more sensitive to outliers than Huber loss, it outperforms it in the aforementioned environments. This can be attributed to the stronger corrective gradients of L2 loss for large prediction errors, which enable a more accurate modeling of hidden states and observations of the teammates. 
71
4.4.6 Impact of exploration on the performance of Q-Diffuser 
As established in prior work, QMIX is unable to solve this scenario through simple parameter tuning, regardless of the number of training steps. Consequently, we applied several modifications to enhance the QMIX backbone: using a parallel episode runner with 8 parallel environments (compared to 4), and replacing the RMSProp optimizer with Adam. The Diffuser component retained the Adam optimizer in this experiment. Additionally, we extended the epsilon annealing time from 50,000 to 1 million steps and increased the total observed environment time elapsed to 8 million. 
With these changes, we observed that both algorithms approached near-optimal performance around 6.5 million steps. Although Q-Diffuser exhibited an earlier performance spike and generally maintained higher win rates, it experienced a significant drop in performance around 6.2 million steps. This instability renders the approach unreliable and unsuitable for the Corridor Scenario in SMAC. Overall, the performance gains for QMIX remainmarginal. Nonetheless, this experiment highlights how implementationlevel parameter adjustments can significantly influence results [23] 
Figure 29: Effect of exploration (epsilon annealing) 
72
5 Conclusions and Further Discussion 
This thesis was motivated by the lack of Multi-Agent Reinforcement Learning (MARL) approaches grounded in diffusionmodels, as identified in the existing literature. While prior work by Xu et al. [81] presented a diffusion-based MARL method, it was limited in several ways: it was applicable only to image-based environments—an uncommon setting in MARL benchmarks [55, 52]—and involved a complex and unintuitive architecture that underperformed against standard baselines in tasks such as image-based SMAC [63]. 
To address these issues, this thesis presented a method, called Q-Diffuser, which combined the QMIX algorithm [60] with Denoising Diffusion Probabilistic Models [18] within the frameworks of Centralized Training with Decentralized Execution (CTDE) and AgentModeling (AM). The key idea behindQ-Diffuser was to augment each agent’s Q-value estimation with an additional term,Qbias, which captured the contextual influence of other agents. Through a diffusion model, each agent was able to model the hidden states and observations of its teammates, conditioned on its own observations. This design enabled agents to develop internal beliefs about what their teammates perceived and intended, thus improving coordination. 
Although QMIX originally used recurrent neural networks (RNNs) for agent modeling, Q-Diffuser extended this with more expressive representations and an attention mechanism that weighted the relevance of each teammate’s predicted behavior. As a result, agents were able to make decisions based on both their own observations and the inferred beliefs and intentions of other agents, leading to more informed and cooperative strategies. 
The experimental evaluation demonstrated that Q-Diffuser outperformedQMIX across multiple establishedMARL benchmarks, including theHard and Super-Hard scenarios of the StarCraft Multi-Agent Challenge (SMAC) [76]. The results confirmed that diffusionmodels can be effectively used as an agent modeling component inMARL, without the need for overly complex architectural designs such as those proposed in [81]. 
An extensive ablation studywas conducted, offering insights into various design choices and hyperparameters, such as batch size, reconstruction loss, and the use of parallel training environments. These findings contribute to a deeper understanding of the practical aspects of deploying diffusion-based agent modeling in MARL systems. 
Introducing the diffusion-based Qbias yielded a 5–30% improvement in win rate over vanilla QMIX and in hard scenarios, validating that sampling diverse context embeddings captures coordination modes that an RNN with MLP cannot. When trained online, the Q-Diffuser hybrid converged approximately 20 % faster in terms of environ-
73
ment timesteps and exhibited lower variance in episode returns than a standalone vanilla QMIX, demonstrating that backbone integration is essential for stable learning. Ab-lating the attention mechanism degraded performance by on average, confirming that weighting RNN hidden states by predicted teammate behaviors materially enhances decision relevance. Since the DDPM’s role was to model agents using their local views, the observed performance improvement can be attributed to its generation of novel, more informative observations that anticipate future game states. This enhanced jointobservation synthesis, as evidencedby superior results overQMIX, led to stronger strategies in SMAC, thereby mitigating the partial-observability and non-stationarity challenges inherent in this online MARL setting. 
As a future work, we aim to further enrich Q-Diffuser, in order to better weight the impact of the inferred Q-values, dubbed Qbias, in the total estimation of the action-value function and be able to learn an even better approximation of it. Moreover, our method will be tested on other benchmarks and compared with more baseline methods. An-other promising direction for future work is the incorporation of more advanced diffusion models, which may enhance both the runtime efficiency and the quality of the generated samples. Score-based generative models can potentially assist in identifying salient components of observations by leveraging the learned gradients of the data distribution, thus focusing attention on the most informative features during learning and generation. Another viable research trajectory is to refine the attentionmechanism so that each agent can attend to distinct aspects of the joint state, such as enemy positions or global objectives, instead of relying solely on raw observations. In addition, enriching each agent’s input with auxiliary information (e.g., predicted opponent actions, resource maps, or latent variables from a world model) could further improve the quality of representation and downstream performance. Lastly, the adoption of a custom loss function guided by the reward signal, rather than relying solely on the standard L2 loss currently used in the diffusionmodel, could lead to improved performance by more directly aligning the learning process with task-specific objectives. 
74
6 Appendix 
6.1 Installation instructions 
To install the project dependencies, first clone this repository and then run: 
pip install -r requirements.txt apt update apt install build-essential gcc python3-dev -y sudo apt-get update && sudo apt-get install unzip -y pip install --upgrade sacred pip install --no-build-isolation --no-cache-dir 'PyYAML>=6.0' 
Table 3: Installation Commands 
Depending on your GPU version, you may need to install a different version of the Py-Torch packages. In that case, run the following commands in your terminal to uninstall the existing versions and install a GPU-compatible one: 
pip uninstall torch torchvision torchaudio -y pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118 
Table 4: Reinstall PyTorch packages for GPU compatibility 
Replace the versions above with the ones supported by your specific GPU and CUDA setup, if necessary. 
To install smac environment, simply run in command line: 
./install_sc2.sh unzip -P iagreetotheeula SC2.4.10.zip pip install lbforaging rware pettingzoo python3 src/main.py --config=TM_qmix --env-config=sc2 
Table 5: Install smac and more environments 
The code was heavily based on a GitHub repository. 1 
1The code implementation was based on https://github.com/zhjie/Diffusion_MARL_main. 
75
6.2 QMIX and Q-Diffuser Configuration files 
Name Description Value action_selector use epsilon greedy action selector ”epsilon_greedy” epsilon_start 1.0 epsilon_finish 0.05 epsilon_anneal_time 50000 buffer_size 5000 target_update_interval update the target network every {} episodes 200 agent_output_type use the Q_Learner to train ”q” learner ”q_learner” double_q True mixer ”qmix” mixing_embed_dim 32 hypernet_layers 2 hypernet_embed 64 batch_size 32 t_max Stop running after this many timesteps 2500000 runner ”episode” obs_agent_id True obs_last_action False obs_individual_obs False standardise_returns use the Q_Learner to train False standardise_rewards True seed 337663438 name ”qmix” 
Table 6: QMIX configuration file 
76
Name Description Value action_selector use epsilon greedy action selector ”epsilon_greedy” epsilon_start 1.0 epsilon_finish 0.05 epsilon_anneal_time 50000 or 1000000 evaluation_epsilon 0.0 runner ”episode” t_max 2500000 buffer_size 5000 target_update_interval update the target network every {} episodes 200 obs_agent_id True obs_last_action False obs_individual_obs False use_rnn True standardise_returns use the Q_Learner to train False standardise_rewards True agent_output_type ”q” double_q True mac ”tm_mac” learner ”teammate_learner” agent ”TM_agent” mixer ”qmix” mixing_embed_dim 32 hypernet_layers 2 hypernet_embed 64 timesteps diffusion timesteps 1 denoise_batch_size 32 attention_hidden_size 64 attention_hidden_dim 32 Unet_lr 0.0001 batch_size 32 lr rl learning rate 0.0005 lr_decre_step 3000 lr_decre_gamma 0.999 seed 337663438 save_model False name ”TM_qmix” 
Table 7: Q-Diffuser configuration file 
77
6.3 Hardware and versions 
The expected runtime is approximately 4 to 24 hours for the Q-Diffuser program and 2 to 8 hours for the QMIX program, based on the hardware configuration listed below. 
Component Specification GPU NVIDIA A4000 CPU Intel i9-14900K SMAC Version 2.4.10 MARL Environment PyMARL Python version 3.xx 
Table 8: System Configuration and SMAC Version 
78
References 
[1] Alekh Agarwal et al. “Reinforcement learning: Theory and algorithms”. In: CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep 32 (2019). 
[2] Stefano V Albrecht, Filippos Christianos, and Lukas Schäfer. Multi-agent reinforcement learning: Foundations and modern approaches. MIT Press, 2024. 
[3] Stefano V Albrecht and Peter Stone. “Reasoning about Hypothetical Agent Be-haviours and their Parameters”. In: Proceedings of the 16th Conference on Au-tonomous Agents and MultiAgent Systems. 2017, pp. 547–555. 
[4] Stefano V. Albrecht, Filippos Christianos, and Lukas Schäfer.Multi-Agent Rein-forcement Learning: Foundations and Modern Approaches. MIT Press, 2023. URL: https://www.marl-book.com. 
[5] Marcin Andrychowicz et al. “Hindsight experience replay”. In: Advances in neural information processing systems 30 (2017). 
[6] Raphaël Avalos et al. “Local advantage networks for multi-agent reinforcement learning in dec-pomdps”. In:Transactions onMachineLearningResearch (2023). 
[7] Evangelos Axiotis et al. “A Personalized Machine-Learning-Enabled Method for Efficient Research in Ethnopharmacology. The Case of the SouthernBalkans and the Coastal Zone of Asia Minor”. In: Applied Sciences 11.13 (2021), p. 5826. 
[8] Claudine Badue et al. “Self-driving cars: A survey”. In: Expert systems with applications 165 (2021), p. 113816. 
[9] Yuhui Chen, Haoran Li, and Dongbin Zhao. “Boosting continuous control with consistency policy”. In: arXiv preprint arXiv:2310.06343 (2023). 
[10] Xiaoyi Dong, Jian Cheng, and Xi Sheryl Zhang. “Maximum entropy reinforcement learningwith diffusionpolicy”. In:arXivpreprint arXiv:2502.11612 (2025). 
[11] Jakob Foerster et al. “Counterfactual multi-agent policy gradients”. In: Proceed-ings of the AAAI conference on artificial intelligence. Vol. 32. 1. 2018. 
[12] Haobo Fu et al. “Greedy when sure and conservative when uncertain about the opponents”. In: International Conference on Machine Learning. PMLR. 2022, pp. 6829–6848. 
[13] Github: Code for ”Diffusion Models for Multi-Agent Reinforcement Learning”. https://github.com/zhjie/Diffusion_MARL_main. Accessed: 2025-07-14. 2023. 
[14] Hafsa Habehh and Suril Gohel. “Machine learning in healthcare”. In: Current genomics 22.4 (2021), pp. 291–300. 
79
[15] Matthew Hausknecht and Peter Stone. “Deep recurrent q-learning for partially observable mdps”. In: 2015 aaai fall symposium series. 2015. 
[16] Xiangnan He. The Reparameterization Trick: Unlocking Backpropagation in VAEs. https://medium.com/@hexiangnan/the-reparameterization-trick-unlocking-backpropagation-in-vaes-63917855074b. Accessed: 2025-06-20. 2023. 
[17] Pablo Hernandez-Leal, Bilal Kartal, and Matthew E Taylor. “Agent modeling as auxiliary task for deep reinforcement learning”. In:Proceedings of the AAAI conference on artificial intelligence and interactive digital entertainment. Vol. 15. 1. 2019, pp. 31–37. 
[18] Jonathan Ho, Ajay Jain, and Pieter Abbeel. “Denoising diffusion probabilistic models”. In: Advances in neural information processing systems 33 (2020), pp. 6840–6851. 
[19] Jonathan Ho, Ajay Jain, and Pieter Abbeel. “Denoising diffusion probabilistic models”. In: Advances in neural information processing systems 33 (2020), pp. 6840–6851. 
[20] Ronald A Howard. “Dynamic programming and markov processes.” In: (1960). 
[21] HengyuanHu and JakobNFoerster. “Simplified ActionDecoder for DeepMulti-AgentReinforcement Learning”. In: International Conference onLearningRepresentations. 2019. 
[22] Hengyuan Hu et al. “Off-belief learning”. In: International Conference on Ma-chine Learning. PMLR. 2021, pp. 4369–4379. 
[23] Jian Hu et al. “Rethinking the Implementation Tricks and Monotonicity Con-straint in CooperativeMulti-agent Reinforcement Learning”. In: ICLRBlogposts 2023. https://iclr-blogposts.github.io/2023/blog/2023/riit/. 2023.URL: https: //iclr-blogposts.github.io/2023/blog/2023/riit/. 
[24] Siyi Hu et al. “Marllib: A scalable and efficient multi-agent reinforcement learning library”. In: Journal of Machine Learning Research 24.315 (2023), pp. 1– 23. 
[25] Michael Janner et al. “Planning with Diffusion for Flexible Behavior Synthesis”. In: International Conference on Machine Learning. PMLR. 2022, pp. 9902– 9915. 
[26] Jiechuan Jiang and Zongqing Lu. “The emergence of individuality”. In: Interna-tional Conference on Machine Learning. PMLR. 2021, pp. 4992–5001. 
[27] Yonghyeon Jo et al. “FoX: Formation-aware exploration in multi-agent reinforcement learning”. In: Proceedings of the AAAI Conference on Artificial In-telligence. Vol. 38. 12. 2024, pp. 12985–12994. 
80
[28] Diederik PKingmaandMaxWelling. “Auto-encoding variational bayes”. In:arXiv preprint arXiv:1312.6114 (2013). 
[29] AndreasKontogiannis andKonstantinosPapathanasiou. “Count-basedAgentMod-elling in Multi-Agent Reinforcement Learning”. In: (2023). 
[30] Andreas Kontogiannis andGeorge A Vouros. “Inherently Interpretable Deep Re-inforcement Learning Through OnlineMimicking”. In: InternationalWorkshop on Explainable, Transparent Autonomous Agents and Multi-Agent Systems. Springer. 2023, pp. 160–179. 
[31] AndreasKontogiannis et al. “EnhancingCooperativeMulti-AgentReinforcement Learning with State Modelling and Adversarial Exploration”. In: arXiv preprint arXiv:2505.05262 (2025). 
[32] Andreas Kontogiannis et al. “Tree-based focused web crawling with reinforcement learning”. In: arXiv preprint arXiv:2112.07620 (2021). 
[33] L. Kraemer and B. Banerjee. “Multi-agent reinforcement learning as a rehearsal for decentralized planning”. In: Neurocomputing 190 (2016), pp. 82–94. 
[34] Theocharis Kravaris et al. “Explaining deep reinforcement learning decisions in complex multiagent settings: towards enabling automation in air traffic flow management”. In: Applied Intelligence 53.4 (2023), pp. 4063–4098. 
[35] Chenghao Li et al. “Celebrating diversity in shared multi-agent reinforcement learning”. In: Advances in Neural Information Processing Systems 34 (2021), pp. 3991–4002. 
[36] Jiahui Li et al. “Two Heads are Better Than One: A Simple Exploration Frame-work forEfficientMulti-AgentReinforcement Learning”. In:Advances inNeural Information Processing Systems 36 (2024). 
[37] Liquipedia Contributors. Colossus (Legacy of the Void). Accessed: 2025-07-08. Liquipedia. 2025. URL: https : / / liquipedia . net / starcraft2 / Colossus _ (Legacy_of_the_Void). 
[38] Liquipedia Contributors. Zealot (Legacy of the Void). Accessed: 2025-07-09. n.d. URL: https://liquipedia.net/starcraft2/Zealot_(Legacy_of_the_ Void). 
[39] Boyin Liu et al. “Lazy agents: A new perspective on solving sparse reward problem in multi-agent reinforcement learning”. In: International Conference on Machine Learning. PMLR. 2023, pp. 21937–21950. 
[40] Ryan Lowe et al. “Multi-agent actor-critic for mixed cooperative-competitive environments”. In:Advances in neural information processing systems 30 (2017). 
[41] Calvin Luo. “Understanding diffusion models: A unified perspective”. In: arXiv preprint arXiv:2208.11970 (2022). 
81
[42] Mingwei Ma et al. “Learning intuitive policies using action features”. In: Inter-national Conference on Machine Learning. PMLR. 2023, pp. 23358–23372. 
[43] Xiaoteng Ma et al. “Modeling the Interaction between Agents in Cooperative Multi-AgentReinforcement Learning”. In:Proceedings of the 20th International Conference on Autonomous Agents and MultiAgent Systems. 2021, pp. 853– 861. 
[44] Thomas Melistas et al. “Benchmarking counterfactual image generation”. In: Advances in Neural Information Processing Systems 37 (2024), pp. 133207– 133230. 
[45] Pol Moreno et al. “Neural recursive belief states in multi-agent reinforcement learning”. In: arXiv preprint arXiv:2102.02274 (2021). 
[46] Andrew Y Ng, Daishi Harada, and Stuart Russell. “Policy invariance under reward transformations: Theory and application to reward shaping”. In: Icml. Vol. 99. Citeseer. 1999, pp. 278–287. 
[47] Dung Nguyen et al. “Social Motivation for Modelling Other Agents under Partial Observability in Decentralised Training”. In: Proceedings of the Thirty-Second International Joint Conference onArtificial Intelligence, IJCAI-23. Ed. by Edith Elkind. Main Track. International Joint Conferences on Artificial Intelligence Organization, Aug. 2023, pp. 4082–4090. DOI: 10.24963/ijcai.2023/454. URL: https://doi.org/10.24963/ijcai.2023/454. 
[48] Dung Nguyen et al. “Theory of mind with guilt aversion facilitates cooperative reinforcement learning”. In: Asian Conference on Machine Learning. PMLR. 2020, pp. 33–48. 
[49] nirhso.ADetailed Explanation of the PathingGrid in SMAC. Zhihu Column. Ac-cessed: 2025-07-09. 2025. URL: https://zhuanlan.zhihu.com/p/543542116. 
[50] Frans AOliehoek, Christopher Amato, et al.A concise introduction to decentralized POMDPs. Vol. 1. Springer, 2016. 
[51] James Orr and Ayan Dutta. “Multi-agent deep reinforcement learning for multirobot applications: A survey”. In: Sensors 23.7 (2023), p. 3625. 
[52] George Papadopoulos et al. “An Extended Benchmarking of Multi-Agent Rein-forcement Learning Algorithms in Complex Fully Cooperative Tasks”. In: arXiv preprint arXiv:2502.04773 (2025). 
[53] Georgios Papoudakis and Stefano V Albrecht. “Variational Autoencoders for Op-ponent Modeling in Multi-Agent Systems”. In: AAAI 2020 Workshop on Rein-forcement Learning in Games. 2020. 
82
[54] Georgios Papoudakis, Filippos Christianos, and Stefano Albrecht. “Agent modelling under partial observability for deep reinforcement learning”. In:Advances in Neural Information Processing Systems 34 (2021), pp. 19210–19222. 
[55] Georgios Papoudakis et al. “Benchmarkingmulti-agent deep reinforcement learning algorithms in cooperative tasks”. In:arXivpreprint arXiv:2006.07869 (2020). 
[56] Vasilis Pollatos, Loukas Kouvaras, and Eleni Charou. “Land cover semantic segmentation using ResUNet”. In: arXiv preprint arXiv:2010.06285 (2020). 
[57] Vasilis Pollatos,DebmalyaMandal, andGoranRadanovic. “On corruption-robustness in performative reinforcement learning”. In: Proceedings of the AAAI Confer-ence on Artificial Intelligence. Vol. 39. 19. 2025, pp. 19939–19947. 
[58] Liang Qifan et al. “Reconstruction-Guided Policy: Enhancing Decision-Making through Agent-Wise State Consistency”. In: The Thirteenth International Con-ference on Learning Representations. 
[59] GuannanQu et al. “ScalableMulti-AgentReinforcement Learning forNetworked Systems with Average Reward”. In: (). 
[60] TabishRashid et al. “Monotonic value function factorisation for deepmulti-agent reinforcement learning”. In: The Journal of Machine Learning Research 21.1 (2020), pp. 7234–7284. 
[61] Jason Rennie, Andrew Kachites McCallum, et al. “Using reinforcement learning to spider the web efficiently”. In: ICML. Vol. 99. 1999, pp. 335–343. 
[62] Marc Rigter, Jun Yamada, and Ingmar Posner. “World models via policy-guided trajectory diffusion”. In: arXiv preprint arXiv:2312.08533 (2023). 
[63] Mikayel Samvelyan et al. “The starcraftmulti-agent challenge”. In:arXivpreprint arXiv:1902.04043 (2019). 
[64] John Schulman et al. “Trust region policy optimization”. In: International conference on machine learning. PMLR. 2015, pp. 1889–1897. 
[65] Wenling Shang et al. “Agent-centric representations for multi-agent reinforcement learning”. In: arXiv preprint arXiv:2104.09402 (2021). 
[66] Junjie Sheng et al. “Learning structured communication for multi-agent reinforcement learning”. In:AutonomousAgents andMulti-Agent Systems36.2 (2022), p. 50. 
[67] Kyunghwan Son et al. “Qtran: Learning to factorize with transformation for cooperative multi-agent reinforcement learning”. In: International conference on machine learning. PMLR. 2019, pp. 5887–5896. 
[68] Nikos Spyrou et al. “Causally Steered Diffusion for Automated Video Counter-factual Generation”. In: arXiv preprint arXiv:2506.14404 (2025). 
83
[69] Sinarwati Mohamad Suhaili, Naomie Salim, andMohamad Nazim Jambli. “Ser-vice chatbots: A systematic review”. In: Expert Systems with Applications 184 (2021), p. 115461. 
[70] Jing Sun et al. “Decision-MakingWith Speculative Opponent Models”. In: IEEE Transactions on Neural Networks and Learning Systems (2024). 
[71] Peter Sunehag et al. “Value-Decomposition Networks For Cooperative Multi-Agent Learning Based On Team Reward”. In: Proceedings of the 17th Interna-tional Conference onAutonomousAgents andMultiAgent Systems. 2018, pp. 2085– 2087. 
[72] SiyangTan andBinqiangChen. “AttentionalOpponentModelling forMulti-agent Cooperation”. In:2023 International Joint Conference onNeuralNetworks (IJCNN). IEEE. 2023, pp. 1–9. 
[73] Haoran Tang et al. “# exploration: A study of count-based exploration for deep reinforcement learning”. In: Advances in neural information processing systems 30 (2017). 
[74] Muhammad Tsohail. SMAC lite: A lightweight SMAC based environment for Multi Agent Reinforcement Learning. Master’s thesis. Accessed: 2025-07-09. Agents Lab, University of Oxford, 2022. URL: https://agents-lab.org/blog/ master-dissertations/tsohail_msc2022.pdf. 
[75] Ashish Vaswani et al. “Attention is all you need”. In: Advances in neural information processing systems 30 (2017). 
[76] Oriol Vinyals et al. “Starcraft ii: A new challenge for reinforcement learning”. In: arXiv preprint arXiv:1708.04782 (2017). 
[77] Sizhe Wang et al. “SADMA: Scalable Asynchronous Distributed Multi-agent Re-inforcement LearningTrainingFramework”. In: InternationalWorkshop onEngineering Multi-Agent Systems. Springer. 2024, pp. 64–81. 
[78] Muning Wen et al. “Multi-agent reinforcement learning is a sequence modeling problem”. In: Advances in Neural Information Processing Systems 35 (2022), pp. 16509–16521. 
[79] Annie Wong et al. “Deep multiagent reinforcement learning: Challenges and directions”. In: Artificial Intelligence Review 56.6 (2023), pp. 5023–5056. 
[80] MichaelWooldridge.An introduction tomultiagent systems. John wiley & sons, 2009. 
[81] Zhiwei Xu et al. “Beyond Local Views: Global State Inference with Diffusion Models for CooperativeMulti-AgentReinforcement Learning”. In:CoRR (2024). 
[82] Long Yang et al. “Policy representation via diffusion probability model for reinforcement learning”. In: arXiv preprint arXiv:2305.13122 (2023). 
84
[83] Yaodong Yang et al. “Transformer-based working memory for multiagent reinforcement learning with action parsing”. In: Advances in Neural Information Processing Systems 35 (2022), pp. 34874–34886. 
[84] Lei Yuan et al. “Multi-agent incentive communication via decentralized teammate modeling”. In: Proceedings of the AAAI Conference on Artificial Intelli-gence. Vol. 36. 9. 2022, pp. 9466–9474. 
[85] Yunpeng Zhai et al. “Dynamic Belief for Decentralized Multi-Agent Cooperative Learning”. In: Proceedings of International Joint Conference on Artificial In-telligence. 2023, pp. 344–352. 
[86] Qingpeng Zhao et al. “Boosting Value Decomposition via Unit-Wise Attentive State Representation for CooperativeMulti-Agent Reinforcement Learning”. In: arXiv preprint arXiv:2305.07182 (2023). 
[87] Qingpeng Zhao et al. “Boosting Value Decomposition via Unit-Wise Attentive State Representation for CooperativeMulti-Agent Reinforcement Learning”. In: arXiv preprint arXiv:2305.07182 (2023). 
[88] Xutong Zhao et al. “Conditionally optimistic exploration for cooperative deep multi-agent reinforcement learning”. In: Proceedings of the Thirty-Ninth Con-ference on Uncertainty in Artificial Intelligence. UAI ’23. Pittsburgh, PA, USA: JMLR.org, 2023. 
[89] Lulu Zheng et al. “Episodic multi-agent reinforcement learning with curiosity-driven exploration”. In: Advances in Neural Information Processing Systems 34 (2021), pp. 3757–3769. 
[90] Zhengbang Zhu et al. “Madiff: Offline multi-agent learning with diffusion models”. In:Advances inNeural InformationProcessingSystems37 (2024), pp. 4177– 4206. 
[91] Luisa Zintgraf et al. “Deep interactive bayesian reinforcement learning via metalearning”. In: arXiv preprint arXiv:2101.03864 (2021). 
85