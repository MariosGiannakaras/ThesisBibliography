> Source: https://arxiv.org/pdf/2505.17342

A Survey of Safe Reinforcement Learning and 
Constrained MDPs: A Technical Survey on 
Single-Agent and Multi-Agent Safety 
Ankita Kushwaha1, Kiran Ravish1, Preeti Lamba1, Pawan Kumar1, Anuj Mahajan2 
1International Institute of Information Technology, Hyderabad, India 2Meta SuperIntelligence, USA 
April 30, 2026 
Abstract 
Safe Reinforcement Learning (SafeRL) is the subfield of reinforcement learning that explicitly deals with safety constraints during the learning and deployment of agents. This survey provides a mathematically rigorous overview of SafeRL formulations based on Constrained Markov Decision Processes (CMDPs) and extensions to Multi-Agent Safe RL (SafeMARL). We review theoretical foundations of CMDPs, covering definitions, constrained optimization techniques, and fundamental theorems. We then summarize state-of-the-art algorithms in SafeRL for single agents, including policy gradient methods with safety guarantees and safe exploration strategies, as well as recent advances in SafeMARL for cooperative and competitive settings. Additionally, we propose five open research problems to advance the field, with three focusing on SafeMARL. Each problem is described with motivation, key challenges, and related prior work. This survey is intended as a technical guide for researchers interested in SafeRL and SafeMARL, highlighting key concepts, methods, and open future research directions. 
Contents 
1 Introduction 2 
2 Related Work 3 
3 Safe Reinforcement Learning and Constrained MDPs: Foundations 4 3.1 Markov Decision Processes (MDPs) . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 3.2 Constrained Markov Decision Processes (CMDPs) . . . . . . . . . . . . . . . . . . 5 3.3 Constraint Types and Safety Specifications . . . . . . . . . . . . . . . . . . . . . . 8 3.4 Theoretical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 
4 State-of-the-Art Methods in SafeRL and SafeMARL 17 4.1 Lagrangian-based Policy Optimization . . . . . . . . . . . . . . . . . . . . . . . . . 18 4.2 Safety Shields and Action Correction . . . . . . . . . . . . . . . . . . . . . . . . . . 21 4.3 Risk-Sensitive and Distributional Methods . . . . . . . . . . . . . . . . . . . . . . . 22 4.4 Safe Multi-Agent Reinforcement Learning (SafeMARL) . . . . . . . . . . . . . . . 22 
5 Safe RL and Safe MARL Libraries 25 
 
 
 
 
 
 
 
 
 
 
 
 
6 Open Research Challenges and Future Directions 27 
7 Conclusion 30 
1 Introduction 
Reinforcement learning (RL) has achieved remarkable success in domains such as games, robotics, and autonomous systems. However, when deploying RL in real-world safety-critical applications (e.g., autonomous driving, healthcare, robotics), it is essential to ensure that the learning agent avoids catastrophic failures or unsafe behaviors Amodei et al. [2016], Garcia and Fernandez [2015]. Safe Reinforcement Learning (SafeRL) addresses this need by augmenting standard RL objectives with safety considerations, typically in the form of constraints on the agent’s behavior or environment outcomes. 
Definition 1.1. The goal in SafeRL is to maximize performance (cumulative reward) while satisfying safety constraints during training and deployment. 
A common framework for SafeRL is the Constrained Markov Decision Process (CMDP) introduced by Altman [1999]. In a CMDP, an agent seeks to maximize expected return subject to one or more constraints (e.g., bounds on certain costs or probabilities of unsafe events). This framework allows formalizing safety requirements as mathematical constraints and provides tools from constrained optimization and control theory to enforce them. SafeRL algorithms often leverage CMDP theory to find policies that respect constraints (at least approximately) while learning efficiently. SafeRL has gained significant attention in recent years. Early work in SafeRL explored modifications of the RL objective to encode risk or safety (e.g., worst-case guarantees Heger [1994], risk-sensitive criteria Borkar [2002], or probability of failure constraints Geibel and Wysotzki [2005]). More recent approaches explicitly enforce constraints during learning using techniques like Lagrange multipliers, trust-region methods, or safety monitors. There have been comprehensive surveys of SafeRL (e.g., Garcia and Fernandez [2015]) and increasing theoretical study of constrained RL algorithms Achiam et al. [2017], Chow et al. [2018]. An emerging frontier is Multi-Agent Safe Reinforcement Learning (SafeMARL), which considers multiple agents learning and interacting under safety constraints. SafeMARL is crucial for applications like coordinated robotics, drone swarms, and autonomous driving with multiple vehicles, where safety conditions involve interactions among agents. SafeMARL introduces additional challenges such as coordinating safety in a team, handling the coupling of constraints across agents, and new solution concepts (like safe equilibria Ganzfried [2023] in competitive settings). While single-agent SafeRL is relatively well-studied, SafeMARL remains a young research area with many open problems ElSayed-Aly et al. [2021], Gu et al. [2023]. This survey provides 
 A rigorous introduction to SafeRL formulations based on CMDPs, including mathematical definitions and theorems. 
 A review of state-of-the-art SafeRL methods for single agents, and their extensions to multiagent scenarios (SafeMARL), highlighting major algorithms and theoretical guarantees. 
 A discussion of related work and different perspectives on safety in RL (e.g., risk-sensitive RL, robust RL, safe exploration techniques). 
 Five open research problems that we believe are important for advancing SafeRL and SafeMARL. Three of these focus specifically on challenges in SafeMARL. Our target audience is researchers familiar with fundamental RL concepts who seek a deeper 
understanding of how to incorporate safety in RL. We assume knowledge of basic RL (Markov decision processes, policy optimization, etc.) and provide definitions and notation for SafeRL topics. We believe that by the end of this paper, the reader should be equipped with the theoretical background of CMDPs, knowledge of leading algorithms in SafeRL/SafeMARL, and insight into promising research directions in this field. 
A Survey of SafeRL and CMDPs 
Foundations (Sec. 3) 
Methods (Sec. 4) 
Open Problems (Sec. 5) 
MDPs 
CMDPs 
Constraint Types 
Lagrangian & LP 
Theorems 
Lagrangian Methods 
CPO / Trust Region 
Safety Shields 
SafeMARL 
Centralized (MACPO) 
Decentralized 
P1: Zero-violation 
P2: Partial Observability 
P3: Decentral. SafeMARL 
P4: Competitive SafeMARL 
P5: Non-stationarity 
Figure 1: Overview and structure of this survey. The paper covers theoretical foundations of SafeRL via CMDPs (Sec. 3), state-of-the-art methods for single-agent and multi-agent settings (Sec. 4), and five open research problems (Sec. 5). 
2 Related Work 
SafeRL has been surveyed and reviewed from multiple angles. Garc’ıa and Fern’andez Garcia and Fernandez [2015] provide an earlier comprehensive survey of SafeRL methods up to 2015, categorizing approaches into modifications of the optimality criterion (e.g., constrained or risk-sensitive objectives) and modifications of the exploration process (e.g., using external knowledge or risk metrics to guide learning). They classify safety criteria into four groups: 
 Constrained criteria – optimization with explicit constraints on policies Geibel and Wysotzki [2005], 
 Worst-case (robust) criteria – optimize the minimal possible return under adversarial conditions Heger [1994], 
 Risk-sensitive criteria – incorporate risk measures like variance or CVaR (Conditional Value-at-Risk) into the objective Borkar [2002], Tamar et al. [2015], 
 Others – e.g., criteria based on higher moments or probability of ruin. Our survey focuses primarily on the constrained criterion approach (CMDPs), which has be-
come the prevalent formalism for SafeRL in recent years. Since 2015, the field has advanced with new algorithms and theoretical results. Recent reviews such as Wachi et al. Wachi et al. [2024] examine various formulations of safety constraints (e.g., how constraints are represented and enforced) and draw connections between them. Another forthcoming survey by Gu et al. Gu et al. [2024] provides an extensive review of SafeRL methods, theory, and applications, reflecting the growing maturity of the field. Domain-specific surveys have also emerged, such as Brunke et al. Brunke et al. [2022] who provide a comprehensive review of safe RL methods for robotics. These works indicate an increasing interest in unifying SafeRL concepts and developing a systematic understanding of safety constraint representations and their implications. On the multi-agent side, SafeMARL has been less surveyed due to its emergent status. Gu et al. Gu et al. [2023] investigate safe multi-robot control tasks and propose algorithms like Multi-Agent Constrained Policy Optimization (MACPO). Some recent papers introduce safe multi-agent learning algorithms or frameworks ElSayed-Aly et al. [2021], Gu et al. [2023], Zhang et al. [2024], but a comprehensive survey of SafeMARL is still lacking. Our work contributes by reviewing both single-agent and multi-agent safe RL in one document and highlighting SafeMARL-specific challenges. Other related areas include robust RL (handling model uncertainty or adversarial disturbances) and reward hacking / alignment (ensuring the specified reward leads to intended safe behavior). 
While robust RL (e.g., solving worst-case MDPs) and SafeRL share some techniques (like min-max optimization), they address different problem formulations (uncertainty vs. explicit constraints). Similarly, reward specification and alignment problems are complementary to SafeRL: one can combine learned reward shaping with SafeRL constraints to yield agents that both seek correct objectives and stay safe Amodei et al. [2016], Achiam et al. [2017]. Benchmark suites such as the AI Safety Gridworlds Leike et al. [2017] and SafeLife Wainwright and Eckersley [2021] specifically test for specification robustness and side-effect avoidance. We touch upon these connections where relevant. In summary, our survey builds upon and extends prior work by providing a focused treatment of CMDP-based SafeRL and the novel area of SafeMARL, presented in a rigorous yet accessible manner for researchers. 
3 Safe Reinforcement Learning and Constrained MDPs: Foun-dations 
In this section, we introduce the theoretical foundations of SafeRL with an emphasis on Con-strained Markov Decision Processes (CMDPs). We present formal definitions, notation, and key mathematical results that underpin SafeRL algorithms. We also discuss how safety constraints are formulated and how they can be tackled using constrained optimization techniques in an RL context. 
3.1 Markov Decision Processes (MDPs) 
Definition 3.1 (Markov Decision Process). We begin with the standard Markov Decision Process (MDP) formulation of an RL problem. An MDP is defined by the tuple M = (S,A, P, r, γ), where 
 S is a (finite or continuous) set of states. 
 A is a set of actions available to the agent. 
 P (s′|s, a) is the transition probability function (Markovian dynamics), giving the distribution over next states s′ when action a is taken in state s. 
 r(s, a) is a reward function (or r(s, a, s′) including next state, depending on context) giving a scalar reward for executing action a in state s. 
 γ ∈ [0, 1] is a discount factor that weights immediate vs. future rewards (with γ < 1 typically for infinite-horizon problems). 
Definition 3.2 (Policy and Value Function). A (stationary) policy π is a mapping from states to a distribution over actions. We denote π(a|s) as the probability of taking action a in state s under π. The value function for a policy π is 
V π(s) = Eπ 
[ ∞∑ t=0 
γtr(st, at) | s0 = s 
] , 
the expected cumulative discounted reward starting from state s and following π. The goal in standard RL is to find an optimal policy π∗ maximizing V π(s) for all s (or maximizing a specific initial state or distribution performance). Equivalently, one maximizes the return J(π) = Es0∼ρ [V 
π(s0)] for some initial state distribution ρ. In unconstrained RL, π∗ solves maxπ J(π). 
Agent Policy π(a|s) 
Environment P (s′|s, a) 
Action at 
State st+1 
Reward r(s, a) 
Cost c(i)(s, a) 
Safety Constraint Check Jc(i)(π) ≤ di, ∀i 
Evaluate policy 
Accumulate costs 
π ∈ Πsafe: Feasible policy set 
Figure 2: The Constrained MDP (CMDP) agent-environment interaction loop. In addition to the standard reward signal r(s, a), the environment provides cost signals c(i)(s, a). The agent must find a policy π that maximizes cumulative reward while ensuring all cost constraints Jc(i)(π) ≤ di are satisfied. 
3.2 Constrained Markov Decision Processes (CMDPs) 
A Constrained Markov Decision Process extends an MDP with the concept of costs (or negative rewards) and associated constraints. Formally, a CMDP can be defined as: 
MC = (S,A, P, r, {c(i)}mi=1, γ), 
where r(s, a) is the primary reward as before, and c(i)(s, a) for i = 1, . . . ,m are m cost functions (or penalty functions) encoding the aspects of the task we want to constrain. Each cost function usually corresponds to a particular notion of “unsafe” behavior or resource usage that should be limited. For example, c(1)(s, a) might be an indicator of entering an unsafe state or a measure of damage/risk at state s. A policy π in a CMDP has not only a reward return J(π) = Eπ[ 
∑ t γ 
tr(st, at)], but also a cost return for each cost function: 
J (i) c (π) = Eπ 
[ ∞∑ t=0 
γtc(i)(st, at) 
] . 
The safe RL objective can be posed as a constrained optimization problem 
maximizeπ J(π) = Eπ 
[∑ tγtr(st, at) 
] , subject to Jc(i)(π) ≤ di, i = 1, 2, . . . ,m, (1) 
where di is a specified threshold for the i-th cost (safety limit). The set 
Πsafe = {π | Jc(i)(π) ≤ di, ; ∀i} 
is called the feasible policy set. We assume this set is non-empty (the constraints are attainable). Problem (1) is the standard 
formulation of SafeRL as a CMDP optimization problem Altman [1999]. It is a constrained Markov decision problem which, in principle, can be solved via dynamic programming or linear programming if the model is known and state-action spaces are small. Eitan Altman’s foundational work Altman [1999] established that for finite CMDPs, there exists an optimal policy that is stationary (time-independent) and, if multiple constraints are present, possibly stochastic (randomized). Intuitively, sometimes a mixture of actions is required to exactly satisfy multiple constraints: a deterministic policy might violate a constraint, whereas a stochastic policy can blend strategies to meet the constraint bounds exactly. 
Lagrangian formulation: A common theoretical approach to solve CMDPs is to form the Lagrangian of (1). Introduce Lagrange multipliers λ = (λ1, . . . , λm) ≥ 0 for the m constraints. The Lagrangian for policy π is 
L(π, λ) = J(π) + 
m∑ i=1 
λi 
( di − J (i) 
c (π) ) . 
We can rearrange L(π, λ) = J(π) − ∑ 
i λiJc(i)(π) + ∑ 
i λidi. Often it is written as J(π) −∑ i λi(Jc(i)(π)− di) or J(π)− 
∑ i λiJc(i)(π) up to constants, since 
∑ i λidi does not depend on π. 
For a fixed λ, the term 
J(π)− ∑ i 
λiJc(i)(π) = Eπ 
[∑ t 
γt(r(st, at)− ∑ i 
λic (i)(st, at)) 
] . 
This suggests defining a penalized reward 
rλ(s, a) = r(s, a)− m∑ i=1 
λic (i)(s, a). 
For any λ ≥ 0, we can compute 
π∗(λ) = argmax π L(π, λ) = argmax 
π Eπ 
[∑ t 
γtrλ(st, at) 
] , 
which is the optimal policy for the MDP with reward rλ. In other words, π(λ) is the unconstrained optimal policy if we treat −λi as a weight (penalty) for cost c(i). The dual function is 
g(λ) = max π L(π, λ) = J(π(λ)) + 
∑ i 
λi(di − Jc(i)(π (λ))). (2) 
We then minimize g(λ) over λ ≥ 0 to find the best multipliers 
λ∗ = argmin λ≥0 
g(λ). 
Under certain conditions (convexity or linearity of the CMDP problem), strong duality holds and solving the dual yields the primal optimum Altman [1999], Achiam et al. [2017]. The optimal policy π∗ for the CMDP is then π∗(λ∗) (or a mixture of policies if needed when the optimum is not unique). The Lagrangian perspective is very useful in SafeRL for the following reasons 
 It leads to Lagrange multiplier methods for safe RL, where one maintains estimates of λi 
