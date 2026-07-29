> Source: https://cognizancejournal.com/vol6issue4/V6I402.pdf

cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Humans as Safety Constraints: A Survey 
of Human-in-the-Loop Reinforcement 
Learning for Critical Systems 
 
Kenneth Besigomwe   
East African School of Higher Education Studies and Development, Makerere University, Kampala, Uganda 
besigomwe.kenneth@students.mak.ac.ug, https://orcid.org/0009-0009-9386-2219  
 DOI: 10.47760/cognizance.2026.v06i04.002 
 
Abstract: This survey examines human involvement in safety-critical reinforcement learning (RL), 
focusing on safety enforcement rather than learning efficiency. Using a PRISMA-based systematic 
review, 100 studies published between 2010 and 2025 were analyzed across domains including 
autonomous driving, medical robotics, and power systems. The survey identifies a key gap: existing RL 
safety approaches rely heavily on algorithmic guarantees, which often fail under uncertainty, rare events, 
and high-stakes ethical trade-offs. To address this, I introduce the Human Safety Constraint Framework 
(HSCF), which formalizes human roles as preventive, corrective, advisory, and normative constraints. 
Case studies illustrate how human oversight complements algorithmic safeguards, mitigating residual 
risks and highlighting practical limitations such as cognitive load, latency, and trust calibration. The 
survey concludes that integrating human judgment as an explicit safety component is essential for robust, 
certifiable RL systems. Recommendations include developing formal models of human constraints, event-
driven intervention strategies, and scalable hybrid architectures for real-world deployment. 
 
Keywords: human-in-the-loop, reinforcement learning, safety-critical systems, hybrid safety 
architectures, human factors 
 
I. INTRODUCTION AND SCOPE 
Reinforcement learning (RL) is a class of algorithms in which an agent learns to select actions through 
trial-and-error interactions with an environment to maximize cumulative reward [1, 2]. RL has achieved state-of-the-
art performance in simulations, robotics, and games. However, its deployment in safety-critical systems requires 
fundamentally different considerations. Safety-critical systems are those in which failures can cause irreversible 
harm, including injury, loss of life, or major economic or societal consequences [3, 4]. In such domains, average 
performance metrics are insufficient because rare, high-consequence events dominate risk. Analyses across 
transportation, healthcare, and industrial automation consistently show that a small fraction of atypical scenarios 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
accounts for more than 80 percent of severe outcomes, highlighting the need for safety-focused design beyond 
standard RL objectives. 
Safety-critical RL systems often violate key assumptions of classical learning-based control. Agents may 
encounter partial observability, non-stationary dynamics, or states that differ substantially from the training 
distribution [5]. For example, autonomous vehicles experience the majority of safety-critical failures in out-of-
distribution scenarios, such as dense urban intersections or construction zones, with human safety interventions 
accounting for over 50 percent of cases in these rare conditions [6]. In surgical robotics, 10–20% of procedures 
involve complications, with a small subset of rare events accounting for the majority of severe adverse outcomes [7]. 
In industrial control, post-incident analyses indicate that unexpected interactions between automated policies and 
operators account for a disproportionate share of cascading failures [4]. These examples illustrate that low-
probability, high-impact events dominate safety risk and cannot be fully mitigated by RL training or algorithmic 
safeguards alone. 
Algorithmic safety mechanisms, including constrained optimization, control barrier functions, and safety 
shields, aim to restrict unsafe agent behavior. These mechanisms provide formal guarantees under well-characterized 
system models [8,9]. However, empirical studies show that even modest model mismatch or distributional shift can 
lead to constraint violations in long-horizon tasks, particularly in rare but critical scenarios. This underscores the 
limitations of relying solely on algorithmic safety for high-consequence applications [30]. 
Human-in-the-loop (HITL) systems address this gap by incorporating human judgment, supervision, and 
intervention directly into the control loop. Humans contribute contextual awareness, domain expertise, and ethical 
judgment that remain difficult to encode algorithmically [4]. In autonomous driving, human operators intervene to 
prevent collisions when the agent encounters complex or ambiguous situations. In medical robotics, clinicians 
supervise and override robotic actions near critical anatomy to avoid complications that automation alone cannot 
reliably prevent. In industrial automation and power systems, operators enforce regulatory safety margins and 
mitigate cascading failures. Empirical evidence across these domains demonstrates that human involvement prevents 
a substantial fraction of severe incidents, even while introducing challenges such as latency, cognitive workload, and 
variability in decision-making quality. 
Most existing work on human-in-the-loop RL frames humans primarily as tools to accelerate learning, 
provide demonstrations, or shape reward functions [4, (10-12)]. While effective in many domains, this approach is 
insufficient for safety-critical systems. In these contexts, the primary objective is the prevention of unacceptable 
outcomes, not faster convergence or higher expected return. From this perspective, humans are not merely auxiliary 
learning aids, they act as structural safety constraints, restricting or overriding agent behavior to maintain the 
operational safety envelope. 
This survey advances the thesis that humans should be treated as explicit safety constraints in safety-critical 
RL. To formalize this perspective, we introduce the Human Safety Constraint Framework (HSCF), which 
categorizes and operationalizes the ways humans enforce safety. We further illustrate its application with case 
studies in autonomous driving, medical robotics, and power systems, and discuss open challenges for scalable, 
certifiable, and reliable human-in-the-loop safety architectures. 
 
II. METHODOLOGY 
A systematic survey of human-in-the-loop reinforcement learning in safety-critical systems was conducted 
using a PRISMA-based workflow. Articles were retrieved from IEEE Xplore, ACM Digital Library, Scopus, and 
Web of Science using combinations of the keywords ―human-in-the-loop,‖ ―reinforcement learning,‖ and ―safety-
critical,‖ covering the period 2010–2025. Although the survey covers the period 2010–2025, the majority of 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
included studies are from 2022–2025. Earlier studies from 2010–2021 were largely excluded due to limited 
experimental validation or the absence of standard safety metrics. This focus ensures the survey reflects the most 
relevant and methodologically rigorous developments in human-in-the-loop reinforcement learning for safety-
critical systems. 
From 420 records identified, 50 duplicates were removed, leaving 370 unique articles for screening based 
on title and abstract. Screening excluded 230 records deemed irrelevant. The remaining 140 full-text articles were 
assessed for eligibility, of which 40 were excluded due to insufficient experimental validation or non-standard safety 
metrics. The final survey includes 100 studies, sufficient to capture the major experimental, conceptual, and applied 
contributions in human-in-the-loop reinforcement learning for safety-critical systems, forming the basis for the 
analyses presented in Sections 3–7. 
This survey does not present new experiments; rather, it develops formal definitions and mathematical 
mechanisms in Sections 3 and 4 to provide a rigorous conceptual framework for human safety constraints. These 
formulas define how humans can prevent, correct, advise, or normatively constrain agent behavior, serving as a 
common reference for interpreting the selected studies. In this way, the framework bridges existing literature with 
practical, reproducible modeling of human-in-the-loop safety in reinforcement learning systems. 
The PRISMA diagram in Figure 1 visualizes the selection process and highlights the inclusion/exclusion 
criteria, ensuring transparency and reproducibility. 
 
 Figure 1: PRISMA flow diagram of the article selection process for the survey of human-in-the-loop reinforcement 
learning in safety-critical systems. 
Source: Author 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Figure 2: Effectiveness of Literature Search Queries Based on Precision and Recall 
Source: Author 
 
III. POSITIONALITY STATEMENT 
I am a chemical process design engineer and STEM researcher focusing on artificial intelligence. My 
experience with complex industrial processes gives me insight into high-stakes environments where rare failures can 
have serious consequences. This perspective leads me to view human judgment as a key safety factor, working 
alongside algorithms to manage uncertainty, ethical trade-offs, and unexpected risks. The Human Safety Constraint 
Framework (HSCF) in this work reflects this view by defining human roles as preventive, corrective, advisory, and 
normative, showing how human oversight and automated systems must work together to maintain safety. 
 
