> Source: https://arxiv.org/pdf/1902.08708

Distributionally Robust Reinforcement Learning 
Elena Smirnova 1 Elvis Dohmatob 1 Jeremie Mary 1 
Abstract Real-world applications require RL algorithms to act safely. During learning process, it is likely that the agent executes sub-optimal actions that may lead to unsafe/poor states of the system. Explo-ration is particularly brittle in high-dimensional state/action space due to increased number of lowperforming actions. In this work, we consider risk-averse exploration in approximate RL setting. To ensure safety during learning, we propose the distributionally robust policy iteration scheme that provides lower bound guarantee on state-values. Our approach induces a dynamic level of risk to prevent poor decisions and yet preserves the convergence to the optimal policy. Our formulation results in a efficient algorithm that accounts for a simple re-weighting of policy actions in the standard policy iteration scheme. We extend our approach to continuous state/action space and present a practical algorithm, distributionally robust soft actor-critic, that implements a different exploration strategy: it acts conservatively at short-term and it explores optimistically in a long-run. We provide promising experimental results on continuous control tasks. 
1. Introduction At root of difficulties to deploy Reinforcement Learning in the real-world is the problem of exploration. In all generality, in order to guarantee the optimality of a policy we need to build estimates of all state-values that may result in some occasional catastrophic outcomes. This is of course unacceptable in many applications, such as real-world robot tasks (Abbeel & Ng, 2005) or online recommendation systems (Theocharous et al., 2015). One strategy to avoid disastrous events is to lower the risk in face of uncertainty. 
In this work, we consider risk-averse exploration in the con-
1Criteo AI Lab. Correspondence to: Elena Smirnova <e.smirnova@criteo.com>. 
Reinforcement Learning for Real Life (RL4RealLife) Workshop in the 36 th International Conference on Machine Learning, Long Beach, California, USA, 2019. Copyright 2019 by the author(s). 
text of modified policy iteration (MPI) scheme (Puterman, 1994). MPI defines an iterative process that alternates between policy improvement and (partial) policy evaluation steps. Applying this scheme to practical problems with large state/action space and finite number of interactions leads to errors at the policy evaluation step, resulting in the approximate MPI scheme (Scherrer et al., 2015). In the approximate MPI the policy state-values are inexact, and thus, exploration strategies, such as Boltzmann exploration, are likely to execute poor actions (Garcıa & Fernández, 2015). 
Prior works studied safety guarantees w.r.t. approximate policy evaluation step. Risk-sensitive approach explicitly modifies the policy’s long-term outcome to incorporate the notion of risk, typically expressed as variance of return over policy trajectories. In approximate dynamic programming, risk-sensitive counterparts of value iteration and policy iteration have been developed (Tamar et al., 2013; Prashanth & Ghavamzadeh, 2016), although they are known to result in computationally difficult algorithms (Mannor & Tsitsik-lis, 2011). In model-free setting, the proposed algorithms are computationally extensive as they involve integration over the state space and nonconvex parameter optimization. To mitigate this issue, approximation schemes have been proposed based on temporal differences (Mihatsch & Ne-uneier, 2002), stochastic approximation (Borkar, 2002) and recently, policy gradient (Tamar et al., 2015). 
In this paper, we consider the inexact computation of policy state-values due to the finite number of interactions with the environment, called estimation errors. The risk-averse strategy consists in lowering the risk of catastrophic outcome under estimation errors. To implement risk-averse strategy, we introduce a family of distributionally robust Bellman operators that provide lower bound guarantee on policy statevalues. Using this operator instead of standard Bellman operator, we formulate a distributionally robust modified policy iteration scheme that places an adaptive level of conservatism w.r.t estimation errors at policy evaluation step. Differently from prior work, our proposed algorithms are computationally tractable and preserve convergence to the optimal policy at growing amount of collected experience. 
Using the Legendre-Fenchel transform (Boyd & Vanden-berghe, 2004), our formulation results in a simple modification to the standard policy iteration scheme that consists in 
 
 
 
 
 
 
 
 
 
 
 
Distributionally robust reinforcement learning 
computing the evaluation step w.r.t. re-weighted policy stateaction probabilities. The proposed algorithm is applicable to large state spaces since the additional computation scales with the size of the action space. For continuous action space, we derive an efficient approximation of our scheme that only involves a constant-time reward modification. 
We propose a practical algorithm for continuous control tasks, called distributionally robust soft actor-critic, by combining risk-averse policy evaluation under finite sample of data with optimistic exploration of Soft Actor-Critic (Haarnoja et al., 2018b). Distributionally robust soft actor-critic implements a different exploration strategy: it acts conservatively at short-term to ensure the lower bound on policy performance, and it explores optimistically at long-term to preserve convergence to the optimal policy. 
To summarize, our main contributions are as follows: 
 We propose a principled and scalable modification of MPI that ensures risk-averse policy evaluation w.r.t. estimation errors, while preserving convergence to the optimal policy. Convergence rate is analyzed. 
 We apply this scheme to maximum entropy policies that results in a risk-averse short-term and optimistic long-term exploration strategy. 
 We derive an extension of our scheme to the continuous state/action space that only involves a modification of reward. We provide promising experimental results on continuous control tasks. 
