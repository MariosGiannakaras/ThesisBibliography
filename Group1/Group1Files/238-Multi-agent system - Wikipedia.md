> Source: https://en.wikipedia.org/wiki/Multi-agent_system

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
1   Concept  1.1   Characteristics  
1.2   Self-organisation and self-direction  
1.3   System paradigms  
1.4   Properties  
2   Research  
3   Frameworks  
4   Applications  
5   See also  
6   References  
7   Further reading  
Multi-agent system
Afrikaans
العربية
Azərbaycanca
Català
Čeština
Deutsch
Ελληνικά
Español
فارسی
Français
한국어
Ido
Bahasa Indonesia
Italiano
Nederlands
日本語
Polski
Português
Română
Русский
Українська
粵語
中文
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
Wikimedia Commons
Wikidata item
From Wikipedia, the free encyclopedia   Built of multiple interacting agents  
Part of a series onMulti-agent systemsMulti-agent simulationIn computational economics
In biology
In social simulation
Modeling software
Agent-oriented programmingAuto-GPT
Botnets
FIPA
Platforms for software agentsJADE
JACK
GORITE
Software agent
 Related  
Distributed artificial intelligence
Multi-agent pathfinding
Multi-agent planning
Multi-agent reinforcement learning
Self-propelled particles
Swarm robotics
v
t
e
Simple reflex agent  Learning agent  
A multi-agent system (MAS or "self-organized system") is a computerized system composed of multiple interacting intelligent agents.[ 1 ][ 2 ] Multi-agent systems can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve.[ 3 ] Intelligence may include methodic, functional, procedural approaches, algorithmicsearch or reinforcement learning.[ 4 ] With advancements in large language models (LLMs), LLM-based multi-agent systems have emerged as a new area of research, enabling more sophisticated interactions and coordination among agents.[ 5 ]
Despite considerable overlap, a multi-agent system is not always the same as an agent-based model (ABM). The goal of an ABM is to search for explanatory insight into the collective behavior of agents (which do not necessarily need to be "intelligent") obeying simple rules, typically in natural systems, rather than in solving specific practical or engineering problems. The terminology of ABM tends to be used more often in the science, and MAS in engineering and technology.[ 6 ] Applications where multi-agent systems research may deliver an appropriate approach include online trading,[ 7 ] disaster response,[ 8 ][ 9 ] target surveillance[ 10 ] and social structure modelling.[ 11 ]
Concept
[edit]  
Multi-agent systems consist of agents and their environment. Typically multi-agent systems research refers to software agents. However, the agents in a multi-agent system could equally well be robots, humans or human teams. A multi-agent system may contain combined human-agent teams. 
Agents can be divided into types spanning simple to complex. Categories include: 
Passive agents[ 12 ] or "agent without goals" (such as obstacle, apple or key in any simple simulation)
Active agents[ 12 ] with simple goals (like birds in flocking, or wolf–sheep in prey-predator model)
Cognitive agents (complex calculations)
Agent environments can be divided into: 
Virtual
Discrete
Continuous
Agent environments can also be organized according to properties such as accessibility (whether it is possible to gather complete information about the environment), determinism (whether an action causes a definite effect), dynamics (how many entities influence the environment in the moment), discreteness (whether the number of possible actions in the environment is finite), episodicity (whether agent actions in certain time periods influence other periods),[ 13 ] and dimensionality (whether spatial characteristics are important factors of the environment and the agent considers space in its decision making).[ 14 ] Agent actions are typically mediated via an appropriate middleware. This middleware offers a first-class design abstraction for multi-agent systems, providing means to govern resource access and agent coordination.[ 15 ]
Characteristics
[edit]  
The agents in a multi-agent system have several important characteristics:[ 16 ]
Autonomy: agents at least partially independent, self-aware, autonomous
Local views: no agent has a full global view, or the system is too complex for an agent to exploit such knowledge
Decentralization: no agent is designated as controlling (or the system is effectively reduced to a monolithic system)[ 17 ]
Self-organisation and self-direction
[edit]  
Multi-agent systems can manifest self-organisation as well as self-direction and other control paradigms and related complex behaviors even when the individual strategies of all their agents are simple.[citation needed] When agents can share knowledge using any agreed language, within the constraints of the system's communication protocol, the approach may lead to a common improvement. Example languages are Knowledge Query Manipulation Language (KQML) or Agent Communication Language (ACL). 
System paradigms
[edit]  
Many MAS are implemented in computer simulations, stepping the system through discrete "time steps". The MAS components communicate typically using a weighted request matrix, e.g. 
 Speed-VERY_IMPORTANT: min=45 mph, Path length-MEDIUM_IMPORTANCE: max=60 expectedMax=40, Max-Weight-UNIMPORTANT Contract Priority-REGULAR 