during learning and adjusts them based on constraint violations. Many algorithms in practice (Section 4) use this primal-dual approach. 
 It gives insight into how costs trade off with reward: λi can be interpreted as the “price” of violating constraint i. A high λi at optimum means the agent sacrifices a lot of reward to reduce cost i. 
 The gradient of g(λ) can be derived as ∇λi g(λ) = di − Jc(i)(π 
∗(λ)). This leads to a gradient descent update: λi ← λi+α(Jc(i)(π)−di) which intuitively increases the penalty λi if constraint i is violated (Jc(i) > di) and decreases it if the constraint is satisfied with slack. 
Linear programming solution: For finite-state CMDPs, an alternative formulation is via occupancy measures and linear programming. One can define variables x(s, a) representing the discounted visitation frequency of state-action pair (s, a) under a stationary policy. The constraints of an optimal occupancy measure include flow conservation (infinite-horizon occupancy distribution) and positivity. 
Policy πθ 
(Primal variable) Evaluate 
J(πθ), Jc(i)(πθ) 
Penalized Reward rλ = r − 
∑ i λic 
(i) Multiplier λ ≥ 0 (Dual variable) 
Roll out episodes 
Constraint gap: J c(i) 
(πθ)− di 
Penalty weights λi 
Policy update: θ ← θ + β∇θJλ(πθ) 
Primal: maxθ 
Dual: minλ 
λi ← [λi + α(J c(i) − di)]+ 
At convergence: (π∗, λ∗) solves the CMDP 
Figure 3: The Lagrangian primal-dual optimization framework for CMDPs. The policy πθ (primal variable) is updated to maximize the penalized reward rλ, while the Lagrange multipliers λ (dual variables) are updated based on constraint violations. This alternating optimization converges to the CMDP solution under strong duality. 
The total expected discounted reward under a stationary policy π is defined as: 
J(π) = Eπ 
[ ∞∑ t=0 
γtr(st, at) 
] . 
The occupancy measure x(s, a) represents the discounted visitation frequency of state-action pairs under policy π 
x(s, a) = (1− γ) 
∞∑ t=0 
γt Pr(st = s, at = a | π) 
which is the expected discounted number of times that the agent visits state s and takes action a. By unrolling the expectation, the expected return can be rewritten in terms of the occupancy 
measure: J(π) = 
∑ s,a 
x(s, a)r(s, a) 
This expression is the key to formulating the CMDP as a linear program since the objective becomes linear in x(s, a). Furthermore, the expected cumulative cost constraints can be similarly written as 
Jc(i)(π) = ∑ s,a 
x(s, a)c(i)(s, a) ≤ di, ∀i = 1, . . . ,m 
which are also linear in x(s, a). This linear structure is crucial as it allows the CMDP optimization problem to be expressed as a linear program (LP). The CMDP can then be written as a linear program: 
max x(s,a)≥0 
∑ s,a 
x(s, a)r(s, a) 
s.t. ∑ s,a 
x(s, a)c(i)(s, a) ≤ di, i = 1, . . . ,m, 
∑ a 
x(s, a) = (1− γ)ρ(s) + γ ∑ s′,a′ 
P (s|s′, a′)x(s′, a′), ∀s, 
Ego Vehicle 
Safety zone: dsafe 
dist(st) ≥ dsafe 
RL Agent π(a|s) 
Sensors / Perception 
Safety Filter 
c(st, at) = 1[dist < dsafe] 
at 
asafe t 
st 
Reward: reach goal quickly 
Constraint: zero collisions 
Figure 4: SafeRL for autonomous driving. The RL agent receives state observations from sensors and outputs actions (steering, acceleration). A safety filter ensures the executed action satisfies the instantaneous constraint dist(st) ≥ dsafe, preventing collisions while optimizing travel efficiency. 
where ρ(s) is the starting state distribution. This linear program can be solved efficiently for moderate state-action sizes and yields an optimal (potentially stochastic) policy for the CMDP Altman [1999]. While model-based and not directly applicable to large-scale problems, this approach provides theoretical validation that CMDPs are solvable optimally and also serves as a basis for certain planning algorithms in safe RL. 
3.3 Constraint Types and Safety Specifications 
The formulation above uses expected cumulative costs as constraints. This is a flexible and popular choice in SafeRL research, but it is worth noting other types of constraints that have been considered 1. Instantaneous constraints: instead of long-term expected cost, one could require c(st, at) ≤ 
d at every time step t (almost surely). This is a stricter requirement (no violations at all). Such hard constraints are challenging for learning, and often enforced via external mechanisms (like safety filters). In CMDP theory, instantaneous constraints can be encoded by making any violation transition to an absorbing failure state with heavy penalty. 
Examples of Instantaneous Constraints in Safe RL 
Instantaneous constraints refer to safety requirements that must hold at every time step during the agent’s execution, rather than only in expectation over a trajectory. Below are typical examples of such constraints arising in real-world applications. Robotics –Torque or Force Limits Dalal et al. [2018], Cheng et al. [2019], Achiam et al. [2017]: Robotic manipulators and mobile robots have strict actuator limits. A common constraint is ||τt|| ≤ τmax, where τt is the torque vector applied at time t. Exceeding these limits even once can cause irreversible hardware damage. Therefore, the torque constraint must hold at every step. Dalal et al. Dalal et al. [2018] proposed a safety layer that projects RL actions to satisfy such constraints, while Cheng et al. Cheng et al. [2019] combined model-free RL with control barrier functions to enforce actuator limits during learning. Autonomous Driving –Collision Avoidance Shalev-Shwartz et al. [2018], Isele et al. [2018], Nguyen and Han [2023]: Autonomous vehicles must avoid collisions at all times. This is often modeled as a minimum distance constraint, distance(st) ≥ dsafe, where dsafe is a safety margin. Unlike reward penalties for collisions, instantaneous constraints aim to ensure that no collision ever occurs, even during learning. Shalev-Shwartz et al. Shalev-Shwartz et al. [2018] formalized hard safety constraints via the Responsibility-Sensitive Safety (RSS) framework, while Isele et al. Isele et al. [2018] used prediction-based constraints to safely learn intersection-handling behaviors. 
Patient State st: vitals, labs 
RL Treatment Policy π(at|st) 
Treatment at: drug dose, 
ventilator settings 
Safety Constraint doset ≤ dmax 
Pr[mortality] ≤ δ 
Patient Outcome Recovery / Adverse event 
observe 
prescribe at 
check 
safe action 
st+1 
Reward: patient recovery rt = f(vitals) 
Cost: adverse effects ct = g(doset) 
reject if unsafe 
Figure 5: SafeRL for healthcare treatment planning. The RL policy observes patient state (vitals, lab values) and prescribes treatment actions (drug dosage, ventilator settings). A safety constraint enforces dose limits (doset ≤ dmax) and bounds mortality risk (Pr[mortality] ≤ δ). Unsafe actions are rejected and the patient state evolves based on the administered treatment. 
Aerial Vehicles (Drones) –Altitude Constraints Fisac et al. [2019], Gillula and Tomlin [2012], Yuan et al. [2022]: Drones often operate within restricted altitude corridors, leading to constraints of the form zmin ≤ zt ≤ zmax. Exceeding altitude boundaries may result in collisions with terrain (if zt < zmin) or violation of airspace regulations (if zt > zmax). Such constraints must be enforced at all times. Fisac et al. Fisac et al. [2019] proposed a Hamilton-Jacobi reachability-based framework guaranteeing state constraint satisfaction for quadrotors, and Gillula and Tomlin Gillula and Tomlin [2012] demonstrated guaranteed safe online learning on a quadrotor with altitude bounds. Medical Applications –Dose Limits in Treatment Planning Tseng et al. [2017], Sprouts et al. [2022]: In adaptive radiation therapy or drug administration, instantaneous dosage constraints are essential. The instantaneous constraint may take the form doset ≤ dmax, limiting the maximum dose administered at each step to prevent severe side effects. Tseng et al. Tseng et al. [2017] developed a deep RL framework for dose fractionation in lung cancer constrained by tissue complication limits, and Sprouts et al. Sprouts et al. [2022] trained a DRL-based treatment planner enforcing hard dose-volume constraints on organs at risk. Power Systems –Voltage and Current Limits Vu et al. [2021], Duan et al. [2020]: Power grids are subject to operational safety limits such as Vt ∈ [Vmin, Vmax] for voltage levels or similar constraints on current. Violations could cause system instability, equipment damage, or even large-scale blackouts. Safe control must respect these constraints instantaneously. Vu et al. Vu et al. [2021] proposed barrier function-based safe RL for emergency voltage control with hard safety bounds, while Duan et al. Duan et al. [2020] developed a DRL-based autonomous voltage control agent that maintains voltage within operational limits. Industrial Process Control –Pressure Limits Kim and Kim [2022]: In chemical plants, nuclear reactors, and manufacturing systems, pressure constraints of the form pt ≤ pmax are typical. Exceeding pressure thresholds even once may lead to catastrophic failures such as explosions or hazardous material leaks. Kim and Oh Kim and Kim [2022] developed safe model-based RL using Lyapunov barrier functions for chemical process control (CSTR) with hard state and input constraints on temperature and pressure. These types of instantaneous constraints are significantly harder to handle than cumulative (long-term) cost constraints since they require the policy to remain within the safe region at every time step, regardless of randomness. In practice, many SafeRL algorithms enforce such constraints through external mechanisms like safety layers, control barrier functions, or shielding. 
2. Probability of failure: Here, for example, the constrain is defined as Pr(eventual failure) ≤ δ. 
If one defines a cost c(s, a) that is 1 upon entering a failure state and 0 otherwise, then Jc(π) is “essentially” the (discounted) probability of failure. A constraint Jc(π) ≤ δ limits failure probability. This can be handled in CMDP by that cost formulation Geibel and Wysotzki [2005]. 
Examples of Probability of Failure Constraints 
Probability of failure constraints aim to limit the chance that an agent enters a catastrophic or irrecoverable state throughout its lifetime. As discussed, such constraints can be formalized by defining a cost function c(s, a) which equals 1 when taking an action a in state s leads to a failure state (or belongs to a set of failure states), and 0 otherwise. The expected cumulative cost Jc(π) under this formulation directly corresponds to the probability of failure. Below are typical scenarios where such constraints are relevant. Spacecraft and Autonomous Vehicles –Safe Landing or Docking Probability Blackmore et al. [2006], Ono et al. [2015], Chow et al. [2015]: In space missions or autonomous landing scenarios, failure is often defined as crashing during landing or docking. One may enforce a constraint such as Pr[crash] ≤ δ, where δ is a small acceptable risk level. The cost function is defined as c(s, a) = 1 if (s, a) leads to a crash state. Specifically, The paper Blackmore et al. [2006] is one of the earliest works in chance-constrained motion planning and is frequently cited in spacecraft and UAV planning and Ono et al. [2015], is a classic reference on chance-constrained formulations for spacecraft landing and docking. The paper Ono et al. [2015] directly deals with probability of failure constraints for spacecraft control. Robotics: Falling or Tipping Over Berkenkamp et al. [2017], Wabersich and Zeilinger [2018], Berkenkamp and Schoellig [2015]: In humanoid or legged robots, failure is typically associated with falling down. The agent is required to maintain Pr[fall] ≤ δ to ensure physical integrity and task feasibility. In this case, any state classified as “fallen” is marked as a failure state, and c(s, a) = 1 if the next state is a fallen state. Specifically, Berkenkamp et al. [2017] is a classic paper that specifically addresses falling in legged robots and balance maintenance as a safety constraint. They model unsafe states (like falls) and ensure with high probability that they are avoided. The paper Wabersich and Zeilinger [2018] introduces a safety certification approach ensuring that robots do not enter dangerous states (including falls). It applies to both wheeled and legged robots. The earlier work Berkenkamp and Schoellig [2015] focuses on safe policy learning for balancing and preventing falls. It explicitly models unsafe states (falls) in the dynamics and safety set. Healthcare: Patient Mortality or Critical Failure Raghu et al. [2018], Gottesman et al. [2019], Jia et al. [2020], Tu et al. [2025]: In reinforcement learning for clinical decision-making (e.g., ICU treatment policies), a failure may be defined as the patient’s mortality or reaching a critical medical condition. The constraint Pr[critical failure] ≤ δ limits the treatment policy to maintain acceptable risk levels. Here, failure states correspond to medical emergencies. In particular, Raghu et al. [2018], models ICU treatment as an MDP where mortality is treated as an absorbing failure state. While optimizing expected return, they explicitly consider trajectories leading to death. In 2018, M et al. [2024] did a comprehensive study on use of RL systems for ICU treatment. Gottesman et al. [2019], proposed a foundational paper outlining safety and interpretability concerns in clinical RL. It explicitly discusses mortality and adverse outcomes as critical failure events. While not formalizing constraints as Pr[failure] ≤ δ, it motivates their necessity. Finance: Bankruptcy or Insolvency Events Neto et al. [2020], Borkar and Jain [2014], Chow et al. [2015, 2017], Schlosser [2020]: In financial portfolio management, the failure event could be the agent’s wealth dropping below a bankruptcy threshold. The probability of this event is often constrained by Pr[bankruptcy] ≤ δ to limit risk exposure. The cost function is c(s, a) = 1 if wealth crosses the bankruptcy boundary. The paper Neto et al. [2020] discusses risk-sensitive portfolio optimization with Markov decision processes. It addresses ruin (bankruptcy) probabilities explicitly. In 2014 paper Borkar and 
Jain [2014], proposes to directly deals with probability of ruin (bankruptcy) in constrained MDPs. It proposes algorithms under constraints like Pr[bankruptcy] ≤ Pr[bankruptcy] ≤ δ. The paper Chow et al. [2017] models percentile-based risk for financial RL tasks where falling below a wealth threshold triggers bankruptcy. While applied to cloud scheduling, demonstrates the same probability of ruin modeling, similar to financial insolvency constraints. Manufacturing –Production System Breakdown: In industrial automation, a failure might occur when production machinery exceeds thermal, mechanical, or chemical safety limits leading to breakdown. The probability of such system failure is constrained to be below a pre-specified threshold, e.g., Pr[breakdown] ≤ δ. Power Grids –Blackout Events: In power system control, blackouts (large-scale power failures) are often modeled as absorbing failure states. The system may enforce Pr[blackout] ≤ δ to reduce the chance of a cascading failure. Failure is usually caused by overloading, component failures, or instability. In all these scenarios, Jc(π) acts as the failure probability and CMDPs provide a natural framework for enforcing such probabilistic constraints. 
3. Risk measures: Instead of expectation of cumulative cost, one could constrain a risk measure of the return (or cost). For example, constrain the variance of return below a threshold, or ensure CVaRα(cost) ≤ δ. Some works incorporate CVaR into RL as a way to ensure low probability of catastrophic outcomes Chow et al. [2015]. These constraints often do not fit the linear structure of CMDPs, but can be tackled with specialized algorithms. 
Examples of Risk Measure Constraints 
Risk measure constraints go beyond the expectation of cumulative cost and aim to control higher-order statistics or tail behavior of the cost distribution. These constraints are useful when we are concerned not only with average performance but also with rare but high-impact events. The most common risk measures in SafeRL include variance, Value-at-Risk (VaR), and Conditional Value-at-Risk (CVaR). Below are several examples from real-world applications. Autonomous Driving –Variance-Constrained Driving Comfort: While avoiding collisions is a safety constraint, maintaining comfortable driving also involves controlling the variance of acceleration, jerk, or lane deviations. A variance constraint of the form Var [ 
∑ t c(st, at)] ≤ δ 
can ensure that passenger discomfort due to aggressive or unstable maneuvers remains limited, reducing the risk of loss of control or accidents. Specifically, in 2012, Tamar et al. [2012], introduced variance-constrained reinforcement learning where variance of return is explicitly controlled. It is applicable to driving scenarios when controlling variance of acceleration or jerk. Huang et al. [2026] explicitly focuses on reducing control variability to improve smoothness and driving comfort. In 2021 Kiran et al. [2022] wrote a comprehensive survey that discusses driving comfort (acceleration, jerk minimization, smoothness) as key secondary objective in autonomous driving, and mentions various papers that incorporates constraints. Finance: CVaR-Constrained Portfolio Optimization: In financial portfolio management, it is common to limit the Conditional Value-at-Risk (CVaR) of the portfolio’s return. A CVaR constraint CVaRα[loss] ≤ δ ensures that the expected loss in the worst α% of cases does not exceed a tolerable threshold. This is widely used to manage downside risk beyond what variance alone captures. A seminal paper on optimization of conditional Value-at-Risk was by Rockafellar and Urya-sev [2000] for portfolio problems. In 2014, Prashanth [2014] specifically focuses on CVaR-constrained MDPs with application to financial risk. This is the go-to reference in both optimization and financial risk management. In 2015, Chow et al. [2015], introduces CVaR-constrained RL applicable to portfolio optimization and other decision-making tasks. It provides methods to enforce CVaR constraints in sequential decision-making. In the same year Tamar et al. [2015], introduces policy gradient methods for risk-sensitive criteria including CVaR. It directly applies to portfolio optimization under CVaR constraints. Healthcare: CVaR for Adverse Outcomes: In healthcare applications such as treatment plan-
Market st: prices, indicators 
RL Portfolio Agent π(at|st) 
Allocation at: portfolio weights 
w1, w2, . . . , wn 
Risk Constraint CVaRα[loss] ≤ δ 
Portfolio Returns rt = 
∑ i wi · Ri 
Loss 
Prob 
VaRα CVaRα 
Tail risk 
observe 
allocate 
risk check 
execute trade 
st+1 
Reward: maximize 
expected return 
Cost: tail losses 
Pr[ruin] ≤ δ 
Figure 6: SafeRL for risk-constrained portfolio management. The RL agent observes market state and outputs portfolio allocations. A CVaR constraint CVaRα[loss] ≤ δ limits tail risk, ensuring the expected loss in the worst α% of scenarios stays bounded. The inset shows the loss distribution with the CVaR tail region highlighted. 
ning or resource allocation, minimizing the expected number of adverse events may not be sufficient. A CVaR constraint on cumulative adverse events or side effects ensures that treatment policies control the likelihood of rare but severe negative outcomes. Although general, the paper Prashanth and Ghavamzadeh [2013] is frequently cited in healthcare RL as it provides risk-sensitive methods including CVaR for controlling adverse events. A position paper Gottesman et al. [2019] emphasizes that minimizing expected adverse outcomes is insufficient and recommended the use of risk measures (e.g., CVaR). Although it doesn’t present an algorithm, it motivates CVaR as a necessary tool in treatment planning. To summarize, CVaR is used in healthcare RL to limit the risk of rare but severe adverse events, to model tail risk (e.g., mortality, critical organ failure, side effects), and to design safe treatment policies under uncertainty. Supply Chain Management –Risk-Averse Inventory Control: In supply chains, stockout events (inventory drops below zero) cause disruptions. Instead of just minimizing expected stockouts, a CVaR constraint on stockout penalties ensures that even in rare demand spikes, the risk of large cumulative stockouts is controlled. One of the foundational works on risk-averse inventory control, discusses CVaR and other risk measures Chen et al. [2007]. It models stockouts as undesirable events and controls the risk via dynamic programming. Widely used as a textbook, Shapiro et al. [2021] includes detailed treatment of CVaR in supply chain optimization. It explains how risk measures such as CVaR can control stockouts and demand uncertainties. While not supply chain specific, Chow et al. [2015] is often cited in supply chain literature for inventory control under CVaR constraints. It’s techniques directly apply when modeling stockouts as risky events. A highly cited paper is Bertsimas and Thiele [2006] showing how robust optimization (a precursor to CVaR-type models) controls stockout risks. Provides insight into handling demand uncertainty and stockout penalties. Robotics –CVaR-Constrained Trajectory Optimization: For autonomous robots navigating uncertain environments, one may use CVaR constraints on cumulative collision risk or energy consumption. This ensures that the robot does not just minimize average risk but is also robust against worst-case environmental uncertainties or adversarial perturbations. The paper Ahmadi et al. [2022] directly studies CVaR-constrained trajectory optimization for robots under uncertainty (see also Hakobyan et al. [2019], Ahmadi et al. [2021], Bian et al. [2023] for CVaR-based motion planning and path planning). Formulates trajectory optimization problems where collision risk is controlled using CVaR. The paper Yu et al. [2026] focuses on risk-averse path planning under environmental uncertainty using CVaR. Provides algorithms 
and examples for safe robot navigation with collision risk control. Power Systems –Risk-Sensitive Stability Control: In power grid operations, rather than just minimizing expected frequency deviations or power outages, operators may use CVaR or variance constraints to ensure that the probability of large-scale instabilities remains acceptably low, accounting for rare but impactful demand or supply fluctuations. The paper Bitar and Xu [2017] addresses reliability and demand uncertainties in power systems with a risk-sensitive approach. It Models constraints on load shedding and supply-demand balancing. The paper Dall’Anese et al. [2017] directly introduces chance-constrained optimization for voltage stability and power flow Zhang and Li [2011], which is equivalent to controlling the probability of instability; CVaR and probability bounds are discussed. In 2012, Roald et al. [2014] introduces risk-constrained OPF formulations using CVaR and chance constraints. It ensures that the probability of voltage violations and instabilities is below a prescribed risk level. A year earlier in 2011, Wang et al. [2025] models the variance and tail risk of power system instability due to fluctuating wind generation. While not CVaR directly, it motivates variance and higher-order moment-based risk constraints. Power systems use variance, probabilistic, and CVaR constraints to: Avoid rare but catastrophic blackouts, to maintain voltage and frequency within safe margins, and to ensure reliability under demand and renewable generation uncertainty. Risk measures provide a flexible modeling tool for specifying safety, robustness, and fairness. However, incorporating them often requires non-standard methods such as CVaR-optimized policy gradients, distributional reinforcement learning, or scenario-based optimization, as these constraints typically violate the linear structure required for classic CMDP formulations. 
4. Multi-objective viewpoint: SafeRL can be seen as a multi-objective optimization where one objective is reward and others are (negative) costs Horie et al. [2019], Gu et al. [2025]. The constraint formulation picks one point on the Pareto frontier by treating costs as hard constraints. Alternatively, one could combine reward and costs into a single scalar reward via weighted sum (penalty method), but that requires tuning weights and does not guarantee constraint satisfaction Achiam et al. [2017]. Constrained formulation cleanly separates objectives and safety. 
Examples of Multi-Objective Viewpoint in Safe Reinforcement Learning 
In many real-world applications, agents must simultaneously optimize multiple objectives that may conflict. Typically, SafeRL is modeled as a multi-objective problem where one objective is the primary reward, while others are safety-related costs. The CMDP formulation addresses this by enforcing costs as hard constraints, selecting a specific point on the Pareto frontier. Alternatively, some works use a scalarization (penalty) method by combining reward and costs into a single objective. Below are common examples illustrating the multi-objective viewpoint. Robotics –Speed vs. Safety Trade-off Achiam et al. [2017], Berkenkamp et al. [2017], Chow et al. [2018]: A mobile robot navigating in an environment may aim to maximize the reward associated with reaching the goal quickly. However, it also needs to minimize the probability of collisions and energy consumption. Here, speed contributes positively to the reward, while collisions and energy usage are treated as negative costs. The CMDP formulation could enforce a maximum acceptable collision rate and energy budget, leading to an explicit safety-performance trade-off. Autonomous Driving –Travel Time vs. Accident Risk Dalal et al. [2018], Shalev-Shwartz et al. [2018], Zheng and Gu [2025], Nguyen and Han [2023]: In autonomous driving, agents aim to minimize the expected travel time while simultaneously ensuring a low probability of accidents. The agent faces a trade-off between driving faster (leading to higher reward) and maintaining safe distances or reduced speeds to avoid collisions (cost). The Pareto frontier consists of policies ranging from conservative (low accident risk, long travel time) to aggressive (low travel time, high accident risk). SafeRL selects a policy on this frontier according to the safety constraint. Energy Systems –Power Supply vs. Cost and Reliability Bitar and Xu [2017], Dall’Anese et al. [2017]: In power grid management, the agent may aim to optimize electricity production to 
meet demand (reward) while minimizing costs associated with fuel consumption and the risk of violating reliability standards (costs). This problem naturally involves multiple objectives: maximizing supply quality and minimizing operational risks and costs. Healthcare: Treatment Success vs. Adverse Effects Gottesman et al. [2019], Raghu et al. [2018]: In medical decision-making, an RL agent may need to maximize treatment efficacy while minimizing adverse effects or treatment toxicity. For example, maximizing patient recovery speed could conflict with the need to limit drug dosage to avoid harmful side effects. A CMDP constraint could limit the expected cumulative adverse effects to a tolerable threshold, enforcing safety. Manufacturing: Production Efficiency vs. Maintenance Costs Li et al. [2023], Siraskar et al. [2023], Chen and Zhou [2025]: In automated manufacturing, increasing production speed or output (reward) may result in higher machine wear and maintenance costs (costs). A CMDP-based SafeRL framework may impose a constraint on expected maintenance cost or machine degradation, forcing the agent to balance throughput and longevity. Drone Swarms: Task Completion vs. Communication Load Gu et al. [2023]: In multi-drone systems, agents may wish to maximize task completion rates (reward) while minimizing communication overhead (cost). Communication constraints can act as safety constraints in environments with bandwidth limitations or interference risks. In all these cases, treating costs as hard constraints via CMDPs gives a systematic way to trade off reward and cost by directly selecting a feasible point on the Pareto frontier. In contrast, using a scalarization approach (reward minus weighted costs) can lead to policies that violate constraints unless the weights are carefully chosen and tuned. 
5. Temporal logic specifications Alshiekh et al. [2018], ElSayed-Aly et al. [2021], Turchetta et al. [2016], Wabersich and Zeilinger [2018]: In some safety-critical settings, the safety requirement is given as a formal temporal logic formula (e.g., “always avoid region X unless Y happens”). Such logic specifications can be converted to automata and then to reward/cost functions or shields that enforce them Alshiekh et al. [2018], ElSayed-Aly et al. [2021]. While not a traditional CMDP constraint, they can often be incorporated by extending the state space to include automaton states representing the satisfaction of the formula. Specif-ically, in Alshiekh et al. [2018], Alshiekh et al. (2018) introduced safe reinforcement learning via shielding; they used LTL (Linear Temporal Logic) specifications to construct shields for RL agents. In Wabersich and Zeilinger (2018) Wabersich and Zeilinger [2018], linear model predictive safety certification for learning-based control was employed. Although it focused on model predictive safety, their framework is capable of incorporating logic-based safety constraints. The paper ElSayed-Aly et al. [2021] extends shield-based safe RL to the multi-agent setting using temporal logic specifications. The paper Turchetta et al. [2016] while focused on safe exploration, their work shows how formal safety specifications can be integrated into exploration guarantees. One of the older but influential paper Sadigh et al. [2016] shows how specifications from temporal logic can shape safe planning. Throughout this survey, we largely assume the standard expected cumulative cost constraints 
unless stated otherwise. This assumption covers many practical cases (like average constraint violation rate, or total resource consumption) and has well-developed theoretical tools. When discussing specific algorithms, we will note what type of constraint they handle (most often, it is expected cost). 
3.4 Theoretical Results 
We highlight a few key theoretical results for CMDPs relevant to SafeRL: 
Safe RL (CMDP) 
Autonomous Driving 
Healthcare 
Finance 
Robotics 
Power Systems 
Manufacturing 
dist(st) ≥ dsafe 
doset ≤ dmax 
CVaRα ≤ δ 
∥τt∥ ≤ τmax 
Vt ∈ [Vmin, Vmax] 
Pr[fail] ≤ δ 
Figure 7: Application domains of Safe Reinforcement Learning. Each domain connects to the CMDP framework through domain-specific safety constraints: collision avoidance in autonomous driving, dosage limits in healthcare, risk measures (CVaR) in finance, actuator limits in robotics, operational bounds in power systems, and failure probability in manufacturing. 
Safety Constraint Types in SafeRL 
Instantaneous c(st, at) ≤ d, ∀t 
Expected Cumulative Jc(π) ≤ d 
Probability of Failure 
Pr[fail] ≤ δ 
Risk Measures CVaR, Variance 
Temporal Logic LTL specifications 
Hard per-step limits. Torque, collision avoid. 
Long-run average cost. Most common in CMDPs. 
Bound on catastrophic event probability. 
Tail risk via CVaRα or variance bounds. 
Formal specs via automata and shields. 
Strictest ←→ Most flexible 
Figure 8: Taxonomy of safety constraint types in SafeRL. Instantaneous constraints are the strictest (must hold at every time step), while expected cumulative constraints (the standard CMDP formulation) are the most common. Probability of failure, risk measures, and temporal logic specifications offer alternative ways to encode safety requirements. 
Theorem 3.3 (Optimal Policy for CMDP Altman [1999]). For a finite CMDP with bounded rewards and costs, there exists an optimal policy (π∗, λ∗) that attains the maximum in (1) (and corresponding optimal dual variables). Moreover, there exists an optimal policy that is stationary (time-independent) and can be chosen to be deterministic with respect to actions at all but possibly a measure-zero set of states. In practice, optimal policies may randomize between a small number of deterministic policies if needed to exactly satisfy constraints. 
In short, one does not need complex history-dependent or non-Markovian policies to solve CMDPs optimally; memoryless policies suffice, simplifying the search space for algorithms. 
Theorem 3.4 (Lagrange Duality Altman [1999]). Under mild regularity conditions (e.g., finite state/action or convexity in policy space), The strong duality holds for the CMDP problem. That is, 
min λ≥0 
max π L(π, λ) = max 
π min λ≥0 
L(π, λ), 
and solving the dual yields the primal optimum. The optimal dual variables λ∗ provide valuable information: if λ∗i > 0, then the i-th constraint is active (tight) at the optimum; if λ∗i = 0, the optimum policy naturally satisfies i-th constraint with some slack. 
This theorem justifies many SafeRL approaches that focus on solving the dual via gradient methods on λ while finding optimal policies for a given λ using RL. 
Proposition 3.5 (Policy Gradient for Constrained Objectives). If the policy πθ is parameterized by θ (e.g., a neural network), one can derive gradients for the constrained problem. For instance, using the Lagrangian, the gradient of L(πθ, λ) with respect to θ is 
∇θL = ∇θJ(πθ)− ∑ i 
λi∇θJ (i) c (πθ). 
This leads to constrained policy gradient algorithms, where θ is updated in the direction of ∇θL and λ is updated in the direction of ∇λL = di − Jc(i)(πθ). Many actor-critic style SafeRL methods employ this simultaneous gradient update (a form of primal-dual gradient descent) Chow et al. [2018]. 
Proposition 3.6 (Policy Performance Bounds Achiam et al. [2017]). For any two policies π and π′, let J(π) denote the expected reward return, and JCi 
(π) denote the expected return for a cost function Ci. The change in performance when updating from π to π′ is bounded as (as given by Corollary 1 and Corollary 2 of Achiam et al. [2017]). Reward (Lower Bound): The improvement in expected reward is bounded by 
J(π′)− J(π) ≥ 1 
1− γ Es∼dπ, a∼π′ 
[ Aπ(s, a) 
− 2γϵπ ′ 
1− γ DTV (π 
′∥π)[s] ] . (3) 
Cost (Upper Bound): The change in expected cost is bounded by 
JCi(π ′)− JCi(π) ≤ 
1 
1− γ Es∼dπ, a∼π′ 
[ Aπ 
Ci (s, a) 
+ 2γϵπ 
′ 
Ci 
1− γ DTV (π 
′∥π)[s] ] . (4) 
Here, Aπ and Aπ Ci 
are the advantage functions for the reward and cost, respectively; dπ is the state distribution of policy π; the ϵ terms represent the maximum absolute advantage values; and DTV denotes the Total Variation divergence. 
Sketch of proof, detail in Achiam et al. [2017]. (1) Reward-shaping identity and surrogate. For any f : S → R define δf (s, a, s 
′) := R(s, a, s′) + γf(s′)− f(s) and 
Lπ,f (π ′) := Es∼dπ, a∼π′, s′∼P 
[(π′(a|s) π(a|s) − 1 
) δf (s, a, s 
′) ] . 
Using the discounted visitation measures one shows 
J(π′)− J(π) = 1 
 (Edπ′ [δf ]− Edπ [δf ]) , 
