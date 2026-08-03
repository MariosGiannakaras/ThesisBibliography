> Source: https://arxiv.org/pdf/2301.04299

SoK: Adversarial Machine Learning Attacks and Defences in Multi-Agent Reinforcement Learning 
Maxwell Standen1,2, Junae Kim1, and Claudia Szabo2 
1Defence Science and Technology Group 2The University of Adelaide 
Abstract—Multi-Agent Reinforcement Learning (MARL) is vulnerable to Adversarial Machine Learning (AML) attacks and needs adequate defences before it can be used in real world applications. We have conducted a survey into the use of execution-time AML attacks against MARL and the defences against those attacks. We surveyed related work in the application of AML in Deep Reinforcement Learning (DRL) and Multi-Agent Learning (MAL) to inform our analysis of AML for MARL. We propose a novel perspective to understand the manner of perpetrating an AML attack, by defining Attack Vectors. We develop two new frameworks to address a gap in current modelling frameworks, focusing on the means and tempo of an AML attack against MARL, and identify knowledge gaps and future avenues of research. 
1. Introduction Deep Reinforcement Learning (DRL) has made signif-
icant progress over the past decade, from its start playing Atari games [1], to beating humans in board [2] and video games [3, 4], to now addressing important complex safetycritical challenges such as defending computer systems [5], managing power networks [6] and driving vehicles [7]. This increase in complexity has transitioned from fullyobservable single-agent environments to partially-observable multi-agent environments. However, to realise positive societal impacts, DRL must overcome the major vulnerability in all deep learning systems to Adversarial Machine Learning (AML) attacks [8], which exploit the neural networks that are the fundamental component of deep learning. 
AML identifies vulnerabilities in machine learning algorithms, such as slight human-imperceptible changes to inputs returning significantly different outputs from neural networks [8]. Neural networks are the core of all deep learning, and may generalise to unseen inputs which is key to DRL [1]. Despite existing research interest [9], there are many challenges with the application of AML techniques to Multi-Agent Reinforcement Learning (MARL), Multi-Agent Learning (MAL), and DRL, including discovering effective attacks [10–13] and finding defences that can generalise to unseen attacks [14, 15]. 
AML attacks exist in a large potential solution space. Attacks against supervised image classifiers use approximation techniques such as Fast Gradient Sign Method (FGSM) 
[16] to find adversarial examples for single static images. DRL involves many sequential observations and finding an effective attack requires knowing when, how, and what to attack. Huang et al. [11] showed that approaches such as FGSM attacks were able to attack DRL by altering the observation at every time step. Subsequent research has found attacks that reduced the number of perturbed timesteps required to degrade the agent performance [10, 12, 13], demonstrating the importance of discovering the best attack timing. 
Adversarial training may defend against AML attacks on supervised learning and DRL [15]. Adversarial training uses both original and adversarially produced examples to retrain a vulnerable algorithm. In supervised learning, the retrained algorithm is then more robust against similar future attacks [17]. However, adversarial training in DRL produces a narrow robustness only against the specific attack being used and thus is unable to generalise to other attacks [14]. 
There is a critical need for MARL practitioners to understand the AML attacks and defences [18]. A number of previous works have surveyed the state of AML as applied to DRL [9, 15, 19–21]. However, to the best of our knowledge, there is no work concerning the application of AML against MARL. In this work we address the use of AML techniques on MARL, by employing a new attack perspective called Attack Vector and proposing classifications for AML attacks and defences. Our taxonomy of AML attacks covers how an attack may be deployed, what information it uses, and the attack goal. Our taxonomy of AML defences covers a range of different types of defences, the Attack vectors a defence can counter, when a defence is deployed, and what information a defence requires about an attack. The contributions we make in this work are fivefold: 
 A survey of AML attacks and defences as applied to MARL, DRL, and MAL more broadly. 
 A cyber-security inspired perspective on AML attacks against MARL, Attack Vectors. 
 An improved categorisation on AML defences, which better categorises the different defences against execution-time attacks against MARL. 
 Two new frameworks for modelling AML attacks against DRL that describe combinations of Attack Vectors and attack magnitude, tempo and location. 
 
 
 
 
 
 
 
 
 
 
 An in-depth discussion of future research directions. 
2. Background and Related Work 
We provide a background to MARL. We discuss previous surveys that have covered AML attacks against MARL, DRL, and MAL and existing gaps that we aim to cover. 
2.1. Multi-Agent Reinforcement Learning 
MARL extends DRL to a multi-agent context. Multi-agent environments can be competitive, cooperative, or mixed based on the rewards provided to the agents [22]. Competitive environments include but are not limited to zero-sum rewards, where an increase in one agent’s reward directly reduces another agent’s reward. Cooperative environments include rewards that are completely shared by all agents. Mixed environments may feature a combination of competitive and cooperative elements in their reward structure. An example of a mixed environment is where there are two competing teams, with agents on the same team receiving the same reward and agents on opposing teams vying for a zero-sum reward. 
Two important characteristics of MARL algorithms focus on where the algorithms are trained and executed. Centralised training occurs when all agents are trained on a single system and may exploit this by sharing parameters between agents [23] or using a single critic for all agents [24]. Decentralised training requires agents to coordinate their training and includes examples such as Independent Q-Learning (IQL) [25] and Fully Decentralized MARL with Networked Agents [26]. A centrally executed MARL algorithm operates similar to a single agent algorithm. How-ever, the structure of the centralised multi-agent system may have greater scalability but worse coordination than a single-agent. This trade-off occurs because the centralised multi-agent system reduces the coupling between its components. Decentralised execution occurs when each agent autonomously and independently executes its policy. 
Decentralised MARL [25–27] faces challenges due to the requirement of stationarity for theoretically guaranteed convergence [27]. However, breaking the stationarity requirement does not always lead to failure as demonstrated by IQL [25]. Each agent in the IQL performs its own Q-learning independent of all other agents. Updating individual agent policies in this manner causes the environment to appear non-stationary from each agent’s perspective. However in practice this has been shown to be an effective MARL algorithm in a range of environments [27]. 
While centralised training with centralised execution is very similar to single-agent DRL, existing hierarchical approaches have shown scalability to larger action spaces [28, 29]. CommNet [29] is an example of a centrally-trained centrally-executed MARL algorithm. CommNet shares aggregations of the intermediate outputs between its agents, improving agent coordination. However, CommNet requires centralised execution because of the amount of data being shared and the frequency of inter-agent communication. 
There are many approaches to centralised training decentralised execution [23, 24, 30–35]. Differentiable Inter-Agent Learning (DIAL) [32] learns efficient inter-agent communications. Inter-agent communication allows agents to better coordinate their actions, and is critical in partiallyobservable environments as it allows agents to share information. DIAL learns a communication protocol by directly connecting agents through explicit communication channels and allowing the back-propagation of learning gradients across them. This training requires centralisation, however, it allows the algorithm to find effective communication protocols quicker than random search. To enable decentralised execution, additional noise is added to communication channels during training, to represent the discretisation loss present during execution. Then, during execution, the direct connections between agents are replaced with a discretisation/regularisation unit that converts between the continuous outputs of the agents and discrete messages. 
2.2. Related Work 
There are multiple surveys that focus on AML for DRL [9, 15, 19, 36]. However our analysis has found that these surveys have limited coverage of AML as applied to MARL and MAL [9]. Several surveys focus strongly on Observation Perturbation attacks [9, 19, 36], including on the information used to craft an attack and when an attack should occur. In our analysis of previous work that classifies AML attacks [9, 15] specifically against MARL, we found no surveys that covered AML defences for MARL; we have identified several that covered AML defences for DRL [9, 15, 19, 36]. Our work is unique due to its focus on AML execution-time attacks and defences for DRL, MAL and MARL. 
MAL is a major focus of our work and attacks against it can be highly effective as discussed by Ilahi et al. [9]. Their survey discusses an Observation Perturbation attack against c-MARL by Lin et al. [37] and in competitive environments by Gleave et al. [38]. To build from this work, we have found additional work that investigates attacks against cooperative MARL [37, 39] and cooperative multi-agent supervised learning [40]. We also found a number of AML attacks in competitive MARL [41–45], which is often overlooked due to the focus of AML on direct Observation Perturbations. 
Observation Perturbation attacks against DRL algorithms have been covered by a number of surveys [9, 19, 36]. These have largely focused on the work inspired by Huang et al. [11]. Discovering effective Observation Perturbation attacks with white and black-box information was covered by Chen et al. [19]. Discovering when to attack is a unique problem for AML attacks against DRL and approaches to this question were covered by Ilahi et al. [9]. We believe our work presents the most extensive survey of Observation Perturbation attacks against DRL to date. 
DRL practitioners must understand potential AML attacks and researchers assist in this requirement through the classification of AML attacks such as those proposed in previous work [9, 15]. Ilahi et al. [9] presents a taxonomy based on Markov Decision Processes (MDPs) to categorise
an attack, which uses the major categories of reward space, action space, state space, and agent space to cover both test-time and training-time attacks. Bai et al. [15] classified attacks based on the information an adversary requires to create the attack. However, neither of these classifications support the categorisation of AML attacks unique against MARL, such as attacks against communications in cooperative MARL and adversarial policies in competitive MARL. To address this gap, we have developed a classification of AML attacks against MARL and DRL that covers the means of attack, the aim of the attack, and the knowledge of the target required by an adversary. 
No AML defences for MARL have been covered by previous surveys to the best of our knowledge. To find related work, we consider surveys that cover AML defences for DRL [9, 15, 19, 36]. Ilahi et al. [9] propose a taxonomy that features a number of classifications including adversarial training, defensive distillation, robust learning, and adversarial detection, however it fails to consider Competitive Training, which aims to use a competitor in the environment to train the DRL agent. Our work addresses this gap. Chen et al. [19] also use Input Alteration, which includes the minor categories of various adversarial training, as the alteration covers both test and training time. They further propose two other categories of altering objective function and altering network structure to improve the robustness against AML attacks. However, the examples they use for AML defence are from supervised learning. Bai et al. [15] focussed on adversarial training which was a category in both Ilahi et al. [9] and Chen et al. [19], however Bai et al. restructured adversarial training as a competitive multi-agent problem. This move towards using multi-agent perspectives to better understand AML attacks is one that we expand upon. Adver-sarial Training, Input Alteration, and Robust Learning were categories used by Ren et al. [36]. We have drawn from these existing classifications and our own analyses and present a classification system for defences for both MARL and DRL. 
Our paper is unique in focusing on execution-time AML attacks against DRL and defences against those attacks. Ilahi et al. [9] covered both execution-time and training-time attacks and defences. Chen et al. [19] focused on executiontime attacks against DRL but looked at AML defences for supervised learning. Bai et al. [15] focused on adversarial training as a defence against execution-time attacks in both DRL and supervised learning. Ren et al. [36] covered AML attacks and defences against the whole deep learning field including supervised learning and DRL. Our unique focus allows us to better analyse the problem of defending a DRL algorithm from execution-time attacks. Related work has covered aspects of AML applied to DRL, however there remain gaps in the coverage of existing surveys around AML attacks and defences for MARL, and the classification of AML attacks and defence when applied to DRL and MAL. 
3. Methodology 
We used a literature review methodology based on [46]. We first identified and refined a number of research ques-
tions. From these questions, we identified keywords and constructed search strings. The search strings were used to find relevant papers in top-tier conferences that publish DRL, AML and MAL papers. We augmented this collection by forward snowballing [47] papers on the topic to discover very recent breakthroughs in the topic, for a total of 350 papers. From this collection, we rejected papers that did not match our accept/reject criteria, resulting in 85 papers. Finally we extracted data from these papers using a set of guiding questions, resulting in 57 papers in our final set. 
3.1. Research Questions and Search Strings 
For a broad overview of AML attacks against MARL, MAL, and DRL approaches, our research questions are: 
 RQ1: What AML attacks exploit vulnerabilities in MARL, MAL, and DRL during execution? 
 RQ2: What AML defences mitigate execution-time attacks against MARL, MAL and DRL? 
