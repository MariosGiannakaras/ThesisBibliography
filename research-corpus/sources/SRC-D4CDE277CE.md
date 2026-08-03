> Source: https://aws.amazon.com/what-is/ai-agents/

Skip to main content
Contact us
AWS Marketplace
 Sign in to console 
Create account
What is Cloud Computing?›
Cloud Computing Concepts Hub›
Artificial Intelligence
What are AI Agents?
Create an AWS AccountWhat are AI Agents?What are the key principles that define AI agents?What are the benefits of using AI agents?What are the key components of AI agent architecture?How does an AI agent work?What are the types of AI agents?What are the challenges of using AI agents?How can AWS help with your AI agent requirements?What are AI Agents?
An artificial intelligence (AI) agent is a software program that can interact with its environment, collect data, and use that data to perform self-directed tasks that meet predetermined goals. Humans set goals, but an AI agent independently chooses the best actions it needs to perform to achieve those goals. For example, consider a contact center AI agent that wants to resolve customer queries. The agent will automatically ask the customer different questions, look up information in internal documents, and respond with a solution. Based on the customer responses, it determines if it can resolve the query itself or pass it on to a human.
Multiple AI agents can collaborate to automate complex workflows and can also be used in agentic ai systems. They exchange data with each other, allowing the entire system to work together to achieve common goals. Individual AI agents can be specialized to perform specific subtasks with accuracy. An orchestrator agent coordinates the activities of different specialist agents to complete larger, more complex tasks.
Learn more about what is artificial intelligence (AI)
What are the key principles that define AI agents?
All software autonomously performs various routine tasks as specified by the software developer. So, what makes AI agents special?
Autonomy
AI agents act autonomously, without constant human intervention. While traditional software follows hard-coded instructions, AI agents identify the next appropriate action based on past data and execute it without continuous human oversight.
For example, a bookkeeping agent automatically flags and requests missing invoice data for purchases.
Goal-oriented behavior
AI agents are driven by objectives. Their actions aim to maximize success as defined by a utility function or performance metric. Unlike traditional programs that merely complete tasks, intelligent agents pursue goals and evaluate the consequences of their actions in relation to those goals.
For example, an AI logistics system optimizes delivery routes to balance speed, cost, and fuel consumption simultaneously, thereby balancing multiple objectives.
Perception
AI agents interact with their environment by collecting data through sensors or digital inputs. They can collect data from external systems and tools via APIS. This data allows them to perceive the world around them, recognize changes, and update their internal state accordingly.
For example, cybersecurity agents collect data from third-party databases to remain aware of the latest security incidents.
Rationality
AI agents are rational entities with reasoning capabilities. They combine data from their environment with domain knowledge and past context to make informed decisions, achieving optimal performance and results.
For example, a robotic agent collects sensor data, and a chatbot uses customer queries as input. The AI agent applies the data to make an informed decision. It analyzes the collected data to predict the best outcomes that support predetermined goals. The agent also uses the results to formulate the next action that it should take. For example, self-driving cars navigate around obstacles on the road based on data from multiple sensors.
Proactivity
AI agents can take initiative based on forecasts and models of future states. Instead of simply reacting to inputs, they anticipate events and prepare accordingly.
For instance, an AI-based customer service agent might reach out to a user whose behavior suggests frustration, offering help before a support ticket is filed. Autonomous warehouse robots may reposition themselves in anticipation of upcoming high-traffic operations.
Continuous learning
AI agents improve over time by learning from past interactions. They identify patterns, feedback, and outcomes to refine their behavior and decision-making. This differentiates them from static programs that always behave the same way regardless of new inputs.
For instance, predictive maintenance agents learn from past equipment failures to better forecast future issues.
Adaptability
AI agents adjust their strategies in response to new circumstances. This flexibility allows them to handle uncertainty, novel situations, and incomplete information.
For example, a stock trading bot adapts its strategy during a market crash, while a game-playing agent like AlphaZero discovers new tactics through self-play, even without prior human strategies.
Collaboration
AI agents can work with other agents or human agents to achieve shared goals. They are capable of communicating, coordinating, and cooperating to perform tasks together. Their collaborative behavior often involves negotiation, sharing information, allocating tasks, and adapting to others' actions.
For example, multi-agent systems in healthcare can have agents specializing in specific tasks like diagnosis, preventive care, medicine scheduling, etc., for holistic patient care automation.
What are the benefits of using AI agents?
AI agents can improve your business operations and your customers' experiences.
Improved productivity
Business teams are more productive when they delegate repetitive tasks to AI agents. This way, they can divert their attention to mission-critical or creative activities, adding more value to their organization.
Reduced costs
Businesses can utilize intelligent agents to minimize unnecessary costs resulting from process inefficiencies, human errors, and manual processes. They can confidently tackle complex tasks because autonomous agents follow a consistent model that adapts to changing environments. Agent technology automating business processes can lead to significant cost savings.
Informed decision-making
Advanced intelligent agents have predictive capabilities and can collect and process massive amounts of real-time data. This enables business managers to make more informed predictions at speed when strategizing their next move. For example, you can use AI agents to analyze product demands in different market segments when running an ad campaign.
Improved customer experience
Customers seek engaging and personalized experiences when interacting with businesses. Integrating AI agents allows businesses to personalize product recommendations, provide prompt responses, and innovate to improve customer engagement, conversion, and loyalty. AI agents can provide detailed responses to complex customer questions and resolve challenges more efficiently.
What are the key components of AI agent architecture?
An AI agent architecture contains the following key components.
Foundation model
At the core of any AI agent lies a foundation or large language model (LLM) such as GPT or Claude. It enables the agent to interpret natural language inputs, generate human-like responses, and reason over complex instructions. The LLM acts as the agent's reasoning engine, processing prompts and transforming them into actions, decisions, or queries to other components (e.g., memory or tools). It retains some memory across sessions by default and can be coupled with external systems to simulate continuity and context awareness.
Planning module
The planning module enables the agent to break down goals into smaller, manageable steps and sequence them logically. This module employs symbolic reasoning, decision trees, or algorithmic strategies to determine the most effective approach for achieving a desired outcome. It can be implemented as a prompt-driven task decomposition or more formalized approaches, such as Hierarchical Task Networks (HTNs) or classical planning algorithms. Planning allows the agent to operate over longer time horizons, considering dependencies and contingencies between tasks.
Memory module
The memory module allows the agent to retain information across interactions, sessions, or tasks. This includes both short-term memory, such as chat history or recent sensor input, and long-term memory, including customer data, prior actions, or accumulated knowledge. Memory enhances the agent’s personalization, coherence, and context-awareness. When building AI agents, developers use vector databases or knowledge graphs to store and retrieve semantically meaningful content.
Tool integration
AI agents often extend their capabilities by connecting to external software, APIs, or devices. This allows them to act beyond natural language, performing real-world tasks such as retrieving data, sending emails, running code, querying databases, or controlling hardware. The agent identifies when a task requires a tool and then delegates the operation accordingly. Tool use is typically guided by the LLM through planning and parsing modules that format the tool call and interpret its output.
Learning and reflection
Reflection can occur in multiple forms:
The agent evaluates the quality of its own output (e.g., did it solve the problem correctly?).
Human users or automated systems provide corrections.
The agent selects uncertain or informative examples to improve its learning.
Reinforcement Learning (RL) is a key learning paradigm. The agent interacts with an environment, receives feedback in the form of rewards or penalties, and learns a policy that maps states to actions for maximum cumulative reward. RL is especially useful in environments where explicit training data is sparse, such as robotics, gaming, or financial trading. The agent balances exploration (trying new actions) and exploitation (using known best actions) to improve its strategy over time.
How does an AI agent work?
AI agents work by simplifying and automating complex tasks. Most autonomous agents follow a specific workflow when performing assigned tasks.
Determine goals
The AI agent receives a specific instruction or goal from the user. It uses the goal to plan tasks that make the final outcome relevant and useful to the user. Then, the agent breaks down the goal into several smaller, actionable tasks. To achieve the goal, the agent performs those tasks based on specific orders or conditions.
Acquire information
AI agents require information to execute tasks they have planned successfully. For example, the agent must extract conversation logs to analyze customer sentiments. As such, AI agents might access the internet to search for and retrieve the information they need. In some applications, an intelligent agent can interact with other agents or machine learning models to access or exchange information.
Implement tasks
With sufficient data, the AI agent methodically implements the task at hand. Once it accomplishes a task, the agent removes it from the list and proceeds to the next one. Between task completions, the agent evaluates whether it has achieved the designated goal by seeking external feedback and inspecting its own logs. During this process, the agent may create and act on additional tasks to achieve the final outcome. 
What are the types of AI agents?
Organizations create and deploy AI agents across a range of types and tasks. We share some examples below.
Simple reflex agents
A simple reflex agent operates strictly based on predefined rules and its immediate data. It will not respond to situations beyond a given event, condition, and action rule. Hence, these agents are suitable for simple tasks that don’t require extensive training. For example, you can use a simple reflex agent to reset passwords by detecting specific keywords in a user’s conversation.
Model-based reflex agents
A model-based agent is similar to simple reflex agents, except that it has a more advanced decision-making mechanism. Rather than merely following a specific rule, a model-based agent evaluates probable outcomes and consequences before making a decision. Using supporting data, it builds an internal model of the world it perceives and uses that to support its decisions.
Goal-based agents
Goal-based agents, also known as rule-based agents, are AI agents that possess more robust reasoning capabilities. Besides evaluating the environment data, the agent compares different approaches to help it achieve the desired outcome. Goal-based agents always choose the most efficient path. They are suitable for performing complex tasks, such as natural language processing (NLP) and robotics applications.
Utility-based agents
A utility-based agent employs a complex reasoning algorithm to assist users in maximizing the outcome they desire. The agent compares different scenarios and their respective utility values or benefits. Then, it selects one that offers users the most rewards. For example, customers can use a utility-based agent to search for flight tickets with the minimum travel time, regardless of the price.
Learning agents
A learning agent continually learns from past experiences to enhance its performance. Using sensory input and feedback mechanisms, the agent adapts its learning element over time to meet specific standards. Additionally, it utilizes a problem generator to design new tasks that train itself using collected data and past results.
Hierarchical agents
Hierarchical agents are an organized group of intelligent agents arranged in tiers. Higher-level agents decompose complex tasks into smaller ones and assign them to lower-level agents. Each agent runs independently and submits a progress report to its supervising agent. The higher-level agent collects the results and coordinates subordinate agents to ensure they collectively achieve goals.
Multi-agent systems
A multi-agent system (MAS) consists of multiple agents that interact with one another to solve problems or achieve shared objectives. These agents can be homogeneous (similar in design) or heterogeneous (different in structure or function) and may collaborate, coordinate, or even compete depending on the context. MAS are particularly effective in complex, distributed environments where centralized control is impractical.
For example, in autonomous vehicle fleets, each vehicle acts as an independent agent but collaborates with others to avoid traffic congestion and prevent collisions, leading to smoother traffic flow.
What are the challenges of using AI agents?
AI agents are helpful software technologies that automate business workflows to achieve better outcomes. That being said, organizations should address the following concerns when deploying autonomous AI agents for business use cases.
Data privacy concerns
Developing and operating advanced AI agents requires acquiring, storing, and moving massive volumes of data. Organizations should be aware of data privacy requirements and employ necessary measures to improve their data security posture.
Ethical challenges
In certain circumstances, AI models may produce results that are biased or inaccurate. Applying safeguards, such as human reviews, helps to ensure customers receive helpful and fair responses from the agents deployed.
Technical complexities
Implementing advanced AI agents requires specialized experience and knowledge of machine learning technologies. Developers must be able to integrate machine learning libraries with software applications and train the agent with enterprise-specific data.
Limited compute resources
Training and deploying deep learning AI agents require substantial computing resources. When organizations implement these agents on-premise, they must invest in and maintain costly infrastructure that is not easily scalable.
How can AWS help with your AI agent requirements?
Amazon Bedrock is a fully managed service that provides easy access to industry-leading generative AI models, such as Claude, Llama 2, and Amazon Titan, along with a broad set of capabilities needed to build generative AI applications.
Amazon Bedrock Agents use the reasoning of FMs, APIs, and data to break down user requests, gather relevant information, and efficiently complete tasks. Building an agent is straightforward and fast, with setup in just a few steps. Amazon Bedrock supports:
Memory retention for seamless task continuity
Multi-agent collaboration to build multiple specialized agents under the coordination of a supervisor agent
Amazon Bedrock Guardrails for built-in security and reliability.
AWS has introduced an open-source toolkit with a growing catalog of starter agents purpose-built for healthcare and life sciences use cases.
AWS Transform is the first agentic AI service for transforming .NET, mainframe, and VMware workloads. Built on 19 years of migration experience, it deploys specialized AI agents to automate complex tasks like assessments, code analysis, refactoring, decomposition, dependency mapping, validation, and transformation planning. It helps organizations to simultaneously modernize hundreds of applications while maintaining quality and control.
Amazon Q Business is a generative AI-powered assistant designed to help you find information, gain insights, and take action at work. It puts the power of AI agent creation in the hands of every employee. Anyone can use it to create lightweight agentic AI apps that interact with common enterprise software and automate repetitive tasks.
Get started with AI agents on AWS by creating a free account today.
Next Steps on AWS
Check out additional product-related resources
Learn more  Sign up for a free account
Instantly get access to the AWS Free Tier.
Sign up  Start building in the console
Get started building with AWS in the AWS Management Console.
Sign in  
Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.  x  facebook  linkedin  instagram  twitch  youtube  podcasts  email  Privacy
Site terms
Cookie Preferences
© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved.  