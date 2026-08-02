> Source: https://www.reddit.com/r/AI_Agents/comments/1nnh4wn/which_ai_approach_do_you_prefer_one_super_agent/

Skip to main content  Open navigation  Go to Reddit Home  Log In  Log in to Reddit   Open settings menu  
Log In / Sign Up  
Advertise on Reddit  
Cookie Preferences  
Try Reddit Pro  BETA  
Reddit, Inc. © 2025. All rights reserved. Copy link 
 Copy link 
 Go to AI_Agents r/AI_Agentsr/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members   •  Weekly_Cry_5522Português (Brasil)Español (Latinoamérica)Which AI approach do you prefer: One "super" Agent or multiple specialized ones? 
Discussion  Hey everyone, I'm doing some research and would love your quick opinion on a fundamental question about AI agents.
When it comes to AI agents, what do you think is a better approach?
A single, unified agent that has access to all the tools and knowledge it needs, acting as a one-stop-shop for any task.
Specialized, separate agents, where each agent is an expert at a different type of task (e.g., one for writing, one for data analysis, one for programming).
If you prefer the specialized agents, would you want them to be able to talk to each other? For example, if a writing agent gets a confusing request, it could ask a data analysis agent for help to get the right information before it responds.
I'm genuinely curious to hear what you all think about the trade-offs and potential use cases. What would be most useful to you?
 Share  Sort by:  Best   Open comment sort options   Best  
Top  
New  
Controversial  
Old  
Q&A  
 Nerdyedad •  2mo ago  I believe the multi agent is more effective as the cooperative approach can lead to better results and in a faster way.
Additionally it would cost less.
 Weekly_Cry_5522 •  2mo ago  Yes it's less costly ( to a certain limit) and the advantage is the distributed context window.
 AlyonaAutomates •  2mo ago  Have the same thoughts! It is even critical to have multiple specialized ones if you are engaged in super niche.
