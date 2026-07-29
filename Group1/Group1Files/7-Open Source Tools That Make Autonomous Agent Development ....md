> Source: https://www.reddit.com/r/AI_Agents/comments/1ou4vb4/open_source_tools_that_make_autonomous_agent/

Skip to main content  Open navigation  Go to Reddit Home  Log In  Log in to Reddit   Open settings menu  
Log In / Sign Up  
Advertise on Reddit  
Cookie Preferences  
Try Reddit Pro  BETA  
Reddit, Inc. © 2025. All rights reserved. Copy link 
 Copy link 
 Go to AI_Agents r/AI_Agentsr/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members   •  Substantial_Step_351Open Source Tools That Make Autonomous Agent Development Easier 
Discussion  As of recently, these 3 tools consistently help me speed up development and improve reliability of my agents. I'll share why I like them and include pro's and con's. 
 This is just my take, give feedback, share suggestions.
Lang Chain, is great for chaining LLM calls and integrating tools like search, calculators or APIs. Pros: modular, active community and supports memory. Cons: can get complex quickly, debugging chains isn't always intuitive.
AutoGen, designed for multi-agent collaboration and task orchestration. Pros: has built in agent roles, supports human in the loop workflows. Cons: docs are improving but advanced features can still be tricky
CrewAI, has great focus on structured agent teams with defined roles and workflows. Pros: clear abstractions, good for business logic-heavy tasks. Cons: has a smaller community and few integrations.
What open source tools are you using for agent development? What's working or not for you right now?
 Share  Sort by:  Best   Open comment sort options   Best  
Top  
New  
Controversial  
Old  
Q&A  
 ai-agents-qa-bot •  7d ago  Top 1% Commenter  
Here are some open-source tools that can facilitate autonomous agent development, along with their pros and cons:
LangChain
Pros:
Modular design allows for easy integration of various tools like search engines, calculators, and APIs.
Active community support, which can be helpful for troubleshooting and enhancements.
Supports memory, enabling agents to retain context over interactions.
Cons:
Complexity can increase rapidly, especially for larger projects.
Debugging chains may not be straightforward, making it challenging to identify issues.
AutoGen
Pros:
Specifically designed for multi-agent collaboration and task orchestration, making it suitable for complex workflows.
Built-in agent roles facilitate easier management of tasks and responsibilities.
Supports human-in-the-loop workflows, enhancing the interaction between agents and users.
Cons:
Documentation is improving, but some advanced features can still be difficult to navigate.
CrewAI
Pros:
Focuses on structured agent teams with clearly defined roles and workflows, which can streamline development.
Provides clear abstractions, making it easier to manage business logic-heavy tasks.
Cons:
Smaller community compared to other tools, which may limit support and resources.
Fewer integrations available, potentially restricting functionality.
If you're exploring other tools or have experiences to share, feel free to discuss. For more insights on AI agents and their development, you might find the following resources useful:
AI agent orchestration with OpenAI Agents SDK
10 best AI agent frameworks
 Ok_Student8599 •  7d ago  Add Playbooks to your 10 best list please - https://github.com/playbooks-ai/playbooks
More replies   wheres-my-swingline •  7d ago  A for-loop and an LLM api
 AutoModerator •  8d ago  Thank you for your submission, for any questions regarding AI, please check out our wiki at https://www.reddit.com/r/ai_agents/wiki (this is currently in test and we are actively adding to the wiki)
I am a bot, and this action was performed automatically. Please contact the moderators of this subreddit if you have any questions or concerns.
 b_nodnarb •  8d ago  Check out 2 things: Agno (open source Apache-2.0 License) and AgentSystems:
Full disclosure: I'm a maintainer of AgentSystems, which is an open-source (also Apache-2.0) self-hosted app store for third-party agents. Discover agents built by others, install them, run them on your infrastructure. Aims to solve the discovery + trust problem (how do you run someone else's agent without exposing credentials?). https://github.com/agentsystems/agentsystems
 Curious-Victory-715 •  7d ago  Been there, it’s rough juggling tool complexity with actual agent building. I've also leaned on Lang Chain heavily for its modularity, but found debugging chains can be a time sink if you don't structure early. AutoGen’s multi-agent orchestration is neat but yeah, the docs could use some love to smooth that learning curve. CrewAI’s focus on business logic resonates, though smaller community means fewer ready-made solutions. Curious, have you tried combining these or layering them in your workflows, or do you find sticking to one tool streamlines development better?
 Ok_Student8599 •  7d ago  •    Edited  7d ago  
10x smaller code and code that your CEO can understand - Playbooks - https://github.com/playbooks-ai/playbooks
Comparison - https://playbooks-ai.github.io/playbooks-docs/reference/playbooks-traditional-comparison/
 ugon •  7d ago  ADK is definitely the best, langchain is bloated af and wouldn’t use it in production. Too many vulnerabilities to deal with
 grow_stackai •  7d ago  Solid breakdown. LangChain still feels like the backbone for most setups, but I’ve also found CrewAI’s structured team logic surprisingly stable for complex workflows. AutoGen is powerful but takes time to tune properly.
