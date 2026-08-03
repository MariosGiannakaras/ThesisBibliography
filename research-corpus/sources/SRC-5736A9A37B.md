# Belief–desire–intention software model - Wikipedia

- Jump to contentMain menu    Navigation

- Main page

- Contents

- Current events

- Random article

- About Wikipedia

- Contact us

- Contribute

- Help

- Learn to edit

- Community portal

- Recent changes

- Upload file

- Special pages

- Search  Donate

- Create account

- Log in

- Donate

- Create account

- Log in

- (Top)

- 1   Overview

- 2   BDI agents  2.1   Architecture

- 2.2   BDI interpreter

- 2.3   Limitations and criticisms

- 3   BDI agent implementations  3.1   'Pure' BDI

- 3.2   Extensions and hybrid systems

- 4   See also

- 5   References

- 6   Further reading

# Belief–desire–intention software model

- العربية

- Català

- Čeština

- Deutsch

- Français

- Italiano

- Русский

- Українська

- Edit links

- Tools    Actions

- Read

- Edit

- View history

- General

- What links here

- Related changes

- Upload file

- Permanent link

- Page information

- Cite this page

- Get shortened URL

- Download QR code

- Print/export

- Download as PDF

- Printable version

- In other projects

- Wikidata item

- From Wikipedia, the free encyclopedia   Model for designing artificial intelligence

- The **belief–desire–intention software model** (**BDI**) is a [software model](https://en.wikipedia.org/wiki/Modeling_language) developed for programming [intelligent agents](https://en.wikipedia.org/wiki/Intelligent_agent). Superficially characterized by the implementation of an agent's *beliefs*, *desires* and *intentions*, it actually uses these concepts to solve a particular problem in agent programming. In essence, it provides a mechanism for separating the activity of selecting a plan (from a plan [library](https://en.wikipedia.org/wiki/Library_(computing)) or an external planner application) from the execution of currently active plans. Consequently, BDI agents are able to balance the time spent on deliberating about plans (choosing what to do) and executing those plans (doing it). A third activity, creating the plans in the first place ([planning](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling)), is not within the scope of the model, and is left to the system designer and programmer.

## Overview

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=1)]

- In order to achieve this separation, the BDI software model implements the principal aspects of [Michael Bratman](https://en.wikipedia.org/wiki/Michael_Bratman)'s [theory of human practical reasoning](https://en.wikipedia.org/wiki/Belief-Desire-Intention_model) (also referred to as Belief-Desire-Intention, or BDI). That is to say, it implements the notions of belief, desire and (in particular) intention, in a manner inspired by Bratman.

- For Bratman, desire and intention are both pro-attitudes (mental attitudes concerned with action). He identifies commitment as the distinguishing factor between desire and intention, noting that it leads to (1) temporal persistence in plans and (2) further plans being made on the basis of those to which it is already committed. The BDI software model partially addresses these issues. Temporal persistence, in the sense of explicit reference to time, is not explored. The hierarchical nature of plans is more easily implemented: a plan consists of a number of steps, some of which may invoke other plans. The hierarchical definition of plans itself implies a kind of temporal persistence, since the overarching plan remains in effect while subsidiary plans are being executed.

- An important aspect of the BDI software model (in terms of its research relevance) is the existence of logical models through which it is possible to define and reason about BDI agents. Research in this area has led, for example, to the [axiomatization](https://en.wikipedia.org/wiki/Axiomatic_system) of some BDI implementations, as well as to [formal logical](https://en.wikipedia.org/wiki/Logic) descriptions such as Anand Rao and [Michael Georgeff](https://en.wikipedia.org/wiki/Michael_Georgeff)'s BDICTL. The latter combines a [multiple-modal logic](https://en.wikipedia.org/wiki/Modal_logic) (with modalities representing beliefs, desires and intentions) with the [temporal logic](https://en.wikipedia.org/wiki/Temporal_logic)[CTL*](https://en.wikipedia.org/wiki/Temporal_logic). More recently, Michael Wooldridge has extended BDICTL to define LORA (the Logic Of Rational Agents), by incorporating an action logic. In principle, LORA allows reasoning not only about individual agents, but also about communication and other interaction in a [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system).

- The BDI software model is closely associated with intelligent agents, but does not, of itself, ensure all the characteristics associated with such agents. For example, it allows agents to have private beliefs, but does not force them to be private. It also has nothing to say about agent communication. Ultimately, the BDI software model is an attempt to solve a problem that has more to do with plans and planning (the choice and execution thereof) than it has to do with the programming of intelligent agents. This approach has recently been proposed by [Steven Umbrello](https://en.wikipedia.org/w/index.php?title=Steven_Umbrello&action=edit&redlink=1) and [Roman Yampolskiy](https://en.wikipedia.org/wiki/Roman_Yampolskiy) as a means of designing [autonomous vehicles](https://en.wikipedia.org/wiki/Self-driving_car) for human values.[ 1 ]

## BDI agents

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=2)]

- A BDI agent is a particular type of [bounded](https://en.wikipedia.org/wiki/Bounded_rationality)[rational software agent](https://en.wikipedia.org/wiki/Bounded_rationality), imbued with particular *mental attitudes*, viz: Beliefs, Desires and Intentions (BDI).

### Architecture

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=3)]

