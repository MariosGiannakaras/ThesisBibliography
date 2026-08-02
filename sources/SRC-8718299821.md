> Source: https://arxiv.org/pdf/1708.08611

Safe Reinforcement Learning via Shielding 
Mohammed Alshiekh1, Roderick Bloem2, Rüdiger Ehlers3, Bettina Könighofer2, Scott Niekum1, Ufuk Topcu1 
1 University of Texas at Austin, USA 2 IAIK, Graz University of Technology, Austria 
3 University of Bremen and DFKI GmbH, Bremen, Germany 
Abstract. Reinforcement learning algorithms discover policies that maximize reward, but do not necessarily guarantee safety during learning or execution phases. We introduce a new approach to learn optimal policies while enforcing properties expressed in temporal logic. To this end, given the temporal logic specification that is to be obeyed by the learning system, we propose to synthesize a reactive system called a shield. The shield is introduced in the traditional learning process in two alternative ways, depending on the location at which the shield is implemented. In the first one, the shield acts each time the learning agent is about to make a decision and provides a list of safe actions. In the second way, the shield is introduced after the learning agent. The shield monitors the actions from the learner and corrects them only if the chosen action causes a violation of the specification. We discuss which requirements a shield must meet to preserve the convergence guarantees of the learner. Finally, we demonstrate the versatility of our approach on several challenging reinforcement learning scenarios. 
1 Introduction 
Advances in learning have enabled a new paradigm for developing controllers for autonomous systems that are able to accomplish complicated tasks in possibly uncertain and dynamic environments. For example, in reinforcement learning (RL), an agent acts to optimize a long-term return that models the desired behavior for the agent and is revealed to it incrementally in a reward signal as it interacts with its environment [18]. Increasing use of learning-based controllers in physical systems in the proximity of humans also strengthens the concern of whether these systems will operate safely. 
While convergence, optimality and data-efficiency of learning algorithms are relatively well understood, safety or more generally correctness during learning and execution of controllers has attracted significantly less attention. A number of different notions of safety were recently explored [8,15]. We approach the problem of ensuring safety in reinforcement learning from a formal methods perspective. We begin with an unambiguous and rich set of specifications of what safety and more generally correctness mean. To this end, we adopt temporal logic as a specification language [6]. For algorithmic purposes, we focus on the so-called safety fragment of (linear) temporal logic [12]. We then investigate the question “how can we let, whenever it is fine, a learning agent do whatever it is doing, and also monitor and interfere with its operation whenever absolutely needed in order to ensure safety?” In this paper, we introduce 
 
 
 
 
 
 
 
 
 
 
2 
actions 
reward 
Shield 
Learning Agent 
observation 
Environment 
safe action 
reward 
action 
Learning Agentobservation 
Environment 
reward 
safe actions 
Learning Agent 
observation 
Environment 
safe action 
Shield 
Fig. 1: Preemptive Shielding. 
actions 
reward 
Shield 
Learning Agent 
observation 
Environment 
safe action 
reward 
action 
Learning Agentobservation 
Environment 
 
 
 Agent 
 
 
safe action 
 