More replies   bbu3 •  2mo ago  My rules of thumb:
As little AI as necessary, as much deterministic code as possible.
As few agents as possible (pro wrt your single agent option)
Multiple agents are one of the easiest ways to organize context windows (that's one of the best reasons to split something into multiple agents).
Prefer deterministic calling of agents and manual orchestration. If you must, an orchestrator agent is okay. Avoid anything beyond a star-shaped orchestrator plus agents at all costs. No long chains of agents calling each other at will
 Weekly_Cry_5522 •  2mo ago  I would like to talk about its details, if you don't mind can i dm?
 Dizzy2046 •  2mo ago  multiple ai voice agent are difficult to handle that's you need flexible open source, and ai to ai testing voice agent like i am using dograh ai for inbound/outbound calling
 Fluffy-Wrongdoer-400 •  2mo ago  I think one pushback I have on your process is manual orchestration wholesale. I would prefer automated orchestration agents with each sub agent a single portion of the knowledge base (most people use them for process orchestration as opposed to knowledge subset orchestration.
For example: if I want to run due diligence I may or may not have agents to call for data and write the report but I’m going to have agents running dd on an investment under tax, finance, legal, marketing metrics, etc. I always would want a poor mans version of a MoE agent to run a red team report (it’s not a true MoE, but I find having different agents with single bodies of knowledge each with their own RAG based on the public information on figures I respect on a topic all weighing in on the red team surfaces different concerns and catches more contextualized concerns or orthogonal thinking that a ToT model or few shot llm api.
So the orchestration wouldn’t happen on full process but on first pass screening and assembling areas of concern. I would want to work with the orchestration agent to better surface responses, not press a big red button to run the entire business.
More replies   LizzyMoon12 •  2mo ago  I don’t really see one “super” agent as the answer, in enterprise contexts I’ve noticed something interesting when comparing approaches.
When organizations try to build a single unified agent that does everything, it often feels very much like the old monolithic systems, simple at first glance, but hard to scale, hard to maintain, and quick to hit limitations. The promise of “one brain to rule them all” sounds efficient, but in practice, these setups can become bottlenecks.
By contrast, the specialized agent model, where each agent is excellent at a narrow task, maps more naturally to real business workflows. Think of one agent designed to parse a contract, another to summarize risks, and a third to prepare a client-ready communication. Individually, each does a focused job. Together, they create a far more robust and flexible system. And when these agents can talk to each other, the result feels closer to microservices: modular, adaptable, and easier to evolve as needs change.
So the real value isn’t in choosing one model over the other in theory, but in recognizing that specialized agents with the ability to collaborate bring both resilience and agility. That’s where I see the most potential, reducing complexity while still allowing organizations to adapt quickly as AI capabilities advance.
 blopiter •  2mo ago  Multiple specialized is the future
 JudgmentFederal5852 •  2mo ago  I lean toward specialized agents. In one setup I worked on, a voice agent handled customer feedback while a separate one structured and synced that data back into the system. Keeping them focused made the process smoother than trying to run everything through one super agent.
When you’ve tested them, did you notice any significant downsides to letting agents communicate with each other versus keeping them siloed?
 Weekly_Cry_5522 •  2mo ago  Well, when the agents are siloed they can't answer or proceed on the tasks that require little bit of another field's knowledge, and that might stop the process or lead to the agents hallucination.
And when they are connected to communicate, it would be one or bi-directional chain. And can complete the work which requires the knowledge of multiple fields.
I was thinking what if there is another hybrid direction that determines based on the usecase and the agents hallucination level to connect with another agent for the information.
What do you think about it?
 JudgmentFederal5852 •  2mo ago  That’s an interesting point. I’ve also seen the downside of siloed agents, where they hit a wall if the task overlaps with another domain. But on the flip side, fully connected agents sometimes over-communicate and create noise. A hybrid setup makes sense, where the agent only pulls in another when confidence drops or the task clearly spans multiple fields. The bigger challenge is deciding what that trigger looks like in practice.
 Fluffy-Wrongdoer-400 •  2mo ago  My answer would be a fine tuned orchestrator layer that works on the bridging below anything human or master orchestrator. Multi topic integration agent if you will. Its job is to error check across the Chinese wall and communicate the lack of context or the lack of broader implications considered.
 JudgmentFederal5852 •  2mo ago  Makes sense. An orchestrator that flags context gaps instead of letting errors slip through sounds solid. Have you tried letting it auto-route to another agent when it spots missing info, or do you always keep a human in the loop?
More replies  More replies  More replies  More replies   Joy_Boy_12 •  2mo ago  I have a question for those who claim multiple agents is better.
how small should agent be? How can I know when to say that the agent is specialized enough?
for example travel agent, should it be split to booking and search flight? Maybe the search flight should be split to more agents?
I feel that I’m not sure at deciding when I should split an agent to multiple agents and when to say this scope is enough for one agent.
moreober Should a specialized agent get at anytime all the tools or we should filter for him the tools Based on the task?
 Fluffy-Wrongdoer-400 •  2mo ago  For me it’s a question of how big your base knowledge is that the drift in output becomes unreliable. Too small and you go deterministic (flights from JFK to Heathrow is a google search, not an agentic process). I would actually argue in your travel agent example your smallest agent would be one querying extisting flights on ITA matrix or whatever.
In the travel agent scenario most people are focusing on splitting agents based on task. But the flight booking agent is the same body of knowledge.
Knowing for example to interpret weather for delays or scan sentiment for geopolitical shifts (oh you are Ukrainian? May not be the best time for a vacation to Moscow).would be separate
More replies   National_Machine_834 •  2mo ago  I prefer specialized agents but only if they can talk to each other without me babysitting them.
A single “super agent” sounds elegant… until it hallucinates a SQL query while writing a poem, or tries to “optimize” your blog post into a Python script.
Specialized agents? They stay in their lane. 
 → The writer writes. 
 → The analyst crunches. 
 → The coder builds. 
 No identity crisis. No tool confusion. No “I thought you meant…”
But here’s the catch: 
 If they can’t collaborate — it’s just silos with extra steps.
The real magic happens when:
→ The writing agent hits a data gap → pings the analyst → gets clean numbers → drops them into the draft — without me copying/pasting. 
 → The coding agent needs context → asks the research agent → gets summarized docs → auto-generates the right function. 
 → The design agent pulls tone + keywords from the writer → generates on-brand visuals — no brief needed.
That’s not sci-fi. That’s n8n + LangChain + a little routing logic.
Biggest win? Debugging.When something breaks, you know which agent failed — not “the whole system is down.”
And if you want to swap out one piece? Replace the image generator. Keep the rest. No full rewrite.
Downside? Complexity. Setup. Testing. 
 You’re not building one agent. You’re building a team — and teams need rules, handoffs, and fallbacks.
But once it works? It scales cleaner, fails softer, and feels more… human.
Because humans don’t do everything. 
 We call the right person for the job.
Your AI should too.
If you’re testing this, start small: 
 → Build two agents: one that writes, one that fact-checks. 
 → Let them pass messages. Watch what breaks. Fix it. Repeat.
And if you want free tools to prototype prompts, workflows, or agent handoffs: 
https://freeaigeneration.com/blog/from-idea-to-draft-accelerating-your-writing-with-ai-toolshttps://freeaigeneration.com/blog/the-ai-content-workflow-streamlining-your-editorial-process
No paywall. No login. Just paste your idea → get back something structured.
Let me know how your test goes — I’ll help you debug the handoff.
 Altruistic-Classic72 •  2mo ago  One doing everything is a recipe for disaster. You need smaller specialized ones for reliability
 crystalanntaggart •  2mo ago  I use ALL the AIs and I have them cross-collaborate with each other. But I also have specialized prompts for specific tasks targeted for specific AIs as well.
Question: are you building a platform? Reason why I ask is I have started development on an open source platform that does this and have software designs for capabilities to do this. If you want to collaborate, ping me on LinkedIn. My name is real and I’m a top .00001% user of ChatGPT.
I haven’t been able to get back to coding this platform yet (currently working on a startup called Cinemachina.ai where we create movies with ai.
 fasti-au •  2mo ago  Unless you have context or control of the training you sorta need context size for all levels. It doesn’t make sense to build bottlenecks so calling smaller agents seems to be the superior option for most things
 AutoModerator •  2mo ago  Thank you for your submission, for any questions regarding AI, please check out our wiki at https://www.reddit.com/r/ai_agents/wiki (this is currently in test and we are actively adding to the wiki)
I am a bot, and this action was performed automatically. Please contact the moderators of this subreddit if you have any questions or concerns.
 Dan27138 •  2mo ago  Both approaches have merit, but specialized agents often offer more reliable, explainable outputs—especially in mission-critical domains. Cross-agent collaboration can combine expertise without sacrificing transparency. At AryaXAI, our research (DLBacktrace: https://arxiv.org/abs/2411.12643) emphasizes interpretability and risk management, which aligns well with multi-agent systems working together safely and effectively.
 DecodeBytes •  2mo ago  Smaller agents, with a limited set of tools to select from , beat behemoths trying to do everything: https://www.youtube.com/watch?v=3Ak8fk3PaBU
 Dizzy2046 •  2mo ago  there is no super agent there is always a gap for updating ai voice agent, like i myself using dograh ai for real estate business for inbound/outbound calling, i need to update according to my use case as open source give me flexibility to customize as per my need
 realAIsation •  2mo ago  I lean toward specialized agents that can hand off work to each other. In my experience, “super agents” sound cool on paper but usually end up spreading thin, missing depth in execution. Having multiple focused agents feels closer to how real teams operate, each good at their domain, but collaborating when needed.
I’ve seen platforms like ZBrain build around this idea, where finance, supply chain, and ops agents can run independently but also connect when workflows overlap. That combo has been more reliable for me than trying to make one mega-agent handle everything.
I want to ask, do you picture your ideal setup being more like a team of experts or a personal assistant who tries to do it all?
 SERPArchitect •  2mo ago  Separate agents all the way. One “super” agent sounds cool, but it ends up being a jack of all trades, master of none.
Specialized agents stay sharp, faster, and way easier to debug.
 Designer_Manner_6924 •  2mo ago  a single unified one is something i'd prefer tbh because it would require less training, if you will. like i have one that icreated via voicegenie that i use to handle my customer service, and it can not only answer FAQs, but also book meetings, do reminders and follow ups.
 acloudfan •  2mo ago  My take:
Based on my research and experience, the answer isn't one-size-fits-all; it depends entirely on the complexity of the tasks you want to accomplish.
So we are on the same page, let me break down the two main architectures you're describing:
Single Agent System (SAS): A "master" agent that has access to all necessary tools and knowledge. Think of it as a skilled generalist.
For straightforward tasks that require a linear sequence of actions using a few tools, a single agent is easier to design, build, and manage. There's no overhead of managing inter-agent communication, which can be complex. If a task doesn't require deep specialization, the back-and-forth of a multi-agent system might just add unnecessary time.
In case you are building a complex SAS, then yes by all means you should consider breaking into multiple specialized agents and then apply the "Agent as tool" pattern in which a single master agent leverages other agents like any other tool. An additional benefit of this approach is re-use of agents.
With SAS, since there is a "Single brain" at work, the inter-communication between agents is non-existent by nature.
Multi-Agent System (MAS): A team of specialized agents (e.g., Writer, Analyst, Coder) that can work independently or collaboratively. Collaboration between agents require communication between them that can be achieved via different topologies.
My rule of thumb is that "Use MAS over SAS only if its necessary"; use it only for complex tasks. There are multiple benefits of this approach : Modularity, Scalability, Efficiency.
Now some folks have indicated that multiple-agents are more cost effective - I would not agree with this as a "blanket statement". Answer depends on multiple factors. I would say "MAS done the right way can potentially lead to cost saving".
 sleepydevs •  2mo ago  Multiple fine tuned small models orchestrated by something larger is The Way imo.
 sleepydevs •  2mo ago  With deterministic tools everywhere. Rely on the models as little as possible.
You wouldn't try to put a nail into a wall with your bare hand, you'd get a hammer and use it. Small Agents should use tools as much as possible.
 csells •  2mo ago  What do you use for the orchestration?
More replies   help-me-grow •  2mo ago  best practice rn is multiple specialized ones
you can introduce a managing or orchestrating agent on top to reduce your load
 BidWestern1056 •  2mo ago  i find very rarely that agent coding tools help me get to solutions faster than just chatting and carrying out actions that LLMs suggest. it also forces me as an intermediary in all cases so i dont waste as much time in nonsense loops where nothing gets fixed.
 astronomikal •  2mo ago  Multiple specialized is the hands down obvious choice, distributed across many domains you make a super intelligence
 stevenverses •  2mo ago  Here's a paper co-authored by Karl Friston Designing Ecosystems of Intelligence from First Principles that envisions a diverse array of specialized self-optimizing self-organizing systems. Makes so much more sense than one monolithic all-knowing general purpose pre-trained LLM.
 madolid511 •  2mo ago  The more "dedicated" your agent the more it will be deterministic.
Shorter prompt, more relevant (controlled) context. Easier to debug and maintain. Development can be in parallel with different teams.
I have experience in both. 
 Multiple "polished" agents significantly more reliable than over-promised feature-rich unstructured no-architect know-all agent 😅.
 ViriathusLegend •  2mo ago  It really depends on the use case.
A single “super” agent can be easier to manage in simple, tightly scoped projects, but it often becomes monolithic and hard to adapt. Multiple specialized agents, on the other hand, encourage modularity, reusability, and scalability - you can plug them into new workflows or upgrade components independently. They also mirror real-world systems better, where different roles handle different tasks. The trade-off is added orchestration complexity, but with good coordination patterns, specialized agents usually scale more effectively in complex environments.
I suggest comparing various agentic frameworks to see which ones provide workflows and orchestration styles that best match your intended setup. This repo is good starting point: https://github.com/martimfasantos/ai-agent-frameworks
 alvincho •  2mo ago  No matter how super it is, a single agent can’t know or do everything, and waste the resources. Specialized tiny agents collaborate together is much better than a single super agent.
 Middle_Macaron1033 •  1mo ago  I lean toward the “multiple specialized agents” approach, because it’s more flexible and mirrors how teams work in real life.
For example, I use different models for different strengths: GPT-4 for reasoning and writing, Claude for summarization and tone, and Mistral or Gemini for quick idea exploration.
We actually just launched a platform that utilizes over 2,200 LLMs using only one API.
It lets you connect multiple AIs and your own data in one place, so you can experiment with which model handles each task best. Instead of trying to build one “super” agent that does everything, our software coordinates specialized ones through our unified platform.
I can send you the details if you're interested in trying it out.
 ai-agents-qa-bot •  2mo ago  Top 1% Commenter  
The choice between a single "super" agent and multiple specialized agents often depends on the specific use case and requirements.
Single Unified Agent:
Pros:
Simplifies user interaction by providing a one-stop solution.
Can leverage a broad range of knowledge and tools without needing to coordinate between agents.
Cons:
May become overly complex and less efficient as it tries to handle diverse tasks.
Risk of performance bottlenecks if the agent is overloaded with requests.
Multiple Specialized Agents:
Pros:
Each agent can focus on its area of expertise, potentially leading to higher quality outputs.
Easier to update or improve individual agents without affecting the entire system.
Cons:
Requires an orchestration mechanism to manage communication and task delegation between agents.
Complexity in ensuring that agents can effectively collaborate when needed.
If opting for specialized agents, enabling them to communicate can enhance their effectiveness. For instance, a writing agent could consult a data analysis agent for accurate information, leading to more informed responses.
For more insights on AI agent orchestration and the benefits of using multiple specialized agents, you might find this article helpful: AI agent orchestration with OpenAI Agents SDK.
 alokin_09 •  2mo ago  Depends on the use case tbh.
For general stuff like writing and brainstorming - single agent all the way. ChatGPT/Claude handles this fine.
For coding though, I'm all about the specialized approach. Been using Kilo Code (I'm one of the contributors there) and their separate modes for orchestration, architecture, coding, and debugging just work better. Breaking things into chunks gives me way more control.
 Weekly_Cry_5522 •  2mo ago  Yeah right, depends on the usecase. But whenever we need to add actions on steps rather than just information the multiple agent ones is better ig.
More replies   glassBeadCheney •  2mo ago  i favor a single agent approach every single time, with one built-in exception: if i implement a "review gate" where the big agent's actions require review at some juncture before they're cleared, the reviewer is always a different agent.
a multi-agent system has more failures in it than a single-agent system. it can hide more surprises from us than the single agent can, and surprises are usually bad when we're building something. we know the problem we're solving w/ multi-agent, but we don't know every problem multi-agent is introducing. so, if we're going from single -> multi agent, we should expect the known problem to cost us more than we expect all the new unknowns to cost combined. policy compliance, legal, potentially major breaking changes, etc. meet that standard.
 FlyingDogCatcher •  2mo ago  Less is more.
The more context your llm has the less you know what it will do next
More posts you may like
 What’s your ideal AI agent setup? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What’s your ideal AI agent setup?
 upvotes  ·    comments  
 How do you choose a "business worthy" AI agent? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  How do you choose a "business worthy" AI agent?
 upvotes  ·    comments  
 Which is most preferred way for everyone build AI agents? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Which is most preferred way for everyone build AI agents?
 upvotes  ·    comments  
 "Pricing for a Custom AI WhatsApp Bot: How Much Would You Charge?" r/n8n  •  r/n8nn8n is an extendable workflow automation tool. With a fair-code distribution model, n8n will always have visible source code, be available to self-host, and allow you to add your own custom functions, logic and apps. n8n's node-based approach makes it highly versatile, enabling you to connect anything to everything. https://n8n.io/
Members  "Pricing for a Custom AI WhatsApp Bot: How Much Would You Charge?"
 upvotes  ·    comments  
 What's the difference between an AI Agent and just a really in depth automation? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What's the difference between an AI Agent and just a really in depth automation?
 upvotes  ·    comments  
 Beyond the Basics: What Do You Consider "Advanced" in Flutter? r/flutterhelp  •  r/flutterhelpA community to request help with your flutter code.
Members  Beyond the Basics: What Do You Consider "Advanced" in Flutter?
 upvotes  ·    comments  
 I'm done with AI agent frameworks, but it is a great learning curve to understand how to make effective agents r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  I'm done with AI agent frameworks, but it is a great learning curve to understand how to make effective agents
 upvotes  ·    comments  
 What tech is used by expert networks? Would you guys use a full-stack platform as your expert network instead? r/expertnetworks  •  r/expertnetworksHave you been invited to consult or interview with an expert network like GLG, Guidepoint, Alphasights, Third Bridge, or Coleman Research? This is the place to learn how they work, what to expect on calls, where to set your hourly rate, how to land more projects, how to remain in compliance and how to grow your expert network consulting practice.
Members  What tech is used by expert networks? Would you guys use a full-stack platform as your expert network instead?
 comments  
 Stop asking 'Which vector DB is best?' Ask 'Which one is right for my project?' Here are 5 options. r/n8n  •  r/n8nn8n is an extendable workflow automation tool. With a fair-code distribution model, n8n will always have visible source code, be available to self-host, and allow you to add your own custom functions, logic and apps. n8n's node-based approach makes it highly versatile, enabling you to connect anything to everything. https://n8n.io/
Members  Stop asking 'Which vector DB is best?' Ask 'Which one is right for my project?' Here are 5 options.
 upvotes  ·    comments  
 Any critical views on AI agents? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Any critical views on AI agents?
 upvotes  ·    comments  
 Which class do you think can reliably convey what's "Wrong" with a team the quickest r/marvelrivals  •  r/marvelrivalsMarvel Rivals is a Super Hero Team-Based PVP Shooter! Assemble an all-star Marvel squad, devise countless strategies by combining powers to form unique Team-Up skills and fight in destructible, ever-changing battlefields across the continually evolving Marvel universe!
Members  Which class do you think can reliably convey what's "Wrong" with a team the quickest
 comments  
 What tools do you use to OE easier? AI? r/overemployed  •  r/overemployedWork multiple jobs during the same 40 hours, reach financial freedom.
Members  What tools do you use to OE easier? AI?
 upvotes  ·    comments  
 What are your criteria for defining what an AI agent requires to be an actual AI agent? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What are your criteria for defining what an AI agent requires to be an actual AI agent?
 upvotes  ·    comments  
 What’s the best way to get serious about building AI agents? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What’s the best way to get serious about building AI agents?
 upvotes  ·    comments  
 Want to build an AI agent — where do we start? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Want to build an AI agent — where do we start?
 upvotes  ·    comments  
 Why is everyone building AI agents when nobody can agree what an "AI agent" even is? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Why is everyone building AI agents when nobody can agree what an "AI agent" even is?
 comments  
 Is building an AI agent this easy? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Is building an AI agent this easy?
 upvotes  ·    comments  
 Looking for honest feedback: Would your team use a "Vibe Coding" dev environment powered by AI? r/ChatGPTCoding  •  r/ChatGPTCodingWelcome to our community! This subreddit focuses on the coding side of ChatGPT - from interactions you've had with it, to tips on using it, to posting full blown creations! Make sure to read our rules before posting!
Members  Looking for honest feedback: Would your team use a "Vibe Coding" dev environment powered by AI?
 comments  
 Looking for honest feedback: Would your team use a "Vibe Coding" dev environment powered by AI? r/cursor  •  r/cursorThe AI Code Editor - cursor.com
Members  Looking for honest feedback: Would your team use a "Vibe Coding" dev environment powered by AI?
 comments  
 Anyone who builds AI agents professionally or running an agency ? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Anyone who builds AI agents professionally or running an agency ?
 upvotes  ·    comments  
 What is AI agent?and how should i build one r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  What is AI agent?and how should i build one
 upvotes  ·    comments  
 Anyone using multiple AI agents at once instead of just one model? r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Anyone using multiple AI agents at once instead of just one model?
 upvotes  ·    comments  
 Forget the hype. Here's how you actually get good at building AI agents. r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Forget the hype. Here's how you actually get good at building AI agents.
 upvotes  ·    comments  
 Self-improving AI agent is a myth r/AI_Agents  •  r/AI_AgentsA place for discussion around the use of AI Agents and related tools. AI Agents are LLMs that have the ability to "use tools" or "execute functions" in an autonomous or semi-autonomous (also known as human-in-the-loop) fashion. Follow our event calendar: https://lu.ma/oss4ai Join us on Discord! https://discord.gg/6tGkQcFjBY
Members  Self-improving AI agent is a myth
 upvotes  ·    comments  
 Opus or Sonnet? How do you decide which AI model to use for a task? r/ClaudeAI  •  r/ClaudeAIThis is a Claude by Anthropic discussion subreddit to help you make a fully informed decision about how to use Claude and Claude Code to best effect for your own purposes. ¹⌉ Anthropic does not control or operate this subreddit or endorse views expressed here. ²⌉ If your problem requires Anthropic's help, visit https://support.anthropic.com/ This subreddit is not the right place to fix your account issues. ³⌉ For more help, check the resources below. ⁴⌉ Please read the rules before posting.
Members  Opus or Sonnet? How do you decide which AI model to use for a task?
 upvote  ·    comments  
View Post in
Français हिन्दी 0   0  Reddit RulesPrivacy PolicyUser AgreementAccessibilityReddit, Inc. © 2025. All rights reserved.
Log In / Sign Up  
Advertise on Reddit  
Cookie Preferences  
Try Reddit Pro  BETA  