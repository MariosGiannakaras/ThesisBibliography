> Source: https://arxiv.org/pdf/2410.06212

Solving robust MDPs as a sequence of static RL problems 
Adil Zouitine1,2, Matthieu Geist3, Emmanuel Rachelson1 
1ISAE-SUPAERO, France 2IRT Saint-Exupery, France 
3Cohere, Canada adil.zouitine@irt-saintexupery.com 
matthieu@cohere.com emmanuel.rachelson@isae-supaero.fr 
October 10, 2024 
Abstract 
Designing control policies whose performance level is guaranteed to remain above a given threshold in a span of environments is a critical feature for the adoption of reinforcement learning (RL) in real-world applications. The search for such robust policies is a notoriously difficult problem, related to the so-called dynamic model of transition function uncertainty, where the environment dynamics are allowed to change at each time step. But in practical cases, one is rather interested in robustness to a span of static transition models throughout interaction episodes. The static model is known to be harder to solve than the dynamic one, and seminal algorithms, such as robust value iteration, as well as most recent works on deep robust RL, build upon the dynamic model. In this work, we propose to revisit the static model. We suggest an analysis of why solving the static model under some mild hypotheses is a reasonable endeavor, based on an equivalence with the dynamic model, and formalize the general intuition that robust MDPs can be solved by tackling a series of static problems. We introduce a generic meta-algorithm called IWOCS, which incrementally identifies worst-case transition models so as to guide the search for a robust policy. Discussion on IWOCS sheds light on new ways to decouple policy optimization and adversarial transition functions and opens new perspectives for analysis. We derive a deep RL version of IWOCS and demonstrate it is competitive with state-of-the-art algorithms on classical benchmarks. 
1 Introduction One major obstacle in the way of real-life deployment of reinforcement learning (RL) algorithms is their inability to produce policies that retain, without further training, a guaranteed level of efficiency when controlling a system that somehow differs from the one they were trained upon. This property is referred to as robustness, by opposition to resilience, which is the ability to recover, through continued learning, from environmental changes. For example, when learning control policies for aircraft stabilization using a simulator, it is crucial that the learned controller be able to control a span of aircraft configurations with different geometries, or masses, or in various atmospheric conditions. Depending on the criticality of the considered application, one will prefer to optimize the expected performance over a set of environments (thus weighting in the probability of occurrence of a given configuration) or, at the extreme, optimize for the worst case configuration. Here, we consider 
1 
 
 
 
 
 
 
 
 
 
 
such worst case guarantees and revisit the framework of robust Markov Decision Processes (MDPs) [Iyengar, 2005]. 
Departing from the common perspective which views robust MDPs as two-player games, we investigate whether it is possible to solve them through a series of non-robust problems. The two-player game formulation is called the dynamic model of transition function uncertainty, as an adversarial environment is allowed to change the transition dynamics at each time step. The solution to this game can be shown to be equivalent, for stationary policies and rectangular uncertainty sets, to that of the static model, where the environment retains the same transition function throughout the time steps. 
Our first contribution is a series of arguments which cast the search for a robust policy as a resolution of the static model (Section 2). We put this formulation in perspective of recent related works in robust RL (Section 3). Then, we introduce a generic meta-algorithm which we call IWOCS for Incremental Worst-Case Search (Section 4). IWOCS builds upon the idea of incrementally identifying worst case transition functions and expanding a discrete uncertainty set, for which a robust policy can be approximated through a finite set of non-robust value functions. We instantiate two IWOCS algorithms, one on a toy illustrative problem with a discrete state space, then another on popular, continuous states and actions, robust RL benchmarks where it is shown to be competitive with state-of-the art robust deep RL algorithms (Section 5). 
2 Problem statement Reinforcement Learning (RL) [Sutton and Barto, 2018] considers the problem of learning a decision making policy for an agent interacting over multiple time steps with a dynamic environment. At each time step, the agent and environment are described through a state s P S, and an action a P A is performed; then the system transitions to a new state s1 according to probability T ps1|s, aq, while receiving reward rps, a, s1q. 
The tuple MT “ pS,A, T, rq forms a Markov Decision Process (MDP) [Puterman, 2014], which is often complemented with the knowledge of an initial state distribution p0psq. Without loss of generality and for the sake of readability, we will consider a unique starting state s0 in this paper, but our results extend straightforwardly to a distribution p0psq. A stationary decision making policy is a function πpa|sq mapping states to distributions over actions (writing πpsq the action for the special case of deterministic policies). 
Training a reinforcement learning agent in MDP MT consists in finding a policy that maximizes the expected γ-discounted return from s0: Jπ 
T “ Er ř8 
t“0 γ trpst, at, st`1q|s0, at „ π, st`1 „ T s “ V π 
T ps0q, where V π 
T is the value function of π in MDP MT , and γ P r0, 1q. An optimal policy in MT will be noted π˚ 
T and its value function V ˚ T . A convenient notation is the state-action value function 
Qπ T ps, aq “ Es1„T rrps, a, s1q ` γV π 
T ps1qs of policy π in MDP MT , and the corresponding optimal Q˚ T . 
Key notations are summarized in Appendix C. 
Robust MDPs, as introduced by Iyengar [2005] or Nilim and El Ghaoui [2005], introduce an additional challenge. The transition functions T are picked from an uncertainty set T and are allowed to change at each time step, yielding a sequence T “ tTtutPN. A common assumption, called sa-rectangularity, states that T is a Cartesian product of independent marginal sets of distributions on S, for each state-action pair. The value of a stationary policy π in the sequence of MDPs induced by T “ tTtutPN is noted V π 
T . The pessimistic value function for π is V π T psq “ minT V 
π T psq, where the 
agent plays a sequence of actions at P A drawn from π, against the environment, which in turn picks transition models Tt P T so as to minimize the overall return. The robust value function is the largest 
2
such pessimistic value function and hence the solution to V ˚ T psq “ maxπ minT V 
π T psq. The robust 
MDP problem can be cast as the zero-sum two-player game, where π̂ denote the decision making policy of the adversarial environment, deciding Tt P T based on previous observations. Then, the problem becomes maxπ minπ̂ V 
π π̂ psq, where V π 
π̂ is the expected value of a trajectory where policies π and π̂ play against each other. Hence, the optimal policy becomes the minimax policy, which makes it robust to all possible future evolutions of the environment’s properties. 
Robust Value Iteration. Following Iyengar [2005, Theorem 3.2], the optimal robust value function V ˚ 
T psq “ maxπ minT V π T psq is the unique solution to the robust Bellman equation V psq “ 
maxa minT Es1„T rrps, a, s1q ` γV ps1qs “ LV psq. This directly translates into a robust value iteration algorithm which constructs the Vn`1 “ LVn sequence of value functions [Satia and Lave Jr, 1973, Iyengar, 2005]. Such robust policies are, by design, very conservative, in particular when the uncertainty set is large and under the rectangularity assumption. Several attempts at mitigating this intrinsic over-conservativeness have been made from various perspectives. For instance, Lim et al. [2013] propose to learn and tighten the uncertainty set, echoing other works that incorporate knowledge about this set into the minimax resolution [Xu and Mannor, 2010, Mannor et al., 2012]. Other approaches [Wiesemann et al., 2013, Lecarpentier and Rachelson, 2019, Goyal and Grand-Clement, 2022] propose to lift the rectangularity assumption and capture correlations in uncertainties across states or time steps, yielding significantly less conservative policies. Ho et al. [2018] and Grand-Clément and Kroer [2021] retain the rectangularity assumption and propose algorithmic schemes to tackle large but discrete state and action spaces. 
The static model. In many applications, one does not wish to consider non-stationary transition functions, but rather to be robust to any transition function from T which remains stationary throughout a trajectory. This is called the static model of transition function uncertainty, by opposition to the dynamic model where transition functions can change at each time step. Hence, the static model’s minimax game boils down to maxπ minT V 
π T psq. If the agent is restricted to stationary 
policies πpa|sq, then maxπ minT V π T psq “ maxπ minT V 
π T psq [Iyengar, 2005, Lemma 3.3], that is the 
static and dynamic problems are equivalent, and the solution to the dynamic problem is found for a static adversary.1 In this paper, we will only consider stationary policies. 
No-duality gap. Wiesemann et al. [2013, Equation 4 and Proposition 9] introduce an important saddle point condition stating that maxπ minT V 
π T psq “ minT maxπ V 
π T psq. 2 
Incrementally solving the static model. Combining the static and dynamic models equivalence and the no-duality gap condition, we obtain that, for rectangular uncertainty sets and stationary policies, the optimal robust value function V ˚ 
T psq “ maxπ minT V π T psq “ maxπ minT V 
π T psq “ 
minT maxπ V π T psq “ minT V 
˚ T psq. The key idea we develop in this paper stems from this formulation. 
Suppose we are presented with MT0 and solve it to optimality, finding V ˚ 
0 psq “ V ˚ T0 
psq. Then, suppose we identify MT1 
as a possible better estimate of a worst case MDP in T than T0. We can solve for V ˚ T1 
and V ˚ 1 psq “ mintV ˚ 
T0 psq, V ˚ 
T1 psqu is the robust value function for the discrete uncertainty set 
T1 “ tT0, T1u. The intuition we attempt to capture is that by incrementally identifying candidate worst case MDPs, one should be able to define a sequence of discrete uncertainty sets Ti “ tTjujPr0,is 
whose robust value function V ˚ i decreases monotonously, and may converge to V ˚. In other words, 
1This does not imply the solution to the static model is the same as that of the dynamic model in general: the optimal static π may be non-stationary and finding it is known to be NP-hard. 
2The static-dynamic equivalence and the no-duality gap property’s context is recalled in Appendix B. 
3
it should be possible to incrementally robustify a policy by identifying the appropriate sequence of transition models and solving individually for them, trading the complexity of the dynamic model’s resolution for a sequence of classical MDP problems. The algorithm we propose in Section 4 follows this idea and searches for robust stationary policies for the dynamic model, using the static model, by incrementally growing a finite uncertainty set. 
3 Related work Robust RL as two-player games. A common approach to solving robust RL problems is to cast the dynamic formulation as a zero-sum two player game, as formalized by Morimoto and Doya [2005]. In this framework, an adversary, denoted by π̂ : S Ñ T , is introduced, and the game is formulated as maxπ minπ̂ Er 
ř8 
t“0 γ trpst, at, st`1q|s0, at „ πp¨|stq, Tt “ π̂pst, atq, st`1 „ Ttp¨|st, atqs. 
Most methods differ in how they constrain π̂’s action space within the uncertainty set. A first family of methods define π̂pstq “ Tref `∆pstq, where Tref denotes the reference transition function. Among this family, Robust Adversarial Reinforcement Learning (RARL) [Pinto et al., 2017] applies external forces at each time step t to disturb the reference dynamics. For instance, the agent controls a planar monopod robot, while the adversary applies a 2D force on the foot. In noisy action robust MDPs (NR-MDP) [Tessler et al., 2019] the adversary shares the same action space as the agent and disturbs the agent’s action πpsq. Such gradient-based approaches incur the risk of finding stationary points for π and π̂ which do not correspond to saddle points of the robust MDP problem. To prevent this, Mixed-NE [Kamalaruban et al., 2020] defines mixed strategies and uses stochastic gradient Langevin dynamics. Similarly, Robustness via Adversary Populations (RAP) [Vinitsky et al., 2020] introduces a population of adversaries, compelling the agent to exhibit robustness against a diverse range of potential perturbations rather than a single one, which also helps prevent finding stationary points that are not saddle points. Aside from this first family, State Adversarial MDPs [Zhang et al., 2020, 2021, Stanton et al., 2021] involve adversarial attacks on state observations, which implicitly define a partially observable MDP. The goal in this case is not to address robustness to the worst-case transition function but rather against noisy, adversarial observations. A third family of methods considers the general case of π̂pstq “ Tt where Tt P T . Minimax Multi-Agent Deep Deterministic Policy Gradient (M3DDPG) [Li et al., 2019] is designed to enhance robustness in multi-agent reinforcement learning settings, but boils down to standard robust RL in the two-agents case. Max-min TD3 (M2TD3) [Tanabe et al., 2022] considers a policy π, defines a value function Qps, a, T q which approximates Qπ 
T ps, aq “ Es1„T rrps, a, s1q ` γV π T ps1qs, updates an adversary π̂ so as 
to minimize Qps, πpsq, π̂psqq by taking a gradient step with respect to π̂’s parameters, and updates the policy π using a TD3 gradient update in the direction maximizing Qps, πpsq, π̂psqq. As such, M2TD3 remains a robust value iteration method which solves the dynamic problem by alternating updates on π and π̂, but since it approximates Qπ 
T , it is also closely related to the method we introduce in the next section. Wang et al. [2023] introduced a policy gradient method for robust MDPs with global convergence guarantees. While their work shares some conceptual similarities with ours in optimizing policies using a static model, it differs in key aspects. Their approach is limited to policy-based methods, whereas ours is more versatile, applicable to any RL algorithm, and scalable to larger state and action spaces. 
Regularization. Derman et al. [2021], Eysenbach and Levine [2022] also highlighted the strong link between robust MDPs and regularized MDPs, showing that a regularized policy learned during interaction with a given MDP was actually robust to an uncertainty set around this MDP. Kumar et al. [2023] propose a promising approach in which they derive the adversarial transition function in 
4
a closed form and demonstrate that it is a rank-one perturbation of the reference transition function. This simplification results in more streamlined computation for the robust policy gradient. 
Domain randomization (DR) [Tobin et al., 2017] learns a value function V psq “ maxπ ET„UpT qV π T psq 
which maximizes the expected return on average across a fixed distribution on T . As such, DR approaches do not optimize the worst-case performance. Nonetheless, DR has been used convincingly in applications [Mehta et al., 2020, OpenAI et al., 2019]. Similar approaches also aim to refine a base DR policy for application to a sequence of real-world cases [Lin et al., 2020, Dennis et al., 2020, Yu et al., 2018]. 
For a more complete survey of recent works in robust RL, we refer the reader to the work of Moos et al. [2022]. To the best of our knowledge, the approach sketched in the previous section and developed in the next one is the only one that directly addresses the static model. For that purpose, it exploits the equivalence with the dynamic model for stationary policies and solves the dual of the minimax problem, owing to the no-duality gap property. 
4 Incremental Worst-case Search In order to search for robust policies, we consider the no-duality gap property: the best performance one can expect in the face of transition function uncertainty maxπ minT V 
π T ps0q, is also the worst 
performance the environment can induce for each transition function’s optimal policy minT V ˚ T ps0q. 
If the value V π T ps0q was strictly concave/convex with respect to π/T respectively, we could hope 
to solve for the robust policy through a (sub)gradient ascent/descent method. Unfortunately, it seems V π 
T ps0q easily admits more convoluted optimization landscapes, involving stationary points, local minima and maxima. The maxπ problem often benefits from regularization [Geist et al., 2019]. Although one could study regularization for the minT problem [Grand-Clément and Petrik, 2022] or the equivalence with a regularized objective [Derman et al., 2021], we turn towards a simpler process conceptually. 
Algorithm. We consider a (small) discrete set of MDPs Ti “ tTjujPr0,is, for which we derive the corresponding optimal value functions Q˚ 
Tj . Then we define Qi as the function that maps any pair 
s, a to the smallest expected optimal outcome Qips, aq “ minjPr0,istQ ˚ Tj 
ps, aqu. The corresponding greedy policy is πipsq P argmaxaQips, aq and is a candidate for the robust policy. Let us define Ti`1 P argminTPT V 
πi 
T ps0q. Then, if V πi 
Ti`1 ps0q “ Qips0, πips0qq, we have found a robust policy for 
all transition models in T . Otherwise, we can solve for Q˚ Ti`1 
, append Ti`1 to Ti to form Ti`1, and repeat. Consequently, the idea we develop is to incrementally expand Ti by solving minTPT V 
πi 
T ps0q 
using optimization methods that can cope with ill-conditioned optimization landscapes. We call Incremental Worst Case Search (IWOCS) this general method, which we summarize in Algorithm 1. 
Rectangularity. One should note that Ti is a subset of a (supposed) sa-rectangular uncertainty set, but is not sa-rectangular itself, so there is no guarantee that the static-dynamic equivalence holds in Ti, and Qi is a pessimistic value function for the static case only, on the Ti uncertainty set. However, one can consider the sa-rectangular set T̃i “ 
Ś 
s,atTjp¨|s, aqujPr0,is composed of the cartesian product of all local tTjp¨|s, aqujPr0,is sets for each s, a pair. 
Property 1. For any i, s, a, we have 
Qips, aq ě Q˚ 
T̃i ps, aq ě Q˚ 
T ps, aq. 
5
Algorithm 1 Incremental Worst-Case Search meta-algorithm (in blue: the sub-algorithms) Input: T , T0, max nb of iterations M , tolerance on robust value ϵ for i “ 0 to M do 
Find non-robust Q˚ Ti 
“ maxπQ π Ti 
Define Ti “ tTjujďi 
Define robust Qi : s, a ÞÑ minjďitQ ˚ Tj 
ps, aqu 
Define candidate πipsq “ argmaxapQips, aqq 
Find worst Ti`1 “ argminTPT V πi 
T ps0q 
if |V πi 
Ti`1 ps0q ´Qips0, πips0q| ď ϵ then 
return πi, Ti`1, V πi 
Ti`1 ps0q 
end if end for return πM , TM`1, V πM 
TM`1 ps0q 
The proof follows directly from the fact that Ti Ă T̃i Ă T . We abusively call Qi the Ti-robust value function. In s0, Qi coincides with the robust value 
function for the static model of uncertainty with respect to the Ti uncertainty set. 
Property 2. For any i, s, a, we have 
Qi`1ps, aq ď Qips, aq. 
The proof is immediate as well since Qi`1 drawn among the same finite set of functions as Qi, complemented with Q˚ 
Ti`1 . Hence the Qi functions form a monotonically decreasing sequence. Since 
Qi is lower bounded (by Q˚ T ), IWOCS is necessarily convergent.3 
Choosing Ti`1. One could define a variant of Algorithm 1 which picks Ti`1 using another criterion than the worst-case transition model for πi, for instance by drawing Ti`1 uniformly at random, without loosing the two properties above. This underlines that the procedure for choosing Ti`1 
is a heuristic part of IWOCS. In all cases, the sequence of Qi remains monotonous and hence convergence in the limit remains guaranteed. Specifically, if, in the limit, Ti converges to T (under some appropriate measure on uncertainty sets), then Qi converges to the robust value function by definition. Whether this occurs or not, strongly depends on how Ti`1 is chosen at each iteration. In particular, premature stopping can occur if Ti`1 is among Ti. We conjecture choosing the worst-case transition model for πi is an intuitive choice here, and reserve further theoretical analysis on this matter for future work. One bottleneck difficulty of this selection procedure for Ti`1 lies in solving the minT problem accurately enough. However this difficulty is decoupled from that of the policy optimization process, which is only concerned with static MDPs. 
Illustration. We implement an IWOCS algorithm on a toy example, using value iteration (VI) as the policy optimization algorithm and a brute force search across transition functions to identify worst-case MDPs (V πi 
T ps0q is evaluated through Monte-Carlo rollouts). Detailed pseudo-code is provided in Appendix E. The goal here is to illustrate the behavior of IWOCS, compare it to the seminal robust value iteration (RVI) algorithm, and validate empirically that IWOCS is able to find worst-case static MDPs and robust policies. This vanilla IWOCS is evaluated on the “windy walk” 
3Although not necessarily to Q˚ T . 
6
Figure 1: Convergence to V ˚ vs Bellman iterates (right) in the Windy walk grid-world (left). 
grid-world MDP illustrated on Figure 1, where an agent wishes to navigate from a starting position S to a goal G. Actions belong to the discrete tN,S,E,W u set and transitions are deterministic, except in the “corridors”, where wind can knock back the agent to the left. In the topmost corridor, the probability of being knocked left is α, in the middle corridor it is α3 and it is α6 in the bottom corridor. Hence, the uncertainty set is fully parameterized by α, which takes 25 discrete values, uniformly distributed in r0, 0.5s. Rewards are ´1 at each time step and the goal is an absorbing state yielding zero reward. 
Figure 1 illustrates how IWOCS converges to the robust value function V ˚. RVI builds the sequence Vn`1 “ LVn and we plot |Vnps0q ´ V ˚ 
T ps0q| versus the number of robust Bellman iterates n. On the other hand, IWOCS requires its first policy optimization to terminate before it can report its first Qips0, πips0qq. Thus, we plot |Qips0, πips0qq ´ V ˚ 
T ps0q| after a fixed number of 100 standard Bellman backups for VI. It is important to note that one iterate of the standard Bellman operator requires solving a maxa in each state, while an iterate of the robust Bellman operator requires solving a more costly maxa minT problem in each state. Therefore, the x-axis does not account for computational time. IWOCS finds the worst-case static model after two iterations and converges to the same value as RVI. 
Computational complexity. Recall that the complexity of robust value iteration (RVI), in discrete state and action MDPs, and for a sa-rectangular uncertainty set, is Opcn2 
SnA logp1{ϵq{ logp1 ´ γqq, where nS is the number of states, nA the number of actions, ϵ is the tolerance for the robust value function and c is the cost of computing a single minT solution [Iyengar, 2005]. Recall also that the complexity of value iteration (VI) is Opn2SnA logp1{ϵq{ logp1 ´ γqq (VI is a special case of RVI with a singleton as uncertainty set, so c “ 1). Comparing IWOCS and RVI is a delicate matter because IWOCS is not based on a contraction mapping and has no convergence guarantees to the robust value function. Consequently, comparisons should be taken with a grain of salt. Yet, it is legitimate to wonder whether one can analyse the time complexity of IWOCS versus RVI. One iteration of IWOCS in discrete state and action spaces, as presented in Section 4, has the complexity of VI for the policy search part, plus the complexity of finding a worst case transition function in an sa-rectangular uncertainty set, which is OpcnSnAq. Hence, the overall complexity for M iterations of IWOCS is OpMpn2SnA logp1{ϵq{ logp1 ´ γq ` cnSnAqq. Compared to RVI, this bound will be smaller when c is large, which is the case when one deals with complex uncertainty sets and without further hypotheses. This short discussion provides a rationale to why IWOCS might be a time-efficient algorithm in large scale robust RL problems. 
5 Deep IWOCS We now turn towards challenging robust control problems and introduce an instance of IWOCS meant to accommodate large and continuous state and action spaces, using function approximators 
7
such as neural networks. This instance of IWOCS uses Soft Actor Critic (SAC) Haarnoja et al. [2018] as the policy optimization method, as it has been proven to yield a locally robust policy around the MDP it is trained upon [Eysenbach and Levine, 2022]. Appendix D summarizes our experimental computing setup. 
5.1 Method Accounting for regularization terms. Since SAC learns a regularized Q-function which accounts for the policy’s entropy, and lets the importance of this term vary along the optimization, orders of magnitude may change between QTi 
and QTj . To avoid the influence of this regularization term 
when defining the Ti-robust Q-function, we train an additional unregularized Q-network which only takes rewards into account. We call πT the policy network which approximates the optimal policy of the regularized MDP based on T . This policy’s (regularized) value function is approximated by the Q1 
T network (our implementation uses double Q-networks as per the common practice — all details in Appendix F), while an additional QT network (double Q-network also) tracks the unregularized value function of πT . The Ti-robust Q-function is defined with respect to this unregularized value function as Qips, aq “ minjPr0,istQTj ps, aqu. 
Partial state space coverage. In large state space MDPs, it is likely that interactions will not explore the full state space. Consequently, the different QTj 
functions are trained on replay buffers whose empirical distribution’s support my vary greatly. Evaluating neural networks outside of their training distribution is prone to generalization errors. This begs for indicator functions specifying on which ps, aq pair each QT is relevant. We chose to implement such an indicator function using predictive coding [Rao and Ballard, 1999] on the dynamical model Tj . Note that other choices can be equally good (or better), such as variance networks [Neklyudov et al., 2019], ensembles of neural networks [Lakshminarayanan et al., 2016] or 1-class classification [Béthune et al., 2023]. Our predictive coding model for Tj predicts T̂jps, aq “ s1 for deterministic dynamics, by minimizing the expected value of the loss ℓpT̂jps, aq; s1q “ }T̂jps, aq ´ s1}1. At inference time, along a trajectory, we consider QTj has been trained on sufficient data in st, at, if ℓpT̂jpst´1, at´1q; stq ď ρj , ie. if the prediction error for st is below the threshold ρj (details about tuning ρj in Appendix G). We set Q˚ 
Tj to be `8 in all states where ℓpT̂jpst´1, at´1q; stq ą ρj , so that it does not participate in the 
definition of Qi. 
Worst case identification. When V πi 
T ps0q is non differentiable with respect to T (or T ’s parameters), one needs to fall back on black-box optimization to find Ti`1 “ argminTPT V 
πi 
T ps0q. We turn to evolutionary strategies, and in particular CMA-ES [Hansen and Ostermeier, 2001] for that purpose, for its ability to escape local minima and efficiently explore the uncertainty set T even when the latter is high-dimensional (hyperparameters in Appendix F). Note that making V π 
T ps0q differentiable with respect to T is feasible by making the critic network explicitly depend on T ’s parameters, as in the work of Tanabe et al. [2022]. We do not resort to such a model, as it induces the risk for generalization errors, but it constitutes a promising alternative for research. To evaluate V πi 
T ps0q for a given T , we run a roll-out from s0 by applying πipsq in each encountered state s. Since we consider continuous action spaces and keep track of the critics QTj 
, Q1 Tj 
and the actor πTj for all Tj P Ti, we 
can make direct use of πTj which is designed to mimic an optimal policy in MTj . Specifically, in s, we evaluate j˚ “ argminjďiQ 
˚ Tj 
ps, πTj psqq, and apply πipsq “ πj˚ psq. If no Q˚ Tj 
is valid in s, we fall back to a default policy trained with domain randomization. 
8
5.2 Empirical evaluation Experimental framework. This section assesses the proposed algorithm’s worst-case performance and generalization capabilities. Experimental validation is performed on optimal control problems using the MuJoCo simulation environments4 [Todorov et al., 2012]. IWOCS is benchmarked against state-of-the-art robust reinforcement learning methods, including M2TD3 [Tanabe et al., 2022], M3DDPG [Li et al., 2019], and RARL [Pinto et al., 2017]. We also compare with Domain Randomization (DR) [Tobin et al., 2017] for completeness. 
For each environment, two versions of the uncertainty set are considered, following the benchmarks reported by Tanabe et al. [2022]. In the first one, T is parameterized by a global friction coefficient and the agent’s mass In the second one, a third, environment-dependent parameter is included (details in Appendix J). To ensure a fair comparison we also aligned with the sample budget of Tanabe et al. [2022]: performance metrics were collected after 4 million steps for environments with a 2D uncertainty set and after 5 million steps for those with a 3D uncertainty set. All reference methods optimize a single policy along these 4 or 5 million steps, but IWOCS optimizes a sequence of non-robust policies, for which we divide this sample budget: we constrain IWOCS to train its default policy and each subsequent SAC agent for a fixed number of interaction steps, so that the sum is 4 or 5 million steps (Appendix H and I).5 Results for all methods other than IWOCS are taken from the work of Tanabe et al. [2022]. All results reported below are averaged over 10 distinct random seeds. 
IWOCS*. We define a variant of IWOCS by replacing CMA-ES with a plain grid search across the uncertainty set, mimicking the worst case search of Tanabe et al. [2022], in order to assess whether CMA-ES effectively finds adequate worst-case transition models. 
Contrarily to CMA-ES, this will not scale to larger uncertainty set dimensions, but provides a safe baseline for optimization performance. 
Worst-case performance. Table 1 reports the normalized worst-case scores comparing IWOCS, M2TD3, SoftM2TD3, M3DDPG, RARL, and DR using TD3.6 
The worst-case scores for all final policies are evaluated by defining a uniform grid over the transition function’s parameter space and performing roll-outs for each transition model. 
To obtain comparable metrics across environments, we normalize each method’s score v using the vanilla TD3 (trained on the default transition function only) 
reference score vTD3 as a minimal baseline and the M2TD3 score vM2TD3 as target score: pv ´ vTD3q{|vM2TD3 ´ vTD3|. Hence this metric reports how much a method improves upon TD3, compared to how much M2TD3 improved upon TD3. Non-normalized scores are reported in Appendix K. IWOCS* and IWOCS demonstrate competitive performance, outperforming all other methods in 7 out of the 11 environments (note that we did not report results on 
simpler 1D uncertainty sets). IWOCS* permits a 2.04-fold improvement on average across environments, over the state-of-the-
art M2TD3. This validates in practice the soundness of solving a sequence of static models as an alternative to traditional methods building on dynamic models of uncertainty. It seems that Ant is an environment where IWOCS struggles to reach convincing worst case scores. We conjecture this is due to the wide range of possible mass and friction parameters, which make the optimization process very noisy (almost zero mass and friction is a worst-case T making the ant’s movement rather chaotic 
4Note that these do not respect the rectangularity assumption. 5Additional experiments allowing more samples to SAC at each iteration of IWOCS showed only marginal 
performance gains. This also illustrates how IWOCS can accomodate sub-optimal value functions and policies. 6Note that this DR agent is independent of the one we use as a default policy for IWOCS. 
9
Table 1: Avg. of normalized worst-case performance over 10 seeds for each method (HC=half-cheetah, H=hopper, HS=humanoid-standup, IP=inverted-pendulum, W=walker). 
Env M2TD3 SoftM2TD3 M3DDPG RARL DR (TD3) IWOCS* IWOCS 
Ant 2 1.00 ˘ 0.04 0.92 ˘ 0.06 ´0.72 ˘ 0.05 ´1.32 ˘ 0.04 0.02 ˘ 0.05 0.27 ˘ 0.36 ´0.27 ˘ 0.44 Ant 3 1.00 ˘ 0.09 0.97 ˘ 0.18 ´0.36 ˘ 0.20 ´1.28 ˘ 0.06 0.61 ˘ 0.03 0.28 ˘ 0.24 0.43 ˘ 0.68 HC2 1.00 ˘ 0.05 1.07 ˘ 0.05 ´0.02 ˘ 0.02 ´0.05 ˘ 0.02 0.84 ˘ 0.04 1.13 ˘ 0.02 0.75 ˘ 0.28 HC3 1.00 ˘ 0.14 1.39 ˘ 0.15 ´0.03 ˘ 0.05 ´0.13 ˘ 0.05 1.10 ˘ 0.04 0.61 ˘ 0.05 0.56 ˘ 0.15 H2 1.00 ˘ 0.05 1.09 ˘ 0.06 0.46 ˘ 0.06 0.61 ˘ 0.17 0.87 ˘ 0.03 6.52 ˘ 0.01 6.34 ˘ 0.11 H3 1.00 ˘ 0.09 0.68 ˘ 0.08 0.22 ˘ 0.04 0.56 ˘ 0.17 0.73 ˘ 0.13 4.94 ˘ 0.17 4.64 ˘ 0.16 HS2 1.00 ˘ 0.12 1.25 ˘ 0.16 0.98 ˘ 0.12 0.88 ˘ 0.13 1.14 ˘ 0.14 1.02 ˘ 0.12 0.98 ˘ 0.25 HS3 1.00 ˘ 0.11 0.96 ˘ 0.07 0.97 ˘ 0.07 0.88 ˘ 0.13 0.86 ˘ 0.06 1.18 ˘ 0.08 1.12 ˘ 0.21 IP2 1.00 ˘ 0.37 0.38 ˘ 0.08 ´0.00 ˘ 0.00 ´0.00 ˘ 0.00 0.15 ˘ 0.01 2.82 ˘ 0.00 2.82 ˘ 0.00 W2 1.00 ˘ 0.14 0.83 ˘ 0.15 0.04 ˘ 0.04 ´0.08 ˘ 0.01 0.71 ˘ 0.17 1.34 ˘ 0.02 1.23 ˘ 0.10 W3 1.00 ˘ 0.23 1.03 ˘ 0.20 0.06 ˘ 0.05 ´0.10 ˘ 0.01 0.65 ˘ 0.19 2.33 ˘ 0.10 2.10 ˘ 0.50 
Agg. 1.0 ˘ 0.13 0.96 ˘ 0.11 0.15 ˘ 0.06 ´0.0 ˘ 0.07 0.7 ˘ 0.08 2.04 ˘ 0.11 1.88 ˘ 0.26 
and hence induces a possibly misleading replay buffer) and may prevent the policy optimization algorithm to yield good non-robust policies and value functions given its sample budget. However, IWOCS provides a major (up to 6.5-fold) improvement on other environments. 
Average performance. While our primary aim is to maximize the worst-case performance, we also appreciate the significance of average performance in real-world scenarios. Table 2 reports the normalized average score (non-normalized scores in Appendix K) obtained by the resulting policy over a uniform grid of 100 transition functions in 2D uncertainty sets (1000 in 3D ones). Interestingly, M3DDPG and RARL feature negative normalized scores and perform worse on average than vanilla TD3 on most environments (as M2TD3 on 3 environments). DR and IWOCS display the highest average performance. Although this outcome was anticipated for DR, it may initially seem surprising for IWOCS, which was not explicitly designed to optimize mean performance. We posit this might be attributed to two factors. 
First, in MDPs which have not been identified as worst-cases, encountered states are likely to have no valid QTj 
value function. In these MDPs, if we were to apply any of the πTj , its score could be as 
low as the worst cast value (but not lower, otherwise the MDP should have been identified as a worst case earlier). But since IWOCS’ indicator functions identify these states as unvisited, the applied policy falls back to the DR policy, possibly providing a slightly better score above the worst case value for these MDPs. Second, the usage of indicator functions permits defining the IWOCS policy as an aggregate of locally optimized policies, possibly avoiding averaging issues. As for the worst-case scores, IWOCS does not perform well on Ant environments. However, it provides significantly better average scores than both DR and M2TD3 on all 9 other benchmarks. 
Worst case paths in the uncertainty set. IWOCS aims at solving iteratively the robust optimization problem by covering the worst possible case at each iteration. IWOCS and IWOCS* seem to reliably find worst case MDPs and policies in a number of cases, and we could expect the value of the candidate robust policy πi to increase throughout iterations. Table 3 permits tracking the worst case MDPs and policies along iterations for the Humanoid 2D environment (all other results in Appendix M). Specifically, it reports the worst case T1 “ pψ0 
1 , ψ 1 1q for the default policy π0, 
and its score Jπ0 
T1 (all scores are divided by 104 for readability). The next set of columns repeats these 
values for later iterations. Each line corresponds to a different random seed. In all lines, the worst 
10
Table 2: Avg. of normalized average performance over 10 seeds for each method. 
Env. M2TD3 SoftM2TD3 M3DDPG RARL DR (TD3) IWOCS* IWOCS 
A2 1.00 ˘ 0.02 1.04 ˘ 0.00 ´0.13 ˘ 0.12 ´1.04 ˘ 0.02 1.28 ˘ 0.03 1.03 ˘ 0.02 1.03 ˘ 0.02 A3 ´1.00 ˘ 0.44 ´0.36 ˘ 0.46 ´6.98 ˘ 0.44 ´8.94 ˘ 0.18 0.92 ˘ 0.22 ´0.24 ˘ 0.58 ´1.06 ˘ 2.00 HC2 1.00 ˘ 0.03 1.10 ˘ 0.04 ´1.08 ˘ 0.07 ´1.94 ˘ 0.03 1.84 ˘ 0.09 2.12 ˘ 0.02 2.11 ˘ 0.04 HC3 1.00 ˘ 0.07 1.17 ˘ 0.03 ´1.43 ˘ 0.14 ´2.48 ˘ 0.05 2.33 ˘ 0.12 2.86 ˘ 0.02 2.82 ˘ 0.12 H2 1.00 ˘ 0.07 0.74 ˘ 0.12 ´0.40 ˘ 0.11 1.86 ˘ 0.92 0.36 ˘ 0.08 2.27 ˘ 0.00 2.26 ˘ 0.07 H3 ´1.00 ˘ 0.23 ´1.20 ˘ 0.13 ´2.20 ˘ 0.37 1.63 ˘ 1.53 1.17 ˘ 0.23 7.33 ˘ 0.30 7.30 ˘ 0.23 HS2 ´1.00 ˘ 0.67 0.67 ˘ 0.83 ´1.83 ˘ 0.67 ´3.00 ˘ 1.33 0.50 ˘ 0.67 5.33 ˘ 1.83 5.00 ˘ 4.00 HS3 1.00 ˘ 0.75 0.38 ˘ 0.37 0.00 ˘ 0.50 ´1.75 ˘ 0.87 0.38 ˘ 0.87 7.75 ˘ 0.25 7.75 ˘ 0.25 IP2 1.00 ˘ 0.68 1.06 ˘ 0.46 ´1.10 ˘ 0.25 ´0.47 ˘ 0.32 2.47 ˘ 0.03 2.86 ˘ 0.00 2.86 ˘ 0.00 W2 1.00 ˘ 0.06 0.83 ˘ 0.16 ´0.53 ˘ 0.11 ´1.21 ˘ 0.02 0.91 ˘ 0.15 1.13 ˘ 0.00 1.14 ˘ 0.01 W3 1.00 ˘ 0.13 0.96 ˘ 0.18 ´0.57 ˘ 0.09 ´1.43 ˘ 0.04 1.13 ˘ 0.10 1.94 ˘ 0.05 1.95 ˘ 0.05 
Agg. 0.45 ˘ 0.29 0.58 ˘ 0.25 ´1.48 ˘ 0.26 ´1.71 ˘ 0.48 1.21 ˘ 0.24 3.13 ˘ 0.28 3.01 ˘ 0.62 
Table 3: Humanoid standup 2, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 Jπ3 
T4 
0 7.21 14.41 5.67 12.25 0.1 11.23 7.12 11.97 0.1 9.64 7.46 13.24 0.1 9.64 7.46 1 7.21 14.41 5.67 6.99 0.1 8.05 7.32 12.66 0.1 8.05 7.32 - - - -2 7.21 14.41 5.67 6.99 0.1 9.64 7.46 2.9 0.1 9.64 7.46 - - - -3 7.21 14.41 5.67 14.47 4.84 14.41 6.54 7.39 4.84 14.41 7.46 - - - -4 7.21 14.41 5.67 14.66 0.1 12.82 7.03 8.31 0.1 12.82 7.03 - - - -5 7.21 14.41 5.67 10.06 6.42 14.41 6.88 9.31 6.42 14.41 6.88 - - - -6 7.21 14.41 5.67 15.81 7.21 14.41 5.67 - - - - - - - -7 7.21 14.41 5.67 15.35 7.21 14.41 5.67 - - - - - - - -8 7.21 14.41 5.67 13.80 7.21 14.41 5.67 - - - - - - - -9 7.21 14.41 5.67 15.16 7.21 14.41 5.67 - - - - - - - -
11
case value Jπi 
Ti`1 steadily increases until convergence. In some runs (last 4 seeds), IWOCS’s stopping 
criterion is met after a single iteration: the worst case T2 “ p7.21, 14.41q for π1 is the same as T1, upon which π1 was trained. Overall the path through transition models and candidate robust policies illustrates the algorithmic behavior of IWOCS. As indicated in Section 4, IWOCS is guaranteed to converge but may miss the optimal pT, πq pair because the selection criterion for Ti`1 is a (well motivated) heuristic. This happens for a few seeds, where IWOCS seems to reach a different saddle point after 2 or 3 iterations. 
6 Conclusion The search for robust policies in uncertain MDPs is a long-standing challenge. In this work, we proposed to revisit the static model of transition function uncertainty, which is equivalent to the dynamic model in the case of sa-rectangular uncertainty sets and stationary policies. We proposed to exploit this equivalence and the no-duality-gap property to design an algorithm that trades the resolution of a two-player game, for a sequence of one-player MDP resolutions. This led to the IWOCS (Incremental Worst-Case Search) meta-algorithm, which incrementally builds a discrete, non-sa-rectangular uncertainty set and a sequence of candidate robust policies. An instance of IWOCS, using SAC for policy optimization, and CMA-ES or grid-search for worst-case search, appeared as a relevant method on popular robust RL benchmarks, and outperformed the state-of-the-art algorithms on a number of environments. IWOCS proposes a new perspective on the resolution of robust MDPs and robust RL problems, which appears as a competitive formulation with respect to traditional methods. It also poses new questions, like the tradeoffs between policy optimization precision and overall robustness, gradient-based methods for worst-case search, bounds due to approximate value functions, or validity of using Qi as a surrogate of the robust value function for the Ti uncertainty set. All these open interesting avenues for future research. 
References Louis Béthune, Paul Novello, Thibaut Boissin, Guillaume Coiffier, Mathieu Serrurier, Quentin 
Vincenot, and Andres Troya-Galvis. Robust one-class classification with signed distance function using 1-lipschitz neural networks. In Proceedings of the 40th International Conference on Machine Learning. PMLR, 2023. 
Michael Dennis, Natasha Jaques, Eugene Vinitsky, A. Bayen, Stuart J. Russell, Andrew Critch, and S. Levine. Emergent complexity and zero-shot transfer via unsupervised environment design. Neural Information Processing Systems, 2020. 
Esther Derman, Matthieu Geist, and Shie Mannor. Twice regularized mdps and the equivalence between robustness and regularization. Advances in Neural Information Processing Systems, 34, 2021. 
Benjamin Eysenbach and Sergey Levine. Maximum entropy rl (provably) solves some robust rl problems. In International Conference on Learning Representations, 2022. 
Matthieu Geist, Bruno Scherrer, and Olivier Pietquin. A theory of regularized markov decision processes. In International Conference on Machine Learning, pages 2160–2169. PMLR, 2019. 
Vineet Goyal and Julien Grand-Clement. Robust markov decision processes: Beyond rectangularity. Mathematics of Operations Research, 2022. 
12
Julien Grand-Clément and Christian Kroer. Scalable first-order methods for robust mdps. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, pages 12086–12094, 2021. 
Julien Grand-Clément and Marek Petrik. On the convex formulations of robust markov decision processes. arXiv preprint arXiv:2209.10187, 2022. 
Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan, Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, and Sergey Levine. Soft actor-critic algorithms and applications. arXiv preprint arXiv: Arxiv-1812.05905, 2018. 
Nikolaus Hansen and Andreas Ostermeier. Completely derandomized self-adaptation in evolution strategies. Evolutionary Computation, 9(2):159–195, 2001. doi: 10.1162/106365601750190398. 
Chin Pang Ho, Marek Petrik, and Wolfram Wiesemann. Fast bellman updates for robust mdps. In International Conference on Machine Learning, pages 1979–1988. PMLR, 2018. 
Garud Iyengar. Robust dynamic programming. Technical report, CORC Tech Report TR-2002-07, 2022. 
Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2): 257–280, 2005. 
Parameswaran Kamalaruban, Yu ting Huang, Ya-Ping Hsieh, Paul Rolland, C. Shi, and V. Cevher. Robust reinforcement learning via adversarial training with langevin dynamics. Neural Information Processing Systems, 2020. 
Navdeep Kumar, Esther Derman, Matthieu Geist, Kfir Levy, and Shie Mannor. Policy gradient for s-rectangular robust markov decision processes. arXiv preprint arXiv:2301.13589, 2023. 
B Lakshminarayanan, A Pritzel, and C Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. arxiv. arXiv preprint arXiv:1612.01474, 2016. 
Erwan Lecarpentier and Emmanuel Rachelson. Non-stationary markov decision processes, a worstcase approach using model-based reinforcement learning. Advances in neural information processing systems, 32, 2019. 
Shihui Li, Yi Wu, Xinyue Cui, Honghua Dong, Fei Fang, and Stuart Russell. Robust multi-agent reinforcement learning via minimax deep deterministic policy gradient. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 33, pages 4213–4220, 2019. 
Shiau Hong Lim, Huan Xu, and Shie Mannor. Reinforcement learning in robust markov decision processes. Advances in Neural Information Processing Systems, 26, 2013. 
Zichuan Lin, Garrett Thomas, Guangwen Yang, and Tengyu Ma. Model-based adversarial metareinforcement learning. In Advances in Neural Information Processing Systems, volume 33, pages 10161–10173, 2020. 
Shie Mannor, Ofir Mebel, and Huan Xu. Lightning does not strike twice: robust mdps with coupled uncertainty. In Proceedings of the 29th International Coference on International Conference on Machine Learning, pages 451–458, 2012. 
Bhairav Mehta, Manfred Diaz, Florian Golemo, Christopher J. Pal, and Liam Paull. Active domain randomization. In Proceedings of the Conference on Robot Learning, volume 100, pages 1162–1176, 2020. 
13
Janosch Moos, Kay Hansel, Hany Abdulsamad, Svenja Stark, Debora Clever, and Jan Peters. Robust reinforcement learning: A review of foundations and recent advances. Machine Learning and Knowledge Extraction, 4(1):276–315, 2022. 
Jun Morimoto and Kenji Doya. Robust reinforcement learning. Neural computation, 17(2):335–359, 2005. 
Kirill Neklyudov, Dmitry Molchanov, Arsenii Ashukha, and Dmitry Vetrov. Variance networks: When expectation does not meet your expectations. In International Conference on Learning Representations, 2019. 
Arnab Nilim and Laurent El Ghaoui. Robust control of markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005. 
OpenAI, Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias Plappert, Glenn Powell, Raphael Ribas, Jonas Schneider, Nikolas Tezak, Jerry Tworek, Peter Welinder, Lilian Weng, Qiming Yuan, Wojciech Zaremba, and Lei Zhang. Solving rubik’s cube with a robot hand. arXiv preprint arXiv: Arxiv-1910.07113, 2019. 
Lerrel Pinto, James Davidson, Rahul Sukthankar, and Abhinav Gupta. Robust adversarial reinforcement learning. In International Conference on Machine Learning, pages 2817–2826. PMLR, 2017. 
Martin L Puterman. Markov decision processes: discrete stochastic dynamic programming. John Wiley & Sons, 2014. 
Rajesh PN Rao and Dana H Ballard. Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. Nature neuroscience, 2(1):79–87, 1999. 
Jay K Satia and Roy E Lave Jr. Markovian decision processes with uncertain transition probabilities. Operations Research, 21(3):728–740, 1973. 
Samuel Stanton, Rasool Fakoor, Jonas Mueller, Andrew Gordon Wilson, and Alex Smola. Robust reinforcement learning for shifting dynamics during deployment. In Workshop on Safe and Robust Control of Uncertain Systems at NeurIPS, 2021. 
Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
Takumi Tanabe, Rei Sato, Kazuto Fukuchi, Jun Sakuma, and Youhei Akimoto. Max-min off-policy actor-critic method focusing on worst-case robustness to model misspecification. In Advances in Neural Information Processing Systems, 2022. 
Chen Tessler, Yonathan Efroni, and Shie Mannor. Action robust reinforcement learning and applications in continuous control. In International Conference on Machine Learning, pages 6215–6224. PMLR, 2019. 
Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In 2017 IEEE/RSJ international conference on intelligent robots and systems (IROS), pages 23–30. IEEE, 2017. 
Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 5026–5033. IEEE, 2012. doi: 10.1109/IROS.2012.6386109. 
14
Eugene Vinitsky, Yuqing Du, Kanaad Parvate, Kathy Jang, Pieter Abbeel, and Alexandre Bayen. Robust reinforcement learning using adversarial populations. arXiv preprint arXiv:2008.01825, 2020. 
Qiuhao Wang, Chin Pang Ho, and Marek Petrik. Policy gradient in robust mdps with global convergence guarantee. In Proceedings of the 40th International Conference on Machine Learning, ICML’23. JMLR.org, 2023. 
Wolfram Wiesemann, Daniel Kuhn, and Berç Rustem. Robust markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013. 
Huan Xu and Shie Mannor. Distributionally robust markov decision processes. Advances in Neural Information Processing Systems, 23, 2010. 
Wenhao Yu, C. K. Liu, and Greg Turk. Policy transfer with strategy optimization. International Conference On Learning Representations, 2018. 
Huan Zhang, Hongge Chen, Chaowei Xiao, Bo Li, Mingyan Liu, Duane Boning, and Cho-Jui Hsieh. Robust deep reinforcement learning against adversarial perturbations on state observations. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, Advances in Neural Information Processing Systems, volume 33, pages 21024–21037, 2020. 
Huan Zhang, Hongge Chen, Duane S Boning, and Cho-Jui Hsieh. Robust reinforcement learning on state observations with learned optimal adversary. In International Conference on Learning Representations, 2021. 
A Appendix 
B Key results from the literature In order to ease the reading of this paper, we recall the two theoretical results that Section 2 builds upon. We reproduce the text from the original papers [Iyengar, 2022, Wiesemann et al., 2013] but, for the sake of consistency, we use the notations of the present paper and indicate [in brackets] whenever we adjusted the original notation. All results quoted below apply to sa-rectangular uncertainty sets. 
Definition of the static and dynamic models, in the introduction of section 3 of [Iyengar, 2005]. 
(i) Static model: The adversary is restricted to choose the same, but unknown, [T p¨|s, aq] every time the state-action pair ps, aq is encountered. (ii) Dynamic model: The adversary is allowed to choose a possibly different conditional measure [T p¨|s, aq] every time the state-action pair ps, aq is encountered. [...] As mentioned in the introduction, the goal of the robust formulation is to systematically mitigate the effect of errors associated with estimating the state transitions; i.e., the state transition is, in fact, fixed but the decision maker is only able to estimate it to within a set. Thus, the static model is appropriate for this scenario. However, computing the optimal policy for the static model is NP-hard, therefore, we will restrict attention to the dynamic model. Clearly the value function in the dynamic model is a lower bound for the value function in the static model. We contrast the implications of the two models in Lemma 3.3. 
15
Equivalence of the value functions under the static and dynamic models [Iyengar, 2005, Lemma 3.3]. 
Lemma 3.3 (Dynamic vs. static adversary). Let [π : S Ñ A be a] stationary policy. Let V π and V̂ π be the value of the π in the dynamic and static model respectively. Then V π “ V̂ π. [...] In the proof of the result we have implicitly established that the “best-response” of dynamic adversary when the decision maker employs a stationary policy is, in fact, static [...]. 
Non-equivalence of the static and dynamic models for non-stationary policies, at the end of Section 3 of [Iyengar, 2005] 
Lemma 3.3 highlights an interesting asymmetry between the decision maker and the adversary that is a consequence of the fact that the adversary plays second. While it is optimal for a dynamic adversary to play static (stationary) policies when the decision maker is restricted to stationary policies, it is not optimal for the decision maker to play stationary policies against a static adversary. 
No-duality gap property [Wiesemann et al., 2013, Equation 4]. 
To date, the literature on robust MDPs has focused on (s, a)-rectangular ambiguity sets. For this class of ambiguity sets, it is shown in [Iyengar, 2005] and [Nilim and El Ghaoui, 2005] that the worst-case expected total reward [...] is maximized by a deterministic stationary policy for finite and infinite horizon MDPs. Optimal policies can be determined via extensions of the value and policy iteration. For some ambiguity sets, finding an optimal policy, as well as evaluating (2) for a given stationary policy, can be achieved in polynomial time. Moreover, the policy improvement problem satisfies the following saddle point condition 
sup π 
inf TPT 
E 
« 
8 ÿ 
t“0 
γtrpst, at, st`1q|s0 
ff 
“ inf TPT 
sup π 
E 
« 
8 ÿ 
t“0 
γtrpst, at, st`1q|s0 
ff 
C Notations Table 4 recalls all key notations used throughout the paper. The first block in Table 4 is for standard (non-robust) MDP quantities (used in Section 2 and after), the second for standard robust MDP quantities (Section 2 and after), the third for IWOCS-specific quantities (Section 4 and after), and finally the fourth for Deep-IWOCS notations (Section 5 and after). 
D Computing resources All experiments were run on a desktop machine (Intel i9, 10th generation processor, 64GB RAM) with a single NVIDIA RTX 3090 GPU. Averages, medians, and standard deviations were computed from 10 independent repetitions of each experiment. 
16
Table 4: Key notations 
Symbol Meaning 
MT “ pS,A, T, rq MDP with transition kernel T π Stationary policy S Ñ A V π T , Qπ 
T State and state-action value functions of policy π in MT 
Jπ T Scalar value V π 
T ps0q of initial state under π in MT 
π˚ T Optimal policy in MT 
V ˚ T , Q˚ 
T Optimal state and state-action value functions in MT 
T Uncertainty set V π T Value function of policy π under sequence of transition kernels T V π T , Qπ 
T Pessimistic value function of policy π for uncertainty set T V ˚ T , Q˚ 
T Robust value function for uncertainty set T Ti Non-sa-rectangular discrete uncertainty set T̃i sa-rectangular uncertainty superset of Ti Qi Ti-robust value function πT SAC’s approximation of π˚ 
T 
QT SAC’s approximation of Q˚ T 
Q1 T SAC’s estimate of πT ’s regularized value function 
T̂j Predictive coding model for Tj 
E Windy-walk gridworld The windy-walk environment used in Section 4 is a discrete grid-world environment illustrated in Figure 2. It features 36 discrete states corresponding to positions on the grid, and 4 discrete actions corresponding to cardinal moves. Six states are unreachable and correspond to walls, defining three corridors. The transition model is deterministic by default, except in the corridors where the wind blows. This transition model is parameterized by a scalar parameters α. In the Northern corridor: 
 the W action moves West with probability 1, 
 the N and S actions leave the position unchanged with probability 1 ´ α and the agent is pushed West with probability α, 
 the E action moves East with probability 1 ´ α and West with probability α. 