I’d add LlamaIndex to your list—it bridges data sources smoothly and plays well with both LangChain and custom agents. The ecosystem’s maturing fast, but unified debugging across these tools is still the missing piece.
 Black-Rose445 •  4d ago  Accurate
 IdeaAffectionate945 •  11h ago  You should check out my platform, specifically created to be a no-code AI agent creator platform.
https://github.com/polterguy/magic
More posts you may like
 50+ Open-Source Tools to Build and Deploy Autonomous AI Agents r/AIAGENTSNEWS  •  r/AIAGENTSNEWSFind trending AI Agents Updates...
Members  50+ Open-Source Tools to Build and Deploy Autonomous AI Agents
 upvotes  ·    comments  
 How are you using computer-use agents? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  How are you using computer-use agents?
 upvotes  ·    comments  
 Tested 5 agent frameworks in production - here's when to use each one r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Tested 5 agent frameworks in production - here's when to use each one
 upvotes  ·    comments  
 Awesome List of AI Software Development Agents r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Awesome List of AI Software Development Agents
 upvotes  ·    comments  
 What AI tools/agents are you really using regularly (not just testing)? Any fresh discoveries? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What AI tools/agents are you really using regularly (not just testing)? Any fresh discoveries?
 upvotes  ·    comments  
 What Are Your Biggest Pain Points in Workflow Automation? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What Are Your Biggest Pain Points in Workflow Automation?
 upvotes  ·    comments  
 Has anyone integrated an AI agent or Agentic Workflow into a business at scale? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Has anyone integrated an AI agent or Agentic Workflow into a business at scale?
 upvotes  ·    comments  
 Getting Started with AI Automation & Agents — Any Tips for Beginners? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Getting Started with AI Automation & Agents — Any Tips for Beginners?
 upvotes  ·    comments  
 Any actual agentic/autonomous agents out there? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Any actual agentic/autonomous agents out there?
 upvotes  ·    comments  
 The HARDEST part about running an AI automation agency r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  The HARDEST part about running an AI automation agency
 upvotes  ·    comments  
 I'm done with AI agent frameworks, but it is a great learning curve to understand how to make effective agents r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  I'm done with AI agent frameworks, but it is a great learning curve to understand how to make effective agents
 upvotes  ·    comments  
 We're focusing way too much on autonomous agents and not enough on human-in-the-loop systems r/Agentic_AI_For_Devs  •  r/Agentic_AI_For_DevsFocused on developing AI agents for useful apps. For experienced software developers only. The moderator is mean and will remove dumb posts. Search Google first before asking questions. Technical and highly relevant questions only.
Members  We're focusing way too much on autonomous agents and not enough on human-in-the-loop systems
 upvotes  ·    comments  
 I built an AI Agent to Fix Database Query Bottlenecks r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  I built an AI Agent to Fix Database Query Bottlenecks
 upvotes  ·    comments  
 what's your biggest pain with AI agents and structured data access? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  what's your biggest pain with AI agents and structured data access?
 upvotes  ·    comments  
 Best Open-Source AI agent? Help! Switching from Manus & OpenAI r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Best Open-Source AI agent? Help! Switching from Manus & OpenAI
 upvotes  ·    comments  
 Top 5 AI QA tools ? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Top 5 AI QA tools ?
 upvotes  ·    comments  
 Building a Computer-Use Agent that works like a real human r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Building a Computer-Use Agent that works like a real human
 upvotes  ·    comments  
 Creating an AI agent for unit testing automation r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Creating an AI agent for unit testing automation
 upvotes  ·    comments  
 Any good analytics tool for AI Agents? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Any good analytics tool for AI Agents?
 upvotes  ·    comments  
 Built 5 Agentic AI products in 3 months (10 hard lessons i’ve learned) r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Built 5 Agentic AI products in 3 months (10 hard lessons i’ve learned)
 upvotes  ·    comments  
 Has anyone here tried using automated AI agents for content audits, content optimization, or AI search visibility? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  SPOILER  
Has anyone here tried using automated AI agents for content audits, content optimization, or AI search visibility?
 upvotes  ·    comments  
 I need help getting clients for my AI agency r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  I need help getting clients for my AI agency
 comments  
 What automation tools are actually helping ? r/RecruitmentAgencies  •  r/RecruitmentAgenciesA community for recruiting and talent acquisition professionals to share their knowledge regarding the latest trends in recruiting, recruitment entrepreneurship, and other recruitment and staffing issues.
Members  What automation tools are actually helping ?
 upvotes  ·    comments  
 Running an AI Agency? Whats your biggest problem? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Running an AI Agency? Whats your biggest problem?
 upvotes  ·    comments  
0   0  Reddit RulesPrivacy PolicyUser AgreementAccessibilityReddit, Inc. © 2025. All rights reserved.
Log In / Sign Up  
Advertise on Reddit  
Cookie Preferences  
Try Reddit Pro  BETA  