IV. ANALYSIS AND DISCUSSION 
4.1. Safety-Critical Reinforcement Learning: Risks and Limitations 
Safety-critical systems are characterized by the potential for high-consequence failures, which can result in 
loss of life, severe injury, environmental damage, or substantial economic loss [13,14]. Empirical analyses across 
transportation, healthcare, and industrial domains indicate that a small fraction of atypical conditions accounts for a 
disproportionate share of severe incidents. For instance, over 80 percent of fatal traffic accidents involve rare 
combinations of human behavior, environmental conditions, and system interactions [15], while in surgical practice, 
approximately 15 percent of procedures experience complications, with only a minority leading to severe adverse 
outcomes [16]. These observations demonstrate that safety-critical systems are dominated by low-probability, high-
impact events, posing unique challenges for reinforcement learning (RL) agents. 
Standard RL agents typically learn policies by maximizing expected cumulative reward, often without 
explicit regard for rare catastrophic outcomes [17]. This can lead to failure modes that are unacceptable in high-
stakes applications. Key failure modes include out-of-distribution behavior, where agents encounter states not 
represented in training data, making policies unpredictable or unsafe; reward hacking and misaligned objectives, 
where agents exploit loopholes to achieve high nominal performance while violating safety constraints; 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
compounding errors in long-horizon tasks, where small estimation or model errors accumulate into catastrophic 
outcomes; and sensitivity to stochasticity and rare events, where agents fail to adequately handle low-frequency but 
dangerous conditions. For example, research in autonomous driving and other safety-critical domains highlights that 
reinforcement learning agents often encounter safety-critical events that lie outside of their training distribution, and 
performance can degrade significantly in rare or previously unseen scenarios, posing challenges for reliable 
deployment [18].  
To mitigate these risks, a variety of algorithmic safety methods have been developed. Constrained Markov 
Decision Processes (CMDPs) impose hard or soft constraints on expected cumulative cost or risk, providing formal 
guarantees under known dynamics but degrading under out-of-distribution scenarios or model uncertainty [(19-20)]. 
Control Barrier Functions (CBFs) enforce state-based safety conditions in continuous control systems, maintaining 
guarantees when system dynamics are accurately modeled but becoming sensitive to parameter mis-specification 
and unmodeled disturbances. Safety shields and intervention layers override unsafe actions in real time based on 
predefined rules or learned safety critics, improving robustness but introducing latency, restricting autonomy, and 
potentially failing in novel situations. 
Despite these safeguards, significant limitations remain. Formal guarantees often assume perfect 
knowledge of system dynamics, fully observable states, and stationary environments—assumptions frequently 
violated in deployed systems. Field data from autonomous driving and industrial automation demonstrate that even 
state-of-the-art safety algorithms cannot prevent failures in rare, out-of-distribution scenarios [4, (21-22)]. 
Algorithmic mechanisms are also inherently limited in incorporating contextual judgment, ethical reasoning, and 
complex trade-offs that human operators can handle. These studies on autonomous driving perception show that 
state-of-the-art algorithmic safety mechanisms frequently fail to generalize to out-of-distribution environments and 
rare road scenarios due to dataset and annotation limitations, leaving persistent safety gaps that necessitate human 
oversight. These observations highlight the limitations of algorithmic safety mechanisms in addressing rare, high-
consequence events. Humans complement these mechanisms by providing contextual awareness, judgment under 
uncertainty, and ethical reasoning that automated agents cannot replicate. To formalize and leverage this role, the 
Human Safety Constraint Framework (HSCF) explicitly positions humans as safety-enforcing components in 
reinforcement learning systems, laying the foundation for the conceptual and mathematical developments presented 
in the following sections. 
 
4.2. Humans as Safety Constraints: A Conceptual Framework 
In safety-critical reinforcement learning (RL), human involvement is not merely a means to accelerate 
learning or provide demonstrations. Humans serve as safety-enforcing agents, contributing judgment, contextual 
awareness, and domain expertise that are difficult to encode algorithmically [4, 23]. Human-in-the-loop (HITL) 
interventions are essential in domains where rare or unmodeled events dominate risk. Empirical studies across 
autonomous driving, medical robotics, and industrial control consistently indicate that human intervention prevents a 
substantial fraction of catastrophic incidents. For instance, disengagement reports from semi-autonomous vehicles 
show that over 50 percent of avoided collisions are due to timely human intervention in complex or out-of-
distribution scenarios. In robot-assisted surgery, comparative studies indicate that expert human supervision and 
procedural protocols are associated with modest but meaningful reductions in perioperative complications. Meta-
analytic evidence suggests that, when procedures are performed under experienced human oversight, robot-assisted 
techniques achieve relative reductions of approximately 20 % to 30 % in key adverse outcomes such as infection, 
conversion to open surgery, and overall complication rates compared to conventional approaches [100].  
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
4.3. Rethinking the Role of Humans in Safety-Critical Reinforcement Learning 
Human involvement in reinforcement learning systems has traditionally been framed as training efficiency, 
data annotation, or preference elicitation, where humans provide demonstrations, corrective feedback, or reward 
shaping signals to accelerate learning [10, (23-25)]. While this perspective suffices for non-critical applications, it 
falls short in safety-critical systems, where failures may lead to irreversible harm, legal liability, or loss of life. In 
such contexts, the central challenge shifts from merely learning an effective policy to preventing unacceptable 
behavior under uncertainty [(26-28)]. Humans contribute not just as auxiliary learning aids but as safety-enforcing 
components within the system, leveraging contextual awareness, ethical judgment, and domain expertise difficult to 
encode algorithmically especially in rare or unforeseen scenarios [4]. This motivates a reframing of human-in-the-
loop reinforcement learning, treating humans as explicit safety constraints that govern agent behavior alongside 
algorithmic safety mechanisms. The emphasis is on when and how humans restrict or shape behavior to prevent 
unsafe outcomes, rather than solely improving learning performance. 
 
4.3.1 Human Safety Constraint Framework (HSCF) 
To formalize human involvement in safety-critical reinforcement learning, I introduce the Human Safety 
Constraint Framework (HSCF), a conceptual taxonomy that categorizes human safety constraints according to their 
functional role in enforcing safety. The framework is mechanism-agnostic, focusing on what humans do to constrain 
agent behavior rather than the specific algorithmic methods used. Human safety constraints are grouped into four 
interrelated categories: preventive, corrective, advisory, and normative. 
 
 Figure 3: Human Safety Constraint Framework (HSCF). 
Source: Author 
The framework (figure 3) above categorizes human safety involvement into preventive, corrective, advisory, and 
normative roles. Humans function as safety-enforcing agents, constraining reinforcement learning behavior through 
pre-action restriction, real-time correction, guidance under uncertainty, and normative judgment. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
 
Preventive constraints act before an action is executed, limiting the agent’s permissible actions to prevent 
unsafe outcomes. In this role, humans serve as gatekeepers, using pre-action authorizations in medical robotics, 
approving high-risk maneuvers in autonomous vehicles, or defining safety envelopes in industrial control systems 
[(29-30)]. These constraints are effective when unsafe actions can be anticipated, though excessive use can introduce 
latency and reduce agent autonomy. 
Corrective constraints involve intervention during execution, allowing humans to override or modify agent 
behavior in response to unsafe conditions [4, (31-32)]. Typical mechanisms include emergency stops, manual 
takeovers, shared control, and mid-trajectory corrections. Corrective constraints are especially valuable when unsafe 
behavior cannot be reliably predicted in advance, though their effectiveness depends on human reaction time, 
situational awareness, and workload. 
Advisory constraints provide guidance without directly enforcing action restrictions. Humans influence 
decision-making by supplying risk assessments, preference feedback, or high-level recommendations [(33-35)]. 
Examples include human-provided safety scores, on-demand guidance in ambiguous states, or preference 
annotations. Advisory constraints preserve autonomy while injecting human judgment but rely on the agent’s ability 
to interpret and act on imperfect or delayed information. 
Normative constraints reflect ethical, legal, or domain-specific norms that cannot easily be encoded in 
rewards or formal constraints. Humans serve as arbiters of acceptable behavior when trade-offs arise between 
performance, safety, and societal or professional values. Examples include ethical decision-making in autonomous 
driving, regulatory compliance in aviation and healthcare, and context-sensitive judgments about acceptable risk 
[(36-37)]. Normative constraints are critical for real-world deployment, but they remain the least formalized and 
most challenging to integrate into learning systems. 
Collectively, the HSCF provides a unifying vocabulary and conceptual framework for analyzing, 
comparing, and designing human-in-the-loop safety architectures [4]. By explicitly categorizing human authority, 
the framework enables systematic evaluation of intervention roles, timing, and trade-offs, supporting principled 
integration of humans as safety-enforcing components in reinforcement learning systems. 
To formalize this perspective, I introduce the Human Safety Constraint Framework (HSCF), a conceptual 
taxonomy that categorizes human involvement in reinforcement learning systems according to the mode of safety 
enforcement. The framework is intentionally mechanism-agnostic and focuses on the functional role played by 
humans in constraining agent behavior. 
Under the HSCF, human safety constraints are classified into four categories: preventive, corrective, 
advisory, and normative. These categories are not mutually exclusive and may coexist within a single system. 
 