and by adding/subtracting ⟨dπ, δπ ′ 
f ⟩ and applying Hölder’s inequality, Achiam et al. [2017] obtain the two-sided bound 
1 
1−γ 
( Lπ,f (π 
′)− 2 ∥π′∥f DTV (d π′ ∥dπ) 
) ≤ J(π′)− J(π) 
≤ 1 
1−γ 
( Lπ,f (π 
′) + 2 ∥π′∥f DTV (d π′ ∥dπ) 
) , 
where ∥π′∥f := maxs ∣∣Ea∼π′ [δf (s, a, s 
′)] ∣∣. 
(2) From DTV (d π′∥dπ) to statewise TV between policies. Bound the shift in discounted 
visitation by the average per-state TV between action distributions, yielding 
DTV (d π′ ∥dπ) ≤ γ 
1−γ Es∼dπ 
[ DTV (π 
′∥π)[s] ] . 
Substituting this into the previous display gives the Theorem 1 bounds in Achiam et al. [2017]. (3) Choose f to recover advantages. Setting f = V π makes Es′∼P [δf |s, a] = Aπ(s, a), and 
∥π′∥f becomes ϵπ ′ := maxs |Ea∼π′ [Aπ(s, a)]|, yielding 
J(π′)− J(π) ≥ 1 
1− γ Es∼dπ, a∼π′ 
[ Aπ(s, a)− 2γ ϵπ 
′ 
1− γ DTV (π 
′∥π)[s] ] , 
which is Eq. (3) (lower bound). Likewise, taking f = V π Ci 
produces the cost version with Aπ Ci 
and 
ϵπ ′ 
Ci , giving Eq. (4) (upper bound). 
These bounds are significant as they justify using the expected advantage (the first term inside the expectation) as a surrogate objective for policy optimization. The bounds formally characterize the worst-case approximation error (the second term) that arises from using the state distribution dπ of the old policy instead of the new policy’s distribution dπ 
′ . 
Safe exploration and probably safe learning: A distinction in SafeRL theory is between methods that guarantee safety during learning vs. only at convergence. Most theoretical results (like the ones above) ensure that the final learned policy can satisfy constraints. Ensuring that intermediate policies (during training) also satisfy constraints is much harder. Constrained policy optimization approaches (Section 4) aim to maintain safety at each iteration by conservative updates Achiam et al. [2017]. Another line of work uses PAC-style analysis or high-probability bounds to derive exploration strategies that with high probability never violate constraints beyond a tolerance Turchetta et al. [2016], Berkenkamp et al. [2017]. These often rely on optimistic models or Lyapunov functions to formally verify safe regions of state-space the agent can explore. Though we do not delve into detailed proofs, we note that providing safety guarantees during learning typically requires additional assumptions (such as mild system dynamics, or an initial safe policy to bootstrap from). Having established the CMDP framework and theoretical background, we now move on to discuss concrete algorithms and methods developed for SafeRL, both in the single-agent case (Section 4) and multi-agent extensions (Section 5). 
4 State-of-the-Art Methods in SafeRL and SafeMARL 
In this section, we survey major methods and algorithms in Safe Reinforcement Learning, covering both single-agent SafeRL in CMDP settings and extensions to multi-agent SafeMARL. We organize the discussion by methodological categories, explaining how each approach incorporates safety and highlighting key algorithms. For each category, we provide examples of state-of-the-art techniques and cite representative works. 
SafeRL & SafeMARL Methods 
Constrained Optimization Safety Shields Risk-Sensitive Multi-Agent 
Extensions 
Lagrange Actor-Critic 
CPO (Trust Region) 
Lyapunov-based 
PCPO (Projection) 
Safety Layer (QP) 
LTL Shielding 
Human Oversight 
CVaR Optimization 
Distributional RL 
MACPO (Centralized) 
Decentralized (κ-hop) 
Shielded MARL 
Stackelberg SafeRL 
Sec. 4.1 
Sec. 4.2 
Sec. 4.3 
Sec. 4.4 
Figure 9: Taxonomy of SafeRL and SafeMARL methods surveyed in this paper. Methods are categorized into four groups: constrained optimization approaches (Sec. 4.1), safety shield mechanisms (Sec. 4.2), risk-sensitive methods (Sec. 4.3), and multi-agent extensions (Sec. 4.4). 
4.1 Lagrangian-based Policy Optimization 
One broad class of SafeRL algorithms uses the primal-dual (Lagrangian) approach discussed earlier to enforce constraints. The idea is to transform the constrained problem into a sequence of unconstrained problems with adjusted rewards. 
Lagrangian Actor-Critic: In this approach, one augments the standard RL loss with penalty terms for constraint costs. For example, one can define a penalized reward rλ(s, a) = r(s, a) − λc(s, a) (eqn (11) in Tessler et al. [2019]) for a single-constraint problem, where λ is treated as a learnable parameter. An actor-critic algorithm (Algorithm 1 in Tessler et al. [2019]) can then be used: The actor (policy πθ) is updated with respect to the penalized objective Jpen(π) = J(π)− λJc(π), using policy gradient or other optimization. The critic(s) estimate both the value of the reward and the cost (often one critic for V π(s) and one for V π 
c (s)). The Lagrange multiplier λ is updated by gradient ascent on the constraint satisfaction term, e.g. λ ← λ + β(Jc(π) − d). This simple scheme is often called the Lagrange method or reward shaping method in safe RL. It was used in early safe deep RL implementations (e.g., Tessler et al. [2019] for safe DQN with constraints, and policy-gradient variants, i.e., Trust Region Policy Optimization and Proximal Policy Optimization in Ray et al. [2019a]). While straightforward, a drawback is that the penalty coefficient λ can be hard to tune (“Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on Safety Gym environments” as quoted in Ray et al. [2019a]) and the method does not guarantee strict constraint satisfaction until convergence. The agent might violate constraints during learning if λ is not large enough, or conversely, learn too slowly if λ is too large initially. 
Projected Lagrangian (Constrained Policy Optimization): Achiam et al. Achiam et al. [2017] introduced Constrained Policy Optimization (CPO), a landmark algorithm that improves upon the basic Lagrangian method by ensuring each policy update is safe. CPO is built on trust-region policy optimization: At each iteration, it solves a local constrained optimization: maximize policy improvement subject to a constraint that the cost does not increase beyond a small tolerance. This is done by a quadratic approximation of the objective and a linear approximation of the constraints (using policy gradient and cost gradient), then solving a convex subproblem. If the proposed update violates the constraint (predicted cost increase too high), CPO backtracks or projects the policy update to the nearest feasible update. CPO provides theoretical guarantees of near-constraint satisfaction at each iteration: essentially, it never overshoots the constraint by more than a certain second-order error term, keeping training safe. CPO demonstrated that one can train neural network policies for control tasks while maintaining safety throughout training Achiam et al. [2017]. It was the first general-purpose safe RL algorithm with such guarantees. 
Environment 
Actor πθ(a|s) 
Multiplier λ 
Reward Critic V̂ π(s) 
Cost Critic V̂ π c (s) 
st at 
rt ct 
Â π (s , a ) Â π 
c (s, a) 
J c (π 
) − 
d 
λ penalty 
Policy update: θ ← θ + α∇θ[J(π)− λJc(π)] Dual update: λ← [λ + β(Jc(π)− d)]+ 
Figure 10: Lagrangian actor-critic architecture for SafeRL. The actor (policy network) is updated using advantage estimates from both a reward critic and a cost critic. The Lagrange multiplier λ is adapted online based on constraint violation, automatically balancing reward maximization with safety. 
However, CPO is more complex and computationally heavier than standard policy gradient (due to solving the constrained optimization subproblem each step). It also requires a reliable estimation of the cost value and cost advantage, which can be challenging; for complex environments, cost estimates may be derived from a separate classifier trained to identify safe/unsafe actions Chirra et al. [2025]. 
Proposition 4.1 (CPO Trust Region Safety Guarantee Achiam et al. [2017]). Let πk be the current feasible policy and πk+1 be the new policy obtained by solving the CPO trust region optimization problem: 
πk+1 = arg max π∈Πθ 
Es∼dπk , a∼π[A πk(s, a)] 
s.t. JCi (πk) + 
1 
1− γ Es∼dπk , a∼π 
[ Aπk 
Ci (s, a) 
] ≤ di, ∀i, 
DKL(π ∥πk) ≤ δ. (5) 
The new policy πk+1 is guaranteed to satisfy the original cost constraint JCi up to a bounded 
error term: 
JCi (πk+1) ≤ di + 
√ 2δ γ ϵ 
πk+1 
Ci 
(1− γ)2 . (6) 
Here, ϵ πk+1 
Ci = maxs 
∣∣Ea∼πk+1 [Aπk 
Ci (s, a)] 
∣∣. Sketch of proof, detail in Achiam et al. [2017]. (1) Start from the cost performance bound. For any cost Ci and policies π′, π, Achiam et al. [2017] give (Corollary 2): 
JCi (π′)− JCi 
(π) ≤ 1 
1− γ Es∼dπ, a∼π′ 
[ Aπ 
Ci (s, a) 
] + 
2γ 
(1− γ)2 ϵπ 
′ 
Ci Es∼dπ 
[ DTV (π 
′∥π)[s] ] , 
where ϵπ ′ 
Ci = maxs 
∣∣Ea∼π′ [Aπ Ci (s, a)] 
∣∣. 
θ1 
θ2 
Constraint: Jc(π) = d 
Feasible: Jc ≤ d 
Infeasible: Jc > d 
θk 
Trust region DKL ≤ δ ∇J(π) 
Standard PG 
(violates constraint) 
θk+1 
CPO update 
PCPO projection 
Figure 11: Geometric illustration of Constrained Policy Optimization (CPO). At each iteration, CPO seeks the policy update that maximizes reward improvement within a trust region (KL divergence constraint) while staying in the feasible set (Jc ≤ d). If the standard policy gradient step would violate the constraint, CPO projects or backtracks the update to the feasible boundary. PCPO achieves this via explicit projection (dashed purple arrow). 
(2) Replace TV by average KL under a trust region. By Pinsker’s inequality and Jensen’s inequality, 
Es∼dπ [DTV (π ′∥π)[s]] ≤ 
√ 1 2 Es∼dπ [DKL(π′∥π)[s]]. 
If π′ is produced by the CPO update with trust region DKL(π ′∥π) = Es∼dπ [DKL(π 
′∥π)[s]] ≤ δ, then Es∼dπ [DTV (π 
′∥π)[s]] ≤ √ δ/2. 
(3) Apply to the constrained subproblem and re-arrange. In the CPO subproblem, the surrogate constraint enforces JCi(πk) + 
1 1−γ Es∼dπk ,a∼π 
[ Aπk 
Ci (s, a) 
] ≤ di. Plugging π′ = πk+1 and 
π = πk into the inequality of Step (1), and then substituting the TV→KL bound from Step (2) yields 
JCi(πk+1) ≤ di + 2γ 
(1− γ)2 ϵ πk+1 
Ci 
√ δ 
2 = di + 
√ 2δ γ ϵ 
πk+1 
Ci 
(1− γ)2 , 
which is exactly the stated bound. 
Many subsequent works have built on or modified CPO: PCPO (Projection-based CPO): an algorithm that explicitly projects the policy gradient to the feasible set defined by constraint gradients Yang et al. [2020]. It is a simplification that avoids solving a quadratic program but still aims to keep updates safe by geometric projection. 
TRPO-Lagrangian: A simpler baseline where one applies a trust-region update on the penalized objective J − λJc instead of solving a constrained QP. This does not guarantee strict feasibility but often empirically manages constraint violations by proper λ adaptation. OpenAI’s Safety Gym benchmark release Ray et al. [2019b,a] used such baselines1. 
Actor-Critic with Lyapunov: Chow et al. Chow et al. [2018] proposed using a Lyapunov function (a monotonic function of the cost-to-go) to derive a safe update rule. They ensure the new policy does not increase a Lyapunov function, which in turn guarantees the constraint remains satisfied. This can be seen as another form of trust-region or projection method specialized using Lyapunov theory. 
1https://github.com/openai/safety-starter-agents 
RL Agent πθ(a|s) 
Safety Shield (Filter / QP / Formal Verifier) 
Environment 
Safety Model (Dynamics / LTL spec / 
Learned model) 
Proposed at Safe a′ t 
st+1, rt, ct 
Safe/unsafe prediction 
st 
If safe: a′ t = at 
If unsafe: a′ t = asafe 
Figure 12: Safety shield / action correction pipeline. The RL agent proposes an action at, which passes through a safety shield before reaching the environment. The shield uses a safety model (dynamics model, formal specification, or learned predictor) to check whether at is safe. If unsafe, it corrects the action to the nearest safe alternative a′t, guaranteeing no constraint violation. 
Off-policy and Model-based extensions: While most policy optimization methods are onpolicy, there have been adaptations to off-policy learning: Safe DDPG or TD3: by incorporating a cost critic and Lagrange multiplier, one can train deterministic policies (as in DDPG) with a constraint. For example, a constrained variant of TD3 (Twin Delayed Deep Deterministic Policy GradientFujimoto et al. [2018]2) was proposed by Zhang et al. [2023], Yang et al. [2025]. 
Model-based SafeRL: Berkenkamp et al. Berkenkamp et al. [2017], Berkenkamp and Schoel-lig [2015], Berkenkamp et al. [2016] used Gaussian process models of the dynamics to ensure safety. They construct a stabilizing controller (via control theory) that acts as a baseline policy and only allow the learning agent to explore if it can certify (using a Lyapunov condition) that the new policy is safe. While not directly a CMDP approach, this provides an alternative angle: blending traditional control safety with RL exploration. 
4.2 Safety Shields and Action Correction 
Another category of SafeRL methods focuses on safe exploration: how to prevent an agent from ever taking an action that could lead to catastrophe. These methods act as a layer on top of any standard RL algorithm, modifying or filtering its actions (see Figure 12): 
 Safety Shield / Filter: A mechanism that monitors the agent’s chosen action and overrides it if it is deemed unsafe. The override might be a safe default action or the closest safe action. Dalal et al. Dalal et al. [2018] introduced a safety layer that solves a quadratic program (QP) in continuous action spaces to minimally adjust the action such that predicted next state stays within safety bounds. This method guaranteed zero constraint violations during training on those tasks. However, it requires a model (or learned model) to predict constraint violations. 
 Shielding via formal methods: Alshiekh et al. Alshiekh et al. [2018] and later ElSayed-Aly et al. ElSayed-Aly et al. [2021] (extended to multiagents) use formal verification and temporal logic to build shields. The idea is to pre-compute a set of forbidden state-action pairs using model checking of an abstract model, or to synthesize a runtime observer from a formal specification. The shield then blocks any action that would lead into a bad state (violating the LTL safety specification) in finite steps. In multi-agent settings, as ElSayed-Aly et al. [2021] shows, one can have a centralized shield watching over joint actions or distributed shields for each agent. 
 Human or Oracle intervention: In practical scenarios, one may employ a human overseer or a safety oracle to intervene when the agent is about to do something unsafe. While not a scalable solution for all time, during training it can prevent disasters. Safe RL with human 
