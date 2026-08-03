> Source: https://arxiv.org/pdf/1306.6189

Scaling Up Robust MDPs by Reinforcement Learning 
Aviv Tamar Electrical Engineering Department 
The Technion - Israel Institute of Technology Haifa, Israel 32000 
avivt@tx.technion.ac.il 
Huan Xu Mechanical Engineering Department 
National University of Singapore Singapore 117575, Singapore mpexuh@nus.edu.sg 
Shie Mannor Electrical Engineering Department 
The Technion - Israel Institute of Technology Haifa, Israel 32000 
shie@ee.technion.ac.il 
Abstract 
We consider large-scale Markov decision processes (MDPs) with parameter uncertainty, under the robust MDP paradigm. Previous studies showed that robust MDPs, based on a minimax approach to handle uncertainty, can be solved using dynamic programming for small to medium sized problems. However, due to the “curse of dimensionality”, MDPs that model real-life problems are typically prohibitively large for such approaches. In this work we employ a reinforcement learning approach to tackle this planning problem: we develop a robust approximate dynamic programming method based on a projected fixed point equation to approximately solve large scale robust MDPs. We show that the proposed method provably succeeds under certain technical conditions, and demonstrate its effectiveness through simulation of an option pricing problem. To the best of our knowledge, this is the first attempt to scale up the robust MDPs paradigm. 
1 Introduction 
Markov decision processes (MDPs) are standard models for solving sequential decision making problems in stochastic dynamic environments [16, 3]. Given the parameters, namely, transition probability and immediate reward, the strategy that achieves maximal expected accumulated reward is considered optimal. However, in practice, these parameters are typically estimated from noisy data, or even worse, they may change during the execution of a policy. It is thus not surprising that the actual performance of the chosen strategy can significantly differ from the model’s prediction due to such parameter uncertainty – the deviation of the model parameters from the true ones (see experiments in [13]). 
To mitigate performance deviation due to parameter uncertainty, the robust MDP framework, initially proposed in [10, 14, 1], is now a common method. In this context, it is assumed that the uncertain parameters can be any member of a known set (termed the “uncertainty set”), and solutions are ranked based on their performance under the (respective) worst parameter realizations. Under mild technical conditions, the optimal solution of a robust MDP can be solved using dynamic programming, at least for small to medium sized MDPs. 
This paper considers planning in large scale robust MDPs, a setup largely untouched in literature. It is widely known that, due to the “curse of dimensionality”, practical problems modeled as MDPs often have prohibitively large state-spaces, under which dynamic programming becomes intractable. 
 
 
 
 
 
 
 
 
 
 
 
