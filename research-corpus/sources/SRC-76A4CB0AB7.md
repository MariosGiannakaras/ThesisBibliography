Emergence and Resilience in Multi-Agent Reinforcement Learning 
Thomy Phan 
München 2023
Emergence and Resilience in Multi-Agent Reinforcement Learning 
Thomy Phan 
Dissertation an der Fakultät für Mathematik, Informatik und Statistik 
der Ludwig–Maximilians–Universität München 
vorgelegt von Thomy Phan 
Tag der Einreichung: 17. Oktober 2022
1. Gutachter/in: Prof. Dr. Claudia Linnhoff-Popien 2. Gutachter/in: Prof. Dr. Sven Koenig 3. Gutachter/in: Prof. Dr. Long Tran-Thanh 
Tag der Einreichung: 17. Oktober 2022 Tag der Disputation: 19. Juni 2023
Eidesstattliche Versicherung 
(siehe Promotionsordnung vom 12.07.11, § 8, Abs. 2 Pkt. 5) 
Hiermit erkläre ich an Eides statt, dass die Dissertation von mir selbstständig, ohne unerlaubte Beihilfe angefertigt ist. 
Thomy Phan München, 20. Juni 2023
Abstract 
Our world represents an enormous multi-agent system (MAS), consisting of a plethora of agents that make decisions under uncertainty to achieve certain goals. The interaction of agents constantly affects our world in various ways, leading to the emergence of interesting phenomena like life forms and civiliza-tions that can last for many years while withstanding various kinds of distur-bances. Building artificial MAS that are able to adapt and survive similarly to natural MAS is a major goal in artificial intelligence as a wide range of poten-tial real-world applications like autonomous driving, multi-robot warehouses, and cyber-physical production systems can be straightforwardly modeled as MAS. Multi-agent reinforcement learning (MARL) is a promising approach to build such systems which has achieved remarkable progress in recent years. However, state-of-the-art MARL commonly assumes very idealized conditions to optimize performance in best-case scenarios while neglecting further aspects that are relevant to the real world. In this thesis, we address emergence and resilience in MARL which are impor-tant aspects to build artificial MAS that adapt and survive as effectively as natural MAS do. We first focus on emergent cooperation from local interaction of self-interested agents and introduce a peer incentivization approach based on mutual acknowledgments. We then propose to exploit emergent phenomena to further improve coordination in large cooperative MAS via decentralized planning or hierarchical value function factorization. To maintain multi-agent coordination in the presence of partial changes similar to classic distributed systems, we present adversarial methods to improve and evaluate resilience in MARL. Finally, we briefly cover a selection of further topics that are relevant to advance MARL towards real-world applicability. 
VII
VIII
Zusammenfassung 
Unsere Welt stellt ein riesiges Multiagentensystem (MAS) dar, welches aus einer Vielzahl von Agenten besteht, die unter Unsicherheit Entscheidungen treffen müssen, um bestimmte Ziele zu erreichen. Die Interaktion der Agen-ten beeinflusst unsere Welt stets auf unterschiedliche Art und Weise, wodurch interessante emergente Phänomene wie beispielsweise Lebensformen und Zi-vilisationen entstehen, die über viele Jahre Bestand haben und dabei unter-schiedliche Arten von Störungen überwinden können. Die Entwicklung von künstlichen MAS, die ähnlich anpassungs- und überlebensfähig wie natürli-che MAS sind, ist eines der Hauptziele in der künstlichen Intelligenz, da viele potentielle Anwendungen wie zum Beispiel das autonome Fahren, die multi-robotergesteuerte Verwaltung von Lagerhallen oder der Betrieb von cyber-phyischen Produktionssystemen, direkt als MAS formuliert werden können. Multi-Agent Reinforcement Learning (MARL) ist ein vielversprechender An-satz, mit dem in den letzten Jahren bemerkenswerte Fortschritte erzielt wur-den, um solche Systeme zu entwickeln. Allerdings geht der Stand der Forschung aktuell von sehr idealisierten Annahmen aus, um die Effektivität ausschließ-lich für Szenarien im besten Fall zu optimieren. Dabei werden weiterführende Aspekte, die für die echte Welt relevant sind, größtenteils außer Acht gelassen. In dieser Arbeit werden die Aspekte Emergenz und Resilienz in MARL betrach-tet, welche wichtig für die Entwicklung von anpassungs- und überlebensfähi-gen künstlichen MAS sind. Es wird zunächst die Entstehung von emergenter Kooperation durch lokale Interaktion von selbstinteressierten Agenten unter-sucht. Dazu wird ein Ansatz zur Peer-Incentivierung vorgestellt, welcher auf gegenseitiger Anerkennung basiert. Anschließend werden Ansätze zur Nutzung emergenter Phänomene für die Koordinationsverbesserung in großen koopera-tiven MAS präsentiert, die dezentrale Planungsverfahren oder hierarchische Faktorisierung von Evaluationsfunktionen nutzen. Zur Aufrechterhaltung der Multiagentenkoordination bei partiellen Veränderungen, ähnlich wie in klassi-schen verteilten Systemen, werden Methoden des Adversarial Learning vorge-stellt, um die Resilienz in MARL zu verbessern und zu evaluieren. Abschließend wird kurz eine Auswahl von weiteren Themen behandelt, die für die Einsatz-fähigkeit von MARL in der echten Welt relevant sind. 
IX
X
Acknowledgments 
This thesis is the emergent result of an exciting journey involving many won-derful people and comprising more than just the mere sum of encounters. I would like to express my gratitude to my advisor Claudia Linnhoff-Popien for her trust, her guidance, and the freedom I was given to conduct my research. Her experience and enthusiasm as well as the opportunity to work at her chair was very valuable to me to grow scientifically and personally. I thank Sven Koenig for his passionate support and inspiration even beyond my thesis work. I thank Long Tran-Thanh for his interest in my research and support of my work. It was my great honor meeting Sven and Long right before the global lockdown and finally having them both serving on my dissertation committee. I also thank Dieter Kranzlmüller for chairing the committee and Albrecht Schmidt for serving as substitute examiner. During my journey, I was blessed with several amazing mentors. I am particu-larly grateful to Alf Zugenmaier, Joerg Bewersdorf, and Fang Huang for their initial guidance, patience, and wisdom, which greatly influenced my scientific path at an early stage. I am deeply indebted to Lenz Belzner and Thomas Gabor for continually sharing valuable knowledge, experience, and ideas with me – even late after hours. I thank my colleagues Fabian Ritz, André Ebert, Sebastian Feld, Markus Friedrich, Carsten Hahn, Steffen Illium, Marie Kiermeier, Robert Müller, Christoph Roch, Kyrill Schmid, Andreas Sedlmeier, Philipp Altmann, Jonas Nüßlein, Michael Kölle, Maximilian Zorn, and all other members of the Mo-bile and Distributed Systems chair for the great time I had at LMU Munich along with countless inspiring and entertaining conversations, gatherings, and activities that pushed me forward. Finally, I would like to thank my family and friends for their love, patience, and open ears. Having them around gave me the strength and the resilience to pursue my PhD in the best way possible. 
XI
XII
Contents 
1. Introduction 1 1.1. Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1.2. Scope and Research Questions . . . . . . . . . . . . . . . . . . . . 3 1.3. Thesis Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 
2. Background 5 2.1. Multi-Agent Settings . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.2. Dynamic Programming . . . . . . . . . . . . . . . . . . . . . . . . 6 2.3. Multi-Agent Reinforcement Learning . . . . . . . . . . . . . . . . . 7 
3. Emergent Cooperation in General-Sum Games 9 3.1. Learning in Social Dilemmas . . . . . . . . . . . . . . . . . . . . . 9 3.2. Mutual Acknowledgment Exchange . . . . . . . . . . . . . . . . . . 10 
4. Emergence in Cooperative Multi-Agent RL 13 4.1. Distributed Policy Iteration . . . . . . . . . . . . . . . . . . . . . . 14 4.2. Variable Agent-Sub Teams . . . . . . . . . . . . . . . . . . . . . . 16 
5. Resilience in Cooperative Multi-Agent RL 19 5.1. Antagonist-Ratio Training Scheme . . . . . . . . . . . . . . . . . . 20 5.2. Adversarial Value Decomposition . . . . . . . . . . . . . . . . . . . 21 
6. Further Topics 25 6.1. Resource Efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 6.2. State Uncertainty . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 6.3. Non-Cooperative Emergence . . . . . . . . . . . . . . . . . . . . . 27 
7. Conclusion 29 7.1. Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 7.2. Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 
Bibliography 33 
A. Publications 45 A.1. Emergent Cooperation from Mutual Acknowledgment Exchange . . 46 A.2. Distributed Policy Iteration for Scalable Approximation of Coop-
erative Multi-Agent Policies . . . . . . . . . . . . . . . . . . . . . . 47 
XIII
A.3. A Distributed Policy Iteration Scheme for Cooperative Multi-Agent Policy Approximation . . . . . . . . . . . . . . . . . . . . . 48 
A.4. VAST: Value Function Factorization with Variable Agent Sub-Teams 49 A.5. Learning and Testing Resilience in Cooperative Multi-Agent Systems 50 A.6. Resilient Multi-Agent Reinforcement Learning with Adversarial 
Value Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . 51 A.7. Memory Bounded Open-Loop Planning in Large POMDPs using 
Thompson Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . 52 A.8. Adaptive Thompson Sampling Stacks for Memory Bounded Open-
Loop Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53 A.9. Attention-Based Recurrence for Multi-Agent Reinforcement Learn-
ing under Stochastic Partial Observability . . . . . . . . . . . . . . 54 A.10. Emergent Escape-based Flocking Behavior using Multi-Agent Re-
inforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . 69 
XIV
1. Introduction 
Do cities learn? Not the individuals who populate cities, not the institutions they foster, but the cities themselves. I think the answer is yes. 
Emergence Steven Johnson 
1.1. Motivation 
Agents are everywhere. An agent is an autonomous entity which is able to make decisions under uncertainty to achieve a certain goal. Our world con-sists of a plethora of agents, naturally representing an enormous multi-agent system (MAS). Agents may represent MAS themselves, consisting of several sub-agents. All agent decisions, no matter what level, constantly affect our world and our future in various unpredictable ways. Genes represent natural MAS on a micro-level that jointly decide how a living organism is supposed to be built – without actually "knowing" the future be-havior and lifestyle of the resulting organism [12]. Such organisms represent agents on a higher level that can make decisions on their own with uncer-tain future consequences to themselves, their surroundings – and their genes. Humans are highly intelligent specimen of organisms that can make complex decisions to pursue a variety of goals by collaborating or competing with each other regardless of kinship and race [3, 7]. Unlike genes, where failures are ultimately punished by nature with extinc-tion, humans and many other organisms are able to learn from experience and therefore being able to adapt to changing circumstances, e.g., caused by natural disasters, conflicts, or economic crises [4]. Through learning, humans successfully established MAS in form of civilizations and nations that last for centuries while withstanding various kinds of disturbances [23]. We define external disturbances in a MAS as events that naturally occur in the environment regardless of any agent behavior like seismic activities or as-tronomical events [23]. Internal disturbances in a MAS, on the other hand, are directly caused by agent behavior, e.g., in case of defection, manipulation, or failures [79]. Human society exhibits impressively high degrees of resilience against both kinds of disturbances as humankind managed to adapt and sur-vive for thousands of years [3, 12]. 
1
1. Introduction 
Building artificial MAS that are able to solve complex tasks while withstanding disturbances similarly to natural MAS is a major goal in artificial intelligence (AI) [74, 87]. Many potential real-world applications of AI like autonomous driving, multi-robot warehouses, and cyber-physical production systems can be straightforwardly modeled as MAS, consisting of several autonomous com-ponents with individual or common objectives [31, 46, 91]. Reinforcement Learning (RL) provides a general framework to enable agents to learn and adapt from experience [69, 76]. Multi-agent RL (MARL) extends RL to MAS, where all agents are additionally trained to interact with each other [3, 87]. Recent advances in complex board and video games have demonstrated the po-tential of MARL to build artificial MAS under idealized conditions [70, 84, 85]. However, there are several important aspects that need further consideration in order to advance MARL towards real world applicability. In this thesis, we focus on emergence and resilience in MARL, where 
Emergence is a phenomenon that arises from local interaction of multiple agents, representing an effect that comprises more than just the mere sum of parts or interactions [11]. Life in organisms is the emergent re-sult of multiple interacting genes despite genes themselves being actually non-living molecules [12]. Living organisms exhibit interactive behavior on their own to jointly form swarms or civilizations which steadily evolve and adapt as a whole. In these examples, agents are usually only aware of their local interaction but not of potential global consequences. Emer-gence therefore represents some kind of self-organizing macrobehavior without any centralized controller [23]. 
Resilience is the ability of a MAS to withstand external and internal dis-turbances. Animal groups like swarms, flocks, or herds are resilient as the occasional loss or mutation of some individuals does not affect the existence of the whole group [23]. Global economy is typically resilient against crises, since most companies are able to adapt through emer-gency plans and innovation. Even if single companies die out, the global economy itself persists. Classic distributed systems are designed with resilience in mind to ensure constant availability of data and services without failing entirely. Resilience is therefore required to maintain cer-tain emergent properties of the MAS [79]. 
The main contents presented in the thesis are based on the following central hypothesis: 
Hypothesis 1.1 
Emergence and resilience are important aspects that need to be con-sidered in MARL in order to build artificial multi-agent systems that adapt and survive in the real world as effectively as natural multi-agent systems do. 
2
1.2. Scope and Research Questions 
1.2. Scope and Research Questions 
Our goal is to provide methods that explicitly consider emergence and resilience to advance MARL towards building artificial MAS according to our central hypothesis 1.1. We focus on multi-agent cooperation in various settings to build cohesive agent systems that directly benefit our world1 [79]. Unless stated otherwise, we simply use the term agent for artificial agent. The research presented in this thesis is guided by the following questions: 
(Q1) Can cooperation emerge in MARL from local interaction? As self-learning agents become more and more omnipresent in the real world, they will inevitably learn to interact with each other. Non-cooperative game theory and empirical studies have shown that naive RL approaches commonly fail to cooperate, possibly leading to undesirable emergent results. We present a peer incentivization protocol, where agents learn to cooperate from mutual acknowledgments. Our approach is only based on local information and communication therefore offering scalability which is useful in a steadily expanding world of agents. 
(Q2) How to maintain emergent cooperation in MARL? Achieving emergent cooperation under specific circumstances is an important step towards real-world deployment of agents. However, the real world is messy with many unpredictable external factors that could destabilize cooperative situations. In our peer incentivization protocol mentioned in Q1, we introduce a penalization mechanism that enables agents to reciprocate in order to maintain cooperation even under social pressure, where many agents compete for scarce resources. We also demonstrate that the locality of information and communication naturally provides some degree of resilience against random protocol defections and communication failures. 
(Q3) How to consider emergence to improve performance in MARL? Learning typically involves self-reflection about past or potential future behavior. Cooperative MARL often exploits global information like states and joint actions during training to produce coordinated strategies for decentralized decision making. However, emergent phenomena can dynamically occur in various forms and levels which are difficult to deduce from mere states and joint actions therefore limiting performance and scalability. We propose to explicitly consider emergence in form of globally tracked models for prediction and dynamic team structures for hierarchization to overcome these limitations. 
1We point out that emergence and resilience are not necessarily limited to cooperation though. The insights drawn from the thesis can be applied to the opposite as well, where multi-agent defection is desirable, e.g., to uncover weaknesses or flaws in a MAS [23, 82]. 
3
1. Introduction 
(Q4) How to improve resilience in MARL against partial changes? As known from classic distributed systems, partial changes can occur as internal disturbances in MAS, where agents unexpectedly alter their behavior due to updates, manipulation, or flaws. Thus, even fully cooperative MAS should be prepared for partial changes to prevent catastrophic failure. While many works on MARL assume idealistic con-ditions to optimize performance for the best-case, we focus on worst-case scenarios in cooperative MAS and propose antagonist-based methods, where all agents can potentially change their behavior adversarially to expose the target system to less idealistic situations. 
(Q5) How to evaluate resilience in MARL against partial changes? The performance of a MAS is often evaluated in best-case scenarios, where the MAS under test consists of the exact same agents as seen during training therefore not considering the possibility of partial change at all. In addition to our antagonist-based methods mentioned in Q4, we propose testing methods to evaluate resilience of any MAS using dedicated test sets of cooperative and adversarial agents. 
(Q6) What are further relevant topics? Beside emergence and resilience, there are many other topics that are also relevant to building artificial MAS for the real world. We briefly present a selection of work regarding resource efficiency, state uncertainty, and non-cooperative emergence. 
1.3. Thesis Structure 
Chapter 2 provides background knowledge and important terms that are rele-vant for the main body of the thesis. In each main chapter as listed in Table 1.1, we give a brief introduction and present a selection of results but also refer to the corresponding literature and the attached publications for a better overall understanding. 
Table 1.1.: Overview of the main contents of the thesis. Thesis chapter Questions Publications 3. Emergent Cooperation in General-Sum Games Q1, Q2 [55] 4. Emergence in Cooperative Multi-Agent RL Q3 [49, 53, 54] 5. Resilience in Cooperative Multi-Agent RL Q4, Q5 [47, 51] 6. Further Topics Q6 [18, 48, 50, 52] 
Chapter 7 concludes the thesis by connecting the findings to the research ques-tions of Section 1.2 and provides potential directions for future research. All publications that contributed to this thesis are listed in Table 1.1. Further information on the publications is provided in the appendix. 
4
2. Background 
[...] if bacteria can play games, so can people and nations. 
The Evolution of Cooperation Robert Axelrod 
2.1. Multi-Agent Settings 
We formulate MAS as partially observable stochastic game (POSG) M = 〈D,S,A,P ,R,Z,Ω, b0〉, where D = {1, ..., N} is a set of agents i, S is a set of states st at time step t, A = 〈A1, ...,AN〉 = 〈Ai〉i∈D is the set of joint actions at = 〈at,i〉i∈D, P(st+1|st, at) is the state transition probability, R(st, at) = 〈Ri(st, at)〉i∈D = 〈rt,i〉i∈D ∈ R is the joint reward, Z is a set of (local) observations zt,i for each agent i, Ω(st) = zt = 〈zt,i〉i∈D ∈ ZN is the joint observation of state st, and b0 is the probability distribution over initial states s0 ∈ S [13, 19]. Each agent i maintains a (local) history τt,i ∈ (Z ×Ai)t with τt = 〈τt,i〉i∈D being the joint history. A belief state b(st|τt) is a sufficient statistic for joint history τt and defines a probability distribution over states st given τt which can be updated by Bayes’ theorem [25, 41, 61]. A joint policy π = 〈πi〉i∈D with (local) policies πi, defines the joint action probability π(at|τt) = 
∏ i∈D πi(at,i|τt,i). We define π−i as opponent policies 
such that π = 〈πi, π−i〉. For convenience, we use the term opponent of agent i for all other agents j 6= i without strictly assuming a competitive game as suggested in [14]. The return of agent i is defined by Gt,i = 
∑T−1 c=0 γ 
crt+c,i, where T is the horizon and γ ∈ [0, 1] is the discount factor. Local policies πi can be evaluated with a value function defined by V π 
i (τt) = Eπ,b0,P [Gt,i|τt]. Nash equilibria are a solution concept describing joint policies π+ = 〈π+ 
i 〉i∈D, where all π+ 
i maximize their values w.r.t. the opponent policies π+ −i such that 
V π+ 
i = V + i ≥ V 
〈πi,π+ −i〉 
i for all πi. Another concept are optimal joint policies π∗ = 〈π∗i 〉i∈D, where social welfare, i.e., the utilitarian metric or efficiency U = 
∑ i∈DG0,i, is maximized such that Eπ∗,b0,P [U ] ≥ Eπ,b0,P [U ] for all π. 
We assume that all agents only perceive their own observations zt+1,i and rewards rt,i but have no knowledge about the actual state st or their opponents’ actions, observations, or rewards. In addition, we assume all agents to be 
5
2. Background 
rational, i.e., act to maximize their individual values1 V π i [62, 66]. 
POSGs can model various multi-agent scenarios with different purposes and challenges. In this thesis, we focus on the following settings: 
Cooperative Games are situations of pure coordination, where all agents i, j ∈ D share the same global reward rt = rt,i = rt,j thus need to collaborate to achieve a common goal [6, 41, 66]. Tasks that are solv-able in a distributed manner like multi-robot warehouse commissioning or automated manufacturing in smart factories, naturally represent a co-operative game [31, 46]. A Nash equilibrium in a cooperative game is equivalent to an optimal joint policy such that π+ = π∗ [6]. 
Zero-Sum Games are situations of pure competition with N = 2 agents hav-ing opposing rewards rt,1 = −rt,2 [33, 66]. Zero-sum games are often used for learning and testing policy robustness in worst-case scenarios [16, 56, 82]. A Nash equilibrium in a zero-sum game consists of two min-imax optimal policies π+ = 〈π+ 
1 , π + 2 〉 which maximize their respective 
worst-case value defined by V + i = maxπiminπj{V 
〈πi,πj〉 i } [33]. 
General-Sum Games represent the middle ground between pure coordina-tion and competition, where all agents i ∈ D have individual preferences expressed by their respective rewards rt,i. Self-learning systems designed for different tasks form a general-sum game when sharing the same en-vironment [14, 17]. Those systems or agents can learn to benefit from interaction with each other [87]. In general, there can be multiple Nash equilibria with different levels of social welfare, where the true system goal depends on domain-dependent aspects [66]. 
Due to our focus on multi-agent cooperation, we adopt an optimization per-spective to find optimal joint policies2 π∗ in cooperative and general-sum games or minimax optimal policies π+ in zero-sum games respectively [33, 41, 67]. The joint policy π could in principle be realized with a centralized controller which has access to the joint history τt. However, this would limit scalability, privacy, and resilience in practice [41]. We therefore focus on learning local policies πi for decentralized decision making. 
2.2. Dynamic Programming 
Local policies πi can be optimized with dynamic programming (DP) by assum-ing that the opponent policies π−i are fixed and known [40]. Given a model of 
1The values may change, e.g., due to opponent adaptation or peer incentivization. 2Searching for Nash equilibria π+ is a sensible goal for cooperative and zero-sum games but not necessarily desirable for general-sum games because they can be globally inefficient [3, 12, 67]. Furthermore, prior work implies that knowing one’s opponent is often more beneficial than merely striving for a Nash equilibrium [62, 67, 73]. 
6
2.3. Multi-Agent Reinforcement Learning 
the environment M , πi can be evaluated by computing V π i for all τt: 
V π i (τt) = 
∑ 
at∈A π(at|τt) 
∑ 
st∈S b(st|τt) 
( Ri(st, at) + γ 
∑ 
st+1∈S P(st+1|st, at)V π 
i (τt+1) 
) 
(2.1) where τt+1 = 〈τt, at, zt+1〉 is the updated joint history as concatenation of τt, at, and zt+1 = Ω(st+1). πi can be improved with V π 
i by selecting actions that maximize the value for all joint histories τt. The iterative process of alternating policy evaluation and policy improvement is known as policy iteration and provably converges to an optimal local policy given that all other policies π−i are fixed [58, 76]. Value iteration is an alternative DP algorithm to compute the optimal value function V ∗i from a random guess V 0 
i by repeatedly applying the following update for all τt until convergence [19, 40]: 
V k+1 i (τt)← maxat∈A 
   ∑ 