We used two search strings to find papers that would address our research questions. The first string is "reinforcement AND (training OR learning) AND (adversarial OR attack) and found 160 papers that relate to adversarial attacks and defences against DRL and MARL. The second string is (multiagent OR multi-agent OR (multi AND agent)) AND (policy OR learning) AND (adversarial OR attack) and found 88 papers that relate to adversarial attacks and defences against MAL and MARL. 
We limited our search to high-quality conferences that published work in DRL, MAL, and MARL since 2010. Our search strings were used in Scopus and external proceedings servers where necessary to search the following conferences: 
 Intl. Joint Conference on Autonomous Agents and Multiagent Systems 
 Intl. Conference on Machine Learning 
 Usenix Security Symposium 
 Intl. Joint Conference on Artificial Intelligence 
 Intl. Conference on Learning Representations 
 National Conference of the American Association 
for Artificial Intelligence 
 IEEE Symposium on Security and Privacy 
 ACM Conference on Computer and Communica-
tions Security 
 ACM International Conference on Knowledge Dis-
covery and Data Mining 
 Advances in Neural Information Processing Systems 
This list does not cover 2010 to 2021 for the relevant conferences, as some did not run in some years. 
Finally, we used several well known papers that address our research questions [12, 30, 40] and used a forward snowball search method [47] to find 147 papers that cited them. These papers were chosen because they made significant discoveries that are relevant to our search.
Figure 1. Classification of Adversarial Machine Learning (AML) attacks against Deep Reinforcement Learning (DRL) and the number of papers that considered those categories. 
We identified accept and reject criteria and applied these to the papers in our set. For a paper to be excluded, it must either fail to meet all of the accept criteria or meet any of the reject criteria. Our accept criteria were: 
 Uses either an execution-time adversarial attack or a defence against an execution-time adversarial attack 
 The attack or defence are used on either an offline deep reinforcement learning or a cooperative multiagent decentrally-executable deep learning algorithm 
Our reject criteria were: 
 Number of pages is less than five 
 Does not feature any experimentation 
