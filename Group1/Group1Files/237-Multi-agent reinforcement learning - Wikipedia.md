> Source: https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning

Jump to contentMain menu    Navigation 
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
 Contribute 
Help
Learn to edit
Community portal
Recent changes
Upload file
Special pages
Search  Donate
Create account
Log in
Donate
Create account
Log in
(Top)  
1   Definition  
2   Cooperation vs. competition  2.1   Pure competition settings  
2.2   Pure cooperation settings  
2.3   Mixed-sum settings  
3   Social dilemmas  3.1   Sequential social dilemmas  
4   Autocurricula  
5   Applications  5.1   AI alignment  
6   Limitations  
7   Further reading  
8   References  
Multi-agent reinforcement learning
Català
Español
فارسی
עברית
Українська
Edit links
Tools    Actions 
Read
Edit
View history
 General 
What links here
Related changes
Upload file
Permanent link
Page information
Cite this page
Get shortened URL
Download QR code
 Print/export 
Download as PDF
Printable version
 In other projects 
Wikidata item
From Wikipedia, the free encyclopedia   Sub-field of reinforcement learning   Part of a series onMachine learningand data miningParadigms  
Supervised learning
Unsupervised learning
Semi-supervised learning
Self-supervised learning
Reinforcement learning
Meta-learning
Online learning
Batch learning
Curriculum learning
Rule-based learning
Neuro-symbolic AI
Neuromorphic engineering
Quantum machine learning
Problems  
Classification
Generative modeling
Regression
Clustering
Dimensionality reduction
Density estimation
Anomaly detection
Data cleaning
AutoML
Association rules
Semantic analysis
Structured prediction
Feature engineering
Feature learning
Learning to rank
Grammar induction
Ontology learning
Multimodal learning
Supervised learning(classification • regression)  
Apprenticeship learning
Decision trees
EnsemblesBagging
Boosting
Random forest
k-NN
Linear regression
Naive Bayes
Artificial neural networks
Logistic regression
Perceptron
Relevance vector machine (RVM)
Support vector machine (SVM)
ClusteringBIRCH
CURE
Hierarchical
k-means
Fuzzy
Expectation–maximization (EM)
DBSCAN
OPTICS
Mean shift
Dimensionality reductionFactor analysis
CCA
ICA
LDA
NMF
PCA
PGD
t-SNE
SDL
Structured predictionGraphical modelsBayes net
Conditional random field
Hidden Markov
Anomaly detectionRANSAC
k-NN
Local outlier factor
Isolation forest
Neural networksAutoencoder
Deep learning
Feedforward neural network
Recurrent neural networkLSTM
GRU
ESN
reservoir computing
Boltzmann machineRestricted
GAN
Diffusion model
SOM
Convolutional neural networkU-Net
LeNet
AlexNet
DeepDream
Neural fieldNeural radiance field
Physics-informed neural networks
TransformerVision
Mamba
Spiking neural network
Memtransistor
Electrochemical RAM (ECRAM)
Reinforcement learningQ-learning
Policy gradient
SARSA
Temporal difference (TD)
Multi-agentSelf-play
Learning with humans  
Active learning
Crowdsourcing
Human-in-the-loop
Mechanistic interpretability
RLHF
Model diagnostics  
Coefficient of determination
Confusion matrix
Learning curve
ROC curve
Mathematical foundations  
Kernel machines
Bias–variance tradeoff
Computational learning theory
Empirical risk minimization
Occam learning
PAC learning
Statistical learning
VC theory
Topological deep learning
Journals and conferences  
AAAI
ECML PKDD
NeurIPS
ICML
ICLR
IJCAI
ML
JMLR
Related articles  
Glossary of artificial intelligence
List of datasets for machine-learning researchList of datasets in computer vision and image processing
Outline of machine learning
v
t
e
Two rival teams of agents face off in a MARL experimentMulti-agent reinforcement learning (MARL) is a sub-field of reinforcement learning. It focuses on studying the behavior of multiple learning agents that coexist in a shared environment.[ 1 ] Each agent is motivated by its own rewards, and does actions to advance its own interests; in some environments these interests are opposed to the interests of other agents, resulting in complex group dynamics. 
Multi-agent reinforcement learning is closely related to game theory and especially repeated games, as well as multi-agent systems. Its study combines the pursuit of finding ideal algorithms that maximize rewards with a more sociological set of concepts. While research in single-agent reinforcement learning is concerned with finding the algorithm that gets the biggest number of points for one agent, research in multi-agent reinforcement learning evaluates and quantifies social metrics, such as cooperation,[ 2 ] reciprocity,[ 3 ] equity,[ 4 ] social influence,[ 5 ] language[ 6 ] and discrimination.[ 7 ]
Definition
[edit]  
Similarly to single-agent reinforcement learning, multi-agent reinforcement learning is modeled as some form of a Markov decision process (MDP). Fix a set of agents  I   =   {   1   ,   .   .   .   ,   N   }   {\displaystyle I=\{1,...,N\}}   . We then define: 
A set  S   {\displaystyle S}    of environment states.
One set  A   i   {\displaystyle {\mathcal {A}}_{i}}    of actions for each of the agents  i   ∈   I   =   {   1   ,   …   ,   N   }   {\displaystyle i\in I=\{1,\dots ,N\}}   .
P   a   →   (   s   ,   s   ′   )   =   Pr   (   s   t   +   1   =   s   ′   ∣   s   t   =   s   ,   a   →   t   =   a   →   )   {\displaystyle P_{\vec {a}}(s,s')=\Pr(s_{t+1}=s'\mid s_{t}=s,{\vec {a}}_{t}={\vec {a}})}    is the probability of transition (at time  t   {\displaystyle t}   ) from state  s   {\displaystyle s}    to state  s   ′   {\displaystyle s'}    under joint action  a   →   {\displaystyle {\vec {a}}}   .
R   →   a   →   (   s   ,   s   ′   )   {\displaystyle {\vec {R}}_{\vec {a}}(s,s')}    is the immediate joint reward after the transition from  s   {\displaystyle s}    to  s   ′   {\displaystyle s'}    with joint action  a   →   {\displaystyle {\vec {a}}}   .
In settings with perfect information, such as the games of chess and Go, the MDP would be fully observable. In settings with imperfect information, especially in real-world applications like self-driving cars, each agent would access an observation that only has part of the information about the current state. In the partially observable setting, the core model is the partially observable stochastic game in the general case, and the decentralized POMDP in the cooperative case. 
Cooperation vs. competition
[edit]  
When multiple agents are acting in a shared environment their interests might be aligned or misaligned. MARL allows exploring all the different alignments and how they affect the agents' behavior: 
In pure competition settings, the agents' rewards are exactly opposite to each other, and therefore they are playing against each other.
Pure cooperation settings are the other extreme, in which agents get the exact same rewards, and therefore they are playing with each other.
Mixed-sum settings cover all the games that combine elements of both cooperation and competition.
Pure competition settings
[edit]  
When two agents are playing a zero-sum game, they are in pure competition with each other. Many traditional games such as chess and Go fall under this category, as do two-player variants of video games like StarCraft. Because each agent can only win at the expense of the other agent, many complexities are stripped away. There is no prospect of communication or social dilemmas, as neither agent is incentivized to take actions that benefit its opponent. 
The Deep Blue[ 8 ] and AlphaGo projects demonstrate how to optimize the performance of agents in pure competition settings. 
One complexity that is not stripped away in pure competition settings is autocurricula. As the agents' policy is improved using self-play, multiple layers of learning may occur. 
Pure cooperation settings
[edit]  
MARL is used to explore how separate agents with identical interests can communicate and work together. Pure cooperation settings are explored in recreational cooperative games such as Overcooked,[ 9 ] as well as real-world scenarios in robotics.[ 10 ]
In pure cooperation settings all the agents get identical rewards, which means that social dilemmas do not occur. 
In pure cooperation settings, oftentimes there are an arbitrary number of coordination strategies, and agents converge to specific "conventions" when coordinating with each other. The notion of conventions has been studied in language[ 11 ] and also alluded to in more general multi-agent collaborative tasks.[ 12 ][ 13 ][ 14 ][ 15 ]
Mixed-sum settings
[edit]  In this mixed sum setting, each of the four agents is trying to reach a different goal. Each agent's success depends on the other agents clearing its way, even though they are not directly incentivized to assist each other.[ 16 ]Most real-world scenarios involving multiple agents have elements of both cooperation and competition. For example, when multiple self-driving cars are planning their respective paths, each of them has interests that are diverging but not exclusive: Each car is minimizing the amount of time it's taking to reach its destination, but all cars have the shared interest of avoiding a traffic collision.[ 17 ]
Zero-sum settings with three or more agents often exhibit similar properties to mixed-sum settings, since each pair of agents might have a non-zero utility sum between them. 
Mixed-sum settings can be explored using classic matrix games such as prisoner's dilemma, more complex sequential social dilemmas, and recreational games such as Among Us,[ 18 ]Diplomacy[ 19 ] and StarCraft II.[ 20 ][ 21 ]
Mixed-sum settings can give rise to communication and social dilemmas. 
Social dilemmas
[edit]  
As in game theory, much of the research in MARL revolves around social dilemmas, such as prisoner's dilemma,[ 22 ]chicken and stag hunt.[ 23 ]
While game theory research might focus on Nash equilibria and what an ideal policy for an agent would be, MARL research focuses on how the agents would learn these ideal policies using a trial-and-error process. The reinforcement learning algorithms that are used to train the agents are maximizing the agent's own reward; the conflict between the needs of the agents and the needs of the group is a subject of active research.[ 24 ]
Various techniques have been explored in order to induce cooperation in agents: Modifying the environment rules,[ 25 ] adding intrinsic rewards,[ 4 ] and more. 
Sequential social dilemmas
[edit]  
Social dilemmas like prisoner's dilemma, chicken and stag hunt are "matrix games". Each agent takes only one action from a choice of two possible actions, and a simple 2x2 matrix is used to describe the reward that each agent will get, given the actions that each agent took. 
In humans and other living creatures, social dilemmas tend to be more complex. Agents take multiple actions over time, and the distinction between cooperating and defecting is not as clear cut as in matrix games. The concept of a sequential social dilemma (SSD) was introduced in 2017[ 26 ] as an attempt to model that complexity. There is ongoing research into defining different kinds of SSDs and showing cooperative behavior in the agents that act in them.[ 27 ]
Autocurricula
[edit]  
An autocurriculum[ 28 ] (plural: autocurricula) is a reinforcement learning concept that's salient in multi-agent experiments. As agents improve their performance, they change their environment; this change in the environment affects themselves and the other agents. The feedback loop results in several distinct phases of learning, each depending on the previous one. The stacked layers of learning are called an autocurriculum. Autocurricula are especially apparent in adversarial settings,[ 29 ] where each group of agents is racing to counter the current strategy of the opposing group. 
The Hide and Seek game is an accessible example of an autocurriculum occurring in an adversarial setting. In this experiment, a team of seekers is competing against a team of hiders. Whenever one of the teams learns a new strategy, the opposing team adapts its strategy to give the best possible counter. When the hiders learn to use boxes to build a shelter, the seekers respond by learning to use a ramp to break into that shelter. The hiders respond by locking the ramps, making them unavailable for the seekers to use. The seekers then respond by "box surfing", exploiting a glitch in the game to penetrate the shelter. Each "level" of learning is an emergent phenomenon, with the previous level as its premise. This results in a stack of behaviors, each dependent on its predecessor. 
Autocurricula in reinforcement learning experiments are compared to the stages of the evolution of life on Earth and the development of human culture. A major stage in evolution happened 2-3 billion years ago, when photosynthesizing life forms started to produce massive amounts of oxygen, changing the balance of gases in the atmosphere.[ 30 ] In the next stages of evolution, oxygen-breathing life forms evolved, eventually leading up to land mammals and human beings. These later stages could only happen after the photosynthesis stage made oxygen widely available. Similarly, human culture could not have gone through the Industrial Revolution in the 18th century without the resources and insights gained by the agricultural revolution at around 10,000 BC.[ 31 ]
Applications
[edit]  
Multi-agent reinforcement learning has been applied to a variety of use cases in science and industry: 
Broadbandcellular networks such as 5G[ 32 ]
Content caching[ 32 ]
Packet routing[ 32 ]
Computer vision[ 33 ]
Network security[ 32 ]
Transmit power control[ 32 ]
Computation offloading[ 32 ]
Language evolution research[ 34 ]
Global health[ 35 ]
Integrated circuit design[ 36 ]
Internet of Things[ 32 ]
Microgridenergy management[ 37 ]
Multi-camera control[ 38 ]
Autonomous vehicles[ 39 ]
Sports analytics[ 40 ]
Traffic control[ 41 ] (Ramp metering[ 42 ])
Unmanned aerial vehicles[ 43 ][ 32 ]
Wildlife conservation[ 44 ]
AI alignment
[edit]  
Multi-agent reinforcement learning has been used in research into AI alignment. The relationship between the different agents in a MARL setting can be compared to the relationship between a human and an AI agent. Research efforts in the intersection of these two fields attempt to simulate possible conflicts between a human's intentions and an AI agent's actions, and then explore which variables could be changed to prevent these conflicts.[ 45 ][ 46 ]
Limitations
[edit]  
There are some inherent difficulties about multi-agent deep reinforcement learning.[ 47 ] The environment is not stationary anymore, thus the Markov property is violated: transitions and rewards do not only depend on the current state of an agent. 
Further reading
[edit]  Scholia has a topic profile for Multi-agent reinforcement learning.  
Stefano V. Albrecht, Filippos Christianos, Lukas Schäfer. Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. MIT Press, 2024. https://www.marl-book.com
Kaiqing Zhang, Zhuoran Yang, Tamer Basar. Multi-agent reinforcement learning: A selective overview of theories and algorithms. Studies in Systems, Decision and Control, Handbook on RL and Control, 2021. [1]
Yang, Yaodong; Wang, Jun (2020). "An Overview of Multi-Agent Reinforcement Learning from Game Theoretical Perspective". arXiv:2011.00583 [cs.MA].
References
[edit]  
^Stefano V. Albrecht, Filippos Christianos, Lukas Schäfer. Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. MIT Press, 2024. https://www.marl-book.com/
^Lowe, Ryan; Wu, Yi (2020). "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments". arXiv:1706.02275v4 [cs.LG].  
^Baker, Bowen (2020). "Emergent Reciprocity and Team Formation from Randomized Uncertain Social Preferences". NeurIPS 2020 proceedings. arXiv:2011.05373.  
^ abHughes, Edward; Leibo, Joel Z.; et al. (2018). "Inequity aversion improves cooperation in intertemporal social dilemmas". NeurIPS 2018 proceedings. arXiv:1803.08884.  
^Jaques, Natasha; Lazaridou, Angeliki; Hughes, Edward; et al. (2019). "Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning". Proceedings of the 35th International Conference on Machine Learning. arXiv:1810.08647.  
^Lazaridou, Angeliki (2017). "Multi-Agent Cooperation and The Emergence of (Natural) Language". ICLR 2017. arXiv:1612.07182.  
^Duéñez-Guzmán, Edgar; et al. (2021). "Statistical discrimination in learning agents". arXiv:2110.11404v1 [cs.LG].  
^Campbell, Murray; Hoane, A. Joseph Jr.; Hsu, Feng-hsiung (2002). "Deep Blue". Artificial Intelligence. 134 ( 1– 2). Elsevier:  57– 83. doi:10.1016/S0004-3702(01)00129-1. ISSN0004-3702.  
^Carroll, Micah; et al. (2019). "On the Utility of Learning about Humans for Human-AI Coordination". arXiv:1910.05789 [cs.LG].  
^Xie, Annie; Losey, Dylan; Tolsma, Ryan; Finn, Chelsea; Sadigh, Dorsa (November 2020). Learning Latent Representations to Influence Multi-Agent Interaction(PDF) . CoRL.  
^Clark, Herbert; Wilkes-Gibbs, Deanna (February 1986). "Referring as a collaborative process". Cognition. 22 (1):  1– 39. doi:10.1016/0010-0277(86)90010-7. PMID3709088. S2CID204981390.  
^Boutilier, Craig (17 March 1996). "Planning, learning and coordination in multiagent decision processes". Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge:  195– 210.  
^Stone, Peter; Kaminka, Gal A.; Kraus, Sarit; Rosenschein, Jeffrey S. (July 2010). Ad Hoc Autonomous Agent Teams: Collaboration without Pre-Coordination. AAAI 11.  
^Foerster, Jakob N.; Song, H. Francis; Hughes, Edward; Burch, Neil; Dunning, Iain; Whiteson, Shimon; Botvinick, Matthew M; Bowling, Michael H. Bayesian action decoder for deep multi-agent reinforcement learning. ICML 2019. arXiv:1811.01458.  
^Shih, Andy; Sawhney, Arjun; Kondic, Jovana; Ermon, Stefano; Sadigh, Dorsa. On the Critical Role of Conventions in Adaptive Human-AI Collaboration. ICLR 2021. arXiv:2104.02871.  
^Bettini, Matteo; Kortvelesy, Ryan; Blumenkamp, Jan; Prorok, Amanda (2022). "VMAS: A Vectorized Multi-Agent Simulator for Collective Robot Learning". The 16th International Symposium on Distributed Autonomous Robotic Systems. Springer. arXiv:2207.03530.  
^Shalev-Shwartz, Shai; Shammah, Shaked; Shashua, Amnon (2016). "Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving". arXiv:1610.03295 [cs.AI].  
^Kopparapu, Kavya; Duéñez-Guzmán, Edgar A.; Matyas, Jayd; Vezhnevets, Alexander Sasha; Agapiou, John P.; McKee, Kevin R.; Everett, Richard; Marecki, Janusz; Leibo, Joel Z.; Graepel, Thore (2022). "Hidden Agenda: a Social Deduction Game with Diverse Learned Equilibria". arXiv:2201.01816 [cs.AI].  
^Bakhtin, Anton; Brown, Noam; et al. (2022). "Human-level play in the game of Diplomacy by combining language models with strategic reasoning". Science. 378 (6624). Springer:  1067– 1074. Bibcode:2022Sci...378.1067M. doi:10.1126/science.ade9097. PMID36413172. S2CID253759631.  
^Samvelyan, Mikayel; Rashid, Tabish; de Witt, Christian Schroeder; Farquhar, Gregory; Nardelli, Nantas; Rudner, Tim G. J.; Hung, Chia-Man; Torr, Philip H. S.; Foerster, Jakob; Whiteson, Shimon (2019). "The StarCraft Multi-Agent Challenge". arXiv:1902.04043 [cs.LG].  
^Ellis, Benjamin; Moalla, Skander; Samvelyan, Mikayel; Sun, Mingfei; Mahajan, Anuj; Foerster, Jakob N.; Whiteson, Shimon (2022). "SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning". arXiv:2212.07489 [cs.LG].  
^Sandholm, Toumas W.; Crites, Robert H. (1996). "Multiagent reinforcement learning in the Iterated Prisoner's Dilemma". Biosystems. 37 ( 1– 2):  147– 166. Bibcode:1996BiSys..37..147S. doi:10.1016/0303-2647(95)01551-5. PMID8924633.  
^Peysakhovich, Alexander; Lerer, Adam (2018). "Prosocial Learning Agents Solve Generalized Stag Hunts Better than Selfish Ones". AAMAS 2018. arXiv:1709.02865.  
^Dafoe, Allan; Hughes, Edward; Bachrach, Yoram; et al. (2020). "Open Problems in Cooperative AI". NeurIPS 2020. arXiv:2012.08630.  
^Köster, Raphael; Hadfield-Menell, Dylan; Hadfield, Gillian K.; Leibo, Joel Z. "Silly rules improve the capacity of agents to learn stable enforcement and compliance behaviors". AAMAS 2020. arXiv:2001.09318.  
^Leibo, Joel Z.; Zambaldi, Vinicius; Lanctot, Marc; Marecki, Janusz; Graepel, Thore (2017). "Multi-agent Reinforcement Learning in Sequential Social Dilemmas". AAMAS 2017. arXiv:1702.03037.  
^Badjatiya, Pinkesh; Sarkar, Mausoom (2020). "Inducing Cooperative behaviour in Sequential-Social dilemmas through Multi-Agent Reinforcement Learning using Status-Quo Loss". arXiv:2001.05458 [cs.AI].  
^Leibo, Joel Z.; Hughes, Edward; et al. (2019). "Autocurricula and the Emergence of Innovation from Social Interaction: A Manifesto for Multi-Agent Intelligence Research". arXiv:1903.00742v2 [cs.AI].  
^Baker, Bowen; et al. (2020). "Emergent Tool Use From Multi-Agent Autocurricula". ICLR 2020. arXiv:1909.07528.  
^Kasting, James F; Siefert, Janet L (2002). "Life and the evolution of earth's atmosphere". Science. 296 (5570):  1066– 1068. Bibcode:2002Sci...296.1066K. doi:10.1126/science.1071184. PMID12004117. S2CID37190778.  
^Clark, Gregory (2008). A farewell to alms: a brief economic history of the world. Princeton University Press. ISBN978-0-691-14128-2.  
^ abcdefghLi, Tianxu; Zhu, Kun; Luong, Nguyen Cong; Niyato, Dusit; Wu, Qihui; Zhang, Yang; Chen, Bing (2021). "Applications of Multi-Agent Reinforcement Learning in Future Internet: A Comprehensive Survey". arXiv:2110.13484 [cs.AI].  
^Le, Ngan; Rathour, Vidhiwar Singh; Yamazaki, Kashu; Luu, Khoa; Savvides, Marios (2021). "Deep Reinforcement Learning in Computer Vision: A Comprehensive Survey". arXiv:2108.11510 [cs.CV].  
^Moulin-Frier, Clément; Oudeyer, Pierre-Yves (2020). "Multi-Agent Reinforcement Learning as a Computational Tool for Language Evolution Research: Historical Context and Future Challenges". arXiv:2002.08878 [cs.MA].  
^Killian, Jackson; Xu, Lily; Biswas, Arpita; Verma, Shresth; et al. (2023). Robust Planning over Restless Groups: Engagement Interventions for a Large-Scale Maternal Telehealth Program. AAAI.  
^Krishnan, Srivatsan; Jaques, Natasha; Omidshafiei, Shayegan; Zhang, Dan; Gur, Izzeddin; Reddi, Vijay Janapa; Faust, Aleksandra (2022). "Multi-Agent Reinforcement Learning for Microprocessor Design Space Exploration". arXiv:2211.16385 [cs.AR].  
^Li, Yuanzheng; He, Shangyang; Li, Yang; Shi, Yang; Zeng, Zhigang (2023). "Federated Multiagent Deep Reinforcement Learning Approach via Physics-Informed Reward for Multimicrogrid Energy Management". IEEE Transactions on Neural Networks and Learning Systems. PP (5):  5902– 5914. arXiv:2301.00641. doi:10.1109/TNNLS.2022.3232630. PMID37018258. S2CID255372287.  
^Ci, Hai; Liu, Mickel; Pan, Xuehai; Zhong, Fangwei; Wang, Yizhou (2023). Proactive Multi-Camera Collaboration for 3D Human Pose Estimation. International Conference on Learning Representations.  
^Vinitsky, Eugene; Kreidieh, Aboudy; Le Flem, Luc; Kheterpal, Nishant; Jang, Kathy; Wu, Fangyu; Liaw, Richard; Liang, Eric; Bayen, Alexandre M. (2018). Benchmarks for reinforcement learning in mixed-autonomy traffic(PDF) . Conference on Robot Learning.  
^Tuyls, Karl; Omidshafiei, Shayegan; Muller, Paul; Wang, Zhe; Connor, Jerome; Hennes, Daniel; Graham, Ian; Spearman, William; Waskett, Tim; Steele, Dafydd; Luc, Pauline; Recasens, Adria; Galashov, Alexandre; Thornton, Gregory; Elie, Romuald; Sprechmann, Pablo; Moreno, Pol; Cao, Kris; Garnelo, Marta; Dutta, Praneet; Valko, Michal; Heess, Nicolas; Bridgland, Alex; Perolat, Julien; De Vylder, Bart; Eslami, Ali; Rowland, Mark; Jaegle, Andrew; Munos, Remi; Back, Trevor; Ahamed, Razia; Bouton, Simon; Beauguerlange, Nathalie; Broshear, Jackson; Graepel, Thore; Hassabis, Demis (2020). "Game Plan: What AI can do for Football, and What Football can do for AI". arXiv:2011.09192 [cs.AI].  
^Chu, Tianshu; Wang, Jie; Codec├á, Lara; Li, Zhaojian (2019). "Multi-Agent Deep Reinforcement Learning for Large-scale Traffic Signal Control". IEEE Transactions on Intelligent Transportation Systems. 21 (3): 1086. arXiv:1903.04527. Bibcode:2020ITITr..21.1086C. doi:10.1109/TITS.2019.2901791.  
^Belletti, Francois; Haziza, Daniel; Gomes, Gabriel; Bayen, Alexandre M. (2017). "Expert Level control of Ramp Metering based on Multi-task Deep Reinforcement Learning". arXiv:1701.08832 [cs.AI].  
^Ding, Yahao; Yang, Zhaohui; Pham, Quoc-Viet; Zhang, Zhaoyang; Shikh-Bahaei, Mohammad (2023). "Distributed Machine Learning for UAV Swarms: Computing, Sensing, and Semantics". arXiv:2301.00912 [cs.LG].  
^Xu, Lily; Perrault, Andrew; Fang, Fei; Chen, Haipeng; Tambe, Milind (2021). "Robust Reinforcement Learning Under Minimax Regret for Green Security". arXiv:2106.08413 [cs.LG].  
^Leike, Jan; Martic, Miljan; Krakovna, Victoria; Ortega, Pedro A.; Everitt, Tom; Lefrancq, Andrew; Orseau, Laurent; Legg, Shane (2017). "AI Safety Gridworlds". arXiv:1711.09883 [cs.AI].  
^Hadfield-Menell, Dylan; Dragan, Anca; Abbeel, Pieter; Russell, Stuart (2016). "The Off-Switch Game". arXiv:1611.08219 [cs.AI].  
^Hernandez-Leal, Pablo; Kartal, Bilal; Taylor, Matthew E. (2019-11-01). "A survey and critique of multiagent deep reinforcement learning". Autonomous Agents and Multi-Agent Systems. 33 (6):  750– 797. arXiv:1810.05587. doi:10.1007/s10458-019-09421-1. ISSN1573-7454. S2CID52981002.  
Retrieved from "https://en.wikipedia.org/w/index.php?title=Multi-agent_reinforcement_learning&oldid=1309856401"  Categories: 
Reinforcement learning
Multi-agent systems
Deep learning
Hidden categories: 
Articles with short description
Short description matches Wikidata