- This section defines the idealized architectural components of a BDI system.

- **Beliefs**: Beliefs represent the informational state of the agent–its beliefs about the world (including itself and other agents). Beliefs can also include [inference rules](https://en.wikipedia.org/wiki/Inference_rule), allowing [forward chaining](https://en.wikipedia.org/wiki/Forward_chaining) to lead to new beliefs. Using the term *belief* rather than *knowledge* recognizes that what an agent believes may not necessarily be true (and in fact may change in the future).

- **Beliefset**: Beliefs are stored in [database](https://en.wikipedia.org/wiki/Database) (sometimes called a *belief base* or a *belief set*), although that is an [implementation](https://en.wikipedia.org/wiki/Implementation) decision.

- **Desires**: Desires represent the motivational state of the agent. They represent objectives or situations that the agent *would like* to accomplish or bring about. Examples of desires might be: *find the best price*, *go to the party* or *become rich*.

- **Goals**: A goal is a desire that has been adopted for active pursuit by the agent. Usage of the term *goals* adds the further restriction that the set of active desires must be consistent. For example, one should not have concurrent goals to go to a party and to stay at home – even though they could both be desirable.

- **Intentions**: Intentions represent the deliberative state of the agent – what the agent *has chosen* to do. Intentions are desires to which the agent has to some extent committed. In implemented systems, this means the agent has begun executing a plan.

- **Plans**: Plans are sequences of actions (recipes or knowledge areas) that an agent can perform to achieve one or more of its intentions. Plans may include other plans: my plan to go for a drive may include a plan to find my car keys. This reflects that in Bratman's model, plans are initially only partially conceived, with details being filled in as they progress.

- **Events**: These are triggers for reactive activity by the agent. An event may update beliefs, trigger plans or modify goals. Events may be generated externally and received by sensors or integrated systems. Additionally, events may be generated internally to trigger decoupled updates or plans of activity.

- BDI was also extended with an obligations component, giving rise to the BOID agent architecture[ 2 ] to incorporate obligations, norms and commitments of agents that act within a social environment.

### BDI interpreter

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=4)]

- This section defines an idealized BDI interpreter that provides the basis of SRI's [PRS](https://en.wikipedia.org/wiki/Procedural_reasoning_system) lineage of BDI systems:[ 3 ]

- initialize-state

- repeat

- options: option-generator (event-queue)

- selected-options: deliberate(options)

- update-intentions(selected-options)

- execute()

- get-new-external-events()

- drop-unsuccessful-attitudes()

- drop-impossible-attitudes()

- end repeat

### Limitations and criticisms

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=5)]

- The BDI software model is one example of a reasoning architecture for a single rational agent, and one concern in a broader [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system). This section bounds the scope of concerns for the BDI software model, highlighting known limitations of the architecture.

- **Learning**: BDI agents lack any specific mechanisms within the architecture to learn from past behavior and adapt to new situations.[ 4 ][ 5 ]

- **Three attitudes**: Classical [decision theorists](https://en.wikipedia.org/wiki/Decision_theory) and planning research questions the necessity of having all three attitudes, [distributed AI](https://en.wikipedia.org/wiki/Distributed_artificial_intelligence) research questions whether the three attitudes are sufficient.[ 3 ]

- **Logics**: The multi-modal logics that underlie BDI (that do not have complete axiomatizations and are not efficiently computable) have little relevance in practice.[ 3 ][ 6 ]

- **Multiple agents**: In addition to not explicitly supporting learning, the framework may not be appropriate to learning behavior. Further, the BDI model does not explicitly describe mechanisms for interaction with other agents and integration into a [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system).[ 7 ]

- **Explicit goals**: Most BDI implementations do not have an explicit representation of goals.[ 8 ]

- **Lookahead**: The architecture does not have (by design) any lookahead deliberation or forward planning. This may not be desirable because adopted plans may use up limited resources, actions may not be reversible, task execution may take longer than forward planning, and actions may have undesirable side effects if unsuccessful.[ 9 ]

## BDI agent implementations

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=6)]