2https://spinningup.openai.com/en/latest/algorithms/td3.html 
intervention was studied in Saunders et al. [2018] where a human can cancel dangerous actions, and the agent is penalized for those. Over time the agent learns to avoid actions that would have been blocked. Shielding approaches have the advantage of hard safety (no violations in theory), but they 
often rely on having additional knowledge: either a dynamics model, a predefined safe set, or an external supervisor. They also may introduce performance bias (the agent might become too conservative if the shield is not carefully designed, since it never experiences certain parts of state space). Combining shielding with CMDP-based learning is an interesting direction: one can use shielding in early training and gradually lift it as the agent’s own policy becomes safe with learned constraints. 
4.3 Risk-Sensitive and Distributional Methods 
Although our focus is on constraint-based SafeRL, a brief mention of risk-sensitive RL is warranted as an alternative approach: In risk-sensitive RL, instead of constraints, the optimization criterion itself is altered to account for risk. For example, one might maximize U−1(E[U( 
∑ r)]) where U 
is a concave utility (exponential utility gives risk-aversion) or maximize CVaRα( ∑ 
r) of return at some confidence level α. Tamar et al. Tamar et al. [2015] and others have developed policy gradient methods for CVaR (see Bäuerle and Jaśkiewicz [2024] for an overview of risk-sensitive criteria in MDPs). These effectively try to ensure with high probability the return is above some level, which is conceptually similar to constraints on probabilities of bad events. Distributional RL (as popularized by Bellemare et al. [2017]) learns the full distribution of returns. One can combine distributional RL with safety by focusing on the lower tail of the return distribution to ensure it is above some threshold. This is another way to encode safety without explicit constraints. Risk-sensitive methods can sometimes be converted into CMDP style constraints. For instance, requiring CVaR(cost) ≤ d is a constraint on a specific risk measure of cost. Solving such constraints often introduces auxiliary variables or uses sample-based approximations. While we do not detail these methods here, they are part of the broader SafeRL toolbox. 
4.4 Safe Multi-Agent Reinforcement Learning (SafeMARL) 
SafeMARL extends the ideas above to multi-agent systems Albrecht et al. [2024], Weiss [2000], Wooldridge [2009], Shoham and Leyton-Brown [2008]. We consider environments with N agents, indexed by i ∈ 1, . . . , N . A convenient formal model is a constrained Markov game, defined 
by (S,Ai, P, ri, c (j) i , γ). Here each agent i chooses an action ai ∈ Ai, forming a joint action 
a = (a1, . . . , aN ) that causes state transitions via P (s′|s,a). Each agent can receive an individual 
reward ri(s,a) and has possibly its own set of cost functions c (j) i (s,a) for j = 1 . . .mi. 
SafeMARL scenarios can be cooperative, competitive, or mixed 
 In fully cooperative SafeMARL, all agents share a common reward (or their rewards are aligned) and typically the safety constraints are also shared or at least all agents are interested in satisfying all constraints. For example, a team of robots might have a joint goal (maximize sum of rewards) and constraints like “no collisions among any robots” which is a global safety constraint. 
 In competitive or general-sum SafeMARL, each agent has its own reward to maximize, and constraints might be individual (each agent has its own safety requirement) or shared (environment-level safety that everyone needs to uphold, like traffic rules). The solution concept might be a safe equilibrium Ganzfried [2023] (e.g., a Nash equilibrium that respects constraints, related works Altman and Shwartz [2000], Mccracken and Bowling [2004] consider constrained Markov games and safe strategies for players) rather than a single policy optimization. Most existing work in SafeMARL addresses cooperative settings, since even standard MARL is most tractable in either fully cooperative (centralized training for a team) or fully competitive (twoplayer zero-sum) cases. 