and a weighted response matrix, e.g. 
 Speed-min:50 but only if weather sunny, Path length:25 for sunny / 46 for rainy Contract Priority-REGULAR note – ambulance will override this priority and you'll have to wait 
A challenge-response-contract scheme is common in MAS systems, where 
First a "Who can?" question is distributed.
Only the relevant components respond: "I can, at this price".
Finally, a contract is set up, usually in several short communication steps between sides,
also considering other components, evolving "contracts" and the restriction sets of the component algorithms. 
Another paradigm commonly used with MAS is the "pheromone", where components leave information for other nearby components. These pheromones may evaporate/concentrate with time, that is their values may decrease (or increase). 
Properties
[edit]  
MAS tend to find the best solution for their problems without intervention. There is high similarity here to physical phenomena, such as energy minimizing, where physical objects tend to reach the lowest energy possible within the physically constrained world. For example: many of the cars entering a metropolis in the morning will be available for leaving that same metropolis in the evening. 
The systems also tend to prevent propagation of faults, self-recover and be fault tolerant, mainly due to the redundancy of components. 
Research
[edit]  
The study of multi-agent systems is "concerned with the development and analysis of sophisticated AI problem-solving and control architectures for both single-agent and multiple-agent systems."[ 18 ] Research topics include: 
agent-oriented software engineering
beliefs, desires, and intentions (BDI)
cooperation and coordination
distributed constraint optimization (DCOPs)
organization
communication
negotiation
distributed problem solving
multi-agent learning[ 19 ]
agent mining
scientific communities (e.g., on biological flocking, language evolution, and economics)[ 20 ][ 21 ]
dependability and fault-tolerance
robotics,[ 22 ] multi-robot systems (MRS), robotic clusters
multi-agent systems also present possible applications in microrobotics,[ 23 ] where the physical interaction between the agents are exploited to perform complex tasks such as manipulation and assembly of passive components.
language model-based multi-agent systems[ 5 ]
Frameworks
[edit]  
Frameworks have emerged that implement common standards (such as the FIPA and OMG MASIF standards).[ 24 ] These frameworks e.g. JADE, save time and aid in the standardization of MAS development.[ 25 ]
Currently though, no standard is actively maintained from FIPA or OMG. Efforts for further development of software agents in industrial context are carried out in IEEE IES technical committee on Industrial Agents.[ 26 ]
With advancements in large language models (LLMs) such as ChatGPT, LLM-based multi-agent frameworks, such as CAMEL,[ 27 ][ 5 ] have emerged as a new paradigm for developing multi-agent applications. Recent work has shown that such debate-oriented systems vary in their orchestration (e.g., discussion paradigms[ 28 ]). The MALLM framework is used to systematically evaluate possible configurations of frameworks.[ 29 ]
Applications
[edit]  
MAS have not only been applied in academic research, but also in industry.[ 30 ] MAS are applied in the real world to graphical applications such as computer games. Agent systems have been used in films.[ 31 ] It is widely advocated for use in networking and mobile technologies, to achieve automatic and dynamic load balancing, high scalability and self-healing networks. They are being used for coordinated defence systems. 
Other applications[ 32 ] include transportation,[ 33 ] logistics,[ 34 ] graphics, manufacturing, power system,[ 35 ]smartgrids,[ 36 ] and the GIS. 
Also, Multi-agent Systems Artificial Intelligence (MAAI) are used for simulating societies, the purpose thereof being helpful in the fields of climate, energy, epidemiology, conflict management, child abuse, ....[ 37 ]
Some organisations working on using multi-agent system models include Center for Modelling Social Systems,[ 38 ] Centre for Research in Social Simulation,[ 39 ] Centre for Policy Modelling, Society for Modelling and Simulation International.[ 37 ]
Vehicular traffic with controlled autonomous vehicles can be modelling as a multi-agent system involving crowd dynamics.[ 40 ]
Hallerbach et al. discussed the application of agent-based approaches for the development and validation of automated driving systems via a digital twin of the vehicle-under-test and microscopic traffic simulation based on independent agents.[ 41 ]Waymo has created a multi-agent simulation environment Carcraft to test algorithms for self-driving cars.[ 42 ][ 43 ] It simulates traffic interactions between human drivers, pedestrians and automated vehicles. People's behavior is imitated by artificial agents based on data of real human behavior. 
See also
[edit]  
Comparison of agent-based modeling software
Agent-based computational economics (ACE)
Artificial brain
Artificial intelligence
Artificial life
Artificial philosophy
AI mayor
Black box
Blackboard system
Complex systems
Discrete event simulation
Distributed artificial intelligence
Emergence
Evolutionary computation
Friendly artificial intelligence
Game theory
Hallucination (artificial intelligence)
Human-based genetic algorithm
Hybrid intelligent system
Knowledge Query and Manipulation Language (KQML)
Microbial intelligence
Multi-agent planning
Multi-agent reinforcement learning
Pattern-oriented modeling
PlatBox Project
Reinforcement learning
Scientific community metaphor
Self-reconfiguring modular robot
Simulated reality
Social simulation
Software agent
Software bot
Swarm intelligence
Swarm robotics
References
[edit]  
^Yoav Shoham, Kevin Leyton-Brown. Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations. Cambridge University Press, 2009. http://www.masfoundations.org/
^H. Pan; M. Zahmatkesh; F. Rekabi-Bana; F. Arvin; J. Hu "T-STAR: Time-Optimal Swarm Trajectory Planning for Quadrotor Unmanned Aerial Vehicles" IEEE Transactions on Intelligent Transportation Systems, 2025.  
^Hu, J.; Turgut, A.; Lennox, B.; Arvin, F., "Robust Formation Coordination of Robot Swarms with Nonlinear Dynamics and Unknown Disturbances: Design and Experiments" IEEE Transactions on Circuits and Systems II: Express Briefs, 2021.  
^Stefano V. Albrecht, Filippos Christianos, Lukas Schäfer. Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. MIT Press, 2024. https://www.marl-book.com/
^ abcLi, Guohao (2023). "Camel: Communicative agents for "mind" exploration of large language model society"(PDF) . Advances in Neural Information Processing Systems. 36:  51991– 52008. arXiv:2303.17760. S2CID257900712.  
^Niazi, Muaz; Hussain, Amir (2011). "Agent-based Computing from Multi-agent Systems to Agent-Based Models: A Visual Survey"(PDF) . Scientometrics. 89 (2):  479– 499. arXiv:1708.05872. doi:10.1007/s11192-011-0468-9. hdl:1893/3378. S2CID17934527.  
^Rogers, Alex; David, E.; Schiff, J.; Jennings, N.R. (2007). "The Effects of Proxy Bidding and Minimum Bid Increments within eBay Auctions". ACM Transactions on the Web. 1 (2): 9–es. CiteSeerX10.1.1.65.4539. doi:10.1145/1255438.1255441. S2CID207163424. Archived from the original on April 2, 2010 . Retrieved  March 18,  2008 .  
^Schurr, Nathan; Marecki, Janusz; Tambe, Milind; Scerri, Paul; Kasinadhuni, Nikhil; Lewis, J.P. (2005). "The Future of Disaster Response: Humans Working with Multiagent Teams using DEFACTO". Archived(PDF)  from the original on June 3, 2013 . Retrieved  January 8,  2024 .  
^Genc, Zulkuf; et al. (2013). "Agent-Based Information Infrastructure for Disaster Management"(PDF) . Intelligent Systems for Crisis Management. Lecture Notes in Geoinformation and Cartography. pp.  349– 355. doi:10.1007/978-3-642-33218-0_26. ISBN978-3-642-33217-3.  
^Hu, Junyan; Bhowmick, Parijat; Lanzon, Alexander (2020). "Distributed Adaptive Time-Varying Group Formation Tracking for Multiagent Systems With Multiple Leaders on Directed Graphs". IEEE Transactions on Control of Network Systems. 7:  140– 150. doi:10.1109/TCNS.2019.2913619. S2CID149609966.  
^Sun, Ron; Naveh, Isaac (June 30, 2004). "Simulating Organizational Decision-Making Using a Cognitively Realistic Agent Model". Journal of Artificial Societies and Social Simulation.  
^ abKubera, Yoann; Mathieu, Philippe; Picault, Sébastien (2010), "Everything can be Agent!"(PDF) , Proceedings of the Ninth International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'2010):  1547– 1548  
^Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle River, New Jersey: Prentice Hall, ISBN0-13-790395-2
^Salamon, Tomas (2011). Design of Agent-Based Models. Repin: Bruckner Publishing. p. 22. ISBN978-80-904661-1-1.  
^Weyns, Danny; Omicini, Amdrea; Odell, James (2007). "Environment as a first-class abstraction in multiagent systems". Autonomous Agents and Multi-Agent Systems. 14 (1):  5– 30. CiteSeerX10.1.1.154.4480. doi:10.1007/s10458-006-0012-0. S2CID13347050.  
^Wooldridge, Michael (2002). An Introduction to MultiAgent Systems. John Wiley & Sons. p. 366. ISBN978-0-471-49691-5.  
^Panait, Liviu; Luke, Sean (2005). "Cooperative Multi-Agent Learning: The State of the Art"(PDF) . Autonomous Agents and Multi-Agent Systems. 11 (3):  387– 434. CiteSeerX10.1.1.307.6671. doi:10.1007/s10458-005-2631-2. S2CID19706.  
^"The Multi-Agent Systems Lab". University of Massachusetts Amherst. Retrieved  October 16,  2009 .  
^Albrecht, Stefano; Stone, Peter (2017), "Multiagent Learning: Foundations and Recent Trends. Tutorial", IJCAI-17 conference(PDF)  
^Cucker, Felipe; Steve Smale (2007). "The Mathematics of Emergence"(PDF) . Japanese Journal of Mathematics. 2:  197– 227. doi:10.1007/s11537-007-0647-x. S2CID2637067. Retrieved  June 9,  2008 .  
^Shen, Jackie (Jianhong) (2008). "Cucker–Smale Flocking under Hierarchical Leadership". SIAM J. Appl. Math. 68 (3):  694– 719. arXiv:q-bio/0610048. doi:10.1137/060673254. S2CID14655317. Retrieved  June 9,  2008 .  
^Ahmed, S.; Karsiti, M.N. (2007), "A testbed for control schemes using multi agent nonholonomic robots", 2007 IEEE International Conference on Electro/Information Technology, p. 459, doi:10.1109/EIT.2007.4374547, ISBN978-1-4244-0940-2, S2CID2734931
^Yang, Lidong; Li, Zhang (2021). "Motion control in magnetic microrobotics: From individual and multiple robots to swarms". Annual Review of Control, Robotics, and Autonomous Systems. 4:  509– 534. doi:10.1146/annurev-control-032720-104318. S2CID228892228.  
^"OMG Document – orbos/97-10-05 (Update of Revised MAF Submission)". www.omg.org. Retrieved  February 19,  2019 .  
^Ahmed, Salman; Karsiti, Mohd N.; Agustiawan, Herman (2007). "A development framework for collaborative robots using feedback control". Retrieved  January 8,  2024 .  
^"IEEE IES Technical Committee on Industrial Agents (TC-IA)". tcia.ieee-ies.org. Retrieved  February 19,  2019 .  
^"CAMEL: Finding the Scaling Law of Agents. The first and the best multi-agent framework". GitHub.  
^Yin, Zhangyue; Sun, Qiushi; Chang, Cheng; Guo, Qipeng; Dai, Junqi; Huang, Xuanjing; Qiu, Xipeng (December 2023). "Exchange‑of‑Thought: Enhancing Large Language Model Capabilities through Cross‑Model Communication". Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. Singapore: Association for Computational Linguistics. pp.  15135– 15153. doi:10.18653/v1/2023.emnlp-main.936.  
^Becker, Jonas; Kaesberg, Lars Benedikt; Bauer, Niklas; Wahle, Jan Philip; Ruas, Terry; Gipp, Bela (November 2025). "MALLM: Multi‑Agent Large Language Models Framework". Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. Suzhou, China: Association for Computational Linguistics. pp.  418– 439. doi:10.18653/v1/2025.emnlp-demos.29.  
^Leitão, Paulo; Karnouskos, Stamatis (March 26, 2015). Industrial agents : emerging applications of software agents in industry. Leitão, Paulo,, Karnouskos, Stamatis. Amsterdam, Netherlands. ISBN978-0128003411. OCLC905853947. {{cite book}} : CS1 maint: location missing publisher (link)  
^"Film showcase". MASSIVE. Retrieved  April 28,  2012 .  
^Leitao, Paulo; Karnouskos, Stamatis; Ribeiro, Luis; Lee, Jay; Strasser, Thomas; Colombo, Armando W. (2016). "Smart Agents in Industrial Cyber–Physical Systems". Proceedings of the IEEE. 104 (5):  1086– 1101. doi:10.1109/JPROC.2016.2521931. hdl:10198/15438. ISSN0018-9219. S2CID579475.  
^Xiao-Feng Xie, S. Smith, G. Barlow. Schedule-driven coordination for real-time traffic network control. International Conference on Automated Planning and Scheduling (ICAPS), São Paulo, Brazil, 2012: 323–331.  
^Máhr, T. S.; Srour, J.; De Weerdt, M.; Zuidwijk, R. (2010). "Can agents measure up? A comparative study of an agent-based and on-line optimization approach for a drayage problem with uncertainty". Transportation Research Part C: Emerging Technologies. 18 (1):  99– 119. Bibcode:2010TRPC...18...99M. CiteSeerX10.1.1.153.770. doi:10.1016/j.trc.2009.04.018.  
^Kazemi, Hamidreza; Liasi, Sahand; Sheikh-El-Eslami, Mohammadkazem (November 2018). "Generation Expansion Planning Considering Investment Dynamic of Market Participants Using Multi-agent System". 2018 Smart Grid Conference (SGC). pp.  1– 6. doi:10.1109/SGC.2018.8777904. ISBN978-1-7281-1138-4. Retrieved  January 8,  2024 .  
^Singh, Vijay; Samuel, Paulson (June 6, 2017). "Distributed Multi -Agent System Based Load Frequency Control for Multi- Area Power System in Smart Grid". IEEE Transactions on Industrial Electronics. 64 (6):  5151– 5160. doi:10.1109/TIE.2017.2668983. Retrieved  January 8,  2024 .  
^ ab"AI can predict your future behaviour with powerful new simulations". New Scientist.  
^"Center for Modeling Social Systems - Norce". NORCE Norwegian Research Centre. Retrieved  April 13,  2025 .  
^"Centre for Research in Social Simulation – A multidisciplinary centre bringing together the social sciences and agent-based modelling to promote and support the use of social simulation in research in the human sciences". Retrieved  April 13,  2025 .  
^Gong, Xiaoqian; Herty, Michael; Piccoli, Benedetto; Visconti, Giuseppe (May 3, 2023). "Crowd Dynamics: Modeling and Control of Multiagent Systems". Annual Review of Control, Robotics, and Autonomous Systems. 6 (1):  261– 282. doi:10.1146/annurev-control-060822-123629. ISSN2573-5144.  
^Hallerbach, S.; Xia, Y.; Eberle, U.; Koester, F. (2018). "Simulation-Based Identification of Critical Scenarios for Cooperative and Automated Vehicles". SAE International Journal of Connected and Automated Vehicles. 1 (2). SAE International: 93. doi:10.4271/2018-01-1066.  
^Madrigal, Story by Alexis C. "Inside Waymo's Secret World for Training Self-Driving Cars". The Atlantic. Retrieved  August 14,  2020 .  
^Connors, J.; Graham, S.; Mailloux, L. (2018). "Cyber Synthetic Modeling for Vehicle-to-Vehicle Applications". In International Conference on Cyber Warfare and Security. Academic Conferences International Limited: 594-XI.  
Further reading
[edit]  
Wooldridge, Michael (2002). An Introduction to MultiAgent Systems. John Wiley & Sons. p. 366. ISBN978-0-471-49691-5.
Shoham, Yoav; Leyton-Brown, Kevin (2008). Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations. Cambridge University Press. p. 496. ISBN978-0-521-89943-7.
Mamadou, Tadiou Koné; Shimazu, A.; Nakajima, T. (August 2000). "The State of the Art in Agent Communication Languages (ACL)". Knowledge and Information Systems. 2 (2):  1– 26.
Hewitt, Carl; Inman, Jeff (November–December 1991). "DAI Betwixt and Between: From "Intelligent Agents" to Open Systems Science"(PDF) . IEEE Transactions on Systems, Man, and Cybernetics. 21 (6):  1409– 1419. doi:10.1109/21.135685. S2CID39080989. Archived from the original(PDF)  on August 31, 2017.
The Journal of Autonomous Agents and Multi-Agent Systems (JAAMAS)
Weiss, Gerhard, ed. (1999). Multiagent Systems, A Modern Approach to Distributed Artificial Intelligence. MIT Press. ISBN978-0-262-23203-6.
Ferber, Jacques (1999). Multi-Agent Systems: An Introduction to Artificial Intelligence. Addison-Wesley. ISBN978-0-201-36048-6.
Weyns, Danny (2010). Architecture-Based Design of Multi-Agent Systems. Springer. ISBN978-3-642-01063-7.
Sun, Ron (2006). Cognition and Multi-Agent Interaction. Cambridge University Press. ISBN978-0-521-83964-8.
Keil, David; Goldin, Dina (2006). Weyns, Danny; Parunak, Van; Michel, Fabien (eds.). Indirect Interaction in Environments for Multiagent Systems. LNCS 3830. Vol. 3830. Springer. pp. 68–87. doi:10.1007/11678809_5. ISBN978-3-540-32614-4.   {{cite book}} :  |journal=  ignored (help)
Whitestein Series in Software Agent Technologies and Autonomic Computing, published by Springer Science+Business Media Group
Salamon, Tomas (2011). Design of Agent-Based Models : Developing Computer Simulations for a Better Understanding of Social Processes. Bruckner Publishing. ISBN978-80-904661-1-1.
Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle River, New Jersey: Prentice Hall, ISBN0-13-790395-2
Fasli, Maria (2007). Agent-technology for E-commerce. John Wiley & Sons. p. 480. ISBN978-0-470-03030-1.
Cao, Longbing, Gorodetsky, Vladimir, Mitkas, Pericles A. (2009). Agent Mining: The Synergy of Agents and Data Mining, IEEE Intelligent Systems, vol. 24, no. 3, 64-72.
v
t
e
Systems scienceSystemtypes  
Art
Biological
Complex
Coupled human–environment
Ecological
Economic
Information
Multi-agent
Nervous
Recommender
Social
Concepts  
Doubling time
Leverage points
Limiting factor
Negative feedback
Positive feedback
Theoretical 
 fields  
