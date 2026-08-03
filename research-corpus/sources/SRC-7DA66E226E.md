# applsci-15-05663-v2.pdf

Academic Editors: Phivos Mylonas, 

Katia Lida Kermanidis and Manolis 

Maragoudakis 

Received: 13 March 2025 

Revised: 10 May 2025 

Accepted: 16 May 2025 

Published: 19 May 2025 

Citation: Han, Z.; Wang, J.; Yan, X.; 

Jiang, Z.; Zhang, Y.; Liu, S.; Gong, Q.; 

Song, C. CoReaAgents: A 

Collaboration and Reasoning 

Framework Based on LLM-Powered 

Agents for Complex Reasoning Tasks. 

Appl. Sci. 2025, 15, 5663. https:// 

doi.org/10.3390/app15105663 

Copyright: © 2025 by the authors. 

Licensee MDPI, Basel, Switzerland. 

This article is an open access article 

distributed under the terms and 

conditions of the Creative Commons 

Attribution (CC BY) license 

(https://creativecommons.org/ 

licenses/by/4.0/). 

Article 

### CoReaAgents: A Collaboration and Reasoning Framework Based on LLM-Powered Agents for Complex Reasoning Tasks

Zhonghe Han 1,2,3,4,†, Jiaxin Wang 5,† , Xiaolu Yan 6, Zhiying Jiang 5,*, Yuanben Zhang 1,2,3,4, Siye Liu 1,2,3,4, Qihang Gong 1,2,3,4 and Chenwei Song 5 

1 Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100190, China; hanzhonghe317@163.com (Z.H.); zhangyb@aircas.ac.cn (Y.Z.); 18010076513@163.com (S.L.); gongqh@aircas.ac.cn (Q.G.) 

2 Key Laboratory of Network Information System Technology (NIST), Institute of Electronics, Chinese Academy of Sciences, Beijing 100190, China 

3 Key Laboratory of Target Cognition and Application Technology (TCAT), Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100190, China 

4 School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing 100190, China 

5 College of Information Science and Technology, Beijing University of Chemical Technology, Beijing 100029, China; wjx000129@126.com (J.W.); 2023210566@buct.edu.cn (C.S.) 

6 Institute of Tracking and Telecommunications Technology, Beijing 100094, China; yanxl_dut@163.com * Correspondence: jiangzy@buct.edu.cn † These authors contributed equally to this work. 

Abstract: As LLMs demonstrate remarkable reasoning capabilities, LLM-powered agents are seen as key to achieving AGI (Artificial General Intelligence) and are widely applied in various complex real-world scenarios. Nevertheless, existing studies still suffer from missing steps, deviated task execution and incorrect tool selection. This paper proposes CoReaAgents, a collaboration and reasoning framework based on LLM-powered agents, comprising the Plan Agent (as a precise task planner), the Tool Agent (as a proficient tool user) and the Reflect Agent (as an objective task evaluator). These agents simulate the social division of labor and synergistic cooperation to enable each agent to perform different specialized capabilities in order to solve complex tasks together. Through the above mechanism, the CoReaAgents framework has the skills of prospective thinking and flexible execution. To verify the capability of the CoReaAgents framework, this paper conducts extensive experiments on different complex tasks such as tool learning, math reasoning and multi-hop QA. The results show that the CoReaAgents framework outperforms various comparative methods in both quantity and quality. 

Keywords: LLM; LLM-powered agent; artificial intelligence; multi-agent systems; machine learning; smart tools and applications 

1. Introduction AGI (Artificial General Intelligence) refers to a form of AI that possesses the ability 

to understand, learn and apply knowledge across a broad range of tasks with human-like flexibility and adaptability [1]. In recent years, AGI has made notable progress across vari-ous fields, including improving human–computer interactions and optimizing multimodal automation [2,3]. The prevailing consensus is that AI agents are at the forefront of AGI research, given their capacity for a broad spectrum of intelligent operations [4,5]. These agents can sense their surroundings and utilize those perceptions to make decisions aimed at accomplishing defined objectives. Previously, researchers relied on symbolic logic and 

 2 of 26 

reinforcement learning to build agents, such as AlphaGo and the DQN algorithm [6,7]. With the advancement of LLMs (Large Language Models), LLMs equipped with a rich knowledge base and strong reasoning capabilities have become a cornerstone in the devel-opment of AI agents, offering numerous advantages that expand their functionalities [8,9]. Nevertheless, traditional methods may struggle with complex reasoning tasks, but as illus-trated in Figure 1, collaboration among multiple agents significantly enhances the capacity of LLMs to tackle these challenges more effectively. Likewise, MetaGPT [10] utilizes LLM-powered agents to simulate virtual software teams, implementing meta-programming techniques. It enhances the performance of complex software development tasks through social behaviors such as collaboration and competition. 

LLM 

Prompts 

Step-1 

Step-2 

Step-n 

Q 

Question 

# CoReaAgents

# Traditional Method

# (CoT)

### Query meeting of John

### and send email

### reminder to

### john@example.com.

Execute 

Toolset 

Tool Agent 

Tool Augmentation 

Task Execution 

Plan Agent 

Tool Filter 

Task Planning 

Reflect Agent 

Subtask Reflection 

Plan Reflection 

QueryMeeting 

AddMeeting 

AccountInfo 

EmailReminder 

UpdateAccountInfo 

OrganizationMembers 

Figure 1. Comparison of the traditional methods and the proposed CoReaAgents framework. Tradi-tional methods may get confused when executing complex reasoning tasks. In contrast, the CoRe-aAgents framework is equipped with various LLM-powered agents and collaboration mechanisms, which can significantly enhance the reasoning capabilities of LLMs. 

It is widely acknowledged that existing studies on planning strategies for LLM-powered agents have achieved signal success, which can be categorized into two types: static planning and dynamic planning [11]. Static planning methods, such as CoT (Chain of Thought) [12] and ToT (Tree of Thought) [13], enable LLMs to break down reasoning tasks into intermediate steps or subproblems. These approaches often lead to LLMs generating static task plans or sequences of steps that are not re-planned when issues arise during execution, lacking flexibility and causing delays in updating real-time information [14]. In dynamic planning methods, each step is derived through reasoning based on actions and feedback, providing decent capabilities for single-step invocation and planning [15]. However, due to the lack of overall planning capability, dynamic planning methods may encounter issues such as execution deviations and deficiencies in summarization when handling complex or long-term planning tasks [16]. Therefore, previous methods often suffer from missing steps, lags when updating real-time information and deviations in task execution when using LLM-powered agents. To address these challenges, the ability to correct results through reflection is a distinctive reasoning capability of LLMs. Such

 3 of 26 

capabilities enable LLM-powered agents to iteratively evaluate their outputs and adjust the reasoning process accordingly [17]. Consequently, it is essential to devise strategies that integrate the insight and foresight of static planning with the adaptability of dynamic planning through reflective mechanisms. 

Moreover, several studies tackle complex problems by assigning a single agent multi-ple roles within a task [18]. In this paradigm, there is no feedback mechanism from other agents, nor is there communication between different agents. Notably, humans tend to be limited by their own capabilities and knowledge when dealing with complex tasks, and LLM-powered agents with human-like reasoning face similar limitations. To alleviate these challenges, it is often necessary for team members to cooperate and negotiate with one another, whereas a single agent as an individual lacks the ability to synergize their resources in executing the task [19]. Consequently, a multi-agent framework involves two or more agents, each of which has different roles and responsibilities. The communication and nego-tiation mechanisms among multiple agents can effectively enhance the overall performance of task solutions [20]. For example, COPPER [21] enhances the collaborative performance of multi-agent systems through a self-reflective mechanism that enables the intelligence agents to learn from environmental feedback and iteratively improve their behavior. 

In addition to the aforementioned research, there are also studies dedicated to improv-ing LLMs for tool learning to leverage external resources, such as API calls for intermediate steps [22,23]. By utilizing tools, LLMs can significantly improve an agent’s performance on certain tasks, such as improving their accuracy in mathematical reasoning problems [24] and web searching for relevant news [25]. Several studies have improved the ability of LLMs to use tools through fine-tuning. For example, Toolformer [26] employs a self-supervised approach to fine-tune LLMs so that they can acquire the ability to call APIs. These methods necessitate training with specialized datasets and toolsets, limiting their application to proprietary LLMs and their adaptation to various complex tasks. In contrast, there are also methods for using external tools through searching tool documentation or tool descriptions [27]. The main challenge with these approaches is that as the number of tools increases, LLMs tend to get disillusioned and confused when selecting tools [28]. In this regard, exploiting the rich knowledge and powerful comprehension of LLMs for the semantic enhancement of tool descriptions can improve LLMs’ accuracy in retrieving tools and strengthen their ability to utilize external tools. 

To sum up, this paper proposes CoReaAgents, a collaboration and reasoning frame-work based on LLM-powered agents, which benefit from group intelligence [29]. The CoRe-aAgents framework enhances task processing accuracy and quality by simulating social division and collaboration among specialized agents, including the Plan Agent, the Tool Agent and the Reflect Agent. The Plan Agent functions as a precise task planner, responsi-ble for task planning and decision making. It employs prospective reasoning to decompose tasks into multiple subtasks with specific dependencies and execution sequences. The Tool Agent functions as a proficient tool user, performing tool augmentation for each tool in the relevant toolset and executing each subtask as a single-step reasoning task. The Reflect Agent functions as an objective task evaluator, reflecting on the results of each subtask and determining the next planning step based on the current results. This ensures dynamic adjustments in task planning and facilitates reflection throughout the process. Moreover, our framework accomplishes overall planning and intermediate steps through the collabo-ration of multiple team members for continuous adjustment and updating over the course of the tasks. With the assistance of these agents and synergistic mechanisms, the CoReaA-gents framework can significantly improve the ability and effectiveness of LLMs in solving complex reasoning tasks. To validate our framework, we conduct extensive experiments on three distinct complex reasoning tasks. The datasets for these tasks include API-Bank

 4 of 26 

and ToolBench for tool learning, FuncQA and SVAMP for math reasoning and HotpotQA for multi-hop QA. The results show that the CoReaAgents framework outperforms various comparative methods in both quantity and quality. 

In summary, our contributions can be summarized as follows: 

 We propose CoReaAgents, a collaboration and reasoning framework based on LLM-powered agents. This framework simulates social division and cooperation to enhance LLMs’ reasoning and complex task execution capabilities, with a meticulously assem-bled team of diverse agents. 

 Our framework features multiple specialized agents, namely the Plan Agent, which functions as a precise task planner; the Tool Agent, which functions as a proficient tool user; and the Reflect Agent, which functions as an objective task evaluator, thereby effectively targeting complex reasoning tasks. 

 Our framework includes multi-agent communication and negotiation mechanisms that facilitate effective exchange and feedback among different agents, addressing the limitations encountered in planning complex tasks that require iterative updates. 

 Our approach is experimented with on five open-source and challenging datasets across three different complex reasoning tasks. The results show that the CoReaAgents framework outperforms various comparative methods in both quantity and quality. 