st∈S b(st|τt) 
( Ri(st, at) + γ 
∑ 
st+1∈S P(st+1|st, at)V k 
i (τt+1) 
)  
(2.2) An optimal policy for agent i is then determined by maximizing V ∗i . DP can find optimal joint policies π∗ in cooperative games via policy or value iteration, e.g., by optimizing all local policies alternatingly while keeping the opponent policies fixed or by backward policy construction [19, 40]. However, finding optimal joint policies in POSGs is NEXP-complete hence being intractable for long-horizon games with many states and agents because of the curse of dimensionality w.r.t. the space of belief states, which is |S|-dimensional, as well as exponentially scaling joint action and history spaces [41]. Furthermore, DP requires the explicit distributions of b0 and P , which are infeasible to specify for large state spaces S. Practical algorithms based on DP often use a black box simulator as generative model for Monte Carlo planning, function approximation techniques for RL, or a combination of both [27, 39, 69, 71]. 
2.3. Multi-Agent Reinforcement Learning 
Multi-agent RL (MARL) can approximate optimal policies π∗i from experience which is generated through explorative3 interaction between agent i with a sim-ulated or real environment along with all opponents. Many MARL algorithms approximate the action-value function Qπ 
i instead of V π i [15, 60, 72]: 
3The exploration-exploitation dilemma is a fundamental RL problem to balance between data acquisition and convergence speed, which is out of scope for this thesis. 
7
2. Background 
Qπ i (τt, at) = Eπ,b0,P 
[T−1∑ 
c=0 
γcRi(st+c, at+c) ∣∣∣τt, at 
] (2.3) 
= Eb0 [ Ri(st, at) + γ 
∑ 
st+1∈S 
P(st+1|st, at)V π i (τt+1) 
∣∣∣τt, at ] 
(2.4) 
= ∑ 
st∈S 
b(st|τt) ( Ri(st, at) + γ 
∑ 
st+1∈S 
P(st+1|st, at)V π i (τt+1) 
) (2.5) 
The optimal action-value function Q∗i is defined analogously to V ∗i . In fully observable games, πi can be improved by maximizing Qπ 
i without depending on P therefore enabling model-free control [6, 76]. Most real-world domains are too large for a tabular representation of Qπ 
i , V π i , and πi though. Thus, 
function approximation techniques like deep learning are used to train an ap-proximator Q̂i,ω ≈ Qπ 
i or V̂i,ω ≈ V π i with parameters ω [39, 68, 80]. πi can be 
improved through maximization of Q̂i,ω or actor-critic methods by training an approximator π̂i,θ with parameters θ via gradient ascent on Q̂i,ω or V̂i,ω [77]. For simplicity, we always omit θ, ω and write π̂i, Q̂i, and V̂i instead. We focus on the following MARL paradigms that can be combined and applied to any multi-agent setting from Section 2.1: 
Independent Learning applies single-agent RL techniques to each agent in the game [78]. Functions like Qπ 
i and V π i that require global information, 
i.e., st, τt, or at, are approximated using local information, i.e., τt,i and at,i, per agent i such that Q̂i(τt,i, at,i) ≈ Qπ 
i (τt, at) or V̂i(τt,i) ≈ V π i (τt) re-
spectively. Independent learning offers optimal scalability in all settings due to the locality of information and parallelization of training but ig-nores concurrent adaptation of opponents which causes non-stationarity therefore lacking convergence guarantees [28, 72]. 
Centralized Training for Decentralized Execution (CTDE) assumes training to take place in a laboratory or a simulator hence having access to global information to learn Q̂i(τt, at) ≈ Qπ 
i (τt, at) or V̂i(τt) ≈ V π i (τt). 
Local policy approximators π̂i are trained with Q̂i or V̂i, e.g., via actor-critic methods or value function factorization and can be executed independently afterwards without requiring Q̂i or V̂i anymore [15, 60]. 
Adversarial Learning assumes a zero-sum game to train two agents or agent teams with opposing objectives. Adversarial learning can be realized in different ways like self-play, alternating training, or co-evolution and is used to learn minimax optimal policies π+ to achieve safe and resilient behavior, to validate RL systems, or to build MAS with potentially un-known agents [16, 33, 38, 82]. 
8
3. Emergent Cooperation in General-Sum Games 
Not being nice may look promising at first, but in the long run it can destroy the very environment it needs for its own success. 
The Evolution of Cooperation Robert Axelrod 
3.1. Learning in Social Dilemmas 
What will happen if two or more agents meet each other for the first time? Let us assume that all agents originate from different manufacturers and have individual goals therefore being self-interested. Let us further assume that all agents – regardless of their origins – are unaware of each others’ goals and any global information while being able to adapt to individual experience using independent learning. In autonomous driving, e.g., several self-driving cars need to coordinate their decisions without knowing each others’ destinations or the preferences of each others’ passengers. In a smart home, multiple intelli-gent devices like cleaning robots and smart speakers share the same household while having obviously different purposes and probably never met each other before. Despite initial mutual unawareness, all agents will inevitably learn to interact with each other – either directly or through manipulation of the shared environment [3, 87]. As self-learning systems are becoming more and more omnipresent in the future, such scenarios are becoming the norm, not the exception [14, 17]. We can naturally formulate them as general-sum games. Sharing an environment means competing over its resources which can cause self-interested agents to adopt defective policies that exploit each other and harm social welfare, e.g., self-driving cars causing traffic jams due to greedy navigation or the cleaning robot of a smart home removing all smart speak-ers to keep the household "quiet and clean". Such tension between individual and collective rationality is typically modeled as social dilemma (SD), i.e., a general-sum game, where Nash equilibria π+ are different from optimal joint policies π∗ such that individual rationality would lead to worse outcomes than is possible [3, 12]. Although scenarios of mutual defection are certainly not desirable for real-world applications, non-cooperative game theory and empir-
9
3. Emergent Cooperation in General-Sum Games 
ical studies have shown that naive independent learning agents commonly fail to cooperate in SDs as studied extensively for the prisoner’s dilemma [4, 59]. Fortunately, studies from evolutionary biology and human society have shown that cooperation can still emerge in various ways despite all individuals be-ing (presumably) selfish at the core [4, 7, 12, 81]. Especially human society is seen as an "unusual and interesting special case" of emergent cooperation that is not exclusively based on kinship or race thus providing inspiration for building agents that are able to cooperate out of self-interest [3, 7, 12]. However, merely establishing emergent cooperation is not sufficient to sustain social welfare under social pressure, where many agents compete for scarce resources [30, 45]. Furthermore, cooperative situations could be easily desta-bilized through disturbances [3, 12]. Hence, reciprocity is important to achieve and maintain cooperation in general-sum games by adequately responding to both cooperative and defective opponent behavior [3]. To address the above challenges, we present a scalable peer incentivization approach based on a two-phase communication protocol in the next section. 
3.2. Mutual Acknowledgment Exchange 
Peer incentivization (PI) is an increasingly popular MARL approach, where agents learn to reward each other to achieve emergent cooperation in SDs [35, 64, 83, 90]. Flawless communication is often assumed to exchange re-wards which are simply integrated into the learning process without further feedback. PI is motivated by evolutionary biology and human society, where individuals incentivize each other via supporting actions or side payments in the hope of future compensation [22, 81]. While conceptually interesting, most PI approaches rely on global information like joint actions [90], central market functions [64], or publicly available information [83] which limits scalability and applicability to real-world scenarios. Another common weakness is the lack of opponent penalization for reciprocity, which makes most PI approaches vulnerable to social pressure and disturbances. Therefore, we propose Mutual Acknowledgment Token Exchange (MATE), a PI approach defined by a two-phase communication protocol to mutually ex-change acknowledgment tokens xtoken > 0 to shape rewards for independent learning [55]. After every state transition, each agent i evaluates themonotonic improvement MIi of its situation defined by: 
MIi(r̂t,i) = MI〈τt,i,at,i,rt,i,zt+1,i〉,V̂i(r̂t,i) = r̂t,i + γV̂i(τt+1,i)− V̂i(τt,i) (3.1) 
which is the temporal difference (TD) residual of V̂i w.r.t. to some arbitrary reward r̂t,i estimating the expected long-term improvement of agent i. The two-phase communication protocol of exchanging rewards using acknowl-edgment tokens xi = xtoken > 0 is based on humans thanking and acknowledg-ing each other as illustrated in Figure 3.1. After the acknowledgment token 
10
3.2. Mutual Acknowledgment Exchange 
agent 1 
agent 2 
agent 3 
(a) Request phase 
agent 1 
agent 2 
agent 3 
(b) Response phase 
Figure 3.1.: MATE protocol example. (a) If agent 1 estimates a monotonic improvement MI1(rt,1) ≥ 0 of its situation, it "thanks" its neigh-bor agents 2 and 3 by sending an acknowledgment request x1 > 0 as reward. (b) Agent 2 and 3 check if the request x1 monotoni-cally improves their own situation along with their own respective reward. If so, a positive reward (e.g., y2 = +x1) is sent back as a response. If not, a negative reward (e.g., y3 = −x1) is sent back. Image taken from [55]. 
exchange, the shaped reward r̂MATE t,i for each agent i is computed as follows: 
r̂MATE t,i = rt,i + r̂req + r̂res = rt,i + max{〈xj〉j∈Nt,i}+ min{〈yj〉j∈Nt,i} (3.2) 
where r̂req ∈ {0, xtoken} is the aggregation of all received requests xj and r̂res ∈ {−xtoken, 0, xtoken} is the aggregation of all received responses yj. r̂MATE 
t,i 
replaces the original reward rt,i to stably learn cooperative local policies using any RL algorithm, e.g., actor-critic methods. MATE advances existing PI approaches w.r.t. scalability, stability, and re-silience against external disturbances. MATE is completely decentralized, only relying on local information, i.e., individual experience and rewards exchanged within a local neighborhood Nt,i thus being more scalable than most prior PI approaches. The term r̂res in Equation 3.2 enables penalization which is necessary for reciprocity to maintain social welfare. Due to the locality of infor-mation and communication, MATE naturally exhibits some degree of resilience as local disturbances should not affect the whole MAS. Empirical results from [55] show that MATE achieves and maintains signif-icantly higher levels of cooperation than alternative MARL w.r.t. different metrics in sequential SD domains as shown in Figure 3.2 for Harvest with 12 agents. The modified TD residual of V̂i in Equation 3.1 is shown to be a suit-able monotonic improvement estimator to incentivize emergent cooperation. MATE is able to maintain social welfare in contrast to prior PI approaches, 
11
3. Emergent Cooperation in General-Sum Games 
which become unstable under social pressure and switch to more defective strategies [35, 90]. MATE is also able to maintain its superior cooperation in the presence of random protocol defections and communication failures as shown in Figure 3.2c and 3.2d. 
(a) Harvest Domain (N = 12) 
(b) Original Setting (c) Protocol Defectors (d) Communication Failures 
Figure 3.2.: (a) Harvest domain inspired by [45]. All agents (red circles) need to collect apples (green squares) while avoiding to be tagged and exhaustion of all apples which would prevent regrowth of apples. (b-d) Performance of MATE (as MATE-TD) compared to alterna-tive MARL approaches in different settings of Harvest. (b) Learn-ing progress of MATE and alternative MARL in the standard set-ting. (c) MATE exhibits resilience w.r.t. protocol defectors as social welfare is not harmed. (d) MATE is able to maintain its su-perior cooperation even when communication fails with a chance of up to 80%. Image and results taken from [55] 
12
4. Emergence in Cooperative Multi-Agent RL 
There is great power and creative energy in self-organization [...] but it needs to be channeled toward specific forms for it to blossom into something like intelligence. 
Emergence Steven Johnson 
How do we know that our society is doing well? Or that it is improving after all? In the previous chapter, we studied how cooperation can emerge in general-sum games as a positive effect of local interaction and adaptation. The agents are not "aware" that their individual decisions lead to overall cooperation though [23]. They simply adapt out of self-interest. Many distributed real-world applications like multi-robot warehouses or smart factories represent purely cooperative games, where all agents are part of a team, sharing a common goal [31, 46]. While still being able to make individual decisions, all agents now need to collaborate to not just achieve emergent cooperation but overall coordination, i.e., cooperation in the best way possible. In such cooperative settings, we assume all agents to be trained together in a controlled environment, e.g., in a laboratory or a simulator with access to global information, e.g., states and joint actions, to learn a centralized value function Q̂ or V̂ according to the CTDE paradigm explained in Section 2.3. The resulting policies are deployable for decentralized decision making. Multi-agent credit assignment is a central challenge in cooperative games, since all agents only observe a single global reward. Hence, the deduction of individ-ual contributions is difficult and could lead to uncoordinated policies or "lazy" agents [8, 75, 89]. Another challenge is the limited representational capacity of the centralized value function approximator which becomes a performance bottleneck [5, 49, 53]. Both challenges can lead to the emergence of poor local optima, especially in large MAS with many agents. As state-of-the-art CTDE is often limited to a handful of agents despite ex-ploiting states and joint actions during training, we hypothesize that explicit consideration of emergence is needed to effectively address the above chal-lenges. From a theory of mind perspective, providing higher level knowledge beyond mere states and joint actions could enable agents and CTDE regimes to 
13
4. Emergence in Cooperative Multi-Agent RL 
effectively "read the (emergent) mind" of the whole MAS therefore potentially improving overall coordination in large cooperative games [23, 57]. In the following sections, we present two MARL approaches that explicitly con-sider emergence in form of globally tracked models for prediction or dynamic team structures for hierarchization to overcome the limitations of state-of-the-art CTDE. 
4.1. Distributed Policy Iteration 
According to the dual-system theory, human reasoning is guided by a system 1, which is fast and intuitive, and a system 2, which is slow and (self-)reflective [26]. Hybrid (RL) approaches like AlphaZero or Expert Iteration realize system 1 using statistical methods to learn a fast and generalizing policy π̂ while sys-tem 2 is based on symbolic or model-based methods like planning, representing a stronger but computationally more expensive policy π̃ [2, 69]. The fast pol-icy approximator of π̂ is trained via imitation of the symbolic policy π̃ while π̃ is improved by using the fast policy π̂ as a prior for efficient reasoning. So far, state-of-the-art hybrid approaches mainly focused on single-agent systems or symmetric zero-sum games hence only requiring a single planning process to guide policy learning without any coordination [65]. To learn optimal policies in cooperative games, system 2 can be implemented on different levels. Centralized planning could realize high-level (but not emer-gent) reasoning for optimal coordination in the MAS. However, as noted in Section 2.2, centralized planning of optimal joint policies π∗ is intractable due to exponential computation time. Centralized Monte Carlo planning (MCP) could address the curse of dimensionality regarding (belief) states via statisti-cal sampling and a generative model but also does not scale to large MAS due to exponential branching factors caused by the joint action space A [1, 71]. Decentralized MCP, on the other hand, could realize low-level reasoning in a scalable way but possibly leads to the emergence of uncoordinated behavior. Beside the generative model, decentralized MCP requires knowledge of the opponent policies π−i for coordinated planning [10]. To address this dilemma, we propose Stable Emergent Policies (STEP), a dis-tributed policy iteration scheme, combining centralized learning for policy eval-uation and decentralized MCP for policy improvement [49, 54]. Centralized learning approximates the emergent joint policy π̂ via agent-wise imitation of the decentralized planners π̃ = 〈π̃i〉i∈D and a centralized value function V̂ to evaluate π̃. Decentralized MCP is implemented with agent-wise open-loop Monte Carlo Tree Search (MCTS) and reintegrates π̂ and V̂ to predict emer-gent effects in order to improve efficiency and coordination w.r.t. V̂ . After training, the approximated policies π̂i can be executed in a decentralized way without depending on V̂ , opponent policies π̂−i, or the slower MCTS anymore. The whole STEP training scheme is illustrated in Figure 4.1. Integrating π̂ and V̂ improves decentralized MCP in the following aspects: 
14
4.1. Distributed Policy Iteration 
Value Function 
Planner 1 Planner N 
Policy 1 Policy NJoint Policy 
... 
Full Observability (only required during training) 
Partial Observability (present in production / execution) 
Policy Evaluation 
Policy Improvement 
Policy Learning 
Figure 4.1.: Training architecture of STEP and information flow between the learned policies π̂i,θi (red), the learned value function V̂ω (blue), and the decentralized planners (green). The policy iteration com-ponents (blue and green) within the gray dashed rectangle use global information and are only required during centralized learn-ing, while the learned policies (red) can act under partial observ-ability. Image taken from [49]. 
Prediction of potential emergent effects is generally a non-trivial task due to non-stationarity and opponent uncertainty. Since π̂ is trained via imitation of all decentralized planners π̃, reintegrating π̂ into the MCTS process enables explicit consideration of potential opponent behavior. This effectively addresses the credit assignment problem, allowing for decentralized improvement of individual decisions for the global benefit. 
Infinite horizon planning is enabled by V̂ , which can extend the foresight of MCP to potentially infinite horizons [68, 70]. V̂ is learned from global experience produced by all decentralized planners π̃ thus being able to predict the expected return based on simulated states in each planner. Learning V̂ instead of Q̂ alleviates the performance bottleneck problem, since the input space of V̂ only depends on S without A. 
Open-loop planning with closed-loop priors can significantly reduce the branching factor by merely focusing on individual action sequences. De-spite lacking optimality guarantuees in stochastic domains, open-loop planning can still be effective in large domains with restricted computa-tional resources, often outperforming closed-loop counterparts in practice 
15
4. Emergence in Cooperative Multi-Agent RL 
[29, 44, 86]. We use π̂i as closed-loop prior to weight actions depending on simulated histories in the MCTS selection rule which maximizes: 
UCB1π̂iNdt(τt,i, at,i) = Q(Ndt, at,i) + π̂i(at,i|τt,i)c √ 
2log(nt,i) nat,i 
(4.1) 
where Ndt is a node in the open-loop tree, Q is the tracked open-loop action value, c > 0 is an exploration constant, nt,i is the visitation count of node Ndt, and nat,i is the action count of at,i in node Ndt. π̂i can po-tentially recommend different prior actions for the same action sequences due to explicitly considering observations which would be otherwise ig-nored therefore enabling efficient and effective search. 
We evaluated STEP in a predator-prey and a smart factory domain. Our abla-tion results suggest that integrating π̂ and V̂ can significantly improve overall coordination in cooperative games therefore improving π̂i [49, 54]. Combin-ing decentralized open-loop MCTS with closed-loop priors can be superior to closed-loop MCTS when the computation budget is low or when the branching factor is intractably large [54]. The policy approximations of STEP outper-form model-free CTDE approaches like COMA and QMIX in settings with up to 200 agents. The results indicate that our hybrid approach offers a more effective solution to the multi-agent credit assignment and performance bot-tleneck problem through explicit consideration of emergent effects instead of merely regarding states and joint actions [49]. 
4.2. Variable Agent-Sub Teams 
Hybrid approaches like STEP combine statistical and symbolic methods to produce fast and effective policy approximations. However, MCP requires sufficient simulations per decision hence adding computational costs and being prohibitive if simulations are expensive. Thus, we focus on model-free MARL in the following. The state-of-the-art in model-free MARL is based on value function factoriza-tion (VFF), where the centralized value function Q̂ = Qtot is decomposed into local value functions 〈Qi〉i∈D using a learned VFF operator Ψ. Therefore, VFF directly addresses the multi-agent credit assignment problem via end-to-end learning [60, 72, 75]. However, most VFF approaches are limited to a hand-ful of agents in most domains due to the flat factorization scheme, where Ψ becomes a performance bottleneck with increasing number of agents N . To this end, we propose VFF with variable agent sub-teams (VAST) to address that performance bottleneck problem [53]. Instead of directly factorizing Q̂ for each agent, VAST approximates a factorization using a VFF operator Ψ for K ≤ N disjoint agent sub-teams Dt,k ⊆ D which can be defined in an arbitrary way and vary over time, e.g., to adapt to different situations. The sub-team 
16
4.2. Variable Agent-Sub Teams 
Agent 1 Agent 2 Agent 3 Agent 4 Agent 5 
Figure 4.2.: Our hierarchical factorization scheme based on K = 2 sub-team values QD 
t,k, which are linearly decomposed into local values Qj per sub-team member j ∈ Dt,k ⊆ D. Image reproduced from [53]. 
valuesQD t,k are linearly decomposed for all sub-team members j ∈ Dt,k via value 
decomposition networks (VDN) [75]. VDN offers a simple and flexible way to learn sub-team member values Qj of variable sized sub-teams without adding further complexity through additional parameters. The hierarchization enables Ψ to learn on a more focused and compact input representation. Agents can be assigned to sub-teams by an arbitrary assignment operator X without loosing any guarantuees w.r.t. decentralizability. The hierarchical VFF scheme is illustrated in Figure 4.2. Our empirical results in Figure 4.3 show that a random sub-team assignment XRandom can already be sufficient to outperform flat VFF approaches like QMIX and QTRAN in large-scale domains with up to 800 agents [53]. However, we found that meta optimization of agent sub-teams w.r.t. the return or utilitarian metric U is most effective due to successfully exploiting emergence in form of dynamic team structures. Figure 4.4 shows an example for emergent sub-teams in the Battle domain de-termined by a meta-gradient optimizing assignment operator XMetaGrad. The sub-teams vary depending on the situation, enabling the learning process to adapt accordingly in order to further improve performance compared to alter-native assignments like spatial clustering (XSpatial), which would simply deter-mine sub-teams based on spatial distances regardless of the actual situation. 
17
4. Emergence in Cooperative Multi-Agent RL 
(a) Warehouse[16] (b) Battle[80] (c) GaussianSqueeze[800] 
Figure 4.3.: Average training progress of VAST with sub-team assignment operator X ∈ {XRandom,XFixed,XSpatial,XMetaGrad}, ΨQTRAN, and η = 1 
4 as well as the respective best VFF baselines reported in 
[53]. Results taken from [53]. 
(a) early, XMetaGrad (b) middle, XMetaGrad (c) late, XMetaGrad 
(d) early, XSpatial (e) middle, XSpatial (f) late, XSpatial 
Figure 4.4.: Visualizations of the determined sub-teams of XMetaGrad with η = 1 4 
and XSpatial with k-means clustering using 10 centroids at different stages (early, middle, late) in Battle[80] after training. All learning agents (round circles) of the same sub-team have the same color. Image taken from [53]. 
18
5. Resilience in Cooperative Multi-Agent RL 
Do we assume, in real life [...], that we are playing a zero sum game when we are not? 
The Selfish Gene Richard Dawkins 
What happens if something goes wrong or not the way we expected? In human society, this question often arises when planning activities under uncertainty to prepare for undesirable or unexpected events. In Chapter 3 and 4, we focused on emergent cooperation and coordination via MARL, where we assumed all agents to act exactly according to their learned policies even in the presence of external disturbances. However in the real world, agents themselves can change unexpectedly by altering their policies due to updates, manipulation, or flaws in hardware and software [79]. Such internal disturbances or partial changes can cause catastrophic failures, i.e., mutual defection in general-sum games or degrading performance in cooperative games with potentially severe consequences in industrial and safety-critical domains [82]. Resilience has been considered a main motivation for artificial MAS and is commonly found in natural MAS like animal groups or human society, and in classic distributed systems, which are able to survive various kinds of partial change. Resilient artificial MAS are supposed to withstand partial changes by ensuring "graceful degradation" of performance without failing entirely [41]. However, many works on cooperative MARL commonly assume idealized con-ditions, where all agents only optimize the best-case performance while being evaluated against the exact same agents as seen during training [15, 60, 85]. The possibility of partial change is therefore not considered at all. We argue that even when being trained for a fully cooperative task, a MAS should always be prepared for partial changes and exhibit resilience similar to natural MAS and classic distributed systems to prevent catastrophic failure. Due to the high complexity in MAS, there are many possibilities for agents to deviate from their original policy with potentially negative global impact which cannot be considered exhaustively a priori. We take inspiration from en-gineering of classic distributed systems, which focuses on worst-case scenarios to ensure dependability through resilience, e.g., reliable and secure commu-
19
5. Resilience in Cooperative Multi-Agent RL 
nication or permanent availability of data and services, without exhaustive consideration of partial changes [79]. Thus, we focus on worst-case scenarios in MARL using adversarial learning techniques. In the following sections, we propose two adversarial MARL approaches to improve resilience in cooperative games. We also provide testing methods to evaluate resilience w.r.t. partial changes based on dedicated agent test sets. 
5.1. Antagonist-Ratio Training Scheme 
The goal is to build cooperative MAS which are resilient against partial failure. Our target system represents a cooperative gameMC = M withN agents i ∈ D and a common reward rt = Ri(st, at) for all i ∈ D as defined in Section 2.1 For learning and testing, we reformulate the target system as mixed (cooperative-competitive) game MX with N agents i ∈ DX = Dpro ∪ Dant and Dpro ∩ Dant = ∅. Dpro ⊆ D is a team of protagonists and represents a set of functional agents of the target system MC . Dant is a team of antagonists and represents a set of adversarial agents, i.e., some partial change in the MAS. The protagonists observe the original reward rt,pro = rt of MC , while the an-tagonist reward is defined by rt,ant = −rt,pro. MX represents a zero-sum game between two agent teams Dpro and Dant, where each team consists of internally cooperating agents [34]. We define the antagonist-ratio Rant = |Dant| 
|D| as adversarial fraction in the mixed-game MX . If Rant = 0, then MX reduces to the target system MC . Based on this setting, we propose an Antagonist-Ratio Training Scheme (ARTS) [51]. Since all agents of the target system may be subject to par-tial change, we maintain a pool of N protagonist policies π̂pro = 〈π̂i,pro〉i∈D and a pool of N antagonist policies π̂ant = 〈π̂i,ant〉i∈D to model an adversarial coun-terpart for each agent or protagonist i ∈ D of the target system. We therefore aim to approximate minimax optimal joint policies π̂pro ≈ π+ for various MX 
rather than an optimal joint policy π∗ for the target system MC . Given a fixed Rant, there are theoretically 
( N−1 N ·Rant 
) possible antagonist team 
compositions per protagonist i ∈ D. To avoid exhaustive exposure of all antagonist team compositions to all agents, we train π̂pro and π̂ant on randomly sampled mixed-games MX , where πX is composed of a random selection of protagonist and antagonist policies according to Rant. A centralized value function Q̂(τt, at) ≈ EMX ,πX [QπX (τt, at)] is learned via CTDE based on the protagonist rewards rt,pro. The policies of π̂pro are then updated to maximize Q̂, while the policies of π̂ant are updated to minimize Q̂ according to the minimax principle [33, 66]. Figure 5.1 gives an overview of ARTS. ARTS can also be used to test resilience of MAS by omitting the policy updates. Given some cooperative MAS with joint policy π = π̂pro and an antagonist policy pool π̂ant, e.g., provided by domain experts or a different MARL process, the scheme from Figure 5.1 can be used to evaluate performance w.r.t. different 
20
5.2. Adversarial Value Decomposition 
Episode 1: 
Episode 2: 
Episode T: 
... 
Protagonists Antagonists 
Sample 
with 
Run T mixed-game episodes 
with randomly sampled 
}Train policies or evaluate test results 
Figure 5.1.: Overview of the components and an example process of ARTS with Rant = 0.5 and N = 4. Image reproduced from [51]. 
partial change scenarios depending on Rant. With ARTS, all agents of a target system can be evaluated with opponents or antagonists from different training processes to truly assess the ability of a MAS to withstand partial changes. Testing π with Rant = 0 corresponds to evaluating the best-case performance similarly to most state-of-the-art works on MARL. We evaluated ARTS in a simulated cyber physical production system (CPPS) as shown in Figure 5.2a using DQN(Rant), QMIX(Rant), and QMixMax as QMIX( |D|−1|D| ). The completion rate of produced items is used as performance measure. Our results in Figure 5.3a show that antagonist-based training with Rant > 0 is competitive to idealized MARL w.r.t. best-case performance for ad-equately chosen Rant. Figure 5.3b shows the results of a cross-validation, where protagonists and antagonists from independent QMIX(Rant) training processes with different Rant are evaluated in random mixed-games using ARTS. We can see a tradeoff between resilience and best-case performance, where training with large Rant leads to better resilience against more antagonists but rather poor performance in actually cooperative settings. Training with Rant > 0 always improves resilience compared to idealized cooperative MARL except QMixMax, which focuses on extreme cases, where a single protagonist faces N − 1 antagonists and always performs poorly. However, the antagonists of QMixMax are able to easily uncover flaws in MAS therefore being well suited for testing [51]. 
5.2. Adversarial Value Decomposition 
Adversarial MARL approaches like ARTS often focus on specialized settings, assuming adversaries with a fixed strength defined by a hyperparameter like Rant [32, 51]. The resulting performance and resilience therefore depends on the choice of Rant, which must be either known a priori or extensively tuned. 
21
5. Resilience in Cooperative Multi-Agent RL 
Figure 5.2.: Two CPPS instances with Rant = 1 4 . The white and red cylin-
ders represent protagonists and antagonists respectively. (a, b) CPPS[4] as 4-agent setting with 1 antagonist. (c) CPPS[16] as 16-agent setting with 4 antagonists. Image taken from [47]. 
Having a fixed Rant can lead to inflexible policies, which either perform well in purely cooperative settings or in mixed-games with many antagonists, but rarely in both. Furthermore, Rant may affect the training quality, e.g., if Rant is too large, the sampled mixed-games become too difficult to learn any meaningful protagonist policy as indictated by QMixMax in Figure 5.3. 
To this end, we propose Resilient Adversarial value Decomposition with Antagonist-Ratios (RADAR) to flexibly train protagonists and antagonists with variable Rant hence overcoming the limitations of ARTS [47]. RADAR is a CTDE approach based on the same setting as ARTS, assuming a coopera-tive target system MC , which is trained via random mixed-games MX using protagonist and antagonist policy pools. 
In RADAR, Rant ∈ [0, 1) is iteratively sampled from a uniform distribution during training thus enabling training with mixed-games of varying number of protagonists and antagonists. RADAR uses VDN-based value function factor-ization, where two value functions Q̂pro and Q̂ant are approximated for protag-onists and antagonists respectively: 
22
5.2. Adversarial Value Decomposition 
(a) Learning progress (b) Cross-validation 
Figure 5.3.: (a) Learning progress of 50 runs of DQN and QMIX using ARTS, Minimax, and QMixMax in CPPS[4]. (b) Cross-validation of pro-tagonists and antagonists trained with different antagonist-ratios Rant using QMIX or QMixMax. Results taken from [51]. 
Q̂pro(τt,pro, at,pro) = ∑ 
i∈Dpro 
Q̂i,pro(τt,i, at,i) = Eπ,b0,P [ |Dpro| 
N Gt,pro 
∣∣∣τt, at ] 
(5.1) 
Q̂ant(τt,ant, at,ant) = ∑ 
j∈Dant 
Q̂j,ant(τt,j, at,j) = −Eπ,b0,P [ |Dpro| 
N Gt,pro 
∣∣∣τt, at ] 
(5.2) 
where Gt,pro is the return of protagonist rewards rt,pro and |Dpro| N 
is used to normalize Gt,pro w.r.t. the current number of participating protagonists as the scale of Gt,pro otherwise gives more weight to settings, where Rant is small. Q̂pro and Q̂ant can be approximated via end-to-end learning using backpropa-gation on 〈Q̂i,pro〉i∈Dpro and 〈Q̂j,ant〉j∈Dant respectively [75]. Local policies can be derived from Q̂i,pro and Q̂j,ant using, e.g., multi-armed bandits or actor-critic methods. The striking simplicity of VDN compared to alternative non-linear factorization methods is beneficial when training teams of variable sizes as mentioned in Section 4.2. Many works on MARL simply evaluate the best-case using only the exact same agents as seen during training. Hence, it is unclear if the MAS would still behave as intended if some agents were replaced, e.g., by "newer versions" in case of an update, or by adversarially behaving agents in case of manipulation or flaws. Therefore, in addition to RADAR, we propose an agent-based test scheme to evaluate performance and resilience in MAS in a fair way [47]. Before training the target system, we prepare some test suites Tcooperation and Tfailure,Rant which consist of pretrained protagonist or antagonist agents, e.g., 
23
5. Resilience in Cooperative Multi-Agent RL 
created by domain experts or any kind of adversarial MARL like ARTS or RADAR. During training, the target system can be tested with Tcooperation and Tfailure,Rant and some normalized performance measure g like the average return or some domain specific value to evaluate the following measures: 
Cooperation performance which estimates ETcooperation [g] to assess the abil-ity of a MAS to collaborate with new agents. Note that unlike in the best-case, protagonists from different training processes than the target system are used as π̂ant for testing. 
Worst case performance which estimates minc∈Tcooperation∪(⋃χ Tfailure,χ){g} to assess the resilience of a MAS against a variety of partial changes. 
With Tcooperation and Tfailure,Rant , we can compare the cooperation and worst-case performance of different MARL approaches in a fair way because the trained MAS are evaluated (but not trained) against the same set of test agents. Hence, the agents of a MAS can no longer rely on the assumption of only meeting fellow agents from training during evaluation. We evaluated RADAR in a predator-prey domain and the simulated CPPS shown in Figure 5.2c. The CPPS results are shown in Figure 5.4 and demon-strate the effectiveness of RADAR in terms of cooperation and worst-case performance, where all approaches are evaluated with the same agent-based test suites. Ablation studies show the flexibility and superiority of RADAR compared to variants with fixed Rant and without VDN for adversarial value decomposition [47]. 
(a) cooperation performance (b) worst-case performance 
Figure 5.4.: Cooperation performance and worst-case performance of RADAR and state-of-the-art MARL for CPPS[16]. Results taken from [47]. 
24
6. Further Topics 
The tradeoff between complexity and optimality is very common in real life. 
Modeling Bounded Rationality Ariel Rubinstein 
6.1. Resource Efficiency 
The increasing complexity of potential AI domains often leads to more complex algorithms which require tremendous effort on tuning and execution [24]. Such developments can limit actual progress in the long run due to the physical limits regarding compute and memory, especially in low resource environments. Furthermore, increasing demand for computational and memory resources has potential negative societal impacts, e.g., regarding energy consumption [88]. We focus on model-based decision making in particular, where Monte Carlo planning (MCP) seems promising to solve complex problems via statistical sampling [27, 71, 86]. MCTS represents the current state-of-the-art in MCP, which constructs sparse closed-loop trees over (belief) states and actions for efficient policy search. Despite avoiding exhaustive search, the closed-loop trees can still become arbitrarily large for highly complex domains with large branching factors, e.g., due to large (joint) action spaces. In environments with highly restricted memory resources, MCTS could become either infeasible or perform very poorly – regardless of the provided computation time. As mentioned in Section 4.1, open-loop planning can significantly reduce the branching factor by discarding (belief) state information and merely focusing on action sequences [29, 44, 86]. Especially in low resource environments, open-loop planning seems promising to find good solutions in a much more scalable way than closed-loop planning. Focusing on games with N = 11, we propose memory bounded open-loop MCP algorithms using stacks of Thompson Sam-pling bandits. Each bandit represents a decision rule for a particular time step t regardless of the actual simulated state, observation, or preceding actions, in order to generate and evaluate open-loop plans [48, 50]. These bandits are updated recursively according to the corresponding returns Gt. The stack size 1Such games are known as games against nature or POMDPs, where a single decision making agent faces the environment as "stationary opponent" [43]. 
25
6. Further Topics 
can be either fixed or dynamically adapted, depending on the convergence of bandits. Our stack-based algorithms are highly efficient w.r.t. compute and memory being competitive against tree-based (open- and closed-loop) MCP in domains with large action spaces and significantly outperform tree-based MCP when memory resources are restricted. Our approaches can be used in hybrid meth-ods like STEP from Section 4.1 to enable resource efficient planning supported by emergent policy and value functions. 
6.2. State Uncertainty 
Decentralized partially observable Markov decision processes (Dec-POMDP) are more general variants of cooperative games, where the observation function Ω is stochastic to model noisy sensors [25, 41]. Dec-POMDPs often exhibit high degrees of state uncertainty, which pose a major challenge for decentralized coordination [42]. State-based CTDE tackles Dec-POMDPs by exploiting state information to learn a centralized value function in order to derive coordinated local policies [15, 53, 60]. Due to its empirical effectiveness in the StarCraft Multi-Agent Challenge (SMAC) as the current de facto standard for MARL evaluation [63], state-based CTDE has become very popular and is widely considered an adequate approach to general Dec-POMDPs [15, 36, 37]. However, state-based CTDE is generally insufficient to learn proper value func-tions under state uncertainty, since all agents make decisions on a completely different basis, i.e., individual histories of noisy observations and actions. Fur-thermore, SMAC has very limited state uncertainty due to deterministic obser-vations and low variance in initial states, being insufficient for assessing prac-ticability of MARL. Thus, merely relying on state-based CTDE and SMAC in MARL research can be a pitfall in practice as state uncertainty is largely neglected – despite being an important aspect in Dec-POMDPs. To this end, we propose Attention-based Embeddings of Recurrence In multi-Agent Learning (AERIAL), which replaces the true state with a learned repre-sentation of multi-agent recurrence as illustrated in Figure 6.1 [52]. By lever-aging the memory representations of all agents’ recurrent functions, AERIAL considers more accurate closed-loop information about decentralized agent de-cisions than state-based CTDE to learn proper value functions under state uncertainty [9, 20, 21]. We also introduce MessySMAC which extends SMAC with observation stochas-ticity w.r.t. Ω, where all measured values of observation zt,i are negated with a probability of φ ∈ [0, 1), and initialization stochasticity w.r.t. b0, where K random steps are initially performed before officially starting an episode [52]. MessySMAC represents a more general Dec-POMDP benchmark than SMAC, enabling systematic evaluation under different configurations of state uncer-tainty according to φ and K. Figure 6.2 shows the PCA visualization of joint observations in two SMAC and MessySMAC maps within the first 5 steps of 
26
6.3. Non-Cooperative Emergence 
Agent NAgent 1MLP 
RNN 
MLP 
Transformer 
... 
Figure 6.1.: Illustration of the AERIAL setup. Left: Recurrent agent net-work structure with memory representations ht−1,i and ht,i. Right: Value function factorization via factorization operator Ψ using the joint memory representation ht = 〈ht,i〉i∈D of all agents’ RNNs instead of true states st. All memory representations ht,i are de-tached from the computation graph to avoid additional differenti-ation (indicated by the dashed gray arrows) and passed through a simplified transformer before being used by Ψ for value function factorization. Image taken from [52]. 
1,000 episodes, indicating higher state uncertainty in MessySMAC maps. Our experiments demonstrate that AERIAL is competitive against state-based CTDE in SMAC and superior in MessySMAC, confirming the effectiveness of exploiting multi-agent recurrence instead of true states in centralized training. Considering state uncertainty in MARL is important to avoid emergence of uncoordinated behavior and to improve resilience as the real world is generally messy and only observable through noisy sensors [25, 41, 71]. 
6.3. Non-Cooperative Emergence 
In Chapter 3, we studied how emergent cooperation can be incentivized in general-sum games using local communication. In Chapter 4, we demonstrated how coordination can be improved by exploiting emergent properties in CTDE. In both chapters, the resulting emergent behavior improves social welfare over the course of training. In the real world, not all emergent phenomena im-prove social welfare though. Traffic jams or panic buying are examples of non-cooperative emergence, where individuals act greedily regardless of others leading to worse social welfare than is possible. In our study, we conducted predator-prey simulations of N learning agents representing fishes as prey in a general-sum game along with a shark as preda-tor, which greedily hunts fishes within close vicinity [18]. The goal of all agents 
27
6. Further Topics 
Figure 6.2.: Left: Screenshot of two SMAC maps. Middle: PCA visualization of the joint observations in original SMAC within the first 5 steps of 1,000 episodes using a random policy with K = 0 initial ran-dom steps. Right: Analogous PCA visualization for MessySMAC with K = 10 initial random steps. For visual comparability, the observations are deterministic here. Image taken from [52]. 
is to survive regardless of others which is individually rewarded with +1 for each time step. However, an agent gets penalized with −1000 and removed from the game when being caught by the shark. As expected from nature, the agents learned to form swarms – despite not being explicitly rewarded to do so – effectively distracting the shark, which consequently focused on hunting "outlier" agents instead. At first glance, one might assume the resulting swarm to be an emergent cooperative structure. However, further analysis revealed that swarm forming policies are rather in-efficient w.r.t. the expected agent life time, which is a surprising finding given that agents are actually rewarded for surviving [18]. We found that if all agents simply escaped from the shark independently of each other, their expected life time would increase significantly. However if a swarm emerges, then indepen-dent escaping agents tend to be caught first, causing the swarm to occasionally "sacrifice" some agents by isolating them as bait for the shark. Therefore, the whole swarm can be hypothesized to be an emergent selfish but stable struc-ture which has a long expected life time "as a whole" while its individuals are rather short lived. Extending such analyses to more domains could provide valuable insights to devise better MARL algorithms that consider emergence and resilience. 
28
7. Conclusion 
Fortunately, humans do have foresight and use it to speed up what would otherwise be a blind process of evolution. 
The Evolution of Cooperation Robert Axelrod 
7.1. Summary 
Due to the rapid progress in MARL, artificial agents are going to become more and more omnipresent in our everyday life, influencing our world through their decisions like natural MAS already do [14, 17]. In this thesis, we investigated the explicit consideration of emergence and resilience in MARL and presented methods that overcome common limitations of the state-of-the-art regarding various aspects relevant to the real world. Our work is based on common MAS settings and paradigms as described in Chapter 2. We first studied how cooperation can emerge in general-sum games from local interaction. Agents are able to incentivize each other to adopt more coopera-tive policies via locally exchanged rewards using a two-phase communication protocol. To avoid destabilization of cooperation by social pressure, agents need the ability to reciprocate via adequate responses. The locality of infor-mation and communication naturally offers some degree of resilience against external disturbances like random protocol defections and communication fail-ures, which are common challenges in the real world [79]. While the emergence of cooperation in general-sum games is desirable for po-tential future multi-agent scenarios, many distributed real-world applications can be straightforwardly modeled as cooperative games, where all agents share a common goal and are trainable via CTDE. Agents of a cooperative game need to make individual decisions to not just achieve emergent cooperation but to improve overall coordination. Despite state-of-the-art CTDE commonly using states and joint actions to learn coordinated policies, we hypothesized that emergent phenomena are not sufficiently considered during training therefore limiting performance and scalability. To this end, we proposed MARL ap-proaches that explicitly consider emergence in form of globally tracked models for prediction and dynamic team structures for hierarchization to overcome these limitations. 
29
7. Conclusion 
MAS are supposed to withstand internal disturbances or partial changes, where agents themselves can unexpectedly alter their policies due to updates, manip-ulation, or flaws. Even if the underlying setting is purely cooperative, a MAS should always be prepared for partial changes and exhibit resilience similar to natural MAS and classic distributed systems in order to prevent catastrophic failure. We therefore reformulated originally cooperative games as zero-sum games of agent teams and devised antagonist-based methods, where all agents can potentially change their behavior adversarially, to learn resilient policies. We also proposed testing methods to evaluate resilience w.r.t. partial changes based on dedicated agent test sets. At last, we briefly presented further topics that are also relevant to building artificial MAS. We addressed the problem of resource efficiency, which is im-portant regarding low resource environments and societal impact, by proposing memory bounded open-loop MCP for effective decision making in a computa-tionally and memory efficient way. As state uncertainty is largely neglected in MARL research, we introduced a configurable benchmark for adequate evalu-ation as well as a recurrence-based approach to MARL which implicitly con-siders state uncertainty to advance MARL towards more general settings. We also investigated non-cooperative emergence in form of selfish swarms, where individual agents are occasionally "sacrificed" by the swarm to ensure its sur-vival. A better understanding of such phenomena could be useful to further improve algorithms considering emergence and resilience. Returning to our research questions formulated in Section 1.2, we can now give the following answers: 
(Q1) Can cooperation emerge in MARL from local interaction? In Chapter 3, we proposed a peer incentivization approach based on mu-tual acknowledgments, where self-interested agents are able to exchange rewards and penalties. Agent interaction is completely local due to partial observability and neighborhood communication therefore offering scalability and better applicability to real-world scenarios. Compared to prior methods, which mostly assume global information, our approach is able to achieve superior cooperation, emerging from local interaction. 
(Q2) How to maintain emergent cooperation in MARL? Our mutual ac-knowledgment approach is able to stably maintain cooperation even un-der social pressure due to our penalization mechanism which enables reciprocity. In Chapter 3, we additionally presented a resilience evalua-tion regarding external disturbances like random protocol defections and communication failures. Our approach naturally offers some degree of resilience due to the locality of information and communication as it is able to maintain its superior cooperation in large and partially observable domains in contrast to prior methods that assume global information. 
(Q3) How to consider emergence to improve performance in MARL? State-of-the-art CTDE is currently limited to domains with a handful of 
30
7.1. Summary 
agents despite using global information like states and joint actions to learn coordinated policies. In Chapter 4, we hypothesized that explicit consideration of emergence beyond mere states and joint actions is needed to improve overall coordination in large MAS. We first presented a model-based hybrid approach, integrating learned policy and value functions into decentralized open-loop planning to efficiently predict emergent effects for agent-wise policy learning. We then presented a model-free approach which is able to exploit the emergence of dynamic team structures to form an optimized hierarchy for scalable value function factorization. Both approaches are able to outperform state-of-the-art CTDE approaches that do not explicitly consider emergence, especially in large-scale domains with many agents. 
(Q4) How to improve resilience in MARL against partial changes? Despite resilience being a main motivation for artificial MAS for decades, many works on MARL focus on optimizing the best-case performance under idealized conditions, assuming no partial changes at all. In Chapter 5, we proposed two antagonist-based methods, where all agents can change their behavior, i.e., through random replacement by adversarial counterparts, during training to learn resilient policies. The resulting MAS outperform idealized MARL in the presence of partial changes, indicating that antagonist-based training can produce resilient MAS that are able to survive internal disturbances. 
(Q5) How to evaluate resilience in MARL against partial changes? Since many works on MARL assume idealized conditions, the evaluation of a MAS is typically conducted with the exact same agents as seen during training. In addition to our antagonist-based training methods, we introduce testing methods in Chapter 5 to evaluate resilience w.r.t. partial changes based on dedicated agent test sets. These test sets can be used for cross-validation at the end of training or as pretrained test suites to evaluate the target system during training. By using the same set of test suites or agents to evaluate different MARL approaches, we can ensure a fair comparison w.r.t. cooperation and worst-case performance regarding any kind of partial change. 
(Q6) What are further relevant topics? Beside emergence and resilience, there are many other topics that are also relevant to building artificial MAS. In Chapter 6, we briefly addressed resource efficiency, state uncer-tainty, and non-cooperative emergence. Resource efficiency is important regarding low resource environments and societal impact. Considering state uncertainty is important to avoid emergence of uncoordinated be-havior and to improve resilience in a messy world that is only observable through noisy sensors. Studying the emergence of selfish structures in large MAS like swarms could provide a starting point for devising better algorithms considering emergence and resilience. 
31
7. Conclusion 
Based on the findings of our work and the provided answers to the research questions, we conclude that the explicit consideration of emergence and re-silience in MARL is important to build artificial MAS that are able to solve complex tasks while withstanding disturbances thus confirming our central hy-pothesis 1.1. As our world is steadily expanding towards more artificial agents and MAS that coexist with natural MAS, considering emergence and resilience is going to become an increasingly important task. 
7.2. Outlook 
In this thesis, we assumed all agents to be purely rational. In the real world, where AI systems are supposed to coexist with humans and other living organ-isms, pure rationality cannot always be assumed (from an artificial agent’s per-spective) though [62]. Modeling non-rational or bounded rational agents can help MARL to better align with human behavior and preferences to improve safety, trustworthiness, and acceptance in wide areas. Assuming bounded ra-tionality in agents could also improve resilient MARL, where disturbances can occur due to irrational actions, e.g., human intervention or mistakes, without any adversarial intention. Social abstraction may be useful to reduce complexity in large MAS with many agents. In Section 3.2 and 4.2, we found that locality and optimized group-ing of agents can improve performance and resilience in MAS. However, we only assumed a single level of abstraction, where agents are merely part of some sub-team or neighborhood without further structure or hierarchization. In real life, humans and animals can have multiple levels of abstractions to classify others, e.g., as close relatives, friends, rivals, or completely unrelated individuals. These abstractions enable efficient prioritization of actions with-out needing to know each opponent in full detail. Social abstraction in MARL could improve cooperation and resilience in large MAS by integrating emer-gent social structures, e.g., to cooperate based on social relationships or to adversarially attack important relationships in order to evaluate resilience. As mentioned in Section 6.1, the complexity of algorithms w.r.t. hyperparam-eters and mechanisms tends to increase as AI advances towards more complex domains. Increasing complexity can be prohibitive for actual progress because more effort is required for implementation, execution, tuning, and understand-ing, which has potential negative societal impacts. Therefore, addressing com-plexity with simplicity is a more sensible goal than vice versa. In our research, we put some effort in introducing rather simple methods with very few addi-tional hyperparameters that are able to overcome limitations of more complex state-of-the-art methods. However, future work should actually aim to reduce the number of hyperparameters instead of introducing new ones [24]. 
32
Bibliography 
[1] Christopher Amato and Frans Oliehoek. "Scalable Planning and Learn-ing for Multiagent POMDPs". Proceedings of the AAAI Conference on Artificial Intelligence, 29(1), February 2015. doi:https://doi.org/10. 1609/aaai.v29i1.9439. 
[2] Thomas Anthony, Zheng Tian, and David Barber. "Thinking Fast and Slow with Deep Learning and Tree Search". In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 30. Curran Associates, Inc., 2017. doi:https://dl.acm.org/doi/abs/10. 5555/3295222.3295288. 
[3] Robert Axelrod. "The Evolution Of Cooperation". Basic Books, 1984. doi:https://doi.org/10.1007/978-3-319-16999-6_1220-1. 
[4] Robert Axelrod and William D. Hamilton. "The Evolution of Coopera-tion". Science, 211(4489):1390–1396, 1981. doi:https://doi.org/10. 1126/science.7466396. 
[5] Wendelin Boehmer, Vitaly Kurin, and Shimon Whiteson. "Deep Coordi-nation Graphs". In Hal Daumé III and Aarti Singh, editors, Proceedings of the 37th International Conference on Machine Learning, volume 119 of Proceedings of Machine Learning Research, pages 980–991. PMLR, 13– 18 July 2020. doi:https://dl.acm.org/doi/abs/10.5555/3524938. 3525030. 
[6] Craig Boutilier. "Planning, Learning and Coordination in Multiagent Decision Processes". In Proceedings of the 6th Conference on Theo-retical Aspects of Rationality and Knowledge, TARK ’96, pages 195– 210, San Francisco, CA, USA, 1996. Morgan Kaufmann Publishers Inc. doi:https://dl.acm.org/doi/10.5555/1029693.1029710. 
[7] Robert Boyd and Peter J. Richerson. "The Evolution of Indirect Reci-procity". Social networks, 11(3):213–236, 1989. doi:https://doi.org/ 10.1016/0378-8733(89)90003-8. 
[8] Yu-Han Chang, Tracey Ho, and Leslie P Kaelbling. "All Learning is Local: Multi-Agent Learning in Global Reward Games". In Advances in Neural Information Processing Systems, pages 807–814, 2004. doi: https://dl.acm.org/doi/10.5555/2981345.2981446. 
33
Bibliography 
[9] Kyunghyun Cho, Bart van Merriënboer, Dzmitry Bahdanau, and Yoshua Bengio. "On the Properties of Neural Machine Translation: Encoder-Decoder Approaches". In Proceedings of SSST-8, 8th Workshop on Syntax, Semantics and Structure in Statistical Translation, pages 103–111, 2014. 
[10] Daniel Claes, Frans Oliehoek, Hendrik Baier, and Karl Tuyls. "Decen-tralised Online Planning for Multi-Robot Warehouse Commissioning". In Proceedings of the 16th Conference on Autonomous Agents and Multi-Agent Systems, AAMAS ’17, pages 492–500. International Foundation for Autonomous Agents and Multiagent Systems, 2017. doi:https: //dl.acm.org/doi/abs/10.5555/3091125.3091198. 
[11] S. Marc Cohen and C. D. C. Reeve. "Aristotle’s Metaphysics". In Ed-ward N. Zalta, editor, The Stanford Encyclopedia of Philosophy. Meta-physics Research Lab, Stanford University, Winter 2021 edition, 2021. 
[12] R. Dawkins. "The Selfish Gene: 40th Anniversary Edition". Oxford Landmark Science. OUP Oxford, 2016. 
[13] Rosemary Emery-Montemerlo, Geoff Gordon, Jeff Schneider, and Sebas-tian Thrun. "Approximate Solutions for Partially Observable Stochas-tic Games with Common Payoffs". AAMAS ’04, pages 136–143, USA, 2004. IEEE Computer Society. doi:https://dl.acm.org/doi/10.5555/ 1018409.1018741. 
[14] Jakob Foerster, Richard Y. Chen, Maruan Al-Shedivat, ShimonWhiteson, Pieter Abbeel, and Igor Mordatch. "Learning with Opponent-Learning Awareness". In Proceedings of the 17th International Conference on Au-tonomous Agents and Multiagent Systems, AAMAS ’18, pages 122–130. International Foundation for Autonomous Agents and Multiagent Sys-tems, 2018. doi:https://dl.acm.org/doi/10.5555/3237383.3237408. 
[15] Jakob Foerster, Gregory Farquhar, Triantafyllos Afouras, Nantas Nardelli, and Shimon Whiteson. "Counterfactual Multi-Agent Policy Gradients". Proceedings of the AAAI Conference on Artificial Intelligence, 32(1), 2018. doi:https://doi.org/10.1609/aaai.v32i1.11794. 
[16] Thomas Gabor, Andreas Sedlmeier, Thomy Phan, Fabian Ritz, Marie Kiermeier, Lenz Belzner, Bernhard Kempter, Cornel Klein, Horst Sauer, Reiner Schmid, Jan Wieghardt, Marc Zeller, and Claudia Linnhoff-Popien. "The Scenario Coevolution Paradigm: Adaptive Quality Assur-ance for Adaptive Systems". International Journal on Software Tools for Technology Transfer, 22(4):457–476, 2020. doi:https://doi.org/10. 1007/s10009-020-00560-5. 
[17] Balint Gucsi, Danesh S. Tarapore, William Yeoh, Christopher Amato, and Long Tran-Thanh. "To Ask or Not to Ask: A User Annoy-ance Aware Preference Elicitation Framework for Social Robots". In 
34
Bibliography 
2020 IEEE/RSJ International Conference on Intelligent Robots and Sys-tems (IROS), pages 7935–7940, 2020. doi:https://doi.org/10.1109/ IROS45743.2020.9341607. 
[18] Carsten Hahn, Thomy Phan, Thomas Gabor, Lenz Belzner, and Clau-dia Linnhoff-Popien. "Emergent Escape-Based Flocking Behavior us-ing Multi-Agent Reinforcement Learning". In The 2021 Conference on Artificial Life, ALIFE 2021, pages 598–605, July 2019. doi:https: //doi.org/10.1162/isal_a_00226. 
[19] Eric A. Hansen, Daniel S. Bernstein, and Shlomo Zilberstein. "Dynamic Programming for Partially Observable Stochastic Games". In Proceed-ings of the 19th National Conference on Artifical Intelligence, AAAI’04, pages 709–715. AAAI Press, 2004. doi:https://dl.acm.org/doi/abs/ 10.5555/1597148.1597262. 
[20] Sepp Hochreiter and Jürgen Schmidhuber. "Long Short-Term Memory". Neural Computation, 9(8):1735–1780, 1997. doi:https://doi.org/10. 1162/neco.1997.9.8.1735. 
[21] Hengyuan Hu and Jakob N Foerster. "Simplified Action Decoder for Deep Multi-Agent Reinforcement Learning". In International Conference on Learning Representations, 2019. 
[22] Matthew O. Jackson and Simon Wilkie. "Endogenous Games and Mecha-nisms: Side Payments Among Players". The Review of Economic Studies, 72(2):543–566, 04 2005. doi:https://doi.org/10.1111/j.1467-937X. 2005.00342.x. 
[23] Steven Johnson. "Emergence: The Connected Lives of Ants, Brains, Cities, and Software". Scribner, 2002. 
[24] Scott Jordan, Yash Chandak, Daniel Cohen, Mengxue Zhang, and Philip Thomas. "Evaluating the Performance of Reinforcement Learning Algo-rithms". In Hal Daumé III and Aarti Singh, editors, Proceedings of the 37th International Conference on Machine Learning, volume 119 of Pro-ceedings of Machine Learning Research, pages 4962–4973. PMLR, 2020. doi:https://dl.acm.org/doi/abs/10.5555/3524938.3525399. 
[25] Leslie Pack Kaelbling, Michael L Littman, and Anthony R. Cassandra. "Planning and Acting in Partially Observable Stochastic Domains". Ar-tificial intelligence, 101(1-2):99–134, 1998. doi:https://doi.org/10. 1016/S0004-3702(98)00023-X. 
[26] Daniel Kahneman. "Thinking, Fast and Slow". Farrar, Straus and Giroux, New York, 2011. doi:https://doi.org/10.1007/s00362-013-0533-y. 
35
Bibliography 
[27] Levente Kocsis and Csaba Szepesvári. "Bandit Based Monte-Carlo Plan-ning". In European Conference on Machine Learning, pages 282–293. Springer, 2006. doi:https://doi.org/10.1007/11871842_29. 
[28] Guillaume J. Laurent, Laëtitia Matignon, and Le Fort-Piat. "The World of Independent Learners is Not Markovian". International Journal of Knowledge-based and Intelligent Engineering Systems, 15(1):55–64, 2011. doi:https://dl.acm.org/doi/10.5555/1971886.1971887. 
[29] Erwan Lecarpentier, Guillaume Infantes, Charles Lesire, and Emmanuel Rachelson. "Open Loop Execution of Tree-Search Algorithms". In Pro-ceedings of the 27th International Joint Conference on Artificial Intel-ligence, pages 2362–2368. IJCAI Organization, July 2018. doi:https: //doi.org/10.24963/ijcai.2018/327. 
[30] Joel Z. Leibo, Vinicius Zambaldi, Marc Lanctot, Janusz Marecki, and Thore Graepel. "Multi-Agent Reinforcement Learning in Sequential So-cial Dilemmas". In Proceedings of the 16th Conference on Autonomous Agents and Multiagent Systems, AAMAS ’17, pages 464–473. Interna-tional Foundation for Autonomous Agents and Multiagent Systems, 2017. doi:https://dl.acm.org/doi/10.5555/3091125.3091194. 
[31] Jiaoyang Li, Andrew Tinka, Scott Kiesel, JosephW. Durham, T. K. Satish Kumar, and Sven Koenig. "Lifelong Multi-Agent Path Finding in Large-Scale Warehouses". Proceedings of the AAAI Conference on Artificial Intelligence, 35(13):11272–11281, May 2021. doi:https://doi.org/10. 1609/aaai.v35i13.17344. 
[32] Shihui Li, Yi Wu, Xinyue Cui, Honghua Dong, Fei Fang, and Stuart Russell. "Robust Multi-Agent Reinforcement Learning via Minimax Deep Deterministic Policy Gradient". In Proceedings of the AAAI Conference on Artificial Intelligence, volume 33, pages 4213–4220, 2019. doi:https: //doi.org/10.1609/aaai.v33i01.33014213. 
[33] Michael L. Littman. "Markov Games as a Framework for Multi-Agent Reinforcement Learning". In William W. Cohen and Haym Hirsh, edi-tors, Machine Learning Proceedings 1994, pages 157–163. Morgan Kauf-mann, San Francisco (CA), 1994. doi:https://doi.org/10.1016/ B978-1-55860-335-6.50027-1. 
[34] Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch. "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments". In Advances in Neural Information Processing Systems, pages 6379–6390, 2017. doi:https://dl.acm.org/doi/abs/10.5555/ 3295222.3295385. 
36
Bibliography 
[35] Andrei Lupu and Doina Precup. "Gifting in Multi-Agent Reinforce-ment Learning". In Proceedings of the 19th International Conference on Autonomous Agents and Multiagent Systems, pages 789–797, 2020. doi:https://dl.acm.org/doi/abs/10.5555/3398761.3398855. 
[36] Xueguang Lyu, Andrea Baisero, Yuchen Xiao, and Christopher Amato. "A Deeper Understanding of State-Based Critics in Multi-Agent Rein-forcement Learning". Proceedings of the AAAI Conference on Artifi-cial Intelligence, 36(9):9396–9404, Jun. 2022. doi:https://doi.org/10. 1609/aaai.v36i9.21171. 
[37] Xueguang Lyu, Yuchen Xiao, Brett Daley, and Christopher Amato. "Con-trasting Centralized and Decentralized Critics in Multi-Agent Reinforce-ment Learning". In Proceedings of the 20th International Conference on Autonomous Agents and Multiagent Systems, pages 844–852, 2021. doi:https://dl.acm.org/doi/abs/10.5555/3463952.3464053. 
[38] Alexander Mey and Frans A. Oliehoek. "Environment Shift Games: Are Multiple Agents the Solution, and not the Problem to Non-Stationarity?". AAMAS ’21, pages 23–27. International Foundation for Autonomous Agents and Multiagent Systems, 2021. doi:https://dl.acm.org/doi/ 10.5555/3463952.3463958. 
[39] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. "Human-Level Control through Deep Reinforcement Learning". Nature, 518(7540):529–533, 2015. doi:https: //doi.org/10.1038/nature14236. 
[40] Ranjit Nair, Milind Tambe, Makoto Yokoo, David Pynadath, and Stacy Marsella. "Taming Decentralized POMDPs: Towards Efficient Policy Computation for Multiagent Settings". In Proceedings of the 18th In-ternational Joint Conference on Artificial Intelligence, IJCAI’03, pages 705–711, San Francisco, CA, USA, 2003. Morgan Kaufmann Publishers Inc. doi:https://dl.acm.org/doi/abs/10.5555/1630659.1630762. 
[41] Frans A. Oliehoek and Christopher Amato. "A Concise Introduction to Decentralized POMDPs". Springer, 2016. doi:https://doi.org/10. 1007/978-3-319-28929-8. 
[42] Frans A Oliehoek, Matthijs TJ Spaan, and Nikos Vlassis. "Optimal and Approximate Q-Value Functions for Decentralized POMDPs". Journal of Artificial Intelligence Research, 32:289–353, 2008. doi:https://doi. org/10.1613/jair.2447. 
37
Bibliography 
[43] Christos H. Papadimitriou. "Games against Nature". Journal of Com-puter and System Sciences, 31(2):288–301, 1985. doi:https://doi.org/ 10.1016/0022-0000(85)90045-5. 
[44] Diego Perez Liebana, Jens Dieskau, Martin Hunermund, Sanaz Mostaghim, and Simon Lucas. "Open Loop Search for General Video Game Playing". In Proceedings of the 2015 Annual Conference on Ge-netic and Evolutionary Computation, pages 337–344. ACM, 2015. doi: https://dl.acm.org/doi/10.1145/2739480.2754811. 
[45] Julien Perolat, Joel Z. Leibo, Vinicius Zambaldi, Charles Beattie, Karl Tuyls, and Thore Graepel. "A Multi-Agent Reinforcement Learning Model of Common-Pool Resource Appropriation". In Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS’17, pages 3646–3655, Red Hook, NY, USA, 2017. Curran Associates Inc. doi:https://dl.acm.org/doi/abs/10.5555/3294996.3295122. 
[46] Thomy Phan, Lenz Belzner, Thomas Gabor, and Kyrill Schmid. "Leverag-ing Statistical Multi-Agent Online Planning with Emergent Value Func-tion Approximation". In Proceedings of the 17th International Confer-ence on Autonomous Agents and MultiAgent Systems, AAMAS ’18, pages 730–738. International Foundation for Autonomous Agents and Multia-gent Systems, 2018. doi:https://dl.acm.org/doi/10.5555/3237383. 3237491. 
[47] Thomy Phan, Lenz Belzner, Thomas Gabor, Andreas Sedlmeier, Fabian Ritz, and Claudia Linnhoff-Popien. "Resilient Multi-Agent Reinforce-ment Learning with Adversarial Value Decomposition". Proceedings of the AAAI Conference on Artificial Intelligence, 35(13):11308–11316, May 2021. doi:https://doi.org/10.1609/aaai.v35i13.17348. 
[48] Thomy Phan, Lenz Belzner, Marie Kiermeier, Markus Friedrich, Kyrill Schmid, and Claudia Linnhoff-Popien. "Memory Bounded Open-Loop Planning in Large POMDPs using Thompson Sampling". Proceedings of the AAAI Conference on Artificial Intelligence, 33(01):7941–7948, July 2019. doi:https://doi.org/10.1609/aaai.v33i01.33017941. 
[49] Thomy Phan, Lenz Belzner, Kyrill Schmid, Thomas Gabor, Fabian Ritz, Sebastian Feld, and Claudia Linnhoff-Popien. "A Distributed Policy It-eration Scheme for Cooperative Multi-Agent Policy Approximation". In 12th Adaptive and Learning Agents Workshop, ALA ’20, 2020. 
[50] Thomy Phan, Thomas Gabor, Robert Müller, Christoph Roch, and Clau-dia Linnhoff-Popien. "Adaptive Thompson Sampling Stacks for Memory Bounded Open-Loop Planning". In Proceedings of the 28th International Joint Conference on Artificial Intelligence, IJCAI-19, pages 5607–5613. 
38
Bibliography 
International Joint Conferences on Artificial Intelligence Organization, July 2019. doi:https://doi.org/10.24963/ijcai.2019/778. 
[51] Thomy Phan, Thomas Gabor, Andreas Sedlmeier, Fabian Ritz, Bernhard Kempter, Cornel Klein, Horst Sauer, Reiner Schmid, Jan Wieghardt, Marc Zeller, and Claudia Linnhoff-Popien. "Learning and Testing Re-silience in Cooperative Multi-Agent Systems". In Proceedings of the 19th International Conference on Autonomous Agents and MultiAgent Sys-tems, AAMAS ’20, pages 1055–1063. International Foundation for Au-tonomous Agents and Multiagent Systems, 2020. doi:https://dl.acm. org/doi/10.5555/3398761.3398884. 
[52] Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning. PMLR, 2023. To appear. 
[53] Thomy Phan, Fabian Ritz, Lenz Belzner, Philipp Altmann, Thomas Ga-bor, and Claudia Linnhoff-Popien. "VAST: Value Function Factoriza-tion with Variable Agent Sub-Teams". In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, Advances in Neural Information Processing Systems, volume 34, pages 24018–24032. Curran Associates, Inc., 2021. 
[54] Thomy Phan, Kyrill Schmid, Lenz Belzner, Thomas Gabor, Sebastian Feld, and Claudia Linnhoff-Popien. "Distributed Policy Iteration for Scal-able Approximation of Cooperative Multi-Agent Policies". In Proceedings of the 18th International Conference on Autonomous Agents and Mul-tiAgent Systems, AAMAS ’19, pages 2162–2164. International Founda-tion for Autonomous Agents and Multiagent Systems, 2019. doi:https: //dl.acm.org/doi/10.5555/3306127.3332044. 
[55] Thomy Phan, Felix Sommer, Philipp Altmann, Fabian Ritz, Lenz Belzner, and Claudia Linnhoff-Popien. "Emergent Cooperation from Mutual Acknowledgment Exchange". In Proceedings of the 21st International Conference on Autonomous Agents and MultiAgent Systems, AAMAS ’22, pages 1047–1055. International Foundation for Autonomous Agents and Multiagent Systems, 2022. doi:https://dl.acm.org/doi/10.5555/ 3535850.3535967. 
[56] Lerrel Pinto, James Davidson, Rahul Sukthankar, and Abhinav Gupta. "Robust Adversarial Reinforcement Learning". In Doina Precup and Yee Whye Teh, editors, Proceedings of the 34th International Confer-ence on Machine Learning, volume 70 of Proceedings of Machine Learn-
39
Bibliography 
ing Research, pages 2817–2826. PMLR, 06–11 August 2017. doi:https: //dl.acm.org/doi/10.5555/3305890.3305972. 
[57] David Premack and Guy Woodruff. "Does the Chimpanzee Have a Theory of Mind?". Behavioral and brain sciences, 1(4):515–526, 1978. doi:https://doi.org/10.1017/S0140525X00076512. 
[58] Martin L. Puterman. "Markov Decision Processes: Discrete Stochastic Dynamic Programming". Wiley Series in Probability and Statistics. Wiley, 2014. doi:https://dx.doi.org/10.1002/9780470316887. 
[59] Anatol Rapoport. "Prisoner’s Dilemma — Recollections and Observa-tions". In Game Theory as a Theory of a Conflict Resolution, pages 17–34. Springer, 1974. doi:https://doi.org/10.1007/978-94-010-2161-6_ 2. 
[60] Tabish Rashid, Mikayel Samvelyan, Christian Schroeder de Witt, Gregory Farquhar, Jakob Foerster, and Shimon Whiteson. "QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learn-ing". In Jennifer Dy and Andreas Krause, editors, Proceedings of the 35th International Conference on Machine Learning, volume 80 of Proceedings of Machine Learning Research, pages 4295–4304. PMLR, 2018. 
[61] Stéphane Ross, Joelle Pineau, Sébastien Paquet, and Brahim Chaib-Draa. "Online Planning Algorithms for POMDPs". Journal of Artificial In-telligence Research, 32:663–704, 2008. doi:https://doi.org/10.1613/ jair.2567. 
[62] Ariel Rubinstein. "Modeling Bounded Rationality". The MIT Press, 1998. doi:https://doi.org/10.1023/A:1008058417088. 
[63] Mikayel Samvelyan, Tabish Rashid, Christian Schroeder de Witt, Gregory Farquhar, Nantas Nardelli, Tim GJ Rudner, Chia-Man Hung, Philip HS Torr, Jakob Foerster, and Shimon Whiteson. "The StarCraft Multi-Agent Challenge". In Proceedings of the 18th International Conference on Autonomous Agents and Multiagent Systems, AAMAS ’19, pages 2186– 2188. International Foundation for Autonomous Agents and Multiagent Systems, 2019. doi:https://dl.acm.org/doi/abs/10.5555/3306127. 3332052. 
[64] Kyrill Schmid, Lenz Belzner, Robert Müller, Johannes Tochtermann, and Claudia Linnhoff-Popien. "Stochastic Market Games". In Zhi-Hua Zhou, editor, Proceedings of the 30th International Joint Conference on Artificial Intelligence, IJCAI-21, pages 384–390. International Joint Conferences on Artificial Intelligence Organization, August 2021. doi:https://doi. org/10.24963/ijcai.2021/54. 
40
Bibliography 
[65] Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, Karen Si-monyan, Laurent Sifre, Simon Schmitt, Arthur Guez, Edward Lockhart, Demis Hassabis, Thore Graepel, Timothy Lillicrap, and David Silver. "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model". Nature, 588(7839):604–609, 2020. doi:https://doi.org/10. 1038/s41586-020-03051-4. 
[66] Yoav Shoham and Kevin Leyton-Brown. "Multiagent Systems: Algorith-mic, Game-Theoretic, and Logical Foundations". Cambridge University Press, 2008. doi:https://doi.org/10.1017/CBO9780511811654. 
[67] Yoav Shoham, Rob Powers, and Trond Grenager. "If Multi-Agent Learn-ing is the Answer, What is the Question?". Artificial Intelligence, 171(7):365–377, 2007. Foundations of Multi-Agent Learning. doi:https: //doi.org/10.1016/j.artint.2006.02.006. 
[68] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Has-sabis. "Mastering the Game of Go with Deep Neural Networks and Tree Search". Nature, 529(7587):484–489, 2016. doi:https://doi.org/10. 1038/nature16961. 
[69] David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Ku-maran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, and Demis Hassabis. "A General Reinforcement Learning Algorithm that Masters Chess, Shogi, and Go through Self-Play". Science, 362(6419):1140–1144, 2018. doi:https://doi.org/10.1126/science.aar6404. 
[70] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel, and Demis Hassabis. "Master-ing the Game of Go without Human Knowledge". Nature, 550(7676):354– 359, 2017. doi:https://doi.org/10.1038/nature24270. 
[71] David Silver and Joel Veness. "Monte-Carlo Planning in Large POMDPs". In J. Lafferty, C. Williams, J. Shawe-Taylor, R. Zemel, and A. Culotta, editors, Advances in Neural Information Processing Systems, volume 23. Curran Associates, Inc., 2010. doi:https://dl.acm.org/doi/abs/10. 5555/2997046.2997137. 
[72] Kyunghwan Son, Daewoo Kim, Wan Ju Kang, David Earl Hostallero, and Yung Yi. "QTRAN: Learning to Factorize with Transformation for Co-
41
Bibliography 
operative Multi-Agent Reinforcement Learning". In Kamalika Chaudhuri and Ruslan Salakhutdinov, editors, Proceedings of the 36th International Conference on Machine Learning, volume 97 of Proceedings of Machine Learning Research, pages 5887–5896. PMLR, 09–15 Jun 2019. 
[73] Peter Stone and Michael L. Littman. "Implicit Negotiation in Re-peated Games". In Pre-proceedings of the 8th International Workshop on Agent Theories, Architectures, and Languages (ATAL-2001), pages 96–105, 2001. 
[74] Peter Stone and Manuela Veloso. "Multiagent Systems: A Survey from a Machine Learning Perspective". Autonomous Robots, 8(3):345–383, July 2000. doi:https://doi.org/10.1023/A:1008942012299. 
[75] Peter Sunehag, Guy Lever, Audrunas Gruslys, Wojciech Marian Czar-necki, Vinicius Zambaldi, Max Jaderberg, Marc Lanctot, Nicolas Sonnerat, Joel Z Leibo, Karl Tuyls, and Thore Graepel. "Value-Decomposition Networks for Cooperative Multi-Agent Learning based on Team Reward". In Proceedings of the 17th International Conference on Autonomous Agents and Multiagent Systems (Extended Abstract), AA-MAS ’18, pages 2085–2087. International Foundation for Autonomous Agents and Multiagent Systems, 2018. doi:https://dl.acm.org/doi/ 10.5555/3237383.3238080. 
[76] Richard S. Sutton and Andrew G. Barto. "Reinforcement Learning: An Introduction". A Bradford Book, Cambridge, MA, USA, 2018. 
[77] Richard S Sutton, David A McAllester, Satinder P Singh, and Yishay Mansour. "Policy Gradient Methods for Reinforcement Learning with Function Approximation". In S. Solla, T. Leen, and K. Müller, editors, Advances in Neural Information Processing Systems, volume 12, pages 1057–1063. MIT Press, 2000. doi:https://dl.acm.org/doi/abs/10. 5555/3009657.3009806. 
[78] Ming Tan. "Multi-Agent Reinforcement Learning: Independent versus Cooperative Agents". In Proceedings of the 10th International Conference on International Conference on Machine Learning, pages 330–337. Mor-gan Kaufmann Publishers Inc., 1993. doi:https://dl.acm.org/doi/ 10.5555/3091529.3091572. 
[79] Andrew S. Tanenbaum and Maarten Van Steen. "Distributed Systems: Principles and Paradigms". Prentice-Hall, 2007. 
[80] Gerald Tesauro. "Temporal Difference Learning and TD-Gammon". Communications of the ACM, 38(3):58–68, March 1995. doi:https: //doi.org/10.1145/203330.203343. 
42
Bibliography 
[81] Robert L. Trivers. "The Evolution of Reciprocal Altruism". The Quarterly Review of Biology, 46(1):35–57, 1971. doi:https://doi.org/10.1086/ 406755. 
[82] Jonathan Uesato, Ananya Kumar, Csaba Szepesvari, Tom Erez, Avra-ham Ruderman, Keith Anderson, Krishmamurthy (Dj) Dvijotham, Nico-las Heess, and Pushmeet Kohli. "Rigorous Agent Evaluation: An Adver-sarial Approach to Uncover Catastrophic Failures". International Con-ference on Learning Representations, 2019. 
[83] Eugene Vinitsky, Raphael Köster, John P Agapiou, Edgar Duéñez-Guzmán, Alexander Sasha Vezhnevets, and Joel Z Leibo. "A Learning Agent that Acquires Social Norms from Public Sanctions in Decentralized Multi-Agent Settings". arXiv preprint arXiv:2106.09012, 2021. 
[84] Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki, Michaël Math-ieu, Andrew Dudzik, Junyoung Chung, David H Choi, Richard Pow-ell, Timo Ewalds, Petko Georgiev, Junhyuk Oh, Dan Horgan, Manuel Kroiss, Ivo Danihelka, Aja Huang, Laurent Sifre, Trevor Cai, John P. Agapiou, Max Jaderberg, Alexander S. Vezhnevets, Rémi Leblond, To-bias Pohlen, Valentin Dalibard, David Budden, Yury Sulsky, James Mol-loy, Tom L. Paine, Caglar Gulcehre, Ziyu Wang, Tobias Pfaff, Yuhuai Wu, Roman Ring, Dani Yogatama, Dario Wünsch, Katrina McKinney, Oliver Smith, Tom Schaul, Timothy Lillicrap, Koray Kavukcuoglu, Demis Has-sabis, Chris Apps, and David Silver. "Grandmaster Level in StarCraft II using Multi-Agent Reinforcement Learning". Nature, pages 1–5, 2019. doi:https://doi.org/10.1038/s41586-019-1724-z. 
[85] Jianhao Wang, Zhizhou Ren, Terry Liu, Yang Yu, and Chongjie Zhang. "QPLEX: Duplex Dueling Multi-Agent Q-Learning". In International Conference on Learning Representations, 2021. 
[86] Ari Weinstein and Michael L Littman. "Open-loop Planning in Large-Scale Stochastic Domains". In Proceedings of the AAAI Conference on Artificial Intelligence, pages 1436–1442. AAAI Press, 2013. doi:https: //doi.org/10.1609/aaai.v27i1.8547. 
[87] Gerhard Weiß, editor. "Multiagent Systems: A Modern Approach to Dis-tributed Artificial Intelligence". MIT Press, Cambridge, MA, USA, 1999. doi:https://dl.acm.org/doi/10.5555/305606. 
[88] Jess Whittlestone, Kai Arulkumaran, and Matthew Crosby. "The Soci-etal Implications of Deep Reinforcement Learning". Journal of Artificial Intelligence Research, 70:1003–1030, May 2021. doi:https://doi.org/ 10.1613/jair.1.12360. 
43
Bibliography 
[89] David H Wolpert and Kagan Tumer. "Optimal Payoff Functions for Mem-bers of Collectives". In Modeling Complexity in Economic and Social Sys-tems, pages 355–369. World Scientific, 2002. doi:https://doi.org/10. 1142/9789812777263_0020. 
[90] Jiachen Yang, Ang Li, Mehrdad Farajtabar, Peter Sunehag, Edward Hughes, and Hongyuan Zha. "Learning to Incentivize Other Learning Agents". Advances in Neural Information Processing Systems, 33, 2020. doi:https://dl.acm.org/doi/abs/10.5555/3495724.3496999. 
[91] Ming Zhou, Jun Luo, Julian Villella, Yaodong Yang, David Rusu, Ji-ayu Miao, Weinan Zhang, Montgomery Alban, IMAN FADAKAR, Zheng Chen, Chongxi Huang, Ying Wen, Kimia Hassanzadeh, Daniel Graves, Zhengbang Zhu, Yihan Ni, Nhat Nguyen, Mohamed Elsayed, Haitham Ammar, Alexander Cowen-Rivers, Sanjeevan Ahilan, Zheng Tian, Daniel Palenicek, Kasra Rezaee, Peyman Yadmellat, Kun Shao, dong chen, Baokuan Zhang, Hongbo Zhang, Jianye Hao, Wulong Liu, and Jun Wang. "SMARTS: An Open-Source Scalable Multi-Agent RL Training School for Autonomous Driving". In Jens Kober, Fabio Ramos, and Claire Tomlin, editors, Proceedings of the 2020 Conference on Robot Learning, volume 155 of Proceedings of Machine Learning Research, pages 264–285. PMLR, 16–18 Nov 2021. 
44
A. Publications 
We list all publications that contain the core findings of the thesis and provide the core contributions as well as the credit in accordance with LMU Munich regulations. We reprint Table 1.1 below as an overview for easier reference. 
Thesis chapter Questions Publications 3. Emergent Cooperation in General-Sum Games Q1, Q2 [55] 4. Emergence in Cooperative Multi-Agent RL Q3 [49, 53, 54] 5. Resilience in Cooperative Multi-Agent RL Q4, Q5 [47, 51] 6. Further Topics Q6 [18, 48, 50, 52] 
45
A.1. Emergent Cooperation from Mutual Acknowledgment Exchange 
Publication 
Thomy Phan, Felix Sommer, Philipp Altmann, Fabian Ritz, Lenz Belzner, and Claudia Linnhoff-Popien. "Emergent Cooperation from Mutual Acknowl-edgment Exchange". In Proceedings of the 21st International Conference on Autonomous Agents and MultiAgent Systems (AAMAS), pages 1047–1055. In-ternational Foundation for Autonomous Agents and Multiagent Systems, 2022. 
DOI: https://dl.acm.org/doi/10.5555/3535850.3535967 URL: https://ifaamas.org/Proceedings/aamas2022/pdfs/p1047.pdf 
Contributions 
1. A two-phase communication protocol for reciprocal peer incentivization. 
2. Robustness evaluation w.r.t. random protocol defectors and communi-cation failures. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Sommer conceived and conducted a preliminary study of a centralized MARL approach based on trust metrics supervised by Phan and Altmann. Ritz sup-ported the robustness evaluation. Altmann, Ritz, and Belzner discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. This publication is based on Sommer’s thesis to achieve the degree Master of Science. 
Purpose 
Main focus of Chapter 3 regarding the research questions Q1 and Q2 from Section 1.2. 
46
A.2. Distributed Policy Iteration for Scalable Approximation of Cooperative Multi-Agent Policies 
Publication 
Thomy Phan, Kyrill Schmid, Lenz Belzner, Thomas Gabor, Sebastian Feld, and Claudia Linnhoff-Popien. "Distributed Policy Iteration for Scalable Approximation of Cooperative Multi-Agent Policies". In Proceedings of the 18th International Conference on Autonomous Agents and MultiAgent Sys-tems (AAMAS), pages 2162–2164. International Foundation for Autonomous Agents and Multiagent Systems, 2019. 
DOI: https://dl.acm.org/doi/10.5555/3306127.3332044 URL: https://ifaamas.org/Proceedings/aamas2019/pdfs/p2162.pdf 
Contributions 
1. A distributed policy iteration scheme combining planning and RL for fully observable multi-agent domains. 
2. An open-loop planning algorithm integrating learned multi-agent policies and value functions for efficient search. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Schmid and Belzner discussed the concepts and results, and provided feedback on related work. Gabor and Feld discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 4 regarding the research question Q3 from Section 1.2. 
47
A.3. A Distributed Policy Iteration Scheme for Cooperative Multi-Agent Policy Approximation 
Publication 
Thomy Phan, Lenz Belzner, Kyrill Schmid, Thomas Gabor, Fabian Ritz, Sebastian Feld, and Claudia Linnhoff-Popien. "A Distributed Policy Iteration Scheme for Cooperative Multi-Agent Policy Approximation". In 12th Adaptive and Learning Agents Workshop (ALA), 2020. 
URL: https://ala2020.vub.ac.be/papers/ALA2020_paper_36.pdf 
Contributions 
1. Extension of [54] to partially observable multi-agent domains. 
2. A centralized training and decentralized planning scheme to learn effec-tive local policies for large-scale multi-agent scenarios. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Belzner and Schmid discussed the concepts and results, and provided feedback on related work. Gabor, Ritz, and Feld discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 4 regarding the research question Q3 from Section 1.2. 
48
A.4. VAST: Value Function Factorization with Variable Agent Sub-Teams 
Publication 
Thomy Phan, Fabian Ritz, Lenz Belzner, Philipp Altmann, Thomas Gabor, and Claudia Linnhoff-Popien. "VAST: Value Function Factorization with Variable Agent Sub-Teams". In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, Advances in Neural Informa-tion Processing Systems (NeurIPS), volume 34, pages 24018–24032. Curran Associates, Inc., 2021. 
URL: https://proceedings.neurips.cc/paper/2021/hash/ c97e7a5153badb6576d8939469f58336-Abstract.html 
Contributions 
1. Hierarchical value function factorization with variable agent sub-teams. 
2. Meta-gradient optimization of sub-teams. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Ritz and Belzner discussed the concepts and results, and provided support on the sub-team evaluation. Altmann and Gabor discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 4 regarding the research question Q3 from Section 1.2. 
49
A.5. Learning and Testing Resilience in Cooperative Multi-Agent Systems 
Publication 
Thomy Phan, Thomas Gabor, Andreas Sedlmeier, Fabian Ritz, Bernhard Kempter, Cornel Klein, Horst Sauer, Reiner Schmid, Jan Wieghardt, Marc Zeller, and Claudia Linnhoff-Popien. "Learning and Testing Resilience in Cooperative Multi-Agent Systems". In Proceedings of the 19th International Conference on Autonomous Agents and MultiAgent Systems (AAMAS), pages 1055–1063. International Foundation for Autonomous Agents and Multiagent Systems, 2020. 
DOI: https://dl.acm.org/doi/10.5555/3398761.3398884 URL: https://ifaamas.org/Proceedings/aamas2020/pdfs/p1055.pdf 
Contributions 
1. Antagonist-based training and test scheme. 
2. Resilience evaluation based on agent cross-validation. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Gabor discussed the concepts and results, and provided feedback on related work. Sedlmeier and Ritz discussed and reviewed the results, and supported the setup implementation. Kempter, Klein, Sauer, Schmid, Wieghardt, and Zeller reviewed and discussed the concepts, and provided feedback on the setup. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 5 regarding the research questions Q4 and Q5 from Section 1.2. 
50
A.6. Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition 
Publication 
Thomy Phan, Lenz Belzner, Thomas Gabor, Andreas Sedlmeier, Fabian Ritz, and Claudia Linnhoff-Popien. "Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition". In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), volume 35(13), pages 11308–11316, 2021. 
DOI: https://doi.org/10.1609/aaai.v35i13.17348 URL: https://ojs.aaai.org/index.php/AAAI/article/view/17348 
Contributions 
1. Antagonist-based training with variable sized antagonist teams. 
2. Resilience evaluation based on cooperation and worst-case performance using dedicated test sets of agents. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Belzner and Gabor discussed the concepts and results, and provided feedback on related work. Sedlmeier supported the setup implementation. Ritz reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 5 regarding the research questions Q4 and Q5 from Section 1.2. 
51
A.7. Memory Bounded Open-Loop Planning in Large POMDPs using Thompson Sampling 
Publication 
Thomy Phan, Lenz Belzner, Marie Kiermeier, Markus Friedrich, Kyrill Schmid, and Claudia Linnhoff-Popien. "Memory Bounded Open-Loop Planning in Large POMDPs using Thompson Sampling". In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), volume 33(01), pages 7941–7948, 2019. 
DOI: https://doi.org/10.1609/aaai.v33i01.33017941 URL: https://ojs.aaai.org/index.php/AAAI/article/view/4794 
Contributions 
1. Memory bounded open-loop planning with fixed Thompson Sampling stacks. 
2. Memory efficiency evaluation of open- and closed-loop Monte Carlo plan-ning algorithms. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Belzner co-conceived the concepts and provided feedback on implementing Thompson Sampling. Kiermeier, Friedrich, and Schmid discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 6 regarding the research question Q6 from Section 1.2. 
52
A.8. Adaptive Thompson Sampling Stacks for Memory Bounded Open-Loop Planning 
Publication 
Thomy Phan, Thomas Gabor, Robert Müller, Christoph Roch, and Claudia Linnhoff-Popien. "Adaptive Thompson Sampling Stacks for Memory Bounded Open-Loop Planning". In Proceedings of the 28th International Joint Confer-ence on Artificial Intelligence (IJCAI), pages 5607–5613. International Joint Conferences on Artificial Intelligence Organization, 2019. 
DOI: https://doi.org/10.24963/ijcai.2019/778 URL: https://www.ijcai.org/proceedings/2019/778 
Contributions 
Memory bounded open-loop planning with adaptive Thompson Sampling stacks based on bandit convergence. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Gabor, Müller, and Roch discussed the concepts and results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 6 regarding the research question Q6 from Section 1.2. 
53
A.9. Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Publication 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
Contributions 
1. Value function factorization scheme, which exploits the recurrence of all agents using self-attention instead of true states. 
2. General and configurable Dec-POMDP benchmark, extending StarCraft Multi-Agent Challenge with stochastic observations and higher variance in initial states. 
Credit 
Phan conceived the original concepts and conducted the empirical analysis. Ritz, Altmann, Zorn, Nüßlein, Kölle, and Gabor discussed the concepts and results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 6 regarding the research question Q6 from Section 1.2. 
Preprint attached below. 
54
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Thomy Phan 1 † Fabian Ritz 2 Philipp Altmann 2 Maximilian Zorn 2 Jonas Nüßlein 2 Michael Kölle 2 
Thomas Gabor 2 Claudia Linnhoff-Popien 2 
Abstract Stochastic partial observability poses a major challenge for decentralized coordination in multi-agent reinforcement learning but is largely ne-glected in state-of-the-art research due to a strong focus on state-based centralized training for de-centralized execution (CTDE) and benchmarks that lack sufficient stochasticity like StarCraft Multi-Agent Challenge (SMAC). In this paper, we propose Attention-based Embeddings of Recur-rence In multi-Agent Learning (AERIAL) to ap-proximate value functions under stochastic partial observability. AERIAL replaces the true state with a learned representation of multi-agent re-currence, considering more accurate information about decentralized agent decisions than state-based CTDE. We then introduce MessySMAC, a modified version of SMAC with stochastic ob-servations and higher variance in initial states, to provide a more general and configurable bench-mark regarding stochastic partial observability. We evaluate AERIAL in Dec-Tiger as well as in a variety of SMAC and MessySMAC maps, and compare the results with state-based CTDE. Fur-thermore, we evaluate the robustness of AERIAL and state-based CTDE against various stochastic-ity configurations in MessySMAC. 
1. Introduction A wide range of real-world applications like fleet manage-ment, industry 4.0, or communication networks can be for-mulated as decentralized partially observable Markov de-cision process (Dec-POMDP) representing a cooperative multi-agent system (MAS), where multiple agents have to coordinate to achieve a common goal (Oliehoek & Amato, 
1University of Southern California, USA. †Work done at LMU Munich 2LMU Munich, Germany. This paper is an ex-tension of (Phan et al., 2023). Correspondence to: Thomy Phan <thomy.phan@ifi.lmu.de>. 
2016). Stochastic partial observability poses a major chal-lenge for decentralized coordination in Dec-POMDPs due to noisy sensors and potentially high variance in initial states which are common in the real world (Kaelbling et al., 1998; Oliehoek & Amato, 2016). 
Multi-agent reinforcement learning (MARL) is a general approach to tackle Dec-POMDPs with remarkable progress in recent years (Wang et al., 2021; Wen et al., 2022). State-of-the-art MARL is based on centralized training for de-centralized execution (CTDE), where training takes place in a laboratory or a simulator with access to global informa-tion (Lowe et al., 2017; Foerster et al., 2018). For example, state-based CTDE exploits true state information to learn a centralized value function in order to derive coordinated policies for decentralized decision making (Rashid et al., 2018; Yu et al., 2022). Due to its effectiveness in the Star-Craft Multi-Agent Challenge (SMAC) as the current de facto standard for MARL evaluation, state-based CTDE has be-come very popular and is widely considered an adequate approach to general Dec-POMDPs for more than half a decade, leading to the development of many increasingly complex algorithms (Lyu et al., 2021; 2022). 
However, merely relying on state-based CTDE and SMAC in MARL research can be a pitfall in practice as stochastic partial observability is largely neglected – despite being an important aspect in Dec-POMDPs (Lyu et al., 2022): 
From an algorithm perspective, purely state-based value functions are insufficient to evaluate and adapt multi-agent behavior, since all agents make decisions on a completely different basis, i.e., individual histories of noisy observa-tions and actions. True Dec-POMDP value functions con-sider more accurate closed-loop information about decen-tralized agent decisions though (Oliehoek et al., 2008). Fur-thermore, the optimal state-based value function represents an upper-bound of the true optimal Dec-POMDP value func-tion thus state-based CTDE can result in overly optimistic behavior in general Dec-POMDPs (Lyu et al., 2022). 
From a benchmark perspective, SMAC has very limited stochastic partial observability due to deterministic obser-vations and low variance in initial states (Ellis et al., 2022). 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
55
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Therefore, SMAC scenarios only represent simplified spe-cial cases rather than general Dec-POMDP challenges, be-ing insufficient for assessing practicability of MARL. 
In this paper, we propose Attention-based Embeddings of Re-currence In multi-Agent Learning (AERIAL) to approximate value functions under agent-wise stochastic partial observ-ability. AERIAL replaces the true state with a learned repre-sentation of multi-agent recurrence, considering more accu-rate closed-loop information about decentralized agent de-cisions than state-based CTDE. We then introduce MessyS-MAC, a modified version of SMAC with stochastic observa-tions and higher variance in initial states, to provide a more general and configurable Dec-POMDP benchmark for more adequate evaluation. Our contributions are as follows: 
 We formulate and discuss the concepts of AERIAL w.r.t. stochastic partial observability in Dec-POMDPs. 
 We introduce MessySMAC to enable systematic evalu-ation under various stochasticity configurations. 
 We evaluate AERIAL in Dec-Tiger, a small and tradi-tional Dec-POMDP benchmark, as well as in a variety of original SMAC and MessySMAC maps, and com-pare the results with state-based CTDE. Our results show that AERIAL achieves competitive performance in original SMAC, and superior performance in Dec-Tiger and MessySMAC. Furthermore, we evaluate the robustness of AERIAL and state-based CTDE against various stochasticity configurations in MessySMAC. 
