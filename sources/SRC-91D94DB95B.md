> Source: https://proceedings.mlr.press/v70/achiam17a/achiam17a.pdf

Constrained Policy Optimization 
Joshua Achiam 1 David Held 1 Aviv Tamar 1 Pieter Abbeel 1 2 
Abstract 
For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior through the reward function. For example, systems that physically interact with or around humans should satisfy safety constraints. Recent advances in policy search algorithms (Mnih et al., 2016; Schul-man et al., 2015; Lillicrap et al., 2016; Levine et al., 2016) have enabled new capabilities in high-dimensional control, but do not consider the constrained setting. We propose Constrained Policy Optimization (CPO), the first generalpurpose policy search algorithm for constrained reinforcement learning with guarantees for nearconstraint satisfaction at each iteration. Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training. Our guarantees are based on a new theoretical result, which is of independent interest: we prove a bound relating the expected returns of two policies to an average divergence between them. We demonstrate the effectiveness of our approach on simulated robot locomotion tasks where the agent must satisfy constraints motivated by safety. 
1. Introduction Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et al., 2015; 2016), robot locomotion and manipulation (Schulman et al., 2015; Levine et al., 2016; Lillicrap et al., 2016), and even Go at the human grandmaster level (Silver et al., 2016). 
1UC Berkeley 2OpenAI. Correspondence to: Joshua Achiam <jachiam@berkeley.edu>. 
Proceedings of the 34 th International Conference on Machine Learning, Sydney, Australia, PMLR 70, 2017. Copyright 2017 by the author(s). 
In reinforcement learning (RL), agents learn to act by trial and error, gradually improving their performance at the task as learning progresses. Recent work in deep RL assumes that agents are free to explore any behavior during learning, so long as it leads to performance improvement. In many realistic domains, however, it may be unacceptable to give an agent complete freedom. Consider, for example, an industrial robot arm learning to assemble a new product in a factory. Some behaviors could cause it to damage itself or the plant around it—or worse, take actions that are harmful to people working nearby. In domains like this, safe exploration for RL agents is important (Moldovan & Abbeel, 2012; Amodei et al., 2016). A natural way to incorporate safety is via constraints. 
A standard and well-studied formulation for reinforcement learning with constraints is the constrained Markov Deci-sion Process (CMDP) framework (Altman, 1999), where agents must satisfy constraints on expectations of auxilliary costs. Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking. 
Currently, policy search algorithms enjoy state-of-the-art performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016). Heuristic algorithms for policy search in CMDPs have been proposed (Uchibe & Doya, 2007), and approaches based on primal-dual methods can be shown to converge to constraint-satisfying policies (Chow et al., 2015), but there is currently no approach for policy search in continuous CMDPs that guarantees every policy during learning will satisfy constraints. In this work, we propose the first such algorithm, allowing applications to constrained deep RL. 
Driving our approach is a new theoretical result that bounds the difference between the rewards or costs of two different policies. This result, which is of independent interest, tightens known bounds for policy search using trust regions (Kakade & Langford, 2002; Pirotta et al., 2013; Schulman et al., 2015), and provides a tighter connection between the theory and practice of policy search for deep RL. Here, we use this result to derive a policy improvement step that guarantees both an increase in reward and satisfaction of constraints on other costs. This step forms the basis for our algorithm, Constrained Policy Optimization (CPO), which
Constrained Policy Optimization 
computes an approximation to the theoretically-justified update. 
In our experiments, we show that CPO can train neural network policies with thousands of parameters on highdimensional simulated robot locomotion tasks to maximize rewards while successfully enforcing constraints. 
2. Related Work Safety has long been a topic of interest in RL research, and a comprehensive overview of safety in RL was given by (Garcı́a & Fernández, 2015). 
Safe policy search methods have been proposed in prior work. Uchibe and Doya (2007) gave a policy gradient algorithm that uses gradient projection to enforce active constraints, but this approach suffers from an inability to prevent a policy from becoming unsafe in the first place. Bou Ammar et al. (2015) propose a theoretically-motivated policy gradient method for lifelong learning with safety constraints, but their method involves an expensive inner loop optimization of a semi-definite program, making it unsuited for the deep RL setting. Their method also assumes that safety constraints are linear in policy parameters, which is limiting. Chow et al. (2015) propose a primal-dual subgradient method for risk-constrained reinforcement learning which takes policy gradient steps on an objective that trades off return with risk, while simultaneously learning the trade-off coefficients (dual variables). 
Some approaches specifically focus on application to the deep RL setting. Held et al. (2017) study the problem for robotic manipulation, but the assumptions they make restrict the applicability of their methods. Lipton et al. (2017) use an ‘intrinsic fear’ heuristic, as opposed to constraints, to motivate agents to avoid rare but catastrophic events. Shalev-Shwartz et al. (2016) avoid the problem of enforcing constraints on parametrized policies by decomposing ‘desires’ from trajectory planning; the neural network policy learns desires for behavior, while the trajectory planning algorithm (which is not learned) selects final behavior and enforces safety constraints. 
In contrast to prior work, our method is the first policy search algorithm for CMDPs that both 1) guarantees constraint satisfaction throughout training, and 2) works for arbitrary policy classes (including neural networks). 
3. Preliminaries A Markov decision process (MDP) is a tuple, (S,A,R, P, µ), where S is the set of states, A is the set of actions, R : S ×A× S → R is the reward function, P : S×A×S → [0, 1] is the transition probability function (where P (s�|s, a) is the probability of transitioning to state 
s� given that the previous state was s and the agent took action a in s), and µ : S → [0, 1] is the starting state distribution. A stationary policy π : S → P(A) is a map from states to probability distributions over actions, with π(a|s) denoting the probability of selecting action a in state s. We denote the set of all stationary policies by Π. 
In reinforcement learning, we aim to select a policy π which maximizes a performance measure, J(π), which is typically taken to be the infinite horizon discounted total return, J(π) 
. = E 
τ∼π [ �∞ 
t=0 γ tR(st, at, st+1)]. Here 
γ ∈ [0, 1) is the discount factor, τ denotes a trajectory (τ = (s0, a0, s1, ...)), and τ ∼ π is shorthand for indicating that the distribution over trajectories depends on π: s0 ∼ µ, at ∼ π(·|st), st+1 ∼ P (·|st, at). Letting R(τ) denote the discounted return of a trajectory, we express the on-policy value function as V π(s) 
. = 
Eτ∼π[R(τ)|s0 = s] and the on-policy action-value function as Qπ(s, a) 
. = Eτ∼π[R(τ)|s0 = s, a0 = a]. The 
advantage function is Aπ(s, a) . = Qπ(s, a)− V π(s). 
Also of interest is the discounted future state distribution, dπ , defined by dπ(s) = (1−γ) 
�∞ t=0 γ 
tP (st = s|π). It allows us to compactly express the difference in performance between two policies π�,π as 
J(π�)− J(π) = 1 
1− γ E 
s∼dπ� 
a∼π� 
[Aπ(s, a)] , (1) 
where by a ∼ π�, we mean a ∼ π�(·|s), with explicit notation dropped to reduce clutter. For proof of (1), see (Kakade & Langford, 2002) or Section 10 in the supplementary material. 
4. Constrained Markov Decision Processes A constrained Markov decision process (CMDP) is an MDP augmented with constraints that restrict the set of allowable policies for that MDP. Specifically, we augment the MDP with a set C of auxiliary cost functions, C1, ..., Cm 
(with each one a function Ci : S × A × S → R mapping transition tuples to costs, like the usual reward), and limits d1, ..., dm. Let JCi(π) denote the expected discounted return of policy π with respect to cost function Ci: JCi 
(π) = E τ∼π 
[ �∞ 
t=0 γ tCi(st, at, st+1)]. The set of 
feasible stationary policies for a CMDP is then 
ΠC . = {π ∈ Π : ∀i, JCi(π) ≤ di} , 
and the reinforcement learning problem in a CMDP is 
π∗ = arg max π∈ΠC 
J(π). 
The choice of optimizing only over stationary policies is justified: it has been shown that the set of all optimal policies for a CMDP includes stationary policies, under mild
Constrained Policy Optimization 
technical conditions. For a thorough review of CMDPs and CMDP theory, we refer the reader to (Altman, 1999). 
We refer to JCi as a constraint return, or Ci-return for 
short. Lastly, we define on-policy value functions, actionvalue functions, and advantage functions for the auxiliary costs in analogy to V π , Qπ , and Aπ , with Ci replacing R: respectively, we denote these by V π 
Ci , Qπ 
Ci , and Aπ 
Ci . 
5. Constrained Policy Optimization For large or continuous MDPs, solving for the exact optimal policy is intractable due to the curse of dimensionality (Sutton & Barto, 1998). Policy search algorithms approach this problem by searching for the optimal policy within a set Πθ ⊆ Π of parametrized policies with parameters θ (for example, neural networks of a fixed architecture). In local policy search (Peters & Schaal, 2008), the policy is iteratively updated by maximizing J(π) over a local neighborhood of the most recent iterate πk: 
πk+1 = arg max π∈Πθ 
J(π) 
s.t. D(π,πk) ≤ δ, (2) 
where D is some distance measure, and δ > 0 is a step size. When the objective is estimated by linearizing around πk as J(πk) + gT (θ − θk), g is the policy gradient, and the standard policy gradient update is obtained by choosing D(π,πk) = �θ − θk�2 (Schulman et al., 2015). 
In local policy search for CMDPs, we additionally require policy iterates to be feasible for the CMDP, so instead of optimizing over Πθ, we optimize over Πθ ∩ΠC : 
πk+1 = arg max π∈Πθ 
J(π) 
s.t. JCi(π) ≤ di i = 1, ...,m 
D(π,πk) ≤ δ. 
(3) 
This update is difficult to implement in practice because it requires evaluation of the constraint functions to determine whether a proposed point π is feasible. When using sampling to compute policy updates, as is typically done in high-dimensional control (Duan et al., 2016), this requires off-policy evaluation, which is known to be challenging (Jiang & Li, 2015). In this work, we take a different approach, motivated by recent methods for trust region optimization (Schulman et al., 2015). 
We develop a principled approximation to (3) with a particular choice of D, where we replace the objective and constraints with surrogate functions. The surrogates we choose are easy to estimate from samples collected on πk, and are good local approximations for the objective and constraints. Our theoretical analysis shows that for our choices of surrogates, we can bound our update’s worst-
case performance and worst-case constraint violation with values that depend on a hyperparameter of the algorithm. 
To prove the performance guarantees associated with our surrogates, we first prove new bounds on the difference in returns (or constraint returns) between two arbitrary stochastic policies in terms of an average divergence between them. We then show how our bounds permit a new analysis of trust region methods in general: specifically, we prove a worst-case performance degradation at each update. We conclude by motivating, presenting, and proving gurantees on our algorithm, Constrained Policy Optimiza-tion (CPO), a trust region method for CMDPs. 
5.1. Policy Performance Bounds 
In this section, we present the theoretical foundation for our approach—a new bound on the difference in returns between two arbitrary policies. This result, which is of in-dependent interest, extends the works of (Kakade & Lang-ford, 2002), (Pirotta et al., 2013), and (Schulman et al., 2015), providing tighter bounds. As we show later, it also relates the theoretical bounds for trust region policy improvement with the actual trust region algorithms that have been demonstrated to be successful in practice (Duan et al., 2016). In the context of constrained policy search, we later use our results to propose policy updates that both improve the expected return and satisfy constraints. 
The following theorem connects the difference in returns (or constraint returns) between two arbitrary policies to an average divergence between them. 
Theorem 1. For any function f : S → R and any policies π� and π, define δf (s, a, s�) 
. = R(s, a, s�)+ γf(s�)− f(s), 
�π � 
f . = max 
s |Ea∼π�,s�∼P [δf (s, a, s 
�)]| , 
Lπ,f (π �) 
. = E 
s∼dπ 
a∼π s�∼P 
�� π�(a|s) π(a|s) − 1 
� δf (s, a, s 
�) 
� , and 
D± π,f (π 
�) . = 
Lπ,f (π �) 
1− γ ± 
2γ�π � 
f 
(1− γ)2 E 
s∼dπ [DTV (π 
�||π)[s]] , 
where DTV (π �||π)[s] = (1/2) 
� a |π�(a|s)− π(a|s)| is 
the total variational divergence between action distributions at s. The following bounds hold: 
D+ π,f (π 
�) ≥ J(π�)− J(π) ≥ D− π,f (π 
�). (4) 
Furthermore, the bounds are tight (when π� = π, all three expressions are identically zero). 
Before proceeding, we connect this result to prior work. By bounding the expectation Es∼dπ [DTV (π 
�||π)[s]] with maxs DTV (π 
�||π)[s], picking f = V π , and bounding �π � 
V π
Constrained Policy Optimization 
to get a second factor of maxs DTV (π �||π)[s], we recover 
(up to assumption-dependent factors) the bounds given by Pirotta et al. (2013) as Corollary 3.6, and by Schulman et al. (2015) as Theorem 1a. 
The choice of f = V π allows a useful form of the lower bound, so we give it as a corollary. Corollary 1. For any policies π�,π, with �π 
� . = 
maxs |Ea∼π� [Aπ(s, a)]|, the following bound holds: 
J(π�)− J(π) 
≥ 1 
1− γ E 
s∼dπ 
a∼π� 
� Aπ(s, a)− 2γ�π 
� 
1− γ DTV (π 
�||π)[s] � . 
(5) 
The bound (5) should be compared with equation (1). The term (1 − γ)−1Es∼dπ,a∼π� [Aπ(s, a)] in (5) is an approximation to J(π�)− J(π), using the state distribution dπ instead of dπ 
� , which is known to equal J(π�)− J(π) to first 
order in the parameters of π� on a neighborhood around π (Kakade & Langford, 2002). The bound can therefore be viewed as describing the worst-case approximation error, and it justifies using the approximation as a surrogate for J(π�)− J(π). 
Equivalent expressions for the auxiliary costs, based on the upper bound, also follow immediately; we will later use them to make guarantees for the safety of CPO. Corollary 2. For any policies π�,π, and any cost function Ci, with �π 
� Ci 
. = maxs |Ea∼π� [Aπ 
Ci (s, a)]|, the follow-
ing bound holds: 
JCi (π�)− JCi 
(π) 
≤ 1 
1− γ E 
s∼dπ 
a∼π� 
� Aπ 
Ci (s, a) + 
2γ�π � 
Ci 
1− γ DTV (π 
�||π)[s] � . 
(6) 
The bounds we have given so far are in terms of the TV-divergence between policies, but trust region methods constrain the KL-divergence between policies, so bounds that connect performance to the KL-divergence are desirable. We make the connection through Pinsker’s inequality (Csiszar & Körner, 1981): for arbitrary distributions p, q, the TV-divergence and KL-divergence are related by DTV (p||q) ≤ 
� DKL(p||q)/2. Combining this with 
Jensen’s inequality, we obtain 
E s∼dπ 
[DTV (π �||π)[s]] ≤ E 
s∼dπ 
�� 1 
2 DKL(π�||π)[s] 
� 
≤ � 
1 
2 E 
s∼dπ [DKL(π�||π)[s]] (7) 
From (7) we immediately obtain the following. 
Corollary 3. In bounds (4), (5), and (6), make the substitution 
E s∼dπ 
[DTV (π �||π)[s]] → 
� 1 
2 E 
s∼dπ [DKL(π�||π)[s]]. 
The resulting bounds hold. 
5.2. Trust Region Methods 
Trust region algorithms for reinforcement learning (Schul-man et al., 2015; 2016) have policy updates of the form 
πk+1 = arg max π∈Πθ 
E s∼dπk 
a∼π 
[Aπk(s, a)] 
s.t. D̄KL(π||πk) ≤ δ, 
(8) 
where D̄KL(π||πk) = Es∼πk [DKL(π||πk)[s]], and δ > 0 
is the step size. The set {πθ ∈ Πθ : D̄KL(π||πk) ≤ δ} is called the trust region. 
The primary motivation for this update is that it is an approximation to optimizing the lower bound on policy performance given in (5), which would guarantee monotonic performance improvements. This is important for optimizing neural network policies, which are known to suffer from performance collapse after bad updates (Duan et al., 2016). Despite the approximation, trust region steps usually give monotonic improvements (Schulman et al., 2015; Duan et al., 2016) and have shown state-of-the-art performance in the deep RL setting (Duan et al., 2016; Gu et al., 2017), making the approach appealing for developing policy search methods for CMDPs. 
Until now, the particular choice of trust region for (8) was heuristically motivated; with (5) and Corollary 3, we are able to show that it is principled and comes with a worstcase performance degradation guarantee that depends on δ. Proposition 1 (Trust Region Update Performance). Sup-pose πk, πk+1 are related by (8), and that πk ∈ Πθ. A lower bound on the policy performance difference between πk and πk+1 is 
J(πk+1)− J(πk) ≥ − √ 2δγ�πk+1 
(1− γ)2 , (9) 
where �πk+1 = maxs ��Ea∼πk+1 
[Aπk(s, a)] ��. 
Proof. πk is a feasible point of (8) with objective value 0, so Es∼dπk ,a∼πk+1 
[Aπk(s, a)] ≥ 0. The rest follows by (5) and Corollary 3, noting that (8) bounds the average KL-divergence by δ. 
This result is useful for two reasons: 1) it is of independent interest, as it helps tighten the connection between theory and practice for deep RL, and 2) the choice to develop CPO as a trust region method means that CPO inherits this performance guarantee.
Constrained Policy Optimization 
5.3. Trust Region Optimization for Constrained MDPs 
Constrained policy optimization (CPO), which we present and justify in this section, is a policy search algorithm for CMDPs with updates that approximately solve (3) with a particular choice of D. First, we describe a policy search update for CMDPs that alleviates the issue of off-policy evaluation, and comes with guarantees of monotonic performance improvement and constraint satisfaction. Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods. 
By corollaries 1, 2, and 3, for appropriate coefficients αk, βi k the update 
πk+1 = arg max π∈Πθ 
E s∼dπk 
a∼π 
[Aπk(s, a)]− αk 
� D̄KL(π||πk) 
s.t. JCi (πk) + E 
s∼dπk 
a∼π 
� Aπk 
Ci (s, a) 
1− γ 
� + βi 
k 
� D̄KL(π||πk) ≤ di 
is guaranteed to produce policies with monotonically nondecreasing returns that satisfy the original constraints. (Ob-serve that the constraint here is on an upper bound for JCi(π) by (6).) The off-policy evaluation issue is alleviated, because both the objective and constraints involve expectations over state distributions dπk , which we presume to have samples from. Because the bounds are tight, the problem is always feasible (as long as π0 is feasible). How-ever, the penalties on policy divergence are quite steep for discount factors close to 1, so steps taken with this update might be small. 
Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: 
πk+1 =arg max π∈Πθ 
E s∼dπk 
a∼π 
[Aπk(s, a)] 
s.t. JCi (πk) + 
1 
1− γ E 
s∼dπk 
a∼π 
� Aπk 
Ci (s, a) 
� ≤ di ∀i 
D̄KL(π||πk) ≤ δ. (10) 
Because this is a trust region method, it inherits the performance guarantee of Proposition 1. Furthermore, by corollaries 2 and 3, we have a performance guarantee for approximate satisfaction of constraints: Proposition 2 (CPO Update Worst-Case Constraint Viola-tion). Suppose πk,πk+1 are related by (10), and that Πθ in (10) is any set of policies with πk ∈ Πθ. An upper bound on the Ci-return of πk+1 is 
JCi(πk+1) ≤ di + 
√ 2δγ� 
πk+1 
Ci 
(1− γ)2 , 
where � πk+1 
Ci = maxs 
��Ea∼πk+1 
� Aπk 
Ci (s, a) 
���. 
6. Practical Implementation In this section, we show how to implement an approximation to the update (10) that can be efficiently computed, even when optimizing policies with thousands of parameters. To address the issue of approximation and sampling errors that arise in practice, as well as the potential violations described by Proposition 2, we also propose to tighten the constraints by constraining upper bounds of the auxilliary costs, instead of the auxilliary costs themselves. 
6.1. Approximately Solving the CPO Update 
For policies with high-dimensional parameter spaces like neural networks, (10) can be impractical to solve directly because of the computational cost. However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KL-divergence constraint is well-approximated by second order expansion (at πk = π, the KL-divergence and its gradient are both zero). Denoting the gradient of the objective as g, the gradient of constraint i as bi, the Hessian of the KL-divergence as H , and defining ci 
. = JCi(πk) − di, the 
approximation to (10) is: 
θk+1 = argmax θ 
gT (θ − θk) 
s.t. ci + bTi (θ − θk) ≤ 0 i = 1, ...,m 
1 
2 (θ − θk) 
TH(θ − θk) ≤ δ. 
(11) Because the Fisher information matrix (FIM) H is always positive semi-definite (and we will assume it to be positive-definite in what follows), this optimization problem is convex and, when feasible, can be solved efficiently using duality. (We reserve the case where it is not feasible for the next subsection.) With B 
. = [b1, ..., bm] and 
c . = [c1, ..., cm]T , a dual to (11) can be expressed as 
max λ≥0 ν�0 
−1 
2λ 
� gTH−1g − 2rT ν + νTSν 
� + νT c− λδ 
2 , 
(12) where r 
. = gTH−1B, S . 
= BTH−1B. This is a convex program in m+1 variables; when the number of constraints is small by comparison to the dimension of θ, this is much easier to solve than (11). If λ∗, ν∗ are a solution to the dual, the solution to the primal is 
θ∗ = θk + 1 
λ∗H −1 (g −Bν∗) . (13) 
Our algorithm solves the dual for λ∗, ν∗ and uses it to propose the policy update (13). For the special case where there is only one constraint, we give an analytical solution in the supplementary material (Theorem 2) which removes the need for an inner-loop optimization. Our experiments
Constrained Policy Optimization 
Algorithm 1 Constrained Policy Optimization 
Input: Initial policy π0 ∈ Πθ tolerance α for k = 0, 1, 2, ... do 
Sample a set of trajectories D = {τ} ∼ πk = π(θk) 
Form sample estimates ĝ, b̂, Ĥ, ĉ with D if approximate CPO is feasible then 
Solve dual problem (12) for λ∗ k, ν 
∗ k 
Compute policy proposal θ∗ with (13) else 
Compute recovery policy proposal θ∗ with (14) end if Obtain θk+1 by backtracking linesearch to enforce satisfaction of sample estimates of constraints in (10) 
end for 
have only a single constraint, and make use of the analytical solution. 
Because of approximation error, the proposed update may not satisfy the constraints in (10); a backtracking line search is used to ensure surrogate constraint satisfaction. Also, for high-dimensional policies, it is impractically expensive to invert the FIM. This poses a challenge for computing H−1g and H−1bi, which appear in the dual. Like (Schulman et al., 2015), we approximately compute them using the conjugate gradient method. 
6.2. Feasibility 
Due to approximation errors, CPO may take a bad step and produce an infeasible iterate πk. Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary. In our experiments, where we only have one constraint, we recover by proposing an update to purely decrease the constraint value: 
θ∗ = θk − � 
2δ 
bTH−1b H−1b. (14) 
As before, this is followed by a line search. This approach is principled in that it uses the limiting search direction as the intersection of the trust region and the constraint region shrinks to zero. We give the pseudocode for our algorithm (for the single-constraint case) as Algorithm 1, and have made our code implementation available online.1 
6.3. Tightening Constraints via Cost Shaping 
Because of the various approximations between (3) and our practical algorithm, it is important to build a factor of safety into the algorithm to minimize the chance of constraint violations. To this end, we choose to constrain upper bounds 
1https://github.com/jachiam/cpo 
on the original constraints, C+ i , instead of the original con-
straints themselves. We do this by cost shaping: 
C+ i (s, a, s�) = Ci(s, a, s 
�) +Δi(s, a, s �), (15) 
where Δi : S × A × S → R+ correlates in some useful way with Ci. 
In our experiments, where we have only one constraint, we partition states into safe states and unsafe states, and the agent suffers a safety cost of 1 for being in an unsafe state. We choose Δ to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated at each iteration. This choice confers the additional benefit of smoothing out sparse constraints. 
7. Connections to Prior Work Our method has similar policy updates to primal-dual methods like those proposed by Chow et al. (2015), but crucially, we differ in computing the dual variables (the Lagrange multipliers for the constraints). In primal-dual optimization (PDO), dual variables are stateful and learned concurrently with the primal variables (Boyd et al., 2003). In a PDO algorithm for solving (3), dual variables would be updated according to 
νk+1 = (νk + αk (JC(πk)− d))+ , (16) 
where αk is a learning rate. In this approach, intermediary policies are not guaranteed to satisfy constraints—only the policy at convergence is. By contrast, CPO computes new dual variables from scratch at each update to exactly enforce constraints. 
8. Experiments In our experiments, we aim to answer the following: 
 Does CPO succeed at enforcing behavioral constraints when training neural network policies with thousands of parameters? 
 How does CPO compare with a baseline that uses primal-dual optimization? Does CPO behave better with respect to constraints? 
 How much does it help to constrain a cost upper bound (15), instead of directly constraining the cost? 
 What benefits are conferred by using constraints instead of fixed penalties? 
