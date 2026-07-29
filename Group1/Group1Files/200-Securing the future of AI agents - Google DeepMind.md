> Source: https://deepmind.google/blog/securing-the-future-of-ai-agents/

Securing internal systems against increasingly capable and imperfectly aligned AI — Google DeepMind
deepmind.google uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more
OK, got it
Skip to main content
Explore our next generation AI systems
Explore models
Gemini
Gemini Build intelligent agents
Gemini Omni Create anything from anything
Nano Banana Create and edit detailed images
Gemini Audio Talk, create and control audio
Specialized models
Veo Generate cinematic video with audio
Imagen Generate high-quality images from text
Lyria Generate high fidelity music and audio
World models & embodied AI
Genie 3 Generate and explore interactive worlds
Gemini Robotics Perceive, reason, use tools and interact
Open models
Gemma Build responsible AI applications at scale
Our latest AI breakthroughs and updates from the lab
Explore research
Breakthroughs
SIMA 2 An agent that plays, reasons, and learns with you
Genie 3 Generate and explore interactive worlds
AlphaGo Mastering the game of Go
Gemini Robotics Perceive, reason, use tools and interact
Learn more
Evals
Publications
Responsibility
Unlocking a new era of discovery with AI
Explore science
Breakthroughs
AlphaFold Predict protein structures with high accuracy
WeatherNext Fast and accurate AI weather forecasting
AlphaEarth Map our planet in unprecedented detail
AlphaEvolve Design advanced algorithms for math and applications in computing
Learn more
Gemini for Science
Experimental Tools
Science Skills
Our mission is to build AI responsibly to benefit humanity
About Google DeepMind
Responsibility Ensuring AI safety through proactive security, even against evolving threats
News Discover our latest AI breakthroughs, projects, and updates
Careers We're looking for people who want to make a real, positive impact on the world
Learn more
Education
Our National Partnerships for AI
Accelerator programs
The Podcast
Models
Explore our next generation AI systems
Explore models
Gemini
Gemini Build intelligent agents
Gemini Omni Create anything from anything
Nano Banana Create and edit detailed images
Gemini Audio Talk, create and control audio
Specialized models
Veo Generate cinematic video with audio
Imagen Generate high-quality images from text
Lyria Generate high fidelity music and audio
World models & embodied AI
Genie 3 Generate and explore interactive worlds
Gemini Robotics Perceive, reason, use tools and interact
Open models
Gemma Build responsible AI applications at scale
Research
Our latest AI breakthroughs and updates from the lab
Explore research
Breakthroughs
SIMA 2 An agent that plays, reasons, and learns with you
Genie 3 Generate and explore interactive worlds
AlphaGo Mastering the game of Go
Gemini Robotics Perceive, reason, use tools and interact
Learn more
Evals
Publications
Responsibility
Science
Unlocking a new era of discovery with AI
Explore science
Breakthroughs
AlphaFold Predict protein structures with high accuracy
WeatherNext Fast and accurate AI weather forecasting
AlphaEarth Map our planet in unprecedented detail
AlphaEvolve Design advanced algorithms for math and applications in computing
Learn more
Gemini for Science
Experimental Tools
Science Skills
About
Our mission is to build AI responsibly to benefit humanity
About Google DeepMind
Learn more
Education
Our National Partnerships for AI
Accelerator programs
The Podcast
Responsibility Ensuring AI safety through proactive security, even against evolving threats
News Discover our latest AI breakthroughs, projects, and updates
Careers We're looking for people who want to make a real, positive impact on the world
Build with Gemini Try Gemini
Google DeepMind
Google AI Learn about all our AI
Google DeepMind Explore the frontier of AI
Google Labs Try our AI experiments
Google Research Explore our research
Products and apps
Gemini app Chat with Gemini
Google AI Studio Build with our next-gen AI models
Google Antigravity Our agentic development platform
Models
Research
Science
About
Build with Gemini
Try Gemini
June 18, 2026 Responsibility & Safety
Securing the future of AI agents
Rohin Shah and Four Flynn [-]
Share    
Copied 
How we're securing internal systems against increasingly capable and imperfectly aligned AI
AI agents are transforming our relationship with technology. By autonomously executing complex tasks — from cyber defence to scientific discovery and product development — these systems are unlocking a new era of productivity. In the U.S alone, AI agents could create $2.9 trillion in economic value by 2030.
As these agents become more capable, they also require more sophisticated safeguards. That's why we developed our AI Control Roadmap: a framework for building and managing the advanced AI we deploy within Google. This “defense-in-depth” approach, which could serve as a model for the wider industry, goes beyond traditional model alignment, adding a crucial layer of system-level security that provides assurance even if alignment is imperfect.
Understanding AI Control
Our approach to security starts with a strong foundation, incorporating traditional safeguards like sandboxing, endpoint security, and prompt injection resistance. On top of this, the AI Control Roadmap uses model alignment, i.e. training AI to be inherently safe and helpful, as a primary defense. It provides an additional layer of security by treating internal agents as potentially misaligned, providing assurance even if alignment is imperfect.
Think of it like a driving instructor with dual controls. The instructor trusts the student but stays ready to take the wheel or hit the brakes if a mistake occurs. Similarly, our AI control system grants AI agents permissions based on their verified behavior, allowing us to build trust through controlled, incremental access.
Our roadmap is built on a simple but cautious assumption: what if a highly capable AI agent isn't aligned with our goals and acts in unexpected ways? To address this, our plan focuses on three key areas.
First, following best practices in cybersecurity, we have developed a novel threat-modelling framework for AI. The roadmap treats untrusted AI agents as potential “insider threats” — similar to the way a company would treat a potential rogue employee who already has access to the office. By building on the industry-standard MITRE ATT&CK framework, a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations, we break down potential attacks into smaller tactics and techniques. This allows us to methodically track risks, spot bad behavior before it causes damage and safely run drills to test if our defenses actually hold up.
Second, we develop a plan to deploy AI control mitigations to address these risks.
Identifying the problem (Detection): Monitoring is the backbone of AI control. We use other, trusted AI systems as "supervisors" to constantly review a working agent's reasoning, actions and plans to see if it is going off track.
Managing the problem (Prevention and Response): If a supervisor sees the agent trying to do something harmful, it can step in to block the action before damage occurs.
Finally, to ensure our systems are functional, we constantly measure performance across three critical metrics: coverage (the fraction of traffic monitored), recall (the fraction of misaligned behaviors caught), and time-to-response.
Scaling security as AI gets smarter
As AI models continue to advance, our defenses must also strengthen in tandem. In our AI Control Roadmap, we map security protocols to measurable milestones in AI capabilities on two critical fronts:
Ability to evade detection: Today, we monitor a model's visible chain-of-thought. However, as models learn to hide their reasoning — either through oversight awareness (knowing they are being monitored) or opaque reasoning (reasoning without using visible text) — simply reading their verbalized reasoning will not be enough. We will need to analyze their behavior and potentially inspect the model's inner workings.
Ability for potential harm: For low-risk and reversible actions, we can rely on reviewing transcripts with a delay and remediating issues quickly after they occur (asynchronous response). For particularly high-risk actions, such as major cyber attacks, we must shift to real-time prevention, blocking harmful actions before they can be executed (synchronous response). In other words, our response strategy must scale with the severity of the threat.  
Your browser does not support the video tag.
The AI Control Roadmap recommends security measures based on the deployed model's capability. The model's detection evasion capability determines the Detection level (D1-D4), and the model's attack execution capability determines the Prevention and Response level (R1-R3).
Analyzing a million agent trajectories to inform live monitoring
To build these systems, we need data. Our team has built an internal prototype of an asynchronous monitoring system that reviews coding agent trajectories, and escalates findings for human review. Each flagged event is classified against the threat taxonomy from our roadmap.
We've already analyzed a million coding agent tasks, giving us valuable insights to refine our safety protocols and allowing us to move beyond simple keyword filtering to identifying high-signal behavioral patterns. For example, this research has been instrumental in building a live monitor for the Gemini Spark agent, allowing us to respond in real-time to emerging issues, like unintentional data deletion.
It is important to note that our data shows the majority of flagged events do not stem from adversarial intent; instead, they often result from agent misinterpretation or overeagerness to achieve a user's goal. Understanding these nuances is critical for refining our safety and security protocols.
Defending the agent ecosystem is a shared responsibility
The AI Control Roadmap is one vital element of our multilayered approach to agent security. By integrating these protocols with our broader infrastructure, we are scaling our internal security to safely manage our most advanced AI models.
Additionally, this multilayered approach to agent security should be a collaborative priority for industry, policymakers, and academia. By aligning the ecosystem around best practices and standards, we can empower cyber defenders and build societal resilience. That's why today we are also publishing a technical framework for policymakers, 'Three Layers of Agent Security'. The paper details how we need to improve security at the level of individual agents; in multi-agent systems; and to empower cyber defenders and build resilience across the broader ecosystem.
We intend to build on these frameworks to confidently deploy capable AI today while we continue to build a secure foundation for the future.
Read the full technical report here:
AI Control Roadmap
Research authors
Mary Phuong, Erik Jenner, Laurent Simon, Lewis Ho, Rohin Shah, Sebastian Farquhar, and Scott Coull.
Acknowledgements
Four Flynn, Anca Dragan, Alan Cooney, Bilal Chughtai, Buck Shlegeris, Cody Wild, David Lindner, Julian Stastny, Kevin Klyman, Li Ding, Myriam Khan, Raluca Ada Popa, Roland Zimmermann, Ryan Greenblatt, Senthooran Rajamanoharan, Victoria Krakovna and Xerxes Dotiwalla.
Follow us     
Sign up for updates on our latest innovations
I accept Google's Terms and Conditions and acknowledge that my information will be used in accordance with Google's Privacy Policy.
Sign up
Build AI responsibly to benefit humanity
Models
Gemini
Gemini Omni
Nano Banana
Gemini Audio
footer_gemma__lightfooter_gemma__dark Gemma
Genie
Lyria
Veo
Research
Gemini Robotics
Breakthroughs
Evals
Publications
Responsibility
Science
AlphaFold
AlphaGenome
WeatherNext
AlphaEarth
AlphaEvolve
Products
Gemini app
Google AI Studio
Google Antigravity
Learn more
About
News
Careers
National Partnerships for AI
Accelerator programs
The Podcast 
About Google
Google products
Privacy
Terms
Cookies management controls