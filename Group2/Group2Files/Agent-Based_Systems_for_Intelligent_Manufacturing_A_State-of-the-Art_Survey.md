# Agent-Based Systems for Intelligent Manufacturing: A State-of-the-Art Survey

### Agent-Based Systems for Intelligent Manufacturing: A State-of-the-Art Survey

(Note: It is an extended HTML version of the paper published in KAIS: "Shen, W. and Norrie, D.H. Agent-Based Systems for Intelligent Manufacturing: A State-of-the-Art Survey. Knowledge and Information Systems, an International Journal, 1(2), 129-156, 1999. Its extended HTML version is available at: http://imsg.enme.ucalgary.ca/publication/abm.htm") 

  Weiming Shen and Douglas H. Norrie 

Division of Manufacturing Engineering, The University of Calgary 2500 University Dr. NW, Calgary, Alberta, Canada, T2N 1N4 

E-mail: wshen@ieee.org, norrie@enme.ucalgary.ca URL: http://imsg.enme.ucalgary.ca/ 

Abstract 

Agent technology has been considered as an important approach for developing distributed intelligent manufacturing systems. A number of researchers have attempted to apply agent technology to manufacturing enterprise integration, supply chain management, manufacturing planning, scheduling and control, materials handling, and holonic manufacturing systems. This paper gives a brief survey of some related projects in this area, and discusses some key issues in developing agent-based manufacturing systems such as agent technology for enterprise integration and supply chain management, agent encapsulation, system architectures, dynamic system reconfiguration, learning, design and manufacturability assessments, distributed dynamic scheduling, integration of planning and scheduling, concurrent scheduling and execution, factory control structures, potential tools and standards for developing agent-based manufacturing systems. An extensive annotated bibliography is provided. 

1. Introduction 2. Overview 

2.1 Requirements for Next Generation Manufacturing Systems 2.2 Agent-Based Approaches for Intelligent Manufacturing 2.3 Agents, Autonomous Agents and Agent-Based Systems 

3. Agent-Based Systems for Intelligent Manufacturing 3.1 Enterprise Integration and Supply Chain Management Table 1. Summary of projects using agent technology for enterprise integration and supply chain management 3.2 Manufacturing Planning, Scheduling and Control Table 2. Summary of projects using agent technology for manufacturing planning, scheduling and control 3.3 Holonic Manufacturing Systems (HMS) 

4. Key Issues in Developing Agent-Based Manufacturing Systems 4.1 Agent Technology for Enterprise Integration and Supply Chain Management 4.2 Agent Encapsulation 

4.3 Multi-Agent Organization - System Architectures 4.4 Dynamic System Reconfiguration 4.5 Learning in Agent-Based Manufacturing Systems 4.6 Design and manufacturability assessments 4.7 Distributed Dynamic Scheduling 4.8 Planning, Scheduling and Execution 4.9 Factory Control Architectures 4.10 Tools and Standards 

References 

1. Introduction 

Global competition and rapidly changing customer requirements are forcing major changes in the production styles and configuration of manufacturing organizations. Increasingly, traditional centralized and sequential manufacturing planning, scheduling, and control mechanisms are being found insufficiently flexible to respond to changing production styles and highly dynamic variations in product requirements. The traditional approaches limit the expandability and reconfiguration capabilities of the manufacturing systems. The traditional centralized hierarchical organization may also result in much of the system being shut down by a single point of failure, as well as plan fragility and increased response overheads. Agent technology provides a natural way to overcome such problems, and to design and implement distributed intelligent manufacturing environments. 

Recently, agent technology has been considered as an important approach for developing industrial distributed systems (Jennings et al 1995; Jennings and Wooldridge 1998). A number of researchers have attempted to apply agent technology to manufacturing enterprise integration, supply chain management, manufacturing planning, scheduling and control, materials handling, and holonic manufacturing systems. In this paper, we give a brief survey of some related projects in this area (Section 3), and discuss some key issues in developing agent-based manufacturing systems (Section 4). An extensive annotated bibliography is provided. Note that we only selected research projects related to agent-based manufacturing. 

A review of agent theories, architectures and languages can be found in (Wooldridge and Jennings 1995). A survey of cooperative environments for engineering design can be found in (Shen and Barthès 1996b), a review of some simultaneous engineering systems in (Molina et al 1995), and a taxonomy for multi-agent robotics in (Jenkin et al 1996). 

2. Overview 

2.1 Requirements for Next Generation Manufacturing Systems 

The manufacturing enterprises of the 21st century will be in an environment where markets are frequently shifting, new technologies are continuously emerging, and competitors are multiplying globally. Manufacturing strategies should therefore shift to support global competitiveness, new product innovation and introduction, and rapid market responsiveness. The next generation manufacturing systems will thus be more strongly time-oriented, while still focusing on cost and quality. Such

manufacturing systems will need to satisfy the following fundamental requirements: 

Enterprise Integration: In order to support global competitiveness and rapid market responsiveness, an individual or collective manufacturing enterprise will have to be integrated with its related management systems (e.g., purchasing, orders, design, production, planning & scheduling, control, transport, resources, personnel, materials, quality, etc.) and its partners via networks. Distributed Organization: For effective enterprise integration across distributed organizations, distributed knowledge-based systems will be needed so as to link demand management directly to resource and capacity planning and scheduling. Heterogeneous Environments: Such manufacturing systems will need to accommodate heterogeneous software and hardware in both their manufacturing and information environments. Interoperability: Heterogeneous information environments may use different programming languages, represent data with different representation languages and models, and operate in different computing platforms. The sub-systems and components in such heterogeneous environments should interoperate in an efficient manner. Translation and other capabilities will be needed to enable such interoperation or interaction. Open and Dynamic Structure: It must be possible to dynamically integrate new subsystems (software, hardware, or manufacturing devices) into or remove existing subsystems from the system without stopping and reinitializing the working environment. This will require an open and dynamic system architecture. Cooperation: Manufacturing enterprises will have to fully cooperate with their suppliers, partners, and customers for material supply, parts fabrication, final product commercialization, and so on. Such cooperation should be in an efficient and quick-response manner. Integration of humans with software and hardware: P ople and computers need to be integrated to work collectively at various stages of the product development and even the whole product life cycle, with rapid access to required knowledge and information. Heterogeneous sources of information must be integrated to support these needs and to enhance the decision capabilities of the system. Bi-directional communication environments are required to allow effective, quick communication between human and computers to facilitate their interaction. Agility: Considerable attention must be given to reducing product cycle time to be able to respond to customer desires more quickly. Agile manufacturing is the ability to adapt quickly in a manufacturing environment of continuous and unanticipated change and thus is a key component in manufacturing strategies for global competition. To achieve agility, manufacturing facilities must be able to rapidly reconfigure and interact with heterogeneous systems and partners. Ideally, partners are contracted with "on the fly" only for the time required to complete specific tasks. Scalability: Scalability means that additional resources can be incorporated into the organization as required. This capability should be available at any working node in the system and at any level within the nodes. Expansion of resources should be possible without disrupting organizational links previously established. Fault Tolerance: The system should be fault tolerant both at the system level and at the subsystem level so as to detect and recover from system failures at any level and minimize their impacts on the working environment. 

2.2 Agent-Based Approaches for Intelligent Manufacturing 

Techniques from Artificial Intelligence (AI) have already been used in Intelligent Manufacturing for more than twenty years. However, the recent developments in multi-agent systems in the new domain of

Distributed Artificial Intelligence (DAI) have brought new and interesting possibilities. Thus, in the past ten years, researchers have been applying agent technology to manufacturing enterprise integration and supply chain management, manufacturing planning, scheduling and execution control, materials handling and inventory management, and developing new types of manufacturing systems such as holonic manufacturing systems. 

In distributed intelligent manufacturing systems, agents can be used to 

encapsulate existing software systems so as to resolve legacy problems and integrate manufacturing enterprises’ activities such as design, planning, scheduling, simulation, execution, and product distribution, with those of their suppliers, customers and partners into an open, distributed intelligent environment via networks (Fox et al 1993; Barbuceanu and Fox 1997; Peng et al 1998; Shen et al 1998a); represent manufacturing resources such as workers, cells, machines, tools, fixtures, AGVs, as well as products, parts, operations (Butler and Ohtsubo 1992; Parunak et al 1998; Shen and Norrie 1998) to facilitate manufacturing resource planning, scheduling and execution control; model special services in manufacturing systems, such as: Agent Name Server in CIIMPLEX (Peng et al 1998) and Enterprise Mediator in MetaMorph (Maturana and Norrie 1996; Shen et al 1998a) for providing registration and administration services; Facilitator agents (also called Facilitators) in PACT (Cutkosky et al 1993) and CIIMPLEX (Peng et al 1998) and Mediator Agents (also called Mediators) in MetaMorph for facilitating communication, cooperation and coordination among other agents; Database Agents (Lin and Solberg 1992) and Information Agents (Fox et al 1993; McEleney et al 1998) for providing information management; and incorporate a whole scheduler or planner into manufacturing planning and scheduling systems (Fox et al 1993; McEleney et al 1998). 

In holonic manufacturing systems, agents are used to model holons which are software and hardware entities (Deen 1994; Christensen et al 1994; Hasegawa et al 1994; Biswas et al 1995). A good discussion on agent technology for holonic manufacturing systems can be found in (Bussmann 1998). We introduce the main concepts of the holonic manufacturing systems and review some projects in this area later in Section 3.3. 

2.3 Agents, Autonomous Agents and Agent-Based Systems 

For the notion of agent and autonomy used in this paper, we employ Jennings and Wooldridge’s definition (Jennings and Wooldridge 1998): "an agent is a computer system situated in some environment, and that is capable of autonomous action in this environment in order to meet its design objectives." An autonomous agent should be able to act without the direct intervention of humans or other agents, and should have control over its own actions and internal state. And an "agent based system" means one in which the key abstraction used is that of an agent. 

3. Agent-Based Systems for Intelligent Manufacturing 

In this section we review some related projects, in a tabular format, giving for each project where available: its name, research group (in reference citation format), application domain(s) and main characteristics. The projects are classified in three categories: (i) Enterprise Integration and Supply Chain Management, (ii) Manufacturing Planning, Scheduling and Control, and (iii) Holonic Manufacturing Systems. 

3.1 Enterprise Integration and Supply Chain Management 

Enterprise Integration means that each unit of the organization will have access to information relevant to its task and will understand how its actions will impact other parts of the organization thereby enabling it to choose alternatives that optimize the organization’s goals. The supply chain of a manufacturing enterprise is a world-wide network of suppliers, factories, warehouses, distribution centers and retailers through which raw materials are acquired, transformed and delivered to customers (Fox et al 1993). Improving supply chain management is a key strategy for increasing the enterprise’s competitive position and profitability. Consequently, enterprises are moving towards open architectures for integrating their activities with those of their suppliers, customers and partners within wide supply chain networks. Agent-based technology provides a natural way to design and implement such environments. Table 1 summarizes some projects in this area. 