Many approximation schemes have been proposed to alleviate the curse of dimensionality of large scale MDPs, among them approximate dynamic programming (ADP) is a popular approach [15]. ADP considers approximations of the optimal value function, for example, as a linear functional of some features of the state, that can be solved efficiently using a sampling based approach. Inspired by the empirical success of ADP in a broad range of application domains involving large scale MDPs, we adapt it to the robust MDP setup, and develop and analyze methods that handle large scale robust MDPs. From a high level, we indeed solve a planning problem via a reinforcement learning (RL) approach: while the robust MDP model, the parameters, and the uncertainty sets are all known, and hence the optimal solution is well defined, we still use an RL approach to approximately find the solution due to the scale of the problem [17]. Our specific contributions are the following: 
1. A framework for approximate solution of large-scale robust MDPs. 
2. Convergence proof for robust policy evaluation with linear function approximation. 
3. A robust policy improvement algorithm with linear function approximation. 
4. Application of the framework to the problem of option pricing. 
2 Background 
We describe our problem formulation and some preliminaries from robust MDPs and ADP. 
2.1 Robust Markov Decision Processes 
For a discrete set B, letM(B) denote the set of probability measures on B, and let |B| denote its cardinality. A Markov Decision Process (MDP; [16]) is a tuple {X ,Z,U , P, r, γ} where X is a finite set of states, Z is a (possibly empty) set of absorbing terminal states, and U is a finite set of actions. Also, r : X ×U → R is a deterministic and bounded reward function, γ is a discount factor, and P : X × U →M(X ∪ Z) denotes the probability distribution of next states, given the current state and action. We assume zero reward at terminal states. 
A policy π : X →M(U) maps each state to a probability distribution over the actions. The value of a state x under policy π is denoted V π,P (x) and represents the expected sum of discounted returns when starting from that state and executing π, 
V π,P (x) = Eπ,P [ ∞∑ t=0 
γtr(xt, ut) 
∣∣∣∣∣x0 = x 
] , 
where Eπ,P denotes expectation w.r.t. the state-action distribution induced by the transitions P and the policy π. Note that for any terminal state z ∈ Z and all π and P we have V π,P (z) = 0. 
Typically in MDPs, one is interested in finding a policy that maximizes the value of certain (or all) states. When the state space is small enough, and all the parameters are known, efficient methods exist [16]. In practice, however, the state transition probabilities may not be exactly known. A widely-applied approach in this setting is the Robust MDP (RMDP; [14, 10], also termed Am-biguous MDP). In this framework, the unknown transition probabilities are assumed to lie in some known uncertainty set. Such a set may be obtained, for example, from statistical confidence intervals when the transition probabilities are estimated from data. Mathematically, an RMDP is a tuple {X ,Z,U ,P, r, γ} where X ,Z,U , r, and γ are as defined for MDPs. The uncertainty set P , where P(x, u) ⊂M(X ∪Z), denotes a known uncertainty in the state transitions. Note that this definition implicitly assumes a rectangularity of the uncertainty set [10]. Also note, that an RMDP is reduced to an MDP when there is no uncertainty, i.e., when P(x, u) is a singleton for all x and u. In robust MDPs, one is typically interested in maximizing the worst case performance. Formally, we define the robust value function [10, 14] for a policy π as its worst-case value function 
V π(x) = inf P∈P 
V π,P (x), 
and we seek for the optimal robust value function V ∗(x) = supπ { 
infP∈P V π,P (x) 
} . In [10, 14] 
it was shown that similarly to the regular value function, the robust value function is obtained by a 
deterministic policy, and satisfies a (robust) Bellman recursion of the form 
V ∗(x) = sup u∈U 
{ r(x, u) + γ inf 
P∈P EP [V ∗(x′)|x, u] 
} , 
where x′ denotes the state following the state x and action u. Thus, in the sequel we shall only consider deterministic policies, and write π(x) as the action prescribed by policy π at state x. 
In [10], a policy iteration algorithm was proposed for the robust MDP framework. This algorithm repeatedly improves a policy π by choosing greedy actions with respect to V π . The key step in this approach is therefore policy evaluation - calculating V π , which satisfies 
V π(x) = r(x, π(x)) + γ inf P∈P 
EP [V π(x′)|x, π(x)] . (1) 
The non-linear equation (1) may be solved for V π using an iterative method as follows. Let us first write (1) in vector notation. For some x and u we define the operator σP(x,u) : R|X | → R as 
σP(x,u)v . = inf 
{ p>v : p ∈ P(x, u)] 
} , 
where v ∈ R|X | and, slightly abusing notation, we ignore transitions to terminal states in P(x, u). Also, for some policy π let the operator σπ : R|X | → R|X | be defined such that {σπv} (x) 
. = 
σP(x,π(x))v. Then (1) may be written as V π = rπ + γσπV π. Let Tπ : R|X | → R|X | denote the 
robust Bellman operator for a fixed policy, defined by Tπv 
. = rπ + γσπv. (2) 
We see that V π is a fixed point of Tπ , i.e., V π = TπV π . Furthermore, since Tπ is known to be a contraction in the sup norm [10], V π may be found by iteratively applying Tπ to some vector v. 
2.2 Projected Fixed Point Equation Methods 
For MDPs, when the state space is large, dynamic programming methods become intractable, and one has to resort to an approximation procedure. A popular approach involves a projection of the value function onto a lower dimensional subspace by means of linear function approximation [4], and solving the solution of a projected Bellman equation. We briefly review this approach. 
Assume a regular MDP setting without uncertainty, where the Bellman equation (1) for a fixed policy is reduced to V π(x) = r(x, π(x)) + γEPV π(x′). When the state space is large, calculating V π(x) for every x in prohibitively computationally expensive, and a lower dimensional approximation of V π is sought. Consider the linear approximation given by a weighted sum of features 
Ṽ π(x) = φ(x)>w, x ∈ X , where φ(x) ∈ Rk, k < |X | contains the features of state x and w ∈ Rk are the approximation weights. Let Φ ∈ R|X |×k denote a matrix with the feature vectors in its rows. A popular approach for finding w is by solving the projected Bellman equation [2], given by 
Ṽ π = ΠTπṼ π, (3) where Π is a projection operator onto the subspace spanned by Φ with respect to a d-weighted Eu-clidean norm. At this point we only assume that d ∈ R|X | is positive. Since there is no uncertainty, Tπ here is a linear mapping, and Equation (3) may be written in matrix form as follows 
Φ>DΦw = Φ>Dr + Φ>DPπΦw, (4) where D = diag(d), and Pπ ∈ R|X |×|X| is the Markov transition matrix induced by policy π. Given Φ>DΦ, Φ>Dr, and Φ>DPπΦ, Eq. (4) may be solved for w either by matrix inversion [6], or iteratively (known as Projected Value Iteration; PVI; [2]) 
wk+1 = ( Φ>DΦ 
)−1 ( Φ>Dr + γΦ>DPπΦwk 
) . (5) 
When d corresponds to the steady state distribution over states for policy π, the iterative procedure in (5) can be shown to converge using contraction properties of ΠTπ [2]. For a large state space, the terms in (5) cannot be calculated explicitly. However, the strength of this approach is that these terms may be sampled efficiently, using trajectories from the MDP [2]. 
Recall that our ultimate goal is policy improvement. For a regular MDP, the policy evaluation procedure described above may be combined with a policy improvement step using Least Squares Policy Iteration (LSPI; [11]), which extends policy iteration to the function approximation setting. 
3 Robust Policy Evaluation 
In this section we propose an extension of ADP to the robust setting. We do this as follows. First, we consider policy evaluation, and extend the projected fixed point equation (3) to the robust case, with the robust Tπ operator as defined in (2). We discuss the conditions under which this equation has a solution, and how it may be obtained. We then propose a sampling based procedure to solve the equation for large state spaces, and prove its convergence. Finally, in Section 4, we will use our policy evaluation procedure as part of a policy improvement algorithm in the spirit of LSPI [11], for obtaining an (approximately) optimal robust policy. 
3.1 A Projected Fixed Point Equation 
Throughout this section we consider a fixed policy π. For some positive d, let the projection operator Π be defined as above. Consider the following projected robust Bellman equation for a fixed policy 
Ṽ π = ΠTπṼ π. (6) 
Note that here, as opposed to (3), Tπ is not necessarily linear, and hence it is not clear whether Eq. (6) has a solution at all. We now show that under suitable conditions the operator ΠTπ is a contraction and Equation (6) has a unique solution. We consider two different cases, depending on the existence of terminal states Z . Let P̂ : X →M(X ∪ Z) represent some given state transitions probabilities. Slightly abusing notation, we let P̂ (xt = j) denote the probability that the state at time t is j, given that the states evolve according to a Markov chain with transitions P̂ . In the sequel, P̂ will be used to represent the exploration policy of the MDP in an offline learning setting. We make the following assumption on P̂ , which also defines the projection weights d. Assumption 1. Either Z = ∅, and there exists positive numbers dj such that 
dj = lim t→∞ 
P̂ (xt = j|x0 = i) ∀i, j ∈ X , 
or Z 6= ∅, and the policy underlying P̂ is proper [2], that is, for t̄ = |X | 
P̂ (xt̄ ∈ Z|x0 = i) > 0 ∀i ∈ X , and all states have a positive probability of being visited. In this case we let 
dj = 
∞∑ t=0 
P̂ (xt = j) ∀j ∈ X . 
The following key assumption relates the transitions of the exploration policy and the (uncertain) transitions of the policy under evaluation. We further discuss its significance in Section 3.4. 
Assumption 2. There exists β ∈ (0, 1) such that γP (x′|x, π(x)) ≤ βP̂ (x′|x, π(x)), ∀P ∈ P, x ∈ X , x′ ∈ X . 
Let ‖ · ‖d denote the d-weighted Euclidean norm, which is well-defined due to Assumption 1. Our key insight is the following proposition, which shows that under Assumption 2, the robust Bellman operator is a β-contraction in ‖ · ‖d. 
Proposition 3. Let Assumptions 1 and 2 hold. Then ‖Tπy−Tπz‖d ≤ β‖y−z‖d for all y, z ∈ R|X | 
Proof. Fix x ∈ X , and assume that Tπy(x) ≥ Tπz(x). Choose some ε > 0, and Px ∈ P such that 
EPx [z(x′)|x, π(x)] ≤ inf P∈P 
EP [z(x′)|x, π(x)] + ε. (7) 
Also, note that by definition 
inf P∈P 
EP [y(x′)|x, π(x)] ≤ EPx [y(x′)|x, π(x)] . (8) 
Now, we have 
0 ≤ Tπy(x)− Tπz(x) ≤ (γEPx [y(x′)|x, π(x)])− (γEPx [z(x′)|x, π(x)]− γε) = γEPx [y(x′)− z(x′)|x, π(x)] + γε 
≤ βEP̂ [ |y(x′)− z(x′)| |x, π(x)] + γε, 
where the second inequality is by (7) and (8), and the last inequality is by Assumption 2. Con-versely, if Tπz(x) ≥ Tπy(x), following the same procedure we obtain 0 ≤ Tπz(x) − Tπy(x) ≤ βEP̂ [ |y(x′)− z(x′)| |x, π(x)] + γε, and we therefore conclude that |Tπy(x)− Tπz(x)| ≤ βEP̂ [ |y(x′)− z(x′)| |x, π(x)] + γε. Since ε was arbitrary, we have that |Tπy(x)− Tπz(x)| ≤ βEP̂ [ |y(x′)− z(x′)| |x, π(x)] for all x, and therefore 
‖Tπy − Tπz‖d ≤ β ∥∥∥P̂ |y − z|∥∥∥ 
d ≤ β ‖y − z‖d , 
where in last equality we used the well-known result that the state transition matrix P̂ is contracting in the d-weighted Euclidean norm [2]. 
Since the projection operator Π is known to be non-expansive in the d-weighted norm [2], we have the following corollary. Corollary 4. Let Assumptions 1 and 2 hold. Then the projected robust Bellman operator ΠTπ is a β-contraction in the d-weighted Euclidean norm. 
The contraction property in Corollary 4 guarantees an error bound for the fixed point approximation on the order of 1/(1− β) [2]. It also suggests a straightforward procedure for solving Equation (6) which we describe next. 
3.2 Robust Projected Value Iteration 
A natural method for for solving Equation (6) is the robust equivalent of PVI 
Φwk+1 = ΠTπ (Φwk) . (9) 
Corollary 4 guarantees that the iterates of (9) converge to the fixed point of ΠTπ . The algorithm (9) may be written explicitly in matrix form (see [2]) as 
wk+1 = ( Φ>DΦ 
)−1 ( Φ>Dr + γΦ>Dσπ(Φwk) 
) . (10) 
We refer to the algorithm in (10) as robust projected value iteration (RPVI). Note that a matrix inversion approach would not be applicable here, as (10) is not linear due to non-linearity of σπ(·). 
For a large state space, computing the terms in (10) exactly is intractable. For this case we propose a sampling procedure for estimating these terms, as described next. 
3.3 A Sampling Based Approach 
When the state space is too large for the terms in Equation (6) to be computed exactly, one may resort to a sampling based procedure. This approach is popular in the RL and ADP literature, and has been used successfully on problems with very large state spaces [15]. Here, we describe how it may be applied for the robust MDP setting. 
Assume that we have obtained a long trajectory from an MDP with transition probabilities P̂ , while following policy π. We denote this data by x0, u0, r0, x1, u1, r1, . . . , xN , uN , rN . A very useful property of the terms in (10) is that they may be estimated from the data by1 
Φ>DΦ ∼ 1 
N 
N−1∑ t=0 
φ(xt)φ(xt) >, Φ>Dr ∼ 1 
N 
N−1∑ t=0 
φ(xt)r(xt, ut) >, 
and 
Φ>Dσπ(Φwk) ∼ 1 
N 
N−1∑ t=0 
φ(xt)σP(xt,ut)(Φwk). (11) 
Using the law of large numbers, it may be proved 2 that these estimates converge with probability 1 to their respective terms in (10) as N → ∞. Together with Corollary 4 we have the following convergence result. The proof is straightforward and omitted. 
1These estimates are for the case Z = ∅ in Assumption 1. Modifying these estimates for the case Z 6= ∅ is straightforward, along the lines of Chapter 7.1 in [2]. 
2The proof is similar to the case without uncertainty, detailed in [2]. 
Proposition 5. Let Assumptions 1 and 2 hold. Consider the RPVI algorithm with the terms in (10) replaced by their sampled counterparts (11). Then as N → ∞ and k → ∞, wk converges with probability 1 to w∗, and Φw∗ is the unique solution of (6). 
In Eq. (11), the calculation of σP(xt,ut)(Φwk) requires a model, and, depending on the uncertainty set and state transitions, may be computationally demanding. One very natural class of models, proposed in [10, 14], is constructed from empirical state transitions xt → xt+1, and the uncertainty set corresponds to confidence regions associated with probability density estimation. In these studies, efficient methods for performing the minimization in σP(xt,ut) were suggested. In the case of binary transitions, as in our option pricing example of Section 5, performing the minimization is trivial. 
3.4 Some Remarks on Assumption 2 
Assumption 2 may appear quite restrictive, especially when the discount factor γ approaches 1. At present, we are not aware of a relaxation that will work for general features. However, we emphasize that the inequality in Assumption 2 is not required for transitions to a terminal state. This is significant, for example, in optimal stopping problems. There, if Assumption 2 holds for an exploration policy that never stops, it can be shown to hold for all policies; we discuss this in more detail in Section 5. 
One may question whether this exception for terminal states is due to the fact that their value is not approximated, and whether we can cope with states for which the assumption does not hold by not approximating their values. Unfortunately, this is not the case, as we show in the supplementary material that even if Assumption 2 fails for a single state, and for that state there is no approximation, iteratively applying ΠTπ may diverge. 
We note that a similar difficulty arises in off-policy RL [5, 18] (in fact, our Assumption 2 is similar to an assumption in [5]) , where some algorithms are shown to converge to a solution of (3) even when ΠTπ is not a contraction [20, 18]. However, in these cases not much can be said about the solution itself, and we therefore do not pursue such an approach here. 
Finally, we note that for averager type function approximation [9], Π contracts in the sup norm, and since Tπ also contracts in the sup norm [10], ΠTπ contracts regardless of Assumption 2. 
4 Robust Approximate Policy Iteration 
In this section we propose a policy improvement algorithm, driven by the RPVI method of the previous section. 
We begin by introducing the state-action value function Qπ(x, u) 
Qπ(x, u) = inf P∈P 
Eπ,P [ ∞∑ t=0 
γtr(xt, ut) 
∣∣∣∣∣x0 = x, u0 = u 
] , 
which is more convenient for applying the optimization step of policy iteration than V π(x). Again, we assume linear function approximation of the form Q̃π(x, u) = φ(x, u)>w, where φ(x, u) ∈ Rk is a state-action feature vector and w ∈ Rk is a parameter vector. Note that Qπ(x, u) may be seen as the value function of an equivalent RMDP with states in X × U , therefore the policy evaluation algorithm of Section 3 applies. Also, note that given some w, a greedy policy π∗w(x) at state x with respect to that approximation may be computed by 
π∗w(x) = arg max u 
φ(x, u)>w, 
and we write φ∗w(x) = φ(x, π∗w(x)), and let Φ∗w denote a matrix with φ∗w(x) in its rows. 
The Approximate Robust Policy Iteration (ARPI) algorithm is initialized with an arbitrary parameter vector w0. At iteration i + 1, we estimate the parameter wi+1 of the greedy policy with respect to wi as follows. We first initialize θ0 ∈ Rk to some arbitrary value, and then iterate on θ: 
θj+1 = ( Φ>DΦ 
)−1 ( Φ>Dr + γΦ>Dσπ(Φ∗wi 
θj) ) , (12) 
where the terms in (12) are estimated from data (cf. (10)) according to Φ>DΦ ∼ 1 N 
∑N−1 t=0 φ(xt, ut)φ(xt, ut) 
>, Φ>Dr ∼ 1 N 
∑N−1 t=0 φ(xt, ut)r(xt, ut) 
>, and Φ>Dσπ(Φ∗wi θj) ∼ 
1 N 
∑N−1 t=0 φ(xt, ut)σP(xt,ut)(Φ 
∗ wi θj). After θ has converged, we set wi+1 to its final value. 
For comparison, in regular LSPI [11] the iteration on θ is not needed, as the policy evaluation equation (3) is linear, and may be solved using a least squares approach (LSTD; [6]). Computationally, the contraction property of Corollary 4 guarantees a linear convergence rate for the θ iteration, therefore the addition of this step should not impact performance significantly. Also, note that the computation of Φ>DΦ and Φ>Dr only needs to be done once. 
5 Applications 
In this section we discuss applications of robust ADP. We first consider optimal stopping problems, a subclass of MDPs, for which we can show that Assumption 2 may be satisfied broadly. We then present an empirical evaluation on the problem of option pricing – a finite horizon continuous state space optimal stopping problem, for which an exact solution is intractable. 
5.1 Optimal Stopping Problems 
An optimal stopping problem is an RMDP where the only choice is when to terminate the process. Formally, the action set is binary U = {0, 1}, and executing u = 1 from any state always transitions to a terminal state with probability 1 (and no uncertainty). Let π̂ denote a policy that never chooses to terminate, i.e., π̂(x) = 0, ∀x. We now show that if Assumption 2 is satisfied for π̂, then it is immediately satisfied for all other policies. The proof is in the supplementary material. 
Proposition 6. Consider an optimal stopping problem, and let Assumption 2 hold for π̂. Then, for every policy π we have 
γP (x′|x, π(x)) ≤ βP̂ (x′|x, π(x)), ∀P ∈ P, x ∈ X , x′ ∈ X . 
and γP (x′, π(x′)|x, π(x)) ≤ βP̂ (x′, π(x′)|x, π(x)), ∀P ∈ P, x ∈ X , x′ ∈ X . 
5.2 Option Pricing 
In this section we apply ARPI to the problem of pricing American-style options. An American-style put option is a contract which gives the owner the right, but not the obligation, to sell an asset at a specified strike price K on or before some maturity time T . Letting xt denote the price (state) of the asset at time t ≤ T , the immediate payoff of executing a put option at that time is therefore max (0,K − xt). Assuming Markov state transitions, an optimal execution policy may be found by solving a finite horizon optimal stopping problem, and the expected profit under that policy is termed the ‘fair’ price of the option. Since the state space is typically continuous, an exact solution is infeasible, calling for approximate, sampling based techniques. Previous studies [19, 12] have proposed RL solutions for this task, and shown their utility. Here we extend this approach. 
One challenge of option pricing is that the underlying model is never truly known, but instead we can only access historical data in the form of state trajectories (e.g., stock prices over time). Naturally, uncertainty in the options value as predicted from this data should reflect in its price. Here, we propose to price the option according to its robust value, thereby treating uncertainty in a well-founded manner. 
We now show how the option pricing problem may be formulated as an optimal stopping RMDP, and then present our empirical results of applying the ARPI algorithm to the problem. 
5.2.1 An RMDP Formulation 
The option pricing problem may be formulated as an RMDP as follows. To account for the finite horizon, we include time explicitly in the state, thus, the state at time t is {xt, t}. The action set is binary, where 1 stands for executing the option and 0 for continuing to hold it. Once an option is executed, or when t = T , a transition to a terminal state takes place. Otherwise, the state transitions 
to {xt+1, t+1}where xt+1 is determined by a stochastic kernel P̂ (x′|x, t). The reward for executing u = 1 at state x is g(x) 
. = max (0,K − x) and zero otherwise. 
Note that the state-action values for execution is known in advance, for we have Q({x, t}, u = 1) = g(x) by definition; therefore, we only need to estimate the value of continuation. We use linear function approximation Q̃π({x, t}, u = 0) = φ({x, t})>w, and the ARPI update equation (12) in this case may be written as θj+1 = 
( Φ>DΦ 
)−1 ( γΦ>Dσπ(ν) 
) , where ν(x, t) equals g(x) 
if g(x) > φ({x, t})>wi, and equals φ({x, t})>θj otherwise. By Proposition 6, if the trajectories are obtained by a policy that never chooses to terminate, ARPI may be used safely as each policy evaluation step is guaranteed to converge. 
5.2.2 Results 
We focus on in-the-money options, where K is equal to the initial price x0. Our price fluctuation model follows a Bernoulli distribution [8], 
xt+1 = 
{ fuxt, w.p. p fdxt, w.p. 1− p , 
where the up and down factors, fu and fd, are constant. Our empirical evaluation proceeds as follows. In each experiment, we generate Ndata trajectories of length T from the true model. From these trajectories we form the maximum likelihood estimate of the up probability p̂, and the 100(1− α)% confidence intervals p̂− and p̂+ using the Clopper-Pearson method [7], which constructs our uncertain model Mrobust. We also build a model without uncertainty Mnominal by setting p̂− = p̂+ = p̂. Using p̂, we then simulate Nsim trajectories of length T (this corresponds to a policy that never executes the option), where x0 = K + ε, and ε is uniformly distributed in [−δ, δ]. These trajectories are used as input data for the ARPI algorithm of Section 4. 
For our linear function approximation we chose 2-dimensional (for x and t) radial basis function (RBF) features. In comparison, [12] used Laguerre polynomials for x and several monotone functions for t. We initially experimented with these features as well, but then opted for the RBF’s, which displayed significantly better performance. We attribute this performance improvement to the non-separable (in x and t) nature of the value function, a property that is not captured by the representation of [12]. 
Let πrobust and πnominal denote the policies found by ARPI using Mrobust and Mnominal, respectively. We evaluate the performance of πrobust and πnominal using Ntest trajectories obtained from the true model. In Figure 1 we compare the average p−percentiles (averaged over 200 independent experiments) of the total reward obtained by πrobust and πnominal, for different values of α and Ndata. As expected, the robust policy gains higher payoff in the lower percentiles, while sacrificing payoff in higher percentiles, and displays a risk-averse behavior. The effect is proportional to the uncertainty, controlled by α and Ndata. 
The parameters for the experiments were chosen to balance the different factors in the problem, and are provided in the supplementary material, as well as Matlab code for reproducing these results. 
6 Conclusion 
This work presented a novel framework for solving large-scale robust Markov decision processes. To the best of our knowledge, such problems are beyond the capabilities of previous studies, which focused on exact solutions and hence suffer from the “curse of dimensionality”. Our approach to tackling the planning problem is through reinforcement learning methods: we reduce the dimensionality of the robust value function using linear function approximation, and employ an iterative sampling based procedure to learn the approximation weights. We presented both formal guarantees and empirical evidence to the usefulness of our approach in general robust MDPs, and optimal stopping problems in particular. 
References [1] A. Bagnell, A. Ng, and J. Schneider. Solving uncertain Markov decision problems. Technical 
Report CMU-RI-TR-01-25, Carnegie Mellon University, August 2001. 
Figure 1: Performance of robust vs. regular policies. The p−percentiles of the total reward, averaged over 200 independent runs of the experiment, are shown for different values of α and Ndata. Percentiles for which the difference in performance is statistically significant (according to a paired t-test, p < 0.05) are marked by an asterisk. 
[2] D. P. Bertsekas. Dynamic Programming and Optimal Control, Vol II. Athena Scientific, fourth edition, 2012. 
[3] D. P. Bertsekas and J. N. Tsitsiklis. Neuro-Dynamic Programming. Athena Scientific, 1996. [4] D. P. Bertsekas and J. N. Tsitsiklis. Neuro-Dynamic Programming. Athena Scientific, 1996. [5] D. P. Bertsekas and H. Yu. Projected equation methods for approximate solution of large linear 
systems. Journal of Computational and Applied Mathematics, 227(1):2750, 2009. [6] J. A. Boyan. Technical update: Least-squares temporal difference learning. Machine Learning, 
49(2):233–246, 2002. [7] C. Clopper and E. S. Pearson. The use of confidence or fiducial limits illustrated in the case of 
the binomial. Biometrika, 26(4):404–413, 1934. [8] J. C. Cox, S. A. Ross, and M. Rubinstein. Option pricing: A simplified approach. Journal of 
financial Economics, 7(3):229–263, 1979. [9] G. J. Gordon. Stable function approximation in dynamic programming. In Proceedings of the 
12th International Conference on Machine Learning, 1995. [10] G. N. Iyengar. Robust dynamic programming. Mathematics of Operations Research, 
30(2):257–280, 2005. [11] M. G. Lagoudakis and R. Parr. Least-squares policy iteration. The Journal of Machine Learn-
ing Research, 4:1107–1149, 2003. [12] Y. Li, C. Szepesvari, and D. Schuurmans. Learning exercise policies for american options. 
In Proc. of the 12th International Conference on Artificial Intelligence and Statistics, JMLR: W&CP, volume 5, pages 352–359, 2009. 
[13] S. Mannor, D. Simester, P. Sun, and J. N. Tsitsiklis. Bias and variance approximation in value function estimates. Management Science, 53(2):308–322, 2007. 
[14] A. Nilim and L. El Ghaoui. Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005. 
[15] W. B. Powell. Approximate Dynamic Programming. John Wiley and Sons, 2011. [16] M. L. Puterman. Markov decision processes: discrete stochastic dynamic programming. John 
Wiley & Sons, Inc., 1994. [17] R. S. Sutton and A. G. Barto. Reinforcement Learning: An Introduction. MIT Press, 1998. [18] R. S. Sutton, H. R. Maei, D. Precup, S. Bhatnagar, D. Silver, C. Szepesvri, and E. Wiewiora. 
Fast gradient-descent methods for temporal-difference learning with linear function approximation. In Proceedings of the 26th Annual International Conference on Machine Learning, 2009. 
[19] J. N. Tsitsiklis and B. Van Roy. Regression methods for pricing complex american-style options. Neural Networks, IEEE Transactions on, 12(4):694–703, 2001. 
[20] H. Yu. Convergence of least squares temporal difference methods under general conditions. In Proceedings of the 27th Annual International Conference on Machine Learning, 2010. 