We designed experiments that are easy to interpret and motivated by safety. We consider two tasks, and train multiple different agents (robots) for each task:
Constrained Policy Optimization 
Returns: 
Constraint values: (closer to the limit is better) 
(a) Point-Circle (b) Ant-Circle (c) Humanoid-Circle (d) Point-Gather (e) Ant-Gather 
Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration. CPO drives the constraint function almost directly to the limit in all experiments, while PDO frequently suffers from over- or under-correction. TRPO is included to verify that optimal unconstrained behaviors are infeasible for the constrained problem. 
 Circle: The agent is rewarded for running in a wide circle, but is constrained to stay within a safe region smaller than the radius of the target circle. 
 Gather: The agent is rewarded for collecting green apples, and constrained to avoid red bombs. 
For the Circle task, the exact geometry is illustrated in Fig-ure 5 in the supplementary material. Note that there are no physical walls: the agent only interacts with boundaries through the constraint costs. The reward and constraint cost functions are described in supplementary material (Section 10.3.1). In each of these tasks, we have only one constraint; we refer to it as C and its upper bound from (15) as C+. 
We experiment with three different agents: a point-mass (S ⊆ R9, A ⊆ R2), a quadruped robot (called an ‘ant’) (S ⊆ R32, A ⊆ R8), and a simple humanoid (S ⊆ R102, A ⊆ R10). We train all agent-task combinations except for Humanoid-Gather. 
For all experiments, we use neural network policies with two hidden layers of size (64, 32). Our experiments are implemented in rllab (Duan et al., 2016). 
8.1. Evaluating CPO and Comparison Analysis 
Learning curves for CPO and PDO are compiled in Figure 1. Note that our constraint value graphs show C+ return, instead of the C return (except for in Point-Gather, where we did not use cost shaping due to that environment’s short time horizon), because this is what the algorithm actually constrains in these experiments. 
For our comparison, we implement PDO with (16) as the 
(a) Humanoid-Circle (b) Point-Gather 
Figure 2. The Humanoid-Circle and Point-Gather environments. In Humanoid-Circle, the safe area is between the blue panels. 
update rule for the dual variables, using a constant learning rate α; details are available in supplementary material (Sec-tion 10.3.3). We emphasize that in order for the comparison to be fair, we give PDO every advantage that is given to CPO, including equivalent trust region policy updates. To benchmark the environments, we also include TRPO (trust region policy optimization) (Schulman et al., 2015), a state-of-the-art unconstrained reinforcement learning algorithm. The TRPO experiments show that optimal unconstrained behaviors for these environments are constraint-violating. 
We find that CPO is successful at approximately enforcing constraints in all environments. In the simpler environments (Point-Circle and Point-Gather), CPO tracks the constraint return almost exactly to the limit value. 
By contrast, although PDO usually converges to constraintsatisfying policies in the end, it is not consistently constraint-satisfying throughout training (as expected). For example, see the spike in constraint value that it experi-
Constrained Policy Optimization 
ences in Ant-Circle. Additionally, PDO is sensitive to the initialization of the dual variable. By default, we initialize ν0 = 0, which exploits no prior knowledge about the environment and makes sense when the initial policies are feasible. However, it may seem appealing to set ν0 high, which would make PDO more conservative with respect to the constraint; PDO could then decrease ν as necessary after the fact. In the Point environments, we experiment with ν0 = 1000 and show that although this does assure constraint satisfaction, it also can substantially harm performance with respect to return. Furthermore, we argue that this is not adequate in general: after the dual variable decreases, the agent could learn a new behavior that increases the correct dual variable more quickly than PDO can attain it (as happens in Ant-Circle for PDO; observe that performance is approximately constraint-satisfying until the agent learns how to run at around iteration 350). 
We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. CPO quickly stabilizes the constraint return around to the limit value, while PDO is not consistently able to enforce constraints all throughout training. 
8.2. Ablation on Cost Shaping 
In Figure 3, we compare performance of CPO with and without cost shaping in the constraint. Our metric for comparison is the C return, the ‘true’ constraint. The cost shaping does help, almost completely accounting for CPO’s inherent approximation errors. However, CPO is nearly constraint-satisfying even without cost shaping. 
8.3. Constraint vs. Fixed Penalty 
In Figure 4, we compare CPO to a fixed penalty method, where policies are learned using TRPO with rewards R(s, a, s�)− νC+(s, a, s�) for ν ∈ {1, 5, 50}. 
We find that fixed penalty methods can be highly sensitive to the choice of penalty coefficient: in Ant-Circle, a penalty coefficient of 1 results in reward-maximizing policies that accumulate massive constraint costs, while a coefficient of 5 (less than an order of magnitude difference) results in cost-minimizing policies that never learn how to acquire any rewards. In contrast, CPO automatically picks penalty coefficients to attain the desired trade-off between reward and constraint cost. 
9. Discussion In this article, we showed that a particular optimization problem results in policy updates that are guaranteed to both improve return and satisfy constraints. This enabled the development of CPO, our policy search algorithm for CMDPs, which approximates the theoretically-guaranteed 
(a) Ant-Circle Return (b) Ant-Gather Return 
(c) Ant-Circle C Return (d) Ant-Gather C Return 
Figure 3. Using cost shaping (CS) in the constraint while optimizing generally improves the agent’s adherence to the true constraint on C return. 
(a) Ant-Circle Return (b) Ant-Circle C+-Return 
Figure 4. Comparison between CPO and FPO (fixed penalty optimization) for various values of fixed penalty. 
algorithm in a principled way. We demonstrated that CPO can train neural network policies with thousands of parameters on high-dimensional constrained control tasks, simultaneously maximizing reward and approximately satisfying constraints. Our work represents a step towards applying reinforcement learning in the real world, where constraints on agent behavior are sometimes necessary for the sake of safety. 
Acknowledgements The authors would like to acknowledge Peter Chen, who independently and concurrently derived an equivalent policy improvement bound. 
Joshua Achiam is supported by TRUST (Team for Re-search in Ubiquitous Secure Technology) which receives support from NSF (award number CCF-0424422). This
Constrained Policy Optimization 
project also received support from Berkeley Deep Drive and from Siemens. 
References Altman, Eitan. Constrained Markov Decision Processes. 
pp. 260, 1999. ISSN 01676377. doi: 10.1016/ 0167-6377(96)00003-X. 
Amodei, Dario, Olah, Chris, Steinhardt, Jacob, Christiano, Paul, Schulman, John, and Mané, Dan. Concrete Prob-lems in AI Safety. arXiv, 2016. URL http://arxiv. org/abs/1606.06565. 
Bou Ammar, Haitham, Tutunov, Rasul, and Eaton, Eric. Safe Policy Search for Lifelong Reinforcement Learning with Sublinear Regret. International Conference on Ma-chine Learning, 37:19, 2015. URL http://arxiv. org/abs/1505.0579. 
Boyd, Stephen, Xiao, Lin, and Mutapcic, Almir. Subgra-dient methods. Lecture Notes of Stanford EE392, 2003. URL http://xxpt.ynjgy.com/resource/ data/20100601/U/stanford201001010/ 02-subgrad{_}method{_}notes.pdf. 
Chow, Yinlam, Ghavamzadeh, Mohammad, Janson, Lucas, and Pavone, Marco. Risk-Constrained Reinforcement Learning with Percentile Risk Criteria. Journal of Ma-chine Learning Research, 1(xxxx):1–49, 2015. 
Csiszar, I and Körner, J. Information Theory: Coding Theorems for Discrete Memoryless Systems. Book, 244:452, 1981. ISSN 0895-4801. doi: 10.2307/ 2529636. URL http://www.getcited.org/ pub/102082957. 
Duan, Yan, Chen, Xi, Schulman, John, and Abbeel, Pieter. Benchmarking Deep Reinforcement Learning for Con-tinuous Control. The 33rd International Conference on Machine Learning (ICML 2016) (2016), 48:14, 2016. URL http://arxiv.org/abs/1604.06778. 
Garcı́a, Javier and Fernández, Fernando. A Comprehensive Survey on Safe Reinforcement Learning. Journal of Ma-chine Learning Research, 16:1437–1480, 2015. ISSN 15337928. 
Gu, Shixiang, Lillicrap, Timothy, Ghahramani, Zoubin, Turner, Richard E., and Levine, Sergey. Q-Prop: Sample-Efficient Policy Gradient with An Off-Policy Critic. In International Conference on Learning Repre-sentations, 2017. URL http://arxiv.org/abs/ 1611.02247. 
Held, David, Mccarthy, Zoe, Zhang, Michael, Shentu, Fred, and Abbeel, Pieter. Probabilistically Safe Policy 
Transfer. In Proceedings of the IEEE International Con-ference on Robotics and Automation (ICRA), 2017. 
Jiang, Nan and Li, Lihong. Doubly Robust Off-policy Value Evaluation for Reinforcement Learning. Interna-tional Conference on Machine Learning, 2015. URL http://arxiv.org/abs/1511.03722. 
Kakade, Sham and Langford, John. Approximately Optimal Approximate Reinforcement Learning. Proceedings of the 19th International Conference on Machine Learning, pp. 267–274, 2002. URL http://www.cs.cmu.edu/afs/cs/Web/ People/jcl/papers/aoarl/Final.pdf. 
Levine, Sergey, Finn, Chelsea, Darrell, Trevor, and Abbeel, Pieter. End-to-End Training of Deep Visuo-motor Policies. Journal of Machine Learning Re-search, 17:1–40, 2016. ISSN 15337928. doi: 10.1007/ s13398-014-0173-7.2. 
Lillicrap, Timothy P., Hunt, Jonathan J., Pritzel, Alexander, Heess, Nicolas, Erez, Tom, Tassa, Yuval, Silver, David, and Wierstra, Daan. Continuous control with deep reinforcement learning. In International Conference on Learning Representations, 2016. ISBN 2200000006. doi: 10.1561/2200000006. 
Lipton, Zachary C., Gao, Jianfeng, Li, Lihong, Chen, Jianshu, and Deng, Li. Combating Deep Reinforce-ment Learning’s Sisyphean Curse with Intrinsic Fear. In arXiv, 2017. ISBN 2004012439. URL http: //arxiv.org/abs/1611.01211. 
Mnih, Volodymyr, Kavukcuoglu, Koray, Silver, David, Rusu, Andrei a, Veness, Joel, Bellemare, Marc G, Graves, Alex, Riedmiller, Martin, Fidjeland, Andreas K, Ostrovski, Georg, Petersen, Stig, Beattie, Charles, Sadik, Amir, Antonoglou, Ioannis, King, Helen, Kumaran, Dharshan, Wierstra, Daan, Legg, Shane, and Hassabis, Demis. Human-level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015. ISSN 0028-0836. doi: 10.1038/nature14236. URL http: //dx.doi.org/10.1038/nature14236. 
Mnih, Volodymyr, Badia, Adrià Puigdomènech, Mirza, Mehdi, Graves, Alex, Lillicrap, Timothy P., Harley, Tim, Silver, David, and Kavukcuoglu, Koray. Asynchronous Methods for Deep Reinforcement Learning. pp. 1– 28, 2016. URL http://arxiv.org/abs/1602. 01783. 
Moldovan, Teodor Mihai and Abbeel, Pieter. Safe Explo-ration in Markov Decision Processes. Proceedings of the 29th International Conference on Machine Learn-ing, 2012. URL http://arxiv.org/abs/1205. 4810.
Constrained Policy Optimization 
Ng, Andrew Y., Harada, Daishi, and Russell, Stuart. Pol-icy invariance under reward transformations : Theory and application to reward shaping. Sixteenth Inter-national Conference on Machine Learning, 3:278–287, 1999. doi: 10.1.1.48.345. 
Peters, Jan and Schaal, Stefan. Reinforcement learning of motor skills with policy gradients. Neural Networks, 21 (4):682–697, 2008. ISSN 08936080. doi: 10.1016/j. neunet.2008.02.003. 
Pirotta, Matteo, Restelli, Marcello, and Calandriello, Daniele. Safe Policy Iteration. Proceedings of the 30th International Conference on Machine Learning, 28, 2013. 
Schulman, John, Moritz, Philipp, Jordan, Michael, and Abbeel, Pieter. Trust Region Policy Optimization. In-ternational Conference on Machine Learning, 2015. 
Schulman, John, Moritz, Philipp, Levine, Sergey, Jordan, Michael, and Abbeel, Pieter. High-Dimensional Contin-uous Control Using Generalized Advantage Estimation. arXiv, 2016. 
Shalev-Shwartz, Shai, Shammah, Shaked, and Shashua, Amnon. Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving. arXiv, 2016. URL http: //arxiv.org/abs/1610.03295. 
Silver, David, Huang, Aja, Maddison, Chris J., Guez, Arthur, Sifre, Laurent, van den Driessche, George, Schrittwieser, Julian, Antonoglou, Ioannis, Panneer-shelvam, Veda, Lanctot, Marc, Dieleman, Sander, Grewe, Dominik, Nham, John, Kalchbrenner, Nal, Sutskever, Ilya, Lillicrap, Timothy, Leach, Madeleine, Kavukcuoglu, Koray, Graepel, Thore, and Hassabis, Demis. Mastering the game of Go with deep neural networks and tree search. Nature, 529(7587): 484–489, 2016. ISSN 0028-0836. doi: 10.1038/ nature16961. URL http://dx.doi.org/10. 1038/nature16961. 
Sutton, Richard S and Barto, Andrew G. Introduction to Reinforcement Learning. Learning, 4(1996):1–5, 1998. ISSN 10743529. doi: 10.1.1.32.7692. URL http:// dl.acm.org/citation.cfm?id=551283. 
Uchibe, Eiji and Doya, Kenji. Constrained reinforcement learning from intrinsic and extrinsic rewards. 2007 IEEE 6th International Conference on Development and Learning, ICDL, (February):163–168, 2007. doi: 10. 1109/DEVLRN.2007.4354030.