2. Related Works 2.1. Complex Reasoning Tasks 

In the field of NLP (natural language processing), complex reasoning tasks usually refer to those problems that require deep analysis and understanding of the available information with the application of reasoning mechanisms in order to draw the correct conclusions [30]. This involves considering multiple variables and conditions, inferring out-comes using logical, inductive, deductive and other modes of reasoning [31,32]. Complex reasoning tasks typically require integrating various information sources to build inference chains, uncovering deeper associations and deriving inferred results. Currently, LLMs can handle common tasks like natural language understanding and text generation, but when task complexity exceeds a certain threshold, they may struggle to manage this [33]. Com-pared to traditional complex reasoning tasks such as logical reasoning and common sense reasoning, tasks such as tool learning, math reasoning and multi-hop QA present unique challenges. Addressing these tasks demands robust reasoning capabilities, sophisticated planning mechanisms and effective tool invocation strategies. As LLMs continue to exhibit strong language comprehension and text generation capabilities, research into using LLMs to tackle these complex tasks deepens and progresses with ongoing innovation. 

The tool learning task allows LLMs to enhance their ability to solve problems and perform tasks by invoking external tools, such as Application Programming Interfaces (APIs) [34]. The core goal of this task is to enable the model to understand user commands and to select the appropriate tool to perform a specific operation based on those commands, eventually reaching the demands of the user. Tool learning is a highly complex and diverse domain used to obtain not only strong language comprehension but also the capability to perform multi-step operations and interact with external tools [35]. For this task, DFSDT [36] explores different reasoning paths by simulating a Depth-First Search (DFS) of a decision tree and makes decisions during the search process to find an efficient way to solve a problem. ToolNet [28] is designed to connect LLMs to a large number of tools by constructing a directed graph, thus improving their ability to handle real-world tasks. Nevertheless, the tool learning task demands a high level of operational planning and the utilization of tools.

 5 of 26 

The math reasoning task involves the application of mathematical knowledge and logical reasoning skills to solve mathematical problems [37]. This type of task usually relates to the understanding of mathematical concepts, executing mathematical operations and developing problem-solving strategies [38]. The solution of this task requires the model to understand problem descriptions in natural language and to extract key information from them, such as numbers, operators and the specific requirements of the problem. The initial idea was to use natural language fundamentals to solve math problems through a series of intermediate steps [39]. Since then, this task has emerged as a crucial method for evaluating and enhancing the ability of NLP models to understand natural language and perform complex computations. Self-Consistency [40] selects the most consistent answer in the final answer set by sampling diverse reasoning paths. Self-Contrast [41] encourages LLMs to autonomously generate multiple different prompts, each representing a unique perspective on problem solving. These perspectives may include different ways of thinking, identities, personalities or preferences and so on. Contrasting differences in perspectives effectively reduce overconfidence or inconsistent feedback when self-evaluating, resulting in improved accuracy and stability in mathematical reasoning. In addition, EASYTOOL [42] designs detailed function usage guides, including parameters and examples, for each arithmetic tool when solving math reasoning problems. These guides help LLMs understand how to use the right arithmetic tools for different scenarios. Due to the limited computational ability of LLMs, it is essential to enhance the capability of LLM-powered agents to leverage external tools for assistance with math reasoning tasks. 

The multi-hop QA task requires the model to extract information sequentially from multiple sources, rather than relying on a single source, to obtain the final answer [43]. The completion of multi-hop QA requires integrating information from different documents, which is more complex than using a single document or reasoning based on logic or common sense. In the early days, some research focused on simple QA, which could usually be solved directly [44]. As research on QA tasks advances, many researchers are turning to a more complex QA scenario, which is multi-hop QA. Many studies have proposed a variety of techniques for solving multi-hop QA tasks, including embedding-based approaches, path-based approaches and logic-based approaches [45,46]. These approaches are designed to improve the performance of the model in multi-hop QA tasks, including understanding the complexity of the questions and improving the accuracy of the reasoning. With the development of LLMs, many studies have begun to explore the use of LLMs to handle multi-hop QA tasks. DIETNERD [47] is based on LLMs and aims to enhance public health education about diet and nutrition by summarizing and evaluating peer-reviewed scientific articles. AMOR [48] formalizes reasoning logic as a finite state machine (FSM). In this way, AMOR is able to deal with problems in a stepwise and systematic way until a final answer is found. HGOT [49] uses a divide and conquer strategy to solve problems by constructing a hierarchical, structured graph to organize and optimize the retrieval of relevant information. GMeLLo [50] solves multi-hop QA tasks after knowledge editing by integrating LLMs and knowledge graphs. However, LLM-powered agents still have substantial room for improvement in planning inference paths and comprehending textual content when addressing multi-hop QA tasks. 

2.2. LLM-Powered Agents 

LLMs have evolved from previous task-specific models for supervised learning on labeled data to modern generalized learning models trained on massive text data [51]. This evolution marks a shift in LLMs from specialization to generalization. The autonomy, environmental awareness and social competence of LLMs enable them to use natural language interactions to accomplish a wide range of tasks [52].

 6 of 26 

A lot of studies have already started to construct AI agents leveraging LLMs [9,53]. Specifically, they use the LLM as the brain or controller of the agent, extending its reasoning capabilities and action space through strategies such as task planning and tool use. In terms of improving the reasoning ability of LLMs, in order to decrease the difficulty encountered by LLMs in providing answers, some studies have been conducted to improve the accuracy of reasoning through problem decomposition methods. For example, methods like CoT [12] choose to decompose the question first and answer a subset of the question later. In contrast to integrating reasoning into the planning process, ReAct separates reasoning from planning and enhances the reasoning capabilities of LLMs by integrating clear reasoning steps with targeted action strategies [15]. Subsequently, more sophisticated reasoning frameworks have been introduced, like ToT (Tree of thoughts) [13], GoT (Graph of thoughts) [54] and several other variants. On the other hand, the use of tools can reduce the inherent limitations of LLMs, including acquiring real-time information, improving math skills and reducing hallucinations. In mathematics and some specialized fields, utilizing tools can reduce error rates [55]. In the domain knowledge of specific models and APIs, the choice to adopt various external tools to enhance LLMs in multiple ways is prevalent. Many studies have long been focused on how to improve the ability of LLMs to use tools. Toolformer [26] uses tools in a self-supervised manner; subsequently, various external tools have emerged to enhance LLMs in multiple ways. ToolAlpaca [56] proposes to build a multi-agent simulation environment by modeling real-world tool usage scenarios. From there, it automatically generates a tool using corpus, which provides a way for LLMs to learn to generalize their tool use capabilities. ToolLLM [36] addresses the need for real-world APIs by leveraging RapidAPI Hub, including both single-tool and multi-tool scenarios. 

Despite the commendable reasoning abilities of LLM-powered agents, they primarily operate as isolated entities [57]. A single agent lacks the capability to collaborate with other agents and acquires knowledge through social interactions. This limitation constrains their potential to learn from the feedback of others, thereby hindering their performance improvement [8]. In addition, they cannot effectively handle complex scenarios that require information sharing. Recent studies have shown that LLMs can improve themselves or bet-ter align themselves with human values by interacting with each other [58]. These advances raise the possibility that LLM-powered agents could be expected to engage in challenges in a more natural way. Each agent in a multi-agent framework has different roles and responsi-bilities, enabling them to coordinate their actions and work together to achieve a goal. This structure reduces the burden on a single agent and thus improves task performance [59]. Some scholars create virtual towns by populating an interactive sandbox environment inspired by the Life Sandbox Game [53]. These agents can perform convincing individual and group social behaviors, providing a whole new perspective. Several studies explore how LLM-powered agents can be applied to Werewolf, which demonstrates the potential of LLM-powered agents in communication games [60]. ChatEval [61] employs multiple agents and debates using different communication strategies to promote the automatic evaluation of LLMs. LangGround [62] is a Multi-Agent Reinforcement Learning (MARL) computational framework that enables agents to learn human-interpretable communication languages in order to collaborate effectively with humans or other agents without prior coordination. AgentDropout [63] identifies and eliminates redundant agents in different communication rounds by optimizing the adjacency matrix of the communication graph to improve the efficiency and performance of multi-agent collaboration. These studies have shown that an effective division of labor among multiple agents can accomplish a larger workload and improve the efficiency and quality of the executions.

 7 of 26 

3. Method In this section, we introduce the CoReaAgents framework, a multi-agent collaboration 

framework that imitates the division of labor in human society. This framework enables not only continuous adjustments to task planning through reflection on the process but also autonomous tool augmentation for task scenarios. Meanwhile, each agent in the CoReaA-gents framework coordinates its actions with the others, acting as team members to achieve a same goal. 

3.1. Overview 

Complex reasoning tasks, characterized by complexity and abstraction, demand ad-vanced cognitive, planning and execution skills from LLM-powered agents. While a single agent has decent reasoning skills, it still essentially completes tasks as a separate individual and cannot handle complex tasks which require competence in multiple domains. To ad-dress these challenges, we propose the CoReaAgents framework, in which each agent has distinct functionalities and equal significance, collectively enhancing overall performance in tackling complex tasks. This allows the framework to correct errors and deviations in a timely manner and continuously optimize the task execution process. In contrast, ReAct, although dynamic, lacks a specialized reflection mechanism to systematically evaluate and adjust task planning, while Reflexion focuses on learning and improving task execution through reflection, but its reflection process is relatively independent, unlike the CoReaA-gents framework, where the Reflect Agent collaborates closely with the other agents to drive the dynamic adjustment of tasks. 

An overview of the CoReaAgents framework is shown in Figure 2, including the Plan Agent, the Tool Agent and the Reflect Agent. In detail, the Plan Agent serves as a precise task planner that thoughtfully considers the task in order to control the overall direction of the task. The Tool Agent serves as a proficient tool user, who has a deep comprehension of external data sources to effectively utilize tools in the completion of a task. The Reflect Agent serves as an objective task evaluator, evaluating the task planning and execution processes from other perspectives, which guarantees the success of the task through continuous reflection and feedback. Through the specialized separation of tasks and a mutual consultation mechanism for each agent, we are able to continuously refine the task plan during task and tool augmentation for autonomous task completion scenarios. 

