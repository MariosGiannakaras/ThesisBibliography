Cooperative Resilience in Artificial Intelligence Multiagent Systems 
Manuela Chacon-Chamorro Luis Felipe Giraldo Nicanor Quijano Vicente Vargas-Panesso 
César González Juan Sebastián Pinzón Rubén Manrique Manuel Ŕıos Yesid Fonseca 
Daniel Gómez-Barrera Mónica Perdomo-Pérez ∗ 
September 25, 2024 
Abstract 
Resilience refers to the ability of systems to withstand, adapt to, and recover from disruptive events. While studies on resilience have attracted significant attention across various research domains, the precise definition of this concept within the field of cooperative artificial intelligence remains unclear. This paper addresses this gap by proposing a clear definition of ‘cooperative resilience’ and outlining a methodology for its quantitative measurement. The methodology is validated in an environment with RL-based and LLM-augmented autonomous agents, subjected to environmental changes and the introduction of agents with unsustainable behaviors. These events are parameterized to create various scenarios for measuring cooperative resilience. The results highlight the crucial role of resilience metrics in analyzing how the collective system prepares for, resists, recovers from, sustains well-being, and transforms in the face of disruptions. These findings provide foundational insights into the definition, measurement, and preliminary analysis of cooperative resilience, offering significant implications for the broader field of AI. Moreover, the methodology and metrics developed here can be adapted to a wide range of AI applications, enhancing the reliability and effectiveness of AI in dynamic and unpredictable environments. 
Keywords: Cooperative AI, Cooperative resilience, Large Language Model, Melting Pot 2.0, Reinforcement Learning, Social dilemma 
1 Introduction 
Understanding how systems withstand and adapt to adversity has become a focal point for researchers. This capability is referred to as resilience. The concept of resilience has been extensively explored across various domains, ranging from game theory [1–4], artificial intelligent (AI) systems [5–9], engineering [10–12], psychology [13–18], economy [19–21], social science [22, 23], network science [24–26], dynamical systems theory [27, 28], and ecology [29–31]. Particular interest lies in understanding how systems that involve collective action, whether from humans, machines, or both, exhibit resilience as an emergent property from their interactions. These systems are encompassed within the domain of cooperative AI. 
Cooperative AI systems operate in complex, dynamic environments [32]. Interactions with various actors, whether human or machine, add further complexity and uncertainty. This makes them more susceptible to disruptions and failures, as they must continually adapt to changes while maintaining efficient responses [6,11, 25]. Consequently, understanding and transferring the concept of resilience from other domains to cooperative AI systems is crucial. Doing so can inspire the development robust AI architectures and methodologies [33]. Emphasizing resilience ensures that these systems remain adaptable and persistent in the face of disruptions. 
While the concept of resilience has been studied extensively across various domains, its definition in the context of cooperative AI problems remains unclear. This situation represents a need not only to contribute 
∗This work was supported by Google through the Google Research Scholar program and the UniAndes-DeepMind Scholarship 2023. M. Chacon-Chamorro (m.chaconc), L.F. Giraldo (lf.giraldo404), N. Quijano (nquijano), V. Vargas-Panesso (jv.vargas), C. González (cl.gonzalezg), J.S. Pinzón (js.pinzonr), R. Manrique (rf.manrique), Y. Fonseca (y.fonseca) and D. Gómez-Barrera (df.gomezb) are with the Universidad de los Andes, Colombia [@uniandes.edu.co]. M. Ŕıos (manrios) is with Center of Excellence in Analytics and Artificial Intelligence Bancolombia [@bancolombia.com.co]. M. Perdomo-Pérez (tatiana.perdomo) is with the Universidad de Ibagué, Colombia [@unibague.edu.co]. 
1 
 
 
 
 
 
 
 
 
 
 
to unifying terminology in this field but also to understand how the capacity to withstand adversity emerges in systems of this nature. Furthermore, to characterize these systems and enhance their resilience capacity, it is necessary to establish a method for quantifying this property. This method should provide a measurable value that must be related to the definition of the concept. 
Several indicators have been proposed to quantify resilience. For instance, in critical infrastructure [34–37], or in community systems [38, 39]. Through a review of such metrics, two general approaches for quantifying resilience emerge. The first approach involves analyzing time-dependent measures to establish the system’s performance and compare it against its performance during disruptive events. The second approach involves resilience indices, using instantaneous measures of dimensions linked to the system’s performance. These measures can be estimated before, during, or after the disruptive event and are used to assess changes in the system’s performance [37, 38]. While the proposed measures aim to quantify resilience, they often lack guidance on applying this concept across various domains. This gap is particularly challenging in environments where collective interactions between humans, machines, or both are crucial to cooperative AI. 
To fill this gap, the first contribution of this paper is to define the concept of resilience in cooperative AI. This definition is consistent with the work in [32], which unified concepts in cooperative AI. As we explain later in the paper, each element of this definition provides an important aspect of the concept of cooperative resilience. Also, we introduce a methodology to quantify cooperative resilience that aligns with the proposed definition, establishing a series of characteristics, assumptions, and stages designed to quantify cooperative resilience. The proposed methodology is crafted to be adaptable across various contexts, aiming to characterize resilience within cooperative AI systems. This approach will aid in understanding the emergence of resilience and guide strategies for enhancing it. 
The proposed methodology is then validated through experiments conducted in the field of cooperative AI. The experiments are developed in Melting Pot 2.0 [40], a multiagent domain for studying scenarios in which social dilemmas can arise. In particular, we study the Common Harvest Open scenario. In this scenario, agents interact with a resource patch of apple trees that regenerate based on current availability. This configures a social dilemma: if all apples are consumed, no more will grow, so agents must have a social understanding of their actions to avoid overharvesting and ensure the resource’s sustainability. The experiments utilize agents based on Reinforcement Learning (RL) and Large Language Models (LLM) to explore this dilemma. Two disruptive events are tested: environmental changes and the introduction of agents with unsustainable behaviors. This scenario is particularly useful for evaluating cooperative resilience because it highlights how agents’ collective well-being and the system’s ability to handle disruptions are interrelated. The experimental results show that the proposed metric highlights aspects of agents’ ability to resist, adapt, and transform in the face of disruptions, which other metrics may overlook. 
This document is organized as follows: in Section 2 the definition of cooperative resilience and the analysis of key elements is presented. Section 3 introduces the proposed methodology for measuring cooperative resilience. Section 4 elaborates on specific examples applying the suggested methodology. These three sections aim to establish an understanding of the cooperative resilience concept and provide a framework for measurement aligned with the definition. Finally, conclusions and further discussions are presented in Section 5. 
2 Defining Cooperative Resilience 
Several key factors from definitions of resilience across various disciplines contribute to defining cooperative resilience. The essence of defining resilience lies in identifying the resilient entity (who?), the actions that define resilience (what is it?), and recognizing the disruptive event (to what?). These key questions, along with their corresponding keywords, are illustrated in Fig. 1. This figure summarizes a review of resilience concepts across various fields and demonstrates the broad scope of the concept across multiple disciplines1. In the figure, fields are represented as blue nodes, while the guiding questions are shown as nodes in orange (who?), green (to what?), and purple (what is it?). The edges illustrate the relationships between the fields and these questions, as well as the interdisciplinary connections of the concept. 
For instance, in ecology, resilience is related to verbs such as absorb, transform, and respond [30]. It encompasses elements such as resistance and latitude, representing the extent to which a system can be 
1See the detailed review in the supplementary file. 
2
Figure 1: Keyword map of resilience across diverse fields and contexts, addressing guiding questions. 
altered before losing its capacity to recover, as well as stability [29, 31]. Here, the resilient entity is an ecological system, and the disruptive event involves disruptions in population dynamics [30]. In engineering, these disruptions often involve failures [41, 42], errors, or adversarial attacks [6, 7], with resilience linked to terms like resist, recover, and adapt [10, 11, 43, 44]. In psychology, a resilience entity spans from individuals to groups such as families and communities [13–16,45,46], with disruptions related with stress, threats, and disturbances that are embedded in life events [13–16]. In economics, resilience is linked with actions such as withstand, grow, or resist and the disruptions are associated with terms like risk, crisis, and change, and [19–21]. Resilience in dynamic systems pertains to how these systems respond to disturbances that can include external factors, changes in initial conditions, or variations in parameters [27,28]. In network science, the resilient entity could be clusters of interacting agents responding to disturbances, and the disruptions can include failures, errors, threats, or changes in their environment [24–26]. 
In each field of study, resilience is defined by a resilient entity, a disruptive event affecting its normal behavior, and verbs describing the entity’s actions before, during, and/or after the disruption. Based on a literature review covering the concept of resilience across diverse fields, emphasizing the previously mentioned key elements and considering the scope and terminological unification in cooperative AI [32], we introduce a novel concept aligned with cooperation paradigms: ‘cooperative resilience,’ proposed in Definition 1. 
Definition 1 Cooperative resilience is the ability of a system, involving the collective action of individuals —whether humans, machines, or both— to anticipate, prepare for, resist, recover from, and transform in the face of disruptive events that threaten their joint welfare. 
In Definition 1, the resilience entity is identified as a system comprising a collective of individuals, whether humans or machines, interacting with each other. This definition incorporates five key actions: anticipate, prepare, resist, recover, and transform. These verbs represent critical moments that span from the 
3
pre-disruptive event stage to its subsequent management. By including these verbs, resilience is analyzed not only as an inherent system capability but also as a process composed of a series of fundamental stages. In particular, the verbs ‘anticipate’ and ‘prepare’ are related to the static capabilities of resilience, often referred to as capitals in the literature [38]. 
Additionally, resilience also encompasses a reinforcement effect, wherein disruptive events experienced by a system could lead to learning about how to react, act, and prepare for future occurrences. The ability to transform is included as part of promoting either a positive, neutral, or negative change in the system’s performance and how it attains a different configuration. These aspects are inspired in psychology and economics, where systems exhibit resilience when strategies are developed to confront disruptive events and foster growth. The notion of growth is relevant in defining resilience, often referred to as the capacity to exploit opportunities. 
The last part in Definition 1 focuses on the aspect of the expected behavior of the system in absence of disruptive events. This factor is crucial for measuring and interpreting resilience in any context. To assess how resilient a system is, it is necessary not only to characterize its prior configuration, but also to approach the concept from the dynamics of the system’s performance and how this expected behavior should manifest. It is additionally emphasized that disruptive events pose a risk to the collective well-being of the system, implying that the expected behavior will be addressed in terms of joint welfare. This consideration is introduced with the recognition that “AI research is aimed at helping individuals, both humans and machines, find ways to enhance their joint welfare,” [32] as highlighted in the cooperative AI approach. 
Also, Definition 1 specifies that disruptive events pose a risk, emphasizing the stochastic nature inher-ent in these occurrences. In resilience literature, a disruptive event is identified as a phenomenon that could be external, internal, or even an attack on the resilient entity, disturbing its normal operational con-ditions. Given the entity’s focus, the stochastic nature of disruptive events lies in their randomness and unpredictability in terms of timing or magnitude. 
3 Measuring Cooperative Resilience 
Once the definition of Cooperative Resilience has been proposed, it is essential to establish a consistent measurement approach. This section proposes a methodology that comprehensively captures all aspects of the concept. It is important to note that resilience, as outlined in Definition 1, depends on the random nature of disruptive events. This randomness is characterized by the probability of occurrence (ps) and the probabilistic magnitude of impact (vs). These parameters are related to risk and vulnerability and could be associated with various sources depending on the system. Therefore, the measure is determined by the realization of the random disruptive event, and this realization, based on specific values of ps and vs, is referred to as a scenario. 
The proposed methodology consists of four stages summarized in Fig. 2. In the first stage, we begin by assessing a group of autonomous agents engaged in collective actions. Variables related to collective well-being are identified and measured, for instance resource availability, resource distribution, resource sustainability, or in general variables related to the welfare of the agents. These variables, specific to the problem at hand, will serve as the basis for calculating resilience. We measure these variables under normal conditions (reference curve) and during disruptions (performance curve). The reference behavior is not necessarily an ideal behavior. Rather, the goal in this stage is to compare the system’s behavior with and without disruptions. 
In the second stage, we recognize that systems often face successive adverse events over time. We assume that disruptions occur sequentially. To capture resilience at a specific moment, the system’s response to all previous disruptions is analyzed within defined time windows, considering the timing of event occurrence, failure, and recovery. Resilience is then calculated within each window by comparing the performance and reference curves. In the third stage, we aggregate the resilience metrics over time for each variable. This aggregation penalizes decreasing resilience and rewards improvement during the sequence of disruptions, reflecting the system’s ability to learn from past disruptions. Finally in the last stage, the individual resilience measurement across all variables are then combined into a single resilience score. 
Each stage is elaborated upon in detail as follows. Table 1 includes some notation for better comprehen-sion of this section. 
4
Variables assembly 
Metrics summarized in each time window for every 
variable 
Agents 
Collective actions 
Time-window assembly 
Reference curves 
Performance curves 
Time-window extraction 
Measure of cooperative resilience 
Stage I Stage II Stage III Stage IV 
Figure 2: Diagram illustrating the proposed methodology for measuring cooperative resilience. 
Table 1: Symbol notation used in the methodology. 
Notation Description 
N Number of agents. 
K Number of variables measure for performance of the system. 
L Number of disruptive events in a time windows [t0, tf ]. 
Pij(t) Performance curve measure for agent i and variable j with i ∈ 1 ≤ i ≤ N and j ∈ 1 ≤ j ≤ K. Measure in a time window [t0, tf ]. 
Rij(t) Reference curve measure for agent i and variable j with i ∈ 1 ≤ i ≤ N and j ∈ 1 ≤ j ≤ K. Measure in a time window [t0, tf ]. 
Pj(t) Performance curve assembly for all agents for variable j with j ∈ 1 ≤ j ≤ K. 
Rj(t) Reference curve assembly for all agents for variable j with j ∈ 1 ≤ j ≤ K. 
Jjl Resilience measure for variable j with j ∈ 1 ≤ j ≤ K, and disruptive event l ∈ 1 ≤ l ≤ L. 
Fjl Failure profile for variable j with j ∈ 1 ≤ j ≤ K, and disrup-tive event l ∈ 1 ≤ l ≤ L. 
Gjl Recovery profile for variable j with j ∈ 1 ≤ j ≤ K, and disruptive event l ∈ 1 ≤ l ≤ L. 
Jj Resilience measure for variable j with j ∈ 1 ≤ j ≤ K assembly in all disruptive event. 
J Resilience measure assembly for all indicator, and assembly for all disruptive event. 
3.1 Stage I: Performance and reference Curves 
The objective of this stage is to define and measure variables related to collective well-being. Initially, we assume that there are N interacting agents, depicted as circles in Fig. 2. This stage entails defining K 
5
variables related to collective well-being of the agents. For example, in an environment where the goal is resource consumption, variables could include resource availability, equality in access to resources, among others. Each variable is time dependent, with and without disruptive events, to establish performance and reference curves. These are shown in the magenta foreground of the second layer in Fig. 2. 
Performance curves for indicator j and agent i are denoted as Pij(t), with reference curves as Rij(t) (see Table 1). The performance curves, initially gathered separately for each agent, are consolidated at this stage. Consolidation at the agent level is achieved using function h, producing a single curve Pj(t) representing collective consolidation each indicator j. The same applies to reference curves. For example, to measure resource access equality, h might use the Gini index to quantify equality based on resource consumption. The specific functional form of h depends on the context and variable. Additionally, aggregated variables by agents can also be utilized. For instance, if measuring resource availability, this variable, which is part of the environment, is already aggregated by agents. In any case, at the end of this stage, performance and reference curves for each variable should be consolidated. 
3.2 Stage II: Computed summary metrics 
The purpose of this stage is to derive metrics that summarize resilient behavior for each adversity across time intervals and for each measured variable. The performance and reference curves are defined for the entire observation period [t0, tf ]. Within this period, smaller time windows are used to isolate and analyze each disruptive event, as illustrated in the orange plane of Fig. 2. Resilience metrics are calculated by comparing the performance curve with the reference curve for each time window. This process allows for detailed assessment of how the system behaves before, during, and after each disruption. 
This summary value is denoted as Jjl (variable j and disruptive event l) and is calculated by the metric described in [34]. The metric involves identifying the failure profile, which relates to the speed and magnitude of the system’s degraded behavior after the disruptive event. Additionally, it also takes into account the recovery profile, considering the speed and stabilization of the system following the disruptive event. 
The equation relating to the calculation of the summary metric denoted as Jjl is as follows in Equation (1): 
Jjl = ti + Fjl∆tf +Gjl∆tr 
ti +∆tf +∆tr , (1) 
where Fjl corresponds to the failure profile, and Gjl represents the recovery profile. ∆tf and ∆tr denote the failure and recovery event duration, computed as ∆tf = tf − ti and ∆tr = tr − tf . The terms ti, tf , tr respectively represent the time of the incident occurrence, the time of failure when the performance deteriorates to the lowest point, and the recovery time, where it is assumed the system should reach a stable state. Total recovery is not necessarily expected, but the time tr is set as a reference to consider the recovery progress. 
The method for calculating the failure and recovery profiles is as follows: 
Fjl = 
∫ tf ti 
Pjl(t)dt∫ tf ti 
Rjl(t)dt , 
and 
Gjl = 
∫ tr tf 
Pjl(t)dt∫ tr tf 
Rjl(t)dt . 
These profiles are positive measures. Values close to 1 indicate that observed and expected behaviors are nearly identical, suggesting minimal deviation from the reference interval. Values below 1 indicate performance below expectations, while values above 1 demonstrate behavior exceeding expectations for the performance curves. For this analysis to be meaningful, it is crucial that the well-being variables have a positive interpretation, meaning higher values correspond to better well-being. 
At the conclusion of this stage, for each variable the summary metrics for all L disruptive events are computed, resulting in a set of Jjl index by variable and disruptive event. 
6
3.3 Stage III: Time-window assembly 
The proposed definition of resilience emphasizes transformation, suggesting that more resilient systems improve their behavior in response to disruptive events. Systems that adapt and learn from disruptions become better prepared for future occurrences, enhancing their ability to anticipate and respond to new events. Conversely, systems that fail to recover from disruptions may become more sensitive to future events, leading to decreased resilience. During this stage, efforts focus on penalizing behaviors where the system fails to transform between disruptive events, reducing resilience over time. Conversely, rewarding occurs when the system demonstrates improved resilience across events. Averaging across consecutive time-windows is proposed, penalizing decreases and incrementally rewarding increases. Therefore, the proposed metric rewards systems that not only recover and adapt but also show measurable improvements in well-being indicators, enhancing their ability to anticipate and manage future disruptions. 
For each variable and across all disruptive events, a single metric Jj (with j ∈ 1 ≤ j ≤ K is computed. In the initial iteration of the calculation, it is performed as follows:( 
Jkl + Jk(l+1) 
2 
)( 1 + (Jk(l+1) − Jkl) 
) . 
The resulting metrics undergo an iterative process, consolidating into a single value. Negative variations indicate decreasing factors of the summary metric across successive disruptive events. If a negative variation results in a negative value, we apply saturation, forcing the value to zero. Conversely, positive variations, which indicate an increase in resilience through disruptive events, are saturated at 1 if they exceed this value. This stage is represented in the green plane of Fig. 2. At the conclusion of this stage, we obtain a measure Jk, which represents the resilience assembly for agents and disruptive events in a specific scenario. 
3.4 Stage IV: Variables assembly 
So far, we have the set {J1, · · · , JK} of summary metrics, one for each variable. However, coupling is necessary to generate a single metric across all K variables. Typically, coupling summary metrics involves averaging or using a weighted average. However, since each indicator represents a component associated with well-being, it is expected that the coupling should penalize low values in the set, indicating poor performance in some variables. Therefore, the harmonic mean is proposed as the coupling metric. This stage is represented in the blue plane of Fig. 2, where at the end of this stage, a single measure J is obtained, representing the measure of resilience assembly among agents, disruptive events, and variable for well-being. 
4 Case Studies 
The objective of this section is to measure cooperative resilience in AI multiagent systems, and investigate how cooperative resilience manifests when these systems are subjected to disruptive events. To achieve this, used Melting Pot 2.0 [40], a research tool designed to study multi-agent AI systems. The specific scenario chosen is referred to as ‘Commons Harvest Open,’ where multiple agents inhabit a confined space containing trees laden with apples. The objective for each agent is to consume as many apples as possible. Consumed apples regenerate with a probability per step that depends on the number of remaining apples on the tree. If all the apples on a tree are consumed, the tree vanishes. In this scenario a social dilemma might arise, when all apples are depleted from a tree, no further apples with grow and this goes in detriment of the entire population. 
Currently, the primary metrics used to evaluate system performance in such scenarios focus on the number of resources consumed by the agents. However, this is insufficient to fully understand the dynamics at play, especially in a context where external disruptive conditions can significantly impact collective welfare. The social dilemma emulated in this scenario requires a deeper evaluation that considers not just resource consumption, but also how agents anticipate, prepare, resist, recover and transform from these disruptions. This underscores the need for a cooperative resilience metric that can assess how the system face of adversity. 
To systematically assess resilience, we introduce two distinct disruptive events. As per the definition, events should pose a risk to the joint-welfare of the agents. The first disruptive event involves the sudden removal of apples from the environment, simulating resource depletion and testing the agents’ ability to 
7
sustain the remaining trees. This event is characterized by the probability of occurrence(ps) and the severity of the depletion (vs). The original environment in Melting Pot is modified to include the introduction of this event. 
The second disruptive event is designed not to be contingent upon environmental conditions, but rather on the introduction of agents lacking established policies or decision-making methods. This event involves adding two bots that engage in unsustainable harvesting, symbolizing a breakdown in social behavior. The event is triggered at a specified time, with the duration of interaction varying across three experiments. This duration indirectly influences the magnitude of the disruption. By adjusting the timing and length of the bots’ introduction, we can assess the system’s cooperative resilience to internal disruptions caused by non-cooperative behaviors. 
The decision-making of the agents is defined through two approaches: Reinforcement Learning and Large Language Models. In RL, agents are trained using Proximal Policy Optimization (PPO) algorithm [47]. Although the disruptive events are not explicitly included in the training, the agents may develop an implicit capacity to anticipate such events based on low apple counts observed during training episodes. On the other hand, for LLM-based agents, an adapter is developed to connect the Melting Pot environment with a language model. The model is informed about the environment through text descriptions and decides agent actions sequentially. In this approach, each agent makes and executes a plan before other agent to move. Once all agents have moved, it constitutes a complete round. This contrasts with RL, where all agents move simultaneously at each time step. Besides, unlike RL, which relies on extensive pre-training, LLM support in pre-existing world knowledge embedded within the language model to reason and make decisions. 
4.1 Reinforcement Learning-based agents 
The PPO algorithm [47], a gradient-based optimization method aimed at maximizing the expected return of policies, is employed to train the agents using RL. The training is conducted using independent RL for each agent. This resulting in each agent possessing its own policy parameterized by its own neural network. The architecture of the network for each agent consisting of a feedforward neural network with two hidden layers, each with 64 neurons and ReLU activation function. This neural network is connected to another network that features a single hidden layer with 1280 neurons, also utilizing the ReLU activation function. 
The total training process span 1.280.000 steps, with mean duration episode 1500 steps. The training process took a total of 769 episodes. For training, the reward function of the problem is defined as 1 if an apple was eaten and 0 otherwise at each step. The agents are capable of executing the following actions: moving up, down, right, or left, rotating right or left, or shoot a laser beam that relocated agents within its range to a distant position from the apples. 
4.2 Large Language Model-augmented agents 
To work with an LLM in the decision-making process of each agent, we develop an adapter that converts the spatial observations received by each agent into textual observations that are comprehensible for a language model, specifically GPT-4. This process is divided into two parts: first, a converter is developed to transform the visual information into ASCII format, representing what each agent perceives about the environment at any given moment in real-time. Subsequently, this information is transformed into detailed textual descriptions of what is observed by each agent within their field of vision. 
To integrate the adapter for working with an LLM in the decision-making process of each agent, the architecture “Generative Agents” proposal in [48] is used. The architecture consists of a memory module, a perception module, a planning module, a reflection module, and an action module. Fig. 3 shows a diagram of the modules comprising it. It is important to note that each module of the architecture is structured around a prompt directed at the language model, utilizing engineering practices of prompting that follow specific guidelines, similar to those applied in projects such as MetaGPT and AutoGPT. The prompts incorporate relevant details of each agent, adapting to current observations and pertinent memories. 
Furthermore, the “Chain of Thought” methodology [49], except for the action module, is employed to structure the responses, enhancing the model’s capability to reason and generate coherent outputs. Regard-ing the module responsible for action execution and decision-making within the simulated environment, an 
8
Game Observations 
Perceive Enviroment React? 
Generate New Plan Generate Actions 
Recent observations > 
Treshold 
Execute Actions 
Reflect 
No 
No 
Yes 
Yes 
Figure 3: Diagram summarizing the reasoning process flow within the LLM architecture, leading to the action-taking phase of each agent. The diagram is inspired by the architecture proposed in [48]. 
innovative prompting technique called “SELF-DISCOVER,” developed by Zhou et al. [50], has been imple-mented. This technique enables the LLM to explore and apply complex reasoning structures autonomously enhancing its ability to generate adaptive responses. 
4.3 Evaluation of cooperative resilience 
In the previously described environment, the phases of the methodology are followed to establish a value of cooperative resilience with both RL and LLM decision-making systems. The evaluation is conducted for a set of experiments proposed in the two disruptive events. Below are the detailed parameters of the experiments conducted. 
4.3.1 First type of disruptive events: apple disappearance 
To cover various scenarios related to the probability of occurrence of a disruptive event and its probabilistic magnitude, the probability of the disruptive event occurring is fixed at certain points in the simulation, with ps = 1 at specific moments and ps = 0 at others. For the impact level, the event iterates through each apple and removes this with a probability corresponding to vs, ensuring that at least one apple remains on each tree. Three probabilistic values for vs are considered, leading to nine scenarios described in the Table 2, the cells in the table with darker hues indicating higher disruption. 
Table 2: Characterization of experiments with first disruptive event. 
Time-step / round 
vs = 0.3 vs =0.5 vs =0.7 
[250] / [25] 
E1: one disruption and low mag-nitude. 
E2: one dis-ruption and medium magni-tude. 
E3: one dis-ruption and highest mag-nitude. 
[50, 250] / [5, 25] 
E4: two dis-ruptions and lowest magni-tude. 
E5: two dis-ruptions and medium magni-tude. 
E6: two dis-ruptions and high magni-tude. 
[50, 250, 400] / [5, 25, 40] 
E7: three disruptions and low mag-nitude. 
E8: three dis-ruptions and medium magni-tude. 
E9: three disruptions and high mag-nitude. 
In the initial phase of the methodology, within the described environment, we have decided to incorporate curves related to resource availability, sustainability, and distribution. These factors are essential components of collective well-being. These dimensions are explored through the following specific measures: (1) apples alive per capita, (2) trees alive per capita, (3) cumulative gini equality index and (4) collective hunger level Index2. 
2Detailed descriptions of these indicators, including their theoretical foundations are provided in supplementary file. 
9
Fig. 4 shows some examples of the performance and references curves taken in the initial phase of the methodology. In Fig. 4, it is observed that a disruptive event significantly influences the system across four key metrics. A direct impact is seen on the metric related to the number of apples in the environment, while a decline in expected performance is also noted in the other metrics. In the case of the number of living trees, the reference curve is situated above the value for the scenario presented. A similar trend is noted for the cumulative gini equality index, where, although the effect is not immediate, the disruptive event, over time, leads to a degradation in performance in comparison to the reference scenario. Regarding the hunger index for the depicted scenario, a significant disruption is not immediately evident. However, as events unfold, an increase in ‘hunger’ becomes apparent, which makes sense given the scarcity of resources. Another important aspect is that, in the case of LLM decision-making techniques, unlike RL, behavior is not optimized according to resource availability. This results in rapid apple harvesting and eventual total tree disappearance due to disruptive events. These elements are analyzed for the experiments presented. However, depending on the experiment, different behaviors may be observed. 
(a) 
0 200 400 600 800 1000 Time-step 
0 
5 
10 
15 
20 
Ap pl 
es  p 
er  c 
ap ita 
(b) 
0 200 400 600 800 1000 Time-step 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
Tr ee 
s pe 
r ca 
pi ta 
(c) 
0 200 400 600 800 1000 Time-step 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
0.8 
0.9 
1.0 
C um 
ul at 
iv e 
G in 
i E qu 
al ity 
(d) 
0 200 400 600 800 1000 Time-step 
0.00 
0.05 
0.10 
0.15 
0.20 
0.25 
0.30 
C ol 
le ct 
iv e 
H un 
ge r 
Le ve 
l 
(e) 
0 20 40 60 80 100 Round 
0 
5 
10 
15 
20 
Ap pl 
es  p 
er  c 
ap ita 
(f) 
0 20 40 60 80 100 Round 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
Tr ee 
s pe 
r ca 
pi ta 
(g) 
0 20 40 60 80 100 Round 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
0.8 
0.9 
1.0 
C um 
ul at 
iv e 
G in 
i E qu 
al ity 
(h) 
0 20 40 60 80 100 Round 
0.00 
0.05 
0.10 
0.15 
0.20 
0.25 
0.30 
C ol 
le ct 
iv e 
H un 
ge r 
Le ve 
l 
Figure 4: Performance and reference curves: The blue line represents the mean performance curve over five episodes, while the orange line indicates the mean reference curve. The shaded regions correspond to the standard deviation. The red dashed line marks the occurrence of the disruptive event. The top row (a, b, c, d) shows the results of agents trained with RL, while the bottom row (e, f, g, h) displays the results of LLM-based models. (a) and (e) depict the apples alive per capita in experiment E9. (b) and (f) show the trees alive per capita in experiment E2. (c) and (g) illustrate the Gini Equality Index in experiment E5. Finally, (d) and (h) present the Collective Hunger Level in experiment E7. 
After deriving the curves, the methodology conducts an ensemble analysis over time-windows. Critical milestones: incidence time, failure time, and recovery time are identified within the windows where the disruptive event occurs. The failure time marks the system’s lowest performance level between the incidence and recovery times. Using these milestones, a summary metric is calculated, followed by ensemble analysis to produce a single resilience value for each variable. Then, an ensemble analysis is performed to obtain a final value across all variables. Fig. 5 presents a heat map showing the cooperative resilience values in the proposed scenarios. 
The cooperative resilience map in Fig. 5 reveals a general trend: resilience decreases as the disturbance magnitude and the number of disruptive events increase, with this effect being more pronounced in LLM than in RL. Interestingly, in the RL approach, when vs = 0.3, resilience is higher with three disruptive events (E7) compared to two (E4). This counterintuitive result can be attributed to the transformation property of the proposed methodology, which suggests that the system may be rewarded for improving its tolerance to successive disruptions after experiencing previous ones. This phenomenon underscores the importance of using resilience as a metric, as it captures dynamic system behaviors and adaptive capacities. The previous situation is also replicated in experiments E5 and E8 of LLM. In this case, we would expect 
10
(a) 
0.3 0.5 0.7 vs 
1 2 
3N um 
be r 
of  d 
is ru 
pt iv 
e ev 
en ts 1 0.91 0.92 
0.85 0.9 0.8 
0.97 0.89 0.78 
0.0 0.2 0.4 0.6 0.8 1.0 
(b) 
0.3 0.5 0.7 vs 
1 2 
3N um 
be r 
of  d 
is ru 
pt iv 
e ev 
en ts 0.87 0.66 0.97 
0.73 0.24 0.24 
0.38 0.46 0.29 
0.0 0.2 0.4 0.6 0.8 1.0 
Figure 5: Cooperative Resilience Map: This heatmap illustrates the impact of varying the number of dis-ruptive events (1, 2, or 3) and the disturbance magnitude (vs) on system resilience. The map uses darker colors to represent lower resilience values. Figure (a) shows results for the RL approach, while (b) displays results for the LLM. 
resilience to reach a higher value for experiment E5 compared to E8. However, this is not the case. This outcome can be explained similarly to what was observed in RL. 
Contrary to expectations, where a higher impact represented by vs would typically result in greater system degradation, the results show a lower resilience value in RL for the scenario with two events and vs = 0.3 (E4) compared to vs = 0.5 (E5). Similarly, in LLM, both vs = 0.5 (E5) and vs = 0.7 (E6) with two disruptive events yield the same resilience values. This deviation from the hypothesis suggests that a higher magnitude does not necessarily lead to poorer system recovery. Factors such as agent dynamics, environmental conditions, and scenario variability likely contribute to this unexpected behavior. 
This highlights the importance of the cooperative resilience metric, as it captures complex interactions, adaptive responses and capacities that conventional metrics may overlook, providing a more understanding of the system’s performance under disruptions. Additionally, the cooperative resilience metric allows for a comparison between the two decision-making systems, RL and LLM. RL models generally outperform LLM, owing to their training on diverse episodes with varying apple values. In contrast, LLM, which lacks a training phase and generates actions based on its architecture alone, demonstrates an incomplete understanding of how actions impact resource depletion. This indicates potential advantages of employing cooperative-focused LLM architectures. 
4.3.2 Second type of disruptive events: unsustainable bots 
In the second disruptive event, unsustainable bots are introduced into the simulation. These bots are introduced at a standardized point: the 10th round in LLM or the 100th time-step in RL. The impact of this disruption is evaluated based on the duration of the bots’ interaction with the environment. Three levels of disruption are considered: E1: Bots interact for 25 time-steps in RL and 5 rounds in LLM. E2: Bots interact for 50 time-steps in RL and 10 rounds in LLM. E3: Bots interact for 75 time-steps in RL and 15 rounds in LLM. 
These duration intervals are chosen to ensure a proportionate comparison of the disruption impact across both approaches. In the case of LLM-agumented agents, one round consists of all the steps in which agents execute their plan in turns. The bots were configured to move only half the time within a round, meaning they do not move every step but alternate instead. The evaluation of cooperative resilience employs the same variables as the previous disruptive event. 
Fig. 6 presents the cooperative resilience measure across the three experiments. The results demonstrate 
11
that as the duration of bot interaction in the simulation increases, resilience values decrease. This outcome is anticipated, given that the bots consume resources unsustainably, directly and indirectly impacting the variables considered for resilience measurement. Resource scarcity directly affects the availability of apples in the environment and the survival of trees. Moreover, bots that consume large quantities of apples create inequality in resource access, a situation that is exacerbated with prolonged bot presence. 
(a) 
25 50 75 Bots Duration (Time-steps) 
0.86 0.65 0.52 
0.0 0.2 0.4 0.6 0.8 1.0 
(b) 
5 10 15 Bots Duration (Rounds) 
0.91 0.77 0.62 
0.0 0.2 0.4 0.6 0.8 1.0 
Figure 6: Cooperative resilience map: This heatmap illustrates the impact of varying bot interaction dura-tions on system resilience. Darker hues represent lower resilience values. Figure (a) shows the results for the RL approach, while (b) displays the results for the LLM-augmented agents. 
When comparing the results between RL and LLM techniques, it is evident that the values for LLM surpass those of RL across all three experiments. This suggests that, for this disruptive event, the LLM technique exhibits better recovery and failure profiles. Expanding on the previous observation, certain indicators in RL suggest that agents continue their resource consumption policy regardless of the disruptive event. For instance, in Fig. 7a, the slope of apple availability for agents remains unchanged post-bot intrusion. This implies that the bots’ presence does not alter resource consumption patterns once they depart. The previous situation differs in LLM. For instance, in Fig. 7b, once the bots leave, the slope changes, promoting a return to the expected behavior. This indicates that agents in the LLM framework may adapt their strategies based on the bots’ actions, leading to a more socially adaptive behavior. 
This adaptability observed in LLM is captured effectively by our cooperative resilience metric, underscor-ing its significance. The metric not only reveals how systems recover from disruptions but also highlights how agents adjust their behaviors in response to external social influences. This ability to measure and analyze adaptive responses demonstrating why our cooperative resilience metric is a valuable tool in understanding the system’s robustness to disruptions. 
(a) 
0 200 400 600 800 1000 Time-step 
0 
5 
10 
15 
20 
Ap pl 
es  p 
er  c 
ap ita 
(b) 
0 20 40 60 80 100 Round 
0 
5 
10 
15 
20 
Ap pl 
es  p 
er  c 
ap ita 
Figure 7: Apples alive per capita. The blue line is the mean value throughout 5 episodes of the performance curve and the orange line is the mean of reference curve. The shaded areas indicate the standard deviation. The red dashed line shows the occurrence of the disruptive event. (a) E3 in RL and (b) E2 in LLM. 
12
4.4 Discusion of the Results 
The results from both types of disruptive events highlight the complex dynamics that influence the system’s resilience. These findings underscore the need for a broader understanding of how varying magnitudes and frequencies of disruptive events affect the final value of cooperative resilience. While additional experiments could enhance the accuracy of the cooperative resilience metric, the current methodology effectively captures resilience by focusing on the process of confronting disruptions, an aspect often overlooked by traditional metrics in AI multiagent systems. This approach is particularly valuable for studying AI systems prone to failures, as it addresses the impact of disruptions and highlights the agents’ adaptive responses. Despite these complexities, the methodology can be appropriately applied to these experiments, establishing a cooperative resilience value that aligns with the definition outlined in this document. 
5 Conclusion and Future Work 
In this article, we have introduced the concept of cooperative resilience in cooperative AI, a notion proposed after analyzing the definition of resilience across various domains and aligning it with the concepts and scope of cooperative AI. This contribution not only try to unify the terminology within cooperative AI, but also aligns with interdisciplinary research efforts to understand emergent resilience in complex systems. Following the establishment of this definition, we have proposed a methodology designed to quantify cooperative resilience consistently with the defined concept. This methodology aims to estimate resilience in cooperative AI systems with the aim of enhance or comparing this value in future studies. 
The proposed methodology is applied to and validated in experiments using Melting Pot 2.0, specifically the ‘Common Harvest Open’ scenario, employing both RL and LLM approaches for the control of agents. Two sets of experiments were conducted, one involving a disruptive event related to vanished apples at some point, and the other involving a disruptive event associated with the inclusion of bots. Under varying conditions of disruptive events, the value of cooperative resilience is determined in 9 experiments in the first case and in 3 experiments in the other disruptive event. The interplay of factors contributing to system resilience is underscored by the results, revealing instances where unexpected recovery patterns are demonstrated by the systems. Notably, the observation that resilience can sometimes increase with the number of disruptive events or vary with the magnitude of disruption, challenges conventional ideas and suggests a complex adaptive capacity inherent in these systems. These results, while preliminary, provide a foundation for deeper investigation into the dynamics of cooperative resilience and highlight the need for a broader range of experiments to understand the behavior of resilience. 
Moreover, this research opens avenues for interdisciplinary collaboration, drawing parallels with resilience studies in ecology, psychology, network science, and other domains. Such collaborations can enrich our understanding of resilience as a multi-faceted concept and foster the development of more resilient cooperative AI systems. 
Future research should aim to expand the experimental framework to encompass a broader range of scenarios and disruptive events. Applying the developed methodology to experiments involving human performance could also enable comparisons between machine-only decision-making and human-machine in-teractions, providing valuable insights into cooperative resilience. Furthermore, a deeper exploration of the factors contributing to the emergence of resilience would be beneficial. Inverse problem approaches, such as inverse games and inverse reinforcement learning, can help uncover the underlying motivations driving resilient behaviors, facilitating their replication and enhancing resilience properties in AI systems. 
References 
[1] R. Jiménez, H. Lugo, J. A. Cuesta, and A. Sánchez, “Emergence and resilience of cooperation in the spatial prisoner’s dilemma via a reward mechanism,” Journal of theoretical biology, vol. 250, no. 3, pp. 475–483, 2008. 
[2] H. Lugo and R. Jiménez, “Incentives to cooperate in network formation,” Computational Economics, vol. 28, pp. 15–27, 2006. 
13
[3] E. K. Chiou and J. D. Lee, “Cooperation in human-agent systems to support resilience: A microworld experiment,” Human factors, vol. 58, no. 6, pp. 846–863, 2016. 
[4] N. B. I. Wulandhari, I. Gölgeci, N. Mishra, U. Sivarajah, and S. Gupta, “Exploring the role of social capital mechanisms in cooperative resilience,” Journal of Business Research, vol. 143, pp. 375–386, 2022. 
[5] A. Tripathi, S. Suresh, and P. Kaur, “Resilience: Some conceptual considerations in the case of ai,” Procedia Computer Science, vol. 185, pp. 135–143, 2021. 
[6] O. Eigner, S. Eresheim, P. Kieseberg, L. D. Klausner, M. Pirker, T. Priebe, S. Tjoa, F. Marulli, and F. Mercaldo, “Towards resilient artificial intelligence: Survey and research issues,” in Proceedings of IEEE International Conference on Cyber Security and Resilience (CSR). IEEE, 2021, pp. 536–542. 
[7] S. Jha, “Trust, resilience and interpretability of ai models,” in Numerical Software Verification: The 12th International Workshop, NSV 2019, New York City, NY, USA, July 13–14, 2019, Proceedings 12. Springer, 2019, pp. 3–25. 
[8] Q. Hu and Z. Pan, “Can ai benefit individual resilience? the mediation roles of ai routinization and infusion,” Journal of Retailing and Consumer Services, vol. 73, p. 103339, 2023. 
[9] A. Petrilli and S.-h. Lau, “Measuring resilience in artificial intelligence and machine learning systems,” Carnegie Mellon University, Software Engineering Institute’s Insights (blog), Dec 2019. 
[10] J. Carlson, R. Haffenden, G. Bassett, W. Buehring, M. Collins III, S. Folga, F. Petit, J. Phillips, D. Verner, and R. Whitfield, “Resilience: Theory and application.” Argonne National Lab.(ANL), Argonne, IL (United States), Tech. Rep., 2012. 
[11] A. Melendez, D. Caballero-Russi, M. Gutierrez Soto, and L. F. Giraldo, “Computational models of community resilience,” Natural Hazards, vol. 111, no. 2, pp. 1121–1152, 2022. 
[12] A. Zambrano, A. P. Betancur, L. Burbano, A. F. Niño, L. F. Giraldo, M. G. Soto, J. Giraldo, and A. A. Cardenas, “You make me tremble: A first look at attacks against structural control systems,” in Proceedings of the 2021 ACM SIGSAC conference on computer and communications security, 2021, pp. 1320–1337. 
[13] D. Fletcher and M. Sarkar, “Psychological resilience,” European psychologist, 2013. 
[14] G. Wu, A. Feder, H. Cohen, J. J. Kim, S. Calderon, D. S. Charney, and A. A. Mathé, “Understanding resilience,” Frontiers in behavioral neuroscience, vol. 7, p. 10, 2013. 
[15] H. Herrman, D. E. Stewart, N. Diaz-Granados, E. L. Berger, B. Jackson, and T. Yuen, “What is resilience?” The Canadian Journal of Psychiatry, vol. 56, no. 5, pp. 258–265, 2011. 
[16] O. Hjemdal, O. Friborg, T. C. Stiles, J. H. Rosenvinge, and M. Martinussen, “Resilience predicting psychiatric symptoms: A prospective study of protective factors and their role in adjustment to stressful life events,” Clinical Psychology & Psychotherapy: An International Journal of Theory & Practice, vol. 13, no. 3, pp. 194–201, 2006. 
[17] M. A. Waller, “Resilience in ecosystemic context: Evolution of the concept,” American Journal of orthopsychiatry, vol. 71, no. 3, pp. 290–297, 2001. 
[18] M. Perdomo, F. Sanchez, and A. Blanco, “Effects of a community resilience intervention program on victims of forced displacement: A case study,” Journal of Community Psychology, vol. 49, no. 6, pp. 1630–1647, 2021. 
[19] A. Rose, “Economic resilience to natural and man-made disasters: Multidisciplinary origins and con-textual dimensions,” Environmental Hazards, vol. 7, no. 4, pp. 383–398, 2007. 
[20] L. Briguglio, G. Cordina, N. Farrugia, and S. Vella, “Economic vulnerability and resilience: concepts and measurements,” in Measuring Vulnerability in Developing Countries. Routledge, 2014, pp. 47–65. 
14
[21] J. Simmie and R. Martin, “The economic resilience of regions: towards an evolutionary approach,” Cambridge journal of regions, economy and society, vol. 3, no. 1, pp. 27–43, 2010. 
[22] F. Ozbay, D. C. Johnson, E. Dimoulas, C. Morgan Iii, D. Charney, and S. Southwick, “Social support and resilience to stress: from neurobiology to clinical practice,” Psychiatry (edgmont), vol. 4, no. 5, p. 35, 2007. 
[23] M. Keck and P. Sakdapolrak, “What is social resilience? lessons learned and ways forward,” Erdkunde, pp. 5–19, 2013. 
[24] A.-L. Barabási and M. Pósfai, Network science. Cambridge: Cambridge University Press, 2016. 
[25] J. Gao, B. Barzel, and A.-L. Barabási, “Universal resilience patterns in complex networks,” Nature, vol. 530, no. 7590, pp. 307–312, 2016. 
[26] X. Liu, D. Li, M. Ma, B. K. Szymanski, H. E. Stanley, and J. Gao, “Network resilience,” Physics Reports, vol. 971, pp. 1–108, 2022. 
[27] H. Krakovská, C. Kuehn, and I. P. Longo, “Resilience of dynamical systems,” European Journal of Applied Mathematics, pp. 1–46, 2021. 
[28] G. Como, “On resilient control of dynamical flow networks,” Annual Reviews in Control, vol. 43, pp. 80–90, 2017. 
[29] K. Van Meerbeek, T. Jucker, and J.-C. Svenning, “Unifying the concepts of stability and resilience in ecology,” Journal of Ecology, vol. 109, no. 9, pp. 3114–3132, 2021. 
[30] C. S. Holling, “Resilience and stability of ecological systems,” Annual review of ecology and systematics, vol. 4, no. 1, pp. 1–23, 1973. 
[31] A. Hastings, “Transient dynamics and persistence of ecological systems,” Ecology Letters, vol. 4, no. 3, pp. 215–220, 2001. 
[32] A. Dafoe, E. Hughes, Y. Bachrach, T. Collins, K. R. McKee, J. Z. Leibo, K. Larson, and T. Graepel, “Open problems in cooperative ai,” arXiv preprint arXiv:2012.08630, 2020. 
[33] B. A. Han, K. R. Varshney, S. LaDeau, A. Subramaniam, K. C. Weathers, and J. Zwart, “A syner-gistic future for ai and ecology,” Proceedings of the National Academy of Sciences, vol. 120, no. 38, p. e2220283120, 2023. 
[34] B. M. Ayyub, “Systems resilience for multihazard environments: Definition, metrics, and valuation for decision making,” Risk analysis, vol. 34, no. 2, pp. 340–355, 2014. 
[35] C. Wang, “A generalized index for functionality-sensitive resilience quantification,” Resilient Cities and Structures, vol. 2, no. 1, pp. 68–75, 2023. 
[36] S. A. Argyroudis, “Resilience metrics for transport networks: a review and practical examples for bridges,” in Proceedings of the Institution of Civil Engineers-Bridge Engineering, vol. 175. Thomas Telford Ltd, 2022, pp. 179–192. 
[37] F. Gerges, H. Nassif, X. Geng, H. A. Michael, and M. C. Boufadel, “Gis-based approach for evaluating a community intrinsic resilience index,” Natural Hazards, vol. 111, no. 2, pp. 1271–1299, 2022. 
[38] E. Serfilippi and G. Ramnath, “Resilience measurement and conceptual frameworks: a review of the literature,” Annals of Public and Cooperative Economics, vol. 89, no. 4, pp. 645–664, 2018. 
[39] G. P. Cimellaro, C. Renschler, A. M. Reinhorn, and L. Arendt, “Peoples: a framework for evaluating resilience,” Journal of Structural Engineering, vol. 142, no. 10, p. 04016063, 2016. 
15
[40] J. P. Agapiou, A. S. Vezhnevets, E. A. Duéñez-Guzmán, J. Matyas, Y. Mao, P. Sunehag, R. Köster, U. Madhushani, K. Kopparapu, R. Comanescu et al., “Melting pot 2.0,” arXiv preprint arXiv:2211.13746, 2022. 
[41] Y. Zhang and J. Jiang, “Bibliographical review on reconfigurable fault-tolerant control systems,” Annual reviews in control, vol. 32, no. 2, pp. 229–252, 2008. 
[42] Y. Huang, L. Huang, and Q. Zhu, “Reinforcement learning for feedback-enabled cyber resilience,” Annual reviews in control, vol. 53, pp. 273–295, 2022. 
[43] B. M. Ayyub, “Systems resilience for multihazard environments: Definition, metrics, and valuation for decision making,” Risk analysis, vol. 34, no. 2, pp. 340–355, 2014. 
[44] E. Serfilippi and G. Ramnath, “Resilience measurement and conceptual frameworks: a review of the literature,” Annals of Public and Cooperative Economics, vol. 89, no. 4, pp. 645–664, 2018. 
[45] A. Sisto, F. Vicinanza, L. L. Campanozzi, G. Ricci, D. Tartaglini, and V. Tambone, “Towards a transver-sal definition of psychological resilience: A literature review,” Medicina, vol. 55, no. 11, p. 745, 2019. 
[46] S.-L. C. Vella and N. B. Pai, “A theoretical review of psychological resilience: Defining resilience and resilience research over the decades,” Archives of Medicine and Health Sciences, vol. 7, no. 2, pp. 233– 239, 2019. 
[47] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algo-rithms,” arXiv preprint arXiv:1707.06347, 2017. 
[48] M. Mosquera, J. S. Pinzon, M. Rios, Y. Fonseca, L. F. Giraldo, N. Quijano, and R. Manrique, “Can llm-augmented autonomous agents cooperate?, an evaluation of their cooperative capabilities through melting pot,” arXiv preprint arXiv:2403.11381, 2024. 
[49] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou et al., “Chain-of-thought prompting elicits reasoning in large language models,” Advances in Neural Information Processing Sys-tems, vol. 35, pp. 24 824–24 837, 2022. 
[50] P. Zhou, J. Pujara, X. Ren, X. Chen, H.-T. Cheng, Q. V. Le, E. H. Chi, D. Zhou, S. Mishra, and H. S. Zheng, “Self-discover: Large language models self-compose reasoning structures,” arXiv preprint arXiv:2402.03620, 2024. 
16