2. Preliminaries We will use the following notation: ∆X is the set of probability distributions over a finite set X and Y X is a set of mappings from set X to set Y . 
We consider a Markov decision process M := (S,A, P, r, γ) where S is a finite state space, A is a finite action space, P ∈ ∆S×AS is the transition kernel with transition probability p(s′|s, a), r(s, a) ∈ RS×A, |r(s, a)| ≤ Rmax is a bounded reward function. We define a stochastic stationary policy π ∈ ∆SA and let Π be the set of stochastic stationary policies. We consider the discounted setting with discount factor γ ∈ [0, 1). 
We define the Bellman operator T π for any function V ∈ RS , ∀s ∈ S as follows: 
[T πV ](s) := Ea∼π(·|s) [ r(s, a) + γEs′∼p(s′|s,a)[V (s′)] 
] (1) 
This is a γ-contraction in `∞ norm and its unique fixed point is V π: limk→∞(T π)kV = V π, where equality holds component-wise. By denoting QV (s, a) := r(s, a) + 
γEs′∼p(s′|s,a)[V (s′)], Eq. (1) can be re-written as: 
[T πV ](s) = 〈π(·|s), QV (s, ·)〉. (2) 
From (1), we define the Bellman optimality operator as follows: 
[T ?V ](s) := max π(·|s)∈∆(A) 
[T πV ](s) ∀s ∈ S, (3) 
which is a γ-contraction in `∞ norm and its unique fixed point is the optimal value function V ?. Further, the equalities hold state-wise, so we will omit the per-state notation and write T ?V = maxπ∈Π T πV . 
We denote by G(V ) the set of optimal policies that achieve the maximum of Eq. (3) state-wise: 
G(V ) := {π : π ∈ arg max π∈Π 
TπV } (4) 
Equivalently, this set coincides with the set of optimal policies: G(V ) = {π : T πV = T ?V }. 
The Modified Policy Iteration (MPI) algorithm (Puterman, 1994) is the iterative process that alternates between policy improvement and (partial) policy evaluation steps: 
πt+1 ∈ G(Vt); Vt+1 = (T πt+1)mVt (5) 
where m = 1 corresponds to Value Iteration and m = ∞ corresponds to Policy Iteration. Here Vt denotes an approximation of V πt . 
Finally, we will make use of the Legendre-Fenchel duality, e.g. see Section 3.3.1 in (Boyd & Vandenberghe, 2004). For a strongly convex function Ω : ∆(A)→ R its Fenchel dual Ω? : RA → R is given by: 
Ω?(QV ) = max π∈∆(A) 
〈π,QV 〉 − Ω(π). (6) 
Using properties of the Fenchel transform at the maximum of the of (6) we have for the gradient of the dual function: 
∇Ω?(QV ) = arg max π∈∆(A) 
〈π,QV 〉 − Ω(π) (7) 
Similarly to standard Bellman operators, we define the regularized Bellman operator (Geist et al., 2019) as follows: 
T π,ΩV := T πV − Ω(π). (8) 
and the set of optimal policies: 
GΩ(V ) := {π : π ∈ arg max π∈Π 
T π,ΩV = ∇Ω?(QV )} (9)
Distributionally robust reinforcement learning 
3. Distributionally robust policy iteration We consider the Approximate Modified Policy Iteration scheme (Scherrer et al., 2015), where the evaluation step in (5) is subject to an estimation error δt due to finite sample of transitions used to perform evaluation: 
πt+1 ∈ G(Ṽt); Ṽt+1 = T πt+1 Ṽt + δt. (10) 
This is indeed a practical scenario as state-of-the-art offpolicy algorithms sample a mini-batch of independent samples from a replay buffer to perform value update (Mnih et al., 2013); on-policy algorithms directly draw a finite number of trajectories from πt+1 (Schulman et al., 2015). 
Due to the finite amount of collected experience, the value Vt is uncertain. The uncertainty of empirical estimate is captured by its variance and is known under parametric uncertainty (Mannor et al., 2004). Optimistic exploration strategies (Auer et al., 2002; Jaksch et al., 2010) are classically used under parametric uncertainty. They construct, at any state, an optimistically biased value estimate and take action with the highest value. If the selected action is not near-optimal, i.e., the value estimates are overly-optimistic, it may lead to unsafe states of the system. Therefore, to prevent the exploration process from catastrophic outcomes, we consider the notion of safety under finite sample estimates. 
In Section 3.1 we introduce a family of Bellman operators that guarantee policy performance with finite-sample bounds. Section 3.2 describes their efficient computation and the resulting policy iteration scheme. Theorem 1 establishes the asymptotic convergence of the proposed scheme to the optimal policy, while reducing the chance of catastrophic failure. In Section 3.3 we apply this scheme to a class of maximum entropy policies. The resulting algorithm is expected to achieve, under parametric uncertainty, a risk-averse behaviour at short-term time horizon and a risk-seeking behaviour in a long-run. 
3.1. Distributionally robust Bellman operator 
We formalize the risk-averse strategy under estimation errors in approximate MPI scheme (10). We define a family of operators that represent a lower bound on the exact operator given a sequence of convergent errors. 
Definition 1 (Distributionally robust Bellman operator). For a sequence of error vectors ε1, ε2, . . . , εt, . . . ∈ RS , we say that an operator T πtεt : RS → RS is distributionally robust if 
 T πtεt is a Bellman operator and provides a lower bound on T πt at finite time: 
T πtεt v ≤ T πtv ≤ T πtεt v + εt, ∀v ∈ RS . (11) 
 The errors εt are controllable: 