We define adversarial attacks as the intentional manipulation of aspects of an environment to reduce the performance of a target network and cause a target agent to take irrational or self-defeating actions. We further limit the scope of our study to execution-time attacks. 
4. AML Attacks 
Our analysis of the papers in our set allows us to propose a new classification system for discussing AML attacks, shown in Figure 1. We have identified three important properties of an AML attack, namely, Attack Vector, Information, and Objective. We consider the adversary’s knowledge capability by classifying what information the adversary knows about the target algorithm. We use the standard categories of white-box information [10–14, 37, 40, 41, 44, 48–63], blackbox information [11, 30, 38–40, 43–45, 51, 53, 55, 64–73] as presented by Bai et al. [15], with the additional category for attacks that use no information [74–77]. 
The final category is the Objective of the attack. A common classification are untargeted attacks [14, 40, 41, 49, 
51, 54, 58, 63, 64, 66, 68, 73, 75–77], which do not pursue a specific goal but instead aim to alter the behaviour of an agent. Untargeted misclassification was originally identified in a taxonomy for AML attacks on supervised learning algorithms [78], which also proposed the objective of targeted misclassification. In a DRL context, targeted misclassification means causing the agent to select a specific action [55, 63, 64]. Objectives unique to reinforcement learning methods are state-based and reward-based targets. Attack that use state-based objectives aim to influence the agent to move towards a specific goal state [10, 62, 65, 72]. Reward-based objectives focus on altering the reward returned by the environment during execution and include goals such as maximising the adversary’s reward and minimising the rewards of the targeted agent [10–13, 30, 37–39, 41, 43– 45, 48, 50, 52, 53, 56, 57, 59–61, 64, 67, 69–71, 74]. 
5. AML Attack Vectors 
We have identified five major Attack Vectors that exploit different aspects of MARL, DRL, or MAL during executiontime, namely, Action Perturbation, Observation Perturbation, Communication Perturbation, Malicious Communications, and Natural Adversarial Examples. Adversaries use Action Perturbations against DRL and MARL to alter the action selection of an agent, which affects the state transition function and the observation function. Observation Pertur-bations allows adversaries to directly inject data into an agent, altering the action selected by an agent to induce an adversarial effect. Communication Perturbation intercepts and alters agent communications to attack MAL and MARL. Malicious Communications provides adversarial agents with a communication capability that exploits the use of communications without intercepting or altering existing communications in MARL. Natural Adversarial Examples use the environmental actions of an adversary to alter the state of the environment and indirectly attack a MARL algorithm. 
5.1. Action Perturbation 
Action Perturbations are a form of attack unique to DRL and MARL in which the adversary directly alters the action of an agent. Altering this action reduces the performance of the target agent because the new action will be the worst possible action for that agent based on an adversary’s capability. Additionally, this alteration may cause the environment to transition to a state to which the target agent is unable to optimally act. 
A number of papers consider Action Perturbations [52, 61, 68, 71, 74]. The techniques covered by these papers are presented in Table 1. These techniques are able to use a range of information from white-box [52, 61], blackbox [68, 71], and no information [74]. These techniques generally used a reward-based objective [52, 61, 71, 74] with the exception of an attack using EDGE [68] which was untargeted. Action Perturbation attacks were able to target the state-of-the-art Proximal Policy Optimisation (PPO) algorithm [79] as well as the commonly used Double Deep
TABLE 1. ACTION PERTURBATION ATTACKS 
Attack Name Information for Attack 
Objective of Attack 
Attacked Algorithm(s) 
Frame-work 
Action Space 
Experimental Platform 
Targeted Adversarial Perturbations [71] 
Black-box Reward-based 
PPO MDP Continuous Point-Goal, Car-Goal 
Myopic Action Space (MAS) attack [61] 
White-box Reward-based 
DDQN, PPO MDP Continuous MuJoCo, OpenAI Gym 
Look-ahead Action Space (LAS) attack [61] 
White-box Reward-based 
DDQN, PPO MDP Continuous MuJoCo, OpenAI Gym 
Probabilistic Action Perturbation [74] 
None Reward-based 
DDPG PR-MDP 
Continuous MuJoCo 
Noisy Action Perturbation [74] 
None Reward-based 
DDPG NR-MDP 
Continuous MuJoCo 
EDGE [68] Black-box Untargeted EDGE MDP Discrete, Continuous 
ALE, MuJoCo 
Model-based Attack [52] White-box Reward-based 
D4PG MDP Continuous MuJoCo 
Q-Network (DDQN) [80] and Deep Deterministic Policy Gradient (DDPG) [81] algorithms. MDPs were used as the framework for all of the attacks except for those by Tessler et al. [74], which used MDP variants that modelled Action Perturbation attacks. All of the attacks were demonstrated against continuous action spaces, while EDGE was also shown to be effective against discrete action spaces. 
For attacks on continuous action spaces [52, 61, 68, 71, 74], the perturbation alters the action selection based on the attack magnitude. Action Perturbations may reveal vulnerabilities in the uncertain execution of actions. This risk of uncertain action execution is common to the robotics domain applications, thus the simulation environment Mu-JoCo [82] was used to demonstrate the applicability of the attack [52, 61, 68, 74]. Furthermore, an adversary may be able to use a cyber-physical attack to influence the execution of actions and achieve an Action Perturbation attack. 
Action Perturbation attacks may also reveal weaknesses in the generalisation of an algorithm to states in the environment, which is similar to Natural Adversarial Examples. Both of these vectors aim to move the environment to a state to which the target algorithm non-optimally responds. This vulnerability has explicitly been explored in both discrete [68] and continuous action spaces [74]. 
The vulnerability an Action Perturbation attack exploits cannot easily be identified using the metrics of reward or win rate. However these metrics are commonly used in the evaluation of Action Perturbation attacks [52, 61, 68, 71, 74]. We believe that a metric such as counterfactual regret [83] may better evaluate the effectiveness of Action Perturbation attacks. Regret measures the difference between the action an agent takes and the best possible action it could have taken in hindsight. The regret at the point of attack would indicate the level of vulnerability an algorithm has to a worst case action and the regret in the steps following an attack would indicate the degree of the generalisation vulnerability. 
5.2. Observation Perturbations 
Observation Perturbation attacks, also known as Evasion attacks [84] in supervised learning, expose a vulnerability in an agent that may be exploited by an adversary with the capability of altering the observation received by an agent. This capability requires the adversary to alter the environment [85] or an agent’s sensors through a cyber attack [86]. The adversary induces the agent to take an action that may differ from the original action the agent would have taken based on the unaltered observation. Thus, Observation Perturbations may be a path to achieving Action Perturbation attacks. 
We present many of these Observation Perturbation attacks in Table 8 in the Appendix. This table covers the information used by the attacks and the objective of the attacks. We also cover additional information such as if the attack is a transfer attack [87], which algorithms the attack has been demonstrated against, and the framework that the original paper used when presenting the attack. 
All of the Observation Perturbation attacks that we found altered continuous observation spaces. Many of these attacks were against unstructured images, however an attack was presented that targeted the structured observations of an energy management system of an electric vehicle [51]. The data collected from the vehicle was presented to the agent as a vector of continuous values, which was smaller and contained a greater density of information than images. The empirical results showed the effectiveness of the attack, which suggests that attacks against other structured observations, such as those used in autonomous cyber defence [5], may also be effective. However, the observations in an autonomous cyber defence environment may be discrete and it is unclear how effective these attacks would be against discrete observation spaces. 
We have identified two unique sub-categories of Ob-servation Perturbation attacks based on the magnitude and
localisation of an attack. Patch attacks target a small section of the observation but may use a larger magnitude. Gener-alisation attacks use both a large magnitude and may affect the whole image, but are restricted to ’natural’ alterations of the observation, such as rotations or colour swaps. Patch Attacks occur when a small area of an observation is altered. They are easier to realise than other Observation Perturbation attacks, as an adversary only needs to change a small part of the observation. We believe that the localisation of Patch attacks will reduce their effectiveness compared with other Observation Perturbation attacks of similar magnitude but without the localisation restriction. This comparison has not yet been explored. 
Patch attacks have been demonstrated against supervised learning algorithms [85] and we have found two papers that use this attack against DRL [57, 62]. A Targeted Physical attack [62] controls the appearance of a fixed-size square object that exists in the observation. UniAck [57] generates a universal perturbation that attacks an the interpretation module of a DRL algorithm to identify the non-perturbed region of an image as the cause of the action. Generalisation Attacks use ’natural’ alterations to the observation to degrade the performance of an algorithm. These attacks are untargeted and aim to change the observation in a way that a human could easily adapt. These attacks include changing colours, rotating, introducing compression artefacts, or altering the dimensions of the observation. 
Generalisation attacks vary in their ability to be realised. Rotating a sensor to attack an agent may be easier to achieve than changing the colours that the sensor perceives. Gen-eralisation attacks expose potential weaknesses in a DRL algorithm to basic changes in the environment to which a human would be easily able to adapt. We only found three approaches to generalisation attacks [75–77], that all attacked DDQN and used a MDP framework. 
5.3. Communication Perturbation 
Communication Perturbation exploits vulnerabilities in communications between agents. An adversary may exploit this vulnerability if they are capable of altering the messages sent through explicit channels in a cooperative multi-agent system. Implicit communication uses an agent’s observation of the environment to communicate information, and so perturbation attacks against implicit communication would be considered a type of Observation Perturbation attack. Observation Perturbation overlaps with Communication Per-turbation as an environment may include the message in the observation. Messages sent from other agents may be considered actions and so there is an overlap between Action Perturbation and Communication Perturbation. Separately categorising Communication Perturbation from the other forms of perturbation reveals unique challenges of AML attacks against MARL. 
MARL algorithms find communication protocols that use explicit communication in partially-observed cooperative environments. Techniques such as CommNet [29] use the output of a layer of a neural network from one agent 
as the direct input to a layer in a different agent. Commu-nication Perturbations against this form of communication can be highly effective as shown by Xue et al. [39]. An-other paradigm of communication embeds the messages as continuously-valued observations, thus AML attacks against this form of communication are similar to those used in Patch and other Observation Perturbation attacks. 
Discretely-valued communications are another form of communication that is common to MARL. RIAL [32] treats messages as a part of the action-space, whereas DIAL [32] uses a discretisation/regularisation unit to turn a continuously-valued message into a discrete message. The robustness of discrete messages to AML attack is unclear as all AML attacks that we found attacked continuous observations. 
Two papers consider the Communication Perturbation attack vector [39, 40]. Xue et al. [39] present a reward-based black-box attack against CommNet [29], TarMAC [31], and NDQ [88]. Tu et al. [40] present the only supervised learning algorithm discovered in our search that fits our criteria. They train a decentralised algorithm that uses emergent communications to recognise an object with information from multiple perspectives. An adversary is then introduced that perturbs the communications to reduce the effectiveness of the object recognition algorithm. Tu et al. [40] demonstrated both a white-box attack and transfer black-box attack against Multi-View ShapeNet. 
Communication Perturbation attacks may be more easily realisable than the more commonly explored Obser-vation Perturbation attacks. Cyber security attackers may use a technique called Meddler-In-The-Middle (MITM) [89] which allow them to intercept and alter messages that are sent over a network. The messages sent by MARL agents may be indecipherable to humans, and so the constraints that are normally imposed, such as magnitude of attack or location of attack may not apply. Without these constraints an adversary could completely change the messages sent between agents. This change is similar to Malicious Communication, except that the message is coming from a trusted source. None of the techniques that we found use an unlimited white-box attack against communications, however as communications may make up a small part of an agent’s observation, we believe that its effectiveness may be similar to that of a Patch attack. 
5.4. Malicious Communications 
Malicious Communications exploit the vulnerability that occurs when an adversary is able to send messages to a target agent. Adversarial messages are used by both Mali-cious Communications and Communication Perturbations. However, Malicious Communication attacks craft a new message instead of altering an existing message. An adversary may realise Malicious Communications more easily than Communication Perturbation, as the adversary does not need to intercept and alter an existing message. We believe that defences against Malicious Communications may be
more effective than against Communication Perturbations, as messages do not originate from a trusted source. 
Exploration of Malicious Communications in the literature has been limited [30, 67]. The attacks presented in these papers are limited to using black-box information, however we believe that white-box information could also be used to craft more devastating and effective attacks. Blumenkamp et al. [30] trained then fixed the policy of a MARL system and then trained an adversarial agent, with Malicious Communications capabilities against that system. However, the primary goal of the adversarial agent was to maximise its own reward, with the reduction in performance of the cooperative system being a secondary effect. Qu et al. [67] also took the approach of maximising the adversary’s reward. Their adversary attacked a system of decentralised sensors with a central agent receiving data from those sensors. The cooperative sensors used a fixed policy to determine what information to communicate. 
The communication paradigm employed should influence the effectiveness of Malicious Communications. Broad-cast is the most common communication paradigm in MARL [90], in which all agents send a message that is received by all other agents in the system. Neither of the papers we found used broadcast communications. Blu-menkamp et al. [30] aggregated received messages and propagated this to nearby agents, such that those agents that were closer had a greater effect on the message that was received. Qu et al. [67] used a many-to-one communication where the many sensors were communicating back to the central agent. We believe that a broadcast malicious message should be highly effective because it is able to simultaneously affect all agents in the system. 
5.5. Natural Adversarial Examples 
Natural Adversarial Examples exploit an agent vulnerability by finding naturally occurring environment states and observations that have an adversarial effect on agents. This type of attack is used in competitive MARL to exploit weaknesses in an opponent’s policy. Both Malicious Communication and Natural Adversarial Examples use valid actions in the environment to attack a target, however, Natural Adversarial Examples may only indirectly affect a target. 
This type of attack is the most feasible of all the Attack Vectors considered, however it is also both the most difficult and least effective attack. The only requirement for an adversary is that it can take actions in an environment. However, this attack may be countered by both AML defences and improvements to the DRL agent generalisation. 
An adversary must find states and observations that exist in the environment that have either not been encountered or generalised by the target policy. Several papers we found consider Natural Adversarial Examples [38, 42–45, 54] and their attacks are presented in Table 2 along with the information required for the attack, the objective of the attack, if a transfer attack is used, the algorithms that were attacked, and the framework used in the paper to present the attack. 
Figure 2. Classification of AML defences for DRL and the number of papers that considered those categories. 
A major type of Natural Adversarial Example attack was pioneered by Gleave et al. [38] and extended by Guo et al. [43]. These attacks used competitive MARL against a fixed target policy to find the actions they could perform in the environment that cause the opponent to lose. Gleave et al. [38] use a zero-sum reward to minimise the target’s reward, and found effective strategies in MuJoCo. The extension by Guo et al. [43], that relaxed the zero-sum constraint, was highly effective in Starcraft II environments. 
6. AML Defences 
We consider several categories in the classification of AML defences for MARL, DRL and MAL, namely, the type of defence, when the defence occurs, and what attacks the defence counters. We have identified several types of AML defences that are used to defend MARL and DRL algorithms from AML attacks. These are Adversarial Train-ing, Competitive Training, Robust Learning, Adversarial Detection, Input Alteration, Memory, and Regularisation. When considering when a defence is applied, we identify four general times, namely, during training, during execution before an attack, during an attack, and after an attack. Figure 2 shows our classification. Adversarial Training [15] retrains the original agent against the AML attack. Adversarial training occurs during the training phase of the ML pipeline, and its main purpose is to counter Observation Perturbations. It has also been shown to be effective in countering Communication Perturbations [40]. Table 3 presents the adversarial training techniques and the attack vector countered, the defence’s impact on performance, the algorithms being defended, and the framework the paper used to present the defence. 
We exclude online training from this category despite its potential for performing adversarial training during execution. Online training against an adversary poses a risk
TABLE 2. NATURAL ADVERSARIAL EXAMPLE ATTACKS 
Name of attack Information for attack 
Objective of attack 
Transfer attack 
Attacked algorithms 
Framework 
Failure Search [42] Black-box State-based × D4PG MDP Adversarial Policy [54] White-box Untargeted × PPO MDP Adversarial Policy [38, 43] Black-box Reward-based × PPO SG White-box Adversary [44] White-box Reward-based × KAIST, PARL, 
NANYANG, D3QN MDP 
Black-box Adversary [44] Black-box Reward-based X KAIST, PARL, NANYANG, D3QN 
Failure-MDP 
Antagonists [45] Black-box Reward-based × DQN, QMIX POSG 
as the adversary may influence the data collected from the environment. This adversary-influenced data will be used by the algorithm during the online training process. An adversary may intentionally poison this training data to cause the algorithm to learn a poor policy [91, 92]. Thus online adversarial training needs to handle data poisoning attacks before it can be deployed as an effective defence. 
TABLE 3. ADVERSARIAL TRAINING DEFENCES 
Name of defence 
Counters attacks 
Impact on performance 
Defended algorithm(s) 
Framework 
Adversarial training [77] 
Observation Perturbation 
Negative DDQN MDP 
Robustifying models [40] 
Communication Perturbation 
Positive Multi-View ShapeNet 
N/A 
DQWAE [93] Observation Perturbation 
Positive DQN MDP 
Adversarial training [14] 
Observation Perturbation 
Not evaluated 
A3C MDP 
Adversarial training [94] 
Observation Perturbation 
Not evaluated 
SA-DQN 
MDP 
SA DRL [59] Observation Perturbation 
Positive PPO, DDPG, DQN 
SA-MDP 
RADIAL-RL [95] 
Observation Perturbation 
Mixed DQN, A3C, PPO 
MDP 
Robust training [73] 
Observation Perturbation 
Positive DDQN, DDPG 
MDP 
Adversarial training [49] 
Observation Perturbation 
Not evaluated 
DQN MDP 
PA-ATLA [50] 
Observation Perturbation 
Mixed DQN, A2C, PPO 
MDP 
Competitive Training is similar to Adversarial Training, however instead of training the agent against perturbed observations, the target is trained against an opponent agent. This defence is largely deployed against Natural Adversarial Examples but has also been shown to be effective against Action Perturbations and Communication Perturbations. Ta-ble 4 presents the defences in this category, which attacks the defence counters, the impact on performance, the algorithm being defended, and the framework used by the paper that presented the defence. 
TABLE 4. COMPETITIVE TRAINING DEFENCES 
Name of defence 
Counters attacks 
Impact on performance 
Defended algorithm(s) 
Framework 
RARL [96] Natural Adversarial Examples 
Positive TRPO SG 
Probabilistic Operator [74] 
Action Perturbations 
Not evaluated 
DDPG PR-MDP 
Noisy Operator [74] 
Action Perturbations 
Not evaluated 
DDPG NR-MDP 
Adversary Resistance [43] 
Natural Adversarial Examples 
Not evaluated 
PPO SG 
Adversarial training [44] 
Natural Adversarial Examples 
Positive KAIST, PARL, NANYANG, D3QN 
MDP 
ARTS [45] Natural Adversarial Examples 
Negative DQN, QMIX 
POSG 
MACRL [39] Communication Perturbations 
Not evaluated 
CommNet, TarMAC, NDQ 
Dec-POMDP-Com 
Robust Learning increases the robustness of an agent in an environment. These methods do not consider specific attacks and instead consider robustness against specific adversary capabilities, such as the magnitude of perturbation. Table 5 shows robust learning techniques, their impact on performance, and which algorithm is defended. 
A limitation of our work is that our data collection only found papers that considered the improved robustness in the context of defending against an AML attack. We believe that the robust learning category could be extended to consider approaches that do not consider specific AML adversary capabilities, but instead look at generally improving the robustness of an agent to other conditions such as robustness against non-stationary environments [97]. Input Alteration mitigates an AML attack by removing the adversarial component of the observation or communication. Table 6 shows the input alteration defences, their requirement for adversarial detection, which attacks they counter, their impact on performance, the name of the algorithm being defended, and the framework used by the paper that
TABLE 5. ROBUST LEARNING DEFENCES 
Name of defence Impact on performance 
Defended algorithm(s) 
A2PD [98] Positive DQN CARRL [99] Not evaluated DQN CROP [100] Not evaluated DQN CPPO [101] Positive PPO TRC [102] Positive CPO, TRPO-L 
presented the defence. Methods that do not require the detection of adversarial 
inputs alter the observation based on assumptions about an adversary’s capabilities, such as the magnitude of perturbation. These defences have been considered in supervised learning contexts [103] and we found three Input Alteration defences for DRL [38, 68, 93]. These methods have a risk of removing valuable data from the input that could improve the performance of an agent as shown by the observation masking defence [38]. However, using an auto-encoder did improve the performance over the original agent [93]. 
Methods that detect adversarial inputs are able to more precisely blind the agent to those inputs or sanitise the observation to remove the malicious components. Message filtering was used against both perturbed [39] and malicious communications[104]. However, attacks have been shown to avoid detection [105] in a supervised learning context. We believe that this evasion of detection has yet to be considered in the context of RL. Adversarial Detection identifies either the existence or location of adversarial attacks. Tekgul et al. [58] considers adversarial detection but does not consider how to remove or repair adversarial observations. Regularisation is a method of avoiding overfitting and has been used as a defence against AML attacks through the regularisation of the Lipschitz Constant [107]. Memory allows an agent to operate in a partially observable environment. Deep Recurrent Q-Networks use a Long Short-Term Memory component to remember a latent state representation [108]. This is considered as a potential AML defence in [70], however we believe that further research is required into the potential risks of this defence. An adversary could target the memory component of the algorithm to increase the effectiveness of a single-step attack to impact future steps. 
7. Frameworks 
We discuss the various frameworks that are currently being used to model AML attacks against DRL and MARL. We then identify a number of challenges in these frameworks, and propose two new frameworks that address them. 
7.1. Reinforcement Learning Frameworks 
Agents in reinforcement learning [109] interact with an environment to optimise return. The environment is 
described by a framework, e.g., a Markov Decision Pro-cess (MDP) [110], Partially Observable Markov Decision Process (POMDP) [111], Decentralised Partially Observable Markov Decision Process (DEC-POMDP) [112], Stochastic Game (SG) [113], or a Partially Observable Stochastic Game (POSG) [114]. Table 7 captures the suitability of these frameworks in modelling our identified attack vectors. 
In a MDP [110] (in Definition 1), a single agent is operating in an environment where it is able to observe the state of the entire environment. At each time step, the agent selects a single action from the action space, causing the state to probabilistically transition to a new state. MDPs do not feature an adversary and so are unable to model any AML Attack Vector. Despite this, this framework is the most commonly used for AML in DRL literature [10, 12, 48– 57, 60–62, 64–68, 71, 75, 93, 95, 98–102, 106]. Definition 1. A Markov Decision Process (MDP) is defined 
by the 4-tuple (S,A, T,R), in which S is the set of states, A is the set of actions, T is the state transition function that stochastically maps a state s ∈ S and action a ∈ A to a next state s′ ∈ S such that T (s, a) = s′, and R is the reward function. 
A POMDP [111] (see Definition 2) is an extension of an MDP that separates the state from the observation. In doing so, the agent observes only a part of the state and must infer the true state from partial observations. The addition of partial observability does not improve the ability of the POMDP to represent different AML Attack Vectors because a POMDP does not allow for the modelling of an adversary. Definition 2. A Partially Observable Markov Deci-
sion Process (POMDP) is defined by the 6-tuple (S,A, T,Ω, O,R), in which S is the set of states, A is the set of actions, T is the state transition function that maps a state s ∈ S and action a ∈ A to a next state s′ ∈ S such that s′ = T (s, a), Ω is the set of observations, O is the observation probability function that maps a state s ∈ S and action a ∈ A to an observation o ∈ Ω such that O(s, a) = o, and R is the reward function. 
A DEC-POMDP [112] (see Definition 3) extends a POMDP to cooperative multi-agent environments. Multiple agents act simultaneously in this framework and all agents receive the same reward [115]. The state transition, reward, and observation functions are dependent on the joint actions of all agents in the environment. This framework is used in AML for MARL [30, 37]. However, DEC-POMDPs cannot represent any of the AML Attack Vectors that we have identified because of the fully cooperative nature of DEC-POMDPs. The lack of a competitive reward signal prevents the existence of an adversarial agent which may use an attack vector to affect other agents in the environment. Definition 3. A Decentralised Partially Observable Markov 
Decision Process (DEC-POMDP) is defined by the 7-tuple (I, S, {Ai}, T, {Ωi}, O,R), in which I is the set of agents, S is the set of states, {Ai} is the joint set of action sets, Ai is the action set of agent i ∈ I , T is
TABLE 6. INPUT ALTERATION DEFENCES 
Name of defence Requires Adversarial Detection 
Counters attacks Impact on performance 
Defended algorithm 
Framework 
DQWAE [93] × Observation Per-turbation 
Positive DQN MDP 
Blinding [68] × Natural Adversar-ial Examples 
Not evaluated 
EDGE MDP 
Message Filtering for Robust Cooperation [104] 
X Malicious Communications 
Not evaluated 
Cooperative Agents 
DEC-POMDP 
Instance-based defense [106] 
X Observation Per-turbation 
Not evaluated 
DQN MDP 
Message filter [39] X Communication Pertrubations 
Not evaluated 
CommNet, Tar-MAC, NDQ 
Dec-POMDP-Com 
Observation masking [38] 
× Natural Adversar-ial Examples 
Negative PPO SG 
TABLE 7. REINFORCEMENT LEARNING FRAMEWORKS AND THEIR ABILITY TO MODEL DIFFERENT AML ATTACK VECTORS 
Framework Observation Action Communication Malicious Natural Adversarial Perturbations Perturbations Perturbations Communications Examples 
MDP [110] × × × × × POMDP [111] × × × × × DEC-POMDP [112] × × × × × SG [113] × × × X X POSG [114] × × × X X PR-MDP [74] × X × × × NR-MDP [74] × X × × × SA-MDP [59] X × × × × 
the state transition function that maps a state s ∈ S and joint action {ai} ∈ {Ai} to a next state s′ ∈ S such that s′ = T (s, {ai}), {Ωi} is the joint set of observations, Ωi is the set of observations of agent i ∈ I , O is the joint observation probability function that maps a state s ∈ S and joint action {ai} ∈ {Ai} to a joint observation {oi} ∈ {Ωi} such that O(s, {ai}) = {oi}, and R is the reward function. 
A SG [113] (Definition 4) is focused on multi-agent environments. This framework provides each agent with an independent reward thus allowing competitive, cooperative and mixed multi-agent environments. These environments are able to contain adversaries, providing the framework with the capability of modelling the Natural Adversarial Examples attack vector [38, 43, 96], since other agents take actions that affect the transition of the state. Furthermore, the joint action set may include communication actions that other agents use to perform an AML attack. This allows SGs to represent the Malicious Communications attack vector. Definition 4. A Stochastic Game (SG) is defined by the 
5-tuple (I, S, {Ai}, T, {Ri}), in which I is the set of agents, S is the set of states, {Ai} is the joint set of 
action sets, Ai is the action set of agent i ∈ I , T is the state transition function that maps a state s ∈ S and joint action {ai} ∈ {Ai} to a next state s′ ∈ S such that s′ = T (s, {ai}), {Ri} is the set of reward functions, and Ri is the reward function of agent i ∈ I . A POSG [114] (Definition 5) extends a SG to separate 
agents’ observations from the state similar to what POMDPs do for MDPs. Like the SG, a POSG can model Malicious Communications and Natural Adversarial Examples [45]. Definition 5. A Partially Observable Stochastic 
Game (POSG) is defined by the 7-tuple (I, S, {Ai}, T, {Ωi}, O, {Ri}), I is the set of agents, S is the set of states, {Ai} is the joint set of action sets, Ai is the action set of agent i ∈ I , T is the state transition function that maps a state s ∈ S and joint action {ai} ∈ {Ai} to a next state s′ ∈ S, s′ = T (s, a), {Ωi} is the joint set of observations Ωi for agent i ∈ I , O is the joint observation probability function that maps a state s ∈ S and joint action {ai} ∈ {Ai} to a joint observation {oi} ∈ {Ωi} such that O(s, {ai}) = {oi}, {Ri} is the set of reward functions Ri for agent i ∈ I . Probabilistic Action Robust MDP
7.2. AML for DRL Frameworks 
Many papers that consider AML attacks against DRL use standard frameworks. However, some consider variations of these frameworks to better describe interactions between AML attacks and the targeted agents, such as the State Adversarial MDP (SA-MDP) [59], the Probabilistic Action Robust MDP (PR-MDP) [74], and the Noisy Action Robust MDP (NR-MDP) [74]. 
The PR-MDP [74] (Definition 6) adds an adversary to the standard MDP that is probabilistically able to take an action in place of the original agent. This framework represents Action Perturbations, however as it is single agent and unable to represent adversarial changes to the observation, it cannot represent any other AML attack vector. Definition 6. A Probabilistic Action Robust MDP (PR-
MDP) is defined by the 6-tuple (S,A, T,R, v, α), in which S is the set of states, A is the set of actions, T is the state transition function that maps a state s ∈ S and action a ∈ A to a next state s′ ∈ S such that T (s, a) = s′, R is the reward function, and v is the Probabilistically-Robust (PR) operator such that v(s) = a′ where a′ ∈ A is either an adversarial action with probability α or the agent’s original action with probability 1− α that is executed in the state transition function. 
The NR-MDP [74] (see Definition Definition 7) adds an adversary to the standard MDP that is able to add a perturbation into the action selection of an agent. Like PR-MDPs, NR-MDPs only represent Action Perturbation Attack Vectors. Definition 7. A Noisy Action Robust MDP (NR-MDP) is 
defined by the 6-tuple (S,A, T,R, v,∆), in which S is the set of states, A is the set of actions, T is the state transition function that maps a state s ∈ S and action a′ ∈ A to a next state s′ ∈ S such that T (s, a′) = s′, R is the reward function, and v is the noisy-robust operator such that v(s, a) = a′ where a, a′ ∈ A and |a− a′| < ∆, a′ is the perturbed action that is executed in the state transition function, and ∆ is the magnitude of the perturbation. 
The SA-MDP [59] (Definition 8) adds an adversary to an MDP that is able to alter the state observation that the agent usually receives. The SA-MDP is capable of representing perturbations to the observation through the adversarial state-permutation function and is used as such in the literature [58, 59, 63, 76, 77, 94, 116]. The SA-MDP cannot represent any other AML attack vector due to the restriction on adversaries present in MDPs. Definition 8. A State-Adversarial Markov Decision Process 
(SA-MDP) is defined by the 5-tuple (S,A, T,R, v), in which S is the set of states, A is the set of actions, T is the state transition function that maps a state s ∈ S and action a ∈ A to a next state s′ ∈ S such that T (s, a) = s′, R is the reward function, and v is the adversarial state-permutation function such that v(s) = s′ where 
s, s′ ∈ S, s is the original state and s′ is the state as observed by the agent. This state permutation is only a change to the perception of the agent and does not change the true state of the environment. 
7.3. Proposed AML for MARL Frameworks 
POMDP and DEC-POMDP are suitable frameworks for modelling single-agent and cooperative multi-agent reinforcement learning respectively. However, they are unable to model Malicious Communications or Natural Adversarial Examples. On the other hand, POSGs are able to effectively model both of these Attack Vectors. We thus propose two new frameworks that extend and combine the existing frameworks presented in sections 7.1 and 7.2, namely the Observation Adversarial POSG (OA-POSG) (Definition 9) and Action Robust POSG (AR-POSG) (Definition 10). 
OA-POSG (Definition 9) is the extension of the POSG with adversarially perturbed observations, allowing Obser-vation Perturbations to be applied to any form of multiagent environment. We introduce an observation-adversarial function, vi, for each agent i in the environment. This function perturbs the observation of an agent, similar to the single-agent SA-MDP [59]. We introduce a parameter that captures the magnitude of perturbation, ∆i. This parameter allows us to model the magnitude of change that an adversary may inflict on the observation. OA-POSG features a scope function, Σi, which captures what elements of an observation are perturbed. The tempo function Θ, in the OA-POSG, determines if a particular state will be attacked and captures the concept of when an attack will occur. 
Definition 9. An Observation-Adversarial Partially Observable Stochastic Game (OA-POSG) is defined by the 11-tuple (I, S, {Ai}, T, {Ωi}, O, {Ri}, {vi}, {Θi}, {∆i}, {Σi}) 
 I is the set of agents. The subscript i indicates that parameter or function is unique to the ith agent 
 S is the set of states 
 {Ai} is the joint action space of all agents 
 T is the state transition function that maps a state 