### 'Pure' BDI

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=7)]

- [Procedural Reasoning System](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=7) (PRS)

- IRMA (not implemented but can be considered as PRS with non-reconsideration)

- UM-PRS[ 10 ]

- OpenPRS[ 11 ]

- Distributed Multi-Agent Reasoning System (dMARS)

- AgentSpeak(L) – see Jason below

- AgentSpeak(RT)[ 12 ][ 13 ]

- Agent Real-Time System (ARTS)[ 14 ] (ARTS)[ 15 ]

- JAM[ 16 ]

- JACK Intelligent Agents

- JADEX (open source project)[ 17 ]

- JaKtA[ 18 ]

- JASON[ 19 ]

- GORITE

- SPARK[ 20 ]

- 3APL

- 2APL[ 21 ]

- GOAL agent programming language

- CogniTAO (Think-As-One)[ 22 ][ 23 ]

- Living Systems Process Suite[ 24 ][ 25 ]

- PROFETA[ 26 ]

- Gwendolen[ 27 ] (Part of the Model Checking Agent Programming Languages Framework[ 28 ][ 29 ])

### Extensions and hybrid systems

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=8)]

- [JACK Teams](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=8)

- CogniTAO (Think-As-One)[ 22 ][ 23 ]

- Living Systems Process Suite[ 24 ][ 25 ]

- Brahms[ 30 ]

- JaCaMo[ 31 ]

## See also

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)]

- [Action selection](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Artificial intelligence](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Belief–desire–intention model](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Belief revision](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [GOLOG](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Intelligent agent](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Reasoning](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

- [Software agent](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)

## References

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=10)]