Table 1. Summary of projects using agent technology for enterprise integration and supply chain management 

Project Group Domain Main characteristics 

ABMA Budenske et al 1998 Architecture Tech. Co. 

Enterprise Integration Middleware architecture 

ADE Mehra & Nissen 1998 

Gensym Co. 

Supply Chain Management 

Using delegation based event handling similar to JavaBeans 

AIMS Park et al 1993 

Lockheed Martin 

Agile Manufacturing Using the Internet 

ATP Nist 1998 

NIST 

Agile Manufacturing Plug-and-play framework 

CIIMPLEX Peng et al 1998 

UMBC 

Enterprise Integration Service agents (Name Server, Facilitator Agent, Gateway 

Agent) 

CLAIM Malkoun & Kendall 1997 

RMIT 

Enterprise Integration Methodology for Enterprise Integration using agents 

IA framework Pan & Tenenbaum 1991 

EIT 

Enterprise Integration Large number of computerized assistants, known as Intelligent 

Agents (IAs) 

IAO Kwok and Norrie 1994 

U. of Calgary 

Intelligent Manufacturing 

A rule based object system for developing intelligent 

manufacturing software 

iDCSS Klein 1995 

CSS, MIT Concurrent Engineering 

A integrated model that combines 

existingcoordination technologie

ISCM Fox et al 1993 

U. of Toronto 

Supply Chain Management 

Agent Building Shell (ABS); Coordination Language (COOL); 

functional agents 

KRAFT Gray et al 1998 

KRAFT consortium 

Transformation and Reuse of Knowledge 

Mediators as knowledge brokers 

Madefast Cutkosky et al 1996 

Stanford 

Collaborative Engineering 

Using the Internet 

MADEsmart Jha et al 1998 

Boeing 

Collaborative Engineering 

Wrapper agents for legacy system encapsulation 

MetaMorph I Maturana & Norrie 1996 

U of Calgary 

Intelligent Manufacturing 

Mediator-centric architecture; dynamic clustering & cloning; 

learning 

MetaMorph II Shen et al 1998a 

U of Calgary 

Intelligent Manufacturing, Supply 

Chain Management 

Hybrid architecture; Mediators as subsystem coordinators and 

interfaces to the main system 

? Brugali et al 1998 

Politecnico di Torino 

Supply Chain Management 

Using mobile agents to an industrial process 

? Fleury et al 1996 Manufacturing System Optimization 

’Triple coupling’ of multi-agent techniques, simulated annealing, 

and simulation 

? Papaioannou & Edwards 1998 

Loughborough 

Virtual Enterprise Using mobile agents 

? Pancerella et al 1995 

Sandia Lab 

Agile Manufacturing An agent defined as an autonomous, encapsulated 

software component 

? Swaminathan et al 1996 

CMU 

Supply Chain Management 

Supply chain library with structural elements (agents) and 

control elements for coordination 

? Wunderli et al 1996 

ETH Zentrum 

CIM Systems Database agents for CIM systems 

? Yan et al 1998 

Leipzig 

Project Management Using mobile agents 

? No project name found through available publications. 

3.2 Manufacturing Planning, Scheduling and Control

Planning is the process of selecting and sequencing activities such that they achieve one or more goals and satisfy a set of domain constraints. Scheduling is the process of selecting among alternative plans and assigning resources and times to the set of activities in the plan. These assignments must obey a set of rules or constraints that reflect the temporal relationships between activities and the capacity limitations of a set of shared resources. The assignments also affect the optimality of a schedule with respect to criteria such as cost, tardiness, or throughput. In summary, scheduling is an optimization process where limited resources are allocated over time among both parallel and sequential activities (Zweben and Fox 1994). 

Manufacturing scheduling is a difficult problem, particularly when it takes place in an open, dynamic environment. In a manufacturing system, rarely do things go as expected. The set of things to do is generally dynamic. The system may be asked to do additional tasks that were not anticipated, and sometimes is allowed to omit certain tasks. The resources available to perform tasks are subject to change. Certain resources can become unavailable, and additional resources introduced. The beginning time and the processing time of a task are also subject to variation. A task can take more time than anticipated or less time than anticipated, and tasks can arrive early or late. Because of its highly combinatorial aspects, its dynamic nature and its practical interest for manufacturing systems, the scheduling problem has been widely studied in the literature by various methods: heuristics, constraint propagation techniques, constraint satisfaction problem formalism, simulated annealing, Taboo search, genetic algorithms, neural networks, etc. Agent technology has recently been used in attempts to resolve this problem. 

Manufacturing control relates to strategies and algorithms for operating a manufacturing plant, taking into account both the present and past observed states of the manufacturing plant, as well as the demand from the market. The manufacturing control problem can be considered at two levels: low- and high-level. At the low-level, the individual manufacturing resources are to be controlled to deliver unit-processes expected by the high-level control functions. High-level manufacturing control is concerned with coordinating the available manufacturing resources to make the desired numbers of types of products. In agent-based manufacturing systems, agent technology is usually applied to high-level manufacturing control, but can also be applied at the lower level (Brennan et al 1997; Wang et al 1998). 

Shaw may have been the first to propose using agents in manufacturing scheduling and factory control. He proposed that a manufacturing cell could subcontract work to other cells through a bidding mechanism (Shaw and Whinston 1983; Shaw 1988). YAMS (Yet Another Manufacturing System) (Parunak 1987) was another of the earliest agent-based manufacturing systems, wherein each factory and factory component is represented as an agent. Each agent has a collection of plans, representing its capabilities. The Contact Net is used for inter-agent negotiation. 

During this survey’s literature research, we found some 30 projects using agent technology for manufacturing planning, scheduling and execution control. Table 2 presents a summary of these projects. 

Table 2. Summary of projects using agent technology for manufacturing planning, scheduling and control 

Project Group Domain Main characteristics

AARIA Parunak et al 1998 

ITI, U of Cincinnati 

Manufacturing Scheduling & Control 

Using autonomous agents to represent physical entities, processes and operations 

ABACUS McEleney et al 1998 

UCB, UMIST 

Manufacturing Scheduling 

Using functional agents; BDI approach for agent design 

ADDYMS Butler & Ohtsubo 1992 Manufacturing Scheduling 

Agents represent physical resources; dynamic local resource 

scheduling 

AMACOIA Sprumont & Muller 1996 

U. of Neuchatel 

Flexible assembly lines design 

Using simulated annealing to search problem space 

AMC Goldsmith & Interrrante 1998 

Sandia Lab 

Manufacturing Scheduling 

Using physical agents: part agents and machine agents 

ARMOSE Overgaard et al 1994 

Odense U. 

Robotics Each joint of a robot is modeled as an agent 

CAMPS Miyashita 1998 Manufacturing Planning, Scheduling 

Repair-based methodology together with constraint-based 

mechanism 

CORTES Sadeh & Fox 1989, Sycara et al 1991 

CMU 

Manufacturing Scheduling 

Micro-opportunistic techniques for solving scheduling problems 

DAS Burke & Prosser 1991 

U. of Strathclyde 

Manufacturing Scheduling 

Hierarchical architecture with agents representing resources, resource groups, and a whole 

scheduling process 

I-Control Brennan et al 1997, Wang et al 1998, 

U of Calgary 

Manufacturing system control 

Partial Dynamic Control Hierarchy (PDCH); Using agents to model IEC-1499 Functional 

Blocks (IEC 1997) 

IFCF Lin and Solberg 1992 

Purdue 

Manufacturing Scheduling & Control 

Resource agents represent physical resources; market-like 

control model 

LMS Fordyce & Sullivan 1994 Manufacturing Scheduling 

Using functional agents; voting protocol for communication 

MAPP Hayes 1998 

U. of Minnesota 

Process Planning Combination of sequential and blackboard architectures

MASCADA 

Bruckner et al 1998 

Daimler-Benz AG, KULeuven 

Manufacturing Scheduling & Control 

Emergent Behavior in Manufacturing Control; Proactive 

Disturbance Handling; Hot Plugable Agents 

MASCOT Parunak 1993 

ITI 

Manufacturing Scheduling & Control 

A shared ontology & a base set of realistic modules 

Reagere Berry & Kumura 1998 

Penn State U. 

Manufacturing Scheduling & Control 

Based on blackboard architecture 

Sensible Agents 

Barber et al 1998 

U of Texas at Austin 

Manufacturing Scheduling 

Implemented as CORBA objects communicating through ILU 

object environment 

SFA Parunak 1996 

NCMS 

Manufacturing Scheduling & Control 

Real manufacturing applications 

YAMS Parunak 1987 

ITI 

Manufacturing Scheduling & Control 

One of earliest applications in the domain 

? Baker 1991 

U. of Cincinnati 

Manufacturing Scheduling & Control 

Market-Driven Contract Net; forward & backward scheduling 

? Choi and Park 1997 Shop Floor Scheduling of Shipbuilding Yard 

An economical method for developing intelligent agent 

systems 

? Duffie & Piper 1986 

Wisconsin 

Manufacturing Scheduling & Control 

Agents represent physical resources, parts, and humans; 

part-oriented scheduling 

? Fischer 1994 

DFKI 

Manufacturing Planning & Control 

Hierarchical layered architecture 

? Hasegawa et al 1994 

Toshiba 

Manufacturing Planning, Scheduling 

Using HMS approach 

? Interrante & Goldsmith 1998 

Sandia Lab 

Manufacturing Scheduling & Control 

Type-A, Type-B and Type-C agents 

? Saad et al 1995 

Vanderbilt 

Manufacturing Scheduling & Control 

Production Reservation approach; machine-centered & part-centered 

negotiation 

? Kouiss et al 1997 Manufacturing Scheduling 

Each agent represents a work center

? Liu & Sycara 1994, 1995 

CMU 

Job Shop Constraint Satisfaction & Optimization 

CP&CR (Constraint Partition and Coordinated Reaction) for 

constraint satisfaction; Anchor&Ascend for distributed 

constraint optimization 

? Murthy et al 1997 Manufacturing Scheduling 

A-team architecture 

? Ouelhadj et al 1998 

U. of Toulouse 1 

Manufacturing Scheduling & Control 

Agents represent physical resources 

? Patriti et al 1997, Schaefer et al 1996 

CRAN GGP 

Manufacturing Scheduling & Control 

Layered architecture; using different mechanisms at different 

levels 

? Sousa & Ramos 1997 

ISEP/IPP 

Manufacturing Scheduling 

Using HMS approach; dynamic scheduling 

? Tseng et al 1997 

HKUST 

Manufacturing Scheduling & Control 

