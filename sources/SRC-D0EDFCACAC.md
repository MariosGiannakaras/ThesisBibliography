> Source: https://en.wikipedia.org/wiki/Markov_decision_process

Markov decision process - Wikipedia
Jump to content [-]
Main menu
Main menu
move to sidebar hide
Navigation
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
WikipediaThe Free Encyclopedia
Search
Search [-]
Appearance
Donate
Create account
Log in [-]
Personal tools
Donate
Create account
Log in
Contents
move to sidebar hide
(Top)
1 Definition Toggle Definition subsection
1.1 Optimization objective
1.2 Simulator models
2 Example
3 Algorithms Toggle Algorithms subsection
3.1 Notable variants
3.1.1 Value iteration
3.1.2 Policy iteration
3.1.3 Modified policy iteration
3.1.4 Prioritized sweeping
3.2 Computational complexity
4 Extensions and generalizations Toggle Extensions and generalizations subsection
4.1 Partial observability
4.2 Constrained Markov decision processes
4.3 Continuous-time Markov decision process
4.3.1 Discrete space: Linear programming formulation
4.3.2 Continuous space: Hamilton–Jacobi–Bellman equation
5 Reinforcement learning Toggle Reinforcement learning subsection
5.1 Reinforcement Learning for discrete MDPs
6 Other scopes Toggle Other scopes subsection
6.1 Learning automata
6.2 Category theoretic interpretation
7 Alternative notations
8 See also
9 References
10 Sources
11 Further reading [-]
Toggle the table of contents
Markov decision process
[-]
23 languages
العربية
Català
Čeština
Deutsch
Español
Euskara
فارسی
Français
עברית
Íslenska
Italiano
日本語
한국어
ဘာသာမန်
Português
Русский
Simple English
Српски / srpski
Türkçe
Українська
Tiếng Việt
粵語
中文
Edit links
Article
Talk [-]
English
Read
Edit
View history [-]
Tools
Tools
move to sidebar hide
Actions
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
Switch to legacy parser
Expand all
Edit interlanguage links
Print/export
Download as PDF
Printable version
In other projects
Wikidata item
Appearance
move to sidebar hide
Text
[-] 0 Small [x] 1 Standard [-] 2 Large
This page always uses small font size
Width
[x] 1 Standard [-] 0 Wide
The content is as wide as possible for your browser window.
Color
[-] os Automatic [x] day Light [-] night Dark
This page is always in light mode.
From Wikipedia, the free encyclopedia
Mathematical model for sequential decision making under uncertainty
A Markov decision process ( MDP) is a mathematical model for sequential decision making when outcomes are uncertain. [1] It is a type of stochastic decision process [2], and is often solved using the methods of stochastic dynamic programming.
Originating from operations research in the 1950s, [3] [4] MDPs have since gained recognition in a variety of fields, including ecology, economics, healthcare, telecommunications and reinforcement learning. [5] Reinforcement learning utilizes the MDP framework to model the interaction between a learning agent and its environment. In this framework, the interaction is characterized by states, actions, and rewards. The MDP framework is designed to provide a simplified representation of key elements of artificial intelligence challenges. This modeling framework incorporates the understanding of cause and effect, the management of uncertainty and nondeterminism, and the pursuit of explicit goals. [5]
The name comes from its connection to Markov chains, a concept developed by the Russian mathematician Andrey Markov. The "Markov" in "Markov decision process" refers to the underlying structure of state transitions that still follow the Markov property. The process is called a "decision process" because it involves making decisions that influence these state transitions, extending the concept of a Markov chain into the realm of decision-making under uncertainty.
Definition
[ edit source] 
Example of a simple MDP with three states (green circles) and two actions (orange circles), with two rewards (orange arrows)
A Markov decision process is a 4- tuple ( S , A , P a , R a ) {\displaystyle (S,A,P_{a},R_{a})} 
, where:
S {\displaystyle S} is a set of states called the state space . The state space may be discrete or continuous, like the set of real numbers.
A {\displaystyle A} is a set of actions called the action space (alternatively, A s {\displaystyle A_{s}} is the set of actions available from state s {\displaystyle s} ). As for state, this set may be discrete or continuous.
P a ( s , s ′ ) {\displaystyle P_{a}(s,s')} is the probability that action a {\displaystyle a} in state s {\displaystyle s} at time t {\displaystyle t} will lead to state s ′ {\displaystyle s'} at time t + 1 {\displaystyle t+1} . In general, this probability transition is defined to satisfy Pr ( s t + 1 ∈ S ′ ∣ s t = s , a t = a ) = ∫ S ′ P a ( s , s ′ ) d s ′ , {\displaystyle \Pr(s_{t+1}\in S'\mid s_{t}=s,a_{t}=a)=\int {S'}P{a}(s,s')ds',} for every S ′ ⊆ S {\displaystyle S'\subseteq S} measurable. In case the state space is discrete, the integral is intended with respect to the counting measure, so that the latter simplifies as P a ( s , s ′ ) = Pr ( s t + 1 = s ′ ∣ s t = s , a t = a ) {\displaystyle P_{a}(s,s')=\Pr(s_{t+1}=s'\mid s_{t}=s,a_{t}=a)} ; in case S ⊆ R d {\displaystyle S\subseteq \mathbb {R} ^{d}} , the integral is usually intended with respect to the Lebesgue measure.
R a ( s , s ′ ) {\displaystyle R_{a}(s,s')} is the immediate reward (or expected immediate reward) received after action a {\displaystyle a} is taken to transition from state s {\displaystyle s} to state s ′ {\displaystyle s'} . The reward is in general a random variable.
A policy function π {\displaystyle \pi } 
is a (potentially probabilistic) mapping from state space ( S {\displaystyle S} 
) to action space ( A {\displaystyle A} 
).
Optimization objective
[ edit source]
The goal in a Markov decision process is to find a good "policy" for the decision maker: a function π {\displaystyle \pi } 
that specifies the action π ( s ) {\displaystyle \pi (s)} 
that the decision maker will choose when in state s {\displaystyle s} 
. Once a Markov decision process is combined with a policy in this way, this fixes the action for each state and the resulting combination behaves like a Markov chain (since the action chosen in state s {\displaystyle s} 
is completely determined by π ( s ) {\displaystyle \pi (s)} 
).
The objective is to choose a policy π {\displaystyle \pi } 
that will maximize some cumulative function of the random rewards, typically the expected discounted sum over a potentially infinite horizon:
E [ ∑ t = 0 ∞ γ t R a t ( s t , s t + 1 ) ] {\displaystyle E\left[\sum {t=0}^{\infty }{\gamma ^{t}R{a_{t}}(s_{t},s_{t+1})}\right]} 
(where we choose a t = π ( s t ) {\displaystyle a_{t}=\pi (s_{t})} 
, i.e. actions given by the policy). And the expectation is taken over s t + 1 ∼ P a t ( s t , s t + 1 ) {\displaystyle s_{t+1}\sim P_{a_{t}}(s_{t},s_{t+1})} 
where γ {\displaystyle \ \gamma \ } 
is the discount factor satisfying 0 ≤ γ ≤ 1 {\displaystyle 0\leq \ \gamma \ \leq \ 1} 
, which is usually close to 1 {\displaystyle 1} 
(for example, γ = 1 / ( 1 + r ) {\displaystyle \gamma =1/(1+r)} 
for some discount rate r {\displaystyle r} 
). A lower discount factor makes the decision maker more short-sighted, in that it comparatively disregards the effect that following its current policy has at times lying further in the future.
Another possible, but strictly related, objective that is commonly used is the H − {\displaystyle H-} 
step return. This time, instead of using a discount factor γ {\displaystyle \ \gamma \ } 
, the agent is interested only in the first H {\displaystyle H} 
steps of the process, with each reward having the same weight.
E [ ∑ t = 0 H − 1 R a t ( s t , s t + 1 ) ] {\displaystyle E\left[\sum {t=0}^{H-1}{R{a_{t}}(s_{t},s_{t+1})}\right]} 
(where we choose a t = π ( s t ) {\displaystyle a_{t}=\pi (s_{t})} 
, i.e. actions given by the policy). And the expectation is taken over s t + 1 ∼ P a t ( s t , s t + 1 ) {\displaystyle s_{t+1}\sim P_{a_{t}}(s_{t},s_{t+1})} 
where H {\displaystyle \ H\ } 
is the time horizon. Compared to the previous objective, the latter one is more used in Learning Theory.
A policy that maximizes the function above is called an optimal policy and is usually denoted π ∗ {\displaystyle \pi ^{*}} 
. A particular MDP may have multiple distinct optimal policies. Because of the Markov property, it can be shown that the optimal policy is a function of the current state, as assumed above. When R a ( s , s ′ ) {\displaystyle R_{a}(s,s')} 
is deterministic, there will always exist an optimal policy π ∗ {\displaystyle \pi ^{*}} 
which is deterministic as well.
show
[Proof]
Assume that R {\displaystyle R} 
is deterministic, meaning for constants a , s , s ′ {\displaystyle a,s,s'} 
the value R a ( s , s ′ ) {\displaystyle R_{a}(s,s')} 
is also constant. For γ < 1 {\displaystyle \gamma <1} 
it is known that there exists a unique fixed point V ∗ {\displaystyle V^{*}} 
which satisfies the value iteration (Bellman equation) recursion
V ∗ ( s ) = max a E [ R a ( s , s ′ ) + γ V ∗ ( s ′ ) ] {\displaystyle V^{}(s)=\max {a}E\left[R{a}(s,s')+\gamma V^{}(s')\right]} 
From inspection, notice that this fixed point is the value function associated to the following policy.
π ∗ ( s ) := arg  max a E [ R a ( s , s ′ ) + γ V ∗ ( s ′ ) ] {\displaystyle \pi ^{}(s):=\arg \max {a}E\left[R{a}(s,s')+\gamma V^{}(s')\right]} 
By unrolling the Bellman recursion, one can show that V ∗ {\displaystyle V^{*}} 
is indeed optimal (simultaneously for all states) over the set of deterministic policies.
V ∗ ( s 0 ) = max a 0 E [ R a 0 ( s 0 , s 1 ) + γ V ∗ ( s 1 ) ] = max a 0 E [ R a 0 ( s 0 , s 1 ) + γ max a 1 E [ R a 1 ( s 1 , s 2 ) + γ V ∗ ( s 2 ) ] ] = max a 0 , a 1 E [ R a 0 ( s 0 , s 1 ) + γ ( R a 1 ( s 1 , s 2 ) + γ V ∗ ( s 2 ) ) ] = sup { a t } t = 0 ∞ E [ ∑ t = 0 ∞ γ t R a t ( s t , s t + 1 ) ] {\displaystyle {\begin{aligned}V^{}(s_{0})&=\max {a{0}}E\left[R_{a_{0}}(s_{0},s_{1})+\gamma V^{}(s_{1})\right]\&=\max {a{0}}E\left[R_{a_{0}}(s_{0},s_{1})+\gamma \max {a{1}}E\left[R_{a_{1}}(s_{1},s_{2})+\gamma V^{}(s_{2})\right]\right]\&=\max {a{0},a_{1}}E\left[R_{a_{0}}(s_{0},s_{1})+\gamma \left(R_{a_{1}}(s_{1},s_{2})+\gamma V^{}(s_{2})\right)\right]\&=\sup {{a{t}}{t=0}^{\infty }}E\left[\sum {t=0}^{\infty }\gamma ^{t}R{a{t}}(s_{t},s_{t+1})\right]\end{aligned}}} 
Consider the case where π {\displaystyle \pi } 
is probabilistic, meaning the action taken a := π ( s ) {\displaystyle a:=\pi (s)} 
is a random variable. One can show any such non-deterministic policy is dominated by deterministic π ∗ {\displaystyle \pi ^{*}} 
as follows.
V ∗ ( s 0 ) = max a 0 E [ R a 0 ( s 0 , s 1 ) + γ V ∗ ( s 1 ) ] ≥ E [ R π ( s 0 ) ( s 0 , s 1 ) + γ V ∗ ( s 1 ) ] = E [ R π ( s 0 ) ( s 0 , s 1 ) + γ max a 1 E [ R a 1 ( s 1 , s 2 ) + γ V ∗ ( s 2 ) ] ] ≥ E [ R π ( s 0 ) ( s 0 , s 1 ) + γ ( R π ( s 1 ) ( s 1 , s 2 ) + γ V ∗ ( s 2 ) ) ] ≥ E [ ∑ t = 0 ∞ γ t R π ( s t ) ( s t , s t + 1 ) ] {\displaystyle {\begin{aligned}V^{}(s_{0})&=\max {a{0}}E\left[R_{a_{0}}(s_{0},s_{1})+\gamma V^{}(s_{1})\right]\&\geq E\left[R_{\pi (s_{0})}(s_{0},s_{1})+\gamma V^{}(s_{1})\right]\&=E\left[R_{\pi (s_{0})}(s_{0},s_{1})+\gamma \max {a{1}}E\left[R_{a_{1}}(s_{1},s_{2})+\gamma V^{}(s_{2})\right]\right]\&\geq E\left[R_{\pi (s_{0})}(s_{0},s_{1})+\gamma \left(R_{\pi (s_{1})}(s_{1},s_{2})+\gamma V^{*}(s_{2})\right)\right]\&\geq E\left[\sum {t=0}^{\infty }\gamma ^{t}R{\pi (s_{t})}(s_{t},s_{t+1})\right]\end{aligned}}} 
Simulator models
[ edit source]
In many cases, it is difficult to represent the transition probability distributions, P a ( s , s ′ ) {\displaystyle P_{a}(s,s')} 
, explicitly. In such cases, a simulator can be used to model the MDP implicitly by providing samples from the transition distributions. One common form of implicit MDP model is an episodic environment simulator that can be started from an initial state and yields a subsequent state and reward every time it receives an action input. In this manner, trajectories of states, actions, and rewards, often called episodes may be produced.
Another form of simulator is a generative model , a single step simulator that can generate samples of the next state and reward given any state and action. [6] (Note that this is a different meaning from the term generative model in the context of statistical classification.) In algorithms that are expressed using pseudocode, G {\displaystyle G} 
is often used to represent a generative model. For example, the expression s ′ , r ← G ( s , a ) {\displaystyle s',r\gets G(s,a)} 
might denote the action of sampling from the generative model where s {\displaystyle s} 
and a {\displaystyle a} 
are the current state and action, and s ′ {\displaystyle s'} 
and r {\displaystyle r} 
are the new state and reward. Compared to an episodic simulator, a generative model has the advantage that it can yield data from any state, not only those encountered in a trajectory.
These model classes form a hierarchy of information content: an explicit model trivially yields a generative model through sampling from the distributions, and repeated application of a generative model yields an episodic simulator. In the opposite direction, it is only possible to learn approximate models through regression. The type of model available for a particular MDP plays a significant role in determining which solution algorithms are appropriate. For example, the dynamic programming algorithms described in the next section require an explicit model, and Monte Carlo tree search requires a generative model (or an episodic simulator that can be copied at any state), whereas most reinforcement learning algorithms require only an episodic simulator.
Example
[ edit source] 
Pole Balancing example (rendering of the environment from the Open AI gym benchmark)
An example of MDP is the Pole-Balancing model, which comes from classic control theory.
In this example, we have
S {\displaystyle S} is the set of ordered tuples ( θ , θ ˙ , x , x ˙ ) {\displaystyle (\theta ,{\dot {\theta }},x,{\dot {x}})} given by pole angle, angular velocity, position of the cart and its speed.
A {\displaystyle A} is { − 1 , 1 } {\displaystyle {-1,1}} , corresponding to applying a force on the left (right) on the cart.
P a ( s , s ′ ) {\displaystyle P_{a}(s,s')} is the transition of the system, which in this case is going to be deterministic and driven by the laws of mechanics.
R a ( s , s ′ ) {\displaystyle R_{a}(s,s')} is 1 {\displaystyle 1} if the pole is up after the transition, zero otherwise. Therefore, this function only depend on s ′ {\displaystyle s'} in this specific case.
Algorithms
[ edit source]
Solutions for MDPs with finite state and action spaces may be found through a variety of methods such as dynamic programming. The algorithms in this section apply to MDPs with finite state and action spaces and explicitly given transition probabilities and reward functions, but the basic concepts may be extended to handle other problem classes, for example using function approximation. Also, some processes with countably infinite state and action spaces can be exactly reduced to ones with finite state and action spaces. [7]
The standard family of algorithms to calculate optimal policies for finite state and action MDPs requires storage for two arrays indexed by state: value V {\displaystyle V} 
, which contains real values, and policy π {\displaystyle \pi } 
, which contains actions. At the end of the algorithm, π {\displaystyle \pi } 
will contain the solution and V ( s ) {\displaystyle V(s)} 
will contain the discounted sum of the rewards to be earned (on average) by following that solution from state s {\displaystyle s} 
.
The algorithm has two steps, (1) a value update and (2) a policy update, which are repeated in some order for all the states until no further changes take place. Both recursively update a new estimation of the optimal policy and state value using an older estimation of those values.
V ( s ) := ∑ s ′ P π ( s ) ( s , s ′ ) ( R π ( s ) ( s , s ′ ) + γ V ( s ′ ) ) {\displaystyle V(s):=\sum {s'}P{\pi (s)}(s,s')\left(R_{\pi (s)}(s,s')+\gamma V(s')\right)} 
π ( s ) := argmax a  { ∑ s ′ P a ( s , s ′ ) ( R a ( s , s ′ ) + γ V ( s ′ ) ) } {\displaystyle \pi (s):=\operatorname {argmax} {a}\left{\sum {s'}P{a}(s,s')\left(R{a}(s,s')+\gamma V(s')\right)\right}} 
Their order depends on the variant of the algorithm; one can also do them for all states at once or state by state, and more often to some states than others. As long as no state is permanently excluded from either of the steps, the algorithm will eventually arrive at the correct solution. [8]
Notable variants
[ edit source]
Value iteration
[ edit source]
In value iteration ( Bellman 1957), which is also called backward induction, the π {\displaystyle \pi } 
function is not used; instead, the value of π ( s ) {\displaystyle \pi (s)} 
is calculated within V ( s ) {\displaystyle V(s)} 
whenever it is needed. Substituting the calculation of π ( s ) {\displaystyle \pi (s)} 
into the calculation of V ( s ) {\displaystyle V(s)} 
gives the combined step; [furtherexplanationneeded]
V i + 1 ( s ) := max a { ∑ s ′ P a ( s , s ′ ) ( R a ( s , s ′ ) + γ V i ( s ′ ) ) } , {\displaystyle V_{i+1}(s):=\max {a}\left{\sum {s'}P{a}(s,s')\left(R{a}(s,s')+\gamma V_{i}(s')\right)\right},} 
where i {\displaystyle i} 
is the iteration number. Value iteration starts at i = 0 {\displaystyle i=0} 
and V 0 {\displaystyle V_{0}} 
as a guess of the value function. It then iterates, repeatedly computing V i + 1 {\displaystyle V_{i+1}} 
for all states s {\displaystyle s} 
, until V {\displaystyle V} 
converges with the left-hand side equal to the right-hand side (which is the " Bellman equation" for this problem [clarificationneeded] ). Lloyd Shapley's 1953 paper on stochastic games included as a special case the value iteration method for MDPs, [9] but this was recognized only later on. [10]
Value iteration is guaranteed to converge for γ < 1 {\displaystyle \gamma <1} 
by the Banach fixed-point theorem.
show
[Proof]
The Banach fixed-point theorem states that a given contraction mapping has a unique fixed point; further, one can asymptotically approach this fixed points by iterated application of the contraction mapping. It then suffices to show that value iteration is a contraction mapping, which is shown below for γ < 1 {\displaystyle \gamma <1} 
.
Denote X a V ( s ) := ∑ s ′ P a ( s , s ′ ) ( R a ( s , s ′ ) + γ V i ( s ′ ) ) {\displaystyle X_{a}^{V}(s):=\sum {s'}P{a}(s,s')\left(R_{a}(s,s')+\gamma V_{i}(s')\right)} 
and ( B V ) ( s ) := max a X a V ( s ) {\displaystyle ({\mathcal {B}}V)(s):=\max {a}X{a}^{V}(s)} 
for convenience.
‖ B V − B W ‖ ∞ = max s | ( B V ) ( s ) − ( B W ) ( s ) | = max s | max a X a V ( s ) − max a X a W ( s ) | ≤ max s max a | X a V ( s ) − X a W ( s ) | = max s max a γ | ∑ s ′ P a ( s , s ′ ) ( V i ( s ′ ) − W i ( s ′ ) ) | ≤ max s max a γ max s ′ | V i ( s ′ ) − W i ( s ′ ) | = γ max s ′ | V i ( s ′ ) − W i ( s ′ ) | = γ ‖ V i − W i ‖ ∞ {\displaystyle {\begin{aligned}|{\mathcal {B}}V-{\mathcal {B}}W|{\infty }&=\max {s}\left|({\mathcal {B}}V)(s)-({\mathcal {B}}W)(s)\right|\&=\max {s}\left|\max {a}X{a}^{V}(s)-\max {a}X{a}^{W}(s)\right|\&\leq \max {s}\max {a}\left|X{a}^{V}(s)-X{a}^{W}(s)\right|\&=\max {s}\max {a}\gamma \left|\sum {s'}P{a}(s,s')\left(V{i}(s')-W{i}(s')\right)\right|\&\leq \max {s}\max {a}\gamma \max {s'}\left|V{i}(s')-W{i}(s')\right|\&=\gamma \max {s'}\left|V{i}(s')-W{i}(s')\right|\&=\gamma |V{i}-W{i}|{\infty }\end{aligned}}} 
Policy iteration
[ edit source]
In policy iteration [11], one first performs Value Determination by solving for V {\displaystyle V} 
from the linear system described in step one, then performs Policy Improvement by computing π {\displaystyle \pi } 
as in step two, then repeats both steps until the policy converges. (Policy iteration was invented by Howard to optimize Sears catalogue mailing, which he had been optimizing using value iteration. [12])
Since policy iteration effectively interleaves a linear inverse problem with a nonlinear operation, it may interpreted as a type of relaxation method.
This variant has the advantage that there is a definite stopping condition. Since there is a unique solution V {\displaystyle V} 
for each policy π {\displaystyle \pi } 
, the algorithm is completed once the Policy Improvement produces the same policy twice consecutively.
While there are situations where policy iteration may be faster than value iteration (e.g. when the action space is significantly larger than the state space), policy iteration is usually slower than value iteration for a large number of possible states.
Modified policy iteration
[ edit source]
In modified policy iteration ( van Nunen 1976; Puterman & Shin 1978), step one is repeated several times, and then step two is performed once. [13] [14] Then step one is again repeated several times and so on.
Prioritized sweeping
[ edit source]
In this variant, the steps are preferentially applied to states which are in some way important – whether based on the algorithm (there were large changes in V {\displaystyle V} 
or π {\displaystyle \pi } 
around those states recently) or based on use (those states are near the starting state, or otherwise of interest to the person or program using the algorithm).
Computational complexity
[ edit source]
Algorithms for finding optimal policies with time complexity polynomial in the size of the problem representation exist for finite MDPs. Thus, decision problems based on MDPs are in computational complexity class P. [15] However, due to the curse of dimensionality, the size of the problem representation is often exponential in the number of state and action variables, limiting exact solution techniques to problems that have a compact representation. In practice, online planning techniques such as Monte Carlo tree search can find useful solutions in larger problems, and, in theory, it is possible to construct online planning algorithms that can find an arbitrarily near-optimal policy with no computational complexity dependence on the size of the state space. [16]
Extensions and generalizations
[ edit source]
A Markov decision process is a stochastic game with only one player.
Partial observability
[ edit source]
Main article: Partially observable Markov decision process
The solution above assumes that the state s {\displaystyle s} 
is known when action is to be taken; otherwise π ( s ) {\displaystyle \pi (s)} 
cannot be calculated. When this assumption is not true, the problem is called a partially observable Markov decision process or POMDP.
Constrained Markov decision processes
[ edit source]
Constrained Markov decision processes (CMDPS) are extensions to Markov decision process (MDPs). There are three fundamental differences between MDPs and CMDPs. [17]
There are multiple costs incurred after applying an action instead of one.
CMDPs are solved with linear programs only, and dynamic programming does not work.
The final policy depends on the starting state.
The method of Lagrange multipliers applies to CMDPs. Many Lagrangian-based algorithms have been developed.
Natural policy gradient primal-dual method. [18]
There are a number of applications for CMDPs. It has recently been used in motion planning scenarios in robotics. [19]
Continuous-time Markov decision process
[ edit source]
In discrete-time Markov Decision Processes, decisions are made at discrete time intervals. However, for continuous-time Markov decision processes, decisions can be made at any time the decision maker chooses. In comparison to discrete-time Markov decision processes, continuous-time Markov decision processes can better model the decision-making process for a system that has continuous dynamics, i.e., the system dynamics are defined by ordinary differential equations (ODEs). This modelling framework can be applied to areas such as queueing systems, epidemic processes, and population processes.
Like the discrete-time Markov decision processes, in continuous-time Markov decision processes the agent aims to find the optimal policy that would maximize the expected cumulative reward. The key difference with the standard case is that, due to the continuous nature of the time variable, summation is replaced by an integral:
max E π  [ ∫ 0 ∞ γ t r ( s ( t ) , π ( s ( t ) ) ) d t | s 0 ] {\displaystyle \max \operatorname {E} _{\pi }\left[\left.\int {0}^{\infty }\gamma ^{t}r(s(t),\pi (s(t))),dt;\right|s{0}\right]} 
where 0 ≤ γ < 1. {\displaystyle 0\leq \gamma <1.} 
Discrete space: Linear programming formulation
[ edit source]
If the state space and action space are finite, we could use linear programming to find the optimal policy, which was one of the earliest approaches applied. Here we only consider the ergodic model, which means our continuous-time MDP becomes an ergodic continuous-time Markov chain under a stationary policy. Under this assumption, although the decision maker can make a decision at any time in the current state, there is no benefit in taking multiple actions. It is better to take an action only at the time when system is transitioning from the current state to another state. Under some conditions, [20] if our optimal value function V ∗ {\displaystyle V^{*}} 
is independent of state i {\displaystyle i} 
, we will have the following inequality:
g ≥ R ( i , a ) + ∑ j ∈ S q ( j ∣ i , a ) h ( j ) ∀ i ∈ S and a ∈ A ( i ) {\displaystyle g\geq R(i,a)+\sum _{j\in S}q(j\mid i,a)h(j)\quad \forall i\in S{\text{ and }}a\in A(i)} 
If there exists a function h {\displaystyle h} 
, then V ¯ ∗ {\displaystyle {\bar {V}}^{*}} 
will be the smallest g {\displaystyle g} 
satisfying the above equation. In order to find V ¯ ∗ {\displaystyle {\bar {V}}^{*}} 
, we could use the following linear programming model:
Primal linear program(P-LP)
Minimize g s.t g − ∑ j ∈ S q ( j ∣ i , a ) h ( j ) ≥ R ( i , a ) ∀ i ∈ S , a ∈ A ( i ) {\displaystyle {\begin{aligned}{\text{Minimize}}\quad &g\{\text{s.t}}\quad &g-\sum _{j\in S}q(j\mid i,a)h(j)\geq R(i,a),,\forall i\in S,,a\in A(i)\end{aligned}}} 
Dual linear program(D-LP)
Maximize ∑ i ∈ S ∑ a ∈ A ( i ) R ( i , a ) y ( i , a ) s.t. ∑ i ∈ S ∑ a ∈ A ( i ) q ( j ∣ i , a ) y ( i , a ) = 0 ∀ j ∈ S , ∑ i ∈ S ∑ a ∈ A ( i ) y ( i , a ) = 1 , y ( i , a ) ≥ 0 ∀ a ∈ A ( i ) and ∀ i ∈ S {\displaystyle {\begin{aligned}{\text{Maximize}}&\sum _{i\in S}\sum _{a\in A(i)}R(i,a)y(i,a)\{\text{s.t.}}&\sum _{i\in S}\sum _{a\in A(i)}q(j\mid i,a)y(i,a)=0\quad \forall j\in S,\&\sum _{i\in S}\sum _{a\in A(i)}y(i,a)=1,\&y(i,a)\geq 0\qquad \forall a\in A(i){\text{ and }}\forall i\in S\end{aligned}}} 
y ( i , a ) {\displaystyle y(i,a)} 
is a feasible solution to the D-LP if y ( i , a ) {\displaystyle y(i,a)} 
is nonnative and satisfied the constraints in the D-LP problem. A feasible solution y ∗ ( i , a ) {\displaystyle y^{*}(i,a)} 
to the D-LP is said to be an optimal solution if
∑ i ∈ S ∑ a ∈ A ( i ) R ( i , a ) y ∗ ( i , a ) ≥ ∑ i ∈ S ∑ a ∈ A ( i ) R ( i , a ) y ( i , a ) {\displaystyle {\begin{aligned}\sum _{i\in S}\sum _{a\in A(i)}R(i,a)y^{*}(i,a)\geq \sum _{i\in S}\sum _{a\in A(i)}R(i,a)y(i,a)\end{aligned}}} 
for all feasible solution y ( i , a ) {\displaystyle y(i,a)} 
to the D-LP. Once we have found the optimal solution y ∗ ( i , a ) {\displaystyle y^{*}(i,a)} 
, we can use it to establish the optimal policies.
Continuous space: Hamilton–Jacobi–Bellman equation
[ edit source]
In continuous-time MDP, if the state space and action space are continuous, the optimal criterion could be found by solving the Hamilton–Jacobi–Bellman (HJB) partial differential equation. In order to discuss the HJB equation, we need to reformulate our problem
V ( s ( 0 ) , 0 ) = max a ( t ) = π ( s ( t ) ) ∫ 0 T r ( s ( t ) , a ( t ) ) d t + D [ s ( T ) ] s.t. d s ( t ) d t = f [ t , s ( t ) , a ( t ) ] {\displaystyle {\begin{aligned}V(s(0),0)={}&\max _{a(t)=\pi (s(t))}\int _{0}^{T}r(s(t),a(t)),dt+D[s(T)]\{\text{s.t.}}\quad &{\frac {ds(t)}{dt}}=f[t,s(t),a(t)]\end{aligned}}} 
D ( ⋅ ) {\displaystyle D(\cdot )} 
is the terminal reward function, s ( t ) {\displaystyle s(t)} 
is the system state vector, a ( t ) {\displaystyle a(t)} 
is the system control vector we try to find. f ( ⋅ ) {\displaystyle f(\cdot )} 
shows how the state vector changes over time. The Hamilton–Jacobi–Bellman equation is as follows:
0 = max a ( r ( t , s , a ) + ∂ V ( t , s ) ∂ s f ( t , s , a ) ) {\displaystyle 0=\max _{a}(r(t,s,a)+{\frac {\partial V(t,s)}{\partial s}}f(t,s,a))} 
We could solve the equation to find the optimal value function V ∗ {\displaystyle V^{*}} 
, which in turns yield the optimal control at any time t {\displaystyle t} 
, a ( t ) {\displaystyle a(t)} 
through a ( t ) = argmax a ( r ( t , s , a ) + ∂ V ∗ ( t , s ) ∂ s f ( t , s , a ) ) . {\displaystyle a(t)={\underset {a}{\text{argmax}}}(r(t,s,a)+{\frac {\partial V^{*}(t,s)}{\partial s}}f(t,s,a)).} 
Reinforcement learning
[ edit source]
Main article: Reinforcement learning
Reinforcement learning is an interdisciplinary area of machine learning and optimal control that has, as main objective, finding an approximately optimal policy for MDPs where transition probabilities and rewards are unknown. [21]
Reinforcement learning can solve Markov-Decision processes without explicit specification of the transition probabilities which are instead needed to perform policy iteration. In this setting, transition probabilities and rewards must be learned from experience, i.e. by letting an agent interact with the MDP for a given number of steps. Both on a theoretical and on a practical level, effort is put in maximizing the sample efficiency, i.e. minimimizing the number of samples needed to learn a policy whose performance is ε − {\displaystyle \varepsilon -} 
close to the optimal one (due to the stochastic nature of the process, learning the optimal policy with a finite number of samples is, in general, impossible).
Reinforcement Learning for discrete MDPs
[ edit source]
For the purpose of this section, it is useful to define a further function, which corresponds to taking the action a {\displaystyle a} 
and then continuing optimally (or according to whatever policy one currently has):
Q ( s , a ) = ∑ s ′ P a ( s , s ′ ) ( R a ( s , s ′ ) + γ V ( s ′ ) ) . {\displaystyle \ Q(s,a)=\sum {s'}P{a}(s,s')(R_{a}(s,s')+\gamma V(s')).\ } 
While this function is also unknown, experience during learning is based on ( s , a ) {\displaystyle (s,a)} 
pairs (together with the outcome s ′ {\displaystyle s'} 
; that is, "I was in state s {\displaystyle s} 
and I tried doing a {\displaystyle a} 
and s ′ {\displaystyle s'} 
happened"). Thus, one has an array Q {\displaystyle Q} 
and uses experience to update it directly. This is known as Q-learning.
Other scopes
[ edit source]
Learning automata
[ edit source]
Main article: Learning automata
Another application of MDP process in machine learning theory is called learning automata. This is also one type of reinforcement learning if the environment is stochastic. The first detail learning automata paper is surveyed by Narendra and Thathachar (1974), which were originally described explicitly as finite-state automata. [22] Similar to reinforcement learning, a learning automata algorithm also has the advantage of solving the problem when probability or rewards are unknown. The difference between learning automata and Q-learning is that the former technique omits the memory of Q-values, but updates the action probability directly to find the learning result. Learning automata is a learning scheme with a rigorous proof of convergence. [23]
In learning automata theory, a stochastic automaton consists of:
a set x of possible inputs,
a set Φ = { Φ 1, ..., Φ s } of possible internal states,
a set α = { α 1, ..., α r } of possible outputs, or actions, with r ≤ s,
an initial state probability vector p(0) = ≪ p 1(0), ..., p s(0) ≫,
a computable function A which after each time step t generates p( t + 1) from p( t), the current input, and the current state, and
a function G: Φ → α which generates the output at each time step.
The states of such an automaton correspond to the states of a "discrete-state discrete-parameter Markov process". [24] At each time step t = 0,1,2,3,..., the automaton reads an input from its environment, updates P( t) to P( t + 1) by A, randomly chooses a successor state according to the probabilities P( t + 1) and outputs the corresponding action. The automaton's environment, in turn, reads the action and sends the next input to the automaton. [23]
Category theoretic interpretation
[ edit source]
Other than the rewards, a Markov decision process ( S , A , P ) {\displaystyle (S,A,P)} 
can be understood in terms of Category theory. Namely, let A {\displaystyle {\mathcal {A}}} 
denote the free monoid with generating set A. Let Dist denote the Kleisli category of the Giry monad. Then a functor A → D i s t {\displaystyle {\mathcal {A}}\to \mathbf {Dist} } 
encodes both the set S of states and the probability function P.
In this way, Markov decision processes could be generalized from monoids (categories with one object) to arbitrary categories. One can call the result ( C , F : C → D i s t ) {\displaystyle ({\mathcal {C}},F:{\mathcal {C}}\to \mathbf {Dist} )} 
a context-dependent Markov decision process, because moving from one object to another in C {\displaystyle {\mathcal {C}}} 
changes the set of available actions and the set of possible states. [citationneeded]
Alternative notations
[ edit source]
The terminology and notation for MDPs are not entirely settled. There are two main streams — one focuses on maximization problems from contexts like economics, using the terms action, reward, value, and calling the discount factor β or γ, while the other focuses on minimization problems from engineering and navigation [citationneeded] , using the terms control, cost, cost-to-go, and calling the discount factor α. In addition, the notation for the transition probability varies.
In addition, transition probability is sometimes written Pr ( s , a , s ′ ) {\displaystyle \Pr(s,a,s')} 
, Pr ( s ′ ∣ s , a ) {\displaystyle \Pr(s'\mid s,a)} 
or, rarely, p s ′ s ( a ) . {\displaystyle p_{s's}(a).} 
See also
[ edit source]
Probabilistic automata
Odds algorithm
Quantum finite automata
Partially observable Markov decision process
Dynamic programming
Bellman equation for applications to economics.
Hamilton–Jacobi–Bellman equation
Optimal control
Recursive economics
Mabinogion sheep problem
Stochastic games
Q-learning
Markov chain
References
[ edit source]
↑ Puterman, Martin L. (1994). Markov decision processes: discrete stochastic dynamic programming. Wiley series in probability and mathematical statistics. Applied probability and statistics section. New York: Wiley. ISBN 978-0-471-61977-2 .
↑ Yin, Bo (2021). Airtime Management for Low-Latency Densely Deployed Wireless Networks (PhD thesis). Japan: Kyoto University.
↑ Schneider, S.; Wagner, D. H. (1957-02-26). "Error detection in redundant systems". Papers presented at the February 26-28, 1957, western joint computer conference: Techniques for reliability on - IRE-AIEE-ACM '57 (Western). New York, NY, USA: Association for Computing Machinery. pp. 115– 121. doi: 10.1145/1455567.1455587. ISBN 978-1-4503-7861-1 . {{ [cite book](https://en.wikipedia.org/wiki/Template:Cite_book)}} : ISBN / Date incompatibility ( help)
↑ Bellman, Richard (1958-09-01). "Dynamic programming and stochastic control processes". Information and Control. 1 (3): 228– 239. Bibcode: 1958InfCo...1..228B. doi: 10.1016/S0019-9958(58)80003-0. ISSN 0019-9958.
Jump up to: 1 2 Sutton, Richard S.; Barto, Andrew G. (2018). Reinforcement learning: an introduction. Adaptive computation and machine learning series (2nd ed.). Cambridge, Massachusetts: The MIT Press. ISBN 978-0-262-03924-6 .
↑ Kearns, Michael; Mansour, Yishay; Ng, Andrew (2002). "A Sparse Sampling Algorithm for Near-Optimal Planning in Large Markov Decision Processes". Machine Learning. 49 ( 193– 208): 193– 208. doi: 10.1023/A:1017932429737.
↑ Wrobel, A. (1984). "On Markovian decision models with a finite skeleton". Zeitschrift für Operations Research. 28 (1): 17– 27. doi: 10.1007/bf01919083. S2CID 2545336.
↑ Reinforcement Learning: Theory and Python Implementation. Beijing: China Machine Press. 2019. p. 44. ISBN 9787111631774 .
↑ Shapley, Lloyd (1953). "Stochastic Games". Proceedings of the National Academy of Sciences of the United States of America. 39 (10): 1095– 1100. Bibcode: 1953PNAS...39.1095S. doi: 10.1073/pnas.39.10.1095. PMC 1063912. PMID 16589380.
↑ Kallenberg, Lodewijk (2002). "Finite state and action MDPs". In Feinberg, Eugene A.; Shwartz, Adam (eds.). Handbook of Markov decision processes: methods and applications. Springer. ISBN 978-0-7923-7459-6 .
↑ Howard, Ronald A. (1960). Dynamic Programming and Markov Processes (PDF). The M.I.T. Press.
↑ Howard 2002, "Comments on the Origin and Application of Markov Decision Processes"
↑ Puterman, M. L.; Shin, M. C. (1978). "Modified Policy Iteration Algorithms for Discounted Markov Decision Problems". Management Science. 24 (11): 1127– 1137. doi: 10.1287/mnsc.24.11.1127.
↑ van Nunen, J.A. E. E (1976). "A set of successive approximation methods for discounted Markovian decision problems". Zeitschrift für Operations Research. 20 (5): 203– 208. doi: 10.1007/bf01920264. S2CID 5167748.
↑ Papadimitriou, Christos; Tsitsiklis, John (1987). "The Complexity of Markov Decision Processes". Mathematics of Operations Research. 12 (3): 441– 450. doi: 10.1287/moor.12.3.441. hdl: 1721.1/2893. Retrieved November 2, 2023.
↑ Kearns, Michael; Mansour, Yishay; Ng, Andrew (November 2002). "A Sparse Sampling Algorithm for Near-Optimal Planning in Large Markov Decision Processes". Machine Learning. 49 (2/3): 193– 208. doi: 10.1023/A:1017932429737.
↑ Altman, Eitan (1999). Constrained Markov decision processes. Vol. 7. CRC Press.
↑ Ding, Dongsheng; Zhang, Kaiqing; Jovanovic, Mihailo; Basar, Tamer (2020). Natural policy gradient primal-dual method for constrained Markov decision processes. Advances in Neural Information Processing Systems.
↑ Feyzabadi, S.; Carpin, S. (18–22 Aug 2014). "Risk-aware path planning using hierarchical constrained Markov Decision Processes". Automation Science and Engineering (CASE). IEEE International Conference. pp. 297, 303.
↑ Continuous-Time Markov Decision Processes. Stochastic Modelling and Applied Probability. Vol. 62. 2009. doi: 10.1007/978-3-642-02547-1. ISBN 978-3-642-02546-4 .
↑ Shoham, Y.; Powers, R.; Grenager, T. (2003). "Multi-agent reinforcement learning: a critical survey" (PDF). Technical Report, Stanford University: 1– 13. Retrieved 2018-12-12.
↑ Narendra, K. S.; Thathachar, M. A. L. (1974). "Learning Automata – A Survey". IEEE Transactions on Systems, Man, and Cybernetics. SMC-4 (4): 323– 334. Bibcode: 1974ITSMC...4..323N. CiteSeerX 10.1.1.295.2280. doi: 10.1109/TSMC.1974.5408453. ISSN 0018-9472.
Jump up to: 1 2 Narendra, Kumpati S.; Thathachar, Mandayam A. L. (1989). Learning automata: An introduction. Prentice Hall. ISBN 9780134855585 .
↑ Narendra & Thathachar 1974, p.325 left.
Sources
[ edit source]
Bellman, R. (1957), Dynamic Programming, Princeton University Press, ISBN 978-0-486-42809-3 {{ [citation](https://en.wikipedia.org/wiki/Template:Citation)}} : ISBN / Date incompatibility ( help) . Dover paperback edition (2003)
Further reading
[ edit source]
Bellman., R. E. (2003) [1957]. Dynamic Programming (Dover paperback ed.). Princeton, NJ: Princeton University Press. ISBN 978-0-486-42809-3 .
Bertsekas, D. (1995). Dynamic Programming and Optimal Control. Vol. 2. MA: Athena.
Derman, C. (1970). Finite state Markovian decision processes. Academic Press.
Feinberg, E.A.; Shwartz, A., eds. (2002). Handbook of Markov Decision Processes. Boston, MA: Kluwer. ISBN 9781461508052 .
Guo, X.; Hernández-Lerma, O. (2009). Continuous-Time Markov Decision Processes. Stochastic Modelling and Applied Probability. Springer. ISBN 9783642025464 .
Meyn, S. P. (2007). Control Techniques for Complex Networks. Cambridge University Press. ISBN 978-0-521-88441-9 . Archived from the original on 19 June 2010. Appendix contains abridged "Meyn & Tweedie". Archived from the original on 18 December 2012.
Puterman., M. L. (1994). Markov Decision Processes. Wiley.
Ross, S. M. (1983). Introduction to stochastic dynamic programming (PDF). Academic press. Archived from the original (PDF) on 2022-03-04. Retrieved 2019-01-19.
Sutton, R. S.; Barto, A. G. (2017). Reinforcement Learning: An Introduction. Cambridge, MA: The MIT Press.
Tijms., H.C. (2003). A First Course in Stochastic Models. Wiley. ISBN 9780470864289 .
Retrieved from " https://en.wikipedia.org/w/index.php?title=Markov_decision_process&oldid=1366464633"
Categories:
Optimal decisions
Dynamic programming
Markov processes
Stochastic control
Hidden categories:
Articles with short description
Short description matches Wikidata
CS1 errors: ISBN date
Wikipedia articles needing clarification from July 2018
Wikipedia articles needing clarification from January 2018
CS1: long volume value
All articles with unsourced statements
Articles with unsourced statements from December 2020
Articles with unsourced statements from December 2019
This page was last edited on 28 July 2026, at 04:28 (UTC).
Page was rendered with Parsoid.
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view
Search
Search [-]
Toggle the table of contents
Markov decision process
23 languages Add topic 