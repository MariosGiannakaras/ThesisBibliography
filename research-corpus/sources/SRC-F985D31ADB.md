> Source: https://arxiv.org/pdf/2305.19004

POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS WITH NON-RECTANGULAR UNCERTAINTY SETS 
MENGMENG LI∗, DANIEL KUHN∗, AND TOBIAS SUTTER† 
Abstract. We propose policy gradient algorithms for robust infinite-horizon Markov decision processes (MDPs) with non-rectangular uncertainty sets, thereby addressing an open challenge in the robust MDP literature. Indeed, uncertainty sets that display statistical optimality properties and make optimal use of limited data often fail to be rectangular. Unfortunately, the corresponding robust MDPs cannot be solved with dynamic programming techniques and are in fact provably intractable. We first present a randomized projected Langevin dynamics algorithm that solves the robust policy evaluation problem to global optimality but is inefficient. We also propose a deterministic policy gradient method that is efficient but solves the robust policy evaluation problem only approximately, and we prove that the approximation error scales with a new measure of non-rectangularity of the uncertainty set. Finally, we describe an actor-critic algorithm that finds an ϵ-optimal solution for the robust policy improvement problem in O(1/ϵ4) iterations. We thus present the first complete solution scheme for robust MDPs with non-rectangular uncertainty sets offering global optimality guarantees. Numerical experiments show that our algorithms compare favorably against state-of-the-art methods. 
Key words. Robust Markov decision processes, Policy gradient, Non-rectangular uncertainty sets 
MSC codes. 90C17, 90C26 
1. Introduction. Markov decision processes (MDPs) form the backbone of reinforcement learning and dynamic decision-making [6, 39, 46, 37]. Classical MDPs operate in a time-invariant stochastic environment represented by a known constant transition kernel. In most applications, however, the transition kernel is only indirectly observable through a state-action trajectory generated under a fixed policy. In addition, it may even change over time. Uncertain and non-stationary transition kernels are routinely encountered, for example, in finance, healthcare or robotics etc. [18, 44, 52]. In these applications it is thus expedient to work with robust MDPs [38, 57, 58], which assume that the unknown true transition kernel falls within a known uncertainty set and aim to identify a policy that exhibits the best performance under the worst-case transition kernel in this uncertainty set. Optimal policies of robust MDPs display a favorable out-of-sample performance when the transition kernel must be estimated from scarce data or changes over time [36, 53]. Robust MDPs are also popular in machine learning—particularly in inverse reinforcement learning with expert demonstrations or in offline reinforcement learning with time-varying environments [12, 51, 50, 11]. 
The literature on robust MDPs distinguishes rectangular and non-rectangular uncertainty sets. An uncertainty set is called (s)-rectangular (or (s, a)-rectangular) if it is representable as a Cartesian product of separate uncertainty sets for the transition probabilities associated with the different current states s (or current state-action pairs (s, a)). Otherwise, the uncertainty set is called non-rectangular. Rectangularity is intimately related to computational tractability. Indeed, robust MDPs with rectangular polyhedral uncertainty sets can be solved in polynomial time, whereas robust MDPs with non-rectangular polyhedral uncertainty sets are NP-hard [58]. Most existing papers on robust MDPs focus on rectangular uncertainty sets. However, statistically optimal uncertainty sets often fail to be rectangular. Indeed, classical Cramér-Rao bounds imply that non-rectangular ellipsoidal uncertainty sets around the maximum likelihood estimator of the transition kernel constitute—in an asymptotic sense—the 
∗Risk Analytics and Optimization Chair, EPFL, 1015 Lausanne, Switzerland (mengmeng.li@epfl.ch, daniel.kuhn@epfl.ch). 
†Department of Economics, University of St.Gallen, 9000 St. Gallen, Switzerland (to-bias.sutter@unisg.ch). 
1 
 
 
 
 
 
 
 
 
 
 
 