The middle corridor works the same way, but with probability α3 instead of α. In the Southern corridor: 
 the W action moves West with probability 1, 
 the N (resp. S) action move the agent respectively North (resp. South) with probability 1´α6 
(unless it runs into a wall in which case the position is unchanged), and West with probability α6, 
 the E action moves East with probability 1 ´ α6 and West with probability α6. 
Rewards are -1 for all transitions and the G state is an absorbing goal states yielding zero reward. The agent always starts in state S. Consequently, windy-walk is a stochastic shortest path. For small values of α, the optimal policy is to go straight from S to G, but as α increases, the wind 
17
blows harder, and it becomes more interesting to make a detour through the middle then Southern corridors. The corresponding robust MDP problem features an uncertainty set spanned by 25 discrete values of α, uniformly distributed in r0, 0.5s. 
The instance of IWOCS evaluated in Section 4 uses value iteration as a policy optimization algorithm and a brute-force grid search as a search method for worst-case transition functions, as summarized in Algorithm 1. In Algorithm 1 we abusively write Tα the transition model parameterized by α. 
In the experiments of Section 4, value iteration is run until a tolerance of 10´3 is met. γ is set to 0.95. Monte-Carlo estimates of V πi 
T ps0q use 300 independent rollouts (of length at most 104) from the starting state. 
Figure 2: Windy walk grid-world. 
Algorithm 1: IWOCS with value iteration and brute force worst-case search Input: T , T0, max number of iterations M , tolerance on robust value ϵ for i “ 0 to M do 
1 Find Q˚ Ti 
“ value_iterationpTiq /* Non-robust policy optimization */ 2 Define Ti “ tTjujPr0,is 
3 Define Qi : s, a ÞÑ minjPr0,istQ ˚ Tj 
ps, aqu /* Ti-robust value function */ 4 Define πipsq “ argmaxapQips, aqq /* Candidate policy */ 5 V πi 
Ti`1 ps0q “ `8 
6 for α P T do /* Identify worst T */ 7 Ṽ “ Monte-Carlo_rolloutspπiq 
8 if Ṽ ă V πi 
Ti`1 ps0q then 
9 V πi 
Ti`1 ps0q “ Ṽ 
10 Ti`1 “ Tα 
11 if |V πi 
Ti`1 ps0q ´Qips0, πips0q| ď ϵ then 
12 return πi, Ti`1, V πi 
Ti`1 ps0q /* Early termination condition */ 
return πM , TM`1, V πM 
TM`1 ps0q 
F Soft Actor-Critic and CMA-ES hyperparameters Deep IWOCS uses SAC [Haarnoja et al., 2018] for policy optimization and trains jointly a predictive coding model to predict the outcome of a state-action pair. Specifically, a single network called 
18
“enhanced critic” is trained to predict the regularized value function Q1ps, aq, the unregularized value function Qps, aq and a prediction of the transition outcome T̂ ps, aq. The critic network’s architecture is summarized in Figure 3a. All activation functions are ReLU except for the output layers (identity functions). Note that one more layer was necessary to appropriately estimate Q compared to Q1. Our implementation also uses double critics as per the common practice, to avoid overestimating Q and Q1 (totally independent networks, no shared layers). Given a replay buffer D, learning Q minimizes the loss 
LQ “ Es,a,s1„D,a1„π 
“ 
Qps, aq ´ rr ` γQ´ps1, a1qs ‰2 , 
where Q´ is a target network, updated through Polyak averaging. Similarly, Q1 minimizes 
L1 Q “ Es,a,s1„D,a1„π 
“ 
Q1ps, aq ´ rr ` γpQ1´ps1, a1q ´ α log πpa1|s1qqs ‰2 . 
Finally, T̂ minimizes LT̂ “ Es,a,s1„D 
” 
}T̂ ps, aq ´ s1}1 
ı 
. 
These three objective functions are minimized in turn with three distinct Adam optimizers to account for possible different orders of magnitude. 
(a) Enhanced critic (b) Actor 
Figure 3: Network architectures 
The actor network is a standard SAC actor trained with respect to the regularized Q-function Q1. The network’s architecture is depicted in Figure 3b. All activation functions are ReLU, except for the output values (identify for µ and tanh for log σ as per the common practice). The output action drawn from the network’s output is run through an additional tanh function following the usual SAC implementations. 
The search for worst case transition functions is performed by using the CMA-ES black-box optimization method [Hansen and Ostermeier, 2001]. The implementation used is the reference one of https://github.com/CyberAgentAILab/cmaes, off-the-shelf. 
All hyperparameter values for SAC and CMA-ES are summarized in Table 5. These values are the same across all experiments. 
19
Table 5: Hyperparameters of SAC 
Hyperparameter Value 
Learning rate actor 3e-4 Learning rate critic 1e-3 Adam epsilon 1e-5 Adam pβ1, β2q (0.9, 0.999) Batch size 256 Memory size 1e6 Gamma 0.99 Polyak update 0.995 Number of steps before training 1e4 
CMA-ES generations 6 CMAS-ES population size 100 CMA ES mean 0.5 CMA ES std 0.5 
G Adaptive thresholding for predictive coding As introduced in Section 5, the SAC-based implementation of IWOCS used in the experiments exploits a predictive coding mechanism in order to characterize each policy’s training distribution support and to avoid using a given πTi 
on samples outside its training distribution. Policy πTi and 
value function QTi are deemed usable in state st along the current trajectory if st was accurately 
predicted by the dynamics model T̂ipst´1, at´1q. Specifically, we consider a threshold ρi on the prediction error and consider QTi and πTi to be viable in st if ℓpT̂ipst´1, at´1q, stq ď ρi, with ℓpT̂ipst´1, at´1q, stq “ }T̂ipst´1, at´1q ´ st}1. In states where QTi is non-viable, we arbitrarily set its value to `8 so that it does not participate in Qips, aq “ minjďitQTj 
ps, aqu. We noted in the main text that alternative characterizations of the support distribution were possible, and we do not claim the present choice outperforms the alternatives. Notably, all choices induce a number of parameters to tune (here ρi). This leads to a number of design choices that make the implementation somehow more convoluted than the simple principle of IWOCS. While the main text kept things focused on the principles of IWOCS, we provide here a full pseudo-code (which is more representative of the provided code) for the sake of completeness. Appendix F already covered the network structure, the training losses and the training hyperparameters for SAC and CMA-ES. Hence, the present section focuses on how to adjust each ρi. 
Training of the enhanced critic network does not provide a usable value for ρi and experimental results demonstrated that accurate characterization of the training distribution’s support required per-MDP tuning. Since ρi needs to be tuned for πTi 
during iteration i (and is kept fixed thereafter), we couple its search with that of the worst case transition model to permit better overall efficiency. Specifically, at iteration i, we consider a discrete set R of possible values for threshold ρi. For each value in R, we identify the worst case transition model. Then, we keep the value of ρi that enabled the best pessimistic value. In a sense, this makes ρi a parameter of the candidate robust policy. This parameter is single-dimensional and hence its optimization is computationally undemanding. We emphasize that this tuning mechanism is both very naive and arbitrary. It is naive since it performs a grid search over discrete values of ρi, where it could have exploited optimization methods. It is arbitrary in the sense that it picks ρi by keeping as a selection heuristic the overall goal of identifying 
20
robust policies. Algorithm 2 summarizes the complete IWOCS process with adaptive thresholding for predictive 
coding. In the experiments of Section 5, R is a discrete set of 10 values evenly spaced between 0.1 and 1. 
Algorithm 2: Deep IWOCS with adaptive threshold Input: T , T0, maximum number of iterations M , discrete thresholds set R for i “ 0 to M do 
Find QTi , πTi 
, T̂i “ SACpTiq // Non-robust SAC and pred coding 1 Define Ti “ tTjujPr0,is 
2 Define V̂ “ ´8 // candidate worst value 3 for ρ P R do // loop over thresholds 
4 Define Q̃Tips, aq “ 
" 
`8 if ℓpT̂ipst´1, at´1q; stq ą ρ for s “ st QTi 
ps, aq otherwise. 5 Define Q̃ips, aq “ minjďitQ̃Tj ps, aqujPr0,is,@s, a // Ti-robust value function 6 Define J˚psq “ argminjďi Q̃Tj ps, πTj psqq,@s 
7 Define π̃ipsq “ 
" 
πdefaultpsq if Q̃ips, aq “ `8, πTj˚ psq with j˚ P J˚psq otherwise. // Candidate policy 
8 Find T̃i`1, V π̃i 
T̃i`1 ps0q “CMA-ESpV π̃i 
T ps0qq // Identify worst T 
9 if V π̃i 
T̃i`1 ps0q ě V̂ then // keep best ρ 
10 Set ρj “ ρ, V̂ “ V π̃i 
T̃i`1 ps0q 
11 Define Ti`1 “ T̃i`1, πi “ π̃i, V πi 
Ti`1 ps0q “ V π̃i 
T̃i`1 ps0q, Qi “ Q̃i 
12 if |V πi 
Ti`1 ps0q ´Qips0, πips0q| ď ϵ then 
13 return πi, Ti`1, V πi 
Ti`1 ps0q // Early termination condition 
return πM , TM`1, V πM 
TM`1 ps0q 
H Sample budgets In order to enable a fair comparison with the results of Tanabe et al. [2022] which we report in Table 1, we evaluate IWOCS with the same overall sample budget, ie. 4 million samples in 2D uncertainty set environments and 5 million samples in 3D uncertainty set environments. 
In 2D environments, the default DR policy is trained for 1.6 ¨ 106 steps, then 3 IWOCS iterations of 8 ¨ 105 each are run, for a total of 4 ¨ 106 collected samples. 
In 3D environments, the default DR policy is trained for 1.8 ¨ 106 steps, then 4 IWOCS iterations of 8 ¨ 105 each are run, for a total of 5 ¨ 106 collected samples. 
No fine-tuning of these training durations was performed. 
I Computational overhead due to IWOCS In Table 6 we report the average wall-clock time needed for our implementation of SAC to cover the 4 (resp. 5) million samples allocated for 2D (resp. 3D) environments without IWOCS. Then, we report 
21
Environment SAC IWOCS Ant 2 18h 36h Ant 3 22.5h 40h Halfcheetah 2 20h 38.5h Halfcheetah 3 25h 41h Walker 2 19h 40h Walker 3 24h 45h Hopper 2 20h 38h Hopper 3 25h 47h HumanoidStandup 2 18h 40h HumanoidStandup 3 22.5h 48h 
Table 6: Average wall-clock time for plain SAC and for IWOCS for the same number of samples. 
the time required by IWOCS to cover the same sample budget. This permits a fair evaluation of the overhead computational cost of IWOCS, without the bias due to implementation optimizations. 
J Uncertainty sets in MuJoCo environments The experiments of Section 5 follow the evaluation protocol proposed by Tanabe et al. [2022] and based on MuJoCo environments [Todorov et al., 2012]. These environments are designed with 2D or 3D uncertainty sets. Table 7 lists all environments evaluated, along with their uncertainty sets. The uncertainty sets column defines the ranges of variation for the parameters within each environment. The reference parameters column indicates the nominal or default values. The uncertainty parameters column describes the physical meaning of each parameter. 
Table 7: List of environment and parameters for the experiements 
Environment Uncertainty set T Reference values Uncertainty parameters Ant 2 r0.1, 3.0s ˆ r0.01, 3.0s p0.33, 0.04q torso mass; front left leg mass Ant 3 r0.1, 3.0s ˆ r0.01, 3.0s ˆ r0.01, 3.0s p0.33, 0.04, 0.06q torso mass; front left leg mass; front right leg mass 
HalfCheetah 2 r0.1, 4.0s ˆ r0.1, 7.0s p0.4, 6.36q world friction; torso mass HalfCheetah 3 r0.1, 4.0s ˆ r0.1, 7.0s ˆ r0.1, 3.0s p0.4, 6.36, 1.53q world friction; torso mass; back thigh mass 
Hopper 2 r0.1, 3.0s ˆ r0.1, 3.0s p1.00, 3.53q world friction; torso mass Hopper 3 r0.1, 3.0s ˆ r0.1, 3.0s ˆ r0.1, 4.0s p1.00, 3.53, 3.93q world friction; torso mass; thigh mass 
HumanoidStandup 2 r0.1, 16.0s ˆ r0.1, 8.0s p8.32, 1.77q torso mass; right foot mass HumanoidStandup 3 r0.1, 16.0s ˆ r0.1, 5.0s ˆ r0.1, 8.0s p8.32, 1.77, 4.53q torso mass; right foot mass; left thigh mass InvertedPendulum 2 r1.0, 31.0s ˆ r1.0, 11.0s p4.90, 9.42q pole mass; cart mass 
Walker 2 r0.1, 4.0s ˆ r0.1, 5.0s p0.7, 3.53q world friction; torso mass Walker 3 r0.1, 4.0s ˆ r0.1, 5.0s ˆ r0.1, 6.0s p0.7, 3.53, 3.93q world friction; torso mass; thigh mass 
K Non-normalized results Table 8 reports the non-normalized worst case scores, averaged across 10 independent runs for each benchmark. Table 9 reports the average score obtained by each agent across a grid of environments, also averaged across 10 independent runs for each benchmark. 
22
Table 8: Avg. ˘ std. error of worst-case performance over 10 seeds for each method 
Environment M2TD3 SoftM2TD3 M3DDPG RARL DR (TD3) IWOCS* IWOCS 
Ant 2 4.13 ± 0.11 3.92 ± 0.14 -0.25 ± 0.13 -1.77 ± 0.09 1.64 ± 0.13 2.27 ± 0.91 0.90 ± 1.13 Ant 3 0.10 ± 0.10 0.07 ± 0.20 -1.38 ± 0.22 -2.38 ± 0.07 -0.32 ± 0.03 -0.69 ± 0.26 -0.52 ± 0.74 HalfCheetah 2 2.61 ± 0.16 2.82 ± 0.16 -0.58 ± 0.06 -0.70 ± 0.05 2.12 ± 0.13 3.02 ± 0.07 1.81 ± 0.87 HalfCheetah 3 0.93 ± 0.21 1.53 ± 0.23 -0.66 ± 0.08 -0.81 ± 0.07 1.09 ± 0.06 0.33 ± 0.07 0.25 ± 0.23 Hopper 2 5.33 ± 0.28 5.79 ± 0.29 2.58 ± 0.29 3.34 ± 0.89 4.68 ± 0.15 33.58 ± 0.03 32.68 ± 0.54 Hopper 3 2.84 ± 0.25 1.98 ± 0.22 0.73 ± 0.11 1.64 ± 0.46 2.10 ± 0.35 13.47 ± 0.45 12.66 ± 0.42 HumanoidStandup 2 6.50 ± 0.70 7.94 ± 0.90 6.37 ± 0.72 5.78 ± 0.73 7.31 ± 0.78 6.62 ± 0.71 6.41 ± 1.46 HumanoidStandup 3 6.20 ± 0.64 5.99 ± 0.37 6.01 ± 0.38 5.54 ± 0.76 5.41 ± 0.34 7.19 ± 0.46 6.86 ± 1.19 InvertedPendulum 2 3.56 ± 1.32 1.36 ± 0.30 0.02 ± 0.00 0.02 ± 0.00 0.57 ± 0.02 10 ± 00 10 ± 00 Walker 2 3.14 ± 0.39 2.64 ± 0.43 0.39 ± 0.11 0.06 ± 0.04 2.31 ± 0.50 4.10 ± 0.07 3.80 ± 0.28 Walker 3 1.94 ± 0.40 2.00 ± 0.35 0.28 ± 0.09 0.00 ± 0.02 1.32 ± 0.34 4.29 ± 0.18 3.89 ± 0.89 
Table 9: Avg. ˘ std. deviation of average performance over 10 seeds for each method 
Environment M2TD3 SoftM2TD3 M3DDPG RARL (DDPG) DR (TD3) IWOCS* IWOCS 
Ant 2 5.44 ± 0.05 5.56 ± 0.01 1.86 ± 0.38 -1.00 ± 0.06 6.32 ± 0.09 5.54 ± 0.06 5.53 ± 0.06 Ant 3 2.66 ± 0.22 2.98 ± 0.23 -0.33 ± 0.22 -1.31 ± 0.09 3.62 ± 0.11 3.04 ± 0.29 2.63 ± 1.00 HalfCheetah 2 4.35 ± 0.05 4.52 ± 0.07 0.77 ± 0.12 -0.70 ± 0.05 5.79 ± 0.15 6.28 ± 0.04 6.26 ± 0.07 HalfCheetah 3 3.79 ± 0.09 4.02 ± 0.04 0.58 ± 0.18 -0.81 ± 0.07 5.54 ± 0.16 6.24 ± 0.03 6.19 ± 0.16 Hopper 2 2.51 ± 0.07 2.26 ± 0.12 1.15 ± 0.11 3.34 ± 0.89 1.89 ± 0.08 3.74 ± 0.00 3.73 ± 0.07 Hopper 3 0.85 ± 0.07 0.79 ± 0.04 0.49 ± 0.11 1.64 ± 0.46 1.50 ± 0.07 3.35 ± 0.09 3.34 ± 0.07 HumanoidStandup 2 0.97 ± 0.04 1.07 ± 0.05 0.92 ± 0.04 0.85 ± 0.08 1.06 ± 0.04 1.35 ± 0.11 1.33 ± 0.24 HumanoidStandup 3 1.09 ± 0.06 1.04 ± 0.03 1.01 ± 0.04 0.87 ± 0.07 1.04 ± 0.07 1.63 ± 0.02 1.63 ± 0.02 InvertedPendulum 2 6.13 ± 1.42 6.26 ± 0.95 1.76 ± 0.51 3.07 ± 0.66 9.18 ± 0.07 10 ± 00 10 ± 00 Walker 2 4.72 ± 0.12 4.37 ± 0.32 1.63 ± 0.22 0.26 ± 0.05 4.54 ± 0.31 4.99 ± 0.01 5.00 ± 0.02 Walker 3 4.27 ± 0.21 4.21 ± 0.30 1.65 ± 0.15 0.21 ± 0.07 4.48 ± 0.16 5.84 ± 0.08 5.86 ± 0.08 
23
L Soft Actor Critic baseline We conducted additional experiments using SAC to train on the reference transition kernel across all environments. These experiments aimed to confirm the performance similarities with TD3 and to emphasize the performance gap with IWOCS. The results are summarized in Table 10. 
Overall, SAC performs poorly in terms of worst-case score, reinforcing our earlier observation of its similarity to TD3. Specifically, SAC exhibits variability across different environments, sometimes outperforming TD3 and sometimes not. However, the scores generally remain within the same order of magnitude. For instance, in the Hopper environment, SAC achieves scores of 14 and 5.8 on Hopper 2 and Hopper 3, respectively, which surpass previous state-of-the-art methods. Despite this, IWOCS still shows a significant improvement, with final scores of 32.68 and 12.66, respectively. These results highlight the distinct advantages of our approach in achieving robust performance. 
Environment Avg ± Std Ant 2 -1.0 ± 0.4 Ant 3 -2.1 ± 0.1 Halfcheetah 2 -0.2 ± 0.002 Halfcheetah 3 -0.26 ± 0.04 Hopper 2 14 ± 0.99 Hopper 3 5.8 ± 0.4 Humanoid 2 3.8 ± 0.1 Humanoid 3 3.6 ± 0.27 Walker 2 0.8 ± 0.9 Walker 3 0.5 ± 0.7 
Table 10: Avg ˘ std. error of worst-case performance over 10 for SAC 
M Worst-case paths Table 3 illustrated the path followed by the successive identified worst-case transition functions Ti in the 2D uncertainty set of the Humanoid Standup 2 environment, across 10 independent optimization runs. For the sake of completeness, we provide here the same results for all environments, which permit drawing similar conclusions. Tables 11 and 12 start by recalling the physical meaning of each transition function’s parameters. Then, Tables 13 to 21 follow the same logic as Table 3 and report the evolution of worst-case parameters and values on all other environments than Humanoid Standup 2. 
Table 11: Physical meaning of transition function parameters in 2D environments 
Environment ψ1 ψ2 
Ant 2 torso mass front left leg mass Halfcheetah 2 world friction torso mass Hopper 2 world friction torso mass HumanoidStandup 2 right foot mass torsomass Walker 2 world friction torso mass 
24
Table 12: Physical meaning of transition function parameters in 3D environments 
Environment ψ1 ψ2 ψ3 
Ant 3 torso mass front left leg mass front right leg mass Halfcheetah 3 world friction torso mass back thigh mass Hopper 3 world friction torso mass thigh mass HumanoidStandup 3 torso mass left thigh mass right foot mass Walker 3 world friction torso mass thigh mass 
Table 13: Ant 2, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 Jπ3 
T4 
0 0.68 0.608 0.5 2.87 0.1 0.01 2.5 2.44 0.1 0.01 2.5 - - - -1 0.68 0.608 0.5 3.58 0.1 0.309 2.5 2.8 0.1 0.01 2.5 - - - -2 0.68 0.608 0.5 0.06 0.1 0.01 2.5 2.32 0.1 0.01 2.5 - - - -3 0.68 0.608 0.5 3.54 0.1 0.01 2.67 2.17 0.1 0.01 2.67 - - - -4 0.68 0.608 0.5 5.13 0.1 0.01 2.47 0.69 0.1 0.01 2.47 - - - -5 0.68 0.608 0.5 1.77 0.1 0.01 3.56 0.51 0.1 0.01 3.56 - - - -6 0.68 0.608 0.5 4.81 0.1 2.103 0.83 2.1 0.1 2.103 0.83 - - - -7 0.68 0.608 0.5 0.4 0.1 2.402 1.81 1.91 0.1 0.01 2.55 1.3 0.39 0.01 2.55 8 0.68 0.608 0.5 0.03 0.1 0.01 2.5 3.1 0.1 0.01 2.5 - - - -9 0.68 0.608 0.5 4.88 0.1 0.01 2.51 2.3 0.1 0.01 2.51 - - - -
N How many valid policies in s? The Deep-IWOCS method proposed in Section 5 introduced indicator functions constraining the use of a given policy to a subset of states. Depending on the environment and uncertainty parameters, we expect some policies to remain within the same set of explored states, while others will cover a very different state distribution. To quantify this aspect, we ran an experiment where the IWOCS final policy is run on the Hopper 3 benchmark, across a grid of transition functions. For each encountered state, we count how many policies are valid. Figure 4 reports the corresponding histograms (note the log-scale on the y-axis). 
O Discussion on the complexity of IWOCS Recall that the complexity of robust value iteration (RVI) in discrete state and action MDPs is OpCnS logp1{ϵq{ logp1 ´ γqq, where nS is the number of states, ϵ is the tolerance for the robust value function and C is the cost of computing maxa minT ER,S1 rR ` γV pS1qs in a given s [Iyengar, 2005]. In discrete state and action spaces, computing the value of the expectation has cost O(nS). The minT has to be solved once for every state and action and it’s a search over measures on S. Let c be its cost, and nA be the number of actions, then the cost of the maxa minT operation is OpcnSnAq for a sa-rectangular uncertainty set and the overall complexity of RVI is Opcn2SnA logp1{ϵq{ logp1 ´ γqq. 
Recall also that the complexity of value iteration (VI) is Opn2SnA logp1{ϵq{ logp1 ´ γqq (VI is a special case of RVI with a singleton as uncertainty set, so c “ 1). The ratio between the two complexity bounds is c. 
Comparing IWOCS and RVI is a delicate matter because IWOCS is not based on a contraction mapping and has no convergence guarantees to the robust value function. Consequently, comparisons 
25
Table 14: Halfcheetah 2, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 Jπ3 
T4 
0 3.61 0.79 1.57 5.28 3.61 0.1 3.02 7.23 3.61 0.1 3.02 - - - -1 3.61 0.79 1.57 6.93 3.61 0.1 3.02 7.23 3.61 0.1 3.02 - - - -2 3.61 0.79 1.57 7.82 3.61 0.1 3.01 6.32 3.61 0.1 3.01 - - - -3 3.61 0.79 1.57 5.70 3.61 0.1 3.09 6.40 3.61 0.1 3.09 - - - -4 3.61 0.79 1.57 7.83 3.61 0.1 3.02 7.26 3.61 0.1 3.02 - - - -5 3.61 0.79 1.57 4.29 3.61 0.1 3.02 7.04 3.61 0.1 3.02 - - - -6 3.61 0.79 1.57 4.80 3.61 0.1 2.98 7.62 3.61 0.1 2.98 - - - -7 3.61 0.79 1.57 7.70 3.61 0.1 3.03 8.56 3.61 0.1 3.03 - - - -8 3.61 0.79 1.57 5.17 3.61 0.1 3.02 6.28 3.61 0.1 3.02 - - - -9 3.61 0.79 1.57 4.89 3.61 0.1 3.03 6.79 3.61 0.1 3.03 - - - -
Table 15: Hopper 2, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 Jπ3 
T4 
0 2.13 0.1 3.35 2.43 2.13 0.1 3.35 - - - - - - - -1 2.13 0.1 3.35 1.07 2.13 0.1 3.35 - - - - - - - -2 2.13 0.1 3.35 3.51 2.13 0.1 3.35 - - - - - - - -3 2.13 0.1 3.35 1.35 2.13 0.1 3.35 - - - - - - - -4 2.13 0.1 3.35 3.32 2.13 0.1 3.35 - - - - - - - -5 2.13 0.1 3.35 3.53 2.13 0.1 3.35 - - - - - - - -6 2.13 0.1 3.35 1.20 2.13 0.1 3.35 - - - - - - - -7 2.13 0.1 3.35 3.33 2.13 0.1 3.35 - - - - - - - -8 2.13 0.1 3.35 3.48 2.13 0.1 3.35 - - - - - - - -9 2.13 0.1 3.35 1.90 2.13 0.1 3.35 - - - - - - - -
Table 16: Walker 2, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 Jπ3 
T4 
0 3.22 0.1 3.77 3.27 3.22 0.1 4.1 1.57 3.22 0.1 4.1 - - - -1 3.22 0.1 3.77 4.92 3.22 0.1 4.1 6.6 3.22 0.1 4.1 - - - -2 3.22 0.1 3.77 3.17 3.22 0.1 4.14 5.47 3.22 0.1 4.14 - - - -3 3.22 0.1 3.77 5.91 3.22 0.1 4.13 5.09 3.22 0.1 4.13 - - - -4 3.22 0.1 3.77 6.72 3.22 0.1 4.11 5.4 3.22 0.1 4.11 - - - -5 3.22 0.1 3.77 3.93 3.22 0.1 4.1 5.87 3.22 0.1 4.1 - - - -6 3.22 0.1 3.77 4.67 3.22 0.1 3.8 6.25 3.22 0.59 3.81 3.22 0.59 3.92 5.4 7 3.22 0.1 3.77 6.54 3.22 1.08 4.07 3.33 3.22 0.1 4.07 - - - -8 3.22 0.1 3.77 4.88 3.22 0.1 4.15 4.37 3.22 0.1 4.15 - - - -9 3.22 0.1 3.77 3.99 3.22 0.1 4.14 3.28 3.22 0.1 4.14 - - -
26
Table 17: Ant 3, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 ψ3 1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 ψ3 2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 ψ3 3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 ψ3 4 Jπ3 
T4 
0 0.68 0.01 0.309 -1.21 3.59 0.68 0.01 0.309 -1.21 4.59 - - - - - - - - -1 0.68 0.01 0.309 -1.21 0.54 1.26 1.505 2.701 -1.08 2.54 1.26 1.804 2.402 -0.9 2.3 1.26 1.804 2.402 -0.9 2 0.68 0.01 0.309 -1.21 5.92 2.13 0.309 1.804 -0.44 3.92 2.13 0.309 1.804 -0.44 - - - - -3 0.68 0.01 0.309 -1.21 -1.35 2.13 0.309 1.804 -0.44 1.23 2.13 0.309 1.804 -0.44 - - - - -4 0.68 0.01 0.309 -1.21 2.58 0.68 0.608 2.701 -1.02 2.71 0.1 0.309 2.402 -0.75 2.4 0.1 0.309 2.402 -0.75 5 0.68 0.01 0.309 -1.21 3.07 2.42 0.608 2.103 -0.78 5.29 2.42 0.608 2.103 -0.78 - - - - -6 0.68 0.01 0.309 -1.21 2.07 2.42 1.505 0.01 -0.92 3.33 2.71 0.309 2.103 -0.63 5.42 2.71 0.309 2.103 -0.63 7 0.68 0.01 0.309 -1.21 1.94 0.39 1.804 0.608 -1.02 2.21 0.1 1.505 2.103 -0.84 6.08 0.1 1.505 2.103 -0.84 8 0.68 0.01 0.309 -1.21 2.33 2.13 0.309 1.804 -0.44 4.21 2.13 0.309 1.804 -0.43 - - - - -9 0.68 0.01 0.309 -1.21 1.44 2.13 0.309 1.804 -0.44 2.1 2.13 0.309 1.804 -0.45 - - - - -
Table 18: Halfcheetah , worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 ψ3 1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 ψ3 2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 ψ3 3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 ψ3 4 Jπ3 
T4 
0 2.44 5.62 0.39 0.28 10.11 2.44 5.62 0.39 0.28 - - - - - - - - - -1 2.44 5.62 0.39 0.28 4.31 2.83 2.86 0.1 0.37 8.79 2.83 2.86 0.1 0.37 - - - - -2 2.44 5.62 0.39 0.28 8.74 2.44 5.62 0.39 0.28 - - - - - - - - - -3 2.44 5.62 0.39 0.28 9.78 2.44 5.62 0.39 0.28 - - - - - - - - - -4 2.44 5.62 0.39 0.28 10.30 2.44 5.62 0.39 0.28 - - - - - - - - - -5 2.44 5.62 0.39 0.28 8.9 2.83 6.31 0.39 0.35 8.0 2.83 6.31 0.39 0.35 - - - - -6 2.44 5.62 0.39 0.28 9.8 2.83 6.31 0.1 0.30 8.37 2.83 6.31 0.01 0.31 8.22 2.83 6.31 0.1 0.34 7 2.44 5.62 0.39 0.28 8.39 3.22 5.62 0.1 0.49 7.04 3.22 5.62 0.1 0.49 - - - - -8 2.44 5.62 0.39 0.28 11.60 2.44 5.62 0.39 0.28 - - - - - - - - - -9 2.44 5.62 0.39 0.28 9.15 2.44 5.62 0.39 0.28 - - - - - - - - - -
Table 19: Hopper 3, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 ψ3 1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 ψ3 2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 ψ3 3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 ψ3 4 Jπ3 
T4 
0 2.71 0.1 0.49 1.23 3.41 2.71 0.1 0.49 1.23 3.73 - - - - - - - - -1 2.71 0.1 0.49 1.23 3.81 2.71 0.39 0.1 1.31 3.51 2.71 0.39 0.1 1.35 2.81 2.71 0.39 0.1 1.35 2 2.71 0.1 0.49 1.23 2.29 2.71 0.39 0.1 1.31 3.24 2.71 0.39 0.1 1.31 - - - - -3 2.71 0.1 0.49 1.23 3.16 2.71 0.39 0.1 1.30 2.21 2.71 0.39 0.1 1.32 3.29 2.71 0.39 0.1 1.34 4 2.71 0.1 0.49 1.23 3.88 2.71 0.39 0.1 1.32 3.8 2.71 0.39 0.1 1.326 2.203 2.71 0.39 0.1 1.326 5 2.71 0.1 0.49 1.23 3.65 2.42 0.1 0.88 1.362 3.89 2.42 0.1 0.88 1.364 3.505 2.71 0.1 0.49 1.46 6 2.71 0.1 0.49 1.23 3.39 2.71 0.39 0.1 1.32 3.47 2.71 0.39 0.1 1.32 - - - - -7 2.71 0.1 0.49 1.23 3.11 2.71 0.39 0.1 1.31 3.65 2.71 0.39 0.1 1.31 - - - - -8 2.71 0.1 0.49 1.23 3.37 2.71 0.1 0.88 1.32 3.76 2.71 0.39 0.1 1.33 3.75 2.71 0.39 0.1 1.33 9 2.71 0.1 0.49 1.23 3.12 2.71 0.39 0.1 1.34 3.24 2.71 0.39 0.1 1.344 3.81 2.71 0.39 0.1 1.35 
Table 20: Humanoid 3, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 ψ3 1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 ψ3 2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 ψ3 3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 ψ3 4 Jπ3 
T4 
0 14.41 0.59 0.1 6.88 15.37 14.41 0.59 0.1 6.88 - - - - - - - - - -1 14.41 0.59 0.1 6.88 8.19 14.41 0.59 0.1 6.88 - - - - - - - - - -2 14.41 0.59 0.1 6.88 14.05 12.82 1.57 0.1 8.41 12.02 12.82 1.57 0.1 8.41 - - - - -3 14.41 0.59 0.1 6.88 14.18 14.41 0.59 0.1 7.41 8.23 14.41 0.59 0.1 7.41 - - - - -4 14.41 0.59 0.1 6.88 13.42 14.41 0.59 0.1 6.88 - - - - - - - - - -5 14.41 0.59 0.1 6.88 10.43 14.41 0.59 0.1 6.88 - - - - - - - - - -6 14.41 0.59 0.1 6.88 11.38 14.41 0.59 0.1 7.10 13.39 14.41 0.59 0.1 7.10 - - - - -7 14.41 0.59 0.1 6.88 12.78 14.41 0.59 0.1 7.10 11.86 14.41 0.59 0.1 7.10 - - - - -8 14.41 0.59 0.1 6.88 13.20 14.41 2.06 0.1 7.171 9.27 14.41 2.06 0.1 7.171 - - - - -9 14.41 0.59 0.1 6.88 15.43 14.41 2.06 0.1 7.175 14.37 14.41 2.06 0.1 7.175 - - - - -
27
Table 21: Walker 3, worst parameters search for each iteration over 10 seeds. 
ψ0 1 ψ1 
1 ψ3 1 Jπ0 
T1 Jπ1 
T1 ψ0 2 ψ1 
2 ψ3 2 Jπ1 
T2 Jπ2 
T2 ψ0 3 ψ1 
3 ψ3 3 Jπ2 
T3 Jπ3 
T3 ψ0 4 ψ1 
4 ψ3 4 Jπ3 
T4 
0 3.22 4.02 0.1 3.92 4.84 3.22 4.02 0.1 3.92 - - - - - - - - - -1 3.22 4.02 0.1 3.92 5.14 2.05 3.53 0.69 4.28 4.44 2.05 3.53 0.69 4.28 - - - - -2 3.22 4.02 0.1 3.92 5.36 3.22 4.02 0.1 3.92 - - - - - - - - - -3 3.22 4.02 0.1 3.92 4.60 3.22 2.55 0.1 4.21 4.75 3.22 2.55 0.1 4.21 - - - - -4 3.22 4.02 0.1 3.92 5.24 2.05 3.53 0.69 4.287 4.49 2.05 3.53 0.69 4.287 - - - - -5 3.22 4.02 0.1 3.92 3.16 2.05 3.53 0.69 4.28 3.3 2.05 3.53 0.69 4.28 - - - - -6 3.22 4.02 0.1 3.92 4.87 2.44 4.02 0.1 4.06 4.21 3.22 2.55 0.1 4.61 4.42 3.22 2.55 0.1 4.61 7 3.22 4.02 0.1 3.92 4.70 3.61 0.1 0.1 4.45 5.92 3.61 0.1 0.1 4.45 - - - - -8 3.22 4.02 0.1 3.92 5.91 3.61 0.1 0.1 4.19 5.97 3.61 0.1 0.1 4.19 - - - - -9 3.22 4.02 0.1 3.92 3.51 3.61 0.1 0.1 4.29 4.23 3.61 0.1 0.1 4.29 - - - - -
Figure 4: Counting how many policies are valid in each state, in Hopper 3 
should be taken with a grain of salt. Yet, it is legitimate to wonder whether one can analyse the time complexity of IWOCS versus RVI. One iteration of IWOCS in discrete state and action spaces, as presented in Section 4, has the complexity of VI for the policy search part, plus the complexity of finding a worst case transition function in an sa-rectangular uncertainty set, which is OpcnSnAq. Hence, the overall complexity for M iterations of IWOCS is OpMpn2SnA logp1{ϵq{ logp1´γq`cnSnAqq. Compared to RVI (depending on M which we cannot easily quantify), this bound will be smaller when c is large, which is the case when one deals with complex uncertainty sets and without further hypotheses. 
This short discussion provides a rationale to why IWOCS might be a time-efficient algorithm in large scale robust RL problems. 
P On the variance of the domain randomization policy Domain randomization on the full uncertainty set yields policies with a very large span of worst-case scores from one random seed to the other (Table 22). In other words, DR provides policies with a very large variance in worst-case performance. In turn, running a separate DR training for each seed of IWOCS induces a large variance on scores across seeds from the first iteration. IWOCS still 
28
converges, but this variance is carried through the iterations. For the sake of completeness, Table 23 report the scores of IWOCS and IWOCS* with a varying starting policy which is issued from the (very noisy) DR optimization process. Interestingly, even with these very noisy policies, IWOCS still outperforms other algorithms on average across environments. However the variance of obtained scores is quite high. The columns of Table 23 should be compared with those of Table 1 in the main text of the paper, showing that variance in IWOCS’ performance with variables DR initial policy is mostly due to the large variance in DR’s initial policies. 
Environment Jπ0 
T1 
Ant 2 ´0.43 ˘ 0.96 Ant 3 ´0.32 ˘ 0.50 HalfCheetah 2 0.66 ˘ 0.30 HalfCheetah 3 0.41 ˘ 0.11 Hopper 2 1.78 ˘ 2.16 Hopper 3 2.33 ˘ 1.44 HumanoidStandup 2 0.51 ˘ 0.50 HumanoidStandup 3 0.45 ˘ 0.89 InvertedPendulum 2 2.32 ˘ 0.42 Walker 2 1.06 ˘ 0.29 Walker 3 1.74 ˘ 0.40 Aggregated 0.96 ˘ 0.72 
Table 22: Worst-case score distribution of π0 trained with DR on each environment. 
Table 23: Avg. of normalized worst-case performance over 10 seed for IWOCS* and IWOCS without fixed initial policy 
Environment IWOCS* without fixed π0 IWOCS without fixed π0 Ant 2 0.12 ˘ 0.81 ´0.27 ˘ 0.44 Ant 3 0.19 ˘ 0.52 0.43 ˘ 0.68 HalfCheetah 2 0.72 ˘ 0.31 0.75 ˘ 0.28 HalfCheetah 3 0.51 ˘ 0.18 0.56 ˘ 0.15 Hopper 2 5.41 ˘ 1.15 6.34 ˘ 0.11 Hopper 3 4.34 ˘ 0.32 4.64 ˘ 0.16 HumanoidStandup 2 0.69 ˘ 0.30 0.98 ˘ 0.25 HumanoidStandup 3 0.86 ˘ 0.72 1.12 ˘ 0.21 InvertedPendulum 2 2.82 ˘ 0.00 2.82 ˘ 0.00 Walker 2 1.14 ˘ 0.30 1.23 ˘ 0.10 Walker 3 1.90 ˘ 0.42 2.10 ˘ 0.50 
Aggregated 1.7 ˘ 0.46 1.88 ˘ 0.26 
29
Q Impact statement This paper presents work whose goal is to advance the field of reinforcement learning. It tackles generic mathematical and computational challenges, which might have potential societal and technological consequences, none of which we feel must be specifically highlighted here. 
R Limitations The IWOCS algorithm assumes that all transition kernels in the uncertainty set T are known during training. In real-world applications, obtaining such detailed information is not always feasible. This reliance on precise uncertainty set knowledge limits the practical usage of our algorithms in some cases. 
Another limitation of the Deep IWOCS algorithm is the need for hand-tuning or grid-search for the threshold ρ. A promising approach is using a variance network to detect non-valid value functions automatically. We plan to work on this for future developments. 
30