We highlight a few key approaches (see Figure 13 for an architectural comparison): 
(a) Centralized SafeMARL 
Central Controller Joint policy π(a|s) 
Global constraint: Jglobal c (π) ≤ d 
i=1 i=2 i=N· · · 
Shared Environment 
Global s 
(b) Decentralized SafeMARL 
i=1 i=2 i=N· · · 
Local Jc1 ≤ d1 Local JcN ≤ dN 
comm 
π1 πN 
Shared Environment 
o1 oN 
κ-hop neighborhood 
Figure 13: Comparison of centralized vs. decentralized SafeMARL architectures. (a) Centralized: a central controller observes global state and optimizes a joint policy subject to a global safety constraint (e.g., MACPO). (b) Decentralized: each agent i has a local policy πi, local observations oi, and local constraint approximations. Agents coordinate via limited communication within a κ-hop neighborhood. 
Proposition 4.2 (Safe MARL Monotonic Improvement Guarantee Gu et al. [2023]). In the cooperative setting, a team of n agents aims to maximize a joint reward J(π) while ensuring that each agent i satisfies its own set of cost constraints JCi 
j (π) ≤ cij , ∀i ∈ 
{1, . . . , n}, j ∈ Ci. The paper introduces a Safe Multi-Agent Policy Iteration procedure that provides the following guarantees at every iteration k: 1. J(πk+1) ≥ J(πk) (monotonic reward improvement), 2. JCi 
j (πk) ≤ cij for all i, j (per-iteration constraint satisfaction). 
These guarantees are achieved through a sequential update scheme in which each agent ih solves a constrained optimization problem with agent-wise KL trust region radii chosen to ensure that every other agent’s constraint remains bounded by its threshold. 
Sketch of proof. Step 1: Multi-agent surrogate decomposition. Let Aπ be the joint advantage under the current joint policy πk. By the multi-agent advantage decomposition (Lemma 1 in Gu et al. [2023]), for any ordering i1:n, 
Es∼ρπk , a∼πk+1 
[ Aπk 
(s, a) ] 
= 
n∑ h=1 
Es∼ρπk , ai1:h−1 ∼πk+1 
i1:h−1 , aih ∼πk+1 
ih 
[ A ih 
πk 
( s, ai1:h−1 
, aih )] . 
Define the one-agent surrogate 
L i1:h πk 
(πk+1 i1:h−1 
, πih)=Es,a 
[ A ih 
πk (s, ai1:h−1 
, aih) ] . 
A standard TRPO bound (applied in the multi-agent setting) gives 
J(πk+1) ≥ J(πk) + 
n∑ h=1 
{ L i1:h πk 
(πk+1 i1:h−1 
, πk+1 ih 
) 
− ν Dmax KL 
( πk ih , πk+1 
ih 
)} , 
for ν = 4γ (1−γ)2 maxs,a |Aπk 
(s, a)|. 
Step 2: Sequential argmax and the identity L = 0 at the old policy. By construction, L i1:h πk 
(πk+1 i1:h−1 
, πk ih ) = 0. Each agent update πk+1 
ih is chosen to maximize the penalized surrogate 
L i1:h πk 
(πk+1 i1:h−1 
, ·) − νDmax KL (πk 
ih , ·), so replacing πk+1 
ih by πk 
ih yields a lower value. Summing over h 
gives J(πk+1) ≥ J(πk), proving monotonic improvement. Step 3: Per-iteration feasibility via cost surrogates + KL budgets. For each agent i 
and cost index j, Lemma 2 in Gu et al. [2023] bounds the change of cost under a joint update: 
J i Cj (πk+1) ≤ J i 
Cj (πk) + L i 
Cj ,πk (πk+1 
i ) + νij 
n∑ ℓ=1 
Dmax KL (πk 
ℓ , π k+1 ℓ ), 
with νij = 4γ (1−γ)2 maxs,ai 
|A i Cj ,πk 
(s, ai)|. Choosing agent-wise KL radii δih ensures that, starting 
from a feasible πk, the sequential update of ih keeps every other agent’s constraint bounded by its threshold; hence J i 
Cj (πk+1) ≤ cij for all i, j. This proves per-iteration constraint satisfaction. 
Combining Steps 1–3 yields the proposition. 
 Centralized Training with Global Constraints: A straightforward extension of singleagent SafeRL to multi-agent cooperative tasks is to treat the entire multi-agent system as one big agent with a joint action Albrecht et al. [2024]. One can then apply CMDP methods on the joint system. For example, one can define a joint policy π(a|s) and a global cost cglobal(s,a) that encodes any violation by any agent. Then apply CPO or Lagrange methods on this joint policy. This was essentially the approach in the MACPO algorithm3 by Gu et al. [2023]: they derived a multi-agent version of the CPO update (ensuring monotonic improvement in team reward and satisfaction of safety constraints). In practice, they implemented MACPO with two variants: one using a centralized critic (accessible during training) that estimates global reward and cost, and another using a factorized approach (MAPPO-Lagrangian, See Lemma 1: Multiagent advantage decompositon in Gu et al. [2023] ) which is simpler and uses decentralized advantage estimates with a Lagrange penalty for costs. The challenge with centralized approaches is the scalability: the joint action space grows exponentially with number of agents, and a centralized policy might be impractical for many agents. It also requires a central controller during training (and possibly execution) that knows all agent’s states, which might not be available in all applications. 
 Decentralized Safe Learning with Coordination: An important research direction is how to achieve safe multi-agent learning without relying on a central entity or a global state accessible to all. Recent work by Zhang et al. Zhang et al. [2024] introduced a scalable constrained policy optimization where each agent optimizes a localized objective that approximates the global safety. They use the concept of κ-hop neighborhood (each agent coordinates with others within κ hops in a communication graph) to truncate the dependence on far-away agents. They proved that if each agent optimizes a local policy with these truncated safety constraints and updates sequentially, the overall system still improves reward and satisfies constraints. The resulting algorithm (Scalable MAPPO-Lagrangian) shows promising results on large multi-agent environments, demonstrating that strict centralization is not always necessary for SafeMARL. Another method for decentralization is to factor the safety constraints: ElSayed-Aly et al. [2021] did this via shields for subsets of agents. In general, one can attempt to decompose a global constraint into local constraints for each agent. For example, a global cost cglobal(s,a) might be decomposed as cglobal = 
∑ i ci(s, ai) if the unsafe events are localized per agent. 
Then each agent could constrain its own ci. However, not all safety constraints are additively separable; many (like collision avoidance) are inherently about joint configurations. This remains a hard problem: designing local reward/cost structures whose alignment with global safety yields provable guarantees. 
 Multi-agent Credit Assignment for Safety: In multi-agent RL, credit assignment (determining each agent’s contribution to global reward) is crucial. Similarly, for safety, one might need to assign “blame” or responsibility to individual agents for a safety violation. Approaches like difference rewards Wolpert and Tumer [2001], Tumer and Wolpert [2004] or shaped team 
3https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation 
rewards Devlin and Kudenko [2011] can be used to ensure each agent gets feedback about how its actions affected the global outcome. For SafeRL, one could design each agent’s cost signal such that it corresponds to the marginal increase in global risk due to that agent. Some initial works have considered approaches where each agent considering the safety constraints of others Gu et al. [2023], though a general solution is open research (we outline this as a problem later). 
 Safe Equilibria and Non-Cooperative Agents: For competitive settings, one could consider each agent solving its own CMDP subject to safety constraints, leading to a game where each agent’s strategy must satisfy its own constraints. The concept of a constrained Nash equilibrium arises: a profile of policies π1, . . . , πN such that no agent can improve its reward without violating constraints given the other’s policies. Algorithms to compute such equilibria are not well-developed; this might involve ideas from game theory (like best response dynamics with constraints or Lagrangian for each agent). One example in literature is safe multi-agent learning via Stackelberg games: one agent (leader) accounts for the follower’s response. Zheng and Gu [2025] apply a bilevel optimization (Stackelberg) to model an autonomous driving scenario with safety, effectively solving a two-agent safe RL where the vehicles plans with knowledge of the other’s constraints (for example, in road intersection environments). This is a rich area for future investigation. 
 Benchmarking SafeMARL: The progress in SafeMARL has been accelerated by the introduction of benchmarks. Gu et al. Gu et al. [2023] provided Safe Multi-Agent MuJoCo4, Safe MARobosuite, and Safe MA-IsaacGym, which are multi-robot simulation tasks with safety constraints (like torque limits or collision constraints). These environments allow systematic evaluation of SafeMARL algorithms in settings requiring coordination. Similarly, for single-agent SafeRL, OpenAI’s Safety Gym5 Ray et al. [2019a] introduced a suite of continuous control tasks with hazards and constraints, which has become a standard testbed. More recently, Safety Gym-nasium Ji et al. [2023a] provides a modernized successor with Gymnasium API support, and algorithm libraries such as OmniSafe Ji et al. [2023b] and Safe Policy Optimization (SafePO) Ji et al. [2023a] offer unified implementations of constrained RL baselines. For safe control benchmarking, Safe-Control-Gym Yuan et al. [2022] integrates constraint-aware control tasks for robotics. Multi-agent driving environments such as SMARTS Zhou et al. [2020] and singleagent driving suites like Highway-env Leurent [2018] further expand the available testbeds for safe RL research. 