- Instruction CoReaAgents solves complex tasks Output Result

- Plan Agent Tool Agent

- Reflect Agent

### Step#6: Plan Reflection

Current task planning needs 

no modification 

#Next-Step:Subtask Target_i` 

Import Tool_i` from RTS 

<API>Tool_i` </API> 

Re-Plan 

Step-I in Task Planning 

### Step#5: Subtask Reflection

Re-Select Re-Call Re-Sum 

Tool selected is 

correct? 

Result contains 

error? 

Result consistent 

with target? 

### Step#1: Tool Filter

### Tool Set Related Tool Set

#Step-1: Generate a QR code for the provided 

flight ticket URL 

from tools import Generate QR 

QR_code = <API>Generate QR</API> 

#Step-2: Convert the date '2022-12-25' to the 

Islamic calendar. 

from tools import Convert Date 

Calendar_date = <API>Convert Date</API> 

#Step-3: Generate a random UUID for the hotel 

reservation. 

from tools import Generate UUID 

UUID = <API>Generate UUID()</API> 

#Last-step:Summarize the above results 

#Summarize 

### Step#3: Task Planning

API Name 

API Description 

Parameter Description: 

Parameter 1, 

Description 

Parameter 2, 

Description 

Parameter 3, 

Description 

API Documentation 

API Name 

API Description 

Parameter 1, 

Description 

Augmented API Documentation 

### Step#2: Tool Augmentation

Parameter 2, 

Description 

Parameter 3, 

Description 

Subtask Target: 

Tool: Parameters: "Parameter1": "         ", "Parameter2": "         " 

Execute 

Result 

### Related Tool Set

### Step#4: Task Execution

- A

# 1. A QR code has been successfully

# generated for your flight ticket URL

# 'https://www.airline.com/ticket/

# ABC123' based on the API response.

# 2. Regarding the conversion of the

# date '2022-12-25' to the Islamic

# calendar, 'December 25, 2022' from

# the Gregorian Calendar converts to

# 'Jumada ath-Thaniyah 6, 1444' in the

# Islamic Calendar.

# 3. For your hotel reservation, a

# random UUID has been generated as

# requested. The UUID for your hotel

# reservation is 'cff5b3e8-1d40-4b50-

# bc01-a111aa4a13db'.

# I am planning a trip to Paris next week

# and I would like to generate a QR

# code for my flight ticket. Can you

# please generate a QR code for the

# following URL: 'https://

# www.airline.com/ticket/ABC123'?

# Additionally, I need to convert the

# date '2022-12-25' to the Islamic

# calendar to check if it falls on a

# holiday. Finally, I would like to

# generate a random UUID for my hotel

# reservation. Thank you!

- Q

Figure 2. The overview of our proposed CoReaAgents framework. First, the Plan Agent performs tool filtering and transfers the related tool set to the Tool Agent for tool augmentation. Next, the Plan Agent conducts task planning based on the enhanced tool descriptions, while the Tool Agent executes each subtask of the plan in turn. Finally, the Reflect Agent performs subtask reflection and plan reflection during the execution process, providing feedback on the results to the Tool Agent and the Plan Agent to continuously update task planning.

 8 of 26 

3.2. The Framework of CoReaAgents 3.2.1. Plan Agent: A Precise Task Planner 

There are two categories of static and dynamic planning in the current task reasoning strategies. Static planning lacks the ability to flexibly execute tasks and cannot adjust its approach in a timely manner if problems arise during the execution process.Dynamic planning lacks an overview understanding of the task and could deviate from the task target when performing complex tasks. Thus, we propose the Plan Agent in the CoReaAgents framework, which can provide a blueprint for the execution of the task, controlling the general direction for the task’s accomplishment. Specifically, the primary responsibilities of the Plan Agent include tool filtering and task planning. 

Tool filtering: The Plan Agent filters the retrieved tools to discard irrelevant and redundant information. It accomplishes this by understanding the description, the parame-ters and the role of each tool, which ensures the selections are highly relevant to a specific task. This process can significantly avoid the negative impact of irrelevant information on task planning. 

Task planning with CCoT: Inspired by GOLLIE [64], we propose CCoT (Code and Comments of Thoughts), which accomplishes task planning with codes and comments. As shown in Figure 3, CCoT comprises two main parts: the first part involves analytical natural language task descriptions given as comment parts, and the second part contains the actions needed to invoke the tool as code segments. This not only ensures the continuity of LLMs in carrying out logical planning but also enables LLMs to maintain consistency between the thoughts involved in task planning and the behavior involved in tool invoca-tion. Utilizing this method, the Plan Agent develops a comprehensive planning strategy by decomposing complex tasks into manageable subtasks that exhibit specific dependency relationships and an established execution order. 

API 1, 

API Description 

API 2, 

API Description 

API 3, 

API Description 

Tool Description Documentation augmented by Tool Agent 

Task Information 

Target Task: 

Task Instruction: 

Task Description: 

### Plan Agent

### Task Planning of Plan Agent

#Understand the meaning expressed by the user: 

The user wants to... 

#Step-1: Subtask Target_1 

Import Tool_1 from RTS 

Result1=<API>Tool_1</API> 

#Completing the last step we have learned ...... 

 and the next step we should ... 

#Step-2: Subtask Target_2 

Import Tool_2 from RTS 

Result2=<API>Tool_2</API> 

#So far, we've learned … Next we should... 

#Step-n: Subtask Target_n 

Import Tool_n from RTS 

Resultn=<API>Tool_n </API> 

#Summarize the content and provide feedback to 

the user on the completion of the task. 

#Last-step:Summarize the above results 

#Summarize: ...... 

Task Planning(with CCoT) 

Tool Agent 

Collaboration Planning 

Figure 3. Task planning with the proposed CCoT by the Plan Agent. It takes natural language task descriptions as comment parts (noted as blue words ) and designs the actions required to invoke the tool as code segments (noted as red words). This not only ensures the continuity of LLMs in carrying out logical planning, but also enables LLMs to maintain consistency between the thoughts involved in task planning and the behavior involved in tool invocation.

 9 of 26 

Communication with the Tool Agent and the Reflect Agent. The Plan Agent acts as a precise task planner, taking into account the global aspects with a prospective approach to the overall planning of the task (details in Section 3.3.2). It plans an execution strategy that is coordinated with the plan for reflection of the Reflect Agent and the tool augmentation task of the Tool Agent to facilitate dynamic adjustments of the action path. 

3.2.2. Tool Agent: A Proficient Tool User 

The Tool Agent demonstrates an excellent understanding of tool usage, rapidly al-tering various tool applications to accommodate environmental changes. The primary responsibilities of the Tool Agent include tool augmentation and task execution. 

Tool augmentation. Tools with multiple functions are widely applicable across various scenarios, yet they are often not described in a targeted manner. The Tool Agent leverages the extensive knowledge and strong comprehension abilities of the LLM to enhance the tools required for task completion. As shown in Figure 4, the Tool Agent carries out additional descriptions in the current instruction scenario based on the general description, which improves the accuracy applied by the Plan Agent in planning the task. 

I am planning a trip to Paris next week and I 

would like to generate a QR code for my 

flight ticket. Additionally, I need to convert 

the date '2022-12-25' to the Islamic calendar 

to check if it falls on a holiday. 

Utilizing diverse external 

tools to handle complex 

commands 

Task Instruction 

### Tool Augmentation of Tool Agent

Task Description 

API Name: Convert Date 

API Description: Converts a 

date to a specified calendar. 

thinking 

Parameter Description: 

Parameter Name: "to", 

Description: "The calendar to 

convert the specified date.", 

Required: true 

Parameter Name: "date", 

Description: "A date in \\\\ 

format." 

Required: false 

Parameter Name: "from", 

Description: " " 

Required: false 

API Documentation 

API Name:Convert Date 

API Description:By calling this API, users are 

able to quickly convert a Gregorian date to the 

Islamic calendar (or other supported calendars) 

and accurately determine the significance of that 

date in the target calendar. 

Parameter1: "to", 

Description: "Specifies the target calendar to 

convert to. In user scenarios, this parameter 

should be Islamic to convert calendar dates to the 

Islamic calendar.", 

Required:true 

Parameter2: "date", 

Description: "Specifies the date to be converted. 

In the user's instructions, this parameter should be 

set to the specific calendar date that the user 

wants to convert.", 

Required: false 

Parameter3: "from", 

Description: "Specifies the calendar to which the 

entered date belongs. In user commands, this 

parameter should be Gregorian.", 

Required:false 

Augmented API Documentation 

Tool learning 

Target Task 

Instruction Scenarios 

1.Generate QR Code for URL 

2.Users wishing to know the 

equivalent date of a certain 

date in other calendars 

Tool Agent 

Figure 4. Sample diagram of the Tool Agent performing tool augmentation. In this instructional scenario, the Tool Agent provides additional descriptions based on the tool’s general specifications. 

Task execution. The results from a particular tool often contain substantial data that are irrelevant to the subtask. Such information is regarded as noise for the subtask, potentially impacting its performance. To optimize tool utility, the Tool Agent executes the specific actions planned by the Plan Agent. Specifically, for each subtask to be executed, the Tool Agent invokes the corresponding tool and performs a task summary to obtain the final results of the subtask. 

Execution of the Plan Agent’s planning and its interaction with the Reflect Agent. As a proficient tool user, the Tool Agent can ensure the effective execution of tasks planned by the Plan Agent and provide the CoReaAgents framework with the practical operational capabilities required to complete tasks (details in Section 3.3.1). 

3.2.3. Reflect Agent: An Objective Task Evaluator 

Recent studies have shown that LLMs often display overconfidence in self-reflecting on their own generated content, leading to stubborn feedback [41]. In this regard, the Reflect Agent assesses and reflects on the completion of intermediate steps and task planning from a tertiary perspective. Specifically, the Reflect Agent monitors and analyzes the plan developed by the Plan Agent and the subtask results generated by the Tool Agent to ensure that the task is performed to the expected standard. As a result, the duties of the Reflect Agent are divided into subtask reflection and plan reflection.

 10 of 26 

Subtask reflection. To ensure that each subtask is completed successfully, the Reflect Agent reflects on the results of each subtask after its execution. The Reflect Agent deter-mines whether the tool selected for the current subtask satisfies the expectations based on the relevant tool description. It also further determines exceptions in the process of invoking the tool. Finally, the Reflect Agent evaluates if the execution results summarized by the Tool Agent contain the information needed for the subtask. 