2. Background 2.1. Decentralized POMDPs 
We formulate cooperative MAS problems as Dec-POMDP M = 〈D,S,A, T ,R,Z,Ω, b0〉, whereD = {1, ..., N} is a set of agents i, S is a set of (true) states st at time step t,A = 〈Ai〉i∈D is the set of joint actions at = 〈at,1, ..., at,N 〉 = 〈at,i〉i∈D, T (st+1|st,at) is the state transition probability, rt = R(st,at) ∈ R is the shared reward, Z is a set of local observations zt,i for each agent i ∈ D, Ω(zt+1|at, st+1) is the probability of joint observation zt+1 = 〈zt+1,i〉i∈D ∈ ZN , and b0 is the probability distribution over initial states s0 (Oliehoek & Amato, 2016). Each agent i maintains a local history τt,i ∈ (Z × Ai)t and τ t = 〈τt,i〉i∈D is the joint history. A belief state b(st|τ t) is a sufficient statistic for joint history τ t and defines a probability distribution over true states st, updatable by Bayes’ theorem (Kaelbling et al., 1998). Joint quantities are written in bold face. 
Stochastic partial observability inM is given by observation and initialization stochasticity w.r.t. Ω and b0 respectively. 
A joint policy π = 〈πi〉i∈D with decentralized or local poli-cies πi defines a deterministic mapping from joint histories 
to joint actions π(τ t) = 〈πi(τt,i)〉i∈D ∈ A. The return is defined by Gt = 
∑T−1 c=0 γ 
crt+c, where T is the horizon and γ ∈ [0, 1] is the discount factor. π can be evaluated with a value function Qπ(τ t,at) = Eb0,T ,Ω[Gt|τ t,at,π]. The goal is to find an optimal joint policy π∗ with optimal value function Qπ∗ 
= Q∗ as defined in the next section. 
2.2. Optimal Value Functions and Policies 
Fully Observable MAS In MDP-like settings with a cen-tralized controller, the optimal value function Q∗MDP is de-fined by (Watkins & Dayan, 1992; Boutilier, 1996): 
Q∗MDP(st,at) = rt + γ ∑ 
st+1∈S X (1) 
where X = T (st+1|st,at)maxat+1∈AQ ∗ MDP(st+1,at+1). 
Due to full observability, Q∗MDP does not depend on τ t but on st. Thus, decentralized observations zt,i and probabil-ities according to Ω and b0 are not considered at all. An optimal (joint) policy π∗MDP of the centralized controller sim-ply maximizes Q∗MDP for all st (Watkins & Dayan, 1992): 
π∗MDP = argmaxπMDP 
∑ 
st∈S Q∗MDP(st,πMDP(st)) (2) 
Partially Observable MAS In general Dec-POMDPs, where true states are not fully observable and only decentral-ized controllers or agents exist, the optimal value function Q∗ is defined by (Oliehoek et al., 2008): 
Q∗(τ t,at) = ∑ 
st∈S b(st|τ t) 
 rt + γ 