s ∈ S and joint action {ai} ∈ {Ai} to a next state s′ ∈ S such that T (s, a) = s′ 
 {Ωi} is the joint set of observations Ωi 
 O is the joint observation probability function 
 {Ri} is the set of reward functions for all agents 
 Θi is the tempo of attack determines if the obser-
vation of the agent i for a given state s will be perturbed by the function vi 
 ∆i is the maximum magnitude of the change of a single element in the perturbed observation eij ∈ o′i from the original observation oi of agent i 
 Σi is the scope of the attack which determines which elements of the observation oi is perturbed at state s. Σi(s) = {eij}, where element eij ∈ oi will be perturbed by the function vi and any element not in the returned set will not be changed
 {vi} is the set of adversarial observationpermutation functions, such that the observation received by agent i is 
o′i = vi(oi,∆i, {eij}) if Θi(s) ≤ α oi if Θi(s) > α 
We have not found a requirement for a framework that models both input and output perturbations so we do not consider any extensions that would combine either the PR-MDP or NR-MDP with the OA-POSG. The goal of Ob-servation Perturbations is to affect the actions selected by an agent, however Action Perturbations are able to directly alter these actions. Instead, we propose the AR-POSG which combines and extends the PR-MDP, NR-MDP, and POSG to allow the modelling of Action Perturbations in multi-agent environments. 
AR-POSG (Definition 10) features an action-robust operator vi that adversarially perturbs the action of agent i. This allows the action of each agent in the environment to be subject to different perturbations. The action-robust operator is conditioned by Θi and ∆i. Θi is the attack tempo and determines whether action ai is perturbed at state s. ∆i sets a maximum magnitude on the perturbation. Definition 10. An Action-Robust Partially Observable 
Stochastic Game (AR-POSG) is defined by the 10-tuple (I, S, {Ai}, T, {Ωi}, O, {Ri}, {vi}, {Θi}, {∆i}), 
 I is the set of agents. The subscript i indicates that parameter or function is unique to the ith agent 
 S is the set of states 
 {Ai} is the joint action space of all agents 
 T is the state transition function that maps a state 