4.3.2. Human Versus Algorithmic Safety Constraints 
Algorithmic safety mechanisms, such as constrained Markov decision processes (CMDPs), control barrier 
functions, or safety shields, provide formal guarantees under well-defined assumptions and known system dynamics 
[38]. In reinforcement learning terms, a standard agent aims to maximize expected return. The goal of a 
reinforcement learning (RL) agent is to learn a policy that maximizes long-term reward. This objective is formalized 
as:  
 
 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
 
where π denotes a policy mapping states to actions (or a distribution over actions), π∗ is the optimal policy that 
maximizes expected cumulative reward, 𝒔𝒕and 𝒂𝒕 represent the environment state and agent action at time step t, 
respectively, with  𝒂𝒕 selected according to π, R(𝒔𝒕 , 𝒂𝒕) is the scalar reward obtained for taking action 𝒂𝒕 in state 𝒔𝒕, 
γ∈[0,1] is the discount factor weighting future rewards, T is the (finite or infinite) time horizon, and E[⋅] denotes 
expectation over the stochasticity of the environment and/or policy. 𝐀𝒓𝒈 𝒎𝒂𝒙𝝅  selects the policy π that yields the 
highest expected cumulative reward. This objective ensures optimal performance in expectation, but it does not 
guarantee safety in all individual trajectories. High expected reward can still allow rare but catastrophic outcomes. 
 
To address this limitation, algorithmic safety mechanisms impose formal constraints on the agent’s behavior by 
restricting it to a predefined set of safe states: 
 Where; 𝑺𝒔𝒂𝒇𝒆  is the safe state set, representing all states deemed acceptable according to safety specifications. The 
constraint enforces that the agent never enters unsafe states, regardless of expected reward. Such constraints are 
typically used in safety-critical applications (e.g., robotics, autonomous driving, or control systems), where 
violations may lead to physical or ethical harm. Important algorithmic methods can also incorporate human-derived 
parameters, such as risk preference or safety annotations, into the learning process via modified rewards R (𝒔𝒕 , 𝒂𝒕) 
or constraints, bridging the gap between formal guarantees and adaptive judgment. 
 
 Figure 4: Radar Chart Comparing Human and Algorithmic Safety Constraints Across Key Dimensions 
Source: Author 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Figure 4 above visualizes five key dimensions of safety constraints: formal guarantees, context awareness, 
adaptability, runtime cost, and failure severity. Human constraints excel in context awareness and adaptability, 
reflecting superior judgment in uncertain or novel situations [(39-40)]. Algorithmic constraints dominate formal 
guarantees and runtime efficiency, providing strong model-based assurances at low operational cost [(41-42)]. 
Failure severity highlights complementary vulnerabilities: humans are susceptible to fatigue and latency, whereas 
algorithms may fail due to model errors or over-conservatism [43]. The overlaid lines and shaded areas facilitate a 
quick visual comparison of strengths and trade-offs between human and algorithmic safety mechanisms. 
 
4.3.4 When Should Humans Be in the Loop? 
Determining when human safety constraints should be engaged is a key design question. Continuous 
human oversight ensures constant vigilance but imposes high cognitive and operational costs [4, (44-45)]. Fully 
autonomous operation may be unsafe in uncertain environments or when the agent encounters out-of-distribution 
states. Within the Human Safety Constraint Framework (HSCF), humans are engaged strategically when their 
judgment provides the most value. 
 
 
Where  denotes the autonomous policy and  is a binary human safety indicator that 
evaluates whether the proposed autonomous action 𝒂 is admissible in states 𝒔. When  control is 
deferred to a human-selected corrective action 𝒂𝑯, which may be deterministic or selected through direct human 
judgement.  
Humans are activated when uncertainty or estimated risk exceeds predefined thresholds, when the agent 
encounters out-of-distribution or unfamiliar states, when safety margins are approached or violated, or when trade-
offs between competing objectives require ethical or contextual judgment. This event-triggered, intermittent 
engagement balances safety with human workload, reducing fatigue while ensuring oversight during critical 
decision points. 
 
4.3.5 Implications of the Framework 
By framing humans as safety constraints, and by explicitly defining when and how human authority 
overrides autonomous decisions, the HSCF shifts the focus of human-in-the-loop reinforcement learning from how 
humans improve learning to how humans prevent unacceptable outcomes. This perspective enables clearer reasoning 
about system design, authority allocation, and failure modes, and provides a principled basis for integrating human 
oversight into safety-critical reinforcement learning systems. 
In the following sections, I build on this framework to examine concrete mechanisms for enforcing human safety 
constraints, and to analyze how human and algorithmic safety layers can be combined in practical deployments. 
 
4.4. Mechanisms for Enforcing Human Safety Constraints 
These mechanisms instantiate the authority structures and safety roles implied by the Human Safety 
Constraint Framework. Human safety constraints can be enforced through several mechanisms, which can be 
formalized mathematically. 
Preventive constraints serve as a proactive safety mechanism by restricting the agent’s available actions 
before execution. At any given state 𝒔, the allowed action set  consists of all actions 𝒂 from the full 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
action space  that have been explicitly approved by the human, as indicated by the human approval function 
. This constraint acts as a gatekeeper, ensuring that the agent cannot select or execute any action deemed 
unsafe or inappropriate by human judgment, effectively preventing hazardous behavior before it occurs. 
  
In contrast, corrective constraints provide a mechanism for real-time human intervention by enabling 
humans to override or adjust the agent’s actions dynamically. The final executed action 𝒂𝒉𝒚𝒃𝒓𝒊𝒅  is computed as a 
weighted blend of the agent’s action  𝒂𝒂𝒈𝒆𝒏𝒕 and the human’s corrective input 𝒂𝑯, controlled by a tunable parameter 
α∈ [0,1]. This parameter balances control authority, with α=1corresponding to full agent autonomy and α=0 
representing complete human control. By blending actions in this way, the system supports shared control paradigms 
where human operators can intervene as needed without completely taking over or relinquishing control. 
 
 Advisory constraints influence agent behavior indirectly by modifying reward functions or other guiding signals 
rather than imposing direct restrictions on actions.  The modified reward 
 
, 
 
adds a human-provided guidance or risk assessment term , weighted by  to the original reward  . 
This encourages the agent to favor safer or more ethical actions without hard constraints.  
 
Normative constraints encode contextual ethical, legal or domain-specific rules and can be integrated into the policy 
optimization as formal constraints on allowable actions. Extending the earlier defined optimization,  
 
 
where  denotes the set of actions permitted under normative rules, ensuring compliance with human-judged 
standards.  
 
4.5. Hybrid Safety Architectures 
Hybrid safety architectures combine human and algorithmic safety layers to constrain reinforcement 
learning agents in safety-critical systems [(46-48)]. As shown in Figure 5, the RL agent generates policies π(a|s) that 
are filtered through an algorithmic safety layer, providing formal guarantees via methods such as constrained 
Markov decision processes and safety shields, while a human safety layer delivers preventive, corrective, advisory, 
and normative constraints. The outputs of both layers feed into a hybrid safety module, which integrates these 
signals to produce actions that balance formal safety, contextual awareness, and ethical judgment. 
This structure enables authority arbitration, allowing preventive human constraints to veto unsafe actions 
prior to execution, while algorithmic mechanisms enforce runtime safety bounds. Corrective and advisory inputs are 
applied selectively, triggered by risk thresholds or unfamiliar states, ensuring human engagement is focused on high-
value interventions. Conflicts between human guidance and algorithmic recommendations are resolved 
systematically within the hybrid layer, maintaining overall safety without compromising autonomy [4, 49]. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
From a certification perspective, hybrid architectures provide an auditable safety path. Algorithmic layers 
demonstrate compliance with formal specifications, while human oversight mitigates risks in rare or unmodeled 
scenarios. By combining these complementary mechanisms, hybrid architectures enhance robustness, reduce 
reliance on any single safety modality, and facilitate safer deployment in domains such as autonomous driving, 
medical robotics, and industrial control systems [50]. 
 
 Figure 5: Hybrid Safety Architecture for Safety-Critical Reinforcement Learning 
Source: Author 
 
Figure 5 illustrates how a reinforcement learning agent’s actions are filtered through both algorithmic and human 
safety layers. Algorithmic constraints (CMDPs, safety shields) enforce formal guarantees, while human oversight 
provides preventive, corrective, advisory, and normative constraints. The hybrid layer integrates these inputs to 
ensure safer action execution, demonstrating the complementary roles of automated mechanisms and human 
judgment in safety-critical systems. 
 