Plan reflection. In order to advance continuous improvement in task planning, the Re-flect Agent constantly forecasts the next step based on currently known information. In this process, the Reflect Agent achieves dynamic task planning by predicting the next pending subtask based on the completed subtasks. Subsequently, the predicted next subtask is compared with the corresponding subtask in the overall plan of the Plan Agent. The pro-gression and learning of complex reasoning tasks by the CoReaAgents framework are achieved by comparing the task target and execution actions of both. 

Reflection for the Plan Agent and the Tool Agent. The Reflect Agent enables reflection on the entire process of task planning and execution, seeking out potential for refinement. The dynamic task planning performed by the Reflect Agent is combined with the global planning performed by the Plan Agent to ensure the expected quality of tasks (details in Section 3.3.3). 

3.3. The Multi-Agent Communication and Negotiation Mechanisms in the CoReaAgents Framework 

Figure 2 illustrates the mechanism through which the various agents act in the CoRe-aAgents framework. Specifically, the Plan Agent and the Tool Agent collaborate to enable the CoReaAgents framework’s autonomous tool filtering and tool augmentation. The Plan Agent conducts task planning with CCoT, leveraging the results of the tool augmenta-tion and then communicating the plan to the Tool Agent to execute each step of the task. The Reflect Agent provides feedback to the Tool Agent and the Plan Agent through subtask reflection and plan reflection. This process enables the facilitation of iterative refinements throughout task execution. 

3.3.1. Autonomous Tool Filter and Tool Augmentation Between the Plan Agent and the Tool Agent 

To avoid irrelevant and redundant information from impacting task planning, we design a synergy mechanism between the Plan Agent and the Tool Agent. Specifically, the Plan Agent performs tool filtering on the toolset prior to task planning, while the Tool Agent augments each tool in the filtered toolset. 

As shown in Figure 2, Step1 gives a toolset TS = {T1, T2, T3, . . . , Tn} containing all the tools and a brief description of each tool Ti in the TS, including tool-related parameters and roles, to make it easy to select the tools that are highly relevant to this task. As shown in Equation (1), the Plan Agent Mplan combines prompts Pf ilter and complex task information I to select a related toolset RTS = {T′ 

1, T′ 2, T′ 

3, . . . , T′ m} where m < n from TS, which reduces 

the negative impact of irrelevant information on task planning. 

RTS = Mplan(Pf ilter, TS, I) (1) 

After the Plan Agent completes tool filtering, the Tool Agent performs tool augmen-tation in RTS. As shown in Figure 4, the Tool Agent combines the task scenario with a general description of the tool to further provide supplementary details specific to the cur-rent command scenario. This mechanism can enhance the accuracy of the tools’ application during subsequent task planning.

 11 of 26 

3.3.2. From Task Planning by the Plan Agent to Task Execution by the Tool Agent 

The Plan Agent performs task planning based on enhanced tool descriptions, and the Tool Agent executes each subtask of the overall plan in turn. The Plan Agent analyzes the given complex task instruction Q and performs task planning to obtain a collection of logically related subtasks S. The Plan Agent selects the appropriate tools to assist with the various subtasks when planning a task in conjunction with the enhanced tool descriptions in RTS. This process can be expressed by the following Equation (2): 

S = Mplan(Pplan, RTS, Q) → {s1, s2, s3, . . . , sn} 

si = {ti, ai, pi, ri} (2) 

where Pplan is a task planning prompt, and n is the number of subtasks. The basic attribute data of any subtask si in S are shown in Table 1. 

Table 1. The details of subtasks’ basic attributes. 

Basic Attribute Notation Attribute Description 

Current subtask si Logical position in the collection of subtasks Subtask target ti Subtask target expressed through comments 

Tool requirement ai Tool to be invoked expressed through code Parameter configuration pi Parameters required to invoke the tool 

Subtask result ri Result of this subtask 

Following the completion of task planning, the Tool Agent completes each subtask si 

in S and consolidates its result. Specifically, as shown in Equation (3), the Tool Agent Mtool 

determines the parameters pi for invoking the tool through subtask target ti, the tool to be invoked ai and an enhanced targeted description of the tool Dai . Eventually, the Tool Agent performs a task summary for ti on the results obtained from the use of external resources to obtain the final result of the subtask ri. Task planning by the Plan Agent and task execution by the Tool Agent based on CCoT can maximize tool utilization and improve task success rates. 

pi = Mtool(Ptool , ti, ai, I, Dai ) 

ri = Mtool(Psum, ti, Exe(ai, pi)) (3) 

where Psum is the task summary prompt and Exe(ai, pi) indicates that ai is invoked by pi 

using the configured interpreter. 

3.3.3. Static and Dynamic Task Planning Combination by the Reflect Agent 

The Reflect Agent performs subtask reflection and plan reflection, consulting with the Tool Agent and the Plan Agent. When the Tool Agent completes each subtask, the Reflect Agent performs subtask reflection on its result, as shown in Figure 5. 

 <Re-Select> indicates that the tool invoked for this subtask needs to be reselected. The Tool Agent needs to reselect the tool and execute it based on the feedback. 

 <Re-Call> indicates that the tool call failed and necessitates a reconsideration of the tool parameters. The Tool Agent needs to analyze the parameters of the call again. 

 <Re-Sum> indicates that the Tool Agent needs to execute the subtask again and sum-marize it based on the feedback. 

The Reflect Agent performs plan reflection for the Plan Agent, thereby enabling continuous iterative updates to the task plan: 

 The Reflect Agent combines information about completed subtasks {s1, s2, s3, . . . , si} to plan the next task s′i+1, drawing inspiration from ReAct [15]. 

 s′i+1 is compared with the corresponding subtask si+1 in the overall plan.

 12 of 26 

 <Re-Plan> indicates that their task target ti+1 or invoked tool ai+1 is inconsistent. the Plan Agent should replan the subsequent tasks. 

After completing the above steps, dynamic planning with flexible execution can be integrated into each step of the overall planning, realizing the organic combination of static and dynamic planning. 

### Subtask Reflection Plan Reflection

### Tool selected for the subtask is correct?

### Re-Select

### Re-Call

### Re-Sum

### Subtask execution result contains

### abnormal information?

### Subtask execution result is consistent with

### the subtask target?

### Current subtask completion result

### Complex task

### instruction

### Plan the next step

### Current task planning needs no

### modification

### Compare with the subtask in the overall

### plan

### Re-Plan

### Completed subtask

### information

Figure 5. The process of the Reflect Agent for subtask reflection and plan reflection. The Reflect Agent first conducts subtask reflection to assess the appropriateness of the selected tool, the execution result and the alignment of the result with the target (noted as the yellow part). Finally, the Reflect Agent conducts plan reflection to perform the next single-step planning process and compare it with the corresponding subtask in the Plan Agent’s plan (noted as the green part). 

4. Experiments In this section, we experiment with our approach in several complex reasoning tasks: 

tool learning, math reasoning and multi-hop QA. We evaluate both the baselines and our approach using GPT-3.5 [65] to ensure a fair comparison with identical model parame-ters. The experimental results reported for each dataset in this study are calculated as the average of five independent trials. Specifically, for each test set, performance metrics are derived from five repeated experiments conducted under identical experimental conditions. The arithmetic mean is employed to mitigate stochastic variations inherent to individ-ual trials, thereby ensuring both result stability and experimental reproducibility. This methodological design minimizes potential confounding effects from singular experimental artifacts while strengthening the statistical validity of the findings. 

4.1. Tool Learning 4.1.1. Settings for Tool Learning 