In summary, state-of-the-art SafeRL methods range from modified policy gradient algorithms (with theoretical guarantees like CPO) to pragmatic penalty-based methods, model-based safe exploration, and safety layers, whereas SafeMARL is exploring centralized vs. decentralized learning, coordination mechanisms, and safe policy equilibrium concepts. Table 1 provides a high-level summary of key selected algorithms in SafeRL and SafeMARL. 
5 Safe RL and Safe MARL Libraries 
In Tables 2 and 3, we show various available popular libraries and environments for further research in safe RL and safe MARL. 
Taxonomy of Safe Reinforcement Learning Libraries and Environments. To consolidate the growing ecosystem of reproducible and standardized implementations in Safe Reinforce-ment Learning (SafeRL) and Safe Multi-Agent Reinforcement Learning (SafeMARL), Tables 2 and 3 summarize the major algorithmic libraries and environment suites currently used by the research community. Table 2 lists the most widely adopted open-source frameworks that implement constrained or risk-aware reinforcement learning algorithms under the Constrained Markov Decision Process (CMDP) formulation. These include high-quality benchmark suites such as Om-niSafe, Safe Policy Optimization (SafePO), Safety Starter Agents, and Safe-Control-Gym. Each 
4https://github.com/chauncygu/Safe-Multi-Agent-Mujoco 5https://github.com/openai/safety-gym 
Method/Algorithm Description and Key Features 
Lagrangian actor-critic Tessler et al. [2019] 
Add constraint cost as penalty to reward; update λ online. Sim-ple but may violate constraints before convergence. 
Constrained Policy Opti-mization (CPO) Achiam et al. [2017] 
Trust-region policy updates with theoretical guarantee of nearconstraint satisfaction each iteration. Uses second-order approximations to ensure safety. 
Lyapunov-based Policy Op-timization Chow et al. [2018] 
Uses a Lyapunov function (cost critic) to constrain updates. Guarantees decrease in an upper bound of cost. 
Reward Constrained DQN Tessler et al. [2019] 
DQN with a reward penalty for constraint, ensuring discrete actions respect cost limit in expectation. 
Safe DDPG/TD3 (La-grangian) 
Extends continuous control off-policy algorithms with cost critics and Lagrange multipliers for constraints. 
Safe Model-Based RL Berkenkamp et al. [2017] 
Uses model uncertainty estimates and stability analysis to allow only proven-safe explorations. Ensures no violations under certain dynamics assumptions. 
Safety Layer (action shield) Dalal et al. [2018] 
A differentiable layer that projects chosen actions to the nearest safe action by solving a QP. Guarantees zero immediate violations given local dynamics linearization. 
Shielding (LTL) ElSayed-Aly et al. [2021] 
Pre-compute shields from formal specifications; filter multiagent joint actions to avoid unsafe outcomes. Achieves provable safety with respect to spec. 
Multi-Agent CPO (MACPO) Gu et al. [2023] 
Extension of CPO for multi-agent teams. Centralized training, uses a joint policy or coordinated update. Demonstrated on multi-robot tasks. 
Scalable Decentralized Safe MARL Zhang et al. [2024] 
Each agent optimizes a local surrogate constrained problem using truncated observation of others. Achieves near-centralized performance with better scalability. 
Safe MARL via Bilevel (Stackelberg) Zheng and Gu [2025] 
Models one agent as leader, others as followers in a game with safety constraints. Solves via bilevel optimization to account for interactive safety. 
Safe MARL with Shielding ElSayed-Aly et al. [2021] 
Combines MARL with runtime shielding (central or factored) to ensure no unsafe joint actions are taken during learning. 
Table 1: Representative SafeRL (single-agent) and SafeMARL (multi-agent) methods. 
library is characterized by its category, algorithmic focus, GitHub repository, and the environments it supports. The table also provides typical application domains ranging from robotics and navigation to multi-agent coordination and associated references, thereby serving as a guide to reproducible SafeRL experimentation and comparison across methods. 
Benchmarking Environments and Datasets. Complementing the algorithmic libraries, Ta-ble 3 categorizes the principal benchmark environments and datasets that provide structured safety signals for policy learning. These include the Safety-Gymnasium and the legacy OpenAI Safety Gym for constrained navigation and manipulation, as well as the AI Safety Gridworlds and SafeLife platforms that test specification robustness and side-effect avoidance in discrete domains. More complex continuous and multi-agent settings are covered by simulation frameworks such as SMARTS for autonomous driving and Highway-env for risk-sensitive control. Each environment entry specifies whether it supports single-agent or multi-agent training, the structure of safety constraints or cost signals, representative tasks, and intended application areas. Together, these two tables form a comprehensive taxonomy of tools that underpin experimental research in safe and trustworthy reinforcement learning. 
Table 2: Taxonomy of Safe Reinforcement Learning and Multi-Agent Safety Libraries. 
Name Category Algorithms / Capabili-ties 
Application Areas 
OmniSafe Ji et al. [2023b] 
Algorithm Li-brary (Safe RL) 
PPO/TRPO-Lagrangian, CPO, NPG-Lag, SAC-Lag; experiment management 
Robotics, safe navigation 
SafePO Ji et al. [2023a] 
Safe RL & Safe MARL 
Lagrangian & CPO-style variants; MARL support; training pipelines 
Multi-agent coordination, safe control 
Safety Starter Agents Ray et al. [2019a] 
Baselines / Refer-ence 
CPO, PPO-Lag, TRPO-Lag, DDPG-Lag baselines 
Benchmarking baselines 
Safe-Control-Gym Yuan et al. [2022] 
Benchmarking Suite 
Constraint-aware control tasks; integrates SB3 and RL agents 
Safe robotics & continuous control 
Table 3: Taxonomy of Environments and Datasets for Safe RL and Safe MARL. 
Name Agent Type 
Key Features / Sig-nals 
Example Tasks Citations 
Safety Gym-nasium 
Both Cost signals & constraints (hazards); Gymnasium API 
Goal/Button/Push with hazards 
Ji et al. [2023a] 
OpenAI Safety Gym 
Single Original cost/constraint tasks (archived) 
Point/Car/Doggo: Goal/Button/Push 
Ray et al. [2019a] 
AI Safety Gridworlds 
Single Side-effect & reward specification tests 
Multiple gridworlds for specification failures 
Leike et al. [2017] 
SafeLife Single Procedurally generated levels; side-effect metrics 
Life-like tasks minimizing side effects 
Wainwright and Eckersley [2021] 
SMARTS Multi Traffic simulation, risk modeling for multi-agent driving 
Merging, intersection, adversarial driving 
Zhou et al. [2020] 
Highway-env Single Collision-avoidance objectives; Gym-compatible 
Highway, merge, roundabout, parking 
Leurent [2018] 
6 Open Research Challenges and Future Directions 
While significant progress has been made in SafeRL and SafeMARL, many challenges remain open. In this section, we present five research problems that, if solved, would substantially advance the field (see Figure 14). Three of these pertain specifically to SafeMARL, reflecting the newer nature of multi-agent safety. For each problem, we describe the motivation, outline possible approaches (steps toward a solution), and reference relevant prior work to build upon. 
Most SafeRL algorithms guarantee safety in expectation or asymptotically, but they often allow some violations during learning (especially early on). In high-stakes applications, even a single catastrophic failure is unacceptable. The research challenge is to design RL methods that ensure zero (or provably bounded) constraint violations throughout the entire training process, without relying on a human in the loop. 
Ensuring no violations typically requires either very conservative exploration or prior knowledge (dynamics models, safe baseline policy). Too conservative an approach can severely slow down learning. Balancing caution with exploration is tricky, as overly restrictive safety can trap the 
P1: Zero-Violation Safe Exploration 
P2: Safety Under Partial Observability 
P3: Decentralized SafeMARL 
P4: Competitive SafeMARL 
P5: Non-Stationary Multi-Agent Safety 
Single-Agent 
Single-Agent 
Multi-Agent Multi-Agent 
Multi-Agent sa 
fe ex 
pl or 
at ion guarantees 
lo c a l o b s . 
no central authority 
a d a p t a t io 
n 
co ord 
ina tio 
n 
Problems are interconnected 
Figure 14: Five open research problems in SafeRL and SafeMARL, and their interconnections. Problems 1–2 focus on single-agent challenges (zero-violation guarantees and partial observability), while Problems 3–5 address multi-agent settings (decentralized safety, competitive equilibria, and non-stationarity). Dashed lines indicate how progress on one problem can benefit others. 
policy in a local optima (not exploring better solutions). The concept of never violating constraints relates to safe exploration. Moldovan and Abbeel 
(2012) and others studied conditions for “safe policy learning” where certain states are absorbing traps (unsafe) and should be avoided forever. Approach like learning with a safety critic mentorassisted exploration Saunders et al. [2018], Zhou and Li [2018], Huang et al. [2018] have been tried. However, a general solution remains elusive, especially for high-dimensional continuous tasks. Solving this problem would likely require combining learning with elements of control theory or formal methods to get the needed guarantees. 
Many real-world problems are partially observable (POMDPs) – the agent does not have full knowledge of the true state relevant to safety. Examples: a robot with limited sensors, or an autonomous car that cannot see around corners. In such cases, ensuring safety is harder because the agent might inadvertently take an unsafe action due to missing information. The challenge is to design SafeRL algorithms that operate under uncertainty/partial observability and still guarantee safety. 
In a POMDP, the agent typically maintains a belief (distribution over states). Constraints might need to be satisfied with respect to the true state (which is unknown). For instance, we might require that for all possible true states consistent with the agent’s observations, the safety constraint holds. This is a very strict condition and can be overly conservative. Alternatively, one might demand a high probability of safety given the belief. There is work on POMDPs with chance constraints, where constraints must hold with a certain probability. Techniques often convert these into augmented state MDPs by including some memory or using scenario optimization. Another related concept is belief shielding: e.g., using human feedback to avoid ambiguous unsafe states. Solving safe RL in POMDPs could connect to robust control in partially observed systems (like robust Model Predictive Control with chance constraints). This problem remains largely open; progress would benefit fields like autonomous systems operating with imperfect sensors. In many multi-agent applications, each agent has only partial, local observations (e.g., each car in traffic sees only nearby cars). A central authority that monitors and enforces safety for all agents may not exist. The challenge is to achieve safe multi-agent learning in a fully decentralized way: each agent makes decisions based on its local view and (optionally) limited communication, and together their behaviors ensure global safety constraints are respected. 
Global safety constraints often involve the joint state of multiple agents (e.g., distance between any two drones must exceed a threshold to avoid collision). No single agent can evaluate the global 
constraint alone. If communication is limited (bandwidth or range), agents might not know the actions or states of others in time to react safely. Moreover, learning is now on a game (or team) level, complicated by non-stationarity (each agent’s environment is affected by others learning simultaneously). 
Decentralized MARL has been studied (e.g., independent learners, mean-field MARL), but safety adds extra difficulty. Zhang et al. [2024] is one of few works aiming at decentralized Safe-MARL. Also relevant are distributed constrained optimization Fioretto et al. [2018], Chang et al. [2014], Notarnicola and Notarstefano [2018], Luan et al. [2024] in control theory where multiple controllers ensure a global constraint (like distributed frequency control in power grids Parandehgheibi et al. [2016], Wang et al. [2019] ensuring safety constraints on voltage). Tech-niques from graphical games or networked control systems could be applied. Success in this problem would directly impact fields like distributed robotics Testa et al. [2025], Wang et al. [2022] and network safety (e.g., ensuring no network congestion collapse via decentralized RL controllers Sunassee et al. [2021], Kamau Kiarie et al. [2025]). 
SafeRL research has mostly focused on a single agent or cooperative teams. However, in the real world, multiple independent agents (e.g., companies trading stocks with safety limits, or autonomous cars from different manufacturers) may not share a common goal. They might even be adversarial. Each has safety constraints (like not going bankrupt, or not crashing) but they also have competing objectives. The challenge is to extend SafeRL to general-sum or competitive environments, finding appropriate equilibrium notions and algorithms to compute them. 
In competitive multi-agent scenarios, one cannot simply optimize a joint objective. Methods like CPO do not directly apply, because improving one agent’s reward might hurt another’s. We need an equilibrium concept like constrained Nash equilibrium Xu et al. [2025] or constrained correlated equilibrium Boufous et al. [2024], Chen et al. [2022]. Another issue is that safety for one agent might depend on the behavior of others. If others act recklessly, an agent might be unable to guarantee its safety without overly sacrificing reward (or might need to assume worst-case opponents). Constrained game equilibria have been studied in economics (e.g., Nash equilibria with budget constraints). In RL, one related field is Mean-Field Games with constraints Cannarsa et al. [2018], Barreiro-Gomez and Tembine [2019], Arjmand and Mazanti [2021], Capuani and Marigonda [2022], but results are sparse. Another is Multi-agent reinforcement learning for traffic K.J. et al. [2014], Zeynivand et al. [2022], Li et al. [2024], where multiple self-interested cars must avoid collisions (a safety constraint) – some works use hand-crafted rules or potential fields, but learning such behavior while each optimizes their own objective is largely open. If this problem is solved, it could define how autonomous systems from different stakeholders safely coexist (think of air traffic control but without a central controller—planes negotiating to avoid collisions while meeting their own goals). 
Consider multi-agent systems that operate over long time scales where the environment or the set of agents may change. For example, a fleet of autonomous vehicles might encounter new types of vehicles or changing traffic rules; or a robotic factory might add/remove robots over time. We need SafeMARL algorithms that can adapt to non-stationarity in the environment or agent population, while preserving safety. This includes scenarios like agents entering or leaving, changes in the dynamics, or even adversarial perturbations. 
Non-stationarity breaks the assumptions of convergence for most RL algorithms. SafeRL adds another layer: after training, if something changes and the policy is no longer safe, the agent must detect and correct this quickly (ideally without catastrophic failure during the transition). Multi-agent adds complexity because one agent’s non-stationarity (learning or adapting) is another agent’s non-stationary environment. Non-stationary RL is a growing area (sometimes framed as lifelong learning or non-stationary bandits). SafeRL in non-stationary settings has seen little study. One relevant angle is robust safe RL: algorithms that ensure safety under model perturbations (e.g., Chen et al. [2021], Coursey et al. [2025] considered adversarial changes in cost function within limits or continual safety in non-stationary dynamics). Another is meta-learning safety: a recent work by Grbic and Risi [2020] attempted to meta-learn a safety critic for quickly evaluating new scenarios. Achieving continual safe learning could pave the way for real-world deployment 
Summary of Research Directions 
The problems outlined above are interconnected. For example, solving safe exploration (Problem 1) will likely benefit safe adaptation (Problem 5); and advances in decentralized safe learning (Problem 3) will be crucial for tackling competitive safe learning (Problem 4) where a central authority is absent. Each problem requires a blend of techniques—RL algorithms, optimization theory, control theory, and even insights from economics or game theory.Crucially, addressing these problems will move SafeRL from a laboratory curiosity to a dependable component of autonomous systems. We expect that success in these areas will result in publishable work at top venues (NeurIPS, ICML, ICRA, etc.), given the importance and difficulty of ensuring safety in learning systems. By formulating them here, we hope to encourage more researchers to contribute to these challenges. 
7 Conclusion 
Safe Reinforcement Learning is a vital area of research for deploying learning agents in realworld environments where failures are costly or dangerous. In this survey, we provided a detailed overview of SafeRL with a focus on the CMDP framework for incorporating constraints. We reviewed theoretical foundations including CMDP definitions, Lagrangian duality, and solution methods like linear programming and policy gradient for constrained problems. Building on this foundation, we discussed state-of-the-art SafeRL algorithms such as Constrained Policy Opti-mization, Lagrange multiplier methods, safe exploration via shielding, and how these have been extended to multi-agent settings.Our survey highlights that: 
 SafeRL is inherently a cross-disciplinary field, drawing from machine learning, optimal control, and formal methods. The CMDP formulation provides a unifying language for many approaches. 
 There is a rich toolbox of algorithms for single-agent SafeRL that can achieve good performance while respecting constraints, though each has trade-offs in terms of safety guarantees vs. efficiency. 
 SafeMARL is a frontier with significant potential impact (e.g., fleet management, multi-robot systems). Early algorithms like MACPO and shielding strategies show feasibility, but general solutions for decentralized and competitive scenarios are still lacking. 