4.6. Human Factors and Practical Limitations 
Human involvement in safety-critical reinforcement learning (RL) systems introduces unique challenges 
that algorithmic safety layers alone cannot address [51]. Key limitations include cognitive load, latency, trust 
calibration, and human-specific failure modes. These factors directly affect system safety, particularly in scenarios 
requiring rapid decision-making under uncertainty. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Cognitive load, defined as the mental effort required to process and respond to information during task 
performance, arises when operators must monitor complex RL agents, interpret evolving states, and intervene when 
safety thresholds are approached [(52-54)]. In telesurgery and other time-critical remote robotic applications, 
maintaining low latency is crucial: latencies ≤200 milliseconds are often cited as the ideal threshold for safe and 
responsive control, while delays approaching 400–500 milliseconds are associated with noticeable performance 
degradation and increased errors in simulation studies. Accounting for these latency constraints is essential when 
integrating human safety interventions in hybrid control architectures. [(55-57)]. 
Trust calibration refers to the alignment between a human operator’s expectations and the actual behavior 
and reliability of an autonomous system [(56, 58)]. Studies of human interaction with semi-autonomous systems 
indicate that a significant portion of manual interventions are related to mismatches between the operator’s trust and 
the system’s actual capabilities. For example, interventions can be triggered by either overconfidence or undue 
skepticism in system performance. Improvements in system transparency and feedback can reduce such 
miscalibrated trust and improve collaborative safety. 
Human failure modes encompass fatigue, distraction, and inconsistency. Unlike algorithmic safety 
mechanisms, which provide repeatable guarantees under model assumptions, humans are susceptible to stochastic 
errors that scale with task complexity and environmental stressors [(59-61)]. These limitations necessitate careful 
design of hybrid safety architectures, where human oversight is strategically engaged, rather than continuous, to 
balance vigilance with workload. 
Figure 6 presents a radar chart summarizing the relative severity of key human factors in safety-critical 
reinforcement learning. Scores are synthesized from the reviewed literature, where 1 indicates low impact and 5 
represents a critical influence on safety outcomes. The chart highlights that latency and cognitive load impose the 
greatest constraints on effective human intervention, followed by failure modes and trust calibration. By quantifying 
and visualizing these factors, system designers can identify priority areas for mitigation, inform authority allocation, 
and optimize human-in-the-loop workflows in safety-critical RL deployments. 
 
 Figure 6. Radar chart of human factors affecting safety-critical RL. 
Source: Author 
Scores reflect relative severity of cognitive load, latency, trust calibration, and failure modes on system safety. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
4.7. Case Studies in Safety-Critical Systems 
4.7.1 Rationale and Selection Criteria 
Safety-critical reinforcement learning has been explored across diverse application domains. Rather than 
attempting an exhaustive review, this survey focuses on three representative domains: autonomous driving, medical 
robotics, and power systems. These domains differ significantly in system dynamics, failure consequences, human– 
machine interaction paradigms, and regulatory oversight. They were selected because they involve real-world 
deployments or advanced prototypes that provide empirical data, exhibit distinct modes of human authority suitable 
for comparative analysis under the Human Safety Constraint Framework (HSCF), and illustrate complementary 
safety challenges that highlight the interplay of preventive, corrective, advisory, and normative constraints. This 
selection ensures coverage of systems with rapid, high-consequence events such as autonomous driving, high-risk 
localized interventions such as medical robotics, and large-scale infrastructure oversight such as power systems. The 
HSCF provides a unified framework to interpret these differences, linking human safety constraints with observed 
performance, operational trade-offs, and regulatory requirements. 
 
4.7.2 Autonomous Driving 
Autonomous driving systems operate under immediate physical safety risks and high uncertainty arising 
from perception errors, unpredictable human behavior, and rare but catastrophic edge cases [(62-64)]. Analyses of 
real-world deployments and disengagement reports consistently indicate that human safety drivers must intervene in 
complex urban scenarios, including dense intersections, construction zones, and atypical traffic behaviors. These 
interventions demonstrate that, despite advances in reinforcement learning and end-to-end driving models, humans 
continue to serve as essential corrective safety constraints in operational autonomous driving systems. 
Human safety constraints in autonomous driving manifest in three complementary roles: preventive, 
corrective, and normative. Preventive constraints restrict the operational design domain or require human approval 
for complex maneuvers such as merges or unprotected turns [65]. Corrective constraints allow safety drivers to 
disengage autonomy or assume manual control during unsafe conditions [66]. Normative constraints reflect 
adherence to traffic laws, ethical risk considerations, and acceptable trade-offs in system behavior [67]. Table 1 
summarizes the human safety constraints, enforcement mechanisms, and observed outcomes for autonomous driving 
systems based on the surveyed studies [62–67]. 
 
Table 1: Human Safety Constraints and Observed Outcomes in Autonomous Driving Systems 
Dimension Description References 
System Context Urban and highway driving [62–67] 
Human Safety Role Preventive, Corrective, Normative [62–67] 
Enforcement 
Mechanisms 
Action gating; manual takeover; rule-based 
compliance 
[65–66] 
Trigger Conditions Edge cases; perception uncertainty; near-
collision events 
[62–64] 
Observed Benefits Mitigation of catastrophic failures; regulatory 
alignment 
[65] 
Limitations Reaction latency; trust miscalibration; operator 
fatigue 
[66–67] 
Source: Author 
 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Figure 6’s radar chart visualizes key human limitations, showing that latency and cognitive load are the 
dominant factors constraining intervention effectiveness. While safety drivers prevent many critical incidents, 
reliance on sustained human vigilance introduces cognitive strain and reaction time delays. These limitations 
motivate event-triggered or confidence-aware engagement strategies, where human input is prioritized for high-risk 
events, consistent with the Human Safety Constraint Framework (HSCF). The table and narrative together illustrate 
how human authority is embedded structurally rather than incidentally in deployed systems. 
 
4.7.3 Medical Robotics 
Medical robotics involves irreversible consequences in the event of failure, stringent ethical standards, and 
close human–robot collaboration. Reviews of robot-assisted surgery consistently report low rates of major 
complications, typically on the order of a few percent or less, particularly in mature procedures and high-volume 
centers. Nevertheless, the potential severity of rare failures necessitates conservative human oversight and deliberate 
authority allocation in safety-critical surgical workflows [(68-70)]. 
Human safety constraints in medical robotics operate across preventive, corrective, and normative roles 
[71]. Preventive constraints include pre-action authorization, safety envelopes, and shared control schemes that 
restrict robot motion near critical anatomy. Corrective constraints rely on emergency stop mechanisms and 
immediate clinician override. Normative constraints enforce adherence to medical ethics, professional 
accountability, and standards of care. Table 2 summarizes the human safety constraints, enforcement mechanisms, 
and observed outcomes for medical robotics systems, highlighting preventive, corrective, and normative roles based 
on the surveyed studies [68–71].   
Table 2: Human Safety Constraints and Observed Outcomes in Medical Robotics 
Dimension Description References 
System Context Robot-assisted surgery and intervention [68–71] 
Human Safety Role Preventive, Corrective, Normative [68–71] 
Enforcement Mechanisms Pre-action approval; shared control; emergency stop [68, 71] 
Trigger Conditions High-risk maneuvers; proximity to sensitive anatomy [68–70] 
Observed Benefits Reduced procedural risk; increased clinician trust [69–70] 
Limitations Reduced autonomy; workflow disruption; cognitive load [70–71] 
Source: Author 
 
Human safety constraints in medical robotics prioritize harm avoidance over autonomy. While this enhances 
clinician trust and patient safety, it limits the degree to which reinforcement learning agents can act independently. 
Figure 6’s radar chart illustrates that cognitive load and trust calibration are particularly relevant in domains 
requiring constant human vigilance. The Human Safety Constraint Framework contextualizes these trade-offs, 
emphasizing careful allocation of authority where ethical and normative considerations dominate. 
 
4.7.4 Power Systems and Energy Infrastructure 
Power systems present large-scale, delayed consequences, with strong regulatory oversight [(72-74)]. 
Human interventions primarily focus on advisory guidance, enforcing preventive safety margins, and ensuring 
compliance with grid reliability standards. Conceptual and empirical analyses indicate that human input remains 
critical for mitigating faults and maintaining system reliability, highlighting the continued importance of supervisory 
control even in highly automated energy infrastructures. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Human safety constraints in power systems span advisory, preventive, and normative roles. Advisory 
constraints include operator guidance and risk assessment for nonstandard actions. Preventive constraints involve 
operator-defined safety margins and operational limits. Normative constraints reflect regulatory compliance and 
standards for reliability. Table 3 summarizes the human safety constraints, enforcement mechanisms, and observed 
outcomes for power systems and energy infrastructure, emphasizing advisory, preventive, and normative roles based 
on the surveyed studies [72–74]. 
 