Datasets 

 ToolBench [36] is a dataset with multiple types of data that covers multiple domain application scenarios and contains over 16,000 real-time APIs collected from the RapidAPI Hub (https://rapidapi.com/hub accessed on 30 January 2025) that cover 49 categories. We evaluate our approach using the most complex subset of ToolBench, including intra-category multi-tool instructions (I2) and intra-collection multi-tool instructions (I3). The final evaluation is divided into three subsets for testing, I2-Inst (200 test data), I2-Cat (200 test data) and I3-Inst (100 test data). 

 API-Bank [34] is a multi-task benchmark consisting of various tools used to evaluate the performance of tool-augmented LLMs. API-Bank involves the offline usage of multiple API tools. We conduct an evaluation on the test data ranging from level-1 to level-2 of this dataset, which comprises a total of 534 test data.

 13 of 26 

Baselines We compared the CoReaAgents framework with the following recent and classic baselines: 

 ReAct [15] guides LLMs to take appropriate actions at each step to solve a particular problem and carry out reasoning for the actions, iterating the process to finally solve the problem. 

 Reflexion [17] enables the LLMs to learn from error information and retry when an error occurs, continuing until the task is successfully completed or the maximum number of reflection attempts is reached. 

 DFSDT [36] simulates the Depth-First Search process by constructing a decision tree to explore different solution paths. 

 EASYTOOL [42] distills the necessary information from tool documentation and converts it into concise tool descriptions, enhancing LLMs’ ability to select tools more accurately. 

 ToolNet [28] organizes the tools into a directed graph, allowing the LLM to start from an initial tool node and iteratively select the next node in the graph until the task is resolved. 

 Tool-Planner [66] performs dynamic solution tree planning based on toolkits, which group APIs with the same functionality into a single toolkit. When tool errors occur, LLMs can reselect tools based on toolkits. 

Evaluation metrics For the ToolBench, we use the Pass Rate from ToolEval [36] to evaluate our framework, 

which is calculated from the proportion of tasks successfully completed with a limited budget. For API-Bank, we use Exact Match (EM) to compare the execution output of LLMs with the real answers. 

4.1.2. Main Results from Tool Learning 

The CoReaAgents framework demonstrated the most advanced performance on Tool-Bench and API-Bank. Table 2 shows the results from tool learning for all baselines and our approach. For ToolBench, our method outperforms Tool-Planner, the baseline with the best average performance, by over 4.0% in terms of Pass Rate. This validates the comprehensive capabilities of the CoReaAgents framework on the ToolBench. The CoRe-aAgents framework achieves varying degrees of improvement on both I2 and I3 tasks. Specifically, the CoReaAgents framework shows a significant improvement in the I3 sce-nario, which demonstrates that our approach is better adapted to multi-category multi-tool task scenarios. 

The same situation is also observed in the API-Bank dataset. For the API-Bank dataset, our method outperforms all baselines in terms of Exact Match (EM). For level-1 and level-2 instructions in API-Bank with a small number of tools, the CoReaAgents framework demonstrates a slight enhancement. This indicates that, even with a single tool or a limited number of tools, the CoReaAgents framework can still select the appropriate tools and generate correct answers. In addition, the experimental results from API-Bank to ToolBench illustrate that the performance of the framework remains stable as the number of tools increases, which reflects its good scalability. 

The rightmost column in Table 2 shows the average number of tokens consumed by the CoReaAgents framework versus other baselines for completing the tool learning task. The results indicate that, despite the higher computational cost associated with the CoReaAgents framework, the trade-off is justified by the enhanced performance in tool learning tasks.

 14 of 26 

Table 2. The results of different baselines and the ablation study in terms of Pass Rate (%) and EM (%). The table highlights the highest scores in bold, with underscores indicating the highest scores achieved by prior methods. - indicates that the method is not publicly available. The rightmost column in the table shows the number of tokens completing this task for each baseline. 

ToolBench (Pass Rate) API-Bank (EM) Methods I2-Ins I2-Cat I3-Ins Average Lv1 + Lv2 Tokens 

ReAct 42.5 46.5 22.0 37.0 70.0 5100 Reflexion 58.0 66.0 55.0 59.7 77.0 8750 DFSDT 75.0 71.5 62.0 69.5 72.0 25,000 

DFSDT-EASYTOOL 77.5 74.5 65.0 72.3 76.4 -ToolNet - - - - 75.0 4112 

ToolNet + Reflexion - - - - 83.0 7950 Tool-Planner 75.5 78.0 66.0 73.2 - -CoReaAgents 80.5 79.0 72.0 77.2 84.0 15,000 

w/o TA 75.0 74.0 68.0 72.3 79.8 w/o RA 73.0 72.5 65.0 70.2 79.5 

w/o TA&RA 70.5 70.0 61.0 67.2 74.5 

4.1.3. Ablation Study of Tool Learning 

In order to assess the impact of specific strategies or team members in the CoReaAgents framework, we perform ablation studies on tool learning datasets to develop three variants of our framework. Note that task planning by the Plan Agent is an indispensable component for solving complex reasoning tasks, making it impossible to remove the Plan Agent from our framework. The settings for the ablation study are as follows: 

 The CoReaAgents framework + w/o TA: the Tool Agent is removed from the CoRe-aAgents framework, meaning that no tool augmentation and subtask execution are conducted when handling complex tasks. 

 The CoReaAgents framework + w/o RA: similarly, the task division of the Reflect Agent, including subtask reflection and plan reflection, is removed from the process. 

 The CoReaAgents framework + w/o TA&RA: the Reflect Agent and the Tool Agent are removed from the processing of complex tasks in the CoReaAgents framework, only utilizing the Plan Agent to complete tasks. 

For tool learning, it is often necessary to use external tools to obtain the information required to complete the task, and LLMs are expected to make timely adjustments to task planning based on the acquired information. Table 2 shows the results of the ablation study. The results show that removing the Reflect Agent has the greatest impact on the CoReaAgents framework, followed by the removal of the Tool Agent. The main reason for this is that timely adjustments to task planning are more critical in quite complex scenarios. The improvement in effectiveness provided by the Reflect Agent confirms the importance of reflecting on subtasks and overall planning during the process. The impact of removing the Tool Agent confirms that our strategy aids in selecting more appropriate tools and using them effectively. 

Whereas removing the Reflect Agent and Tool Agent degrades the performance of the CoReaAgents framework, this strongly supports the idea that collaboration among multiple agents leads to better results than relying solely on a single agent to complete tool learning tasks. The ablation results on the API-Bank dataset suggest that when the number and variety of tools are minor, removing either the Reflect Agent or the Tool Agent has a similar impact on the CoReaAgents framework’s performance.

 15 of 26 

4.2. Math Reasoning 4.2.1. Settings for Math Reasoning 

Datasets 

 FuncQA [67] involves 13 arithmetic operation tools (e.g., power, sqrt, lcm), which are used to test the reasoning ability of LLMs in complex mathematical problems. We evaluate our approach using multi-hop problems from this dataset. Multi-hop problems consist of 68 math problems that can be solved with multiple tools. 

 SVAMP [37] is a dataset of mathematical application problems designed specifically to test the ability of natural language processing models to solve basic mathematical problems. The dataset contains four arithmetic operations: addition, subtraction, multiplication and division. Each problem contains up to two mathematical expres-sions and one unknown variable. The sample size of the test set for this dataset is 1000 test data. 

Baselines 

 CoT [12] improves the performance of LLMs on complex inference tasks by generating intermediate inference steps. 

 Self-Consistency [40] samples multiple inference paths and selects the output with the highest consistency as the final answer based on a voting strategy. 

 Self-Contrast [41] improves the reflectivity and corrective accuracy of LLMs by creating a diversity of perspectives and comparing the differences in the different perspectives. 

 ReAct, Reflexion, EASYTOOL are the same as the baselines in Section 4.1.1. 

Evaluation metrics For the math reasoning task, we use accuracy to evaluate the answers derived from 

LLMs’ step-by-step reasoning, with a 0.1% error tolerance. 

4.2.2. Main Results from Math Reasoning 

The CoReaAgents framework demonstrates powerful performance in math reasoning tasks. The results in Table 3 show that our framework significantly improves the ability of LLMs to solve complex math reasoning problems. The CoReaAgents framework shows the best behavior both in a Multi-hop subset of FuncQA and in SVAMP. For the Multi-hop subset of FuncQA with multiple math formulas, due to the limited size of the test set and the higher number of correct answers provided by our method, the CoReaAgents framework demonstrates a performance improvement of 8.82% over EASYTOOL. For SVAMP, due to the limited number of formulas involved in the task and the high accuracy that many studies have achieved, it is challenging to obtain significant improvements. As a result, our method achieves a slight improvement compared to other baselines. This could also indicate that the CoReaAgents framework can fully comprehend the reasoning steps behind mathematical problems and apply mathematical formulas. Furthermore, the experimental results from SVAMP to Funcqa illustrate the ability of the CoReaAgents framework to adapt to different types of mathematical problems, from simple arithmetic operations to complex multi-step mathematical reasoning. This adaptability demonstrates the framework’s scalability. 

The rightmost column in Table 3 shows the average number of tokens consumed by the CoReaAgents framework versus the other baselines to complete the math reasoning task. The results show that the cost is not significant compared to the improved performance of the CoReaAgents framework in the mathematical reasoning task. If the focus is more on pushing the limits of performance, the CoReaAgents framework could be more effective.

 16 of 26 

Table 3. The results of different baselines and the ablation study on math reasoning. The table highlights the highest scores in bold, with underscores indicating the highest scores achieved by prior methods. - indicates that the method is not publicly available. The rightmost column in the table shows the number of tokens completing this task for each baseline. 

Accuracy Methods FuncQA (Multi-Hop) SVAMP Tokens 

CoT 17.64 79.8 433 ReAct 41.17 80.3 2260 

Reflexion 42.65 80.5 2312 Self-Consistency 45.59 84.6 5750 

EASYTOOL 48.53 84.9 1411 Self-Contrast - 89.0 -CoReaAgents 57.35 90.3 3900 

w/o TA 50.00 87.1 w/o RA 47.05 85.5 

w/o TA&RA 44.12 82.4 

4.2.3. Ablation Study of Math Reasoning 

We analyze the effects of different agents in the CoReaAgents framework on the math reasoning task separately. The results of the ablation study are presented in Table 3. Removing the Reflect Agent has the greatest impact on the CoReaAgents framework, while removing the Tool Agent also affects task performance. The reason for this is that complex math problems require objective analysis at each step. The Reflect Agent facilitates subtask reflection and plan reflection, allowing LLMs to analyze the problem from multiple perspectives and make timely adjustments. Due to the limited computational power of LLMs and the high demands of math reasoning tasks in terms of computational capabilities, utilizing external tools for assistance becomes especially crucial. The performance without the Tool Agent on both datasets confirms the effectiveness of tool augmentation and subtask execution performed by the Tool Agent. Eventually, the experimental results indicate that the CoReaAgents framework significantly outperforms a single LLM-powered agent in solving math problems. 

4.3. Multi-Hop QA 4.3.1. Settings for Multi-Hop QA 

Datasets 

 HotpotQA [43] is a dataset of challenging multi-hop QA tasks. It extracts relevant facts and performs multi-hop reasoning based on article passages from Wikipedia. The answers to the questions in HotpotQA cover a wide range of domains, reflecting its diversity and complexity for QA tasks. We randomly selected 500 questions to construct the test set for evaluation. 

Baselines 

 AMOR [48] decomposes the problem solving process into a series of modular steps, each corresponding to a state in a Finite State Machine. 

 UALA [68] quantifies the degree of certainty of a language model in answering a question through various existing measures of uncertainty. 

 Self-ask [69] allows the model to explicitly ask and answer a series of subquestions before answering the final question. In this way, the model is able to decompose complex questions more systematically and construct the final answer step by step. 

 HGOT [49] leverages the planning capabilities of LLMs. It uses a divide strategy to de-compose complex queries into subqueries and build dependency graphs at a deeper level. 

 CoT, ReAct, Self-Consistency are the same as the baselines in Sections 4.1.1 and 4.2.1.

 17 of 26 

Evaluation metrics For HotpotQA, we evaluated it with Exact Match (EM) and F1 scores. EM identifies the 

proportion of predictions that are in precise agreement with the correct answer, while the F1 score evaluates the average token overlap between the prediction and the correct answer. 

4.3.2. Main Results from Multi-Hop QA 

The CoReaAgents framework shows a slight improvement compared to other base-lines. Multi-hop QA tasks place greater emphasis on the LLM’s reasoning capabilities. As shown in Table 4, the CoReaAgents framework slightly outperforms other reasoning-enhanced baselines on the HotpotQA dataset. Compared to the best-performing HGOT, the CoReaAgents framework improves the EM scores by 1.46% and the F1 scores by 2.29%. This demonstrates that our method realizes autonomous planning and readjustment with the collaboration of multiple agents. 

Table 4. The results of different baselines and the ablation study on HotpotQA in terms of EM (%) and F1 (%). The table highlights the highest scores in bold, with underscores indicating the highest scores achieved by prior methods. - indicates that the method is not publicly available. 

HotpotQA Methods EM F1 

CoT 34.80 42.32 ReAct 35.47 42.18 

Self-Consistency 39.40 -AMOR 39.60 49.30 UALA 41.30 -Self-ask 43.98 54.67 HGOT 47.37 59.48 

CoReaAgents 48.83 61.77 

w/o TA 46.64 58.28 w/o RA 44.87 56.34 

w/o TA&RA 41.93 54.83 

4.3.3. Ablation Study of Multi-Hop QA 

In the ablation study results presented in Table 4 for HotpotQA, the impact of removing the Reflect Agent is greater than that of removing the Tool Agent. The reason for this is that the multi-hop QA task is focused on understanding textual content and has less reliance on utilizing external resources. Nevertheless, the Tool Agent can still improve the performance of the CoReaAgents framework on HotpotQA. The main explanation for this is that the Tool Agent summarizes the results for each subtask after completing it, which helps the CoReaAgents framework to integrate critical information. The Reflect Agent emphasizes the significance of reflection by iteratively updating the task plan, which enables the CoReaAgents framework to distill information from multiple sources and obtain a final answer. 

4.4. Further Analysis 4.4.1. Specific Analysis of Ablation Study on ToolBench 

In this paper, we examine the experimental results from 500 test cases across I2-Ins, I2-Cat and I3-Ins in ToolBench. We summarize and categorize the types of problems in ToolBench that directly lead to task failure and provide further specific analysis. Figure 6 shows the number of various problem types present in ToolBench and their distribution across experimental conditions. The CoReaAgents framework without the Tool Agent makes more errors in tool selection and usage. The experimental results show that the

 18 of 26 

CoReaAgents framework using the Tool Agent for tool augmentation and subtask execution can more effectively select the appropriate tool. 

The CoReaAgents framework without the Reflect Agent makes more mistakes in both tool application and task planning. This indicates that the Reflect Agent enables the timely correction of mistakes in selecting or using tools, significantly reducing the occurrence of API hallucinations. In addition, the reflection on the overall planning by the Reflect Agent can guide the task direction to the correct reasoning path in time, which effectively reduces task planning errors. 

Figure 6. The number of various problem types in ToolBench and their distribution under different experimental conditions. There are five main causes of direct task failure: parameter error, API hallucination, missing parameters, incorrect tool and plan error. 

4.4.2. Analysis of Tool Augmentation by the Tool Agent 

The accuracy of tool selection is a key factor in evaluating the ability of LLM-powered agents to solve complex tasks. The CoReaAgents framework primarily enhances tool selection accuracy through tool augmentation. Figure 7 illustrates the impact of tool augmentation on tool selection in both tool learning and math reasoning tasks. The results may not be representative since the CoReaAgents framework employs a few tools for the multi-hop QA task. The results in Figure 7 indicate that tool selection errors lead to task failures more frequently in math reasoning tasks than in tool learning tasks. We found that the reasons for mistakes in math reasoning tasks are centered on formula selection, and there are almost no instances of tool failure or missing parameters. 

The experimental results demonstrate that tool augmentation, which provides targeted explanations of tool descriptions, significantly decreases incorrect tool selections and facilitates successful task completion. 

4.4.3. Reflection Frequency Statistics for the Reflect Agent 

After each step during subtask execution, the Reflect Agent evaluates the feasibility of the task plan. Figure 8 shows the Pass Rate for each subset of ToolBench for different maximum numbers of reflections after each step of the subtask. With the increase in reflection iterations, the Pass Rate for I2 and I3 in ToolBench shows varying degrees of improvement. The bias in test data between I2-Cat and I2-Ins means that issues in I2-Cat can be more easily corrected through reflection. As a result, the Pass Rate of I2-Cat increases more rapidly before reaching six reflection iterations. The complexity of I3-Ins causes its Pass Rate to increase slowly as the number of reflection iterations grows. In summary, we consider that in complex scenarios requiring numerous tool invocations, setting the

 19 of 26 

maximum number of reflection iterations to 12 strikes a balance between performance and efficiency. 

Figure 7. The effect of tool augmentation on tool selection in tool learning and math reasoning tasks. 

Figure 8. The Pass Rate for each subset of ToolBench for different maximum numbers of reflections after each step of the subtask. 

4.4.4. Case Study 

In order to improve the interpretability of each agent’s decisions, we visualize the collaboration process and decision-making results of the agents through a specific case study. Figure 9 illustrates the success of the CoReaAgents framework in the tool learning task. For the instruction “Update Jerry’s personal information and address. Password is zxcvbn. Address is 345 Main St.”, the Plan Agent performs tool filtering and hands over the results to the Tool Agent for tool augmentation. Then, the Plan Agent performs task planning and the Tool Agent executes subtasks sequentially. The Reflect Agent reflects on the results of the subtask execution and the next steps in this process. The figure shows the results of the Reflect Agent’s feedback during the execution of the subtasks and the task plan without errors. 

We conducted a case study to further investigate the performance of the CoReaAgents framework. Figure 10 shows a case study of the CoReaAgents framework involving tool learning, and we compare our method with only a single agent. The results indicate that in complex scenarios requiring external resources, relying solely on a single agent to complete

 20 of 26 

the task leads to planning errors and tool usage mistakes. In contrast, the CoReaAgents framework can perform more accurate task planning and tool usage. As shown in Figure 10, the tool augmentation in the CoReaAgents framework provides targeted enhancements to tool descriptions, increasing tool selection accuracy. The specific collaborative mechanism of the CoReaAgents framework enables real-time adjustments to task planning during execution, significantly improving the success rate of complex tasks. 

Instruction 

### Update Jerry's personal information and address. Password is zxcvbn. Address is 345 Main St.

### CoReaAgents

Plan Agent 

Step#1: Tool Filter 

Toolset 

QueryMeeting 

AddMeeting 

AccountInfo 

EmailReminder 

UpdateAccountInfo 

OrganizationMembers 

Step#2: Tool Augmentation 

AccountInfo UpdateAccountInfo 

API for retrieving and updating 

user account information... 

Parameter Description: 

username, 

Name of the user... 

password, 

Password of the user... 

The API for updating a user's 

personal information and 

address... 

Parameter Description: 

username, 

Name of the user... 

password, 

Password of the user... 

address, 

Updated address information... 

Tool Agent 

# Step1: Get user account information. 

UserInfor= <API>AccountInfo()</API> 

# Step2: Update user information. 

NewInfor= 

<API>UpdateAccountInfo()</API> 

Step#3: Task Planning 

Plan Agent 

Execute 

Step#4: Task Execution 

Subtask Target: Get user 

account information. 

Tool: AccountInfo 

Parameters: 

"username": "Jerry", 

"password": "zxcvbn" 

Step1 

Subtask Target: Get user 

account information. 

Output: 

"email": "jerry@example.com", 

"phone": "7897897890" 

Subtask Target: Update user 

information. 

Tool: UpdateAccountInfo 

Parameters: 

"username": "Jerry", 

"password": "zxcvbn" 

"address": "345 Main St" 

Step2 

Subtask Target: Update user 

information. 

Output: 

"status": "success", 

Execute 

Tool Agent 

Step#6: Plan Reflection 

Step#5: Subtask Reflection 

Tool selected is correct. 

The result does not contain errors 

and is consistent with the target. 

Current task planning needs no 

modification 

Reflect Agent 

Figure 9. Specific case of successful completion of tool learning task by the CoReaAgents frame-work, where the Reflect Agent performed subtask reflection and plan reflection after each subtask was performed. 

Instruction 

### I'm a huge fan of Leonardo DiCaprio and I want to know more about his career. Can you give me the basic information,

### including the birth year and known titles, of Leonardo DiCaprio? Also, provide me with the streaming sources for the

### movie 'The Wolf of Wall Street' and the latest arrivals on different platforms in the US.

### CoReaAgents

# Step1: Get People_Id. 

People_Id= <API>Get_Id_Byname()</API> 

# Step2: Get birth year. 

Birth_Year= <API>Info_Details()</API> 

# Step3: Get the streaming sources. 

Sources= <API>Streaming_Availability()</API> 

# Step4: Get the latest arrivals. 

Arrivals = <API>Arrivals_Details()</API> 

# Last step: Summarize the above results 

# Step1: Get People_Id. 

People_Id= <API>Get_Id_Byname()</API> 

# Step2: Get birth year. 

Birth_Year= <API>Info_Details()</API> 

# Step3: Get the streaming sources. 

Sources= <API>Title_Sources()</API> 

# Step4: Get the latest arrivals. 

Arrivals = <API>Arrivals_Details()</API> 

# Last step: Summarize the above results 

<Re-Plan> 

# Step2: Get basic information. 

<API>Info_Details()</API> 

Reflect Agent 

Plan Agent 

Streaming_Availability, 

Augmented Description 

Title_Sources, 

Augmented Description 

... 

Info_Details, 

Augmented Description 

Tool Agent 

### Single Agent

Figure 10. Case study of the CoReaAgents framework carrying out tool learning, where red words indicate the error portion and green words indicate the correction portion. 

4.4.5. Limitations 

Although the CoReaAgents framework performs well in several complex reasoning tasks, it is not without limitations. As shown in Figure 11, first, the performance of the

 21 of 26 

framework relies heavily on the quality and reliability of the tools provided. If the tools themselves are vulnerable or flawed, this may negatively impact the stability and accuracy of the overall system. Second, the CoReaAgents framework may make errors in selecting tools when there are multiple tools of similar usefulness. In addition, when an instruction fails to state explicit requirements for the CoReaAgents framework, i.e., when the CoReaAgents framework is asked to select parameters on its own, it may make errors during parameter passing, especially when confronted with novel or unseen task types. Nevertheless, we plan to further explore ways to improve the robustness of the system in future research. 

Instruction 

### I'm organizing a company retreat in a remote location and I need to find a suitable venue. Can you help me

### locate an area with breathtaking natural landscapes and good accessibility? Additionally, provide me with

### the Terrain RGB and Hillshading tiles for the selected location to assess the topography.

### CoReaAgents

Plan Agent 

Step#1: Tool Filter 

Toolset 

Nearest 

Terrain RGB 

Reverse 

Hillshading 

LimitByViewbox 

LookupCoordinates 

Step#2: Tool Augmentation 

Reverse geocoding is the 

process of converting a 

coordinate or location... 

Parameter Description: 

lat, 

Latitude of the location to... 

lon, 

Longitude of the location to... 

Available are worldwide 

terrain RGB tiles... 

Parameter Description: 

x, 

Horizontal coordinates in... 

y, 

Vertical coordinate in... 

z, 

Zoom level in... 

Tool Agent 

# Step1: Get an area. 

Area= <API>Reverse()</API> 

# Step2: Get the Terrain RGB. 

RGB= <API>Terrain RGB()</API> 

Step#3: Task Planning 

Plan Agent 

Execute 

Step#4: Task Execution 

Subtask Target: Get an area. 

Tool: Reverse 

Parameters: 

"lat": "default", 

"lon": "default" 

Step1 

Subtask Target: Get an area. 

Output: 

request invalid, data error. 

status_code=500 

Tool Agent 

Reverse Terrain RGB 

# Step3: Get hillshading tiles. 

Tiles= <API>Hillshading()</API> 

<Re-Select> 

# Step 1: Get an area. 

<API>Nearest()</API> 

Parameters: 

"lat": "default", 

"lon": "default" 

Reflect Agent 

Figure 11. Specific error cases for the CoReaAgents framework, where the red portion indicates the error portion. The example in the figure shows an error in calling the tool to pass a parameter. 

5. Conclusions In this paper, we introduce CoReaAgents, a collaboration and reasoning framework 

based on LLM-powered agents. This framework simulates social division and cooperation to enhance LLMs’ reasoning and complex task execution capabilities, using a meticulously assembled team of diverse agents, including the Plan Agent, the Tool Agent and the Reflect Agent. The Plan Agent functions as a precise task planner, responsible for task planning and decision making. The Tool Agent functions as a proficient tool user, performing tool augmentation for each tool in the relevant toolset and executing each subtask as a single-step reasoning task. The Reflect Agent functions as an objective task evaluator,

 22 of 26 

performing subtask reflection and plan reflection during the task. Our framework includes multi-agent communication and negotiation mechanisms that facilitate effective exchange and feedback among different agents, addressing the limitations encountered in planning complex tasks that require iterative updates. We conducted experiments on a total of five datasets involving complex reasoning tasks, such as tool learning, math reasoning and multi-hop QA, and supplemented them with qualitative and quantitative analyses. The experiment results demonstrate the adaptability and effectiveness of the CoReaAgents framework in various types of complex tasks. 

Additionally, we documented and analyzed the decisions of each agent during task planning, tool selection and result reflection through specific cases. We have provided users with a clear understanding that will help them trust and use our system. To ensure the safety of the system, we also introduced human supervision and intervention mechanisms that allow humans to intervene at critical decision points or when the system becomes abnormal. We developed a program that allows supervisors to monitor the operational status of the system in real time and manually adjust task planning or tool selection if necessary. 

6. Future Work While the CoReaAgents framework has achieved comparative results on several 

complex tasks, there is still room for improvement in this work. In this paper, we performed experimental comparisons across multiple tasks. However, comparisons with other multi-agent frameworks remain to be conducted. Looking forward, we intend to carry out a more comprehensive comparative analysis. This will not only help to more fully illustrate the potential and advantages of the CoReaAgents framework but also further research into multi-agent systems. Affected by the diversity of complex tasks and datasets, each agent of the CoReaAgents framework needs different prompting samples. We will further investigate the prompt generation method used in our framework, thus enhancing its flexibility and applicability to a wider range of complex tasks. Meanwhile, applying additional memory mechanisms could further improve our framework’s performance on complex reasoning tasks. 

Author Contributions: Conceptualization, Z.H. and Z.J.; methodology, Z.H. and J.W.; software, Y.Z.; validation, C.S. and Q.G.; formal analysis, Y.Z.; investigation, S.L.; resources, S.L. and Y.Z.; data curation, S.L.; writing—original draft preparation, J.W.; writing—review and editing, Z.H. and J.W.; visualization, Q.G.; supervision, X.Y.; project administration, X.Y.; funding acquisition, Z.H. All authors have read and agreed to the published version of the manuscript. 

Funding: This research received no external funding. 

Institutional Review Board Statement: Not applicable. 

Informed Consent Statement: Not applicable. 

Data Availability Statement: The original data presented by the API-Bank dataset in the study are openly available at https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank (accessed on 30 January 2025). The original data presented by the ToolBench dataset in the study are openly available at https://github.com/OpenBMB/ToolBench (accessed on 30 January 2025). The original data presented by the FuncQA dataset in the study are openly available at https://drive.google.com/file/d/13Sj7uIsyqWXoTh1ejWUviTzeQSES2Omd/view (accessed on 30 January 2025). The original data presented by the SVAMP dataset in the study are openly available at https://github.com/arkilpatel/SVAMP (accessed on 30 January 2025). The original data presented by the HotpotQA dataset in the study are openly available at https://github.com/hotpotqa/hotpot (accessed on 30 January 2025). 

Conflicts of Interest: The authors declare no conflicts of interest.

 23 of 26 

References 1. Mitchell, M. Debates on the Nature of Artificial General Intelligence. Science 2024, 383, eado7069. [CrossRef] [PubMed] 2. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.; 

Ostrovski, G.; et al. Human-Level Control through Deep Reinforcement Learning. Nature 2015, 518, 529–533. [CrossRef] 3. Durante, Z.; Huang, Q.; Wake, N.; Gong, R.; Park, J.S.; Sarkar, B.; Taori, R.; Noda, Y.; Terzopoulos, D.; Choi, Y.; et al. Agent AI: 

Surveying the Horizons of Multimodal Interaction. arXiv 2024, arXiv:2401.03568. 4. Heaven, W.D. Google DeepMind Wants to Define What Counts as Artificial General Intelligence. MIT Technology Review, 

16 November 2023. Available online: https://www.technologyreview.com/2023/11/16/1083498 (accessed on 1 June 2024). 5. Xu, J.; Fei, H.; Pan, L.; Liu, Q.; Lee, M.-L.; Hsu, W. Faithful Logical Reasoning via Symbolic Chain-of-Thought. In Proceedings of 

the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Bangkok, Thailand, 11–16 August 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 13326–13365. 

6. Silver, D.; Huang, A.; Maddison, C.J.; Guez, A.; Sifre, L.; Driessche, G.V.D.; Schrittwieser, J.; Antonoglou, I.; Panneershelvam, V.; Lanctot, M.; et al. Mastering the Game of Go with Deep Neural Networks and Tree Search. Nature 2016, 529, 484–489. [CrossRef] 

7. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Graves, A.; Antonoglou, I.; Wierstra, D.; Riedmiller, M. Playing Atari with Deep Reinforcement Learning. arXiv 2013, arXiv:1312.5602. 

8. Liu, R.; Yang, R.; Jia, C.; Zhang, G.; Zhou, D.; Dai, A.M.; Yang, D.; Vosoughi, S. Training Socially Aligned Language Models in Simulated Human Society. arXiv 2023, arXiv:2305.16960. 

9. Sumers, T.R.; Yao, S.; Narasimhan, K.; Griffiths, T.L. Cognitive Architectures for Language Agents. arXiv 2023, arXiv:2309.02427. 10. Hong, S.; Zhuge, M.; Chen, J.; Zheng, X.; Cheng, Y.; Wang, J.; Zhang, C.; Wang, Z.; Yau, S.K.S.; Lin, Z.; et al. MetaGPT: Meta 

Programming for A Multi-Agent Collaborative Framework. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. 

11. Xie, J.; Chen, Z.; Zhang, R.; Wan, X.; Li, G. Large Multimodal Agents: A Survey. arXiv 2024, arXiv:2402.15116. 12. Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Ichter, B.; Xia, F.; Chi, E.; Le, Q.; Zhou, D. Chain-of-Thought Prompting Elicits 

Reasoning in Large Language Models. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2022; Volume 35, pp. 24824–24837. 

13. Yao, S.; Yu, D.; Zhao, J.; Shafran, I.; Griffiths, T.; Cao, Y.; Narasimhan, K. Tree of Thoughts: Deliberate Problem Solving with Large Language Models. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

14. Zhang, Y.; Sun, R.; Chen, Y.; Pfister, T.; Zhang, R.; Arik, S. Chain of Agents: Large Language Models Collaborating on Long-Context Tasks. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2024; Volume 37, pp. 132208–132237. 

15. Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. ReAct: Synergizing Reasoning and Acting in Language Models. In Proceedings of the International Conference on Learning Representations (ICLR), Kigali, Rwanda, 1–5 May 2023. 

16. Shen, W.; Li, C.; Chen, H.; Yan, M.; Quan, X.; Chen, H.; Zhang, J.; Huang, F. Small LLMs Are Weak Tool Learners: A Multi-LLM Agent. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024), Miami, FL, USA, 12–16 November 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 16658–16680. 

17. Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K.; Yao, S. Reflexion: Language Agents with Verbal Reinforcement Learning. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

18. Wang, Z.; Mao, S.; Wu, W.; Ge, T.; Wei, F.; Ji, H. Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Mexico City, Mexico, 16–21 June 2024; pp. 257–279. 

19. Li, G.; Hammoud, H.; Itani, H.; Khizbullin, D.; Ghanem, B. Camel: Communicative Agents for “Mind” Exploration of Large Language Model Society. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36, pp. 51991–52008. 

20. Qiao, S.; Zhang, N.; Fang, R.; Luo, Y.; Zhou, W.; Jiang, Y.E.; Lv, C.; Chen, H. AutoAct: Automatic Agent Learning from Scratch for QA via Self-Planning. In Proceedings of the ICLR 2024 Workshop on Large Language Model (LLM) Agents, Vienna, Austria, 7–11 May 2024. 

21. Bo, X.; Zhang, Z.; Dai, Q.; Feng, X.; Wang, L.; Li, R.; Chen, X.; Wen, J.-R. Reflective Multi-Agent Collaboration Based on Large Language Models. In Proceedings of the Thirty-Eighth Annual Conference on Neural Information Processing Systems, Vancouver, BC, Canada, 9–15 December 2024. 

22. Yang, R.; Song, L.; Li, Y.; Zhao, S.; Ge, Y.; Li, X.; Shan, Y. Gpt4tools: Teaching Large Language Model to Use Tools via Self-Instruction. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