∑ 
st+1∈S 
∑ 
zt+1∈ZN 
X 
  
(3) 
where X = T (st+1|st,at)Ω(zt+1|at, st+1)Q∗(τ t+1, π∗(τ t+1)) with τ t+1 = 〈τ t,at, zt+1〉. An optimal joint policy π∗ for decentralized execution maxi-mizes the expectation ofQ∗ for all joint histories τ t (Emery-Montemerlo et al., 2004; Oliehoek et al., 2008): 
π∗ = argmaxπ 
T−1∑ 
t=0 
∑ 
τ t∈(ZN×A)t 
Cπ(τ t)P π(τ t|b0)Q∗(·) 
(4) where Q∗(·) = Q∗(τ t,π(τ t)), indicator Cπ(τ t) filters out joint histories τ t that are inconsistent with π, and prob-ability Pπ(τ t|b0) represents the recurrence of all agents considering agent-wise stochastic partial observability w.r.t. decentralization of π and τ t (Oliehoek et al., 2008): 
Pπ(τ t|b0) = P(z0|b0) ∏t 
c=1 P(zc|τ c−1,π) 
= P(z0|b0) ∏t 
c=1 
∑ 
sc∈S 
∑ 
sc−1∈S T (·)Ω(·) (5) 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
56
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
where T (·) = T (sc|sc−1,π(τ c−1)) and Ω(·) = Ω(zc|π(τ c−1), sc). 
Since all agents act according to their local history τt,i without access to the complete joint history τ t, recurrence Pπ(τ t|b0) depends on more accurate closed-loop informa-tion than just true states st, i.e., all previous observations, actions, and probabilities according to b0, T , and Ω. 
Q∗MDP is proven to represent an upper bound of Q∗ 
(Oliehoek et al., 2008). Thus, naively deriving local policies πi from Q∗MDP instead of Q∗ can result in overly optimistic behavior as we will show in Section 4.1 and 6. 
2.3. Multi-Agent Reinforcement Learning 
Finding an optimal joint policy π∗ via exhaustive compu-tation of Q∗ according to Eq. 3-5 is intractable in prac-tice (Nair et al., 2003; Szer et al., 2005). MARL offers a scalable way to learn Q∗ and π∗ via function approxi-mation, e.g., using CTDE, where training takes place in a laboratory or a simulator with access to global informa-tion (Lowe et al., 2017; Foerster et al., 2018). We focus on value-based MARL to learn a centralized value func-tion Qtot ≈ Q∗, which can be factorized into local utility functions 〈Qi〉i∈D for decentralized decision making via πi(τt,i) = argmaxat,iQi(τt,i, at,i). For that, a factorization operator Ψ is used (Phan et al., 2021): 
Qtot(τ t,at) = Ψ(Q1(τt,1, at,1), ..., QN (τt,N , at,N )) (6) 
In practice, Ψ is realized with deep neural networks, such that 〈Qi〉i∈D can be learned end-to-end via backpropagation by minimizing the mean squared temporal difference (TD) error (Rashid et al., 2018; Sunehag et al., 2018). A factor-ization operator Ψ is decentralizable when satisfying the IGM (Individual-Global-Max) such that (Son et al., 2019): 
argmaxat Qtot(τ t,at) = 
  