Table 3: Human Safety Constraints and Observed Outcomes in Power Systems and Energy Management 
Dimension Description References 
System Context Grid control and energy management [72–74] 
Human Safety Role Advisory, Preventive, Normative [72–74] 
Enforcement Mechanisms Supervisory control; operating limits; regulatory rules [72–74] 
Trigger Conditions Threshold violations; instability indicators [72–73] 
Observed Benefits Improved robustness; accountability; compliance [73–74] 
Limitations Slow response to fast dynamics; operator overload [72, 74] 
Source: Author 
Unlike domains requiring immediate physical intervention, power systems emphasize deliberative human 
oversight [4]. While regulatory and advisory roles improve systemic safety, the response to fast transients can be 
limited. Hybrid safety architectures that combine automated safeguards with human supervision exemplify the 
layered, complementary constraints outlined in the HSCF. Figure 6’s radar chart highlights that latency and 
cognitive load are less critical than in real-time domains, but the complexity of supervisory decision-making remains 
an important human factor. 
 
4.7.5 Cross-Domain Synthesis 
The preceding case studies illustrate that human safety constraints are ubiquitous, but their instantiation 
varies significantly depending on system dynamics, acceptable risk, and regulatory requirements. Table 4 provides a 
concise comparison of dominant human roles, primary intervention mechanisms, and key limitations across 
autonomous driving, medical robotics, and power systems, illustrating the patterns of human involvement in safety-
critical applications based on the surveyed studies [62–74].  
Table 4: Comparative Summary of Human Roles, Mechanisms, and Limitations Across Domains 
Domain Dominant Human 
Role 
Primary Mechanism Key Limitation References 
Autonomous Driving Corrective Manual takeover Latency; cognitive 
load; trust 
miscalibration 
[62–67] 
Medical Robotics Preventive Shared control; pre-
action approval 
Reduced autonomy; 
workflow disruption; 
cognitive load 
[68–71] 
Power Systems Advisory / 
Normative 
Supervisory control; 
operating limits 
Slow response; 
operator overload 
[72–74] 
Source: Author 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
Several patterns emerge across domains. Humans assume distinct roles depending on the operational 
context: they function as corrective agents in fast, high-consequence domains such as autonomous driving, 
preventive supervisors in high-risk, localized interventions like medical robotics, and advisory or regulatory 
overseers in slow, infrastructure-scale systems such as power systems [4]. These roles are shaped by human 
limitations. Figure highlights that cognitive load and latency are critical in domains requiring rapid intervention, 
whereas trust calibration is more salient in domains demanding sustained oversight. Hybrid safety architectures 
often combine preventive, corrective, and normative constraints, and the Human Safety Constraint Framework 
(HSCF) provides a unified lens for mapping these constraints to observed outcomes, emphasizing that human 
involvement is not auxiliary but fundamental to maintaining safety. 
Recognizing these patterns informs the design of reinforcement learning agents and human-in-the-loop 
workflows. Event-triggered or confidence-aware engagement strategies can optimize the balance between human 
authority and agent autonomy, improving safety without unnecessarily constraining learning [(75-76)]. By making 
human safety constraints explicit, the HSCF enables system designers to compare, evaluate, and optimize hybrid 
architectures across domains, providing a principled foundation for allocating authority, designing intervention 
triggers, and quantifying the impact of human limitations. This structured perspective directly supports the safe 
deployment of reinforcement learning in critical applications, ensuring that human judgment complements 
algorithmic safety mechanisms effectively and systematically. 
 
4.8. Open Challenges and Future Directions 
Despite the widespread reliance on human safety constraints in deployed systems, their integration into 
reinforcement learning remains largely ad hoc. The Human Safety Constraint Framework (HSCF) highlights several 
open challenges that must be addressed to enable principled, scalable, and certifiable human-in-the-loop safety 
architectures. Figures 5 and 6 illustrate structural and human-centric perspectives that motivate these challenges. 
 
4.8.1 Formalizing Human Safety Constraints 
A central challenge lies in reconciling human safety constraints with formal safety frameworks [77]. While 
algorithmic mechanisms such as constrained Markov decision processes, control barrier functions, and safety shields 
(Figure 5) offer mathematical guarantees under well-defined assumptions, human constraints are often implicit, 
context-dependent, and difficult to formalize. Future research must explore representations that capture human 
authority without oversimplifying it into scalar rewards or hard-coded rules. Promising directions include 
probabilistic constraint models, uncertainty-aware human feedback representations, and abstractions that encode 
ranges of acceptable behavior rather than single optimal actions [78, 79]. Formalization efforts should preserve the 
flexibility and adaptability that motivate human involvement in the first place, as emphasized by comparative 
analyses in Figures 6 and the radar comparing human vs algorithmic constraints. 
 
4.8.2 Triggering and Timing of Human Intervention 
Determining when human safety constraints should be activated remains an open problem [(80-82)]. 
Continuous oversight ensures maximal coverage but is impractical due to cognitive load and operator fatigue (Figure 
6). Conversely, insufficient engagement risks delayed or ineffective intervention during critical events. Open 
research questions include how to define reliable triggers for human involvement based on uncertainty estimation, 
out-of-distribution detection, or proximity to safety boundaries. Event-driven and confidence-aware engagement 
mechanisms represent promising avenues, but their effectiveness depends on accurate risk estimation and 
transparent communication of system state to human operators [(83-84)]. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
4.8.3 Managing Human Cognitive Load and Reliability 
Human safety constraints introduce failure modes that differ fundamentally from algorithmic ones [85-86]. 
Fatigue, attentional lapses, inconsistent judgment, and delayed responses can degrade safety, particularly in 
prolonged monitoring tasks (Figure 6). Cognitive load and latency are especially critical in real-time domains such 
as autonomous driving, whereas workflow and normative constraints dominate in slower-paced or high-stakes 
systems like medical robotics and power systems (cross-domain synthesis, Section 7.5). Future systems must 
explicitly account for human limitations when assigning safety authority. This includes designing interfaces that 
support rapid situational awareness, adapting intervention frequency to operator workload, and incorporating 
redundancy across human and algorithmic safety layers [(87-88)]. Evaluating safety architectures should therefore 
consider not only worst-case system behavior, but also human reliability under realistic operational conditions. 
 
4.8.4 Authority Allocation and Conflict Resolution 
Hybrid safety architectures (Figure 5) inevitably raise questions of authority: when should human judgment 
override algorithmic decisions, and when should algorithmic safeguards constrain human actions? Resolving such 
conflicts requires clear authority hierarchies and arbitration mechanisms [(89-90)]. While hard overrides simplify 
accountability, they may reduce efficiency or conflict with regulatory constraints. Soft arbitration mechanisms, such 
as shared control or advisory vetoes, offer greater flexibility but complicate verification and responsibility 
assignment. Developing systematic approaches to authority allocation remains an open and underexplored area, 
particularly when considering the cross-domain differences highlighted in Section 7.5. 
 
4.8.5 Evaluation, Benchmarking, and Reproducibility 
Progress in human-in-the-loop safety is hindered by the lack of standardized benchmarks and evaluation 
metrics. Many existing studies rely on domain-specific simulations or small-scale user studies, limiting 
comparability and reproducibility [(91-92)]. Future work should develop benchmarks that explicitly evaluate human 
safety constraints, including intervention frequency, response latency, workload, and failure recovery. Such 
benchmarks should support controlled comparison between purely algorithmic safety mechanisms and hybrid 
approaches, enabling quantitative assessment of the trade-offs highlighted by Figures 5 and 6, as well as the radar 
chart comparing human and algorithmic constraints in Section 4. 
 
4.8.6 Certification, Regulation, and Accountability 
Safety-critical systems are subject to certification and regulatory approval, yet existing processes are 
primarily designed for deterministic or model-based control systems. The inclusion of learning agents and human-
in-the-loop safety complicates certification by introducing stochastic behavior and variable human performance 
[(93-95)]. Open challenges include defining certifiable safety envelopes for systems with intermittent human 
intervention, establishing accountability in shared-control scenarios, and aligning learning-based systems with 
evolving regulatory frameworks. Addressing these challenges will require collaboration between technical 
researchers, domain experts, and regulatory bodies. 
 
4.8.7 Toward Scalable Human-Centered Safety Architectures 
Ultimately, the scalability of human safety constraints depends on reducing human burden without 
compromising safety. This motivates research into adaptive autonomy, where human authority is dynamically 
modulated based on risk, uncertainty, and operator state [(96-99)]. The HSCF provides a foundation for such 
architectures by clarifying the roles humans play in constraining unsafe behavior. Future work should build on this 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
framework to design systems that treat human judgment as a scarce and valuable safety resource, rather than an 
always-on supervisory signal. Addressing these challenges is essential for transitioning human-in-the-loop 
reinforcement learning from experimental deployments to robust, certifiable safety-critical systems. By explicitly 
framing humans as safety constraints and connecting visual insights from Figures 5 and 6, the HSCF offers a 
principled foundation for guiding this transition. 
 