23. Patil, S.G.; Zhang, T.; Wang, X.; Gonzalez, J.E. Gorilla: Large Language Model Connected with Massive APIs. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2024; Volume 37, pp. 126544–126565. 

24. Gou, Z.; Shao, Z.; Gong, Y.; Shen, Y.; Yang, Y.; Huang, M.; Duan, N.; Chen, W. Tora: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving. arXiv 2023, arXiv:2309.17452.

 24 of 26 

25. Song, Y.; Xiong, W.; Zhu, D.; Wu, W.; Qian, H.; Song, M.; Huang, H.; Li, C.; Wang, K.; Yao, R.; et al. RestGPT: Connecting Large Language Models with Real-World RESTful APIs. arXiv 2023, arXiv:2306.06624. 

26. Schick, T.; Dwivedi-Yu, J.; Dessí, R.; Raileanu, R.; Lomeli, M.; Hambro, E.; Zettlemoyer, L.; Cancedda, N.; Scialom, T. Toolformer: Language Models Can Teach Themselves to Use Tools. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

27. Lu, P.; Peng, B.; Cheng, H.; Galley, M.; Chang, K.; Wu, Y.N.; Zhu, S.; Gao, J. Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

28. Liu, X.; Peng, Z.; Yi, X.; Xie, X.; Xiang, L.; Liu, Y.; Xu, D. ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph. arXiv 2024, arXiv:2403.00839. 