s ∈ S and joint action {ai} ∈ {Ai} to a next state s′ ∈ S such that T (s, a) = s′ 
 {Ωi} is the joint set of observations Ωi 
 O is the joint observation probability function 
 {Ri} is the set of reward functions for all agents 
 Θi is the tempo of attack determines if the action of 
the agent i for a given state s will be perturbed by the function vi 
 ∆i is the maximum magnitude of change from the perturbed action a′ to the original action ai where a, a′ ∈ Ai of agent i 
 {vi} is the set of action-robust operators, such that the action performed by agent i is 
a′i = vi(oi, ai,∆i) if Θi(s) ≤ α ai if Θi(s) > α 
. 
where ai ∈ Ai is the original action selected by the agent. 
The new frameworks of AR-POSG and OA-POSG enable more sophisticated modelling of execution-time AML attacks against both DRL and MARL. The frameworks allow us to model multiple simultaneous Attack Vectors and are the only frameworks capable of modelling Communication Perturbation attacks to the best of our knowledge. The frameworks enable the modelling of more detail in AML attacks, namely, the tempo, magnitude, and attack locations. 
8. Research Gaps and Challenges 
We focus on new AML attacks that may be effective against DRL and MARL algorithms, and suggest approaches to AML defences that may improve algorithm robustness. 
8.1. Attacks against Multiple Agents 
A major research direction that we have identified is AML attacks against multiple agents. The development and understanding of these attacks allow us to better understand the vulnerability and risks of using MARL. MARL uses both explicit [32] and implicit communications [23] to coordinate the agent behaviours and we believe that a cascading effect on the system may be produced by attacking a single agent. This failure induced by a single agent’s actions is shown by works that present Malicious Communications [39, 40] and Natural Adversarial Example [38, 41–45] attacks. Certain individuals in social networks are able to unduly influence the behaviour of the whole network [117]. Likewise, an attack against an individual agent may disproportionately affect the performance of the whole system. An attack may be more effective based on factors, such as timing and communication protocols. Measuring this impact is a very important research problem that could be used to improve robustness of multi-agent systems against attacks. 
The influence of a single agent in a multi-agent system changes over the course of an episode. We believe that investigating the effect of switching the targeted agent of an attack is an important research direction. Findings may be used to increase the effectiveness of attacks or demonstrate flaws in AML defences that assume all agents are being attacked [39, 104]. Attack such as the Strategically Timed Attack [10] and the Critical Point Attack [12] consider the importance of an action at a particular time step during a game. Extending these to consider the agent importance at a particular time step would allow for more precise attacks against multi-agent systems. 
Multi-agent systems may be homogeneous, in which all agents share an identical policy, or heterogeneous, in which agents have different policies. The relative vulnerability to AML attacks of heterogeneous vs homogeneous systems has yet to be explored. We hypothesise that homogeneous systems are vulnerable based on the increased implicit communication [23] and reduced variance between policies. 
Attacks that use reward-based targeting rely on the target agent attempting to optimise a single reward. A single reward is often used in cooperative MARL for all agents. However, mixed MARL can produce cooperation and coordination due to the use of certain reward functions [118]. We believe that it would be valuable to compare the vulnerability of MARL algorithms that use shared rewards to those that use individual rewards such as COMA [24]. 
8.2. Attack Vectors 
The OA-POSG and AR-POSG frameworks allow research into combining different Attack Vectors that may
produce more effective attacks than those that use a single attack vector. For example, allowing an adversarial agent to both play the opponent and discover Natural Adversarial Examples while simultaneously perturbing inter-agent communications could be much more effective than either of those attacks individually. 
Research into the quantification of the impact of different Attack Vectors on different algorithms and environments would be highly valuable. We believe that attacks that give an adversary direct input to the target agents such as Ob-servation and Communication Perturbations and Malicious Communications may be more effective than those that rely on indirect effects such as Natural Adversarial Examples. 
The enumeration of Attack Vectors has revealed potential gaps in AML attacks against MARL, namely, white-box Malicious Communications, patch attacks, action-based and state-based targeted Communication Perturbation attacks, untargeted Communication Perturbation attacks, action-based and state-based targeted Natural Adversarial Exam-ples. Malicious Communications allow an adversary to send any data to a target which we believe would be devastating as shown by the single-pixel attack in the supervised learning domain [119]. Similarly, the single-pixel attack could be investigated in the Patch Attack vector. Communica-tion Perturbation has only been considered with reward-based targeting. However, no research has been done to our knowledge into targeting actions and states. Further, untargeted Communication Perturbation attacks have not been investigated. Natural Adversarial Examples have been used to target rewards, but no research has been done to see if natural examples exist that could manipulate a target into taking certain actions or moving towards certain states. Being able to convince an adversary to move towards specific states, or take certain actions could have a significant impact on the field of competitive MARL. 
We did not find any requirement for a framework capable of modelling simultaneous Observation Perturbations and Action Perturbations. However, an advantage of investigating simultaneous Observation Perturbations and Action Perturbations may be to find a combined attack that can use a lower magnitude perturbation for both attacks. 
8.3. Quantifying Defence Generalisations 
Measuring the effectiveness of a defence against multiple different attack types would provide insight into practical AML mitigations. Our survey has shown that many AML defences are only evaluated against the attack they were designed to mitigate. DRL trained algorithms are already being used in vital systems and will be subject to a broad range of attacks. AML defences must be able to be deployed to protect these algorithms and it is vitally important that the impact of AML defences be well understood before deployment or risk increasing the overall system vulnerability. We believe that future work can contribute by evaluating the impact of any new defences against AML attacks on the performance of the unattacked algorithm. 
Many defences focus on the training before an attack has occurred. An alternative defences could occur during an attack by identifying and removing adversarial examples. An ideal defence would selectively sanitise an observation to remove adversarial aspects of the observation but retain other important and unattacked information. We believe that using defences before and during an attack will provide better security than either option alone. 
We found a single defence against Action Perturbation [74]. However these defences hold the potential to address both the mitigation of Action Perturbation attacks and to explore resilience in the face of attacks from other vectors. That is if a bad action occurs then the agent should learn how to best recover. This is a vital property for any system that may be operating in the real world. 
8.4. Employing Attacker Metrics in Defence 
In cyber-security, intelligence about the adversary is vital to crafting an appropriate response. To this end, we believe that both identifying the presence of an attack and the properties of the attacker such as preferred Attack Vectors, tempo of attacks, etc. may produce more effective defences. For example, if an attack is periodic, that information can be used to better identify and remove future attacks. 
Another key research direction is using the results of simulated attacks to reduce vulnerabilities. For example, if an attack consistently targets a few key state-action pairs to achieve its goal then more focus should be on those stateactions to reduce the vulnerability in those states. 
9. Conclusion 
There are significant gaps in the research around AML attacks and defences for MARL that need to be addressed, including mitigating AML attacks against multiple agents, the combined effect of multiple AML attacks, quantifying the effectiveness of AML defences, and using knowledge about an attacker to improve AML defences. Our survey has identified numerous Adversarial Machine Learning (AML) attacks and defences for single-agent Deep Reinforcement Learning (DRL) algorithms. However we found few attacks and defences for Multi-Agent Reinforcement Learn-ing (MARL). Beyond the much needed systematisation of knowledge, a key contribution of this work is the perspective of Attack Vectors used to understand attacks by capturing the means by which an adversary might execute an attack, i.e., action, observation, communication perturbations, malicious communications, and natural adversarial examples. Another key contribution of this work is the proposal of two new frameworks, Observation Adversarial Partially Ob-servable Stochastic Game (OA-POSG) and Action Robust Partially Observable Stochastic Game (AR-POSG), which address a gap in the current frameworks being used to research AML in DRL, namely, the inability to model Com-munication Perturbations, the inability to model multiple simultaneous AML attack vectors, and the lack of detail around the tempo, magnitude and location of attacks. Future
work identifies the need for studying attacks against multiple agents, and on quantifying the effectiveness of defences through the use of various metrics. 
References 
[1] V. Mnih, K. Kavukcuoglu, et al., “Playing Atari with Deep Reinforcement Learning,” Deep Learning Workshop, 2013. 
[2] D. Silver, A. Huang, et al., “Mastering the game of Go with deep neural networks and tree search,” Nature, vol. 529, pp. 484–489, Jan. 2016. 
[3] OpenAI, C. Berner, et al., “Dota 2 with Large Scale Deep Reinforcement Learning,” Dec. 2019. 
[4] O. Vinyals, I. Babuschkin, et al., “Grandmaster level in StarCraft II using multi-agent reinforcement learning,” Nature, vol. 575, pp. 350–354, Nov. 2019. 
[5] M. Standen, M. Lucas, et al., “CybORG: A Gym for the Development of Autonomous Cyber Agents,” International Workshop on Adaptive Cyber Defense, 2021. 
[6] A. Marot, I. Guyon, et al., “L2RPN: Learning to Run a Power Network in a Sustainable World NeurIPS2020 challenge design,” June 2020. 
[7] Ó. Pérez-Gil, R. Barea, et al., “Deep reinforcement learning based control for Autonomous Vehi-cles in CARLA,” Multimedia Tools and Applications, vol. 81, pp. 3553–3576, Jan. 2022. 
[8] C. Szegedy, W. Zaremba, et al., “Intriguing properties of neural networks,” International Conference on Learning Representations, 2014. 
[9] I. Ilahi, M. Usama, et al., “Challenges and Coun-termeasures for Adversarial Attacks on Deep Rein-forcement Learning,” IEEE Transactions on Artificial Intelligence, vol. 3, pp. 90–109, Sept. 2021. 
[10] Y.-C. Lin, Z.-W. Hong, et al., “Tactics of Adversarial Attack on Deep Reinforcement Learning Agents,” International Joint Conference on Artificial Intelli-gence, pp. 3756–3762, 2017. 
[11] S. Huang, N. Papernot, et al., “Adversarial Attacks on Neural Network Policies,” International Conference on Learning Representations, 2017. 
[12] J. Sun, T. Zhang, et al., “Stealthy and Efficient Adver-sarial Attacks against Deep Reinforcement Learning,” AAAI Conference on Artificial Intelligence, pp. 5883– 5891, 2020. 
[13] Y. Qiaoben, X. Zhou, et al., “Strategically-timed State-Observation Attacks on Deep Reinforcement Learning Agents,” Workshop on Adversarial Machine Learning, 2021. 
[14] J. Kos and D. Song, “Delving into adversarial attacks on deep policies,” International Conference on Learn-ing Representations, 2017. 
[15] T. Bai, J. Luo, et al., “Recent Advances in Adversarial Training for Adversarial Robustness,” International Joint Conference on Artificial Intelligence, pp. 4312– 4321, 2021. 
[16] I. J. Goodfellow, J. Shlens, et al., “Explaining and Harnessing Adversarial Examples,” International Conference on Learning Representations, 2015. 
[17] A. Madry, A. Makelov, et al., “Towards Deep Learn-ing Models Resistant to Adversarial Attacks,” In-
ternational Conference on Learning Representations, 2018. 
[18] R. S. Siva Kumar, M. Nyström, et al., “Adversarial Machine Learning-Industry Perspectives,” IEEE Se-curity and Privacy Workshops, pp. 69–75, 2020. 
[19] T. Chen, J. Liu, et al., “Adversarial attack and defense in reinforcement learning-from AI security view,” Cybersecurity, vol. 2, pp. 1–22, Mar. 2019. 
[20] A. Prorok, M. Malencia, et al., “Beyond Robustness: A Taxonomy of Approaches towards Resilient Multi-Robot Systems,” 2021. 
[21] O. Eigner, S. Eresheim, et al., “Towards Resilient Artificial Intelligence: Survey and Research Issues,” IEEE International Conference on Cyber Security and Resilience, pp. 536–542, 2021. 
[22] L. Busoniu, R. Babuska, et al., “A Comprehensive Survey of Multiagent Reinforcement Learning,” IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), vol. 38, pp. 156–172, Mar. 2008. 
[23] J. K. Gupta, M. Egorov, et al., “Cooperative multiagent control using deep reinforcement learning,” In-ternational Conference on Autonomous Agents and Multiagent Systems, pp. 66–83, 2017. 
[24] J. Foerster, G. Farquhar, et al., “Counterfactual multiagent policy gradients,” AAAI Conference on Artificial Intelligence, 2018. 
[25] M. Tan, “Multi-agent reinforcement learning: Inde-pendent vs. cooperative agents,” International Con-ference on Machine Learning, pp. 330–337, 1993. 
[26] K. Zhang, Z. Yang, et al., “Fully Decentral-ized Multi-Agent Reinforcement Learning with Net-worked Agents,” International Conference on Ma-chine Learning,, pp. 9340–9371, 2018. 
[27] L. Matignon, G. Laurent, et al., “Independent reinforcement learners in cooperative Markov games: A survey regarding coordination problems,” The Knowl-edge Engineering Review, vol. 27, pp. 1–31, Mar. 2012. 
[28] D. Liu, A. Lamb, et al., “Discrete-Valued Neural Communication,” Advances in Neural Information Processing Systems, pp. 2109–2121, 2021. 
[29] S. Sukhbaatar, A. Szlam, et al., “Learning Multiagent Communication with Backpropagation,” Advances in Neural Information Processing Systems, pp. 2252– 2260, 2016. 
[30] J. Blumenkamp and A. Prorok, “The Emergence of Adversarial Communication in Multi-Agent Rein-forcement Learning,” Conference on Robot Learning, pp. 1394–1414, 2021. 
[31] A. Das, T. Gervet, et al., “TarMAC: Targeted multiagent communication,” International Conference on Machine Learning, pp. 1538–1546, 2019. 
[32] J. N. Foerster, Y. M. Assael, et al., “Learning to Communicate with Deep Multi-Agent Reinforcement Learning,” Advances in Neural Information Process-ing Systems, pp. 2145–2153, 2016. 
[33] S. Iqbal and F. Sha, “Actor-Attention-Critic for Multi-
Agent Reinforcement Learning,” International Con-ference on Machine Learning, pp. 2961–2970, 2019. 
[34] R. Lowe, Y. Wu, et al., “Multi-agent actor-critic for mixed cooperative-competitive environments,” Ad-vances in Neural Information Processing Systems, 2017. 
[35] A. Singh, T. Jain, et al., “Learning when to communicate at scale in multiagent cooperative and competitive tasks,” International Conference on Learning Representations, 2018. 
[36] K. Ren, T. Zheng, et al., “Adversarial Attacks and Defenses in Deep Learning,” Engineering, vol. 6, pp. 346–360, Mar. 2020. 
[37] J. Lin, K. Dzeparoska, et al., “On the Robustness of Cooperative Multi-Agent Reinforcement Learning,” IEEE Security and Privacy Workshops, pp. 62–68, 2020. 
[38] A. Gleave, M. Dennis, et al., “Adversarial Policies: Attacking Deep Reinforcement Learning,” Interna-tional Conference on Learning Representations, 2020. 
[39] W. Xue, W. Qiu, et al., “Mis-spoke or mis-lead: Achieving Robustness in Multi-Agent Communica-tive Reinforcement Learning,” International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS ’22, pp. 1418–1426, 2022. 
[40] J. Tu, T. Wang, et al., “Adversarial Attacks On Multi-Agent Communication,” IEEE/CVF Interna-tional Conference on Computer Vision, pp. 7748– 7757, 2021. 
[41] T. Fujimoto and A. P. Pedersen, “Adversarial Attacks in Cooperative AI,” 2021. 
[42] J. Uesato, B. O’Donoghue, et al., “Adversarial risk and the dangers of evaluating against weak attacks,” International Conference on Machine Learn-ing, pp. 7995–8007, 2018. 
[43] W. Guo, X. Wu, et al., “Adversarial Policy Learn-ing in Two-player Competitive Games,” International Conference on Machine Learning, pp. 3910–3919, 2021. 
[44] A. Pan, Y. Lee, et al., “Improving Robustness of Reinforcement Learning for Power System Control with Adversarial Training,” Oct. 2021. 
[45] T. Phan, T. Gabor, et al., “Learning and testing resilience in cooperative multi-agent systems,” Interna-tional Joint Conference on Autonomous Agents and Multiagent Systems, pp. 1055–1063, 2020. 
[46] B. Kitchenham, O. Pearl Brereton, et al., “Systematic literature reviews in software engineering – A systematic literature review,” Information and Software Technology, vol. 51, pp. 7–15, Jan. 2009. 
[47] C. Wohlin, “Guidelines for snowballing in systematic literature studies and a replication in software engineering,” International Conference on Evaluation and Assessment in Software Engineering, pp. 1–10, 2014. 
[48] Y. Zheng, Z. Yan, et al., “Vulnerability Assessment of Deep Reinforcement Learning Models for Power System Topology Optimization,” IEEE Transactions on Smart Grid, 2021.
[49] V. Behzadan and A. Munir, “Whatever Does Not Kill Deep Reinforcement Learning, Makes It Stronger,” 2017. 
[50] Y. Sun, R. Zheng, et al., “Who Is the Strongest En-emy? Towards Optimal and Efficient Evasion Attacks in Deep RL,” International Conference on Learning Representations, 2021. 
[51] P. Wang, Y. Li, et al., “Adversarial Attacks on Rein-forcement Learning based Energy Management Sys-tems of Extended Range Electric Delivery Vehicles,” June 2020. 
[52] T.-W. Weng, K. D. Dvijotham, et al., “Toward Eval-uating Robustness of Deep Reinforcement Learning with Continuous Control,” International Conference on Learning Representations, 2020. 
[53] P. Chan, Y. Wang, et al., “Adversarial Attack against Deep Reinforcement Learning with Static Reward Im-pact Map,” ACM Asia Conference on Computer and Communications Security, ASIA CCS ’20, pp. 334– 343, 2020. 
[54] X. Wu, W. Guo, et al., “Adversarial Policy Training against Deep Reinforcement Learning,” USENIX Se-curity Symposium, pp. 1883–1900, 2021. 
[55] L. Hussenot, M. Geist, et al., “CopyCAT: Taking Control of Neural Policies with Constant Attacks,” In-ternational Joint Conference on Autonomous Agents and Multiagent Systems, pp. 548–556, 2020. 
[56] R. Praveen Kumar, I. Niranjan Kumar, et al., “Critical State Detection for Adversarial Attacks in Deep Rein-forcement Learning,” IEEE International Conference on Machine Learning and Applications, pp. 1761– 1766, 2021. 
[57] M. Huai, J. Sun, et al., “Malicious Attacks against Deep Reinforcement Learning Interpretations,” KDD, pp. 472–482, 2020. 
[58] B. G. A. Tekgul, S. Wang, et al., “Real-time Ad-versarial Perturbations against Deep Reinforcement Learning Policies: Attacks and Defenses,” Apr. 2022. 
[59] H. Zhang, H. Chen, et al., “Robust Deep Reinforce-ment Learning against Adversarial Perturbations on State Observations,” Advances in Neural Information Processing Systems, pp. 21024–21037, 2020. 
[60] E. Tretschk, S. J. Oh, et al., “Sequential Attacks on Agents for Long-Term Adversarial Goals,” 2018. 
[61] X. Lee, S. Ghadai, et al., “Spatiotemporally constrained action space attacks on deep reinforcement learning agents,” AAAI Conference on Artificial Intel-ligence, pp. 4577–4584, 2020. 
[62] P. Buddareddygari, T. Zhang, et al., “Targeted At-tack on Deep RL-based Autonomous Driving with Learned Visual Patterns,” 2021. 
[63] Y. Qiaoben, C. Ying, et al., “Understanding Adversar-ial Attacks on Observations in Deep Reinforcement Learning,” 2021. 
[64] M. Inkawhich, Y. Chen, et al., “Snooping attacks on deep reinforcement learning,” International Joint Conference on Autonomous Agents and Multiagent Systems, pp. 557–565, 2020. 
[65] Y. Chen, D. Arnold, et al., “Understanding the Safety Requirements for Learning-based Power Systems Op-erations,” Oct. 2021. 
[66] V. Behzadan and A. Munir, “Vulnerability of Deep Reinforcement Learning to Policy Induction At-tacks,” Machine Learning and Data Mining in Pat-tern Recognition, Lecture Notes in Computer Science, pp. 262–275, 2017. 
[67] A. Qu, Y. Tang, et al., “Attacking Deep Reinforce-ment Learning-Based Traffic Signal Control Systems with Colluding Vehicles,” Nov. 2021. 
[68] W. Guo, X. Wu, et al., “EDGE: Explaining Deep Re-inforcement Learning Policies,” Advances in Neural Information Processing Systems, pp. 12222–12236, 2021. 
[69] J. García, R. Majadas, et al., “Learning adversarial attack policies through multi-objective reinforcement learning,” Eng. Appl. Artif. Intell., 2020. 
[70] A. Russo and A. Proutiere, “Optimal Attacks on Reinforcement Learning Policies,” July 2019. 
[71] X. Y. Lee, Y. Esfandiari, et al., “Query-based targeted action-space adversarial policies on deep reinforcement learning agents,” ICCPS, 2021. 
[72] J. Uesato, A. Kumar, et al., “Rigorous agent evaluation: An adversarial approach to uncover catastrophic failures,” International Conference on Learning Rep-resentations, 2019. 
[73] A. Pattanaik, Z. Tang, et al., “Robust Deep Reinforce-ment Learning with adversarial attacks,” International Joint Conference on Autonomous Agents and Multia-gent Systems, pp. 2040–2042, 2018. 
[74] C. Tessler, Y. Efroni, et al., “Action robust reinforcement learning and applications in continuous control,” International Conference on Machine Learning, pp. 10846–10855, 2019. 
[75] E. Korkmaz, “Daylight: Assessing Generalization Skills of Deep Reinforcement Learning Agents,” 2020. 
[76] E. Korkmaz, “Assessing Deep Reinforcement Learn-ing Policies via Natural Corruptions at the Edge of Imperceptibility,” Sept. 2021. 
[77] E. Korkmaz, “Adversarial Training Blocks General-ization in Neural Policies,” NeurIPS Workshop on Distribution Shifts: Connecting Methods and Appli-cations, 2021. 
[78] N. Papernot, P. McDaniel, et al., “The Limitations of Deep Learning in Adversarial Settings,” IEEE Euro-pean Symposium on Security and Privacy, pp. 372– 387, 2016. 
[79] J. Schulman, F. Wolski, et al., “Proximal Policy Op-timization Algorithms,” Aug. 2017. 
[80] H. van Hasselt, Y. Doron, et al., “Deep Reinforcement Learning and the Deadly Triad,” Dec. 2018. 
[81] T. P. Lillicrap, J. J. Hunt, et al., “Continuous control with deep reinforcement learning,” July 2019. 
[82] E. Todorov, T. Erez, et al., “MuJoCo: A physics engine for model-based control,” IEEE/RSJ Interna-tional Conference on Intelligent Robots and Systems,
pp. 5026–5033, 2012. [83] M. Zinkevich, M. Johanson, et al., “Regret Min-
imization in Games with Incomplete Information,” Advances in Neural Information Processing Systems, 2007. 
[84] E. Tabassi, K. J. Burns, et al., “A taxonomy and terminology of adversarial machine learning,” preprint 8269, National Institute of Standards and Technology, Gaithersburg, Maryland, USA, Oct. 2019. 
[85] T. B. Brown, D. Mané, et al., “Adversarial Patch,” Conference on Neural Information Processing Sys-tems, 2017. 
[86] A. Ferdowsi, U. Challita, et al., “Robust Deep Rein-forcement Learning for Security and Safety in Au-tonomous Vehicle Systems,” International Confer-ence on Intelligent Transportation Systems, pp. 307– 312, 2018. 
[87] A. Demontis, M. Melis, et al., “Why Do Adversar-ial Attacks Transfer? Explaining Transferability of Evasion and Poisoning Attacks,” USENIX Security Symposium, pp. 321–338, 2019. 
[88] T. Wang, J. Wang, et al., “Learning Nearly Decom-posable Value Functions via Communication Min-imization,” International Conference on Learning Representations, 2020. 
[89] D. Poddebniak, F. Ising, et al., “Why TLS is better without STARTTLS: A Security Analysis of START-TLS in the Email Context,” USENIX Security Sym-posium, 2021. 
[90] C. Zhu, M. Dastani, et al., “A Survey of Multi-Agent Reinforcement Learning with Communication,” Mar. 2022. 
[91] P. Kiourti, K. Wardega, et al., “TrojDRL: Evalua-tion of Backdoor Attacks on Deep Reinforcement Learning,” ACM/IEEE Design Automation Confer-ence, pp. 1–6, 2020. 
[92] Y. Han, D. Hubczenko, et al., “Adversarial Reinforce-ment Learning under Partial Observability in Au-tonomous Computer Network Defence,” International Joint Conference on Neural Networks, pp. 1–8, 2020. 
[93] K. Ohashi, K. Nakanishi, et al., “Deep Adversarial Reinforcement Learning With Noise Compensation by Autoencoder,” IEEE Access, vol. 9, pp. 143901– 143912, 2021. 
[94] E. Korkmaz, “Investigating vulnerabilities of deep neural policies,” Conference on Uncertainty in Ar-tificial Intelligence, pp. 1661–1670, 2021. 
[95] T. Oikarinen, W. Zhang, et al., “Robust Deep Rein-forcement Learning through Adversarial Loss,” Ad-vances in Neural Information Processing Systems, pp. 26156–26167, 2021. 
[96] L. Pinto, J. Davidson, et al., “Robust adversarial reinforcement learning,” International Conference on Machine Learning, pp. 4310–4319, 2017. 
[97] E. Lecarpentier and E. Rachelson, “Non-stationary markov decision processes a worst-case approach using model-based reinforcement learning,” Advances in Neural Information Processing Systems, 2019. 
[98] X. Qu, A. Gupta, et al., “Adversary Agnostic Robust Deep Reinforcement Learning,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–12, 2021. 
[99] M. Everett, B. Lütjens, et al., “Certifiable Robustness to Adversarial State Uncertainty in Deep Reinforce-ment Learning,” IEEE Transactions on Neural Net-works and Learning Systems, pp. 1–15, 2021. 
[100] F. Wu, L. Li, et al., “CROP: Certifying Robust Poli-cies for Reinforcement Learning through Functional Smoothing,” International Conference on Learning Representations, 2022. 
[101] C. Ying, X. Zhou, et al., “Towards Safe Reinforce-ment Learning via Constraining Conditional Value at Risk,” Workshop on Adversarial Machine Learning, 2021. 
[102] D. Kim and S. Oh, “TRC: Trust Region Condi-tional Value at Risk for Safe Reinforcement Learn-ing,” IEEE Robotics and Automation Letters, vol. 7, pp. 2621–2628, Apr. 2022. 
[103] C. Guo, M. Rana, et al., “Countering Adversarial Images using Input Transformations,” International Conference on Learning Representations, 2018. 
[104] R. Mitchell, J. Blumenkamp, et al., “Gaussian process based message filtering for robust multi-agent cooperation in the presence of adversarial communication,” 2020. 
[105] N. Carlini and D. Wagner, “Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods,” ACM Workshop on Artificial Intelligence and Security, pp. 3–14, 2017. 
[106] J. García and I. Sagredo, “Instance-based defense against adversarial attacks in Deep Reinforcement Learning,” Engineering Applications of Artificial In-telligence, vol. 107, p. 104514, Jan. 2022. 
[107] X. Tang, Z. Qin, et al., “A deep value-network based approach for multi-driver order dispatching,” ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 1780–1790, 2019. 
[108] M. Hausknecht and P. Stone, “Deep Recurrent Q-Learning for Partially Observable MDPs,” AAAI Fall Symposium Series, 2015. 
[109] L. P. Kaelbling, M. L. Littman, et al., “Reinforcement Learning: A Survey,” Journal of Artificial Intelligence Research, vol. 4, pp. 237–285, May 1996. 
[110] R. Bellman, “A Markovian Decision Process,” Jour-nal of Mathematics and Mechanics, vol. 6, no. 5, pp. 679–684, 1957. 
[111] K. J. Åström, “Optimal Control of Markov Pro-cesses with Incomplete State Information I,” Journal of Mathematical Analysis and Applications, vol. 10, pp. 174–205, 1965. 
[112] D. S. Bernstein, S. Zilberstein, et al., “The Com-plexity of Decentralized Control of Markov Decision Processes,” Jan. 2013. 
[113] L. Shapley, “Stochastic games,” National Academy of Sciences of the United States of America, vol. 39, pp. 1095–1100, Jan. 1953.
[114] E. Hansen, D. Bernstein, et al., “Dynamic Program-ming for Partially Observable Stochastic Games,” AAAI Workshop - Technical Report, June 2004. 
[115] F. A. Oliehoek and C. Amato, A Concise Intro-duction to Decentralized POMDPs. SpringerBriefs in Intelligent Systems, Cham: Springer International Publishing, 2016. 
[116] E. Korkmaz, “Non-Robust Feature Mapping in Deep Reinforcement Learning,” Workshop on Adversarial Machine Learning, 2021. 
[117] Y. Yang and G. Xie, “Efficient identification of node importance in social networks,” Information Process-ing & Management, vol. 52, pp. 911–922, Sept. 2016. 
[118] N. Jaques, A. Lazaridou, et al., “Social Influence as Intrinsic Motivation for Multi-Agent Deep Re-inforcement Learning,” International Conference on Machine Learning, pp. 5372–5381, 2019. 
[119] J. Su, D. V. Vargas, et al., “One pixel attack for fooling deep neural networks,” IEEE Transactions on Evolutionary Computation, vol. 23, pp. 828–841, Oct. 2019. 
Appendix 
In Table 8, we present a list of Observation Perturba-tion attacks focusing on the attack information, the attack objective, whether the attack is transferred, the algorithms that are attacked, and the framework used by the paper that presented the attack. 
Observation Perturbation attacks require carefully crafted alterations to induce an adversarial effect. AML attacks against supervised learning algorithms may use the Fast Gradient Sign Method (FGSM) [16] or Projected Gra-dient Descent (PGD) [17], and are commonly used to craft Observation Perturbation attacks [11, 14, 40, 41, 56, 63]. Other methods find universal perturbations [55, 57, 58]. However, some algorithms have been presented to focus on the unique characteristics of DRL. Chan et al. [53] used a Static Reward Impact Map to generate an attack by evaluating the impact that perturbations of different features had on the cumulative reward of an agent. Other methods use DRL to craft observation perturbations [12, 13, 60, 70]. The other set of methods use the the gradient of the Q-value to craft an attack [56, 59, 73]. 
The timing of an attack has been shown to be a key factor in the success of that attack [10–13]. The simplest timing is the uniform attack [11], which attacks at every time step. More efficient attacks wait until the value of a state or action is above a certain threshold [10, 13]. The number of time steps can further be decreased by considering the future effects of an attack [12].
TABLE 8. OBSERVATION PERTURBATION ATTACKS 
Name of attack Information for attack 
Objective of attack 
Transfer attack 
Target algorithm(s) Framework 
SRIMA [53] Black-box Reward-based X DQN, PPO MDP Adversarial Examples [11] Black-box Reward-based X A3C, TRPO, DQN None CopyCAT [55] Black-box Action X DQN MDP Critical State Detection [56] White-box Reward-based × A3C MDP VF [14] White-box Untargeted × A3C None MO-RL attack [69] Black-box Reward-based × MODQN MDP Optimal Attack [70] Black-box Reward-based × DDPG, DRQN POMDP OSFW(U) [58] White-box Untargeted × DQN, PPO, A3C SA-MDP UAP [58] White-box Untargeted × DQN, PPO, A3C SA-MDP RS [59] White-box Reward-based × PPO, DDPG, DQN SA-MDP MAD [59] White-box Reward-based × PPO, DDPG, DQN SA-MDP Naive Adversarial attack [73] Black-box Untargeted × DDQN, DDPG None Gradient based attack [73] White-box Reward-based × DDQN, DDPG None ATN [60] White-box Reward-based × DQN MDP Snooping attack [64] Black-box Untargeted X DQN, PPO MDP Antagonist Attack [12] White-box Reward-based × A3C, DDPG, PPO MDP Critical Point Attack [12] White-box Reward-based × A3C, DDPG, PPO MDP Tentative Frame Attack [13] White-box Reward-based × PPO SS-MDP STA [10] White-box Reward-based × DQN, A3C MDP EA [10] White-box State-based × DQN, A3C MDP Two-stage attack [63] White-box Untargeted × DQN, A2C, PPO SA-MDP Grid Manipulation Attack [65] Black-box State-based × D3QN, PPO, A2C MDP Action Distortion Attack [65] Black-box State-based × D3QN, PPO, A2C MDP Criticality-Based Adversarial Perturbation [48] 
White-box Reward-based × DQN MDP 
Policy Induction Attack [66] Black-box Untargeted X DQN MDP Contiguous attack [49] White-box Untargeted × DQN MDP PA-AD [50] White-box Reward-based × DQN, A2C, PPO MDP OWR [37] White-box Reward-based × QMIX DEC-POMDP FGSM-based attack [51] White-box Untargeted × DQN, IQN MDP FD Method[51] Black-box Untargeted × DQN, IQN MDP Model Based Attack [52] White-box Reward-based × D4PG MDP Attacks on Beliefs [41] White-box Reward-based × CAPI PuB-MDP