Market-like model for manufacturing control with agents 

representing resources 

? No project name found through available publications. 

3.3 Holonic Manufacturing Systems (HMS) 

The HMS concept was proposed in 1994 by the HMS consortium as a test case under the international Intelligent Manufacturing Systems (IMS) Research Program (Hayashi 1993). "Holon" is a word coined by combining ’holos’ (the whole) and ’on’ (a particle) following Koestler (1967). A holon is defined by the HMS consortium as "an autonomous and cooperative building block of a manufacturing system for transforming, transporting, storing and/or validating information and physical objects" (Van Leeuwen and Norrie 1997). Another important concept is the "holarchy" which is defined as "a system of holons which can cooperate to achieve a goal or objective". A Holonic Manufacturing System (HMS) is "a holarchy which integrates the entire range of manufacturing activities from order booking through design, production and marketing to realize the agile manufacturing enterprise". An HMS is therefore a manufacturing system where key elements, such as raw materials, machines, products, parts, AGVs, etc., have autonomous and cooperative properties (Christensen 1994; Deen 1994). In an HMS, each holon’s activities are determined through cooperation with other holons, as opposed to being determined by a centralized mechanism. In this type of systems, intelligent agents called ’holons’ have a physical part as well as a software part. A holon can be part of another holon. 

With the same concepts and similar system architecture, the partners of HMS consortium have developed their own testbeds using their existing software and hardware environments. Most of the research results on HMS are reported only internally in the HMS consortium. However, some results have been published, for materials handling (Christensen et al 1994), manufacturing planning and scheduling (Hasegawa et al 1994; Biswas et al 1995; Sousa and Ramos 1997), and intelligent manufacturing control (Brennan et al 1997; Wang et al 1998).

4. Key Issues in Developing Agent-Based Manufacturing Systems 

Key issues related to agent-based cooperative systems, such as representation, ontology management, agent structure, system architecture, communications, system dynamics, overall system control, conflict resolution, legacy problems and external interfaces, have been discussed in (Shen and Barthès 1996b). Most of these issues are also applicable in agent-based manufacturing systems. In this section, we discuss those key issues especially related to agent-based manufacturing, such as agent technology for enterprise integration and supply chain management, agent encapsulation, system architectures, dynamic system reconfiguration, learning, design and manufacturability assessments, distributed dynamic scheduling, integration of planning and scheduling, concurrent scheduling and execution, factory control architectures, tools and standards for developing agent-based manufacturing systems, based on our experience and an analysis of the research projects summarized in Section 3. 

Most of those issues are also applicable in agent-based manufacturing systems. In this section, we discuss key issues especially related to agent-based manufacturing, such as enterprise integration and supply chain management, agent encapsulation, system architectures, design and manufacturability assessments, manufacturing planning and scheduling, factory control architectures, tools and standards for developing agent-based manufacturing systems, based on our experience and an analysis of the research projects summarized in Section 3. 

4.1 Agent Technology for Enterprise Integration and Supply Chain Management 

In order to support its global competitiveness and rapid market responsiveness, an individual manufacturing enterprise has to be integrated with its related management systems (e.g., purchasing, orders, design, production, planning & scheduling, control, transport, resources, personnel, materials, quality, etc.), its partners, suppliers and customers via networks (local networks, the Internet or Intranet), which are, in general, heterogeneous software and hardware environments. 

The supply chain of a manufacturing enterprise is a world-wide network of suppliers, factories, warehouses, distribution centers and retailers through which raw materials are acquired, transformed and delivered to customers (Fox et al 1993). This network also, in general, involves heterogeneous environments. Agent based approaches provide a natural way to design and implement manufacturing enterprise integration and supply chain management within such environments. Fox et al (1993) may have been the first to propose organizing the supply chain as a network of cooperating, intelligent agents. A similar proposal has been made by Swaminathan et al (1996) using a multi-agent framework for modeling supply chain dynamics. In ISCM (Fox et al 1993), each agent performs one or more supply chain functions and coordinates its actions with other agents. In the supply chain library proposed by Swaminathan et al (1996), two categories of elements are distinguished: structural elements and control elements. Structural elements including production elements (retailers, distribution centers, plants, suppliers) and transportation elements are modeled as agents. Control elements (inventory, demand, supply, flow and information controls) are used to help in coordinating flow of products in an efficient manner with the use of messages. 

MetaMorph II (Shen et al 1998a) used a hybrid agent-based mediator-centric architecture to integrate partners, suppliers and customers dynamically with the main enterprise through their respective mediators within a supply chain network via the Internet and Intranets. In MetaMorph II, agents can be used to represent manufacturing resources (machines, tools etc) and parts, to encapsulate existing software systems, to function as system/subsystem coordinators (mediators), and to perform one or more

supply chain functions. Also, some researchers have proposed applying mobile agent technology to enterprise integration and supply chain management (Brugali et al 1998; Papaioannou & Edwards 1998; Yan et al 1998). 

The research results have shown that agent based approaches have the following advantages for enterprise integration and supply chain management: 

increasing the responsiveness of the enterprise to the market requirements; involving customers in total supply chain optimization; realizing supply chain optimization through effective resource allocation; achieving dynamic optimization of materials and inventory management; realizing total supply chain optimization including all linked enterprises; increasing the effectiveness of the information exchange and feedback. 

However, the security problem resulting from the open architecture of agent based systems, particularly when using the Internet and the mobile agent technology, has been recognized by both manufacturing enterprises and the researchers in this area. This is not unique to agent-based systems and may be mitigated through further research. 

4.2 Agent Encapsulation 

Among the different approaches used for agent encapsulation in agent based manufacturing systems, two approaches are distinct: the functional decomposition approach and the physical decomposition approach. 

In the functional decomposition approach, agents are used to encapsulate modules assigned to functions such as order acquisition, planning, scheduling, material handling, transportation management, and product distribution. There is no explicit relationship between agents and physical entities. Examples of this type of approach are ISCM (Fox et al 1993), CIIMPLEX (Peng et al 1998), ABACUS (McEleney et al 1998), and LMS (Fordyce and Sullivan 1994). 

In the physical decomposition approach, agents are used to represent entities in the physical world, such as workers, machines, tools, fixtures, products, parts, features, and operations, etc. There exists an explicit relationship between an agent and a physical entity. Examples can be found in MetaMorph I & II (Maturana and Norrie 1996; Shen et al 1998a), ADDYMS (Butler and Ohtsubo 1992), AIMS (Park et al 1993), AARIA (Parunak et al 1998), YAMS (Parunak 1987). 

The functional approach tends to share many state variables across different functions. Separate agents must share many state variables, thus leading to problems of consistency and unintended interactions. The physical approach naturally defines distinct sets of state variables that can be managed efficiently by individual agents with limited interactions. 

However, the functional approach is very useful in integrating existing systems (e.g., CAD tools, MRP systems, etc.) and resolving legacy problems. Even in an agent-based manufacturing system using primarily the physical approach, the functional approach may still be useful. This agents encapsulating some special functions may be used to provide such services at the system level, such as facilitators in PACT (Cutkosky et al 1993), broker agents in CIIMPLEX and AIMS, mediators in MetaMorph I & II, and system monitors in DIDE (Shen and Barthès 1996a) and in IFCF (Lin and Solberg 1992).

4.3 Multi-Agent Organization - System Architectures 

The different system architectures proposed in the literature for agent-based manufacturing systems can be classified into three categories: the Hierarchical approach, the Federation approach and the Autonomous Agent approach. 

A typical modern manufacturing enterprise consists of a number of, often physically distributed, semi-autonomous units, each with a degree of control over local resources or with different information requirements. For such a real situation, a number of practical agent-based industrial applications still use the hierarchical architecture, though it may be criticized for its centralized appearance. Examples can be found in HMS (Van Leeuwen and Norrie 1997; Bussmann 1998), ADDYMS (Butler and Ohtsubo 1992), DAS (Burke and Prosser 1991), and the Production Planning and Control Structure by Fischer (1994). 

Three approaches have been proposed for federation architectures: Facilitators, Brokers and Mediators. In the Facilitator approach, several related agents are combined into a group. Communication between agents takes place always through an interface called a facilitator. Each facilitator is responsible for providing an intermedium between a local collection of agents and remote agents, usually by providing two main services: (1) routing outgoing messages to the appropriate destinations; (2) translating incoming messages for consumption by its agents. CIIMPLEX (Peng et al 1998), PACT (Cutkosky et al 1993) and other SHADE-based projects (McGuire et al 1993; Park et al 1994; Petrie et al 1994) used this approach. 

Brokers (also called broker agents) are similar to facilitators with some additional functions such as monitoring and notification. The functional difference between a facilitator and a broker is that a facilitator is responsible only for a designated group of agents, whereas any agent may contact any broker in the same system for finding service agents to complete a special task. Broker agents can be found in AIMS (Park et al 1993) and CIIMPLEX (Peng et al 1998). 

The Mediator approach is another type of federation architecture. In addition to the functions of a facilitator and a broker, a mediator assumes the role of system coordinator by promoting cooperation among intelligent agents and learning from the agents’ behavior. A detailed description of the mediator concept and architecture can be found in (Gaines et al 1995). Applications using mediators in intelligent manufacturing systems can be found in (Gaines et al 1995; Maturana and Norrie 1996; Shen et al 1998a; Ouelhadj et al 1998). 

Federation multi-agent architectures (the Facilitator approach, the Broker approach and the Mediator approach) are able to coordinate multi-agent activity via facilitation as a means of reducing overheads, ensuring stability, and providing scalability. The federation approach promises to be a good foundation upon which to develop open, scalable multi-agent system architectures (Genesereth and Ketchpel 1994). 

The Autonomous Agent approach is different. Although different definitions have been proposed for autonomous agents, we argue that an autonomous agent should have at least the following characteristics: (1) it is not controlled or managed by any other software agents or human beings; (2) it can communicate/interact directly with any other agents in the system and also with other external systems; (3) it has knowledge about other agents and its environment; (4) it has its own goals and an associated set of motivations. DIDE used this approach for developing agent-based engineering design systems (Shen and Barthès 1996a). AARIA also used the Autonomous Agent approach, but with fixed

negotiation protocols (Parunak et al 1998). 

According to our experience, the Autonomous Agent approach is well suited for developing distributed intelligent design systems where existing engineering tools are encapsulated as agents and connected to the system for providing special services, and the system consists of a small number of agents. This type of architecture is also very useful for developing autonomous multiple robotic systems. In the mediator architecture, a static or dynamic hierarchy is imposed for every specific task, which provides computational simplicity and manageability. This type of architecture is quite suitable for developing distributed manufacturing systems which are complex, dynamic, and composed of a large number of resource agents. A combination of above mentioned approaches as a hybrid approach was proposed in MetaMorph II (Shen et al 1998a) for developing more flexible, modular, scalable and dynamic manufacturing systems. 