2 M. LI, D. KUHN, AND T. SUTTER 
smallest possible confidence sets for the ground truth transition kernel (see [58, § 5] and Appendix A). Results from large deviations theory further imply that non-rectangular conditional relative entropy uncertainty sets lead to polices that display an optimal trade-off between in-sample performance and out-of-sample disappointment [45, 29]. 
Robust MDPs with rectangular uncertainty sets are usually addressed with value iteration, policy iteration, convex reformulation, or policy gradient methods. Value iteration constructs a sequence of increasingly accurate estimates for the value function of the optimal policy by iterating the robust Bellman operator [24, 38, 58], whereas policy iteration computes a sequence of increasingly optimal policies by iteratively computing the value function of the current policy and updating it greedily [24, 58]. The convex reformulation method is reminiscent of the linear programming approach for non-robust MDPs [22]. It uses an exponential change of variables to construct a convex optimization problem whose solution coincides with the fixed point of an entropyregularized robust Bellman operator [21]. Policy gradient methods, finally, construct a sequence of increasingly optimal policies by locally updating the current policy along the policy gradient of the value function [53]. Value iteration methods enjoy linear convergence and are thus theoretically faster than most known policy gradient methods, which are only guaranteed to display sublinear convergence. However, evaluating the robust Bellman operator can be costly, and value iteration methods can be slower than policy gradient methods for large state and action spaces [53]. This observation has spurred significant interest in gradient-based methods. A policy gradient method tailored to robust MDPs with specially structured (s, a)-rectangular uncertainty sets is described in [56], while a policy mirror descent algorithm that can handle general (s, a)-rectangular uncertainty sets is developed in [31]. In addition, there exists a projected policy gradient method for robust MDPs with s-rectangular uncertainty sets [53, 54]. While this paper was under review, it has been discovered that policy gradient methods for the robust policy evaluation problem can in fact achieve linear convergence [30]. We emphasize that the convergence guarantees of all reviewed solution methods for robust MDPs critically exploit a robust version of Bellman’s optimality principle, which ceases to hold for non-rectangular uncertainty sets [20]. 
To make things worse, the solution methods described above become inefficient or converge to strictly suboptimal solutions of the robust MDP if the uncertainty set fails to be rectangular. For example, value iteration outputs the optimal value function corresponding to the s-rectangular hull of the uncertainty set. This function provides only an upper bound on the sought value function if the uncertainty set is non-rectangular [58, Proposition 3.6]. The corresponding optimal policy is therefore over-conservative and may perform poorly in out-of-sample tests [58, § 6]. Policy iteration, on the other hand, is computationally excruciating because the robust policy evaluation subroutine is already NP-hard [58, Theorem 1]. However, there exists an efficient approximate policy iteration scheme based on ideas from robust optimization [58]. This scheme characterizes the value function of any given policy as the solution of an adjustable robust optimization problem, which can be solved approximately but efficiently in linear decision rules. However, the decision rule approximation is accurate only for small uncertainty sets. A Frank-Wolfe policy gradient method for robust policy evaluation with a non-rectangular conditional relative entropy uncertainty set is described in [29]. However, this method is only guaranteed to find a stationary point. A projected policy gradient method for robust MDPs with generic convex uncertainty sets is proposed in [53]. However, its convergence proof assumes access to a robust policy evaluation oracle. Yet no such oracle is provided. In addition, its convergence proof differs methodologically from ours in that it expresses
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 3 
the subgradients of the worst-case net present cost as convex combinations of value function gradients evaluated at finitely many worst-case transition kernels. In contrast, we approximate the subgradients at non-differentiable points by sequences of gradients at nearby differentiable points. By focusing on a single worst-case kernel rather than relying on convex combinations, our proof is thus arguably more transparent and more directly reveals the essential gradient dominance property. 
The main contributions of our paper can be summarized as follows. 1. We show that robust policy evaluation problems with non-rectangular un-
certainty sets can be solved to global optimality with a projected Langevin dynamics algorithm. Numerical results suggest that if the uncertainty set happens to be rectangular, then this randomized algorithm is competitive with state-of-the-art deterministic first-order methods in terms of runtime. 
2. We present a Frank-Wolfe algorithm that solves robust policy evaluation problems approximately. The approximation error is shown to scale with a new measure of non-rectangularity of the uncertainty set. We prove that the same method solves robust policy evaluation problems with rectangular uncertainty sets to any accuracy ϵ > 0 in O(S2/ϵ2) iterations, where S denotes the number of states. In contrast, the iteration complexity of the state-of-the-art policy gradient method for this problem class developed in [53] includes an extra factor S3A, where A denotes the number of actions. 
3. We present an actor-critic method that solves robust policy improvement problems with non-rectangular uncertainty sets to any accuracy ϵ > 0 in O(1/ϵ4) iterations. This is the first complete solution scheme for robust MDPs with non-rectangular uncertainty sets offering global optimality guarantees. A similar projected gradient descent algorithm with an approximate robust policy evaluation oracle is described in [53]. However, the policy evaluation oracle is not made explicit for general non-rectangular uncertainty sets. We also analyze the convergence properties of our actor-critic method when the robust policy evaluation oracle can only be solved up to a fixed accuracy. 
Our theoretical contributions critically rely on celebrated results in approximate dynamic programming and multi-agent reinforcement learning. Specifically, we adapt a policy iteration algorithm for non-robust MDPs described in [25] to solve robust policy evaluation problems. In addition, the convergence analysis of our actor-critic algorithm for robust policy improvement exploits a gradient dominance result originally developed for multi-agent reinforcement learning problems with a fixed transition kernel and adapts it to single-agent MDPs with an uncertain transition kernel. 
We remark that if the uncertainty set of the transition kernel is non-rectangular, then the corresponding robust MDP fails to be time consistent [35, 42, 43]. Thus, it satisfies no Bellman-type equation and cannot be addressed with dynamic programming. Even though alternative optimality criteria are discussed in [10, 28, 59], robust MDPs with general non-rectangular ambiguity sets remain unsolved to date. 
Notation. We use ∆(S) = {p ∈ R∣S∣ + ∶ ∑s∈S p(s) = 1} as a shorthand for the 
probability simplex over a finite set S. Random variables are denoted by capital letters (e.g., X) and their realizations by the corresponding lowercase letters (e.g., x). For any i, j ∈ N, the Kronecker delta is defined through δij = 1 if i = j, and δij = 0 otherwise. We say that a function f ∶ X → R is ℓ-weakly convex for some ℓ ≥ 0 if f̃(x) = f(x) + ℓ∥x∥22/2 is convex. In this case, the subdifferential ∂f of f is defined as ∂f(x) = ∂f̃(x) − {ℓx}. In addition, we say that f is ℓ-smooth for some ℓ ≥ 0 if it is continuously differentiable and if ∥∇f(x) −∇f(x′)∥2 ≤ ℓ∥x − x′∥2 for all x,x′ ∈ X . The
4 M. LI, D. KUHN, AND T. SUTTER 
Frobenious norm of a matrix M ∈ Rm×n is defined as ∥M∥F = (∑m i=1∑ 
n j=1M 
2 ij) 
1/2. 2. Rectangular and Non-rectangular Uncertainty Sets. Consider an MDP 
given by a five-tuple (S,A, P, c, ρ) comprising a finite state space S = {1, . . . , S}, a finite action space A = {1, . . . ,A}, a transition kernel P ∶ S ×A → ∆(S), a cost-per-stage function c ∶ S ×A→ R, and an initial distribution ρ ∈∆(S). Note that (S,A, P, c, ρ) describes a controlled discrete-time stochastic system, where the state at time t and the action applied at time t are denoted as random variables St and At, respectively. If the system is in state st ∈ S at time t and action at ∈ A is applied, then an immediate cost c(st, at) is incurred, and the system moves to state st+1 at time t + 1 with probability P (st+1∣st, at). Actions are chosen according to a policy that prescribes a random action at time t depending on the state history up to time t and the action history up to time t − 1. Throughout the rest of the paper, we restrict attention to stationary policies, which are described by a stochastic kernel π ∈ Π =∆(A)S , that is, π(at∣st) denotes the probability of choosing action at if the current state is st. Unless otherwise stated, we assume without loss of generality that c(s, a) ∈ [0, 1] for all s ∈ S and a ∈ A. 
Given a stationary policy π, there exists a unique probability measure PP π defined 
on the canonical sample space Ω = (S ×A)∞ equipped with its power set σ-algebra F = 2Ω such that PP 
π (S0 = s0) = ρ(s0) for every s0 ∈ S, while PP π (St = st∣St−1 = st−1,At−1 = at−1, . . . , S0 = s0,A0 = a0) = P (st∣st−1, at−1)(2.1a) 
and PP π (At = at∣St = st, . . . , S0 = s0,A0 = a0) = π(at∣st)(2.1b) 
for all s1, . . . , st ∈ S, a0, . . . , at ∈ A, and t ∈ N. We denote the expectation operator with respect to PP 
π by EP π [⋅]. One readily verifies that the stochastic process {St} 
∞ 
t=0 
represents a time-homogeneous Markov chain under PP π with transition probabilities 
PP π (St+1 = s′∣St = s) = ∑a∈A P (s′∣s, a)π(a∣s). Throughout this paper, we assess the 
desirability of a policy by its expected net present cost with respect to a prescribed discount factor γ ∈ (0,1). 
Definition 2.1 (Value function). The value function V P π ∈ RS corresponding to a 
transition kernel P and a stationary policy π is defined through 
V P π (s) = E 
P π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s] . 
One can show that V P π (s) constitutes a continuous, rational function of P and π [39, 
Appendix A]. The policy evaluation problem consists in evaluating the value function V P 
π (s) for a fixed policy π and initial state s, whereas the policy improvement problem seeks a policy that solves minπ∈Π V P 
π (s). In this paper, we are interested in robust MDPs. We thus assume that the 
transition kernel P is only known to belong to an uncertainty set P ⊆∆(S)S×A, and we assess the desirability of a policy by its worst-case expected net present cost. 
Definition 2.2 (Worst-case value function). The worst-case value function V ⋆π ∈ RS associated with a given policy π and an uncertainty set P is defined through (2.2) V ⋆π (s) =max 
P ∈P V P π (s). 
The robust policy evaluation problem then consists in evaluating the worst-case value function V ⋆π (s) for a fixed policy π and initial state s, and the robust policy improvement problem aims to solve 
min π∈Π 
max P ∈P 
V P π (s).(2.3) 
The structure of the uncertainty set P largely determines the difficulty of solving
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 5 
the robust policy evaluation and improvement problems. These problems become relatively easy if the uncertainty set is rectangular. 
Definition 2.3 (Rectangular uncertainty sets). A set P ⊆ ∆(S)S×A of transition matrices is called (i) (s, a)-rectangular [24] if P =∏(s,a)∈S×APs,a for some Ps,a ⊆∆(S), (s, a) ∈ S ×A; (ii) s-rectangular [27] if P =∏s∈S Ps for some Ps ⊆∆(S) 
A, s ∈ S. 
There is also an alternative notion of rectangularity, known as r-rectangularity [18], which models the transition kernel as a linear function of an uncertain factor matrix. We will not study r-rectangular uncertainty sets in the remainder. From now on, we call an uncertainty set P ⊆ ∆(S)S×A non-rectangular if it is neither (s, a)-rectangular nor s-rectangular (nor r-rectangular). As the probability simplex and thus also P has an empty interior, we employ a reparametrization to represent P as the image of a solid parameter set Ξ. Specifically, we assume that there exists an affine function P ξ 
that maps a solid parameter set Ξ ⊆ Rq to ∆(S)S×A such that P = {P ξ ∶ ξ ∈ Ξ}. This reparametrization may lead to a dimensionality reduction as it allows us to account for structural knowledge about the uncertainty set (e.g., it may be known that certain transitions are impossible or that some transitions have the same probabilities). This reparametrization will also help us to establish algorithmic guarantees in Section 3. 
If P is rectangular, then the robust policy improvement problem (2.3) can be solved in polynomial time using robust value iteration. 
Theorem 2.4 (Complexity of robust policy improvement with s-rectangular uncertainty sets [58, Corollary 3]). If the parameter set Ξ ⊆ Rq is representable through J linear and convex quadratic constraints, and if Ξ induces an s-rectangular uncertainty set P, then an ϵ-optimal solution to the robust policy improvement problem (2.3) can be computed in polynomial time O((q +A+J)1/2(qJ +A)3S log2(1/ϵ)+ qAS2 log(1/ϵ)). 
If the uncertainty set P fails to be rectangular, on the other hand, then the robust policy evaluation problem is strongly NP-hard even if P is a convex polyhedron. 
Theorem 2.5 (Hardness of robust policy evaluation with non-rectangular uncertainty sets [58, Theorem 1]). Deciding whether the worst-case value function (2.2) over a non-rectangular polyhedral uncertainty set P exceeds a given value α is strongly NP-hard for any stationary policy π. 
Theorem 2.5 implies that, unless P=NP, there exists no algorithm for computing an ϵ-optimal solution of the robust policy evaluation problem (2.2) with a non-rectangular uncertainty set in time polynomial in the input size and log(1/ϵ). Thus, the best we can realistically hope for is to develop methods that have a runtime polynomial in 1/ϵ. 
3. Robust Policy Evaluation. Throughout this section we fix a policy π ∈ Π and a convex and compact parameter set Ξ that induces an uncertainty set P = {P ξ ∶ ξ ∈ Ξ}. Our aim is to solve the robust policy evaluation problem (2.2) to global optimality. The following definitions are needed throughout the paper. 
Definition 3.1 (Action-value function). The action-value function QP π ∈ RS×A 
corresponding to a transition kernel P and a stationary policy π is defined through 
QP π (s, a) = E 
P π [ 
∞ 
∑ t=0 
γtc(St,At)∣S0 = s,A0 = a] . 
Definition 3.2 (Action-next-state value function). The action-next-state value function GP 
π ∈ RS×A×S corresponding to a transition kernel P and a stationary policy π
6 M. LI, D. KUHN, AND T. SUTTER 
is defined through 
GP π (s, a, s 
′ ) = EP 
π [ ∞ 
∑ t=0 
γtc(St,At)∣S0 = s,A0 = a,S1 = s ′ ] . 
Definition 3.3 (Discounted state visitation distribution). (i) The discounted state visitation distribution dPπ ∈ ∆(S) 
S corresponding to a transition kernel P , a stationary policy π, and an initial state s0 is defined through 
dPπ (s∣s0) = (1 − γ) ∞ 
∑ t=0 
γtPP π (St = s∣S0 = s0) . 
(ii) The discounted state-action visitation distribution µP π ∈ ∆(S ×A) 
S×A corresponding to a transition kernel P and an initial state-action pair (s0, a0) is defined through 
µP π (s, a∣s0, a0) = (1 − γ) 
∞ 
∑ t=0 
γtPP π (St = s,At = a∣S0 = s0,A0 = a0) . 
Lemma B.1 in the appendix shows that the value functions V P π ,QP 
π , and GP π are 
related through several linear equations, which imply the Bellman equation for V P π . 
One can use these equations to express V P π ,QP 
π , and GP π as explicit rational functions 
of π and P. These functions are well-defined on dense subsets of RA×S and RS×S×A and, in particular, on open neighborhoods of the physically meaningful domains ∆(A)S 
and ∆(S)S×A. In the following, we can thus assume that the functions V P π ,QP 
π , and GP 
π extend to open sets containing ∆(A)S and ∆(S)S×A. This implies in particular that the gradients of these functions with respect to π and P are well-defined. 
Remark 3.4 (Analytical formula for V P π ). One can show that dPπ (s∣s0) is the 
(s0, s)-th entry of the matrix (1−γ)(I−γPπ) −1, where Pπ(s, s 
′) = ∑a∈A π(a∣s)P (s′∣s, a). If we set rπ(s) = ∑a∈A π(a∣s)r(s, a), then V P 
π = (I − γPπ) −1rπ by [39, Theorem 6.1.1]. 
A robust MDP can be viewed as a zero-sum game between the decision maker, who selects the policy π, and an adversary, who chooses the transition kernel P ξ. In this view, the parameter ξ encodes the adversary’s policy. Adopting a similar reasoning as in [47, Theorem 1], we can thus derive an explicit formula for the gradient of the value function with respect to the adversary’s policy parameter ξ. 
Lemma 3.5 (Adversary’s policy gradient). For any ξ ∈ Ξ and s0 ∈ S, we have 
∇ξV P ξ 
π (s0) = 1 
1 − γ ∑ 
s,s′∈S,a,a0∈A 
π(a0∣s0)µ P ξ 
π (s, a∣s0, a0)G P ξ 
π (s, a, s ′ )∇ξP 
ξ (s′∣s, a). 
Proof of Lemma 3.5. By Lemma B.1(i) and the chain rule we have 
∇ξV P ξ 
π (s0) = ∑ s,s′∈S,a,a0∈A 
π(a0∣s0) ∂QP 
π (s0, a0) 
∂P (s′∣s, a) ∣ P=P ξ 
∇ξP ξ (s′∣s, a).(3.1) 
Thus, it remains to find an explicit formula for the derivative of the action-value function QP 
π with respect to the transition kernel P . A direct calculation reveals that ∂QP 
π (s0, a0) 
∂P (s′∣s, a) = 
∂ 
∂P (s′∣s, a) ∑ s1∈S 
P (s1∣s0, a0)G P π (s0, a0, s1) 
= ∑ s1∈S 
[ ∂P (s1∣s0, a0) 
∂P (s′∣s, a) GP 
π (s0, a0, s1) + P (s1∣s0, a0) ∂GP 
π (s0, a0, s1) 
∂P (s′∣s, a) ] 
= δss0δaa0G P π (s, a, s 
′ ) + ∑ 
s1∈S 
P (s1∣s0, a0) 
∂ 
∂P (s′∣s, a) 
⎡ ⎢ ⎢ ⎢ ⎣ c(s0, a0) + γ ∑ 
a1∈A 
π(a1∣s1)Q P π (s1, a1) 
⎤ ⎥ ⎥ ⎥ ⎦
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 7 
= δss0δaa0G P π (s, a, s 
′ ) + γ ∑ 
s1∈S,a1∈A 
P (s1∣s0, a0)π(a1∣s1) ∂QP 
π (s1, a1) 
∂P (s′∣s, a) 
= δss0δaa0G P π (s, a, s 
′ ) 
+ γ ∑ s1∈S,a1∈A 
PP π (S1 = s1,A1 = a1∣S0 = s0,A0 = a0) 
∂QP π (s1, a1) 
∂P (s′∣s, a) ,(3.2) 
where the first and third equalities use Lemmas B.1(ii) and B.1(iii), respectively. The last equality follows from the defining properties (2.1a) and (2.1b) of PP 
π . Repeating the above reasoning for the state-action pair (st, at) instead of (s0, a0) yields ∂QP 
π (st, at) 
∂P (s′∣s, a) = δsstδaatG 
P π (s, a, s 
′ ) 
+ γ ∑ st+1∈S,at+1∈A 
PP π (St+1 = st+1,At+1 = at+1∣St = st,At = at) 
∂QP π (st+1, at+1) 
∂P (s′∣s, a) . 
Substituting the above expression for t = 1 into (3.2) and recalling that {(St,At)} ∞ 
t=0 
constitutes a Markov chain under PP π yields 
∂QP π (s0, a0) 
∂P (s′∣s, a) = δss0δaa0G 
P π (s, a, s 
′ ) + γPP 
π (S1 = s,A1 = a∣S0 = s0,A0 = a0)G P π (s, a, s 
′ ) 
+ γ2 ∑ 
s2∈S,a2∈A 
PP π (S2 = s2,A2 = a2∣S0 = s0,A0 = a0) 
∂QP π (s2, a2) 
∂P (s′∣s, a) 
= γ0PP π (S0 = s,A0 = a ∣ S0 = s0,A0 = a0)G 
P π (s, a, s 
′ ) 
+ γ1PP π (S1 = s,A1 = a ∣ S0 = s0,A0 = a0)G 
P π (s, a, s 
′ ) 
+ γ2 ∑ 
s2∈S,a2∈A 
PP π (S2 = s2,A2 = a2∣S0 = s0,A0 = a0) 
∂QP π (s2, a2) 
∂P (s′∣s, a) . 
Iteratively reformulating ∂QP π (st, at)/∂P (s 
′∣s, a) for t = 2,3, . . ., we finally obtain ∂QP 
π (s0, a0) 
∂P (s′∣s, a) = ∞ 
∑ t=0 
γtPP π (St = s,At = a ∣ S0 = s0,A0 = a0)G 
P π (s, a, s 
′ ) 
= 1 
1 − γ µP π (s, a∣s0, a0)G 
P π (s, a, s 
′ ), 
where the last equality exploits the definition of the discounted state visitation distribution. The claim then follows by substituting the above expression into (3.1). 
Lemma 3.5 is a key ingredient for two complementary algorithms for solving the robust policy evaluation problem (2.2) with a non-rectangular uncertainty set. Section 3.1 first develops a Markov chain Monte Carlo method for solving (2.2) exactly. Next, Sec-tion 3.2 develops a more efficient Frank-Wolfe method for solving (2.2) approximately. Throughout the two sections we fix an initial state s0 ∈ S. 
3.1. Projected Langevin Dynamics. We now develop a Markov Chain Monte Carlo method to solve the robust policy evaluation problem (2.2) to global optimality and derive its convergence rate in expectation. To this end, we assume throughout this section that Ξ ⊆ Rq is a compact convex body, and we consider the problem of sampling from the Gibbs distribution 
νβ(dξ) = exp (βV P ξ 
π (s0)) 
∫ Ξ exp (βV P ξ′ 
π (s0))dξ ′ 
dξ,
8 M. LI, D. KUHN, AND T. SUTTER 
where β > 1 represents the inverse temperature. Note that the denominator is finite because Ξ is compact and V P ξ 
π (s0) is continuous in ξ. Indeed, V P π (s0) is continuous 
in P [39, Appendix A], and P ξ is affine in ξ. Sampling from the Gibbs distribution νβ is of interest because the robust policy evaluation problem (2.2) is equivalent to 
V ⋆π (s0) =max ξ∈Ξ 
V P ξ 
π (s0),(3.3) 
and because νβ converges weakly to the uniform distribution on the set of global maximizers of (3.3) as β tends to infinity [23, Section 2]. We use the discrete-time counterpart of the Langevin diffusion [40] to generate samples that are (approximately) governed by the Gibbs distribution νβ , see Algorithm 3.1. In each iteration m ∈ Z+, Algorithm 3.1 first uses Lemma 3.5 to compute the adversary’s policy gradient ∇ξV 
P ξ 
π (s0) at the current iterate ξ = ξ(m), perturbs it by adding Gaussian noise, and then applies a projected gradient step to find the next iterate ξ(m+1). After M iterations, Algorithm 3.1 outputs a random iterate ξ(M) whose distribution νM approximates νβ in the 1-Wasserstein distance [26, Theorem 1]. 
Algorithm 3.1 Projected Langevin dynamics for solving the robust policy evaluation problem (2.2) 
Require: Initial iterate ξ(0) ∈ Ξ, Gibbs parameter β > 1, stepsize η > 0, iteration number M ∈ N 
1: for m = 0, . . . ,M − 1 do 2: Sample wm+1 ∼ N (0, Iq) 
3: Find ξ(m+1) = ProjΞ (ξ (m) + η∇ξ V 
P ξ 
π (s0)∣ ξ=ξ(m) 
+ √ 2η/βwm+1) 
4: end for 
Theorem 3.6 (Convergence of Algorithm 3.1). If ϵ > 0, η < 1/2, and λ ∈ (0,1), then there exist universal constants a > 4, b > 1, and c1, c2, c3 > 0 such that for β ≥ c−11 (2q/(c1(1 − λ)ϵe)) 
1/λ and M ≥max{4, c2 exp(c3q b)/ϵa}, the distribution νM of 
the output ξ(M) of Algorithm 3.1 satisfies Eξ∼νM [V P ξ 
π (s0)] ≥ V ⋆ 
π (s0) − ϵ. 
Proof. By [53, Lemma 4], there exists a constant L > 0 such that the objective function V P ξ 
π (s0) of problem (3.3) is L-smooth in ξ. In addition, Ξ is a convex body. The claim thus follows from [26, Proposition 3]. 
Theorem 3.6 shows that the number of iterations M needed by Algorithm 3.1 to compute an ϵ-optimal solution for the robust policy evaluation problem (2.2) scales exponentially with the dimension q of the uncertain parameter ξ and with the number of desired accuracy digits log(1/ϵ). This is consistent with the hardness result of Theorem 2.5. Nonetheless, Algorithm 3.1 solves the robust policy evaluation problem via a simple gradient-based approach and enjoys global optimality guarantees even if the uncertainty set fails to be rectangular. 
Remark 3.7 (Implementation of Algorithm 3.1). The following modifications can improve the scalability of Algorithm 3.1 in practice. First, Algorithm 3.1 computes an exact policy gradient in every iteration, which can be costly when the state and action spaces are large. Stochastic or approximate policy gradients may be cheaper to evaluate. Fortunately, Theorem 3.6 continues to hold when stochastic instead of exact policy gradients are used provided that they are affected by sub-Gaussian noise [26, Proposition 3]. In addition, the projection onto the parameter space Ξ is computed in
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 9 
every iteration, which can be costly. As Ξ is convex, however, the Euclidean projection subroutine solves a convex program and is thus amenable to efficient general-purpose solvers that scale to high dimensions [49]. For specific non-rectangular polyhedral uncertainty sets, Euclidean balls, or ℓ1-balls, projections are available in closed form or can be computed highly efficiently with specialized methods [16, 34]. 
The concentration behavior of the discrete-time counterpart of the Langevin diffusion is generally open despite some recent results for convex objective functions [2]. We leave the study of strong concentration bounds complementing Theorem 3.6 for future research. However, by applying Markov’s inequality, we directly obtain the following probabilistic guarantee. 
Corollary 3.8 (Probabilistic suboptimality guarantee). Under the assumptions of Theorem 3.6 we have Pξ∼νM 
[V P ξ 
π (s0) > V ⋆ 
π (s0) − ϵ/δ] ≥ 1 − δ for all δ ∈ (0,1). 
3.2. Frank-Wolfe Algorithm. The robust policy evaluation problem (2.2) is challenging because the objective function V P 
π (s0) is non-concave in P. Accordingly, it is not surprising that the runtime of the Markov Chain Monte Carlo method developed in Section 3.1 scales exponentially with the dimension q of ξ. In this section we show that a stationary point of (2.2) can be found in time polynomial in q. We will also show that the suboptimality of this stationary point vis-à-vis the global maximum of (2.2) admits a tight computable estimate that depends on the degree of non-rectangularity of the uncertainty set P. To this end, we first note that problem (2.2) is susceptible to a Frank-Wolfe (FW) algorithm [17], see Algorithm 3.2. A similar FW method has been proposed to solve the policy improvement problem associated with non-robust MDPs [7]. This method is often referred to as conservative policy iteration [25]. Algorithm 3.2 can thus be also viewed as a conservative policy iteration method for robust policy evaluation problems with non-rectangular uncertainty sets. 
Algorithm 3.2 FW algorithm for solving the robust policy evaluation problem (2.2) 
Require: Initial iterate P (0) ∈ P, positive stepsizes {αm} ∞ 
m=0, tolerence ϵ > 0 1: m← 0 2: repeat 3: Find an ϵ-optimal solution Pϵ of problem (3.4) with P ′ = P (m) 
4: Update P (m+1) = (1 − αm)P (m) + αmPϵ 
5: m←m + 1 6: until ⟨∇PV 
P (m) π (s0), Pϵ − P 
(m)⟩ ≤ ϵ 7: return P̂ = P (m) 
In each iteration m ∈ Z+, Algorithm 3.2 computes an ϵ-optimal solution of the direction-finding subproblem 
max P ∈P ⟨∇PV 
P ′ π (s0), P − P 
′ ⟩,(3.4) 
which linearizes the objective function of problem (2.2) around the current iterate P ′ = P (m). The next iterate P (m+1) is constructed as a point on the line segment connecting P (m) and Pϵ. The algorithm terminates as soon as the (approximate) Frank-Wolfe gap ⟨∇PV 
P (m) π (s0), Pϵ − P 
(m)⟩ drops below the prescribed tolerance ϵ. A more explicit reformulation of the direction-finding subproblem (3.4) suitable for implementation is provided in Proposition 3.9 below. For notational convenience, we define the adversary’s advantage function as 
AP π (s, a, s 
′ ) = GP 
π (s, a, s ′ ) −QP 
π (s, a).
10 M. LI, D. KUHN, AND T. SUTTER 
It quantifies the extent to which the adversary prefers to set the next state to s′ 
instead of sampling it from P (⋅∣s, a), assuming that the future dynamics of the states and actions are determined by π and P. 
It can be shown that the direction-finding subproblem (3.4) can be equivalently expressed in terms of the adversary’s advantage function. 
Proposition 3.9 (Direction-finding subproblem). Problem (3.4) is equivalent to 1 
1 − γ max P ∈P 
∑ s∈S,a∈A 
dP ′ 
π (s∣s0)π(a∣s) ∑ s′∈S 
P (s′∣s, a)AP ′ π (s, a, s 
′ ).(3.5) 
Proof. Under the trivial embedding P ξ = ξ for ξ = P ∈ Ξ = P, nature’s policy gradient ∇ξP 
ξ(s′∣s, a) ∈ RS×S×A constitutes a tensor containing a 1 in position (s′, s, a) and zeros elsewhere. Thus, Lemma 3.5 implies that ⟨∇PV 
P ′ π (s0), P − P 
′ ⟩ 
= 1 
1 − γ ∑ 
s,s′∈S,a,a0∈A 
π(a0∣s0)µ P ′ π (s, a∣s0, a0)G 
P ′ π (s, a, s 
′ )(P (s′∣s, a) − P ′(s′∣s, a)) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
dP ′ 
π (s∣s0)π(a∣s) ∑ s′∈S (P (s′∣s, a) − P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
dP ′ 
π (s∣s0)π(a∣s) ∑ s′∈S 
P (s′∣s, a)AP ′ π (s, a, s 
′ ), 
where the second equality follows from (2.1) and the law of total probability, which implies that∑a0∈A 
π(a0∣s0)µ P ′ π (s, a∣s0, a0)=d 
P ′ π (s∣s0)π(a∣s). The last equality follows 
from Lemma B.2 in the appendix. Thus, (3.4) and (3.5) are equivalent. 
The following assumption is instrumental for the main results of this section. 
Assumption 1 (Irreducibility). The Markov chain {St} ∞ 
t=0 induced by the given policy π is irreducible for every P ∈ Ps, where Ps denotes the smallest s-rectangular uncertainty set that contains P. 
Assumption 1 ensures that, for every transition kernel P ∈ Ps, every state s′ can be reached from any other state s within a finite number of transitions. Similar assumptions are frequently adopted in the literature on robust and non-robust MDPs [58, 19]. 
In the following, we define the distribution mismatch coefficient associated with two transition kernels P,P ′ ∈ Ps as δd(P 
′, P ) =maxs∈S d P ′ π (s∣s0)/d 
P π (s∣s0), and we set 
the universal distribution mismatch coefficient to δd =maxP ′,P ∈Ps δd(P ′, P ). 
In addition, we define the degree of non-rectangularity of the uncertainty set P with respect to an anchor point P ′ ∈ P as 
δP(P ′ ) = max 
Ps∈Ps 
⟨∇PV P ′ π (s0), Ps⟩ −max 
P ∈P ⟨∇PV 
P ′ π (s0), P ⟩, 
where Ps denotes again the smallest s-rectangular uncertainty set that contains P , and we set the absolute degree of non-rectangularity of P to δP =maxP ′∈P δP(P 
′). Note that if P is s-rectangular, then Ps = P, and thus δP(P 
′) vanishes for every anchor point P ′ ∈ P, implying that δP = 0. If P is non-rectangular, however, then P ⊆ Ps, and thus δP(P 
′) is non-negative for every P ′ ∈ P. Hence, δP is non-negative, too. 
Remark 3.10 (Finiteness of δd and δP). Assumption 1 ensures that δd(P ′, P ) > 0 
for all P,P ′ ∈ P. As dP ′ 
π (s∣s0) and dPπ (s∣s0) are respectively continuous in P ′ and P for all s ∈ S, and as Ps is compact, it is clear that δd is finite and strictly positive. Similarly, as ∇PV 
P ′ π (s0) is continuous in P ′ [53, Lemma 4] while P and Ps are compact, Berge’s 
maximum theorem [4, pp. 115-116] ensures that δP(P ′) is continuous in P ′. Thus, δP
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 11 
is finite and non-negative. Note that both δd and δP depend only on P, π and s0. 
Remark 3.11 (Measures of non-rectangularity). The degree of non-rectangularity of the uncertainty set P could also be quantified by the Hausdorff distance between P and its s-rectangular hull Ps. However, this alternative non-rectangularity measure is agnostic of the value function V P 
π (s) to be maximized over P . In contrast, the proposed non-rectangularity measure δP accounts for the geometry of V P 
π (s). For example, δP vanishes even if P fails to be s-rectangular provided that V P 
π (s) is constant in P , say. Hence, δP is small not only when P closely approximates Ps but also when replacing P with Ps does not significantly change the solution of the robust policy evaluation problem (2.2). Note that δP is particularly tailored to Algorithm 3.2 because it estimates the impact of replacing P with Ps on the direction-finding subproblem (3.4). 
The following theorem uses Assumption 1 to show that the FW algorithm offers a global performance guarantee. 
Theorem 3.12 (Global performance guarantee). Suppose that Assumption 1 holds and that ϵ > 0. For every m ∈ Z+, define the approximate Frank-Wolfe gap 
Gm = ⟨∇PV P (m) π (s0), Pϵ − P 
(m) ⟩, 
where Pϵ denotes the ϵ-optimal solution of problem (3.4) computed in the m-th iteration of Algorithm 3.2, and let αm = Gm(1 − γ) 
3/(4γ2). Then, Algorithm 3.2 terminates within O(1/ϵ2) iterations, and its output P̂ satisfies V ⋆π (s0) − V 
P̂ π (s0) ≤ δd(2ϵ + δP). 
Theorem 3.12 implies that if P is s-rectangular, in which case δP = 0, then Algorithm 3.2 solves the robust policy evaluation problem (2.2) to global optimality. This insight is formalized in the next corollary. 
Corollary 3.13 (Global optimality guarantee when P is rectangular). Suppose that all assumptions of Theorem 3.12 hold and that P is s-rectangular. Then, the output P̂ of Algorithm 3.2 satisfies V ⋆π (s0) − V 
P̂ π (s0) ≤ 2δdϵ. 
Remark 3.14 (Robust policy evaluation with rectangular uncertainty sets). A policy gradient method that solves robust policy evaluation problems with s-rectangular uncertainty sets to global optimality is proposed in [53]. While displaying the same dependence on ϵ, one can show that the iteration complexity of this alternative method exceeds that of our algorithm by a factor S3A. The theoretical analysis in Section 3.2 implies that our FW algorithm requires 32γ2δ2d/(δ 
2(1 − γ)5) iterations to find a δ-optimal solution for problem (2.2). Indeed, if we set ϵ = δ/(2δd), then the output P̂ of Algorithm 3.2 satisfies V ⋆π (s0) − V 
P̂ π (s0) ≤ δ by Corollary 3.13, and the 
algorithm terminates within 32γ2δ2d/(δ 2(1 − γ)5) iterations by Lemma 3.18. Similarly, 
one can show that [53, Algorithm 2] requires 32γS3Aδ2d/(δ 2(1 − γ)4) iterations to find 
a δ-optimal solution for problem (2.2); see [53, Theorem 4.4]. Thus, the iteration complexity of [53, Algorithm 2] includes an extra factor S3A, which grows polynomially with the numbers of states and actions, but lacks a dimensionless factor γ/(1 − γ). 
Note that the iteration complexities of both methods scale with the squared distribution mismatch coefficient δ2d. As s0 follows the uniform distribution on S, the discounted state visitation distribution dPπ (s∣s0) must be averaged over s0. Hence, one can use the trivial bounds dPπ (s0∣s0) ≥ 1 − γ and dPπ (s∣s0) ≤ 1 for all s, s0 ∈ S to show that δ2d ≤ S2/(1 − γ)2. The iteration complexities of the FW algorithm and [53, Algorithm 2] can thus be expressed as explicit functions of the fundamental parameters S, A, γ and δ. In addition, the method in [53] requires an exact projection oracle onto the uncertainty set, while our FW algorithm only requires approximate solutions of the direction-finding subproblem (3.4). Our projection-free FW algorithm
12 M. LI, D. KUHN, AND T. SUTTER 
is thus preferable for non-elementary uncertainty sets. Numerical experiments suggest that the policy gradient method developed in [53] converges faster than dynamic programming methods despite its suboptimal theoretical convergence rate. 
The proof of Theorem 3.12 relies on a few preparatory results. First, we need the following variant of the celebrated performance difference lemma for non-robust MDPs [25, Lemma 6.1], which compares the performance of different transition kernels under a fixed policy π. 
Lemma 3.15 (Performance difference across transition kernels). For any P,P ′ ∈ P, π ∈ Π, and s0 ∈ S, we have 
V P π (s0) −V 
P ′ π (s0) = 
1 
1 − γ ∑ 
s∈S,a∈A 
dPπ (s∣s0)π(a∣s) ∑ s′∈S (P (s′∣s, a) −P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ). 
Proof of Lemma 3.15. For any t ∈ Z+ we have QP 
π (st, at) −Q P ′ π (st, at) 
= γ ∑ st+1∈S 
P (st+1∣st, at)(V P π (st+1) −V 
P ′ π (st+1)) 
+ γ ∑ st+1∈S 
(P (st+1∣st, at) −P ′ (st+1∣st, at))V 
P ′ π (st+1) 
= γ ∑ st+1∈S 
P (st+1∣st, at) ∑ at+1∈A 
π(at+1∣st+1)(Q P π (st+1, at+1) −Q 
P ′ π (st+1, at+1)) 
+ ∑ st+1∈S 
(P (st+1∣st, at) − P ′ (st+1∣st, at))G 
P ′ π (st, at, st+1) 
= γ ∑ st+1∈S at+1∈A 
PP π (St+1 = st+1,At+1 = at+1∣St = st,At = at)(Q 
P π (st+1, at+1) −Q 
P ′ π (st+1, at+1)) 
+ ∑ st+1∈S 
(P (st+1∣st, at) − P ′ (st+1∣st, at))G 
P ′ π (st, at, st+1), 
where the first equality follows from Lemma B.1(ii), the second equality follows from Lemmas B.1(i) and B.1(iii), and the last equality holds because of (2.1). Substituting the above equation for t = 1 into the above equation for t = 0 yields 
QP π (s0, a0) −Q 
P ′ π (s0, a0) 
= ∑ s1∈S 
(P (s1∣s0, a0) − P ′ (s1∣s0, a0))G 
P ′ π (s0, a0, s1) 
+γ ∑ s1∈S,a1∈A 
PP π (S1 = s1,A1 = a1∣S0 = s0,A0 = a0) 
∑ s2∈S 
(P (s2∣s1, a1) −P ′ (s2∣s1, a1))G 
P ′ π (s1, a1, s2) 
+ γ2 ∑ 
s2∈S,a2∈A 
PP π (S2 = s2,A2 = a2∣S0 = s0,A0 = a0)(Q 
P π (s2, a2) −Q 
P ′ π (s2, a2)). 
By iteratively expanding QP π (st, at) − QP ′ 
π (st, at) for all t ∈ N and recalling that
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 13 
γ ∈ (0,1), we then find QP 
π (s0, a0) −Q P ′ π (s0, a0) 
= ∞ 
∑ t=0 
γt ∑ 
s∈S,a∈A 
PP π (St = s,At = a∣S0 = s0,A0 = a0) 
∑ s′∈S (P (s′∣s, a) − P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
µP π (s, a∣s0, a0) ∑ 
s′∈S (P (s′∣s, a) − P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ), 
(3.6) 
where the second equality follows from the construction of µP π (s, a∣s0, a0) in Defini-
tion 3.3. By Lemma B.1(i), we finally obtain V P π (s0) − V 
P ′ π (s0) = ∑ 
a0∈A 
π(a0∣s0)(Q P π (s0, a0) −Q 
P ′ π (s0, a0)) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
dPπ (s∣s0)π(a∣s)∑ s′∈S (P (s′∣s, a) −P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ), 
where the last equality follows from (3.6) and the identity ∑a0∈A µP π (s, a∣s0, a0)π(a0∣s0) 
= dPπ (s∣s0)π(a∣s). Thus, the claim follows. 
Step 4 of Algorithm 3.2 readily implies that ∑ s′∈S ∣P (m+1)(s′∣s, a) − P (m)(s′∣s, a)∣ ≤ 2αm ∀s ∈ S, a ∈ A.(3.7) 
Thus, the difference between any two consecutive iterates of Algorithm 3.2 is bounded by twice the stepsize. The next lemma, which is inspired by [25, Theorem 4.1], translates this bound to one for the difference between the discounted state visitation frequencies corresponding to two consecutive iterates. 
Lemma 3.16 (Similarity between discounted state visitation frequencies). The iterates of Algorithm 3.2 satisfy 
∑ s∈S 
∣dP (m+1) 
π (s∣s0) − d P (m) π (s∣s0)∣ ≤ 
2αmγ 
1 − γ ∀m ∈ Z+. 
Proof of Lemma 3.16. We use ρPt ∈ ∆(S) to denote the probability mass function of St under PP 
π conditional on S0 = s0. Its dependence on π and s0 is suppressed to avoid clutter. Note first that for any t ∈ N we have 
ρP (m+1) 
t (s′) −ρP (m) 
t (s′) = ∑ s∈S,a∈A 
(ρP (m+1) 
t−1 (s)P (m+1)(s′∣s, a) −ρP (m) 
t−1 (s)P (m) (s′∣s, a))π(a∣s) 
=∑ s∈S 
ρP (m+1) 
t−1 (s) ∑ a∈A 
(P (m+1)(s′∣s, a) − P (m)(s′∣s, a))π(a∣s) 
+∑ s∈S 
(ρP (m+1) 
t−1 (s) − ρP (m) 
t−1 (s)) ∑ a∈A 
P (m)(s′∣s, a)π(a∣s) ∀s′ ∈ S. 
Taking absolute values on both sides, using the triangle inequality and summing over s′ then yields 
∥ρP (m+1) 
t − ρP (m) 
t ∥ 1 ≤∑ s∈S 
ρP (m+1) 
t−1 (s) ∑ a∈A 
π(a∣s) ∑ s′∈S ∣P (m+1)(s′∣s, a) − P (m)(s′∣s, a)∣ 
+∑ s∈S 
∣ρP (m+1) 
t−1 (s) − ρP (m) 
t−1 (s)∣ ∑ s′∈S ∑ a∈A 
P (m)(s′∣s, a)π(a∣s) 
≤2αm + ∥ρ P (m+1) t−1 − ρP 
(m) t−1 ∥ 
1 , 
where the second inequality follows from (3.7). By unfolding this recursive bound for
14 M. LI, D. KUHN, AND T. SUTTER 
all time points from t to 0 and noting that ρP (m+1) 
0 = ρP (m) 
0 , we then obtain 
∥ρP (m+1) 
t − ρP (m) 
t ∥ 1 ≤ 2tαm.(3.8) 
Next, from the definition of dPπ it is clear that 
dP (m+1) 
π (s∣s0) − d P (m) π (s∣s0) = (1 − γ) 
∞ 
∑ t=0 
γt (ρP 
(m+1) t (s) − ρP 
(m) t (s)) ∀s ∈ S. 
By (3.8), we therefore find 
∑ s∈S 
∣dP (m+1) 
π (s∣s0) − d P (m) π (s∣s0)∣ ≤ (1 − γ) 
∞ 
∑ t=0 
γt2tαm ≤ 2αmγ 
1 − γ , 
where the second inequality holds because ∑∞t=0 γ tt = γ/(1 − γ)2. 
The next lemma shows that, under the adaptive stepsize schedule of Theorem 3.12, the objective function values of the transition kernels generated by Algorithm 3.2 are non-decreasing. It is inspired by [25, Corollary 4.2]. 
Lemma 3.17 (Adversary’s policy improvement). Under the stepsize schedule of Theorem 3.12, we have V P (m+1) 
π (s0) − V P (m) π (s0) ≥ G2 
m(1 − γ) 4/(8γ2) for all m ∈ Z+. 
Proof of Lemma 3.17. Throughout the proof we use Pϵ to denote the ϵ-optimal solution of problem (3.4) that is computed in the m-th iteration of Algorithm 3.2. By Lemma 3.15, we then have 
(1 − γ)(V P (m+1) π (s0) − V 
P (m) π (s0)) 
= ∑ s∈S,a∈A 
dP (m+1) 
π (s∣s0)π(a∣s) ∑ s′∈S (P (m+1)(s′∣s, a) − P (m)(s′∣s, a))GP (m) 
π (s, a, s′) 
= ∑ s∈S,a∈A 
dP (m+1) 
π (s∣s0)π(a∣s) ∑ s′∈S 
αm(Pϵ(s ′ ∣s, a) − P (m)(s′∣s, a))GP (m) 
π (s, a, s′) 
= ∑ s∈S,a∈A 
dP (m+1) 
π (s∣s0)π(a∣s) ∑ s′∈S 
αmPϵ(s ′ ∣s, a)AP (m) 
π (s, a, s′), 
(3.9) 
where the second equality follows from the construction of P (m+1) in Algorithm 3.2, and the last equality follows from Lemma B.2. Adding and subtracting αmGm(1 − γ) on the right hand side of (3.9) and using a similar reasoning as in the proof of Proposition 3.9 to express the approximate Frank-Wolfe gap Gm in terms of the advantage function AP (m) 
π , we obtain 
(1 − γ)(V P (m+1) π (s0) − V 
P (m) π (s0)) 
= αmGm(1 − γ) + αm ∑ s∈S,a∈A 
dP (m+1) 
π (s∣s0)π(a∣s) ∑ s′∈S 
Pϵ(s ′ ∣s, a)AP (m) 
π (s, a, s′) 
− αm ∑ s∈S,a∈A 
dP (m) 
π (s∣s0)π(a∣s) ∑ s′∈S 
Pϵ(s ′ ∣s, a)AP (m) 
π (s, a, s′) 
≥ αmGm(1 − γ) − αm max s,s′∈S,a∈A,P ∈P 
∣AP π (s, a, s 
′ )∣∑ 
s∈S 
∣dP (m+1) 
π (s∣s0) − d P (m) π (s∣s0)∣ 
≥ αmGm(1 − γ) − αmγ 
1 − γ ∑ s∈S 
∣dP (m+1) 
π (s∣s0) − d P (m) π (s∣s0)∣ 
≥ αm (Gm(1 − γ) − 2αmγ2 
(1 − γ)2 ) . 
The first inequality in the above expression follows from Hölder’s inequality. Recall next that c(s, a) ∈ [0,1] for all (s, a) ∈ S × A, which implies that 0 ≤ V P 
π (s0) ≤ 
∑ ∞ 
t=0 γ t = 1/(1 − γ) for all P ∈ P. By the definition of the advantage function and by
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 15 
Lemmas B.1(ii) and B.1(iii), we then have ∣AP π (s, a, s 
′)∣ ≤ γ/(1−γ) for all s, s′ ∈ S, a ∈ A, and P ∈ P. This justifies the second inequality. The last inequality follows from Lemma 3.16. The stepsize αm = Gm(1 − γ) 
3/(4γ2) was chosen to maximize the last expression. Replacing αm by this formula yields the desired bound. 
We can now show that the proposed FW algorithm terminates within O(1/ϵ2) iterations with a Frank-Wolfe gap of at most 2ϵ. 
Lemma 3.18 (Finite termination). Under the stepsize schedule of Theorem 3.12, Algorithm 3.2 terminates within 8γ2/(ϵ2(1 − γ)5) iterations, and its output P̂ satisfies maxP ∈P⟨∇PV 
P̂ π (s0), P − P̂ ⟩ ≤ 2ϵ. 
Theorem 5 in [29] also shows that Algorithm 3.2 converges to an approximate stationary point but does not provide an explicit expression for the iteration complexity. While [29] focuses on a specific non-rectangular uncertainty set constructed from the conditional relative entropy and uses exact line search to determine the stepsize sequence, which is computationally expensive, Lemma 3.18 applies to general nonrectangular uncertainty sets and leverages an easily computable stepsize schedule. In addition, [29] assumes to have access to an exact optimizer of the direction-finding subproblem, while Lemma 3.18 only requires access to an ϵ-optimal solution. 
Proof of Lemma 3.18. Note that if Algorithm 3.2 does not terminate in iteration m, then Gm > ϵ, and hence V P (m+1) 
π (s0) ≥ V P (m) π (s0)+ϵ 
2(1−γ)4/(8γ2) by Lemma 3.17. As c(s, a) ∈ [0, 1], we have 0 ≤ V P 
π (s0) ≤ ∑ ∞ 
t=0 γ t = 1/(1−γ) for every P ∈ P . The above 
per-iteration improvement can thus only persist for at most 8γ2/(ϵ2(1−γ)5) iterations. If Algorithm 3.2 terminates in iteration m, however, then Gm ≤ ϵ, and thus we have 
max P ∈P ⟨∇PV 
P (m) π (s0), P − P 
(m) ⟩ ≤ ⟨∇PV 
P (m) π (s0), Pϵ − P 
(m) ⟩ + ϵ = Gm + ϵ ≤ 2ϵ. 
Hence, the claim follows. 
We are now ready to establish the convergence behavior of Algorithm 3.2. 
Proof of Theorem 3.12. Let P ⋆s be any maximizer of the robust policy evaluation problem (2.2) when P is replaced with the smallest s-rectangular uncertainty set Ps 
that contains P. As P ⊆ Ps, we have 
V ⋆π (s0) −V P̂ π (s0)=max 
P ∈P V P π (s0) −V 
P̂ π (s0) ≤ max 
Ps∈Ps 
V Ps π (s0) −V 
P̂ π (s0) = V 
P ⋆s π (s0) −V 
P̂ π (s0). 
This in turn implies that 
V ⋆π(s0)−V P̂ π (s0)≤ V 
P ⋆s π (s0) − V 
P̂ π (s0) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
d P ⋆s π (s∣s0)π(a∣s) ∑ 
s′∈S (P ⋆s (s 
′ ∣s, a) − P̂ (s′∣s, a))GP̂ 
π (s, a, s ′ ) 
= 1 
1 − γ ∑ 
s∈S,a∈A 
d P ⋆s π (s∣s0)π(a∣s) ∑ 
s′∈S P ⋆s (s 
′ ∣s, a)AP̂ 
π (s, a, s ′ ) 
≤ 1 
1 − γ ∑ s∈S 
d P ⋆s π (s∣s0)max 
Ps∈Ps 
∑ a∈A 
π(a∣s) ∑ s′∈S 
Ps(s ′ ∣s, a)AP̂ 
π (s, a, s ′ ) 
≤ 1 
1 − γ δd(P 
⋆ 
s , P̂ )∑ s∈S 
dP̂π (s∣s0)max Ps∈Ps 
∑ a∈A 
π(a∣s) ∑ s′∈S 
Ps(s ′ ∣s, a)AP̂ 
π (s, a, s ′ ) 
= 1 
1 − γ δd(P 
⋆ 
s , P̂ )max Ps∈Ps 
∑ s∈S 
dP̂π (s∣s0) ∑ a∈A 
π(a∣s) ∑ s′∈S 
Ps(s ′ ∣s, a)AP̂ 
π (s, a, s ′ ) 
= δd(P ⋆ 
s , P̂ )max Ps∈Ps 
⟨∇PV P̂ π (s0), Ps − P̂ ⟩,
16 M. LI, D. KUHN, AND T. SUTTER 
where the first two equalities exploit Lemma 3.15 and Lemma B.2, respectively. The third inequality follows from the definition of the distribution mismatch coefficient δd(P 
⋆ 
s , P̂ ) and from Hölder’s inequality, which applies because∑s′∈S P̂ (s ′∣s, a)AP̂ 
π (s,a,s ′) 
= 0 and hence maxPs∈Ps ∑a∈A π(a∣s)∑s′∈S P (s ′∣s, a)AP̂ 
π (s, a, s ′) ≥ 0 for all s ∈ S. The 
third equality exploits the s-rectangularity of Ps, and the last equality follows from a variant of Proposition 3.9 where P is replaced by Ps. Hence, we find 
V ⋆π (s0) − V P̂ π (s0) ≤ δd(P 
⋆ 
s , P̂ ) (max Ps∈Ps 
⟨∇PV P̂ π (s0), Ps − P̂ ⟩ −max 
P ∈P ⟨∇PV 
P̂ π (s0), P − P̂ ⟩ 
+max P ∈P ⟨∇PV 
P̂ π (s0), P − P̂ ⟩) 
≤ δd(P ⋆ 
s , P̂ )(δP(P̂ ) + 2ϵ) ≤ δd(δP + 2ϵ), 
where the second inequality holds thanks to the definition of δP(P̂ ) and Lemma 3.18. The claim finally follows because δd(P 
⋆ 
s , P̂ ) and δP(P̂ ) are trivially bounded above by δd and δP , respectively, which are independent of the output P̂ of Algorithm 3.2. 
4. Robust Policy Improvement. We now develop an actor-critic algorithm to solve the robust policy improvement problem (2.3) for a fixed initial state s0 to global optimality; see Algorithm 4.1. In each iteration k ∈ Z+, Algorithm 4.1 first computes an ϵ-optimal solution P (k) of the robust policy evaluation problem (2.2) associated with the current policy π(k) (critic) and then applies a projected gradient step to find a new policy π(k+1) that locally improves the value function associated with the current transition kernel P (k) (actor). The critic’s subproblem could be addressed with Algorithm 3.1, for example, which outputs an ϵ-optimal solution of the robust policy evaluation problem with high probability. The actor’s subproblem consists in projecting a vector onto the probability simplex Π, which can be done efficiently [55]. 
Algorithm 4.1 Actor-critic algorithm for solving the robust policy improvement problem (2.3) 
Require: Iteration number K ∈ N, stepsize η > 0, tolerance ϵ > 0 1: Initialize π(0)(a∣s) = 1/A ∀s ∈ S, a ∈ A, and set k ← 0 2: while k ≤K − 1 do 3: Critic: Find P (k) ∈ P such that V P (k) 
π(k) (s0) ≥ V ⋆ 
π(k)(s0) − ϵ 
4: Actor : π(k+1) = ProjΠ (π (k) + η∇πV 
P (k) π(k) (s0)) 
5: k ← k + 1 6: end while 
The following assumption is essential for the main results of this section. 
Assumption 2 (Irreducibility). The Markov chain {St} ∞ 
t=0 is irreducible for any P ∈ P and π ∈ Π. 
The sole purpose of Assumption 2 is to ensure that the distribution mismatch coefficient C = maxπ,π′∈Π,s∈S,P ∈P dPπ (s∣s0)/d 
P π′(s∣s0) is finite and strictly positive. This can be 
shown by using a similar reasoning as in Remark 3.10. Instead of requiring irreducibility, one could also simply require that all components of the initial state distribution ρ ∈ ∆(S) are strictly positive. However, this would imply that the initial state is random, which contradicts the standard assumption that states are observed. 
Recall now from Remark 3.4 and the surrounding discussion that V P π constitutes 
a rational function of π that is defined on a neighborhood of Π. The following lemma establishes several desirable properties this value function. In the remainder of this
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 17 
section, we frequently use the constants L = √ A/(1 − γ)2 and ℓ = 2γA/(1 − γ)3. 
Lemma 4.1 (Properties of the value function). Suppose that Assumption 2 holds. Then, for every δ > 0, there exists an open neighborhood Πδ of Π such that any point in Πδ has a (Frobenius) distance of at most δ from some point in Π, and the value function V P 
π (s0) satisfies the following conditions for every P ∈ P. (i) V P 
π (s0) is (L + δ)-Lipschitz continuous and (ℓ + δ)-smooth in π on Πδ. (ii) C−1(V P 
π (s0)−minπ′∈Π V P π′ (s0))−δ ≤maxπ′∈Πδ 
⟨π−π′,∇πV P π (s0)⟩ for all π ∈ Πδ. 
Proof. By [53, Lemma 3.1], V P π (s0) is L-Lipschitz continuous and ℓ-smooth on Π. 
In addition, C−1(V P π (s0)−minπ′∈Π V P 
π′ (s0)) ≤maxπ′∈Π⟨π −π ′,∇πV 
P π (s0)⟩ for all π ∈ Π 
thanks to [1, Lemma 4.1]. As V P π (s0) is continuous and rational in π and P on a 
neighborhood of Π×P and as Π is compact, Berge’s maximum theorem [4, pp. 115-116] implies that maxπ′∈Π⟨π − π 
′,∇πV P π (s0)⟩ is continuous in π on a neighborhood of Π. 
The claim then follows because both Π and P are compact. 
Throughout the rest of this section we use Φ(π) as a shorthand for the worst-case value function V ⋆π (s0) =maxP ∈P V P 
π (s0), which is defined for all π ∈ Πδ. This helps us to avoid clutter. We henceforth refer to Φ as the primal function. In addition, we let π⋆ ∈ argminπ∈ΠΦ(π) be an optimal solution of the policy improvement problem (2.3). The primal function Φ generically fails to be differentiable. It is thus useful to approximate Φ by its Moreau envelope Φλ ∶ RS×A → R parametrized by λ > 0, which is defined through Φλ(π) = minπ′∈ΠΦ(π′) + ∥π′ − π∥2F/(2λ). The following lemma establishes useful properties of the primal function Φ and its Moreau envelope Φλ. 
Lemma 4.2 (Properties of the primal function). The following hold. (i) Φ(π) is (ℓ + δ)-weakly convex and (L + δ)-Lipschitz continuous on Πδ. (ii) If 0 < λ < 1/(ℓ + δ), then Φλ(π) is convex and differentiable. If additionally ∥∇Φλ(π)∥F ≤ ϵ for some π ∈ Πδ, then there exists π̂ ∈ Πδ such that ∥π−π̂∥F ≤ ϵλ and minv∈∂Φ(π̂) ∥v∥F ≤ ϵ. 
Proof. As for Assertion (i), note first that Φ(π) is (L + δ)-Lipschitz continuous on Πδ thanks to [33, Lemma 4.3], which applies because of the (L + δ)-Lipschitz continuity of V P 
π (s0) established in Lemma 4.1(i). Similarly, [48, Lemma 3.3] implies that Φ(π) inherits (ℓ + δ)-weak convexity from the (ℓ + δ)-smoothness of V P 
π (s0) established in Lemma 4.1(i). Assertion (ii) then holds because of [14, Section 2.2]. We include a short proof to keep this paper self-contained. For ease of notation we set fπ(π 
′) = Φ(π′)+∥π′−π∥2F/(2λ). Note first that fπ(π′) is strongly convex in π′ because Φ(π′) is (ℓ + δ)-weakly convex and because 0 < λ < 1/(ℓ + δ). Danskin’s theorem [5, Proposition B.25] thus implies that, for any π ∈ Πδ, Φλ(π) =minπ′∈Π fπ(π 
′) is convex and differentiable with ∇Φλ(π) = ∇πfπ(π̂) = (π−π̂)/λ, where π̂ is the unique minimizer of fπ(π′) across all π′ ∈ Π. This implies that if ∥∇Φλ(π)∥F ≤ ϵ, then ∥π̂ − π∥F ≤ ϵλ. It suffices to show that π̂ = argminπ′∈Π f(π′) satisfies minξ∈∂Φ(π̂) ∥ξ∥F ≤ ϵ and ∥π−π̂∥F ≤ ϵλ. Therefore, the optimal solution of minπ′∈Π f(π′) is unique, and Danskin’s theorem [5, Proposition B.25] implies that ∇Φλ(π) = ∇πfπ(π̂) = (π − π̂)/λ. Taking the norm of the previous equality yields ∥π̂ − π∥F = ∥∇Φλ(π)∥Fλ ≤ ϵλ, where the inequality follows from the premise that ∥∇Φλ(π)∥F ≤ ϵ. On the other hand, the optimality of π̂ implies that 0 ∈ ∂π′fπ(π 
′)∣π′=π̂, which is equivalent to (π − π̂)/λ ∈ ∂Φ(π̂). Hence, it follows that minv∈∂Φ(π̂) ∥v∥F ≤ ∥(π − π̂)/λ∥F ≤ ϵ. 
Lemma 4.2(ii) asserts that if 0 < λ < 1/ℓ, then the λϵ-neighborhood of any approximate stationary point of the Moreau envelope Φλ contains an approximate stationary point of Φ. Thus, approximate stationary points of Φ can be found by searching for approximate stationary points of Φλ.
18 M. LI, D. KUHN, AND T. SUTTER 
Lemma 4.3 (Stationarity guarantee [53, Theorem 3.3]). The iterates {π(k)}K−1k=0 
of Algorithm 4.1 satisfy K−1 
∑ k=0 
∥∇Φ1/(2ℓ)(π (k) )∥ 
2 
F ≤ 
√ 4ℓS 
η + 2KηℓL2 + 4ℓϵK. 
Lemma 4.3 guarantees that if ϵ = L √ 2S/K/2 and η = 
√ 2S/K/L, then the iterates 
{π(k)}Kk=0 generated by Algorithm 4.1 satisfy 
min k=0,...,K−1 
∥∇Φ1/(2ℓ)(π (k) )∥ 
F =( min 
k=0,...,K−1 ∥∇Φ1/(2ℓ)(π 
(k) )∥ 
2 
F ) 
1 2 
≤(6ℓL √ 2SK) 
1 2=O(K− 
1 4). 
The following lemma, which is inspired by [13, Lemma 12], establishes a fundamental inequality that can be used to convert an approximate stationary point of the Moreau envelope Φ1/(2ℓ) to an approximate minimizer of Φ. 
Lemma 4.4 (Gradient dominance property of Φ). If Assumption 2 holds, then we have Φ(π) −Φ (π⋆) ≤ (C 
√ 2S +L/(2ℓ))∥∇Φ1/(2ℓ)(π)∥F for all π ∈ Π. 
Proof of Lemma 4.4. Choose any δ > 0. By Lemma 4.2(i), Φ is (ℓ + δ)-weakly convex on Πδ. Theorem 25.5 in [41] then implies that the set of points at which Φ is differentiable is dense in intΠδ and hence in Πδ. We first prove that the claimed inequality holds approximately for any point π ∈ Πδ at which Φ is differentiable. In this case the subdifferential ∂Φ(π) = {∇Φ(π)} is a singleton, and a generalization of Danskin’s theorem (Theorem B.4) implies that ∇Φ(π) = ∇πV 
P ⋆ π (s0) for any P ⋆ ∈ 
argmaxP ∈P V P π (s0). As Lemma 4.1(ii) holds in particular for P = P ⋆, we have max π′∈Πδ 
⟨π − π′,∇πV P ⋆ π (s0)⟩ ≥ C 
−1 (V P ⋆ 
π (s0) −min π′∈Π 
V P ⋆ π′ (s0)) − δ 
≥ C−1(Φ(π) −Φ(π⋆)) − δ, 
(4.1) 
where the second inequality holds because minπ∈Π V P ⋆ π (s0) ≤minπ∈ΠmaxP ∈P V P 
π (s0) = Φ(π⋆). The Cauchy-Schwarz inequality then allows us to conclude that√ 
2S + 2δ √ 2S + 2δ 
∥∇Φ(π)∥F ≥ 1 
√ 2S + 2δ 
max π′∈Πδ,∥π′−π∥F≤ 
√ 
2S+2δ ⟨π − π′,∇Φ(π)⟩ 
= 1 
√ 2S + 2δ 
max π′∈Πδ 
⟨π − π′,∇πV P ⋆ π (s0)⟩ 
≥ 1 
C( √ 2S + 2δ) 
(Φ(π) −Φ(π⋆)) − δ 
√ 2S + 2δ 
. 
The equality in the above expression holds because there exist π′δ, πδ ∈ Π with ∥π − πδ∥F ≤ δ and ∥π′ − π′δ∥F ≤ δ and because ∥π′δ − πδ∥F ≤ 
√ 2S thanks to Lemma B.3. 
This implies that ∥π′−π∥F ≤ ∥π′−π′δ∥F+∥π ′ 
δ −πδ∥F+∥πδ −π∥F ≤ √ 2S+2δ. The second 
inequality follows from (4.1). Next, set ϵ=∥∇Φ1/(2ℓ+2δ)(π)∥F. By Lemma 4.2(ii), there is π̂ ∈ Πδ such that ∥π − π̂∥F ≤ ϵ/(2ℓ + 2δ) and minv∈∂Φ(π̂) ∥v∥F ≤ ϵ. Theorem B.4 thus implies that there exists P̂ ∈ argmaxP ∈P V P 
π̂ (s0) with ∥∇πV P̂ π̂ (s0)∥F ≤ ϵ. We then find 
ϵ ≥ ∥∇πV P̂ π̂ (s0)∥F ≥ 
1 √ 2S + 2δ 
max π′∈Πδ 
⟨π̂ − π′,∇πV P̂ π̂ (s0)⟩ 
≥ 1 
C( √ 2S + 2δ) 
(V P̂ π̂ (s0) −min 
π∈Π V P̂ π (s0)) − 
δ √ 2S + 2δ 
≥ 1 
C( √ 2S + 2δ) 
(Φ(π̂) −Φ(π⋆)) − δ 
√ 2S + 2δ 
, 
(4.2) 
where the second inequality follows from the Cauchy-Schwarz inequality and our earlier insight that ∥π̂ − π′∥F ≤ 
√ 2S + 2δ for all π̂, π′ ∈ Πδ, the third inequality follows
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 19 
from Lemma 4.1(ii), and the fourth inequality holds because V P̂ π̂ (s0) = Φ(π̂) and 
minπ∈Π V P̂ π (s0) ≤minπ∈ΠmaxP ∈P V P 
π (s0) = Φ(π ⋆). The above reasoning implies that 
Φ(π) −Φ(π⋆) = Φ(π̂) −Φ(π⋆) +Φ(π) −Φ(π̂) 
≤ C(ϵ( √ 2S + 2δ) + δ) + (L + δ)∥π̂ − π∥F 
≤ (C( √ 2S + 2δ) + 
L + δ 
2(ℓ + δ) ) ϵ +Cδ, 
where the first inequality follows from (4.2) and Lemma 4.2(i), and the second inequality holds because ∥π̂ − π∥F ≤ ϵ/(2ℓ + 2δ). As ϵ=∥∇Φ1/(2ℓ+2δ)(π)∥F, we thus have 
Φ(π) −Φ(π⋆) ≤ (C( √ 2S + 2δ) + 
L + δ 
2(ℓ + δ) ) ∥∇Φ1/(2ℓ+2δ)(π)∥F +Cδ.(4.3) 
Hence, if δ is small, the claimed gradient dominance condition holds approximately at any point π ∈ Πδ where the primal function Φ is differentiable. 
Consider now an arbitrary π ∈ Π irrespective of whether or not Φ is differentiable at π. Let {πt} 
∞ 
t=0 be a sequence in an open neighborhood of Π converging to π such that Φ is differentiable at πt and πt ∈ Πδt with δt = 1/t for every t ∈ N. From the inequality (4.3) established in the first part of the proof we know that 
Φ(πt) −Φ(π ⋆ ) ≤ (C( 
√ 2S + 2δt) + 
L + δt 2(ℓ + δt) 
) ∥∇Φ1/(2ℓ+2δt)(πt)∥F +Cδt ∀t ∈ N. 
The claim then follows because πt converges to π and δt converges to 0, while Φ as well as the gradient ∇Φ1/(2ℓ+2δ) of its Moreau envelope are continuous at π. 
With all these preparatory results at hand, we are now ready to characterize the convergence behavior of Algorithm 4.1. 
Theorem 4.5 (Convergence of Algorithm 4.1). If Assumption 2 holds, ϵ = 
L √ 2S/K/2 and η = 
√ 2S/K/L, then the iterates {π(k)}K−1k=0 of Algorithm 4.1 satisfy 
1 
K 
K−1 
∑ k=0 
(V ⋆π(k)(s0) −min π∈Π 
V ⋆π (s0)) ≤ (72S)1/4(C 
√ 2ℓLS +L 
√ L/ℓ/2) 
K1/4 . 
Proof of Theorem 4.5. We have 1 
K 
K−1 
∑ k=0 
(V ⋆π(k)(s0) −min π∈Π 
V ⋆π (s0)) = 1 
K 
K−1 
∑ k=0 
(Φ(π(k)) −min π∈Π 
Φ(π)) 
≤ (C √ 2S +L/(2ℓ)) 
K 
K−1 
∑ k=0 
∥∇Φ1/(2ℓ)(π (k) )∥F 
≤ (C √ 2S +L/(2ℓ)) √ K 
¿ Á ÁÀ 
K−1 
∑ k=0 
∥∇Φ1/(2ℓ)(π(k))∥ 2 F 
≤ (C √ 2S +L/(2ℓ))(72S)1/4(ℓL)1/2 
K1/4 , 
where the equality exploits the definition of the primal function Φ, while the three inequalities follow from Lemma 4.4, Jensen’s inequality and Lemma 4.3 with ϵ = L √ 2S/K/2 and η = 
√ 2S/K/L, respectively. 
Theorem 4.5 implies that an ε-optimal solution of the robust policy improvement problem (2.3) can be computed in K = O(1/ε4) iterations provided that the robust policy evaluation oracle is guaranteed to output an ϵ-optimal solutions with ϵ = O(ε2). Arbitrarily accurate solutions of the robust policy improvement problem (2.3) can thus only be obtained if the error ϵ of the robust policy evaluation oracle can be made
20 M. LI, D. KUHN, AND T. SUTTER 
arbitrarily small. If the robust policy evaluation oracle has a fixed accuracy ϵ, however, then the robust policy improvement problem (2.3) can only be solved up to a certain accuracy. The following corollary of Theorem 4.5 formalizes this statement. 
Corollary 4.6 (Performance of Algorithm 4.1 under constant policy evaluation error). Suppose that Assumption 2 holds and that the robust policy evaluation oracle (called in step 3 of Algorithm 4.1) is solved to a constant error ϵ ≥ 0. If the learning rate is η = 
√ 2S/K/L, then the iterates {π(k)}K−1k=0 of Algorithm 4.1 satisfy 
1 
K 
K−1 
∑ k=0 
(V ⋆π(k)(s0) −min π∈Π 
V ⋆π (s0)) ≤ C1K −1/4 +C2 
√ ϵ, 
where C1 = (32S) 1/4(C 
√ 2S +L/(2ℓ)) 
√ ℓL and C2 = (C 
√ 2S +L/(2ℓ)) 
√ 4ℓ. 
Proof of Corollary 4.6. By using a similar reasoning as in the proof of Theorem 4.5, we obtain 
1 
K 
K−1 
∑ k=0 
(V ⋆π(k)(s0) −min π∈Π 
V ⋆π (s0)) 
≤ (C √ 2S +L/(2ℓ)) √ K 
¿ Á ÁÀ 
K−1 
∑ k=0 
∥∇Φ1/(2ℓ)(π(k))∥ 2 F 
≤ (C √ 2S +L/(2ℓ)) √ K 
√ 4ℓS 
η + 2KηℓL2 + 4ℓϵK 
≤ (C √ 2S +L/(2ℓ)) √ K 
⎛ 
⎝ 
√ 4ℓS 
η + 2KηℓL2 + 
√ 4ℓϵK 
⎞ 
⎠ 
= (C √ 2S +L/(2ℓ)) √ K 
( 
√ 
4 √ 2KSℓL + 
√ 4ℓϵK) 
= (32S)1/4(C 
√ 2S +L/(2ℓ)) 
√ ℓL 
K1/4 + (C 
√ 2S +L/(2ℓ)) 
√ 4ℓϵ. 
The first inequality follows from the definition of Φ, from Lemma 4.4 and from Jensen’s inequality. The second inequality uses Lemma 4.3, and the third inequality holds because 
√ x + y < 
√ x + √ y for all x, y > 0. The first equality, finally, follows from the 
choice of the learning rate η. 
A similar global convergence result for a projected gradient descent algorithm with access to an approximate robust policy evaluation oracle was established in [53]. However, no robust policy evaluation oracle for general non-rectangular uncertainty sets is described, and its accuracy is required to increase geometrically with the number of iterations of the algorithm. Also, the proof strategy leading up to the gradient dominance condition is methodologically different from ours. In [53] any subgradient of the primal function must be expressed as a convex combination of gradients of the value function evaluated at a finite number of worst-case kernels. In contrast, we approximate the subgradients at non-differentiable points by sequences of gradients at nearby differentiable points. This alternative proof technique is arguably more transparent and more directly reveals the gradient dominance property of the Moreau envelope of the primal function. 
5. Numerical Experiments. We assess the performance of the proposed algorithms on standard test problems: A stochastic GridWorld problem [46], randomly generated Garnet MDPs [3], and a machine replacement problem [15]. Sections 5.1 and 5.2 focus on robust policy evaluation. Section 5.1 first compares the solution
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 21 
qualities of the projected Langevin dynamics algorithm (PLD, Algorithm 3.1) and the Frank-Wolfe algorithm (FW, Algorithm 3.2) in the context of a GridWorld problem. Section 5.2 uses Garnet MDPs to assess the runtime performance of FW against that of the state-of-the-art projected gradient descent algorithm for robust policy evaluation described in [53]. Section 5.3, finally, focuses on a machine replacement problem and compares the actor-critic algorithm (ACA, Algorithm 4.1) against the only existing method for robust policy improvement with non-rectangular uncertainty sets described in [58]. All experiments are implemented in Python, and are run on an Intel i7-10700 CPU (2.9GHz) computer with 16 GB RAM. 
5.1. Stochastic GridWorld: Rectangular and Non-Rectangular Uncer-tainty Sets. The purpose of the first experiment is to show that PLD outputs the same policy value as FW when the uncertainty set is rectangular but may output a higher policy value than FW otherwise. Our experiment is based on a stylized GridWorld problem, which is widely studied in reinforcement learning [46]. Specifically, the state space S comprises the 25 cells of a 5×5 grid, and the action space A comprises the 4 directions “up,” “down,” “left,” and “right.” An agent moves across the grid with the aim to reach the Goal State in cell 1 (in the top left corner) while avoiding the Bad State in cell 25 (in the bottom right corner). If the agent resides in cell s ∈ S and selects action a ∈ A, then she moves to cell s′ ∈ S with probability P (s′∣s, a). The agent incurs a cost of 10 in the Bad State, a cost of 0 in the Goal State, and a cost of 0.2 in any other state. The initial state s0 is assumed to follow the uniform distribution on S, which we denote as ρ, and the discount factor is set to γ = 0.9. We also assume that the agent’s knowledge is captured by an uncertainty set P, which is defined as some neighborhood of a reference transition kernel Pref . In the following we define S(s) ⊆ S as the set of all cells adjacent to s. We set Pref(s 
′∣s, a) = 0.7 if s′ is the cell adjacent to s in direction a, Pref(s 
′∣s, a) = 0.1 if s′ is any other cell adjacent to s, Pref(s 
′∣s, a) = 1 − ∑s′′∈S(s) Pref(s ′′∣s, a) if s′ = s, and Pref(s 
′∣s, a) = 0 otherwise. If there is no cell adjacent to s in direction a, then we set Pref(s 
′∣s, a) = 0.1 if s′ is any cell adjacent to s, Pref(s 
′∣s, a) = 1 − ∑s′′∈S(s) Pref(s ′′∣s, a) if s′ = s, and 
Pref(s ′∣s, a) = 0 otherwise. Our goal is to compute the worst-case net present cost 
V ⋆π (ρ) =maxP ∈P ∑s0∈S ρ(s0)V P π (s0) of the policy π ∈ Π that selects actions randomly 
from the uniform distribution on A irrespective of the current state. Gradient-based methods such as PLD or FW can be used to compute V ⋆π (ρ) even 
if the initial state is random. In this case, however, nature’s policy gradients of the form ∇PV 
P π (s0) must be replaced with ∑s0∈S ρ(s0)∇PV 
P π (s0). Throughout the first 
experiment we employ PLD with Gibbs parameter β = 160, stepsize η = 0.8, initial iterate ξ(0) = ξref corresponding to the nominal transition kernel Pref and M = 100 iterations. In addition, we use FW with tolerance ϵ = 10−2, stepsizes {αm} 
∞ 
m=0 chosen as in Theorem 3.12 and initial iterate P (0) = Pref . We also work with variants of the PLD and FW algorithms that output the best iterates found during execution. We first assume that P constitutes an (s, a)-rectangular uncertainty set of the form 
P = {P ∈∆(S)S×A ∶ ∥P (⋅∣s, a) − Pref(⋅∣s, a)∥2 ≤ r ∀s ∈ S, a ∈ A} 
with size parameter r ≥ 0. Note that if P ∈ P and r > 0, then P (s′∣s, a) can be strictly positive even if s′ is not adjacent to s. Figure 1a shows the worst-case policy values output by PLD averaged over 20 independent simulation runs and compares them against the deterministic values output by FW. We highlight that the standard deviations of the values output by PLD range from 6.50×10−5 to 0.12 and are therefore practically negligible. As expected from Theorems 3.6 and 3.12, we observe that the two algorithms are consistent. That is, if the uncertainty set is rectangular, then
22 M. LI, D. KUHN, AND T. SUTTER 
both PLD and FW succeed in solving the robust policy evaluation problem to global optimality. Figure 1b visualizes the policy values associated with the iterates ξ(m) of a single simulation run of PLD, illustrating the exploratory nature of the algorithm. Specifically, we see that for large m the policy values oscillate around a constant level. 
10−3 10−2 10−1 100 
10 
20 
30 
size parameter r 
V ⋆ π ( ρ ) 
PLD CPI 
(a) Robust policy value output by PLD (blue) and FW (red) for an (s, a)-rectan-gular uncertainty set of varying size r. 
100 101 102 
10 
20 
30 
iteration counter m 
V P 
ξ (m ) 
π ( ρ ) 
PLD 
(b) Trajectory of policy values computed by PLD for an (s, a)-rectangular uncertainty set of fixed size r = 10. 
Figure 1: Comparison of PLD (Algorithm 3.1) against FW (Algorithm 3.2) on a stochastic GridWorld problem with an (s, a)-rectangular uncertainty set. 
Next, we assume that P constitutes a non-rectangular ambiguity set of the form P = {P ξ 
∶ (ξ − ξref) ⊺H(ξ − ξref) ≤ r} 
with size parameter r ≥ 0 and Hessian matrix H = diag(1,2, . . . , (S − 1)SA). As shown in Appendix A, ellipsoidal uncertainty sets of this type naturally emerge when maximum likelihood estimation is used to construct statistically optimal confidence regions for ξ. Figure 2a shows the worst-case policy values output by PLD (averaged over 20 independent simulation runs) and FW. The standard deviations of the values output by PLD range from 3.57 × 10−2 to 7.75 × 10−2 and are thus again negligible. We observe that for r ≲ 1 PLD reports higher worst-case policy values than FW. This suggests that the deterministic FW method may get trapped in local maxima, while the randomized PLD method manages to escape local maxima. For r ≳ 1 the outputs of PLD and FW match. This is to be expected from Theorem 3.12 because the uncertainty set P converges to the (s, a)-rectangular product simplex ∆(S)S×A—and thus becomes increasingly rectangular—as r grows. Figure 2a visualizes the policy values associated with the iterates ξ(m) of a single simulation run of PLD. We remark that PLD can outperform FW by up to 80% on 2×2 GridWorld problems (not shown). 
Table 1 shows the runtimes of PLD and FW for non-rectangular uncertainty sets of different sizes. Despite the suboptimal theoretical convergence rate, PLD is empirically faster than FW while producing more accurate solutions for robust policy evaluation problems with non-rectangular uncertainty sets. 
Runtime [s] r = 0.01 r = 0.1 r = 1 r = 10 
PLD (Algorithm 3.1) 357.56 (6.08) 310.05 (6.20) 428.57 (6.73) 370.87 (91.08) 
FW (Algorithm 3.2) 499.48 850.60 948.65 1,950.04 
Table 1: Runtimes of PLD and FW for non-rectangular uncertainty sets. For PLD we report both means and standard deviations (in parenthesis) over 20 simulation runs. 
5.2. Garnet MDPs: Rectangular Uncertainty Sets. The purpose of the second experiment is to show that FW may solve robust policy evaluation problems with s-rectangular uncertainty sets faster than the state-of-the-art method for this problem
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 23 
10−2 10−1 100 101 
6 
6.5 
7 
7.5 
size parameter r 
V ⋆ π ( ρ ) 
PLD CPI 
(a) Robust policy value output by PLD (blue) and FW (red) for a non-rectangular uncertainty set of varying size r. 
100 101 102 5.5 
6 
6.5 
7 
7.5 
iteration counter m 
V P 
ξ (m ) 
π ( ρ ) 
PLD 
(b) Trajectory of policy values computed by PLD for a non-rectangular uncertainty set of fixed size r = 10. 
Figure 2: Comparison of PLD (Algorithm 3.1) against FW (Algorithm 3.2) on a stochastic GridWorld problem with a non-rectangular uncertainty set. 
class developed in [53]. We use the Generalized Average Reward Non-stationary Environment Test-bench (Garnet) [3, 8] to generate random reference transition kernels Pref with a prescribed number of states and actions and with a prescribed branching parameter b ∈ [0,1]. By definition, b determines the proportion of states that are reachable from any given state-action pair in one single transition. We set the branching parameter to b = 1 and the discount factor to γ = 0.6, and we generate the cost c(s, a) corresponding to any a ∈ A and s ∈ S randomly from the uniform distribution on [0,1]. The initial state s0 follows the uniform distribution over S. In addition, we fix a policy π ∈ Π defined through π(a∣s) = v(s, a)/∑a′∈A v(s, a′), where v(s, a) is sampled uniformly from {1, . . . ,10} for every s ∈ S and a ∈ A. Finally, we assume that P constitutes an s-rectangular uncertainty set of the form 
P = {P ∈∆(S)S×A ∶ ∥P (⋅∣s, ⋅) − Pref(⋅∣s, ⋅)∥1 ≤ 5 ∀s ∈ S} . 
We solve the resulting instances of the robust policy evaluation problem (2.2) with FW and with [53, Algorithm 2], a state-of-the-art projected gradient descent method. 
In the second experiment we seek δ-optimal solutions of (2.2) for δ = 0.01. To this end, we use FW with tolerance ϵ = δS/(1 − γ), stepsizes {αm} 
∞ 
m=1 chosen as in Theorem 3.12 and initial iterate P (0) = Pref. In addition, we use [53, Algorithm 2] with initial iterate P (0) = Pref and stepsize (1−γ)3/(2γS2) as suggested by [53, Theorem 4.4]. The above estimates of the iteration complexity and the distribution mismatch coefficient imply that we would have to run [53, Algorithm 2] over 32γS5A/(δ2(1 − γ)6) iterations in order to guarantee that it outputs a δ-optimal solution. Unfortunately, this is impractical. For example, already our smallest test problem with only S = 100 states would require more than 1018 iterations. We thus use the inequality 
∣V P (m+1) π (ρ) − V P (m) 
π (ρ)∣ ≤ 2 × 10−5 
as a heuristic termination criterion. Even though it has no theoretical justification, this criterion ensures that [53, Algorithm 2] terminates within a reasonable amount of time and outputs similar value estimates as FW with a maximum difference of 2.5%. 
The direction-finding subproblems of FW as well as the projection subproblems of [53, Algorithm 2] are solved with GUROBI. To faithfully assess algorithmic efficiency, we record the solver times for these most time-consuming subroutines. For all other processes we record the wall-clock time. Table 2 reports the overall runtimes of FW
24 M. LI, D. KUHN, AND T. SUTTER 
and [53, Algorithm 2] (based on the authors’ code available from GitHub1) averaged over 20 random instances with A = 10 actions and increasing numbers of states. 
As expected from the analysis of the iteration complexities, FW is significantly faster than [53, Algorithm 2] on instances with large state spaces. The value estimates of both algorithms differ at most 2.5%, with FW outputting a more accurate solution. 
Runtime [s] S = 100 S = 200 S = 300 S = 400 
[53, Algorithm 2] 51.14 426.83 1,887.47 5,328.41 
FW (Algorithm 3.2) 28.39 209.18 696.60 1,120.26 
Table 2: Runtimes of the projected gradient descent algorithm developed in [53] and FW on Garnet MDP instances with s-rectangular uncertainty sets with A = 10. 
5.3. Machine Replacement: Non-Rectangular Uncertainty Sets. The purpose of the third experiment is to assess the out-of-sample performance of different data-driven policies for MDPs with unknown transition kernels. Our experiment is based on a now standard machine replacement problem described in [15, 58]. The goal is to find a repair strategy for a machine whose condition is described by eight “operative” states 1, . . . ,8 and two “repair” states R1 and R2. The available actions are “do nothing” or “repair.” The states 8, R1 and R2 incur a cost of 20, 2 and 10 per time period, respectively, whereas no cost is incurred in the other states. The discount factor is set to γ = 0.8, and the initial state s0 follows the uniform distribution on S. In addition, we define the transition kernel P 0 as in [58, Section 6]. The optimal value of the resulting (non-robust) policy improvement problem then amounts to 5.98. 
In the following we assume that P 0 is unknown but falls within a known structural uncertainty set P0. We specifically assume that some of the 2 × 102 transition probabilities are known to vanish such that P0 = {P ξ ∶ ξ ∈ Ξ0}, where P ξ is an affine function, and Ξ0 = [0,1]25 is a hypercube of dimension 25. The components of ξ represent different entries of the transition kernel that are neither known to vanish nor determined by the normalization conditions ∑s′∈S P 
0(s′∣s, a) = 1 for all s ∈ S and a ∈ A. Sometimes we will additionally assume that certain transition probabilities are known to be equal, in which case Ξ0 = [0,1]5 reduces to a hypercube of dimension 5. Full details about these structural assumptions are provided in [58, Section 6]. 
In addition to structural information, there is statistical information about P 0, that is, P 0 is indirectly observable through a history of n states and actions generated under a known policy π0. We assume that π0 chooses the actions “do nothing” and “repair” in each operative state 1, . . . ,7 with probabilities 0.8 and 0.2, respectively. In the states 8 and R2, π0 always chooses the action “repair”, and in state R1, π0 
always chooses the action “do nothing.” In the following we use ξn to denote the maximum likelihood estimator for the parameter ξ0 ∈ Ξ0 that generates the unknown true transition kernel P 0 = P ξ0 . Following [58, Section 5], one can use the observation history of length n to construct an ellipsoidal confidence region Ξn ⊆ Ξ0 centered at ξn 
that contains ξ0 with probability at least 1 − α for any prescribed α ∈ [0,1]. It is then natural to construct an uncertainty set Pn = {P ξ ∶ ξ ∈ Ξn} that amalgamates all structural and statistical information about P 0 and is guaranteed to contain the data-generating kernel P 0 with probability 1 − α. A related but simpler recipe for constructing uncertainty sets using maximum likelihood estimation is sketched in 
1https://github.com/JerrisonWang/ICML-DRPG
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 25 
Appendix A for illustrative purposes. Full details are provided in [58, Section 5]. The uncertainty set Pn is non-rectangular, and thus the corresponding robust 
policy improvement problem is hard. A sequential convex optimization procedure that solves a decision rule approximation of the robust policy improvement problem is described in [58, Algorithm 4.1]. To our best knowledge, this is the only existing method for addressing robust MDPs with non-rectangular uncertainty sets. Replacing Pn 
with its s-rectangular or even its (s, a)-rectangular hull leads to a simpler robust policy improvement problem that can be solved exactly and efficiently via dynamic programming. However, the resulting optimal policy is dominated by the policy output by [58, Algorithm 4.1] in that it generates up to 30% or even 60% higher out-of-sample net present costs, respectively, see [58, Table 3]. 
Unlike [58, Algorithm 4.1], ACA (Algorithm 4.1) uses no decision rule approximation and computes near-optimal solutions to the robust policy improvement problem of any prescribed accuracy (see Theorem 4.5). We will now show numerically that the near-optimal policies found by ACA dominate the approximately optimal policies found by [58, Algorithm 4.1] in terms of out-of-sample net present cost under P 0. Throughout the experiment we employ ACA with iteration number K = 100 and stepsize η = 0.05. The critic’s subproblem computes near-optimal solutions to the robust policy evaluation problem by using PLD (Algorithm 3.1) with initial iterate ξ(0) = ξn, Gibbs parameter β = 450, stepsize η = 0.07 and iteration number M = 50. We work with a variant of PLD that outputs the best iterate found during execution. 
Tables 3 and 4 compare the out-of-sample costs of the policies found by ACA and [58, Algorithm 4.1] under the assumption of full (ξ ∈ R5) and partial (ξ ∈ R25) structural information, respectively, as a function of the length n of the observation history and the coverage probability 1 − α of the uncertainty set. The out-of-sample costs corresponding to [58, Algorithm 4.1] in Table 3 are directly borrowed from [58, Table 3]. Conversely, the out-of-sample costs corresponding to [58, Algorithm 4.1] in Table 4 are computed using the authors’ source code in C++ (private communication). 
Table 3 shows that when the transition kernel has only 5 degrees of freedom, both policies generate an out-of-sample cost close to the optimal value 5.98 of the classical policy improvement problem under the unknown true transition kernel P 0. Moreover, the out-of-sample costs of the two policies differ at most by 0.5%. These observations are not surprising because kernels with only 5 degrees of freedom are easy to learn and because the uncertainty set Pn is small already for small sample sizes n. In this case, the decision rule approximation underlying [58, Algorithm 4.1] is highly accurate. Algorithm 4.1, which is designed for uncertainty sets of arbitrary size and solves the critic’s subproblem with a randomized PLD scheme, slightly outperforms the benchmark method only for the smallest sample sizes considered. 
n 1 − α 80% 90% 95% 99% 
500 6.02 (6.04) 6.02 (6.04) 6.02 (6.04) 6.02 (6.06) 
1,000 6.03 (6.02) 6.04 (6.02) 6.04 (6.02) 6.00 (6.02) 
2,500 6.03 (6.01) 6.03 (6.00) 6.02 (6.00) 6.02 (6.01) 
5,000 6.01 (5.99) 6.03 (5.99) 6.02 (5.99) 6.03 (5.99) 
Table 3: Out-of-sample costs of the policies found by ACA and [58, Algorithm 4.1] (in parenthesis) under full structural information (kernel with 5 degrees of freedom). 
Table 4 shows that when the transition kernel has 25 degrees of freedom, then Algorithm 4.1 outperforms [58, Algorithm 4.1] uniformly across all values of n and 1−α. The advantage is most significant when the uncertainty set is large (i.e., for n ≤ 1,000).
26 M. LI, D. KUHN, AND T. SUTTER 
We also highlight that the average wall-clock time for solving all problem instances with Algorithm 4.1 amounts to 179.16 seconds. The average solver time consumed by [58, Algorithm 4.1], on the other hand, amounts to 351.24 seconds. 
n 1 − α 80% 90% 95% 99% 
500 8.34 (15.72) 8.40 (14.24) 6.48 (13.44) 7.41 (19.29) 
1,000 6.57 (8.45) 6.27 (9.79) 6.96 (10.60) 6.77 (10.02) 
2,500 6.26 (6.55) 6.08 (6.84) 6.36 (6.82) 6.20 (8.47) 
5,000 6.23 (6.64) 6.49 (6.53) 6.29 (6.50) 6.24 (6.54) 
Table 4: Out-of-sample costs of the policies found by ACA and [58, Algorithm 4.1] (in parenthesis) under partial structural information (kernel with 25 degrees of freedom). 
Acknowledgements. This work was supported as a part of the NCCR Auto-mation, a National Center of Competence in Research, funded by the Swiss National Science Foundation (grant number 51NF40_225155). The authors are indebted to George Lan and Yan Li for helpful comments on an earlier version of this paper, and to Ilyas Fatkhullin for useful discussions. 
Appendix A. Construction of Uncertainty Sets via Maximum Likelihood Estimation. We now review a standard procedure for constructing an uncertainty set for the transition kernel of an MDP as described in [58, Section 5]. This uncertainty set is statistically optimal in a precise sense but fails to be rectangular. 
Assume for ease of exposition that it is possible to move from any state of the MDP to any other state in one single transition, that is, all entries of the unknown transition kernel are strictly positive. The uncertainty set can thus be expressed as the image of a solid parameter set Ξ ⊆ Rq of dimension q = SA(S − 1) under an affine function P ξ. Specifically, there exists a bijection g ∶ S ×A × (S/{S}) → {1, . . . , q}, and any such bijection can be used to construct a valid function P ξ defined through P ξ(s′∣s, a) = ξg(s,a,s′) for all s ∈ S, a ∈ A and s′ ∈ S/{S}, and P ξ(S∣s, a) = 1 −∑ 
S−1 s′=1 ξg(s,a,s′) for all 
s ∈ S and a ∈ A. The largest imaginably uncertainty set P0 =∆(S) S×A of all possible 
transition kernels can then be expressed as the image of the parameter set 
Ξ0 = {ξ ∈ Rq 
+ ∶ S−1 
∑ s′=1 
ξg(s,a,s′) ≤ 1 ∀s ∈ S, a ∈ A} 
under P ξ. In the following we assume that the decision maker has access to a stateaction observation history (s0, a0, . . . , sn−1, an−1) ∈ (S ×A)n of the MDP generated under some known policy π0 ∈ Π and the unknown true transition kernel P ξ0 encoded by ξ0 ∈ Ξ0. The log-likelihood of observing this history under any ξ ∈ Ξ is given by 
ℓn(ξ) = n−2 
∑ t=0 
log[P ξ (st+1∣st, at)] + ζ, where ζ = log[ρ(s0)] + 
n−1 
∑ t=0 
log[π0 (at∣st)] 
is an irrelevant constant independent of ξ, and ρ represents the initial state distribution. One can show that the maximum likelihood estimator ξn that maximizes ℓn(ξ) over Ξ0 
corresponds to the kernel of empirical transition probabilities [58, Remark 6]. This means that P ξn(s′∣s, a) coincides with number of observed transitions from (s, a) to s′, normalized by the length n of the observation history. One can use the maximum likelihood estimator ξn as well as the log-likelihood function ℓn(ξ) to construct a confidence set {ξ ∈ Ξ0 ∶ ℓn(ξ) ≥ ℓn(ξ 
n) − δ} for ξ0. Indeed, this set contains ξ0 with probability 1−α asymptotically for large n if δ is set to one half of the (1−α)-quantile of the chi-squared distribution with S − 1 degrees of freedom [58, Theorem 5]. This
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 27 
statistical guarantee persists if we approximate the log-likelihood function ℓn by its second-order Taylor expansion 
φn(ξ) = ℓn(ξ n ) − 
1 
2 (ξ − ξn) 
⊺ [∇ 
2 ξℓn (ξ 
n )] (ξ − ξn) . 
One can show that, as n grows, the scaled Hessian matrix ∇2 ξℓn(ξ 
n)/n converges in probability to the Fisher information matrix, which we denote as I(ξ0) [9, Section 2]. In addition, the scaled estimation error 
√ n(ξn − ξ0) converges in distribution to the 
normal distribution with mean 0 and covariance matrix I(ξ0)−1 [9, Theorem 2.2]. A generalization of the classical Cramér-Rao inequality ensures that the covariance matrix of any unbiased estimator for ξ0 is bounded below by I(ξ0)−1/n in Loewner order asymptotically for large n [32, Remark 7.9]. In conjunction, these findings suggest that Ξn = {ξ ∈ Ξ0 ∶ φn(ξ) ≥ ℓn(ξ 
n) − δ} constitutes the smallest possible (1 − α)-confidence set for ξ0 asymptotically for large n. The uncertainty set P = {P ξ ∶ ξ ∈ Ξn} therefore enjoys a statistical efficiency property. However, it fails to be rectangular [58, pp. 173]. 
Appendix B. Auxiliary Lemmas. The following results will be used throughout the main text. Their proofs are elementary and thus omitted. 
Lemma B.1 (Relations between value functions [46, Section 3.5]). For any π ∈ Π and P ∈ P we have 
(i) V P π (s) = ∑a∈A π(a∣s)QP 
π (s, a) for all s ∈ S, (ii) QP 
π (s, a) = c(s, a) + γ∑s′∈S P (s ′∣s, a)V P 
π (s ′) = ∑s′∈S P (s 
′∣s, a)GP π (s, a, s 
′) for all s ∈ S and a ∈ A, 
(iii) GP π (s, a, s 
′) = c(s, a) + γ∑a′∈A π(a′∣s′)QP π (s 
′, a′) = c(s, a) + γV P π (s 
′) for all s, s′ ∈ S and a ∈ A. 
Proof of Lemma B.1. As for Assertion (i), we have 
V P π (s) = E 
P π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s] 
= ∑ a∈A 
π(a∣s)EP π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s,A0 = a] = ∑ a∈A 
π(a∣s)QP π (s, a), 
where the second equality follows from the law of total expectation and (2.1b), and the last equality follows from the definition of QP 
π (s, a). Next, we prove Assertion (iii), which will help us to prove Assertion (ii). By the definition of GP 
π (s, a, s ′), we have 
GP π (s, a, s 
′ ) = EP 
π [ ∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s,A0 = a,S1 = s ′ ] 
= EP π [c(s, a) + 
∞ 
∑ t=1 
γtc(St,At) ∣ S1 = s ′ ] 
= c(s, a) + γ ∑ a′∈A 
EP π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s ′,A0 = a 
′ ]π(a′∣s′) 
= c(s, a) + γ ∑ a′∈A 
π(a′∣s′)QP π (s 
′, a′) 
= c(s, a) + γV P π (s 
′ ), 
where the second equality holds because {(St,At)} ∞ 
t=1 is a Markov chain and because At 
is independent of this Markov chain conditional on St under PP π . The third equality 
follows from law of total expectation and (2.1b) together with an index shift t← t + 1, the fourth equality follows from the definition of QP 
π (s, a), and the last equality follows
28 M. LI, D. KUHN, AND T. SUTTER 
from Assertion (i). As for Assertion (ii), finally, we have 
QP π (s, a) = E 
P π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s,A0 = a] 
= ∑ s′∈S 
P (s′∣s, a)EP π [ 
∞ 
∑ t=0 
γtc(St,At) ∣ S0 = s,A0 = a,S1 = s ′ ] 
= ∑ s′∈S 
P (s′∣s, a)GP π (s, a, s 
′ ) 
= c(s, a) + γ ∑ s′∈S 
P (s′∣s, a)V P π (s 
′ ), 
where the second equality follows from the law of total expectation and (2.1a), the third equality follows from the definition of GP 
π (s, a, s ′), and the fourth equality holds 
thanks to Assertion (iii). 
Lemma B.2 (Relation between the advantage function and the action-next state value function). For any P,P ′ ∈ P and π ∈ Π, we have 
∑ s′∈S (P (s′∣s, a) − P ′(s′∣s, a))GP ′ 
π (s, a, s ′ ) = ∑ 
s′∈S P (s′∣s, a)AP ′ 
π (s, a, s ′ ) ∀s ∈ S, a ∈ A. 
Lemma B.3 (Frobenius distance between policies). We have ∥π′ − π∥F ≤ √ 2S for 
any π,π′ ∈ Π. 
Inspired by [48, Lemma 3], we present a generalization of Danskin’s theorem for optimization problems with a smooth but not necessarily convex objective functions. 
Theorem B.4 (Danskin’s theorem). Let X ⊆ Rn be an open convex set, Y ⊆ Rm 
an arbitrary compact set and f ∶ X ×Y → R a continuous function such that f(x, y) is ℓ-smooth in x for each y ∈ Y and some ℓ ≥ 0. In addition, suppose that ∇xf(x, y) is continuous in y for each x ∈ X . Then, the optimal value function Φ(x) =maxy∈Y f(x, y) is ℓ-weakly convex, and its subdifferential is given by 
∂Φ(x) = conv{∇xf(x, y ⋆ ) ∣ y⋆ ∈ argmax 
y∈Y f(x, y)} . 
REFERENCES 
[1] A. Agarwal, S. Kakade, J. Lee, and G. Mahajan, On the theory of policy gradient methods: Optimality, approximation, and distribution shift, Journal of Machine Learning Research, 22 (2021), pp. 1–76. 
[2] J. Altschuler and K. Talwar, Concentration of the Langevin algorithm’s stationary distribution, arXiv preprint arXiv:2212.12629, (2022). 
[3] T. Archibald, K. McKinnon, and L. Thomas, On the generation of Markov decision processes, Journal of the Operational Research Society, 46 (1995), pp. 354–361. 
[4] C. Berge, Topological Spaces: Including a Treatment of Multi-valued Functions, Vector Spaces, and Convexity, Courier Corporation, 1997. 
[5] D. Bertsekas, Nonlinear Programming, Athena Scientific, 2016. [6] D. P. Bertsekas and J. Tsitsiklis, Neuro-Dynamic Programming, Athena Scientific, 1996. [7] J. Bhandari and D. Russo, On the linear convergence of policy gradient methods for finite 
MDPs, in International Conference on Artificial Intelligence and Statistics, 2021. [8] S. Bhatnagar, R. S. Sutton, M. Ghavamzadeh, and M. Lee, Natural actor-critic al-
gorithms, Automatica, 45 (2009), pp. 2471–2482. [9] P. Billingsley, Statistical Inference for Markov Processes, The University of Chicago Press, 
1961. [10] T. Björk and A. Murgoci, A theory of Markovian time-inconsistent stochastic control in 
discrete time, Finance and Stochastics, 18 (2014), pp. 545–592. [11] J. Blanchet, M. Lu, T. Zhang, and H. Zhong, Double pessimism is provably efficient for 
distributionally robust offline reinforcement learning: Generic algorithm and robust partial
POLICY GRADIENT ALGORITHMS FOR ROBUST MDPS 29 
coverage, arXiv preprint arXiv:2305.09659, (2023). [12] J. Chae, S. Han, W. Jung, M. Cho, S. Choi, and Y. Sung, Robust imitation learning 
against variations in environment dynamics, in International Conference on Machine Learning, 2022. 
[13] C. Daskalakis, D. J. Foster, and N. Golowich, Independent policy gradient methods for competitive reinforcement learning, in Advances in Neural Information Processing Systems, 2020. 
[14] D. Davis and D. Drusvyatskiy, Stochastic model-based minimization of weakly convex functions, SIAM Journal on Optimization, 29 (2019), pp. 207–239. 
[15] E. Delage and S. Mannor, Percentile optimization for Markov decision processes with parameter uncertainty, Operations research, 58 (2010), pp. 203–213. 
[16] J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, Efficient projections onto the ℓ1-ball for learning in high dimensions, in International Conference on Machine Learning, 2008. 
[17] M. Frank and P. Wolfe, An algorithm for quadratic programming, Naval Research Logistics Quarterly, 3 (1956), pp. 95–110. 
[18] J. Goh, M. Bayati, S. Zenios, S. Singh, and D. Moore, Data uncertainty in Markov chains: Application to cost-effectiveness analyses of medical innovations, Operations Research, 66 (2018), pp. 697–715. 
[19] H. Gong and M. Wang, A duality approach for regret minimization in average-award ergodic Markov decision processes, in Learning for Dynamics and Control, 2020. 
[20] V. Goyal and J. Grand-Clement, Robust Markov decision processes: Beyond rectangularity, Mathematics of Operations Research, 48 (2022), pp. 203–226. 
[21] J. Grand-Clément and M. Petrik, On the convex formulations of robust Markov decision processes, arXiv preprint arXiv:2209.10187, (2022). 
[22] O. Hernández-Lerma and J. Lasserre, Discrete-Time Markov Control Processes: Basic Optimality Criteria, Springer, 1996. 
[23] C.-R. Hwang, Laplace’s method revisited: Weak convergence of probability measures, The Annals of Probability, 8 (1980), pp. 1177–1182. 
[24] G. Iyengar, Robust dynamic programming, Mathematics of Operations Research, 30 (2005), pp. 257–280. 
[25] S. Kakade and J. Langford, Approximately optimal approximate reinforcement learning, in International Conference on Machine Learning, 2002. 
[26] A. Lamperski, Projected stochastic gradient Langevin algorithms for constrained sampling and non-convex learning, in Conference on Learning Theory, 2021. 
[27] Y. Le Tallec, Robust, Risk-Sensitive, and Data-Driven Control of Markov Decision Processes, PhD thesis, Massachusetts Institute of Technology, 2007. 
[28] N. Lesmana, H. Su, and C. S. Pun, Reinventing policy iteration under time inconsistency, Transactions on Machine Learning Research, (2022). 
[29] M. Li, T. Sutter, and D. Kuhn, Distributionally robust optimization with Markovian data, in International Conference on Machine Learning, 2021. 
[30] Y. Li and G. Lan, First-order policy optimization for robust policy evaluation, arXiv preprint arXiv:2307.15890, (2023). 
[31] Y. Li, T. Zhao, and G. Lan, First-order policy optimization for robust Markov decision process, arXiv preprint arXiv:2209.10579, (2022). 
[32] F. Liese and K.-J. Miescke, Statistical Decision Theory: Estimation, Testing, and Selection, Springer, 2008. 
[33] T. Lin, C. Jin, and M. I. Jordan, A nonasymptotic analysis of gradient descent ascent for nonconvex-concave minimax problems, Available at SSRN, (2022). 
[34] J. Liu and J. Ye, Efficient Euclidean projections in linear time, in International Conference on Machine Learning, 2009. 
[35] G. Loomes and R. Sugden, Disappointment and dynamic consistency in choice under uncertainty, The Review of Economic Studies, 53 (1986), pp. 271–282. 
[36] S. Mannor, O. Mebel, and H. Xu, Robust MDPs with k-rectangular uncertainty, Mathematics of Operations Research, 41 (2016), pp. 1484–1509. 
[37] S. Meyn, Control Systems and Reinforcement Learning, Cambridge University Press, 2022. [38] A. Nilim and L. El Ghaoui, Robust control of Markov decision processes with uncertain 
transition matrices, Operations Research, 53 (2005), pp. 780–798. [39] M. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming, Wiley, 
2005. [40] G. O. Roberts and R. L. Tweedie, Exponential convergence of Langevin distributions and 
their discrete approximations, Bernoulli, 2 (1996), pp. 341 – 363.
30 M. LI, D. KUHN, AND T. SUTTER 
[41] R. T. Rockafellar, Convex Analysis, Princeton University Press, 1970. [42] A. Shapiro, Time consistency of dynamic risk measures, Operations Research Letters, 40 
(2012), pp. 436–439. [43] A. Shapiro, Rectangular sets of probability measures, Operations Research, 64 (2016), pp. 528– 
541. [44] S. Sun, R. Wang, and B. An, Reinforcement learning for quantitative trading, ACM Trans-
actions on Intelligent Systems and Technology, 14 (2023), pp. 1–29. [45] T. Sutter, B. P. G. V. Parys, and D. Kuhn, A Pareto dominance principle for data-driven 
optimization, Operations Research, 72 (2024). [46] R. Sutton and A. Barto, Reinforcement Learning: An Introduction, MIT Press, 2018. [47] R. Sutton, D. McAllester, S. Singh, and Y. Mansour, Policy gradient methods for 
reinforcement learning with function approximation, in Advances in Neural Information Processing Systems, 1999. 
[48] K. K. Thekumparampil, P. Jain, P. Netrapalli, and S. Oh, Efficient algorithms for smooth minimax optimization, in Advances in Neural Information Processing Systems, 2019. 
[49] I. Usmanova, M. Kamgarpour, A. Krause, and K. Levy, Fast projection onto convex smooth constraints, in International Conference on Machine Learning, 2021. 
[50] L. Viano, Y.-T. Huang, P. Kamalaruban, C. Innes, S. Ramamoorthy, and A. Weller, Robust learning from observation with model misspecification, in International Conference on Autonomous Agents and Multiagent Systems, 2022. 
[51] L. Viano, Y.-T. Huang, P. Kamalaruban, A. Weller, and V. Cevher, Robust inverse reinforcement learning under transition dynamics mismatch, in Advances in Neural Information Processing Systems, 2021. 
[52] J. Wang, J. Zhang, H. Jiang, J. Zhang, L. Wang, and C. Zhang, Offline meta reinforcement learning with in-distribution online adaptation, in International Conference on Machine Learning, 2023. 
[53] Q. Wang, C. P. Ho, and M. Petrik, Policy gradient in robust MDPs with global convergence guarantee, in International Conference on Machine Learning, 2023. 
[54] Q. Wang, S. Xu, C. P. Ho, and M. Petrik, Policy gradient for robust Markov decision processes, arXiv preprint arXiv:2410.22114, (2024). 
[55] W. Wang and M. A. Carreira-Perpinán, Projection onto the probability simplex: An efficient algorithm with a simple proof, and an application, arXiv preprint arXiv:1309.1541, (2013). 
[56] Y. Wang and S. Zou, Policy gradient method for robust reinforcement learning, in International Conference on Machine Learning, 2022. 
[57] C. White and H. Eldeib, Markov decision processes with imprecise transition probabilities, Operations Research, 42 (1994), pp. 739–749. 
[58] W. Wiesemann, D. Kuhn, and B. Rustem, Robust Markov decision processes, Mathematics of Operations Research, 38 (2013), pp. 153–183. 
[59] Z. Zhou, Time inconsistency, precommitment, and equilibrium strategies for a Stackelberg game, SIAM Journal on Control and Optimization, 61 (2023), pp. 361–397.