Control theory
Cybernetics
Earth system science
Living systems
Sociotechnical system
Systemics
Urban metabolism
World-systems theory
Analysis
Biology
Dynamics
Ecology
Engineering
Neuroscience
Pharmacology
Philosophy
Psychology
Theory (Systems thinking)
ScientistsRussell L. Ackoff
Victor Aladjev
William Ross Ashby
Ruzena Bajcsy
Béla H. Bánáthy
Gregory Bateson
Stafford Beer
Richard E. Bellman
Ludwig von Bertalanffy
Margaret Boden
Alexander Bogdanov
Kenneth E. Boulding
Murray Bowen
Kathleen Carley
Mary Cartwright
C. West Churchman
Manfred Clynes
George Dantzig
Edsger W. Dijkstra
Fred Emery
Heinz von Foerster
Stephanie Forrest
Jay Wright Forrester
Barbara Grosz
Charles A. S. Hall
Mike Jackson
Lydia Kavraki
James J. Kay
Faina M. Kirillova
George Klir
Allenna Leonard
Edward Norton Lorenz
Niklas Luhmann
Humberto Maturana
Margaret Mead
Donella Meadows
Mihajlo D. Mesarovic
James Grier Miller
Radhika Nagpal
Howard T. Odum
Talcott Parsons
Ilya Prigogine
Qian Xuesen
Anatol Rapoport
John Seddon
Peter Senge
Claude Shannon
Katia Sycara
Eric Trist
Francisco Varela
Manuela M. Veloso
Kevin Warwick
Norbert Wiener
Jennifer Wilby
Anthony Wilden
Applications  
Systems theory in anthropology
Systems theory in archaeology
Systems theory in political science
Organizations  
List
Principia Cybernetica
Category
Portal
Commons
v
t
e
Information processingInformation processes information processes by function  
perception
attention
influence
operating
communication
reasoning
learning
storing
decision-making
information processing abstractions  
event processing
sign processesing
signal processing
data processing
stream processing
agent processing
state processing
Information processors natural  
nature as information processing
humans as information processing systems
society as information processing system
mixed  
mixed reality
brain–computer interface
physical computing
human–computer interaction
artificial  
processors and processes
bio-inspired computing
ubiquitous computing
artificial brain and mind uploading
virtual reality
virtual world
Information processing  theories and concepts in biology  
computational and systems biology
genetic informatics and cellular computing
computational neuroscience and neurocomputing
in cognitive psychology  
information processing theory
mind and intelligence
cognitive informatics and neuroinformatics
behavior informatics
in computer science  
neural computation
computation theory
algorithms and information structures
computational circuits
artificial intelligence
in philosophy  
computational theory of mind
philosophy of information
philosophy of artificial intelligence
interdisciplinary  
information theory
decision theory
systems theory
other  
infosphere
inforg
Decoding the Universe
information overload
Authority control databasesInternational
GND
FAST
National
United States
Czech Republic
Other
Yale LUX
Retrieved from "https://en.wikipedia.org/w/index.php?title=Multi-agent_system&oldid=1321619272"  Categories: 
Multi-agent systems
Management theory
Hidden categories: 
CS1 maint: location missing publisher
Articles with short description
Short description matches Wikidata
Use mdy dates from October 2023
All articles with unsourced statements
Articles with unsourced statements from December 2016
Pages using div col with small parameter
CS1 errors: periodical ignored