We identified several open research problems that require further work: from guaranteeing zero violations to handling partial observability, and from fully decentralized safe coordination to safe learning in non-stationary multi-agent environments. These problems underscore that SafeRL is not a solved problem—there are theoretical challenges (ensuring safety and convergence), practical issues (scalability, function approximation errors), and new frontiers (multi-agent interactions). In conclusion, SafeRL offers a pathway to more trustworthy AI systems by marrying reinforcement learning with constraint satisfaction. As RL agents become more capable and autonomous, ensuring their safety will be paramount. We hope this survey serves as a useful resource for researchers to understand the current landscape and to inspire further advances. The continued development of SafeRL methods will help unlock applications of RL in domains that are currently out of reach due to safety concerns, ultimately enabling AI to make beneficial decisions without posing undue risk. 
LLM Usage 
ChatGPT-5.1 free version was used for polishing of initial draft text to improve the English and grammar. Claude Code was used to assist with TikZ figure creation, formatting, and bibliography management. 
References 
J. Achiam, D. Held, A. Tamar, and P. Abbeel. Constrained policy optimization. In Proceedings of the 34th International Conference on Machine Learning, pages 22–31. PMLR, 2017. 
Mohamadreza Ahmadi, Xiaobin Xiong, and Aaron D. Ames. Risk-averse planning via cvar barrier functions: Application to bipedal robot locomotion, 2021. URL https://arxiv.org/abs/ 
2011.01578. arXiv: 2011.01578. 
Mohamadreza Ahmadi, Xiaobin Xiong, and Aaron D. Ames. Risk-averse control via cvar barrier functions: Application to bipedal robot locomotion. IEEE Control Systems Letters, 6:878–883, 2022. doi: 10.1109/LCSYS.2021.3086854. 
Stefano V. Albrecht, Filippos Christianos, and Lukas Schäfer. Multi-Agent Reinforcement Learn-ing: Foundations and Modern Approaches. MIT Press, 2024. URL https://www.marl-book. 
com. 
Moayad Alshiekh, Roderick Bloem, Richard Ehlers, Bernhard Könighofer, Scott Niekum, and Ufuk Topcu. Safe reinforcement learning via shielding. In Proceedings of the AAAI Conference on Artificial Intelligence, 2018. 
E. Altman. Constrained Markov Decision Processes. Chapman & Hall/CRC, 1999. 
Eitan Altman and Adam Shwartz. Constrained markov games: Nash equilibria. In Jerzy A. Filar, Vladimir Gaitsgory, and Koichi Mizukami, editors, Advances in Dynamic Games and Applications, pages 213–221, Boston, MA, 2000. Birkhäuser Boston. ISBN 978-1-4612-1336-9. 
Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety, 2016. URL https://arxiv.org/abs/1606.06565. arXiv: 1606.06565. 
Saeed Sadeghi Arjmand and Guilherme Mazanti. On the characterization of equilibria of nonsmooth minimal-time mean field games with state constraints. In 2021 60th IEEE Conference on Decision and Control (CDC), pages 5300–5305, 2021. doi: 10.1109/CDC45484.2021.9683104. 
Julian Barreiro-Gomez and Hamidou Tembine. Constrained mean-field-type games: Stationary case. In 2019 IEEE 58th Conference on Decision and Control (CDC), pages 2208–2213, 2019. doi: 10.1109/CDC40024.2019.9029483. 
Nicole Bäuerle and Anna Jaśkiewicz. Markov decision processes with risk-sensitive criteria: an overview. Mathematical Methods of Operations Research, 99:141–178, 2024. 
Marc G. Bellemare, Will Dabney, and Rémi Munos. A distributional perspective on reinforcement learning, 2017. URL https://arxiv.org/abs/1707.06887. arXiv: 1707.06887. 
F. Berkenkamp and A. Schoellig. Safe and robust learning control with gaussian processes. In Proceedings of the European Control Conference (ECC), 2015. 
Felix Berkenkamp, Angela P. Schoellig, and Andreas Krause. Safe controller optimization for quadrotors with gaussian processes. In 2016 IEEE International Conference on Robotics and Automation (ICRA), pages 491–496, 2016. doi: 10.1109/ICRA.2016.7487170. 
Felix Berkenkamp, Matteo Turchetta, Angela P. Schoellig, and Andreas Krause. Safe model-based reinforcement learning with stability guarantees. In Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS’17, page 908–919, Red Hook, NY, USA, 2017. Curran Associates Inc. ISBN 9781510860964. 
D. Bertsimas and A. Thiele. A robust optimization approach to inventory theory. Operations Research, 54(1):150–168, 2006. 
Jun Bian, Jianchun Zhang, Kexin Guo, Wenshuo Li, Xiang Yu, and Lei Guo. Risk-aware path planning using cvar for quadrotors. In 2023 6th International Symposium on Autonomous Systems (ISAS), pages 1–6, 2023. doi: 10.1109/ISAS59543.2023.10164417. 
Eilyan Bitar and Yunjian Xu. Deadline differentiated pricing of deferrable electric loads. IEEE Transactions on Smart Grid, 8(1):13–25, 2017. doi: 10.1109/TSG.2016.2601914. 
L. Blackmore, Hui Li, and B. Williams. A probabilistic approach to optimal robust path planning with obstacles. In 2006 American Control Conference, pages 7 pp.–, 2006. doi: 10.1109/ACC. 2006.1656653. 
V. S. Borkar. Q-learning for risk-sensitive control. Mathematics of Operations Research, 27(2): 294–311, 2002. 
V. S. Borkar and R. Jain. Risk-constrained markov decision processes. IEEE Transactions on Automatic Control, 59(9):2574–2579, 2014. 
Omar Boufous, Rachid El-Azouzi, Mikaël Touati, Eitan Altman, and Mustapha Bouhtou. Con-strained correlated equilibria. In 2024 60th Annual Allerton Conference on Communication, Control, and Computing, pages 1–8, 2024. doi: 10.1109/Allerton63246.2024.10735321. 
Lukas Brunke, Melissa Greeff, Adam W. Hall, Zhaocong Yuan, Siqi Zhou, Jacopo Panerati, and Angela P. Schoellig. Safe learning in robotics: From learning-based control to safe reinforcement learning. Annual Review of Control, Robotics, and Autonomous Sys-tems, 5(Volume 5, 2022):411–444, 2022. ISSN 2573-5144. doi: https://doi.org/10.1146/ annurev-control-042920-020211. URL https://www.annualreviews.org/content/journals/ 
10.1146/annurev-control-042920-020211. 
Piermarco Cannarsa, Rossana Capuani, and Pierre Cardaliaguet. Mean field games with state constraints: from mild to pointwise solutions of the pde system, 2018. URL https://arxiv. 
org/abs/1812.11374. arXiv: 1812.11374. 
Rossana Capuani and Antonio Marigonda. Constrained mean field games equilibria as fixed point of random lifting of set-valued maps. IFAC-PapersOnLine, 55(30):180–185, 2022. ISSN 2405-8963. doi: https://doi.org/10.1016/j.ifacol.2022.11.049. URL https://www.sciencedirect. 
com/science/article/pii/S2405896322026829. 25th International Symposium on Mathe-matical Theory of Networks and Systems MTNS 2022. 
Tsung-Hui Chang, Angelia Nedić, and Anna Scaglione. Distributed constrained optimization by consensus-based primal-dual perturbation method. IEEE Transactions on Automatic Control, 59(6):1524–1538, 2014. doi: 10.1109/TAC.2014.2308612. 
Baiming Chen, Zuxin Liu, Jiacheng Zhu, Mengdi Xu, Wenhao Ding, and Ding Zhao. Context-aware safe reinforcement learning for non-stationary environments, 2021. URL https://arxiv. 
org/abs/2101.00531. arXiv: 2101.00531. 
Jiangxi Chen and Xiaojun Zhou. Reinforcement learning based maintenance scheduling of flexible multi-machine manufacturing systems with varying interactive degradation. Reliability Engineering & System Safety, 260:111018, 2025. ISSN 0951-8320. doi: https://doi.org/ 10.1016/j.ress.2025.111018. URL https://www.sciencedirect.com/science/article/pii/ 
S0951832025002194. 
Xin Chen, Melvyn Sim, David Simchi-Levi, and Peng Sun. Risk aversion in inventory management. Oper. Res., 55:828–842, 2007. URL https://api.semanticscholar.org/CorpusID:5864509. 
Ziyi Chen, Shaocong Ma, and Yi Zhou. Finding correlated equilibrium of constrained markov game: a primal-dual approach. In Proceedings of the 36th International Conference on Neural Information Processing Systems, NIPS ’22, Red Hook, NY, USA, 2022. Curran Associates Inc. 
Richard Cheng, Gábor Orosz, Richard M. Murray, and Joel W. Burdick. End-to-end safe reinforcement learning through barrier functions for safety-critical continuous control tasks. In Proceedings of the Thirty-Third AAAI Conference on Artificial Intelligence and Thirty-First Innovative Applications of Artificial Intelligence Conference and Ninth AAAI Sympo-sium on Educational Advances in Artificial Intelligence, AAAI’19/IAAI’19/EAAI’19. AAAI Press, 2019. ISBN 978-1-57735-809-1. doi: 10.1609/aaai.v33i01.33013387. URL https: 
//doi.org/10.1609/aaai.v33i01.33013387. 
Shashank Reddy Chirra, Pradeep Varakantham, and Praveen Paruchuri. Safety through feedback in constrained rl, 2025. URL https://arxiv.org/abs/2406.19626. arXiv: 2406.19626. 
Yinlam Chow, Aviv Tamar, Shie Mannor, and Marco Pavone. Risk-sensitive and robust decisionmaking: a cvar optimization approach. In Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 1, NIPS’15, page 1522–1530, Cambridge, MA, USA, 2015. MIT Press. 
Yinlam Chow, Mohammad Ghavamzadeh, Lucas Janson, and Marco Pavone. Risk-constrained reinforcement learning with percentile risk criteria, 2017. URL https://arxiv.org/abs/1512. 
01629. 
Yinlam Chow, Ofir Nachum, Edgar Duenez-Guzman, and Mohammad Ghavamzadeh. A lyapunov-based approach to safe reinforcement learning. In Proceedings of the 32nd International Con-ference on Neural Information Processing Systems, NIPS’18, page 8103–8112, Red Hook, NY, USA, 2018. Curran Associates Inc. 
Austin Coursey, Marcos Quinones-Grueiro, and Gautam Biswas. On the design of safe continual rl methods for control of nonlinear systems, 2025. URL https://arxiv.org/abs/2502.15922. arXiv: 2502.15922. 
Gal Dalal, Krishnamurthy Dvijotham, Matej Vecerik, Todd Hester, Cosmin Paduraru, and Yuval Tassa. Safe exploration in continuous action spaces, 2018. URL https://arxiv.org/abs/ 
1801.08757. arXiv: 1801.08757. 
Emiliano Dall’Anese, Kyri Baker, and Tyler Summers. Chance-constrained ac optimal power flow for distribution systems with renewables. IEEE Transactions on Power Systems, 32(5): 3427–3438, 2017. doi: 10.1109/TPWRS.2017.2656080. 
Sam Devlin and Daniel Kudenko. Theoretical considerations of potential-based reward shaping for multi-agent systems. In Proceedings of the 10th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), pages 225–232, 2011. 
Jiajun Duan, Di Shi, Ruisheng Diao, Haifeng Li, Zhiwei Wang, Bei Zhang, Desong Bian, and Zhehan Yi. Deep-reinforcement-learning-based autonomous voltage control for power grid operations. IEEE Transactions on Power Systems, 35(1):814–817, 2020. 
I. ElSayed-Aly, S. Bharadwaj, C. Amato, R. Ehlers, U. Topcu, and L. Feng. Safe multi-agent reinforcement learning via shielding. In Proc. of the 20th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), pages 483–491, 2021. 
Ferdinando Fioretto, Enrico Pontelli, and William Yeoh. Distributed constraint optimization problems and applications: A survey. Journal of Artificial Intelligence Research, 61:623–698, March 2018. ISSN 1076-9757. doi: 10.1613/jair.5565. URL http://dx.doi.org/10.1613/ 
jair.5565. 
Jaime F. Fisac, Anayo K. Akametalu, Melanie N. Zeilinger, Shahab Kaynama, Jeremy Gillula, and Claire J. Tomlin. A general safety framework for learning-based control in uncertain robotic systems. IEEE Transactions on Automatic Control, 64(7):2737–2752, 2019. 
Scott Fujimoto, Herke van Hoof, and David Meger. Addressing function approximation error in actor-critic methods. arXiv preprint arXiv:1802.09477, 2018. 
Sam Ganzfried. Safe equilibrium. In 2023 62nd IEEE Conference on Decision and Control (CDC), pages 5230–5236, 2023. 
J. Garcia and F. Fernandez. A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research, 16(1):1437–1480, 2015. 
P. Geibel and F. Wysotzki. Risk-sensitive reinforcement learning applied to control under constraints. Journal of Artificial Intelligence Research, 24:81–108, 2005. 
Jeremy H. Gillula and Claire J. Tomlin. Guaranteed safe online learning via reachability: Track-ing a ground target using a quadrotor. In IEEE International Conference on Robotics and Automation (ICRA), pages 2723–2730, 2012. 
O. Gottesman, F. Johansson, and M. et al. Komorowski. Guidelines for reinforcement learning in healthcare. Nature Medicine, 25(1):16–18, 2019. 
Djordje Grbic and Sebastian Risi. Safe reinforcement learning through meta-learned instincts, 2020. URL https://arxiv.org/abs/2005.03233. 
S. Gu, J. G. Kuba, Y. Chen, Y. Du, L. Yang, A. Knoll, and Y. Yang. Safe multi-agent reinforcement learning for multi-robot control. Artificial Intelligence, 319:103905, 2023. 
Shangding Gu, Long Yang, Yali Du, Guang Chen, Florian Walter, Jun Wang, and Alois Knoll. A review of safe reinforcement learning: Methods, theories, and applications. IEEE Trans. Pattern Anal. Mach. Intell., 46(12):11216–11235, December 2024. ISSN 0162-8828. doi: 10. 1109/TPAMI.2024.3457538. URL https://doi.org/10.1109/TPAMI.2024.3457538. 
Shangding Gu, Bilgehan Sel, Yuhao Ding, Lu Wang, Qingwei Lin, Alois Knoll, and Ming Jin. Safe and balanced: A framework for constrained multi-objective reinforcement learning. IEEE Trans. Pattern Anal. Mach. Intell., 47(5):3322–3331, May 2025. ISSN 0162-8828. doi: 10.1109/ TPAMI.2025.3528944. URL https://doi.org/10.1109/TPAMI.2025.3528944. 
Astghik Hakobyan, Gyeong Chan Kim, and Insoon Yang. Risk-aware motion planning and control using cvar-constrained optimization. IEEE Robotics and Automation Letters, 4(4):3924–3931, 2019. doi: 10.1109/LRA.2019.2929980. 
Matthias Heger. Consideration of risk in reinforcement learning. In William W. Co-hen and Haym Hirsh, editors, Machine Learning Proceedings 1994, pages 105–111. Mor-gan Kaufmann, San Francisco (CA), 1994. ISBN 978-1-55860-335-6. doi: https://doi. org/10.1016/B978-1-55860-335-6.50021-0. URL https://www.sciencedirect.com/science/ 
article/pii/B9781558603356500210. 
Naoto Horie, Tohgoroh Matsui, Koichi Moriyama, Atsuko Mutoh, and Nobuhiro Inuzuka. Multi-objective safe reinforcement learning: the relationship between multi-objective reinforcement learning and safe reinforcement learning. Artificial Life and Robotics, 24(3):352– 359, September 2019. doi: 10.1007/s10015-019-00523-3. URL https://doi.org/10.1007/ 
s10015-019-00523-3. 
Jessie Huang, Fa Wu, Doina Precup, and Yang Cai. Learning safe policies with expert guidance. In Proceedings of the 32nd International Conference on Neural Information Processing Systems, NIPS’18, page 9123–9132, Red Hook, NY, USA, 2018. Curran Associates Inc. 
Zilin Huang, Zhengyang Wan, Zihao Sheng, Boyue Wang, Junwei You, Yue Leng, and Sikai Chen. Sim2real-ad: A modular sim-to-real framework for deploying vlm-guided reinforcement learning in real-world autonomous driving, 2026. URL https://arxiv.org/abs/2604.03497. 
David Isele, Alireza Nakhaei, and Kikuo Fujimura. Safe reinforcement learning on autonomous vehicles. In IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2018. 
Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan, Weidong Huang, Ruiyang Sun, Yiran Geng, Yifan Zhong, Josef Dai, and Yaodong Yang. Safety gymnasium: A unified safe reinforcement learning benchmark. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2023a. URL https://openreview.net/forum?id= 
WZmlxIuIGR. 
Jiaming Ji, Jiayi Zhou, Borong Zhang, Juntao Dai, Xuehai Pan, Ruiyang Sun, Weidong Huang, Yiran Geng, Mickel Liu, and Yaodong Yang. Omnisafe: An infrastructure for accelerating safe reinforcement learning research, 2023b. URL https://arxiv.org/abs/2305.09304. 
Yan Jia, John Burden, Tom Lawton, and Ibrahim Habli. Safe reinforcement learning for sepsis treatment. In 2020 IEEE International conference on healthcare informatics (ICHI), pages 1–7. IEEE, 2020. 
Lincoln Kamau Kiarie, Mahsa Derakhshani, and Konstantinos G. Kyriakopoulos. Design principles for reinforcement learning in congestion control environments. IEEE Access, 13:85217–85230, 2025. doi: 10.1109/ACCESS.2025.3569093. 
Yeonsoo Kim and Jong Woo Kim. Safe model-based reinforcement learning for nonlinear optimal control with state and input constraints. AIChE Journal, 68(5):e17601, 2022. doi: https: //doi.org/10.1002/aic.17601. URL https://aiche.onlinelibrary.wiley.com/doi/abs/10. 
1002/aic.17601. 
B Ravi Kiran, Ibrahim Sobh, Victor Talpaert, Patrick Mannion, Ahmad A. Al Sallab, Senthil Yogamani, and Patrick Pérez. Deep reinforcement learning for autonomous driving: A survey. IEEE Transactions on Intelligent Transportation Systems, 23(6):4909–4926, 2022. doi: 10.1109/ TITS.2021.3054625. 
Prabuchandran K.J., Hemanth Kumar A.N, and Shalabh Bhatnagar. Multi-agent reinforcement learning for traffic signal control. In 17th International IEEE Conference on Intelligent Trans-portation Systems (ITSC), pages 2529–2534, 2014. doi: 10.1109/ITSC.2014.6958095. 
Jan Leike, Miljan Martic, Victoria Krakovna, Pedro A. Ortega, Tom Everitt, Andrew Lefrancq, Laurent Orseau, and Shane Legg. Ai safety gridworlds. arXiv preprint arXiv:1711.09883, 2017. URL https://github.com/deepmind/ai-safety-gridworlds. 
Edouard Leurent. An environment for autonomous driving decision-making. https://github. 
com/eleurent/highway-env, 2018. 
Dazi Li, Wentao Gu, and Tianheng Song. Multi-objective reinforcement learning in process control: A goal-oriented approach with adaptive thresholds. Journal of Process Control, 129:103063, 2023. ISSN 0959-1524. doi: https://doi.org/10.1016/j.jprocont.2023.103063. URL https: 
//www.sciencedirect.com/science/article/pii/S0959152423001506. 
Lulu Li, Ruijie Zhu, Shuning Wu, Wenting Ding, Mingliang Xu, and Jiwen Lu. Adaptive multiagent deep mixed reinforcement learning for traffic light control. IEEE Transactions on Vehic-ular Technology, 73(2):1803–1816, 2024. doi: 10.1109/TVT.2023.3319698. 
Meng Luan, Guanghui Wen, Yuezu Lv, Jialing Zhou, and C. L. Philip Chen. Distributed constrained optimization over unbalanced time-varying digraphs: A randomized constraint solving algorithm. IEEE Transactions on Automatic Control, 69(8):5154–5167, 2024. doi: 10.1109/TAC.2023.3347328. 
Otten M, Jagesar AR, Dam TA, Biesheuvel LA, den Hengst F, Ziesemer KA, Thoral PJ, de Grooth HJ, Girbes ARJ, François-Lavet V, Hoogendoorn M, and Elbers PWG. Does reinforcement learning improve outcomes for critically ill patients? a systematic review and level-of-readiness assessment. Crit Care Med., 52, 2024. 
Peter Mccracken and Michael Bowling. Safe strategies for agent modelling in games. In AAAI Technical Report, 2004. URL https://api.semanticscholar.org/CorpusID:682388. 
Eduardo Lopes Pereira Neto, Valdinei Freire, and Karina Valdivia Delgado. Risk sensitive markov decision process for portfolio management. In Advances in Soft Computing: 19th Mexican International Conference on Artificial Intelligence, MICAI 2020, Mexico City, Mexico, October 12–17, 2020, Proceedings, Part I, page 370–382, Berlin, Heidelberg, 2020. Springer-Verlag. ISBN 978-3-030-60883-5. doi: 10.1007/978-3-030-60884-2 27. 
H.D. Nguyen and K. Han. Safe reinforcement learning-based driving policy design for autonomous vehicles on highways. International Journal of Control, Automation and Systems, 21(10):4098–4110, 2023. doi: 10.1007/s12555-023-0255-4. URL https://doi.org/10.1007/ 
s12555-023-0255-4. 
Ivano Notarnicola and Giuseppe Notarstefano. Constraint coupled distributed optimization: a relaxation and duality approach, 2018. URL https://arxiv.org/abs/1711.09221. 1711.09221. 
Masahiro Ono, Marco Pavone, Yoshiaki Kuwata, and J. Balaram. Chance-constrained dynamic programming with application to risk-aware robotic space exploration. Auton. Robots, 39(4): 555–571, December 2015. ISSN 0929-5593. doi: 10.1007/s10514-015-9467-7. URL https: 
//doi.org/10.1007/s10514-015-9467-7. 
Marzieh Parandehgheibi, Konstantin Turitsyn, and Eytan Modiano. Distributed frequency control in power grids under limited communication. In 2016 IEEE 55th Conference on Decision and Control (CDC), pages 6940–6945, 2016. doi: 10.1109/CDC.2016.7799338. 
L. A. Prashanth. Policy gradients for cvar-constrained mdps. In Peter Auer, Alexander Clark, Thomas Zeugmann, and Sandra Zilles, editors, Algorithmic Learning Theory, pages 155–169, Cham, 2014. Springer International Publishing. ISBN 978-3-319-11662-4. 
L. A. Prashanth and Mohammad Ghavamzadeh. Actor-critic algorithms for risk-sensitive mdps. In Proceedings of the 27th International Conference on Neural Information Processing Systems - Volume 1, NIPS’13, page 252–260, Red Hook, NY, USA, 2013. Curran Associates Inc. 
Aniruddh Raghu, Matthieu Komorowski, and Sumeetpal Singh. Model-based reinforcement learning for sepsis treatment, 2018. URL https://arxiv.org/abs/1811.09602. 1811.09602. 
A. Ray, J. Achiam, and D. Amodei. Benchmarking Safe Exploration in Deep Reinforcement Learning. arXiv:1910.01708, 2019a. 
Alex Ray, Joshua Achiam, and Dario Amodei. Benchmarking Safe Exploration in Deep Reinforce-ment Learning. 2019b. 
Line Roald, Maria Vrakopoulou, Frauke Oldewurtel, and Göran Andersson. Risk-constrained optimal power flow with probabilistic guarantees. In 2014 Power Systems Computation Conference, pages 1–7, 2014. doi: 10.1109/PSCC.2014.7038342. 
R. Tyrrell Rockafellar and Stanislav Uryasev. Optimization of conditional value-at risk. Journal of Risk, 3:21–41, 2000. URL https://api.semanticscholar.org/CorpusID:854622. 
Dorsa Sadigh, Shankar Sastry, Sanjit A. Seshia, and Anca D. Dragan. Planning for autonomous cars that leverages effects on human actions. In Proceedings of the Robotics: Science and Systems Conference (RSS), June 2016. 
W. Saunders, G. Sastry, A. Stuhlmüller, and O. Evans. Trial without error: Towards safe reinforcement learning via human intervention. In Proc. of the 17th International Conference on Autonomous Agents and MultiAgent Systems (AAMAS), 2018. 
Rainer Schlosser. Risk-sensitive control of markov decision processes: A moment-based approach with target distributions. Computers & Operations Research, 123:104997, 2020. ISSN 0305-0548. doi: https://doi.org/10.1016/j.cor.2020.104997. URL https://www.sciencedirect.com/ 
science/article/pii/S0305054820301143. 
Shai Shalev-Shwartz, Shaked Shammah, and Amnon Shashua. On a formal model of safe and scalable self-driving cars, 2018. URL https://arxiv.org/abs/1708.06374. arXiv: 1708.06374. 
Alexander Shapiro, Darinka Dentcheva, and Andrzej Ruszczynski. Lectures on Stochastic Program-ming: Modeling and Theory, Third Edition. Society for Industrial and Applied Mathematics, Philadelphia, PA, 2021. doi: 10.1137/1.9781611976595. URL https://epubs.siam.org/doi/ 
abs/10.1137/1.9781611976595. 
Yoav Shoham and Kevin Leyton-Brown. Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations. Cambridge university press, 2008. 
Rajesh Siraskar, Satish Kumar, Shruti Patil, Arunkumar Bongale, and Ketan Kotecha. Reinforce-ment learning for predictive maintenance: a systematic technical review. Artificial Intelligence Review, 56(11):12885–12947, 2023. doi: 10.1007/s10462-023-10468-6. 
Damon Sprouts, Yin Gao, Chao Wang, Xun Jia, Chenyang Shen, and Yujie Chi. The development of a deep reinforcement learning network for dose-volume-constrained treatment planning in prostate cancer intensity modulated radiotherapy. Biomedical Physics & Engineering Express, 8(4), 2022. 
Sharon Sunassee, Avinash Mungur, Sheeba Armoogum, and Sameerchand Pudaruth. A comprehensive review on congestion control techniques in networking. In 2021 5th International Conference on Computing Methodologies and Communication (ICCMC), pages 305–312, 2021. doi: 10.1109/ICCMC51019.2021.9418329. 
A. Tamar, Y. Chow, M. Ghavamzadeh, and S. Mannor. Policy gradient for coherent risk measures. In Advances in Neural Information Processing Systems 28, 2015. 
Aviv Tamar, Dotan Di Castro, and Shie Mannor. Policy gradients with variance related risk criteria. In Proceedings of the 29th International Coference on International Conference on Machine Learning, ICML’12, page 1651–1658, Madison, WI, USA, 2012. Omnipress. ISBN 9781450312851. 
Chen Tessler, Daniel J. Mankowitz, and Shie Mannor. Reward constrained policy optimization. In International Conference on Learning Representations, 2019. URL https://openreview. 
net/forum?id=SkfrvsA9FX. 
Andrea Testa, Guido Carnevale, and Giuseppe Notarstefano. A tutorial on distributed optimization for cooperative robotics: from setups and algorithms to toolboxes and research directions, 2025. URL https://arxiv.org/abs/2309.04257. 
Huan-Hsin Tseng, Yi Luo, Sunan Cui, Jen-Tzung Chien, Randall K. Ten Haken, and Issam El Naqa. Deep reinforcement learning for automated radiation adaptation in lung cancer. Med-ical Physics, 44(12):6690–6705, 2017. 
Rui Tu, Zhipeng Luo, Chuanliang Pan, Zhong Wang, Jie Su, Yu Zhang, and Yifan Wang. Offline safe reinforcement learning for sepsis treatment: Tackling variable-length episodes with sparse rewards. Human-Centric Intelligent Systems, 5(1):63–76, 2025. 
Kagan Tumer and David H. Wolpert. A survey of collectives. In Collectives and the Design of Complex Systems, pages 1–42. Springer, 2004. 
M. Turchetta, F. Berkenkamp, and A. Krause. Safe exploration in finite MDPs with gaussian processes. In Advances in Neural Information Processing Systems 30, 2016. 
Thanh Long Vu, Sayak Mukherjee, Renke Huang, and Qiuhua Huang. Barrier function-based safe reinforcement learning for emergency control of power systems. In 60th IEEE Conference on Decision and Control (CDC), 2021. 
K. P. Wabersich and M. N. Zeilinger. Linear model predictive safety certification for learning-based control. In 2018 IEEE Conference on Decision and Control (CDC), pages 7130–7135, 2018. 
Akifumi Wachi, Xun Shen, and Yanan Sui. A survey of constraint formulations in safe reinforcement learning. In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, IJCAI ’24, 2024. ISBN 978-1-956792-04-1. doi: 10.24963/ijcai.2024/913. URL https://doi.org/10.24963/ijcai.2024/913. 
Carroll L. Wainwright and Peter Eckersley. Safelife 1.0: Exploring side effects in complex environments, 2021. URL https://arxiv.org/abs/1912.01217. 
Yutong Wang, Mehul Damani, Pamela Wang, Yuhong Cao, and Guillaume Sartoretti. Distributed reinforcement learning for robot teams: A review, 2022. URL https://arxiv.org/abs/2204. 
03516. 
Zhaojian Wang, Feng Liu, John Z. F. Pang, Steven H. Low, and Shengwei Mei. Distributed optimal frequency control considering a nonlinear network-preserving model. IEEE Transactions on Power Systems, 34(1):76–86, 2019. doi: 10.1109/TPWRS.2018.2861941. 
ZhengyuWang, Fang Chen, and Yanyi Fu. Probability load flow calculation considering wind speed correlation based on improved cumulant method. 2025 5th International Conference on Intel-ligent Power and Systems (ICIPS), pages 57–62, 2025. URL https://api.semanticscholar. 
org/CorpusID:284925024. 
Gerhard Weiss. Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence. MIT press, 2000. 
David H. Wolpert and Kagan Tumer. Optimal payoff functions for members of collectives. Ad-vances in Complex Systems, 4(2-3):265–279, 2001. 
Michael Wooldridge. An Introduction to Multiagent Systems. John Wiley & Sons, 2009. 
Jing-Zhe Xu, Zhi-Wei Liu, Ding-Xin He, Zhian Jia, and Ming-Feng Ge. Dynamic nash equilibrium seeking for constrained noncooperative game of open multiagent systems. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 55(6):3846–3855, 2025. doi: 10.1109/TSMC.2025. 3548122. 
Ning Yang, Pengyu Wang, Guoqing Liu, Haifeng Zhang, Pin Lv, and Jun Wang. Proactive constrained policy optimization with preemptive penalty, 2025. URL https://arxiv.org/ 
abs/2508.01883. 
Tsung-Yen Yang, Justinian Rosca, Karthik Narasimhan, and Peter J. Ramadge. Projection-based constrained policy optimization. In International Conference on Learning Representations (ICLR), 2020. URL https://arxiv.org/abs/2010.03152. 
Xiang Yu, Jun Bian, Jianchun Zhang, and Kexin Guo. Risk-averse motion planning for quadrotors using conditional value-at-risk. IEEE Transactions on Control Systems Technology, pages 1–15, 
Zhaocong Yuan, Adam W. Hall, Siqi Zhou, Lukas Brunke, Melissa Greeff, Jacopo Panerati, and Angela P. Schoellig. safe-control-gym: A unified benchmark suite for safe learning-based control and reinforcement learning in robotics. IEEE Robotics and Automation Letters, 7(4):11142– 11149, 2022. 
A. Zeynivand, A. Javadpour, S. Bolouki, A.K. Sangaiah, F. Ja’fari, P. Pinto, and W. Zhang. Traffic flow control using multi-agent reinforcement learning. Journal of Network and Computer Ap-plications, 207:103497, 2022. ISSN 1084-8045. doi: https://doi.org/10.1016/j.jnca.2022.103497. URL https://www.sciencedirect.com/science/article/pii/S1084804522001394. 
Hui Zhang and Pu Li. Chance constrained programming for optimal power flow under uncertainty. IEEE Transactions on Power Systems, 26(4):2417–2424, 2011. 
Jing Zhang, Chi Zhang, Wenjia Wang, and Bing-Yi Jing. Constrained policy optimization with explicit behavior density for offline reinforcement learning. In Proceedings of the 37th Interna-tional Conference on Neural Information Processing Systems, NIPS ’23, Red Hook, NY, USA, 2023. Curran Associates Inc. 
L. Zhang, L. Li, W. Wei, H. Song, Y. Yang, and J. Liang. Scalable constrained policy optimization for safe multi-agent reinforcement learning. In Advances in Neural Information Processing Systems, 2024. 
Z. Zheng and S. Gu. Safe multi-agent reinforcement learning with bilevel optimization in autonomous driving. IEEE Transactions on Artificial Intelligence, 2025. 
Ming Zhou, Jun Luo, Julian Villella, Yaodong Yang, David Rusu, Jiayu Miao, Weinan Zhang, Montgomery Alban, Iman Fadakar, Zheng Chen, Aurora Chongxi Huang, Ying Wen, Kimia Has-sanzadeh, Daniel Graves, Dong Chen, Zhengbang Zhu, Nhat Nguyen, Mohamed Elsayed, Kun Shao, Sanjeevan Ahilan, Baokuan Zhang, Jiannan Wu, Zhengang Fu, Kasra Rezaee, Peyman Yadmellat, Mohsen Rohani, Nicolas Perez Nieves, Yihan Ni, Seyedershad Banijamali, Alexan-der Cowen Rivers, Zheng Tian, Daniel Palenicek, Haitham bou Ammar, Hongbo Zhang, Wulong Liu, Jianye Hao, and Jun Wang. Smarts: Scalable multi-agent reinforcement learning training school for autonomous driving, 2020. URL https://arxiv.org/abs/2010.09776. 
Weichao Zhou and Wenchao Li. Safety-aware apprenticeship learning, 2018. URL https://arxiv. 
org/abs/1710.07983. arXiv: 1710.07983. 