lim sup N→∞ 
N−1∑ t=1 
γt‖εN−t‖∞ = 0. (12) 
This Bellman operator provides robustness w.r.t finite sample of observations, represented by the estimation error εt that should decrease with the amount of collected experience. Condition (12) on the sequence of errors εt implies an asymptotic convergence to the exact evaluation step of (5). The next lemma formally introduces this statement. 
Lemma 1 ( (Scherrer et al., 2015)). For any initial value function V0 consider the approximate MPI Ṽt = (T πt)mṼt−1 + δt (with Ṽ0 = V0); πt+1 ∈ G(Vt). Then, one has 
‖ṼN − V ∗‖∞ ≤ 4Rmax 
(1− γ)2 EN + 
2γN 
1− γ ‖V0 − V ∗‖∞, 
where EN := ∑N−1 t=1 γt‖δN−t‖∞. 
Remark. By Def. 1 the approximate MPI using distributionally robust operator is convergent if the sum of discounted uncertainties satisfies lim supN→∞ 
∑N−1 t=1 γt‖εN−t‖∞ = 
0. This is because |δt(s)| ≤ εt(s) ∀s for some global constant , and so lim supN EN ≤  lim supN 
∑N−1 t=1 γt‖εN−t‖∞ = 0. 
Later, we will consider specific constructions of the error sequences in the form εt ∝ nt(s) 
−η, for some η > 0, where nt(s) is a state visitation count. We will show that for this construction of error sequence, the approximate MPI scheme with distributionally robust Bellman operator converges to the optimal policy-value pair (see Theorem 1). 
One way to implement the distributionally robust Bellman operator is to consider the worst-case outcome of executing each action. Indeed, placing adequate uncertainty on action probabilities prevents the agent from selecting possibly low-value actions. We implement this idea in a variant of distributionally robust Bellman operator. 
Definition 2 (Uncertainty set and adversarial Bellman operator). Given a policy π and an error function ε ∈ RS , define the uncertainty set Uε(π) by 
Uε(π) := {π̃ ∈ ∆SA | DKL(π̃(·|s)‖π(·|s)) ≤ ε(s), ∀s ∈ S}, (13) 
Also define the (KL-based) adversarial Bellman operator T πε : RS → RS by 
T π ε 
V := min π̃∈Uε(π) 
T π̃V. (14) 
Proposition 1. T πε is a valid Bellman operator (i.e a monotone `∞-norm γ-contraction mapping on value functions) T πε . Moreover, T πε is distributionally robust.
Distributionally robust reinforcement learning 
Proof. Since mapping T πε is continuous in π and Uε is compact, it follows from the Extreme Value Theorem that there exists a policy πε ∈ Uε such that T πε = T πε . Thus, T πε is a valid Bellman operator. In addition, from (14) there exists a policy πε ∈ Uε such that T πε ≤ T π̃ ∀π̃ ∈ Uε(πt) including πt. This proves the left inequality in (11). The right inequality follows from Lemma 2 (see Appendix) using Pinsker’s inequality. 
The minimization problem of adversarial Bellman operator defines an adversarial policy πε to π as the worst-case realization from the uncertainty set defined in terms of Kullback-Leibler (KL) divergence. The degree of adversarial behaviour is controlled by the size of uncertainty set. 
3.2. Distributionally robust policy evaluation 
In the following, we derive an efficient computation scheme of adversarial Bellman operator (14). We show that it results in simple analytical expression for adversarial policy where the robustification appears as re-weighting of samples based on the adversarial distribution. 
First, we note that the KL constraint in (13) is separable by state and is strongly convex w.r.t. π̃. This makes possible to explicitly express the minimizer πε of (14), i.e. the worst-case policy from the uncertainty set, thanks to the Legendre-Fenchel transform (6). We proceed by applying strong Lagrangian duality and re-writing as maximization problem: 
[T π ε 
V ](s) = max λ(s)>0 
min π̃∈∆(A) 
[T π̃V ](s) 
+ λ(s)DKL(π̃(·|s)‖π(·|s))− λ(s)ε(s) 
= min λ(s)>0 
max π∈∆(A) 
[−T πV ](s) 
− λ(s)DKL(π̃(·|s)‖π(·|s)) + λ(s)ε(s) 
(15) 
where λ(s) is a per-state positive Lagrange multiplier. 
Next, using Fenchel duality (6) in the case of KL-divergence, the solution to the inner maximization problem of (15) is given by the gradient of Fenchel convex conjugate (7) : 
πε(a|s;λ) ∝ exp(−QV (s, a)/λ(s))π(a|s) (16) 
The analytical expression for the adversarial policy has the following interpretation: the adversarial policy re-weights the sampling policy such that the worst-case actions are taken more frequently to the extent determined by the adversarial temperature λ(s). Infinitely small uncertainty set ε → 0+ results in λ → +∞, i.e. the adversarial policy taking the same actions as the optimizing policy. On the other hand, a too large uncertainty set ε → +∞ leads to conservative policies as λ→ 0+. 
To connect the radius of uncertainty set ε to the optimal state-dependent parameter λ?(s), we consider the solution to the 
outer Lagrangian dual problem in (15). By representing the inner maximization problem of (15) in terms of its Fenchel dual (6), we obtain: 
λ?(s) := arg min λ(s)>0 
Ω? (−QV /λ(s)) + λ(s)ε(s). (17) 
This formulation is a 1-d convex optimization over a perstate expression that defines the optimal level of adversarial behaviour. 
We summarize the presented results in the following. 
Corollary 1. The adversarial Bellman operator (14) can be expressed as a regularized Bellman operator (8) w.r.t. adversarial policy (16) with optimal λ?(s) defined in (17). The associated distributionally robust modified policy iteration scheme is given by:{ 
πt+1 ← G(Ṽt) 
Ṽt+1 ← (T π εt t+1)mṼt 
(18) 
We now analyze the convergence of this scheme. Theorem 1 states than any convergent and consistent Bellman operator iteration can be made distributionally robust using (18) and yet converges to the optimal policy in terms of the `∞ norm. The convergence rate of (18) is polynomial instead of exponential in exact MPI (5). 
Theorem 1 (Distributionally robust modified policy iteration). For an integer m ∈ [1,∞], consider the distributionally robust MPI scheme (18), where 
εt(s) = 
{ Cnt(s) 
−η, if nt(s) ≥ t/S, 0, else, 
for some constants C, η > 0 and S denotes the number of states. 
Let ˜̀ t := Ṽt − V ∗ ∈ RS be the loss at iteration t. Then 
after N ≥ 2 iterations, we have 
(A) Sub-optimality bound: 
‖˜̀N‖∞ ≤ 4Rmax 
(1− γ)2 EN + 
2γN 
1− γ ‖˜̀0‖∞, 
where 
EN := 
N−1∑ t=1 
γt‖δN−t‖∞ = ON ( 
CSη 
(1− γ)Nη 
) −→ 0. 
(B) Safety guarantee: 
Ṽt ≤ Vt ≤ V ∗, ∀t ∈ {1, . . . , N}, 
where Vt is the value function computed via exact evaluation step (5).
Distributionally robust reinforcement learning 
Proof. See Appendix A.1. 
Remark. Parameters C and η define the size of uncertainty set, thus, the degree of robustness of the policy. The lower levels imply higher robustness and slower convergence. 
Remark. The condition nt(s) ≥ t/S ensures that states with too few visits are not considered for the uncertainty set construction. The choice η = 1/2 leads to the bound EN = 
ON ( √ 
S (1−γ) 
√ N 
) . It is can be motivated by the general fact 
that empirical means (obtained from finite samples) are within O(1/ 
√ N) of their expected values. 
The pseudo-code corresponding to scheme (18) is presented in Algorithm 1. To implement this algorithm, it is sufficient to learn on samples from adversarial policy. One possibility to do so is to re-sample transitions based on the target distribution, e.g., using importance sampling. Alternatively, one can directly generate samples from the adversarial policy. 
3.3. Extension to entropy-regularized policies 
We apply the distributionally robust approach to the maximum entropy framework (Ziebart et al., 2008; Haarnoja et al., 2017) that has been recently successful on a variety of simulated and real-world tasks (Haarnoja et al., 2018b). The maximum entropy objective modifies the standard RL objective by adding a per-state entropy bonus. This results in improved exploration targeted at high-value actions (Haarnoja et al., 2018a). To obtain robustness guarantees on exploration process, we apply the distributionally robust policy iteration scheme (18) to entropy-regularized policies. 
We define soft adversarial Bellman operator as follows: 
T π ε,ΩV := min 
π̃∈Uε(π) T π̃,ΩV, (19) 
where Ω(π(·|s)) = αH(π(·|s)) ∀s ∈ S. 
Proposition 2. T πε,Ω is a valid Bellman operator (i.e a monotone `∞-norm γ-contraction mapping on value functions). Moreover, T πε,Ω is distributionally robust. 
Proof. T π,Ω is a γ-contraction w.r.t to the `∞-norm on value functions (Geist et al., 2019). Analoguously to T πε , T πε,Ω has a solution in the set of policies since Uε(π) is compact and T π,Ω is continuous in π. 
The solution to regularized maximization problem (9) at the policy improvement step is given by the gradient of Fenchel dual (9), also referred in the literature to the Boltzmann policy: 
π(a|s) ∝ exp(QV (s, a)/α) (20) 
where α > 0 is the exploration temperature. Thus, the adversarial policy (16) takes the following form: 
πε(a|s;α, λ) ∝ exp((1/α− 1/λ(s))QV (s, a)) (21) 
The resulting soft distributionally robust modified policy iteration scheme is given by:{ 
πt+1 ← GΩ(Ṽt) 
Ṽt+1 ← (T π εt t+1,Ω)mṼt. 
(22) 
This is the counterpart of scheme (18) for regularized policies. The difference lies in the presence of the regularizer Ω in both greedy and evaluation steps. Note that, as in (18), the evaluation step is performed w.r.t adversarial policy (21), while the greedy step is done w.r.t. Boltzmann policy (20). 
The scheme (22) different in nature from Soft Q-learning (Haarnoja et al., 2017) and other entropy-based approaches (Nachum et al., 2017; Haarnoja et al., 2018a). Despite apparent similarity in automatic temperature tuning, the scheme (22) adjusts temperature to provide a lower bound guarantee on policy state-values, while the abovementioned entropy-based approaches adjust temperature to ensure a target entropy level alike a re-parametrization. Moreover, the temperature adjustment in our scheme (22) is only performed at the policy evaluation step. 
Since approximate regularized MPI shares the same error propagation bounds as unregularized MPI according to Corollary 1 of (Geist et al., 2019), the convergence of scheme (22) is an adaptation of Theorem 1. 
Algorithm 1 Distributionally Robust Policy Iteration Initialize V , counters n = 0 {Initialize} Set C, η > 0 repeat π ← G(V ) {Maximizing policy} ε← Cn−η {Size of uncertainty size} λ← optimization of (17) {Regularization parameter} πε ∝ exp(−QV /λ)π {Adversarial policy} V ← T πεV {Adversarial Bellman operator} 
until convergence 
4. Continuous control Real-world applications frequently operate in continuous state/action space. To extend the distributionally robust approach to continuous setup, we need to efficiently compute the adversarial Bellman operator in (18). Thus, in Section 4.1 we derive an approximated scheme for KL-regularized Bellman operators that only involves a modification of reward. This allows us to formulate distributionally robust soft actor-critic, a practical algorithm that applies the soft distributional robustness scheme (22) to the soft actorcritic algorithm (Haarnoja et al., 2018b) (see Section 4.2).
Distributionally robust reinforcement learning 
4.1. KL-regularized Bellman operator 
The regularized Bellman operator can be written in terms of its Fenchel conjugate (6): [T ΩV ](s) = Ω?(QV (s, ·)). De-fine the regularization parameter λ such that Ωλ(π(·|s)) := λΩ(π(·|s)) and consider the case of KL-divergence based regularization with respect to the prior policy µ ∈ ∆AS : Ω(π(·|s)) = −DKL(π(·|s)||µ(·|s)). Then, the Fenchel conjugate is given by the smoothed maximum (minimum): 
Ω?λ(QV (s, ·)) = λ logEa∼µ(·|s) exp(QV (s, a)/λ) (23) 
for λ > 0 (λ < 0) respectively. 
When the action space is continuous, the computation of the dual function (23) is intractable. To overcome the problem, we derive computationally feasible approximation of the smoothed maximum (minimum) function. We notice that smoothed maximum (minimum) can be seen as the logarithm of moment-generating function of the dual variable. By performing Taylor expansion of the moment-generating function around λ → +∞ (λ → −∞) and keeping terms up to the 1st order, we obtain: 
Ω?λ(QV (s, ·)) = Ea∼µ[QV (s, a)] 
+ 1 
2λ Vara∼µ(QV (s, a)) +O 
( 1 
λ2 
) . 
(24) 
This approximation gives a new perspective on KL-divergence regularized Bellman operators as encouraging (λ > 0) or penalizing variance (λ < 0) of Q-values under action distribution induced by the prior policy. The parameter λ controls the amount of the regularization. In this view, distributionally robust Bellman operator can be seen as data-driven per-state variance penalization that adapts to the degree of uncertainty over the finite sample of data. 
Approximation (24) provides an efficient way to compute the regularized Bellman operator through a simple modification of reward. Indeed, define potential function Φ(s) ∈ RS as weighted variance of Q-values under the prior policy 
Φ(s) := 1 
2λ Vara∼µ(QV (s, a)) 
and a reward shaping function rΩ(s, a, s′) ∈ RS×A×S as 
rΩ(s, a, s′) := r(s, a) + γΦ(s′)− Φ(s). (25) 
Then, by applying Corollary 2 of (Ng et al., 1999) Eq. (24) can be expressed using potential-based reward shaping: 
Ω?λ(QV (s, ·)) ' QV (s, a) + 1 
2λ Vara∼µ(QV (s, a)) 
= Ea∼µ,s′∼p(·|s,a)[r Ω(s, a, s′) + γV (s′)]. 
(26) 
For λ < 0, the reward shaping function (25) encourages the policy to visit states with less variance over Q-values, i.e. expected to be ”safer” states. 
4.2. Distributionally robust soft actor-critic 
We consider the class of entropy-regularized policies over continuous state/action space (Haarnoja et al., 2018a). We apply the soft distributionally robust policy iteration scheme (22) using reward modification (26) to approximate the computation of regularized Bellman operator over continuous action space. 
As in (Haarnoja et al., 2018a), we consider parametrized Gaussian policies πθ(a|s) = N (µθ(s),Σ 
2 θ(s)). To compute 
a modified reward (26), we approximate the variance of Q-values in (26) using the 1st order Taylor approximation of Q-values around the mean action: 
Vara∼πθ (Q(s, a)) ' g0(s)TΣθ(s)g0(s) (27) 
where g0(s) = ∇aQ(s, a)|a=µθ(s). This approximation involves computing the gradient of Q-values w.r.t. action evaluated at the mean action. When actions are independent Σθ(s) = diag(σ1,θ(s), . . . , σK,θ(s)), the expression (27) simplifies to computing the norm of the gradient weighted by the variance of corresponding action dimension: 
Vara∼πθ (Q(s, a)) ' ||g0(s)||2diag(σ1,θ(s),...,σK,θ(s)) (28) 
We summarize the above steps in Algorithm 2. 
Algorithm 2 Distributionally Robust Soft Actor-Critic Initialize: actor πθ, critic Q Set entropy levelH Set C, η > 0 Initialize s for number of epochs do 
for number of samples do a ∼ πθ(s), s′ ∼ p(s′|s, a) D ← D ∪ {(s, a, r, s′)} 
end for for number of updates do 
(s, a, r, s′) ∼ D ε← Cn−η(s) λ← 1-d optimization of Eq. (17) σ2 Q(s)← 
∑K i=1 g0(s)2 ∗ σ2 
i,θ, see Eq. (28) rΩ(s, a) ← r(s, a) + 1 
2λ (γσ2 Q(s′) − σ2 
Q(s)), see Eq. (25) Q(s, a) ← rΩ(s, a) + γ(Q(s′, πθ(s 
′)) − α log πθ(s 
′)), see Eq. (26) Update πθ, α as in Alg. 1 of (Haarnoja et al., 2018a) 
end for end for 
5. Related work Robust MDP In model-based setting, robust MDP framework has been proposed (Nilim & El Ghaoui, 2004; Iyen-gar, 2005) that optimizes over the worst-case realization
Distributionally robust reinforcement learning 
of uncertain MDP parameters. Specifically, the dynamic programming approach is used to optimize a minimax criterion over an uncertainty set that contains possible MDPs defined in terms of their transition matrices. Multiple works report the worst-case criterion may lead to overly conservative policies (Mihatsch & Neuneier, 2002; Gaskett, 2003). Variants of robust MDP formulations have been proposed to mitigate the conservativeness when additional information on parameter distribution is present (Mannor et al., 2012; Xu & Mannor, 2010; Tirinzoni et al., 2018). Differently, in this work, we employ adaptive uncertainty sets that reflect the amount of uncertainty associated with the finite sample size. We define our uncertainty set in terms of policies that arise naturally in stochastic iterative schemes and result in computationally efficient algorithms. 
Risk-sensitive MDP The framework of risk-sensitive MDP optimizes a modified objective expressed using a risk-sensitive criterion, such as the expected exponential utility or variance-related measure, w.r.t. to the long-term policy performance. In the model-free context, risk-sensitive RL for expected exponential utility has been proposed in (Borkar, 2002) and for coherent risk measures (Tamar et al., 2015). The proposed algorithms are computationally extensive as they involve integration over state space and nonconvex parameter optimization. Differently, we consider a short-term dynamic risk that shrinks with the amount of collected data, and thus, preserves the desired level of long-term risk. 
Adversarial RL Adversarial robustness in RL has been a focus of recent works. (Pinto et al., 2017) studied robustness to model parameters perturbations by manually engineering adversarial forces for a set of continuous control tasks. (Tessler et al., 2019) integrates the adversarial policy into the agent’s policy definition through a convex combination or a noisy action perturbation. The proposed methods are formulated as instances of two-player zero-sum Markov game (Littman, 1994; Perolat et al., 2015). The distributionally robust approach is related to a regularized zero-sum Markov game (Geist et al., 2019), where the adversary is regularized against the optimizing policy with a dynamic data-driven factor. Differently, it defines a multi-stage game where the first m steps are played by the adversary. 
6. Experiments We compare the robustness w.r.t. estimation errors of distributionally robust soft actor-critic (DR-SAC) algorithm (Alg. 2) against soft actor-critic (SAC) (Haarnoja et al., 2018b). We experiment on continuous control tasks from PyBullet simulation module (Coumans & Bai, 2016–2019). In particular, we focus on Hopper and Walker2D domain that exhibit the most variance during training. We note that our scores are not directly comparable to the ones re-
Hopper Walker2D Return Avg -1.7%±89 -0.4%±48 Return Std -76%±21 -78%±48 Episode Len Avg +8%±82 +4.8%±89 Episode Len Std -76%±13 -77%±42 
Table 1. Percent change of DR-SAC vs. SAC metrics computed over 100 test trajectories of the final policy. DR-SAC policies generate trajectories with smaller variance of return and episode length and similar average values. 
ported in (Haarnoja et al., 2018b) since the Roboschool environments behind the PyBullet module are harder than the MuJoCo Gym environments. 
We build our implementation on top of the Softlearning package1. We use the same hyperparameters as described in (Haarnoja et al., 2018b). In addition, we set parameters C = 1 and η = 0.5. We plan to study the impact of hyperparameter choice in future work. 
To implement per-state counter nt(s), we discretize the state space as follows. First, we discretize each dimension into ten equal-size bins, since each dimension takes values from a bounded range. Then, the state representation is given by a joint representation of its dimensions. We count the number of times the state representation appears along the policy trajectory. We leave the question of finding good state representation for future research. 
First, we analyze robustness during training. Fig. 1 shows mean and standard deviation of metrics computed over 5 evaluation rollouts at each training step using stochastic policy. Each evaluation rollout spans over 1000 environment steps. We perform 5 runs of each algorithm with different random seed. The solid curves corresponds to the mean and the shaded region to the minimum and maximum returns over the 5 trials. As expected, the DR-SAC algorithm greatly reduces variance during training in terms of standard deviation of return and episode length. We note that the absolute value of average return is similar to the one of SAC algorithm, but the upper confidence bound shows clearly lower. This empirically confirms the safety guarantee provided by the DR-SAC. 
Next, we analyze the final policy performance. Table 1 presents evaluation results computed across 100 test trajectories over stochastic policies. The policies produced using DR-SAC algorithm generate trajectories with significantly smaller variance of return and episode length. The mean performance and episode length do not show statistically significant difference. Thus, DR-SAC achieves smaller variance of performance without decreasing the average value. 
1https://github.com/rail-berkeley/ softlearning
Distributionally robust reinforcement learning 
Avg return Return std 
Avg episode length Episode length std 
0M 0.2M 0.4M 0.6M 0.8M 1M 0M 0.2M 0.4M 0.6M 0.8M 1M 
0M 0.2M 0.4M 0.6M 0.8M 1M 0M 0.2M 0.4M 0.6M 0.8M 1M 
0 
100 
200 
300 
400 
500 
0 
300 
600 
900 
1200 
0 
250 
500 
750 
1000 
0 
1000 
2000 
Timesteps 
SAC 
DRSAC 
HopperBulletEnv 
Avg return Return std 
Avg episode length Episode length std 
0M 0.4M 0.8M 1.2M 1.6M 2M 0M 0.4M 0.8M 1.2M 1.6M 2M 
0M 0.4M 0.8M 1.2M 1.6M 2M 0M 0.4M 0.8M 1.2M 1.6M 2M 
0 
100 
200 
300 
400 
500 
0 
300 
600 
900 
1200 
0 
250 
500 
750 
1000 
0 
500 
1000 
1500 
2000 
2500 
Timesteps 
SAC 
DRSAC 
Walker2DBulletEnv 
Figure 1. Average and standard deviation of return and episode length during training on Hopper and Walker2D domains. DR-SAC shows significant reduction of variance of return and episode length. 
Finally, the video demonstrations of learned policies are available online2. Qualitatively, the movements of DR-SAC policies are slower and less abrupt than the ones of SAC policies. 
7. Conclusion We study the risk-averse exploration in approximate RL setting. We propose the distributionally robust modified policy iteration scheme that implements safety in policy evaluation step w.r.t. estimation errors. The proposed scheme is based on a family of distributionally robust Bellman operators that provide lower bound guarantee on policy state-values. From a theoretical perspective, we establish the convergence of our scheme to the optimal policy. Practically, the proposed scheme results in tractable algorithms both in the discrete and continuous settings. The proposed practical algorithm implements a mixed exploration strategy that ensures safety at short-term and encourages exploration at long-term. Our experimental results show that distributional robustness is a promising direction for improving stability of training and ensuring the safe behaviour RL algorithms. In future work, we plan to extend the experimental evaluation to more tasks and provide guidance on the choice of hyperparameters. 
References Abbeel, P. and Ng, A. Y. Exploration and apprenticeship 
learning in reinforcement learning. In Proceedings of the 22nd international conference on Machine learning, pp. 
2https://drive.google.com/open?id=1L63_ 52yJQsuZXpG6qFSz2P1MWiZFStR6 
1–8. ACM, 2005. 
Auer, P., Cesa-Bianchi, N., and Fischer, P. Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3):235–256, 2002. 
Borkar, V. S. Q-learning for risk-sensitive control. Math. Oper. Res., 27(2):294–311, May 2002. ISSN 0364-765X. 
Boyd, S. and Vandenberghe, L. Convex optimization. Cam-bridge university press, 2004. 
Coumans, E. and Bai, Y. Pybullet, a python module for physics simulation for games, robotics and machine learning. http://pybullet.org, 2016–2019. 
Garcıa, J. and Fernández, F. A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research, 16(1):1437–1480, 2015. 
Gaskett, C. Reinforcement learning under circumstances beyond its control. International Conference on Computa-tional Intelligence for Modelling Control and Automation, 2003. 
Geist, M., Scherrer, B., and Pietquin, O. A theory of regularized markov decision processes. arXiv preprint arXiv:1901.11275, 2019. 
Haarnoja, T., Tang, H., Abbeel, P., and Levine, S. Rein-forcement learning with deep energy-based policies. In Proceedings of the 34th International Conference on Ma-chine Learning, volume 70 of Proceedings of Machine Learning Research, pp. 1352–1361, 2017.
Distributionally robust reinforcement learning 
Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. arXiv preprint arXiv:1801.01290, 2018a. 
Haarnoja, T., Zhou, A., Hartikainen, K., Tucker, G., Ha, S., Tan, J., Kumar, V., Zhu, H., Gupta, A., Abbeel, P., et al. Soft actor-critic algorithms and applications. arXiv preprint arXiv:1812.05905, 2018b. 
Iyengar, G. N. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005. 
Jaksch, T., Ortner, R., and Auer, P. Near-optimal regret bounds for reinforcement learning. Journal of Machine Learning Research, 11(Apr):1563–1600, 2010. 
Littman, M. L. Markov games as a framework for multiagent reinforcement learning. In Machine learning proceedings 1994, pp. 157–163. Elsevier, 1994. 
Mannor, S. and Tsitsiklis, J. Mean-variance optimization in markov decision processes. arXiv preprint arXiv:1104.5601, 2011. 
Mannor, S., Simester, D., Sun, P., and Tsitsiklis, J. N. Bias and variance in value function estimation. In Proceedings of the twenty-first international conference on Machine learning, pp. 72. ACM, 2004. 
Mannor, S., Mebel, O., and Xu, H. Lightning does not strike twice: Robust mdps with coupled uncertainty. arXiv preprint arXiv:1206.4643, 2012. 
Mihatsch, O. and Neuneier, R. Risk-sensitive reinforcement learning. Machine learning, 49(2-3):267–290, 2002. 
Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013. 
Nachum, O., Norouzi, M., Xu, K., and Schuurmans, D. Trust-pcl: An off-policy trust region method for continuous control. arXiv preprint arXiv:1707.01891, 2017. 
Ng, A. Y., Harada, D., and Russell, S. Policy invariance under reward transformations: Theory and application to reward shaping. In ICML, volume 99, pp. 278–287, 1999. 
Nilim, A. and El Ghaoui, L. Robustness in markov decision problems with uncertain transition matrices. In Advances in Neural Information Processing Systems, pp. 839–846, 2004. 
Perolat, J., Scherrer, B., Piot, B., and Pietquin, O. Approx-imate dynamic programming for two-player zero-sum markov games. In International Conference on Machine Learning (ICML 2015), 2015. 
Pinto, L., Davidson, J., Sukthankar, R., and Gupta, A. Ro-bust adversarial reinforcement learning. In Proceedings of the 34th International Conference on Machine Learning-Volume 70, pp. 2817–2826. JMLR. org, 2017. 
Prashanth, L. and Ghavamzadeh, M. Variance-constrained actor-critic algorithms for discounted and average reward mdps. Machine Learning, 105(3):367–417, 2016. 
Puterman, M. L. Markov decision processes. Wiley, New York, 1994. 
Scherrer, B., Ghavamzadeh, M., Gabillon, V., Lesner, B., and Geist, M. Approximate modified policy iteration and its application to the game of tetris. Journal of Machine Learning Research, 16:1629–1676, 2015. 
Schulman, J., Levine, S., Abbeel, P., Jordan, M., and Moritz, P. Trust region policy optimization. In International Conference on Machine Learning, pp. 1889–1897, 2015. 
Tamar, A., Di Castro, D., and Mannor, S. Temporal difference methods for the variance of the reward to go. In International Conference on Machine Learning, pp. 495–503, 2013. 
Tamar, A., Chow, Y., Ghavamzadeh, M., and Mannor, S. Policy gradient for coherent risk measures. In Advances in Neural Information Processing Systems, pp. 1468–1476, 2015. 
Tessler, C., Efroni, Y., and Mannor, S. Action robust reinforcement learning and applications in continuous control. arXiv preprint arXiv:1901.09184, 2019. 
Theocharous, G., Thomas, P. S., and Ghavamzadeh, M. Personalized ad recommendation systems for life-time value optimization with guarantees. In Twenty-Fourth International Joint Conference on Artificial Intelligence, 2015. 
Tirinzoni, A., Petrik, M., Chen, X., and Ziebart, B. Policy-conditioned uncertainty sets for robust markov decision processes. In Advances in Neural Information Processing Systems, pp. 8939–8949, 2018. 
Xu, H. and Mannor, S. Distributionally robust markov decision processes. In Advances in Neural Information Processing Systems, pp. 2505–2513, 2010. 
Ziebart, B. D., Maas, A. L., Bagnell, J. A., and Dey, A. K. Maximum entropy inverse reinforcement learning. In Aaai, volume 8, pp. 1433–1438. Chicago, IL, USA, 2008.
Distributionally robust reinforcement learning 
A. Appendix A.1. Convergence of distributionally robust MPI 
Lemma 2. Let π and π′ be two policies, and define ∆π := π′(·|s)− π(·|s), for every state s ∈ S. Then 
|(T π ′ V )(s)−(T πV )(s)| ≤ (Rmax+γ‖V ‖∞)‖∆π(·|s)‖1. 
Proof. We first note that π 7→ T π is Lipschitz w.r.t the TV distance on policies. By direct computation, one has 
|(T π′ V )(s)− (T πV )(s)| 
= |rπ′ (s) + γPπ 
′ (s, ·)TV − rπ(s)− γPπ(s, ·)TV | 
= |(π′(·|s)− π(·|s))T r(s, ·) + (Pπ ′ (s|·)− Pπ(·|s))TV | 
≤ |(π′(·|s)− π(·|s))T r(s, ·)|+ |∆π(·|s)P (·|s, ·)V | ≤ ‖∆π(·|s)‖1‖r(s, ·)‖∞ + ‖∆π(·|s)‖1‖P (·|s, ·)TV ‖∞ 
≤ (Rmax + γ‖V ‖∞)‖∆π(·|s)‖1. 
where in the last but one inequality, we have used the fact that ‖P (·|s, ·)V ‖∞ := maxa∈A |P (·|s, a)TV | ≤ maxa∈A ‖P (·|s, a)TV ‖1‖V ‖∞ = ‖V ‖∞, because ‖P (·|, s, a)‖1 = 1 for all a ∈ A since P is a transition matrix. 
Theorem 1 (Distributionally robust modified policy iteration). For an integer m ∈ [1,∞], consider the distributionally robust MPI scheme (18), where 
εt(s) = 
{ Cnt(s) 
−η, if nt(s) ≥ t/S, 0, else, 
for some constants C, η > 0 and S denotes the number of states. 
Let ˜̀ t := Ṽt − V ∗ ∈ RS be the loss at iteration t. Then 
after N ≥ 2 iterations, we have 
(A) Sub-optimality bound: 
‖˜̀N‖∞ ≤ 4Rmax 
(1− γ)2 EN + 
2γN 
1− γ ‖˜̀0‖∞, 
where 
EN := 
N−1∑ t=1 
γt‖δN−t‖∞ = ON ( 
CSη 
(1− γ)Nη 
) −→ 0. 
(B) Safety guarantee: 
Ṽt ≤ Vt ≤ V ∗, ∀t ∈ {1, . . . , N}, 
where Vt is the value function computed via exact evaluation step (5). 
Proof. Part (A) Let π and π′ be two policies, and set ∆π := π′(·|s)−π(·|s), for every state s ∈ S . Then, given any value function v ∈ RS and applying Lemma 2, one has 
|(T π ′ V )(s)−(T πV )(s)| ≤ (Rmax+γ‖V ‖∞)‖∆π(·|s)‖1. 
Further, using Pinsker’s inequality, one has 
|(T π ′ V )(s)−(T πV )(s)| ≤ (Rmax+γ‖V ‖∞) 
√ DKL(π′‖π). 
(29) 
Now, using the inequality (29) and the definition of Ṽt 
0 ≤ ((Tπ εt t )mṼt−1)(s)− Ṽt(s) 
= ((T π εt t )mṼt−1)(s)− ((Tπt)mṼt−1)(s) 
≤ (Rmax + γ‖Ṽt−1‖∞) √ DKL(πεtt (·|s)‖πt(·|s)) 
≤ ‖Ṽt−1‖∞(1− γ)−1Rmaxεt(s), 
where, in the last inequality we have used the fact that ‖Ṽt−1‖∞ ≤ (1 − γ)−1Rmax. On the other hand, by construction of the errors εt, one has 
‖εt‖∞ = max s εt(s) = max 
s|nt(s)≥t/S Cnt(s) 
−η ≤ CSηt−η. 
Thus, setting  := (1 − γ)−1Rmax, for large N , one can bound EN as follows: 
EN = ∑N−1 t=1 γt‖δN−t‖∞ ≤  
∑N−1 t=1 γN−t‖εt‖∞ 
≤ CSηγN ∑N−1 t=1 γ−tt−η ∼ CSη 
(1−γ)Nη , 
where the last asymptote is via this MathOverflow post https://mathoverflow.net/q/329893. The desired result then follows from Lemma 1. 
Part (B). Follows from definition of πεt .