> Source: https://www.research-collection.ethz.ch/bitstreams/3b278f1d-c38d-4782-8996-01ee9558d7db/download

ETH Library 
Discovering and Using Structure in Autonomous Machine Learning 
Doctoral Thesis 
Author(s): Zadaianchuk, Andrii 
Publication date: 2024 
Permanent link: https://doi.org/https://doi.org/10.3929/ethz-b-000671017 
Rights / license: In Copyright - Non-Commercial Use Permitted 
This page was generated automatically upon download from the ETH Zurich Research Collection. For more information, please consult the Terms of use.
DISS. ETH NO. 30001 
Discovering and Using Structure in Autonomous Machine Learning 
A thesis submitted to attain the degree of 
DOCTOR OF SCIENCES 
(Dr. sc. ETH Zurich) 
presented by 
ANDRII ZADAIANCHUK 
Master of Science in Neural Information Processing, Eberhard-Karls-Universität Tübingen 
born on 19.07.1994 
accepted on the recommendation of 
Prof. Dr. Fanny Yang Prof. Dr. Georg Martius 
Dr. Thomas Kipf 
2024
Abstract 
The ability to autonomously understand complex environments and act in them is an essenti-al goal in artificial agents’ development. State-of-the-art agents may excel in structured tasks, such as assembly line work, but they often fail to adapt to dynamic changes such as those encountered in domestic settings or natural outdoor environments, calling for advancement in agents that can perceive, learn, and reason in the real world as situations evolve. While achieving full autonomy is elusive for random changes in the environment, such a goal is attainable because the world around us is highly structured. However, the realistic interface to the world for both humans and artificial agents is a stream of unstructured, high-dimensional sensory inputs, like images. Thus, to build autonomous machines that can explore their open-ended environments and acquire large repertoires of skills, it is essential to equip agents with core and general systems to discover and use the structure present in the real world. In this thesis, we focus on the discovery of the structure from real-world and (mostly) unconstrained visual data, as well as on the efficient use of this discovered structure in autonomous agents. 
We organize the manuscript around these two notions: the usage of structure and its discovery. In the first part of the thesis, we propose several methods to learn object-centric and graph-based structures from the raw observations. We show that the object-centric structure, in combination with goal-directed agents, helps the autonomous agent to discover and learn valuable skills. These skills can be further combined to address compositional tasks like the manipulation of several different objects. In the second part of the thesis, we further investigate general objectives and inductive biases that are useful for scaling object-centric structure discovery methods and scene decomposition to the real world and unconstrained inputs. We show that unsupervised scene decomposition (into objects and their categories) is possible when we bootstrap from highly semantic and dense self-supervised representations. This investigation not only offers a novel approach to structure 
i
discovery from unstructured data but also illustrates the significant potential for these methods to form the building blocks for future, more capable artificial systems. 
ii
Zusammenfassung 
Die Fähigkeit, komplexe Umgebungen autonom zu verstehen und in ihnen zu handeln, ist ein wesentliches Ziel bei der Entwicklung künstlicher Agenten. State-of-the-Art-Agenten können in strukturierten Aufgaben, wie der Arbeit an Montagelinien, hervorragend sein, versagen jedoch oft bei der Anpassung an dynamische Veränderungen, wie sie in häuslichen Umgebungen oder natürlichen Außenumgebungen auftreten. Dies erfordert einen Fortschritt von Agenten, die die reale Welt wahrnehmen, in ihr lernen und schlussfolgern können, während sie sich verändert. Obwohl die Erreichung vollständiger Autonomie unter zufälligen Veränderungen der Umwelt schwer fassbar ist, ist ein solches Ziel erreichbarer, weil die Welt um uns herum hochstrukturiert ist. Allerdings ist die realistische Schnittstelle zur Welt sowohl für Menschen als auch für künstliche Agenten ein Strom von unstrukturierten, hochdimensionalen sensorischen Eingaben, wie Bilder. Daher ist es wesentlich, Agenten mit Kern- und allgemeinen Systemen auszustatten, um ihre offenen Umgebungen zu erkunden und große Repertoires von Fähigkeiten zu erwerben, die Struktur in der realen Welt entdecken und nutzen können. In dieser Dissertation konzentrieren wir uns auf die Entdeckung von Struktur aus realen und (meist) unbeschränkten visuellen Daten sowie auf die effiziente Nutzung dieser entdeckten Struktur in autonomen Agenten. 
Wir organisieren das Manuskript um diese beiden Begriffe: die Nutzung von Struktur und ihre Entdeckung. Im ersten Teil der Dissertation schlagen wir mehrere Methoden vor, um objektzentrische und graphbasierte Strukturen aus den rohen Beobachtungen zu lernen. Wir zeigen, dass die objektzentrische Struktur in Kombination mit zielgeri-chteten Agenten dem autonomen Agenten hilft, wertvolle Fähigkeiten zu entdecken und zu erlernen. Diese Fähigkeiten können weiterhin kombiniert werden, um zusammengesetzte Aufgaben wie die Manipulation mehrerer verschiedener Objekte zu bewältigen. Im zweiten Teil der Dissertation untersuchen wir weiterhin allgemeine Ziele und induktive Vorei-ngenommenheiten, die nützlich sind, um Methoden zur Entdeckung objektzentrischer 
iii
Strukturen und Szenenzerlegung in der realen Welt und bei unbeschränkten Eingaben zu skalieren. Wir zeigen, dass eine unüberwachte Szenenzerlegung (in Objekte und ihre Kategorien) möglich ist, wenn wir von hochsemantischen und dichten selbstüberwachten Darstellungen bootstrappen. Diese Untersuchung bietet nicht nur einen neuen Ansatz zur Strukturentdeckung aus unstrukturierten Daten, sondern illustriert auch das erhebli-che Potenzial dieser Methoden als Bausteine für zukünftige, leistungsfähigere künstliche Systeme. 
iv
Acknowledgments 
In this part of the thesis, I would like to thank everyone who accompanied and helped me in achieving this milestone. Although it’s challenging to name everyone individually, I deeply appreciate each person who has directly or indirectly influenced my doctoral studies. These years of pursuing a Ph.D. have become an extremely valuable part of my life, full of meaning, motivation, and exploration into the unknown. 
My first and foremost thanks go to my Ph.D. advisers, Prof. Georg Martius and Prof. Fanny Yang. Thank you for being the best supervisors I could imagine and for creating an environment where it is so natural to collaborate, help each other, and share knowledge. Georg, you always gave me the freedom to make decisions while supporting and guiding me towards the next step forward. I’m grateful for all the scientific discussions, for showing how to constantly learn and shape ideas. Your support during the most challenging phases of my Ph.D. journey, particularly for me and my family, has been invaluable. Fanny, I am grateful for your priceless advice and the impactful way you taught me to frame research questions, enhance my writing, and structure my thoughts and scientific vision and future plans. 
Next, I want to thank all my colleagues in Tübingen and Zürich who made my journey more interesting. Special thanks to Max, for his time, stimulating discussions, and collaborative spirit throughout my Ph.D. journey. Additionally, he is a good friend with whom I could discuss everything. In addition, I want to thank Chansu, Michal, Dominik, Marin, Sebastian, Dingling, Marco, Nuria, and other AL group members for creating an environment full of ideas and feedback, giving advice, and having thought-provoking conversations. Likewise, I want to thank Konstantin, Alex, Nicolo, and other group members in Zürich for actively thinking together and teaching each other to provide useful critical feedback. Thanks for the nice time (despite the lockdown) and the best Avalon and ramen remote socials in the hard COVID times, as well as great hikes and group retreats during better times. 
v
I am thankful to Francesco Locatello and Thomas Brox for the opportunity to do great research together in the Amazon Lablets team. Francesco, thank you for being a good friend, mentor, and manager, always finding time and actively helping to navigate when I was stuck. Thank you for all the feedback that helped me to better see potential next steps both in scientific projects and in my career. Thomas, thank you for helping to find an interesting and challenging problem and for navigating possible solutions in a new topic. Furthermore, I want to thank Yi, Matthias, Peter, Yash, Chris, and other colleagues at Amazon for helping me to go through all the difficulties of the computing infrastructure, providing valuable feedback, and helping to shape the next steps in my career. 
My research was greatly supported by institutions including the Max Planck Institute for Intelligent Systems, the Department of Computer Science at ETH Zurich, the ETH MPI Center for Learning Systems, and Amazon. I am deeply grateful for their support. In addition, I would also like to thank Dr. Thomas Kipf for serving on my Ph.D. committee. 
To all my friends, especially Sarah, Olha, Sasha, Nastya, Marili, Artem, and Melissa thank you for your unwavering support, for listening to my concerns, and for sharing your perspectives on research and life. Your presence and support during difficult times for my family and country have been a pillar of strength and hope. 
I am also grateful to my partner Kseniia for all the unconditional love and support that made this long path possible. Дякую, що ти поряд, дякую за кожну розмову та за можливiсть вiдчувати та розумiти цей свiт разом з тобою. 
Finally, I’d like to thank my family. Тато, дякую, що завжди вiрив у мене та пiдтримував мiй шлях. Мамо, спасибi за все, що ти зробила, щоб у мене була можливiсть вчитися та розвиватися. Оля, дякую за те, що завжди допомагала, вiрила та бачила мене таким, який я є. Люда та Iра, дякую, що завжди вiдчував себе вдома поряд з вами. 
vi
Contents 
1 Introduction 1 1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1.2 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 1.3 Collaborators and Contributions . . . . . . . . . . . . . . . . . . . . . . . . 5 1.4 Additional Publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 
2 Background 7 2.1 Structured Reinforcement Learning without Supervision . . . . . . . . . . 7 2.2 Unsupervised Structured Representation Learning . . . . . . . . . . . . . . 16 
3 Self-Supervised RL with Object-Centric Representations 29 3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 3.2 Related work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 3.3 Self-Supervised Multi-Object Reinforcement Learning . . . . . . . . . . . . 34 3.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 3.5 Conclusion and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . 41 
4 RL with Independently Controllable Subgoals 43 4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 4.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45 4.3 Relational RL with Independently Controllable Subgoals . . . . . . . . . . 48 4.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 4.5 Conclusion and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . 56 
5 Object Category Discovery for Semantic Segmentation 57 5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 5.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 5.3 Self-supervised Semantic Segmentation . . . . . . . . . . . . . . . . . . . . 63 
vii
CONTENTS 
5.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 5.5 Conclusion and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . 73 
6 Scaling Video Object-Centric Learning 75 6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 6.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 6.3 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 6.4 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 6.5 Conclusion and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . 91 
7 Discussion 95 7.1 Using Structure for Autonomous Agents . . . . . . . . . . . . . . . . . . . 95 7.2 Discovering Structure from Real-World Datasets . . . . . . . . . . . . . . . 98 
A Appendix for Chapter 3 103 A.1 Analysis of Representations Learned by SCALOR . . . . . . . . . . . . . . 103 A.2 Ablation Analysis of Goal-conditioned Attention Policy . . . . . . . . . . . 106 A.3 Longer Training for Visual Rearrange with Two Objects . . . . . . . . . . . 106 A.4 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107 A.5 Problems with SCALOR Tracking during RL Training . . . . . . . . . . . 110 
B Appendix for Chapter 4 115 B.1 SRICS pseudocode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115 B.2 Multi-object Rearrange Environments . . . . . . . . . . . . . . . . . . . . . 116 B.3 Additional Experimental Results . . . . . . . . . . . . . . . . . . . . . . . . 116 B.4 Goal-Conditioned Attention Policy . . . . . . . . . . . . . . . . . . . . . . 117 B.5 Subgoals Selectivity as an Evaluation Metric . . . . . . . . . . . . . . . . . 118 B.6 Estimation of the Global Interaction Graph . . . . . . . . . . . . . . . . . 119 B.7 Evaluation on the Average Objects Distance . . . . . . . . . . . . . . . . . 122 B.8 Ordering of the Subgoals . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122 B.9 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124 
C Appendix for Chapter 5 127 C.1 Sensitivity of the COMUS parameters . . . . . . . . . . . . . . . . . . . . . 127 C.2 Self-supervised features quality . . . . . . . . . . . . . . . . . . . . . . . . 128 C.3 Saliency masks quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129 
viii
CONTENTS 
C.4 Extended Limitations and Future Work . . . . . . . . . . . . . . . . . . . . 131 C.5 More detailed quantitative and qualitative results . . . . . . . . . . . . . . 133 C.6 Implementation details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 C.7 Datasets (directly or indirectly) used in the paper . . . . . . . . . . . . . . 136 
D Appendix for Chapter 6 141 D.1 Comparison with Additional Baselines . . . . . . . . . . . . . . . . . . . . 141 D.2 Additional Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144 D.3 Architectural Details and Hyperparameters . . . . . . . . . . . . . . . . . . 150 D.4 Dataset Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157 D.5 Additional Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158 
ix
1 
Introduction 
“All models are wrong, but some are useful.” 
George E.P. Box 
1.1 Motivation 
The development of autonomous agents that can comprehend complex environments and act to achieve goals is an essential objective for artificial intelligence. Achieving this aim would significantly enhance the functionality of automated systems. It can also reveal insights into the cognitive mechanisms that enable such capabilities in biological organisms. Intelligent systems face the challenge of effectively processing raw, high-dimensional inputs such as images or videos to guide their actions. Such processing can be described in terms of learning the input representation that allows an intelligent system to plan effectively and execute diverse tasks robustly in various environments. In this thesis, we study the forms and properties of high-dimensional input representations and effective methods of discovering and using them in general-purpose intelligent systems. 
Whenever an explicit representation form is selected for a decision-making method, as-sumptions are made implicitly or explicitly introducing inherent biases. Thus, it becomes 
1
Chapter 1. Introduction 
critical to study different forms of representations and their corresponding biases and systematically compare their influences on the functionalities of intelligent systems that adopt them (Mitchell, 1980). For example, humans have been shown to use several core representation systems such as objects, goal-directed actions, and numbers (Spelke and Kin-zler, 2007). Such common representation systems can be helpful in mapping unstructured agents’ observations (i.e., their sensory inputs) to more structured and compact represen-tations of those observations. While we cannot avoid imposing some biases when using explicit representations, it is essential to choose biases that closely mirror the attributes of real-world natural data (Bengio et al., 2013; Peters et al., 2017; Schölkopf et al., 2021). By incorporating these biases, intelligent systems can be better equipped to solve a broad spectrum of real-world tasks, thereby enhancing their generalization and problem-solving capabilities (Dittadi et al., 2022). 
One way of uncovering relevant biases from real-world high-dimensional data is by modeling the data generation process and observing its properties. We refer to such high-level and abstract properties of the data generation process (and thus of the data itself) as structure. This dissertation is centered on discovering the structure in real-world data and using this structure to empower autonomous agents with goal-directed skills. This way, we explore how two core representation systems studied previously in human intelligence can be combined in artificial intelligent systems. Specifically, we focus on the problem of unsupervised structured representation learning for autonomous goal-driven intelligent systems (Mitchell, 1982; Steels, 2004). 
The compositional nature of the real-world visual data generative process and its corre-sponding data emerges as a promising feature for defining inductive biases in representation learning models (Schölkopf et al., 2021). Compositionality is the principle that complex images or scenes can be decomposed into simpler constituent elements and relationships, reflecting how humans perceive their visual environment (Spelke and Kinzler, 2007). Thus, developing systems that enforce the compositional structure of their representations can align the biases of an intelligent system with the structural properties of real-world data, enhancing the system’s ability to learn more efficiently from its environment. For example, learning the representation of a particular object in a simple scene consisting of only this object can be reused when the object is presented in a more complex scene with many objects. Similarly, if the components are represented in a common format the system can carry over experiences between components during learning (Greff et al., 2020). Finally, such systems could be more robust to the sparse changes in their environment as only some 
2
1.2. Outline 
components of compositional representation would be affected by such changes (Schölkopf et al., 2021; Dittadi et al., 2022). 
Compositionality is present not only in the inputs to real-world intelligent systems but also in their behavior: more complex behavior can often be decomposed into a sequence of (mostly) independent behaviors. In this thesis, we explore effective ways of discov-ering compositional structures in real-world high-dimensional visual data by learning a compositional representation of each data point. We show that an agent equipped with such representations can decompose its observations into interpretable and independently controllable components. In the following sections, we describe the main contributions of this thesis. 
1.2 Outline 
In this dissertation, we explore two main research questions related to discovering and using structure from real-world high-dimensional observations: 
1. How can we discover the unknown structure that is present in the data without any human annotations? 
2. How can we use discovered or provided structure to train an autonomous general-purpose agent? 
In Chapter 3 and Chapter 4 of this dissertation, we address the question of using structure for autonomous general-purpose agents. In particular, we explore how an agent that is equipped with structured (object-centric) representations can learn to interact with the environment in a self-supervised manner. 
 Chapter 3 presents a self-supervised object-centric reinforcement learning method for goal-based exploration of the environment. Our agent uses an object-centric representation learning method to learn a representation of the environment that is used by the agent to propose and solve simple subgoals such as the rearrangement of a particular object. We show that our method outperforms the state-of-the-art self-supervised reinforcement learning methods on a set of challenging multi-task and multi-object manipulation environments while operating only from visual observations. This chapter is based on Zadaianchuk et al. (2021): 
3
Chapter 1. Introduction 
“Self-supervised Visual Reinforcement Learning with Object-centric Representa-tions” Andrii Zadaianchuk∗, Maximilian Seitzer∗, and Georg Martius ICLR 2021: International Conference on Learning Representations 
 In Chapter 4, we further study goal-based exploration in cases where objects are not independent from each other. We propose to discover the relations between objects and use them for decomposing the environment into non-interacting subspaces that can serve as goal spaces. This shows that the dynamics of objects can be further used to discover a structure that is relevant for control. This chapter is based on Zadaianchuk et al. (2022): 
“Self-supervised Reinforcement Learning with Independently Controllable Sub-goal” Andrii Zadaianchuk, Georg Martius, and Fanny Yang CoRL 2022: Conference on Robot Learning 
In Chapter 5 and Chapter 6, we investigate how one can discover new structures in high-dimensional image and video datasets without using any supervision from human annota-tions. We consider decomposing the whole dataset to different categories present in the data as well as decomposing each image into independent components such as objects and back-ground parts. In particular, we focus on unsupervised semantic segmentation and object-centric scene decomposition representations using self-supervised dense representations. 
 Chapter 5 shows that it is possible to discover different object categories from the multi-object natural image datasets without any human-labeled annotations (e.g., dense semantic segmentation masks or image-level labels). We achieve this by discovering the categorical structure in a set of object proposals. This chapter is based on Zadaianchuk et al. (2023b): 
“Unsupervised Semantic Segmentation with Self-supervised Object-centric Rep-resentation” Andrii Zadaianchuk, Matthaeus Kleindessner, Yi Zhu, Francesco Locatello, Thomas Brox ICLR 2023: International Conference on Learning Representations 
4
1.3. Collaborators and Contributions 
 In Chapter 6, we further establish that object localization can be discovered jointly with learning their representations from multi-object datasets. We propose to use dense self-supervised features as a highly semantic target for object-centric learning. Such targets are simple and effective ways to scale object-centric methods to real-world datasets. Next, we also show that combining such targets with the more challenging task of predicting temporal feature similarities in video allows us to scale object-centric learning in videos. This chapter is based on Zadaianchuk et al. (2023a): 
“Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities” Andrii Zadaianchuk∗, Maximilian Seitzer∗, and Georg Martius NeurIPS 2023: Conference on Neural Information Processing Systems 
1.3 Collaborators and Contributions 
The work described in the thesis was developed in collaboration with Georg Martius, Fanny Yang, Thomas Brox, Maximilian Seitzer, Francesco Locatello, Matthaeus Kleindessner, Yi Zhu. 
The ideas, experiments, and presentation of them were primarily contributed by the first author, except in the case of papers concerning object-centric RL (Chapter 3) and real-world video-based object-centric learning (Chapter 6). For these papers, the first two authors (indicated by *) shared equal contributions across all material. Other authors significantly contributed as advisors, aided in conducting experiments, and/or directly participated in the writing or editing of a few individual sections in the aforementioned papers. 
5
Chapter 1. Introduction 
1.4 Additional Publications 
The body of this dissertation is augmented by several pieces of collaborative work done with other researchers. Since these additional works don’t directly correspond to the dissertation’s main theme, they are included separately in Appendix A, with a brief summary that explains their relation with the overall context of the work. The associated papers are: 
 Maximilian Seitzer, Max Horn, Andrii Zadaianchuk, Dominik Zietlow, Tianjun Xiao, Carl-Johann Simon-Gabriel, Tong He, Zheng Zhang, Bernhard Schölkopf, Thomas Brox, and Francesco Locatello (2023). “Bridging the Gap to Real-World Object-Centric Learning”. International Conference on Learning Representations. url: https://arxiv.org/abs/2209.14860 
 Andrii Zadaianchuk and Georg Martius (2020). “Unsupervised Learning of Indepen-dently Controllable Dynamic Components”. ICML Object-Oriented Learning (OOL): Perception, Representation, and Reasoning Workshop 
 Diego Agudelo-España, Andrii Zadaianchuk, Philippe Wenk, Aditya Garg, Joel Akpo, Felix Grimminger, Julian Viereck, Maximilien Naveau, Ludovic Righetti, Georg Martius, Andreas Krause, Bernhard Schölkopf, Stefan Bauer, and Manuel Wüthrich (2020). “A Real-Robot Dataset for Assessing Transferability of Learned Dynamics Models”. International Conference on Robotics and Automation, pp. 8151–8157. url: https://ieeexplore.ieee.org/document/9197392 
6
2 
Background 
2.1 Structured Reinforcement Learning without Su-pervision 
In this section, we describe a framework for autonomous, general-purpose agents to explore the real world and learn valuable skills. First, we introduce general reinforcement learning (RL) agents and demonstrate how they can be utilized to solve specific tasks within given environments. Next, we illustrate how to extend the standard RL paradigm to the autonomous case, where agents learn to act within an environment by self-generating tasks and subsequently learning to solve them. We discuss modifications to the agent’s policy needed to support learning of the multiple tasks simultaneously. For this extension, tasks are represented as goal vectors within a certain goal space. Task encoding allows conditioning the agent’s policy on the goal representation, as well as defining the reward function as a distance measure computed in the corresponding goal space. We describe how goal-conditioned agents can be employed for autonomous and hierarchical exploration of the environment by setting their own goals or subgoals. Finally, we address the evaluation of such general-purpose agents performance. Beyond assessing agents’ sample efficiency, it is important to evaluate their generalization capabilities regarding unseen tasks and their adaptability to changes in the environment. 
7
Chapter 2. Background 
2.1.1 Markov Decision Process (MDP) 
The MDP is a mathematical framework that describes a particular task in reinforcement learning and plays a central role in sequential decision-making (Sutton and Barto, 1998). It consists of a tuple (S, A, p, r), where S represents the state space, a set of the agent’s possible states. A represents the action space, a set of all the possible actions the agent can take. The function p : S × S × A 7→ [0, ∞) defines the transition probability density. This function describes the probability of transitioning to a state st+1 given the current state st and the action at taken. As the transition probability is unknown to the agent, the agent can only observe samples from the transition probability distribution while acting in the environment. The reward function r : S 7→ R maps states to real numbers, indicating the reward the agent receives for reaching state st+1. Each instance of an MDP describes a distinct reinforcement learning problem, referred to as a task (as presented in Figure 2.1a). 
2.1.2 Episodic Setting 
We consider an episodic setting, where agents act in the environments for T steps. Such simplification is useful for the formalization of the agent’s utility function. The agent’s objective within this framework is to maximize the expected return R defined as the cumulative reward over a certain time horizon T . The expected return can be formally expressed as 
R = T∑ t=1 
Est∼ρπ ,at∼π,st+1∼p[r(st+1)], (2.1) 
where ρπ(st) is the marginal distribution of states induced by the agent’s policy π(at|st). 
In simpler terms, the agent interacts with its environment by being in a particular state, taking an action based on its policy, and receiving a corresponding reward. The agent aims to maximize the expected cumulative reward over time, effectively solving the MDP. 
2.1.3 Self-Supervised Reinforcement Learning 
In theory, the MDP framework allows the optimization of arbitrary reward functions. To enhance the practicality of Reinforcement Learning (RL) in real-world robotic applica-tions—such as adaptive navigation within spaces or relocating objects—there’s a need for a more autonomous, multi-task learning framework. However, agents trained under 
8
2.1. Structured Reinforcement Learning without Supervision 
Environment 
Agent 
Action StateReward 
(a) Standard RL agent. 
Environment 
Action State 
Agent Reward 
Environment 
Agent 
Action StateReward 
Train Evaluation 
(b) Autonomous RL agent. 
Figure 2.1: Agent-environment interactions by different types of agents. In contrast to standard RL agents, autonomous RL agents should be able to learn in the environment without supervision. During training the agent generates its tasks and learns how to solve them. During the evaluation, the agent is provided with external tasks from the environment. 
this framework are inherently tailored to specific tasks. Unlike standard RL where an agent learns to maximize externally provided rewards, in task-agnostic or self-supervised RL (Schmidhuber, 2010; Sharma et al., 2021; Pong et al., 2020; Florensa et al., 2018; Wang et al., 2020b; Chen et al., 2023), the agent learns to generate its own tasks (while having no access to external reward labels). As shown in Figure 2.1b, the autonomous RL agent, unlike the standard RL agent, acts as a self-supervised learning entity, generating tasks during training and receiving external tasks during evaluation. The capability to generate tasks provides an advantage in situations where there are few external tasks available, or a particular task is not known in advance. This makes self-supervised RL a promising avenue for the advancement of adaptive and self-directed agents. 
The challenge of training adaptable, self-supervised agents primarily revolves around designing a method to encapsulate varying tasks and their associated reward functions in a universal format. This ensures that tasks provided externally during deployment can be represented coherently with tasks that were explored during self-supervised training. Although crafting such a common interface for an arbitrary range of tasks is practically unfeasible, employing the notion of final state configurations (goal states) as a task encoding scheme appears as a broadly applicable and adaptable solution, bridging external and internal task representations. This approach not only bridges external and internal task representations but also enables the agent to generalize to a continuous space of possible tasks in this space, a significant advantage since it’s impractical to manually specify all 
9
Chapter 2. Background 
reward functions. Next, we will cover how to use the state space to learn a goal space where the goals are both achievable and diverse. 
2.1.4 Goal-Conditioned Reinforcement Learning 
In the RL setting described before, the agent only learns a policy to solve a single task specified by the reward function. If we are interested in an agent that can solve multiple tasks (Caruana, 1997; Schaul et al., 2015), each with a different reward function, in the same environment, we should train the agent on those tasks by specifying which distinct task the agent should solve at each time step. To formalize this, one could define a space of reward functions R, where each point specifies a particular task the agent has to solve. However, how can we describe a task to the agent in a compact form? 
Environment 
Agent 
Action StateReward Goal 
(a) Multi-goal Environment (b) Multi-task Agent (c) Hierarchical Agent 
Initial state 
Goal state Sub-goals 
Figure 2.2: Two main advantages of the agents equipped with goals: (b) multitasking, (c) task decomposition. 
One convenient way to provide an agent with information about the tasks is by providing a task representation zg ∈ G, or goal representation, as a point in the goal space G. The goal space G is obtained by mapping agents’ states or observations to the latent space. Goal representation should be defined together with a corresponding reward function rg ∈ R. One natural way to define rg is to define a mapping RG(· | zg) : G → R from goal space G to a space of reward functions R. This mapping is called a goal-conditioned reward function, and it defines a specific task in the environment (Kaelbling, 1993). 
The goal-conditioned RL framework allows an agent to learn a policy conditioned on a specific goal (Schaul et al., 2015; Andrychowicz et al., 2017). This policy, denoted as π(a|s, zg), dictates the agent’s actions a given its current state s and the goal zg. The policy is typically learned through interaction with the environment and by maximizing the expected goal-conditioned return: 
10
2.1. Structured Reinforcement Learning without Supervision 
Ezg∼G 
[ T∑ t=1 
Est∼ρπ ,at∼π,st+1∼p[RG(st+1 | zg)] ] , (2.2) 
where G is some distribution over the goal space G. Given such formulation, an agent should learn how to solve many tasks in the same environment. When a goal-conditioned reward function has additional properties (e.g., if close goal representations encode close tasks), an agent policy π(a|s, zg) should also generalize to goals sampled from the same goal distribution G even if they have been not sampled during training with a finite number of goals. 
Goal Composition with Hierarchical Reinforcement Learning. Solving many tasks in the environment using the same policy allows an agent to tackle more complex and long-term tasks than any original tasks that the agent has mastered. The goals can be seen as abstract high-level actions. They serve as an interface to guide agent behavior in a hierarchical sense. Combining those actions to achieve long-term or compositional goals is a hierarchical reinforcement learning problem. 
Hierarchical Reinforcement Learning (HRL) (Levy et al., 2019; Vezhnevets et al., 2017; Levy et al., 2019; Röder et al., 2020; Zadaianchuk et al., 2021; Zadaianchuk et al., 2022; Gürtler et al., 2021) is a framework that can be used to guide the sequencing of goals, allowing for the decomposition of complex tasks with long-term dependencies into simpler sub-tasks (Dayan and Hinton, 1993; Sutton et al., 1998; Sutton et al., 1999; Precup, 2000). In HRL, a high-level policy is obtained via planning or reinforcement learning to propose a sequence of goals for a lower-level policy to maximize the overall reward function (i.e., to solve the original long-term or compositional goal). 
This approach facilitates breaking down complex tasks with long-term dependencies into more manageable sub-tasks. Traditional goal-conditioned RL algorithms (Levy et al., 2019; Blaes et al., 2019; Röder et al., 2020; Zadaianchuk et al., 2021; Zadaianchuk et al., 2022; Gürtler et al., 2021) could be used to implement low-level policies, which can be trained either independently of, or in conjunction with, the high-level policy (Kulkarni et al., 2016; Frans et al., 2018; Levy et al., 2019; Nachum et al., 2018; Röder et al., 2020). Many HRL algorithms could be seen as goal-conditioned. For example, the options framework (Sutton et al., 1999; Precup, 2000) tries to handle the number of steps needed for each low-level policy by learning a termination function. Options can be viewed as goal-conditioned 
11
Chapter 2. Background 
policies (with simple one-hot vectors as goal embeddings) that can be selected by the high-level policy (Sutton et al., 1999; Precup, 2000). 
While many approaches utilize predefined spaces for subgoals (such as specific positions in a maze), recent strategies propose learning a subgoal space. This space could be abstract (Vezhnevets et al., 2017), or connected to image observations by a generative model (Nasiriany et al., 2019; Zadaianchuk et al., 2021). In Chapter 3, we also show that a learned compositional generative model of environment observations could be seen as a model of learning subgoal spaces and subgoal sampling distributions. In addition, in Chapter 4, we study what is needed for learning independently controllable subgoals that are composable into a sequence of subgoals that can be solved without influencing other subgoals. More concretely, solving a subgoal in the sequence has no influence on earlier solved subgoals. This way the agent’s high-level policy is informed by the environment structure: in the case of independent subgoals, a random goal can be picked, whereas, in the case of dependencies between goals, there is an optimal goal ordering that the policy can follow. However, we see the usage of the more flexible, learned higher-level policy as a promising future direction. 
Autonomous Goal-Conditioned Agents with State-Dependent Goals In the formulation above (e.g. in Equation 2.2 and in Figure 2.2a) the goal space G and the corresponding reward function RG are assumed to be given externally. However, a fully-autonomous agent should have the ability to propose and master its own goals (Steels, 2004; Sharma et al., 2021; Colas et al., 2022). We schematically depict such an agent in Figure 2.3. During training the agent jointly proposes its goals and learns to solve them. This self-guided learning leads to valuable skills that the agent can reuse and combine, enabling it to solve more complex external tasks in the future, e.g., during evaluation. The goal representation outlined above offers the potential to encapsulate any behaviors, including the ones that require observing the sequence of states to be defined, such as dancing or avoiding obstacles (Colas et al., 2022). However, mastering such a broad goal space becomes problematic without external demonstrations to showcase the spectrum of behaviors within the given environments. 
One natural restriction of the goal space that can empower an agent to generate its own goals is to ground its internal task specification (zg, rg) on the observed environment states or observations. Given a mapping m(s) : S → G, the agent can use environment states s to generate new goals zg = m(s). The reward usually can be specified as a distance measure in such a goal space (Nair et al., 2018; Colas et al., 2022), as any state can be mapped to 
12
2.1. Structured Reinforcement Learning without Supervision 
Environment 
Goal 
Train 
Reward 
State 
Agent 
Action 
Environment 
Goal 
Evaluation 
Reward 
State 
Agent 
Action 
Figure 2.3: Autonomous goal-conditioned agents. During training such agents sample goals from the learned goal space. Subsequently, during evaluation agents are provided with external goals to solve. 
this space. Formally, the goal-based reward function is represented as a distance function d : G × G → R. Given the current state st and the goal state zg, the reward function rg is defined as: 
RG(st, zg) = −d(m(st), zg) (2.3) 
Here, d(m(st), zg) computes the distance between the current state’s representation in the goal space and the goal. One common choice for such distance is Euclidean distance, defined as d(m(st), zg) = ||m(st) − zg||2. In addition to this mapping, it is necessary for the agent to learn the distribution G to sample goals during self-supervised training from the goal space. This distribution could be close to already seen goal distribution (Nair et al., 2018; Nair et al., 2020) or skewed towards less seen goals (Pong et al., 2020; Pitis et al., 2020). Control over goal space sampling allows the agent to explore its environment hierarchically, i.e., not only using low-level actions but also using goals to explore the environment. Such agents can achieve a higher level of autonomy as they learn to decompose more difficult or previously unseen goals into a sequence of already explored subgoals. In this thesis, we restrict ourselves to state-dependent goal spaces as they allow practical task specifications, and can be tackled by fully-autonomous agents without any supervision. 
Learning State-Dependent Goal Space The learning of goal space representations without supervision is a challenging, yet crucial aspect of autonomous goal-conditioned agents (Péré et al., 2018). The agent must learn to generate meaningful goals and the corresponding reward functions from environment interactions without any external guidance or predefined task set. 
13
Chapter 2. Background 
One common approach to learning goal representations is to use unsupervised learning techniques such as autoencoders or generative methods (Nair et al., 2018; Pong et al., 2020; Péré et al., 2018). Such methods can learn to encode the high-dimensional state space into a lower-dimensional goal space, and decode the goal representations back into the state space. The learned goal space should ideally capture the underlying structure of the tasks in the environment, allowing the agent to generate diverse and meaningful goals and subgoals. We will cover the details of unsupervised representation learning in the following sections. 
Sampling Goals from Goal Space Designing or learning the goal sampling distribution G is an important part of goal-conditioned reinforcement learning. It involves defining a goal space and effectively sampling from it to facilitate learning. Ideally, goals should be achievable and contribute to the learning process (Pong et al., 2020; Blaes et al., 2019; Forestier et al., 2022). 
One of the challenges in Reinforcement Learning (RL) is the sparsity of rewards in many environments. Hindsight Experience Replay (HER) (Andrychowicz et al., 2017) helps to mitigate this by treating the final state of each unsuccessful attempt as the intended goal, providing a learning signal in each episode. The process involves a balance between exploring novel goals and exploiting familiar ones. Generative models can produce diverse goals, and structured goal spaces can constrain these goals to be meaningful and achievable. In conclusion, a well-defined goal space and efficient sampling method are crucial for achieving higher-level autonomy in RL agents. 
2.1.5 Evaluation of Goal-Conditioned Autonomous Agents 
Traditional reinforcement learning (RL) evaluation metrics, such as expected return for specific tasks in an environment, may no longer suffice for general-purpose agents, given the increasing complexity of tasks and the diversity of environments in which these agents are expected to operate. Consequently, there is a growing need to understand and adopt more sophisticated evaluation methodologies that encapsulate the adaptability and learning capabilities of such agents. This subsection introduces two corresponding evaluation criteria: sample efficiency and generalization (both task-based and environment-based). These criteria are essential in assessing the proficiency of goal-conditioned autonomous agents. 
14
2.1. Structured Reinforcement Learning without Supervision 
Sample Efficiency First, an important criterion of evaluation agent learning capabilities is its sample efficiency. Sample efficiency formally could be defined using the notion of Sample Complexity of Exploration (Kakade, 2003): for given fixed parameters ϵ, δ > 0, a mistake is occurring if the difference between the value functions of a learned policy π and an optimal policy π∗ is ||Qπ(s, a) − Qπ∗(s, a)||∞ > ϵ. The sample complexity of exploration ζ(ϵ, δ) is defined as the total number of mistakes at a timestep t (with probability 1 − δ). Intuitively, if the method is showing a higher return than another method while using the same amount of data it is more sample efficient. 
In this dissertation, we study the difference in sample efficiency for methods that tackle compositional tasks. We show that usage of the state structure to decompose complex tasks into a sequence of subtasks can bring large benefits in terms of sample efficiency. This is due to less noisy learning signals (from simpler subtasks) as well as better state space coverage (as each simple task is only about controlling a particular subspace). 
Generalization While we train an agent in a specific environment to solve self-generated tasks from a particular distribution, we want to investigate how the trained agent can generalize to unseen tasks in the same environment, as well as to the tasks in modified environments. The generalization gap usually is defined as the difference in performance for an agent evaluated on training tasks Mtrain and evaluation tasks Meval: 
Gen(π) := P (π, Mtrain ) − P (π, Meval ). (2.4) 
Here, P is a performance metric, such as success rate or distance to the goal. In the common evaluation setting, evaluation tasks Meval are tasks from the same environment. However, truly open-ended learning should also handle changing environments that share some common structure. For this, we propose to evaluate the generalization gap, when Meval is from a different environment that shares a similar structure, but is combinatorically different. For example, we can investigate how our agent performs if the environment contains a different number of objects than presented during training. 
15
Chapter 2. Background 
2.2 Unsupervised Structured Representation Learn-ing 
The upcoming section outlines the general problem-setting associated with reconstruction-based compositional scene representation learning utilizing deep neural networks. Since there are various ways to structure the representation space, we will focus on methods that best help an agent to learn skills from environment observations and their representations. We start by describing fixed-length representations, where structure can be enforced by additional assumptions on the latent space and using additional regularizers to achieve disentanglement of the latent components. Subsequently, we cover compositional scene representations, which consist of an unordered set of vectors where each vector corresponds to a particular object or entity in the scene, so-called object-centric representations. Such representations might contribute to systematic generalization (Greff et al., 2020) and can enable training agents that exhibit greater robustness to changes in their environment. Additionally, we describe object-centric models that we build upon and the evaluation metrics that are used throughout the thesis. 
2.2.1 Fixed-length Representation Learning 
Representation Learning with Autoencoders Autoencoders are a key tool for unsu-pervised learning of data representations. An autoencoder is a neural network architecture designed to learn efficient encodings of input data (typically referred to as latent represen-tation or latent “codes”) by training the network to reconstruct its inputs. To implement reconstruction-based training, autoencoder architectures consist of two main components: an encoder and a decoder. 
The encoder function, denoted as fθ, maps an input x ∈ RD to a latent representation z ∈ Rd, where D is the dimensionality of the input and d is the dimensionality of the latent representation. The encoder is parameterized by θ, the network weights. Formally, this mapping is given by z = fθ(x). The decoder function, denoted as gϕ, then maps this latent representation z back to the input space, effectively trying to reconstruct the original input. The decoder is parameterized by ϕ. Formally, this mapping is given by x̂ = gϕ(z). 
The objective of an autoencoder is to minimize the reconstruction error between the original input x and its reconstruction x̂, usually defined by a loss function L(x, x̂). In many cases, 
16
2.2. Unsupervised Structured Representation Learning 
the loss function is the mean squared error (MSE), which measures the average squared difference between the original input and its reconstruction. The goal is to find optimal parameters θ∗ and ϕ∗ to minimize the loss function. To put this in a formal notation, for dataset D the optimal parameters are: 
θ∗, ϕ∗ = argmin θ,ϕ 
∑ x∈D 
L(x, gϕ(fθ(x))). (2.5) 
Representation Learning with Variational Autoencoders Variational Autoencoders (VAEs) (Kingma and Welling, 2014) introduce a probabilistic perspective to the encoding and decoding process. This allows the model to capture the data probabilistically and map it to a simple latent distribution (typically a Gaussian), making VAEs a powerful tool for unsupervised representation learning. In addition, a common modeling choice for VAEs is to set the covariance matrix of the latent distribution to be diagonal, forcing additional structure in the latent space and encouraging disentanglement of the learned representations (Rolinek et al., 2019). 
In a VAEs, the encoder network fθ maps an input x to a distribution over the latent space. To achieve this, the encoder outputs the parameters of the distribution, such as the mean µ 
and standard deviation σ: (µ, log σ) = fθ(x). The decoder network in a VAE is similar to that of a traditional autoencoder. It maps a point in the latent space back to the input space, attempting to reconstruct the original input. However, instead of receiving a deterministic point in the latent space, the decoder receives a sample z drawn from the encoder-defined distribution. This mapping is given by x̂ = gϕ(z), where z ∼ N (µ, diag(σ2)). 
The training objective of VAEs, known as the evidence lower bound (ELBO), aims to maximize the data’s log-likelihood while also ensuring that the latent space distribution closely approximates a true posterior: 
Lθ,ϕ(x) = log pθ(x) − DKL(qϕ(z | x)∥pθ(z | x)) (2.6) 
where DKL is the Kullback-Leibler divergence, qθ(z|x) is the distribution defined by the encoder, and p(z | x) is the true posterior distribution. As DKL is non-negative, the ELBO is a lower bound on the marginal likelihood of datapoint x. It can also be written as: 
Lθ,ϕ(x) = Eqϕ(z|x)[log pθ(x | z)] − DKL(qϕ(z | x)∥pθ(z)) (2.7) 
17
Chapter 2. Background 
The first term in the ELBO encourages the VAE decoder to accurately reconstruct the input, while the second term encourages the distribution over the latent space to be close to the (structured) prior. The overall objective for the dataset D is the sum of the individual-datapoint ELBO’s: 
θ∗, ϕ∗ = argmax θ,ϕ 
∑ x∈D 
Lθ,ϕ(x) (2.8) 
Further variants of VAEs (Higgins et al., 2017a; Chen et al., 2018b; Kim and Mnih, 2018) modify the regularization term to force more disentanglement (Bengio et al., 2013) in the latent space. This shows a common pattern in structured representation learning: a general objective such as reconstruction enforces the representation to be informative of the inputs, while additional objectives or architectural biases and bottlenecks encourage that the information about the input is stored in a specific way. 
Self-Supervised Representation Learning Although reconstruction-based representa-tion learning is broadly applicable across various data domains, the learned representations may not always be beneficial for downstream tasks (Liu et al., 2021). For example, learning to reconstruct the input image in the pixel space does not necessarily result in a representa-tion that is useful for downstream tasks such as classification or manipulation of the small objects present in the image. In those situations, it is beneficial to learn a representation that contains only the main information about the input data, while being invariant to the irrelevant factors of variation (Bengio et al., 2013). 
While for arbitrary data it is not possible to know in advance which factors of variation are irrelevant, in the case of specific data domains such as images, it is possible to use the structure of the image to define such factors. To achieve this, self-supervised representation learning leverages input data itself as supervision to learn representations that are useful for many diverse downstream tasks. The examples of such tasks are instance discrimination (Chen et al., 2020b), soft clustering (Caron et al., 2021) and partial input reconstruction (He et al., 2022). 
2.2.2 Compositional Representation Learning 
Motivation Although learning disentangled representations of the scene is a helpful first step in enforcing structure in the latent space, it is not enough to capture the compositional nature of natural and realistic data (Locatello et al., 2020). The generative process of natural 
18
2.2. Unsupervised Structured Representation Learning 
color color color 
Figure 2.4: Illustration of the binding problem. While it is possible to represent each object simultaneously in a consistent format, the representation of the pair of objects using a fixed-length representation is problematic. 
data can be described as the composition of different objects or entities into one scene. The challenge lies in the fact that the number of entities is not known in advance, while properties of the entities often have similar structures. For example, imagine an agent that learned to manipulate an object from visual observations of the environment. One would expect that the agent would be able to control this object in case an additional object is added to the scene. However, it is unclear how to represent a scene with two objects in the same format, as the minimal disentangled representation would have a different dimensionality. 
Even a disentangled fixed-length vector representation is insufficient to represent complex and realistic data in a form that is useful for planning and control. Fixed-length representa-tions cannot represent the scene parts consistently nor allow compositional generalization to unseen scenes composed from similar objects (Dittadi et al., 2022). This limitation is known as the binding problem (Greff et al., 2016) (see Figure 2.4 for a simple example with two objects that illustrate the binding problem in the visual domain). 
The binding problem is the challenge of dynamically and flexibly integrating, or “binding”, information that’s distributed across the network (Greff et al., 2016). To overcome this, we need more than just learning fixed or dense features of the scene. We need a flexible interface module that can connect dense features with a discrete set of object representations in the scene. This interface is essential for the effective representation of objects in the scene that are useful for dynamics learning and control (Battaglia et al., 2016; Santoro et al., 2017; Watters et al., 2019a; Kipf et al., 2020). 
Unsupervised Object-Centric Learning A common approach to compositional repre-sentation learning is to extend the autoencoder or VAE framework to model a scene as 
19
Chapter 2. Background 
a composition of objects (Eslami et al., 2016; Locatello et al., 2020), known as unsuper-vised object-centric learning. Object-centric methods introduce a latent representation for each object in the scene and modify the decoder to generate the scene by composing the representations of the individual objects. 
The encoder function fθ, maps an input scene x ∈ RD to a set of latent representations Z = {z1, z2, ..., zN}. Here, N is the number of objects in the scene, and each zi ∈ Rd 
represents the i-th object. Formally, this mapping is given by Z = fθ(x). Next, the latent representation is transformed by the decoder to predict the target for the current input scene x. The decoder function gϕ then maps each latent representation zi to an object in the input space and composes these objects to reconstruct the original scene. Formally, this mapping is given by x̂ = gϕ(Z). The encoder and decoder are parameterized by ϕ and θ. 
The reconstruction objective alone doesn’t encourage the model to separate information across slots. Therefore, we need additional inductive biases to learn representations that match each object in the scene (Burgess et al., 2019; Weis et al., 2021; Locatello et al., 2020; Brady et al., 2023). One way to add such inductive biases is by designing a decoder function that facilitates scene decomposition. For example, in the case of images, the decoder could be designed to reconstruct the scene by composing the objects in the scene, while using only a particular slot for each object reconstruction. This could be achieved by using a Spatial Broadcast Decoder (Watters et al., 2019b) to transform the object representations into the scene space. 
Self-Supervised Object-Centric Learning Similar to traditional representation learn-ing methods of fixed-length vector representations, object-centric methods can be trained not only by reconstructing their inputs but also in a self-supervised way by predicting targets that are not directly present in the input, but could be extracted from data without human supervision (Kipf et al., 2022; Elsayed et al., 2022; Baldassarre and Azizpour, 2022; Bao et al., 2022; Seitzer et al., 2023; Zadaianchuk et al., 2023a). 
A natural and realistic source of such targets for self-supervised, object-centric learning is the motion cues derived from video data (Kipf et al., 2022; Elsayed et al., 2022; Bao et al., 2022; Tangemann et al., 2023; Zadaianchuk et al., 2023a). The principle of common fate (Wertheimer, 2012), a Gestalt psychology concept, can be applied here. This principle suggests that objects moving in the same direction and at the same speed are perceived as a group and separate from their surroundings. In object-centric learning, this could mean 
20
2.2. Unsupervised Structured Representation Learning 
identifying and grouping pixels or features that share common motion patterns, thereby facilitating the discovery of object representations (Tangemann et al., 2023). 
Going Beyond Set-Based Representations While representing the scene as a set of independent vectors is more flexible than fixed-based representations such representations assume that objects do not interact with each other. This assumption is useful for the initial discovery of the objects in a particular observation, however, could be harmful in cases when we are interested in using such representations to control objects or to plan in such a compositional latent space. For instance, in a robotic arm assembly task, where the robot needs to pick and place different components, relying solely on independent vector representations might lead to a lack of coordination among the robot’s movements, as the vectors do not encapsulate the physical constraints and interactions between the components. For such downstream tasks, an accurate dynamical model of the environment is required. 
One can learn a fixed mapping of the set to another set as the latent dynamical model. How-ever, such an approach has similar limitations as the fixed-length representation of the state: one cannot rely on such a learned transformation for out-of-distribution (OOD) environ-ments, limiting the applicability of initially flexible object-centric representation to model real-world compositional environments. Thus, more general methods that can discover the relational structure of the environmental entities are needed (Adjodah et al., 2018). 
The discovery of the relation structure in the environment could be done by representing an observation in the environment as a graph G = (V , E) (Kipf and Welling, 2017; Kipf et al., 2018), where the nodes V represent entities, and the edges E represent relations between entities. Using such a representation allows us to generalize possible relations between entities and effectively reuse observations of some interactions to infer similar interactions between different entities. Recently, several methods to estimate such relational structure in an unsupervised way were proposed (Kipf et al., 2018; Steenkiste et al., 2018; Kipf et al., 2020; Li et al., 2020; Blaes et al., 2019). Most of those methods assume a given object-centric representation, while joint learning of entities and their relational structure from raw data remains an open problem. 
2.2.3 Object-Centric Learning Methods 
There are various approaches to object separation in object-centric learning (OCL) methods. Most OCL methods separate the objects into different latent vectors or slots. Greff et al. 
21
Chapter 2. Background 
(2020) propose to classify them by the mechanism of object separation to instance, category slots, and to sequential and spacial slots. The difference between these representation methods is further explained and schematically depicted in Figure 2.5. Below, we describe those methods using instance slots and spatial slots that are most relevant to this thesis. 
4321 
Instance slots Sequential slots Spacial slots Category slots 
Figure 2.5: Classification of object-centric representations by the scene separation criteria. Instance slots represent non-overlapping parts of the scene. Each slot bins to one of the objects in the scene without specific preference. In contrast, sequential slots are assigned one by one by explaining those parts of the scene that still need to be explained. Spatial slots bind to representations at particular locations in the image. Finally, categorical slots represent scenes based on the object category. The figure is adapted from Greff et al. (2020). 
2.2.3.1 OCL with Instance Slots 
In the case of instance slots, all slots follow a standard format, yet their data remains separate, i.e. each slot represents a part of the scene. To achieve full scene decomposition, communication between slots is needed as they are initialized identically as samples from the same Gaussian distribution. Slot Attention autoencoders (Locatello et al., 2020), SAVi (Kipf et al., 2022) and DINOSAUR (Seitzer et al., 2023) are using instance slots, where the communication is achieved with the Slot Attention module (Locatello et al., 2020). 
Slot Attention (Locatello et al., 2020) Slot Attention (SA) is a method for learning object-centric representations of images. In contrast with standard autoencoders, the SA encoder consists of two modules: a CNN to produce a dense representation of the scene, i.e. where each pixel or patch has an assigned vector, followed by the Slot Attention module, which groups CNN features into a set of slots through an iterative refinement process. In each iteration, dot-product attention is computed by utilizing the dense CNN 
22
2.2. Unsupervised Structured Representation Learning 
representations as keys and the current slot vectors as queries. Normalizing attention weights over slots creates a competition among them to explain the input. Next, slots are updated using a gated recurrent unit (GRU) with current slots and updated values provided as inputs. This iterative competition process ensures that each image pixel is uniquely associated with a single slot, effectively separating and identifying distinct objects within the scene, which aligns with the natural way images are typically composed and perceived Similar to previous methods (Greff et al., 2019; Burgess et al., 2019), a spatial broadcast decoder (Watters et al., 2019b) is used to reconstruct the original image by alpha compositing the reconstruction from each slot with a corresponding mask that is additionally reconstructed by the decoder. The model is trained by minimizing the MSE reconstruction loss. 
Slot Attention for Video (SAVi) (Kipf et al., 2022) SAVi is an extension of the Slot Attention method to the video domain. One of the main challenges for object-centric learning on videos is to learn representations that are consistent through video frames. To tackle this challenge, SAVi introduces a recurrent slot attention module. This module operates similarly to the original SA module. However, its initialization is modified to produce consistent representations between frames. Specifically, the slot initialization for frame t is obtained by transforming the slot representations from frame t − 1 using a transformer predictor module. 
DINOSAUR (Seitzer et al., 2023) As Slot Attention was shown to work only with synthetic datasets of limited complexity, we propose to exploit additional inductive biases extractable from natural images without supervision. We hypothesize that the main challenge for SA scalability issues is the pixel-level reconstruction loss as it produces too weak of a signal for object-centricness to emerge on real-world datasets with complex objects and backgrounds. We propose to first extract semantically more meaningful dense self-supervised features (Chen et al., 2020b; Grill et al., 2020; He et al., 2022) from the images and use them as an (unsupervised) signal to reconstruct. Such self-supervised features were shown to be powerful representations for classical vision tasks such as classification and object detection using fine-tuning or linear head training on top of them. We show that they can also be useful without any additional supervision if used as reconstruction targets in object-centric models. 
23
Chapter 2. Background 
2.2.3.2 OCL with Spatial Slots 
Spatial slots are specific to certain spatial coordinates within an image or frame of the video. This specificity aids in breaking slot symmetries as each slot is responsible for a particular part of the image. However, it also adds more challenges in producing consistent slots in time if objects’ locations change significantly between frames. Below, we cover the SPACE (Lin et al., 2020) and SCALOR (Jiang et al., 2020) models that use parallel spatial-attention and additionally structured latent representations allowing to scale object-centric methods to many objects. 
SPACE (Lin et al., 2020) SPACE introduces a method to process objects in the foreground that can be represented within bounding boxes. By leveraging parallel spatial-attention, it efficiently differentiates these foreground objects. Concurrently, it decomposes areas containing background segments using component mixtures. This means SPACE not only offers a disentangled depiction of the objects at the forefront, emphasizing attributes like their position and size, but also decomposes background components into parts. 
SCALOR (Jiang et al., 2020) SCALOR is a probabilistic generative world model for learning object-centric representations of a video or stream of high-dimensional environment observations. SCALOR assumes that the environment observation ot at step t is generated by the background latent variable zbg 
t and the foreground latent variable zfg t . The foreground 
is further factorized into a set of object representations zfg t = {zt,n}n∈Ot , where Ot is the 
set of recognised object indices. To combine the information from previous time steps, a propagation-discovery model is used (Kosiorek et al., 2018). In SCALOR, an object is represented by zt,n = 
( zpres t,n , zwhere 
t,n , zwhat t,n 
) . The boolean random variable zpres 
t,n defines if the object is present in the scene, whereas the vector zwhat 
t,n encodes object appearance. The component zwhere 
t,n is further decomposed into the object’s center position zpos t,n , scale zscale 
t,n , and depth zdepth 
t,n . With this, the generative process of SCALOR can be written as: 
p(o1:T , z1:T ) = p(zD 1 )p(zbg 
1 ) T∏ t=2 
p(ot | zt)︸ ︷︷ ︸ rendering 
p(zbg t | zbg 
<t, zfg t )︸ ︷︷ ︸ 
background transition 
p(zD t | zP 
t )︸ ︷︷ ︸ discovery 
p(zP t | z<t)︸ ︷︷ ︸ 
propagation 
, (2.9) 
where zt = (zbg t , zfg 
t ), zD t contains latent variables of objects discovered in the present step, 
and zP t contains latent variables of objects propagated from the previous step. Due to 
24
2.2. Unsupervised Structured Representation Learning 
the intractability of the true posterior distribution p(z1:T |o1:T ), SCALOR is trained using variational inference with the following posterior approximation: 
q(z1:T | o1:T ) = T∏ t=1 
q(zt | z<t, o≤t) = T∏ t=1 
q(zbg t | zfg 
t , ot) q(zD t | zP 
t , o≤t) q(zP t | z<t, o≤t), 
(2.10) by maximizing the following evidence lower bound L(θ, ϕ): 
L(θ, ϕ) = T∑ t=1 
Eqϕ(z<t|o<t) 
[ Eqϕ(zt|z<t,o≤t) 
[ log pθ(ot | zt) 
] −DKL 
[ qϕ(zt | z<t, o≤t) ∥ pθ(zt | z<t) 
]] , 
where DKL denotes the Kullback-Leibler divergence. 
In Chapter 3, we use SCALOR to represent both environment observations and goal images. As we are using SCALOR in an active setting, we additionally condition the next step posterior predictions on the actions at taken by the agent. For more details and hyperparameters used to train SCALOR, we refer to Appendix A.4.3. 
2.2.4 Evaluation of Structure Discovery 
As the discovery of structure (both disentanglement and object-centricness) is not directly supervised, there is no straightforward methodology to evaluate the performance of the methods in structured representation learning. While the final usefulness for solving downstream tasks is a practical and important measure, it mixes how much structure was discovered and how much that structure is useful for a particular downstream task. Thus, it is important to develop task-independent measures of quantifying the discovered structure, for example by comparing it with ground-truth labels, such as factors of variation or object masks. 
Fixed-Length Representations First, for the evaluation of the learned representations disentanglement, several measures have been proposed. Intuitively, for a disentangled representation, each dimension of the learned representation contains information about exactly one of the ground truth factors of variation, while jointly, all the factors are contained in the representation. Below, we describe one practical method for evaluating disentanglement using mutual information (Chen et al., 2018b). 
25
Chapter 2. Background 
Assuming that the underlying factors vk are known, the mutual information between the learned representation component zj and the factor of variation vk can be computed as 
In(zj; vk) = Eq(zj ,vk) 
log ∑ 
xn∈Xvk 
q(zj|xn)p(xn|vk) + H(zj) (2.11) 
where Xvk is the support of generative process p(xn|vk)(Chen et al., 2018b). A larger value 
of mutual information suggests that zj holds significant information about vk. The mutual information reaches its peak when there’s a deterministic, reversible connection between zj and vj. 
As a single factor can be strongly associated with multiple latent variables, one needs to compare mutual information between the underlying factor and different learned repre-sentations to ensure that each latent variable aligns with a distinct factor. For this, the difference between the mutual information values of the top two latent variables (called mutual information gap or MIG) can be compared: 
1 K 
K∑ k=1 
1 H(vk) 
( In(zj(k) ; vk) − max 
j ̸=j(k) In(zj; vk) 
) (2.12) 
Here, j(k) identifies the latent variable that has the maximum mutual information with the factor vk, and K is the total number of recognized factors. Due to normalization by the maximal information value (equal to the entropy H(vk)), mutual information gap values lie between 0 and 1. 
Object-Centric Representations For object-centric representation learning, the main way of evaluating the quality of the learned object representations is by comparing how well the split of the information from the image to slots corresponds to the underlying decomposition of the scene to different objects. 
Scene decomposition can be formulated as the grouping of the pixels in the image into clusters where each cluster corresponds to a unique object. Thus, one can compare the quality of the decomposition by comparing how much the learned decomposition clusters overlap with ground-truth clusters. In this case, ground-truth clusters are pixels from different ground-truth masks of objects provided for the evaluation of the method. To compare the grouping of pixels by the object-centric learning method to the ground-truth masks, we can use the adjusted rand index (ARI) metric. This metric assesses clustering similarity. An ARI value of 1 indicates a perfect alignment, while a value of 0 signifies 
26
2.2. Unsupervised Structured Representation Learning 
similarity equivalent to a random ensemble of clustering (implicitly assuming if the number of clusters or their sizes are fixed (Gates and Ahn, 2017)). As background decomposition could be ambiguous, in most cases, we use foreground ARI (FG-ARI), by excluding background ground-truth masks and evaluating only objects’ masks. 
Next, if we are also interested in evaluating how sharp such object masks are, we can compute a metric based on intersection-over-union (IoU), the mean best overlap (mBO) proposed by Pont-Tuset et al. (2017a). mBO is computed by assigning each ground truth mask the predicted mask with the largest overlap and then averaging the IoUs of the assigned mask pairs. In contrast to ARI, mBO takes background pixels into account, thus also measuring how close masks fit to objects. 
27
3 
Self-Supervised RL with 
Object-Centric Representations 
Autonomous agents need large repertoires of skills to act reasonably on new tasks that they have not seen before. However, acquiring these skills using only a stream of high-dimensional, unstructured, and unlabeled observations is a tricky challenge for any au-tonomous agent. Previous methods have used variational autoencoders to encode a scene into a low-dimensional vector that can be used as a goal for an agent to discover new skills. Nevertheless, in compositional/multi-object environments it is difficult to disentangle all the factors of variation into such a fixed-length representation of the whole scene. We propose to use object-centric representations as a modular and structured observation space, which is learned with a compositional generative world model. We show that the structure in the representations in combination with goal-conditioned attention policies helps the autonomous agent to discover and learn useful skills. These skills can be further combined to address compositional tasks like the manipulation of several different objects. https://github.com/martius-lab/SMORL 
This chapter is based on “Self-supervised Visual Reinforcement Learning with Object-centric Representations” Andrii Zadaianchuk∗, Maximilian Seitzer∗, and Georg Martius ICLR 2021: International Conference on Learning Representations 
29
Chapter 3. Self-Supervised RL with Object-Centric Representations 
3.1 Introduction 
Reinforcement learning (RL) includes a promising class of algorithms that have shown capability to solve challenging tasks when those tasks are well specified by suitable reward functions. However, in the real world, people are rarely given a well-defined reward function. Indeed, humans are excellent at setting their own abstract goals and achieving them. Agents that exist persistently in the world should likewise prepare themselves to solve diverse tasks by first constructing plausible goal spaces, setting their own goals within these spaces, and then trying to achieve them. In this way, they can learn about the world around them. 
In principle, the goal space for an autonomous agent could be any arbitrary function of the state space. However, when the state space is high-dimensional and unstructured, such as only images, it is desirable to have goal spaces that allow efficient exploration and learning, where the factors of variation in the environment are well disentangled. Recently, unsupervised representation learning has been proposed to learn such goal spaces (Nair et al., 2018; Nair et al., 2020; Pong et al., 2020). Most existing methods before we started this work use variational autoencoders (VAEs) to map observations into a low-dimensional latent space that can later be used for sampling goals and reward shaping. 
However, for complex compositional scenes consisting of multiple objects, the inductive bias of VAEs could be harmful. In contrast, representing perceptual observations in terms of entities has been shown to improve data efficiency and transfer performance on a wide range of tasks (Burgess et al., 2019). Recent research has proposed a range of methods for unsupervised scene and video decomposition (Greff et al., 2017; Kosiorek et al., 2018; Burgess et al., 2019; Greff et al., 2019; Jiang et al., 2020; Weis et al., 2021; Locatello et al., 2020). These methods learn object representations and scene decomposition jointly. The majority of them are in part motivated by the fact that the learned representations are useful for downstream tasks such as image classification, object detection, or semantic segmentation. In this work, we show that such learned representations are also beneficial for autonomous control and reinforcement learning. 
We propose to combine these object-centric unsupervised representation methods that represent the scene as a set of potentially structured vectors with goal-conditional visual RL. In our method (illustrated in Figure 3.1), dubbed SMORL (for self-supervised multi-object RL), a representation of raw sensory inputs is learned by a compositional latent variable model based on the SCALOR architecture (Jiang et al., 2020). We show that 
30
3.1. Introduction 
Goal-conditioned attention policy	 
SCALOR encoder 
Train	SCALOR	on data	from	random 
policy 
Train	SMORL	 with	generated	goals	 
Evaluate	SMORL on	new	tasks	from 
environment 
Figure 3.1: Our proposed SMORL architecture. Representations zt are obtained from observations ot through the object-centric SCALOR encoder qϕ, and processed by the goal-conditional attention policy πθ(at|zt, zg). During training, representations of goals are sampled conditionally on the representations of the first observation z1. At test time, the agent is provided with an external goal image og that is processed with the same SCALOR encoder to a set of potential goals {zn}Nn=1. After this, the goal zg is sequentially chosen from this set. This way, the agent attempts to solve all the discovered sub-tasks one-by-one, not simultaneously. 
using object-centric representations simplifies the goal space learning. Autonomous agents can use those representations to learn how to achieve different goals with a reward function that utilizes the structure of the learned goal space. Our main contributions are as follows: 
 We show that structured object-centric representations learned with generative world models can significantly improve the performance of the self-supervised visual RL agent. 
 We develop SMORL, an algorithm that uses learned representations to autonomously discover and learn useful skills in compositional environments with several objects using only images as inputs. 
 We show that even with fully disentangled ground-truth representation there is a large benefit from using SMORL in environments with complex compositional tasks such as rearranging many objects. 
31
Chapter 3. Self-Supervised RL with Object-Centric Representations 
3.2 Related work 
Our work lies in the intersection of several actively evolving topics: visual reinforcement learning for control and robotics, and self-supervised learning. Vision-based RL for robotics is able to efficiently learn a variety of behaviors such as grasping, pushing and naviga-tion (Levine et al., 2016; Pathak et al., 2018; Levine et al., 2018; Kalashnikov et al., 2018) using only images and rewards as input signals. Self-supervised learning is a form of unsupervised learning where the data provides the supervision. It was successfully used to learn powerful representations for downstream tasks in natural language processing (Devlin et al., 2019; Radford et al., 2019) and computer vision (He et al., 2020; Chen et al., 2020c). In the context of RL, self-supervision refers to the agent constructing its own reward signal and using it to solve self-proposed goals (Baranes and Oudeyer, 2013; Nair et al., 2018; Péré et al., 2018; Hausman et al., 2018; Lynch et al., 2019). This is especially relevant for visual RL, where a reward signal is usually not naturally available. These methods can potentially acquire a diverse repertoire of general-purpose robotic skills that can be reused and combined during test time. Such self-supervised approaches are crucial for scaling learning from narrow single-task learning to more general agents that explore the environment on their own to prepare for solving many different tasks in the future. Next, we will cover the two most related lines of research in more detail. 
Self-supervised visual RL (Nair et al., 2018; Nair et al., 2020; Pong et al., 2020; Ghosh et al., 2019; Warde-Farley et al., 2019; Laversanne-Finot et al., 2018) tackles multi-task RL problems from images without any external reward signal. However, all previous methods assume that the environment observation can be encoded into a single vector, e.g. using VAE representations. With multiple objects being present, this assumption may result in object encodings overlapping in the representation, which is known as the binding problem (Greff et al., 2016; Greff et al., 2020). In addition, as the reward is also constructed based on this vector, the agent is incentivized to solve tasks that are incompatible, for instance simultaneously moving all objects to goal positions. In contrast, we suggest to learn object-centric representations and use them for reward shaping. This way, the agent can learn to solve tasks independently and then combine these skills during evaluation. 
Learning object-centric representations in RL (Watters et al., 2019a; Steenkiste et al., 2019; Veerapaneni et al., 2019; Kipf et al., 2020) has been suggested to approach tasks with combinatorial and compositional elements such as the manipulation of multiple objects. However, the previous work has assumed a fixed, single task and a given reward 
32
3.2. Related work 
signal, whereas we are using the learned object-representations to construct a reward signal that helps to learn useful skills that can be used to solve multiple tasks. In addition, these methods use scene-mixture models such as MONET (Burgess et al., 2019) and IODINE (Greff et al., 2019), which do not explicitly contain features like position and scale. These features can be used by the agent for more efficient sampling from the goal space and thus the explicit modeling of these features helps to create additional biases useful for manipulation tasks. However, we expect that other object-centric representations could also be successfully applied as suitable representations for RL tasks. 
33
Chapter 3. Self-Supervised RL with Object-Centric Representations 
3.3 Self-Supervised Multi-Object Reinforcement Learn-ing 
Learning from flexible representations obtained from unsupervised scene decomposition methods such as SCALOR creates several challenges for RL agents. In particular, these representations consist of sets of vectors, whereas standard policy architectures assume fixed-length state vectors as input. We propose to use a goal-conditioned attention policy that can handle sets as inputs and flexibly learns to attend to those parts of the representation needed to achieve the goal at hand. 
In the setting we consider, the agent is not given any reward signal or goals from the environment at the training stage. Thus, to discover useful skills that can be used during evaluation tasks, the agent needs to rely on self-supervision in the form of an internally constructed reward signal and self-proposed goals. Previous VAE-based methods used latent distances to the goal state as the reward signal. However, for compositional goals, this means that the agent needs to master the simultaneous manipulation of all objects. In our experiments in Section 3.4.1, we show that even with fully disentangled, ground-truth representations of the scene, this is a challenging setting for previous state-of-the-art model-free RL agents. Instead, we propose to use the discovered structure of the learned goal and state spaces twofold: the structure within each representation, namely object position and appearance, to construct a reward signal, and the set-based structure between representations to construct sub-goals that correspond to manipulating individual objects. 
3.3.1 Policy with Goal-conditioned Attention 
We use the multi-head attention mechanism (Vaswani et al., 2017) as the first stage of our policy πθ to deal with the challenge of set-based input representations. As the policy needs to flexibly vary its behavior based on the goal at hand, it appears sensible to steer the attention using a goal-dependent query Q(zg) = zgW q. Each object is allowed to match with the query via an object-dependent key K(zt) = ztW k and contribute to the attention’s output through the value V (zt) = ztW v, which is weighted by the similarity between Q(zg) and K(zt). As inputs, we concatenate the representations for object n to vectors zt,n = [zwhat 
t,n ; zwhere t,n ; zdepth 
t,n ], and similarly the goal representation to zg = [zwhat g ; zwhere 
g ; zdepth g ]. 
34
3.3. Self-Supervised Multi-Object Reinforcement Learning 
The attention head Ak is computed as 
Ak = softmax ( 
zgW q(ZtW k)T√ 
de 
) ZtW 
v, (3.1) 
where Zt is a packed matrix of all zt,n’s, W q, W k, W v constitute learned linear transforma-tions and de is the common key, value and query dimensionality. The final attention output A is a concatenation of all the attention heads A = [A1; . . . ; AK ]. In general, we expect it to be beneficial for the policy to not only attend to entities conditional on the goal; we thus let some heads attend based on a set of input independent, learned queries, which are not conditioned on the goal. We go into more details about the attention mechanism in Appendix A.4.1 and ablate the impact of different choices in Appendix A.2. 
The second stage of our policy is a fully-connected neural network f that takes as inputs A and the goal representation zg and outputs an action at. The full policy πθ can thus be described by 
πθ({zt,n}n∈Ot , zg) = f(A, zg). (3.2) 
3.3.2 Self-Supervised Training 
In principle, our policy can be trained with any goal-conditional model-free RL algorithm. For our experiments, we picked soft-actor critic (SAC) (Haarnoja et al., 2018) as a previous state-of-the-art method for continuous action spaces, using hindsight experience replay (HER) (Andrychowicz et al., 2017) as a standard way to improve sample-efficiency in the goal-conditional setting. 
The training algorithm is summarized in Alg. 1. We first train SCALOR on data collected from a random policy and fit a distribution p(zwhere) to representations zwhere of collected data. Each rollout, we generate a new goal for the agent by picking a random zwhat from the initial observation z1 and sampling a new zwhere from the fitted distribution p(zwhere). The policy is then rolled out using this goal. During off-policy training, we are relabeling goals with HER, and, similar to RIG (Nair et al., 2018), also with “imagined goals” produced in the same way as the rollout goals. 
A challenge with compositional representations is how to measure the progress of the agent towards achieving the chosen goal. As the goal always corresponds to a single object, we have to extract the state of this object in the current observation in order to compute a reward. One way is to rely on the tracking of objects, as was shown possible e.g. by 
35
Chapter 3. Self-Supervised RL with Object-Centric Representations 
Algorithm 1 SMORL: Self-Supervised Multi-Object RL (Training) Require: SCALOR encoder qϕ, goal-conditional policy πθ, goal-conditional SAC trainer, number of 
training episodes K. 1: Train SCALOR on sequences uniformly sampled from D using loss described in Eq. 2.2.3.2. 2: Fit prior p(zwhere | zwhat) to the latent encodings of observations. 3: for n = 1, ..., K episodes 4: Sample goal zg = 
( ẑwhere 
g , zwhat g 
) . 
5: Collect episode data with policy πθ(at | zt, zg) and SCALOR representations of observations qϕ(zt | z<t, o≤t). 
6: Store transitions (zt, at, zt+1, zg) into replay buffer R. 7: Sample transitions from replay buffer (z, a, z′, zg) ∼ R. 8: Relabel zwhere 
g goal components to a combination of future states and p(zwhere | zwhat). 9: Compute matching reward signal R = r(z′, zg). 
10: Update policy πθ(at | zt, zg) using R with SAC trainer. We also refer to Alg. 4 in Appendix A.4.2 for a more detailed description of the algorithm. 
SCALOR (Jiang et al., 2020). However, as the agent learns, we noticed that it would discover some flaws of the tracking and exploit them to get a maximal reward that is not connected with environment changes, but rather with internal vision and tracking flaws (details in Appendix A.5). 
We follow an alternative approach, namely to use the zwhat component of discovered objects and match them with the current goal representation zwhat 
g . As the zwhat space encodes the appearance of objects, two detections corresponding to the same object should be close in this space (we verify that this hypothesis holds in Appendix A.1.1). Thus, it is easy to find the object corresponding to the current goal object using the distance mink ||zwhat 
k − zwhat g ||. 
In case of failure to discover a close representation, i.e. when all zwhat k have a distance larger 
than some threshold α to the goal representation zwhat g , we use a fixed negative reward 
rno_goal to incentivise the agent to avoid this situation. 
Our reward signal is thus 
r(z, zg) = 
−||zwhere k̂ 
− zwhere g || if mink ||zwhat 
k − zwhat g || < α, 
rno_goal otherwise, (3.3) 
where k̂ = arg mink ||zwhat k − zwhat 
g ||. 
36
3.4. Experiments 
3.3.3 Composing Independent Subgoals during Evaluation 
At evaluation time, the agent receives a goal image from the environment showing the state to achieve. The goal image is processed by SCALOR to yield a set of goal vectors. For our experiments, we assume that these sub-goals are independent of each other and that the agent can thus sequentially achieve them by cycling through them until all of them are solved. The evaluation algorithm is summarized in Alg. 5, with more details added in Appendix A.4.2. 
3.4 Experiments 
We have done computational experiments to address the following questions: 
 How well does our method scale to challenging tasks with a large number of objects in case when ground-truth representations are provided? 
 How does our method perform compared to prior visual goal-conditioned RL methods on image-based, multi-object continuous control tasks? 
 How suitable are the representations learned by the compositional generative world model for discovering and solving RL tasks? 
To answer these questions, we constructed the Multi-Object Visual Push and Multi-Object Visual Rearrange environments. Both environments are based on MuJoCo (Todorov et al., 2012) and the Multiworld package for image-based continuous control tasks introduced by Nair et al. (2018), and contain a 7-dof Sawyer arm where the agent needs to be controlled to manipulate a variable number of small pucks on a table. In the first environment, the objects are located on fixed positions in front of the robot arm that the arm must push to random target positions. We included this environment as it largely corresponds to the Visual Pusher environments of Nair et al. (2018). In the second environment, the task is to rearrange the objects from random starting positions to random target positions. This task is more challenging for RL algorithms due to the randomness of initial object positions. For both environments, we measure the performance of the algorithms as the average distance of all pucks to their goal positions on the last step of the episode. 
37
Chapter 3. Self-Supervised RL with Object-Centric Representations 
(a) View from top (b) Agent observation 
Figure 3.2: Multi-Object Visual Push and Rearrange environments with 2 objects and a Sawyer robotic arm. 
3.4.1 SMORL with ground-truth (GT) state representation 
We first compared SMORL with ground-truth representation with Soft Actor-Critic (SAC) with Hindsight Experience Replay (HER) relabeling (Andrychowicz et al., 2017) that takes an unstructured vector of all objects coordinates as input. We are using a one-hot encoding for object identities zwhat and object and arm coordinates as zwhere components. With such a representation, the matching task becomes trivial, so our main focus in this experiment is on the benefits of the goal-conditioned attention policy and the sequential solving of independent sub-tasks. We show the results in Figure 3.3. While for 2 objects, SAC+HER is performing similarly, for 3 and 4 objects, SAC+HER fails to rearrange any of the objects. In contrast, SMORL equipped with ground-truth representation is still able to rearrange 3 and 4 objects, and it can solve the more simple sub-tasks of moving each object independently. This shows that provided with good representations, SMORL can use them for constructing useful sub-tasks and learn how to solve them. 
3.4.2 Visual RL Methods Comparison 
We compare the performance of our algorithm with two other self-supervised, multi-task visual RL algorithms on our two environments, with one and two objects. The first one, RIG (Nair et al., 2020), uses the VAE latent space to sample goals and to estimate the reward signal. The second one, Skew-Fit (Pong et al., 2020), also uses the VAE latent space, however, is additionally biased on rare observations that were not modeled well by the VAE on previously collected data. In terms of computational complexity, both our method and RIG need to train a generative model before RL training. We note that 
38
3.4. Experiments 
0 1 2 3 4 5 
Timesteps ×105 
0.075 
0.100 
0.125 
0.150 
0.175 
0.200 
A vg 
.o bj 
ec td 
is t. 
2 objects 
0 1 2 3 4 5 
Timesteps ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
3 objects 
0 1 2 3 4 5 
Timesteps ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
4 objects 
SMORL+GT SAC+GT Passive policy 
Figure 3.3: Average distance of objects to goal positions, comparing SMORL using ground truth representations to SAC with ground truth representations in the Rearrange environ-ment with different number of objects. SAC struggles to improve performance when the combinatorial complexity of the scene rises. The dotted line indicates the performance of a passive policy that performs no movements. Results averaged over 5 random seeds, shaded regions indicate one standard deviation. 
training SCALOR is more costly than training RIG’s VAE due to the sequence processing utilized by SCALOR. However, once trained, SCALOR only adds little overhead compared to RIG’s VAE during RL training, and compared to Skew-Fit, our method is still faster to train as Skew-Fit needs to continuously retrain its VAE. 
We show the results in Figure 3.4. For the simpler Multi-Object Visual Push environment, the performance of SMORL is comparable to the best performing baseline, while for the more challenging Multi-Object Visual Rearrange environment, SMORL is significantly better then both RIG and Skew-Fit. This shows that learning of object-oriented representations brings benefits for goal sampling and self-supervised learning of useful skills. However, our method is still significantly worse than SAC with ground-truth representations. We hypothesize that one reason for this could be that SCALOR right now does not properly deal with occluded objects, which makes the environment partially observable from the point of view of the agent. On top of this, we suspect noise in the representations, misdetections and an imperfect matching signal to slow down training and ultimately hurt performance. Thus, we expect that adding recurrence to the policy or improving SCALOR itself could help close the gap to an agent with perfect information. 
39
Chapter 3. Self-Supervised RL with Object-Centric Representations 
Visual Push 
0.0 0.5 1.0 1.5 2.0 2.5 3.0 
Timesteps ×105 
0.025 
0.050 
0.075 
0.100 
0.125 
0.150 
A vg 
.o bj 
ec td 
is t. 
1 object 
0.0 0.5 1.0 1.5 2.0 2.5 3.0 
Timesteps ×105 
0.02 
0.04 
0.06 
0.08 
0.10 
0.12 
2 objects 
Visual Rearrange 
0.0 0.5 1.0 1.5 2.0 2.5 3.0 
Timesteps ×105 
0.050 
0.075 
0.100 
0.125 
0.150 
0.175 
0.200 
A vg 
.o bj 
ec td 
is t. 
1 object 
0 1 2 3 4 
Timesteps ×105 
0.08 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
2 objects 
SMORL RIG Skew-Fit SAC+GT Passive policy 
Figure 3.4: Average distance of objects to goal positions, comparing SMORL to Visual RL Baselines. In addition to the baselines, we show SAC’s performance with ground truth representations. Results averaged over 5 random seeds, shaded regions indicate one standard deviation. 
3.4.3 Out-of-Distribution Generalization for different number of objects 
One important advantage of structured policies is that they could potentially still be applicable for observations that are from different, but related distributions. Standard visual RL algorithms were shown to be sensitive to small changes unrelated to the current task (Higgins et al., 2017b). To see how our algorithm can generalize to a changing 
40
3.5. Conclusion and Future Work 
environment, we tested our SMORL agent trained on observations of the Rearrange environment with 2 objects on the environment with 1 object. As can be seen from Figure 3.5, the performance of such an agent increases during training up to a performance comparable to a SMORL agent that was trained on the 1 object environment. 
0.0 0.2 0.4 0.6 0.8 
Training examples ×106 
0.10 
0.12 
0.14 
0.16 
0.18 
A vg 
.o bj 
ec td 
is t. 
1 object environment 
SMORL (2 objects) SMORL (1 object) 
Figure 3.5: Out-of-distribution generalization of SMORL agent training on Visual Rearrange with two objects and being tested with one object. Green line shows final performance when training with one object. 
3.5 Conclusion and Future Work 
In this chapter, we have shown that discovering structure in the observations of the environment with a compositional generative world models and using it for controlling different parts of the environment is crucial for solving tasks in compositional environments. Learning to manipulate different parts of object-centric representations is a powerful way to acquire useful skills such as object manipulation. Our SMORL agent learns how to control different entities in the environment and can then combine the learned skills to achieve more complex compositional goals such as rearranging several objects using only the final image of the arrangement. 
Limitations and Future Work Directions Given the results presented so far, there are a number of interesting directions to take this work. First, one can combine learned sub-tasks with a planning algorithm to achieve a particular goal. Currently, the agent is simply sequentially cycling through all discovered sub-tasks, so we expect that a more 
41
Chapter 3. Self-Supervised RL with Object-Centric Representations 
complex planning algorithm as e.g. described by Nasiriany et al. (2019) could allow for solving more challenging tasks and improve the overall performance of the policy. To this end, considering interactions between objects in the manner of Kipf et al. (2018) or Kipf et al. (2020) could help to lift the assumption of independence of sub-tasks. In the next chapter, we address this limitation by introducing a novel self-supervised framework SRICS (Zadaianchuk et al., 2022) that overcomes the limitations of SMORL. This approach enables agents to understand and exploit the relationships between objects, allowing for more effective learning and application of manipulation tasks in dynamic multi-object environments. Additionally, Haramati et al. (2023) studied how object interaction can be handled with object-centric latent representation learned with Deep Latent Particles (Daniel and Tamar, 2023), whereas STEDIE (Nakano et al., 2023) separates object features into those relevant for interactions and those not, improving planning performance. 
There are several methods that additionally extend SMORL to different settings. The SMORL policy, based on unique object identities, is effective for limited objects but may falter with diverse object interactions, underscoring the need for advanced object representations that separate attributes and assist in categorization (Yi et al., 2022). Finer representations could enhance reinforcement learning efficiency, and class-based object-centric approaches have shown promise in model-based reinforcement learning (Feng and Magliacane, 2023). Exploration with object-centric representation is studied in detail in Sancaktar et al. (2022). Finally, Yoon et al. (2023) and Nath et al. (2023) study the usefulness of object-centric representation while Mambelli et al. (2022) shows the benefits of using attention-based goal-conditional policies in different RL settings. 
42
4 
RL with Independently Controllable 
Subgoals 
To successfully tackle challenging manipulation tasks, autonomous agents must learn a diverse set of skills and how to combine them. Recently, self-supervised agents that set their own abstract goals by exploiting the discovered structure in the environment were shown to perform well on many different tasks (Colas et al., 2019; Watters et al., 2019a; Veerapaneni et al., 2019; Zadaianchuk et al., 2021). In particular, in the previous chapter, we showed that SMORL (Zadaianchuk et al., 2021) can be applied to learn basic manipulation skills in compositional multi-object environments. However, SMORL learns skills without taking the dependencies between objects into account. Thus, the learned skills are difficult to combine in realistic environments. We propose a novel self-supervised agent that estimates relations between environment components and uses them to independently control different parts of the environment state. We show that, by using this framework, an agent can efficiently and automatically learn manipulation tasks in multi-object environments with different relations between objects. https://github.com/zadaianchuk/SRICS 
This chapter is based on “Self-supervised Reinforcement Learning with Independently Controllable Subgoal” Andrii Zadaianchuk, Georg Martius, and Fanny Yang CoRL 2022: Conference on Robot Learning 
43
Chapter 4. RL with Independently Controllable Subgoals 
4.1 Introduction 
Autonomous agents that need to solve manipulation tasks in environments with many objects have to master a variety of skills. In addition, such agents should be able to properly combine these skills to solve complex tasks. In modular environments, the agent must explore many different ways how it can control the environment (Colas et al., 2022). Self-supervised agents that imagine their own goals can automate this process, and learn many skills without external reward signals (Colas et al., 2022; Nair et al., 2018; Pong et al., 2020; Nair et al., 2020; Florensa et al., 2018; Aubret et al., 2021; Akakzia et al., 2021). One of the main challenges for goal-based autonomous agents is the choice of a suitable goal space and the corresponding reward function (Colas et al., 2019). As this choice determines the difficulty of the learning, it is crucial to exploit all available structure in the environment state for construction of the goal space. 
One natural way to represent the state in modular environments is to use an object-centric representation: the environment state is represented as a set of components, with each component corresponding to the state of an individual object (Veerapaneni et al., 2019; Zadaianchuk et al., 2021; Devin et al., 2018). Such representations can be learned in an unsupervised fashion from high-dimensional observations such as images (Wu et al., 2021; Jiang et al., 2020; Locatello et al., 2020; Veerapaneni et al., 2019; Greff et al., 2019; Burgess et al., 2019; Greff et al., 2017). Therefore, methods that use object-centric representations can be readily extended to take high-dimensional data as input. A simple approach to use object-centric representations in autonomous learning is to first learn how to control each object individually (using the objects’ representations as subgoals), and then combine learned skills to control multiple objects (Zadaianchuk et al., 2021). However, in an environment where different objects interact with each other, this method might learn an incompatible sequence of skills, i.e. achieving one of the subgoals can destroy another previously achieved subgoal. For example, moving one object from a stack of objects may change the position of the others. 
One line of work that aims at learning sequences of skills that are compatible is Hierarchical Reinforcement Learning (HRL) (Vezhnevets et al., 2017; Nachum et al., 2018; Levy et al., 2019). In principle, hierarchical agents should be able to transform a task into a sequence of subtasks that they solve sequentially. However, to date, existing hierarchical agents have mostly been applied to learn navigation or reaching tasks where learned skills do not interact with each other. It is unclear how sensitive hierarchical agents are to possible 
44
4.2. Related Work 
interactions between learned skills. In this chapter, we investigate another approach by reformulating the agent’s subtasks and the corresponding reward signals. Similar to Thomas et al. (2018), we train an agent such that it is motivated to control a particular component of the environment state representation while minimally affecting other components. Such an agent can learn to control components independently from other components, thus making the learned skills compatible with each other. 
As the environment state representation is not necessarily disentangled as in Thomas et al. (2018), our method should additionally account for possible relations between components. We propose a novel selectivity reward signal that uses an interaction graph to determine a set of components that can be selectively controlled without interacting with the remaining scene. The interaction graph can be inferred from observed objects dynamics collected by a random policy without supervision (Battaglia et al., 2016; Kipf et al., 2018). Thus, we com-bine learning of such interaction graphs with a goal-conditional reinforcement learning (RL) method that operates on object-centric representations (Zadaianchuk et al., 2021) and uses the selectivity reward signal. During training (schematically depicted in Figure 4.1), our SRICS agent (for Self-supervised Relational RL with Independently Controllable Subgoals) learns how to efficiently achieve different subgoals (and control the corresponding subspaces) while being incentivized to minimize its effects on other parts of the environment. 
Our main contributions are as follows: 
 We show that the global interaction graph can be estimated from data using a recurrent graph neural network (GNN) dynamical model combined with a sparsity prior. 
 We propose a goal-directed selectivity reward function that allows an agent to learn how to control environment components independently from one another. 
 We develop SRICS, an algorithm that uses the inferred interaction graph to learn simple and independently controllable subtasks and decompose a complex goal into a compatible sequence of subgoals. 
4.2 Related Work 
In self-supervised reinforcement learning, self-supervision refers to the agent constructing its own goals together with the corresponding reward signal and using them to learn to solve self-proposed goals (Colas et al., 2022; Blaes et al., 2019; Forestier et al., 2017; Colas et al., 2020; Nair et al., 2018; Pong et al., 2020; Aubret et al., 2021; Baranes and Oudeyer, 
45
Chapter 4. RL with Independently Controllable Subgoals 
Random agent, 
Observed environment dynamics 
Self-supervised training 
Interaction graph 
3rd 
obj 
Arm 
4th 
obj 
1st obj 
Action 
2nd obj 
Goal-conditioned policy, 
Soft Actor-Critic 
Independently controllable subgoals 
Arm 4th 
obj 3rd 
obj 
Arm 
2nd 
obj 
Arm 
Arm 2nd 
 obj 3rd 
obj 
 Agent with compositional 
skills, Selectivity reward,Env 
Figure 4.1: Our SRICS method. First, the interaction graph is inferred from observed environment dynamics containing links from cause to affected entity. This gives rise to subspaces that can be independently controlled, corresponding to subgoals gi. Next, the subgoals gi are used to construct a selectivity reward signal rsel. The selectivity reward rsel 
incentivizes the agent to only control the main entity i towards sgoal,i within each subgoal gi 
without affecting entities outside the subgoal. SRICS learns to solve an external goal sgoal 
by decomposing it into an ordered list of subgoals gi and solving each using SAC (Haarnoja et al., 2018) with a goal-conditioned policy πθ. As a result, the agent attempts to solve all the discovered subgoals one-by-one, without destroying previously solved subgoals. 
2013; Péré et al., 2018; Hausman et al., 2018; Lynch et al., 2019; Wang et al., 2020b; Nair et al., 2020; Zadaianchuk et al., 2021). Self-supervised agents can acquire a diverse set of general-purpose robotic skills. In the case of complex tasks, it is often beneficial to discover simpler subgoals and learn to solve them (Levy et al., 2019). From this point of view, recent hierarchical RL (HRL) agents (Levy et al., 2019; Nachum et al., 2018; Wang et al., 2020a; Li et al., 2021; Vezhnevets et al., 2017; Florensa et al., 2017) that try to solve external tasks by proposing several levels of internal subgoals are also self-supervised agents. 
46
4.2. Related Work 
Levy et al. (2019), Nachum et al. (2018) and Wang et al. (2020a) propose to learn several goal-conditioned policies. In the HIRO agent (Nachum et al., 2018), lower-level controllers are supervised with goals that are learned and proposed automatically by the higher-level controllers. In contrast, the HAC agent (Levy et al., 2019) trains each level of the hierarchy independently of the lower levels. The I2HRL agent (Wang et al., 2020a) additionally allows bi-directional communication among HRL levels and influence-based exploration to make training more stable and efficient. As such agents need to discover all the structure in the environment while learning on several levels, such approaches struggle to solve complex tasks in modular environments (Dwiel et al., 2019). Next, we review agents operating in environments where some structure is given. 
The SMORL agent, introduced in Chapter 3, exploits learned object-centric representations for gaining control over different objects in a self-supervised way and combines the learned skills for solving more complex compositional tasks. However, in Chapter 3, we assume independence of different objects, restricting the use of the SMORL agent to settings where objects almost do not interact with each other. CURIOUS (Colas et al., 2019) and CWYC (Blaes et al., 2019) exploit the modular structure of the goal space for efficient exploration in a given goal space. Colas et al. (2019) use a policy that obtains the goal module identifier together with the goal value. Blaes et al. (2019) also learn a relational graph between tasks. Both agents use a given modular structure for a learning curriculum (Forestier et al., 2017), however, discovered subtasks are evaluated independently. 
In realistic applications, autonomous agents usually do not have any well-structured representation. Nevertheless, agents can potentially infer it from data. We cover several directions that could be useful for such structure discovery. The first line of works (Jiang et al., 2020; Wu et al., 2021; Veerapaneni et al., 2019; Locatello et al., 2020; Burgess et al., 2019) learns object-centric representations from images or videos. Such representations could be potentially used in combination with the SRICS agent. The second line (Kipf et al., 2018; Kipf et al., 2020; Steenkiste et al., 2018; Li et al., 2020; Löwe et al., 2020) studies how object relations can be discovered from data. The improvements in both of these lines could lead to more general self-supervised agents that use a discovered structure for the generation of goals. 
47
Chapter 4. RL with Independently Controllable Subgoals 
4.3 Relational RL with Independently Controllable Subgoals 
In the setting we consider, at the training stage, the agent only receives a single composi-tional goal from the environment. The agent could try to solve the goal using the usual negative distance to the goal as a reward signal. However, achieving the compositional goal is quite a complex task by itself. This challenge can be addressed by discovering simple skills and combining them to solve the compositional goal. To achieve this, the agent needs to rely on self-supervision in the form of splitting the goal into subgoals and internally constructing the reward signal connected to each subgoal. 
The agent uses data collected from the environment to discover how different parts of the environment are related, including the agent itself, and then uses the discovered relations for the construction of subtasks that are solvable and can be easily combined. First, we describe how to use object-centric representations to estimate a graph of relations between objects, and then show how to utilize the learned graph during agent training, and for goal decomposition during evaluation. 
4.3.1 Estimation of the Latent Interaction Graph with a GNN Dynamical Model 
Relational information in the environment can help the autonomous agent to gain control over different parts of the environment. For example, if some parts of the environment cannot be affected, the agent will be more efficient by not trying to control them. Recently, several methods to estimate this relational information in an unsupervised way were proposed (Kipf et al., 2018; Steenkiste et al., 2018; Kipf et al., 2020; Li et al., 2020; Blaes et al., 2019). Most of them assume that the relations are static (Kipf et al., 2018; Li et al., 2020; Löwe et al., 2020). As this is not the case in many robotic manipulation applications, we propose to use a similar approach suitable for constantly changing relations. For this, we use a graph neural network (GNN) (Battaglia et al., 2016; Li et al., 2016) to model the forward dynamics of the objects. 
Because states could be non-Markovian, we use a recurrent dynamical model. Specifically, we incorporate recurrence in the GNN model by adding a Gated recurrent unit (GRU) (Chung et al., 2014) to the GNN message passing operation (see Figure 4.2a). We use the functions 
48
4.3. Relational RL with Independently Controllable Subgoals 
interaction effect action effect combined effect 
state prediction 
(a) Hidden state dynamics 
(b) State dynamics 
Figure 4.2: The dynamical model. For a given object j, the function dint computes each of the other objects’ effect on the object j using the hidden states ht. The effects from all the other objects are aggregated in the interaction effect vector hj,int 
t . Next, the function dact 
computes the action’s effect hj,act t on the object j. Both effects are combined in the GRU. 
Finally, object’s state estimation ŝjt+1 is estimated from the hidden state hjt+1 using the prediction function dpred. 
dint and dact to model the object-object interaction effect and the action’s effect, respectively. Next, both effects are combined in the GRU. More formally: 
hj,int t = 
∑ i ̸=j 
dint ( hit, hjt 
) , hj,act 
t = dact ( sjt , at 
) , hjt+1 = GRU 
([ hj,int t , hj,act 
t 
] , hjt 
) , (4.1) 
where hj,int t and hj,act 
t are vectors representing interaction and action effects, whereas hjt is the hidden state for object j at time step t. 
To model dynamics with sparse interactions between objects, we model dint as the product of an interaction weight wij 
t ∈ {0, 1} and an interaction effect function dint-eff: 
dint(hit, hjt) = wij t · dint-eff(hit, hjt). (4.2) 
The interaction weight wij t represents the belief in the absence or presence of the interaction 
between object i and object j at time step t. We model the weight’s distribution as 
q ( wij t | st 
) = softmax 
( dint-pres(hit, hjt) 
) , (4.3) 
where dint-pres is the interaction presence function. As we are interested in the estimation of the connections that are necessary for predictions, we additionally encourage the interaction 
49
Chapter 4. RL with Independently Controllable Subgoals 
weights distribution q ( wij t | st 
) to be close to the sparsity prior pprior. In our case, the 
sparsity prior pprior is the Bernoulli distribution with a large probability for zero (see Appendix B.6). 
Finally, we use a function dpred to predict the change in coordinates (see Figure 4.2b): 
ŝj,where t+1 = sj,where 
t + dpred ( hjt+1 
) . (4.4) 
All functions in Eqs. 4.1–4.4 are modeled by small MLPs with parameters ϕ. 
Now, as we defined all the parts of the GNN dynamical model, we describe how to estimate the interaction graph using a variational approach. First, similar to Kipf et al. (2018), we train our model by minimizing the negative ELBO loss: 
L(ϕ) = K∑ j=1 
T−1∑ t=1 
∥∥∥sj,where t+1 − ŝj,where 
t+1 
∥∥∥2 
2σ2 + DKL(q || pprior), (4.5) 
where ŝj,where is the prediction of the position of object j, σ2 is a fixed variance parameter and DKL denotes the Kullback-Leibler divergence. After training, we predict interaction weights wt for each timestep independently, then we average them across the whole dataset. Next, we estimate the global interaction graph by thresholding the average interaction weights to find the most active relations. Finally, we identify which object is directly controlled by the actions by finding the node that is most correlated with the action variable at. In the graph of our running example as in Figure 4.1, we denote this node as "arm" since in all experiments the identified node corresponds to a simulated robot arm. We add the action node with index 0 and the corresponding edge to the most correlated object to the graph (see Appendix B.6 for the details and the graph learning results). 
4.3.2 Learning to Independently Control Objects using the In-teraction Graph 
In this section, we show how the agent can use the learned interaction graph to solve compositional goal sgoal that consists of goals for individual objects sgoal,i. The SRICS agent sequentially gains control over the objects without affecting the previously moved objects. To achieve this, the SRICS method first identifies a set of objects P i that could be used to actively control object i by analyzing the discovered relations in the interaction graph. For each node i, we find the set P i of all nodes that lie in a path 
50
4.3. Relational RL with Independently Controllable Subgoals 
from the action node 0 to object node i. These ancestral nodes P i are the objects that could be used by the agent to control object i. All the other nodes are not required and thus should not be affected during the manipulation of object i. 
Arm2nd obj 
3rd 
obj 
Arm 
4th 
obj 
1st obj 
Action 
2nd obj 3rd 
obj 
Interaction graph (left) and the in-dependently controllable subgoal gi 
for object 3 (right). 
Next, we introduce the reward signal that uses P i 
to incentivize the agent to learn to control an object without moving others (line 8 of Algorithm 6). In or-der to achieve this, we propose to replace the original subgoal sgoal,i by a novel independently controllable subgoal gi that consists of the subgoal sgoal,i and the ancestral nodes P i: 
gi = ( sgoal,i, P i 
) . (4.6) 
In contrast to the original notion of a subgoal which only specifies a state component sgoal,i that the agent should reach, an independently controllable subgoal gi also includes information about which objects should not be interacted with to reach the target state component. 
We now formulate the goal-directed selectivity reward signal that explicitly incentivizes the agent to leave all objects except i and P i untouched. As opposed to the usual reward signal, it depends on the independently controllable subgoal gi and reads: 
rsel,i ( st, st−1, gi 
) = −||sit − sgoal,i|| + α · 
( seli(st, st−1, P i) − 1 
) . (4.7) 
The first term is the usual goal-based negative distance to the goal, which is needed to learn directed control over object i. The second term includes the selectivity that we define as 
seli ( st, st−1, P i 
) = 
 ||si 
t−si t−1||∑ 
j ̸∈Pi ||sj t −sj 
t−1|| , if subgoal is not solved; 
1 −∑ j ̸∈Pi∪{i} ||sjt − sjt−1||, otherwise. 
(4.8) 
The selectivity seli incentivizes the agent to maximize its influence (Seitzer et al., 2021; Zhao et al., 2021; Klyubin et al., 2005) on object i while having a minimal effect on objects j ∈/ P i (corresponding to non-ancestral nodes in graph G) until the subgoal corresponding to the object i is solved. Selectivity reaches its maximum value of 1 when the agent changes only the state of the object i without affecting any objects j ∈/ P i. In Appendix B.5, we show that selectivity naturally increases during learning to control the environment and that using it as a reward signal increases efficiency and stability. 
51
Chapter 4. RL with Independently Controllable Subgoals 
4.3.3 SRICS Policy Architecture and Training 
Similar to the SMORL agent (Zadaianchuk et al., 2021), we use a goal-conditioned attention policy for achieving subgoals. This kind of policy receives a set of object-centric representations as input together with the current subgoal representation. The aforementioned approach allows us to learn several different skills using only one policy. In addition, it is compatible with a different number of objects as inputs, thus allowing to use the agent in novel situations with a different number of objects. For more details on the goal-conditioned attention policy, we refer to Section 3.3.1. 
SRICS can be trained with any off-policy goal-conditioned RL algorithm. In particular, we use Soft-Actor Critic (SAC) (Haarnoja et al., 2018) with Hindsight Experience Replay (HER) (Andrychowicz et al., 2017) as a method to improve sample efficiency. The training of SRICS is presented in Algorithm 6. 
4.3.4 Subgoal Ordering during Evaluation 
After training, the agent can be applied to more complex tasks than the simple subtasks it was trained on. During the evaluation stage (Figure B.7 in Appendix B.8), SRICS encodes the compositional goal given by the environment into a set of independently controllable subgoals. Subsequently, it orders them by the depth of the corresponding nodes in the interaction graph G. Due to this order, subgoals that have a large number of dependencies are attempted first and subgoals that have only a few dependencies, like the robotic arm itself, are attempted as the later subgoals. The order of the independently controllable subgoals makes them compatible with each other. For example, the agent has to first rearrange all objects that need to be manipulated and then try to “solve” the arm subgoal, without destroying the already rearranged objects. More details can be found in Appendix B.8. 
4.4 Experiments 
In this section, we present our experiments that address the following questions: 
 How does SRICS perform compared to prior goal-conditioned RL methods on multi-object continuous control manipulation tasks? 
52
4.4. Experiments 
0 1 2 3 4 5 
Training examples ×105 
0.075 
0.100 
0.125 
0.150 
0.175 
0.200 
0.225 
A vg 
.d is 
t. 
Rearrange with 3 objects 
0 1 2 3 4 5 
Training examples ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
0.22 
Rearrange with 4 objects 
0 1 2 3 4 5 
Training examples ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
0.22 
Relational Rearrange with 4 objects 
SRICS SMORL SAC+HER HAC 
Figure 4.3: Average distance of objects and arm to the goal positions, comparing SRICS to SMORL, SAC+HER and HAC baselines. For all the experiments, results are averaged over 5 random seeds, shaded regions indicate one standard deviation. 
 What is the performance gain obtained from the goal-directed selectivity reward and subgoal ordering during evaluation? 
 How does our agent perform in an environment with an unseen combination of objects? 
We run SRICS and the baseline algorithms in the Multi-Object Rearrange from Zadaianchuk et al. (2021) and the novel Multi-Object Relational Rearrange environments. The latter environment incorporates additional physical connections between objects such as spring connections. Both environments are based on the multiworld package for continuous control tasks introduced by Nair et al. (2018) and use MuJoCo (Todorov et al., 2012) as a realistic simulator. They contain a 7-DoF Sawyer arm where the agent needs to manipulate a variable number of pucks on a table. In the first environment, the task is to rearrange the objects from random starting positions to random target positions. In the second environment, we add a spring connection between some of the objects and constrain other objects to be static (see Appendix B.2). This makes the resulting interaction graph more challenging and thus provides additional insights on the sensitivity of the agent to different interactions between objects. For both environments, we measure the performance of the algorithms as the average distance of all objects (including the robotic arm) to their goal positions (computed on the last step of the episode). 
4.4.1 Comparative Analysis 
As manipulation tasks in compositional environments can be approached from different perspectives, we provide a comparison with a previous state-of-the-art method from each 
53
Chapter 4. RL with Independently Controllable Subgoals 
perspective. In terms of problem assumptions, our work is closest to that of SMORL (Zada-ianchuk et al., 2021) which uses object-centric representations for subgoals and reward construction. In contrast to SRICS, SMORL executes subgoals in a random order and thus can potentially destroy previously solved subgoals. In addition, the SMORL agent does not have the incentive to influence the subgoal object during training. Another approach to learn goal-conditioned policy with coherent behavior is using Soft Actor-Critic (SAC) (Haarnoja et al., 2018) with Hindsight Experience Replay (HER) (Andrychowicz et al., 2017) relabeling. This method tries to achieve the overall goal without splitting it into subgoals. Finally, we consider the Hierarchical Actor-Critic (HAC) (Levy et al., 2019) method that tries to solve compositional tasks on several levels and is state of the art on several continuous control tasks. 
Arm 2 3 4 
Object 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Su 
bt as 
k su 
cc es 
s ra 
te 
Relational Rearrange with 4 objects 
SRICS SMORL 
Figure 4.4: Subtask success rate for SRICS and SMORL for each subtask in-dividually during evaluation in the Re-lational Rearrange environment. Both methods can solve Arm reaching subgoal, whereas on other subtasks SRICS per-forms better than SMORL. 
We show the results in Figure 4.3 and Figure 4.4. The performance of SRICS is significantly better than all other algorithms in both environments. SMORL is able to partially rearrange pucks on a table in the simpler Multi-Object Rearrange environment. However, its random subgoals or-dering is inefficient for arranging all the objects including the arm. In addition, even when eval-uating only based on the puck subtasks (see Ap-pendix B.7), SRICS outperforms SMORL, which further demonstrates the benefits of using a goal-directed selectivity reward signal. Moreover, in the more complex Multi-Object Relational Re-arrange environment, the gap between SRICS’s and SMORL’s performance is even larger. Fur-thermore, in all environments SAC is only able to solve the Arm subtasks, whereas HAC performance is close to that of a random agent. We present further comparison in more challenging environments with 6 different objects and velocity-based state representations in Appendix B.3. 
4.4.2 Ablative Analysis 
Here, we study the importance of different ingredients of our method for the overall performance of the agent. First, we ablate the selectivity term in our reward signal, using 
54
4.4. Experiments 
only the negative distance between the object and the desired position as a reward signal. We then additionally ablate the ordering of subgoals described in Section 4.3.4, using instead a random ordering of all subgoals. The results of the ablations are presented in Figure 4.5. Both ablations significantly deteriorate the performance of SRICS, showing the importance of both the goal-directed selectivity reward signal and the correct ordering in the goal decomposition for object manipulation in multi-object environments. 
0 1 2 3 4 5 
Training examples ×105 
0.075 
0.100 
0.125 
0.150 
0.175 
0.200 
0.225 
A vg 
.d is 
t. 
Rearrange with 3 objects 
0 1 2 3 4 5 
Training examples ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
0.22 
Rearrange with 4 objects 
SRICS w/o Selectivity w/o Selectivity and Ordering 
Figure 4.5: Average distance of objects and arm to the goal positions, comparing our method and two ablated variants on 3 and 4 objects Rearrange environments. 
4.4.3 Generalization to Unseen Object Combinations 
As SRICS can be used with different sets of objects as inputs, we investigate its performance on unseen combinations of objects. To test our agent on a novel combination of objects, we modify the Multi-Object Rearrange environment with 4 objects by deleting one of the objects from the table. We split possible combinations of three objects on training and evaluation combinations as shown in Figure 4.6a. We train the GNN dynamical model on the training combinations and then average all interaction weights to estimate the global interaction graph. Next, we train our SRICS agent on the training combinations and evaluate it on an unseen combination. The performance of SRICS on the unseen combination is close to its performance on Multi-Object Rearrange with 3 objects (see Figure 4.6b). This demonstrates that agents equipped with object-centric representations and a compatible policy are not restricted to the particular combination of objects they were trained on. Such agents should be able to learn how to control many objects and 
55
Chapter 4. RL with Independently Controllable Subgoals 
reuse learned skills for manipulation over different scenes containing only a random subset of objects. 
Train environment Evaluation environment 
Used objects 
(a) Train and evaluation environments. 
0 1 2 3 4 5 
Training examples ×105 
0.075 
0.100 
0.125 
0.150 
0.175 
0.200 
0.225 
A vg 
.d is 
t. 
Rearrange with 3 from 4 objects 
seen unseen 
(b) Average distance to the goal positions, comparing SRICS perfor-mance on seen and unseen combina-tions of 3 objects. 
Figure 4.6: Generalization to unseen combination of objects. 
4.5 Conclusion and Future Work 
In this work, we introduce SRICS, a self-supervised RL method that learns the relational structure of the environment and exploits this structure to learn a compatible sequence of skills to solve a difficult compositional goal. In a range of experiments in multi-object environments with robotic arm manipulation tasks, we demonstrate that SRICS is effective at discovering the most active dynamic relations between objects and can successfully rearrange multiple objects even in the presence of object interactions. 
Limitations and Future Work Directions There are several interesting directions for future work. First, one can extend SRICS to image-based object-centric representations, making it more applicable to realistic robotic settings where only high-dimensional sensory information is provided as input to the agent. Moreover, we expect that SRICS can be combined with different modular curriculum learning and exploration strategies (Colas et al., 2019; Blaes et al., 2019; Sancaktar et al., 2022). Finally, we expect that active training of the dynamic interaction graph (i.e. when the data for training is collected by the agent that actively explores the environment) could further improve the discovery of important structures in the environment. 
56
5 
Object Category Discovery for 
Semantic Segmentation 
In this chapter, we show that recent advances in self-supervised representation learning enable unsupervised object category discovery and semantic segmentation with a perfor-mance that matches the state of the field on supervised semantic segmentation 10 years ago. We propose a methodology based on unsupervised saliency masks and self-supervised feature clustering to kickstart object discovery followed by training a semantic segmentation network on pseudo-labels to bootstrap the system on images with multiple objects. We show that while being conceptually simple our proposed baseline is surprisingly strong. COMUS shows high performance on the PASCAL VOC dataset, significantly exceeding past state of the art. It also introduces first-time unsupervised results on the MS COCO dataset, effectively identifying numerous categories with high accuracy and maintaining a solid average performance across all categories. https://sites.google.com/view/comuspaper 
This chapter is based on the paper “Unsupervised Semantic Segmentation with Self-supervised Object-centric Representations” Andrii Zadaianchuk, Matthaeus Kleindessner, Yi Zhu, Francesco Locatello, Thomas Brox ICLR 2023: International Conference on Learning Representations 
57
Chapter 5. Object Category Discovery for Semantic Segmentation 
5.1 Introduction 
Figure 5.1: Unsupervised semantic segmentation predictions on PASCAL VOC (Everingham et al., 2012). Our COMUS does not use human annotations to discover objects and their precise localization. In contrast to the prior state-of-the-art method MaskContrast (Van Gansbeke et al., 2021), COMUS yields more precise segmentations, avoids confusion of categories, and is not restricted to only one object category per image. 
The large advances in dense semantic labelling in recent years were built on large-scale human-annotated datasets (Everingham et al., 2012; Lin et al., 2014; Cordts et al., 2016). These supervised semantic segmentation methods (e.g., Ronneberger et al., 2015; Chen et al., 2018a) require costly human annotations and operate only on a restricted set of predefined categories. Weakly-supervised segmentation (Pathak et al., 2015; Wei et al., 2018) and semi-supervised segmentation (Mittal et al., 2019; Zhu et al., 2020) approach the issue of annotation cost by reducing the annotation to only a class label or to a subset of labeled images. However, they are still bound to predefined labels. 
In this chapter, we follow a recent trend to move away from the external definition of class labels and rather try to identify object categories automatically by letting the patterns in the data speak. This could be achieved by (1) exploiting dataset biases to replace the missing annotation, (2) a way to get the learning process kickstarted based on “good” samples, and (3) a bootstrapping process that iteratively expands the domain of exploitable samples. 
58
5.1. Introduction 
A recent method that exploits dataset biases, DINO (Caron et al., 2021), reported promis-ing effects of self-supervised feature learning in conjunction with a visual transformer architecture by exploiting the object-centric bias of ImageNet with a multi-crop strategy. Their paper emphasized particularly the object-centric attention maps on some samples. We found that the attention maps of their DINO approach are not strong enough on a broad enough set of images to kickstart unsupervised semantic segmentation (see Fig. 5.4), but their learned features within an object region yield clusters of surprisingly high purity and align well with underlying object categories (see Fig. 5.3). 
Thus, we leverage unsupervised saliency maps from DeepUSPS (Nguyen et al., 2019) and BASNet (Qin et al., 2019) to localize foreground objects and to extract DINO features from these foreground regions. This already enables unsupervised semantic segmentation on images that show a dominant object category together with an unspectacular background as they are common in PASCAL VOC (Everingham et al., 2012). However, on other datasets, such as MS COCO (Lin et al., 2014), most objects are in context with other objects. Even on PASCAL VOC, there are many images with multiple different object categories. 
For extending to more objects, we propose training a regular semantic segmentation network on the obtained pseudo-masks and to further refine this network by self-training it on its own outputs. Our method, dubbed COMUS (for Clustering Object Masks for learning Unsupervised Segmentation), allows us to segment objects also in multi-object images (see Figure 5.1), and it allows us for the first time to report unsupervised semantic segmentation results on the full 80 category MS COCO dataset without any human annotations. While there are some hard object categories that are not discovered by our proposed procedure, we obtain good clusters for many of COCO object categories. 
Our contributions can be summarized as follows: 
1. We propose a strong and simple baseline method (summarized in Figure 5.2) for unsupervised discovery of object categories and unsupervised semantic segmentation in real-world multi-object image datasets. 
2. We show that unsupervised segmentation can reach quality levels comparable to supervised segmentation 10 years ago (Everingham et al., 2012). This demonstrates that unsupervised segmentation is not only an ill-defined academic playground. 
3. We perform extensive ablation studies to analyze the importance of the individual 
59
Chapter 5. Object Category Discovery for Semantic Segmentation 
Object-centric 
dataset  (no labels) 
Self-supervised 
representation learning 
 Categorization Prior  (What?) 
Unsupervised Object Categories Discovery 
Images Object Clusters 
Self-supervised pretraining Iterative Self-training 
Noisy  pseudo masks 
Noisy  pseudo masks 
Semantic segmentation 
network 
Self-training (2 iterations) 
Object proposals 
masks 
Object proposals 
Self-supervised  object  
representations 
Crop and resize Multiply mask to cluster ID Spectral Clustering 
 Localization Prior  (Where?) 
Saliency Dataset 
(no labels) 
Self-supervised 
saliency detector 
Self-supervised saliency detectorSelf-supervised representation learning 
Figure 5.2: Overview of our self-supervised semantic segmentation framework. First, the self-supervised representation learning network (e.g., DINO (Caron et al., 2021)) and the unsupervised saliency detector (e.g., DeepUSPS (Nguyen et al., 2019)) are trained without manual annotation on object-centric and saliency datasets (e.g., ImageNet (Deng et al., 2009) and MSRA (Cheng et al., 2015)). Next, we use the saliency detector to estimate object proposal masks from the original semantic segmentation dataset. After this, the original images are cropped to the boundaries of object proposal masks and resized. We compute feature vectors within these regions and cluster them with spectral clustering to discover different object categories. We filter the clusters by removing the most uncertain examples. The cluster IDs are combined with the saliency masks to form unsupervised pseudo-masks for self-training of a semantic segmentation network (e.g., DeepLabv3). 
components in our proposed pipeline, as well as bottlenecks to identify good directions to further improve the quality of unsupervised object discovery and unsupervised semantic segmentation. 
5.2 Related Work 
There are several research directions that try to tackle the challenging task of detecting and segmenting objects without any, or with only few, human annotations. 
60
5.2. Related Work 
Unsupervised Semantic Segmentation The first line of work (Van Gansbeke et al., 2021; He et al., 2022; Cho et al., 2021; Ji et al., 2019; Hwang et al., 2019; Ouali et al., 2020; Hamilton et al., 2022; Ke et al., 2022) aims to learn dense representations for each pixel in the image and then cluster them (or their aggregation from pixels in the foreground segments) to get each pixel label. While learning semantically meaningful dense representations is an important task itself, clustering them directly to obtain semantic labels seems to be a very challenging task (Ji et al., 2019; Ouali et al., 2020). Thus, usage of additional priors or inductive biases could simplify dense representation learning. PiCIE (Cho et al., 2021) incorporates geometric consistency as an inductive bias to facilitate object category discovery. Recently, STEGO (Hamilton et al., 2022) showed that DINO feature correspondences could be distilled to obtain even stronger bias for category discovery. MaskContrast (Van Gansbeke et al., 2021) uses a more explicit mid-level prior provided by an unsupervised saliency detector to learn dense pixel representations. To obtain semantic labels in an unsupervised way, such representations are averaged over saliency masks and clustered. We show that better representations for each mask could be extracted by using off-the-shelf self-supervised representations from DINO (Caron et al., 2021) encoder. Recently, DeepSpectral (Melas-Kyriazi et al., 2022) proposed to use spectral decomposition of dense DINO features. They suggested over-cluster each image into segments and afterward extracting and clustering DINO representations of such segments while using heuristics to determine the background segment. Those segments represent object parts that could be combined with over-clustering and community detection to improve the quality of pseudo-masks (Ziegler and Asano, 2022). In contrast, we show that starting from object-centric saliency priors discovered on a simpler dataset provides large benefits for discovering object categories (see App. C.3.1). In contrast to estimating pseudo-masks on the full dataset, using only good quality reliable object proposals for each category combined with iterative self-training on expanding datasets additionally decrease biases over the initial pseudo-masks. 
Unsupervised Object Discovery (UOD) UOD is another research direction that also aims to discover object information such as bounding boxes or object masks from images without any human annotations. Recent works on UOD (H’enaff et al., 2022; Melas-Kyriazi et al., 2022; Wang et al., 2022; Simeoni et al., 2021; Vo et al., 2021; Zhang et al., 2020; Vo et al., 2020) showed the potential benefit of using the embeddings of pretrained networks (supervised or self-supervised) for both object localization (to the 
61
Chapter 5. Object Category Discovery for Semantic Segmentation 
Core cluster pseudo masks Filtered pseudo masks 
Figure 5.3: Visualization of unsupervised pseudo-masks on PASCAL VOC val set. (left) 2D t-SNE projection of object proposal features. Colors correspond to cluster IDs. (right) Pseudo-masks from different clusters. The pseudo-masks were randomly sampled for each cluster from both cluster core pseudo-masks (green columns) and filtered pseudo-masks (red columns). 
level of the object’s bounding box) and object clustering. First, rOSD (Vo et al., 2021; Vo et al., 2020) showed that supervised features could be used to localize single objects in the image. Next, LOST (Simeoni et al., 2021) proposed a heuristic that relies on self-supervised features to localize the most salient object in the image. In contrast to those methods we consider the challenging task of object segmentation, not only object detection. Finally, Melas-Kyriazi et al. (2022) and Wang et al. (2022) propose to do spectral decomposition of dense DINO features and use of sign of Fiedler eigenvector as criteria for object localization mask. 
Unsupervised Object-centric Representation Learning Object centric learning assumes that scenes are composed of different objects and aims to learn sets of feature vectors, where each of them binding to one object. Unsupervised methods based on single images (Burgess et al., 2019; Greff et al., 2019; Engelcke et al., 2020; Locatello et al., 2020; Singh et al., 2022a) suffer from single-view ambiguities, which one tries to overcome by exploiting the information in multiple views of a static scene (Chen et al., 2021a), in a single view of a dynamic scene (i.e., a video) (Hsieh et al., 2021; Kipf et al., 2022; Singh et al., 2022c) or multiple views of a dynamic scene (Nanbo et al., 2021). In contrast to 
62
5.3. Self-supervised Semantic Segmentation 
Algorithm 2 Object Categories Discovery for Unsupervised Pseudo-Masks Estimation Given: N images xi, self-supervised salient regions’ segmentation network L with binary threshold θ, self-supervised representation learning method C, percentage of proposals to filter p. 
Step 1: Obtain binary object proposal masks mi by si = L(xi) > θ and object proposal regions oi = crop(xi, si). Step 2: Compute object representations ri of object proposal regions oi, ri = C(oi) Step 3: Cluster object proposal representations ri using spectral clustering to assign cluster ID ti for each object proposal oi. Step 4: Filter p percents of the most uncertain object proposals for each discovered cluster (proposals with the largest distance to the cluster center in the eigenvalue embedding). Step 5: Combine cluster IDs ti with object proposal masks si to obtain initial pseudo-masks mi. 
Return: Noisy object segmentation pseudo-masks mi. 
previous methods and similar to DINOSAUR method (Seitzer et al., 2023), our method exploits unlabeled object-centric datasets to extract object masks and representations. 
5.3 Self-supervised Semantic Segmentation 
5.3.1 Initial Discovery of Object Categories 
Unsupervised decomposition of complex, multi-object scenes into regions that correspond to the present objects categories is hard and largely ill-defined as it is possible to decompose scene with different levels of granularity obtaining several valid decompositions for the same scene (e.g., a person could be considered as one object or additionally decomposed to body parts). However, it is unnecessary to correctly decompose all images of a dataset to kickstart unsupervised object discovery. In this chapter, we show that it is sufficient to exploit simple images in a dataset in order to discover some objects and their categories. This works particularly well due to intrinsic properties of natural images and photos made by humans. One such property is that the most salient region of the image often corresponds to a single distinct object. 
63
Chapter 5. Object Category Discovery for Semantic Segmentation 
Self-supervised Object Localization Similar to MaskContrast (Van Gansbeke et al., 2021), we propose to retrieve a set of object mask proposals for the images in our dataset by using an unsupervised saliency estimator. In particular, we were using the DeepUSPS (Nguyen et al., 2019) model as an unsupervised saliency estimator. DeepUSPS was trained on MSRA (Cheng et al., 2015) in an unsupervised way exploiting the bias towards simple scenes with often homogeneously textured background of the MSRA dataset, as well as the hard-coded saliency priors of classical (non-learning-based) saliency methods. To further improve the estimator’s transfer ability to more complex datasets like PASCAL VOC and MS COCO, we trained another saliency model, BasNet (Qin et al., 2019), on the saliency masks generated by DeepUSPS. Some examples of saliency detector masks are presented in Section 5.4.3; see Figure 5.4. In addition, we studied performance of our method with original DeepUSPS masks and with DeepSpectral saliency masks in App. C.3. 
Self-supervised Representation Learning The self-supervised feature learning tech-nique DINO (Caron et al., 2021) exploits the dataset bias of ImageNet, which mostly shows a single object in the center of the image. DINO uses, among other transformations, the multi-crop strategy to link local patterns of the same object instance to its global pattern in the embedding. This leads to a feature representation that tends to have a similar embedding for patterns from the same category. 
We start extraction of the object representation by cropping the image to the borders of the saliency mask and resizing the obtained crop to 256 × 256 resolution. Next, we feed the object proposal into the Vision Transformer (ViT) (Dosovitskiy et al., 2021a) architecture pretrained in a self-supervised way with DINO. The feature vector of the CLS token from the last layer is used as object representation. As CLS token attention values from the last layer of DINO were shown to attend to foreground objects (Caron et al., 2021), the obtained CLS token features are implicitly aggregating object related information from the object proposal. 
Discovery of Semantic Categories We cluster the feature vectors obtained per image with spectral clustering (Luxburg, 2007). Thanks to the saliency masks, most of the feature vectors are based on foreground patterns and disregard the background, i.e., they become object-centric. Even though this is clearly not the case for all images, either because there are salient regions in the background or because the image shows multiple objects from different categories, there are enough good cases for spectral clustering to yield clusters 
64
5.3. Self-supervised Semantic Segmentation 
Algorithm 3 Self-training with Noisy Pseudo-Masks Given: N images xi with clustering pseudo-masks mi, external M images xj for self-training 
Step 1: Train a Teacher network θt (with prediction function f) on images with unsupervised pseudo-masks by minimizing the total loss L for object segmentation: 
θ∗ t = arg min 
θt 
1 N 
N∑ j=1 
L(mj, f(xj, θt)). 
Step 2: Generate new pseudo-masks m̃j for all unlabeled images xj (e.g., images from PASCAL VOC trainaug set). Step 3: Train a Student network θs on images and new pseudo-masks (xj, m̃j): 
θ∗ s = arg min 
θs 
1 N + M 
N+M∑ j=1 
L(m̃j, f(xj, θs)). 
Return: Semantic segmentation network θ∗ s . 
that are dominated by a single object category; see Figure 5.3. As we show in Table 5.5, this clustering of features within the saliency masks already yields unsupervised object discovery results beyond the state of the art. 
Filtering of Cluster Samples Since neither the salient regions nor DINO features are perfect, we must expect several outliers within the clusters. We tested the simple procedure to filter the most uncertain samples of each cluster and discard them. We measure uncertainty by the distance to the cluster’s mean in the spectral embedding of the Laplacian eigenmap (Luxburg, 2007). In Figure 5.3 we show that such examples are often failure cases of the saliency detector, such as parts of background that are not related to any category. In addition, we study sensitivity of COMUS algorithm in App. C.1, showing that COMUS performs comparably well when the percentage of filtered examples varies from 20% to 40%. We refer the reader to the Algorithm 2 for the detailed pseudocode of object categories discovery part of the COMUS method. 
65
Chapter 5. Object Category Discovery for Semantic Segmentation 
5.3.2 Unsupervised Iterative Self-training with Noisy Pseudo-Masks 
As discussed above, the clustering of feature vectors extracted from within saliency masks makes several assumptions that are only satisfied in some of the samples of a dataset. While this is good enough to get the object discovery process kickstarted, it is important to alleviate these assumptions in order to extend to more samples. In particular, we implicitly relied on the image to show only objects from one category (otherwise the feature vector inside the saliency mask comprises patterns from different categories) and on the correct localization of the object boundaries. 
To extend also to multi-object images and to improve the localization of object boundaries, we propose using the masks with the assigned cluster IDs as initial pseudo-labels for iterative self-training of a semantic segmentation network. Self-training is originally a semi-supervised learning approach that uses labels to train a teacher model and then trains a student model based on the pseudo-labels generated by the teacher on unlabeled data (Xie et al., 2020). Similar self-training methods were shown to be effective also in semantic segmentation (Chen et al., 2020a; Zhu et al., 2020). In this chapter, we use the unsupervised pseudo-masks from Sec. 5.3.1 to train the teacher. In our experiments, we used the network architecture of DeepLabv3 (Chen et al., 2017), but the method applies to all architectures. Since large architectures like DeepLabv3 are typically initialized with an ImageNet pretrained encoder, we also use a pretrained encoder for initialization. However, since we want to stay in the purely unsupervised training regime, we use self-supervised DINO pretraining. 
Once the semantic segmentation network is trained on the pseudo-masks, it can predict its own masks. In contrast to the saliency masks, this prediction is not limited to single-object images. Moreover, the training can consolidate the information of the training masks and, thus, yields more accurate object boundaries. Since the masks of the segmentation network are on average better than the initial pseudo-masks, we use them as pseudo-masks for a second iteration of self-training. In addition, if such masks are obtained from unseen images of an extended dataset, the predictions of the segmentation network are not overfitted to the initial pseudo-masks and thus are an even better supervision signal. We refer to the pseudocode in Algorithm 3 for an overview of iterative self-training. In addition, Table 5.5 in Sec. 5.4.3 shows that both the initial self-training (Step 1 in Algorithm 3) and the second iteration (Step 3 in Algorithm 3) of self-training improve results. 
66
5.4. Experiments 
5.4 Experiments 
Evaluation Setting We tested the proposed approach on two semantic object segmenta-tion datasets, PASCAL VOC (Everingham et al., 2012) and MS COCO (Lin et al., 2014). These benchmarks are classically used for supervised segmentation. In contrast, we used the ground truth segmentation masks only for testing but not for any training. We ran two evaluation settings. For the first, we created as many clusters as there are ground truth classes and did one-to-one Hungarian matching (Kuhn, 1955) between clusters and classes. For the second, we created more clusters than there are ground truth classes and assigned the clusters to classes via majority voting, i.e, for each cluster we chose the class label with most overlap and assigned the cluster to this class. In both cases we used IoU as the cost function for matching and as the final evaluation metric. 
Hungarian matching is more strict, as it requires all clusters to match to a ground truth class. Hence, reasonable clusters are often marked as failure with Hungarian matching; for instance, the split of the dominant person class into sitting and standing persons leads to one cluster creating an IoU of 0. This is avoided by majority voting, where clusters are merged to best match the ground truth classes. However, in the limit of more and more clusters, majority voting will trivially lead to a perfect result. When not noted otherwise, we used Hungarian matching in the following tables. We report mean intersection over union (mIoU) as evaluation metric. 
Implementation Details We used pretrained DINO features with the DINO architecture released in DINO’s official GitHub1. In particular, we used DINO with patch size 8 that was trained for 800 epochs on ImageNet-1k without labels. For the saliency masks, we used the BasNet weights pretrained on predictions from DeepUSPS released by MaskContrast’s official GitHub2 (see folder saliency). All parameters of spectral clustering and self-training are described in Appendix C.6. 
5.4.1 PASCAL VOC Experiments 
PASCAL VOC 2012 (Everingham et al., 2012) comprises 21 classes – 20 foreground objects and the background. First, to qualitatively validate that the obtained clusters correspond 
1https://github.com/facebookresearch/dino 2https://github.com/wvangansbeke/Unsupervised-Semantic-Segmentation 
67
Chapter 5. Object Category Discovery for Semantic Segmentation 
Table 5.1: Comparison to prior art and iterative improvement via self-training (evaluated by IoU after Hungarian matching) on the PASCAL 2012 val set. The results for SwAV and IIC methods are taken from MaskContrast paper. COMUS results are mean ± standard dev. over 5 runs. 
Method mIoU 
Colorization (Zhang et al., 2016) 4.9 
IIC (Ji et al., 2019) 9.8 
SwAV (Caron et al., 2020) 4.4 
MaskContrast (Van Gansbeke et al., 2021) 35.1 
DeepSpectral (Melas-Kyriazi et al., 2022) 37.2 ± 3.8 
DINOSAUR (Seitzer et al., 2023) 37.2 ± 1.8 
Leopart (Ziegler and Asano, 2022) 41.7 
Pseudo-masks (Iteration 0) 43.8 ± 0.1 
COMUS (Iteration 1) 47.6 ± 0.4 
COMUS (Iteration 2) 50.0 ± 0.4 
Table 5.2: COMUS performance on PASCAL VOC 2007 test (evaluated by IoU after Hungarian matching). The test data was never seen during self-learning or validation. 
mIoU 
DeepSpectral 77.3 40.2 0.0 78.2 25.0 6.0 65.7 50.7 82.7 0.0 43.6 24.5 54.4 63.5 31.5 20.6 2.3 0.0 9.4 77.0 0.1 35.8 
COMUS 84.3 38.3 30.9 51.4 47.1 39.9 66.3 54.7 67.7 0.0 60.2 21.3 54.3 57.9 62.7 45.4 9.0 72.2 13.8 81.5 43.4 47.7 
to true object categories, we visualize the t-SNE embedding (Maaten and Hinton, 2008) of DINO representations showing that clusters correspond to different object categories (see Fig. 5.3). Further, we quantitatively confirmed that saliency masks with assigned cluster ID (pseudo-masks) produce state-of-the-art unsupervised semantic segmentation on PASCAL VOC and outperforms the MaskContrast method that learns dense self-supervised representations; see Table 5.1 (Iteration 0 row). 
For self-training the DeepLabv3 architecture, we initialized the encoder with a ResNet50 pretrained with DINO (self-supervised) on ImageNet and finetuned the whole architecture on the pseudo-masks we computed on the PASCAL 2012 train set. This increased the performance from 43.8% mIoU to 47.6% mIoU, see Table 5.1 (Iteration 1), which supports our consideration of bootstrapping from the original pseudo-masks. In particular, it allows us to segment objects in multi-category images. 
Successively, we added one more iteration of self-learning on top of the pseudo-masks on the PASCAL 2012 trainaug set. The PASCAL 2012 trainaug set (10582 images) is 
68
5.4. Experiments 
Table 5.3: Unsupervised semantic segmentation before and after self-learning evaluated by mIoU after Hungarian matching on the MS COCO val set. As discovered object category we count those categories with an IoU > 20% from all 81 categories. Also, we show IoU for categories that have corresponding cluster (i.e., with IoU larger than zero). 
all discovered (with IoU≥ 20%) have cluster (with IoU> 0%) 
mIoU number mIoU number mIoU 
Pseudo-masks 18.2 33 36.6 73 20.2 COMUS 19.6 34 40.7 60 26.5 
Table 5.4: Transfer from PASCAL VOC to MS COCO for the 21 PASCAL VOC classes. Training on the simpler PASCAL dataset yields better performance on COCO than learning on COCO itself while both COMUS runs perform better than DeepSpectral. 
mIoU 
DeepSpectral 71.6 42.4 0.0 51.6 10.1 0.7 54.5 22.9 66.9 1.4 2.3 20.1 35.7 48.3 39.2 16.3 0.0 29.4 1.9 40.2 7.0 26.8 
COMUS (trained on PASCAL) 79.5 40.7 12.4 31.9 25.7 14.0 50.6 12.1 56.1 0.0 31.0 20.1 47.6 39.6 40.6 43.5 6.8 47.6 8.0 39.7 22.8 31.9 
COMUS (trained on COCO) 76.5 39.9 28.2 29.7 34.3 0.1 56.8 6.8 34.9 0.7 50.2 4.4 42.1 38.7 48.4 15.1 0.0 54.4 0.0 40.4 2.6 28.8 
an extension of the original train set (1464 images) (Everingham et al., 2012; Hariharan et al., 2011). It was used by previous work on fully-supervised (Chen et al., 2018a) and unsupervised (Van Gansbeke et al., 2021) learning. The second iteration of self-training further improves the quality to 50.0% mIoU; see Table 5.1 (Iteration 2). In particular, it allows us to make multi-category predictions on images from the validation set unseen during self-supervised training (Fig. 5.1). Accordingly, the method also yields good results on the PASCAL VOC 2007 official test set; see Table 5.2. 
5.4.2 MS COCO Experiments 
We further evaluated our method on the more challenging COCO dataset (Lin et al., 2014). It focuses on object categories that appear in context to each other and has 80 things categories. We transform the instance segmentation masks to category masks by merging all the masks with the same category together. Our method is able to discover 34 categories with more than 20% IoU. Among those categories, we obtained an average IoU of 40.7%; see Table 5.3. 
Additionally, we studied the transfer properties of COMUS under a distribution shift. To this end, we self-trained our COMUS model on the PASCAL VOC dataset and then tested this model on the same 20 classes on the MS COCO dataset. The results in Table 5.4 show 
69
Chapter 5. Object Category Discovery for Semantic Segmentation 
that the transfer situation between datasets is quite different from supervised learning: training on the PASCAL VOC dataset and testing on COCO yields better results than training in-domain on COCO (see Fig. C.5 in Appendix). This is because the PASCAL VOC dataset contains more single object images than MS COCO, which makes self-supervised learning on PASCAL VOC easier. This indicates that the order in which data is presented plays a role for unsupervised segmentation. Starting with datasets that have more single-object bias is advantageous over starting right away with a more complex dataset. 
Table 5.5: Ablation experiment to identify the effect of individual components of the unsupervised learning process. 
Laplacian Eigenmap 
Self-training 
Filtering 2nd self-training 
mIoU 
✗ ✗ ✗ ✗ 42.8 ✓ ✗ ✗ ✗ 43.8 ✓ ✓ ✗ ✗ 47.1 ✓ ✓ ✓ ✗ 47.6 ✓ ✓ ✓ ✓ 50.0 
Figure 5.4: Visualization of foreground masks obtained with different foreground segmenta-tion methods. 
70
5.4. Experiments 
Table 5.6: Comparison of COMUS performance with different feature extractors on PASCAL VOC. 
mIoU 
COMUS with SwAV 28.6 COMUS with iBOT 43.8 
COMUS with DINO 50.0 
Table 5.7: Comparison between different class-agnostic foreground segmentation methods. 
IoU 
Unsupervised saliency 51.0 LOST 34.8 DINOSeg 24.5 
Supervised saliency 60.5 
5.4.3 Analysis 
Ablation Study To isolate the impact of single components of our architecture, we con-ducted various ablation studies on PASCAL VOC; see Table 5.5. All proposed components have a positive effect on the result: spectral clustering that additionally computes Lapla-cian eigenmap before k-means clustering yields better results than k-means clustering (see Appendix C.1 for detailed analysis on clustering method choice and sensitivity of its pa-rameters); self-training is obviously important to extend to multi-category images; filtering the most distant samples from a cluster followed by the second iteration of self-training on the much larger trainaug set gives another strong boost. 
Choice of Categorization Prior Next, we investigated how COMUS works with different self-supervised representation learning methods. COMUS performs best with ViT based features extractors such as DINO (Caron et al., 2021) and iBOT (Zhou et al., 2022), while its performance is significantly worse for SwAV method (Caron et al., 2020) based on ResNet architecture. We further show that clustering ability of categorization method could be evaluated on ImageNet images clustering where self-supervised methods were originally trained on (see Appendix C.2). 
Quality and Impact of Saliency Masks In Table 5.7, we compare the quality of the used unsupervised saliency mask detector with other recently proposed detection methods. We report the IoU for the foreground class while using different methods for foreground object segmentation. In particular, we evaluated segmentation masks proposed in LOST (Simeoni et al., 2021) that uses DINO keys correlation between features, and DINOSeg (Simeoni et al., 2021; Caron et al., 2021), which uses the attention weights 
71
Chapter 5. Object Category Discovery for Semantic Segmentation 
from the last layer of the DINO network, to construct foreground object segmentation masks (see Figure 5.4 for examples of predictions by foreground segmentation methods that we consider). The chosen unsupervised saliency based on DeepUSPS and BASNet outperforms both LOST and DINOSeg with a large margin showing the importance of additional localization prior in contrast with relying only on DINO as both categorization and localization prior. In addition, we show how the quality of saliency masks proposal affects COMUS performance in App. C.3. 
Table 5.8: Over-clustering results on PASCAL VOC evaluated with mIoU after majority voting. We present the results for 30 clusters, whereas also include the results for 50 clusters for comparison with MaskContrast (Van Gansbeke et al., 2021). 
30 clusters 50 clusters 
MaskContrast - 41.4 
COMUS (Iteration 1) 49.3 46.9 COMUS (Iteration 2) 52.6 51.0 
Over-clustering As the number of discovered clusters could be different from the number of human-defined categories, we ran our process with a larger number of clusters than there are ground truth categories (over-clustering). Each cluster was matched to the ground truth category with the highest IoU, i.e., each category can have multiple clusters being assigned to it. This kind of matching avoids penalization of reasonable subcategories (see Fig. 5.5). Discovery of subcategories is a strong motivation for using unsupervised methods. Table 5.8 shows that also under this evaluation protocol we obtain better results. For comparison to MaskContrast, we also included results with 50 clusters, showing that COMUS outperforms MaskContrast in the 50 clusters setting. 
Self-training from pseudo-masks with a larger number of categories decreased the perfor-mance slightly. Potentially the segmentation network has difficulties learning patterns when several clusters have the same semantic interpretation. In the case of fixed saliency masks, this evaluation setting yields better numbers and becomes trivial as the number of clusters becomes very large. 
72
5.5. Conclusion and Future Work 
Figure 5.5: Visualization of discovered subcategories on PASCAL VOC val set after clustering of self-supervised representations into 30 clusters. The pseudo-masks were randomly sampled for each cluster. Each row shows two clusters of the same category. The clusters have clear semantic interpretations, such as different dog breeds, flying or staying on land airplanes. 
5.5 Conclusion and Future Work 
In this chapter, we presented a procedure for semantic object segmentation without using any human annotations clearly improving over previous work. As any unsupervised seg-mentation method requires some biases to be assumed or learned from data, we propose to use object-centric datasets on which localization and categorization priors could be learned in a self-supervised way. We show that combining those priors together with an iterative self-training procedure leads to significant improvements over previous approaches that rely on dense self-supervised representation learning. This combination reveals the hidden potential of object-centric datasets and allows creating a strong baseline for unsupervised segmentation methods by leveraging and combining learned priors. 
While research on this task is still in its infancy, our procedure allowed us to tackle a significantly more complex dataset like MS COCO for the first time. Notably, on PASCAL VOC we obtained results that match the best supervised learning results from 2012, before the deep learning era. Hence, the last ten years of research not only have yielded much 
73
Chapter 5. Object Category Discovery for Semantic Segmentation 
higher accuracy based on supervised learning, but also allow us to remove all annotation from the learning process. 
Limitations and Future Work Directions Although COMUS shows very promising results on the hard tasks of unsupervised object segmentation, there are a number of limitations, as to be expected. Firstly, although we reduced the dependency on the quality of the saliency detector via successive self-training, the approach still fails to segment objects that are rarely marked as salient (see Figure C.6 in Appendix C.4.2). Our research (Seitzer et al., 2023; Zadaianchuk et al., 2023a) marks the initial steps in investigating object-centric methodologies that operate independently of a localization prior, focusing on dense self-supervised features (Van Gansbeke et al., 2022; Seitzer et al., 2023; Zadaianchuk et al., 2023a). Future work can extend category discovery and unsupervised semantic segmentation to operate purely from scene-based data. 
Secondly, while bootstrapping via self-learning can correct some mistakes of the initial discovery stage (Nguyen et al., 2019), it cannot correct all of them and can be itself biased towards self-training data, such as predicting more often only one semantic segmenta-tion category (see App. C.4.1). Thus, determining the optimal number of localization proposals (Ziegler and Asano, 2022; Li et al., 2022) is a noteworthy future work direction. 
Finally, the current approach fixes the number of clusters in spectral clustering based on the dataset’s known category numbers. While COMUS works reasonably with a larger number of clusters (see Figure 5.5 for over-clustering experiments), in a fully open data exploration scheme, the optimal number of clusters should be determined automatically. 
74
6 
Scaling Video Object-Centric 
Learning 
Unsupervised video-based object-centric learning is a promising avenue to learn structured representations from large, unlabeled video collections, but previous approaches have only managed to scale to real-world datasets in restricted domains. Recently, it was shown that the reconstruction of pre-trained self-supervised features leads to object-centric representations on unconstrained real-world image datasets. Building on this approach, we propose a novel way to use such pre-trained features in the form of a temporal feature similarity loss. This loss encodes semantic and temporal correlations between image patches and is a natural way to introduce a motion bias for object discovery. We demonstrate that this loss leads to state-of-the-art performance on the challenging synthetic MOVi datasets. When used in combination with the feature reconstruction loss, our model is the first object-centric video model that scales to unconstrained video datasets such as YouTube-VIS. https://martius-lab.github.io/videosaur/ 
This chapter is based on paper “Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities” Andrii Zadaianchuk∗, Maximilian Seitzer∗, and Georg Martius NeurIPS 2023: Conference on Neural Information Processing Systems 
75
Chapter 6. Scaling Video Object-Centric Learning 
6.1 Introduction 
Autonomous systems should have the ability to understand the natural world in terms of independent entities. Towards this goal, unsupervised object-centric learning meth-ods (Burgess et al., 2019; Greff et al., 2019; Locatello et al., 2020) learn to structure scenes into object representations solely from raw perceptual data. By leveraging large-scale datasets, these methods have the potential to obtain a robust object-based understanding of the natural world. Of particular interest in recent years have been video-based meth-ods (Jiang et al., 2020; Kipf et al., 2022; Elsayed et al., 2022; Singh et al., 2022c), not least because the temporal information in video presents a useful bias for object discovery (Bao et al., 2022). However, these approaches are so far restricted to data of limited complex-ity, successfully discovering objects from natural videos only on closed-world datasets in restricted domains. 
In this paper, we present the method Video S lot Attention U sing temporal feature similaRity, VideoSAUR, that scales video object-centric learning to unconstrained real-world datasets covering diverse domains. To achieve this, we build upon recent advances in image-based object-centric learning. In particular, Seitzer et al. (2023) showed that reconstructing pre-trained features obtained from self-supervised methods like DINO (Caron et al., 2021) or MAE (He et al., 2022) leads to state-of-the-art object discovery on complex real-world images. We demonstrate that combining this feature reconstruction objective with a video object-centric model (Kipf et al., 2022) also leads to promising results on real-world YouTube videos. 
We then identify a weakness in the training objective of current unsupervised video object-centric architectures (Jiang et al., 2020; Singh et al., 2022c): the prevalent reconstruction loss does not exploit the temporal correlations existing in video data for object grouping. To address this issue, we propose a novel self-supervised loss based on feature similarities that explicitly incorporates temporal information (see Fig. 6.1). The loss works by pre-dicting distributions over similarities between features of the current and future frames. These distributions encode information about the motion of individual image patches. To efficiently predict those motions through the slot bottleneck, the model is incentivized to group patches with similar motion into the same slot, leading to better object groupings as patches belonging to an object tend to move consistently. In our experiments, we find that such a temporal similarity loss leads to state-of-the-art performance on challenging synthetic video datasets (Greff et al., 2022), and significantly boosts performance on 
76
6.1. Introduction 
Similarity Loss 
Self-supervised V 
iT Self-supervised 
V iT 
Slots 
Group Predict 
Cosine Distance 
0.0 0.0 0.0 0.0 
0.0 0.0 0.1 0.0 
0.0 0.0 0.3 0.2 
0.0 0.0 0.4 0.0 
0.0 0.0 -0.2 -0.3 
-0.2 0.0 0.6 0.0 
-0.1 0.0 0.9 0.2 
-0.1 0.0 0.8 0.3 
0.0 0.0 0.0 0.0 
0.0 0.0 0.2 0.0 
0.0 0.0 0.4 0.03 
0.0 0.0 0.32 0.05 
Figure 6.1: We propose a self-supervised temporal similarity loss for training object-centric video models. For each patch at time t, the model has to predict a distribution P̂t,t+k 
indicating where all semantically-similar patches have moved to k steps into the future. The target distribution Pt,t+k is computed with a softmax on the affinity matrix At,t+k 
containing the cosine distance between all patch features ht, ht+k. The loss incentivizes the model to group areas with consistent motion and semantics into slots. 
real-world videos when used in conjunction with the feature reconstruction loss. 
In video processing, model efficiency is of particular importance. Thus, we design an efficient object-centric video architecture by adapting the SlotMixer decoder (Sajjadi et al., 2022) recently proposed for 3D object modeling for video decoding. Compared to previous decoder designs (Locatello et al., 2020), the SlotMixer decoder scales gracefully with the number of slots, but has a weaker inductive bias for object grouping. We show that this weaker bias manifests in optimization difficulties in conjunction with conventional reconstruction losses, but trains robustly with our proposed temporal similarity loss. We attribute this to the self-supervised nature of the similarity loss: compared to reconstruction, it requires predicting information that is not directly contained in the input; the harder task seems to compensate for the weaker bias of the SlotMixer decoder. 
To summarize, our contributions are as follows: (1) we propose a novel self-supervised loss for object-centric learning based on temporal feature similarities, (2) we combine this loss with an efficient video architecture based on the SlotMixer decoder where it synergistically reduces optimization difficulties, (3) we show that our model improves the state-of-the-art on the synthetic MOVi datasets by a large margin, and (4) we demonstrate that our model 
77
Chapter 6. Scaling Video Object-Centric Learning 
is able to learn video object-centric representations on the YouTube-VIS dataset (Yang et al., 2021), while staying fully unsupervised. This paper takes a large step towards unconstrained real-world object-centric learning on videos. 
6.2 Related Work 
Video Object-Centric Learning There is a rich body of work on discovering objects from video, with two broad categories of approaches: tracking bounding boxes (Kosiorek et al., 2018; Crawford and Pineau, 2020; Jiang et al., 2020; Lin et al., 2020) or segmentation masks (Greff et al., 2017; Steenkiste et al., 2018; Veerapaneni et al., 2019; Greff et al., 2019; Zoran et al., 2021; Weis et al., 2021; Kabra et al., 2021; Kipf et al., 2022; Elsayed et al., 2022; Singh et al., 2022c; Traub et al., 2023a; Safadoust and Güney, 2023). Architecturally, most recent image-based models for object-centric learning (Locatello et al., 2020; Singh et al., 2022a; Seitzer et al., 2023) are based on an auto-encoder framework with a latent slot attention grouping module (Locatello et al., 2020) that extracts a set of slot representations. For processing video data, a common approach (Zoran et al., 2021; Kipf et al., 2022; Elsayed et al., 2022; Singh et al., 2022c; Traub et al., 2023a) is then to connect slots recurrently over input frames; the slots from the previous frame act as initialization for extracting the slots of the current frame. We also make use of this basic framework. 
Scaling Object-Centric Learning Most recent work has attempted to increase the complexity of datasets where objects can successfully be discovered, such as the synthetic ClevrTex (Karazija et al., 2021) and MOVi datasets (Greff et al., 2022). On natural data, object discovery has so far been limited to restricted domains with a limited variety of objects, such as YouTube-Aquarium and -Cars (Singh et al., 2022c), or autonomous driving datasets like WaymoOpen or KITTI (Geiger et al., 2013). On more open-ended datasets, previous approaches have struggled (Yang and Yang, 2022). 
To achieve scaling, some works attempt to improve the grouping module, for example by introducing equivariances to slot pose transformations (Biza et al., 2023), smoothing attention maps (Kim et al., 2023), formulating grouping as graph cuts (Pervez et al., 2023) or a stick-breaking process (Engelcke et al., 2021), or by overcoming optimization difficulties by introducing implicit differentiation (Chang et al., 2022; Jia et al., 2023). In contrast, we do not change the grouping module, but use the vanilla slot attention cell (Locatello et al., 2020). 
78
6.2. Related Work 
Another prominent approach is to introduce better training signals than the default choice of image reconstruction. For example, one line of work instead models the image as a distribution of discrete codes conditional on the slots, either autoregressively by a Transformer decoder (Singh et al., 2022a; Singh et al., 2022c), or via diffusion (Jiang et al., 2023; Wu et al., 2023a). While this strategy shows promising results on synthetic data, it so far has failed to scale to unconstrained real-world data (Seitzer et al., 2023). 
An alternative is to step away from fully-unsupervised representation learning by intro-ducing weak supervision. For instance, SAVi (Kipf et al., 2022) predicts optical flow, and SAVi++ (Elsayed et al., 2022) additionally predicts depth maps as a signal for object grouping. Other works add an auxiliary loss that regularizes slot attention’s masks towards the masks of moving objects (Bao et al., 2022; Bao et al., 2023). Our model also has a loss that focuses on motion information, but uses an unsupervised formulation. OSRT (Sajjadi et al., 2022) shows promising results on synthetic 3D datasets, but is restricted by the availability of posed multi-camera imagery. While all those approaches improve on the level of data complexity, it has not been demonstrated that they can scale to unconstrained real-world data. 
The most promising avenue so far in terms of scaling to the real-world is to reconstruct features from modern self-supervised pre-training methods (Caron et al., 2021; He et al., 2022; Assran et al., 2022; Chen et al., 2021b). Using this approach, DINOSAUR (Seitzer et al., 2023) showed that by optimizing in this highly semantic space, it is possible to discover objects on complex real-world image datasets like COCO or PASCAL VOC. In this work, we similarly use such self-supervised features, but for learning on video instead of images. Moreover, we improve upon reconstruction of features by introducing a novel loss based on similarities between features. 
Concurrent Work Parallel to this work, two more slot attention-based methods were proposed that learn object-centric representations on real-world videos: SMTC (Qian et al., 2023) and SOLV (Aydemir et al., 2023). SMTC learns to extracts objects from videos by enforcing semantic and instance consistency over time using a student-teacher approach. SOLV extracts per-frame slots using invariant slot attention (Biza et al., 2023), applies a temporal consistency module and merges slots using agglomerative clustering; the model is also trained using DINOSAUR-style feature reconstruction, but on masked out intermediate frames. 
79
Chapter 6. Scaling Video Object-Centric Learning 
Recurrent Slot Attention 
SlotMixer Decoder 
Slots 
Reconstructed Patch FeaturesReconstruction Loss 
Predicted Probabilities 
Patch Transition Probabilities Similarity Loss 
Self-supervised ViT 
Frame 
Slots 
Patch Features 
Patch FeaturesFrame 
Figure 6.2: Overview of VideoSAUR. Object slots st are extracted from patch features ht 
of a self-supervised ViT using time-recurrent slot attention, conditional on slots from the previous time step t − 1. The model is trained by reconstructing the patch features ht of the current frame xt, and by predicting the similarity distribution over patches of a future frame xt+k (see also Fig. 6.1). The predictions yrec 
t and ysim t are decoded efficiently using 
SlotMixer decoder. 
6.3 Method 
In this section, we describe the main new components of VideoSAUR — our proposed object-centric video model — and its training: a pre-trained self-supervised ViT encoder extracting frame features (Sec. 6.3.1), a temporal similarity loss that adds a motion bias to object discovery (Sec. 6.3.2), and the SlotMixer decoder to achieve efficient video processing (Sec. 6.3.3). See Fig. 6.2 for an overview. 
6.3.1 Slot Attention for Videos with Dense Self-Supervised Rep-resentations 
VideoSAUR is based on the modular video object-centric architecture recently proposed by SAVi (Kipf et al., 2022) and also used by STEVE (Singh et al., 2022c). Our model has three primary components: (1) a pre-trained self-supervised ViT feature encoder, (2) a recurrent grouping module for temporal slot updates, and (3) the SlotMixer decoder (detailed below in Sec. 6.3.3). 
80
6.3. Method 
We start by processing video frames xt, with time steps t ∈ {1, . . . T}, into patch features ht: 
ht = fϕ(xt), ht ∈ RL×D (6.1) 
where fϕ is a self-supervised Vision Transformer encoder (ViT) (Dosovitskiy et al., 2021b) with pre-trained parameters ϕ, and xt is the input at time step t. The ViT encoder processes the image by splitting it to L non-overlapping patches of fixed size (e.g. 16 × 16 pixels), adding positional encoding, and transforming them into L feature vectors ht (see App. D.3.2 for more details on ViTs). Note that the i’th feature retains an association to the i’th image patch; the features thus can be spatially arranged. Next, we transform the features from the encoder with a slot attention module (Locatello et al., 2020) to obtain a latent set st = {sit}Ki=1, sit ∈ RM with K slot representations: 
st = SAθ(ht, st−1). (6.2) 
Slot attention is recurrently initialized with the slots of the previous time step t − 1, with initial slots s0 sampled independently from a Gaussian distribution with learned location and scale. Slot attention works by grouping input features into slots by iterating competitive attention steps; we refer to Locatello et al. (2020) for more details. To train the model, we use a SlotMixer decoder gψ (see Sec. 6.3.3) to transform the slots st to outputs yt = gψ(st). Those outputs are used as model predictions for the reconstruction and similarity losses introduced next. 
6.3.2 Self-Supervised Object Discovery by Predicting Temporal Similarities 
We now motivate our novel loss function based on predicting temporal feature similarities. Video affords the opportunity to discover objects from motion: pixels that consistently move together should be considered as one object, sometimes called the “common fate” principle (Tangemann et al., 2023). However, the widely used reconstruction objective — whether of pixels (Kipf et al., 2022), discrete codes (Singh et al., 2022c) or features (Seitzer et al., 2023) — does not exploit this bias, as to reconstruct the input frame, the changes between frames do not have to be taken into account. 
Taking inspiration from prior work using optical flow as a prediction target (Kipf et al., 2022), we design a self-supervised objective that requires predicting patch motion: for 
81
Chapter 6. Scaling Video Object-Centric Learning 
Affinity Matrix A Transition Probability P 
0.0 0.2 0.4 0.6 0.8 1.0 0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
0.0 0.5 1.0 0.0 0.02 0.04 
Affinity Matrix A Transition Probability P 
0.0 0.2 0.4 0.6 0.8 1.0 0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
0.0 0.5 1.0 0.0 0.01 0.02 
Figure 6.3: Affinity matrix At,t+k and transition probabilities Pt,t+k values between patches (marked by purple and green) of the frame xt and patches of the future frame xt+k in MOVi-C (left) and YT-VIS (right). Red indicates maximum affinity/probability. Also see Fig. D.2.4 for more examples, and our website for an interactive visualization of temporal feature similarities. 
each patch, the model needs to predict where all semantically-similar patches have moved to k steps into the future. By comparing self-supervised features describing the patches, we integrate both semantic and motion information; this is in contrast to optical flow prediction, which only relies on motion. Specifically, we construct an affinity matrix At,t+k 
with the cosine similarities between all patch features from the present frame ht and all features from some future frame ht+k: 
At,t+k = ht 
∥ht∥ · ( 
ht+k 
∥ht+k∥ 
)⊤ 
, At,t+k ∈ [−1, 1]L×L. (6.3) 
As self-supervised features are highly semantic, the obtained feature similarities are high for patches that share the same semantic interpretation. Due to the ViT’s positional encoding, the similarities also take spatial closeness of patches into account. Figure 6.3 shows several example affinity matrices. 
Because there are ambiguities in our similarity-based derivation of feature movements, we frame the prediction task as modeling a probability distribution over target patches — instead of forcing the prediction of an exact target location, like with optical flow prediction. Thus, we define the probability that patch i moves to patch j by normalizing the rows of the affinity matrix with the softmax, while masking negative similarity values (superscripts 
82
6.3. Method 
refer to the elements of the matrix): 
P ij = 
 exp(Aij/τ)∑ 
k∈{j|Aij≥0} exp(Aik/τ) if Aij ≥ 0, 
0 if Aij < 0, 
(6.4) 
where τ is the softmax temperature. The resulting distribution can be interpreted as the transition probabilities of a random walk along a graph with image patches as nodes (Jabri et al., 2020). Then, we define the similarity loss as the cross entropy between decoder outputs and transition probabilities: 
Lsim θ,ψ = 
L∑ l=1 
CE(P l t,t+k; ylt). (6.5) 
Figure 6.1 illustrates the loss computation for an example pair of input frames. 
Why is this Loss Useful for Object Discovery? Predicting which parts of the videos move consistently is most efficient with an object decomposition that captures moving objects. This is similar to previous losses predicting optical flow (Kipf et al., 2022). But in contrast, our loss equation 6.5 also yields a useful signal for grouping when parts of the frame are not moving: as feature similarities capture semantic aspects, the task also requires predicting which patches are semantically similar, helping the grouping into objects e.g. by distinguishing fore- and background (see Fig. 6.3). Optical flow for grouping also has limits when camera motion is introduced; in our experiments, we find that our loss is more robust in such situations. Methods based on optical flow or motion masks can also struggle with inaccurate flow/motion mask labels — unlike our method, which does not require such labels. This is of particular importance for in-the-wild video, where motion estimation is challenging. 
Role of Hyperparameters. The loss has two hyperparameters: the time shift into the future k and the softmax temperature τ . The optimal time shift depends on the expected time scales of movements in the modeled videos and should be chosen accordingly. The temperature τ controls the concentration of the distribution onto the maximum. Thus, it effectively modulates between two different tasks: accurately estimating the patch motion (low τ), and predicting the similarity of each patch to all other patches (high τ). In particular in scenes with little movement, the latter may be important to maintain a meaningful prediction task. In our experiments, we find that the best performance is obtained with a balance between the two, showing that both modes are important. 
83
Chapter 6. Scaling Video Object-Centric Learning 
Final Loss. While the temporal similarity loss yields state-of-the-art performance on synthetic datasets, as shown below, we found that on real-world data, performance can be further improved by adding the feature reconstruction objective as introduced in Seitzer et al. (2023). We hypothesize this is because the semantic nature of feature reconstruction adds another useful bias for object discovery. Thus, the final loss is given by: 
Lθ,ψ = T−k∑ t=1 
Lsim θ,ψ(Pt,t+k, ysim 
t ) + αLrec θ,ψ(ht, yrec 
t ), (6.6) 
where yt = [ysim t ∈ RL×L, yrec 
t ∈ RL×D] is the output of the SlotMixer decoder gψ and α is a weighting factor used to make the scales of the two losses similar (we use a fixed value of α = 0.1 for all experiments on real-world datasets). Like in Seitzer et al. (2023), we do not train the ViT encoder fϕ. 
6.3.3 Efficient Video Object-Centric Learning with the SlotMixer Decoder 
In video models, resource efficiency is of particular concern: recurrent frame processing increases the load on compute and memory. The standard mixture-based decoder de-sign (Locatello et al., 2020) decodes each output K-times, where K is the number of slots, and thus scales linearly with K both in compute and memory. This can become prohibitive even for a moderate number of slots. The recently introduced SlotMixer decoder (Sajjadi et al., 2022) for 3D object-centric learning instead has, for all practical purposes, constant overhead in the number of slots, by only decoding once per output. Thus, we propose to use a SlotMixer decoder gψ for predicting the probabilities Pt,t+k from the slots st. To adapt the decoder from 3D to 2D outputs, we change the conditioning on 3D query rays to L learned positional embeddings, corresponding to L patch outputs ylt. See App. D.3.1 for more details on the SlotMixer module. 
As a consequence of the increased efficiency of SlotMixer, there also is increased flexibility of how slots can be combined to form the outputs. Because of this, this decoder has a weaker inductive bias towards object-based groupings compared to the standard mixture-based decoder. With the standard reconstruction loss, we observed that this manifests in training runs in which no object groupings are discovered. But in combination with our temporal similarity loss, these instabilities disappear (see App. D.2.4). We attribute this to the 
84
6.4. Experiments 
In pu 
t 
MOVi-C 
SA Vi 
ST EV 
E Vi 
de oS 
A U 
R 
MOVi-E     YouTube-VIS 
Figure 6.4: Example predictions of VideoSAUR compared to recent video object-centric methods. 
self-supervised nature of the similarity loss1; having to predict information that is not directly contained in the input increases the difficulty of the task, reducing the viability of non-object based groupings. 
6.4 Experiments 
We have conducted a number of experiments to answer the following questions: (1) Can object-centric representations be learned from a large number of diverse real-world videos? (2) How does VideoSAUR perform in comparison to other methods on well-established real-istic synthetic datasets? (3) What are the effects of our proposed temporal feature similarity loss and its parameters? (4) Can we transfer the learned object-grouping to unseen datasets? (5) How efficient is the SlotMixer decoder in contrast to the mixture-based decoder? 
6.4.1 Experimental Setup 
Datasets To investigate the characteristics of our proposed method, we utilize three synthetic datasets and three real-world datasets. For synthetic datasets, we selected the MOVi-C, MOVi-D and MOVi-E datasets (Greff et al., 2022) that consist of numerous moving 
1Novel-view synthesis, the original task for which SlotMixer was proposed, is similarly a self-supervised prediction task. This may have contributed to the success of SlotMixer in that setting. 
85
Chapter 6. Scaling Video Object-Centric Learning 
objects on complex backgrounds. Additionally, we evaluate the performance of our method on the challenging YouTube Video Instance Segmentation (YT-VIS) 2021 dataset (Yang et al., 2021) as an unconstrained real-world dataset. Furthermore, we examine how well our model performs when transferred from YT-VIS 2021 to YT-VIS 2019 (Yang et al., 2019) and DAVIS (Pont-Tuset et al., 2017b). Finally, we use the COCO dataset (Lin et al., 2014) to study our proposed similarity loss function with image-based object-centric learning. 
Metrics We evaluate our approach in terms of the quality of the discovered slot masks (output by the decoder), using two metrics: video foreground ARI (FG-ARI) (Greff et al., 2019) and video mean best overlap (mBO) (Pont-Tuset et al., 2017a). FG-ARI is a video version of a widely used metric in the object-centric literature that measures the similarity of the discovered objects masks to ground truth masks. This metric mainly measures how well objects are split. mBO assesses the correspondence of the predicted and the ground truth masks using the intersection-over-union (IoU) measure. In particular, each ground truth mask is matched to the predicted mask with the highest IoU, and the average IoU is then computed across all assigned pairs. Unlike FG-ARI, mBO also considers background pixels, and provides a measure of how accurately the masks fit the objects. Both metrics also consider the consistency of the assigned object masks over the whole video. 
In addition, we also use image-based versions of those metrics (Image FG-ARI and Image mBO, computed on individual frames) for comparing with image-based methods. 
Baselines We compare our method with two recently proposed methods for unsupervised object-centric learning for videos: SAVi (Kipf et al., 2022) and STEVE (Singh et al., 2022c). SAVi uses a mixture-based decoder and is trained with image reconstruction. We use the unconditional version of SAVi. STEVE uses a transformer decoder and is trained by reconstructing discrete codes of a dVAE (Rolfe, 2017). Similar to Seitzer et al. (2023), we also add a regular block pattern baseline, corresponding to splitting the video into regular block masks of similar size that do not change over time. By showing the metric values for a trivial decomposition of the video, this baseline is useful to contextualize the results of the other methods. In addition to video-based methods, we compare our model to image-based methods, including DINOSAUR (Seitzer et al., 2023), LSD (Jiang et al., 2023) and Slot Diffusion (Wu et al., 2023a), showing that our approach performs well in both object separation and mask sharpness. Last, we also compare our model to two 
86
6.4. Experiments 
Table 6.1: Comparison with state-of-the-art methods on the MOVi-C, MOVi-E, and YT-VIS datasets. We report foreground adjusted rand index (FG-ARI) and mean best overlap (mBO) over 5 random seeds. Both metrics are computed for the whole video (24 frames for MOVi, 6 frames for YT-VIS). 
MOVi-C MOVi-E YT-VIS 
FG-ARI mBO FG-ARI mBO FG-ARI mBO 
Block Pattern 24.2 11.1 36.0 16.5 24 14.9 SAVi (Kipf et al., 2022) 22.2 ± 2.1 13.6 ± 1.6 42.8 ± 0.9 16.0 ± 0.3 11.1 ± 5.6 12.7 ± 2.3 STEVE (Singh et al., 2022c) 36.1 ± 2.3 26.5 ± 1.1 50.6 ± 1.7 26.6 ± 0.9 20.0 ± 1.5 20.9 ± 0.5 VideoSAUR 64.8 ± 1.2 38.9 ± 0.6 73.9 ± 1.1 35.6 ± 0.5 39.5 ± 0.6 29.1 ± 0.4 
concurrent works discovering objects from real-world video, SMTC (Qian et al., 2023) and SOLV (Aydemir et al., 2023). 
6.4.2 Comparison with State-of-the-Art Object-Centric Learning Methods 
When comparing VideoSAUR to STEVE and SAVi, it is evident that VideoSAUR out-performs the baselines by a significant margin, both in terms of FG-ARI and mBO (see Table 6.1 and Fig. 6.4). On the most challenging synthetic dataset (MOVi-E), VideoSAUR reaches 73.9 FG-ARI. Notably, for the challenging YT-VIS 2021 dataset, both baselines perform comparable or worse than the block pattern baseline in terms of FG-ARI, showing that previous methods struggle to decompose real-world videos into consistent objects. We additionally compare VideoSAUR to image-based methods in App. D.1.1, including strong recent methods (LSD, SlotDiffusion and DINOSAUR), and find that our approach also outperforms the prior image-based SoTA. Finally, in App. D.1.2, we find that our method performs competitively with concurrent work. 
Next, we report how well our method performs in terms of zero-shot transfer to other datasets to show that the learned object discovery does generalize to unseen data. In particular, we train VideoSAUR on the YT-VIS 2021 dataset and evaluate it on the YT-VIS 2019 and DAVIS datasets. YT-VIS 2019 has similar object categories, but a smaller number of objects per image. The DAVIS dataset consists of videos from a fully different distribution than YT-VIS 2021. As the number of slots can be changed during evaluation, we test VideoSAUR with different number of slots, revealing that the optimal number of slots is indeed smaller for these datasets. We find that our method achieves a performance 
87
Chapter 6. Scaling Video Object-Centric Learning 
1 2 3 4 5 6 7 8 Number of slots 
20 
40 
m B 
O 
YouTube-VIS 2019 
1 2 3 4 5 6 7 8 Number of slots 
20 
40 
m B 
O 
DAVIS 
VideoSAUR STEVE Random pattern 
Figure 6.5: Zero-shot transfer of learned object-centric representations on YT-VIS 2021 to the YT-VIS 2019 and DAVIS datasets for different number of slots. 
of 41.3 ± 0.9 mBO on YT-VIS 2019 dataset and 34.0 ± 0.4 mBO on DAVIS dataset (see Fig. 6.5), illustrating its capability to effectively transfer the learned representations to previously unseen data with different object categories and numbers of objects. 
Long-term Video Consistency In addition to studying how VideoSAUR performs on relatively short 6-frame video segments from YT-VIS, we also evaluate our method on longer videos. In App. D.2.1, we show the performance for 12-frame and full YT-VIS videos. While, as can be expected, performance on longer video segments is smaller in terms of FG-ARI, we show that the gap between VideoSAUR and the baselines is large, indicating that VideoSAUR can track the main objects in videos over longer time intervals. Closing the gap between short-term and long-term consistency using memory modules (Traub et al., 2023a; Gumbsch et al., 2021) is an interesting future direction that could be useful for video pre-diction (Wu et al., 2023b) as well as for object-centric goal-based (Zadaianchuk et al., 2021; Mambelli et al., 2022) and model-based (Feng and Magliacane, 2023) reinforcement learning. 
6.4.3 Analysis 
In this section, we analyze various aspects of our approach, including the importance of the similarity loss, the impact of hyperparameters (time-shift k and softmax temperature τ), and the effect of the choice of self-supervised features and decoder. 
Choice of Loss Function (Table 6.2) We conduct an ablation study to demonstrate the importance of the proposed temporal similarity loss, comparing and combining it with the feature reconstruction loss (Seitzer et al., 2023). We also consider predicting the 
88
6.4. Experiments 
features of the next frame (see App. D.3.4 for implementation details). For all datasets, feature reconstruction alone performs significantly worse than the combination of feature reconstruction and temporal similarity loss. Predicting the features of the next frame in addition to feature reconstruction also yields improved performance, but is worse than the temporal similarity, suggesting that the success of our loss can be partially explained by the integration of temporal information through future prediction. Interestingly, on MOVi-C, using the temporal similarity loss alone significantly improves the performance over feature reconstruction (+20 FG-ARI, +7 mBO). To provide insight into the qualitative differences between the losses, we analyze the videos with the most significant differences in FG-ARI (see Fig. D.5.4): unlike feature reconstruction, the temporal similarity loss does not fragment the background or large objects into numerous slots, and it exhibits improved object-tracking capabilities even when object size changes. To gain further insights, we also consider (ground truth) optical flow as a prediction target that only captures motion, but no semantic information (see App. D.2.2 for a detailed discussion). We find that only predicting optical flow is not enough for a successful scene decomposition, underscoring the importance of integrating both motion and semantic information for real-world object discovery. 
Table 6.2: Loss Ablation on MOVi-C and YT-VIS. 
MOVi-C YT-VIS 
Feat. Rec. Next Frame Feat. Pred. Temp. Sim. FG-ARI mBO FG-ARI mBO 
✓ 40.2 23.5 35.4 26.7 ✓ ✓ 47.2 24.7 37.9 27.3 
✓ 60.8 30.5 26.2 29.1 ✓ ✓ 60.7 30.3 39.5 29.1 
Robustness to Camera Motion (Table 6.3) Next, we investigate if VideoSAUR training with the similarity loss is robust to camera motion, as such motion makes isolating the object motion more difficult. As a controlled experiment, we compare between MOVi-D (without camera motion) and MOVi-E (with camera motion), and train VideoSAUR using only the temporal similarity loss. We contrast with SAVi trained with optical flow prediction2, and find that VideoSAUR is more robust to camera motion, performing better on the MOVi-E dataset than on the MOVi-D dataset (+6.8 vs −16.7 FG-ARI for SAVi). 
2SAVi results with optical flow are from Greff et al. (2022). 
89
Chapter 6. Scaling Video Object-Centric Learning 
Table 6.3: Robustness to introducing camera motion (MOVi-D → MOVi-E). 
MOVi-D MOVi-E 
SAVi (optical flow) 19.4 2.7 VideoSAUR (temporal sim.) 55.7 62.5 
Choice of Decoder (Table 6.4) We analyze how our method performs with differ-ent decoders and find that both the MLP broadcast decoder (Seitzer et al., 2023) and our proposed SlotMixer decoder can be used for optimizing the temporal similarity loss. VideoSAUR with the MLP broadcast decoder achieves similar performance on YT-VIS and MOVi datasets, but requires 2–3 times more GPU memory (see App. D.3.1 for more details and Table D.2.3 for the detailed comparison of decoders on MOVI-E dataset). Thus, we suggest to use the SlotMixer decoder for efficient video processing. 
Table 6.4: Decoder comparison on MOVi-C and YT-VIS. 
MOVi-C YT-VIS Memory 
FG-ARI mBO FG-ARI mBO GB @24 slots 
Mixer 60.8 30.5 39.5 29.1 24 MLP 64.2 27.2 39.0 29.1 70 
Softmax Temperature (Figure 6.6a) We train VideoSAUR with DINO S/16 features using different softmax temperatures τ . We find that there is a sweet spot in terms of grouping performance at τ = 0.075. Lower and higher temperatures lead to high variance across seeds, potentially because there is not enough training signal with very peaked (low τ) and diffuse (high τ) target distributions. 
Target Time-shift (Figure 6.6b) We train VideoSAUR with DINO S/16 features using different time-shifts k to construct the affinity matrix At,t+k. On both synthetic and real-world datasets, k = 1 generally performs best. Interestingly, we find that for k = 0, performance drops, indicating that predicting pure self-similarities is not a sufficient task for discovering objects on its own. 
Choices for Self-Supervised Features (Figures 6.6c and 6.6d) We study two questions about the usage of the ViT features: which ViT features (queries/keys/val-
90
6.5. Conclusion and Future Work 
ues/outputs) should be used for the temporal similarity loss? Do different self-supervised representations result in different performance? 
In Fig. 6.6c, we observe that using DINO “key” and “query” features leads to signifi-cantly larger mBO, while for FG-ARI “query” is worse and the other features are similar. Potentially, this is because keys are used in the ViT’s self-attention and thus could be particularly good to compare with the scalar product similarity. Consequently, VideoSAUR uses “key” features in all other experiments. Moreover, we study if the temporal similarity loss is compatible with different self-supervised representations. In Fig. 6.6d, we show that VideoSAUR works well with 4 different types of representations, with MSN (Assran et al., 2022) and DINO (Caron et al., 2021) performing slightly better than MAE (He et al., 2022) and MOCO-v3 (Chen et al., 2021b). We also demonstrate that further fine-tuning the DINO features utilizing a self-supervised temporal-alignment clustering approach named Time-Tuning (Salehi et al., 2023) on unlabeled videos enhances the mask quality of VideoSAUR. 
Pre-training Dataset (Table 6.5) All self-supervised methods we utilize are trained on the ImageNet dataset, which a) has a strong bias towards object-centricness as its images mostly contain single objects, and b) introduces a large number of additional images external to the dataset we are training VideoSAUR on. An interesting question is whether a) and b) are actually required for the success of our method. To answer it, we train a ViT-B/16 encoder from scratch on the MOVi-E dataset using the MAE method, and then train VideoSAUR using the obtained features. Interestingly, we find that the features from MOVi-E yield similar results compared to ImageNet-trained features (although with slight drops in mask quality), demonstrating that VideoSAUR is able to perform high-quality object discovery even without access to external data. This result also has broader implications as it potentially increases the applicability of feature reconstruction-based object-centric methods to datasets fully out of the domain of ImageNet. It also raises a follow-up question: what properties of the pre-training dataset (and method) are important to obtain good target features for object discovery? 
6.5 Conclusion and Future Work 
This paper presents the first method for unsupervised video-based object-centric learning that scales to diverse, unconstrained real-world datasets such as YouTube-VIS. By leveraging 
91
Chapter 6. Scaling Video Object-Centric Learning 
0.01 0.05 0.2 0.5 
40 
60 
FG -A 
R I 
MOVi-C 
Optimal  temp. 
(a) Softmax temperature τ . 
0 1 2 3 
0 
20 
40 
60 
FG -A 
R I 
0 1 2 3 0 
10 
20 
30 
m B 
O 
MOVi-C 
0 1 2 3 0 
10 
20 
30 
FG -A 
R I 
0 1 2 3 0 
10 
20 
30 
m B 
O 
YT-VIS 
(b) Target time-shift k on MOVi-C and YT-VIS datasets. 
50 55 60 65 
FG -A 
R I 
25 30 35 40 
m B 
O 
Query Value Output Key 
(c) DINO ViT features. 
50 55 60 65 
FG -A 
R I 
25 30 35 40 
m B 
O 
MAE MOCO-v3 MSN DINO DINO w/ TimeT 
(d) Self-supervised representation method. 
Figure 6.6: Studying the effect of different parameters of the temporal similarity loss. 
Table 6.5: Comparing VideoSAUR with features trained on MOVi-E (MAE+MOVi-E) to features trained on ImageNet (MAE+ImageNet). For MAE+MOVi-E, we pre-train a ViT-B/16 using the self-supervised MAE method on MOVi-E for 200 epochs. VideoSAUR is able to perform high-quality object discovery even without access to any external data. 
MOVi-C MOVi-E 
FG-ARI mBO FG-ARI mBO 
VideoSAUR w/ MAE+ImageNet features 58.0 30.4 72.8 27.1 VideoSAUR w/ MAE+MOVi-E features 59.8 27.5 70.6 23.3 
dense self-supervised features and extracting motion information with temporal similarity loss, we demonstrate superior performance on both synthetic and real-world video datasets. We hope our new loss function can inspire the design of further self-supervised losses for object-centric learning, especially in the video domain where natural self-supervision is available. 
Limitations and Future Work Directions Our method does not come without limitations: in longer videos with occlusions, slots can get reassigned to different objects or the background (see Fig. D.2.5 for visualizations of failure cases). VideoSAUR also inherits a limitation of all slot attention-based method, namely that the the number of slots is static and needs to be chosen a priori. Similar to DINOSAUR (Seitzer et al., 2023), 
92
6.5. Conclusion and Future Work 
the quality of the object masks is restricted by the patch-based nature of the decoder. Finally, while the datasets we use in this work are significantly less constrained compared to datasets used by prior work, they still do not capture the full open-world setting that object-centric learning aspires to solve. Overcoming these limitations is a great direction for future work. 
93
7 
Discussion 
In this dissertation, we concentrate on two challenging questions: discovering structure from real-world data and utilizing structure by autonomous agents. Addressing these questions can equip agents with skills that are composable and flexible enough for solving tasks in real-world open-ended environments, enabling agents to operate on general high-dimensional observations as inputs. 
7.1 Using Structure for Autonomous Agents 
In the first part of this dissertation (Chapter 3 and Chapter 4), we study potential solutions to the second question of the efficient use of structure by autonomous agents. We propose the SMORL and SRICS methods to tackle compositionally challenging tasks, such as the rearrangement of many objects in a scene. To master these tasks, an agent should first explore the environment efficiently, learning to control parts of the environment that are mostly independent. After this, the agent can reuse and combine learned skills to solve more complex tasks in the same environment. 
In Chapter 3, we explore strategies for leveraging object-centric structures to decompose environment observations into set-based or object-centric representations efficiently and use them for control. We demonstrate how the discovery of the environment structure in the form of objects facilitates goal-based exploration of environmental subspaces, leading to 
95
Chapter 7. Discussion 
more versatile agents. These agents can solve compositional tasks by combining basic skills acquired during goal-based exploration. Furthermore, they exhibit enhanced generalization capabilities in environments with partially similar structures, such as those with varying numbers of objects. 
While SMORL has proven to be effective in image-based compositional environments, it also has several limitations that open up avenues for future research. First and foremost, SMORL operates under the assumption that objects do not interact with each other. Under this assumption, objects can be controlled sequentially in any order. Addressing more complex scenarios where objects interact with each other becomes an essential direction for future exploration (Zadaianchuk et al., 2022; Feng and Magliacane, 2023; Haramati et al., 2023). In this thesis, we propose a potential solution to this challenge (Zadaianchuk et al., 2022), suggesting the integration of a sparse Graph Neural Network (GNN) to learn the dynamics of the environment and the corresponding interaction graph. The interaction graph is used for learning to control objects independently from the parts of the environment that are not needed to solve the control problem. 
Chapter 3 illustrates the utility of object-centric structures in a specific goal-conditioned reinforcement learning framework. Although this approach is a natural fit for autonomous goal-based control, as discussed in Section 2.1.4, it is crucial to investigate the effective-ness of object-centric representations across various reinforcement learning and control settings (Watters et al., 2019a; Veerapaneni et al., 2019; Yoon et al., 2023; Nath et al., 2023; Feng and Magliacane, 2023). To this end, Yoon et al. (2023) conducted a compre-hensive study on the application of several object-centric representation methods to a diverse range of control tasks. Their findings indicate that while methods equipped with object-centric representations do not consistently outperform methods with fixed-based representations, they excel in tasks requiring relational reasoning and demonstrate robust out-of-distribution generalization when encountering unseen objects. Thus, further inves-tigation into the usage of more advanced object-centric representation learning methods such as DINOSAUR (Seitzer et al., 2023) and VideoSAUR (Zadaianchuk et al., 2023a) in the different RL frameworks, for example in offline RL (Fujimoto et al., 2019; Gürtler et al., 2023; Levine et al., 2020) or unsupervised skills discovery (Sharma et al., 2019; Park et al., 2023) could further reveal the areas where object-centric structure is beneficial for sequential decision making. 
Finally, the skills discovered by SMORL’s goal-conditional policy are based on specific object instances, assuming a unique identity for each object. While this approach yields good 
96
7.1. Using Structure for Autonomous Agents 
results when dealing with a small number of uniquely characterized objects, this assumption might not scale when developing general-purpose agents that interact with numerous objects spanning different categories. Therefore, it is crucial to investigate more structured object representation formats. Such formats should additionally decouple object properties or attributes (Singh et al., 2022b; Mansouri et al., 2022) and facilitate the identification of object categories (Zadaianchuk et al., 2023b). Utilizing more granular representations can enhance the sample efficiency of the reinforcement learning algorithm (Yi et al., 2022). In addition, incorporating class-based object-centric representations has proven to be advantageous for model-based reinforcement learning (Feng and Magliacane, 2023). 
In Chapter 4, we further study object-centric agents in more realistic environments where objects can interact with each other. To account for object interactions, we propose to learn a graph-based (relational) latent representation of the environments from the objects’ dynamics observations. We discover environment structure in the form of a (sparse) interaction graph between the entities in the environment. Having discovered additional structural information, an agent can propose and master skills of achieving different subgoals independently. We show that such skills are helpful for the agent to decompose complex external tasks into a sequence of subtasks such that achieving each subtask does not destroy the previously achieved subtask. 
Below, we discuss several open questions in Chapter 4 that could be valuable directions for future work. First, one can extend SRICS to image-based object-centric representations, making it more applicable to realistic robotic settings where only high-dimensional sensory information is provided to the agent. Efficient dynamics graph discovery from images is still an open question that could be addressed by causal representation learning on the high dimensional time-series data (Schölkopf et al., 2021; Lippe et al., 2023; Mansouri et al., 2023). 
Causal representation learning seeks to identify causal variables from complex inputs like visual observations. Identifying causal variables solely from observational data is not feasible; however, the use of interventional data can enable this. Previous methods often assume either known intervention targets (Lippe et al., 2022) or a high-level action space, e.g., clicking on an object to act with it (Lippe et al., 2023). However, in realistic scenarios, the relations between the action space and the causal variables are typically unknown. 
To discover the causal structure in a realistic environment, an agent should learn a set of diverse interventions in the environment (similar to skills learned from achieving indepen-dently controllable subgoals with SRICS) while having access only to high-dimensional 
97
Chapter 7. Discussion 
inputs and with an action space decoupled from the causal variables. Simultaneously, the agent should learn a causal representation of the environment with the results of the interventions affecting only specific parts of the representation. This task could be viewed as an unsupervised skill discovery (Sharma et al., 2019; Park et al., 2022; Park et al., 2023) from image-based observations. While previous methods maximize the diversity of learned skills, they do not aim to discover causal skills that affect the causal graph in a particular way. Coupling such methods with additional objectives to affect only parts of the learned latent space is a promising direction towards causal skill discovery. Such joint training of the agent and representation could not only facilitate an active discovery of causal mechanisms but also enhance agent control over the environment’s causal variables. 
Finally, we expect that SRICS can be combined with different modular curriculum learning and exploration strategies (Colas et al., 2019; Blaes et al., 2019; Sancaktar et al., 2022). Actively acquiring data for training structural latent dynamics (i.e. when the data for training is collected by an agent that actively explores the environment and intervenes in the discovered structure) can further improve the discovery of the essential structures in the environment. 
7.2 Discovering Structure from Real-World Datasets 
In the second part of this thesis (Chapter 5 and Chapter 6), we study structure discovery from unlabeled datasets. Previously proposed methods for discovering object-centric structures are applicable only to datasets of limited complexity. In contrast, we study how to scale object-centric representation learning to discover objects and their categories in real-world datasets with complex images and videos. In Chapter 5 and Chapter 6, we further broaden the applicability of the object-centric representation to such real-world unconstrained datasets like COCO (Lin et al., 2014) and YouTube-VIS (Yang et al., 2019). 
In Chapter 5, we propose to use object-centric datasets, e.g., ImageNet dataset (Deng et al., 2009), on which localization and categorization priors can be learned in a self-supervised way without any human annotations. We show that combining these priors together is a simple and efficient way to discover structure in the form of object categories present in the dataset. For example, we can discover 19 from 20 object categories present in the PASCAL VOC image dataset. Next, we show that such a structure (i.e., a cluster ID and distance to the cluster center) can be used for learning semantic segmentation without supervision from 
98
7.2. Discovering Structure from Real-World Datasets 
human annotations. In particular, we show that using such structured object proposals with an iterative self-training procedure leads to significant improvements over previous approaches that rely on dense self-supervised representation learning. This combination reveals the hidden potential of object-centric datasets and allows the creation of a strong baseline for unsupervised segmentation methods effectively decomposing multi-category scenes into semantically meaningful parts. 
While our method COMUS demonstrates promising results in the challenging domain of unsupervised object segmentation, certain limitations are inevitable given the unsupervised nature of the method. First, our approach, despite reducing reliance on the categorization and localization priors obtained from object-centric datasets, is still limited by their applicability to the target dataset. For example, COMUS still fails to segment objects that are rarely marked as salient by the original DeepUSPS method (Nguyen et al., 2019) and segments only one salient object proposal per image. Thus, determining the optimal number of localization proposals (Ziegler and Asano, 2022; Li et al., 2022) as well as learning or fine-tuning the (multi-object) localization and categorization priors jointly on the dataset of interest is a noteworthy future work direction. We make the first steps in this direction by studying object-centric methods that do not require a localization prior and operate from dense self-supervised features (Van Gansbeke et al., 2022; Seitzer et al., 2023; Zadaianchuk et al., 2023a). This way, future work can extend category discovery and unsupervised semantic segmentation to operate purely from scene-based data. 
Additionally, determining the optimal number of categories present in the dataset poses another open problem. Currently, we set the number of clusters for spectral clustering based on the known number of categories. While COMUS continues to perform adequately even when the number of clusters is increased, establishing the optimal number of clusters au-tonomously remains an essential objective in a truly open-ended data exploration framework. 
In Chapter 6, we further explore object structure discovery from unconstrained real-world inputs. We show that dense self-supervised features are great targets for object-centric representation learning from real-world image (Seitzer et al., 2023) and video (Zadaianchuk et al., 2023a) datasets. For the video domain, we propose a novel self-supervised task of predicting temporal similarities of self-supervised features utilizing both motion and semantic cues to discover objects in videos. By solving this task, VideoSAUR scales unsu-pervised video-based object-centric learning to diverse real-world datasets such as DAVIS or YouTube-VIS. Using such powerful scene decomposition could be a core component for several exciting future directions. 
99
Chapter 7. Discussion 
First, VideoSAUR can be extended to consistently represent objects over time in long videos, particularly in more challenging visual scenes featuring object occlusions and reappearance. Currently, similar to SAVi (Kipf et al., 2022), slot initialization is used as the primary mechanism for automatic slot matching between frames. However, this mechanism introduces a strong bias toward object persistence in each video frame. This assumption is unrealistic for unconstrained video data where objects can be fully occluded or appear in the middle of the video. To further scale object-centric representations to the complexity of real-world environments, employing latent memory modules (Gumbsch et al., 2021; Zhao et al., 2023) and a strategy for merging current frame representations with latent scene representations (Jiang et al., 2020) could be beneficial. Additionally, allowing a flexible number of slots per image (Aydemir et al., 2023; Anonymous, 2023) could further enhance VideoSAUR’s applicability to scenes of varying complexity. Such consistent and flexible object-centric representations could be directly used as the goal space for model-free goal-based control, enabling agents to decompose real-world observations into meaningful subgoal spaces. 
Next, while having consistent object-centric models is desirable, it is not sufficient if the aim is to use such models for trajectory planning into the future, thereby enabling the model to learn from outcomes in its latent space (Hafner et al., 2020; Kipf et al., 2020). We need to learn a dynamics module to predict future object-centric representations for several future steps. Such dynamics module can be trained on top of already learned object-centric representations (Wu et al., 2023b; Zadaianchuk et al., 2022) or jointly with object-centric representations (Veerapaneni et al., 2019). Joint training of the object-centric representations and multi-step dynamics predictions in the latent space is a good objective for video-based object-centric learning, as it also requires combining multi-step motion and semantics information to be successfully solved. 
Finally, while current object-centric models, such as DINOSAUR (Seitzer et al., 2023) and VideoSAUR (Zadaianchuk et al., 2023a), based on the slot attention module, assume deterministic representations for each scene, generalizing them to stochastic versions could further increase their applicability in real-world stochastic environments. 
Overall, we hope that such generally applicable and scalable object-centric methods for the discovery of objects in unconstrained real-world scenes will be useful for numerous down-stream tasks, including causal representation learning, dynamics learning, and autonomous reinforcement learning. 
100
Appendix 
101
A 
Appendix for Chapter 3 
A.1 Analysis of Representations Learned by SCALOR 
A.1.1 Clustering of zwhat components 
In this section, we analyze the representations learned by SCALOR. First, we looked at how well different detections of the same object cluster together in the zwhat space SCALOR learns. This is important in order to find out whether we can use distances in zwhat space to match corresponding objects which is necessary to compute rewards for the agent (see Sec. 3.3.2). A well-separated zwhat space also indicates the usefulness of SCALOR’s representations for other potential downstream tasks such as classification. In Fig. A.1, we plot the first and second principal component of points in zwhat space, and color each point according to the mean pixel value of the foreground object in the crop detected by SCALOR. As one can see, the three objects (green, blue, and red points) and the robotic arm (darker red points) are quite well separated, with relatively low intra cluster variance. The robotic arm cluster shows larger variance as it is observed in more different poses than the objects. There is also a small cluster of misdetections (center top), with the gray color of the table. Overall, this shows that the zwhat space is well suited for the purpose of matching. 
103
Appendix A. Appendix for Chapter 3 
1st PCA dimension of zwhat 
2nd PC 
A di 
m en 
si on 
of zw 
ha t 
Analysis of clustering in SCALOR’s zwhat space 
Figure A.1: First and second PCA dimension of zwhat space of SCALOR trained on Visual Rearrange with 3 objects. The plot shows 3000 random zwhat points collected from a random policy. Each point is colored as the mean of the foreground pixels on the crop detected by SCALOR. For each cluster, the highlighted point shows an example crop. Dashed lines indicate the Voronoi partitions according to cluster centers found by running k-means clustering. Figure is best viewed on screen. 
A.1.2 Disentanglement analysis of representations learned by SCALOR and VAE 
After seeing that SCALOR representation can be successfully used for object classification, we further examined the quality of the object location information learned by SCALOR by evaluating how disentangled they are. For this, we computed Mutual Information Gap (MIG) (Chen et al., 2018b) scores for SCALOR and VAE components. As SCALOR representations are unordered sets of vectors, we used the clusters obtained from the cluster analysis (see App. A.1.1) to produce a vector zwhere 
vec that has consistent dimension ordering by matching zwhat components to clusters. In the case of an object not being recognized in an image, we imputed zeros values to its part in the vector zwhere 
vec . We estimated MIG by adapting the disentanglement_lib (Locatello et al., 2019), with an additional discretization of the continuous ground truth factors in the same way the continuous latent 
104
A.1. Analysis of Representations Learned by SCALOR 
space is discretized. 
The results in Fig. A.2 show that SCALOR’s zwhere components are more disentangled and thus are better suited for the construction of independent RL sub-tasks. In addition, it can be seen that the VAE disentanglement score is quite low, potentially because different factors of variation (object coordinates) have the same variance and thus could be more difficult to disentangle (Rolinek et al., 2019). 
SCALOR VAE 0.0 
0.1 
0.2 
0.3 
M IG 
(a) MIG score (higher is better). 
0 1 2 3 4 5 6 7 GT coordinates 
1 0 
3 2 
5 4 
7 6 
zw 
he 
re 
SC 
A L 
O R 
fe at 
ur es 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
(b) Mutual information matrix for SCALOR represen-tations. 
Figure A.2: Comparison of VAE and SCALOR representations. (a) shows MIG scores of VAE and SCALOR representations on data obtained from running a random policy in the Visual Rearrange environment with 3 objects (with whisker showing the standard deviation over 5 runs), (b) shows the mutual information matrix for SCALOR representations on the same data. 
A.1.3 SCALOR trajectory traversals 
One of the ways to evaluate the quality of learned representations is to show how it reconstructs the scene. To this end, Fig. A.3 shows some example environment traversals and how SCALOR processes them. SCALOR is not only able to reconstruct the final image, but in addition is also able to locate objects and produce accurate segmentation masks for each object. 
105
Appendix A. Appendix for Chapter 3 
A.2 Ablation Analysis of Goal-conditioned Attention Policy 
To understand how important the contribution of the goal-conditioned attention policy is to the performance and the generalization properties of our architecture, we have compared it with several other options for processing the set of SCALOR representations. In particular, we test two more variants of our attention mechanism: one where we use only goal-conditional attention heads, and one where we use only goal-unconditional heads with learned, input-independent queries. We hypothesize that using only goal-conditional heads reduces the ability of the policy to easily concentrate on parts of the environment that are globally relevant for all tasks. Using only goal-unconditional heads with learned queries should still allow the policy to learn to order the input representations and produce a consistent fixed-length vector; however, it removes the ability to flexibly select parts of the inputs based on the task at hand. Finally, we also implemented the DeepSet method (Zaheer et al., 2017) as an alternative approach to process inputs of sets of vector representation. In our case, we instantiate DeepSets by transforming each component embedding with one hidden layer MLP with ReLU activation to feature vectors of dimensionality 128 and then summing up these vectors. 
The results in Fig. A.4 show that both types of attention heads are necessary to achieve the best results, with the goal-conditional heads having a larger impact on the final performance. Without the goal-conditional heads, the SMORL algorithm performs significantly worse. In addition, we observe that SMORL with DeepSets can also perform competitively on the two object tasks, however, it is significantly worse on the out-of-distribution task with one object. 
A.3 Longer Training for Visual Rearrange with Two Objects 
For the challenging Visual Rearrange environment with 2 objects, we trained a SMORL agent for twice as long as in the main plot in Fig. 3.4 to better understand the final convergence performance (see Fig. A.5). Whereas the RIG baseline still shows no signs of progress after one million timesteps, our SMORL agent is continuing to improve performance. 
106
A.4. Implementation Details 
This result hints at that with even more training steps, SMORL might eventually reach the performance of a SAC agent that has privileged information of the ground-truth state. 
A.4 Implementation Details 
A.4.1 Details of Attention Mechanism 
As discussed in Sec. 3.3.1, the policy should be able to select from the set of input representations based on the goal it needs to solve. We implement this by running attention with a goal-dependent query Q(zg) = zgW q. However, there might be some parts of the input state that are always relevant to the policy, regardless of the current goal. For example, in our experiments, we expect the state of the robotic arm to always be important, as it is needed to manipulate objects. To simplify the extraction of this information for the policy, we optionally add M learned, input-independent, goal-unconditional queries Q(P q) to the goal-dependent query. P q ∈ RM×de is simply a matrix of parameters that is trained via backpropagation; we initialize P q by sampling from N (0, 0.02). Furthermore, we use two separate sets of attention heads to process the goal-conditional and -unconditional queries, i.e. each set of attention head has its own set of projections W q, W v, W k. The output of both sets of attention heads is simply concatenated before feeding it to the next stage of the policy. 
We use Pytorch’s (Paszke et al., 2019) torch.nn.MultiheadAttention module to imple-ment the attention mechanism. In practice, we use two separate instantiations of these modules to implement goal-conditional and goal-unconditional heads. In accordance to the original transformer attention formulation (Vaswani et al., 2017), this module also includes a linear transformation that mixes the outputs of the different heads together. As we think this transformation is not strictly necessary, we have omitted it for notational clarity. Moreover, note that we also linearly embed the policy inputs zg and zt,n’s into a common space of dimensionality de before processing them further, which we have found to slightly improve performance. 
A.4.2 Full SMORL Training and Evaluation Algorithms 
We display a fully detailed version of the training algorithm in Alg. 4. In addition, Alg. 5 shows how we apply SMORL during evaluation. For evaluation, the agent receives a 
107
Appendix A. Appendix for Chapter 3 
goal image to achieve from the environment. After processing this image into latent representations with SCALOR, the agent picks one of the recognized objects as its sub-goal and attempts to achieve it for a fixed number of time steps. Following this, the agent sequentially moves on to the next object in the goal image that is not solved and repeats this process until either all goals are solved, or the agent runs out of evaluation time steps. For our purpose, we define a goal as solved when the zwhere component of the best matching object from the observation is closer to the zwhere component of the sub-goal than some threshold. 
Algorithm 4 SMORL: Self-Supervised Multi-object RL (Training with Details) Require: SCALOR encoder qϕ, goal-conditioned policy πθ, goal-conditioned value function Qw, number 
of data points from random policy N , number of training episodes K, number of time steps in the episode H 
1: Collect D = {oi}N i=1 using random initial policy. 
2: Train SCALOR on sequences data uniformly sampled from D using loss described in Eq. 2.2.3.2. 3: Fit prior p(zwhere | zwhat) to the latent encodings of observations 
{( zwhere 
i , zwhat i 
)}N 
i=1 obtained using qϕ(zt | z<t, o≤t). 
4: for n = 1, ..., K episodes 5: for t = 1, ..., H steps 6: if t = 1 7: Generate goal zg = 
( ẑwhere 
g , zwhat g 
) using SCALOR and initial observation o1 (pick random 
detected object k and substitute zwhere by sampled from prior ẑwhere g ∼ p(zwhere | zwhat)). 
8: Encode zt using qϕ(zt | z<t, o≤t). 9: Get action at ∼ πθ(at | zt, zg). 
10: Execute at and get next state observation ot+1 from environment. 11: Encode zt+1 using qϕ(zt+1 | z≤t, o≤t+1). 12: Store (zt, at, zt+1, zg) into replay buffer R. 13: With probability 0.5, replace ẑwhere 
g with a sample p(zwhere | zwhat). ▷ Sample “imagined” goals 14: Sample transition (z, a, z′, zg) ∼ R. 15: Compute matching reward signal R = r(z′, zg) using Eq. 3.3. 16: Minimize Bellman Error using (z, a, z′, zg, R). 17: for l = t, ..., H steps 18: Sample future state ohi that has matching component in observation representation set zhi to 
the original goal zg, l < hi ≤ H − 1. ▷ Sample HER “future” goals 19: Store (zl, al, zl+1, zhi,k) into R (for k such that zhi,k is matching the original goal zg). 
108
A.4. Implementation Details 
Algorithm 5 SMORL (Evaluation) Require: Trained SMORL agent πθ, goal image og, SCALOR encoder qϕ, evaluation episode length L, 
sub-goal episode length l 
1: Get goal representation zg = {zm}N m=1 = qϕ(og) where N is the number of recognized objects. 
2: Get the number of attempts K = L l . 
3: Initialize goal index m = 1. 4: Initialize evaluation step t = 1. 5: for k = 1, ..., K steps 6: Obtain initial observation o1 and pick sub-goal zm. 7: for s = 1, ..., l steps 8: Encode zt using qϕ(zt | z<t, o≤t). 9: Get action at ∼ πθ(at | zt, zm). 
10: Execute at and get next observation ot+1 from environment. 11: Set t = t + 1. 12: if all sub-goals zm are solved 13: Stop evaluation. 14: Set m = (m + 1) mod N . 15: while zm is solved 16: Set m = (m + 1) mod N . 
A.4.3 SCALOR 
We are using the SCALOR implementation from the original authors1. The parameters that were modified from the default settings can be found in Table A.1. In particular, we are using zwhat dimension equal to 8 for 1 object and equal to 4 for two objects. We observed that using smaller dimensionalities for zwhat makes the training more stable, if it is possible to train SCALOR with it. As for our purpose, the background model is not important, and our environments have stable backgrounds, for this work, we are modeling the background with small zbg = 1. 
During RL training, we process the first observation o1 of each episode 5 times with SCALOR which we found to stabilize the inferred representations. During evaluation, we do the same with the goal images og given from the environment. 
1https://github.com/JindongJiang/SCALOR 
109
Appendix A. Appendix for Chapter 3 
Hyper-parameter Value Optimizer Adam (Kingma and Ba, 2015) with default settings 
Number of iterations 5000 Learning rate 0.0001 
Batch size 11 Explained Ratio Threshold 0.1 Number of training points 10000 
Number of cells 4 Size bias 0.22 
Size variance 0.12 Ratio bias 1.0 
Ratio variance 0.3 Table A.1: SCALOR hyper-parameters. 
A.4.4 SMORL 
We refer to Table A.2 for general hyper-parameters of SMORL and to Table A.3 for environment-specific hyper-parameters of SMORL. 
A.4.5 Prior Work 
For the baselines, i.e. SAC, RIG, and Skew-Fit, we started from standard settings and made environment-specific tweaks to tune them for the best performance. In particular, significant hyperparameter search effort (>500 runs) was spent on finding the best SAC parameters for Multi-Object Visual Rearrange 2, 3, and 4 objects. 
A.5 Problems with SCALOR Tracking during RL Training 
During our experimentation with the reward specification, we first consider SCALOR’s internal tracking of objects. SCALOR assigns each discovered object an ID, and these IDs are in principle propagated over time steps. By matching IDs, one can easily compute distances to the goal zg in the space of the zwhere component (because we pick the episode 
110
A.5. Problems with SCALOR Tracking during RL Training 
Hyper-parameter Value Optimizer Adam with default settings 
Exploration Noise None (SAC policy is stochastic) RL Batch Size 2048 Reward Scaling 1 
Automatic SAC entropy tuning yes SAC Soft Update Rate 0.05 
# Training Batches per Time Step 1 Hidden Activation ReLU 
Network Initialization Xavier uniform Separate Attention for Policy & Q-Function yes 
Replay Buffer Size 100000 Relabeling Fractions Rollout/Future/Imagined Goals 0.1 / 0.4 / 0.5 
Number of Initial Random Samples 10000 Table A.2: General hyper-parameters used by SMORL for visual environments. 
goal from the objects discovered in the first observation during RL training). However, with such a reward specification, the agent easily finds ways to exploit the biases towards a position in the propagation of the representation to the next time step. 
In particular, one underlying assumption of SCALOR is that "two objects cannot coexist in the same position" (Jiang et al., 2020). However, due to 2D-projecting the 3D objects and possible occlusions, this assumption is not always fulfilled, and the RL agent is able to exploit this during training. For example, the agent learns to position the robotic arm exactly above the object, and due to the positional propagation, this object’s component is then propagated to the arm. After this, the agent was able to "manipulate" this component just by positioning his arm to the object’s goal. This shows the importance of evaluating learned representations in downstream tasks. 
111
Appendix A. Appendix for Chapter 3 
Hyper-parameter Push, 1 Obj. Push, 2 Obj. Training Path Length 15 15 
Evaluation Path Length 45 75 Learning Rate 0.001 0.0007 
Discount Factor 0.925 0.95 Matching Threshold α 1.2 1.3 
No Match Reward rno goal 0.75 1.0 zwhat Dim 8 4 
Embedding Dim de 48 32 Number of Cond./Uncond. Heads 3/0 1/1 
Number of Input-Independent Queries 0 3 Policy Hidden Sizes [128, 128] [128, 128, 128] 
Q-Function Hidden Sizes [256, 256, 256] [128, 128, 128] 
Hyper-parameter Rearrange, 1 Obj. Rearrange, 2 Obj. Training Path Length 20 20 
Evaluation Path Length 60 100 Learning Rate 0.001 0.0005 
Discount Factor 0.95 0.925 Matching Threshold α 1.2 1.3 
No Match Reward rno goal 0.75 1.5 zwhat Dim 8 4 
Embedding Dim de 48 32 Number of Cond./Uncond. Heads 3/0 1/1 
Number of Input-Independent Queries 0 3 Policy Hidden Sizes [64, 64] [128, 128, 128] 
Q-Function Hidden Sizes [128, 128, 128] [128, 128, 128] Table A.3: Environment-specific hyper-parameters used by SMORL for visual environments. 
112
A.5. Problems with SCALOR Tracking during RL Training 
Visual Rearrange environment with 2 objects 
Visual Rearrange environment with 3 objects 
Figure A.3: Reconstructions of scene observations using learned SCALOR representation and decoder. Rows are a) original images (green boxes for recognized objects, red boxes for non-propagated objects), b) full reconstructions, c) bounding boxes of recognized objects produced using zwhere, d) foreground object reconstructions, e) segmentation masks of objects generated by SCALOR. 
113
Appendix A. Appendix for Chapter 3 
0 1 2 3 4 5 
Training examples ×105 
0.15 
0.16 
0.17 
0.18 
0.19 
A vg 
.o bj 
ec td 
is t. 
2 objects 
0 1 2 3 4 5 
Training examples ×105 
0.12 
0.13 
0.14 
0.15 
0.16 
0.17 
0.18 
A vg 
.o bj 
ec td 
is t. 
2 objects policy in 1 object environment 
SMORL SMORL with DeepSet SMORL only unconditional head SMORL only goal-conditional heads 
Figure A.4: Ablation study of goal-conditioned attention policy on Visual Rearrange with two objects (left) and out-of-distribution testing on Visual Rearrange with one object (right). We compare variants of the attention policy with only goal-conditional and only goal-unconditional attention heads, plus an alternative approach to aggregate sets of vector representations in the form of DeepSets (Zaheer et al., 2017). Our results demonstrate that both types of attention heads are necessary to achieve the best results. 
0.0 0.2 0.4 0.6 0.8 
Timesteps ×106 
0.08 
0.10 
0.12 
0.14 
0.16 
0.18 
0.20 
2 objects 
SMORL RIG SAC+GT Passive policy 
Figure A.5: Performance of a SMORL agent trained for 106 timesteps on Visual Rearrange with 2 objects. 
114
B 
Appendix for Chapter 4 
B.1 SRICS pseudocode 
Algorithm 6 SRICS: Self-Supervised Relational RL with Independently Controllable Subgoals Require: GNN Dynamical model D, goal-conditional attention policy πθ, goal-conditional SAC trainer, 
number of training episodes K. 1: Train GNN Dynamical model D on sequences uniformly sampled from D using the loss described in 
Eq. 4.5 and estimate the interaction graph G. 2: for n = 1, ..., K episodes 3: Sample goal sgoal and construct subgoal gi using G. ▷ See Eq. 4.6 4: Collect episode data with policy πθ(at | st, gi). 5: Store transitions { 
( st, at, st+1, gi 
) , . . .} into replay buffer R. 
6: Sample transitions from replay buffer ( s, a, s′, gi 
) ∼ R. 
7: Relabel gi goal components to a combination of future states and goal sampling distribution. 8: Compute selectivity reward signal R = rsel,i(s′, s, gi). ▷ See Eq. 4.7 9: Update policy πθ(at | st, gi) using R with SAC trainer. 
115
Appendix B. Appendix for Chapter 4 
B.2 Multi-object Rearrange Environments 
We implement several modifications of the original Multi-object Rearrange environment to study how our agent performs in more challenging settings. First, we implement the Multi-object Relational Rearrange environment by incorporating additional constraints to the Multi-object Rearrange environment. In particular, for the Multi-object Rearrange environment with 4 objects, we add one spring connection and make one object static. The goals are sampled from a random arrangement of the objects, where the constraints above are fulfilled. Next, we implement Multi-object Rearrange with different objects by varying objects’ shapes (cube and cylinder), size, and mass. The manipulation of such different objects is more challenging thus an agent has to learn more complex policy (see Fig. B.1 for the visualization of the environments) 
(a) (b) (c) 
Figure B.1: Visualization of the Multi-object Rearrange environment with a) 4 objects, b) 6 different objects and c) Multi-object Relational Rearrange environment. 
B.3 Additional Experimental Results 
B.3.1 Larger Number of Different Objects 
We have conducted several additional experiments to study how the SRICS method performs in a more challenging environment with a larger number of different objects. In particular, we trained the SRICS agent in the Multi-object Rearrange environment with 6 
116
B.4. Goal-Conditioned Attention Policy 
different objects (see Fig. B.1b). We compared SRICS performance to the SMORL and SAC baselines that are shown to work in more simple Multi-object Rearrange with 4 objects. For these experiments, we do no additional hyperparameter optimization using optimal parameters from Multi-object Rearrange with 4 objects. 
We show the results in Fig. B.2a. The SRICS agent makes progress in this environment while the SMORL agent performs close to a random agent and SAC consistently solves only the easiest "arm" subgoal. This shows that the SRICS agent can learn and efficiently combine many subtasks when the subtasks are different (e.g. manipulation of objects with different shapes). 
B.3.2 State Representation Extended with Object’s Velocity 
In addition to more challenging environments, it is also important to show that the SRICS method is not restricted to coordinate-based object-centric representations. For this, we studied the performance of the SRICS agent when the state representation also includes the object’s velocity. In the modified environment the representation of each object is encoded by the position vector sj,where ∈ R2, the velocity vector sj,vel ∈ R2 and the identifier sj,what ∈ RK . For all the methods, we use positions sj,where to calculate the distance to the goal in the reward signal. The results are presented in Fig. B.2b. The SRICS agent outperforms both baselines and reaches the performance that is comparable to its performance with coordinates-based state representation. 
B.4 Goal-Conditioned Attention Policy 
We train one policy that incorporates all learned skills. For this purpose, we use a goal-conditioned attention policy (Zadaianchuk et al., 2021). This policy needs to vary its behavior based on the goal at hand (e.g. one goal can be reaching a particular position with the robotic arm, whereas another goal can be moving an object to a particular position). To allow this flexibility, we use the attention module with a goal-dependent query Q(sgoal,i) = sgoal,iW q. Each object is allowed to match with the query via an object-dependent key K(st) = stW k and contribute to the attention’s output through the value V (st) = stW v, which is weighted by the similarity between Q(sgoal,i) and K(st). The 
117
Appendix B. Appendix for Chapter 4 
0 1 2 3 4 5 
Training examples ×105 
0.12 
0.14 
0.16 
0.18 
A vg 
.d is 
t. 
Rearrange with 6 different objects 
(a) 
0 1 2 3 4 5 
Training examples ×105 
0.12 
0.14 
0.16 
0.18 
0.20 Coordinates and Velocity State Rearrange 
(b) 
SRICS SMORL SAC+HER HAC 
Figure B.2: Average distance to the goal positions, comparing our method to the SAC and SMORL baselines on a) Rearrange environment with 6 different objects and b) Rearrange environment with 4 objects with coordinates and velocity state representation. 
attention head Ak is computed as 
Ak = softmax ( 
sgoal,iW q(StW k)T√ de 
) StW 
v, 
where St is a packed matrix of all sit’s; the parameters W q, W k, W v constitute learned linear transformations and de is the common dimensionality of the key, value and query. The attention output A is a concatenation of all attention heads A = [A1; . . . ; AK ]. 
Finally, the attention output A is combined with the subgoal sgoal,i and processed by a fully connected neural network f : 
πθ ( {sit}i∈Ot , sgoal,i 
) = f(A, sgoal,i). 
The parameters used for training of the goal-conditioned attention policy are presented in App. B.9.1. 
B.5 Subgoals Selectivity as an Evaluation Metric 
The selectivity (as defined in Eq. 4.7) is a measure of the agent’s selective influence on the components of the environment. In Sec. 4.3.2, we show that it can be used as an additional reward signal to motivate the agent to selectively control different components 
118
B.6. Estimation of the Global Interaction Graph 
of the environment. Additionally, the selectivity can be used as an evaluation metric. This metric features how selective is the influence of an agent on the components of the environment. Here, we compute the selectivity measure for SRICS and SMORL agents that learn to control components of the representation separately from each other. As seen in Fig. B.3, the selectivity measure increases for both agents during the goal-conditioned training. Concurrent with the objective the SRICS agent is trained on, the selectivity measure for the SRICS agent is increasing much faster and with smaller variance compared to the SMORL agent. Therefore, the selectivity is an important objective for autonomous control that can make training more stable and efficient. 
0 1 2 3 4 5 
Training examples ×105 
0.2 
0.4 
0.6 
0.8 
Se le 
ct iv 
ity 
Rearrange with 3 objects 
0 1 2 3 4 5 
Training examples ×105 
0.2 
0.4 
0.6 
0.8 
Rearrange with 4 objects 
SRICS SMORL 
Figure B.3: The selectivity part of the reward signal for both SRICS and SMORL agents averaged over all entities. While the SMORL agent is not optimized for being selective, the selectivity increases over SMORL training because the agent is gaining control over objects. However, for the SRICS agent, the increase in selectivity is much faster as the agent is incentified to be selective. 
B.6 Estimation of the Global Interaction Graph 
To learn sparse interaction weights wij t , we use the sparsity prior pprior (see Eq. 4.5). 
Specifically, the sparsity prior pprior is the Bernoulli distribution 
f(k; p) = 
p if k = 1, 
1 − p if k = 0. 
For all experiments, we use the same prior probability for the relation presence p = 0.05. The interaction weights wij 
t deviate from this prior only when the relation is required for 
119
Appendix B. Appendix for Chapter 4 
the improvement of the dynamical model predictions. As can be seen in Fig. B.4, such approach successfully reconstructs most of the relations for both Multi-Object Rearrange and Multi-Object Relational Rearrange environments. 
Arm 1 2 3 
Recurrent GNN 
Arm 
1 
2 
3 
Arm 1 2 3 
GT 
Arm 
1 
2 
3 0.00 
0.02 
0.04 
0.06 
0.08 
0.10 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Rearrange with 3 objects 
Arm 1 2 3 4 
Recurrent GNN 
Arm 
1 
2 
3 
4 
Arm 1 2 3 4 
GT 
Arm 
1 
2 
3 
4 0.00 
0.02 
0.04 
0.06 
0.08 
0.10 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Rearrange with 4 objects 
Arm 1 2 3 4 
Recurrent GNN 
Arm 
1 
2 
3 
4 
Arm 1 2 3 4 
GT 
Arm 
1 
2 
3 
4 0.00 
0.02 
0.04 
0.06 
0.08 
0.10 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Relational Rearrange with 4 objects 
Figure B.4: Average interaction weights obtained from the GNN dynamical model. 
120
B.6. Estimation of the Global Interaction Graph 
2nd 
obj 
Arm 
3rd 
obj 
Arm 
2nd 
 obj 
4th 
obj 
Arm 
Arm 
Arm 
4th 
obj 
1st obj 
Action 
2nd obj 
3rd 
obj 
Interaction graph Subgoals ordering 
Figure B.5: Ordering of the independently controllable subgoals according to the depth of the corresponding nodes in the interaction graph. When the interaction graph is a DAG, such ordering corresponds to the reversed topological ordering. 
121
Appendix B. Appendix for Chapter 4 
B.7 Evaluation on the Average Objects Distance 
We additionally evaluate our method on the average object distance metric, similarly to the SMORL paper (Zadaianchuk et al., 2021). This metric is calculated as the average of all distances from objects on a table (without arm) to their goal position. Thus, it is biased towards controlling the external objects (which are mostly independent of each other). As can be seen in Fig. B.6, SRICS outperforms SMORL on this metric, whereas SAC performs similar to a passive policy. This result shows the benefit of using the goal-directed selectivity reward signal for the control of external objects. In contrast to the average object distance metric, the average distance metric presented in this paper also reveals the importance of the goal decomposition into a sequence of compatible subgoals. 
0 1 2 3 4 5 
Training examples ×105 
0.10 
0.12 
0.14 
0.16 
0.18 
A vg 
.o bj 
ec td 
is t. 
Rearrange with 3 objects 
0 1 2 3 4 5 
Training examples ×105 
0.12 
0.14 
0.16 
0.18 
0.20 Rearrange with 4 objects 
0 1 2 3 4 5 
Training examples ×105 
0.12 
0.14 
0.16 
0.18 
0.20 Relational Rearrange with 4 objects 
SRICS SMORL SAC+HER HAC 
Figure B.6: Average object distance to the goal positions, comparing SRICS to SMORL and SAC+HER. 
B.8 Ordering of the Subgoals 
As reaching one subgoal can affect the results of reaching other subgoals, it is necessary to order the subgoals such that the resulting sequence of skills is compatible. Intuitively, for 
Decompose to subgoals Order subgoals Solve subgoals sequentially 
Solved compositional goal 
 Agent with compositional skills, 
Compositional  goal 
Figure B.7: SRICS pipeline during evaluation. 
122
B.8. Ordering of the Subgoals 
each compositional goal, we want to first manipulate such objects that require movement of other objects for their manipulation. For example, in case of a robotic arm and objects on the table, we first want to control objects using the robotic arm and then control the arm itself. As the robotic arm has no dependencies in the interaction graph, the corresponding selectivity reward signal should incentify the agent to control the arm while not affecting all other objects, thus making the arm subgoal compatible with objects’ subgoals (if solved perfectly). 
Generally, we order all subgoals by their depth in the interaction graph, executing subgoals with larger depth first (as illustrated in Fig. B.5). The depth of a node is defined as the length of the longest path without loops from the action variable A to the node. The order of the subgoals with the same depth is random. When the learned interaction graph is a directed acyclic graph (DAG), such ordering corresponds to the reversed topological ordering. The nodes in a DAG are topologically ordered if for any edge v → u in graph G, node v comes after node u. Due to such ordering, only the subgoals that correspond to the nodes j ̸∈ Anc(i) are executed before the subgoal i. These subgoals should not be affected when the selectivity part (Eq. 4.7) of the reward signal is maximized. Thus, such ordering of the subgoals guarantees the compatibility of the subgoals sequence when each of the subgoals is solved with a maximal reward signal. 
123
Appendix B. Appendix for Chapter 4 
B.9 Implementation Details 
B.9.1 SRICS 
We refer to Table B.1 and Table B.2 for the hyperparameters of SRICS for all environments. We use the same number of subgoal solving attempts as in SMORL. During the evaluation, the number of attempts is equal to 7 for environments with 3 objects and 9 for environments with 4 objects. As the number of attempts k is larger than the number of entities n, we order only the last n subgoals. 
B.9.2 Prior Work 
For both SMORL and SAC, we use previously optimized settings for Multi-Object Rearrange with 3 and 4 objects from Zadaianchuk et al. (2021). In addition, we make a hyperparameter search over more than 100 runs for finding the best HAC hyperparameters. Specifically, we evaluate the performance of HAC while varying the number of steps for each subgoal, number of levels, and action noise. For the Multi-Object Relational Rearrange environment with 4 objects, we use the same parameters as in the Multi-Object Rearrange environment with 4 objects for all algorithms. 
124
B.9. Implementation Details 
Hyperparameter Value Selectivity parameter α 0.25 
Optimizer Adam with default settings RL Batch Size 2048 Reward Scaling 1 
Automatic SAC entropy tuning yes SAC Soft Update Rate 0.05 
# Training Batches per Time Step 1 Hidden Activation ReLU 
Network Initialization Xavier uniform Separate Attention for Policy & Q-Function yes 
Replay Buffer Size 250000 Relabeling Fractions Rollout/Future/Sampled Goals 0.1 / 0.4 / 0.5 
Number of Initial Random Samples 10000 Number of Heads 5 Discount Factor 0.95 Learning Rate 0.001 
Policy Hidden Sizes [128, 128] Q-Function Hidden Sizes [128, 128, 128] 
Training Path Length 20 Table B.1: General hyperparameters used by SRICS for all environments. 
Hyperparameter Value Sparsity prior p 0.05 
Threshold θ 0.06 Number of episodes 1000 
Episode length 50 Sequence size during RNN modeling T 20 
Number of updates 100000 Learning Rate 0.0005 
Batch Size 100 Table B.2: Hyperparameters for the interaction graph estimation for all environments. 
125
C 
Appendix for Chapter 5 
C.1 Sensitivity of the COMUS parameters 
First, we compare COMUS performance with different clustering methods. In Figure C.1a we show that SC provides the best supervision signal for COMUS. Additionally, we investigate the sensitivity of COMUS to the choice of % of filtered examples (see Fig. C.1b), showing that [20%-40%] of filtered examples leads to comparably good performance. We observe that larger % of filtered examples leads to drop in performance, potentially due to small size of the obtained dataset for training the segmentation network. 
Next, we look at the sensitivity of COMUS to the choice of SC parameters. In Table C.1 we show that SC is not sensitive to the choice of the number of neighbors and n_init parameters. SC is sensitive to the number of eigenvectors, however, the default value (equal to the number of clusters) shows very good performance. Similar to other works (e.g. (Van Gansbeke et al., 2021; Melas-Kyriazi et al., 2022)), we used the same number of clusters as annotated categories (needed for quantitative evaluation). 
Finally, we also study the effect of additional iterations of self-training iterations on trainaug part of PASCAL VOC dataset. We find that trained for two or three iterations COMUS performs similarly, while for even more self-training iterations we observe slow decrease of the performance (Fig. C.2). While we were performing additional self-training iterations on the same dataset, in the future work, it is interesting to study how our method 
127
Appendix C. Appendix for Chapter 5 
Figure C.1: (a) COMUS (Iteration 1) performance with different clustering methods. (b) Effect of "% filtered" on final performance of COMUS. The results are mean ± standard dev. over 5 runs. 
SC kmeans HACkmedoids 
Clustering 
40 
45 
50 
m Io 
U 
0 10 20 30 40 50 
% filtered 
48 
49 
50 
51 
52 
performs in the open-ended regime where new data is available for each iteration. 
Figure C.2: Number of self-training iterations in COMUS training. The results are mean ± standard dev. over 5 runs. 
0 2 4 6 
Itteration of self-training 
44 
46 
48 
50 
m Io 
U 
Table C.1: Spectral Clustering parameters study, performance after the first iteration. 
n_neighbors n_components n_init 
Range [20 − 50] [10 − 40] [10 − 60] 
mIoU 46.0 ± 1.3 38.8 ± 6.2 47.6 ± 1.0 
C.2 Self-supervised features quality 
As was showed in the original paper (Caron et al., 2021), DINO features are demonstrating excellent performance for k-NN classification (78.3% top-1 ImageNet accuracy), which reveals the quality of the feature space for clustering. In contrast, other self-supervised methods require fine-tuning of last layer (Caron et al., 2020; He et al., 2020) or several last layers (He et al., 2022). We further confirmed (see Table C.2) that DINO performs significantly better than SwAV (Caron et al., 2020) and SCAN method (Van Gansbeke 
128
C.3. Saliency masks quality 
Table C.2: Clustering of random subsets of ImageNet classes. 
Top-1 Accuracy, % 
50 Classes 100 Classes 200 Classes 
SCAN 76.8 68.9 58.1 SwAV 81.6 ± 0.5 71.5 ± 0.4 59.2 ± 0.8 Supervised 91.2 ± 0.9 87.5 ± 0.3 82.2 ± 0.4 
DINO 91.3 ± 0.5 88.0 ± 0.2 83.1 ± 0.4 
et al., 2020) (based on MoCo (He et al., 2020) features) for image clustering. For this, similar to SCAN methods (Van Gansbeke et al., 2020), we picked random subsets of ImageNet categories, consisting of 50, 100 and 200 classes. For this experiment, we were using validation images of ImageNet (50 images per category). The results show that DINO features could be used for image clustering with performance comparable with supervised ResNet-50 features. 
C.3 Saliency masks quality 
In this section, we study how COMUS works with different self-supervised and supervised saliency detectors. Overall, we observe that improving original object proposal masks is important for both category discovery and further iterative self-training. Also, we note that the proposed iterative self-training from filtered pseudo masks is effective for all of the studied choices of saliency detectors. 
C.3.1 Choice of unsupervised saliency masks detector 
First, we compare COMUS combined with self-supervised BasNet saliency detector (Qin et al., 2019) (i.e., BasNet pretrained with DeepUSPS masks on MSRA-B dataset) with COMUS that is using recently proposed Spectral Decomposition saliency masks from DeepSpectral (Melas-Kyriazi et al., 2022). While original predictions from Spectral Decomposition are performing worse than unsupervised semantic segmentation proposed in DeepSpectral (see the first row of the Table C.3), using them in COMUS as objects proposal performs better than DeepSpectral showing the importance of other COMUS 
129
Appendix C. Appendix for Chapter 5 
components, such as the initial discovery of object categories from object proposals, not from clustered segments (as those are not always object-centric and could cover only parts of objects), filtering of the most uncertain pseudo-masks and several iterations of self-training on previously unseen data. This way, we are able to outperform DeepSpectral semantic segmentation on more than 5 mIoU points, while using only DINO features for both object proposal masks and object representation extraction. 
Next, we additionally show how COMUS performs if we use original DeepUSPS masks (Nguyen et al., 2019) as object proposals. As we discussed in the main text, DeepUSPS seems to be less robust than self-supervised BasNet on more complex OOD images from the PASCAL VOC dataset, that was not used in the training (see the first row of the Table C.3). Additional self-training iterations are improving the quality of the original object proposals similarly, showing that COMUS can operate with originally lower quality mask proposals in case of successful object categories discovery. 
While the original DeepUSPS initialize its backbone weights from supervised pretrain-ing (Nguyen et al., 2019), similar to other areas, it was recently shown that this is not necessary for DeepUSPS good performance (Ryali et al., 2021). They show that DeepUSPS2 (Ryali et al., 2021) model that does not use any annotations during backbone pretraining still performs comparable to or better than the original DeepUSPS. Thus, similar to the original DeepUSPS saliency masks could be discovered from architecture where no labels were used. As DeepUSPS2 implementation is not publically available and for better comparison with previous methods in our work, we were using self-supervised BasNet from MaskContrast (Van Gansbeke et al., 2021). 
Table C.3: Choice of the unsupervised salient object detector. We compared COMUS performance with three different unsupervised saliency masks detectors: self-supervised BasNet model (Qin et al., 2019), original DeepUSPS (Nguyen et al., 2019) and spectral decomposition saliency masks from DeepSpectral (Melas-Kyriazi et al., 2022). All the models are evaluated with by IoU after Hungarian matching on the PASCAL 2012 val set. 
Self-supervised BasNet Spectral Decomposition DeepUSPS 
COMUS (Iteration 1) 47.6 43.8 45.5 
COMUS (Iteration 2) 50.0 45.9 47.5 
130
C.4. Extended Limitations and Future Work 
C.3.2 Supervised saliency masks as localization prior 
In addition to using fully self-supervised saliency masks as localization prior, we also consider using BasNet saliency detector trained with supervision on MSRA-B dataset as localization prior. Supervised training of saliency masks leads to even better masks, but drops the property of the method being fully unsupervised. Table C.4 shows that supervised saliency masks also improve the final results, as to be expected. 
Table C.4: Effect of object proposals from supervised saliency detector. 
Unsupervised Saliency Supervised Saliency 
MaskContrast 35.1 38.9 
COMUS (Iteration 1) 47.6 50.4 
COMUS (Iteration 2) 50.0 52.3 
C.4 Extended Limitations and Future Work 
C.4.1 Number of semantic categories bias 
As we are starting our iterative self-training from pseudo-masks restricted to one foreground semantic category per image, it is natural to study how well COMUS can work on more complex images where it is more than one semantic category per image by using discovered categories as an additional signal. Thus, we study COMUS performance in comparison with DeepSpectral (Melas-Kyriazi et al., 2022) on two subsets of PASCAL VOC val: the first one is the subset where it is only one foreground semantic category (subset 1) and the second one is the subset of images with two or more foreground semantic categories (subset 2). We compare several iterations of self-training with DeepSpectral performance using two metrics: first is the standard mIoU showing the overall quality of the predictions. In addition, we compared the precision of recognizing each group. For example for the first subset, it is equal to the percentage of predictions that contain only one foreground semantic category prediction). 
For each method, as expected, we observe that the quality of the predictions on the subset 2 is worse than on the subset 1. Iterations of self-training are improving COMUS 
131
Appendix C. Appendix for Chapter 5 
performance, and allowing reaching better quality (measured by mIoU) on more complex images from subset 2 than overall DeepSpectral predictions. While improving overall prediction quality, the second iteration of COMUS shows bias towards predicting one foreground semantic category per image. This is potentially due to bias in the PASCAL VOC trainaug dataset itself. In contrast, DeepSpectral tends to have the opposite bias toward predicting more than one category per image (i.e., it has lower precision for the first task and higher precision for the second task). This could be due to the image features clustering task that is used by DeepSpectral for segment extraction. Interestingly none of the methods predicts well the number of foreground masks in both subsets. Thus determining the right number of semantic categories for each image is still a challenging problem for unsupervised semantic segmentation and an interesting direction for future work. 
Table C.5: Number of semantic categories bias. Performance of studied methods on two subsets of PASCALVOC val dataset. 
1 semantic category > 1 semantic category overall 
mIoU precision, % mIoU precision, % mIoU precision, % 
DeepSpectral 39.9 50.9 34.5 65.7 37.1 56.2 
COMUS (Itteration 1) 52.0 50.5 39.9 61.8 47.6 54.6 COMUS (Itteration 2) 55.2 67.7 41.2 46.5 50.0 60.1 
C.4.2 Failure Modes Analysis 
We present illustration of several failure cases in Figure C.6. We observe that COMUS still failures to discover some categories, such as table category that is treated as a background by saliency method. Also, when an object fills all the background our method fails to fully recover from initial saliency mask assumption, that objects appears only in the foreground. Finally, as our method has only one category for the background, extending COMUS to additionally split backgrounds (e.g., COCO-Stuff semantic segmentation masks) is an interesting direction for future work. 
132
C.5. More detailed quantitative and qualitative results 
C.5 More detailed quantitative and qualitative results 
C.5.1 PASCAL VOC 
In this subsection, we present additional analysis of COMUS performance on PASCAL VOC dataset. First, in Table C.6, we show COMUS performance for each PASCAL VOC category. COMUS performs better than MaskContrast and DeepSpectral on most of the categories. In addition to fully unsupervised semantic segmentation methods, we compare COMUS with recently proposed, weakly-supervised GroupViT method (Xu et al., 2022). GroupViT uses text descriptions as a weak supervision signal to group image regions into progressively larger arbitrary-shaped segments. While it does not require any pixel-level annotations, GroupViT still relies on large annotated datasets containing millions of image-text pairs. On average COMUS performance is worse than GroupViT performance, COMUS performs better on 9 from 21 categories while using no text annotations. In addition, in Figure C.7, we visualize COMUS predictions on random images from PASCAL VOC dataset for two stages of COMUS as well as MaskContrast predictions. Finally, for exploring Interactive Demo that visualizes clustering of the whole PASCAL VOC val set, visit COMUS project website: https://sites.google.com/view/comuspaper/home. 
Table C.6: More detailed comparison to prior art and iterative improvement via self-training (evaluated by IoU after Hungarian matching) on the PASCAL 2012 val set. Our method results are averaged over 5 runs. 
Method mIoU 
GroupViT (text supervision) (Xu et al., 2022) 80.6 38.1 31.4 51.6 32.7 63.5 78.8 65.1 79.2 18.8 73.4 31.6 76.4 59.4 55.3 44.0 40.9 66.6 31.5 49.5 29.7 52.3 
MaskContrast (Van Gansbeke et al., 2021) 84.4 39.1 20.0 59.5 34.2 38.1 57.8 60.7 46.9 0.29 0.42 3.51 28.6 39.6 54.7 23.2 0.00 40.0 14.9 54.0 37.7 35.1 
DeepSpectral (Melas-Kyriazi et al., 2022) 82.1 46.1 0.0 72.6 31.9 9.1 77.3 66.1 77.5 0.1 43.4 25.9 40.6 62.6 36.9 28.0 2.5 1.1 10.8 63.9 0.0 37.1 
Pseudo-masks (Iteration 0) 82.8 48.1 19.6 59.3 49.7 55.6 63.8 52.7 53.2 0.1 58.3 0.0 37.2 54.7 50.9 36.2 26.8 66.8 17.6 52.3 33.9 43.8 ± 0.1 
COMUS (Iteration 1) 85.9 51.0 21.4 49.4 52.5 61.0 71.0 61.6 65.4 0.0 47.1 16.7 59.9 48.9 56.9 49.6 33.9 58.9 16.1 56.5 36.4 47.6 ± 0.4 
COMUS 86.3 54.8 21.9 53.5 55.3 64.5 75.2 61.8 68.6 0.0 49.0 18.2 64.1 52.2 58.3 52.4 36.8 57.7 16.8 63.5 38.7 50.0 ± 0.4 
C.5.2 COCO 
In this subsection, we present additional analysis of COMUS performance on COCO dataset. Figure C.4 shows the performance of COMUS on COCO for each of 80 COCO categories. We note that COMUS achieves better performance for animal and vehicle categories, as well as salient object categories such as stop sign and traffic light categories. We 
133
Appendix C. Appendix for Chapter 5 
also observe that most of the undiscovered categories have small relative object’s size (e.g., spoon, remote and mouse). For additional analysis of the connection between relative object’s size and COMUS performance, see Figure C.3. In addition, in Figure C.8, we visualize COMUS predictions on random images from PASCAL VOC dataset for two stages of COMUS as well as MaskContrast predictions. 
Figure C.3: Connection between mean relative size of objects and IoU for each COCO category. The Spearman’s rank correlation between relative size and IoU is equal to 0.43. 
C.6 Implementation details 
C.6.1 Spectral Clustering 
We use spectral clustering implementation from sklearn1. In particular, an affinity matrix is obtained from the nearest neighbors graph. Number of eigenvectors and number of clusters is the same as number of GT categories. We refer to Table C.7 for the parameters of spectral clustering. 
C.6.2 Self-Training 
During self-training, DeepLabv3 (Chen et al., 2018a) with standard cross-entropy loss is chosen to make training set up as comparable to previous research (e.g. to MaskCon-trast (Van Gansbeke et al., 2021)) as possible. We use CropResize and HorizontalFlip as data augmentation methods. For PASCAL VOC, we perform two iterations of self-training on train and trainaug sets. For COCO dataset, we perform one iteration of self-training on train set. See Table C.8 for the parameters of the self-training. 
1https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html 
134
C.6. Implementation details 
Table C.7: Spectral clustering parameters for COMUS on PASCAL VOC and MS COCO datasets. 
Hyper-parameter PASCAL VOC MS COCO 
Number of clusters 20 80 Number of components 20 80 
Affinity nearest neightbors nearest neightbors Number of neighbors 30 30 
C.6.3 Computational requirements 
Similar to other unsupervised segmentation methods (Van Gansbeke et al., 2021; Melas-Kyriazi et al., 2022; Hamilton et al., 2022), the most expensive part of our pipeline, is the training of self-supervised representation learning method. In particular, DINO with Vision Transformers training takes 3 days on two 8-GPU servers and is comparable with other self-supervised representation learning methods. However, learned features could be transferred without further fine-tuning on new natural data images, such as scenes from PASCAL VOC and MS COCO. 
The other parts of our method are much faster to train: DeepUSPS could be trained 30 hours of computation time on old four Geforce Titan X (Nguyen et al., 2019), while BasNet could be trained with four GTX 1080ti GPU (with 11GB memory) in around 30 hours (Qin et al., 2019), while the inference for 256×256 image only takes 0.040s (25 fps). For more details, we refer the reader to the main papers for these methods. 
Finally, the main parts of our method that do require training on new data are object proposals clustering and self-training iterations. Spectral Clustering complexity depends on the sample size. For the full COCO train dataset Spectral Clustering with amg solver took 20 minutes on 96 core node. Thus, for large datasets, it is recommendable to use its subset for the initial discovery of object categories and then use self-training on the full dataset. For semantic segmentation self-training, we used the standard in supervised semantic segmentation set up for training DeepLabv3 architecture. While all the models could be trained on a single GPU, for convenience we perform all the experiments on one node with 4 NVIDIA T4 GPUs, where 2 iterations of self-training took around one hour. 
135
Appendix C. Appendix for Chapter 5 
Table C.8: Self-training parameters for COMUS on PASCAL VOC and MS COCO datasets. 
Hyper-parameter PASCAL VOC MS COCO 
Optimizer Adam with default settings Adam with default settings Learning rate 0.00006 0.00006 
Batch size 56 56 Input size 512 256 
Crop scales [0.5, 2] [0.2, 1.0] Number of iterations 2 1 
Number of epochs. Iteration 1 10 1 Number of epochs. Iteration 2 5 -
C.7 Datasets (directly or indirectly) used in the paper 
PASCAL VOC: The PASCAL Visual Object Classes (VOC) project (Everingham et al., 2015) provides different datasets / challenges for the years from 2005 to 2012. We apply our proposed method to the datasets from 2012 and 2007, which come with semantic segmentation masks. All datasets and detailed descriptions are available on the PASCAL VOC homepage (http://host.robots.ox.ac.uk/pascal/VOC/index.html). 
MS COCO: We also apply our method to the Microsoft (MS) COCO dataset (Lin et al., 2014). The dataset and informations are available on https://cocodataset.org/#home. 
ImageNet: For feature extraction, we use vision transformers pretrained with the self-supervised (no labels!) DINO method (Caron et al., 2021) on ImageNet (Deng et al., 2009). The pretrained checkpoint can be found on https://github.com/facebookresearch/di no. Informations about ImageNet are provided on https://image-net.org/. 
MSRA-B: For computing saliency mask, we use BasNet (Qin et al., 2019) pretrained on pseudo-labels generated with the unsupervised DeepUSPS (Nguyen et al., 2019) outputs on the MSRA-B dataset (Wang et al., 2017). The pretrained checkpoint can be found on https://github.com/wvangansbeke/Unsupervised-Semantic-Segmentation/ tree/main/saliency. The dataset and informations about it are available on https: //mmcheng.net/msra10k/. 
136
C.7. Datasets (directly or indirectly) used in the paper 
Figure C.4: IoU for COCO categories after Hungarian matching of the cluster IDs to ground-truth categories. 
137
Appendix C. Appendix for Chapter 5 
Figure C.5: Predictions of the COMUS method trained on PASCAL VOC on COCO val set. We notice that the predictions from models trained on PASCAL VOC transfer reasonably well to COCO. 
Figure C.6: Several failure samples of the COMUS method on PASCAL VOC val set. The failures show the limitation and biases of our method, such as bias towards salient objects and misclassifications in multi-object images. 
138
C.7. Datasets (directly or indirectly) used in the paper 
Image Label MaskContrast COMUS  (Iteration 1) 
COMUS 
Figure C.7: COMUS and MaskContrast pre-dictions on random images from PASCAL VOC val set. 
Image Label COMUS 
Figure C.8: COMUS pre-dictions on random images from COCO val set. 
139
D 
Appendix for Chapter 6 
D.1 Comparison with Additional Baselines 
D.1.1 Comparison with Image-Based Object-Centric Methods 
In this section, we evaluate how effective our model is for unsupervised image segmentation from videos. In addition to reporting results for the video-based object-centric methods SAVi and STEVE, we compare with several recent image-based object-centric learning methods. SLATE (Singh et al., 2022a) is an image-based object-centric model that trains a discrete VAE (Rolfe, 2017) as a dense feature extractor and uses a Transformer decoder conditioned on slots to reconstruct discrete representations of VAE features. LSD (Jiang et al., 2023) replaces the Transformer decoder with a latent diffusion model conditioned on the object slots. Next, DINOSAUR (Seitzer et al., 2023) incorporates dense DINO features as targets and reconstructs the features itself. We report the Image FG-ARI and Image mBO metrics. They measure how well the predicted segmentation matches the ground-truth segmentation of a given single image (frame), thus consistency over the video is not taken into account. 
The results for MOVi datasets are presented in Table D.1.1. VideoSAUR surpasses both pre-vious image- and video-based methods, showing the benefits of using motion information in combination with semantically coherent self-supervised features. Interestingly, VideoSAUR 
141
Appendix D. Appendix for Chapter 6 
performs well on both Image FG-ARI and Image mBO metrics, whereas DINOSAUR and LSD seem to improve either in quality of split (measured in Image FG-ARI) or in the sharpness of masks (measured in Image mBO) at the cost of performing worse on the second metric. We also note that LSD results are from larger resolution of MOVi images (256 × 256). We expect that our method can additionally improve if we also use larger resolution videos; however, to be comparable with other baselines, we use 128 × 128 resolution in this work. 
0 10 20 30 40 
Im ag 
e FG 
-A R 
I 
SAVi STEVE DINOSAUR VideoSAUR 
Figure D.1.1: Image-based comparison on YouTube-VIS (mean ± standard dev., 3 seeds). 
In addition, we also compare VideoSAUR with DINOSAUR and other video-based baselines on the more challenging YouTube-VIS dataset (see Fig. D.1.1). VideoSAUR outperforms DINOSAUR (+4 FG-ARI) and also surpasses video-based STEVE and SAVi methods. This underscores the bene-fit of our temporal similarity loss over mere feature reconstruction for challenging real-world datasets. 
Table D.1.1: Comparison with state-of-the-art methods on the MOVi-C, MOVi-E image datasets. Both metrics are computed for individual frames. The results for SLATE and DINOSAUR are from Seitzer et al. (2023), while LSD results are from Jiang et al. (2023). We report mean ± standard dev. over 5 runs for our model. 
MOVi-C MOVi-E 
Image FG-ARI Image mBO Image FG-ARI Image mBO 
Block Pattern 42.7 19.5 41.9 20.4 SAVi 41.8 25.9 50.3 20.3 STEVE 51.9 41.6 59.5 34.4 SLATE 43.6 26.5 44.4 23.6 LSD 50.5 46.3 53.4 39.6 SlotDiffusion – – 60.0 30.2 DINOSAUR 68.6 39.1 65.1 35.5 VideoSAUR 75.5 ± 0.9 46.0 ± 0.6 78.4 ± 0.7 41.2 ± 0.4 
142
D.1. Comparison with Additional Baselines 
D.1.2 Comparison with Concurrent Work on Real-World Videos 
In concurrent work, two more slot attention-based methods were proposed that learn object-centric representations on real-world videos: SMTC (Qian et al., 2023) and SOLV (Aydemir et al., 2023). SMTC learns to extracts objects from videos by enforcing semantic and instance consistency over time using a student-teacher approach. SOLV extracts per-frame slots using invariant slot attention (Biza et al., 2023), applies a temporal consistency module and merges slots using agglomerative clustering; the model is trained using DINOSAUR-style feature reconstruction on masked out intermediate frames. In this section, we compare to them using the respective evaluation protocols in their papers. 
First, we compare to SMTC in Table D.1.2 on the DAVIS-2017-Unsupervised dataset (Pont-Tuset et al., 2017b). Specifically, we assess our method’s transfer performance when trained on YT-VIS 201, and follow the evaluation procedure outlined in (Pont-Tuset et al., 2017b) for matching ground truth masks to predictions using mean J & F . We report the Jaccard index J (equivalent to IoU), the boundary F-score F and their average as J & F . While the contours of VideoSAUR’s segmentation masks (as measured by F) are not as accurate due to processing images and predicting masks at a lower patch resolution (37 × 37 for VideoSAUR trained with DINOv2 B14 features on original DINOv2 resolution), the Jaccard index J is comparable to SMTC. 
Second, we compare to SOLV in Table D.1.3 on the YT-VIS 2019 dataset. We also list the performance of OCLR (Xie et al., 2022), which uses synthetic data with ground-truth optical flow. As SOLV, we report the mIoU metric matched over the entire video. The results for VideoSAUR are obtained using random 200 videos from the YT-VIS 2019 train split 1. Our results surpass OCLR, showing VideoSAUR ’s effectiveness in extracting motion information directly from video data using dense self-supervised features. Additionally, our performance matches that of SOLV without using agglomerative clustering, while SOLV with slot merging outperforms VideoSAUR (+5 mIoU). This highlights the importance of correctly determining the number of slots. While the main concern in this paper is to integrate motion information from video, we see determining the number of slots as an important orthogonal direction. Thus, combining our method a solution such as the one from Aydemir et al. (2023) is an interesting direction for future work. 
1We use part of the train split, as validation labels are not released. Exact indexes are available at validation split of the Tensorflow version of the YT-VIS 2019 dataset: https://www.tensorflow.org 
/datasets/catalog/youtube_vis#youtube_visonly_frames_with_labels_train_split 
143
Appendix D. Appendix for Chapter 6 
Table D.1.2: Comparison of VideoSAUR with DINOv2 ViT B/14 features to SMTC (Qian et al., 2023) on the DAVIS-2017-Unsupervised validation set. The re-sults for SMTC are from Qian et al. (2023). 
Method J F J & F 
SMTC 36.4 44.6 40.5 VideoSAUR 36.8 21.1 29.0 
Table D.1.3: Comparison of VideoSAUR with DINOv2 ViT B/14 features to OCLR (Xie et al., 2022) and SOLV (Ay-demir et al., 2023) on YT-VIS 2019. The results for OCLR and SOLV are from Ay-demir et al. (2023). 
Method mIoU 
OCLR 32.5 SOLV (w/o slot merging) 39.9 SOLV (w/ slot merging) 45.3 VideoSAUR 40.3 
D.2 Additional Experiments 
D.2.1 Long-Term Video Consistency 
Beyond the initial examination of how our VideoSAUR performs on the relatively brief 6-frame video segments from YouTube-VIS 2021, we extend our evaluation to also assess its effectiveness on more substantial, longer video segments. In Table D.2.1, we show the performance for 12-frame and full YT-VIS video segments (see Fig. D.2.1 for the distribution of video lengths). Although the performance of VideoSAUR on extended video segments predictably decreases in terms of FG-ARI (as we do not have any memory module to handle object occlusions and reidentification (Traub et al., 2023b)), the observed difference between VideoSAUR and the baseline models is significant. This suggests that VideoSAUR maintains its efficacy in tracking the primary objects in videos across longer time intervals. 
Additionally, we investigate if VideoSAUR benefits from using DINOv2 features (Oquab et al., 2023) that are obtained by training DINO on the larger dataset and fine-tuning the representation on larger resolution (518 × 518). We show that VideoSAUR performance benefits from using such features as a backbone, especially in terms of mask quality (+6 mBO points). Using those features with the original resolution VideoSAUR reaching 29.7 mBO on full-length YT-VIS 2021 videos. In addition to this quantitative evaluation, we visualize VideoSAUR predictions on long YT-VIS videos (longer than 30-frames) in 
144
D.2. Additional Experiments 
Table D.2.1: Performance of VideoSAUR on the YT-VIS 2021 dataset, varying the length of the video segment (mean ± standard dev., 5 seeds for VideoSAUR with DINO features and STEVE. VideoSAUR with DINOv2 features are one seed only due to computational limitations). 
6 frames 12 frames Full Videos 
FG-ARI mBO FG-ARI mBO FG-ARI mBO 
Block Pattern 24.0 14.9 20.3 14.2 15.1 13.1 STEVE 20.0 ± 1.5 20.9 ± 0.5 18.0 ± 1.4 21.5 ± 0.5 15.0 ± 0.7 19.1 ± 0.4 VideoSAUR w\DINO B/16 39.5 ± 0.6 29.1 ± 0.4 35.8 ± 0.3 29.4 ± 0.3 28.9 ± 0.4 26.3 ± 0.2 VideoSAUR w\DINOv2 B/14 39.7 35.6 38.7 34.5 31.2 29.7 
10 20 30 40 50 60 Video length, frames 
0 5 
10 15 20 25 30 35 
N um 
be r o 
f v id 
eo s 
Figure D.2.1: Histogram of video lengths on the YT-VIS 2021 validation dataset. 
Figure D.5.5 and Figure D.5.6. 
D.2.2 Optical Flow as Self-Supervised Target 
The choice of the self-supervised target plays an important role in creating suitable inductive biases for object discovery and scene decomposition. As such, understanding the properties of the prediction target leading to an effective scene decomposition is crucial. The temporal feature similarity prediction proposed in this work combines two different inductive biases: high-level semantic information and motion information. To elucidate the significance of both types of bias for scene decomposition, we assess the performance of VideoSAUR with prediction targets that consist only of one of those biases. 
In Table 6.2 in the main text, we compare predicting temporal similarities with predicting 
145
Appendix D. Appendix for Chapter 6 
Table D.2.2: Comparing VideoSAUR predicting temporal similarities to predicting ground truth optical flow on the MOVi-C and MOVi-E datasets. We report Video FG-ARI of a version of VideoSAUR with optical flow (both backward and forward) as well as the original VideoSAUR with temporal features similarity. 
VideoSAUR MOVi-C MOVi-E 
w/ GT Optical Flow (backward) 48.1 28.9 w/ GT Optical Flow (forward) 48.9 30.1 w/ Temporal Similarities 60.7 73.9 
self-supervised features of the current frame. Such features only contain semantic infor-mation, but no information about motion. Depending on the dataset, including temporal information brings a small (YT-VIS) or large benefit (MOVi-C). 
Subsequently, we study if motion cues alone (without the semantic information) are enough for successful scene decomposition. In particular, we compare self-supervised temporal similarity targets with (ground truth) optical flow targets (only motion information) on the MOVi-C and MOVi-E datasets. To this end, we train VideoSAUR by predicting optical flow targets, using a spatial broadcast decoder similar to SAVi (Kipf et al., 2022) instead of the mixer decoder. All other components of VideoSAUR stay unchanged. The optical flow map is predicted at full image resolution (128 × 128). 
The results are presented in Table D.2.2. We train VideoSAUR with GT optical flow for the best potential performance from optical flow alone. Yet, even on the MOVi-C datasets favoring optical flow (no camera motion, no static objects), VideoSAUR with temporal feature similarities significantly outperforme optical flow (+10 FG-ARI). This disparity is even greater on the MOVi-E dataset, highlighting VideoSAUR’s resilience to camera movements and static objects. Together, these results demonstrate that our temporal feature similarity targets, despite not requiring signals such as optical flow (which would need estimation in real-world scenarios like the YouTube-VIS dataset), excel over mere optical flow targets. We attribute this to the enriched semantic bias inherent to the self-supervised feature similarities. 
146
D.2. Additional Experiments 
Table D.2.3: Extended ablation of VideoSAUR components on MOVi-E. We compare VideoSAUR model with different choices of the decoder (Mixer vs MLP used by DINOSAUR) and loss types (temporal similarity loss vs feature reconstruction). 
Decoder Loss Type FG-ARI mBO 
MLP Feature Reconstruction 68.6 27.6 MLP Temp. Feat. Sim. Prediction 74.5 28.8 Mixer Feature Reconstruction 62.3 20.6 Mixer Temp. Feat. Sim. Prediction 74.1 34.1 
D.2.3 Comprehensive Ablation Study on the MOVi-E Dataset 
In this section, we present the results of a comprehensive ablation study conducted on the MOVi-E dataset. The purpose of this study is to investigate the impact of two key factors: decoder choice (MLP vs. Mixer) and loss function selection. Our goal is to gain a deeper understanding of how these choices affect the performance of our method. The results are summarized in Table D.2.3. 
The similarity loss is beneficial for both decoders, pushing the FG-ARI to approximately 74, as compared to 69 when using the feature reconstruction loss. Notably, the Mixer decoder significantly enhances the clarity of the object mask, with an improvement of +5 mBO. When combined, the similarity loss and Mixer consistently outshine the MLP decoder equipped with the feature reconstruction loss. These insights provide valuable auxiliary information to our main paper ablations (see Table 6.2), painting a more detailed picture of VideoSAUR’s components and their respective performances. 
D.2.4 Stability of Mixer Decoder 
As mentioned in Sec. 6.3.3 of the main text, we found that the mixer decoder sometimes exhibits training instabilities. For instance, Table D.2.4 shows that there is high variance over random seeds when training purely with feature reconstruction, i.e. some training runs fail to discover an object grouping. These instabilities manifest in slot masks that follow a Voronoi-like decomposition of the image. When adding the temporal similarity loss, the instabilities disappear. 
147
Appendix D. Appendix for Chapter 6 
Table D.2.4: Mixer decoder with smaller DINO features (S/16) on YT-VIS 2021 (mean ± standard dev., 3 seeds). 
Loss type Metric 
Feat. Rec. Temp. Sim. FG-ARI mBO 
✓ 14.9 ± 12.0 12.9 ± 5.9 ✓ ✓ 37.0 ± 3.5 29.1 ± 0.6 
Table D.2.5: Loss ablation study on COCO dataset. Metrics are image-based ARI and mBO (mean, 3 seeds). 
Loss type Metric 
Feat. Rec. Self-Sim. FG-ARI mBOi 
✓ 34.8 23.9 ✓ 28.5 25.6 
✓ ✓ 38.0 25.9 
We hypothesize this is because the mixer decoder has increased flexibility in how to model the image with slots (compared to the conventional mixture-based decoder), and thus more failure modes (non-object groupings) the model can “fall into” during training. Increasing the difficulty of the task by adding the temporal similarity loss makes these failure modes less viable: by putting more pressure on the slot bottleneck to encode information, object-based slot groupings are more efficient representations than alternative groupings. 
However, we found that the mixer decoder with feature reconstruction does not show instabilities in all settings. For example, training with DINO ViT Base/8 features on MOVi-C or DINO Base/16 features on YouTube-VIS 2021 (Table 6.2 in the main text) is relatively stable. We attribute this to the increased task difficulty when predicting ViT “Base” features instead of ViT “Small” features (as in Table D.2.4). Once more (Kipf et al., 2022; Singh et al., 2022a; Yang and Yang, 2022; Elsayed et al., 2022; Seitzer et al., 2023), these findings demonstrate the central lesson of unsupervised object discovery: to be successful, the model needs to have sufficient inductive biases, whether they stem from the dataset, the decoder, the grouping module, or the training task. 
148
D.2. Additional Experiments 
D.2.5 Image-Based Feature Similarity on COCO 
In this section, we show that our proposed similarity loss can also be useful for image-based datasets, and thus is not restricted to just the video setting. Note that by setting the time-shift k to 0, the temporal similarities turn into a self-similarities, that is, the target similarities are computed by comparing features from the same image. The resulting similarity maps highlight semantically and spatially related patches and thus could be useful targets to discover objects. 
To test this, we train the DINOSAUR method with ViT S/16 (Seitzer et al., 2023) with the self-similarity loss on the real-world COCO dataset (see Table D.2.5). Similar to the results from the time-shift analysis (see k = 0 in Fig. 6.6b), we find that using the self-similarity loss alone does not seem to carry enough signal to train the model and leads to degraded performance. However, combining the self-similarity loss with feature reconstruction shows significant improvement over using only feature reconstruction. Even though the targets contain the same information overall, different transformations of the original targets (e.g. their relative similarity) create different biases — a combination of these different views into the targets appears to be beneficial for object discovery. 
D.2.6 Sensitivity to Number of Slots During Evaluation 
One of the noteworthy properties of slot attention-based models with randomly sampled initialization2 is that the number of slots can be adjusted during inference. As we demon-strate in Fig. 6.6b, this is helpful for successfully transferring to datasets that have a different average number of objects per video. For this purpose, it is important to examine how stable the model’s performance is if it is used with a different number of slots than during training. Thus, we evaluate our model (trained on YT-VIS 2021 with k = 7 slots) using a varying number of slots (from 1 to 12) and present the results in Fig. D.2.2. We observe that while using fewer slots steadily deteriorates the performance, our method performs relatively well with a larger number of slots. This suggests that our method is relatively robust to the usage of a larger number of slots than needed. This property is useful for object discovery in images where the number of objects is unknown. 
2This is in contrast to the fixed learned initialization used in unconditioned SAVi (Kipf et al., 2022) and SAVi++(Elsayed et al., 2022). 
149
Appendix D. Appendix for Chapter 6 
D.2.7 Effect of ViT Architecture on Final Performance 
In addition to studying how the choice of self-superivsed method and ViT outputs affect the performance of VideoSAUR (see Fig. 6.6c and Fig. 6.6d in the main paper), we also explore the effect of the scale of ViT architecture on the performance. To this end, we compare VideoSAUR with DINO features of 2 different ViT sizes (Small and Base) and two different patch sizes (16 × 16 and 8 × 8 resolutions) on the MOVi-C dataset (see Table D.2.6). The results are presented in Fig. D.2.3. We find that smaller patch size is important for sharper masks (measured by the mBO metric), while both larger architecture and smaller patch size are important for a better split of the scene to object masks (measured by the FG-ARI metric). 
D.3 Architectural Details and Hyperparameters 
Here we describe details about our model, its training and baselines that we use for comparison. We release our code at https://github.com/martius-lab/videosaur. 
D.3.1 SlotMixer Decoder 
We describe the SlotMixer decoder, and how we adapted it for 2D decoding. We keep the original terminology from Sajjadi et al. (2022) for consistency. SlotMixer performs three 
1 2 3 4 5 6 7 8 9 101112 Number of slots 
0 
10 
20 
30 
40 
FG -A 
R I 
1 2 3 4 5 6 7 8 9 101112 Number of slots 
0 
10 
20 
30 
40 
m B 
O 
VideoSAUR STEVE Random pattern 
Figure D.2.2: Changing the number of slots during evaluation on the YT-VIS 2021 dataset (mean ± standard dev., 5 seeds). 
150
D.3. Architectural Details and Hyperparameters 
0 
20 
40 
60 
FG -A 
R I 
0 
20 
40 
m B 
O 
Small 16x16 Base 16x16 Small 8x8 Base 8x8 
Figure D.2.3: Effect of ViT architecture choice and patch size on VideoSAUR training on the MOVi-C (mean ± standard dev., 3 seeds). 
Table D.2.6: ViT networks configuration. 
Model Patch Size Dim Heads Tokens Params 
Small 16 384 6 196 21M Small 8 384 6 784 21M Base 16 768 12 196 85M Base 8 768 12 784 85M 
steps for decoding: the allocation step assigns slots to spatial positions, the mixing step creates a slot mix for each spatial position, and the render step decodes the slot mix to the final output. See Fig. D.3.1 for an overview and pseudocode implementing the decoder. 
Allocation Step This step takes as input the slots st ∈ RK×M and a learned positional embedding p ∈ RL×M and outputs a feature vector f ∈ RL×M using a cross-attention Transformer. In particular, this Transformer iterates several cross-attention operations (and applies residual two-layer MLPs) using the position embeddings as queries to attend into the set of slots, where the position embeddings are residually updated using values from the slots. Importantly, the position embeddings are processed independently of each other. We utilize pre-normalization and also apply a layer norm to the slots before feeding them into the Transformer. In contrast to Sajjadi et al. (2022), we use a learned positional embedding initialized from a normal distribution instead of 3D encodings for the query rays, and do not apply a MLP to the positional embedding. 
Mixing Step The mixing step is similar to a single-head attention step using the features f as queries and the slots st as keys, where the slots are averaged as the values to form the slot mix m ∈ RL×M that is used for decoding to the final output: 
q = norm(f) Uq Uq ∈ RM×M , 
k = norm(s) Uk Uk ∈ RM×M , 
A = softmax ( qk⊤/ 
√ M ) 
A ∈ RL×K , 
m = sA m ∈ RL×M . 
Render Step The render step takes the slot mix m ∈ RL×M , adds the positional embedding p ∈ RL×M and applies a MLP with ReLU activation independently to each position: 
y = MLP(m + p). 
151
Appendix D. Appendix for Chapter 6 
A P P̂ 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.0 0.2 0.4 0.6 0.8 1.0 
0.0 
0.5 
1.0 
0.00.51.0 0.0 0.025 0.05 
Figure D.2.4: Additional visualization of affinity matrix A, transition probabilities P and decoder predictions of transition probabilities P̂ between patches (marked by purple and green) of the frame xt and patches of the next frame xt+1 for YouTube-VIS 2021 validation videos. Red indicates maximum affinity/probability. 
Instead of adding the positional embedding, we also explored concatenating it to the slot mix; we did not find large differences from doing so. 
D.3.2 ViT Encoders as Dense Features Extractors 
The Vision Transformer (ViT) (Dosovitskiy et al., 2021b) architecture takes an input frame, denoted here as x ∈ R244×224×3, which is divided into a grid of non-overlapping 
152
D.3. Architectural Details and Hyperparameters 
In pu 
t 
t=1 11 21 31 41 51 
Vi de 
oS A 
U R 
Figure D.2.5: Failure case for long video prediction. Note that the original videos in YouTube-VIS are resampled from the original 30 fps to 6 fps, thus the original length of the video is 250 frames. The slots are reassigned to the background, while small objects are not recognized. 
contiguous patches of resolution N × N . Each of these patches is then passed through a linear transformation to generate a set of patch feature embeddings, h0 ∈ RL×D. 
The set of patch tokens is subsequently provided as input to a standard Transformer network. This Transformer network is comprised of a sequence of self-attention and feed-forward layers, alongside residual connections for each layer. These residual connections are important for letting each patch representation hi keep a correspondence to the original image patch representation h0 and thus making the patch representation a dense (with the resolution 
√ L × 
√ L) representation of the image. In the self-attention layers, the token 
representations are updated through an attention mechanism that takes into account the representations of all tokens: 
[qi, ki, vi] = hi−1Uqkv Uqkv ∈ RD×3D 
A = softmax ( qiki⊤/ 
√ D ) 
A ∈ RL×L 
oi = Avi 
Here qi, ki, vi, oi are queries, keys, values and outputs of the self-attention layer i. In contrast to DINOSAUR (Seitzer et al., 2023), which uses the outputs oi as the target image representation, we use attention keys ki from the last self-attention layer of ViT as the dense image representation that is provided to the temporal similarity loss (see Fig. 6.6c for a detailed comparison of these representations). However, we still use the outputs oi as the input to the slot attention grouping module. 
153
Appendix D. Appendix for Chapter 6 
Slots 
Allocation Transformer 
Position Embed. 
Slot Mixing 
Render MLP 
Predicted Output 
1 pos_emb = Param ( random_norm (n_pos , dim)) 2 
3 def mixer ( slots ): 4 bs , n_slots , dim = slots . shape 5 pos_emb = pos_emb . unsqueeze (0) \ 6 . expand (bs , -1, -1) 7 
8 # Step 1: Allocation Transformer 9 feats = xa_transf (q=pos_emb , 
10 kv= norm_kv ( slots )) 11 
12 # Step 2: Slot Mixing 13 q = linear_q ( norm_q ( feats )) 14 k = linear_k ( norm_k ( slots )) 15 dots = einsum ("bpd , bsd -> bps", 16 q, k) 17 dots *= q. shape [ -1]** -0.5 18 attn = softmax (dots , dim = -1) 19 slot_mix = einsum ("bps , bsd -> bpd", 20 attn , slots ) 21 
22 # Step 3: Rendering with MLP 23 slot_mix += pos_emb 24 outputs = mlp( slot_mix ) 25 
26 return outputs 
Figure D.3.1: SlotMixer decoder. Left: SlotMixer performs three steps for decoding: the allocation transformer assigns slots st to spatial positions p, the slot mixing step creates a slot mix for each spatial position, and the render MLP decodes the slot mix to the final output yt. Right: PyTorch-like pseudocode for the SlotMixer decoder. 
D.3.3 Other Modules 
We group the dense encoder features with a recurrent slot attention module similar to Singh et al. (2022c) and Kipf et al. (2022). First, we transform the original features with a two-layer MLP with an output dimension equal to the slot dimension. Second, we use a slot attention module initialized with randomly sampled slots to group the first frame features, while for subsequent frames, we initialize the slot attention module with the slots of the previous frame, additionally transformed with a predictor module. We use the GRU recurrent unit in the slot attention grouping, but not the residual MLP. Similar to SAVi (Kipf et al., 2022) and STEVE (Singh et al., 2022c), we use a one-layer transformer as the predictor module. In addition, we propose to decouple the number of Slot Attention 
154
D.3. Architectural Details and Hyperparameters 
Table D.3.1: Next-frame feature prediction with different decoders. 
MOVi-C MOVi-E YT-VIS 
FG-ARI mBO FG-ARI mBO FG-ARI mBO 
One decoder head 44.6 23.5 61.3 22.1 33.4 24.6 Two decoder heads 47.2 24.7 62.9 24.0 37.9 27.3 
iterations in the first frame and other frames of the video. This allows more iterations for the first frames (we use 3 iterations similar to image-based methods) and fewer iterations for the next frames where the initialization is much better (we use 2 iterations). For computational reasons, we were training on relatively short 4-frame segments of original videos, i.e. T = 4. 
D.3.4 Next-Frame Feature Prediction Details 
In this part, we cover implementation details for the next-frame feature prediction ablation presented in Table 6.2. Reconstructing frame features from the current and next frame simultaneously with a single decoder is problematic because the decoder masks that are used for evaluation would be in reference to both the current and next frame. One way to overcome this problem is by using two decoder heads: dcurrent for the current frame and dnext for the next frame. Each head produces its own predictions and masks. In this case, masks from the dcurrent head can be used for evaluation. While more powerful, this approach also requires more memory and is slower than standard setting with only one head. In our experiments, we confirm that the version with two different Mixer decoders performs better than simultaneous reconstruction with one decoder (see Table D.3.1). We use this better version for our comparisons even though it is heavier than our method which needs only one decoder. 
D.3.5 Baselines 
Block Pattern The block pattern baseline serves to show metrics for a trivial decompo-sition of the video into regular blocks. It is intended to show the difficulty of the dataset and how much object-centric methods improve upon such a trivial solution, as the metrics values could be difficult to interpret without further calibration. To this end, we are 
155
Appendix D. Appendix for Chapter 6 
splitting the video to k spatial blocks consistently for all frames of the video, similar to how Seitzer et al. (2023) are splitting images into regular blocks. 
SAVi We reimplement SAVi (Kipf et al., 2022) close to the official implementation3. In particular, we use the SAVi-L architecture for all experiments. This corresponds to the version using a ResNet-34 encoder as described by Kipf et al. (2022), and a CNN broadcast mixture decoder with 4 layers. We apply the unconditional version of SAVi, using a fixed learned slot initialization instead. We train the model for 200 000 steps on all datasets, with a batch size of 64, using image reconstruction as the training signal. For training, we use videos with 4 frames, with a single slot attention step per frame. 
STEVE We reimplement STEVE (Singh et al., 2022c) close to the official implemen-tation4. We use the proposed configuration for the MOVi datasets and only change the number of slots to 11 for MOVi-C, 15 for MOVi-E and 7 for YT-VIS 2021. STEVE trains a dVAE (Rolfe, 2017) on the video frames to extract a discrete latent code that is used as the reconstruction target. STEVE uses a CNN encoder with 4 layers and a Transformer decoder with 8 layers. We train the model for 200 000 steps for MOVi-C and YT-VIS datasets and for 100 000 steps for MOVi-E datasets which resulted in optimal performance on this dataset, with a batch size of 24. Like Singh et al. (2022c), for training, we use videos with 3 frames, with two slot attention steps per frame. 
D.3.6 Compute Requirements 
We used a cluster of A100 GPUs (with 40 and 80 Gb memory) for running the experiments. A single training run (100k steps) of VideoSAUR equipped with DINO B/16 with a batch size of 128 takes roughly 18 hours on one A100 GPU with 40 GB memory. We use 5 seeds for the final results and 3 seeds for other experiments. Overall, we estimate the total compute spend on the whole project including training of all baselines and the method development (including dead ends) to be around 800-1000 GPU days (this is a rough estimate obtained from our cluster usage). 
3https://github.com/google-research/slot-attention-video/ 4https://github.com/singhgautam/steve 
156
D.4. Dataset Details 
Table D.4.1: Overview of datasets used in this work. For the training process, we solely utilize images or videos derived from the relevant datasets, with no reliance on labels. To generate central crops, we initially resize the mask so that its shorter dimension is 224 pixels. Subsequently, we extract the most centrally located crop, maintaining a size of 224 by 224 pixels. 
Dataset Videos Images Description Citation 
MOVi-C, -D, -E 9 750 – Train split videos Greff et al. (2022) MOVi-C, -D, -E validation 250 – Val. split w. instance segm. labels Greff et al. (2022) COCO 2017 – 118 287 Train split Lin et al. (2014) COCO 2017 validation – 5 000 Val split w. instance segm. labels Lin et al. (2014) YouTube-VIS 2021 2785 – Part of train split videos Yang et al. (2021) YouTube-VIS 2021 210 – Part of train split w. instance segm. labels Yang et al. (2021) YouTube-VIS 2019 200 – Part of train split w. instance segm. labels Yang et al. (2019) DAVIS-2017-Unsupervised 30 – Val. split w. instance segm. labels Pont-Tuset et al. 
(2017b) 
D.4 Dataset Details 
In this section, we provide details about the datasets used in this work. See Table D.4.1 for an overview. 
MOVi datasets For MOVi-C, MOVi-D and MOVi-E, we use the standard training and test splits provided in the respective releases of MOVi datasets: 9750 training videos and 250 validation videos. For a fair comparison, all the methods are trained on images with the same initial resolution 128 × 128. Consistent with previous work (Kipf et al., 2022; Elsayed et al., 2022; Singh et al., 2022c; Seitzer et al., 2023), we utilize the validation split of the MOVi dataset for our evaluations. 
YouTube-VIS datasets The YouTube-VIS datasets (Yang et al., 2019; Yang et al., 2021) are benchmarks originally used for supervised video instance segmentation. The video instance segmentation task involves segmenting, tracking and classifying instances throughout a video. It is a challenging dataset because it contains various different classes of objects and the complexities of real-world video dynamics. To the best of our knowledge, this is the first work attempting unsupervised instance segmentation on YouTube-VIS. 
157
Appendix D. Appendix for Chapter 6 
There are two different versions of this dataset: YouTube-VIS 2019 and YouTube-VIS 2021. The YouTube-VIS 2019 dataset is mainly derived from the Video Object Segmentation (VOS) dataset. It has a limited number of individual instances (an average of 1.7 per video for the training set), and the categories of instances in the same video are usually different. In contrast, the 2021 edition of YouTube-VIS incorporates a higher quantity of objects with more difficult trajectories (average 3.4 per video for the additional videos in the train set) and thus are more interesting for object-centric learning. We sample both training and validation frames with a rate of 6 frames per second (each 5th frame of the original videos with 30 fps). 
As the original validation dataset is not publicly available, and the evaluation server does not compute the object-centric metrics we need, we split the original training set into two parts (210 videos for validation and the other videos for training). Overall, we use 2775 videos for training, and 210 videos additionally added in YT-VIS 2021 train for validation. 
DAVIS dataset The DAVIS-2017-Unsupervised dataset (Pont-Tuset et al., 2017b) is used for video object segmentation and also contains videos with multiple objects per video (average is 1.97 for 30 validation videos). As those videos are not related to YouTube-VIS videos, this dataset is useful for the evaluation of transfer abilities for real-world object-centric learning algorithms. 
COCO dataset To test the properties of our proposed similarity loss for image-based object-centric learning we use the COCO dataset (Lin et al., 2014). Similar to Seitzer et al. (2023), we use 118287 training images (without labels) to train and 5 000 validation images (with labels) for performance evaluation. 
D.5 Additional Examples 
We include additional example predictions of our model: 
 Figure D.5.1: comparing VideoSAUR to STEVE on Youtube-VIS 2021. 
 Figure D.5.2: comparing VideoSAUR to STEVE on MOVi-C. 
 Figure D.5.3: comparing VideoSAUR to STEVE on MOVi-E. 
158
D.5. Additional Examples 
 Figure D.5.4: comparing feature reconstruction and temporal similarity loss on MOVi-C. 
 Figure D.5.5: long-term video predictions on Youtube-VIS 2021 (VideoSAUR with DINO B/16 features). 
 Figure D.5.6: long-term video predictions on Youtube-VIS 2021 (VideoSAUR with DINOv2 B/14 features). 
159
Appendix D. Appendix for Chapter 6 
In pu 
t t=0 3 6 9 12 15 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R 
Figure D.5.1: Additional examples on YouTube-VIS 2021. 
160
D.5. Additional Examples 
In pu 
t 
t=0 3 6 9 12 15 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R 
Figure D.5.2: Additional examples on MOVi-C. 
161
Appendix D. Appendix for Chapter 6 
In pu 
t t=0 3 6 9 12 15 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R In 
pu t 
ST EV 
E Vi 
de oS 
A U 
R 
Figure D.5.3: Additional examples on MOVi-E. 
162
D.5. Additional Examples 
In pu 
t 
t=0 3 6 9 12 15 18 21 
Fe at 
. Si 
m . 
In pu 
t Fe 
at . 
Si m 
. In 
pu t 
Fe at 
. Si 
m . 
In pu 
t Fe 
at . 
Si m 
. In 
pu t 
Fe at 
. Si 
m . 
Figure D.5.4: Difference between VideoSAUR train with feature reconstruction and tem-poral feature similarity losses on MOVi-C. We show videos with larger differences in performance between the two methods. 
163
Appendix D. Appendix for Chapter 6 
In pu 
t 
t=0 5 10 15 20 25 30 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R In 
pu t 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R In 
pu t 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R 
Figure D.5.5: Prediction of VideoSAUR with DINO B/16 features on longer videos from YouTube-VIS 2021. 
164
D.5. Additional Examples 
In pu 
t 
t=1 5 10 15 20 25 29 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R In 
pu t 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R In 
pu t 
Vi de 
oS A 
U R 
In pu 
t Vi 
de oS 
A U 
R 
Figure D.5.6: Prediction of VideoSAUR with DINOv2 B/14 features on longer videos from YouTube-VIS 2021. 
165
List of Tables 
5.1 Comparison to prior art and iterative improvement via self-training (evalu-ated by IoU after Hungarian matching) on the PASCAL 2012 val set. The results for SwAV and IIC methods are taken from MaskContrast paper. COMUS results are mean ± standard dev. over 5 runs. . . . . . . . . . . 68 
5.2 COMUS performance on PASCAL VOC 2007 test (evaluated by IoU after Hungarian matching). The test data was never seen during self-learning or validation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68 
5.3 Unsupervised semantic segmentation before and after self-learning evaluated by mIoU after Hungarian matching on the MS COCO val set. As discovered object category we count those categories with an IoU > 20% from all 81 categories. Also, we show IoU for categories that have corresponding cluster (i.e., with IoU larger than zero). . . . . . . . . . . . . . . . . . . . . . . . . 69 
5.4 Transfer from PASCAL VOC to MS COCO for the 21 PASCAL VOC classes. Training on the simpler PASCAL dataset yields better performance on COCO than learning on COCO itself while both COMUS runs perform better than DeepSpectral. . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 
5.5 Ablation experiment to identify the effect of individual components of the unsupervised learning process. . . . . . . . . . . . . . . . . . . . . . . . . . 70 
5.6 Comparison of COMUS performance with different feature extractors on PASCAL VOC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71 
5.7 Comparison between different class-agnostic foreground segmentation methods. 71 5.8 Over-clustering results on PASCAL VOC evaluated with mIoU after majority 
voting. We present the results for 30 clusters, whereas also include the results for 50 clusters for comparison with MaskContrast (Van Gansbeke et al., 2021). 72 
166
LIST OF TABLES 
6.1 Comparison with state-of-the-art methods on the MOVi-C, MOVi-E, and YT-VIS datasets. We report foreground adjusted rand index (FG-ARI) and mean best overlap (mBO) over 5 random seeds. Both metrics are computed for the whole video (24 frames for MOVi, 6 frames for YT-VIS). . . . . . . 87 
6.2 Loss Ablation on MOVi-C and YT-VIS. . . . . . . . . . . . . . . . . . . . 89 6.3 Robustness to introducing camera motion (MOVi-D → MOVi-E). . . . . . 90 6.4 Decoder comparison on MOVi-C and YT-VIS. . . . . . . . . . . . . . . . . 90 6.5 Comparing VideoSAUR with features trained on MOVi-E (MAE+MOVi-E) 
to features trained on ImageNet (MAE+ImageNet). For MAE+MOVi-E, we pre-train a ViT-B/16 using the self-supervised MAE method on MOVi-E for 200 epochs. VideoSAUR is able to perform high-quality object discovery even without access to any external data. . . . . . . . . . . . . . . . . . . 92 
A.1 SCALOR hyper-parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . 110 A.2 General hyper-parameters used by SMORL for visual environments. . . . . 111 A.3 Environment-specific hyper-parameters used by SMORL for visual environ-
ments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112 
B.1 General hyperparameters used by SRICS for all environments. . . . . . . . 125 B.2 Hyperparameters for the interaction graph estimation for all environments. 125 
C.1 Spectral Clustering parameters study, performance after the first iteration. 128 C.2 Clustering of random subsets of ImageNet classes. . . . . . . . . . . . . . . 129 C.3 Choice of the unsupervised salient object detector. We compared COMUS 
performance with three different unsupervised saliency masks detectors: self-supervised BasNet model (Qin et al., 2019), original DeepUSPS (Nguyen et al., 2019) and spectral decomposition saliency masks from DeepSpec-tral (Melas-Kyriazi et al., 2022). All the models are evaluated with by IoU after Hungarian matching on the PASCAL 2012 val set. . . . . . . . . . . 130 
C.4 Effect of object proposals from supervised saliency detector. . . . . . . . . 131 C.5 Number of semantic categories bias. Performance of studied methods on 
two subsets of PASCALVOC val dataset. . . . . . . . . . . . . . . . . . . . 132 C.6 More detailed comparison to prior art and iterative improvement via self-
training (evaluated by IoU after Hungarian matching) on the PASCAL 2012 val set. Our method results are averaged over 5 runs. . . . . . . . . . . . . 133 
167
LIST OF TABLES 
C.7 Spectral clustering parameters for COMUS on PASCAL VOC and MS COCO datasets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135 
C.8 Self-training parameters for COMUS on PASCAL VOC and MS COCO datasets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136 
D.1.1Comparison with state-of-the-art methods on the MOVi-C, MOVi-E image datasets. Both metrics are computed for individual frames. The results for SLATE and DINOSAUR are from Seitzer et al. (2023), while LSD results are from Jiang et al. (2023). We report mean ± standard dev. over 5 runs for our model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142 
D.1.2Comparison of VideoSAUR with DINOv2 ViT B/14 features to SMTC (Qian et al., 2023) on the DAVIS-2017-Unsupervised validation set. The results for SMTC are from Qian et al. (2023). . . . . . . . . . . . . . . . . . . . . 144 
D.1.3Comparison of VideoSAUR with DINOv2 ViT B/14 features to OCLR (Xie et al., 2022) and SOLV (Aydemir et al., 2023) on YT-VIS 2019. The results for OCLR and SOLV are from Aydemir et al. (2023). . . . . . . . . . . . . 144 
D.2.1Performance of VideoSAUR on the YT-VIS 2021 dataset, varying the length of the video segment (mean ± standard dev., 5 seeds for VideoSAUR with DINO features and STEVE. VideoSAUR with DINOv2 features are one seed only due to computational limitations). . . . . . . . . . . . . . . . . . 145 
D.2.2Comparing VideoSAUR predicting temporal similarities to predicting ground truth optical flow on the MOVi-C and MOVi-E datasets. We report Video FG-ARI of a version of VideoSAUR with optical flow (both backward and forward) as well as the original VideoSAUR with temporal features similarity.146 
D.2.3Extended ablation of VideoSAUR components on MOVi-E. We compare VideoSAUR model with different choices of the decoder (Mixer vs MLP used by DINOSAUR) and loss types (temporal similarity loss vs feature reconstruction). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147 
D.2.4Mixer decoder with smaller DINO features (S/16) on YT-VIS 2021 (mean ± standard dev., 3 seeds). . . . . . . . . . . . . . . . . . . . . . . . . . . . 148 
D.2.5Loss ablation study on COCO dataset. Metrics are image-based ARI and mBO (mean, 3 seeds). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148 
D.2.6ViT networks configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . 151 D.3.1Next-frame feature prediction with different decoders. . . . . . . . . . . . . 155 
168
LIST OF TABLES 
D.4.1Overview of datasets used in this work. For the training process, we solely utilize images or videos derived from the relevant datasets, with no reliance on labels. To generate central crops, we initially resize the mask so that its shorter dimension is 224 pixels. Subsequently, we extract the most centrally located crop, maintaining a size of 224 by 224 pixels. . . . . . . . . . . . . 157 
169
List of Figures 
2.1 Agent-environment interactions by different types of agents. In contrast to standard RL agents, autonomous RL agents should be able to learn in the environment without supervision. During training the agent generates its tasks and learns how to solve them. During the evaluation, the agent is provided with external tasks from the environment. . . . . . . . . . . . . . 9 
2.2 Two main advantages of the agents equipped with goals: (b) multitasking, (c) task decomposition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 
2.3 Autonomous goal-conditioned agents. During training such agents sample goals from the learned goal space. Subsequently, during evaluation agents are provided with external goals to solve. . . . . . . . . . . . . . . . . . . . 13 
2.4 Illustration of the binding problem. While it is possible to represent each object simultaneously in a consistent format, the representation of the pair of objects using a fixed-length representation is problematic. . . . . . . . . 19 
2.5 Classification of object-centric representations by the scene separation cri-teria. Instance slots represent non-overlapping parts of the scene. Each slot bins to one of the objects in the scene without specific preference. In contrast, sequential slots are assigned one by one by explaining those parts of the scene that still need to be explained. Spatial slots bind to representations at particular locations in the image. Finally, categorical slots represent scenes based on the object category. The figure is adapted from Greff et al. (2020). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 
171
LIST OF FIGURES 
3.1 Our proposed SMORL architecture. Representations zt are obtained from observations ot through the object-centric SCALOR encoder qϕ, and pro-cessed by the goal-conditional attention policy πθ(at|zt, zg). During training, representations of goals are sampled conditionally on the representations of the first observation z1. At test time, the agent is provided with an external goal image og that is processed with the same SCALOR encoder to a set of potential goals {zn}Nn=1. After this, the goal zg is sequentially chosen from this set. This way, the agent attempts to solve all the discovered sub-tasks one-by-one, not simultaneously. . . . . . . . . . . . . . . . . . . . . . . . . 31 
3.2 Multi-Object Visual Push and Rearrange environments with 2 objects and a Sawyer robotic arm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 
3.3 Average distance of objects to goal positions, comparing SMORL using ground truth representations to SAC with ground truth representations in the Rearrange environment with different number of objects. SAC struggles to improve performance when the combinatorial complexity of the scene rises. The dotted line indicates the performance of a passive policy that performs no movements. Results averaged over 5 random seeds, shaded regions indicate one standard deviation. . . . . . . . . . . . . . . . . . . . 39 
3.4 Average distance of objects to goal positions, comparing SMORL to Visual RL Baselines. In addition to the baselines, we show SAC’s performance with ground truth representations. Results averaged over 5 random seeds, shaded regions indicate one standard deviation. . . . . . . . . . . . . . . . 40 
3.5 Out-of-distribution generalization of SMORL agent training on Visual Rearrange with two objects and being tested with one object. Green line shows final performance when training with one object. . . . . . . . . . . . 41 
172
LIST OF FIGURES 
4.1 Our SRICS method. First, the interaction graph is inferred from observed environment dynamics containing links from cause to affected entity. This gives rise to subspaces that can be independently controlled, corresponding to subgoals gi. Next, the subgoals gi are used to construct a selectivity reward signal rsel. The selectivity reward rsel incentivizes the agent to only control the main entity i towards sgoal,i within each subgoal gi without affecting entities outside the subgoal. SRICS learns to solve an external goal sgoal by decomposing it into an ordered list of subgoals gi and solving each using SAC (Haarnoja et al., 2018) with a goal-conditioned policy πθ. As a result, the agent attempts to solve all the discovered subgoals one-by-one, without destroying previously solved subgoals. . . . . . . . . . . . . . . . . 46 
4.2 The dynamical model. For a given object j, the function dint computes each of the other objects’ effect on the object j using the hidden states ht. The effects from all the other objects are aggregated in the interaction effect vector hj,int 
t . Next, the function dact computes the action’s effect hj,act t on 
the object j. Both effects are combined in the GRU. Finally, object’s state estimation ŝjt+1 is estimated from the hidden state hjt+1 using the prediction function dpred. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 
4.3 Average distance of objects and arm to the goal positions, comparing SRICS to SMORL, SAC+HER and HAC baselines. For all the experiments, results are averaged over 5 random seeds, shaded regions indicate one standard deviation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53 
4.4 Subtask success rate for SRICS and SMORL for each subtask individually during evaluation in the Relational Rearrange environment. Both methods can solve Arm reaching subgoal, whereas on other subtasks SRICS performs better than SMORL. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 
4.5 Average distance of objects and arm to the goal positions, comparing our method and two ablated variants on 3 and 4 objects Rearrange environments. 55 
4.6 Generalization to unseen combination of objects. . . . . . . . . . . . . . . 56 
173
LIST OF FIGURES 
5.1 Unsupervised semantic segmentation predictions on PASCAL VOC (Ev-eringham et al., 2012). Our COMUS does not use human annotations to discover objects and their precise localization. In contrast to the prior state-of-the-art method MaskContrast (Van Gansbeke et al., 2021), COMUS yields more precise segmentations, avoids confusion of categories, and is not restricted to only one object category per image. . . . . . . . . . . . . . . 58 
5.2 Overview of our self-supervised semantic segmentation framework. First, the self-supervised representation learning network (e.g., DINO (Caron et al., 2021)) and the unsupervised saliency detector (e.g., DeepUSPS (Nguyen et al., 2019)) are trained without manual annotation on object-centric and saliency datasets (e.g., ImageNet (Deng et al., 2009) and MSRA (Cheng et al., 2015)). Next, we use the saliency detector to estimate object proposal masks from the original semantic segmentation dataset. After this, the original images are cropped to the boundaries of object proposal masks and resized. We compute feature vectors within these regions and cluster them with spectral clustering to discover different object categories. We filter the clusters by removing the most uncertain examples. The cluster IDs are combined with the saliency masks to form unsupervised pseudo-masks for self-training of a semantic segmentation network (e.g., DeepLabv3). . . . 60 
5.3 Visualization of unsupervised pseudo-masks on PASCAL VOC val set. (left) 2D t-SNE projection of object proposal features. Colors correspond to cluster IDs. (right) Pseudo-masks from different clusters. The pseudo-masks were randomly sampled for each cluster from both cluster core pseudo-masks (green columns) and filtered pseudo-masks (red columns). . . . . . . . . . 62 
5.4 Visualization of foreground masks obtained with different foreground seg-mentation methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 
5.5 Visualization of discovered subcategories on PASCAL VOC val set after clustering of self-supervised representations into 30 clusters. The pseudo-masks were randomly sampled for each cluster. Each row shows two clusters of the same category. The clusters have clear semantic interpretations, such as different dog breeds, flying or staying on land airplanes. . . . . . . . . 73 
174
LIST OF FIGURES 
6.1 We propose a self-supervised temporal similarity loss for training object-centric video models. For each patch at time t, the model has to predict a distribution P̂t,t+k indicating where all semantically-similar patches have moved to k steps into the future. The target distribution Pt,t+k is computed with a softmax on the affinity matrix At,t+k containing the cosine distance between all patch features ht, ht+k. The loss incentivizes the model to group areas with consistent motion and semantics into slots. . . . . . . . . 77 
6.2 Overview of VideoSAUR. Object slots st are extracted from patch features ht of a self-supervised ViT using time-recurrent slot attention, conditional on slots from the previous time step t−1. The model is trained by reconstructing the patch features ht of the current frame xt, and by predicting the similarity distribution over patches of a future frame xt+k (see also Fig. 6.1). The predictions yrec 
t and ysim t are decoded efficiently using SlotMixer decoder. 80 
6.3 Affinity matrix At,t+k and transition probabilities Pt,t+k values between patches (marked by purple and green) of the frame xt and patches of the future frame xt+k in MOVi-C (left) and YT-VIS (right). Red indicates maximum affinity/probability. Also see Fig. D.2.4 for more examples, and our website for an interactive visualization of temporal feature similarities. 82 
6.4 Example predictions of VideoSAUR compared to recent video object-centric methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 
6.5 Zero-shot transfer of learned object-centric representations on YT-VIS 2021 to the YT-VIS 2019 and DAVIS datasets for different number of slots. . . 88 
6.6 Studying the effect of different parameters of the temporal similarity loss. 92 
A.1 First and second PCA dimension of zwhat space of SCALOR trained on Visual Rearrange with 3 objects. The plot shows 3000 random zwhat points collected from a random policy. Each point is colored as the mean of the foreground pixels on the crop detected by SCALOR. For each cluster, the highlighted point shows an example crop. Dashed lines indicate the Voronoi partitions according to cluster centers found by running k-means clustering. Figure is best viewed on screen. . . . . . . . . . . . . . . . . . . . . . . . . 104 
175
LIST OF FIGURES 
A.2 Comparison of VAE and SCALOR representations. (a) shows MIG scores of VAE and SCALOR representations on data obtained from running a random policy in the Visual Rearrange environment with 3 objects (with whisker showing the standard deviation over 5 runs), (b) shows the mutual information matrix for SCALOR representations on the same data. . . . . 105 
A.3 Reconstructions of scene observations using learned SCALOR representation and decoder. Rows are a) original images (green boxes for recognized objects, red boxes for non-propagated objects), b) full reconstructions, c) bounding boxes of recognized objects produced using zwhere, d) foreground object reconstructions, e) segmentation masks of objects generated by SCALOR. 113 
A.4 Ablation study of goal-conditioned attention policy on Visual Rearrange with two objects (left) and out-of-distribution testing on Visual Rearrange with one object (right). We compare variants of the attention policy with only goal-conditional and only goal-unconditional attention heads, plus an alternative approach to aggregate sets of vector representations in the form of DeepSets (Zaheer et al., 2017). Our results demonstrate that both types of attention heads are necessary to achieve the best results. . . . . . . . . 114 
A.5 Performance of a SMORL agent trained for 106 timesteps on Visual Rear-range with 2 objects. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114 
B.1 Visualization of the Multi-object Rearrange environment with a) 4 objects, b) 6 different objects and c) Multi-object Relational Rearrange environment. 116 
B.2 Average distance to the goal positions, comparing our method to the SAC and SMORL baselines on a) Rearrange environment with 6 different objects and b) Rearrange environment with 4 objects with coordinates and velocity state representation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118 
B.3 The selectivity part of the reward signal for both SRICS and SMORL agents averaged over all entities. While the SMORL agent is not optimized for being selective, the selectivity increases over SMORL training because the agent is gaining control over objects. However, for the SRICS agent, the increase in selectivity is much faster as the agent is incentified to be selective.119 
B.4 Average interaction weights obtained from the GNN dynamical model. . . 120 
176
LIST OF FIGURES 
B.5 Ordering of the independently controllable subgoals according to the depth of the corresponding nodes in the interaction graph. When the interaction graph is a DAG, such ordering corresponds to the reversed topological ordering. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121 
B.6 Average object distance to the goal positions, comparing SRICS to SMORL and SAC+HER. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122 
B.7 SRICS pipeline during evaluation. . . . . . . . . . . . . . . . . . . . . . . 122 
C.1 (a) COMUS (Iteration 1) performance with different clustering methods. (b) Effect of "% filtered" on final performance of COMUS. The results are mean ± standard dev. over 5 runs. . . . . . . . . . . . . . . . . . . . . . . 128 
C.2 Number of self-training iterations in COMUS training. The results are mean ± standard dev. over 5 runs. . . . . . . . . . . . . . . . . . . . . . . 128 
C.3 Connection between mean relative size of objects and IoU for each COCO category. The Spearman’s rank correlation between relative size and IoU is equal to 0.43. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 
C.4 IoU for COCO categories after Hungarian matching of the cluster IDs to ground-truth categories. . . . . . . . . . . . . . . . . . . . . . . . . . . . 137 
C.5 Predictions of the COMUS method trained on PASCAL VOC on COCO val set. We notice that the predictions from models trained on PASCAL VOC transfer reasonably well to COCO. . . . . . . . . . . . . . . . . . . . 138 
C.6 Several failure samples of the COMUS method on PASCAL VOC val set. The failures show the limitation and biases of our method, such as bias towards salient objects and misclassifications in multi-object images. . . . 138 
C.7 COMUS and MaskContrast predictions on random images from PASCAL VOC val set. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139 
C.8 COMUS predictions on random images from COCO val set. . . . . . . . 139 
D.1.1 Image-based comparison on YouTube-VIS (mean ± standard dev., 3 seeds). 142 D.2.1 Histogram of video lengths on the YT-VIS 2021 validation dataset. . . . . 145 D.2.2 Changing the number of slots during evaluation on the YT-VIS 2021 
dataset (mean ± standard dev., 5 seeds). . . . . . . . . . . . . . . . . . . . 150 D.2.3 Effect of ViT architecture choice and patch size on VideoSAUR training on 
the MOVi-C (mean ± standard dev., 3 seeds). . . . . . . . . . . . . . . . . 151 
177
LIST OF FIGURES 
D.2.4 Additional visualization of affinity matrix A, transition probabilities P and decoder predictions of transition probabilities P̂ between patches (marked by purple and green) of the frame xt and patches of the next frame xt+1 
for YouTube-VIS 2021 validation videos. Red indicates maximum affini-ty/probability. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152 
D.2.5 Failure case for long video prediction. Note that the original videos in YouTube-VIS are resampled from the original 30 fps to 6 fps, thus the original length of the video is 250 frames. The slots are reassigned to the background, while small objects are not recognized. . . . . . . . . . . . . 153 
D.3.1 SlotMixer decoder. Left: SlotMixer performs three steps for decoding: the allocation transformer assigns slots st to spatial positions p, the slot mixing step creates a slot mix for each spatial position, and the render MLP decodes the slot mix to the final output yt. Right: PyTorch-like pseudocode for the SlotMixer decoder. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154 
D.5.1Additional examples on YouTube-VIS 2021. . . . . . . . . . . . . . . . . . 160 D.5.2Additional examples on MOVi-C. . . . . . . . . . . . . . . . . . . . . . . . 161 D.5.3Additional examples on MOVi-E. . . . . . . . . . . . . . . . . . . . . . . . 162 D.5.4 Difference between VideoSAUR train with feature reconstruction and tem-
poral feature similarity losses on MOVi-C. We show videos with larger differences in performance between the two methods. . . . . . . . . . . . . 163 
D.5.5 Prediction of VideoSAUR with DINO B/16 features on longer videos from YouTube-VIS 2021. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164 
D.5.6 Prediction of VideoSAUR with DINOv2 B/14 features on longer videos from YouTube-VIS 2021. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165 
178
List of Algorithms 
1 SMORL: Self-Supervised Multi-Object RL (Training) . . . . . . . . . . . . 36 2 Object Categories Discovery for Unsupervised Pseudo-Masks Estimation . 63 3 Self-training with Noisy Pseudo-Masks . . . . . . . . . . . . . . . . . . . . 65 4 SMORL: Self-Supervised Multi-object RL (Training with Details) . . . . . 108 5 SMORL (Evaluation) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109 6 SRICS: Self-Supervised Relational RL with Independently Controllable 
Subgoals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115 
179
Bibliography 
Adjodah, D., T. Klinger, and J. Joseph (2018). “Symbolic relation networks for reinforcement learning”. Relational Representation Learning NeurIPS Workshop. url: https://r 2learning.github.io/assets/papers/CameraReadySubmission%203.pdf (cit. on p. 21). 
Agudelo-España, Diego et al. (2020). “A Real-Robot Dataset for Assessing Transferability of Learned Dynamics Models”. International Conference on Robotics and Automation. url: https://ieeexplore.ieee.org/document/9197392 (cit. on p. 6). 
Akakzia, Ahmed et al. (2021). “Grounding Language to Autonomously-Acquired Skills via Goal Generation”. International Conference on Learning Representations. url: https://arxiv.org/abs/2006.07185v3 (cit. on p. 44). 
Andrychowicz, Marcin et al. (2017). “Hindsight Experience Replay”. Neural Information Processing Systems. url: https://proceedings.neurips.cc/paper/2017/hash/453 fadbd8a1a3af50a9df4df899537b5-Abstract.html (cit. on pp. 10, 14, 35, 38, 52, 54). 
Anonymous (2023). “Adaptive Slot Attention: Object Discovery with Dynamic Slot Num-ber”. Submitted to International Conference on Learning Representations. url: https: //openreview.net/forum?id=EaLfdBPlIh (cit. on p. 100). 
Assran, Mahmoud et al. (2022). “Masked Siamese Networks for Label-Efficient Learning”. IEEE European Conference on Computer Vision. url: https://arxiv.org/abs/2204 .07141 (cit. on pp. 79, 91). 
Aubret, Arthur, Laetitia matignon, and Salima Hassas (2021). “DisTop: Discovering a Topological representation to learn diverse and rewarding skills”. arXiv:2106.03853. url: https://arxiv.org/abs/2106.03853v1 (cit. on pp. 44, 45). 
Aydemir, Görkay, Weidi Xie, and Fatma Güney (2023). “Self-supervised Object-Centric Learning for Videos”. Neural Information Processing Systems. url: https://arxiv.o rg/abs/2310.06907 (cit. on pp. 79, 87, 100, 143, 144, 168). 
181
BIBLIOGRAPHY 
Baldassarre, Federico and Hossein Azizpour (2022). “Towards self-supervised learning of global and object-centric representations”. arXiv:2203.05997. url: https://arxiv.or g/abs/2203.05997 (cit. on p. 20). 
Bao, Zhipeng et al. (2022). “Discovering Objects that Can Move”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2203.10159 (cit. on pp. 20, 76, 79). 
Bao, Zhipeng et al. (2023). “Object Discovery from Motion-Guided Tokens”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2303.15555 (cit. on p. 79). 
Baranes, Adrien and Pierre-Yves Oudeyer (2013). “Active learning of inverse models with intrinsically motivated goal exploration in robots”. Robotics Autonomous Systems. url: https://arxiv.org/abs/1301.4862v1 (cit. on pp. 32, 45). 
Battaglia, Peter W. et al. (2016). “Interaction Networks for Learning about Objects, Relations and Physics”. Neural Information Processing Systems. url: https://arxiv .org/abs/1612.00222 (cit. on pp. 19, 45, 48). 
Bengio, Yoshua, Aaron Courville, and Pascal Vincent (2013). “Representation learning: A review and new perspectives”. IEEE Transactions on Pattern Analysis and Machine Intelligence. url: https://arxiv.org/abs/1206.5538 (cit. on pp. 2, 18). 
Biza, Ondrej et al. (2023). “Invariant Slot Attention: Object Discovery with Slot-Centric Reference Frames”. International Conference on Machine Learning. url: https://arx iv.org/abs/2302.04973 (cit. on pp. 78, 79, 143). 
Blaes, Sebastian et al. (2019). “Control What You Can: Intrinsically Motivated Task-Planning Agent”. Advances in Neural Information Processing Systems (NeurIPS 2019). Curran Associates, Inc. url: https://arxiv.org/abs/1906.08190v2 (cit. on pp. 11, 14, 21, 45, 47, 48, 56, 98). 
Brady, Jack et al. (2023). “Provably Learning Object-Centric Representations”. url: https://arxiv.org/abs/2305.14229 (cit. on p. 20). 
Burgess, Christopher P. et al. (2019). “MONet: Unsupervised Scene Decomposition and Representation”. url: https://arxiv.org/abs/1901.11390 (cit. on pp. 20, 23, 30, 33, 44, 47, 62, 76). 
Caron, Mathilde et al. (2020). “Unsupervised learning of visual features by contrasting cluster assignments”. url: https://arxiv.org/abs/2006.09882v5 (cit. on pp. 68, 71, 128). 
182
BIBLIOGRAPHY 
Caron, Mathilde et al. (2021). “Emerging Properties in Self-Supervised Vision Transformers”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/2 104.14294 (cit. on pp. 18, 59–61, 64, 71, 76, 79, 91, 128, 136, 174). 
Caruana, Rich (1997). “Multitask learning”. Machine learning (cit. on p. 10). Chang, Michael, Thomas L. Griffiths, and Sergey Levine (2022). “Object Representations as 
Fixed Points: Training Iterative Refinement Algorithms with Implicit Differentiation”. Neural Information Processing Systems. url: https://arxiv.org/abs/2207.00787 (cit. on p. 78). 
Chen, Boyuan et al. (2023). “Self-Supervised Reinforcement Learning that Transfers using Random Features”. arXiv:2305.17250. url: https://arxiv.org/abs/2305.17250v1 (cit. on p. 9). 
Chen, Chang, Fei Deng, and Sungjin Ahn (2021a). “ROOTS: Object-Centric Representation and Rendering of 3D Scenes.” Journal of Machine Learning Research (cit. on p. 62). 
Chen, Liang-Chieh et al. (2017). “Rethinking Atrous Convolution for Semantic Image Segmentation”. ArXiv: 1706.05587. url: https://arxiv.org/abs/1706.05587v3 (cit. on p. 66). 
Chen, Liang-Chieh et al. (2018a). “DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs”. IEEE Transac-tions on Pattern Analysis and Machine Intelligence. url: https://arxiv.org/abs/16 06.00915v2 (cit. on pp. 58, 69, 134). 
Chen, Liang-Chieh et al. (2020a). “Leveraging Semi-Supervised Learning in Video Sequences for Urban Scene Segmentation”. IEEE European Conference on Computer Vision (cit. on p. 66). 
Chen, Tian Qi et al. (2018b). “Isolating Sources of Disentanglement in Variational Au-toencoders”. Neural Information Processing Systems. url: https://proceedings.ne urips.cc/paper/2018/hash/1ee3dfcd8a0645a25a35977997223d22-Abstract.html (cit. on pp. 18, 25, 26, 104). 
Chen, Ting et al. (2020b). “A Simple Framework for Contrastive Learning of Visual Representations”. International Conference on Machine Learning. url: https://proc eedings.mlr.press/v119/chen20j.html (cit. on pp. 18, 23). 
Chen, Ting et al. (2020c). “A Simple Framework for Contrastive Learning of Visual Repre-sentations”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedings.mlr.press/v119/chen20j.ht ml (cit. on p. 32). 
183
BIBLIOGRAPHY 
Chen, Xinlei, Saining Xie, and Kaiming He (2021b). “An Empirical Study of Training Self-Supervised Vision Transformers”. ICCV. url: https://arxiv.org/abs/2104.02057 (cit. on pp. 79, 91). 
Cheng, Ming-Ming et al. (2015). “Global Contrast Based Salient Region Detection”. IEEE Transactions on Pattern Analysis and Machine Intelligence. url: https://mmcheng.n et/mftp/Papers/SaliencyTPAMI.pdf (cit. on pp. 60, 64, 174). 
Cho, Jang Hyun et al. (2021). “Picie: Unsupervised semantic segmentation using invariance and equivariance in clustering”. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2103.17070v1 (cit. on p. 61). 
Chung, Junyoung et al. (2014). “Empirical evaluation of gated recurrent neural networks on sequence modeling”. English (US). NIPS 2014 Workshop on Deep Learning. url: https://arxiv.org/abs/1412.3555v1 (cit. on p. 48). 
Colas, Cédric et al. (2019). “CURIOUS: Intrinsically Motivated Modular Multi-Goal Reinforcement Learning”. International Conference on Machine Learning. url: https: //arxiv.org/abs/1810.06284 (cit. on pp. 43, 44, 47, 56, 98). 
Colas, Cédric et al. (2020). “Language as a Cognitive Tool to Imagine Goals in Curiosity-Driven Exploration”. Neural Information Processing Systems. url: https://arxiv.or g/abs/2002.09253v4 (cit. on p. 45). 
Colas, Cédric et al. (2022). “Autotelic agents with intrinsically motivated goal-conditioned reinforcement learning: a short survey”. Journal of Artificial Intelligence Research. url: https://arxiv.org/abs/2012.09830 (cit. on pp. 12, 44, 45). 
Cordts, Marius et al. (2016). “The cityscapes dataset for semantic urban scene understand-ing”. Proceedings of the IEEE conference on computer vision and pattern recognition. url: https://arxiv.org/abs/1604.01685v2 (cit. on p. 58). 
Crawford, Eric and Joelle Pineau (2020). “Spatially Invariant Unsupervised Object Detec-tion with Convolutional Neural Networks”. AAAI Conference on Artificial Intelligence. url: https://ojs.aaai.org/index.php/AAAI/article/view/4216 (cit. on p. 78). 
Daniel, Tal and Aviv Tamar (2023). “DDLP: Unsupervised Object-centric Video Prection with Deep Dynamic Latent Particles”. arXiv:2306.05957. url: https://arxiv.org/a bs/2306.05957 (cit. on p. 42). 
Dayan, Peter and Geoffrey E Hinton (1993). “Feudal reinforcement learning”. Neural Information Processing Systems. url: https://www.cs.toronto.edu/~fritz/absps /dh93.pdf (cit. on p. 11). 
184
BIBLIOGRAPHY 
Deng, Jia et al. (2009). “ImageNet: A Large-scale Hierarchical Image Database”. Conference on Computer Vision and Pattern Recognition. url: https://ieeexplore.ieee.org/d ocument/5206848 (cit. on pp. 60, 98, 136, 174). 
Devin, Coline et al. (2018). “Deep object-centric representations for generalizable robot learning”. International Conference on Robotics and Automation. url: https://arxiv .org/abs/1708.04225 (cit. on p. 44). 
Devlin, Jacob et al. (2019). “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technolo-gies, Volume 1 (Long and Short Papers). Minneapolis, Minnesota: Association for Computational Linguistics. url: https://www.aclweb.org/anthology/N19-1423 (cit. on p. 32). 
Dittadi, Andrea et al. (2022). “Generalization and Robustness Implications in Object-Centric Learning”. International Conference on Machine Learning. url: https://pro ceedings.mlr.press/v162/dittadi22a.html (cit. on pp. 2, 3, 19). 
Dosovitskiy, Alexey et al. (2021a). “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale”. International Conference on Learning Representations. url: https://openreview.net/forum?id=YicbFdNTTy (cit. on p. 64). 
— (2021b). “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale”. International Conference on Learning Representations. url: https://openrev iew.net/forum?id=YicbFdNTTy (cit. on pp. 81, 152). 
Dwiel, Zach et al. (2019). “Hierarchical policy learning is sensitive to goal space design”. arXiv:1905.01537. url: https://arxiv.org/abs/1905.01537v2 (cit. on p. 47). 
Elsayed, Gamaleldin Fathy et al. (2022). “SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos”. Neural Information Processing Systems. url: htt ps://openreview.net/forum?id=fT9W53lLxNS (cit. on pp. 20, 76, 78, 79, 148, 149, 157). 
Engelcke, Martin, Oiwi Parker Jones, and Ingmar Posner (2021). “GENESIS-V2: Inferring Unordered Object Representations without Iterative Refinement”. Neural Information Processing Systems. url: https://openreview.net/forum?id=nRBZWEUhIhW (cit. on p. 78). 
Engelcke, Martin et al. (2020). “GENESIS: Generative Scene Inference and Sampling with Object-Centric Latent Representations”. International Conference on Learning 
185
BIBLIOGRAPHY 
Representations. url: https://openreview.net/forum?id=BkxfaTVFwH (cit. on p. 62). 
Eslami, S. M. Ali et al. (2016). “Attend, Infer, Repeat: Fast Scene Understanding with Generative Models”. Neural Information Processing Systems. url: https://proceedi ngs.neurips.cc/paper/2016/hash/52947e0ade57a09e4a1386d08f17b656-Abstrac t.html (cit. on p. 20). 
Everingham, Mark et al. (2012). “The pascal visual object classes challenge 2012 (voc2012) results (2012)” (cit. on pp. 58, 59, 67, 69, 174). 
Everingham, Mark et al. (2015). “The pascal visual object classes challenge: A retrospective”. International journal of computer vision (cit. on p. 136). 
Feng, Fan and Sara Magliacane (2023). “Learning Dynamic Attribute-factored World Models for Efficient Multi-object Reinforcement Learning”. Neural Information Processing Systems. url: https://arxiv.org/abs/2307.09205 (cit. on pp. 42, 88, 96, 97). 
Florensa, Carlos, Yan Duan, and Pieter Abbeel (2017). “Stochastic Neural Networks for Hierarchical Reinforcement Learning”. International Conference on Learning Represen-tations. url: https://openreview.net/forum?id=B1oK8aoxe (cit. on p. 46). 
Florensa, Carlos et al. (2018). “Automatic Goal Generation for Reinforcement Learning Agents”. International Conference on Machine Learning (cit. on pp. 9, 44). 
Forestier, Sébastien et al. (2017). “Intrinsically motivated goal exploration processes with automatic curriculum learning”. arXiv:1708.02190. url: https://arxiv.org/abs/17 08.02190v3 (cit. on pp. 45, 47). 
— (2022). “Intrinsically motivated goal exploration processes with automatic curriculum learning”. The Journal of Machine Learning Research. url: https://arxiv.org/abs /1708.02190v3 (cit. on p. 14). 
Frans, Kevin et al. (2018). “Meta Learning Shared Hierarchies”. International Conference on Learning Representations. url: https://openreview.net/forum?id=SyX0IeWAW (cit. on p. 11). 
Fujimoto, Scott, David Meger, and Doina Precup (2019). “Off-policy deep reinforcement learning without exploration”. International Conference on Machine Learning. url: https://arxiv.org/abs/1812.02900 (cit. on p. 96). 
Gates, Alexander J and Yong-Yeol Ahn (2017). “The impact of random models on clustering similarity”. Journal of Machine Learning Research. url: https://arxiv.org/abs/17 01.06508 (cit. on p. 27). 
186
BIBLIOGRAPHY 
Geiger, Andreas et al. (2013). “Vision meets Robotics: The KITTI Dataset”. International Journal of Robotics Research. url: https://www.cvlibs.net/publications/Geiger 2013IJRR.pdf (cit. on p. 78). 
Ghosh, Dibya, Abhishek Gupta, and Sergey Levine (2019). “Learning Actionable Repre-sentations with Goal Conditioned Policies”. 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019. OpenReview.net. url: https://openreview.net/forum?id=Hye9lnCct7 (cit. on p. 32). 
Greff, Klaus, Rupesh Kumar Srivastava, and Jürgen Schmidhuber (2016). “Binding via Reconstruction Clustering”. arXiv:1511.06418. url: https://arxiv.org/abs/1511.0 6418 (cit. on pp. 19, 32). 
Greff, Klaus, Sjoerd van Steenkiste, and Jürgen Schmidhuber (2017). “Neural Expectation Maximization”. Neural Information Processing Systems. url: https://proceedings .neurips.cc/paper/2017/hash/d2cd33e9c0236a8c2d8bd3fa91ad3acf-Abstract.h tml (cit. on pp. 30, 44, 78). 
— (2020). “On the Binding Problem in Artificial Neural Networks”. url: https://arxiv .org/abs/2012.05208 (cit. on pp. 2, 16, 21, 22, 32, 171). 
Greff, Klaus et al. (2019). “Multi-Object Representation Learning with Iterative Variational Inference”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedings.mlr.press/v97/greff19a.ht ml (cit. on pp. 23, 30, 33, 44, 62, 76, 78, 86). 
Greff, Klaus et al. (2022). “Kubric: A Scalable Dataset Generator”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2203.03570 (cit. on pp. 76, 78, 85, 89, 157). 
Grill, Jean-Bastien et al. (2020). “Bootstrap Your Own Latent - A New Approach to Self-Supervised Learning”. Neural Information Processing Systems. url: https://arx iv.org/abs/2006.07733 (cit. on p. 23). 
Gumbsch, Christian, Martin V Butz, and Georg Martius (2021). “Sparsely changing latent states for prediction and planning in partially observable domains”. url: https://arx iv.org/abs/2110.15949 (cit. on pp. 88, 100). 
Gürtler, Nico, Dieter Büchler, and Georg Martius (2021). “Hierarchical Reinforcement Learning with Timed Subgoals”. url: https://arxiv.org/abs/2112.03100v1 (cit. on p. 11). 
187
BIBLIOGRAPHY 
Gürtler, Nico et al. (2023). “Benchmarking Offline Reinforcement Learning on Real-Robot Hardware”. International Conference on Learning Representations. url: https://ope nreview.net/forum?id=3k5CUGDLNdd (cit. on p. 96). 
Haarnoja, Tuomas et al. (2018). “Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedin gs.mlr.press/v80/haarnoja18b.html (cit. on pp. 35, 46, 52, 54, 173). 
Hafner, Danijar et al. (2020). “Dream to control: Learning behaviors by latent imagination”. International Conference on Learning Representations. url: https://arxiv.org/abs /1912.01603 (cit. on p. 100). 
Hamilton, Mark et al. (2022). “Unsupervised Semantic Segmentation by Distilling Feature Correspondences”. International Conference on Learning Representations. url: https: //openreview.net/forum?id=SaKO6z6Hl0c (cit. on pp. 61, 135). 
Haramati, Dan, Tal Daniel, and Aviv Tamar (2023). “Entity-Centric Reinforcement Learn-ing for Object Manipulation from Pixels”. Goal-Conditioned Reinforcement Learning NeurIPS workshop. url: https://openreview.net/forum?id=uDxeSZ1wdI (cit. on pp. 42, 96). 
Hariharan, Bharath et al. (2011). “Semantic contours from inverse detectors”. IEEE International Conference on Computer Vision (cit. on p. 69). 
Hausman, Karol et al. (2018). “Learning an Embedding Space for Transferable Robot Skills”. International Conference on Learning Representations. OpenReview.net. url: https://openreview.net/forum?id=rk07ZXZRb (cit. on pp. 32, 46). 
He, Kaiming et al. (2020). “Momentum Contrast for Unsupervised Visual Representation Learning”. Conference on Computer Vision and Pattern Recognition. IEEE. url: http s://doi.org/10.1109/CVPR42600.2020.00975 (cit. on pp. 32, 128, 129). 
He, Kaiming et al. (2022). “Masked Autoencoders are Scalable Vision Learners”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2111.06 377 (cit. on pp. 18, 23, 61, 76, 79, 91, 128). 
H’enaff, Olivier J. et al. (2022). “Object discovery and representation networks”. IEEE European Conference on Computer Vision (cit. on p. 61). 
Higgins, Irina et al. (2017a). “beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework”. International Conference on Learning Representations. url: https://openreview.net/forum?id=Sy2fzU9gl (cit. on p. 18). 
188
BIBLIOGRAPHY 
Higgins, Irina et al. (2017b). “DARLA: Improving Zero-Shot Transfer in Reinforcement Learning”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedings.mlr.press/v70/higgins17a .html (cit. on p. 40). 
Hsieh, Jun-Ting et al. (2021). “Learning to Decompose and Disentangle Representations for Video Prediction”. Neural Information Processing Systems. url: https://arxiv.o rg/abs/1806.04166v2 (cit. on p. 62). 
Hwang, Jyh-Jing et al. (2019). “SegSort: Segmentation by Discriminative Sorting of Segments”. IEEE International Conference on Computer Vision. url: https://arxiv .org/abs/1910.06962v2 (cit. on p. 61). 
Jabri, Allan, Andrew Owens, and Alexei Efros (2020). “Space-Time Correspondence as a Contrastive Random Walk”. Neural Information Processing Systems. url: https://ar xiv.org/abs/2006.14613 (cit. on p. 83). 
Ji, Xu, João F. Henriques, and Andrea Vedaldi (2019). “Invariant Information Clustering for Unsupervised Image Classification and Segmentation”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/1807.06653 (cit. on pp. 61, 68). 
Jia, Baoxiong, Yu Liu, and Siyuan Huang (2023). “Improving Object-centric Learning with Query Optimization”. International Conference on Learning Representations. url: https://arxiv.org/abs/2210.08990 (cit. on p. 78). 
Jiang, Jindong et al. (2020). “SCALOR: Generative World Models with Scalable Object Representations”. International Conference on Learning Representations. url: https ://openreview.net/pdf?id=SJxrKgStDH (cit. on pp. 24, 30, 36, 44, 47, 76, 78, 100, 111). 
Jiang, Jindong et al. (2023). “Object-Centric Slot Diffusion”. Neural Information Processing Systems. url: https://arxiv.org/abs/2303.10834 (cit. on pp. 79, 86, 141, 142, 168). 
Kabra, Rishabh et al. (2021). “SIMONe: View-Invariant, Temporally-Abstracted Object Representations via Unsupervised Video Decomposition”. Neural Information Processing Systems. url: https://openreview.net/forum?id=YSzTMntO1KY (cit. on p. 78). 
Kaelbling, Leslie Pack (1993). “Learning to achieve goals”. IJCAI. Citeseer (cit. on p. 10). Kakade, Sham Machandranath (2003). On the sample complexity of reinforcement learning. 
University of London, University College London (United Kingdom) (cit. on p. 15). 
189
BIBLIOGRAPHY 
Kalashnikov, Dmitry et al. (2018). “Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation”. arXiv:1806.10293. url: https://arxiv.org/abs/1806 .10293 (cit. on p. 32). 
Karazija, Laurynas, Iro Laina, and Christian Rupprecht (2021). “ClevrTex: A Texture-Rich Benchmark for Unsupervised Multi-Object Segmentation”. NeurIPS Track on Datasets and Benchmarks. url: https://arxiv.org/abs/2111.10265 (cit. on p. 78). 
Ke, Tsung-Wei et al. (2022). “Unsupervised Hierarchical Semantic Segmentation with Multiview Cosegmentation and Clustering Transformers”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2204.11432v1 (cit. on p. 61). 
Kim, Hyunjik and Andriy Mnih (2018). “Disentangling by factorising”. International Conference on Machine Learning. PMLR. url: https://arxiv.org/abs/1802.05983 v3 (cit. on p. 18). 
Kim, Jinwoo et al. (2023). “Shepherding Slots to Objects: Towards Stable and Robust Object-Centric Learning”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2303.17842 (cit. on p. 78). 
Kingma, Diederik P. and Jimmy Ba (2015). “Adam: A Method for Stochastic Optimization”. International Conference on Learning Representations. url: https://arxiv.org/abs /1412.6980 (cit. on p. 110). 
Kingma, Diederik P and Max Welling (2014). “Auto-encoding Variational Bayes”. Interna-tional Conference on Learning Representations. url: https://arxiv.org/abs/1312 .6114 (cit. on p. 17). 
Kipf, Thomas et al. (2022). “Conditional Object-centric Learning from Video”. International Conference on Learning Representations. url: https://openreview.net/forum?id=a D7uesX1GF_ (cit. on pp. 20, 22, 23, 62, 76, 78–81, 83, 86, 87, 100, 146, 148, 149, 154, 156, 157). 
Kipf, Thomas N., Elise van der Pol, and Max Welling (2020). “Contrastive Learning of Structured World Models”. 8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020. OpenReview.net. url: https: //openreview.net/forum?id=H1gax6VtDB (cit. on pp. 19, 21, 32, 42, 47, 48, 100). 
Kipf, Thomas N and Max Welling (2017). “Semi-Supervised Classification with Graph Convolutional Networks”. International Conference on Learning Representations. url: https://arxiv.org/abs/2307.00865v1 (cit. on p. 21). 
190
BIBLIOGRAPHY 
Kipf, Thomas N. et al. (2018). “Neural Relational Inference for Interacting Systems”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedings.mlr.press/v80/kipf18a.html (cit. on pp. 21, 42, 45, 47, 48, 50). 
Klyubin, A.S., D. Polani, and C.L. Nehaniv (2005). “Empowerment: a universal agent-centric measure of control”. IEEE Congress on Evolutionary Computation. url: https: //ieeexplore.ieee.org/document/1554676 (cit. on p. 51). 
Kosiorek, Adam et al. (2018). “Sequential Attend, Infer, Repeat: Generative Modelling of Moving Objects”. Neural Information Processing Systems. url: https://proceedin gs.neurips.cc/paper/2018/hash/7417744a2bac776fabe5a09b21c707a2-Abstract .html (cit. on pp. 24, 30, 78). 
Kuhn, Harold W. (1955). “The Hungarian method for the assignment problem”. Naval Research Logistics Quarterly. url: https://onlinelibrary.wiley.com/doi/abs/10 .1002/nav.3800020109 (cit. on p. 67). 
Kulkarni, Tejas D. et al. (2016). “Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation”. Neural Information Processing Systems. url: https://arxiv.org/abs/1604.06057v2 (cit. on p. 11). 
Laversanne-Finot, Adrien, Alexandre Pere, and Pierre-Yves Oudeyer (2018). “Curiosity Driven Exploration of Learned Disentangled Goal Spaces”. Conference on Robot Learn-ing. Proceedings of Machine Learning Research. PMLR. url: http://proceedings.m lr.press/v87/laversanne-finot18a.html (cit. on p. 32). 
Levine, Sergey et al. (2016). “End-to-end training of deep visuomotor policies”. Journal of Machine Learning Research. url: https://arxiv.org/abs/1504.00702 (cit. on p. 32). 
Levine, Sergey et al. (2018). “Learning hand-eye coordination for robotic grasping with deep learning and large-scale data collection”. The International Journal of Robotics Research. url: https://arxiv.org/abs/1603.02199v4 (cit. on p. 32). 
Levine, Sergey et al. (2020). “Offline reinforcement learning: Tutorial, review, and perspec-tives on open problems”. arXiv:2005.01643. url: https://arxiv.org/abs/2005.016 43 (cit. on p. 96). 
Levy, Andrew et al. (2019). “Learning Multi-Level Hierarchies with Hindsight”. Interna-tional Conference on Learning Representations. url: https://arxiv.org/abs/1712 .00948 (cit. on pp. 11, 44, 46, 47, 54). 
191
BIBLIOGRAPHY 
Li, Kehan et al. (2022). “ACSeg: Adaptive Conceptualization for Unsupervised Semantic Segmentation”. arXiv:2210.05944. url: http://arxiv.org/abs/2210.05944 (cit. on pp. 74, 99). 
Li, Siyuan et al. (2021). “Learning Subgoal Representations with Slow Dynamics”. Inter-national Conference on Learning Representations. url: https://openreview.net/fo rum?id=wxRwhSdORKG (cit. on p. 46). 
Li, Yujia et al. (2016). “Gated Graph Sequence Neural Networks”. International Conference on Learning Representations. url: https://arxiv.org/abs/1511.05493 (cit. on p. 48). 
Li, Yunzhu et al. (2020). “Causal Discovery in Physical Systems from Videos”. Neural Information Processing Systems. url: https://arxiv.org/abs/2007.00631v3 (cit. on pp. 21, 47, 48). 
Lin, Tsung-Yi et al. (2014). “Microsoft COCO: Common Objects in Context”. IEEE European Conference on Computer Vision. url: https://arxiv.org/abs/1405.0312 (cit. on pp. 58, 59, 67, 69, 86, 98, 136, 157, 158). 
Lin, Zhixuan et al. (2020). “SPACE: Unsupervised Object-Oriented Scene Representation via Spatial Attention and Decomposition”. International Conference on Learning Rep-resentations. url: https://openreview.net/forum?id=rkl03ySYDH (cit. on pp. 24, 78). 
Lippe, Phillip et al. (2022). “CITRIS: Causal Identifiability from Temporal Intervened Sequences”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: https://proceedings.mlr.press/v162/lippe22a .html (cit. on p. 97). 
Lippe, Phillip et al. (2023). “BISCUIT: Causal Representation Learning from Binary Interactions”. The 39th Conference on Uncertainty in Artificial Intelligence. url: https://openreview.net/forum?id=VS7Dn31xuB (cit. on p. 97). 
Liu, Xiao et al. (2021). “Self-supervised learning: Generative or contrastive”. IEEE transac-tions on knowledge and data engineering. url: https://arxiv.org/abs/2006.08218 (cit. on p. 18). 
Locatello, Francesco et al. (2019). “Challenging Common Assumptions in the Unsuper-vised Learning of Disentangled Representations”. International Conference on Machine Learning. Proceedings of Machine Learning Research. PMLR. url: http://proceedin gs.mlr.press/v97/locatello19a.html (cit. on p. 104). 
192
BIBLIOGRAPHY 
Locatello, Francesco et al. (2020). “Object-Centric Learning with Slot Attention”. Neural Information Processing Systems. url: https://arxiv.org/abs/2006.15055 (cit. on pp. 18, 20, 22, 30, 44, 47, 62, 76–78, 81, 84). 
Luxburg, Ulrike von (2007). “A tutorial on spectral clustering”. Statistics and Computing. url: https://arxiv.org/abs/0711.0189v1 (cit. on pp. 64, 65). 
Lynch, Corey et al. (2019). “Learning Latent Plans from Play”. url: https://arxiv.org /abs/1903.01973 (cit. on pp. 32, 46). 
Löwe, Sindy et al. (2020). “Amortized causal discovery: Learning to infer causal graphs from time-series data”. arXiv:2006.10833. url: https://arxiv.org/abs/2006.10833v3 (cit. on pp. 47, 48). 
Maaten, Laurens van der and Geoffrey Hinton (2008). “Visualizing Data using t-SNE”. Journal of Machine Learning Research. url: http://jmlr.org/papers/v9/vanderma aten08a.html (cit. on p. 68). 
Mambelli, Davide et al. (2022). “Compositional Multi-object Reinforcement Learning with Linear Relation Networks”. ICLR Workshop on the Elements of Reasoning: Objects, Structure and Causality. url: https://openreview.net/forum?id=HFUxPr_I5ec (cit. on pp. 42, 88). 
Mansouri, Amin et al. (2022). “Object-centric causal representation learning”. NeurIPS 2022 Workshop on Symmetry and Geometry in Neural Representations. url: https: //openreview.net/forum?id=RaIy9t062cD (cit. on p. 97). 
Mansouri, Amin et al. (2023). “Object-centric architectures enable efficient causal repre-sentation learning”. arXiv:2310.19054. url: https://arxiv.org/abs/2310.19054 (cit. on p. 97). 
Melas-Kyriazi, Luke et al. (2022). “Deep Spectral Methods: A Surprisingly Strong Baseline for Unsupervised Semantic Segmentation and Localization”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2205.07839v1 (cit. on pp. 61, 62, 68, 127, 129–131, 133, 135, 167). 
Mitchell, Terence R. (1982). “Motivation: New Directions for Theory, Research, and Practice”. The Academy of Management Review. url: http://www.jstor.org/stabl e/257251 (visited on 10/31/2023) (cit. on p. 2). 
Mitchell, Tom M (1980). “The need for biases in learning generalizations”. url: https: //www.cs.cmu.edu/~tom/pubs/NeedForBias_1980.pdf (cit. on p. 2). 
Mittal, Sudhanshu, Maxim Tatarchenko, and Thomas Brox (2019). “Semi-supervised semantic segmentation with high-and low-level consistency”. IEEE transactions on 
193
BIBLIOGRAPHY 
pattern analysis and machine intelligence. url: https://arxiv.org/abs/1908.05724 (cit. on p. 58). 
Nachum, Ofir et al. (2018). “Data-Efficient Hierarchical Reinforcement Learning”. Neural Information Processing Systems. url: https://arxiv.org/abs/1805.08296 (cit. on pp. 11, 44, 46, 47). 
Nair, Ashvin et al. (2018). “Visual Reinforcement Learning with Imagined Goals”. Neural Information Processing Systems. url: https://proceedings.neurips.cc/paper/2 018/hash/7ec69dd44416c46745f6edd947b470cd-Abstract.html (cit. on pp. 12–14, 30, 32, 35, 37, 44, 45, 53). 
Nair, Ashvin et al. (2020). “Contextual Imagined Goals for Self-Supervised Robotic Learn-ing”. Conference on Robot Learning. url: https://arxiv.org/abs/1910.11670 (cit. on pp. 13, 30, 32, 38, 44, 46). 
Nakano, Akihiro, Masahiro Suzuki, and Yutaka Matsuo (2023). “Interaction-Based Disen-tanglement of Entities for Object-Centric World Models”. International Conference on Learning Representations. url: https://openreview.net/forum?id=JQc2VowqCzz (cit. on p. 42). 
Nanbo, Li et al. (2021). “Object-Centric Representation Learning with Generative Spatial-Temporal Factorization”. Neural Information Processing Systems. url: https://arxi v.org/abs/2111.05393 (cit. on p. 62). 
Nasiriany, Soroush et al. (2019). “Planning with Goal-Conditioned Policies”. Neural Infor-mation Processing Systems. url: https://proceedings.neurips.cc/paper/2019/ha sh/c8cc6e90ccbff44c9cee23611711cdc4-Abstract.html (cit. on pp. 12, 42). 
Nath, Somjit et al. (2023). “Discovering Object-Centric Generalized Value Functions From Pixels”. International Conference on Learning Representations. url: https://arxiv .org/abs/2304.13892 (cit. on pp. 42, 96). 
Nguyen, Tam et al. (2019). “DeepUSPS: Deep Robust Unsupervised Saliency Prediction With Self-Supervision”. Neural Information Processing Systems. url: https://arxiv .org/abs/1909.13055 (cit. on pp. 59, 60, 64, 74, 99, 130, 135, 136, 167, 174). 
Oquab, Maxime et al. (2023). DINOv2: Learning Robust Visual Features without Supervision. url: https://arxiv.org/abs/2304.07193 (cit. on p. 144). 
Ouali, Yassine, Céline Hudelot, and Myriam Tami (2020). “Autoregressive unsupervised image segmentation”. IEEE European Conference on Computer Vision. Springer. url: https://arxiv.org/abs/2007.08247 (cit. on p. 61). 
194
BIBLIOGRAPHY 
Park, Seohong et al. (2022). “Lipschitz-constrained unsupervised skill discovery”. Interna-tional Conference on Learning Representations. url: https://arxiv.org/abs/2202 .00914 (cit. on p. 98). 
Park, Seohong et al. (2023). “Controllability-Aware Unsupervised Skill Discovery”. Interna-tional Conference on Machine Learning. url: https://arxiv.org/abs/2302.05103 (cit. on pp. 96, 98). 
Paszke, Adam et al. (2019). “PyTorch: An Imperative Style, High-Performance Deep Learning Library”. Neural Information Processing Systems. url: https://proceedin gs.neurips.cc/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract .html (cit. on p. 107). 
Pathak, Deepak et al. (2015). “Fully Convolutional Multi-Class Multiple Instance Learning”. ICLR Workshop. url: https://arxiv.org/abs/1412.7144v4 (cit. on p. 58). 
Pathak, Deepak et al. (2018). “Zero-Shot Visual Imitation”. 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. OpenReview.net. url: https://openreview.net /forum?id=BkisuzWRW (cit. on p. 32). 
Pervez, Adeel, Phillip Lippe, and Efstratios Gavves (2023). “Differentiable Mathematical Programming for Object-Centric Representation Learning”. International Conference on Learning Representations. url: https://openreview.net/forum?id=1J-ZTr7aypY (cit. on p. 78). 
Peters, Jonas, Dominik Janzing, and Bernhard Schölkopf (2017). Elements of causal inference: foundations and learning algorithms. MIT press. url: https://mitpress.m it.edu/9780262037310/elements-of-causal-inference (cit. on p. 2). 
Pitis, Silviu et al. (2020). “Maximum Entropy Gain Exploration for Long Horizon Multi-goal Reinforcement Learning”. International Conference on Machine Learning. url: https://arxiv.org/abs/2007.02832 (cit. on p. 13). 
Pong, Vitchyr et al. (2020). “Skew-Fit: State-Covering Self-Supervised Reinforcement Learning”. International Conference on Machine Learning. Proceedings of Machine Learning Research. url: http://proceedings.mlr.press/v119/pong20a.html (cit. on pp. 9, 13, 14, 30, 32, 38, 44, 45). 
Pont-Tuset, Jordi et al. (2017a). “Multiscale Combinatorial Grouping for Image Segmenta-tion and Object Proposal Generation”. IEEE Transactions on Pattern Analysis and Machine Intelligence. url: https://ieeexplore.ieee.org/document/7423791 (cit. on pp. 27, 86). 
195
BIBLIOGRAPHY 
Pont-Tuset, Jordi et al. (2017b). “The 2017 DAVIS Challenge on Video Object Segmenta-tion”. arXiv:1704.00675. url: https://arxiv.org/abs/1704.00675 (cit. on pp. 86, 143, 157, 158). 
Precup, Doina (2000). Temporal Abstraction in Reinforcement Learning. PhD Thesis (cit. on pp. 11, 12). 
Péré, Alexandre et al. (2018). “Unsupervised Learning of Goal Spaces for Intrinsically Motivated Goal Exploration”. 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. OpenReview.net. url: https://openreview.net/forum?id=S1DWPP1A-(cit. on pp. 13, 14, 32, 46). 
Qian, Rui et al. (2023). “Semantics Meets Temporal Correspondence: Self-supervised Object-centric Learning in Videos”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/2308.09951 (cit. on pp. 79, 87, 143, 144, 168). 
Qin, Xuebin et al. (2019). “BASNet: Boundary-Aware Salient Object Detection”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/pdf/2101.04 704.pdf (cit. on pp. 59, 64, 129, 130, 135, 136, 167). 
Radford, Alec et al. (2019). “Language Models are Unsupervised Multitask Learners”. url: https://gwern.net/doc/ai/nn/transformer/gpt/2019-radford.pdf (cit. on p. 32). 
Rolfe, Jason Tyler (2017). “Discrete Variational Autoencoders”. International Conference on Learning Representations. url: https://openreview.net/forum?id=ryMxXPFex (cit. on pp. 86, 141, 156). 
Rolinek, Michal, Dominik Zietlow, and Georg Martius (2019). “Variational Autoencoders Pursue PCA Directions (by Accident)”. IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2019, Long Beach, CA, USA, June 16-20, 2019. Computer Vision Foundation / IEEE. url: https://arxiv.org/abs/1812.06775 (cit. on pp. 17, 105). 
Ronneberger, Olaf, Philipp Fischer, and Thomas Brox (2015). “U-Net: Convolutional Networks for Biomedical Image Segmentation”. MICCAI. url: https://arxiv.org/a bs/1505.04597 (cit. on p. 58). 
Ryali, Chaitanya, David J. Schwab, and Ari S. Morcos (2021). “Learning Background Invariance Improves Generalization and Robustness in Self-Supervised Learning on ImageNet and Beyond”. NeurIPS 2021 Workshop on ImageNet: Past, Present, and Future. url: https://openreview.net/forum?id=zZnOG9ehfoO (cit. on p. 130). 
196
BIBLIOGRAPHY 
Röder, Frank et al. (2020). “Curious hierarchical actor-critic reinforcement learning”. International Conference on Artificial Neural Networks. Springer. url: https://arxiv .org/abs/2005.03420 (cit. on p. 11). 
Safadoust, Sadra and Fatma Güney (2023). “Multi-Object Discovery by Low-Dimensional Object Motion”. IEEE International Conference on Computer Vision. url: https://a rxiv.org/abs/2307.08027 (cit. on p. 78). 
Sajjadi, Mehdi SM et al. (2022). “Object Scene Representation Transformer”. Neural Information Processing Systems. url: https://arxiv.org/abs/2206.06922 (cit. on pp. 77, 79, 84, 150, 151). 
Salehi, Mohammadreza et al. (2023). “Time Does Tell: Self-Supervised Time-Tuning of Dense Image Representations”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/2308.11796 (cit. on p. 91). 
Sancaktar, Cansu, Sebastian Blaes, and Georg Martius (2022). “Curious exploration via structured world models yields zero-shot object manipulation”. url: https://arxiv.o rg/abs/2206.11403v2 (cit. on pp. 42, 56, 98). 
Santoro, Adam et al. (2017). “A simple neural network module for relational reasoning”. url: https://arxiv.org/abs/1706.01427v1 (cit. on p. 19). 
Schaul, Tom et al. (2015). “Universal Value Function Approximators”. International Con-ference on Machine Learning. JMLR Workshop and Conference Proceedings. JMLR.org. url: http://proceedings.mlr.press/v37/schaul15.html (cit. on p. 10). 
Schmidhuber, Jürgen (2010). “Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010)”. IEEE Transactions on Autonomous Mental Development. (Cit. on p. 9). 
Schölkopf, Bernhard et al. (2021). “Towards Causal Representation Learning”. IEEE -Advances in Machine Learning and Deep Neural Networks. url: https://arxiv.org /abs/2102.11107 (cit. on pp. 2, 3, 97). 
Seitzer, Maximilian, Bernhard Schölkopf, and Georg Martius (2021). “Causal Influence Detection for Improving Efficiency in Reinforcement Learning”. arXiv:2106.03443. url: https://arxiv.org/abs/2106.03443v2 (cit. on p. 51). 
Seitzer, Maximilian et al. (2023). “Bridging the Gap to Real-World Object-Centric Learn-ing”. International Conference on Learning Representations. url: https://arxiv.org /abs/2209.14860 (cit. on pp. 6, 20, 22, 23, 63, 68, 74, 76, 78, 79, 81, 84, 86, 88, 90, 92, 96, 99, 100, 141, 142, 148, 149, 153, 156–158, 168). 
Sharma, Archit et al. (2019). “Dynamics-aware unsupervised discovery of skills”. url: https://arxiv.org/abs/1907.01657 (cit. on pp. 96, 98). 
197
BIBLIOGRAPHY 
Sharma, Archit et al. (2021). “Autonomous reinforcement learning via subgoal curricula”. url: https://arxiv.org/abs/2107.12931v2 (cit. on pp. 9, 12). 
Simeoni, Oriane et al. (2021). “Localizing Objects with Self-Supervised Transformers and no Labels”. BMVC. url: https://arxiv.org/abs/2109.14279 (cit. on pp. 61, 62, 71). 
Singh, Gautam, Fei Deng, and Sungjin Ahn (2022a). “Illiterate DALL-E Learns to Compose”. International Conference on Learning Representations. url: https://openreview.ne t/forum?id=h0OYV0We3oh (cit. on pp. 62, 78, 79, 141, 148). 
Singh, Gautam, Yeongbin Kim, and Sungjin Ahn (2022b). “Neural Systematic Binder”. International Conference on Learning Representations. url: https://arxiv.org/abs /2211.01177 (cit. on p. 97). 
Singh, Gautam, Yi-Fu Wu, and Sungjin Ahn (2022c). “Simple Unsupervised Object-Centric Learning for Complex and Naturalistic Videos”. Neural Information Processing Systems. url: https://openreview.net/forum?id=eYfIM88MTUE (cit. on pp. 62, 76, 78–81, 86, 87, 154, 156, 157). 
Spelke, Elizabeth S. and Katherine D. Kinzler (2007). “Core Knowledge”. Developmental Science. url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-7687 .2007.00569.x (cit. on p. 2). 
Steels, Luc (2004). “The autotelic principle”. Embodied Artificial Intelligence: International Seminar, Dagstuhl Castle, Germany, July 7-11, 2003. Revised Papers. Springer (cit. on pp. 2, 12). 
Steenkiste, Sjoerd van, Klaus Greff, and Jürgen Schmidhuber (2019). “A perspective on objects and systematic generalization in model-based rl”. arXiv:1906.01035. url: https://arxiv.org/abs/1906.01035 (cit. on p. 32). 
Steenkiste, Sjoerd van et al. (2018). “Relational Neural Expectation Maximization: Un-supervised Discovery of Objects and their Interactions”. International Conference on Learning Representations. url: https://openreview.net/forum?id=ryH20GbRW (cit. on pp. 21, 47, 48, 78). 
Sutton, Richard S and Andrew G Barto (1998). Reinforcement learning: An introduction (cit. on p. 8). 
Sutton, Richard S, Doina Precup, and Satinder Singh (1999). “Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning”. Artificial intelligence (cit. on pp. 11, 12). 
198
BIBLIOGRAPHY 
Sutton, Richard S, Doina Precup, and Satinder P Singh (1998). “Intra-Option Learning about Temporally Abstract Actions.” International Conference on Machine Learning (cit. on p. 11). 
Tangemann, Matthias et al. (2023). “Unsupervised Object Learning via Common Fate”. Conference on Causal Learning and Reasoning. url: https://arxiv.org/abs/2110.0 6562 (cit. on pp. 20, 21, 81). 
Thomas, Valentin et al. (2018). “Disentangling the independently controllable factors of variation by interacting with the world”. arXiv:1802.09484. url: https://arxiv.org /abs/1804.06955v2 (cit. on p. 45). 
Todorov, E., T. Erez, and Y. Tassa (2012). “MuJoCo: A physics engine for model-based control”. 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems (cit. on pp. 37, 53). 
Traub, Manuel et al. (2023a). “Learning What and Where: Disentangling Location and Identity Tracking Without Supervision”. International Conference on Learning Rep-resentations. url: https://openreview.net/forum?id=NeDc-Ak-H_ (cit. on pp. 78, 88). 
Traub, Manuel et al. (2023b). “Looping LOCI: Developing Object Permanence from Videos”. url: https://arxiv.org/abs/2310.10372 (cit. on p. 144). 
Van Gansbeke, Wouter, Simon Vandenhende, and Luc Van Gool (2022). “Discovering Object Masks with Transformers for Unsupervised Semantic Segmentation”. arXiv:2206.06363. url: https://arxiv.org/abs/2206.06363 (cit. on pp. 74, 99). 
Van Gansbeke, Wouter et al. (2020). “Scan: Learning to classify images without labels”. European Conference on Computer Vision. Springer. url: https://arxiv.org/abs/2 005.12320 (cit. on pp. 128, 129). 
Van Gansbeke, Wouter et al. (2021). “Unsupervised Semantic Segmentation by Contrasting Object Mask Proposals”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/2102.06191 (cit. on pp. 58, 61, 64, 68, 69, 72, 127, 130, 133–135, 166, 174). 
Vaswani, Ashish et al. (2017). “Attention is All you Need”. Neural Information Processing Systems. url: https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547d ee91fbd053c1c4a845aa-Abstract.html (cit. on pp. 34, 107). 
Veerapaneni, Rishi et al. (2019). “Entity Abstraction in Visual Model-based Reinforcement Learning”. Conference on Robot Learning. url: https://arxiv.org/abs/1910.12827 (cit. on pp. 32, 43, 44, 47, 78, 96, 100). 
199
BIBLIOGRAPHY 
Vezhnevets, Alexander Sasha et al. (2017). “FeUdal Networks for Hierarchical Reinforcement Learning”. International Conference on Machine Learning. url: https://arxiv.org /abs/1703.01161v2 (cit. on pp. 11, 12, 44, 46). 
Vo, Huy V., Patrick Pérez, and Jean Ponce (2020). “Toward Unsupervised, Multi-object Discovery in Large-scale Image Collections”. IEEE European Conference on Computer Vision. url: https://arxiv.org/abs/2007.02662 (cit. on pp. 61, 62). 
Vo, Huy V. et al. (2021). “Large-scale Unsupervised Object Discovery”. Neural Information Processing Systems. url: https://arxiv.org/abs/2106.06650 (cit. on pp. 61, 62). 
Wang, Jingdong et al. (2017). “Salient Object Detection: A Discriminative Regional Feature Integration Approach”. International Journal of Computer Vision. url: https://arxi v.org/abs/1410.5926v1 (cit. on p. 136). 
Wang, Rundong et al. (2020a). “I2HRL: Interactive Influence-based Hierarchical Reinforce-ment Learning”. Proceedings of the 29th International Joint Conference on Artificial Intelligence. IJCAI, Yokohama, Japan. url: https://www.ijcai.org/proceedings /2020/433 (cit. on pp. 46, 47). 
Wang, Yangtao et al. (2022). “Self-Supervised Transformers for Unsupervised Object Discov-ery Using Normalized Cut”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2202.11539 (cit. on pp. 61, 62). 
Wang, Yufei et al. (2020b). “ROLL: Visual Self-Supervised Reinforcement Learning with Object Reasoning”. Conference on Robot Learning. url: https://arxiv.org/abs/20 11.06777v1 (cit. on pp. 9, 46). 
Warde-Farley, David et al. (2019). “Unsupervised Control Through Non-Parametric Dis-criminative Rewards”. 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019. OpenReview.net. url: https://openre view.net/forum?id=r1eVMnA9K7 (cit. on p. 32). 
Watters, Nicholas et al. (2019a). COBRA: Data-Efficient Model-Based RL through Unsuper-vised Object Discovery and Curiosity-Driven Exploration. arXiv: 1905.09275 [cs.LG]. url: https://arxiv.org/abs/1905.09275v2 (cit. on pp. 19, 32, 43, 96). 
Watters, Nick et al. (2019b). “Spatial Broadcast Decoder: A Simple Architecture for Disentangled Representations in VAEs”. ICLR Learning from Limited Labeled Data Workshop. url: https://openreview.net/forum?id=S1x7WjnzdV (cit. on pp. 20, 23). 
Wei, Yunchao et al. (2018). “Revisiting Dilated Convolution: A Simple Approach for Weakly-and Semi-Supervised Semantic Segmentation”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/1805.04574v2 (cit. on p. 58). 
200
BIBLIOGRAPHY 
Weis, Marissa A et al. (2021). “Benchmarking Unsupervised Object Representations for Video Sequences”. Journal of Machine Learning Research. url: https://jmlr.org/pa pers/v22/21-0199.html (cit. on pp. 20, 30, 78). 
Wertheimer, Max (2012). “On Perceived Motion and Figural Organization” (cit. on p. 20). Wu, Yizhe et al. (2021). “APEX: Unsupervised, Object-Centric Scene Segmentation and 
Tracking for Robot Manipulation”. arXiv:2105.14895. url: https://arxiv.org/abs /2105.14895v2 (cit. on pp. 44, 47). 
Wu, Ziyi et al. (2023a). “SlotDiffusion: Object-Centric Generative Modeling with Diffusion Models”. Neural Information Processing Systems. url: https://arxiv.org/abs/2305 .11281 (cit. on pp. 79, 86). 
Wu, Ziyi et al. (2023b). “SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models”. International Conference on Learning Representations. url: https://openreview.net/forum?id=TFbwV6I0VLg (cit. on pp. 88, 100). 
Xie, Junyu, Weidi Xie, and Andrew Zisserman (2022). “Segmenting moving objects via an object-centric layered representation”. Neural Information Processing Systems. url: https://arxiv.org/abs/2207.02206 (cit. on pp. 143, 144, 168). 
Xie, Qizhe et al. (2020). “Self-Training With Noisy Student Improves ImageNet Classifica-tion”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv .org/abs/1911.04252v4 (cit. on p. 66). 
Xu, Jiarui et al. (2022). “GroupViT: Semantic Segmentation Emerges from Text Supervi-sion”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv .org/abs/2202.11094 (cit. on p. 133). 
Yang, Linjie, Yuchen Fan, and Ning Xu (2019). “Video instance segmentation”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/1905.0 4804 (cit. on pp. 86, 98, 157). 
Yang, Linjie et al. (2021). The 3rd Large-scale Video Object Segmentation Challenge - video instance segmentation track. url: https://youtube-vos.org/dataset/vis (cit. on pp. 78, 86, 157). 
Yang, Yafei and Bo Yang (2022). “Promising or Elusive? Unsupervised Object Segmentation from Real-world Single Images”. Neural Information Processing Systems. url: https: //openreview.net/forum?id=DzPWTwfby5d (cit. on pp. 78, 148). 
Yi, Qi et al. (2022). “Object-Category Aware Reinforcement Learning”. Neural Information Processing Systems. url: https://openreview.net/forum?id=9Qjn_3gWLDc (cit. on pp. 42, 97). 
201
BIBLIOGRAPHY 
Yoon, Jaesik et al. (2023). “An Investigation into Pre-Training Object-Centric Represen-tations for Reinforcement Learning”. International Conference on Machine Learning. url: https://arxiv.org/abs/2302.04419 (cit. on pp. 42, 96). 
Zadaianchuk, Andrii and Georg Martius (2020). “Unsupervised Learning of Independently Controllable Dynamic Components”. ICML Object-Oriented Learning (OOL): Percep-tion, Representation, and Reasoning Workshop (cit. on p. 6). 
Zadaianchuk, Andrii, Georg Martius, and Fanny Yang (2022). “Self-supervised Rein-forcement Learning with Independently Controllable Subgoals”. Conference on Robot Learning. url: https://openreview.net/forum?id=xppLmXCbOw1 (cit. on pp. 4, 11, 42, 96, 100). 
Zadaianchuk, Andrii, Maximilian Seitzer, and Georg Martius (2021). “Self-supervised Visual Reinforcement Learning with Object-centric Representations”. International Conference on Learning Representations. url: https://openreview.net/forum?id=xppLmXCbOw1 (cit. on pp. 3, 11, 12, 43–46, 52–54, 88, 117, 122, 124). 
— (2023a). “Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities”. Neural Information Processing Systems. url: https://arxiv.or g/abs/2306.04829 (cit. on pp. 5, 20, 74, 96, 99, 100). 
Zadaianchuk, Andrii et al. (2023b). “Unsupervised Semantic Segmentation with Self-supervised Object-centric Representations”. International Conference on Learning Representations. url: https://openreview.net/forum?id=1_jFneF07YC (cit. on pp. 4, 97). 
Zaheer, Manzil et al. (2017). “Deep Sets”. Neural Information Processing Systems. url: https://proceedings.neurips.cc/paper/2017/hash/f22e4747da1aa27e363d86d4 0ff442fe-Abstract.html (cit. on pp. 106, 114, 176). 
Zhang, Richard, Phillip Isola, and Alexei A Efros (2016). “Colorful image colorization”. IEEE European Conference on Computer Vision. Springer. url: https://richzhang .github.io/colorization/ (cit. on p. 68). 
Zhang, Runsheng et al. (2020). “Object discovery from a single unlabeled image by mining frequent itemsets with multi-scale features”. IEEE Transactions on Image Processing. url: https://arxiv.org/abs/1902.09968v3 (cit. on p. 61). 
Zhao, Rui et al. (2021). “Mutual Information State Intrinsic Control”. arXiv:2103.08107. url: https://arxiv.org/abs/2103.08107v1 (cit. on p. 51). 
202
BIBLIOGRAPHY 
Zhao, Zixu et al. (2023). “Object-centric multiple object tracking”. IEEE International Conference on Computer Vision. url: https://arxiv.org/abs/2309.00233 (cit. on p. 100). 
Zhou, Jinghao et al. (2022). “iBOT: Image BERT Pre-Training with Online Tokenizer”. International Conference on Learning Representations. url: https://arxiv.org/abs /2111.07832 (cit. on p. 71). 
Zhu, Yi et al. (2020). “Improving Semantic Segmentation via Self-Training”. ArXiv:2004.14960. url: https://arxiv.org/abs/2004.14960 (cit. on pp. 58, 66). 
Ziegler, Adrian and Yuki M. Asano (2022). “Self-Supervised Learning of Object Parts for Semantic Segmentation”. Conference on Computer Vision and Pattern Recognition. url: https://arxiv.org/abs/2204.13101 (cit. on pp. 61, 68, 74, 99). 
Zoran, Daniel et al. (2021). “PARTS: Unsupervised segmentation with slots, attention and independence maximization”. IEEE International Conference on Computer Vision. url: https://ieeexplore.ieee.org/document/9711314 (cit. on p. 78). 
203