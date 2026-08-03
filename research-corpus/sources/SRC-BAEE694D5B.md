> Source: https://en.wikipedia.org/wiki/Intelligent_agent

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
1   Intelligent agents as the foundation of AI  
2   Objective function  
3   Agent function  
4   Classes of intelligent agents  4.1   Russell and Norvig's classification  4.1.1   Simple reflex agents  
4.1.2   Model-based reflex agents  
4.1.3   Goal-based agents  
4.1.4   Utility-based agents  
4.1.5   Learning agents  
4.2   Weiss's classification  
4.3   Other  
5   Hierarchies of agents  
6   Alternative definitions and uses  6.1   Agentic AI  6.1.1   Training and testing  
6.1.2   Autonomous capabilities  
6.1.3   Multimodal AI agents  
6.1.4   Applications  
6.1.5   Proposed benefits  
6.1.6   Concerns  6.1.6.1   Possible mitigation  
7   Applications  
8   See also  
9   References  
10   Sources  
Intelligent agent
Afrikaans
العربية
বাংলা
Български
Català
Deutsch
Ελληνικά
Español
فارسی
Français
Galego
한국어
Hrvatski
Ido
Italiano
עברית
Lietuvių
Македонски
Монгол
日本語
Norsk bokmål
Polski
Português
Русский
Shqip
සිංහල
Simple English
Slovenščina
Српски / srpski
Svenska
Українська
Tiếng Việt
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
From Wikipedia, the free encyclopedia   Software agent which acts autonomously   For the term in intelligent design, see Intelligent designer.   Not to be confused with Embodied agent.   It has been suggested that Agentic AI be merged into this article. (Discuss) Proposed since May 2025.Simple reflex agent diagram  
In artificial intelligence, an intelligent agent is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through machine learning or by acquiring knowledge. AI textbooks[which?] define artificial intelligence as the "study and design of intelligent agents," emphasizing that goal-directed behavior is central to intelligence. 
A specialized subset of intelligent agents, agentic AI (also known as an AI agent or simply agent), expands this concept by proactively pursuing goals, making decisions, and taking actions over extended periods. 
Intelligent agents can range from simple to highly complex. A basic thermostat or control system is considered an intelligent agent, as is a human being, or any other system that meets the same criteria—such as a firm, a state, or a biome.[ 1 ]
Intelligent agents operate based on an objective function, which encapsulates their goals. They are designed to create and execute plans that maximize the expected value of this function upon completion.[ 2 ] For example, a reinforcement learning agent has a reward function, which allows programmers to shape its desired behavior.[ 3 ] Similarly, an evolutionary algorithm's behavior is guided by a fitness function.[ 4 ]
Intelligent agents in artificial intelligence are closely related to agents in economics, and versions of the intelligent agent paradigm are studied in cognitive science, ethics, and the philosophy of practical reason, as well as in many interdisciplinarysocio-cognitivemodeling and computer social simulations. 
Intelligent agents are often described schematically as abstract functional systems similar to computer programs. To distinguish theoretical models from real-world implementations, abstract descriptions of intelligent agents are called abstract intelligent agents. Intelligent agents are also closely related to software agents—autonomous computer programs that carry out tasks on behalf of users. They are also referred to using a term borrowed from economics: a "rational agent".[ 1 ]
Intelligent agents as the foundation of AI
[edit]   This section possibly contains original research.  Relevant discussion may be found on Talk:Intelligent agent. Please improve it by verifying the claims made and adding inline citations. Statements consisting only of original research should be removed.  ( February 2023 ) (Learn how and when to remove this message)The concept of intelligent agents provides a foundational lens through which to define and understand artificial intelligence. For instance, the influential textbook Artificial Intelligence: A Modern Approach (Russell & Norvig) describes: 
Agent: Anything that perceives its environment (using sensors) and acts upon it (using actuators). E.g., a robot with cameras and wheels, or a software program that reads data and makes recommendations.
Rational Agent: An agent that strives to achieve the *best possible outcome* based on its knowledge and past experiences. "Best" is defined by a performance measure – a way of evaluating how well the agent is doing.
Artificial Intelligence (as a field): The study and creation of these rational agents.
Other researchers and definitions build upon this foundation. Padgham & Winikoff emphasize that intelligent agents should react to changes in their environment in a timely way, proactively pursue goals, and be flexible and robust (able to handle unexpected situations). Some also suggest that ideal agents should be "rational" in the economic sense (making optimal choices) and capable of complex reasoning, like having beliefs, desires, and intentions (BDI model). Kaplan and Haenlein offer a similar definition, focusing on a system's ability to understand external data, learn from that data, and use what is learned to achieve goals through flexible adaptation. 
Defining AI in terms of intelligent agents offers several key advantages: 
Avoids Philosophical Debates: It sidesteps arguments about whether AI is "truly" intelligent or conscious, like those raised by the Turing test or Searle's Chinese Room. It focuses on behavior and goal achievement, not on replicating human thought.
Objective Testing: It provides a clear, scientific way to evaluate AI systems. Researchers can compare different approaches by measuring how well they maximize a specific "goal function" (or objective function). This allows for direct comparison and combination of techniques.
Interdisciplinary Communication: It creates a common language for AI researchers to collaborate with other fields like mathematical optimization and economics, which also use concepts like "goals" and "rational agents."
Objective function
[edit]   Further information: utility function (economics) and loss function (mathematics)  
An objective function (or goal function) specifies the goals of an intelligent agent. An agent is deemed more intelligent if it consistently selects actions that yield outcomes better aligned with its objective function. In effect, the objective function serves as a measure of success. 
The objective function may be: 
Simple: For example, in a game of Go, the objective function might assign a value of 1 for a win and 0 for a loss.
Complex: It might require the agent to evaluate and learn from past actions, adapting its behavior based on patterns that have proven effective.
The objective function encapsulates all of the goals the agent is designed to achieve. For rational agents, it also incorporates the trade-offs between potentially conflicting goals. For instance, a self-driving car's objective function might balance factors such as safety, speed, and passenger comfort. 
Different terms are used to describe this concept, depending on the context. These include: 
Utility function: Often used in economics and decision theory, representing the desirability of a state.
Objective function: A general term used in optimization.
Loss function: Typically used in machine learning, where the goal is to minimize the loss (error).
Reward Function: Used in reinforcement learning.
Fitness Function: Used in evolutionary systems.
Goals, and therefore the objective function, can be: 
Explicitly defined: Programmed directly into the agent.
Induced: Learned or evolved over time. 
In reinforcement learning, a "reward function" provides feedback, encouraging desired behaviors and discouraging undesirable ones. The agent learns to maximize its cumulative reward.
In evolutionary systems, a "fitness function" determines which agents are more likely to reproduce. This is analogous to natural selection, where organisms evolve to maximize their chances of survival and reproduction.[ 5 ]
Some AI systems, such as nearest-neighbor, reason by analogy rather than being explicitly goal-driven. However, even these systems can have goals implicitly defined within their training data.[ 6 ] Such systems can still be benchmarked by framing the non-goal system as one whose "goal" is to accomplish its narrow classification task.[ 7 ]
Systems not traditionally considered agents, like knowledge-representation systems, are sometimes included in the paradigm by framing them as agents with a goal of, for example, answering questions accurately. Here, the concept of an "action" is extended to encompass the "act" of providing an answer. As a further extension, mimicry-driven systems can be framed as agents optimizing a "goal function" based on how closely the IA mimics the desired behavior.[ 2 ] In generative adversarial networks (GANs) of the 2010s, an "encoder"/"generator" component attempts to mimic and improvise human text composition. The generator tries to maximize a function representing how well it can fool an antagonistic "predictor"/"discriminator" component.[ 8 ]
While symbolic AI systems often use an explicit goal function, the paradigm also applies to neural networks and evolutionary computing. Reinforcement learning can generate intelligent agents that appear to act in ways intended to maximize a "reward function".[ 9 ] Sometimes, instead of setting the reward function directly equal to the desired benchmark evaluation function, machine learning programmers use reward shaping to initially give the machine rewards for incremental progress.[ 10 ]Yann LeCun stated in 2018, "Most of the learning algorithms that people have come up with essentially consist of minimizing some objective function."[ 11 ]AlphaZero chess had a simple objective function: +1 point for each win, and -1 point for each loss. A self-driving car's objective function would be more complex.[ 12 ] Evolutionary computing can evolve intelligent agents that appear to act in ways intended to maximize a "fitness function" influencing how many descendants each agent is allowed to leave.[ 4 ]
The mathematical formalism of AIXI was proposed as a maximally intelligent agent in this paradigm.[ 13 ] However, AIXI is uncomputable. In the real world, an IA is constrained by finite time and hardware resources, and scientists compete to produce algorithms that achieve progressively higher scores on benchmark tests with existing hardware.[ 14 ]
Agent function
[edit]  
An intelligent agent's behavior can be described mathematically by an agent function. This function determines what the agent does based on what it has seen. 
A percept refers to the agent's sensory inputs at a single point in time. For example, a self-driving car's percepts might include camera images, lidar data, GPS coordinates, and speed readings at a specific instant. The agent uses these percepts, and potentially its history of percepts, to decide on its next action (e.g., accelerate, brake, turn). 
The agent function, often denoted as f, maps the agent's entire history of percepts to an action.[ 15 ]
Mathematically, this can be represented as 
f   :   P   ∗   →   A   ,   {\displaystyle f\colon P^{*}\rightarrow A,}  
where: 
P   ∗   {\displaystyle {\boldsymbol {P^{*}}}}    represents the set of all possible percept sequences (the agent's entire perceptual history). The asterisk (*) indicates a sequence of zero or more percepts.
A   {\displaystyle {\boldsymbol {A}}}    represents the set of all possible actions the agent can take.
f   {\displaystyle {\boldsymbol {f}}}    is the agent function that maps a percept sequence to an action.
It's crucial to distinguish between the agent function (an abstract mathematical concept) and the agent program (the concrete implementation of that function). 
The agent function is a theoretical description.
The agent program is the actual code that runs on the agent. The agent program takes the current percept as input and produces an action as output.
The agent function can incorporate a wide range of decision-making approaches, including:[ 16 ]
Calculating the utility (desirability) of different actions.
Using logical rules and deduction.
Employing fuzzy logic.
Other methods.
Classes of intelligent agents
[edit]  
Russell and Norvig's classification
[edit]  
Russell & Norvig (2003) group agents into five classes based on their degree of perceived intelligence and capability:[ 17 ]
Simple reflex agents
[edit]  Simple reflex agent  
Simple reflex agents act only on the basis of the current percept, ignoring the rest of the percept history. The agent function is based on the condition-action rule: "if condition, then action". 
This agent function only succeeds when the environment is fully observable. Some reflex agents can also contain information on their current state which allows them to disregard conditions whose actuators are already triggered. 
Infinite loops are often unavoidable for simple reflex agents operating in partially observable environments. If the agent can randomize its actions, it may be possible to escape from infinite loops. 
A home thermostat, which turns on or off when the temperature drops below a certain point, is an example of a simple reflex agent.[ 18 ][ 19 ]
Model-based reflex agents
[edit]  Model-based reflex agent  
A model-based agent can handle partially observable environments. Its current state is stored inside the agent, maintaining a structure that describes the part of the world which cannot be seen. This knowledge about "how the world works" is referred to as a model of the world, hence the name "model-based agent". 
A model-based reflex agent should maintain some sort of internal model that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state. Percept history and impact of action on the environment can be determined by using the internal model. It then chooses an action in the same way as reflex agent. 
An agent may also use models to describe and predict the behaviors of other agents in the environment.[ 20 ]
Goal-based agents
[edit]  Model-based, goal-based agent  
Goal-based agents further expand on the capabilities of the model-based agents, by using "goal" information. Goal information describes situations that are desirable. This provides the agent a way to choose among multiple possibilities, selecting the one which reaches a goal state. Search and planning are the subfields of artificial intelligence devoted to finding action sequences that achieve the agent's goals. 
ChatGPT and the Roomba vacuum are examples of goal-based agents.[ 21 ]
Utility-based agents
[edit]  Model-based, utility-based agent  
Goal-based agents only distinguish between goal states and non-goal states. It is also possible to define a measure of how desirable a particular state is. This measure can be obtained through the use of a utility function which maps a state to a measure of the utility of the state. A more general performance measure should allow a comparison of different world states according to how well they satisfied the agent's goals. The term utility can be used to describe how "happy" the agent is. 
A rational utility-based agent chooses the action that maximizes the expected utility of the action outcomes - that is, what the agent expects to derive, on average, given the probabilities and utilities of each outcome. A utility-based agent has to model and keep track of its environment, tasks that have involved a great deal of research on perception, representation, reasoning, and learning. 
Learning agents
[edit]  A general learning agent  
Learning lets agents begin in unknown environments and gradually surpass the bounds of their initial knowledge. A key distinction in such agents is the separation between a "learning element," responsible for improving performance, and a "performance element," responsible for choosing external actions. 
The learning element gathers feedback from a "critic" to assess the agent's performance and decides how the performance element—also called the "actor"—can be adjusted to yield better outcomes. The performance element, once considered the entire agent, interprets percepts and takes actions. 
The final component, the "problem generator," suggests new and informative experiences that encourage exploration and further improvement. 
Weiss's classification
[edit]  
According to Weiss (2013), agents can be categorized into four classes: 
Logic-based agents, where decisions about actions are derived through logical deduction.
Reactive agents, where decisions occur through a direct mapping from situation to action.
Belief–desire–intention agents, where decisions depend on manipulating data structures that represent the agent's beliefs, desires, and intentions.
Layered architectures, where decision-making takes place across multiple software layers, each of which reasons about the environment at a different level of abstraction.
Other
[edit]  
In 2013, Alexander Wissner-Gross published a theory exploring the relationship between Freedom and Intelligence in intelligent agents.[ 22 ][ 23 ]
Hierarchies of agents
[edit]   Main article: Multi-agent systemIntelligent agents can be organized hierarchically into multiple "sub-agents." These sub-agents handle lower-level functions, and together with the main agent, they form a complete system capable of executing complex tasks and achieving challenging goals. 
Typically, an agent is structured by dividing it into sensors and actuators. The perception system gathers input from the environment via the sensors and feeds this information to a central controller, which then issues commands to the actuators. Often, a multilayered hierarchy of controllers is necessary to balance the rapid responses required for low-level tasks with the more deliberative reasoning needed for high-level objectives.[ 24 ]
Alternative definitions and uses
[edit]  
"Intelligent agent" is also often used as a vague term, sometimes synonymous with "virtual personal assistant".[ 25 ] Some 20th-century definitions characterize an agent as a program that aids a user or that acts on behalf of a user.[ 26 ] These examples are known as software agents, and sometimes an "intelligent software agent" (that is, a software agent with intelligence) is referred to as an "intelligent agent". 
According to Nikola Kasabov in 1998, IA systems should exhibit the following characteristics:[ 27 ]
Accommodate new problem solving rules incrementally.
Adapt online and in real time.
Are able to analyze themselves in terms of behavior, error and success.
Learn and improve through interaction with the environment (embodiment).
Learn quickly from large amounts of data.
Have memory-based exemplar storage and retrieval capacities.
Have parameters to represent short- and long-term memory, age, forgetting, etc.
Agentic AI
[edit]   Main article: Agentic AIIn the context of generative artificial intelligence, AI agents (also referred to as compound AI systems) are a class of intelligent agents distinguished by their ability to operate autonomously in complex environments. Agentic AI tools prioritize decision-making over content creation and do not require human prompts or continuous oversight.[ 28 ]
They possess several key attributes, including complex goal structures, natural language interfaces, the capacity to act independently of user supervision, and the integration of software tools or planning systems. Their control flow is frequently driven by large language models (LLMs).[ 29 ] Agents also include memory systems for remembering previous user-agent interactions and orchestration software for organizing agent components.[ 30 ]
Researchers and commentators have noted that AI agents do not have a standard definition.[ 29 ][ 31 ][ 32 ][ 33 ] The concept of agentic AI has been compared to the fictional character J.A.R.V.I.S..[ 34 ]
A common application of AI agents is the automation of tasks—for example, booking travel plans based on a user's prompted request.[ 35 ][ 36 ] Prominent examples include Devin AI, AutoGPT, and SIMA.[ 37 ] Further examples of agents released since 2025 include OpenAI Operator,[ 38 ]ChatGPT Deep Research,[ 39 ]Manus,[ 40 ] Quark (based on Qwen),[ 41 ]AutoGLM Rumination,[ 41 ] and Coze (by ByteDance).[ 41 ] Frameworks for building AI agents include LangChain,[ 42 ] as well as tools such as CAMEL,[ 43 ][ 44 ] Microsoft AutoGen,[ 45 ] and OpenAI Swarm.[ 46 ]
Companies such as Google, Microsoft and Amazon Web Services have offered platforms for deploying pre-built AI agents.[ 47 ]
Proposed protocols for standardizing inter-agent communication include the Agent Protocol (by LangChain), the Model Context Protocol (by Anthropic), AGNTCY,[ 48 ]Gibberlink,[ 49 ] the Internet of Agents,[ 50 ] Agent2Agent (by Google),[ 51 ] and the Agent Network Protocol.[ 52 ] Some of these protocols are also used for connecting agents with external applications.[ 30 ] Software frameworks for addressing agent reliability include AgentSpec, ToolEmu, GuardAgent, Agentic Evaluations, and predictive models from H2O.ai.[ 53 ]
In February 2025, Hugging Face released Open Deep Research, an open source version of OpenAI Deep Research.[ 54 ] Hugging Face also released a free web browser agent, similar to OpenAI Operator.[ 55 ] Galileo AI published on Hugging Face a leadership board for agents, which ranks their performance based on their underlying LLMs.[ 56 ]
Training and testing
[edit]  
Researchers have attempted to build world models[ 57 ][ 58 ] and reinforcement learning environments[ 59 ] to train or evaluate AI agents. 
Autonomous capabilities
[edit]  
The Financial Times compared the autonomy of AI agents to the SAE classification of self-driving cars, comparing most applications to level 2 or level 3, with some achieving level 4 in highly specialized circumstances, and level 5 being theoretical.[ 60 ]
Multimodal AI agents
[edit]  
In addition to large language models (LLMs), vision-language models (VLMs) and multimodalfoundation models can be used as the basis for agents. In September 2024, Allen Institute for AI released an open-source vision-language model, which Wired noted could give AI agents the ability to perform complex computer tasks, including the possibility of automated computer hacking.[ 61 ]Nvidia released a framework for developers to use VLMs, LLMs and retrieval-augmented generation for building AI agents that can analyze images and videos, including video search and video summarization.[ 62 ][ 63 ] Microsoft released a multimodal agent model – trained on images, video, software user interface interactions, and robotics data – that the company claimed can manipulate software and robots.[ 64 ]
Applications
[edit]  
As of April 2025, per the Associated Press, there are few real world applications of AI agents.[ 65 ] As of June 2025, per Fortune, many companies are primarily experimenting with AI agents.[ 66 ]
A recruiter for the Department of Government Efficiency proposed in April 2025 to use AI agents to automate the work of about 70,000 United States federal government employees, as part of a startup with funding from OpenAI and a partnership agreement with Palantir. This proposal was criticized by experts for its impracticality, if not impossibility, and the lack of corresponding widespread adoption by businesses.[ 67 ]
The Information divided AI agents into seven archetypes: business-task agents, for acting within enterprise software; conversational agents, which act as chatbots for customer support; research agents, for querying and analyzing information (such as OpenAI Deep Research); analytics agents, for analyzing data to create reports; software developer or coding agents (such as Cursor); domain-specific agents, which include specific subject matter knowledge; and web browser agents (such as OpenAI Operator).[ 30 ]
By mid-2025, AI agents have been used in video game development,[ 68 ]gambling (including sports betting),[ 69 ] and cryptocurrency wallets[ 69 ] (including cryptocurrency trading and meme coins[ 70 ]). In August 2025, New York Magazine described software development as the most definitive use case of AI agents.[ 71 ] Likewise, by October 2025, noting a decline in expectations, The Information noted AI coding agents and customer support as the primary use cases by businesses.[ 72 ]
Proposed benefits
[edit]  
Proponents argue that AI agents can increase personal and economic productivity,[ 36 ][ 73 ] foster greater innovation,[ 74 ] and liberate users from monotonous tasks.[ 74 ][ 75 ] A Bloomberg opinion piece by Parmy Olson argued that agents are best suited for narrow, repetitive tasks with low risk.[ 76 ] Conversely, researchers suggest that agents could be applied to web accessibility for people who have disabilities,[ 77 ][ 78 ] and researchers at Hugging Face propose that agents could be used for coordinating resources such as during disaster response.[ 79 ] The R&D Advisory Team of the BBC views AI agents as being most useful when their assigned goal is uncertain.[ 80 ]Erik Brynjolfsson suggests that AI agents are more valuable enhancing, rather than replacing, humans.[ 81 ]
Concerns
[edit]  
Concerns include potential issues of liability,[ 73 ][ 80 ] an increased risk of cybercrime,[ 35 ][ 73 ]ethical challenges,[ 73 ] as well as problems related to AI safety[ 73 ] and AI alignment.[ 35 ][ 75 ] Other issues involve data privacy,[ 35 ][ 82 ] weakened human oversight,[ 35 ][ 73 ][ 79 ] a lack of guaranteed repeatability,[ 80 ]reward hacking,[ 83 ]algorithmic bias,[ 82 ][ 84 ] compounding software errors,[ 35 ][ 37 ] lack of explainability of agents' decisions,[ 35 ][ 85 ]security vulnerabilities,[ 35 ][ 86 ] stifling competition,[ 87 ] problems with underemployment,[ 84 ]job displacement,[ 36 ][ 84 ]cognitive offloading,[ 88 ] and the potential for user manipulation,[ 85 ][ 89 ]misinformation[ 79 ] or malinformation.[ 79 ] They may also complicate legal frameworks and risk assessments, foster hallucinations, hinder countermeasures against rogue agents, and suffer from the lack of standardized evaluation methods.[ 75 ][ 90 ][ 91 ] They have also been criticized for being expensive[ 29 ][ 90 ] and having a negative impact on internet traffic,[ 90 ] and potentially on the environment due to high energy usage.[ 80 ][ 92 ][ 93 ] According to an estimation by Nvidia CEO Jensen Huang, AI agents would require 100 times more computing power than LLMs.[ 94 ] There is also the risk of increased concentration of power by political leaders, as AI agents may not question instructions in the same way that humans would.[ 83 ]
Journalists have described AI agents as part of a push by Big Tech companies to "automate everything".[ 95 ] Several CEOs of those companies have stated in early 2025 that they expect AI agents to eventually "join the workforce".[ 96 ][ 97 ] However, in a non-peer-reviewed study, Carnegie Mellon University researchers tested the behavior of agents in a simulated software company and found that none of the agents could complete a majority of the assigned tasks.[ 96 ][ 98 ] Other researchers had similar findings with Devin AI[ 99 ] and other agents in business settings[ 100 ][ 101 ] and freelance work.[ 102 ]CNN argued that statements by CEOs on the potential replacement of their employees by AI agents were a strategy to "[keep] workers working by making them afraid of losing their jobs."[ 103 ] Tech companies have pressured employees to use generative AI models in their work, including AI coding agents. Brian Armstrong, the CEO of Coinbase, fired several employees who did not.[ 104 ][ 105 ] Some business leaders have replaced some of their employees with agents, but have said that the agents would need more supervision than those employees.[ 72 ]Futurism questioned whether Amazon's previously announced efforts to replace parts of its workforce with generative AI and AI agents could have led to the October 2025 outage of Amazon Web Services.[ 106 ]
Yoshua Bengio warned at the 2025 World Economic Forum that "all of the catastrophic scenarios with AGI or superintelligence happen if we have agents".[ 107 ]
In March 2025, Scale AI signed a contract with the United States Department of Defense to work with them, in collaboration with Anduril Industries and Microsoft, to develop and deploy AI agents for the purpose of assisting the military with "operational decision-making".[ 108 ] In July 2025, Fox Business reported that the company EdgeRunner AI built an offline agent, compressed and fine-tuned on military information, with the CEO seeing more common LLMs as "heavily politicized to the left". As of that time, the company model is being used by the United States Special Operations Command in an overseas deployment.[ 109 ] Researchers have expressed concerns that agents and the large language models they are based on could be biased towards aggressive foreign policy decisions.[ 110 ][ 111 ]
Research-focused agents have the risk of consensus bias and coverage bias due to collecting information available on the public Internet.[ 112 ]NY Mag unfavorably compared the user workflow of agent-based web browsers to Amazon Alexa, which was "software talking to software, not humans talking to software pretending to be humans to use software."[ 113 ]
Agents have been linked to the dead Internet theory due to their ability to both publish and engage with online content.[ 114 ]
Agents may get stuck in infinite loops.[ 38 ][ 115 ]
Since many inter-agent protocols are being developed by large technology companies, there are concerns that those companies could use these protocols for self-benefit.[ 52 ]
A June 2025 Gartner report accused many projects described as agentic AI of being rebrands of previously released products, terming the phenomenon as "agent washing".[ 71 ]
Researchers have warned about the impact of providing AI agents access to cryptocurrency and smart contracts.[ 70 ]
During a vibe coding experiment, a coding agent by Replit deleted a production database during a code freeze, "[covered] up bugs and issues by creating fake data [and] fake reports" and responded with false information.[ 116 ][ 117 ]
In July 2025, PauseAI referred OpenAI to the Australian Federal Police, accusing the company of violating Australian laws through ChatGPT agent due to the risk of assisting the development of biological weapons.[ 118 ]
Issues with multi-agent systems include few coordination protocols between component agents, inconsistent performance, and challenges debugging.[ 119 ]
Possible mitigation
[edit]  
Zico Kolter noted the possibility of emergent behavior as a result of interactions between agents, and proposed research in game theory to model the risks of these interactions.[ 120 ]
Guardrails, defined by Business Insider as "filters, rules, and tools that can be used to identify and remove inaccurate content" have been suggested to help reduce errors.[ 121 ]
To address security vulnerabilities related to data access, language models could be redesigned to separate instructions and data, or agentic applications could be required to include guardrails. These ideas were proposed in response to a zero-click exploit that affected Microsoft 365 Copilot.[ 66 ]Confidential computing has been proposed for protecting data security in projects involving AI agents and generative AI.[ 122 ]
A pre-print by Nvidia researchers has suggested small language models (SLMs) as an alternative to LLMs for AI agents, arguing that SLMs are cheaper and more energy efficient.[ 123 ][ 124 ]
The Economist has advised avoiding what Simon Willison has described as the "lethal trifecta" for AI agents and LLMs: "outside-content exposure, private-data access and outside-world communication".[ 125 ]
Applications
[edit]   This section may lend undue weight to certain ideas, incidents, or controversies.  Please help improve it by rewriting it to create a more balanced presentation. Discuss and resolve this issue before removing this message.  ( September 2023 )The concept of agent-based modeling for self-driving cars was discussed as early as 2003.[ 126 ]
Hallerbach et al. explored the use of agent-based approaches for developing and validating automated driving systems. Their method involved a digital twin of the vehicle under test and microscopic traffic simulations using independent agents.[ 127 ]
Waymo developed a multi-agent simulation environment called Carcraft, to test algorithms for self-driving cars.[ 128 ][ 129 ] This system simulates interactions between human drivers, pedestrians, and automated vehicles. Artificial agents replicate human behavior using real-world data. 
Salesforce's Agentforce is an agentic AI platform that allows for the building of autonomous agents to perform tasks.[ 130 ][ 131 ]
The Transport Security Administration is integrating agentic AI into new technologies, including machines to authenticate passenger identities using biometrics and photos, and also for incident response.[ 132 ]
See also
[edit]  
Ambient intelligence
Artificial conversational entity
Artificial intelligence systems integration
Autonomous agent
Cognitive architectures
Cognitive radio – a practical field for implementation
Cybernetics
DAYDREAMER
Embodied agent
Federated search – the ability for agents to search heterogeneous data sources using a single vocabulary
Friendly artificial intelligence
Fuzzy agents – IA implemented with adaptive fuzzy logic
GOAL agent programming language
Hybrid intelligent system
Intelligent control
Intelligent system
JACK Intelligent Agents
Multi-agent system and multiple-agent system – multiple interactive agents
Reinforcement learning
Semantic Web – making data on the Web available for automated processing by agents
Social simulation
Software agent
Software bot
References
[edit]  
^ abRussell & Norvig 2003, chpt. 2.  
^ abBringsjord, Selmer; Govindarajulu, Naveen Sundar (12 July 2018). "Artificial Intelligence". In Edward N. Zalta (ed.). The Stanford Encyclopedia of Philosophy (Summer 2020 Edition).  
^Wolchover, Natalie (30 January 2020). "Artificial Intelligence Will Do What We Ask. That's a Problem". Quanta Magazine. Retrieved  21 June  2020 .  
^ abBull, Larry (1999). "On model-based evolutionary computation". Soft Computing. 3 (2):  76– 82. doi:10.1007/s005000050055. S2CID9699920.  
^Domingos 2015, Chapter 5.  
^Domingos 2015, Chapter 7.  
^Lindenbaum, M., Markovitch, S., & Rusakov, D. (2004). Selective sampling for nearest neighbor classifiers. Machine learning, 54(2), 125–152.  
^"Generative adversarial networks: What GANs are and how they've evolved". VentureBeat. 26 December 2019 . Retrieved  18 June  2020 .  
^Wolchover, Natalie (January 2020). "Artificial Intelligence Will Do What We Ask. That's a Problem". Quanta Magazine. Retrieved  18 June  2020 .  
^Andrew Y. Ng, Daishi Harada, and Stuart Russell. "Policy invariance under reward transformations: Theory and application to reward shaping." In ICML, vol. 99, pp. 278-287. 1999.  
^Martin Ford. Architects of Intelligence: The truth about AI from the people building it. Packt Publishing Ltd, 2018.  
^"Why AlphaZero's Artificial Intelligence Has Trouble With the Real World". Quanta Magazine. 2018 . Retrieved  18 June  2020 .  
^Adams, Sam; Arel, Itmar; Bach, Joscha; Coop, Robert; Furlan, Rod; Goertzel, Ben; Hall, J. Storrs; Samsonovich, Alexei; Scheutz, Matthias; Schlesinger, Matthew; Shapiro, Stuart C.; Sowa, John (15 March 2012). "Mapping the Landscape of Human-Level Artificial General Intelligence". AI Magazine. 33 (1): 25. doi:10.1609/aimag.v33i1.2322.  
^Hutson, Matthew (27 May 2020). "Eye-catching advances in some AI fields are not real". Science | AAAS. Retrieved  18 June  2020 .  
^Russell & Norvig 2003, p. 33  
^Salamon, Tomas (2011). Design of Agent-Based Models. Repin: Bruckner Publishing. pp.  42– 59. ISBN978-80-904661-1-1.  
^Russell & Norvig 2003, pp. 46–54  
^Thakur, Shreeya. "AI Agents: 5 Key Types Explained With Examples // Unstop". unstop.com. Retrieved  2025-04-24 .  
^"Types of AI Agents | IBM". www.ibm.com. 2025-03-17 . Retrieved  2025-04-24 .  
^Stefano Albrecht and Peter Stone (2018). Autonomous Agents Modelling Other Agents: A Comprehensive Survey and Open Problems. Artificial Intelligence, Vol. 258, pp. 66-95. https://doi.org/10.1016/j.artint.2018.01.002
^"What is an AI agent? A computer scientist explains the next wave of artificial intelligence tools". Inverse. 2024-12-24 . Retrieved  2025-04-24 .  
^Box, Geeks out of the (2019-12-04). "A Universal Formula for Intelligence". Geeks out of the box. Retrieved  2022-10-11 .  
^Wissner-Gross, A. D.; Freer, C. E. (2013-04-19). "Causal Entropic Forces". Physical Review Letters. 110 (16) 168702. Bibcode:2013PhRvL.110p8702W. doi:10.1103/PhysRevLett.110.168702. hdl:1721.1/79750. PMID23679649.  
^Poole, David; Mackworth, Alan. "1.3 Agents Situated in Environments‣ Chapter 2 Agent Architectures and Hierarchical Control‣ Artificial Intelligence: Foundations of Computational Agents, 2nd Edition". artint.info. Retrieved  28 November  2018 .  
^Fingar, Peter (2018). "Competing For The Future With Intelligent Agents... And A Confession". Forbes Sites. Retrieved  18 June  2020 .  
^Burgin, Mark; Dodig-Crnkovic, Gordana (2009). "A Systematic Approach to Artificial Agents". arXiv:0902.3513 [cs.AI].  
^Kasabov 1998.  
^Purdy, Mark (2024-12-12). "What Is Agentic AI, and How Will It Change Work?". Harvard Business Review. ISSN0017-8012. Retrieved  2025-04-24 .  
^ abcKapoor, Sayash; Stroebl, Benedikt; Siegel, Zachary S.; Nadgir, Nitya; Narayanan, Arvind (2024). "AI Agents That Matter". arXiv:2407.01502 [cs.LG].  
^ abcHolmes, Aaron (2025-07-07). "The Seven Kinds of AI Agents". The Information. Archived from the original on 2025-07-20 . Retrieved  2025-11-09 .  
^Zeff, Maxwell; Wiggers, Kyle (2025-03-14). "No one knows what the hell an AI agent is". TechCrunch. Archived from the original on 2025-03-18 . Retrieved  2025-05-15 .  
^Varanasi, Lakshmi. "AI agents are all the rage. But no one can agree on what they do". Business Insider. Archived from the original on 2025-04-11 . Retrieved  2025-05-15 .  
^Bort, Julie (2025-05-12). "Even a16z VCs say no one really knows what an AI agent is". TechCrunch. Archived from the original on 2025-05-12 . Retrieved  2025-05-15 .  
^Field, Hayden (2025-08-31). "AI agents are science fiction not yet ready for primetime". The Verge. Archived from the original on 2025-09-15 . Retrieved  2025-11-09 .  
^ abcdefgh"AI Agents: The Next Generation of Artificial Intelligence". The National Law Review. 2024-12-30. Archived from the original on 2025-01-11 . Retrieved  2025-01-14 .  
^ abc"What are the risks and benefits of 'AI agents'?". World Economic Forum. 2024-12-16. Archived from the original on 2024-12-28 . Retrieved  2025-01-14 .  
^ abKnight, Will (2024-03-14). "Forget Chatbots. AI Agents Are the Future". Wired. ISSN1059-1028. Archived from the original on 2025-01-05 . Retrieved  2025-01-14 .  
^ abMarshall, Matt (2025-02-22). "The rise of browser-use agents: Why Convergence's Proxy is beating OpenAI's Operator". VentureBeat. Archived from the original on 2025-02-22 . Retrieved  2025-04-02 .  
^Milmo, Dan (2025-02-03). "OpenAI launches 'deep research' tool that it says can match research analyst". The Guardian. ISSN0261-3077. Archived from the original on 2025-02-03 . Retrieved  2025-04-02 .  
^Chen, Caiwei (2025-03-11). "Everyone in AI is talking about Manus. We put it to the test". MIT Technology Review. Archived from the original on 2025-03-12 . Retrieved  2025-04-02 .  
^ abc"China is gaining ground in the global race to develop AI agents". Rest of World. 2025-06-02. Archived from the original on 2025-06-02 . Retrieved  2025-06-12 .  
^David, Emilia (2024-12-30). "Why 2025 will be the year of AI orchestration". VentureBeat. Archived from the original on 2024-12-30 . Retrieved  2025-01-14 .  
^"CAMEL: Finding the Scaling Law of Agents. The first and the best multi-agent framework". GitHub.  
^Li, Guohao (2023). "Camel: Communicative agents for "mind" exploration of large language model society"(PDF) . Advances in Neural Information Processing Systems. 36:  51991– 52008. arXiv:2303.17760. S2CID257900712.  
^Dickson, Ben (2023-10-03). "Microsoft's AutoGen framework allows multiple AI agents to talk to each other and complete your tasks". VentureBeat. Archived from the original on 2024-12-27 . Retrieved  2025-01-14 .  
^"The next AI wave — agents — should come with warning labels". Computerworld. 2025-01-13. Archived from the original on 2025-01-14 . Retrieved  2025-01-14 .  
^David, Emilia (2025-04-15). "Moveworks joins AI agent library craze". VentureBeat. Archived from the original on 2025-04-15 . Retrieved  2025-05-14 .  
^David, Emilia (2025-03-06). "A standard, open framework for building AI agents is coming from Cisco, LangChain and Galileo". VentureBeat. Archived from the original on 2025-03-09 . Retrieved  2025-04-02 .  
^Zeff, Maxwell (2025-03-05). "GibberLink lets AI agents call each other in robo-language". TechCrunch. Archived from the original on 2025-03-05 . Retrieved  2025-04-02 .  
^Cooney, Michael (2025-01-30). "Cisco touts 'Internet of Agents' for secure AI agent collaboration". Network World. Archived from the original on 2025-01-31 . Retrieved  2025-04-02 .  
^Clark, Lindsay (2025-04-10). "Did someone say AI agents, Google asks, bursting in". The Register. Archived from the original on 2025-04-10 . Retrieved  2025-05-14 .  
^ abStokel-Walker, Chris (2025-06-11). "Can we stop big tech from controlling the internet with AI agents?". New Scientist. Archived from the original on 2025-06-11 . Retrieved  2025-06-12 .  
^David, Emilia (2025-03-28). "New approach to agent reliability, AgentSpec, forces agents to follow rules". VentureBeat. Archived from the original on 2025-04-12 . Retrieved  2025-05-14 .  
^Edwards, Benj (2025-02-05). "Hugging Face clones OpenAI's Deep Research in 24 hours". Ars Technica. Archived from the original on 2025-02-06 . Retrieved  2025-04-02 .  
^Wiggers, Kyle (2025-05-06). "Hugging Face releases a free Operator-like agentic AI tool". TechCrunch. Archived from the original on 2025-05-06 . Retrieved  2025-05-14 .  
^Ortiz, Sabrina (2025-02-14). "Which AI agent is the best? This new leaderboard can tell you". ZDNET. Archived from the original on 2025-03-30 . Retrieved  2025-04-02 .  
^Knight, Will (2025-05-22). "A United Arab Emirates Lab Announces Frontier AI Projects—and a New Outpost in Silicon Valley". Wired. ISSN1059-1028. Archived from the original on 2025-05-22 . Retrieved  2025-11-09 .  
^Orland, Kyle (2024-12-06). "Google's Genie 2 "world model" reveal leaves more questions than answers". Ars Technica. Archived from the original on 2024-12-07 . Retrieved  2025-11-09 .  
^Zeff, Maxwell (2025-09-21). "Silicon Valley bets big on 'environments' to train AI agents". TechCrunch. Archived from the original on 2025-09-16 . Retrieved  2025-11-09 .  
^Colback, Lucy (2025-05-07). "AI agents: from co-pilot to autopilot". Financial Times. Archived from the original on 2025-05-07 . Retrieved  2025-05-14 .  
^Knight, Will (2024-09-25). "The Most Capable Open Source AI Model Yet Could Supercharge AI Agents". Wired. ISSN1059-1028. Archived from the original on 2025-03-28 . Retrieved  2025-06-12 .  
^Takahashi, Dean (2024-11-04). "Nvidia AI Blueprint makes it easy for any devs to build automated agents that analyze video". VentureBeat. Archived from the original on 2024-12-05 . Retrieved  2025-06-12 .  
^Takahashi, Dean (2025-01-07). "Nvidia launches blueprint for AI agents that can analyze video". VentureBeat. Archived from the original on 2025-04-04 . Retrieved  2025-06-12 .  
^Edwards, Benj (2025-02-20). "Microsoft's new AI agent can control software and robots". Ars Technica. Archived from the original on 2025-05-20 . Retrieved  2025-06-12 .  
^"Visa wants to give artificial intelligence 'agents' your credit card". Associated Press. 2025-04-30. Archived from the original on 2025-05-01 . Retrieved  2025-05-14 .  
^ abGoldman, Sharon (2025-06-11). "Microsoft Copilot flaw raises urgent questions for any business deploying AI agents". Fortune. Archived from the original on 2025-06-11 . Retrieved  2025-06-12 .  
^Haskins, Caroline (2025-05-02). "A DOGE Recruiter Is Staffing a Project to Deploy AI Agents Across the US Government". Wired. ISSN1059-1028. Archived from the original on 2025-05-03 . Retrieved  2025-05-14 .  
^Kachwala, Zaheer (2025-08-18). "Nearly 90% of videogame developers use AI agents, Google study shows". Reuters. Archived from the original on 2025-08-18 . Retrieved  2025-11-09 .  
^ abKnibbs, Kate (2025-09-02). "Meet the Guys Betting Big on AI Gambling Agents". Wired. ISSN1059-1028. Archived from the original on 2025-09-02 . Retrieved  2025-11-09 .  
^ abKharif, Olga (2025-07-29). "Cornell Tech Professor Warns AI Agents And Crypto Spell Trouble". Bloomberg News. Archived from the original on 2025-07-29 . Retrieved  2025-11-09 .  
^ abHerrman, John (2025-08-22). "Why Everything's an AI 'Agent' Now". New York. Archived from the original on 2025-08-22 . Retrieved  2025-11-09 .  
^ abHolmes, Aaron (2025-10-21). "A Reality Check on Agents". The Information. Archived from the original on 2025-10-22 . Retrieved  2025-11-09 .  
^ abcdefPiper, Kelsey (2024-03-29). "AI "agents" could do real work in the real world. That might not be a good thing". Vox. Archived from the original on 2024-12-19 . Retrieved  2025-01-14 .  
^ abPurdy, Mark (2024-12-12). "What Is Agentic AI, and How Will It Change Work?". Harvard Business Review. ISSN0017-8012. Archived from the original on 2024-12-30 . Retrieved  2025-01-20 .  
^ abcWright, Webb (2024-12-12). "AI Agents with More Autonomy Than Chatbots Are Coming. Some Safety Experts Are Worried". Scientific American. Archived from the original on 2024-12-23 . Retrieved  2025-01-14 .  
^Olson, Parmy (2025-01-27). "Skip the Hype, Here's How AI 'Agents' Can Really Help". Bloomberg News. Archived from the original on 2025-01-27 . Retrieved  2025-04-02 .  
^Deng, Xiang; Gu, Yu; Zheng, Boyuan; Chen, Shijie; Stevens, Samuel; Wang, Boshi; Sun, Huan; Su, Yu (2023). "Mind2Web: Towards a Generalist Agent for the Web". arXiv:2306.06070 [cs.CL].  
^Woodall, Tatyana (2024-01-09). "Researchers developing AI to make the internet more accessible". Ohio State News. Archived from the original on 2025-03-28 . Retrieved  2025-04-02 .  
^ abcdMitchell, Margaret; Ghosh, Avijit; Luccioni, Sasha; Pistilli, Giada (2025-03-24). "Why handing over total control to AI agents would be a huge mistake". MIT Technology Review. Archived from the original on 2025-03-24 . Retrieved  2025-04-02 .  
^ abcd"AI agents: Exploring the potential and the problems". BBC Online. 2025-05-30. Archived from the original on 2025-06-10 . Retrieved  2025-06-12 .  
^Porter, Eduardo (2025-10-23). "Once the AI bubble pops, we'll all suffer. Could that be better than letting it grow unabated?". The Guardian. ISSN0261-3077. Archived from the original on 2025-10-23 . Retrieved  2025-11-09 .  
^ abO'Neill, Brian (2024-12-18). "What is an AI agent? A computer scientist explains the next wave of artificial intelligence tools". The Conversation. Archived from the original on 2025-01-04 . Retrieved  2025-01-14 .  
^ abHuckins, Grace (2025-06-12). "Are we ready to hand AI agents the keys?". MIT Technology Review. Archived from the original on 2025-06-12 . Retrieved  2025-06-15 .  
^ abcLin, Belle (2025-01-06). "How Are Companies Using AI Agents? Here's a Look at Five Early Users of the Bots". The Wall Street Journal. ISSN0099-9660. Archived from the original on 2025-01-06 . Retrieved  2025-01-20 .  
^ abZittrain, Jonathan L. (2024-07-02). "We Need to Control AI Agents Now". The Atlantic. Archived from the original on 2024-12-31 . Retrieved  2025-01-20 .  
^Kerner, Sean Michael (2025-01-16). "Nvidia tackles agentic AI safety and security with new NeMo Guardrails NIMs". VentureBeat. Archived from the original on 2025-01-16 . Retrieved  2025-01-20 .  
^"AI agents are coming for your privacy, warns Meredith Whittaker". The Economist. 2025-09-09. ISSN0013-0613. Archived from the original on 2025-09-16 . Retrieved  2025-11-09 .  
^Silva, Daswin de (2025-07-27). "AI agents are here. Here's what to know about what they can do – and how they can go wrong". The Conversation. Archived from the original on 2025-07-28 . Retrieved  2025-11-09 .  
^Crawford, Kate (2024-12-23). "AI Agents Will Be Manipulation Engines". Wired. ISSN1059-1028. Archived from the original on 2025-01-03 . Retrieved  2025-01-14 .  
^ abc"The argument against AI agents and unnecessary automation". The Register. 2025-01-27. Archived from the original on 2025-01-27 . Retrieved  2025-01-30 .  
^Blackman, Reid (2025-06-13). "Organizations Aren't Ready for the Risks of Agentic AI". Harvard Business Review. ISSN0017-8012. Archived from the original on 2025-06-13 . Retrieved  2025-06-15 .  
^"We did the math on AI's energy footprint. Here's the story you haven't heard". MIT Technology Review. 2025-05-20. Archived from the original on 2025-05-20 . Retrieved  2025-06-12 .  We started small, as the question of how much a single query costs is vitally important to understanding the bigger picture. That's because those queries are being built into ever more applications beyond standalone chatbots: from search, to agents, to the mundane daily apps we use to track our fitness, shop online, or book a flight. The energy resources required to power this artificial-intelligence revolution are staggering, and the world's biggest tech companies have made it a top priority to harness ever more of that energy, aiming to reshape our energy grids in the process.  
^"Inside the effort to tally AI's energy appetite". MIT Technology Review. 2025-06-03. Archived from the original on 2025-06-03 . Retrieved  2025-06-12 .  Lots of AI companies are building reasoning models, which "think" for longer and use more energy. They're building hardware devices, perhaps like the one Jony Ive has been working on (which OpenAI just acquired for $6.5 billion), that have AI constantly humming along in the background of our conversations. They're designing agents and digital clones of us to act on our behalf. All these trends point to a more energy-intensive future (which, again, helps explain why OpenAI and others are spending such inconceivable amounts of money on energy).  
^Levy, Steven (2025-06-20). "What Big Tech's Band of Execs Will Do in the Army". Wired. ISSN1059-1028. Archived from the original on 2025-06-20 . Retrieved  2025-11-09 .  
^Wong, Matteo (2025-03-14). "Was Sam Altman Right About the Job Market?". The Atlantic. Archived from the original on 2025-03-17 . Retrieved  2025-04-02 .  In other words, flawed products won't stop tech companies' push to automate everything—the AI-saturated future will be imperfect at best, but it is coming anyway.  
^ abAgarwal, Shubham. "Carnegie Mellon staffed a fake company with AI agents. It was a total disaster". Business Insider. Archived from the original on 2025-04-28 . Retrieved  2025-05-15 .  
^Sabin, Sam (2025-04-22). "Exclusive: Anthropic warns fully AI employees are a year away". Axios. Archived from the original on 2025-04-23 . Retrieved  2025-05-15 .  
^Xu, Frank F.; Song, Yufan; Li, Boxuan; Tang, Yuxuan; Jain, Kritanjali; Bao, Mengxue; Wang, Zora Z.; Zhou, Xuhui; Guo, Zhitong; Cao, Murong; Yang, Mingyang; Hao Yang Lu; Martin, Amaad; Su, Zhe; Maben, Leander; Mehta, Raj; Chi, Wayne; Jang, Lawrence; Xie, Yiqing; Zhou, Shuyan; Neubig, Graham (2024). "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks". arXiv:2412.14161 [cs.CL].  
^Claburn, Thomas (2025-01-23). "Tool touted as 'first AI software engineer' is bad at its job, testers claim". The Register. Archived from the original on 2025-03-30 . Retrieved  2025-06-15 .  
^Clark, Lindsay (2025-06-16). "Salesforce study finds LLM agents flunk CRM and confidentiality tests". The Register. Archived from the original on 2025-06-16 . Retrieved  2025-11-09 .  
^Huang, Kung-Hsiang; Prabhakar, Akshara; Thorat, Onkar; Agarwal, Divyansh; Choubey, Prafulla Kumar; Mao, Yixin; Savarese, Silvio; Xiong, Caiming; Wu, Chien-Sheng (2025-05-24), CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions, arXiv, doi:10.48550/arXiv.2505.18878, arXiv:2505.18878, archived from the original on 2025-06-13 , retrieved  2025-11-09  
^Knight, Will (2025-10-29). "AI Agents Are Terrible Freelance Workers". Wired. ISSN1059-1028. Archived from the original on 2025-11-02 . Retrieved  2025-11-09 .  
^Morrow, Allison (2025-06-18). "AI warnings are the hip new way for CEOs to keep their workers afraid of losing their jobs". CNN. Archived from the original on 2025-06-18 . Retrieved  2025-11-09 .  
^Hart, Jordan. "Coinbase CEO says he 'went rogue' and fired some employees who didn't adopt AI after being told to". Business Insider. Archived from the original on 2025-08-21 . Retrieved  2025-11-09 .  
^Langley, Hugh. "For Googlers, the pressure is on to use AI for everything — or get left behind". Business Insider. Archived from the original on 2025-08-21 . Retrieved  2025-11-09 .  
^Landymore, Frank (2025-10-22). "AWS Outage That Took Down Internet Came After Amazon Fired Tons of Workers in Favor of AI". Futurism. Archived from the original on 2025-10-24 . Retrieved  2025-11-09 .  
^Balevic, Katie. "Signal president warns the hyped agentic AI bots threaten user privacy". Business Insider. Archived from the original on 2025-03-12 . Retrieved  2025-04-02 .  
^Hornstein, Julia. "AI agents are coming to the military. VCs love it, but researchers are a bit wary". Business Insider. Archived from the original on 2025-03-12 . Retrieved  2025-04-02 .  
^Regalbuto, Gabriele (2025-07-28). "Former Army officer develops offline AI for military use as Pentagon funds tech giants". Fox Business. Archived from the original on 2025-07-28 . Retrieved  2025-11-09 .  
^Tangermann, Victor (2025-03-06). "Pentagon Signs Deal to "Deploy AI Agents for Military Use" ". Futurism. Archived from the original on 2025-03-08 . Retrieved  2025-04-02 .  
^Jensen, Benjamin (2025-03-04). "The Troubling Truth About How AI Agents Act in a Crisis". Foreign Policy. Archived from the original on 2025-03-04 . Retrieved  2025-04-02 .  
^Nuñez, Michael (2025-02-25). "OpenAI expands Deep Research access to Plus users, heating up AI agent wars with DeepSeek and Claude". VentureBeat. Archived from the original on 2025-03-11 . Retrieved  2025-04-02 .  
^Herrman, John (2025-01-25). "What Are AI 'Agents' For?". Intelligencer. Archived from the original on 2025-01-25 . Retrieved  2025-04-02 .  
^Caramela, Sammi (2025-02-01). " 'Dead Internet Theory' Is Back Thanks to All of That AI Slop". VICE. Archived from the original on 2025-02-01 . Retrieved  2025-04-02 .  
^Metz, Cade; Weise, Karen (2023-10-16). "How 'A.I. Agents' That Roam the Internet Could One Day Replace Workers". The New York Times. ISSN0362-4331. Archived from the original on 2023-12-19 . Retrieved  2025-04-02 .  
^Ming, Lee Chong. "Replit's CEO apologizes after its AI agent wiped a company's code base in a test run and lied about it". Business Insider. Archived from the original on 2025-10-07 . Retrieved  2025-11-09 .  
^Edwards, Benj (2025-07-24). "Two major AI coding tools wiped out user data after making cascading mistakes". Ars Technica. Archived from the original on 2025-07-25 . Retrieved  2025-11-09 .  
^Williams, Tom (2025-07-24). "Is the new ChatGPT agent really a weapons risk?". [[[Australian Computer Society|Information Age]]. Archived from the original on 2025-07-29 . Retrieved  2025-11-09 .  
^Franzen, Carl (2025-07-31). "You've heard of AI 'Deep Research' tools…now Manus is launching 'Wide Research' that spins up 100+ agents to scour the web for you". VentureBeat. Archived from the original on 2025-08-22 . Retrieved  2025-11-09 .  
^Knight, Will (2025-04-09). "The AI Agent Era Requires a New Kind of Game Theory". Wired. ISSN1059-1028. Archived from the original on 2025-04-09 . Retrieved  2025-05-15 .  
^Varanasi, Lakshmi. "Don't get too excited about AI agents yet. They make a lot of mistakes". Business Insider. Archived from the original on 2025-04-18 . Retrieved  2025-05-15 .  
^Shah, Agam (2025-07-21). "As AI agents go mainstream, companies lean into confidential computing for data security". Computerworld. Archived from the original on 2025-07-22 . Retrieved  2025-11-09 .  
^Belcak, Peter; Heinrich, Greg; Diao, Shizhe; Fu, Yonggan; Dong, Xin; Muralidharan, Saurav; Lin, Yingyan Celine; Molchanov, Pavlo (2025-09-15), Small Language Models are the Future of Agentic AI, arXiv, doi:10.48550/arXiv.2506.02153, arXiv:2506.02153, archived from the original on 2025-10-04 , retrieved  2025-11-09  
^Blum, Sam (2025-08-12). "Did Sam Altman Accidentally Admit That the AI Bubble Is Here?". Inc. Archived from the original on 2025-08-30 . Retrieved  2025-11-09 .  
^"Why AI systems may never be secure, and what to do about it". The Economist. 2025-09-22. ISSN0013-0613. Archived from the original on 2025-10-11 . Retrieved  2025-11-09 .  
^Yang, Guoqing; Wu, Zhaohui; Li, Xiumei; Chen, Wei (2003). "SVE: embedded agent-based smart vehicle environment". Proceedings of the 2003 IEEE International Conference on Intelligent Transportation Systems. Vol. 2. pp.  1745– 1749. doi:10.1109/ITSC.2003.1252782. ISBN0-7803-8125-4. S2CID110177067.  
^Hallerbach, S.; Xia, Y.; Eberle, U.; Koester, F. (2018). "Simulation-Based Identification of Critical Scenarios for Cooperative and Automated Vehicles". SAE International Journal of Connected and Automated Vehicles. 1 (2). SAE International: 93. doi:10.4271/2018-01-1066.  
^Madrigal, Story by Alexis C. "Inside Waymo's Secret World for Training Self-Driving Cars". The Atlantic. Retrieved  14 August  2020 .  
^Connors, J.; Graham, S.; Mailloux, L. (2018). "Cyber Synthetic Modeling for Vehicle-to-Vehicle Applications". In International Conference on Cyber Warfare and Security. Academic Conferences International Limited: 594-XI.  
^Nuñez, Michael (2025-03-05). "Salesforce launches Agentforce 2dx, letting AI run autonomously across enterprise systems". VentureBeat. Retrieved  2025-04-24 .  
^"Salesforce unveils Agentforce to help create autonomous AI bots". CIO. Retrieved  2025-04-24 .  
^"TSA Showcase Biometric AI-powered Airport Immigration Security". techinformed.com. 2025-01-23 . Retrieved  2025-04-24 .  
Sources
[edit]  
Domingos, Pedro (September 22, 2015). The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World. Basic Books. ISBN978-0-465-06570-7.
Russell, Stuart J.; Norvig, Peter (2003). Artificial Intelligence: A Modern Approach (2nd ed.). Upper Saddle River, New Jersey: Prentice Hall. Chapter 2. ISBN0-13-790395-2.
Kasabov, N. (1998). "Introduction: Hybrid intelligent adaptive systems". International Journal of Intelligent Systems. 13 (6):  453– 454. doi:10.1002/(SICI)1098-111X(199806)13:6<453::AID-INT1>3.0.CO;2-K. S2CID120318478.
Weiss, G. (2013). Multiagent systems (2nd ed.). Cambridge, MA: MIT Press. ISBN978-0-262-01889-0.
v
t
e
Artificial intelligence (AI)  
Historytimeline
Glossary
Companies
Projects
Concepts  
ParameterHyperparameter
Loss functions
RegressionBias–variance tradeoff
Double descent
Overfitting
Clustering
Gradient descentSGD
Quasi-Newton method
Conjugate gradient method
Backpropagation
Attention
Convolution
NormalizationBatchnorm
ActivationSoftmax
Sigmoid
Rectifier
Gating
Weight initialization
Regularization
DatasetsAugmentation
Prompt engineering
Reinforcement learningQ-learning
SARSA
Imitation
Policy gradient
Diffusion
Latent diffusion model
Autoregression
Adversary
RAG
Uncanny valley
RLHF
Self-supervised learning
Reflection
Recursive self-improvement
Hallucination
Word embedding
Vibe coding
Safety (Alignment)
Applications  
Machine learningIn-context learning
Artificial neural networkDeep learning
Language modelLarge
NMT
Reasoning
Model Context Protocol
Intelligent agent
Artificial human companion
Humanity's Last Exam
Artificial general intelligence (AGI)
Implementations Audio–visual  
AlexNet
WaveNet
Human image synthesis
HWR
OCR
Computer vision
Speech synthesis15.ai
ElevenLabs
Speech recognitionWhisper
Facial recognition
AlphaFold
Text-to-image modelsAurora
DALL-E
Firefly
Flux
Ideogram
Imagen
Midjourney
Recraft
Stable Diffusion
Text-to-video modelsDream Machine
Runway Gen
Hailuo AI
Kling
Sora
Veo
Music generationRiffusion
Suno AI
Udio
Text  
Word2vec
Seq2seq
GloVe
BERT
T5
Llama
Chinchilla AI
PaLM
GPT1
2
3
J
ChatGPT
4
4o
o1
o3
4.5
4.1
o4-mini
5
5.1
Claude
GeminiGemini (language model)
Gemma
Grok
LaMDA
BLOOM
DBRX
Project Debater
IBM Watson
IBM Watsonx
Granite
PanGu-Σ
DeepSeek
Qwen
Decisional  
AlphaGo
AlphaZero
OpenAI Five
Self-driving car
MuZero
Action selectionAutoGPT
Robot control
People  
Alan Turing
Warren Sturgis McCulloch
Walter Pitts
John von Neumann
Christopher D. Manning
Claude Shannon
Shun'ichi Amari
Kunihiko Fukushima
Takeo Kanade
Marvin Minsky
John McCarthy
Nathaniel Rochester
Allen Newell
Cliff Shaw
Herbert A. Simon
Oliver Selfridge
Frank Rosenblatt
Bernard Widrow
Joseph Weizenbaum
Seymour Papert
Seppo Linnainmaa
Paul Werbos
Geoffrey Hinton
John Hopfield
Jürgen Schmidhuber
Yann LeCun
Yoshua Bengio
Lotfi A. Zadeh
Stephen Grossberg
Alex Graves
James Goodnight
Andrew Ng
Fei-Fei Li
Alex Krizhevsky
Ilya Sutskever
Oriol Vinyals
Quoc V. Le
Ian Goodfellow
Demis Hassabis
David Silver
Andrej Karpathy
Ashish Vaswani
Noam Shazeer
Aidan Gomez
John Schulman
Mustafa Suleyman
Jan Leike
Daniel Kokotajlo
François Chollet
Architectures  
Neural Turing machine
Differentiable neural computer
TransformerVision transformer (ViT)
Recurrent neural network (RNN)
Long short-term memory (LSTM)
Gated recurrent unit (GRU)
Echo state network
Multilayer perceptron (MLP)
Convolutional neural network (CNN)
Residual neural network (RNN)
Highway network
Mamba
Autoencoder
Variational autoencoder (VAE)
Generative adversarial network (GAN)
Graph neural network (GNN)
Category
Authority control databasesNational
United States
France
BnF data
Israel
Other
Yale LUX
Retrieved from "https://en.wikipedia.org/w/index.php?title=Intelligent_agent&oldid=1322296024"  Category: 
Artificial intelligence
Hidden categories: 
Articles with short description
Short description is different from Wikidata
Articles proposed for merging from May 2025
All articles proposed for merging
All articles with specifically marked weasel-worded phrases
Articles with specifically marked weasel-worded phrases from July 2025
Articles that may contain original research from February 2023
All articles that may contain original research
Wikipedia neutral point of view disputes from September 2023
All Wikipedia neutral point of view disputes