- [^](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=10)Umbrello, Steven; Yampolskiy, Roman V. (2021-05-15). ["Designing AI for Explainability and Verifiability: A Value Sensitive Design Approach to Avoid Artificial Stupidity in Autonomous Vehicles"](https://doi.org/10.1007%2Fs12369-021-00790-w). *International Journal of Social Robotics*. **14** (2):  313– 322. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s12369-021-00790-w](https://doi.org/10.1007%2Fs12369-021-00790-w). [hdl](https://en.wikipedia.org/wiki/Hdl_(identifier)):[2318/1788856](https://hdl.handle.net/2318%2F1788856). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier))[1875-4805](https://en.wikipedia.org/wiki/ISSN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISSN_(identifier)) J. Broersen, M. Dastani, J. Hulstijn, Z. Huang, L. van der Torre [The BOID architecture: conflicts between beliefs, obligations, intentions and desires](http://dl.acm.org/citation.cfm?id=375766) Proceedings of the fifth international conference on Autonomous agents, 2001, pages 9-16, ACM New York, NY, USA

- ^ **a****b****c**Rao, M. P. Georgeff. (1995). ["BDI-agents: From Theory to Practice"](https://web.archive.org/web/20110604050051/https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf)(PDF) . *Proceedings of the First International Conference on Multiagent Systems (ICMAS'95)*. Archived from [the original](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf)(PDF)  on 2011-06-04 . Retrieved  2009-07-09 .

- [^](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf)Phung, Toan; Michael Winikoff; Lin Padgham (2005). "Learning Within the BDI Framework: An Empirical Analysis". *Knowledge-Based Intelligent Information and Engineering Systems*. Lecture Notes in Computer Science. Vol. 3683. pp.  282– 288. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/11553939_41](https://doi.org/10.1007%2F11553939_41). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[978-3-540-28896-1](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))Guerra-Hernández, Alejandro; Amal El Fallah-Seghrouchni; Henry Soldano (2004). "Learning in BDI Multi-agent Systems". *Computational Logic in Multi-Agent Systems*. Lecture Notes in Computer Science. Vol. 3259. pp.  218– 233. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-540-30200-1_12](https://doi.org/10.1007%2F978-3-540-30200-1_12). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[978-3-540-24010-5](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))Rao, M. P. Georgeff. (1995). "Formal models and decision procedures for multi-agent systems". *Technical Note, AAII*. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_(identifier))[10.1.1.52.7924](https://en.wikipedia.org/wiki/CiteSeerX_(identifier)).

- [^](https://en.wikipedia.org/wiki/CiteSeerX_(identifier))Georgeff, Michael; Barney Pell; [Martha E. Pollack](https://en.wikipedia.org/wiki/Martha_E._Pollack); Milind Tambe; Michael Wooldridge (1999). "The Belief-Desire-Intention Model of Agency". *Intelligent Agents V: Agents Theories, Architectures, and Languages*. Lecture Notes in Computer Science. Vol. 1555. pp.  1– 10. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/3-540-49057-4_1](https://doi.org/10.1007%2F3-540-49057-4_1). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[978-3-540-65713-2](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))Pokahr, Alexander; Lars Braubach; Winfried Lamersdorf (2005). "Jadex: A BDI Reasoning Engine". *Multi-Agent Programming*. Multiagent Systems, Artificial Societies, and Simulated Organizations. Vol. 15. pp.  149– 174. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/0-387-26350-0_6](https://doi.org/10.1007%2F0-387-26350-0_6). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[978-0-387-24568-3](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))Sardina, Sebastian; Lavindra de Silva; Lin Padgham (2006). ["Hierarchical planning in BDI agent programming languages: a formal approach"](http://portal.acm.org/citation.cfm?id=1160813). *Proceedings of the fifth international joint conference on Autonomous agents and multiagent systems*.

- ^UM-PRS

- ^"OpenPRS". Archived from [the original](http://homepages.laas.fr/felix/PRS) on 2014-10-21 . Retrieved  2014-10-23 .

- [^](http://homepages.laas.fr/felix/PRS)[AgentSpeak(RT)](http://homepages.laas.fr/felix/PRS)[Archived](http://homepages.laas.fr/felix/PRS) 2012-03-26 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)Vikhorev, K., Alechina, N. and Logan, B. (2011). ["Agent programming with priorities and deadlines"](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev11Agent.pdf)[Archived](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev11Agent.pdf) March 26, 2012, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). In Proceedings of the Tenth International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2011). Taipei, Taiwan. May 2011., pp. 397-404.

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)[Agent Real-Time System](https://en.wikipedia.org/wiki/Wayback_Machine)[Archived](https://en.wikipedia.org/wiki/Wayback_Machine) 2011-09-27 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)Vikhorev, K., Alechina, N. and Logan, B. (2009). ["The ARTS Real-Time Agent Architecture"](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev09ARTS.pdf)[Archived](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev09ARTS.pdf) March 26, 2012, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). Turin, Italy. September 2009. CEUR Workshop Proceedings Vol-494.

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)[JAM](https://en.wikipedia.org/wiki/Wayback_Machine)

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)[JADEX](https://en.wikipedia.org/wiki/Wayback_Machine)

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)Baiardi, Martina; Burattini, Samuele; Ciatto, Giovanni; Pianini, Danilo (2024). *Blending BDI Agents with Object-Oriented and Functional Programming with JaKtA*. *Sn Computer Science*. Vol. 5, art. 1003. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s42979-024-03244-y](https://doi.org/10.1007%2Fs42979-024-03244-y). [hdl](https://en.wikipedia.org/wiki/Hdl_(identifier)):[11585/998116](https://hdl.handle.net/11585%2F998116).

- [^](https://hdl.handle.net/11585%2F998116)["Jason | a Java-based interpreter for an extended version of AgentSpeak"](https://hdl.handle.net/11585%2F998116).

- [^](https://hdl.handle.net/11585%2F998116)[SPARK](https://hdl.handle.net/11585%2F998116)

- [^](https://hdl.handle.net/11585%2F998116)[2APL](https://hdl.handle.net/11585%2F998116)

- ^ **a****b**[CogniTAO (Think-As-One)](https://en.wikipedia.org#cite_ref-CogniTAO_Think-As-One_22-0)

- ^ **a****b**TAO: A JAUS-based High-Level Control System for Single and Multiple Robots Y. Elmaliach, CogniTeam, (2008) ["Archived copy"](https://web.archive.org/web/20090107071940/http://www.icr2008.org.il/program.html). Archived from [the original](http://www.icr2008.org.il/program.html) on 2009-01-07 . Retrieved  2008-11-03 . {{[cite web](https://en.wikipedia.org/wiki/Template:Cite_web)}} : CS1 maint: archived copy as title ([link](https://en.wikipedia.org/wiki/Category:CS1_maint:_archived_copy_as_title))

- ^ **a****b**[Living Systems Process Suite](https://en.wikipedia.org#cite_ref-Living_Systems_Process_Suite_24-0)

- ^ **a****b**Rimassa, G., Greenwood, D. and Kernland, M. E., (2006). [The Living Systems Technology Suite: An Autonomous Middleware for Autonomic Computing](http://www.whitestein.com/library/WhitesteinTechnologies_Paper_ICAS2006-gri.pdf)[Archived](http://www.whitestein.com/library/WhitesteinTechnologies_Paper_ICAS2006-gri.pdf) May 16, 2008, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). International Conference on Autonomic and Autonomous Systems (ICAS).

- [^](https://en.wikipedia.org/wiki/Wayback_Machine)Fichera, Loris; Marletta, Daniele; Nicosia, Vincenzo; Santoro, Corrado (2011). "Flexible Robot Strategy Design Using Belief-Desire-Intention Model". In Obdržálek, David; Gottscheber, Achim (eds.). *Research and Education in Robotics - EUROBOT 2010*. Communications in Computer and Information Science. Vol. 156. Berlin, Heidelberg: Springer. pp.  57– 71. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-642-27272-1_5](https://doi.org/10.1007%2F978-3-642-27272-1_5). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[978-3-642-27272-1](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))[Gwendolen Semantics:2017](https://en.wikipedia.org/wiki/ISBN_(identifier))

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))[Model Checking Agent Programming Languages](https://en.wikipedia.org/wiki/ISBN_(identifier))

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))[MCAPL (Zenodo)](https://en.wikipedia.org/wiki/ISBN_(identifier))

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))[Brahms](https://en.wikipedia.org/wiki/ISBN_(identifier))

- [^](https://en.wikipedia.org/wiki/ISBN_(identifier))["Home"](https://en.wikipedia.org/wiki/ISBN_(identifier)). *jacamo.sourceforge.net*.

## Further reading

- [[edit](https://en.wikipedia.org/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=11)]

- A. S. Rao and M. P. Georgeff. [Modeling Rational Agents within a BDI-Architecture](http://jmvidal.cse.sc.edu/lib/rao91a.html). In Proceedings of the 2nd International Conference on Principles of Knowledge Representation and Reasoning, pages 473–484, 1991.

- A. S. Rao and M. P. Georgeff. [BDI-agents: From Theory to Practice](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf)[Archived](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf) 2011-06-04 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), In Proceedings of the First International Conference on Multiagent Systems (ICMAS'95), San Francisco, 1995.

- Bratman, M. E. (1999) [1987]. *Intention, Plans, and Practical Reason*. [CSLI Publications](https://en.wikipedia.org/wiki/Center_for_the_Study_of_Language_and_Information). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[1-57586-192-5](https://en.wikipedia.org/wiki/ISBN_(identifier)).

- Wooldridge, M. (2000). *Reasoning About Rational Agents*. [The MIT Press](https://en.wikipedia.org/wiki/MIT_Press). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[0-262-23213-8](https://en.wikipedia.org/wiki/ISBN_(identifier)). Archived from [the original](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=3533) on 2010-07-30 . Retrieved  2006-06-15 .

- K. S. Vikhorev, N. Alechina, and B. Logan. [The ARTS Real-Time Agent Architecture](http://www.cs.nott.ac.uk/~nza/papers/Vikhorev++:09a.pdf). In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). CEUR Workshop Proceedings, Vol-494, Turin, Italy, 2009.

- Retrieved from "[https://en.wikipedia.org/w/index.php?title=Belief–desire–intention_software_model&oldid=1317126201](https://en.wikipedia.org/w/index.php?title=Belief–desire–intention_software_model&oldid=1317126201)"  [Categories](https://en.wikipedia.org/wiki/Help:Category):

- [Artificial intelligence engineering](https://en.wikipedia.org/wiki/Help:Category)

- [Belief revision](https://en.wikipedia.org/wiki/Help:Category)

- [Agent-based programming languages](https://en.wikipedia.org/wiki/Help:Category)

- Hidden categories:

- [Webarchive template wayback links](https://en.wikipedia.org/wiki/Help:Category)

- [CS1 maint: archived copy as title](https://en.wikipedia.org/wiki/Help:Category)

- [Articles with short description](https://en.wikipedia.org/wiki/Help:Category)

- [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Help:Category)