argmaxat,1Q1(τt,1, at,1) ... 
argmaxat,NQN (τt,N , at,N ) 
  
(7) 
There exists a variety of factorization operators Ψ which satisfy Eq. 7 using monotonicity like QMIX (Rashid et al., 2018), nonlinear transformation like QPLEX (Wang et al., 2021), or loss weighting like CW- and OW-QMIX (Rashid et al., 2020). Most approaches use state-based CTDE to learn Q∗MDP according to Eq. 1 instead of Q∗ (Eq. 3-5). 
2.4. Recurrent Reinforcement Learning 
In partially observable settings, the policy πi of agent i conditions on the history τt,i of past observations and ac-tions (Kaelbling et al., 1998; Oliehoek & Amato, 2016). In 
practice, recurrent neural networks (RNNs) like LSTMs or GRUs are used to learn a compact representation ht,i of τt,i and πi known as hidden state or memory representa-tion1, which implicitly encodes the individual recurrence of agent i, i.e., the distribution Pπi 
i over τt,i (Hochreiter & Schmidhuber, 1997; Cho et al., 2014; Hu & Foerster, 2019): 
Pπi i (τt,i|b0) = Pi(z0,i|b0) 
∏t 
c=1 Pi(zc,i|τc−1,i, πi) (8) 
RNNs are commonly used for partially observable problems and have been empirically shown to be more effective than using raw observations zt,i or histories τt,i (Hausknecht & Stone, 2015; Samvelyan et al., 2019; Vinyals et al., 2019). 
3. Related Work Multi-Agent Reinforcement Learning In recent years, MARL has achieved remarkable progress in challenging domains (Gupta et al., 2017; Vinyals et al., 2019). State-of-the-art MARL is based on CTDE to learn a centralized value function Qtot for actor-critic learning (Lowe et al., 2017; Foerster et al., 2018; Yu et al., 2022) or factorization (Rashid et al., 2018; 2020; Wang et al., 2021). However, the majority of works assumes a simplified Dec-POMDP setting, where Ω is deterministic, and uses true states to approximateQ∗MDP according to Eq. 1 instead of Q∗ (Eq. 3-5). Thus, state-based CTDE is possibly less effective in more general Dec-POMDP settings. Our approach addresses stochastic partial observability with a learned representation of multi-agent recurrence Pπ(τ t|b0) according to Eq. 5 instead of st. 
Weaknesses of State-Based CTDE Recent works investi-gated potential weaknesses of state-based CTDE for multi-agent actor-critic methods regarding bias and variance (Lyu et al., 2021; 2022). The experimental results show that state-based CTDE can surprisingly fail in very simple Dec-POMDP benchmarks that exhibit more stochasticity than SMAC. While these studies can be considered an impor-tant step towards general Dec-POMDPs, there is neither an approach which adequately addresses stochastic partial observability nor a benchmark to systematically evaluate such an approach yet. In this work, we focus on value-based MARL, where learning an accurate value function is impor-tant for meaningful factorization, and propose an attention-based recurrence approach to approximate value functions under stochastic partial observability. We also introduce a modified SMAC benchmark, which enables systematic evaluation under various stochasticity configurations. 
Attention-Based CTDE Attention has been used in CTDE to process information of potentially variable length 
1In this paper, we use the term memory representation to avoid confusion with the state terminology of the (Dec-)POMDP litera-ture (Kaelbling et al., 1998; Oliehoek & Amato, 2016). 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
57
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
N , where joint observations zt, joint actions at, or local utilities 〈Qi〉i∈D are weighted and aggregated to provide a meaningful representation for value function approximation (Iqbal & Sha, 2019; Wang et al., 2021; Iqbal et al., 2021; Wen et al., 2022; Khan et al., 2022). Most works focus on Markov games without observation stochasticity, which are special cases of the Dec-POMDP setting. In this work, we focus on stochastic partial observability and apply self-attention to the memory representations ht,i of all agents’ RNNs instead of the raw observations zt,i to approximate Q∗ for general Dec-POMDPs according to Eq. 3-5. 
4. AERIAL 4.1. Limitation of State-Based CTDE 
Most state-of-the-art works assume a simplified Dec-POMDP setting, where Ω is deterministic, and approximate Q∗MDP according to Eq. 1 instead of Q∗ (Eq. 3-5). 
If there are only deterministic observations and initial states s0 such that b0(s0) = 1 and b0(s′) = 0 if s′ 6= s0, then multi-agent recurrence Pπ(τ t|b0) as defined in Eq. 5 would only depend on state transition probabilities T (st+1|st,at) which are purely state-based, ignoring decentralization of agents and observations (Oliehoek et al., 2008). In such scenarios, stochastic partial observability is very limited, especially if all πi are deterministic. We hypothesize that this is one reason for the empirical success of state-based CTDE in original SMAC, whose scenarios seemingly have these simplifying properties (Ellis et al., 2022). 
In the following, we regard a small example, where state-based CTDE can fail at finding an optimal joint policy π∗. 
Example Dec-Tiger is a traditional and simple Dec-POMDP benchmark with N = 2 agents facing two doors (Nair et al., 2003). A tiger is randomly placed behind the left (sL) or right door (sR) representing the true state. Both agents are able to listen (li) and open the left (oL) or right door (oR). The listening action li produces a noisy obser-vation of either hearing the tiger to be left (zL) or right (zR), which correctly indicates the tiger’s position with 85% chance and a cost of −1 per listening agent. If both agents open the same door, the episode terminates with a reward of -50 if opening the tiger door and +20 otherwise. If both agents open different doors, the episode ends with -100 re-ward and, if only one agent opens a door while the other agent is listening, the episode terminates with -101 if open-ing the tiger door and +9 otherwise. 
Given a horizon of T = 2, the tiger being behind the right door (sR), and both agents having listened in the first step, where agent 1 heard zL and agent 2 heard zR: Assuming that both agents learned to perform the same actions, e.g., due to CTDE and parameter sharing (Tan, 1993; Gupta et al., 
2017), Q∗MDP and Q∗ would estimate the following values2: 
Q∗MDP(sR, 〈li, li〉) = −2 Q∗(τ t, 〈li, li〉) = −2 
Q∗MDP(sR, 〈oL, oL〉) = 20 Q∗(τ t, 〈oL, oL〉) = −15 
Q∗MDP(sR, 〈oR, oR〉) = −50 Q∗(τ t, 〈oR, oR〉) = −15 
Any policy π∗MDP or decentralizable joint policy π w.r.t. IGM (Eq. 7) that maximizes Q∗MDP according to Eq. 2 would optimistically recommend 〈oL, oL〉 based on the true state sR, regardless of what the agents observed. However, any joint policy π∗ that maximizes the expectation of Q∗ 
according to Eq. 4 would consider agent-wise stochastic partial observability and recommend 〈li, li〉, which corre-sponds to the true optimal decision for T = 2 (Szer et al., 2005). 
4.2. Attention-Based Embeddings of Recurrence 
Preliminaries We now introduce Attention-based Embed-dings of Recurrence In multi-Agent Learning (AERIAL) to approximate optimal Dec-POMDP value functions Q∗ ac-cording to Eq. 3-5. Our setup uses a factorization operator Ψ like QMIX or QPLEX according to Eq. 6-7. All agents process their local histories τt,i via RNNs as motivated in Section 2.4 and schematically shown in Fig. 1 (left). 
Unlike Q∗MDP, the true optimal Dec-POMDP value func-tion Q∗ considers more accurate closed-loop information about decentralized agent decisions through multi-agent re-currence Pπ(τ t|b0) according to Eq. 5. Simply replacing st with τ t as suggested in (Lyu et al., 2022) is not sufficient because the resulting value function would assume a central-ized controller with access to the complete joint history τ t, in contrast to decentralized agents i which can only access their respective local history τt,i (Oliehoek et al., 2008). 
Exploiting Multi-Agent Recurrence At first we propose to naively exploit all individual recurrences by simply re-placing the true state st in CTDE with the joint memory representation ht = 〈ht,i〉i∈D of all agents’ RNNs. Each memory representation ht,i implicitly encodes the individ-ual recurrence Pπi 
i (τt,i|b0) of agent i according to Eq. 8. Therefore, ht provides more accurate closed-loop informa-tion about decentralized agent decisions than st. 
This approach, called AERIAL (no attention), can already be considered a sufficient solution if all individual recurrences Pπi 
i (τt,i|b0) are statistically independent such that Pπ(τ t|b0) = 
∏N i=1 P 
πi i (τt,i|b0). 
Attention-Based Recurrence While AERIAL (no attention) offers a simple way to address agent-wise stochastic partial observability, the independence assump-tion of all individual recurrences Pπi 
i (τt,i|b0) does not hold 
2The exact calculation is provided in the Appendix B. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
58
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Agent NAgent 1MLP 
RNN 
MLP 
Transformer 
... 
Figure 1. Illustration of the AERIAL setup. Left: Recurrent agent network structure with memory representations ht−1,i and ht,i. Right: Value function factorization via factorization operator Ψ using the joint memory representation ht = 〈ht,i〉i∈D of all agents’ RNNs instead of true states st. All memory representations ht,i are detached from the computation graph to avoid additional differentiation (indicated by the dashed gray arrows) and passed through a simplified transformer before being used by Ψ for value function factorization. 
in practice due to correlations in observations and actions (Bernstein et al., 2005; Amato et al., 2007). 
Given the Dec-Tiger example above, the individual re-currences according to Eq. 8 are Pπ1 
1 (τt,1|b0) = Pπ2 
2 (τt,2|b0) = 0.5 (Kaelbling et al., 1998). However, the actual multi-agent recurrence according to Eq. 5 is Pπ(τ t|b0) = 0.15 · 0.85 6= Pπ1 
1 (τt,1|b0) · Pπ2 2 (τt,2|b0), 
indicating that individual recurrences are not statistically independent in general (Oliehoek & Amato, 2016). 
Therefore, we process ht by a simplified transformer along the agent axis to automatically consider the latent depen-dencies of all memory representations ht,i ∈ ht through self-attention. The resulting approach, called AERIAL, is depicted in Fig. 1 and Algorithm 1 in Appendix C. 
Our transformer does not use positional encoding or mask-ing, since we assume no particular ordering among agents. The joint memory representation ht is passed through a single multi-head attention layer with the output of each attention head c being defined by (Vaswani et al., 2017): 
attc(ht) = softmax 
( W c q (ht)W 
c k (ht) 
> √ datt 
) W c v (ht) (9) 
where W c q , W c 
k , and W c v are multi-layer perceptrons (MLP) 
with an output dimensionality of datt. All outputs attc(ht) are summed and passed through a series of MLP layers be-fore being fed into the factorization operator Ψ, effectively replacing the true state st by a learned representation of multi-agent recurrence Pπ(τ t|b0) according to Eq. 5. 
To avoid additional differentation of ht through Ψ or Eq. 9, we detach ht from the computation graph. Thus, we make 
sure that ht is only learned through agent RNNs. 
4.3. Discussion of AERIAL 
The strong focus on state-based CTDE in the last few years has led to the development of increasingly complex algo-rithms that largely neglect stochastic partial observability in general Dec-POMDPs (Lyu et al., 2021; 2022). In con-trast, AERIAL offers a simple way to adjust factorization approaches by replacing the true state st with a learned rep-resentation of multi-agent recurrence Pπ(τ t|b0) to consider more accurate closed-loop information about decentralized agent decisions. The rest of the training scheme remains unchanged, which eases adjustment of existing approaches. 
Since the naive independence assumption of individual memory representations ht,i does not hold in practice – de-spite decentralization – we use a simplified transformer to consider the latent dependencies of all ht,i ∈ ht along the agent axis to learn an adequate representation of multi-agent recurrence Pπ(τ t|b0) according to Eq. 5. 
AERIAL does not depend on true states therefore requiring less overall information than state-based CTDE, since we assume ht to be available in all CTDE setups anyway (Fo-erster et al., 2018; Rashid et al., 2020). Note that AERIAL does not necessarily require RNNs to obtain ht as hidden layers of MLPs or decision transformers can be used to approximate ht as well (Son et al., 2019; Chen et al., 2021). 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
59
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Figure 2. Left: Screenshot of two SMAC maps. Middle: PCA visualization of the joint observations in original SMAC within the first 5 steps of 1,000 episodes using a random policy with K = 0 initial random steps. Right: Analogous PCA visualization for MessySMAC with K = 10 initial random steps. For visual comparability, the observations are deterministic here. 
5. MessySMAC 5.1. Limitation of SMAC as a Benchmark 
StarCraft Multi-Agent Challenge (SMAC) provides a rich set of micromanagement tasks, where a team of learning agents has to fight against an enemy team, which acts ac-cording to handcrafted heuristics of the built-in StarCraft AI (Samvelyan et al., 2019). SMAC currently represents the de facto standard for MARL evaluation (Rashid et al., 2018; 2020; Wang et al., 2021). However, SMAC scenarios exhibit very limited stochastic partial observability due to deterministic observations and low variance in initial states therefore only representing simplified special cases rather than general Dec-POMDP challenges (Lyu et al., 2022; Ellis et al., 2022). To assess practicability of MARL, we need benchmarks with sufficient stochasticity as the real-world is generally messy and only observable through noisy sensors. 
5.2. SMAC with Stochastic Partial Observability 
MessySMAC is a modified version of SMAC with obser-vation stochasticity w.r.t. Ω, where all measured values of observation zt,i are negated with a probability of φ ∈ [0, 1), and initialization stochasticity w.r.t. b0, where K random steps are initially performed before officially starting an episode. During the initial phase, the agents can already be ambushed by the built-in AI, which further increases difficulty compared to the original SMAC maps if K > 0. MessySMAC represents a more general Dec-POMDP chal-lenge which enables systematic evaluation under various stochasticity configurations according to φ and K. 
Fig. 2 shows the PCA visualization of joint observations in two maps of original SMAC (K = 0) and MessySMAC (K = 10) within the first 5 steps of 1,000 episodes using a random policy. In original SMAC, the initial observations of s0 (dark purple) are very similar and can be easily distin-guished from subsequent observations by merely regarding time steps. Therefore, open-loop control might already be sufficient to solve these scenarios satisfactorily as hypoth-esized in (Ellis et al., 2022). However, the distinction of observations by time steps is more tricky in MessySMAC due to significantly higher entropy in b0, indicating higher initialization stochasticity and a stronger requirement for closed-loop control, where agents need to explicitly consider their actual observations to make proper decisions. 
5.3. Comparison with SMACv2 
SMACv2 is an update to the original SMAC benchmark featuring initialization stochasticity w.r.t. position and unit types, as well as observation restrictions (Ellis et al., 2022). SMACv2 addresses similar issues as MessySMAC but MessySMAC additionally features observation stochas-ticity w.r.t. Ω according to the general Dec-POMDP for-mulation in Section 2.1. Unlike MessySMAC, SMACv2 does not support the original SMAC maps thus not enabling direct comparability w.r.t. stochasticity configurations. 
Therefore, SMACv2 can be viewed as entirely new StarCraft II benchmark, while MessySMAC represents a SMAC exten-sion, enabling systematic evaluation under various stochas-ticity configurations for the original SMAC maps. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
60
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Figure 3. Average learning progress w.r.t. the return of AERIAL variants and state-of-the-art baselines in Dec-Tiger over 50 runs. Shaded areas show the 95% confidence interval. 
6. Experiments We use the state-based CTDE implementations of QPLEX, CW-QMIX, OW-QMIX, and QMIX from (Rashid et al., 2020) as state-of-the-art baselines with their default hyperparame-ters. We also integrate MAPPO from (Yu et al., 2022). For all experiments, we report the average performance and the 95% confidence interval over at least 20 runs. 
AERIAL is implemented3 using QMIX as factorization op-erator Ψ according to Fig. 1. We also experimented with QPLEX as alternative with no significant difference in per-formance. Thus, we stick with QMIX for efficiency due to fewer trainable parameters. The transformer of AERIAL has 4 heads with W c 
q , W c k , and W c 
v each having one hid-den layer of datt = 64 units with ReLU activation. The subsequent MLP layers have 64 units with ReLU activation. 
For ablation study, we implement AERIAL (no attention), which trains Ψ directly on ht without self-attention as described in Section 4.2, and AERIAL (raw history), which trains Ψ on the raw joint history τ t concatenated with the true state st as originally proposed for actor-critic methods (Lyu et al., 2022). 
6.1. Dec-Tiger 
Setting We use the Dec-Tiger problem described in Sec-tion 4.1 and (Nair et al., 2003) as simple proof-of-concept domain with T = 4 and γ = 1. We also provide the optimal value of 4.8 computed with MAA* (Szer et al., 2005). 
Results The results are shown in Fig. 3. AERIAL comes closest to the optimum, achieving an average return of about zero. AERIAL (no attention) performs sec-ond best with an average return of about -8, while all other approaches achieve an average return of about -15. 
Discussion The results confirm the example from Section 4.1 and the findings of (Oliehoek et al., 2008; Lyu et al., 
3Code is available at https://github.com/ thomyphan/messy_smac. Further details are in Appendix D. 
2022). All state-based CTDE approaches and AERIAL (raw history) converge to a one-step policy, where both agents optimistically open the same door regardless of any agent observation. AERIAL (no attention) converges to a local optimum most of the time, where both agents only listen for all T = 4 time steps. AERIAL per-forms best due to considering the latent dependencies of all memory representations ht,i ∈ ht via self-attention to learn an adequate representation of multi-agent recurrence Pπ(τ t|b0) according to Eq. 5. 
6.2. Original SMAC 
Setting We evaluate AERIAL in original SMAC using the maps 3s5z and 10m vs 11m, which are classified as easy, as well as the hard maps 2c vs 64zg, 3s vs 5z, and 5m vs 6m, and the super hard map 3s5z vs 3s6z (Samvelyan et al., 2019). 
Results The final average test win rates after 2 million steps of training are shown in Table 1. AERIAL is competi-tive to QPLEX and QMIX in the easy maps, while perform-ing best in 3s vs 5z and 5m vs 6m. MAPPO performs best in 2c vs 64zg and 3s5z vs 3s6z with AERIAL being second best in the super hard map 3s5z vs 3s6z. 
Discussion AERIAL is competitive to state-of-the-art baselines in original SMAC, indicating that replacing the true state st with the joint memory representation ht does not notably harm performance. Despite outperforming most baselines in some maps, we do not claim significant outper-formance here, since we regard most SMAC maps as widely solved by the community anyway (Ellis et al., 2022). 
6.3. MessySMAC 
Setting We evaluate AERIAL in MessySMAC using the same maps as in Section 6.2. We set φ = 15% and K = 10. 
Results The results are shown in Fig. 4. AERIAL per-forms best in all maps with AERIAL (no attention) being second best except in 2c vs 64zg. In 3s5z vs 3s6z, only AERIAL and AERIAL (no attention) progress notably. AERIAL (raw history) performs worst in all maps. MAPPO only progresses notably in 2c vs 64zg. 
Discussion Similar to the Dec-Tiger experiment, the re-sults confirm the benefit of exploiting more accurate closed-loop information in domains with stochastic partial observ-ability. AERIAL consistently outperforms AERIAL (no attention), indicating that self-attention can correct for the naive independence assumption of all ht,i ∈ ht. MAPPO performs especially poorly in MessySMAC due to 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
61
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Table 1. Average win rate of AERIAL and state-of-the-art baselines after 2 million time steps of training across 400 final test episodes for the original SMAC maps with the 95% confidence interval. The best results per map are highlighted in boldface and blue. 
AERIAL QPLEX CW-QMIX OW-QMIX QMIX MAPPO 3s5z 0.95± 0.01 0.94± 0.01 0.87± 0.02 0.91± 0.02 0.95± 0.01 68.7± 0.94 10m vs 11m 0.97± 0.01 0.90± 0.02 0.91± 0.02 0.96± 0.01 0.90± 0.02 77.3± 0.66 2c vs 64zg 0.52± 0.11 0.29± 0.1 0.38± 0.12 0.55± 0.13 0.59± 0.11 90.2± 0.24 3s vs 5z 0.96± 0.02 0.74± 0.11 0.18± 0.06 0.08± 0.04 0.81± 0.05 73.8± 0.44 5m vs 6m 0.77± 0.03 0.66± 0.04 0.41± 0.04 0.55± 0.06 0.67± 0.05 60.6± 1.13 3s5z vs 3s6z 0.18± 0.09 0.1± 0.03 0.0± 0.0 0.02± 0.01 0.02± 0.02 20.5± 2.91 
(a) 3s5z (b) 10m vs 11m (c) 2c vs 64zg 
(d) 3s vs 5z (e) 5m vs 6m (f) 3s5z vs 3s6z 
Figure 4. Average learning progress w.r.t. the win rate of AERIAL variants and state-of-the-art baselines in MessySMAC for 2 million steps over 20 runs. Shaded areas show the 95% confidence interval. The legend at the top applies across all plots. 
its misleading dependence on true states without any credit assignment, confirming the findings of (Ellis et al., 2022). 
6.4. Robustness against Stochastic Partial Observability 
Setting To evaluate the robustness of AERIAL and AERIAL (no attention) against various stochastic-ity configurations in MessySMAC, we manipulate Ω through the observation negation probability φ and b0 through the number of initial random steps K as defined in Section 5.2. We compare the results with QMIX and QPLEX as the best performing state-of-the-art baselines in MessyS-MAC according to the results in Section 6.3. We present summarized plots, where the results are aggregated accross all maps from Section 6.3. To avoid that easy maps dominate the average win rate, since all approaches achieve high val-ues there, we normalize the values by the maximum win rate 
achieved in the respective map for all tested configurations of φ and K. Thus, we ensure an equal weighting regardless of the particular difficulty level. If not mentioned otherwise, we set φ = 15% and K = 10 as default parameters based on Section 6.3. 
Results The results regarding observation stochasticity w.r.t. Ω and φ are shown in Fig. 5. Fig. 5(a) shows that the average win rates of all approaches decrease with in-creasing φ with AERIAL consistently achieving the highest average win rate in all configurations. Fig. 5(b) shows that AERIAL performs best in most MessySMAC maps, especially when φ ≥ 15%. AERIAL (no attention) performs second best. 
The results regarding initialization stochasticity w.r.t. b0 and K are shown in Fig. 6. Analogously to Fig. 5, Fig. 6(a) shows that the average (normalized) win rates of all ap-
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
62
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
(a) normalized test win rate (b) # maps best out of 6 
Figure 5. Evaluation of AERIAL, AERIAL (no attention), and the best MessySMAC baselines for different observation nega-tion probabilities φ affecting observation stochasticity w.r.t. Ω (20 runs per configuration). (a) The average normalized test win rate accross all 6 MessySMAC maps from Section 6.3. (b) The number of maps best out of 6. The legend at the top applies across all plots. 
(a) normalized test win rate (b) # maps best out of 6 
Figure 6. Evaluation of AERIAL, AERIAL (no attention), and the best MessySMAC baselines for different initial random steps K affecting initialization stochasticity w.r.t. b0 (20 runs per configuration). (a) The average normalized test win rate accross all 6 MessySMAC maps from Section 6.3. (b) The number of maps best out of 6. The legend at the top applies across all plots. 
proaches decrease with increasing K with AERIAL consis-tently achieving the highest average win rate in all configura-tions. Fig. 6(b) shows that AERIAL performs best in most MessySMAC maps, especially when K ≥ 10. AERIAL (no attention) performs second best. 
Discussion Our results systematically demonstrate the robustness of AERIAL and AERIAL (no attention) against various stochasticity configurations according to Ω and b0. State-based CTDE is notably less effective in settings, where observation and initialization stochasticity is high. As AERIAL consistently performs best in all maps when φ ≥ 15% or K ≥ 10, we conclude that providing an adequate representation of Pπ(τ t|b0) according to Eq. 5 that is learned, e.g., through ht and self-attention, is more beneficial for CTDE than merely relying on true states when facing domains with high stochastic partial observability. 
7. Conclusion and Future Work To tackle general multi-agent problems, which are messy and only observable through noisy sensors, we need ade-quate algorithms and benchmarks that sufficiently consider stochastic partial observability. 
In this paper, we proposed AERIAL to approximate value functions under stochastic partial observability with a learned representation of multi-agent recurrence, consid-ering more accurate closed-loop information about decen-tralized agent decisions than state-based CTDE. 
We then introduced MessySMAC, a modified version of SMAC with stochastic observations and higher variance in initial states, to provide a more general and configurable Dec-POMDP benchmark regarding stochastic partial ob-servability. We showed visually in Fig. 2 and experimen-tally in Section 6 that MessySMAC scenarios pose a greater challenge than their original SMAC counterparts due to observation and initialization stochasticity. 
Compared to state-based CTDE, AERIAL offers a simple but effective approach to general Dec-POMDPs, being com-petitive in original SMAC and superior in Dec-Tiger and MessySMAC, which both exhibit observation and initializa-tion stochasticity unlike original SMAC. Simply replacing the true state with memory representations can already im-prove performance in most scenarios, confirming the need for more accurate closed-loop information about decentral-ized agent decisions. Self-attention can correct for the naive independence assumption of agent-wise recurrence to fur-ther improve performance, especially when observation or initialization stochasticity is high. 
We plan to further evaluate AERIAL in SMACv2 and mixed competitive-cooperative settings with multiple CTDE in-stances (Lowe et al., 2017; Phan et al., 2020). 
Acknowledgements This work was partially funded by the Bavarian Ministry for Economic Affairs, Regional Development and Energy as part of a project to support the thematic development of the Institute for Cognitive Systems. 
References Amato, C., Bernstein, D. S., and Zilberstein, S. Opti-
mizing Memory-Bounded Controllers for Decentralized POMDPs. In Proceedings of the 23rd Conference on Uncertainty in Artificial Intelligence, pp. 1–8, 2007. 
Bernstein, D. S., Hansen, E. A., and Zilberstein, S. Bounded Policy Iteration for Decentralized POMDPs. In IJCAI, pp. 52–57, 2005. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
63
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Boutilier, C. Planning, Learning and Coordination in Multia-gent Decision Processes. In Proceedings of the 6th confer-ence on Theoretical aspects of rationality and knowledge, pp. 195–210. Morgan Kaufmann Publishers Inc., 1996. 
Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A., Laskin, M., Abbeel, P., Srinivas, A., and Mordatch, I. Decision Transformer: Reinforcement Learning via Se-quence Modeling. In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., and Vaughan, J. W. (eds.), Ad-vances in Neural Information Processing Systems, vol-ume 34, pp. 15084–15097. Curran Associates, Inc., 2021. 
Cho, K., van Merriënboer, B., Bahdanau, D., and Bengio, Y. On the Properties of Neural Machine Translation: Encoder-Decoder Approaches. In Proceedings of SSST-8, Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation, pp. 103–111, 2014. 
Ellis, B., Moalla, S., Samvelyan, M., Sun, M., Mahajan, A., Foerster, J. N., and Whiteson, S. SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning. 2022. 
Emery-Montemerlo, R., Gordon, G., Schneider, J., and Thrun, S. Approximate Solutions for Partially Observ-able Stochastic Games with Common Payoffs. In Pro-ceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems - Volume 1, AAMAS ’04, pp. 136–143, USA, 2004. IEEE Computer Society. ISBN 1581138644. 
Foerster, J., Farquhar, G., Afouras, T., Nardelli, N., and Whiteson, S. Counterfactual Multi-Agent Policy Gradi-ents. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1), Apr. 2018. 
Gupta, J. K., Egorov, M., and Kochenderfer, M. Cooperative Multi-Agent Control using Deep Reinforcement Learning. In Autonomous Agents and Multiagent Systems, pp. 66– 83. Springer, 2017. 
Hausknecht, M. and Stone, P. Deep Recurrent Q-Learning for Partially Observable MDPs. In 2015 AAAI Fall Sym-posium Series, 2015. 
Hochreiter, S. and Schmidhuber, J. Long Short-Term Mem-ory. Neural Computation, 9(8):1735–1780, 1997. 
Hu, H. and Foerster, J. N. Simplified Action Decoder for Deep Multi-Agent Reinforcement Learning. In Interna-tional Conference on Learning Representations, 2019. 
Iqbal, S. and Sha, F. Actor-Attention-Critic for Multi-Agent Reinforcement Learning. In Chaudhuri, K. and Salakhut-dinov, R. (eds.), Proceedings of the 36th International Conference on Machine Learning, volume 97 of Pro-ceedings of Machine Learning Research, pp. 2961–2970, Long Beach, California, USA, 09–15 Jun 2019. PMLR. 
Iqbal, S., De Witt, C. A. S., Peng, B., Boehmer, W., White-son, S., and Sha, F. Randomized Entity-wise Factoriza-tion for Multi-Agent Reinforcement Learning. In Meila, M. and Zhang, T. (eds.), Proceedings of the 38th Inter-national Conference on Machine Learning, volume 139 of Proceedings of Machine Learning Research, pp. 4596– 4606. PMLR, 18–24 Jul 2021. 
Kaelbling, L. P., Littman, M. L., and Cassandra, A. R. Plan-ning and Acting in Partially Observable Stochastic Do-mains. Artificial intelligence, 101(1-2):99–134, 1998. 
Khan, M. J., Ahmed, S. H., and Sukthankar, G. Transformer-Based Value Function Decomposition for Cooperative Multi-Agent Reinforcement Learning in StarCraft. Pro-ceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 18(1):113–119, Oct. 2022. 
Lowe, R., Wu, Y., Tamar, A., Harb, J., Abbeel, P., and Mor-datch, I. Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments. In Guyon, I., Luxburg, U. V., Bengio, S., Wallach, H., Fergus, R., Vishwanathan, S., and Garnett, R. (eds.), Advances in Neural Information Processing Systems, volume 30. Curran Associates, Inc., 2017. 
Lyu, X., Xiao, Y., Daley, B., and Amato, C. Contrasting Centralized and Decentralized Critics in Multi-Agent Re-inforcement Learning. In Proceedings of the 20th Interna-tional Conference on Autonomous Agents and Multiagent Systems, pp. 844–852, 2021. 
Lyu, X., Baisero, A., Xiao, Y., and Amato, C. A Deeper Understanding of State-Based Critics in Multi-Agent Re-inforcement Learning. Proceedings of the AAAI Con-ference on Artificial Intelligence, 36(9):9396–9404, Jun. 2022. doi: 10.1609/aaai.v36i9.21171. 
Nair, R., Tambe, M., Yokoo, M., Pynadath, D., and Marsella, S. Taming Decentralized POMDPs: Towards Efficient Policy Computation for Multiagent Settings. In Proceed-ings of the 18th International Joint Conference on Artifi-cial Intelligence, IJCAI’03, pp. 705–711, San Francisco, CA, USA, 2003. Morgan Kaufmann Publishers Inc. 
Oliehoek, F. A. and Amato, C. A Concise Introduction to Decentralized POMDPs, volume 1. Springer, 2016. 
Oliehoek, F. A., Spaan, M. T., and Vlassis, N. Optimal and Approximate Q-Value Functions for Decentralized POMDPs. Journal of Artificial Intelligence Research, 32: 289–353, 2008. 
Phan, T., Gabor, T., Sedlmeier, A., Ritz, F., Kempter, B., Klein, C., Sauer, H., Schmid, R., Wieghardt, J., Zeller, M., et al. Learning and Testing Resilience in Cooperative 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
64
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Multi-Agent Systems. In Proceedings of the 19th Inter-national Conference on Autonomous Agents and Multia-gent Systems, AAMAS ’20, pp. 1055–1063. International Foundation for Autonomous Agents and Multiagent Sys-tems, 2020. 
Phan, T., Ritz, F., Belzner, L., Altmann, P., Gabor, T., and Linnhoff-Popien, C. VAST: Value Function Factorization with Variable Agent Sub-Teams. In Ranzato, M., Beygelz-imer, A., Dauphin, Y., Liang, P., and Vaughan, J. W. (eds.), Advances in Neural Information Processing Systems, vol-ume 34, pp. 24018–24032. Curran Associates, Inc., 2021. 
Phan, T., Ritz, F., Nüßlein, J., Kölle, M., Gabor, T., and Linnhoff-Popien, C. Attention-Based Recurrency for Multi-Agent Reinforcement Learning under State Uncer-tainty. In Extended Abstracts of the 22nd International Conference on Autonomous Agents and Multiagent Sys-tems, AAMAS ’23, pp. 2839–2841. International Foun-dation for Autonomous Agents and Multiagent Systems, 2023. ISBN 9781450394321. 
Rashid, T., Samvelyan, M., Schroeder, C., Farquhar, G., Foerster, J., and Whiteson, S. QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforce-ment Learning. In Dy, J. and Krause, A. (eds.), Proceed-ings of the 35th International Conference on Machine Learning, volume 80 of Proceedings of Machine Learn-ing Research, pp. 4295–4304. PMLR, 10–15 Jul 2018. 
Rashid, T., Farquhar, G., Peng, B., and Whiteson, S. Weighted QMIX: Expanding Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learn-ing. In Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M. F., and Lin, H. (eds.), Advances in Neural Informa-tion Processing Systems, volume 33, pp. 10199–10210. Curran Associates, Inc., 2020. 
Samvelyan, M., Rashid, T., Schroeder de Witt, C., Farquhar, G., Nardelli, N., Rudner, T. G., Hung, C.-M., Torr, P. H., Foerster, J., and Whiteson, S. The StarCraft Multi-Agent Challenge. In Proceedings of the 18th International Con-ference on Autonomous Agents and Multiagent Systems, AAMAS ’19, pp. 2186–2188, Richland, SC, 2019. Inter-national Foundation for Autonomous Agents and Multia-gent Systems. ISBN 9781450363099. 
Son, K., Kim, D., Kang, W. J., Hostallero, D. E., and Yi, Y. QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning. In Chaudhuri, K. and Salakhutdinov, R. (eds.), Proceed-ings of the 36th International Conference on Machine Learning, volume 97 of Proceedings of Machine Learn-ing Research, pp. 5887–5896. PMLR, 09–15 Jun 2019. 
Sunehag, P., Lever, G., Gruslys, A., Czarnecki, W. M., Zam-baldi, V., Jaderberg, M., Lanctot, M., Sonnerat, N., Leibo, 
J. Z., Tuyls, K., and Graepel, T. Value-Decomposition Networks for Cooperative Multi-Agent Learning based on Team Reward. In Proceedings of the 17th Interna-tional Conference on Autonomous Agents and Multiagent Systems, AAMAS ’18, pp. 2085–2087, Richland, SC, 2018. International Foundation for Autonomous Agents and Multiagent Systems. 
Szer, D., Charpillet, F., and Zilberstein, S. MAA*: A Heuristic Search Algorithm for Solving Decentralized POMDPs. UAI’05, pp. 576–583, Arlington, Virginia, USA, 2005. AUAI Press. ISBN 0974903914. 
Tan, M. Multi-Agent Reinforcement Learning: Independent versus Cooperative Agents. In Proceedings of the Tenth International Conference on International Conference on Machine Learning, ICML’93, pp. 330–337, San Fran-cisco, CA, USA, 1993. Morgan Kaufmann Publishers Inc. ISBN 1558603077. 
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. u., and Polosukhin, I. At-tention is All You Need. In Guyon, I., Luxburg, U. V., Bengio, S., Wallach, H., Fergus, R., Vishwanathan, S., and Garnett, R. (eds.), Advances in Neural Information Processing Systems, volume 30. Curran Associates, Inc., 2017. 
Vinyals, O., Babuschkin, I., Czarnecki, W. M., Mathieu, M., Dudzik, A., Chung, J., Choi, D. H., Powell, R., Ewalds, T., Georgiev, P., et al. Grandmaster Level in StarCraft II using Multi-Agent Reinforcement Learning. Nature, pp. 1–5, 2019. 
Wang, J., Ren, Z., Liu, T., Yu, Y., and Zhang, C. QPLEX: Duplex Dueling Multi-Agent Q-Learning. In Interna-tional Conference on Learning Representations, 2021. 
Watkins, C. J. and Dayan, P. Q-Learning. Machine Learning, 8(3-4):279–292, 1992. 
Wen, M., Kuba, J. G., Lin, R., Zhang, W., Wen, Y., Wang, J., and Yang, Y. Multi-Agent Reinforcement Learn-ing is a Sequence Modeling Problem. arXiv preprint arXiv:2205.14953, 2022. 
Whittlestone, J., Arulkumaran, K., and Crosby, M. The Societal Implications of Deep Reinforcement Learning. Journal of Artificial Intelligence Research, 70:1003–1030, May 2021. ISSN 1076-9757. doi: 10.1613/jair.1.12360. 
Yu, C., Velu, A., Vinitsky, E., Gao, J., Wang, Y., Bayen, A., and Wu, Y. The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games. In 36th Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2022. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
65
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
A. Limitations and Societal Impacts A.1. Limitations 
AERIAL does not significantly outperform state-of-the-art baselines in easier domains without stochastic partial observability as indicated by the original SMAC results in Table 1, implying that simplified Dec-POMDP settings might benefit from more specialized algorithms. The dependence on joint memory representations ht = 〈ht,i〉i∈D might induce some bias w.r.t. agent behavior policies which could limit performance in hard exploration domains therefore requiring additional mechanisms beyond the scope of this work. The full version of AERIAL requires additional compute4 due to the transformer component in Fig. 1 which can be compensated by using a more (parameter) efficient value function factorization operator Ψ, e.g., using QMIX instead of QPLEX. 
A.2. Potential Negative Societal Impacts 
The goal of our work is to realize autonomous systems to solve complex tasks under stochastic partial observability as motivated in Section 1. We refer to (Whittlestone et al., 2021) for a general overview regarding societal implications of deep RL and completely focus on cooperative MARL settings in the following. 
AERIAL is based on a centralized training regime to learn decentralized policies with a common objective. That objective might include bias of a central authority and could potentially harm opposing parties, e.g., via discrimination or misleading information. Since training is conducted in a laboratory or a simulation, the resulting system might exhibit unsafe or questionable behavior when being deployed in the real world due to poor generalization, e.g., leading to accidents or unfair decisions. The transformer component in Fig. 1 might require a significant amount of additional compute for tuning and training therefore increasing overall cost. The self-attention weights of Eq. 9 could be used to discriminate participating individuals in an unethical way, e.g., discarding less relevant groups of individuals according to the softmax output. 
Similar to original SMAC, MessySMAC is based on team battles, indicating that any MARL algorithm mastering that challenge could be misused for real combat, e.g., in autonomous weapon systems to realize distributed and coordinated strategies. Since MessySMAC covers the aspect of stochastic partial observability, successfully evaluated algorithms could be potentially more effective and dangerous in real-world scenarios. 
B. Dec-Tiger Example Given the Dec-Tiger example from Section 4.1 with a horizon of T = 2, the tiger being behind the right door (sR), and both agents having listened in the first step, where agent 1 heard zL and agent 2 heard zR: The final state-based values are defined by Q∗MDP(st,at) = R(st,at). 
Due to both agents perceiving different observations, i.e., zL and zR respectively, the probability of being in state sR is 50% according to the belief state, i.e., b(sR|τ t) = b(sL|τ t) = 1 
2 . Thus, the true optimal Dec-POMDP values for the final time step are defined by: 
Q∗(τ t,at) = ∑ 
st∈S b(st|τ t)R(st,at) 
= 1 
2 (Q∗MDP(sL,at) +Q∗MDP(sR,at)) 
(10) 
The values of Q∗MDP and Q∗ for the final time step t = 2 in the example are given in Table 2. Both agents can reduce the expected penalty when always performing the same action. Therefore, it is likely for MARL to converge to a joint policy that recommends the same actions for both agents, especially when synchronization techniques like parameter sharing are used (Tan, 1993; Gupta et al., 2017; Yu et al., 2022). 
C. Full Algorithm of AERIAL The complete formulation of AERIAL is given in Algorithm 1. Note that AERIAL does not depend on true states st at all, since the experience samples et (Line 23) used for training do not record any states. 
4The additional amount regarding wall clock time was negligible in our experiments though. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
66
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
Table 2. The values of Q∗MDP and Q∗ for the final time step t = 2 in the Dec-Tiger example from Section 4.1. at Q∗MDP(sL,at) Q∗MDP(sR,at) Q∗(τ t,at) 〈li, li〉 −2 −2 −2 〈li, oL〉 -101 +9 -46 〈li, oR〉 +9 -101 -46 〈oL, li〉 -101 +9 -46 〈oL,oL〉 −50 +20 −15 〈oL, oR〉 -100 -100 -100 〈oR, li〉 +9 -101 -46 〈oR, oL〉 -100 -100 -100 〈oR,oR〉 +20 −50 −15 
Algorithm 1 Attention-based Embeddings of Recurrence In multi-Agent Learning (AERIAL) 1: Initialize parameters for 〈Qi〉i∈D and Ψ. 2: for episode m← 1, E do 3: Sample s0, z0, and τ0 via b0 and Ω 4: for time step t← 0, T − 1 do 5: for agent i ∈ D do 6: at,i ← πi(τt,i) {Use argmaxat,i∈Ai 
Qi(τt,i, at,i)} 7: rand ∼ U(0, 1){Sample from uniform distribution} 8: if rand ≤ ε then 9: Select random action at,i ∈ Ai {Explore with ε-greedy} 
10: end if 11: end for 12: at ← 〈at,i〉i∈D 13: Execute joint action at 14: st+1 ∼ T (st+1|st,at) 15: zt+1 ∼ Ω(zt+1|at, st+1) 16: ht ← 〈ht,i〉i∈D {Query memory representations of all agents} 17: Detach ht from computation graph{Avoid additional differentiation through Ψ or Eq. 9} 18: τ t+1 ← 〈τ t,at, zt+1〉 {Concatenate τ t, at, and zt+1} 19: for attention head c← 1, C do 20: attentionc ← attc(ht) {Process individual recurrences according to Eq. 9} 21: end for 22: rect ← MLP( 
∑C c=1 attentionc) {See Section 4.2} 
23: et ← 〈τ t,at, rt, zt+1, rect〉 24: Store experience sample et 25: end for 26: Train Ψ and 〈Qi〉i∈D using all et {See Fig. 1} 27: end for 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
67
Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability 
D. Experiment Details D.1. Computing infrastructure 
All training and test runs were performed in parallel on a computing cluster of fifteen x86 64 GNU/Linux (Ubuntu 18.04.5 LTS) machines with i7-8700 @ 3.2GHz CPU (8 cores) and 64 GB RAM. We did not use any GPU in our experiments. 
D.2. Hyperparameters and Neural Network Architectures 
Our experiments are based on PyMARL and the code from (Rashid et al., 2020) under the Apache License 2.0. We use the default setting from the paper without further hyperparameter tuning as well as the same neural network architectures for the agent RNNs, i.e., gated recurrent units (GRU) of (Cho et al., 2014) with 64 units, and the respective factorization operators Ψ as specified by default for each state-of-the-art baseline in Section 6. We set the loss weight α = 0.75 for CW-QMIX and OW-QMIX. 
For MAPPO, we use the hyperparameters suggested in (Yu et al., 2022) for SMAC, where we set the clipping parameter to 0.1 and use an epoch count of 5. The parameter λ for generalized advantage estimation is set to 1. The centralized critic has two hidden layers of 128 units with ReLU activation, a single linear output, and conditions on agent-specific global states which concatenate the global state and the individual observation per agent. The policy network of MAPPO has a similar recurrent architecture like the local utility functions Qi and additionally applies softmax to the output layer. 
AERIAL is implemented using QMIX as factorization operator Ψ according to Fig. 1. We also experimented with QPLEX as alternative with no significant difference in performance. Thus, we stick with QMIX for computational efficiency due to fewer trainable parameters. The transformer has C = 4 heads c ∈ {1, ..., C} with respective MLPs W c 
q , W c k , and W c 
v , each having one hidden layer of datt = 64 units with ReLU activation. The three subsequent MLP layers of Line 22 in Algorithm 1 have 64 units with ReLU activation. 
All neural networks are trained using RMSProp with a learning rate of 0.0005. 
Thomy Phan, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor, and Claudia Linnhoff-Popien. "Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability". In Proceedings of the 40th International Conference on Machine Learning (ICML). PMLR, 2023. To appear. 
68
A.10. Emergent Escape-based Flocking Behavior using Multi-Agent Reinforcement Learning 
Publication 
Carsten Hahn, Thomy Phan, Thomas Gabor, Lenz Belzner, and Claudia Linnhoff-Popien. "Emergent Escape-Based Flocking Behavior using Multi-Agent Reinforcement Learning". In The 2021 Conference on Artificial Life (ALIFE), pages 598–605, 2019. 
DOI: https://doi.org/10.1162/isal_a_00226 URL: https://direct.mit.edu/isal/proceedings/isal2019/31/598/ 99238 
Contributions 
1. Emergent swarm behavior through self-interested MARL. 
2. Analysis of swarm behavior compared to alternative strategies. 
Credit 
Hahn conceived the concepts and conducted the empirical analysis. Phan initiated the work by stating the hypothesis and discussed the concepts and results. Gabor and Belzner discussed and reviewed the results. Linnhoff-Popien consulted the process and reviewed the results. 
Purpose 
Main focus of Chapter 6 regarding the research question Q6 from Section 1.2. 
69