29. Li, W.; Wu, W.-J.; Wang, H.-M.; Cheng, X.-Q.; Chen, H.-J.; Zhou, Z.-H.; Ding, R. Crowd Intelligence in AI 2.0 Era. Front. Inf. Technol. Electron. Eng. 2017, 18, 15–43. [CrossRef] 

30. Wang, S.; Liu, Z.; Zhong, W.; Zhou, M.; Wei, Z.; Chen, Z.; Duan, N. From LSAT: The Progress and Challenges of Complex Reasoning. IEEE/ACM Trans. Audio Speech Lang. Process. 2022, 30, 2201–2216. [CrossRef] 

31. Liu, J.; Cui, L.; Liu, H.; Huang, D.; Wang, Y.; Zhang, Y. LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning. In Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence (IJCAI-20), California, CA, USA, 7–15 January 2021; pp. 3622–3628. 

32. Talmor, A.; Herzig, J.; Lourie, N.; Berant, J. CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), Minneapolis, MN, USA, 2–7 June 2019; Association for Computational Linguistics: Kerrville, TX, USA, 2019; pp. 4149–4158. 

33. Ornes, S. The Unpredictable Abilities Emerging from Large AI Models. Quanta Magazine, 16 March 2023. 34. Li, M.; Zhao, Y.; Yu, B.; Song, F.; Li, H.; Yu, H.; Li, Z.; Huang, F.; Li, Y. API-Bank: A Comprehensive Benchmark for Tool-

Augmented LLMs. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; Association for Computational Linguistics: Kerrville, TX, USA, 2023; pp. 3102–3116. 

35. Qu, C.; Dai, S.; Wei, X.; Cai, H.; Wang, S.; Yin, D.; Xu, J.; Wen, J.-R. Tool learning with large language models: A survey. Front. Comput. Sci. 2025, 19, 198343. [CrossRef] 

36. Qin, Y.; Liang, S.; Ye, Y.; Zhu, K.; Yan, L.; Lu, Y.; Lin, Y.; Cong, X.; Tang, X.; Qian, B.; et al. ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. In Proceedings of the ICLR 2024, Vienna, Austria, 7–11 May 2024. 

37. Patel, A.; Bhattamishra, S.; Goyal, N. Are NLP Models Really Able to Solve Simple Math Word Problems? In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Mexico City, Mexico, 6–11 June 2021; pp. 2080–2094. 

38. Cobbe, K.; Kosaraju, V.; Bavarian, M.; Chen, M.; Jun, H.; Kaiser, L.; Plappert, M.; Tworek, J.; Hilton, J.; Nakano, R.; et al. Training Verifiers to Solve Math Word Problems. arXiv 2021, arXiv:2110.14168. 

39. Ling, W.; Yogatama, D.; Dyer, C.; Blunsom, P. Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Vancouver, BC, Canada, 30 July–4 August 2017; Association for Computational Linguistics: Kerrville, TX, USA, 2017; pp. 158–167. 

40. Wang, X.; Wei, J.; Schuurmans, D.; Le, Q.; Chi, E.; Narang, S.; Chowdhery, A.; Zhou, D. Self-Consistency Improves Chain of Thought Reasoning in Language Models. arXiv 2022, arXiv:2203.11171. 

41. Zhang, W.; Shen, Y.; Wu, L.; Peng, Q.; Wang, J.; Zhuang, Y.; Lu, W. Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Bangkok, Thailand, 11–16 August 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 3602–3622. 

42. Yuan, S.; Song, K.; Chen, J.; Tan, X.; Shen, Y.; Ren, K.; Li, D.; Yang, D. EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Albuquerque, NM, USA, 29 April–4 May 2025; Association for Computational Linguistics: Kerrville, TX, USA, 2025; pp. 951–972. 

43. Yang, Z.; Qi, P.; Zhang, S.; Bengio, Y.; Cohen, W.; Salakhutdinov, R.; Manning, C.D. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, Brussels, Belgium, 31 October–4 November 2018; pp. 2369–2380. 

44. Peng, C.; Xia, F.; Naseriparsa, M.; Osborne, F. Knowledge Graphs: Opportunities and Challenges. Artif. Intell. Rev. 2023, 56, 13071–13102. [CrossRef]

 25 of 26 

45. Ding, M.; Zhou, C.; Chen, Q.; Yang, H.; Tang, J. Cognitive Graph for Multi-Hop Reading Comprehension at Scale. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, Florence, Italy, 28 July–2 August 2019; Association for Computational Linguistics: Kerrville, TX, USA, 2019; pp. 2694–2703. 

46. Saxena, A.; Tripathi, A.; Talukdar, P. Improving Multi-Hop Question Answering over Knowledge Graphs Using Knowledge Base Embeddings. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, Online, 5–10 July 2020; pp. 4498–4507. 

47. Wu, S.; Yacub, Z.; Shasha, D. DietNerd: A Nutrition Question-Answering System That Summarizes and Evaluates Peer-Reviewed Scientific Articles. Appl. Sci. 2024, 14, 9021. [CrossRef] 

48. Guan, J.; Wu, W.; Wen, Z.; Xu, P.; Wang, H.; Huang, M. AMOR: A Recipe for Building Adaptable Modular Knowledge Agents Through Process Feedback. arXiv 2024, arXiv:2402.01469. 

49. Fang, Y.; Thomas, S.; Zhu, X. HGOT: Hierarchical Graph of Thoughts for Retrieval-Augmented In-Context Learning in Factuality Evaluation. In Proceedings of the 4th Workshop on Trustworthy Natural Language Processing (TrustNLP 2024), Mexico City, Mexico, 21–22 June 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 118–144. 

50. Chen, R.; Jiang, W.; Qin, C.; Rawal, I.S.; Tan, C.; Choi, D.; Xiong, B.; Ai, B. LLM-Based Multi-Hop Question Answering with Knowledge Graph Integration in Evolving Environments. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024), Miami, FL, USA, 12–16 November 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 14438–14451. 

51. Zhao, W.X.; Zhou, K.; Li, J.; Tang, T.; Wang, X.; Hou, Y.; Min, Y.; Zhang, B.; Zhang, J.; Dong, Z.; et al. A Survey of Large Language Models. arXiv 2023, arXiv:2303.18223. 

52. Wei, J.; Tay, Y.; Bommasani, R.; Raffel, C.; Zoph, B.; Borgeaud, S.; Yogatama, D.; Bosma, M.; Zhou, D.; Metzler, D.; et al. Emergent Abilities of Large Language Models. arXiv 2022, arXiv:2206.07682. 

53. Park, J.S.; O’Brien, J.; Cai, C.J.; Morris, M.R.; Liang, P.; Bernstein, M.S. Generative Agents: Interactive Simulacra of Human Behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, San Francisco, CA, USA, 29 October–1 November 2023; pp. 1–22. 

54. Besta, M.; Blach, N.; Kubicek, A.; Gerstenberger, R.; Podstawski, M.; Gianinazzi, L.; Gajda, J.; Lehmann, T.; Niewiadomski, H.; Nyczyk, P.; et al. Graph of Thoughts: Solving Elaborate Problems with Large Language Models. Proc. AAAI Conf. Artif. Intell. 2024, 38, 17682–17690. [CrossRef] 

55. Ling, C.; Zhao, X.; Lu, J.; Deng, C.; Zheng, C.; Wang, J.; Chowdhury, T.; Li, Y.; Cui, H.; Zhang, X.; et al. Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey. arXiv 2023, arXiv:2305.18703. 

56. Tang, Q.; Deng, Z.; Lin, H.; Han, X.; Liang, Q.; Cao, B.; Sun, L. ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases. arXiv 2023, arXiv:2306.05301. 

57. Talebirad, Y.; Nadiri, A. Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents. arXiv 2023, arXiv:2306.03314. 58. Fu, Y.; Peng, H.; Khot, T.; Lapata, M. Improving Language Model Negotiation with Self-Play and In-Context Learning from AI 

Feedback. In Proceedings of the CoRR 2023, Atlanta, GA, USA, 6–9 November 2023. 59. Qin, Y.; Zhou, E.; Liu, Q.; Yin, Z.; Sheng, L.; Zhang, R.; Qiao, Y.; Shao, J. MP5: A Multi-Modal Open-Ended Embodied System in 

Minecraft via Active Perception. In Proceedings of the 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle, WA, USA, 16–22 June 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 16307–16316. 

60. Xu, Y.; Wang, S.; Li, P.; Luo, F.; Wang, X.; Liu, W.; Liu, Y. Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf. arXiv 2023, arXiv:2309.04658. 

61. Chan, C.-M.; Chen, W.; Su, Y.; Yu, J.; Xue, W.; Zhang, S.; Fu, J.; Liu, Z. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. 

62. Li, H.; Mahjoub, H.N.; Chalaki, B.; Tadiparthi, V.; Lee, K.; Moradi-Pari, E.; Lewis, M.; Sycara, K. Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2024; Volume 37, pp. 87908–87933. 

63. Wang, Z.; Wang, Y.; Liu, X.; Ding, L.; Zhang, M.; Liu, J.; Zhang, M. AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration. arXiv 2025, arXiv:2503.18891. 

64. Sainz, O.; García-Ferrero, I.; Agerri, R.; de Lacalle, O.L.; Rigau, G.; Agirre, E. GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction. In Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024), Vienna, Austria, 7–11 May 2024. 

65. Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.; et al. Training Language Models to Follow Instructions with Human Feedback. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2022; Volume 35, pp. 27730–27744. 

66. Liu, Y.; Peng, X.; Zhang, Y.; Cao, J.; Zhang, X.; Cheng, S.; Wang, X.; Yin, J.; Du, T. Tool-Planner: Dynamic Solution Tree Planning for Large Language Model with Tool Clustering. arXiv 2024, arXiv:2406.03807.

 26 of 26 

67. Hao, S.; Liu, T.; Wang, Z.; Hu, Z. ToolKengpt: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2023; Volume 36. 

68. Han, J.; Buntine, W.; Shareghi, E. Towards Uncertainty-Aware Language Agent. In Proceedings of the Findings of the Association for Computational Linguistics: ACL 2024, Bangkok, Thailand, 11–16 August 2024; Association for Computational Linguistics: Kerrville, TX, USA, 2024; pp. 6662–6685. 

69. Press, O.; Zhang, M.; Min, S.; Schmidt, L.; Smith, N.; Lewis, M. Measuring and Narrowing the Compositionality Gap in Language Models. In Proceedings of the Findings of the Association for Computational Linguistics: EMNLP 2023, Singapore, 6–10 December 2023; Association for Computational Linguistics: Kerrville, TX, USA, 2023; pp. 5687–5711. 

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.