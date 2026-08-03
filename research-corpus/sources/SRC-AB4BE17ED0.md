> Source: https://www.bartdeschutter.org/publications/06-041-reinforcement-learning-multi-agent/06-041-reinforcement-learning-multi-agent.pdf

Delft University of Technology Delft Center for Systems and Control 
Technical report 06-041 
Reinforcement Learning for Multi-Agent Systems∗ 
R. Babuška, L. Buşoniu, and B. De Schutter 
July 2006 
Paper for a keynote presentation at the 11th IEEE International Conference on Emerging Technologies and Factory Automation (ETFA 2006), Prague, 
Czech Republic, Sept. 2006. 
Delft Center for Systems and Control Delft University of Technology Mekelweg 2, 2628 CD Delft The Netherlands phone: +31-15-278.24.73 (secretary) URL: https://www.dcsc.tudelft.nl 
∗ This report can also be downloaded via https://dspub.eu/06-041
Reinforcement Learning for Multi-Agent Systems 
Robert Babuška Lucian Buşoniu Bart De Schutter 
Delft Center for Systems and Control, Delft University of Technology 
Mekelweg 2, 2628 CD Delft, The Netherlands 
r.babuska@tudelft.nl, i.l.busoniu@tudelft.nl, b.deschutter@tudelft.nl 
Abstract 
Multi-agent systems are rapidly finding applications in 
a variety of domains, including robotics, distributed con-
trol, telecommunications, etc. Although the individual 
agents can be programmed in advance, many tasks require 
that they learn behaviors online. A significant part of the 
research on multi-agent learning concerns reinforcement 
learning techniques. This paper gives a survey of multi-
agent reinforcement learning, starting with a review of the 
different viewpoints on the learning goal, which is a cen-
tral issue in the field. Two generic goals are distinguished: 
stability of the learning dynamics, and adaptation to the 
other agents’ dynamic behavior. The focus on one of these 
goals, or a combination of both, leads to a categoriza-
tion of the methods and approaches in the field. The chal-
lenges and benefits of multi-agent reinforcement learning 
are outlined along with open issues and future research 
directions. 
1 Introduction 
Multi-agent systems are rapidly finding applications in 
a wide variety of domains such as data mining, distributed 
control, collaborative decision support systems, robotic 
teams, etc. Although the individual agents can be pro-
grammed to exhibit some basic behaviors, many tasks re-
quire that agents learn new behaviors online, such that the 
performance of the agent or of the whole multi-agent sys-
tem gradually improves. 
Reinforcement learning (RL) agents learn by interact-
ing with their environment, using only scalar rewards as 
feedback [1]. The simplicity and generality of this setting 
make it attractive also for multi-agent systems. However, 
the main challenge in multiagent RL (MARL) is that each 
learning agent must explicitly consider the other learning 
(and therefore, nonstationary) agents, and coordinate its 
behavior with theirs, such that a coherent joint behavior 
results. 
Over the last years, many algorithms addressing this 
problem were proposed, fusing developments in the areas 
of temporal-difference RL , game theory and more general 
direct policy search techniques. MARL surveys typically 
review the field from a game-theoretic perspective [2–5]. 
The aim of our survey is to take a broader perspective and 
give an overall view of the field. We also address the dif-
ferent viewpoints on the learning goal in MARL , which 
led to certain diversity in the set of MARL algorithms and 
techniques. Finally, we identify open issues and further 
research directions, and outline control-theoretic ways to 
follow some of these directions. 
This paper is organized as follows. Section 2 intro-
duces the necessary background. Section 3 addresses the 
problem of a suitable multi-agent learning goal, and Sec-
tion 4 reviews a representative selection of the literature 
on MARL , classifying algorithms by the type of task they 
solve. Section 5 concludes the paper. 
2 Background 
In single-agent RL, the environment (process) is de-
scribed by a Markov decision process [1]. A definition 
of an MDP is given first, followed by its extension to the 
multi-agent case – the stochastic game. 
2.1 The single-agent case 
Definition 1 A Markov decision process (MDP) is a tuple 
〈X,U, f, ρ〉 where: X is the discrete set of environment 
states, U is the discrete set of agent actions, f : X ×U × X → [0, 1] is the state transition probability distribution, 
and ρ : X × U ×X → R is the reward function. 
As a result of action uk, the environment changes 
state from xk to a next state xk+1 with probability 
f(xk, uk, xk+1). The agent receives (possibly delayed) 
feedback on its performance via the scalar reward signal 
rk+1 ∈ R, rk+1 = ρ(xk, uk, xk+1). For deterministic 
models, the state transition distribution is replaced by a 
function f : X × U → X . This means the reward only 
depends on the current state and action, ρ : X × U → R. 
The agent chooses actions according to its policy that may 
be either stochastic, h : X ×U → [0, 1], or deterministic, 
h : X → U . A policy is called stationary if it does not 
change over time. 
The agent’s goal is to maximize, at each time step k, 
the discounted return: 
Rk = ∑∞ 
j=0 γjrk+j+1, (1) 
where γ ∈ (0, 1) is the discount factor. The action-
value function (Q-function), Qh i : X × U → R, is
the expected return of a state-action pair under a given 
policy: Qh i (x, u) = E {Rk |xk = x, uk = u, h}. The 
agent can maximize its return by first computing the op-
timal Q-function, defined as Q∗(x, u) = maxh Q h(x, u), 
and then choosing actions by the greedy policy h∗(x) = argmaxu Q 
∗(x, u), which is optimal. 
The Q-learning algorithm iteratively approximates Q∗ 
by interaction with the environment, using observed re-
wards rk+1 and pairs of subsequent states xk, xk+1 [6]: 
Qk+1(xk, uk) = Qk(xk, uk)+ 
α [ 
rk+1 + γmax u′ 
Qk(xk+1, u ′)−Qk(xk, uk) 
] 
, (2) 
where α ∈ (0, 1] is the learning rate. In [6] it is proved 
that the sequence Qk converges to Q∗ under certain con-
ditions, including that the agent keeps trying all actions 
in all states with nonzero probability. This means that the 
agent must sometimes explore, i.e., perform other actions 
than dictated by the current greedy policy. 
Example 1 Path optimization through Q-learning. Con-
sider the following simple instance of a path-optimization 
problem. A single agent has to find by trial and error a 
shortest path from its starting position to some fixed goal 
(Figure 1). The agent receives a reward of −0.1 at each in-
termediate time step, and 10 upon reaching the goal. Then 
the trial terminates and the agent is reset to its initial posi-
tion. The negative reward encodes ‘energy consumption’, 
and leads to the minimum-distance solution. 
+ 
0 2 4 6 8 10 12 14 0 
20 
40 
60 
80 
100 
120 
140 
160 
Learning trial 
S te 
p s 
to  c 
o m 
p le 
te  t 
ri al 
Figure 1. Left: a single-agent pathoptimization problem: a robotic agent (cir-
cle) has to find the shortest path to the goal (cross), while avoiding obstacles (gray areas). Right: a typical convergence plot. 
The state x is the agent’s position, discretized on a 5×5 grid. The available actions u are the moves one cell further 
in one of the four compass directions, or standing still. 
The minimum-time path is learned with Q-learning, 
using γ = 0.98 and a constant learning rate α = 0.2. 
The agent explores by choosing at each step, with expo-
nentially decaying probability, a random action instead of 
the greedy one. An eligibility trace with a decay factor 
λ = 0.5 is used to speed up the convergence [1]. Q-
learning converges to an optimal policy in 7 trials. Note 
that convergence is not monotonous, mainly due to explo-
ration: e.g., trial 6 takes longer than trial 5.  
2.2 The multi-agent case 
The underlying model in the multi-agent case is the 
stochastic game [7]. 
Definition 2 A stochastic game (SG) is a tuple 
〈A,X, {Ui}i∈A , f, {ρi}i∈A〉 where: A = {1, . . . , n} is 
the set of n agents, X is the discrete set of environment 
states, {Ui}i∈A are the discrete sets of actions available 
to the agents, yielding the joint action set U = ×i∈AUi, 
f : X×U ×X → [0, 1] is the state transition probability 
distribution, and ρi : X × U × X → R, i ∈ A are the 
reward probability functions of the agents. 
Note that the state transitions, agent rewards ri,k+1, and 
thus also the agent returns Ri,k, depend on the joint action 
uk = [u1,k, . . . , un,k] T,uk ∈ U , ui,k ∈ Ui. The policies 
hi : X×Ui → [0, 1] form together the joint policy h. The 
Q-function of each agent depends on the joint action and 
is conditioned on the joint policy, Qh 
i : X ×U → R. 
If X = ∅, the SG reduces to a matrix game. A ma-
trix game, when played repeatedly by the same agents, is 
called a repeated game. If ρ1 ≡ · · · ≡ ρn, the SG is fully 
cooperative. If n = 2 and ρ1 ≡ −ρ2, the SG is fully 
competitive. 
In a matrix game, the policy loses the state argument 
and transforms into a strategy h : U → [0, 1]. Similarly, 
a policy conditioned on a given state x yields a strategy. 
The best response of agent i to a set of opponent strategies 
is a strategy that achieves the maximum expected reward 
given the opponents’ strategies. A Nash equilibrium is a 
set of strategies such that each is a best-response to the 
others. 
3 Multi-agent learning goal 
In fully cooperative SG s, the common return can be 
jointly maximized. In other cases, however, specifying a 
good MARL goal is difficult, because the agents’ returns 
are correlated and cannot be maximized independently. 
In this section, we review the learning goals put for-
ward in the literature. These goals incorporate stability of 
the learning process on the one hand, and adaptation to the 
dynamic behavior of the other agents on the other hand. 
Stability essentially means the convergence to stationary 
policies, whereas adaptation ensures that performance is 
maintained or improved. 
Convergence to equilibria is a basic stability require-
ment, postulated already in the early MARL literature 
[8, 9]. Nash equilibria are most frequently used. How-
ever, concerns have been voiced regarding their useful-
ness [2], because of the unclear link to performance in 
dynamic tasks and their inherent conservatism. 
Bowling and Veloso [7] add rationality as an adapta-
tion criterion. Rationality means that the agent’s policy
converges to a best response when other agents remain 
stationary. An alternative to rationality is the concept no-
regret, which prevents the learner from ‘being exploited’ 
by the other agents [10]. 
Targeted optimality / compatibility / safety [11] replace 
convergence with adaptation requirements, in the form 
of average reward bounds for three classes of oppo-
nents: those deemed interesting (targeted), those using the 
learner’s algorithm, and remaining opponents. 
Table 1 summarizes the desirable properties of MARL 
algorithms, as discussed above and in the literature. The 
focus on stability, adaptation, or a mix of the two, leads 
to a categorization of MARL algorithms into opponent-
independent, opponent-tracking, and opponent-aware, as 
discussed in the next section. 
Table 1. Stability and adaptation in multiagent learning. 
Stability property Adaptation property Ref. 
convergence rationality [7, 12] 
convergence no-regret [10] 
opponent-independent opponent-aware [5, 13] 
prediction rationality [4] 
— 
{ 
targeted optimality 
compatibility, safety [2, 11] 
4 Multi-agent reinforcement learning 
algorithms 
The MARL algorithms are organized here by the type 
of task they address: fully cooperative, fully competitive, 
and mixed tasks. 
4.1 Fully cooperative tasks 
In a fully cooperative SG , the reward functions are 
identical: ρ1 ≡ . . . ≡ ρn and the learning goal is to 
maximize the common discounted return. If the agents 
are considered together as a centralized controller, the 
task reduces to a Markov decision process whose action 
space is the joint action space of the SG . The goal can be 
achieved by learning the optimal joint-action values with 
Q-learning: 
Qk+1(xk,uk) = Qk(xk,uk)+ 
α [ 
rk+1 + γmax u′ 
Qk(xk+1,u ′)−Qk(xk,uk) 
] 
, (3) 
and using the greedy policy. However, if the agents are in-
dependent decision makers, a coordination problem arises 
even if all the agents use the same learning algorithm. The 
greedy action selection mechanism breaks ties randomly, 
which means that in the absence of additional mecha-
nisms, different agents may break a tie in different ways. 
The resulting joint action may be suboptimal. 
Example 2 Coordination in action selection. Consider 
the situation illustrated in Figure 2: two mobile agents 
need to avoid an obstacle while maintaining formation. 
obstacle 
S2 
R2 
2 L2R1 
S1 
L1 
1 
Q L2 S2 R2 
L1 10 -5 0 
S1 -5 -10 -5 
R1 -10 -5 10 
Figure 2. Two mobile agents approaching an obstacle need to coordinate their action selection mechanism. 
For the given state (positions of the agents), the Q-
function can be projected into the space of the joint agent 
actions. An example of such a table is given in the right 
part of Figure 2. The rows correspond to actions of 
agent 1, the columns to actions of agent 2. If both agents 
go left, or both go right, the obstacle is avoided while 
maintaining the formation: Q(L1, L2) = Q(R1, R2) = 10. If agent 1 goes left, and agent 2 goes right, the for-
mation is broken: Q(L1, R2) = 0. In all other cases, 
collisions occur and the Q-values are negative. 
Note the tie between the two optimal joint actions: 
(L1, L2) and (R1, R2). Without a coordination mecha-
nism, agent 1 might assume that agent 2 will take action 
R2, and therefore it takes action R1. Similarly, agent 2 
might assume that agent 1 will take L1, and consequently 
takes L2. The resulting joint action (R1, L2) is largely 
suboptimal, as the agents collide.  
The following approaches to solving the coordination 
issue can be distinguished in the literature: coordination-
free methods, direct and indirect coordination methods. 
4.1.1 Coordination-free methods 
The Team Q-learning algorithm [13] assumes that the op-
timal joint actions are unique (which will rarely be the 
case) and use (3) directly. 
The Distributed Q-learning algorithm [14] solves the 
cooperative task without assuming coordination, however 
it is only valid in the deterministic setting (with α = 1). 
Each agent i maintains an explicit policy hi(x), and a lo-
cal Q-function Qi(x, ui), depending only on its own ac-
tion. Both are updated only in the direction that increases 
Qi: 
Qi,k+1(xk, ui,k) =max { 
Qi,k(xk, ui,k), 
rk+1 + γmax ui 
Qi,k(xk+1, ui) } (4) 
hi,k+1(xk) = 
 
 
 
 
 
ui,k if maxui Qi,k+1(xk, ui) 
6= maxui Qi,k(xk, ui) 
hi,k(xk) otherwise (5)
Under the conditions that Qi,0 ≡ 0 and the common re-
ward function is positive, the policies of the agents prov-
ably converge to the optimal joint policy h ∗. 
4.1.2 Direct coordination methods 
A more general approach to solving the coordination 
problem is to make sure that ties are broken by all agents 
in the same way. This clearly requires that the action 
choices are somehow coordinated or negotiated: 
– Social conventions [15] and roles [16] restrict the 
action choices of the agents. 
– Coordination graphs explicitly represent where 
coordination between agents is required, thus pre-
venting the agents from engaging in unnecessary 
coordination activities [17]. 
– Communication is used to negotiate action choices, 
either alone or in combination with the above tech-
niques, see, e.g., [18, 19]. 
4.1.3 Indirect coordination methods 
In this class of approaches, action selection is biased to-
ward actions that promise to yield better values, and thus 
steer the agents toward coordination. Joint Action Learn-
ers (JAL) [20] employ empirically learned models of the 
other agents’ behavior. The Frequency Maximum Q-value 
(FMQ) heuristic [21] is based on the frequency with which 
actions yielded good values in the past. In Optimal Adap-
tive Learning (OAL), the bias is towards recently chosen 
optimal joint actions [22]. Using an additional mecha-
nism to guarantee that these actions are eventually se-
lected, OAL provably converges to optimal joint policies 
(at the cost of increased complexity). 
Example 3 Multi-agent coordination. In this multi-agent 
coordination problem, two agents live in a grid world sim-
ilar to that of Example 1. However, here they have to reach 
the goal cell simultaneously. This is represented by a re-
ward of 10 upon simultaneously reaching the goal. 
Coordination is needed around the goal (the agents 
need to move to it simultaneously), and near the passage 
in the middle of the grid-world (a collision would occur 
there if both agents took their own time-optimal paths, so 
one of them has to wait for the other one to pass first). 
The algorithm used is team Q-learning with the ad-
dition of a simple social convention: an ordering of the 
joint actions which is known to both agents. The dis-
count factor is γ = 0.98 and the learning rate at step 
k is αk = 1 1+k/500 . The agents explore by choosing 
at each step, with exponentially decaying probabilities, a 
random action instead of the greedy one. The agents con-
verge to an optimal joint policy in 23 trials. Compared 
to the single-agent case in Figure 1, the agents initially 
take much longer to discover the goal (approximately 950 
steps vs. 160 steps), and the convergence is much slower 
21 
+ 
0 5 10 15 20 25 30 0 
100 
200 
300 
400 
500 
600 
700 
800 
900 
1000 
Learning trial 
S te 
p s 
to  c 
o m 
p le 
te  t 
ri al 
Figure 3. Left: a multi-agent coordination problem: two robotic agent (circles) have to reach the goal (cross) simultaneously, while 
avoiding obstacles (gray areas) and minimizing the distance traveled. Right: a typical convergence plot. 
(21 trials vs. 7 trials). This is because of the relatively 
large state-action space: (5 · 5)2 states times 52 joint ac-
tions = 15265 state-action pairs, as opposed to 125 in the 
single-agent case.  
4.2 Fully competitive tasks 
In a fully competitive SG (for two agents, ρ1 ≡ −ρ2), 
the minimax principle can be applied: maximize one’s 
benefit under the assumption that the opponent will al-
ways act so as to minimize it. The resulting algorithm 
is minimax-Q [13], given here for agent 1: 
h1,k(xk, ·) = argm1(Qk, xk) (6) 
Qk+1(xk, u1,k, u2,k) = Qk(xk, u1,k, u2,k)+ 
α [ 
rk+1 + γm1(Qk, xk+1)−Qk(xk, u1,k, u2,k) ] (7) 
where m1 is the minimax return of agent 1: 
m1(Q, x) = max h̃1(x,·) 
min u2 
∑ 
u1 
h̃1(x, u1)Q(x, u1, u2) (8) 
The Q-table is not subscripted by the agent index, 
because the equations use the implicit assumption that 
Q2 = −Q1 = −Q. The coordination problem does not 
arise here, because even if the minimax optimization has 
multiple solutions, any of them will achieve at least the 
minimax return regardless of what the opponent is doing. 
Thus, minimax-Q is truly opponent-independent. How-
ever, if the learner has a model of the opponent’s policy 
(i.e., is opponent-aware), it might actually do better than 
the minimax return (8). 
4.3 Mixed tasks 
In the general case, the reward functions of the agents 
may differ. This is certainly true for self-interested agents, 
but even cooperating agents may encounter situations 
where their immediate interests are in conflict, e.g., when 
they need to compete for some resource. Mixed, dynamic
tasks, represented by the unrestricted SG , exhibit all the 
MARL challenges: delayed reward, nonstationary oppo-
nents, and conflicting goals. 
Single-agent RL can be directly applied to the multi-
agent case [23]. However, the nonstationarity of the 
MARL problem invalidates most of the single-agent RL 
theoretical results. Therefore, single-agent RL will only 
work when agents do not severely interfere with one an-
other. Despite its limitations, this approach found applica-
tions, mainly because of its simplicity [24,25]. In applica-
tions, information about other agents is typically encoded 
in the learner’s input, thus indirectly enabling it to make 
decisions on the basis of their behavior. 
Game-theoretic concepts of equilibria can be used to 
facilitate convergence. Algorithms in this category typi-
cally require that the agents know the task model (i.e., the 
reward function), and assume observable actions (some of 
them, even observable strategies). 
In the sequel, we distinguish opponent-independent 
methods (targeting convergence), opponent-tracking 
methods (targeting rationality, i.e., the adaptation to 
opponents’ strategies) and opponent-aware methods 
(targeting both convergence and rationality). 
4.3.1 Opponent-independent methods 
These methods are based on Q-learning, where policies 
and state values are computed with game-theoretic solvers 
for the matrix games arising in the states of the SG [5, 9]. 
Denoting by {Q·,k(xk, ·)} the matrix game arising at time 
k and given by all the agents’ Q-values for state xk: 
hi,k(x, ·) = solvei {Q·,k(xk, ·)} (9) 
Qi,k+1(xk,uk) = Qi,k(xk,uk) + α [ 
ri,k+1+ 
γ · evali {Q·,k(xk, ·)} −Qi,k(xk,uk) ] (10) 
solvei returns the i’th agent’s part of some type of equi-
librium (a strategy), and evali gives the agent’s expected 
return at this equilibrium. When multiple equilibria exist 
in a particular state of an SG , the equilibrium selection 
problem arises: the agents need to consistently pick their 
part of the same equilibrium (this problem is similar to the 
one discussed in Section 4.1). 
The learning goal is the convergence to a set of policies 
that contain the equilibrium strategies in every state. The 
updates use the Q-tables of all the agents. So, each agent 
needs to model the Q-tables of the other agents. It can do 
that by applying (10). This requires two assumptions: that 
all agents use the same algorithm, and that all actions and 
rewards are observable. 
Particular instances of solve and eval for Nash Q-
learning [8] are: 
evali {Q·,k(xk, ·)} = Vi(xk,NE {Q·,k(xk, ·)}) (11) 
solvei {Q·,k(xk, ·)} = NEi {Q·,k(xk, ·)} (12) 
where NE computes a Nash equilibrium, NEi is 
agent i’s strategy component of this equilibrium, and 
Vi(xk,NE {Q·,k(xk, ·)}) is the expected return of agent 
i from xk under this equilibrium. Correlated Q-
learning (CE-Q) [9] and asymmetric Q-learning [26] 
work in a similar fashion, by using correlated or Stack-
elberg (leader-follower) equilibria, respectively. For 
asymmetric-Q, the follower does not need to model the 
leader’s Q-table; however, the leader must know how the 
follower chooses its actions. 
Equilibria can also be combined with the Value And 
Policy Search (VAPS) gradient method [27], leading to 
multi-agent VAPS [28]. 
4.3.2 Opponent-tracking methods 
These algorithms adapt to learned models of nonstation-
ary opponent policies without explicitly considering con-
vergence. Actions of other agents have to be observable. 
The Non-Stationary Converging Policies (NSCP) algo-
rithm computes a best-response to the models and uses 
it in estimating value functions [29], whereas Hyper-Q in-
corporates the models in the state vector, and learns on 
their basis [30]. 
4.3.3 Opponent-aware methods 
These methods typically do consider convergence as well 
as adaptation to other agents. Win-or-Learn-Fast Pol-
icy Hill-Climbing (WoLF-PHC) combines the basic Q-
learning update rule (2) with a gradient-based policy up-
date: 
hi,k+1(xk, ui) = hi,k(xk, ui)+  
 
 
δi,k if ui = argmax ũi 
Qi,k+1(xk, ũi) 
− δi,k 
|Ui|−1 otherwise (13) 
The gradient step δi,k is larger when the agent is losing 
than when it is winning. The win criterion is based either 
on a comparison of an average policy with the current one, 
in the original version of WoLF-PHC, or on the second-
order difference of policy elements, in PD-WoLF [31]. 
The rationale is that the agent should escape fast from los-
ing situations, while adapting cautiously when it is win-
ning, in order to encourage convergence. 
The Extended Optimal Response (EXORL) heuristic 
applies a similar idea in two-agent tasks: the policy up-
date is biased in a way that minimizes the other agent’s 
incentive to deviate from its current policy [32]. 
Environment-Independent Reinforcement Acceleration 
(EIRA) pushes policies onto, and pops policies from, a 
policy stack in such a way that long-term reinforcement 
improvements are guaranteed [33]. EIRA does not make 
any assumptions on the environment and on the other 
agents. In this sense, it is very general. However, it may 
not be able to take advantage of the task’s structure.
Remarks 
Much research in this area focuses on repeated games. In 
such a case, one of the essential properties of RL , the 
delayed reward, is lost. However, the learning problem 
is still nonstationary due to the dynamic behavior of the 
agents that play the repeated game. Methods in this cat-
egory can also be classified into opponent-tracking meth-
ods, which aim at adapting to learned models of the oppo-
nents’ behavior [11] and opponent-aware methods, which 
target convergence as well [7, 34]. Note that opponent-
tracking methods do not necessarily converge to station-
ary strategies. 
Static, repeated games represent a limited set of appli-
cations, among which are negotiation, auctions, and bar-
tering. These algorithms provide valuable theoretical re-
sults, which, however, do not necessarily carry over to the 
dynamical SG case. 
5 Conclusions and future perspectives 
We have reviewed the challenges of multi-agent re-
inforcement learning and the methods to address them. 
More general open problems and an outlook are given 
next. 
First, the stage-wise application of game-theoretic 
techniques may not be the most suitable approach, given 
that the environment and the behavior of learning agents 
are generally dynamic processes. So far, game-theory-
based analysis has only been applied to the learning dy-
namics [3, 35]. We expect that tools developed in the area 
of automatic control will play an important role in the ana-
lysis and synthesis of the learning process as a whole (i.e., 
environment and learning dynamics). In addition, this 
framework can incorporate prior knowledge on bounds for 
imperfect observations, such as noise-corrupted variables. 
Second, the issue of a suitable learning goal requires 
additional research. Stability of the learning process is 
desirable, because the behavior of stable agents is more 
amenable to analysis and meaningful performance guar-
antees. Adaptation to the other agents is desirable be-
cause their dynamics are generally unpredictable. There-
fore, a good multi-agent learning goal must include both 
components. This means that MARL algorithms should 
not be purely opponent-independent nor purely opponent-
tracking. The control-theoretic concept of robustness can 
help integrate stability and adaptation into a unified goal. 
If a learning algorithm is robustly stable with respect to 
nonstationarity in the other agents, it will converge while 
allowing for bounded changes in the behavior of these 
agents. 
From a practical viewpoint, a realistic learning goal 
should include bounds on the transient performance, in 
addition to the usual asymptotic requirements. Exam-
ple of such bounds include maximum time constraints for 
reaching a desired performance level, or a lower bound 
on instantaneous performance levels. The authors of [10] 
and [11] already made first steps in this direction. 
Third, scalability is an important concern for MARL . 
Most algorithms require explicit tabular representations of 
the Q-function and possibly of the policy. Due to this, the 
computational requirements of the algorithms scale expo-
nentially with the number of state and action variables, 
and therefore with the number of agents. This also has 
negative consequences for the learning time and conver-
gence speed. Consider, for instance, extending the grid 
world of Example 3) to 10 × 10 cells and the number of 
agents from two to three. The size of the Q-table that each 
agent needs to store then becomes (10 · 10)3 · 53 = 125 million entries. A similar problem arises when state or ac-
tion variables are continuous. In this case, tabular storage 
of Q-values is impossible. 
In our view, significant progress in the field of multi-
agent learning can be achieved by a more intensive cross-
fertilization between the fields of machine learning, game 
theory and control theory. 
Acknowledgement This research is financially supported by Senter, Min-
istry of Economic Affairs of the Netherlands, within the 
BSIK project “Interactive Collaborative Information Sys-
tems” (grant no. BSIK03024). 
References 
[1] R. S. Sutton and A. G. Barto, Reinforcement Learning: 
An Introduction, MIT Press, Cambridge, US, 1998. 
[2] Y. Shoham, R. Powers, and T. Grenager, “Multi-Agent 
Reinforcement Learning: A Critical Survey”, Technical 
report, Computer Science Dept., Stanford University, Cal-
ifornia, US, 16 May 2003. 
[3] K. Tuyls and A. Nowé, “Evolutionary Game Theory and 
Multi-Agent Reinforcement Learning”, The Knowledge 
Engineering Review, vol. 20, no. 1, pp. 63–90, 2005. 
[4] G. Chalkiadakis, “Multiagent Reinforcement Learning: 
Stochastic Games with Multiple Learning Players”, Tech-
nical report, Dept. of Computer Science, University of 
Toronto, Canada, 25 March 2003. 
[5] M. Bowling, Multiagent Learning in the Presence of 
Agents with Limitations, PhD thesis, Computer Science 
Dept., Carnegie Mellon University, Pittsburgh, US, May 
2003. 
[6] C. J. C. H. Watkins and P. Dayan, “Technical Note: Q-
Learning”, Machine Learning, vol. 8, pp. 279–292, 1992. 
[7] M. Bowling and M. Veloso, “Multiagent Learning Using a 
Variable Learning Rate”, Artificial Intelligence, vol. 136, 
no. 2, pp. 215–250, 2002. 
[8] J. Hu and M. P. Wellman, “Nash Q-Learning for General-
Sum Stochastic Games”, Journal of Machine Learning Re-
search, vol. 4, pp. 1039–1069, 2003. 
[9] A. Greenwald and K. Hall, “Correlated-Q Learning”, 
in Proc. Twentieth International Conference on Machine 
Learning (ICML-03), 21–24 August 2003, pp. 242–249, 
Washington, US. 
[10] M. Bowling, “Convergence and No-Regret in Multiagent 
Learning”, in Advances in Neural Information Processing
Systems 17 (NIPS-04), 13–18 December 2004, pp. 209– 
216, Vancouver, Canada. 
[11] R. Powers and Y. Shoham, “New Criteria and a New Algo-
rithm for Learning in Multi-Agent Systems”, in Advances 
in Neural Information Processing Systems 17 (NIPS-04), 
2004, pp. 1089–1096, Vancouver, Canada. 
[12] V. Conitzer and T. Sandholm, “AWESOME: A General 
Multiagent Learning Algorithm that Converges in Self-
Play and Learns a Best Response Against Stationary Op-
ponents”, in Proc. Twentieth International Conference on 
Machine Learning (ICML-03), 21–24 August 2003, pp. 
83–90, Washington, US. 
[13] M. L. Littman, “Value-function Reinforcement Learning 
in Markov Games”, Journal of Cognitive Systems Re-
search, vol. 2, pp. 55–66, 2001. 
[14] M. Lauer and M. Riedmiller, “An Algorithm for Distribu-
ted Reinforcement Learning in Cooperative Multi-Agent 
Systems”, in Proc. Seventeenth International Conference 
on Machine Learning (ICML-00), 29 June – 2 July 2000, 
pp. 535–542, Stanford University, US. 
[15] C. Boutilier, “Planning, Learning and Coordination in 
Multiagent Decision Processes”, in Proc. Sixth Confer-
ence on Theoretical Aspects of Rationality and Knowl-
edge (TARK-96), 17–20 March 1996, pp. 195–210, De 
Zeeuwse Stromen, The Netherlands. 
[16] M. T. J. Spaan, N. Vlassis, and F. C. A. Groen, “High level 
coordination of agents based on multiagent Markov deci-
sion processes with roles”, in Workshop on Cooperative 
Robotics, 2002 IEEE/RSJ International Conference on In-
telligent Robots and Systems (IROS-02), 1 October 2002, 
pp. 66–73, Lausanne, Switzerland. 
[17] C. Guestrin, M. G. Lagoudakis, and R. Parr, “Coordinated 
Reinforcement Learning”, in Proc. Nineteenth Interna-
tional Conference on Machine Learning (ICML-02), 8–12 
July 2002, pp. 227–234, Sydney, Australia. 
[18] N. Vlassis, “A Concise Introduction to Multiagent Sys-
tems and Distributed AI”, Technical report, University 
of Amsterdam, The Netherlands, September 2003, URL: 
http://www.science.uva.nl/ vlassis/cimasdai/cimasdai.pdf. 
[19] F. Fischer, M. Rovatsos, and G. Weiss, “Hierarchical Re-
inforcement Learning in Communication-Mediated Multi-
agent Coordination”, in Proc. 3rd International Joint Con-
ference on Autonomous Agents and Multiagent Systems 
(AAMAS-04), 19–23 August 2004, pp. 1334–1335, New 
York, US. 
[20] C. Claus and C. Boutilier, “The Dynamics of Reinforce-
ment Learning in Cooperative Multiagent Systems”, in 
Proc. 15th National Conference on Artificial Intelligence 
and 10th Conference on Innovative Applications of Arti-
ficial Intelligence (AAAI/IAAI-98), 26–30 July 1998, pp. 
746–752, Madison, US. 
[21] S. Kapetanakis and D. Kudenko, “Reinforcement Learn-
ing of Coordination in Cooperative Multi-Agent Systems”, 
in Proc. 18th National Conference on Artificial Intelli-
gence and 14th Conference on Innovative Applications of 
Artificial Intelligence (AAAI/IAAI-02), 28 July – 1 Au-
gust 2002, pp. 326–331, Menlo Park, US. 
[22] X. Wang and T. Sandholm, “Reinforcement Learning 
to Play an Optimal Nash Equilibrium in Team Markov 
Games”, in Advances in Neural Information Processing 
Systems 15 (NIPS-02), 9–14 December 2002, pp. 1571– 
1578, Vancouver, Canada. 
[23] S. Sen, M. Sekaran, and J. Hale, “Learning to Coordinate 
without Sharing Information”, in Proc. 12th National Con-
ference on Artificial Intelligence (AAAI-94), 31 July – 4 
August 1994, pp. 426–431, Seattle, US. 
[24] M. J. Matarić, “Learning in Multi-Robot Systems”, in 
G. Weiß and S. Sen, editors, Adaptation and Learning 
in Multi–Agent Systems, pp. 152–163. Springer Verlag, 
1996. 
[25] R. H. Crites and A. G. Barto, “Improving Elevator Perfor-
mance Using Reinforcement Learning”, in Advances in 
Neural Information Processing Systems, volume 8, 1996, 
pp. 1017–1023. 
[26] V. Könönen, “Asymmetric Multiagent Reinforcement 
Learning”, in Proc. IEEE/WIC International Conference 
on Intelligent Agent Technology (IAT-03), 13–17 October 
2003, pp. 336–342, Halifax, Canada. 
[27] L. Baird and A. Moore, “Gradient Descent for General 
Reinforcement Learning”, in Advances in Neural Infor-
mation Processing Systems 11 (NIPS-98), 30 November – 
5 December 1998, pp. 968–974, Denver, US. 
[28] V. Könönen, “Gradient Based Method for Symmetric 
and Asymmetric Multiagent Reinforcement Learning”, in 
Proc. 4th International Conference on Intelligent Data En-
gineering and Automated Learning (IDEAL-03), 21–23 
March 2003, pp. 68–75, Hong Kong, China. 
[29] M. Weinberg and J. S. Rosenschein, “Best-Response Mul-
tiagent Learning in Non-Stationary Environments”, in 
Proc. 3rd International Joint Conference on Autonomous 
Agents and Multiagent Systems (AAMAS-04), 19-23 Au-
gust 2004, pp. 506–513, New York, US. 
[30] G. Tesauro, “Extending Q-Learning to General Adaptive 
Multi-Agent Systems”, in Advances in Neural Information 
Processing Systems 16 (NIPS-03), 8–13 December 2003, 
Vancouver and Whistler, Canada. 
[31] B. Banerjee and J. Peng, “Adaptive Policy Gradient in 
Multiagent Learning”, in Proc. 2nd International Joint 
Conference on Autonomous Agents and Multiagent Sys-
tems (AAMAS-03), 14–18 July 2003, pp. 686–692, Mel-
bourne, Australia. 
[32] N. Suematsu and A. Hayashi, “A multiagent reinforcement 
learning algorithm using extended optimal response”, in 
Proc. 1st International Joint Conference on Autonomous 
Agents and Multiagent Systems (AAMAS-02), 15–19 July 
2002, pp. 370–377, Bologna, Italy. 
[33] J. Schmidhuber, “A General Method for Multi-Agent Re-
inforcement Learning in Unrestricted Environments”, in 
Working Notes AAAI Symposium on Adaptation, Co-
evolution and Learning in Multiagent Systems, 25–27 
March 1996, pp. 84–87, Stanford University, US. 
[34] S. Singh, M. Kearns, and Y. Mansour, “Nash Convergence 
of Gradient Dynamics in General-Sum Games”, in Proc. 
16th Conference on Uncertainty in Artificial Intelligence 
(UAI-00), 30 June – 3 July 2000, pp. 541–548, San Fran-
cisco, US. 
[35] J. M. Vidal, “Learning in Multiagent Systems: An Intro-
duction from a Game-Theoretic Perspective”, in Adaptive 
Agents: Lecture Notes in Artificial Intelligence, volume 
2636, pp. 202–215. Springer Verlag, August 2003.