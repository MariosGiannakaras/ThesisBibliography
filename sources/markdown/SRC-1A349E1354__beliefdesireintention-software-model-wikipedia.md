> Source: https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model

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
1   Overview  
2   BDI agents  2.1   Architecture  
2.2   BDI interpreter  
2.3   Limitations and criticisms  
3   BDI agent implementations  3.1   'Pure' BDI  
3.2   Extensions and hybrid systems  
4   See also  
5   References  
6   Further reading  
Belief–desire–intention software model
العربية
Català
Čeština
Deutsch
Français
Italiano
Русский
Українська
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
Wikidata item
From Wikipedia, the free encyclopedia   Model for designing artificial intelligence  
The belief–desire–intention software model (BDI) is a software model developed for programming intelligent agents. Superficially characterized by the implementation of an agent's beliefs, desires and intentions, it actually uses these concepts to solve a particular problem in agent programming. In essence, it provides a mechanism for separating the activity of selecting a plan (from a plan library or an external planner application) from the execution of currently active plans. Consequently, BDI agents are able to balance the time spent on deliberating about plans (choosing what to do) and executing those plans (doing it). A third activity, creating the plans in the first place (planning), is not within the scope of the model, and is left to the system designer and programmer. 
Overview
[edit]  
In order to achieve this separation, the BDI software model implements the principal aspects of Michael Bratman's theory of human practical reasoning (also referred to as Belief-Desire-Intention, or BDI). That is to say, it implements the notions of belief, desire and (in particular) intention, in a manner inspired by Bratman. 
For Bratman, desire and intention are both pro-attitudes (mental attitudes concerned with action). He identifies commitment as the distinguishing factor between desire and intention, noting that it leads to (1) temporal persistence in plans and (2) further plans being made on the basis of those to which it is already committed. The BDI software model partially addresses these issues. Temporal persistence, in the sense of explicit reference to time, is not explored. The hierarchical nature of plans is more easily implemented: a plan consists of a number of steps, some of which may invoke other plans. The hierarchical definition of plans itself implies a kind of temporal persistence, since the overarching plan remains in effect while subsidiary plans are being executed. 
An important aspect of the BDI software model (in terms of its research relevance) is the existence of logical models through which it is possible to define and reason about BDI agents. Research in this area has led, for example, to the axiomatization of some BDI implementations, as well as to formal logical descriptions such as Anand Rao and Michael Georgeff's BDICTL. The latter combines a multiple-modal logic (with modalities representing beliefs, desires and intentions) with the temporal logicCTL*. More recently, Michael Wooldridge has extended BDICTL to define LORA (the Logic Of Rational Agents), by incorporating an action logic. In principle, LORA allows reasoning not only about individual agents, but also about communication and other interaction in a multi-agent system. 
The BDI software model is closely associated with intelligent agents, but does not, of itself, ensure all the characteristics associated with such agents. For example, it allows agents to have private beliefs, but does not force them to be private. It also has nothing to say about agent communication. Ultimately, the BDI software model is an attempt to solve a problem that has more to do with plans and planning (the choice and execution thereof) than it has to do with the programming of intelligent agents. This approach has recently been proposed by Steven Umbrello and Roman Yampolskiy as a means of designing autonomous vehicles for human values.[ 1 ]
BDI agents
[edit]  
A BDI agent is a particular type of boundedrational software agent, imbued with particular mental attitudes, viz: Beliefs, Desires and Intentions (BDI). 
Architecture
[edit]  
This section defines the idealized architectural components of a BDI system. 
Beliefs: Beliefs represent the informational state of the agent–its beliefs about the world (including itself and other agents). Beliefs can also include inference rules, allowing forward chaining to lead to new beliefs. Using the term belief rather than knowledge recognizes that what an agent believes may not necessarily be true (and in fact may change in the future). 
Beliefset: Beliefs are stored in database (sometimes called a belief base or a belief set), although that is an implementation decision.
Desires: Desires represent the motivational state of the agent. They represent objectives or situations that the agent would like to accomplish or bring about. Examples of desires might be: find the best price, go to the party or become rich. 
Goals: A goal is a desire that has been adopted for active pursuit by the agent. Usage of the term goals adds the further restriction that the set of active desires must be consistent. For example, one should not have concurrent goals to go to a party and to stay at home – even though they could both be desirable.
Intentions: Intentions represent the deliberative state of the agent – what the agent has chosen to do. Intentions are desires to which the agent has to some extent committed. In implemented systems, this means the agent has begun executing a plan. 
Plans: Plans are sequences of actions (recipes or knowledge areas) that an agent can perform to achieve one or more of its intentions. Plans may include other plans: my plan to go for a drive may include a plan to find my car keys. This reflects that in Bratman's model, plans are initially only partially conceived, with details being filled in as they progress.
Events: These are triggers for reactive activity by the agent. An event may update beliefs, trigger plans or modify goals. Events may be generated externally and received by sensors or integrated systems. Additionally, events may be generated internally to trigger decoupled updates or plans of activity.
BDI was also extended with an obligations component, giving rise to the BOID agent architecture[ 2 ] to incorporate obligations, norms and commitments of agents that act within a social environment. 
BDI interpreter
[edit]  
This section defines an idealized BDI interpreter that provides the basis of SRI's PRS lineage of BDI systems:[ 3 ]
initialize-state
repeat 
options: option-generator (event-queue)
selected-options: deliberate(options)
update-intentions(selected-options)
execute()
get-new-external-events()
drop-unsuccessful-attitudes()
drop-impossible-attitudes()
end repeat
Limitations and criticisms
[edit]  
The BDI software model is one example of a reasoning architecture for a single rational agent, and one concern in a broader multi-agent system. This section bounds the scope of concerns for the BDI software model, highlighting known limitations of the architecture. 
Learning: BDI agents lack any specific mechanisms within the architecture to learn from past behavior and adapt to new situations.[ 4 ][ 5 ]
Three attitudes: Classical decision theorists and planning research questions the necessity of having all three attitudes, distributed AI research questions whether the three attitudes are sufficient.[ 3 ]
Logics: The multi-modal logics that underlie BDI (that do not have complete axiomatizations and are not efficiently computable) have little relevance in practice.[ 3 ][ 6 ]
Multiple agents: In addition to not explicitly supporting learning, the framework may not be appropriate to learning behavior. Further, the BDI model does not explicitly describe mechanisms for interaction with other agents and integration into a multi-agent system.[ 7 ]
Explicit goals: Most BDI implementations do not have an explicit representation of goals.[ 8 ]
Lookahead: The architecture does not have (by design) any lookahead deliberation or forward planning. This may not be desirable because adopted plans may use up limited resources, actions may not be reversible, task execution may take longer than forward planning, and actions may have undesirable side effects if unsuccessful.[ 9 ]
BDI agent implementations
[edit]  
'Pure' BDI
[edit]  
Procedural Reasoning System (PRS)
IRMA (not implemented but can be considered as PRS with non-reconsideration)
UM-PRS[ 10 ]
OpenPRS[ 11 ]
Distributed Multi-Agent Reasoning System (dMARS)
AgentSpeak(L) – see Jason below
AgentSpeak(RT)[ 12 ][ 13 ]
Agent Real-Time System (ARTS)[ 14 ] (ARTS)[ 15 ]
JAM[ 16 ]
JACK Intelligent Agents
JADEX (open source project)[ 17 ]
JaKtA[ 18 ]
JASON[ 19 ]
GORITE
SPARK[ 20 ]
3APL
2APL[ 21 ]
GOAL agent programming language
CogniTAO (Think-As-One)[ 22 ][ 23 ]
Living Systems Process Suite[ 24 ][ 25 ]
PROFETA[ 26 ]
Gwendolen[ 27 ] (Part of the Model Checking Agent Programming Languages Framework[ 28 ][ 29 ])
Extensions and hybrid systems
[edit]  
JACK Teams
CogniTAO (Think-As-One)[ 22 ][ 23 ]
Living Systems Process Suite[ 24 ][ 25 ]
Brahms[ 30 ]
JaCaMo[ 31 ]
See also
[edit]  
Action selection
Artificial intelligence
Belief–desire–intention model
Belief revision
GOLOG
Intelligent agent
Reasoning
Software agent
References
[edit]  
^Umbrello, Steven; Yampolskiy, Roman V. (2021-05-15). "Designing AI for Explainability and Verifiability: A Value Sensitive Design Approach to Avoid Artificial Stupidity in Autonomous Vehicles". International Journal of Social Robotics. 14 (2):  313– 322. doi:10.1007/s12369-021-00790-w. hdl:2318/1788856. ISSN1875-4805.  
^ J. Broersen, M. Dastani, J. Hulstijn, Z. Huang, L. van der Torre The BOID architecture: conflicts between beliefs, obligations, intentions and desires Proceedings of the fifth international conference on Autonomous agents, 2001, pages 9-16, ACM New York, NY, USA  
^ abcRao, M. P. Georgeff. (1995). "BDI-agents: From Theory to Practice"(PDF) . Proceedings of the First International Conference on Multiagent Systems (ICMAS'95). Archived from the original(PDF)  on 2011-06-04 . Retrieved  2009-07-09 .  
^Phung, Toan; Michael Winikoff; Lin Padgham (2005). "Learning Within the BDI Framework: An Empirical Analysis". Knowledge-Based Intelligent Information and Engineering Systems. Lecture Notes in Computer Science. Vol. 3683. pp.  282– 288. doi:10.1007/11553939_41. ISBN978-3-540-28896-1.  
^Guerra-Hernández, Alejandro; Amal El Fallah-Seghrouchni; Henry Soldano (2004). "Learning in BDI Multi-agent Systems". Computational Logic in Multi-Agent Systems. Lecture Notes in Computer Science. Vol. 3259. pp.  218– 233. doi:10.1007/978-3-540-30200-1_12. ISBN978-3-540-24010-5.  
^Rao, M. P. Georgeff. (1995). "Formal models and decision procedures for multi-agent systems". Technical Note, AAII. CiteSeerX10.1.1.52.7924.  
^Georgeff, Michael; Barney Pell; Martha E. Pollack; Milind Tambe; Michael Wooldridge (1999). "The Belief-Desire-Intention Model of Agency". Intelligent Agents V: Agents Theories, Architectures, and Languages. Lecture Notes in Computer Science. Vol. 1555. pp.  1– 10. doi:10.1007/3-540-49057-4_1. ISBN978-3-540-65713-2.  
^Pokahr, Alexander; Lars Braubach; Winfried Lamersdorf (2005). "Jadex: A BDI Reasoning Engine". Multi-Agent Programming. Multiagent Systems, Artificial Societies, and Simulated Organizations. Vol. 15. pp.  149– 174. doi:10.1007/0-387-26350-0_6. ISBN978-0-387-24568-3.  
^Sardina, Sebastian; Lavindra de Silva; Lin Padgham (2006). "Hierarchical planning in BDI agent programming languages: a formal approach". Proceedings of the fifth international joint conference on Autonomous agents and multiagent systems.  
^UM-PRS
^"OpenPRS". Archived from the original on 2014-10-21 . Retrieved  2014-10-23 .  
^AgentSpeak(RT)Archived 2012-03-26 at the Wayback Machine
^Vikhorev, K., Alechina, N. and Logan, B. (2011). "Agent programming with priorities and deadlines"Archived March 26, 2012, at the Wayback Machine. In Proceedings of the Tenth International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2011). Taipei, Taiwan. May 2011., pp. 397-404.  
^Agent Real-Time SystemArchived 2011-09-27 at the Wayback Machine
^Vikhorev, K., Alechina, N. and Logan, B. (2009). "The ARTS Real-Time Agent Architecture"Archived March 26, 2012, at the Wayback Machine. In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). Turin, Italy. September 2009. CEUR Workshop Proceedings Vol-494.  
^JAM
^JADEX
^Baiardi, Martina; Burattini, Samuele; Ciatto, Giovanni; Pianini, Danilo (2024). Blending BDI Agents with Object-Oriented and Functional Programming with JaKtA. Sn Computer Science. Vol. 5, art. 1003. doi:10.1007/s42979-024-03244-y. hdl:11585/998116.  
^"Jason | a Java-based interpreter for an extended version of AgentSpeak".  
^SPARK
^2APL
^ abCogniTAO (Think-As-One)
^ abTAO: A JAUS-based High-Level Control System for Single and Multiple Robots Y. Elmaliach, CogniTeam, (2008) "Archived copy". Archived from the original on 2009-01-07 . Retrieved  2008-11-03 . {{cite web}} : CS1 maint: archived copy as title (link)  
^ abLiving Systems Process Suite
^ abRimassa, G., Greenwood, D. and Kernland, M. E., (2006). The Living Systems Technology Suite: An Autonomous Middleware for Autonomic ComputingArchived May 16, 2008, at the Wayback Machine. International Conference on Autonomic and Autonomous Systems (ICAS).  
^Fichera, Loris; Marletta, Daniele; Nicosia, Vincenzo; Santoro, Corrado (2011). "Flexible Robot Strategy Design Using Belief-Desire-Intention Model". In Obdržálek, David; Gottscheber, Achim (eds.). Research and Education in Robotics - EUROBOT 2010. Communications in Computer and Information Science. Vol. 156. Berlin, Heidelberg: Springer. pp.  57– 71. doi:10.1007/978-3-642-27272-1_5. ISBN978-3-642-27272-1.  
^Gwendolen Semantics:2017
^Model Checking Agent Programming Languages
^MCAPL (Zenodo)
^Brahms
^"Home". jacamo.sourceforge.net.  
Further reading
[edit]  
A. S. Rao and M. P. Georgeff. Modeling Rational Agents within a BDI-Architecture. In Proceedings of the 2nd International Conference on Principles of Knowledge Representation and Reasoning, pages 473–484, 1991.
A. S. Rao and M. P. Georgeff. BDI-agents: From Theory to PracticeArchived 2011-06-04 at the Wayback Machine, In Proceedings of the First International Conference on Multiagent Systems (ICMAS'95), San Francisco, 1995.
Bratman, M. E. (1999) [1987]. Intention, Plans, and Practical Reason. CSLI Publications. ISBN1-57586-192-5.
Wooldridge, M. (2000). Reasoning About Rational Agents. The MIT Press. ISBN0-262-23213-8. Archived from the original on 2010-07-30 . Retrieved  2006-06-15 .
K. S. Vikhorev, N. Alechina, and B. Logan. The ARTS Real-Time Agent Architecture. In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). CEUR Workshop Proceedings, Vol-494, Turin, Italy, 2009.
Retrieved from "https://en.wikipedia.org/w/index.php?title=Belief–desire–intention_software_model&oldid=1317126201"  Categories: 
Artificial intelligence engineering
Belief revision
Agent-based programming languages
Hidden categories: 
Webarchive template wayback links
CS1 maint: archived copy as title
Articles with short description
Short description is different from Wikidata