V. CONCLUSION 
Human involvement is indispensable for ensuring safety in reinforcement learning applied to high-stakes, 
safety-critical systems. While algorithmic safeguards provide baseline protections, human judgment is essential for 
handling uncertainty, rare events, and ethical trade-offs that automated systems cannot fully anticipate. The Human 
Safety Constraint Framework (HSCF) provides a structured lens to formalize and integrate human roles, but future 
research must focus on scalable methods to quantify, model, and optimize human–algorithm interactions. Event-
driven interventions, confidence-aware authority allocation, and formal evaluation metrics are key to translating 
human oversight into certifiable safety guarantees. Ultimately, reinforcing the human–algorithm partnership, rather 
than treating humans as optional supervisors, is critical for deploying reliable, accountable, and ethically responsible 
reinforcement learning systems across domains such as autonomous driving, medical robotics, and energy 
infrastructure. 
 
VI. CONFLICT OF INTEREST STATEMENT 
The author declares that there is no conflict of interest regarding the publication of this research. All data 
and findings presented in this study are based on objective analysis and have not been influenced by any financial or 
personal relationships that could be perceived as a conflict of interest. 
 
References  
1. Singh, B., Kumar, R., & Singh, V. P. (2022). Reinforcement learning in robotic applications: a comprehensive survey.  Artificial 
Intelligence Review, 55(2), 945-990. Google scholar 
2. Sivamayil, K., Rajasekar, E., Aljafari, B., Nikolovski, S., Vairavasundaram, S., & Vairavasundaram, I. (2023). A systematic study 
on reinforcement learning based applications. Energies, 16(3), 1512. Google scholar 
3. Maity, A., Banerjee, A., & Gupta, S. K. (2025). Detection of Unknown-Unknowns in Human-in-Loop Human-in-Plant Safety 
Critical Systems. IEEE Transactions on Artificial Intelligence. Google scholar 
4. Besigomwe, K. (2025). Human-in-the-Loop Self-Healing Systems: Integrating Human Oversight for Autonomous Failure 
Detection, Repair and System Optimization. Cognizance Journal of Multidisciplinary Studies, 5(3), 254–267. 
https://doi.org/10.47760/cognizance.2025.v05i03.020.  Google scholar 
5. Zhang, R., Hou, J., Walter, F., Gu, S., Guan, J., Röhrbein, F., ... & Knoll, A. (2024). Multi-agent reinforcement learning for 
autonomous driving: A survey. arXiv preprint arXiv:2408.09675. Google scholar 
6. Chen, Y., & Wang, L. (2025). Enhancing safety in AI-based object detection for autonomous vehicles through out-of-distribution 
monitoring. Google scholar 
7. Kumar, A. (2025). Reinforcement Learning for Robotic-Assisted Surgeries: Optimizing Procedural Outcomes and Minimizing 
Post-Operative Complication. Int. J. Res. Publ. Rev, 6, 5669-5684. Google scholar 
8. Besigomwe, K. (2025). Self-Healing Digital Twins for Manufacturing Process Resilience. Cognizance Journal of 
Multidisciplinary Studies, 5(3), 23–38. https://doi.org/10.47760/cognizance.2025.v05i03.003. Google scholar 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
9. Lei, H., Hua, X., Yu, W., Zheng, Y., & Wang, W. (2025). Analysis of Cascading Failure in Urban Metro Networks: A Dynamic 
Perspective Incorporating Changes in Travel Decisions. Journal of Advanced Transportation, 2025(1), 5576254. Google scholar 
10. Retzlaff, C. O., Das, S., Wayllace, C., Mousavi, P., Afshari, M., Yang, T., ... & Holzinger, A. (2024). Human-in-the-loop 
reinforcement learning: A survey and position on requirements, challenges, and opportunities. Journal of Artificial Intelligence 
Research, 79, 359-415.  
11. Kumar, S., Datta, S., Singh, V., Datta, D., Singh, S. K., & Sharma, R. (2024). Applications, challenges, and future directions of 
human-in-the-loop learning. IEEE Access, 12, 75735-75760.  
12. Kaufmann, T., Weng, P., Bengs, V., & Hüllermeier, E. (2024). A survey of reinforcement learning from human feedback. 
13. Zarei, E., Biglari, B., & Yazdi, M. (2024). Safety causation analysis in sociotechnical systems. In Safety causation analysis in 
sociotechnical systems: advanced models and techniques (pp. 1-20). Cham: Springer Nature Switzerland. Google scholar 
14. Basu, S. (2025). Plant hazard analysis and safety instrumentation systems. Elsevier.  
15. Rezwana, S., & Lownes, N. (2024). Interactions and behaviors of pedestrians with autonomous vehicles: A synthesis. Future 
Transportation, 4(3), 722-745.  
16. Samalavicius, N. E., Karpiciute, R., Nausediene, V., Willeke, F., Hansen, O. M., & Menke, V. (2024). Experiences in robotic 
colorectal surgery: comprehensive insights from a multi-center analysis using the Senhance Robotic System. Journal of robotic 
surgery, 18(1), 375.  
17. Yamagata, T., & Santos-Rodriguez, R. (2024). Safe and Robust Reinforcement Learning: Principles and Practice. arXiv preprint 
arXiv:2403.18539.  
18. Hickert, C., Yan, Z., & Wu, C. (2024, October). A Data-Informed Analysis of Scalable Supervision for Safety in Autonomous 
Vehicle Fleets. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 986-993). IEEE. 
19. Satija, H. (2024). Towards Alignment of Reinforcement Learning Agents; for Consideration of Safety, Robustness and Fairness. 
McGill University (Canada).  
20. Jamgochian, A. L. (2024). Planning Under Uncertainty in Safety-Critical Systems. Stanford University. 
21. Shoeb, Y., Nowzad, A., & Gottschalk, H. (2025). Out-of-distribution segmentation in autonomous driving: Problems and state of 
the art. In Proceedings of the Computer Vision and Pattern Recognition Conference (pp. 4310-4320).  
22. Liu, M., Yurtsever, E., Fossaert, J., Zhou, X., Zimmer, W., Cui, Y., ... & Knoll, A. C. (2024). A survey on autonomous driving 
datasets: Statistics, annotation quality, and a future outlook. IEEE Transactions on Intelligent Vehicles. 
23. Hu, H. (2025). Game-Theoretic Integration of Safety and Learning for Human-Centered Robotics (Doctoral dissertation, 
Princeton University). Google scholar 
24. Li, G., Gomez, R., Nakamura, K., & He, B. (2019). Human-centered reinforcement learning: A survey. IEEE Transactions on 
Human-Machine Systems, 49(4), 337-349.  
25. Liu, G. K. M. (2023). Transforming human interactions with AI via reinforcement learning with human feedback 
(RLHF). Massachusetts Institute of Technology.  
26. Cohen, M., & Belta, C. (2023). Adaptive and learning-based control of safety-critical systems. Springer. Google scholar 
27. Hobbs, K. L., Mote, M. L., Abate, M. C., Coogan, S. D., & Feron, E. M. (2023). Runtime assurance for safety-critical systems: 
An introduction to safety filtering approaches for complex control systems. IEEE Control Systems Magazine, 43(2), 28-65. 
28. Thames, C., & Sun, Y. (2024, April). A Survey of Artificial Intelligence Approaches to Safety and Mission-Critical Systems. 
In 2024 Integrated Communications, Navigation and Surveillance Conference (ICNS) (pp. 1-12). IEEE. Google scholar 
29. Srikumar, M., Pratt, J., Chmielinski, K., Ashurst, C., Bakalar, C., Bartholomew, W., ... & Withers, C. (2025). Prioritizing real-
time failure detection in AI agents. Partnership on AI. Google scholar 
30. Besigomwe, K. (2025). Closed-Loop Manufacturing with AI-Enabled Digital Twin Systems. Cognizance Journal of 
Multidisciplinary Studies, 5(1), 18–38. https://doi.org/10.47760/cognizance.2025.v05i01.002  
31. Benson, C., Obasi, I. C., Akinwande, D. V., & Ile, C. (2024). The impact of interventions on health, safety and environment in the 
process industry. Heliyon, 10(1). Google scholar 
32. Strauch, B. (2023). John senders, human error, and system safety. Human factors, 65(5), 766-778. 
33. Liu, Y., Caldwell, G., Rittenbruch, M., Belek Fialho Teixeira, M., Burden, A., & Guertler, M. (2024). What affects human 
decision making in human–robot collaboration?: a scoping review. Robotics, 13(2), 30.  
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
34. Segate, R. V., & Daly, A. (2024). Encoding the enforcement of safety standards into smart robots to harness their computing 
sophistication and collaborative potential: A legal risk assessment for European Union policymakers. European Journal of Risk 
Regulation, 15(3), 665-704. 
35. Rane, J., Amol Chaudhari, R., & Rane, N. (2025). Artificial Intelligence and Machine Learning for Supply Chain Resilience: 
Risk Assessment and Decision Making in Manufacturing Industry 4.0 and 5.0. Artificial Intelligence and Machine Learning for 
Supply Chain Resilience: Risk Assessment and Decision Making in Manufacturing Industry, 4. 
36. de Oliveira Silva, A. (2025). AI Ethics: A Study of Large Language Models in Autonomous Driving Scenarios (Master's thesis, 
Universidade do Porto (Portugal)). 
37. Averill, C. (2024). Algorithmic Reason-Giving, Arbitrary and Capricious Review, and the Need for a Clear Normative 
Baseline. U. Cin. L. Rev., 93, 40. 
38. Wang, Y. (2024). Safety-Assured Autonomy for Learning-Enabled Cyber-Physical Systems (Doctoral dissertation, Northwestern 
University). 
39. Zarei, E., Yazdi, M., Moradi, R., & BahooToroody, A. (2024). Expert judgment and uncertainty in sociotechnical systems 
analysis. In Safety causation analysis in sociotechnical systems: advanced models and techniques (pp. 487-530). Cham: Springer 
Nature Switzerland. 
40. Kuzmanov, I. (2025). The psychology of strategic communication and decision-making: Analytical acumen and cognitive agility 
in complex world. Journal of Novel Research and Innovative Development, 3(1), a421-a437. 
41. Esposito, M., Leva, A., Mancini, T., Picchiami, L., & Tronci, E. (2025). Simulation-Based Design of Industry-Size Control 
Systems With Formal Quality Guarantees. IEEE Transactions on Industrial Informatics. 
42. Wei, R., Jiang, Z., Mei, H., Barmpis, K., Foster, S., Kelly, T., & Zhuang, Y. (2023). Automated Model-Based Assurance Case 
Management Using Constrained Natural Language. IEEE Transactions on Computer-Aided Design of Integrated Circuits and 
Systems, 43(1), 291-304.  
43. Bahadori-Jahromi, A., Room, S., Paknahad, C., Altekreeti, M., Tariq, Z., & Tahayori, H. (2025). The role of artificial intelligence 
and machine learning in advancing civil engineering: A comprehensive review. Applied sciences, 15(19), 10499. 
44. Crootof, R., Kaminski, M. E., Price, W., & Nicholson, I. I. (2023). Humans in the Loop. Vand. L. Rev., 76, 429. 
45. Holzinger, A., Zatloukal, K., & Müller, H. (2025). Is human oversight to AI systems still possible? New Biotechnology, 85, 59-62. 
46. Ahmad, H. M., Sabouni, E., Wasilkoff, A., Budhraja, P., Guo, Z., Zhang, S., ... & Li, W. (2025). Hierarchical multi-agent 
reinforcement learning with control barrier functions for safety-critical autonomous systems. arXiv preprint arXiv:2507.14850. 
47. Yan, B., Shi, P., Lim, C. P., Sun, Y., & Agarwal, R. K. (2024). Security and safety-critical learning-based collaborative control for 
multiagent systems. IEEE Transactions on Neural Networks and Learning Systems. 
48. Zhou, J., Yan, L., & Yang, K. (2024). Enhancing system-level safety in mixed-autonomy platoon via safe reinforcement 
learning. IEEE Transactions on Intelligent Vehicles. 
49. Emami, Y., Almeida, L., Li, K., Ni, W., & Han, Z. (2024). Human-in-the-loop machine learning for safe and ethical autonomous 
vehicles: Principles, challenges, and opportunities. arXiv preprint arXiv:2408.12548. 
50. Tallam, K. (2025, October). Engineering Risk-Aware, Security-by-Design Frameworks for Assurance of Large-Scale 
Autonomous AI Models. In Proceedings of the Future Technologies Conference (pp. 209-227). Cham: Springer Nature 
Switzerland. 
51. Abbas, A. N., Amazu, C. W., Mietkiewicz, J., Briwa, H., Perez, A. A., Baldissone, G., ... & Leva, M. C. (2025). Analyzing 
operator states and the impact of ai-enhanced decision support in control rooms: a human-in-the-loop specialized reinforcement 
learning framework for intervention strategies. International Journal of Human–Computer Interaction, 41(12), 7218-7252. 
52. Howie, E. E., Dharanikota, H., Gunn, E., Ambler, O., Dias, R., Wigmore, S. J., ... & Yule, S. (2023). Cognitive load management: 
an invaluable tool for safe and effective surgical training. Journal of surgical education, 80(3), 311-322. 
53. Chakraborty, S. (2025). Supporting Sense-Making and Resilience in Distributed Cognition Systems: Managing Cognitive Load 
and Uncertainty in Traffic Control Rooms (Doctoral dissertation, ETH Zurich). 
54. Nderitu, J. H. (2023). Mental State Adaptive Interfaces as a Remedy to the Issue of Long-term Continuous Human Machine 
Interaction. Journal of Robotics Spectrum, 1, 078-089. 
55. Kuruppu Appuhamilage, G. D. K., Hussain, M., Zaman, M., & Ali Khan, W. (2025). A health digital twin framework for discrete 
event simulation based optimised critical care workflows. npj Digital Medicine, 8(1), 376. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
56. Balakrishnan, S. K. (2025). Cognitive BGP (C-BGP): AI-Driven Route Optimization for Global Internet Resilience. Geh press. 
57. Motiwala, Z. Y., Desai, A., Bisht, R., Lathkar, S., Misra, S., & Carbin, D. D. (2025). Telesurgery: Current status and strategies for 
latency reduction. Journal of Robotic Surgery, 19(1), 153. 
58. Maity, A., Banerjee, A., & Gupta, S. K. (2025). Detection of Unknown-Unknowns in Human-in-Loop Human-in-Plant Safety 
Critical Systems. IEEE Transactions on Artificial Intelligence. 
59. Xiao, X., Zhu, H., Liang, J., Tong, J., & Wang, H. (2025). A Comprehensive Review of Human Error in Risk-Informed Decision 
Making: Integrating Human Reliability Assessment, Artificial Intelligence, and Human Performance Models. arXiv preprint 
arXiv:2507.01017. 
60. Wang, T. E., & Pinto, A. (2023). Survey of Human Models for Verification of Human-Machine Systems. arXiv preprint 
arXiv:2307.15082. 
61. Wang, C. (2025). Behavioral Computing for Human Factor Security and Safety in Traffic and Transportation. In Human Factor 
Security and Safety: A Behavioral Computing Approach (pp. 219-240). Singapore: Springer Nature Singapore. 
62. Yang, K., Tang, X., Li, J., Wang, H., Zhong, G., Chen, J., & Cao, D. (2023). Uncertainties in onboard algorithms for autonomous 
vehicles: Challenges, mitigation, and perspectives. IEEE Transactions on Intelligent Transportation Systems, 24(9), 8963-8987. 
63. Chib, P. S., & Singh, P. (2023). Recent advancements in end-to-end autonomous driving using deep learning: A survey. IEEE 
Transactions on Intelligent Vehicles, 9(1), 103-118. 
64. Balammagary, S. (2024). Addressing It Failures in Autonomous Cars: Strategies for Complex Driving Situations (Doctoral 
dissertation, University of the Cumberlands). 
65. Li, L., Wang, X., & He, B. (2024, December). Design and Optimization of Safe and Efficient Human-Machine Collaborative 
Autonomous Driving Systems: Addressing Challenges in Interaction, System Downgrade, and Driver Intervention. In 2024 4th 
International Symposium on Artificial Intelligence and Intelligent Manufacturing (AIIM) (pp. 409-420). IEEE. 
66. Gao, F., Wang, X., Fan, Y., Gao, Z., & Zhao, R. (2024). Constraints driven safe reinforcement learning for autonomous driving 
decision-making. IEEE Access. 
67. Sütfeld, L. R., Bronson, J., & Kirchmair, L. (2025). Automated Vehicle Regulation Needs to Speak to Code, not to Humans: 
Keeping Safety and Ethics in the Public Domain. Philosophy & Technology, 38(1), 15. 
68. Pal, H. (2024). Advancements and limitations in integrating robotics into medicine: A comprehensive review. Multidisciplinary 
Reviews, 7(11), 2024248-2024248. 
69. Grasso, J. (2025). Robot-assisted surgery: Past, present, and future. In Digital Health (pp. 171-186). Academic Press. 
70. Abbas, S., & Watters, D. (2026). Surgical Specialization in Reconstructive Surgery, Orthopaedics, Ophthalmology, Neurosurgery, 
Cardiothoracic Surgery, Vascular Surgery and Transplantation. In The Road to Modern Surgery: A Historical Journey Through 
Surgical Landmarks (pp. 369-456). Singapore: Springer Nature Singapore. 
71. Evans, B. J. (2023). Rules for robots, and why medical AI breaks them. Journal of Law and the Biosciences, 10(1), lsad001. 
72. Besigomwe, K. (2025). Process Systems Engineering for Climate-Resilient Infrastructure: A Framework for Vulnerability 
Assessment and Optimization. Cognizance Journal of Multidisciplinary Studies, 5(1), 125–138. 
https://doi.org/10.47760/cognizance.2025.v05i01.010. Google scholar 
73. Egbumokei, P. I., Dienagha, I. N., Digitemie, W. N., Onukwulu, E. C., & Oladipo, O. T. (2024). Automation and worker safety: 
Balancing risks and benefits in oil, gas and renewable energy industries. International Journal of Multidisciplinary Research and 
Growth Evaluation, 5(4), 2582-7138. Google scholar 
74. Hanson, E., Elete, T. Y., Nwakile, C., Esiri, A. E., & Erhueh, O. V. (2024). Risk-Based maintenance and inspection in energy 
infrastructure: Future lessons for safety and efficiency. International Journal of Engineering Research and Development, 20(11), 
823-844. Google scholar 
75. Ding, X., An, Z., Rathee, A., & Du, W. (2025). A safe and data-efficient model-based reinforcement learning system for hvac 
control. IEEE Internet of Things Journal. 
76. Zhang, J., Xu, Q., Li, Z., Xu, C., & Li, K. (2025). Cooperative Safety Intelligence in V2X-Enabled Transportation: A 
Survey. arXiv preprint arXiv:2512.00490. 
77. Fox, S., & Victores, J. G. (2024, May). Safety of Human–Artificial Intelligence systems: Applying safety science to analyze 
loopholes in interactions between human organizations, artificial intelligence, and individual people. In Informatics (Vol. 11, No. 
2, p. 36). MDPI. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
78. Lagomarsino, M., Merlo, E., Pupa, A., Birr, T., Krebs, F., Secchi, C., ... & Ajoudani, A. (2025). Intuitive Programming, Adaptive 
Task Planning, and Dynamic Role Allocation in Human–Robot Collaboration. Annual Review of Control, Robotics, and 
Autonomous Systems, 9. 
79. Firoozi, R., Tucker, J., Tian, S., Majumdar, A., Sun, J., Liu, W., ... & Schwager, M. (2025). Foundation models in robotics: 
Applications, challenges, and the future. The International Journal of Robotics Research, 44(5), 701-739. 
80. Tsamados, A., Floridi, L., & Taddeo, M. (2025). Human control of AI systems: from supervision to teaming. AI and Ethics, 5(2), 
1535-1548. 
81. Sun, C., Zhang, R., Lu, Y., Cui, Y., Deng, Z., Cao, D., & Khajepour, A. (2023). Toward ensuring safety for autonomous driving 
perception: Standardization progress, research advances, and perspectives. IEEE Transactions on Intelligent Transportation 
Systems, 25(5), 3286-3304. 
82. Fui-Hoon Nah, F., Zheng, R., Cai, J., Siau, K., & Chen, L. (2023). Generative AI and ChatGPT: Applications, challenges, and AI-
human collaboration. Journal of information technology case and application research, 25(3), 277-304. 
83. Haider, T., Roscher, K., Herd, B., Schmoeller Roza, F., & Burton, S. (2024, April). Can you trust your agent? The effect of out-of-
distribution detection on the safety of reinforcement learning systems. In Proceedings of the 39th ACM/SIGAPP Symposium on 
Applied Computing (pp. 1569-1578). 
84. Wang, K., Ma, Q., Shen, C., & Lu, J. (2025). Application of Uncertainty to Out-of-Distribution Detection for Autonomous 
Driving Perception Safety. IEEE Transactions on Intelligent Transportation Systems. 
85. Thakur, A., Kaipa, K., Banerjee, A. G., Cappelleri, D. J., Krovi, V. N., & Gupta, S. (2025). Physical artificial intelligence for 
powering the next revolution in robotics. Journal of Computing and Information Science in Engineering, 25(12), 120809. 
86. Booker, S. (2025, September). Design of Everyday Control Rooms: Harnessing Fatigue, Cognitive Loading, and Next-
Generation Technologies to Improve Operator Effectiveness. In SPE Offshore Europe Conference and Exhibition (p. 
D031S013R007). SPE. 
87. Prinzel, L. J., Krois, P., Ellis, K. K., Vincent, M., Stephens, C., Oza, N., ... & Matthews, B. L. (2024). The Adaptable and 
Resilient Safety System: The Human Factor in Future In-Time Aviation Safety Management Systems. In AIAA SCITECH 2024 
Forum (p. 1603). 
88. Baruwal Chhetri, M., Tariq, S., Singh, R., Jalalvand, F., Paris, C., & Nepal, S. (2024). Towards human-ai teaming to mitigate alert 
fatigue in security operations centres. ACM Transactions on Internet Technology, 24(3), 1-22. 
89. Adams-Prassl, J., Abraha, H., Kelly-Lyth, A., Silberman, M. S., & Rakshita, S. (2023). Regulating algorithmic management: A 
blueprint. European Labour Law Journal, 14(2), 124-151. 
90. Zharova, A. K. (2023). Achieving algorithmic transparency and managing risks of data security when making decisions without 
human interference: legal approaches. Journal of Digital Technologies and Law, 1(4), 973-993. 
91. Peterson, S. L. (2025). Beyond standard benchmarking: towards robust and trustworthy robotics for industrial and nuclear 
applications (Doctoral dissertation). 
92. Li, W., Chen, Z., Lin, J., Cao, H., Han, W., Liang, S., ... & Liu, Y. (2025). Reinforcement learning foundations for deep research 
systems: A survey. arXiv preprint arXiv:2509.06733. 
93. Chougule, A., Chamola, V., Sam, A., Yu, F. R., & Sikdar, B. (2023). A comprehensive review on limitations of autonomous 
driving and its impact on accidents and collisions. IEEE Open Journal of Vehicular Technology, 5, 142-161. 
94. Perez-Cerrolaza, J., Abella, J., Borg, M., Donzella, C., Cerquides, J., Cazorla, F. J., ... & Flores, J. L. (2024). Artificial 
intelligence for safety-critical systems in industrial and transportation domains: A survey. ACM Computing Surveys, 56(7), 1-40. 
95. Tambon, F., Laberge, G., An, L., Nikanjam, A., Mindom, P. S. N., Pequignot, Y., ... & Laviolette, F. (2022). How to certify 
machine learning based safety-critical systems? A systematic literature review. Automated Software Engineering, 29(2), 38.  
96. Gallou, J., Lippi, M., Palmieri, J., Gasparri, A., & Marino, A. (2025). A Human-Centered Task Allocation and Scheduling 
Framework for Multi-Human-Multi-Robot Collaboration in Precision Agriculture Settings. IEEE Transactions on Automation 
Science and Engineering. 
97. Di Fede, G., Alrabie, L., & Andolina, S. (2025). Human-centered LLM. In Handbook of Human-Centered Artificial 
Intelligence (pp. 1-35). Singapore: Springer Nature Singapore. 
98. Gu, S., Kshirsagar, A., Du, Y., Chen, G., Peters, J., & Knoll, A. (2023). A human-centered safe robot reinforcement learning 
framework with interactive behaviors. Frontiers in Neurorobotics, 17, 1280341. 
cognizancejournal.com 
Kenneth Besigomwe, Cognizance Journal of Multidisciplinary Studies, Vol.6, Issue.4, April 2026, pg. 15-37 
(An Open Accessible, Multidisciplinary, Fully Refereed and Peer Reviewed Journal) 
ISSN: 0976-7797 
Impact Factor: 5.503 
Index Copernicus Value (ICV) = 92.57 
 
99. Mohammed, A., Sundararajan, S., & Kumar, S. (2024). Enhancing human-centered security in Industry 4.0: Navigating 
challenges and seizing opportunities. In Artificial Intelligence Solutions for Cyber-Physical Systems (pp. 214-235). Auerbach 
Publications. 
100. Fosch-Villaronga, E., Khanna, P., Drukarch, H., & Custers, B. (2023). The role of humans in surgery automation: Exploring the 
influence of automation on human–robot interaction and responsibility in surgery innovation. International Journal of Social 
Robotics, 15(3), 563–580. https://doi.org/10.1007/s12369-022-00875-0 