4.4 Dynamic System Reconfiguration 

Real world manufacturing environments are highly dynamic because of diverse frequently changing situations: bank rates change overnight, political situations change, materials do not arrive on time, power supplies breakdown, production facilities fail, workers are absent, new orders arrive and existing orders are changed or canceled. Such changing situations lead to deviations from existing plans and schedules. It is therefore necessary for the system architecture to meet such requirements and for the working system to adapt to such changing environments. 

In AIMS (Park et al 1993), by using the Internet to connect agents, services can be added or taken out of service at any time, with incremental impact on capacity, simply by informing the appropriate directories and brokers. MetaMorph I & II (Maturana and Norrie 1996; Shen et al 1998a) also provide this feature by using a registration mechanism at both the system level and the mediator level. AARIA (Parunak et al 1998) provides such a feature through its Autonomous Agent approach, and ATP (NIST 1998) through its plug-and-play framework. 

4.5 Learning in Agent-Based Manufacturing Systems 

For most application tasks, it is extremely difficult or even impossible to correctly determine the behavioral repertoire and concrete activities of an agent-based manufacturing system a priori, that is, at the time of its design and prior to its use. This would require, for instance, that it is known a priori which environmental requirements will emerge in the future, which agents will be available at the time of emergence, and how the available agents will have to interact in response to these requirements. Such problems resulting from the complexity of agent-based systems can be avoided or at least reduced by endowing the agents with the ability to learn, that is, with the ability to improve the future performance of the total system, or a part of the system. Thus, learning is one of the key techniques for implementing agent-based manufacturing systems. A more detailed discussion on learning in agent-based manufacturing systems can be found in (Shen et al 1998b). 

4.6 Design and manufacturability assessments 

Geometric and functional specifications, availability of raw materials, and the capability and availability of shop-floor resources each have a major influence on manufacturability. A design may be manufacturable under one combination of product requirements and shop-floor resources, but not under another. An agent-based integrated manufacturing system should provide dynamic manufacturability

assessments during the product design process. 

The MetaMorph I architecture provides a mechanism for immediate manufacturability assessments (Maturana and Norrie 1996). As a product part is progressively designed by repeated instantiation of features, manufacturability is evaluated by resource agents for every instantiation. Design Mediators and Resource Mediators ensure coordination among design parts and resource agents. Design subsystems (or design agents) interact with resource agents via Resource Mediators to obtain manufacturability assessments during the product design process. This process not only ensures the manufacturability of a product, but also results in incremental identification of general process plans. 

4.7 Distributed Dynamic Scheduling 

Corresponding to the two distinct approaches for agent encapsulation described in Section 4.2, two types of distributed manufacturing scheduling systems can be distinguished: 

Those where scheduling is an incremental search process that can involve backtracking. Agents, responsible for scheduling orders, perform local incremental searches for their orders and may consider multiple resources. The global schedule is obtained through the merging of local schedules. This is very similar to centralized scheduling. 

Systems in which an agent represents a single resource (e.g., a work cell, a machine, a tool, a fixture, a worker, etc.) and is responsible for scheduling this resource. This agent may negotiate with other agents to carry out overall scheduling. 

Examples of the first type of scheduling systems can be found in (Sadeh and Fox 1989; Sycara et al 1991; Burke and Prosser 1991; Fordyce and Sullivan 1994; Murthy et al 1997; McEleney et al 1998). 

For the second approach, the scheduling mechanism is generally realized through negotiation among agents. The protocols for negotiation include the voting mechanism (Fordyce and Sullivan 1994), Smith’s Contract net (Smith 1980) or its modified versions, such as the Extended Contract Net Protocol (ECNP) proposed by Fischer et al (1995), the Market-Driven Contract Net by Baker (1991), the B-Contract-Net by Scalabrin (1996), and the Leveled Commitment Contracting Protocol by Sandholm and Lesser (1996). Other examples can be found in (Duffie and Piper 1986; Parunak 1987; Ow and Smith 1988; Shaw 1988; Butler and Ohtsubo 1992; Lin and Solberg 1992; Saad et al 1995; Shen and Norrie 1998; Ouelhadj et al 1998). The bidding mechanism can be part-oriented (Duffie and Piper 1986; Ow and Smith 1988; Lin and Solberg 1992), resource-oriented (Butler and Ohtsubo 1992; Baker 1991; Shen and Norrie 1998), or bi-directional (Saad et al 1995). 

We use "dynamic scheduling" here to indicate that a real-time manufacturing scheduling system can update its schedule to adapt to changing situations such as new order insertion, machine failures, job tardiness, etc. ADDYMS developed a dynamic scheduling mechanism for local resource allocation at the local work cell level (Butler and Ohtsubo 1992). In MetaMorph II, several mechanisms were developed for dynamic scheduling and rescheduling by combining a bidding mechanism based on Contract Net protocol with a mediation mechanism based on the Mediator architecture (Shen and Norrie 1998). Sousa and Ramos (1997) have proposed a dynamic scheduling architecture using holons. 

4.8 Planning, Scheduling and Execution

Integration of planning and scheduling 

The notion of manufacturing planning and scheduling has been introduced in Section 3.2. Traditional approaches to planning and scheduling do not consider the constraints of both domains simultaneously. In spite of being sub-optimal these approaches have been in vogue due to the non-availability of a unified framework. Agent-based approaches provide a possible way to integrate planning and scheduling activities through enterprise-level coordination between the product design system and the factory resource scheduling system. MetaMorph I implemented such a mechanism through enterprise level coordination between Design Mediators and Resource Mediators who in turn coordinate resource agents at the shop floor level (Maturana et al 1996). 

Concurrent Scheduling and Execution 

Traditional systems alternate scheduling and execution. For example, a firm develops a schedule each night for its manufacturing operations the next day. The real world tends to change in ways that invalidate advance schedules. Natural systems do not plan in advance, but adjust their operations on a time scale comparable to that in which their environment changes. MetaMorph II (Shen et al 1998a) proposed to use Execution Mediators to coordinate the execution of the machines, AGVs, and workers as necessary. By such an approach, manufacturing resources (e.g., machines, interfaces for workers, etc.) can be connected directly to the manufacturing system. As the manufacturing is in progress, the information about the execution process (progress of the schedule) is captured by the Execution Mediators which in turn send such information to Resource Mediators for adjusting the schedule as necessary. 

4.9 Factory Control Architectures 

Control architectures for real-time distributed manufacturing systems commonly need to satisfy requirements such as autonomy, reliability, fault-tolerant, interoperability, reconfigurability, and other real-time functionality. In contrast to traditional manufacturing systems using centralized control architectures, agent-based distributed manufacturing systems use decentralized architectures. Decentralized controls have three typical architectures: hierarchical, oligarchical and heterarchical (Brennan et al 1997). Generally, the approach for hierarchical large-scale control systems involves decomposing the overall system into smaller sub-systems that have weaker interactions with each other and also a lower degree of cooperative autonomy. In a hierarchical system, sub-systems or elements at a lower level receive instructions from those in the next higher level, which restricts their autonomy. The oligarchical approach provides less rigid communication paths and supports a higher degree of autonomy. The heterarchical approach supports a yet higher degree of autonomy, offers prospects of reduced complexity, reduced software development costs, high modularity, high flexibility, and improved fault tolerance (Duffie and Piper 1986), but it may take much more time during decision-making, especially when a large number of agents are engaged. 

Duffie and Prabhu (1994) proposed to use a heterarhical, opportunistic scheduling technique for machining cell control. Baker (1991) developed a Market-Driven Contract Net for heterarchical multi-agent manufacturing systems. Lin and Solberg (1992) proposed a generic framework for controlling work flow in manufacturing systems. Based on a market-like model and a combination of objective and price mechanism, the framework allows heterogeneous job objectives, admits job priorities, recognize multiple resource types, and allows multiple step negotiation between parts and resources. Brennan et al (1997) proposed a Partial Dynamic Control Hierarchy by combining both

hierarchical and heterarchical architectures. The use of partial dynamic hierarchies assists reconfigurability and can provide a better system performance than either single control approaches. 

4.10 Tools and Standards 

Most projects or research work reviewed in this paper use traditional programming languages, such as C++, Java, Lisp, SmallTalk, Prolog, and Objective C to develop agent-based manufacturing systems. For wider use of agent technology in the development of agent based manufacturing systems, powerful agent development tools are strongly needed. Recently, a number of tools have been reported, some of which are already commercially available. ABS (Agent Building Shell) is developed in EIL of the University of Toronto especially for developing cooperative enterprise agents (Barbuceanu and Fox 1995a; 1995b; 1996). It is being used to develop multi-agent applications in the area of manufacturing enterprise supply chain integration. ObjectSpace’s VoyagerTM p oduct provides a Java based Object Request Broker (ORB) designed for mobile agents. ObjectSpace, together with AMD (Advanced Micro Devices), won the 1997 NIST ATP (Advanced Technology Program) award for a $4.9M R&D project to create an Agent-Enhanced Manufacturing System using VoyagerTM (ObjectSpace 1997). ZEUS is a tool-kit developed at British Telecom for engineering distributed multi-agent systems (Nwana et al 1998). Gensym’s ADE (Agent Development Environment) builds on its intelligent manufacturing software development environment G2 (Gensym 1997). ADE has been applied to the development of agent-based systems for supply chain management (Mehra and Nissen 1998). It is also being used in NCMS Shop Floor Agents (SFA) project (NCMS 1998). Other general agent development tools include IBM’s Aglets SDK (IBM 1998), General Magic’s OdysseyTM (General Magic 1997), SRI’s ADT (Agent Development Toolkit) and OAA (Open Agent Architecture) (Martin et al 1998), Stanford’s JATLite (Stanford 1997), AARIA team’s Cybele (Baker et al 1997), and DESIRE (Brazier et al 1998). 

Wide use of agent technology in industry depends on the availability of development tools and platforms that protect developers from the need of developing basic functionality with each system. Such tools and platforms, in turn, presume the existence of standards that reflect the agreement of developers on what that basic functionality should be and how it should be presented. Some efforts have been devoted to providing standards for agent-based systems, but no accepted standards can be found for developing agent based manufacturing systems. KQML (Finin et al 1993) is intended to be a common communication language for agents, with KIF (Genesereth and Fikes 1992) as a common content format. Some traditional standards have also been used in agent based system developments, such as, CORBA (Common Object Request Broker Architecture) (OMG 1998) for inter-agent communication, and STEP (Bjork and Wix 1991) for providing semantics of messages in manufacturing applications. Recently, two consortia are focusing on formalizing standards specifically in support of agents. The Foundation for Intelligent Physical Agents (FIPA), established in 1996 as a world-wide consortium, promotes the development of specifications of generic agent technologies that maximize interoperability within and across agent-based applications (FIPA 1998). FIPA has already produced version 0.1 of its set of specifications called FIPA 98. The National Industrial Information Infrastructure Protocols (NIIIP) is a consortium of US companies formed to develop open industry software protocols that will make it possible for manufacturers and their suppliers to effectively inter-operate as if they were part of the same enterprise (NIIIP 1994). 