Fig. 2: Post-Posed Shielding. 
shielded learning, a framework that allows to apply machine learning to control systems in a way that the correctness of the system’s execution against a given specification is assured during the learning and controller execution phases, regardless of how fast the learning process converges. 
In the traditional reinforcement learning setting, in every time step, the learning agent chooses an action and sends it to the environment. The environment evolves according to the action and sends the agent an observation of its state and a reward associated with the underlying transition. The objective of the learning agent is to optimize the reward accumulated over this evolution. 
Our approach introduces a shield into the traditional reinforcement learning setting. The shield is computed upfront from the safety part of the given system specification and an abstraction of the agent’s environment dynamics. It ensures safety and minimum interference. With minimum interference we mean that the shield restricts the agent as little as possible and forbids actions only if they could endanger safe system behavior. 
We modify the loop between the learning agent and its environment in two alternative ways, depending on the location at which the shield is implemented. In the first one, depicted in Fig. 1, the shield is implemented before the learning agent and acts each time the learning agent is to make a decision and provides a list of safe actions. This list restricts the choices for the learner. The shield provides minimum interference, since it allows the agent to follow any policy as long as it is safe. In the alternative implementation of the shield, depicted in Fig. 2, it monitors the actions selected by the learning agent and corrects them if and only if the chosen action is unsafe. 
Shielding offers several pragmatic advantages: Even though the inner working of learning algorithms is often complex, shielding with respect to critical safety specifications may be manageable (as we demonstrate in upcoming sections). The algorithms we present for the computation of shields make relatively mild assumptions on the inputoutput structure of the learning algorithm (rather than its inner working). Consequently, the correctness guarantees are agnostic—to an extent to be described precisely—to the learning algorithm of choice. Our setup introduces a clear boundary between the learning agent and the shield. This boundary helps to separate the concerns, e.g., safety and correctness on one side and convergence and optimality on the other and provides a basis for the convergence analysis of a shielded reinforcement learning algorithm. Last but not least, the shielding framework is compatible with mechanisms such as function approximation, employed by learning algorithms in order to improve their scalability.
3 2 Related Work 
We now overview two complementing yet mostly isolated views on safety in reinforcement learning and in formal methods. 
Safety in Reinforcement Learning. An exploration process is called safe if no undesirable states are ever visited, which can only be achieved through the incorporation of external knowledge [8,14]. The safety fragment of temporal logic that we consider is more general than the notion of safety of [8] (which is technically a so-called invariance property [1]). One way of guiding exploration in learning is to provide teacher advice. A teacher (usually a human) provides advice (e.g., safe actions) when either the learner [15,4] or the teacher [22,19] considers it to be necessary to prevent catastrophic situations. For example, in a Q-learning setting, the agent acts on the teacher’s advice, whenever advice is provided. Otherwise, the agent chooses randomly between the set of actions with the highest Q-values. In each time step, the human teacher tunes the reward signal before sending it to the agent [19,20]. Our work is closely related to teacher-guided RL, since a shield can be considered as a teacher, who provides safe actions only if absolutely necessary. In contrast to previous work, the reward signal does not have to be manipulated by the shield, since the shield corrects unsafe actions in the learning and deployment phases. 
Safety in Formal Methods. Traditional correct-by-construction controller computation techniques are based on computing an abstraction of the environment dynamics and deriving a controller that guarantees to satisfy the specification under the known environment dynamics. Such methods combine reactive synthesis with faithful environment modelling and abstraction. Wongpiromsarn et al. [24] define a receding horizon control approach that combines continuous control with discrete correctness guarantees. For simple system dynamics, the controller can be computed directly [9]. For more complex dynamics, both approaches are computationally too difficult. A mitigation strategy is to compute a set of low-level motion primitives to be combined to an overall strategy [5]. Having many motion primitives however also leads to inefficiency. All of the above approaches have in common that a faithful, yet precise enough, abstraction of the physical environment is required, which is not only difficult to obtain in practice, but also introduces the mentioned computational burden. Control methods based on reinforcement learning partly address this problem, but do not typically incorporate any correctness guarantees. Wen et al. [23] propose a method to combine strict correctness guarantees with reinforcement learning. They start with a non-deterministic correct-by-construction strategy and then perform reinforcement learning to limit it towards cost optimality without having to know the cost function a priori. Unlike the approach in the paper, their technique does not work with function approximation, which prevents it from being used in complex scenarios. Junges et al. [10] adopt a similar framework in a stochastic setting. A major difference between the works by Wen et al. and Junges et al. [23,10] on the one hand and the shielding framework on the other hand is the fact that the computational cost of the construction of the shield depends on the complexity of the specification and a very abstract version of the system, and is independent of the state space components of the system to be controlled that are
4 irrelevant for enforcing the safety specification. Fu et al. [7] establish connections between temporal-logic-constrained strategy synthesis in Markov decision processes and probably-approximately-correct-type bounds in learning [21]. Bloem et al. [3] proposed the idea to synthesize a shield that is attached to a system to enforce safety properties at run time. We adopt this idea, and present our own realization of a shield, geared to the needs of the learning setting. 
3 Preliminaries 
We now introduce some basic concepts used in the following. A word is defined to be a finite or infinite sequence of elements from some set Σ. 
The set of finite words over an alphabet Σ is denoted by Σ∗, and the set of infinite words over Σ is written as Σω. The union of Σ∗ and Σω is denoted by the symbol Σ∞. 
A probability distribution over a (finite) set X is a function µ : X → [0, 1] ⊆ R with 
∑ x∈X µ(x) = µ(X) = 1. The set of all distributions on X is denoted by Distr(X). 
A Markov decision process (MDP)M = (S, sI,A,P,R) is a tuple with a finite set S of states, a unique initial state sI ∈ S, a finite set A = {a1 . . . an} of Boolean actions, a probabilistic transition function P : S × A → Distr(S), and an immediate reward function R : S ×A × S→ R. 
In reinforcement learning (RL), an agent must learn a behavior through trial-and-error via interactions with an unknown environment modeled by a MDP M = (S, sI,A,P,R). Agent and environment interact in discrete time steps. At each step t, the agent receives an observation st. It then chooses an action at ∈ A. The environment then moves to a state st+1 with the probability P(st, at, st+1) and determines the reward rt+1 = R(st, at, st+1). We refer to negative rewards rt < 0 as punishments. The return R = 
∑ ∞ 
t=0 γ trt is the cumulative future discounted reward, where rt is the immediate 
reward at time step t, and γ ∈ [0, 1] is the discount factor that controls the influence of future rewards. The objective of the agent is to learn an optimal policy Π : S→A that maximizes (over the class of policies considered by the learner) the expectation of the return; i.e. maxπ∈ΠEπ(R), where Eπ(.) stands for the expectation w.r.t. the policy π. 
We consider a reactive system with a finite set I = {i1, . . . , im} of Boolean input propositions and a finite set O = {o1, . . . , on} of Boolean output propositions. The input alphabet is ΣI = 2I, the output alphabet is ΣO = 2O, and Σ = ΣI × ΣO. We refer to words over Σ as traces σ. We write |σ| for the length of a trace σ ∈ Σ∞. A set of words L ⊆ Σ∞ is called a language. 
A finite-state reactive system is a tuple S = (Q, q0, ΣI, ΣO, δ, λ) with the input alphabet ΣI, the output alphabet ΣO, a finite set of states Q, and the initial state q0 ∈ Q. We assume that ΣI is a product of Σ1 
I and Σ2 I , i.e., we have ΣI = Σ1 
I × Σ 2 I . Then, δ : 
Q×ΣI → Q is a complete transition function, and λ : Q×Σ1 I → ΣO is a complete output 
function. Given the input trace σI = (x1 0, x 
2 0)(x1 
1, x 2 1) . . . ∈ Σ∞I , the system S produces the 
output trace σO = S(σI) = λ(q0, x1 0)λ(q1, x1 
1) . . . ∈ Σ∞O , where qi+1 = δ(qi, (x1 i , x 
2 i )) for 
all i ≥ 0. The input and output traces can be merged to the trace of S over the alphabet ΣI×ΣO, which is defined as σ = ((x1 
0, x 2 0), λ(q0, x1 
0))((x1 1, x 
2 1), λ(q1, x1)) . . . ∈ (ΣI×ΣO)ω. 
The finite-state reactive system definition is similar to that of a Mealy machine, except that for choosing the output along a transition of the machine, only a part of
5 the input is available. The larger generality of this model is needed for one type of shield that we introduce later, and such an extended Mealy-type computational model has already been used by Saqib and Somenzi [17] in the past. A specification ϕ defines a set L(ϕ) ⊆ Σ∞ of allowed traces. The reactive system S realizes ϕ, denoted by S |= ϕ, iff L(S) ⊆ L(ϕ). ϕ is realizable if there exists such an S. We assume ϕ is a set of properties {ϕ1, . . . , ϕl} such that L(ϕ) = 
⋂ iL(ϕi). A 
system satisfies ϕ iff it satisfies all its properties. In most applications of formal methods, specifications of reactive systems are given 
as formulas in some temporal logic. Linear temporal logic [16] (LTL) is a commonly used formal specification language. Given a set of propositions AP, an LTL formula describes a language in (2AP)ω. LTL extends Boolean logic by the introduction of temporal operators such as X (next time), G (globally/always), F (eventually), and U (until). To use LTL for specifying a set of allowed traces by a reactive system, the joint alphabet Σ = ΣI×ΣO of the system must be decomposable into Σ = 2API ×Σrest 
I ×2APO×Σrest O for 
some system input and output components Σrest I and Σrest 
O that we do not want to reason about in the LTL specification. Then, the LTL formula can use AP = API ∪ APO as the set of atomic propositions. Given a trace σ, we write σAP to denote a copy of the trace where, in each character, the factors Σrest 
O and Σrest I have been stripped away so that 
σAP ∈ (2AP)ω. Let us consider an example for an LTL specification that we build from ground up. 
By default, LTL formulas are evaluated at the first element of a trace. The LTL formula r holds on a trace σAP = σ0σ1σ2 . . . ∈ (2AP)ω if and only if r ∈ σ0. The next-time operator X allows to look one step into the future, so the LTL formula Xg holds if g ∈ σ1. We can take the disjunction between the formulas r and Xg to obtain an LTL formula (r ∨ Xg) which holds for a trace if at least one of r or Xg hold. We can then wrap (r ∨ Xg) into the temporal operator G to obtain G(r ∨ Xg). The effect of adding this operator is that in order for σAP to satisfy G(r ∨ Xg) is that (r ∨ Xg) has to hold at every position in the trace. All in all, we can formalize this description by stating that we have that σ |= G(r ∨ Xg) holds if and only if for every i ∈ N, at least one of r ∈ σi and g ∈ σi+1 hold. 
A specification is called a safety specification if every trace σ that is not in the language represented by the specification has a prefix such that all words starting with the prefix are also not in the language. Intuitively, a safety specification states that “something bad should never happen”. Safety specifications can be simple invariance properties (such as “the level of a water tank should never fall below 1 liter”), but can also also be more complex (such as “whenever a valve is opened, it stays open for at least three seconds”). For specifications in LTL, it is known how to check if it is a safety language and how to compute a safety automaton that represents it [11]. 
Such an automaton is defined as a tuple ϕs = (Q, q0, Σ, δ, F), where Σ = ΣI × ΣO, δ : Q × Σ → Q, and F ⊆ Q is a set of safe states. A run induced by a trace σ = σ0σ1 . . . ∈ Σ∞ is a sequence of states q = q0q1 . . . such that qi+1 = δ(qi, σi). A trace σ of a system S satisfies ϕs if the induced run visits only safe states, i.e., ∀i ≥ 0 . qi ∈ F. 
A (2-player, alternating) game is a tuple G = (G, g0, ΣI, ΣO, δ,win), where G is a finite set of game states, g0 ∈ G is the initial state, δ : G × ΣI × ΣO → G is a complete transition function, and win : Gω 
→ B is a winning condition. The game is played by
6 the system and the environment. In every state g ∈ G (starting with g0), the environment chooses an input σI ∈ ΣI, and then the system chooses some output σO ∈ ΣO. These choices by the system and the environment define the next state g′ = δ(g, σI, σO), and so on. The resulting (infinite) sequence g = g0g1 . . . is called a play. A play is won by the system iff win(g) is true. A (memoryless) strategy for the system is a function ρ : G × ΣI → ΣO. A strategy is winning for the system if all plays g that can be constructed when defining the outputs using the strategy satisfy win(g). The winning region W is the set of states from which a winning strategy exists. 
A safety game defines win via a set Fg ⊆ G of safe states: win(g0g1 . . .) is true 
iff ∀i ≥ 0 . gi ∈ Fg, i.e., if only safe states are visited. We will use safety games to synthesize a shield, which implements the winning strategy in a new reactive system S = (G, q0, ΣI, ΣO, δ′, ρ) with δ′(g, σI) = δ(g, σI, ρ(g, σI)). 
4 Safety Specifications, Abstractions, and Game Solving 
The goal of this paper is to combine the best of two worlds, namely (1) the formal correctness guarantees of a controller with respect to a temporal logic specification, as provided by formal methods (and reactive synthesis in particular), and (2) the optimality with respect to an a priori unknown performance criterion, as provided by reinforcement learning. 
Consider the example of a path planner for autonomous vehicles. Many general requirements on system behaviors such as safety concerns may be known and expressed as specifications in temporal logic and can be enforced by reactive controllers. This includes always driving in the correct lane, never jumping the red light, and never exceeding the speed limit [23]. A learning algorithm is able to incorporate more subtle considerations, such as specific intentions for the current application scenario and personal preferences of the human driver, such as reaching some goal quickly but at the same time driving smoothly. 
By combining reinforcement learning with reactive synthesis, we achieve safe reinforcement learning, which we define in the following way: 
Definition 1. Safe reinforcement learning is the process of learning an optimal policy while satisfying a temporal logic safety specification ϕs during the learning and execution phases. 
In the following, we consider a safety specification to be given in the form of a deterministic safety word automaton ϕs = (Q, q0, Σ, δ, F), i.e., an automaton in which only safe states in F may be visited. Note that since safety specifications given in linear temporal logic can be translated to such automata [11], this assumption does not preclude the use of temporal logic as specification formalism. 
Reactive synthesis enforces ϕs by solving a safety game built from ϕs and an abstraction of the environment in which the policy is to be executed. The game is played by the environment and the system. In every state q ∈ Q, the environment chooses an input σI ∈ ΣI, and then the system chooses some output σO ∈ ΣO. The play is won by the system if only safe states in F are visited during the play. In order to win, the system
7 has to plan ahead: it can never allow the play to visit a state from which the environment can force the play to visit an unsafe state in the future. 
Planning ahead is the true power of synthesis. Let us revisit the autonomous driver example. Suppose that the car is heading towards a cliff. In order to enforce that the car never crosses the cliff, it has to be slowed down long before it reaches the cliff, and thus far before an abnormal operating condition such as falling down can possibly be detected. In particular, the system has to avoid all states from which avoiding to reach the cliff is no longer possible. 
Planning ahead does not require the environment dynamics to be completely known in advance. However, to reason about when exactly a specification violation cannot be avoided, we have to give a (coarse finite-state) abstraction of the environment dynamics. Given that the environment is often represented as an MDP in reinforcement learning, such an abstraction has to be conservative with respect to the behavior of the real MDP. This approximation may have finitely many states even if the MDP has infinitely many states and/or is only approximately known. 
Formally, given an MDP M = (S, sI,A,P,R) and an MDP observer function f : S → L for some set L, we call a deterministic safety word automaton ϕM = (Q, q0, Σ, δ, F) an abstraction ofM if Σ = A × L and for every trace s0s1s2 . . . ∈ Sω 
with the corresponding action sequence a0a1 . . . ∈ Aω of the MDP, for every automaton run q = q0q1 . . . ∈ Qω of ϕM with qi+1 = δ(qi, (li, ai)) for li = L(si) and all i ∈ N, we have that q always stays in F. An abstraction of an MDP describes how its executions can possibly evolve, and provides the needed information about the environment to allow planning ahead with respect to the safety properties of interest. Without loss of generality, we assume in the following that ϕM has no states in F from which all infinite paths eventually leave F. This requirement ensures that paths that model traces that cannot occur inM are rejected by ϕM as early as possible. 
The following example shows how specification automata and abstractions of MDPs are used. 
Example 1. We want to learn an energy-efficient controller for a hot water storage tank, depicted in Figure 3. Water stored in the task is kept warm by a heater whose energy consumption depends on the filling level of the tank, but we do not know what the exact relationship is. 
The outflow is always between 0 and 1 liters per second, and the inflow is known to be between 1 and 2 liters per second whenever the valve is open (and it is 0 otherwise). The capacity of the tank is limited to 100 liters, and whenever the inflow is switched on or off, the setting has to be kept for at least three seconds to limit the wear-out of the valve. Also, the tank must never overflow or run dry. 
Let us now formalize this example. We can express the safety specification for the water tank valve controller using the following linear temporal logic formula: 
G(level > 0) ∧ G(level < 100) ∧ G((open ∧ Xclose)→ XXclose ∧ XXXclose) ∧ G((close ∧ Xopen)→ XXopen ∧ XXXopen)
8 The specification consists of four conjuncts, where the first two conjuncts enforce the water levels to be between the minimum and maximum thresholds. The next conjunct enforces that if the valve is open and then closed, then it has to stay closed for two more time steps (seconds). The final conjunct enforces that if the valve is closed and then opened, it has to stay open for two more time steps. 
We can translate the specification to the safety automaton shown in Figure 4. It uses the action sets A = {open, closed} for the inflow valve state, and the label set L = {level < 1, 1 ≤ level ≤ 99, level > 99} as needed information about the water tank filling status. What we know about the behavior of the water tank can be summarized as the abstraction automaton given in Figure 5. 
We will show in Section 6 how to compute a shield from an abstraction automaton and a safety specification automaton. We will then revisit this example and give the resulting shield that enforces the specification. The shield will enforce that when the water level in the tank becomes too low, the inflow valve is opened until some minimum level of 4 is reached, and it will also prevent the inflow from being opened when the level is above 93. The latter is necessary as the valve has to stay open for at least three time steps. So as the inflow may be up to 2 liters/second during this time and the outflow may be 0, there is otherwise an overflow risk. As the shield is generated using the specification, it plans ahead for this not to happen, so it must prevent the opening of the inflow valve if the level is above 93. Note that for more complicated specifications, the shield behavior can become much more complicated as well. 
Fig. 3: A hot water storage tank with an inflow, an outflow, and a tank heater. 
5 Framework for Shielded Reinforcement Learning 
In this section, we introduce a correct-by-construction reactive system, called a shield, into the traditional learning process. We propose two different ways to modify the loop between the learning agent and its environment: In Sec. 5.1 we introduce the shield before the learning agent. In each time step, the shield modifies the list of actions available to the learner by providing a list of safe actions that the learning agent can choose from. In Sec. 5.2 the shield is implemented after the learning agent. The shield monitors the actions selected by the learning agent, and overwrites them if and only if the
9 qa 
(close, 1 ≤ level ≤ 99) 
qb (open, 1 ≤ level ≤ 99) 
qc 
(open, 1 ≤ level ≤ 99) 
qd 
(open, 1 ≤ level ≤ 99) 
(open, 1 ≤ level ≤ 99) 
qe 
(close, 1 ≤ level ≤ 99) 
q f (close, 1 ≤ level ≤ 99) 
(close, 1 ≤ level ≤ 99) 
Fig. 4: The specification for the water tank controller. All states are accepting and transitions leading to the error state (which exists in addition to the states in the figure and is not accepting) are not shown. 
chosen action is unsafe. Based on the location at which the shield is applied, we call it preemptive shielding and post-posed shielding, respectively. For both settings we make the following assumptions. 
Assumption 1 (i) The environment can be modeled as an MDPM = (S, sI,A,P,R). (ii) We have constructed an abstraction ϕM. (iii) The learner accepts elements from S ×Q as state input (for the state space of the shield Q). 
We describe the operation of a learner and a shield together in this section, and give the construction for computing the shield in the next section. In both preemptive and post-posed shielding, the shield will be given as a reactive systemS = (Q, q0, ΣI, ΣO, δ, λ). 
5.1 Preemptive Shielding 
Fig. 6 depicts the preemptive shielding setting. The interaction between the agent, the environment and the shield is as follows: At every time step t, the shield computes a set of all safe actions {a1 
t , . . . , a k t }, i.e., it takes the set of all actions available, and removes 
all unsafe actions that would violate the safety specification ϕs. The agent receives this list from the shield, and picks an action at ∈ {a1 
t , . . . , a k t } from it. The environment 
executes action at, moves to a next state st+1, and provides the reward rt+1. The task of the shield is basically to modify the set of available actions of the agent in every time step such that only safe actions remain. 
More formally, for a preemptive shield, we have ΣO = 2A, as the shield outputs the set of actions for the learner to choose from for the respective next step. The shield observes the label of the last MDP state in the sequence so far and provides the set of safe actions. For selecting the next transition of the finite-state machine that represents the shield, it also makes use of the action actually chosen by the agent. So for the input alphabet of the shield, we have ΣI = Σ1 
I × Σ 2 I with Σ1 
I = L and Σ2 I = A.
10 
q0 
q1 
q2 
. . . 
q99 
(∗, 0 ≤ level < 1) 
(∗, 1 ≤ level < 2) 
(∗, 2 ≤ level < 3) 
(∗, 99 ≤ level < 100) 
(open, 1 ≤ level < 2) 
(close, 0 ≤ level < 1) 
(open, 2 ≤ level < 3) 
(close, 1 ≤ level < 2) 
. . .. . . 
. . .. . . 
(open, 2 ≤ level < 3) 
. . . 
(open, 3 ≤ level < 4) 
. . . 
(open, 4 ≤ level < 5) 
. . . 
(open, 99 ≤ level < 100) 
Fig. 5: The abstraction of the water tank behavior. All states are accepting and transitions leading to the error state (which exists in addition to the states in the figure and is not accepting) are not shown.
11 
Shield 
Learning Agent 
Environment 
𝑎𝑡 
rt+1 
{at 1, … , at 
n} 
Learning Agent 
st+1 
Environment 
at 
Shield 
{at 1, … , at 
k} st+1 
rt+1 
Fig. 6: Preemptive Shielding. 
Shield 
Learning Agent 
Environment 
𝑎𝑡 
rt+1 
{at 1, … , at 
n} 
Learning Agent 
st+1 
Environ ent 
at 
Shield 
{at 1, … , at 
k} st+1 
rt+1 
Fig. 7: Post-Posed Shielding. 
The shield and the learner together produce a trace s0a0s1a1 . . . ∈ (S × A)ω in the MDP if there exists a trace q0q1 . . . ∈ Qω in the shield such that, for every i ∈ N, we have ai ∈ λ(qi,L(si)) and qi+1 = δ(qi, (L(si), ai). 
Properties of Preemptive Shielding. The preemptive shielding approach can also be seen as transforming the original MDPM into a new MDPM′ = (S′, sI,A′,P′,R′) with the unsafe actions at each state removed, and where S′ is the product of the original MDP and the state space of the shield. For each s ∈ S′, we create a new subset of available actions A′s ⊆ As by applying the shield to As and eliminating all unsafe actions. From each state s ∈ S′, the transition function P′ contains only transition distributions from P for actions contained inA′s. 
5.2 Post-Posed Shielding 
We propose a second shielding setting, in which the shield is placed after the learning algorithm, as shown in Fig. 7. The shield monitors the actions of the agent, and substitutes the selected actions by safe actions whenever this is necessary to prevent the violation of ϕs. In each step t, the agent selects an action a1 
t . The shield forwards a1 t 
to the environment, i.e., at = a1 t . Only if a1 
t is unsafe with respect to ϕs, the shield selects a different safe action at , a1 
t instead. The environment executes at, moves to st+1 and provides rt+1. The agent receives at and rt+1, and performs policy updates based on that information. For the executed action at, the agent updates its policy using rt+1. The question is what the reward for a1 
t should be in case we have at , a1 t . We discuss two 
different approaches. 
1. Assign a punishment r′t+1 to a1 t . The agent assigns a punishment r′t+1 < 0 to the 
unsafe action a1 t and learns that selecting a1 
t at state st is unsafe, without ever violating ϕs. However, there is no guarantee that unsafe actions are not part of the final policy. Therefore, the shield has to remain active even after the learning phase. 
2. Assign the reward rt+1 to a1 t . The agent updates the unsafe action a1 
t with the reward rt+1. Therefore, picking unsafe actions can likely be part of an optimal policy by the agent. Since an unsafe action is always mapped to a safe one, this does not pose a problem and the agent never has to learn to avoid unsafe actions. Conse-quently, the shield is (again) needed during the learning and execution phases.
12 
Properties of Post-Posed Shielding. The big advantage of post-posed shielding is that it works even if the learning algorithm is already in the execution phase and therefore follows a fixed policy. In every step, the learning algorithm only sees the state of the MDP (without the state of the shield), and then the shield corrects the learner’s actions whenever this is necessary to ensure safe operation of the system. The learning agent does not even need to know that it is shielded. 
In order to be less restrictive to the learning algorithm, we propose that in every time step, the agent provides a ranking rankt = (a1 
t , . . . , a k t ) on the allowed actions, i.e., 
the agent wants a1 t to be executed the most, a2 
t to be executed the second most, etc. The ranking does not have to contain all available actions, i.e. 1 ≤ |rankt| ≤ n, where n is the number of available actions in step t. The shield selects the first action at ∈ rankt that is safe according to ϕs. Only if all actions in rankt are unsafe, the shield selects a safe action at < rankt. Both approaches for updating the policy discussed before can naturally be extended for a ranking of several actions. A second advantage of having a ranking on actions is that the learning agent can perform several policy updates at once; e.g., if all actions in rankt are unsafe, the agent can perform |rankt| + 1 policy updates in one step by using the rewards r′t+1 or rt+1 for all of them, depending on which of the above variants is used. 
6 A Shield Synthesis Algorithm for Reinforcement Learning 
A shield S is introduced into the traditional learning process, either before or after the learning agent. In both cases, S enforces two properties: correctness and minimum interference. First, S enforces correctness against a given safety specification ϕs at run time. With minimum interference, we mean that the shield restricts the agent as rarely as possible. The shield S is computed by reactive synthesis from ϕs and an MDP abstraction ϕM that represents the environment in which the agent shall operate. 
In this section, we give an algorithm to compute shields for preemptive shielding and post-posed shielding. We prove that the computed shields (1) enforce the correctness criterion, and (2) are the minimally interfering shields among those that enforce ϕs on all MDPs for which ϕM is an abstraction. 
The first steps of constructing the shield are the same for both variations of shielding. Given is an RL problem in which an agent has to learn an optimal policy for an unknown environment that can be modelled by an MDP M = (S, sI,A,P,R) while satisfying a safety specification ϕs = (Q, q0, Σ, δ, F) with Σ = ΣI × ΣO and A = ΣO. We assume some abstraction ϕM = (QM, q0,M,A × L, δM,FM) ofM for some MDP observer function f : S → L to be given. Since ϕs models a restriction of the traces of the MDP and the learner together that we want to enforce, we assume it to have Σ = L×A, i.e., it reads the part of the system behavior that the abstraction is concerned with. We perform the following steps for both shield types. 
1. We translate ϕs and ϕM to a safety game G = (G, g0, ΣI, ΣO, δ,Fg) between two players. In the game, the environment player chooses the next observations from the MDP state (i.e., elements from L), and the system chooses the next action.
13 
Formally, G has the following components: 
G = Q ×QM, g0 = (q0, q0,M), ΣI = L, ΣO = A, 
δ((q, qM), l, a) = (δ(q, (l, a)), δM(q, (l, a))), for all (q, qM) ∈ G, l ∈ L, a ∈ A, and 
Fg = (F ×QM) ∪ (Q × (QM \ FM)). 
In the construction, the state space of the game is the product between the specification automaton state set and the abstraction state set. The safe states in the game (in the set Fg) are the ones at which either the specification automaton is in a safe state, or the abstraction is in an unsafe state. The latter case represents that the observed MDP behavior differs from the behavior that was modeled in the abstraction. For game solving, it is important that such cases (whose occurrence in the field witnesses the incorrectness of the abstraction) count as winning for the system player, as the system player only needs to work correctly in environments that conform to the abstraction. 
2. Next, we compute the winning region W ⊆ Fg of G by standard safety game solving as described in [3]. 
To compute a preemtive shield, we then perform the following step: 
3. We translate G and W to a reactive system S = (Q,S q0,S, ΣI,S, ΣO,S, δS, λS) that constitutes the shield with ΣI,S = Σ1 
I,S×Σ 2 I,S for Σ1 
I,S = L and Σ2 I,S = A. The shield 
has the following components: 
QS = G, q0,S = g0, 
ΣI,S = A× L, 
ΣO,S = 2A, δS(g, l, a) = δ(g, l, a) 
for all g ∈ G, l ∈ L, a ∈ A, and λS(g, l) = {a ∈ A | δ(g, l, a) ∈W} 
for all g ∈ G, l ∈ L. 
To simplify S, it makes sense to optionally remove all states that are unreachable from q0,S after constructing S. 
To exemplify these steps, let us reconsider the example from Section 4. Building the product game between the specification automaton and the MDP abstraction leads to a game with 602 states (if we merge all states in F×QM into a single error state and all states in Q× (QM \ FM) into a single paradise state from which the game is always won by the system). If we solve the game, then most of the states are winning, but a few
14 
are not. Figure 8 shows a small fraction of the game that contains such non-winning states. We can see that, in state (q3, qd), the system should not choose action close, as otherwise the system cannot avoid to reach qfail. It could be the case that qfail is actually not reached (when the environment chooses to let the level stay the same for a step), but we cannot be sure because we have to consider all evolutions of the environment to be possible that are consistent with our abstraction. Thus, the shield needs to deactivate the close action in state (q3, qd). 
(q3, qd) (q2, qe) (q1, q f ) qfail 
. . .. . .. . . 
. . . open, close 
0 ≤ level ≤ 1 close 
1 ≤ level ≤ 2 close 
2 ≤ level ≤ 3 
open 
close, 1 ≤ level ≤ 2 
close, 2 ≤ level ≤ 3 
open, 4 ≤ level ≤ 5 
open, 5 ≤ level ≤ 6 
close, 3 ≤ level ≤ 4 
Fig. 8: An excerpt for the product game of our running example. Transitions to paradise states are not shown. 
The shield allows all actions that are guaranteed to lead to a state in W, no matter what the next observation is. Since these states, by the definition of the set of winning states, are exactly the ones from which the system player can enforce not to ever visit a state not in F, the shield is minimally interfering. It disables all actions that may lead to an error state (according to the abstraction). 
The construction of a post-posed shield is very similar to the construction of the preemptive shield. The main difference is that the post-posed shield always outputs a single action. Thus, the last step of the construction above should read as follows. 
3. We translate G and W to a reactive system S = (Q,S q0,S, ΣI,S, ΣO,S, δS, λS) that constitutes the shield with ΣI,S = Σ1 
I,S × Σ 2 I,S for Σ1 
I,S = L ×A and Σ2 I,S = {·}. The
15 
shield has the following components: 
QS = G, q0,S = (q0, q0,M), ΣI,S = A× L, ΣO,S = A, 
λS(g, l, a) = 
 a if δ(g, l, a) ∈W a′ if δ(g, l, a) <W for some 
arbitrary but fixed a′ with δ(g, l, a′) ∈W, 
δS(g, l, a) = δ(g, l, λS(g, l, a)) for all g ∈ G, l ∈ L, a ∈ A. 
The construction can be extended naturally if a ranking of actions rankt = {a1 t , . . . , a 
n t } 
is provided by the agent. Then, the shield selects the first action at = ai t that is allowed 
by ϕs. Only if all actions in rankt are unsafe, the shield is allowed to deviate and to select a safe action at < rankt. 
6.1 Correctness and Minimal Interference of the Shields 
We now prove that the shields computed according to the definitions indeed have the claimed properties, namely correctness, and minimal interference. For brevity, we detail the case of preemptive shields. The line of reasoning for post-posed shielding is similar. 
Correctness: A shield works correctly if for every trace s0a0s1a1 . . . ∈ (S × A)ω that MDP, shield and learner can together produce, we have that ( f (s0), a0)( f (s1), a1) . . . is in the language of the specification automaton ϕS for the MDP labeling function f . Additionally, the shield must always report at least one available action at every step. 
Let q0q1 . . . ∈ Qω be the run of ϕS corresponding to s0a0s1a1 . . ., i.e., for which for every i ∈N, we have ai ∈ λ(qi, f (si)) and qi+1 = δ(qi, ( f (si), ai)). By the construction of the shield, we have that Q = Q ×QM, where Q is the state space of ϕS and QM is the state space of the abstraction. Hence, we can also write q0q1 . . . as (qS 
0 , q M 
0 )(qS 1 , q M 
1 ) . . ., where qM0 qM1 . . . is the run of the abstraction automaton on s0a0s1a1 . . . (as defined in Section 4) and qS 
0qS 1 . . . is a run of ϕS on s0a0s1a1 . . .. By the construction of the shield, 
it only has reachable states (qS, qM) that are in the set of winning positions. For all possible next labels l ∈ L, there exists at least one action such that if the action is taken, then the next state (q′S, q′M) is winning as well. Therefore, the shield cannot deadlock. As far as correctness is concerned, the qS component of the run of the shield will always reflect the state of the safety automaton along the trace, and since a winning strategy makes sure that only winning states are ever visited along a play, by the definition of Fg, the error state of ϕS can only be visited after the error state for the abstraction MDP has been visited (and hence the abstraction turned out to be incorrect).
16 
Minimal Interference: Let the shield, learner, and MDP together produce a prefix trace s0a0s1a1s2a2 . . . sk that induces a (prefix) run q0q1 . . . qk−1 ∈ Q∗ of the safety automaton ϕS that we used as the representation of the specification for building the shield. Assume that the shield deactivates an action ak+1 that is available from state sk in the MDP. We show that the shield had to deactivate ak+1 as there is another MDP that is consistent with the observed behavior and the abstraction for which, regardless of the learner’s policy, there is a non-zero probability to violate the specification after the trace prefix s0a0s1a1s2a2 . . . skak+1. 
Using the abstract finite-state machine ϕM = (QM, q0,M, Σ, δ, F), we define this other MDP M′ = (S′, s′I,A,P 
′,R) with S′ = QM × L, s′I = q0,M × f (s0), A being the same set of actions as in the original MDP, and where P′((q, l), a) is a uniform distribution over all elements from the set {(q′, l′) ∈ QM × L | q′ = δ(q, (l, a)), q′ ∈ F,∃a′ ∈ A.δ(q′, (l′, a′)) ∈ F} for every (q, l) ∈ S′ and a ∈ A. Every state (q′, l′) ∈ S′ 
is mapped to l′ by the abstraction function f . The reward function is the same as in the original MDP, except that we ignore the (new) state component of the shield. 
Assume now that action ak+1 was activated after the prefix trace s0a0s1a1s2a2 . . . sk while the shield is in a state (qS, qM). We have thatM′ is an MDP in which every finitelength label sequence that is possible in the abstraction for some action sequence has a non-zero probability to occur if the action sequence is chosen. Due to the construction of the shield by game solving, action ak+1 is only deactivated in state (qS, qM) if in the game, the environment player had a strategy to violate ϕS using only traces allowed by the abstraction. Since ϕS is a safety property, the violation would occur in finite time. Since inM′, all finite traces that can occur in the abstraction have a non-zero probability, activating ak+1 (and the learner choosing ak+1) would imply a non-zero proability to violate the specification in the future, no matter what the learner does in the future. Hence, the shield could not prevent a violation in such a case, and ak+1 needs to be deactivated. 
7 Convergence 
Define an MDPM = (S, sI,A,P,R), with discrete state set S, discrete state-dependent action sets As, and state-dependent transition functions Ps(a, s′) that define the probability of transitioning to state s′ when taking action a in state s. Assume also that a shield S = (QS, q0,S, ΣI,S, ΣO,S, δS, λS) is given for M and for some MDP labeling function f : S→ L. 
For both preemptive and post-posed shielding, we can build a product MDP M′ 
that represents the behavior of the shield and the MDP together. SinceM′ is a standard MDP, all learning algorithms that converge on standard MDPs can be shown to converge in the presence of a shield under this construction. Note that for the postposed shield case, this argument requires that whenever an action ranking is chosen by the learner that does not contain a safe action, there is a fixed probability distribution over the safe actions executed by the learner instead. This distribution may depend on the state of the MDP and the shield and the selected ranking, but must be constant over time, as otherwise we could not model the joint behavior of the shield and the environment MDP as a product MDP.
17 
In both the post-posed and preemptive cases, we make use of the fact that the learner has access to the state of the shield and can base its actions on it in this argument. Shields can be relatively large—especially for complex abstractions and specifications—as they have both the state spaces of the abstraction and the specification automaton as factors. On the other hand, for specifications of the form “at all points during the execution, the label of the MDP states should have a certain form”, the specification automaton has only a single state (plus an error state). The state space of the shield is then exactly the state space of the abstraction (plus paradise states and error states). If the abstraction state can furthermore be determined from the respective last MDP state label, then the shield can be modified to have a single state (plus error states and paradise states). The requirements from Assumption 1 can then be relaxed by allowing the learner to only observe the state of the MDP (rather than the states of both the MDP and the shield) because, if the MDP behaves according to the abstraction, then the paradise state is never visited. At the same time, the shield ensures that no error state is ever visited. Hence, the state space ofM′ can be restructured to have to the same state space ofM. In such a case, it suffices for the learner to observe the current state as state ofM rather thanM′. To the learner, this is indistinguishable from operating onM without a shield. 
8 Experiments 
We applied shielded reinforcement learning in four domains: (1) a robot in 9x9 and 15x9 grid worlds, (2) a self-driving car scenario, (3) an Atari R© game called SeaquestTM, and (4) the water tank example from Section 4. For clarity, we compare between a subset of shielding settings which we later specify for each problem. The simulations were performed on a computer equipped with an Intel R© CoreTMi7-4790K and 16 GB of RAM running a 64-bit version of Ubuntu R© 16.04 LTS. Source code, input files, and detailed instructions to reproduce our experiments are available for download.1 
8.1 Grid world Example 
We performed two experiments on a robot in a grid world. Snapshots of these environments are shown in Fig. 9. In both experiments, the robot’s objective is to visit all the colored regions in a given order while maintaining one or both of the following safety properties. 
– ϕs 1: the robot must not crash into walls or the moving opponent agent. This specifi-
cation applies to both experiments. – ϕs 
2: the robot must not stay on a bomb for more than two consecutive steps. This specification applies only to the 9x9 experiment. 
Fig. 10 shows the deterministic finite automata corresponding to ϕs 1 and ϕs 
2. If the robot visits all marked regions in a given order (called episode), a reward is 
granted, and if a safety property is violated, a penalty is applied. The agent uses tabular Q-learning with an ε-greedy explorer that is capable of multiple policy updates at once. 
1 https://github.com/safe-rl/safe-rl-shielding
18 
Fig. 9: Left: A 9x9 grid world with four bombs, a number of colored regions and walls (black) that must be visited in a specific order. Right: A 15x9 grid world with an opponent agent (green) circling the center of the grid-world and two colored regions that must be visited in a specific order. In both grid worlds, the robot (red) is only allowed to move north, south, east and west in each step. 
s0 s1 
Ou ∧ u Od ∧ d Ol ∧ l Or ∧ r 
else true s0 s1 
s2s3 
b ∧ s 
b ∧ ¬s ¬b 
¬s s¬s 
s 
true 
Fig. 10: DFAs for ϕs 1 (left) and ϕs 
2 (right). 
0 20 40 60 80 100 −0.20 
−0.10 
0.00 
0.10 
0.20 
Episodes 
A cc 
um ul 
at ed 
R ew 
ar d 
No shielding No shielding w/ Large penalty |rankt| = 3 w/ penalty 
0 20 40 60 80 100 
0.00 
0.02 
0.04 
0.06 
0.08 
0.10 
0.12 
Episodes 
|rankt| = 1 w/o penalty |rankt| = 3 w/o penalty |rankt| = 1 w/ penalty |rankt| = 3 w/ penalty 
Fig. 11: The accumulated reward per episode for the 9x9 (left) and the 15x9 (right) grid worlds. 
In the 9x9 grid-world, we synthesized a shield from ϕs 1 ∧ϕ 
s 2 and the (precise) envi-
ronment abstraction in 2 seconds. In the 15x9 experiment, we synthesized a shield from the (precise) environment abstraction and ϕs 
1 to prevent crashes into the wall and the moving opponent agent in 0.6 seconds.
19 
Fig. 11 shows that only the unshielded versions experience negative rewards. Fur-thermore, the shielded versions are not only safe, but also tend to learn more rapidly. Whenever an unsafe action is picked, the agent updates at least two actions with a |rankt| = 1 shield, and up to 4 actions with a |rankt| = 3. Fig. 11 (right) shows that only the shielded version |rankt| = 3 without penalty (blue, dashed) finds the optimal path, resulting in a higher average reward. In scenarios with |rankt| = 1 (red) or with penalties (solid), the agent computes a suboptimal path. In Fig. 11 (left), we compare between no shielding (red, dashed), no shielding with large penalties for unsafe actions (blue, solid), and a |rankt| = 3 post-posed shielding with penalties for corrected actions (green, solid). The unshielded version with large penalty does not reach the maximum reward score as the other two versions. In addition, the unshielded version does not speed up the learning of the agent as the |rankt| = 3 does. 
8.2 A Self-Driving Car Example 
This example considers an agent that learns to drive around a block in a clockwise direction in an environment with the size of 480x480 pixels. In each step, the car moves 3 pixel in the direction of its heading and can make a maximum turn of 7.5 degrees on the shortest direction to the commanded heading. After each step, the value of the reward and the new state of the car are returned. The state consists of the following four variables: the car’s position in the x-axis, its position in the y-axis, the cosine and the sine of its heading. The safety specification in this example is to avoid crashing into a wall. The input to the shield is calculated from the car’s state. It represents the side of the car with a distance less than 60 pixels away from any of the walls. Both of the preemptive and the post-posed shields were synthesized in 2 seconds. In each step, a positive reward is given if the car moves a step in a clockwise direction and a penalty is given if it moves in a counter-clockwise direction. A crash into the wall results in a penalty and a restart. The agent uses a Deep Q-Network (DQN) with a Boltzmann exploration policy. This network consists of four input nodes for the state variables, eight outputs nodes for the headings and three hidden layers. 
The plot in Fig. 12 shows that the accumulated rewards for unshielded reinforcement learning (red, dashed) increases over time, but still experiences crashes at the end of the simulation. The shielded version without punishment (blue, solid) learns more rapidly than the unshielded learning scenario and never crashes. 
8.3 Atari R© 2600 SeaquestTM 
SeaquestTM is a underwater combat game in which the agent controls a submarine. The agent has to pick up divers under water, while avoiding or destroying various objects, and must get to the surface before it runs out of oxygen. The goal of the agent is to maximize the game score. 
For our experiments, we used the OpenAI Gym1 library that integrates the Arcade Learning Environment (ALE) [2], and a Python implementation2 of DeepMind’s Deep 
1 https://gym.openai.com/ 2 https://github.com/devsisters/DQN-tensorflow
20 
0 50 100 150 
−40 
−20 
0 
20 
Episodes 
A cc 
um ul 
at ed 
R ew 
ar d 
No shielding |rankt| = 1 w/o penalty Preemptive Shielding 
Fig. 12: Left: The accumulated rewards per episode. Right: A snapshot of the environment, where the car is moving anti-clockwise. 
0 20 40 60 80 100 
0.15 
0.2 
0.25 
Episodes 
A cc 
um ul 
at ed 
R ew 
ar d 
No shielding |rankt| = 1 w/o penalty 
Fig. 13: Left: The accumulated rewards per episode. Right: A snapshot of SeaquestTM. 
Reinforcement Learning approach [13]. The agent receives as input only RGB images of the screen as in Fig. 13 (right). The agent is used purely as a black box, only changing actions that violate the specification described below. 
We model two simple safety properties. First, the submarine has to surface before oxygen runs out (ϕs 
1). Secondly, the submarine is not allowed to surface if it has enough oxygen but has not collected any divers yet (ϕs 
2). The specificationϕs = ϕs 1∧ϕ 
s 2 decides 
when the submarine has to surface and when it is not allowed to surface, depending on the actual depth, the status of the oxygen reserves, and the number of collected divers. We compute all inputs of the shield from the state of the Atari R© simulator. The results illustrated in Fig. 13 (left) show that shielding the learner did not change its performance, however, the safety properties ϕs 
1 ∧ ϕ s 2 were not violated when shielding 
the learner.
21 
8.4 The Water Tank Example 
In the example shown in Fig. 3, the tank must never run dry or overflow by controlling the inflow switch (ϕs 
1). In addition, the inflow switch must not change its mode of operation before 3 time steps have passed since the last mode change (ϕs 
2). Refer to example 1 of section 4, for a full description of the abstract water tank dynamics and specification. We generated a concrete MDP for this example in which the energy consumption depends only on the state and there are multiple local minima. A post-posed shield was synthesized from ϕs 
1 ∧ ϕ s 2, in less than a second. 
0 200 400 600 800 1,000 0 
2 
4 
6 
8 
10 
Episodes 
A cc 
um ul 
at ed 
R ew 
ar d 
No shielding - Q No shielding - SARSA |rankt| = 1 w/o penalty - Q 
|rankt| = 1 w/o penalty - SARSA 
Fig. 14: The accumulated rewards per episode for different shielding settings and learning algorithms for the water tank environment. 
Fig. 14 shows that both shielded (dashed lines) and unshielded Q-learning and SARSA experiments (solid lines) do reach an optimal policy. However, the shielded implementations reach the optimal policy in a significantly shorter time than the unshielded implementations. 
9 Conclusion 
We developed a method for reinforcement learning under safety constraints expressed as temporal logic specifications. The method is based on shielding the decisions of the underlying learning algorithm from violating the specification. We proposed an algorithm for the automated synthesis of shields for given temporal logic specifications. Even though the inner working of a learning algorithm is often complex, the safety criteria may still be enforced by possibly simple means. Shielding exploits this possibility. 
A shield depends only on the monitored input-output behavior, the environment abstraction, and the correctness specifications – it is independent of the intricate details of the underlying learning algorithm. 
We demonstrated the use of shielded learning on several reinforcement learning scenarios. In all of them, the shielded agents perform at least as well as the unshielded ones. In most cases, our approach even improved the learning performance.
22 
The main downside of our approach is that in order to prevent the learner from making unsafe actions, some approximate model of when which action is unsafe needs to be available. We argue that this is unavoidable if the allowed actions depend on the state of the environment, as otherwise there is no way to know which actions are allowed. Our experiments show, however, that in applications in which safe learning is needed, the effort to construct an abstraction is well-spent, as our approach not only makes learning safe, but also shows great promise of improving learning performance. 
Acknowledgements 
The authors want to thank Francisco Palau-Romero for help with some of the experiments. The first and last authors were supported partly by the grants AFRL FA8650-15-C-2546, AFRL 8650-16-C-2610, DARPA W911NF-16-1-0001 and ARO W911NF-15-1-0592. The last two authors were supported partly by NSF 1617639. The second and the fourth authors were supported by the Austrian Science Fund (FWF) through the projects RiSE (S11406-N23) and LogiCS (W1255-N23). The third author was supported by the Institutional Strategy of the University of Bremen, funded by the German Excellence Initiative. 
References 
1. Baier, C., Katoen, J.P.: Principles of Model Checking (Representation and Mind Series). The MIT Press (2008) 
2. Bellemare, M.G., Naddaf, Y., Veness, J., Bowling, M.: The arcade learning environment: An evaluation platform for general agents. Journal of Art. Intell. Research 47, 253–279 (2013) 
3. Bloem, R., Könighofer, B., Könighofer, R., Wang, C.: Shield synthesis: - runtime enforcement for reactive systems. In: Tools and Algorithms for the Construction and Analysis of Systems - 21st Int. Conf, TACAS 2015, London, UK, April 11-18, 2015. pp. 533–548 (2015) 
4. Clouse, J.: On integrating apprentice learning and reinforcement learning title2:. Tech. rep., Amherst, MA, USA (1997) 
5. DeCastro, J.A., Kress-Gazit, H.: Nonlinear controller synthesis and automatic workspace partitioning for reactive high-level behaviors. In: Proceedings of the 19th International Con-ference on Hybrid Systems: Computation and Control, HSCC 2016. pp. 225–234 (2016) 
6. Emerson, E.A.: Handbook of theoretical computer science (vol. b). chap. Temporal and Modal Logic, pp. 995–1072. MIT Press, Cambridge, MA, USA (1990) 
7. Fu, J., Topcu, U.: Synthesis of shared autonomy policies with temporal logic specifications. IEEE Trans. Automation Science and Engineering 13(1), 7–17 (2016) 
8. Garcı́a, J., Fernández, F.: A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research 16, 1437–1480 (2015) 
9. Henzinger, T.A., Kopke, P.W.: Discrete-time control for rectangular hybrid automata. Theor. Comput. Sci. 221(1-2), 369–392 (1999) 
10. Junges, S., Jansen, N., Dehnert, C., Topcu, U., Katoen, J.: Safety-constrained reinforcement learning for mdps. In: Tools and Algorithms for the Construction and Analysis of Systems -22nd Int. Conference, TACAS 2016, The Netherlands, April 2-8, 2016. pp. 130–146 (2016) 
11. Kupferman, O., Vardi, M.Y.: Model checking of safety properties. Formal Methods in System Design 19(3), 291–314 (2001), https://doi.org/10.1023/A:1011254632723 
12. Manna, Z., Pnueli, A.: Temporal verification of reactive systems - safety. Springer (1995)
23 
13. Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.A., Veness, J., Bellemare, M.G., Graves, A., Riedmiller, M., Fidjeland, A.K., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., Antonoglou, I., King, H., Kumaran, D., Wierstra, D., Legg, S., Hassabis, D.: Human-level control through deep reinforcement learning. Nature 518(7540), 529–533 (02 2015) 
14. Moldovan, T.M., Abbeel, P.: Safe exploration in markov decision processes. arXiv preprint arXiv:1205.4810 (2012) 
15. Pecka, M., Svoboda, T.: Safe Exploration Techniques for Reinforcement Learning – An Overview, pp. 357–375. Springer International Publishing, Cham (2014) 
16. Pnueli, A.: The temporal logic of programs. In: 18th Annual Symposium on Foundations of Computer Science, Providence, Rhode Island, USA, 31 October - 1 November 1977. pp. 46–57 (1977), https://doi.org/10.1109/SFCS.1977.32 
17. Sohail, S., Somenzi, F.: Safety first: a two-stage algorithm for the synthesis of reactive systems. STTT 15(5-6), 433–454 (2013), https://doi.org/10.1007/ s10009-012-0224-3 
18. Sutton, R.S., Barto, A.G.: Reinforcement learning: An introduction. IEEE Trans. Neural Networks 9(5), 1054–1054 (1998) 
19. Thomaz, A.L., Breazeal, C.: Reinforcement learning with human teachers: Evidence of feedback and guidance with implications for learning performance. In: Proceedings of the 21st National Conference on Artificial Intelligence - Vol. 1. pp. 1000–1005. AAAI Press (2006) 
20. Thomaz, A.L., Breazeal, C.: Teachable robots: Understanding human teaching behavior to build more effective robot learners. Artif. Intell. 172(6-7), 716–737 (2008) 
21. Valiant, L.G.: A theory of the learnable. Commun. ACM 27(11), 1134–1142 (1984) 22. Vidal, P.Q., Rodrı́guez, R.I., González, M.R., Regueiro, C.V.: Learning on real robots from 
experience and simple user feedback. Journal of Physical Agents 7(1) (2013) 23. Wen, M., Ehlers, R., Topcu, U.: Correct-by-synthesis reinforcement learning with temporal 
logic constraints. In: IROS 2015, Germany, Sep. 28 - Oct. 2, 2015. pp. 4983–4990 (2015) 24. Wongpiromsarn, T., Topcu, U., Murray, R.M.: Receding horizon temporal logic planning. 
IEEE Trans. Automat. Contr. 57(11), 2817–2830 (2012)