References 

Baker, A.D. (1991). Manufacturing Control with a Market-Driven Contract Net. PhD thesis, Rensselaer

Polytechnic Institute, NY. (A Market-Driven Contract Net was proposed for heterarchical agent-based scheduling. It performs a type of forward / backward scheduling.) (http://www.ececs.uc.edu/~abaker/) 

Baker, A.D., Parunak, H.V.D. and Erol, K. (1997). Manufacturing over the Internet and into Your Living Room: Perspectives from the AARIA Project. Working Paper, Department of Electrical & Computer Engineering and Computer Science, University of Cincinnati. (Outl ne of new directions for On-Line Commerce. AARIA’s architecture and scheduling approach. Introduction to the Cybele Agent Infrastructure in Appendix.) (http://www.ececs.uc.edu/~abaker/) 

Barber, S., White, E., Goel, A., Han, D., Kim, J., Li, H., Liu, T.H., Martin, C.E. and McKay, R. (1998). Sensible Agent Problem-Solving Simulation for Manufacturing Environments. In Proceedings of AI & Manufacturing Research Planning Workshop, Albuquerque, NM, The AAAI Press, pp. 1-9. (Concepts of Sensible Agents. Prototype was implemented as CORBA objects communicating through ILU object environment.) (http://www.lips.utexas.edu/) 

Barbuceanu, M. and Fox, M. (1995a). The Architecture of an Agent Based Infrastructure for Agile Manufacturing. In Proceedings of IJCAI’95, Montreal, Canada. (Agent Based Shell - An Infrastructure and related toolkits for developing cooperative enterprise agents. Main work was focused on Coordination in MAS. Its LISP based COOL may limit its use in developing industrial applications.) (http://www.ie.utoronto.ca/EIL/ABS-page/ABS-intro.html) 

Barbuceanu, M. and Fox, M. (1995b). COOL: A Language for Describing Coordination in Multi Agent Systems. In Proceedings of ICMAS’95, San Francisco, CA, The AAAI press/The MIT Press, pp 17 - 24. (A complementary reference to Barbuceanu and Fox 1995a.) (http://www.ie.utoronto.ca/EIL/ABS-page/ABS-intro.html) 

Barbuceanu, M. and Fox, M. (1996). Capturing and Modeling Coordination Knowledge for Multi-Agent Systems. International Journal of Cooperative Information Systems, 5(2-3). (A complementary reference to Barbuceanu and Fox 1995a.) (http://www.ie.utoronto.ca/EIL/ABS-page/ABS-intro.html) 

Barbuceanu, M. and Fox, M. (1997). Integrating Communicative Action, Conversations and Decision Theory to Coordinate Agents. In Proceedings of Autonomous Agents’97, Marina del Rey, CA. (A complementary reference to Barbuceanu and Fox 1995a.) (http://www.ie.utoronto.ca/EIL/ABS-page/ABS-intro.html) 

Berry, N.M. and Kumura S. (1998). Evaluating the Design and Development of Reagere. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (A multi-agent shop floor control system where the agents represent components including software, hardware, sensors, etc. The system was built on top of the generic blackboard control architecture, so it is somewhat a centralized system with some supporting modules that were called as agents.) (http://www.ie.psu.edu/people/faculty/kumara.htm) 

Biswas, G., Bagchi, S. and Saad, A. (1995). Holonic Planning and Scheduling for Assembly Tasks. TR CIS-95-01, Center for Intelligent Systems, Vanderbilt University. (A complementary reference to Saad et al 1995.) (http://shogun.vuse.vanderbilt.edu/CIS/IMS/index.html) 

Bjork, B. and Wix, J. (1991). An Introduction to STEP. Technical Report, VTT Technical Research Centre of Finland and Wix McLelland Ltd., England. (A introductory description of the STEP standard.) (http://www.nist.gov/sc4/www/stepdocs.htm) 

Brazier, F., Jonker, C., Treur, J. and Wijngaards, N. (1998). Compositional Design of Generic Design

Agent. In Proceedings of AI & Manufacturing Research Planning Workshop, Albuquerque, NM, The AAAI Press, pp. 30-39. (A generic architecture for a design agent, with a compositional development methodology (DESIRE) for developing agent based systems. Interesting features: a generic agent model, graphical design tools, and mechanisms for dynamic agent creation. New features and mechanisms need to be added for developing industrial agent based systems.) (http://www.cs.vu.nl/vakgroepen/ai/projects/desire/) 

Brennan, R.W., Balasubramanian, S., and Norrie, D.H. (1997). Dynamic Control Architecture for Advanced Manufacturing Systems. In Proceedings of International Conference on Intelligent Systems for Advanced Manufacturing, Pittsburgh, PA. (  Partial Dynamic Control Hierarchy (PDCH) was proposed as a manufacturing system control architecture, which combines the features of both hierarchical and heterarchical architectures.) (http://imsg.enme.ucalgary.ca/) 

Brückner, S, Wyns, J, Peeters, P, Kollingbaum, M. (1998). Designing Agents for the Manufacturing Process Control. In Proceedings of Artificial Intelligence and Manufacturing Research Planning Workshop - State of the Art & State of the Practice, AAAI Press, Albuquerque, New Mexico, pp. 40-46. (Methodology chosen in the MASCADA - a European ESPRIT project on developing Manufacturing Control Systems Capable of Managing Production Change and Disturbances. UML from object-oriented design methodology was used to standarize the representation of the specification of agents and a multi-agent system.) (http://www.mech.kuleuven.ac.be/pma/project/mascada/welcome.html) 

Brugali, D., Menga, G. and Galarraga, S. (1998). Inter-Company Supply Chains Integration via Mobile Agents. In Proceedings of PROLAMAT’98, Trento, Italy. (An interesting proposition for using mobile agents in supply chain management.) (http://www.polito.it:80/~brugali/) 

Budenske, J., Ahamad, A. and Chartier, E. (1998). Agent-Based Architecture for Exchanging Modeling Data between Applications. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (An Agent-Based Middleware Architecture (ABMA) was proposed to address the problem of exchanging model and process description information between multiple applications which were not initially developed to be interoperable. It is intended to be useful for resolving legacy problems.) (http://www.atcorp.com/) 

Burke, P. and Prosser, P. (1994). The Distributed Asynchronous Scheduler. Inte ligent Scheduling, Zweben, M. and Fox, M.S., eds., Morgan Kaufman Publishers, San Francisco, CA, pp. 309-339. (The DAS architecture consists of three types of entities: knowledge resources, agents and a constraint maintenance system. DAS was able to make a correct schedule, but it had no method for optimizing that schedule.) (http://www.cs.strath.ac.uk/biography/pat/) 

Bussmann S. (1998). An Agent-Oriented Architecture for Holonic Manufacturing Control. In Proceedings of First International Workshop on IMS, Lausanne, Switzerland, pp. 1-12. (A good discussion on the concepts of two approaches: Agent-Oriented approach and HMS approach, and how to use the Agent-Oriented approach to implement HMS concepts.) (http://www.daimler-benz.com/) 

Butler, J. and Ohtsubo, H. (1992). ADDYMS: Architecture for Distributed Dynamic Manufacturing Scheduling. Artificial Intelligence Applications in Manufacturing, Famili, A., Nau, D.S., and Kim, S.H., (eds.), The AAAI Press, pp. 199-214. (A prototype architecture proposed for distributed manufacturing scheduling. A dynamic local resource allocation mechanism was developed for dynamic scheduling.) 

Choi, H.S. and Park, K.H. (1997). Shop-floor scheduling at shipbuilding yards using the multiple intelligent agent system. Journal of Intelligent Manufacturing, 8(6), 505-515. (A standardized methodology for constructing agent based systems. It provides a method for developing agent systems by using standardizing communication protocols in linguistics speech-act theory, and by supplementing traditional algorithmic systems with intelligent segments using expert system tools. It also provides methods for solving deadlock occurrence and non-uniformity

problems resulting from parallel processing. It was used to develop the shop-floor scheduling system of a large-scale shipbuilding yard.) 

Christensen, J.H. (1994). Holonic manufacturing systems: initial architecture and standards directions. In Proceedings of First European Conference on Holonic Manufacturing Systems, Hanover, Germany. (A summary of concepts and architectural features of holonic manufacturing systems.) (http://www.automation.rockwell.com/) 

Christensen, J.H., Struger, O.J., Norrie, D. and Schaeffer, C. (1994). Material Handling Requirements in Holonic Manufacturing Systems. In Proceedings of the 1994 International Material Handling Research Colloquium, Grand Rapids, MI, The Material Handling Industry of America, 22 pp. (A consideration of material handling issues in holonic manufacturing systems.) (http://www.automation.rockwell.com/) 

Cutkosky, M.R., Engelmore, R.S., Fikes, R.E., Genesereth, M.R., Gruber, T.R., Mark, W.S., Tenenbaum, J.M. and Weber, J.C. (1993). PACT: An Experiment in Integrating Concurrent Engineering Systems. IEEE Computer, 26(1), 28-37. (A well known testbed using agent technology to collaborative engineering design. Uses a federation architecture with facilitators.) (http://cdr.stanford.edu/PACE/) 

Cutkosky, M.R., Tenenbaum, J.M. and Glicksman J. (1996). Madefast: Collaborative Engineering over the Internet. Communication of the ACM, 39(9), 78-87. (A DARPA DSO-sponsored project to demonstrate technologies developed under the DARPA MADE program. This was an ambitious experiment in collaborative engineering over the Internet.) (http://cdr.stanford.edu/html/MADEFAST/home.html) 

Deen, S.M. (1994). A cooperation framework for holonic interactions in manufacturing. In Proceedings of the Second International Working Conference on Cooperating Knowledge Based Systems (CKBS’94), DAKE Centre, Keele University. (Introduction of a holon-based cooperation framework for intelligent manufacturing. One of the earliest propositions of this knid.) (http://www.keele.ac.uk/depts/cs/Research/Dake/home.html) 

Duffie, N.A. and Piper, R.S. (1986). Non-Hierarchical Control of Manufacturing Systems. Journal of Manufacturing Systems, 5(2), 137-139. (A testbed multi-agent heterarchy using "part-oriented" manufacturing scheduling. Both resources (processing equipment, material handling equipment and humans) and parts are represented by agents.) (http://www.engr.wisc.edu/me/faculty/duffie_neil.html) 

Duffie, N.A. and Prabhu, V.V. (1994). Real-time distributed scheduling of heterarchical manufacturing systems. Journal of Manufacturing Systems, 13(2), 94-107. (A heterarhical, opportunistic scheduling technique for machining cell control.) (http://www.engr.wisc.edu/me/faculty/duffie_neil.html) 

Finin, T., Fritzon, R., McKay, D. and McEntire, R. (1993). KQML - A Language and Protocol for Knowledge and Information Exchange. Tech. Report, University of Maryland, Baltimore. (Description of the well-known KQML.) (http://www.cs.umbc.edu/kqml/) 

FIPA. (1998). Foundation for Intelligent Physical Agents. (Web site with information on the FIPA consortium, its proposals and achievements.) http://drogo.cselt.stet.it/fipa/ 

Fischer, K. (1994). The Design of an Intelligent Manufacturing System. In Proceedings of the 2nd International Working Conference on Cooperating Knowledge-based Systems, University of Keele, pp. 83-99. (Description of a hierarchical layered planning and control structure.) (http://www.dfki.uni-sb.de/mas/)

Fischer, K., Muller J.P, Pischel, M. and Schier, D. (1995). A Model for Cooperative Transportation Scheduling. In Proceedings of ICMAS’95, AAAI Press/MIT Press, San Francisco, CA, pp. 109-116. (Proposes the Extended Contract Net Protocol for agent negotiation.) (http://www.dfki.uni-sb.de/mas/) 

Fleury, G., Goujon, J-Y., Gourgand, M. and Lacomme, P. (1996). Multi-Agent Approach for Manufacturing Systems Optimization. In Proceedings of PAAM’96, London, pp. 225-244. (Proposes the ’triple coupling’ of multi-agent techniques, simulated annealing, and simulation for manufacturing systems optimization.) 

Fordyce, K. and Sullivan, G.G. (1994). Logistics Management System (LMS): Integrating Decision Technologies for Dispatch Scheduling in Semiconductor Manufacturing. Intelligent Scheduling, Zweben, M. and Fox, M.S., eds., Morgan Kaufman Publishers, San Francisco, CA, pp. 473-516. (LMS used functional agents, one for each production constraint, and a judge agent to combine the votes of the four critics. Each agent models those aspects of the environment needed to satisfy its objective. A voting protocol was used for communication among agents.) 

Fox, M.S., Chionglo, J.F., and Barbuceanu, M., (1993), The Integrated Supply Chain Management System. Internal Report, Dept. of Industrial Engineering, Univ. of Toronto. (Appears to be the fist to propose organizing the supply chain as a network of cooperating, intelligent agents.) (http://www.ie.utoronto.ca/EIL/iscm-descr.html) 

Gaines, B.R., Norrie, D.H., and Lapsley, A.Z. (1995). Mediator: an Intelligent Information System Supporting the Virtual Manufacturing Enterprise. In Proceedings of 1995 IEEE International Conference on Systems, Man and Cybernetics, New York, pp. 964-969. (Introduction of the Mediator architecture to intelligent manufacturing.) (http://imsg.enme.ucalgary.ca/) 

General Magic (1997). Odyssey Information. (Web site with information on mobile agent technology.) http://www.genmagic.com/technology/odyssey.html 

Genesereth, M.R., Fikes, R.E. (1992): Knowledge Interchange Format, Version 3.0, Reference Manual, Computer Science Department, Stanford University, Technical Report Logic-92-1. (Describes the well-known KIF standard.) (http://www.cs.umbc.edu/agents/kse/kif/) 

Genesereth, M. and Ketchpel, S. (1994) Software agents. Communications of the ACM, 37(7), 48-53. (http://logic.stanford.edu/people/genesereth/) 

Gensym. (1997). Agent Development Environment (ADE): Overview. Project Report, NCMS. (Outlines a software development environment for agent systems.) (http://www.gensym.com/) 

Goldsmith, S.Y. and Interrante, L.D. (1998). An Autonomous Manufacturing Collective for Job Shop Scheduling. In Proceedings of AI & Manufacturing Research Planning Workshop, Albuquerque, NM, The AAAI Press, pp. 69-74. (Using physical resource agents. Contract Net protocol for negotiation. Similar to the approach present in Shen and Norrie 1998.) (http://www.sandia.gov/) 

Gray, P.M.D., Embury, S.M., Hui, K. and Prce, A. (1998). An Agent-Based System for Handling Distributed Design Constraints. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Intelligent mediators act as knowledge brokers and transform knowledge to make it useable by problem-solvers at various sites on the network. A particular class of knowledge, i.e., constraints, is investigated.) (http://www.csd.abdn.ac.uk/~pgray/) (http://www.csd.abdn.ac.uk/~apreece/Research/KRAFT.html) 

Hasegawa, T., Gou, L., Tamura, S., Luh, P.B., and Oblak, J.M. (1994). Holonic Planning and

Scheduling Architecture for Manufacturing. In Proceedings of the 2nd International Working Conference on Cooperating Knowledge-based Systems, University of Keele. (On  of the earliest holonic manufacturing planning and scheduling systems.) (http://www.toshiba.co.jp/) 

Hayashi, H. (1993). The IMS International Collaborative Program. In Proceedings of 24th ISIR, Japan Industrial Robot Association. (Earlier description of the Intelligent Manufacturing Systems international research program. The HMS consortium is one of those operating under this program.) (http://www.ims.org/) 

Hayes, C.C. (1998). MAPP: an Agent Organization for Process Planning. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (MAPP provides a simple way to represent both the temporal organization of the planner (represented by a sequence of planning phases) and the functional organization of the data (achieved by a set of blackboards). It is, in fact, a blackboard system with some special problem solvers.) (http://www.me.umn.edu/) 

IBM. (1998). Aglets Software Development Kit. IBM, http://www.trl.ibm.com/aglets/ (Web site with information about a agent development kit called Aglets.) 

IEC Tchnical Committee, (1997). Function Blocks for Industrial-Process Management and Control Systems, Part-1: Architecture. IEC-TC65/WG6 Committee Draft. (Function blocks have been proposed for modeling agent-based control systems. This is the first part of a proposed standard.) 

Interrante, L. and Glodsmith, S. (1998). Emergent Agent-Based Scheduling of Manufacturing Systems. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Proposes a general agent architecture and three types of agents: Type A agents representing system entities such as a machine, a production line/cell, the shop floor subsystem, or a plant in a supply chain; Type B agents created at runtime by the Type A collective to resolve a scheduling conflict; and Type C agent, as a high-level supervisory agent reasoning about the global effect of multiple interacting schedule propagation on the overall manufacturing goals. Appears to be a useful classification of agents in manufacturing systems.) (http://www.sandia.gov/) 

Jenkin, M.R.M., Milios, E. and Wilkes, D. (1996). A taxonomy for multi-agent robotics. Autonomous Robotics, 3(4), 375-397. (A good survey on agent applications in robotics.) 

Jennings, N.R., Corera, J.M. and Laresgoiti, I. (1995). Developing Industrial Multi-Agent Systems. In Proceedings of ICMAS’95, San Francisco, The AAAI press/The MIT press, pp. 423-430. (Brief description of the well-known ARCHON framework. Detailed analysis of ARCHON’s electricity transportation management application - one of the earliest operational industrial DAI systems. The observations and reflections at the end of the paper are also thoughtful.) (http://www.elec.qmw.ac.uk/dai/) 

Jennings, N.R. and Wooldridge, M.J. (1998). Applications of Intelligent Agents. Agent Technology: Foundations, Applications, and Markets. Jennings, N.R. and Wooldridge, M.J (Eds.), Springer, pp. 3-28. (As an introduction to this book, the authors give a summary of different application domains of agent technology, with brief description of some typical examples.) (http://www.elec.qmw.ac.uk/dai/) 

Jha, K.N., Morris, A. Mytych, E. and Spering, J. (1998). MADEsmart: Agents for Design, Analysis, and Manufacturbility. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (MADEsmart contains several different types of agents including User-Interface Agents for user interaction, Control Agents for inter-agent coordination, Wrapper Agents for legacy system encapsulation, Resource Agents for external resource integration, and Execution Agents for special functionality realization (e.g., Optimization Agent). It is a good example in Enterprise Integration.) (http://www.boeing.com/) 

M. Klein. iDCSS: Integrating Workflow, Conflict and Rationale-based Concurrent Engineering

Coordination Technologies. Concurrent Engineering: Research and Application, 3(1), 21-27, 1995. (Proposes an integrated model that combines existing coordination approaches in an attempt to avoid many of their limitations and combine their strengths.) (http://ccs.mit.edu/) 

Koestler, A. (1967). The Ghost in the Machine. Arkana Books, London, UK. (The book that first introduced the term ’holon’ and related concepts.) 

Kouiss, K., Pierreval, H., and Mebarki, N. (1997). Using multi-agent architecture in FMS for dynamic scheduling. Journal of Intelligent Manufacturing, 8(1), 41-47. (A multi-agent architecture for dynamic job shop scheduling. Each agent is dedicated to a work center. Each agent performs a local dynamic scheduling by selecting an adequate dispatching rule. The selection method is improved through the optimization of the numerical thresholds used in the detection of symptoms. Agents can also coordinate their actions to perform a global dynamic scheduling. A unique approach for agent based manufacturing scheduling.) 

Kwok, A.D. and Norrie, D.H. (1994). A Development System for Intelligent Agent Manufacturing Software. Integrated Manufacturing Systems, 5(4-5), 64-76. (A multi-paradigm development environment IAO (Intelligent Agent Object) based on a rule-based object system for developing intelligent agent manufacturing software.) (http://imsg.enme.ucalgary.ca/) 

Lin, G.Y.-J. and Solberg, J.J. (1992). Integrated Shop Floor Control Using Autonomous Agents. IIE Transactions: Design and Manufacturing, 24(3), 57-71. (A market-like control model used for adaptive resource allocation and distributed scheduling. The market mechanism, using multiple-way and multiple-step negotiation, was incorporated to coordinate the agents, in real time, including part agents, resource agents, database agents, and communication agents.) (http://IE.www.ecn.purdue.edu/IE/) 

Liu, J. and Sycara, K.P. (1994). Distributed problem solving through coordination in a society of agents. In Proceedings of the 13th International Workshop on DAI. (A coordination mechanism called CP&CR (Constraint Partition and Coordinated Reaction) for job shop constraint satisfaction, which assigns each resource to a resource agent responsible for enforcing capacity constraints on the resource, and each job to a job agent responsible for enforcing temporal precedence and release date constraints within the job.) (http://www.cs.cmu.edu/afs/cs/user/katia/www/katia-home.html) 

Liu, J. and Sycara, K.P. (1995). Exploiting Problem Structure for Distributed Constraint Optimization. In Proceedings of ICMAS95, San Francisco, CA, pp. 246-253. (Based on the approach presented in (Liu and Sycara 1994), a new coordination mechanism called Anchor&Ascend was proposed for distributed constraint optimization, which takes advantages of disparity among subproblems to efficiently guide distributed local search for global optimality. Anchor&Ascend employs an anchor agent to conduct local optimization of its subsolution and interacts with other agents who perform constraint satisfaction through CP&CR to achieve global optimization.) (http://www.cs.cmu.edu/afs/cs/user/katia/www/katia-home.html) 

Malkoun, M.T. and Kendall, E.A. (1997). CLAIMS: Cooperative Layered Agents for Integrating Manufacturing Systems. In Proceedings of PAAM’97, London. (A methodology for developing agent based systems for enterprise integration, based upon the IDEF (ICAM Definition) approach for workflow modeling and analysis, the CIMOSA (Computer Integrated Manufacturing Open System Architecture) enterprise modeling framework, and the use case driven approach to object oriented software engineering.) (http://www.cse.rmit.edu.au/~rdsek/) 

Martin, D.L., Cheyer, A.J. and Moran, D.B. (1998). Building Distributed Software Systems with the Open Agent Architecture. In Proceedings of PAAM’98, London. (Description of a well known architecture -Open Agent Architecture for developing multi-agent systems.) (http://www.ai.sri.com/~oaa/) 

Maturana, F. and Norrie, D. (1996). Multi-Agent Mediator Architecture for Distributed manufacturing.

Journal of Intelligent Manufacturing, 7, 257-270. (A multi-agent approach for intelligent manufacturing with some special features such as task decomposition, virtual clustering, agent cloning, and multi-agent learning.) (http://imsg.enme.ucalgary.ca/) 

Maturana, F., Balasubramanian, S. and Norrie, D.H. (1996). A Multi-Agent Approach to Integrated Planning and Scheduling for Concurrent Engineering. In Proceedings of the International Conference on Concurrent Engineering: Research and Applications, Toronto. (An attempt to use a multi-agent approach for integration of planning and scheduling.) (http://imsg.enme.ucalgary.ca/) 

McEleney, B., O’Hare, G.M.P. and Sampson, J. (1998). An Agent Based System for Reducing Changeover Delays in a Job-Shop Factory Environment. In Proc. of PAAM’98, London. (Using functional agents: Scheduling Prediction Agent, Scheduling/ Dispatching Agent, Information Provider Agent, Processor Agent and Event Filtering Agent. The BDI approach was used in agent design to model scheduling environment and scheduler decision making.) (http://www.co.umist.ac.uk/) 

McGuire, J., Huokka, D., Weber, J., Tenenbaum, J., Gruber, T., and Olsen, G. (1993). SHADE: Technology for Knowledge-Based Collaborative Engineering. Journal of Concurrent Engineering: Applications and Research, 1(3). (A good example of the efforts related to knowledge sharing for collaborative engineering.) 

Mehra, A. and Nissen, M. (1998). Intelligent Supply Chain Agents using ADE. In Proceedings of AI & Manufacturing Research Planning Workshop, Albuquerque, NM, The AAAI Press, pp. 112-119. (A good application example of Gensym’s ADE. See Gensym 1997.) (http://www.gensym.com/) 

Miyashita, K. (1998). CAMPS: a constraint-based architecture for multi-agent planning and scheduling. Journal of Intelligent Manufacturing, 9(2), 147-154. (An integrated architecture for distributed planning and scheduling using the repair-based methodology together with the constraint-based mechanism of dynamic coalition formation among agents.) 

Molina, A., Al-Ashaab, A.H., Ellis, T.I.A., Young, R.I.M., and Bell, R. (1995). A Review of Computer-Aided Simultaneous Engineering Systems. Re earch in Engineering Design, 7(1), 38-63. (A review of some concurrent engineering systems, with pertinent discussions on the definition of Concurrent Engineering and the issues on system development. Most of reviewed systems are related to concurrent engineering design and most of those systems use the blackboard architecture.) 

Murthy, S., Akkiraju, R., Rachlin, J. and Wu, F. (1997). Agent-Based Cooperative Scheduling. In Proceedings of AAAI Workshop on Constrains and Agents, AAAI Press, pp. 112-117. (An agent-based scheduling system based on the A-team architecture in which functional agents generate, evaluate, improve, and prune a pool of candidate solutions. It is, in fact, a blackboard system.) 

NCMS. (1998). Shop Floor Agents. NCMS. (Description of a project at NCMS focused on applications of agent-based technology to shop floor scheduling and machine control.) (http://www.ncms.org/3portfolio/1ProjectPortfolio/TechProjPort.htm - Search by ’Agent’) 

NIIIP. (1994). About the NIIIP Consortium. http://www.niiip.org/about-NIIIP-text.html (Web page with information about the National Industrial Information Infrastructure Protocols (NIIIP) Consortium, including its vision, goals, objectives and links to its members’ web site.) 

NIST (1998) Advanced Technology Program. http://www.atp.nist.gov/ (A joint project between US government and private industry to develop technologies for a plug-and-play framework of integratable business objects and software agents to enable agile manufacturing by making shop-floor status and capacity information available in real-time throughout an enterprise. A large project with high-level financial support.)

Nwana, H.S., Ndumu, D.T. and Lee, L.C. (1998). ZEUS: An Advanced Tool-Kit for Engineering Distributed Multi-Agent Systems. In Proceedings of PAAM’98, London. (Description of a tool-kit for distributed engineering multi-agent systems.) (http://www.labs.bt.com/projects/agents/) 

ObjectSpace. (1997). Agent-Enhanced Manufacturing System Initiative: Project Brief. ObjectSpace, http://www.atp.nist.gov/www/comps/briefs/97050018.htm htm (Web page with information about the Advanced Technology Program initiated at NIST.) 

OMG. (1998). OMG Formal Documentation. http://www.omg.org/corba/ (Web site with information about the well-known CORBA.) 

Ouelhadj, D., Hanachi, C. and Bouzouia, B. (1998). Multi-Agent System for Dynamic Scheduling and Control in Manufacturing Cells. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (An agent-based cell control architecture for FMS. It is similar to the MetaMorph I architecture (Maturana and Norrie 1996). The system consists of Task Manager, Resource Manager and several resource agents. Each resource agents represents a physical resource. Each resource agent is responsible for performing four functions: scheduling, dispatching, monitoring and error handling.) 

Overgaard, L., Petersen, H. G. and Perram, J. W. (1994). Motion Planning for an Articulated Robot: A Multi-Agent Approach. In Proceedings of Modelling Autonomous Agent in a Multi-Agent World, Odense University, pp. 171-182. (A multi-agent approach ARMOSE was proposed to control an articulated robot arm with 19 segments. Each joint of this robot was modeled as an agent that derives its positioning goal from the next agent closer to the end effector. An agent models its own location, where it wants to be, and where the next joint in line wants to be. A very interesting example in robotics.) (http://www.imada.ou.dk/) (http://www.amrose.spo.dk/) 

Ow, P.S. and Smith, S.F. (1988). A Cooperative Scheduling System. In Proceedings of the 2nd 

International Conference on Expert Systems and the Leading Edge in Production Planning and Control, pp. 43-56. (Manufacturing scheduling using the part-oriented bidding mechanism.) 

Pan, J.Y.C. and Tenenbaum, M.J. (1991). An intelligent agent framework for enterprise integration. IEEE Transactions on Systems, Man, and Cybernetics, 21(6), 1391-1408. (A software Intelligent Agent (IA) framework for integrating people and computer systems in large, geographically dispersed manufacturing enterprises. This framework is based on the vision of a very large number (e.g. 10 000) computerized assistants, known as Intelligent Agents (IAs). Human participants are encapsulated as Personal Assistants, a special type of IA.) 

Pancerella, C., Hazelton, A. and Frost, R. (1995). An autonomous agent for on-machine acceptance of machined components. In Proceedings of SPIE International Symposium on Intelligent Systems and Advanced Manufacturing, Philadelphia, PA. ( n agent architecture to support agile manufacturing.) 

Papaioannou, T. and Edwards, J. (1998). Mobile Agent technology Enabling the Virtual Enterprise: a Pattern for Database Query. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Mobile agent technology is used for enabling the virtual enterprise. Each mobile agent is used to encapsulate a single order as an order agent responsible for completion of the Sales/Order process for that order. Mobile Order Agents work with several static agents such as Sales Agents and StockControl Agents in the Sales/Order process. A good example of how to use mobile agents in Enterprise Integration.) (http://msiri.lboro.ac.uk/) 

Park, H., Tenenbaum, J. and Dove, R. (1993) Agile Infrastructure for Manufacturing Systems: A Vision for Transforming the US Manufacturing Base. Defense Manufacturing Conference. (O e of the earliest systems for agile manufacturing with negotiation over the Internet.) 

Park, H., Cutkosky, M., Conru, A. and Lee, S.H. (1994). An Agent-Based Approach to Concurrent

Cable Harness Design, AIEDAM, 8(1). (An interesting example of agent-based cooperative engineering design systems.) (http://cdr.stanford.edu/FirstLink/FirstLink.html) 

Parunak, V.D. (1987). Manufacturing Experience with the Contract Net. Distributed Artificial Intelligence, Huhns, M.N. ed., Pitman, pp. 285-310. (Description of one of the earliest agent-based manufacturing systems - YAMS (Yet Another Manufacturing System), wherein each factory and factory component is represented as an agent. Each agent has a collection of plans, representing its capabilities. The Contact Net is used for inter-agent negotiation.) (http://www.erim.org/~van/) 

Parunak, V.D. (1993). MASCOT: A virtual factory for research and development in manufacturing scheduling and control. Tech. Memo 93-02, Industrial Technology Institute. (A simulated testbed for Manufacturing Scheduling and Control. It provides a communication infrastructure, a shared ontology of manufacturing scheduling and control and a shared interface based on that ontology, and a base set of realistic modules, for the design, integration and operation of agile enterprises.) (http://www.erim.org/~van/) 

Parunak, V.D. (1996). Workshop Report: Implementing Manufacturing Agents. Sponsored by the SFA project of NCMS in conjunction with PAAM’96. NCMS. (A report on a related workshop held at PAAM’96, with summary of a number of related papers presented at PAAM’96.) (http://www.erim.org/~van/) 

Parunak, V.D., Baker, A. and Clark, S. (1998). The AARIA Agent Architecture: From Manufacturing Requirements to Agent-Based System Design. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (AARIA was related to investigating large-scale resource allocation and system simulation using autonomous agents in the context of factory scheduling. Its Advance Scheduling and schedule optimization mechanism are quite interesting.) (http://www.aaria.uc.edu/) 

Patriti V., Schaefer K., Ramos M., Charpentier P., Martin P. and Veron M. (1997). Multi-agent and manufacturing: A multilevel point of view. In Proceedings of CAPE’97, Detroit. (Proposes designing multi-agent manufacturing systems at three levels of the manufacturing processes: workshop, cell and machine-tool level. At the workshop level, an autonomous agent model was used, together with a self-organizing protocol, to facilitate the agent identification. At the cell level, the Contract Net protocol was used and modified by using genetic algorithms. At the machine tool level, a formal method was used to describe both the machine and the control system in terms of reliability.) (http://www.cran.u-nancy.fr/) 

Peng, Y., Finin, T., Labrou, Y., Chu, B., Long, J., Tolone, W.J. and Boughannam, A. (1998) A Multi-Agent System for Enterprise Integration. In Proceedings of PAAM’98, London. (A significant step towards agent based enterprise integration for manufacturing planning and execution, through experimentation with a real manufacturing scenario involving real legacy MES and scheduler.) (http://www.cs.umbc.edu/lait/research/ciimplex/) 

Petrie, C., Cutkosky, M., Webster, T., Conru, A. and Park, H. (1994). Next-Link: An Experiment in Coordination of Distributed Agents. Position paper for the AID-94 Workshop on Conflict Resolution, Lausanne. (A good example of agent-based cooperative engineering design system.) (http://cdr.stanford.edu/NextLink/NextLink.html) 

Saad, A., Biswas, G., Kawamura, K., Johnson, M.E. and Salama, A. (1995). Evaluation of Contract Net-Based Heterarchical Scheduling for Flexible Manufacturing Systems. In Proceedings of Intelligent Manufacturing Workshop at IJCAI’95, Montreal, pp. 310-321. (Description of the Production Reservation approach using a bidding mechanism based on the Contract Net protocol to generate the production plan and schedule. Negotiation between part agents and machine agents was established under two different negotiation conditions: machine-centered and part-centered.) (http://shogun.vuse.vanderbilt.edu/CIS/IMS/index.html)

Sadeh, N. and Fox, M.S. (1989). CORTES: An Exploration into Micro-Opportunistic Job-Shop Scheduling. In Proceedings of Workshop on Manufacturing Production Scheduling at IJCAI-89, Detroit. (CORTES used micro-opportunistic techniques for solving the scheduling problem through a 2-agent system. In the CORTES, each agent is responsible for scheduling a set of jobs and for monitoring a set of resources. Resources are shared in the architecture, and the sharing of a resource is coordinated by its monitor.) (http://agile.cimds.ri.cmu.edu/icll/index.html) 

Sandholm, T. and Lesser, V. (1996). Advantages of a Leveled Commitment Contracting Protocol. In Proceedings of the Thirteenth National Conference on Artificial Intelligence (AAAI-96), Portland, OR, pp. 126-133. (Description of a Leveled Commitment Contracting Protocol that allows self-interested agents to efficiently accommodate future events by having the possibility of unilaterally decommitting from a contract based on local reasoning. Its efficiency was shown through formal analysis of several contracting settings.) (http://dis.cs.umass.edu/) (http://siesta.cs.wustl.edu/~sandholm/) 

Scalabrin, E. (1996). Conception et Réalisation d’environnement de développement de systèmes d’agents cognitifs. PhD Thesis, Université de Technologie de Compiègne, France. (Dev lopment of a multi-agent framework and a multi-agent system development environment.) (http://www.hds.utc.fr/~barthes/JPB-rech.html) 

Schaefer, K., Patriti, V., Charpentier, P. Martin, P. and Spath, D. (1996). The Multi-Agent Approach in Scheduling and Control of Manufacturing Systems. In Proceedings of PAAM’96, London. (Initial proposal and research work related to that presented in (Patriti et al 1997).) (http://www.cran.u-nancy.fr/) 

Shaw, M.J. and Whinston, A.B. (1983). Distributed Planning in Cellular Flexible Manufacturing Systems. Tech. Report, Management Information Research Center, Purdue University. (Appears to be the earliest proposition to use agents in manufacturing scheduling and factory control: a manufacturing cell could subcontract work to other cells through a bidding mechanism.) 

Shaw, M.J. (1988). Dynamic Scheduling in Cellular Manufacturing Systems: A Framework for Networked Decision Making. Journal of Manufacturing Systems, 7(2), 83-94. (see above) 

Shen, W. and Barthès, J.P. (1996a). An Experimental Multi-Agent Environment for Engineering Design. International Journal of Cooperative Information Systems, 5(2-3), 131-151. (A cooperative engineering design environment using autonomous agents.) (http://www.hds.utc.fr/~barthes/JPB-rech.html) 

Shen, W. and Barthès, J.P. (1996b). Computer Supported Cooperative Environments for Engineering Design: A Survey. Tech. Report 96-122, CNRS UMR Heudiasyc, Université de Technologie de Compiègne, France. (An extensive survey of cooperative environments for engineering design, with discussions on some related key issues. About 40 related projects were reviewed.) (http://imsg.enme.ucalgary.ca/CIG/papers/csceed.pdf) 

Shen, W. and Norrie, D.H. (1998) An Agent-Based Approach for Dynamic Manufacturing Scheduling. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Combination of a bidding mechanism based on Contract Net protocol with a mediation mechanism based on Mediator architecture for dynamic manufacturing scheduling/rescheduling.) (http://ksi.cpsc.ucalgary.ca/KSI/KSI.html) (http://imsg.enme.ucalgary.ca/) 

Shen, W., Xue, D., and Norrie, D.H. (1998a). An Agent-Based Manufacturing Enterprise Infrastructure for Distributed Integrated Intelligent Manufacturing Systems. In Proceedings of PAAM’98, London, UK. (A hybrid agent-based approach for integrating manufacturing enterprise activities with its suppliers, partners and

customers within an open and dynamic environment. Description of its functional architecture, main features and a prototype implementation.) (http://imsg.enme.ucalgary.ca/) 

Shen, W., Maturana, F. and Norrie, D.H. (1998b). Learning in Agent-Based Manufacturing Systems. In Proceedings of AI & Manufacturing Research Planning Workshop, Albuquerque, NM, The AAAI Press, pp. 177-183. (A detailed discussion on learning in agent-based manufacturing system with an example from the MetaMorph I project.) (http://imsg.enme.ucalgary.ca/) 

Smith, R.G. (1980). The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver. IEEE Transactions on Computers, C-29(12), 1104-1113. (The classic paper introduces the Contract Net.) 

Sousa, P. and Ramos, C. (1997). A Dynamic Scheduling Holon for Manufacturing Orders. Journal of Intelligent manufacturing, 9(2), 107-112. (A dynamic scheduling system architecture composed of the holons representing tasks together with the holons representing manufacturing resources. The contract net protocol was used to handle temporal constraints and deal with conflicts.) (http://www.ipp.pt/ipp/) 

Sprumont, F. and Muller, J.P. (1996). AMACOIA: A Multi-Agent System for Designing Flexible Assembly Lines. In Proceedings of PAAM’96, London, UK, pp. 573-585. (Using simulated annealing to search the problem space so as to optimize the technological cost of the design of flexible assembly lines.) (http://iiun.unine.ch/Research/IA/projects/amacoia/amacoia.html) 

Stanford. (1997). JATLite. CDR, Stanford University, http://java.stanford.edu/ (Web site with information about JATLite, including JATLite Beta version for downloading, online demo, examples, source codes and more.) 

Swaminathan, J.M., Smith, S.F. and Sadeh, N.M. (1996). A Multi-Agent Framework for Supply Chain Dynamics. In Proceedings of NSF Research Planning Workshop on AI & Manufacturing, Albuquerque, NM. (An interesting example of using agents in manufacturing scheduling. See also Sadeh & Fox 1989.) (http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ozone/www/supply-chain/supply-chain.html) 

Sycara, K.P., Roth, S.F., Sadeh, N. and Fox, M.S. (1991). Resource Allocation in Distributed Factory Scheduling. Intelligent Scheduling, Zweben, M. and Fox, M.S., eds., Morgan Kaufman Publishers, San Francisco, CA, pp. 29-40 (A good example using agents in manufacturing scheduling, though it is quite simple from the agent point of view. See also Sadeh & Fox 1989.) (http://www.cs.cmu.edu/afs/cs/user/katia/www/katia-home.html) 

Tseng, M.M., Lei, M., and Su, C. (1997). A collaborative control system for mass customization manufacturing. Annals CIRP, 46(1), 373-376. (A market-like model for collaborative control with intelligent agent representation of manufacturing resources. Similar to the approach by Lin & Solberg (1992).) (http://iesu5.ust.hk/research/gmrg/member/tseng/) 

Van Leeuwen, E.H. and Norrie, D.H. (1997). Intelligent manufacturing: holons and holarchies. Manufacturing Engineer, 76(2), 86-88. (Outlines holonic concepts and architecture and describes the scope of the HMS research consortium.) (http://imsg.enme.ucalgary.ca/) 

Wang L., Balasubramanian S. and Norrie D. (1998). Agent-based Intelligent Control System Design for Real-time Distributed Manufacturing Environments. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Adoption of the PDCH (Brennan et al 1997) and IEC-1499 Function Block architecture (IEC 1997) for implementing real-time distributed manufacturing environments. Each Function Block is modeled as an agent.) (http://imsg.enme.ucalgary.ca/)

Wooldridge, M. and Jennings, N. (1995). Intelligent Agents: Theory and Practice. Knowledge Engineering Review, 10(2), 115-152. (An excellent earlier survey on intelligent agents.) (http://www.elec.qmw.ac.uk/dai/) 

Wunderli, M., Norrie, M.C., and Schaad, W. (1996). Multidatabase agents for CIM systems. International Journal Computer Integrated manufacturing, 9(4), 293-298. (A general coordination architecture proposed for CIM systems based on multi-database and agent technologies.) 

Yan, Y., Kuphal, T. and Bode, J. (1998). Application of Multi-Agent Systems in Project Management. In Working Notes of the Agent-Based Manufacturing Workshop, Minneapolis, MN. (Using mobile agents to implement service agents for realizing project management functions such as determination of the critical path, time calculation and activity scheduling. Each activity or resource needed in a project is represented by an agent. The resource agents and activity agents reside at the site of the project team members who own the resources or implement the activities. Its feasibility needs to be further studied and proved.) (http://www.uni-leipzig.de/wifa/) 

Zweben, M. and Fox, M.S. (1994). Intelligent Scheduling. Morgan Kaufman Publishers, San Francisco, CA. (A collection of papers, spanning a decade of research and development, written by experts in the field of AI planning and scheduling. Some papers describing intelligent scheduling systems using agent-based approaches have been reviewed and cited in this survey.)