> Source: https://arxiv.org/html/2505.19238v3

Efficient Policy Optimization in Robust Constrained MDPs with Iteration Complexity Guarantees
logo Back to arXiv  
logo Back to arXiv
This is experimental HTML to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more about this project and help improve conversions.
Why HTML? Report Issue Back to Abstract Download PDF 
Table of Contents
Abstract
1 Introduction
1.1 Related Works
2 Problem Formulation
3 Policy Gradient Approach for RCMDPs
3.1 Our Proposed Approach
3.2 Policy Optimization Algorithm
4 Theoretical Results
4.1 Proof Outline
5 Experimental Results
5.1 Analysis of results
6 Discussions and Limitation
6.1 Extending to Function Approximation: Robust Constrained Actor-Critic (RCAC)
7 Conclusions and Future Works
A Proof of Proposition 1
B Proof of Lemma 4.2
B.1 Proof of Lemma B.3
C Proof of Theorem 6.1
D Robust policy evaluator based on KL divergence
E Experiments
E.1 Constrained River-swim
E.1.1 Environment Description
E.1.2 Discussions of the result
E.2 Garnet problem
E.2.1 Environment Description
E.2.2 Implementation details
E.2.3 Discussion of Results
E.3 Modified Frozen-lake
E.3.1 Environment description
E.3.2 Discussion of results
E.4 Garbage collection problem
E.4.1 Environment description
E.4.2 Discussion of results
F Implementation Details of RNPG and RPPG
F.1 RNPG
F.2 Robust Projected Policy Gradient (RPPG)
G Extension to Continuous state space (Robust Constrained Actor Critic)
G.1 Results and discussion
H Connection with the CRPO
References
License: CC BY 4.0
arXiv:2505.19238v3 [cs.LG] 07 Feb 2026
Efficient Policy Optimization in Robust Constrained MDPs with Iteration Complexity Guarantees
Report issue for preceding element
Sourav Ganguly
Department of ECE
New Jersey Institute of Technology
New Jersey, USA
sg2786@njit.edu
&Kishan Panaganti
Department of CMS
California Institute of Technology
(now at Tencent AI Lab, Seattle, WA)
kpb.research@gmail.com
&Arnob Ghosh
Department of ECE
New Jersey Institute of Technology
New Jersey, USA
arnob.ghosh@njit.edu
&Adam Wierman
Department of CMS
California Institute of Technology
California, USA
adamw@caltech.edu
Report issue for preceding element
Abstract
Report issue for preceding element
Constrained decision-making is essential for designing safe policies in real-world control systems, yet simulated environments often fail to capture real-world adversities. We consider the problem of learning a policy that will maximize the cumulative reward while satisfying a constraint, even when there is a mismatch between the real model and an accessible simulator/nominal model. In particular, we consider the robust constrained Markov decision problem (RCMDP) where an agent needs to maximize the reward and satisfy the constraint against the worst possible stochastic model under the uncertainty set centered around an unknown nominal model. Primal-dual methods, effective for standard constrained MDP (CMDP), are not applicable here because of the lack of the strong duality property. Further, one cannot apply the standard robust value-iteration based approach on the composite value function either as the worst case models may be different for the reward value function and the constraint value function. We propose a novel technique that effectively minimizes the constraint value function–to satisfy the constraints; on the other hand, when all the constraints are satisfied, it can simply maximize the robust reward value function. We prove that such an algorithm finds a policy with at most ϵ \epsilon sub-optimality and feasible policy after O  ( ϵ − 2 ) O(\epsilon^{-2}) iterations. In contrast to the state-of-the-art methods, we do not need to employ a binary search, thus, we reduce the computation time for larger value of discount factor ( γ \gamma ), and achieve a better performance for large state space.
Report issue for preceding element
1 Introduction
Report issue for preceding element
Ensuring safety or satisfying constraints is important for implementation of the RL algorithms in the real system. A poorly chosen action can lead to catastrophic consequences, making it crucial to incorporate safety constraints into the design. For instance, in self-driving cars [ 1] , a slight safety violation can result in serious harm to the system. Constrained Markov Decision Process (CMDP) can address such safety concerns where the agent aims to maximize the expected reward while keeping the expected constraint cost within a predefined safety boundary [ 2] (cf.( 5)). CMDPs effectively restricted agents from violating safety limits [ 3, 4] . However, in many practical problems, an algorithm is trained using a simulator which might be different from the real world. Thus, policies obtained for CMDP in simulated environment can still violate the constraint in the real environment.
Report issue for preceding element
To resolve the above issues, recently, researchers considered robust CMDP (RCMDP) problem where the constraint needs to be satisfied even when there is a model-mismatch due to the sim-to-real gap. In particular, we seek to solve the problem
Report issue for preceding element
RCMDP objective:  min 𝜋  max P ∈ ℙ  J c 0 π , P  s.t.  max P ∈ ℙ  J c i π , P ≤ b , i ∈ { 1 , … , K } . \displaystyle\textbf{RCMDP objective:}~\underset{\pi}{\min}\underset{P\in\mathbb{P}}{\max}~J^{\pi,P}{c{0}}~~~\text{s.t.}~~\underset{P\in\mathbb{P}}{\max}~J^{\pi,P}{c{i}}\leq b,\quad i\in{1,\ldots,K}.
(1)
where J c n J_{c_{n}} is the expected cumulative cost for the associated RCMDP cost function c n c_{n} (see Section 2). Here ℙ \mathbb{P} is the uncertainty set centered around a nominal (simulator) model described in ( 6). Note that learning the optimal policy for RCMDP are more challenging compared to the CMDP. In particular, the main challenge lies in the fact that the standard primal-dual based approaches, which achieve provable sample complexity results for the CMDP problems [ 5, 6] , cannot achieve the same for the robust CMDP problem as the problem may not admit strong duality even when the strict feasibility holds [ 7] . This is because the state occupancy measure is no longer convex as the worst-case transition probability model depends on the policy. Due to the same reason, even applying robust value iteration is not possible for the Lagrangian unlike the non-robust CMDP problem.
Report issue for preceding element
Recently, [ 8] proposed an epigraph approach to solve the problem in ( 1). In particular, they considered
Report issue for preceding element
min π , b 0 b 0 s.t.  J c n π − b n ≤ 0 ; n ∈ { 0 , … , K } . \displaystyle\min_{\pi,b_{0}}\quad b_{0}\quad\text{s.t.}~J_{c_{n}}^{\pi}-b_{n}\leq 0;~n\in{0,\ldots,K}.
(2)
Hence, the objective is passed on to the constraint with an objective of how tight the constraint can be. [ 8] finds the optimal policy for each b 0 b_{0} , and then optimized b 0 b_{0} using a binary search. They showed that for each b 0 b_{0} , the iteration complexity is O  ( ϵ − 4 ) O(\epsilon^{-4}) to find the optimal policy. Note that one needs to evaluate robust value function at every iteration for each b 0 b_{0} which is costly operation especially when γ \gamma is large as it is evident by Table 1. Further, the binary search method only works when the estimation is perfect [ 9] , thus, if the robust policy evaluator is noisy which is more likely for the large state-space, the binary search method may not work as it is evident in our function approximation setup (Appendix G). Moreover, the complexity of iteration is only O  ( log  ( ϵ − 1 )  ϵ − 4 ) O(\log(\epsilon^{-1})\epsilon^{-4}) , which is worse than that of the CMDP [ 10] . We seek to answer the following:
Report issue for preceding element
Can we develop a computationally more efficient (without binary search) approach for robust CMDP problem with a faster iteration complexity bound?
Report issue for preceding element
Table 1: Comparison of execution times averaged over multiple runs between RNPG, and EPIRC-PGS (inner loop T = 100 and outer-loop K=10) (Some more experimental results to demonstrate faster performance of our algorithms can be found in appendix G) Report issue for preceding element
Our Contributions
Report issue for preceding element
• We propose a novel approach to address the optimization problem. Specifically, we reformulate it as follows: Report issue for preceding element min π  max  { J c 0 π λ , max n  [ J c n π − b n ] } . \min_{\pi}\max\left{\frac{J_{c_{0}}^{\pi}}{\lambda},\max_{n}\left[J_{c_{n}}^{\pi}-b_{n}\right]\right}. (3) This formulation balances the trade-off between optimizing the objective and satisfying the constraints. When max n  [ J c n π − b n ] > 0 \max_{n}\left[J_{c_{n}}^{\pi}-b_{n}\right]>0 , the focus is on reducing constraint violations. Otherwise, the objective J c 0 π J_{c_{0}}^{\pi} is minimized, scaled by the factor λ \lambda . Notably, this framework eliminates the need for binary search over λ \lambda ; solving the above problem directly yields a policy that respects the constraints for an appropriately chosen λ \lambda . We show the almost equivalence of optimal solution of ( 3) and ( 1). However, because of the point-wise maximum over the multiple objectives, it introduces additional challenges in achieving the iteration complexity, as the index of the value function of the objective now depends on the policy. Report issue for preceding element
• We propose an algorithm (RNPG) that gives a policy which is at most ϵ \epsilon -sub optimal and feasible after O  ( ξ − 2  ϵ − 2 ) O(\xi^{-2}\epsilon^{-2}) iterations if the strict feasibility parameter ξ \xi is known. This is the first result to show that strict safety feasibility can be achieved. This improves the existing iteration complexity O  ( log  ( 1 ( 1 − γ )  ϵ )  ϵ − 4 ) O(\log\left(\dfrac{1}{(1-\gamma)\epsilon}\right)\epsilon^{-4}) achieved by EPIRC-PGS by [ 8] . Our algorithm does not rely on binary search and uses KL regularization instead of projected gradient descent. We also show that if we do not know ξ \xi , we can achieve a policy that violates the constraint by at most ϵ \epsilon amount while being at most ϵ \epsilon -suboptimal with O  ( 1 / ϵ 4 ) O(1/\epsilon^{4}) iteration complexity. Moreover, our dependence on the state-space ( S ) (S) , and the effective horizon (i.e., 1 1 − γ \dfrac{1}{1-\gamma} ) are much better compared to EPIRC-PGS. Report issue for preceding element
• We extend our framework to the function approximation setup by proposing a robust constrained actor-critic with integral probability metric as the uncertainty metric. For the finite-state, our empirical results show that our proposed approaches achieve a feasible policy with good reward (comparable or better than the one achieved by EPIRC-PGS, see Table 11) at a faster wall-clock time (see Table 1) 1 1 1 The system specifications are, Processor: Intel(R)Core(TM)i7-14700-2.10 GHz, Installed RAM 32.0 GB (31.7 GB usable),64-bit operating system, x64-based processor No GPU. compared to the EPIRC-PGS. From Table 1, it is evident that our algorithm speeds up the computation process by at-least 2 times as compared to EPIRC-PGS algorithm when γ = 0.9 \gamma=0.9 and at-least 3 times to EPIRC-PGS when γ = 0.995 \gamma=0.995 . For the function approximation setup, our proposed approach is the only one that achieves feasibility and even a better reward to the robust version of CRPO [ 11] during the test time for Cartpole experiment (Table 12). Further, we outperform EPIRC-PGS significant manner for the function approximation setup both in terms of performance and the training time showing its efficacy. Report issue for preceding element
1.1 Related Works
Report issue for preceding element
CMDP: The convex nature of the state-action occupancy measure ensures the existence of a zero duality gap between the primal and dual problem for CMDP, making them well-suited for solution via primal-dual methods [ 2, 12, 13, 14, 15, 16, 17, 18, 19] . The convergence bounds and rates of convergence for these methods have been extensively studied in [ 20, 21, 22, 23, 24, 6, 25, 26] . Beyond primal-dual methods, LP-based and model-based approaches have been explored to solve the primal problem directly [ 27, 18, 28, 29, 11, 30] . However, the above approaches cannot be extended to the RCMDP case.
Report issue for preceding element
Robust MDP: For robust (unconstrained) MDPs (introduced in [ 31] ), recent studies obtain the sample complexity guarantee using robust dynamic programming approach [ 32, 33, 34, 35, 36] . Model-free approaches are also studied [ 34, 37, 38, 39, 40, 41, 42, 43] . However, extending these methods to Robust Constrained MDPs (RCMDPs) presents additional challenges. The introduction of constraint functions complicates the optimization process as one needs to consider the worst value function both for the objective and the constraint.
Report issue for preceding element
RCMDP: Unlike non-robust CMDPs, there is limited research available on robust environments. In [ 7] , it was shown that the optimization function for RCMDPs is not convex, making it difficult to solve the Lagrangian formulation, unlike in standard CMDPs. Some studies have attempted to address this challenge using a primal-dual approach [ 44, 7] without any iteration complexity guarantee. [ 45] proposed a primal-dual approach to solve RCMDP under the strong duality by restricting to the categorical randomized policy class. However, they did not provide any iteration complexity guarantee. As we discussed, [ 8] reformulates the Lagrangian problem into an epigraph representation, addressing the limitations of previous methods while providing valuable theoretical insights. However, this method requires a binary search, significantly increasing computational complexity. Moreover, the binary search approach fails when the estimated robust policy value function is noisy [ 9] .
Report issue for preceding element
2 Problem Formulation
Report issue for preceding element
CMDP: We denote a MDP as ℳ = ⟨ 𝒮 , 𝒜 , 𝒫 , 𝒞 , { c j } j = 1 K , γ ⟩ \mathcal{M}=\langle\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{C},{c_{j}}{j=1}^{K},\gamma\rangle where 𝒮 , 𝒜 , 𝒫 : 𝒮 × 𝒜 × 𝒮 → ℝ \mathcal{S},\mathcal{A},\mathcal{P}:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\to\mathbb{R} denote state space, action space, and probability transition function respectively. γ ∈ [ 0 , 1 ) \gamma\in[0,1) denotes the discount factor and c i : 𝒮 × 𝒜 → ℝ c{i}:\mathcal{S}\times\mathcal{A}\to\mathbb{R} , for i = { 0 , 1 , … , K } i={0,1,\ldots,K} , denotes the constraint function. Let R + = max  ( 0 , R ) R_{+}=\max{(0,R)} for any real number R R and π : 𝒮 → 𝒜 \pi:\mathcal{S}\to\mathcal{A} denote a policy. Let β : 𝒮 → Δ  ( 𝒮 ) \beta:\mathcal{S}\to\Delta(\mathcal{S}) denote the initial state distribution where Δ  ( 𝒮 ) \Delta(\mathcal{S}) denotes the probability distribution taken over space 𝒮 \mathcal{S} . Let V c i P , π ( s ) : 𝒮 → ℝ , s . t . i ∈ { 0 , … , K } V^{P,\pi}{c{i}}(s):\mathcal{S}\to\mathbb{R},~s.t.~i\in{0,\ldots,K} (where c 0 ∈ 𝒞 c_{0}\in\mathcal{C} denote the cost for the objective) denote the value function obtained by following policy π \pi and the transition model P P where
Report issue for preceding element
V c i π , P  ( s ) := 𝔼 P , π  [ Σ t = 1 ∞  γ t − 1  π  ( a | s )  c i t  ( s , a ) ] , \displaystyle V^{\pi,P}{c{i}}(s)=\mathbb{E}{P,\pi}\left[\underset{t=1}{\overset{\infty}{\Sigma}}\gamma^{t-1}\pi(a|s)c{i}^{t}(s,a)\right],
(4)
where c i t  ( s , a ) c_{i}^{t}(s,a) denotes the single step ' i i 'th-cost/reward for being at a state ' s s ' and taking action ' a a ' at the ' t t '-th instant. Without loss of generality, we assume 0 ≤ c i  ( s , a ) ≤ 1 0\leq c_{i}(s,a)\leq 1 s . t . i ∈ { 0 , … , K } ~s.t.~i\in{0,\ldots,K} . This is in consistent with the existing literature [ 8] . We also denote J c i P , π = ⟨ ρ , V c i P , π ⟩ J^{P,\pi}{c{i}}=\langle\rho,V^{P,\pi}{c{i}}\rangle for i ∈ { 0 , … , K } i\in{0,\ldots,K} where ρ \rho is the initial state-distribution. For notational simplicity, we denote H = 1 / ( 1 − γ ) H=1/(1-\gamma) as the maximum cost value.
Report issue for preceding element
The MDP ℳ \mathcal{M} forms a constrained MDP when constraint cost functions are bounded by a threshold, leading to the following optimization problem,
Report issue for preceding element
CMDP objective:  min  J c 0 π , P  s.t.  J c i π , P ≤ b i ∀ i ∈ { 1 , … , K } . \displaystyle\text{{CMDP objective:}}~~\min~J_{c_{0}}^{\pi,P}~~\text{s.t.}~~J_{c_{i}}^{\pi,P}\leq b_{i}\quad\forall i\in{1,\ldots,K}.
(5)
Note that even though we consider a cost-based environment to be consistent with the RCMDP literature [ 8] where the objective is to minimize the expected cumulative cost, our analysis can easily go through for reward-based environment where the objective is to maximize the expected cumulative reward. Further, we can also consider the constraints of the form J c i π , P ≥ b i J^{\pi,P}{c{i}}\geq b_{i} .
Report issue for preceding element
RCMDP: We consider that we have access to the nominal model P 0 P_{0} , however, the true model might be different compared to the nominal model P 0 P_{0} . Such a scenario is relevant when we train using simulator, however, the real environment might be different compared to the simulator. The state-of-the art choice for the uncertainty set is to collect all the probability distribution which are in close proximity to a nominal model P 0 ∈ Δ  ( 𝒮 × 𝒜 ) P_{0}\in\Delta(\mathcal{S}\times\mathcal{A}) . Thus ℙ = ⨂ ( s , a ) ∈ 𝒮 × 𝒜 ℙ ( s , a ) \mathbb{P}=\bigotimes_{(s,a)\in\mathcal{S}\times\mathcal{A}}\mathbb{P}_{(s,a)} such that
Report issue for preceding element
ℙ ( s , a ) = { P ∈ Δ  ( 𝒮 ) : D  ( P , P 0  ( s , a ) ) ≤ ρ } , \mathbb{P}{(s,a)}={P\in\Delta(\mathcal{S}):D(P,P{0}(s,a))\leq\rho},
(6)
where D ( . , . ) D(.,.) is the distance measure between two probability distribution and ρ \rho denotes the maximum perturbation possible from the nominal model. Some poplar choices for D ( . , . ) D(.,.) are TV distance, χ 2 \chi^{2} distance and KL-divergence [ 32] .
Report issue for preceding element
Equation ( 6) satisfies the ( s , a ) (s,a) -rectangularity assumption. It is important to note that our analysis and algorithm remain applicable as long as a robust policy evaluator, that is, max P ∈ 𝒫  J c i π , P \max_{P\in\mathcal{P}}J_{c_{i}}^{\pi,P} is available. Therefore, we can also extend our approach to consider s s -rectangular uncertainty sets. In addition, it is possible to extend this to the integral probability metric (IPM). However, without such an assumption, evaluating a robust value function becomes an NP-hard problem.
Report issue for preceding element
The objective in constrained robust MDPs is to minimize (or maximize in a reward based setting) the worst case value function while keeping the worst case expected cost function within a threshold (user defined) as defined in ( 1). We denote max P  J c i P , π = J c i π \max_{P}J^{P,\pi}{c{i}}=J^{\pi}{c{i}} as the worst possible expected cumulative cost corresponding to cost c i c_{i} following the policy π \pi .
Report issue for preceding element
Learning Metric: Since we do not know the model, we are in the data-driven learning setting. Here, we are interested in finding the number of iterations ( T T ) required to obtain a policy π ^ \hat{\pi} with sub-optimality gap of at most ϵ \epsilon , and a feasible policy incurring no violations. That is, after T T iterations, π ^ \hat{\pi} satisfies
Report issue for preceding element
Gap  ( π ^ ) = J c 0 π ^ − J c 0 π ∗ ≤ ϵ and Violation  ( π ^ ) = max n  J c n π ^ − b n ≤ 0 , \displaystyle\mathrm{Gap}(\hat{\pi})=J_{c_{0}}^{\hat{\pi}}-J_{c_{0}}^{\pi^{*}}\leq\epsilon\quad\text{ and }\quad\mathrm{Violation}(\hat{\pi})=\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}\leq 0,
(7)
where π ∗ \pi^{*} is the optimal policy of ( 1). Note that we do not assume any restriction on the policy class Π \Pi unlike in [ 8] . In [ 45] , the policy class increases as T T increases as it is an ensemble of the learned policies up to time T T . Here, Π \Pi denotes any Markovian policy.
Report issue for preceding element
Thus, the iteration complexity measures how many iterations required to obtain a feasible policy with sub-optimality gap of at most ϵ \epsilon . Iteration complexity is a standard measure for unconstrained robust MDP [ 38] . In addition to sub-optimality gap, we also seek to achieve a feasible policy π ^ \hat{\pi} for RCMDP. Note that unlike in [ 8] , where they allowed a violation of ϵ \epsilon , here, we want to find a feasible policy, a stricter requirement.
Report issue for preceding element
Difficulty with the vanilla primal-dual method The most celebrated method to solve a constrained optimization problem is by introducing Lagrangian multiplers. Let us consider λ = ( λ 1  …  λ K ) ∈ ℝ + N \lambda=(\lambda_{1}\ldots\lambda_{K})\in\mathbb{R}^{N}_{+} be the set of langrangian multipliers introduced to convert the primal problem eqn. ( 1) into the dual space which is shown in eqn. ( 8)
Report issue for preceding element
J ∗ = min π ∈ Π  max λ ∈ ℝ + N  max P ∈ ℙ  J c 0 π , P + Σ i = 1 𝑁  λ i . max P ∈ ℙ  ( J c i π , P − b i ) . \displaystyle J^{*}=\underset{\pi\in\Pi}{\min}\underset{\lambda\in\mathbb{R}^{N}{+}}{\max}\underset{P\in\mathbb{P}}{\max}J^{\pi,P}{c_{0}}+\underset{i=1}{\overset{N}{\Sigma}}\lambda_{i}.\underset{P\in\mathbb{P}}{\max}(J_{c_{i}}^{\pi,P}-b_{i}).
(8)
In the CMDP problem, [ 46] shows that the strong duality holds when there exists a strictly feasible policy (aka Slater's condition). However, a concurrent work [ 47] highlighted that strong duality does not hold for the RCMDP problem as the occupancy measure is no longer convex as the worst transition model differs for different policies. In addition to that, in [ 8] a strong ambiguity regarding the tractability in solving lagrangian problem is discussed. Further, even if one fixes λ \lambda , one cannot apply robust value iteration approach to find the optimal policy for the Lagrangian unlike the CMDP. Hence, it is evident to look for alternative measures to find a solution to the optimality problem.
Report issue for preceding element
3 Policy Gradient Approach for RCMDPs
Report issue for preceding element
In this section, we discuss our approach to solve the RCMDP problem (eqn.( 1)). In what follows, we describe our policy optimization algorithm RNPG in detail.
Report issue for preceding element
3.1 Our Proposed Approach
Report issue for preceding element
In order to address the challenges of the primal-dual problem, We consider the following problem
Report issue for preceding element
min π  max  { J c 0 π / λ , max n  [ J c n π − b n ] } . \displaystyle\min_{\pi}\max{J_{c_{0}}^{\pi}/\lambda,\max_{n}[J_{c_{n}}^{\pi}-b_{n}]}.
(9)
Intuition: Note that when J c i π ≤ b i J_{c_{i}}^{\pi}\leq b_{i} for all i = 1 , … , K i=1,\ldots,K , the second term in the objective becomes negative, and since J c 0 π ≥ 0 J_{c_{0}}^{\pi}\geq 0 , the optimization will focus on minimizing J c 0 π J_{c_{0}}^{\pi} , as the policy is likely to be feasible with respect to all constraints. Conversely, if there exists any i i such that J c i π > b i J_{c_{i}}^{\pi}>b_{i} , then for a sufficiently large λ \lambda , the term J c 0 π / λ J_{c_{0}}^{\pi}/\lambda becomes smaller than J c i π − b i J_{c_{i}}^{\pi}-b_{i} , causing the optimization to prioritize reducing the most violated constraint J c i π J_{c_{i}}^{\pi} .
Report issue for preceding element
Even though we can not claim that ( 9) and ( 1) are the same, we can claim that the optimal solution of ( 9) can only violate the constraint by at most ϵ \epsilon -amount by a suitable choice of λ \lambda . Hence, minimizing ( 9) amounts to searching for policies that can violate at most ϵ \epsilon amount. Thus, the optimal policy of ( 1) can be an optimal of ( 9). In particular, optimal policy of ( 9) indeed has a smaller cost compared to that of ( 1). We formalize this as the following result.
Report issue for preceding element
Proposition 1.
Report issue for preceding element
Suppose that π ^ ∗ \hat{\pi}^{} is the optimal policy of ( 9) then J c 0 π ^ ∗ ≤ J c 0 π ∗ J_{c_{0}}^{\hat{\pi}^{}}\leq J_{c_{0}}^{\pi^{*}} , and can only violate the constraint by at most ϵ \epsilon with λ = 2  H / ϵ \lambda=2H/\epsilon .
Report issue for preceding element
The key distinction from the epigraph-based approach proposed in [ 8] is that we avoid tuning the hyperparameter b 0 b_{0} via binary search. This significantly reduces computational overhead, as also demonstrated in our empirical evaluations. Furthermore, tuning b 0 b_{0} typically requires accurate estimation, even an unbiased estimation would not work, which is prohibitive as the state-space grows when a high-probability estimate becomes challenging.
Report issue for preceding element
Since our goal is to obtain a feasible policy, we assume that the optimal policy is strictly feasible.
Report issue for preceding element
Assumption 1.
Report issue for preceding element
We assume that max n  J c n π ∗ − b n ≤ − ξ \max_{n}J_{c_{n}}^{\pi^{*}}-b_{n}\leq-\xi , for some ξ > 0 \xi>0 .
Report issue for preceding element
The above assumption is required because we want to have a feasible policy rather bounding the violation gap to ϵ \epsilon . Note that we only need to know (or, estimate) the value of ξ \xi . Of course, we do not need to know the optimal policy π ∗ \pi^{*} . Using ξ \xi , we can show that we achieve a feasible policy with at most ϵ \epsilon -gap in Theorem 4.1. Intuitively, if ξ > ϵ \xi>\epsilon , it means that by choosing λ = 2  H / ξ \lambda=2H/\xi , we can actually guarantee feasibility according to Proposition 1. We relax this ξ \xi -dependency in Theorem 6.1 where we show that we can achieve a policy with at most ϵ \epsilon -gap and ϵ \epsilon -violation.
Report issue for preceding element
We consider the problem
Report issue for preceding element
min π  max  { J c 0 π / λ , max n  J c n π − b n + ξ } . \displaystyle\min_{\pi}\max{J_{c_{0}}^{\pi}/\lambda,\max_{n}J_{c_{n}}^{\pi}-b_{n}+\xi}.
(10)
Note that even though for theoretical analysis to achieve a feasible policy we assume the knowledge of ξ \xi ; for our empirical evaluations, we did not assume that and yet we achieved feasible policy with good reward exceeding the state-of-the-art performance. Hence, we modify the policy space to be ξ \xi -dependent.
Report issue for preceding element
3.2 Policy Optimization Algorithm
Report issue for preceding element
We now describe our proposed robust natural policy gradient (RNPG) approach inspired from the unconstrained natural policy gradient [ 48] . For notational simplicity, we define J i  ( π ) = J c i π − b i + ξ J_{i}(\pi)=J_{c_{i}}^{\pi}-b_{i}+\xi for i = 1 , … , K i=1,\ldots,K , and J 0  ( π ) = J c 0 π / λ J_{0}(\pi)=J_{c_{0}}^{\pi}/\lambda . The policy update is then given by–
Report issue for preceding element
π t + 1 ∈ arg min π ∈ Π ⟨ ∇ π t J i ( π t ) , π − π t ⟩ + 1 α t KL ( π | | π t ) \displaystyle\pi_{t+1}\in\arg\min_{\pi\in\Pi}\langle\nabla_{\pi_{t}}J_{i}(\pi_{t}),\pi-\pi_{t}\rangle+\dfrac{1}{\alpha_{t}}\mathrm{KL}(\pi||\pi_{t})
where  i = arg  max  { J c 0 π λ , { J c n π − b n + ξ } n = 1 K } \displaystyle\text{where }i=\arg\max{\frac{J_{c_{0}}^{\pi}}{\lambda},{J_{c_{n}}^{\pi}-b_{n}+\xi}_{n=1}^{K}}
where KL \mathrm{KL} is the usual Kullback-Leibler divergence. Note that this is a convex optimization problem, and can be optimized efficiently. If we use, ℓ 2 \ell_{2} regularization, i.e., ‖ π − π t ‖ 2 2 ||\pi-\pi_{t}||{2}^{2} , then it becomes a robust projected policy gradient (RPPG) adapted from the unconstrained version (see Appendix D) [ 49, 38] , a variant of which is used in [ 8] to find optimal policy for each b 0 b{0} . Of course, our approach also works for ℓ 2 \ell_{2} norm which we define in Algorithm 4. Empirically, we observe that KL-divergence has a better performance, and provide iteration complexity for RNPG.
Report issue for preceding element
The complete procedure is described in Algorithm 1. First, we evaluate J c i π t J_{c_{i}}^{\pi_{t}} and ∇ π t J c i π t \nabla_{\pi_{t}}J_{c_{i}}^{\pi_{t}} using the robust policy evaluator which we describe in the following.
Report issue for preceding element
Robust Policy Evaluator: Our algorithm assumes access to a robust policy evaluation oracle that returns the worst-case performance of a given policy, i.e., J c i π = max P ∈ ℙ  J c i π , P J_{c_{i}}^{\pi}=\max_{P\in\mathbb{P}}J_{c_{i}}^{\pi,P} . This assumption is standard and is also adopted in both constrained [ 8] and unconstrained [ 38] robust MDP frameworks.
Report issue for preceding element
As we discussed, several efficient techniques exist for evaluating robust policies under various uncertainty models especially with ( s , a ) (s,a) rectangular assumption ( 6). In this work, we focus on the widely studied and expressive KL-divergence-based uncertainty set, which not only captures an infinite family of plausible transition models but also admits a closed-form robust evaluation method.
Report issue for preceding element
The robust value function under the KL-uncertainty set is formalized in Lemma 37 (see Appendix D). The advantage is that we obtain a closed form expression for the robust value function, and we can evaluate it by drawing samples from the nominal model only. For further background on KL and other uncertainty sets, we refer the reader to [ 50, 34, 33] .
Report issue for preceding element
Our framework is not limited to KL-divergence. Efficient robust value function evaluation techniques exist for other popular uncertainty models such as Total Variation (TV), Wasserstein, and χ 2 \chi^{2} -divergence sets [ 32, 51, 52, 33] . These approaches typically leverage dual formulations to efficiently solve the inner maximization problem required for robust evaluation. We need our robust policy evaluator to be only ϵ \epsilon -accurate. For many uncertainty sets including popular ( s , a ) (s,a) -rectangular perturbation (e.g., KL-divergence, TV-distance, χ 2 \chi^{2} uncertainty sets) this requires O  ( 1 / ϵ 2 ) O(1/\epsilon^{2}) samples [ 32, 34] . Hence, we need T  ϵ − 2 T\epsilon^{-2} samples in those cases.
Report issue for preceding element
Policy Update: In order to evaluate ∇ π t J i π \nabla_{\pi_{t}}J_{i}^{\pi} , we use the following result directly adapted to our setting from [ 48]
Report issue for preceding element
Lemma 3.1.
Report issue for preceding element
For any π ∈ Π \pi\in\Pi , transition kernel P : S × A → Δ  ( S ) P:S\times A\rightarrow\Delta(S) , for i = 1 , … , K i=1,\ldots,K ( ∇ J i , P  ( π ) )  ( s , a ) = 1 1 − γ  d P π  ( s )  Q i , P π  ( s , a ) (\nabla J_{i,P}(\pi))(s,a)=\dfrac{1}{1-\gamma}d_{P}^{\pi}(s)Q_{i,P}^{\pi}(s,a) , where Q i , P π  ( s , a ) = Q c i , P π Q_{i,P}^{\pi}(s,a)=Q_{c_{i},P}^{\pi} , and Q 0 , P = Q c 0 , P π / λ Q_{0,P}=Q_{c_{0},P}^{\pi}/\lambda .
Report issue for preceding element
Consider i t = arg  max  { J c 0 π t / λ , { J c i π t − b i + ξ } i = 1 K } i_{t}=\arg\max{J_{c_{0}}^{\pi_{t}}/\lambda,{J_{c_{i}}^{\pi_{t}}-b_{i}+\xi}{i=1}^{K}} , and p t = arg  max  J c i t π t , p t p{t}=\arg\max J_{c_{i_{t}}}^{\pi_{t},p_{t}} , we can evaluate ∇ π t J c i t π t , p t \nabla_{\pi_{t}}J_{c_{i_{t}}}^{\pi_{t},p_{t}} using the robust evaluator for Q c i t π t , p t  ( ⋅ , ⋅ ) Q_{c_{i_{t}}}^{\pi_{t},p_{t}}(\cdot,\cdot) as mentioned.
Report issue for preceding element
Hence, the natural policy update at iteration t t can be decomposed as multiple independent Mirror Descent updates across the states–
Report issue for preceding element
π t + 1 , s = arg min Δ A { ⟨ Q i t π t , p t , π s ⟩ + 1 α t K L ( π s | | π t , s ) } , ∀ s . \displaystyle\pi_{t+1,s}=\arg\min_{\Delta_{A}}{\langle Q_{i_{t}}^{\pi_{t},p_{t}},\pi_{s}\rangle+\dfrac{1}{\alpha_{t}}KL(\pi_{s}||\pi_{t,s})},\quad\forall s.
(11)
Again, this is efficient since it is convex. We use direct parameterization and soft-max parameterization for the policy update (Appendix F) by solving the optimization problem ( 11). The Algorithm 1 outputs π t ∗ \pi_{t}^{*} corresponding to the minimum objective over T T iterations. We characterize T T , the iteration complexity in the next section.
Report issue for preceding element
Although Algorithm 1 includes ξ \xi for theoretical analysis, we do not assume knowledge of ξ \xi in our empirical evaluations. In Section 6, we discuss how we achieve a slightly weaker iteration complexity result without assuming the knowledge of ξ \xi .
Report issue for preceding element
Algorithm 1 Robust-Natural Policy Gradient for constrained MDP (RNPG)
Input: α \alpha , λ \lambda , T T , ρ \rho , 𝒱 ( . ) \mathcal{V}(.) (Robust Policy Evaluator, see Algorithm 2))
Initialize: π 0 = 1 / | A | \pi_{0}={1}/{|A|} .
for t = 0  …  T − 1 t=0\ldots T-1 do
J c i π t , ∇ J c i π t = 𝒱  ( c i , ρ )  where  i = { 0 , 1 , … , K } J^{\pi^{t}}{c{i}},\nabla J^{\pi^{t}}{c{i}}~=~\mathcal{V}(c_{i},\rho)~\text{where}~i={0,1,\ldots,K} .
Update π t + 1 \pi_{t+1} according to ( 11).
end for
Output policy arg  min π t  s . t . t ∈ { 0 , … , T − 1 }  max  { J c 0 π t / λ , max i  ( J c i π t − b i + ξ ) } \arg\min_{\pi_{t}s.t.t\in{0,\ldots,T-1}}\max{J_{c_{0}}^{\pi_{t}}/\lambda,\max_{i}(J_{c_{i}}^{\pi_{t}}-b_{i}+\xi)} .
Report issue for preceding element
4 Theoretical Results
Report issue for preceding element
In this section, we will discuss the results obtained for our RNPG algorithm (Algorithm 1). Before describing, the main results, we state the Assumptions.
Report issue for preceding element
Assumption 2.
Report issue for preceding element
There exists β ∈ ( 0 , 1 ) \beta\in(0,1) such that γ  p  ( s ′ | s , a ) ≤ β  p 0  ( s ′ | s , a ) \gamma p(s^{\prime}|s,a)\leq\beta p_{0}(s^{\prime}|s,a) ∀ s ′ , s , a , \forall s^{\prime},s,a, and p ∈ 𝒫 p\in\mathcal{P} .
Report issue for preceding element
This was a common assumption for unconstrained RMDP as well [ 53, 54] . Assumption 2 states that if the perturbed distribution assigns positive probability to an event, the nominal model should also assign positive probability to that event. Otherwise, a mismatch in supports could lead to unsampled regions and render finite‑iteration bounds intractable. More importantly, Algorithm 1 does not need to know β \beta . We also did not enforce in our empirical studies. The algorithm still performed well, suggesting that the practical impact may be less restrictive than the theory implies. Also, EPIRC-PGS [ 8] assumed that the ratio between the state-action occupancy measures on the states covered by all policies and the initial state distribution is bounded.
Report issue for preceding element
We also consider a slightly stronger optimal policy for the surrogate problem.
Report issue for preceding element
Assumption 3.
Report issue for preceding element
We consider π ^ ∗ \hat{\pi}^{} ,a uniform minimizer across all states of the surrogate problem in ( 9), i.e., π ^ ∗ \hat{\pi}^{} is a solution of min π  max  { V c 0 π , P  ( s ) / λ , max n  max P  V c i π , P − b n } \min_{\pi}\max{V_{c_{0}}^{\pi,P}(s)/\lambda,\max_{n}\max_{P}V_{c_{i}}^{\pi,P}-b_{n}} for all s s .
Report issue for preceding element
A similar assumption is also considered for the unconstrained problem [ 54, 31] .
Report issue for preceding element
Theorem 4.1.
Report issue for preceding element
Under Assumptions 1, 2, and 3 with λ = 2  H / min  { ξ , 1 } \lambda=2H/\min{\xi,1} , α t = α 0 = 1 − γ T  S \alpha_{t}=\alpha_{0}=\dfrac{1-\gamma}{\sqrt{TS}} after T = O  ( ϵ − 2  ξ − 2  ( 1 − γ ) − 2  ( 1 − β ) − 2  S  log  ( | A | ) ) T=O(\epsilon^{-2}\xi^{-2}(1-\gamma)^{-2}(1-\beta)^{-2}S\log(|A|)) iterations, Algorithm 1 returns a policy π ^ \hat{\pi} such that J r π ^ − J r π ∗ ≤ ϵ J_{r}^{\hat{\pi}}-J_{r}^{\pi^{*}}\leq\epsilon , and max n  J c n π ^ − b n ≤ 0 \max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}\leq 0 .
Report issue for preceding element
Thus, Algorithm 1 has an iteration complexity of O  ( ϵ − 2 ) O(\epsilon^{-2}) . Also, the policy is feasible and only at most ϵ \epsilon -sub optimal. Our result improves upon the result O  ( ϵ − 4 ) O(\epsilon^{-4}) achieved in [ 8] . Further, they did not guarantee feasibility of the policy (rather, only ϵ \epsilon -violation). More importantly, we do not need to employ a binary search algorithm. Thus, our algorithm is computationally more efficient. Our dependence on S S , A A , and ( 1 − γ ) − 1 (1-\gamma)^{-1} are significantly better compared to [ 8] as well. Note that for the unconstrained case the iteration complexity is O  ( ϵ − 1 ) O(\epsilon^{-1}) [ 48] ; whether we can achieve such a result for robust CMDP has been left for the future.
Report issue for preceding element
As we mentioned, we do not use this ξ \xi for our empirical evaluations. Yet our results indicate that we can achieve feasible policy with better performance compared to EPIRC-PGS in significantly smaller time. In Section 6, we also obtain the result when we relax Assumption 1 with slightly worse iteration complexity by simply putting ξ = 0 \xi=0 , and λ = 2  H / ϵ \lambda=2H/\epsilon .
Report issue for preceding element
4.1 Proof Outline
Report issue for preceding element
The proof will be divided in two parts. First, we bound the iteration complexity for ϵ \epsilon -sub optimal solution of ( 10). Subsequently, we show that the sub-optimality gap and violation gap using the above result.
Report issue for preceding element
Bounding the Iteration complexity for ( 10): The following result is the key to achieve the iteration complexity result of Algorithm 1 for the Problem ( 10)
Report issue for preceding element
Lemma 4.2.
Report issue for preceding element
The policy π ^ \hat{\pi} returned by Algorithm 1 satisfies the following property:
Report issue for preceding element
max  { J c 0 π ^ / λ , max n  J c n π ^ − b n } − max  { J c 0 π / λ , max n  J c n π − b n } ≤ ϵ / λ \displaystyle\max{J_{c_{0}}^{\hat{\pi}}/\lambda,\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}}-\max{J_{c_{0}}^{\pi}/\lambda,\max_{n}J_{c_{n}}^{\pi}-b_{n}}\leq\epsilon/\lambda
(12)
for any policy π \pi after O  ( λ 2  ϵ − 2  ( 1 − γ ) − 4  ( 1 − β ) − 2 ) O(\lambda^{2}\epsilon^{-2}(1-\gamma)^{-4}(1-\beta)^{-2}) iterations under Assumptions 2, and 3.
Report issue for preceding element
Hence, the above result entails that Algorithm 4 returns a policy which is at most ϵ \epsilon -suboptimal for the problem ( 10) after O  ( ϵ − 2  ξ − 2 ) O(\epsilon^{-2}\xi^{-2}) . We show that using this result we bound the sub-optimality and the violation gap.
Report issue for preceding element
Technical Challenge: The main challenge compared to the policy optimization-based approaches for unconstrained RMDP is that here the objective (cf.( 9)) is point-wise maximum of multiple value functions for a particular policy. Hence, one might be optimizing different objectives at different iterations at π t \pi_{t} is varying across the iterations. Hence, unlike the unconstrained case, we cannot apply the robust robust performance difference Lemma as the value-function index might be different for π t \pi_{t} , and π t + 1 \pi_{t+1} . Instead, we bound it using Assumption 2, Holder's, and Pinsker's inequality.
Report issue for preceding element
Bounding the Sub-optimality Gap: By Assumption 1, J c n π ∗ ≤ b n − ξ J_{c_{n}}^{\pi^{}}\leq b_{n}-\xi . Hence, max n  J c n π ∗ − b n + ξ ≤ J c 0 π ∗ / λ \max_{n}J_{c_{n}}^{\pi^{}}-b_{n}+\xi\leq J_{c_{0}}^{\pi^{}}/\lambda as J c 0 π ∗ ≥ 0 J_{c_{0}}^{\pi^{}}\geq 0 . Thus,
Report issue for preceding element
( J c 0 π ^ − J c 0 π ∗ ) / λ \displaystyle(J_{c_{0}}^{\hat{\pi}}-J_{c_{0}}^{\pi^{*}})/\lambda
≤ max  { J c 0 π ^ / λ , max n  J c n π ^ − b n + ξ } − max  { J c 0 π ∗ / λ , max n  J c n π ∗ − b n + ξ } ≤ ϵ / λ \displaystyle\leq\max{J_{c_{0}}^{\hat{\pi}}/\lambda,\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}+\xi}-\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}J_{c_{n}}^{\pi^{}}-b_{n}+\xi}\leq\epsilon/\lambda
(13)
where the last inequality follows from Lemma 4.2. By multiplying both the sides by λ \lambda , we have the result.
Report issue for preceding element
Bounding the Violation: We now bound the violations.
Report issue for preceding element
max n  ( J c n π ^ − b n + ξ ) ≤ max n  ( J c n π ^ − b n + ξ ) − J c 0 π ∗ / λ + H / λ \displaystyle\max_{n}(J_{c_{n}}^{\hat{\pi}}-b_{n}+\xi)\leq\max_{n}(J_{c_{n}}^{\hat{\pi}}-b_{n}+\xi)-J_{c_{0}}^{\pi^{*}}/\lambda+H/\lambda
≤ max  { J c 0 π ^ / λ , max n  J c n π ^ − b n } − max  { J c 0 π ∗ / λ , max n  J c n π ∗ − b n + ξ } + H / λ \displaystyle\leq\max{J_{c_{0}}^{\hat{\pi}}/\lambda,\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}}-\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}J_{c_{n}}^{\pi^{}}-b_{n}+\xi}+H/\lambda
≤ ξ / 2 + ϵ / λ ≤ ξ , \displaystyle\leq\xi/2+\epsilon/\lambda\leq\xi,
(14)
where for the first inequality, we use the fact that J c 0 π ∗ / λ ≤ H / λ J_{c_{0}}^{\pi^{}}/\lambda\leq H/\lambda . For the secnond inequality, we use the fact that J c n π ∗ ≤ b n − ξ J_{c_{n}}^{\pi^{}}\leq b_{n}-\xi . Hence, max n  J c n π ∗ − b n + ξ ≤ J c 0 π ∗ / λ \max_{n}J_{c_{n}}^{\pi^{}}-b_{n}+\xi\leq J_{c_{0}}^{\pi^{}}/\lambda . Since λ ≥ 2  H / ξ \lambda\geq 2H/\xi , thus, H / λ ≤ ξ / 2 H/\lambda\leq\xi/2 . Note that ϵ / λ = ϵ  min  { ξ , 1 } / ( 2  H ) ≤ ϵ  ξ / ( 2  H ) ≤ ξ / 2 \epsilon/\lambda=\epsilon\min{\xi,1}/(2H)\leq\epsilon\xi/(2H)\leq\xi/2 . Hence, the above shows that max n  ( J c n π ^ − b n ) ≤ 0 \max_{n}(J_{c_{n}}^{\hat{\pi}}-b_{n})\leq 0 .
Report issue for preceding element
5 Experimental Results
Report issue for preceding element
We evaluate our algorithms 2 2 2 The complete implementation is available at https://github.com/Sourav1429/RCAC_NPG.git on two environments: (i) Garnet, and (ii) Constrained Riverswim (CRS). Additional experimental results are provided in Appendix E.
Report issue for preceding element
We have fixed λ = 50 \lambda=50 across the environments. This demonstrates that with the inclusion of a KL regularization term over policy updates, RNPG eliminates the need for manual tuning of λ \lambda . A sufficiently large fixed value ( λ = 50 \lambda=50 ) yields consistently strong performance. For a detailed description of the hyperparameters used, please refer to Appendix E.
Report issue for preceding element
Garnet: The Garnet environment is a well-known RL benchmark that consists of n  S nS states and n  A nA actions, as described in [ 55] . For our experiments, we consider 𝒢  ( 15 , 20 ) \mathcal{G}(15,20) with 15 states and 20 actions. The nominal probability function, reward function, and utility function are each sampled from separate normal distributions: 𝒩  ( μ a , σ a ) \mathcal{N}(\mu_{a},\sigma_{a}) , 𝒩  ( μ b , σ b ) \mathcal{N}(\mu_{b},\sigma_{b}) , and 𝒩  ( μ c , σ c ) \mathcal{N}(\mu_{c},\sigma_{c}) , where the means μ a , μ b , \mu_{a},\mu_{b}, and μ c \mu_{c} are drawn from a uniform distribution U  n  i  f  ( 0 , 100 ) Unif(0,100) . To ensure valid probability distributions, the nominal probabilities are exponentiated and then normalized. In this environment, we seek to maximize the reward while ensuring that the constraint is above a threshold.
Report issue for preceding element 
Report issue for preceding element 
Report issue for preceding element
Figure 1: Comparison of RNPG, RPPG and EPIRC-PGS on Garnet(15,20) environment. Here, we want to maximize the objective (vf), and want the constraint (cf) to be above the baseline. Report issue for preceding element
Constrained River-swim (CRS): The River-Swim environment consists of six states, each representing an island in a water body. The swimmer begins at any island and aims to reach either end of the river to earn a reward. At each state, the swimmer has two possible actions: swim left ( a 0 a_{0} ) or swim right ( a 1 a_{1} ). Rewards are only provided at the boundary states, while intermediate states do not offer any rewards. The leftmost state, s 0 s_{0} , and the rightmost state, s 5 s_{5} , correspond to the riverbanks. As the swimmer moves from s 0 s_{0} to s 5 s_{5} , the water depth increases, and dangerous whirlpools become more prevalent. This progression is captured by a safety constraint cost, which varies across states. The safety cost is lowest at s 0 s_{0} and reaches its maximum at s 5 s_{5} , reflecting the increasing risk as the swimmer ventures further downstream. Here the goal is to maximize the cumulative reward while ensuring the cumulative cost is below a threshold.
Report issue for preceding element 
Report issue for preceding element 
Report issue for preceding element
Figure 2: Comparison of RPPG and EPIRC-PGS on CRS environment. Here we want to maximize the objective (vf) while constraint (cf) being below the threshold line. Report issue for preceding element
5.1 Analysis of results
Report issue for preceding element
• Does RNPG perform better than EPIRC-PGS? Report issue for preceding element Performance: Our experimental results demonstrate that RNPG consistently outperforms EPIRC-PGS, in both environments. In fact, for the CRS environment (Figure 2) RNPG is the only one that produces a feasible policy. EPIRC-PGS is unable to produce a feasible policy there. In the Garnet environment (Figure 1), RNPG finds a feasible policy while achieving a better reward compared to the EPIRC-PGS. Also, RNPG shows a better convergence property and is more stable because of the KL regularization. Report issue for preceding element Computational Time: RNPG exhibits significant improvements in computational efficiency, achieving convergence at least 4x faster than EPIRC-PGS for γ = 0.9 \gamma=0.9 , and 6x faster for γ = 0.995 \gamma=0.995 in the CRS setting (Table 1). In the Garnet environment, RNPG achieves a 3x speedup over EPIRC-PGS for γ = 0.9 \gamma=0.9 , and at least 5x speedup for γ = 0.995 \gamma=0.995 (Table 1). The difference in runtime can be attributed to the fact that RNPG eliminates the need for binary search for each b 0 b_{0} value in ( 2) as described above, and it uses a KL regularization. Report issue for preceding element To summarize, RNPG performs better compared to EPIRC-PGS in terms of achieving a better reward while maintaining feasibility across the environments. Moreover, the convergence is stable across the environments, and reduces the computational time significantly compared to EPIRC-PGS as theoretical result suggested. Report issue for preceding element
• KL regularization compared to ℓ 2 \ell_{2} regularization. Report issue for preceding element We also compare RNPG with RPPG (see Appendix D), a projected robust gradient descent variant that uses an ℓ 2 \ell_{2} regularizer instead of KL for policy update in ( 11). In the CRS environment, RPPG performs slightly better than EPIRC-PGS by maintaining smaller constraint violations, though it still occasionally breaches the safety threshold. In the Garnet environment, RPPG achieves a better performance compared to EPIRC-PGS while maintaining feasibility, however, it achieves a smaller reward compared to RNPG. RNPG is also much stable, showing that KL regularization is more effective compared to ℓ 2 \ell_{2} regularization. We observe that RPPG (and, similar to RNPG) also has a smaller computational time compared to EPIRC-PGS, which demonstrates that removing the binary search is the key, as EPIRC-PGS also uses ℓ 2 \ell_{2} regularization for policy update. Report issue for preceding element
• Does λ \lambda require extensive tuning for RNPG? Report issue for preceding element A particularly notable observation from our experiments is that RNPG performs robustly across different environments using a fixed value of λ = 50 \lambda=50 . This highlights that RNPG does not need to set different λ \lambda values for different environments as theoretical result suggested. Rather, one high λ \lambda -value is enough to achieves feasibility while achieving good reward. Report issue for preceding element
6 Discussions and Limitation
Report issue for preceding element
Relaxing Assumption 1: We achieve our results in Theorem 4.1 where we assume that the optimal policy is strictly feasible and the feasibility parameter ξ \xi is known. We will relax both the features of the assumption that ξ \xi is known, and the optimal policy is strictly feasible in the following with a slightly worse iteration complexity while ensuring that the policy has violation of at most ϵ \epsilon , the same metric achieved by EPIRC-PGS [ 8] .
Report issue for preceding element
Theorem 6.1.
Report issue for preceding element
Algorithm 1 gives a policy π ^ \hat{\pi} such that J c 0 π ^ − J c 0 π ∗ ≤ ϵ J_{c_{0}}^{\hat{\pi}}-J_{c_{0}}^{\pi^{*}}\leq\epsilon and max n  J c n π ^ − b n ≤ ϵ \max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}\leq\epsilon after O  ( ϵ − 4  ( 1 − γ ) − 4  ( 1 − β ) − 2  log  ( | A | ) ) O(\epsilon^{-4}(1-\gamma)^{-4}(1-\beta)^{-2}\log(|A|)) number of iterations when we plug λ = 2  H / ϵ \lambda=2H/\epsilon and ξ = 0 \xi=0 .
Report issue for preceding element
Note that since we are not assuming strict feasibility of the optimal policy, we can only bound the violation up to ϵ \epsilon . The key here is to use λ = 2  H / ϵ \lambda=2H/\epsilon as we do not know ξ \xi , and then obtain an ϵ 2 \epsilon^{2} -close result using Lemma 4.2. This makes the iteration complexity of O  ( ϵ − 4 ) O(\epsilon^{-4}) . Note that our dependence on S S , A A , and 1 / ( 1 − γ ) 1/(1-\gamma) are significantly better compared to EPIRC-PGS [ 8] . Further, we do not employ binary search. The proof is in Appendix C.
Report issue for preceding element
6.1 Extending to Function Approximation: Robust Constrained Actor-Critic (RCAC)
Report issue for preceding element
We extend our framework to the function approximation setting motivated by the work of [ 54] for unconstrained Robust MDP problem. In particular, we consider the integral probability metric (IPM) as an uncertainty set, d ℱ  ( p , q ) = sup f ∈ ℱ { p T  f − q T  f } d_{\mathcal{F}}(p,q)=\sup_{f\in\mathcal{F}}{p^{T}f-q^{T}f} where ℱ ⊆ ℝ | S | \mathcal{F}\subseteq\mathbb{R}^{|S|} . Many metrics such as Kantorovich metric, total variation, etc., are special cases of IPM under different function classes [ 56] . We then consider the IPM-based uncertainty set, 𝒫 s , a = { q | d ℱ  ( q , p s , a 0 ) ≤ ρ } \mathcal{P}{s,a}={q|d{\mathcal{F}}(q,p^{0}_{s,a})\leq\rho} around the nominal model.
Report issue for preceding element
Consider the linear function approximation setting where V c i , w π = Ψ  w c i π V^{\pi}{c{i},w}=\Psi w^{\pi}{c{i}} where Ψ ∈ ℜ | S | × d \Psi\in\Re^{|S|\times d} is a feature matrix of ψ T  ( s ) \psi^{T}(s) ∀ s \forall s as each row. We now consider the following function class ℱ = { s → ψ  ( s ) T  ζ , ζ ∈ ℜ d , ‖ ζ ‖ 2 ≤ 1 } \mathcal{F}={s\rightarrow\psi(s)^{T}\zeta,\zeta\in\Re^{d},||\zeta||{2}\leq 1} . Now, we can apply the Proposition 1 in [ 57] to achieve the worst case value function. In particular, we have sup q ∈ d ℱ  ( q , p s , a 0 ) q T  V c i , w π = ( p s , a 0 ) T  V c i , w π + ρ  ‖ w c i , 2 : d π ‖ 2 \sup{q\in d_{\mathcal{F}}(q,p^{0}{s,a})}q^{T}V^{\pi}{c_{i},w}=(p^{0}{s,a})^{T}V^{\pi}{c_{i},w}+\rho||w^{\pi}{c{i},2:d}||_{2} where we normalize to let the first coordinate of ψ  ( s ) = 1 \psi(s)=1 . Hence, we can use the following equation to compute the robust Bellman operator
Report issue for preceding element
L 𝒫  V c i , w π = c i  ( s , a ) + γ  V c i , w π + ρ  ‖ w c i , 2 : d ‖ 2 , \displaystyle L_{\mathcal{P}}V^{\pi}{c{i},w}=c_{i}(s,a)+\gamma V^{\pi}{c{i},w}+\rho||w_{c_{i},2:d}||_{2},
(15)
with the next state s ′ s^{\prime} is drawn from the nominal model. Guided by the last regularization term of the empirical robust Bellman operator in ( 15), when considering value function approximation by neural networks we add a similar regularization term for all the neural network parameters except for the bias parameter in the last layer. We use the expression in ( 15) for the robust value function for the gradient, and J c i J_{c_{i}} in Algorithm 1. We need to estimate the robust Q function. In order to estimate the Q Q -function we first use ( 15) by plugging the V V -approximation, and then we use the linear regression to fit the critic for the robust Q Q -function. The details can be found in Appendix G.
Report issue for preceding element
From the empirical results in Figure 9 and Table 12, it is evident that our proposed approach outperforms the state-of-the-art approaches. More importantly, compared to the EPIRC-PGS (adapted to the function approximation setting), our approach achieves a significantly better performance with small wall-clock time. Also, our proposed approach outperforms the robust version of the CRPO algorithm [ 11, 47] and achieves feasibility unlike robust CRPO. In Appendix H we showed that robust CRPO may not achieve a finite time iteration complexity guarantee even for finite-state space.
Report issue for preceding element
7 Conclusions and Future Works
Report issue for preceding element
In this work, we present a novel algorithm that leverages the projected policy gradient and natural policy gradient techniques to find an ϵ \epsilon -suboptimal and a feasible policy after O  ( ϵ − 2 ) O(\epsilon^{-2}) iterations for RCMDP problem. We demonstrate the practical applicability of our algorithm by testing it on several standard reinforcement learning benchmarks. The empirical results highlight the effectiveness of RNPG, particularly in terms of reduced computation time and achieving feasibility and a better reward compared to other state-of-the-art algorithms for RCMDP.
Report issue for preceding element
Relaxing Assumption 2, and 3 constitute an important future research direction. Achieving a lower bound or improving the iteration complexity is also an important future research direction. Characterizing the results for other uncertainty sets also constitutes an important future research direction. Iteration complexity guarantee for the function approximation setting has been left for the future.
Report issue for preceding element
Acknowledgments
Report issue for preceding element
AG and SG acknowledge NJIT Startup Fund indexed 172884. SG acknowledges Neurips 2025 for awarding him with the NeurIPS 2025 Scholar Award. AW and KP acknowledge NSF grants CCF-2326609, CNS-2146814, CPS-2136197, CNS-2106403, and NGSDI-2105648 and support from the Resnick Sustainability Institute. KP also acknowledges support from the 'PIMCO Postdoctoral Fellow in Data Science' fellowship at the California Institute of Technology and the Resnick Institute.
Report issue for preceding element
References
Report issue for preceding element
Emuna et al. [2020] ↑ Ran Emuna, Avinoam Borowsky, and Armin Biess. Deep reinforcement learning for human-like driving policies in collision avoidance tasks of self-driving cars. arXiv preprint arXiv:2006.04218, 2020.
Altman [1998] ↑ Eitan Altman. Constrained markov decision processes with total cost criteria: Lagrangian approach and dual linear program. Mathematical methods of operations research, 48:387–417, 1998.
Qiu et al. [2020] ↑ Shuang Qiu, Xiaohan Wei, Zhuoran Yang, Jieping Ye, and Zhaoran Wang. Upper confidence primal-dual optimization: Stochastically constrained markov decision processes with adversarial losses and unknown transitions. arXiv preprint arXiv:2003.00660, 2020.
Padakandla et al. [2022] ↑ Sindhu Padakandla, KJ Prabuchandran, Sourav Ganguly, and Shalabh Bhatnagar. Data efficient safe reinforcement learning. In 2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC), pages 1167–1172. IEEE, 2022.
Vaswani et al. [2022] ↑ Sharan Vaswani, Lin F Yang, and Csaba Szepesvári. Near-optimal sample complexity bounds for constrained mdps. arXiv preprint arXiv:2206.06270, 2022.
Ghosh et al. [2022a] ↑ Arnob Ghosh, Xingyu Zhou, and Ness Shroff. Provably efficient model-free constrained rl with linear function approximation. Advances in Neural Information Processing Systems, 35:13303–13315, 2022a.
Wang et al. [2022] ↑ Yue Wang, Fei Miao, and Shaofeng Zou. Robust constrained reinforcement learning. arXiv preprint arXiv:2209.06866, 2022.
Kitamura et al. [2024] ↑ Toshinori Kitamura, Tadashi Kozuno, Wataru Kumagai, Kenta Hoshino, Yohei Hosoe, Kazumi Kasaura, Masashi Hamaya, Paavo Parmas, and Yutaka Matsuo. Near-optimal policy identification in robust constrained markov decision processes via epigraph form. arXiv preprint arXiv:2408.16286, 2024.
Horstein [1963] ↑ Michael Horstein. Sequential transmission using noiseless feedback. IEEE Transactions on Information Theory, 9(3):136–143, 1963.
Jiang and Ye [2024] ↑ Jiashuo Jiang and Yinyu Ye. Achieving o  ( 1 / ϵ ) o(1/\epsilon) sample complexity for constrained markov decision process. arXiv preprint arXiv:2402.16324, 2024.
Xu et al. [2021] ↑ Tengyu Xu, Yingbin Liang, and Guanghui Lan. Crpo: A new approach for safe reinforcement learning with convergence guarantee. In International Conference on Machine Learning, pages 11480–11491. PMLR, 2021.
Paternain et al. [2022] ↑ Santiago Paternain, Miguel Calvo-Fullana, Luiz FO Chamon, and Alejandro Ribeiro. Safe policies for reinforcement learning via primal-dual methods. IEEE Transactions on Automatic Control, 68(3):1321–1336, 2022.
Stooke et al. [2020] ↑ Adam Stooke, Joshua Achiam, and Pieter Abbeel. Responsive safety in reinforcement learning by pid lagrangian methods. In International Conference on Machine Learning, pages 9133–9143. PMLR, 2020.
Liang et al. [2018] ↑ Qingkai Liang, Fanyu Que, and Eytan Modiano. Accelerated primal-dual policy optimization for safe reinforcement learning. arXiv preprint arXiv:1802.06480, 2018.
Tessler et al. [2018] ↑ Chen Tessler, Daniel J Mankowitz, and Shie Mannor. Reward constrained policy optimization. arXiv preprint arXiv:1805.11074, 2018.
Yu et al. [2019] ↑ Ming Yu, Zhuoran Yang, Mladen Kolar, and Zhaoran Wang. Convergent policy optimization for safe reinforcement learning. Advances in Neural Information Processing Systems, 32, 2019.
Zheng and Ratliff [2020] ↑ Liyuan Zheng and Lillian Ratliff. Constrained upper confidence reinforcement learning. In Learning for Dynamics and Control, pages 620–629. PMLR, 2020.
Efroni et al. [2020] ↑ Yonathan Efroni, Shie Mannor, and Matteo Pirotta. Exploration-exploitation in constrained mdps. arXiv preprint arXiv:2003.02189, 2020.
Auer et al. [2008] ↑ Peter Auer, Thomas Jaksch, and Ronald Ortner. Near-optimal regret bounds for reinforcement learning. Advances in neural information processing systems, 21, 2008.
Ding et al. [2020] ↑ Dongsheng Ding, Kaiqing Zhang, Tamer Basar, and Mihailo R Jovanovic. Natural policy gradient primal-dual method for constrained markov decision processes. In NeurIPS, 2020.
Li et al. [2024] ↑ Tianjiao Li, Ziwei Guan, Shaofeng Zou, Tengyu Xu, Yingbin Liang, and Guanghui Lan. Faster algorithm and sharper analysis for constrained markov decision process. Operations Research Letters, 54:107107, 2024.
Liu et al. [2021] ↑ Tao Liu, Ruida Zhou, Dileep Kalathil, PR Kumar, and Chao Tian. Policy optimization for constrained mdps with provable fast global convergence. arXiv preprint arXiv:2111.00552, 2021.
Ying et al. [2022] ↑ Donghao Ying, Yuhao Ding, and Javad Lavaei. A dual approach to constrained markov decision processes with entropy regularization. In International Conference on Artificial Intelligence and Statistics, pages 1887–1909. PMLR, 2022.
Wei et al. [2022] ↑ Honghao Wei, Xin Liu, and Lei Ying. Triple-q: A model-free algorithm for constrained reinforcement learning with sublinear regret and zero constraint violation. In International Conference on Artificial Intelligence and Statistics, pages 3274–3307. PMLR, 2022.
Ghosh et al. [2022b] ↑ Arnob Ghosh, Xingyu Zhou, and Ness Shroff. Achieving sub-linear regret in infinite horizon average reward constrained mdp with linear function approximation. In The Eleventh International Conference on Learning Representations, 2022b.
Ghosh et al. [2024] ↑ Arnob Ghosh, Xingyu Zhou, and Ness Shroff. Towards achieving sub-linear regret and hard constraint violation in model-free rl. In International Conference on Artificial Intelligence and Statistics, pages 1054–1062. PMLR, 2024.
Achiam et al. [2017] ↑ Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. Constrained policy optimization. In International conference on machine learning, pages 22–31. PMLR, 2017.
Chow et al. [2018] ↑ Yinlam Chow, Ofir Nachum, Edgar Duenez-Guzman, and Mohammad Ghavamzadeh. A lyapunov-based approach to safe reinforcement learning. Advances in neural information processing systems, 31, 2018.
Dalal et al. [2018] ↑ Gal Dalal, Krishnamurthy Dvijotham, Matej Vecerik, Todd Hester, Cosmin Paduraru, and Yuval Tassa. Safe exploration in continuous action spaces. arXiv preprint arXiv:1801.08757, 2018.
Yang et al. [2020] ↑ Tsung-Yen Yang, Justinian Rosca, Karthik Narasimhan, and Peter J Ramadge. Projection-based constrained policy optimization. arXiv preprint arXiv:2010.03152, 2020.
Iyengar [2005] ↑ Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005.
Panaganti and Kalathil [2022] ↑ Kishan Panaganti and Dileep Kalathil. Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics, pages 9582–9602. PMLR, 2022.
Yang et al. [2022] ↑ Wenhao Yang, Liangyu Zhang, and Zhihua Zhang. Toward theoretical understandings of robust markov decision processes: Sample complexity and asymptotics. The Annals of Statistics, 50(6):3223–3248, 2022.
Shi et al. [2023] ↑ Laixi Shi, Gen Li, Yuting Wei, Yuxin Chen, Matthieu Geist, and Yuejie Chi. The curious price of distributional robustness in reinforcement learning with a generative model. Advances in Neural Information Processing Systems, 36:79903–79917, 2023.
Clavier et al. [2023] ↑ Pierre Clavier, Erwan Le Pennec, and Matthieu Geist. Towards minimax optimality of model-based robust reinforcement learning. arXiv preprint arXiv:2302.05372, 2023.
Zhou et al. [2021] ↑ Zhengqing Zhou, Zhengyuan Zhou, Qinxun Bai, Linhai Qiu, Jose Blanchet, and Peter Glynn. Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 3331–3339. PMLR, 2021.
Wang et al. [2023a] ↑ Shengbo Wang, Nian Si, Jose Blanchet, and Zhengyuan Zhou. A finite sample complexity bound for distributionally robust q-learning. In International Conference on Artificial Intelligence and Statistics, pages 3370–3398. PMLR, 2023a.
Wang et al. [2023b] ↑ Qiuhao Wang, Chin Pang Ho, and Marek Petrik. Policy gradient in robust mdps with global convergence guarantee. In International Conference on Machine Learning, pages 35763–35797. PMLR, 2023b.
Wang and Zou [2021] ↑ Yue Wang and Shaofeng Zou. Online robust reinforcement learning with model uncertainty. Advances in Neural Information Processing Systems, 34:7193–7206, 2021.
Wang et al. [2023c] ↑ Yue Wang, Alvaro Velasquez, George K Atia, Ashley Prater-Bennette, and Shaofeng Zou. Model-free robust average-reward reinforcement learning. In International Conference on Machine Learning, pages 36431–36469. PMLR, 2023c.
Wang et al. [2023d] ↑ Yue Wang, Jinjun Xiong, and Shaofeng Zou. Achieving minimax optimal sample complexity of offline reinforcement learning: A dro-based approach. 2023d.
Liang et al. [2023] ↑ Zhipeng Liang, Xiaoteng Ma, Jose Blanchet, Jiheng Zhang, and Zhengyuan Zhou. Single-trajectory distributionally robust reinforcement learning. arXiv preprint arXiv:2301.11721, 2023.
Liu et al. [2022] ↑ Zijian Liu, Qinxun Bai, Jose Blanchet, Perry Dong, Wei Xu, Zhengqing Zhou, and Zhengyuan Zhou. Distributionally robust q q -learning. In International Conference on Machine Learning, pages 13623–13643. PMLR, 2022.
Mankowitz et al. [2020] ↑ Daniel J Mankowitz, Dan A Calian, Rae Jeong, Cosmin Paduraru, Nicolas Heess, Sumanth Dathathri, Martin Riedmiller, and Timothy Mann. Robust constrained reinforcement learning for continuous control with model misspecification. arXiv preprint arXiv:2010.10644, 2020.
[45] ↑ Zhengfei Zhang, Kishan Panaganti, Laixi Shi, Yanan Sui, Adam Wierman, and Yisong Yue. Distributionally robust constrained reinforcement learning under strong duality. In Reinforcement Learning Conference.
Paternain et al. [2019] ↑ Santiago Paternain, Luiz Chamon, Miguel Calvo-Fullana, and Alejandro Ribeiro. Constrained reinforcement learning has zero duality gap. Advances in Neural Information Processing Systems, 32, 2019.
Ma et al. [2025] ↑ Shaocong Ma, Ziyi Chen, Yi Zhou, and Heng Huang. Rectified robust policy optimization for model-uncertain constrained reinforcement learning without strong duality. arXiv preprint arXiv:2508.17448, 2025.
Wang et al. [2024] ↑ Qiuhao Wang, Shaohang Xu, Chin Pang Ho, and Marek Petrik. Policy gradient for robust markov decision processes. arXiv preprint arXiv:2410.22114, 2024.
Shani et al. [2020] ↑ Lior Shani, Yonathan Efroni, and Shie Mannor. Adaptive trust region policy optimization: Global convergence and faster rates for regularized mdps. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 5668–5675, 2020.
Panaganti et al. [2022] ↑ Kishan Panaganti, Zaiyan Xu, Dileep Kalathil, and Mohammad Ghavamzadeh. Robust reinforcement learning using offline data. Advances in neural information processing systems, 35:32211–32224, 2022.
Badrinath and Kalathil [2021] ↑ Kishan Panaganti Badrinath and Dileep Kalathil. Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In International Conference on Machine Learning, pages 511–520. PMLR, 2021.
Xu et al. [2023] ↑ Zaiyan Xu, Kishan Panaganti, and Dileep Kalathil. Improved sample complexity bounds for distributionally robust reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 9728–9754. PMLR, 2023.
Tamar et al. [2014] ↑ Aviv Tamar, Shie Mannor, and Huan Xu. Scaling up robust mdps using function approximation. In International conference on machine learning, pages 181–189. PMLR, 2014.
Zhou et al. [2023] ↑ Ruida Zhou, Tao Liu, Min Cheng, Dileep Kalathil, PR Kumar, and Chao Tian. Natural actor-critic for robust reinforcement learning with function approximation. Advances in neural information processing systems, 36:97–133, 2023.
Wang [2024] ↑ Yudan Wang. Model-free robust reinforcement learning with sample complexity analysis. Master's thesis, State University of New York at Buffalo, 2024.
Müller [1997] ↑ Alfred Müller. Integral probability metrics and their generating classes of functions. Advances in applied probability, 29(2):429–443, 1997.
Zhou et al. [2024] ↑ Ruida Zhou, Tao Liu, Min Cheng, Dileep Kalathil, PR Kumar, and Chao Tian. Natural actor-critic for robust reinforcement learning with function approximation. Advances in neural information processing systems, 36, 2024.
Yang et al. [2023] ↑ Wenhao Yang, Han Wang, Tadashi Kozuno, Scott M. Jordan, and Zhihua Zhang. Robust markov decision processes without model estimation, 2023. URL https://arxiv.org/abs/2302.01248.
Towers et al. [2024] ↑ Mark Towers, Ariel Kwiatkowski, Jordan Terry, John U. Balis, Gianluca De Cola, Tristan Deleu, Manuel Goulão, Andreas Kallinteris, Markus Krimmel, Arjun KG, Rodrigo Perez-Vicente, Andrea Pierré, Sander Schulhoff, Jun Jet Tai, Hannah Tan, and Omar G. Younis. Gymnasium: A standard interface for reinforcement learning environments, 2024. URL https://arxiv.org/abs/2407.17032.
Liu et al. [2020] ↑ Yanli Liu, Kaiqing Zhang, Tamer Basar, and Wotao Yin. An improved analysis of (variance-reduced) policy gradient and natural policy gradient methods. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, Advances in Neural Information Processing Systems, volume 33, pages 7624–7636. Curran Associates, Inc., 2020. URL https://proceedings.neurips.cc/paper_files/paper/2020/file/56577889b3c1cd083b6d7b32d32f99d5-Paper.pdf.
Contents
Report issue for preceding element
1 Introduction
1.1 Related Works
2 Problem Formulation
3 Policy Gradient Approach for RCMDPs
3.1 Our Proposed Approach
3.2 Policy Optimization Algorithm
4 Theoretical Results
4.1 Proof Outline
5 Experimental Results
5.1 Analysis of results
6 Discussions and Limitation
6.1 Extending to Function Approximation: Robust Constrained Actor-Critic (RCAC)
7 Conclusions and Future Works
A Proof of Proposition 1
B Proof of Lemma 4.2
B.1 Proof of Lemma B.3
C Proof of Theorem 6.1
D Robust policy evaluator based on KL divergence
E Experiments
E.1 Constrained River-swim
E.1.1 Environment Description
E.1.2 Discussions of the result
E.2 Garnet problem
E.2.1 Environment Description
E.2.2 Implementation details
E.2.3 Discussion of Results
E.3 Modified Frozen-lake
E.3.1 Environment description
E.3.2 Discussion of results
E.4 Garbage collection problem
E.4.1 Environment description
E.4.2 Discussion of results
F Implementation Details of RNPG and RPPG
F.1 RNPG
F.2 Robust Projected Policy Gradient (RPPG)
G Extension to Continuous state space (Robust Constrained Actor Critic)
G.1 Results and discussion
H Connection with the CRPO
Appendix A Proof of Proposition 1
Report issue for preceding element
Proof.
Report issue for preceding element
Recall that π ^ ∗ \hat{\pi}^{*} is the solution of ( 9). For the first result, we have:
Report issue for preceding element
J c 0 π ^ ∗ / λ − J c 0 π ∗ / λ ≤ max  { J c 0 π ^ ∗ / λ , max n  [ J c n π ^ ∗ − b n ] } − max  { J c 0 π ∗ / λ , max n  [ J c n π ∗ − b n ] } \displaystyle J_{c_{0}}^{\hat{\pi}^{}}/\lambda-J_{c_{0}}^{\pi^{}}/\lambda\leq\max{J_{c_{0}}^{\hat{\pi}^{}}/\lambda,\max_{n}[J_{c_{n}}^{\hat{\pi}^{}}-b_{n}]}-\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}[J_{c_{n}}^{\pi^{}}-b_{n}]}
≤ 0 \displaystyle\leq 0
(16)
where we use the fact that π ∗ \pi^{} is feasible in the first inequality. For the second inequality, we use the optimality of π ^ ∗ \hat{\pi}^{} for ( 9).
Report issue for preceding element
We prove the second result using contradiction. Assume that the optimal solution π ^ ∗ \hat{\pi}^{} of ( 9) violates the constraint by ϵ \epsilon . We then show by contradiction that it cannot be an optimal solution of ( 9). Since at least one of the constraints violates by ϵ \epsilon , thus max n  [ J c n π ^ ∗ − b n ] ≥ ϵ \max_{n}[J_{c_{n}}^{\hat{\pi}^{}}-b_{n}]\geq\epsilon . Note that since λ = 2  H / ϵ \lambda=2H/\epsilon , therefore J c 0 π ^ ∗ ≤ ϵ / 2 J_{c_{0}}^{\hat{\pi}^{}}\leq\epsilon/2 as the maximum value of J c 0 π ^ ∗ J_{c_{0}}^{\hat{\pi}^{}} is H H . Thus, we have
Report issue for preceding element
max  { J c 0 π ^ ∗ / λ , max n  [ J c n π ^ ∗ − b n ] } ≥ ϵ . \displaystyle\max{J_{c_{0}}^{\hat{\pi}^{}}/\lambda,\max_{n}[J_{c_{n}}^{\hat{\pi}^{}}-b_{n}]}\geq\epsilon.
(17)
Now, consider the optimal solution π ∗ \pi^{} of ( 1). It is feasible thus max n  [ J c n π ∗ − b n ] ≤ 0 \max_{n}[J_{c_{n}}^{\pi^{}}-b_{n}]\leq 0 . Further, J c 0 π ∗ / λ ≤ ϵ / 2 J_{c_{0}}^{\pi^{*}}/\lambda\leq\epsilon/2 . Hence,
Report issue for preceding element
max  { J c 0 π ∗ / λ , max n  [ J c n π ∗ − b n ] } ≤ ϵ / 2 < ϵ ≤ max  { J c 0 π ^ ∗ / λ , max n  [ J c n π ^ ∗ − b n ] } , \displaystyle\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}[J_{c_{n}}^{\pi^{}}-b_{n}]}\leq\epsilon/2<\epsilon\leq\max{J_{c_{0}}^{\hat{\pi}^{}}/\lambda,\max_{n}[J_{c_{n}}^{\hat{\pi}^{}}-b_{n}]},
(18)
which contradicts the fact that π ^ \hat{\pi} is optimal for ( 9). This proves the second result. ∎
Report issue for preceding element
Appendix B Proof of Lemma 4.2
Report issue for preceding element
We use the following results proved in [ 48] in order to prove Lemma 4.2.
Report issue for preceding element
Lemma B.1 ( [ 48, Lemma 4.1] ).
Report issue for preceding element
Let us assume that i t = arg  max  { J c i π t − b i } i_{t}=\arg\max{J_{c_{i}}^{\pi_{t}}-b_{i}} , then,
Report issue for preceding element
α t  ⟨ Q s , i t π t , p t , π t + 1 , s − y ⟩ + B  ( π t + 1 , s , π t , s ) ≤ B  ( y , π t , s ) − B  ( y , π t + 1 , s ) , \displaystyle\alpha_{t}\langle Q_{s,i_{t}}^{\pi_{t},p_{t}},\pi_{t+1,s}-y\rangle+B(\pi_{t+1,s},\pi_{t,s})\leq B(y,\pi_{t,s})-B(y,\pi_{t+1,s}),
(19)
where B B is the Bregman's divergence.
Report issue for preceding element
The above result follows from Bregmen divergence and the policy update. In our case, B B is the KL divergence.
Report issue for preceding element
Lemma B.2 ( [ 48, Lemma A.3] ).
Report issue for preceding element
For any π , π ′ \pi,\pi^{\prime} , p p , c i c_{i} , and ρ \rho , we have
Report issue for preceding element
J c i , ρ  ( π ′ , p ) − J c i , ρ  ( π , p ) = 1 1 − γ  ∑ s d ρ π , p  ( s )  ∑ a ( π s , a ′ − π s , a )  Q s , a , c i π ′ , p . \displaystyle J_{c_{i},\rho}(\pi^{\prime},p)-J_{c_{i},\rho}(\pi,p)=\dfrac{1}{1-\gamma}\sum_{s}d_{\rho}^{\pi,p}(s)\sum_{a}(\pi^{\prime}{s,a}-\pi{s,a})Q_{s,a,c_{i}}^{\pi^{\prime},p}.
(20)
The following result is a direct consequence of Assumption 2, and has been proved in Appendix B.1.
Report issue for preceding element
Lemma B.3.
Report issue for preceding element
For any π ∈ Π \pi\in\Pi
Report issue for preceding element
Φ  ( π ) − Φ  ( π ^ ∗ ) ≤ 1 1 − β  𝔼 s ∼ d ρ π ∗ , p 0  [ ⟨ Q c i π , p , π s − π ^ ∗ ⟩ ] , \displaystyle\Phi(\pi)-\Phi(\hat{\pi}^{})\leq\dfrac{1}{1-\beta}\mathbb{E}{s\sim d{\rho}^{\pi^{},p_{0}}}[\langle Q^{\pi,p}{c{i}},\pi_{s}-\hat{\pi}^{*}\rangle],
(21)
where i = arg  max  { J c i π − b i } i=\arg\max{J_{c_{i}}^{\pi}-b_{i}} , and p = arg  max  J c i π , P p=\arg\max J_{c_{i}}^{\pi,P} .
Report issue for preceding element
Now, we are ready to prove Lemma 4.2.
Report issue for preceding element
Proof.
Report issue for preceding element
From Lemma B.3
Report issue for preceding element
Φ  ( π t ) − Φ  ( π ^ ∗ ) ≤ 1 1 − β  ∑ s d ρ π ^ ∗ , p 0  ( s )  ∑ a ( π t , s , a − π ^ s , a ∗ )  Q ^ s , a , c i t π t , p t . \displaystyle\Phi(\pi_{t})-\Phi(\hat{\pi}^{})\leq\dfrac{1}{1-\beta}\sum_{s}d_{\rho}^{\hat{\pi}^{},p_{0}}(s)\sum_{a}(\pi_{t,s,a}-\hat{\pi}^{*}{s,a})\hat{Q}{s,a,c_{i_{t}}}^{\pi_{t},p_{t}}.
where Q ^ \hat{Q} is the estimated value. Consider that the worst-case evaluator is only ϵ 0 \epsilon_{0} is close that is ‖ Q c i t π t , p t − Q ^ c i t π t , p t ‖ ∞ ≤ ϵ 0 ||Q_{c_{i_{t}}}^{\pi_{t},p_{t}}-\hat{Q}{c{i_{t}}}^{\pi_{t},p_{t}}||{\infty}\leq\epsilon{0} .
Report issue for preceding element
Hence, we have
Report issue for preceding element
Φ  ( π t ) − Φ  ( π ^ ∗ ) ≤ 1 1 − β  ∑ s d ρ π ^ ∗ , p 0  ( s )  ∑ a ( π t , s , a − π ^ s , a ∗ )  Q s , a , c i t π t , p t + ϵ 0 \displaystyle\Phi(\pi_{t})-\Phi(\hat{\pi}^{})\leq\dfrac{1}{1-\beta}\sum_{s}d_{\rho}^{\hat{\pi}^{},p_{0}}(s)\sum_{a}(\pi_{t,s,a}-\hat{\pi}^{*}{s,a})Q{s,a,c_{i_{t}}}^{\pi_{t},p_{t}}+\epsilon_{0}
(22)
Applying Lemma B.1 (subtracting and adding ⟨ Q s , i t π t , p t , π t , s ⟩ \langle Q_{s,i_{t}}^{\pi_{t},p_{t}},\pi_{t,s}\rangle , we then have from ( 22)
Report issue for preceding element
Φ  ( π t ) − Φ  ( π ^ ∗ ) ≤ \displaystyle\Phi(\pi_{t})-\Phi(\hat{\pi}^{*})\leq
[ 1 1 − β  𝔼 s ∼ d ρ π ^ ∗ , p 0  [ ⟨ Q s , i t π t , p t , π t , s − π t + 1 , s ⟩ + 1 α  B  ( π ^ ∗ , π t ) − 1 α  B  ( π ^ ∗ , π t + 1 ) − 1 α  B  ( π t + 1 , π t ) ] ] + ϵ 0 . \displaystyle[\dfrac{1}{1-\beta}\mathbb{E}{s\sim d{\rho}^{\hat{\pi}^{},p_{0}}}[\langle Q_{s,i_{t}}^{\pi_{t},p_{t}},\pi_{t,s}-\pi_{t+1,s}\rangle+\dfrac{1}{\alpha}B(\hat{\pi}^{},\pi_{t})-\dfrac{1}{\alpha}B(\hat{\pi}^{*},\pi_{t+1})-\dfrac{1}{\alpha}B(\pi_{t+1},\pi_{t})]]+\epsilon_{0}.
(23)
Now,
Report issue for preceding element
⟨ Q s , i t π t , p t , π t , s − π t + 1 , s ⟩ − 1 α  B  ( π t + 1 , π t ) ≤ ‖ q s , i t π t , p t ‖ ∞  ‖ π t , s − π t + 1 , s ‖ 1 − 1 2  α  ‖ π t , s − π t + 1 , s ‖ 1 2 \displaystyle\langle Q_{s,i_{t}}^{\pi_{t},p_{t}},\pi_{t,s}-\pi_{t+1,s}\rangle-\dfrac{1}{\alpha}B(\pi_{t+1},\pi_{t})\leq||q_{s,i_{t}}^{\pi_{t},p_{t}}||{\infty}||\pi{t,s}-\pi_{t+1,s}||{1}-\dfrac{1}{2\alpha}||\pi{t,s}-\pi_{t+1,s}||_{1}^{2}
= − 1 2  α  ( α t  ‖ Q s , i t π t , p t ‖ ∞ − ‖ π t , s − π t + 1 , s ‖ 1 ) 2 + α 2  ‖ Q s , i t π t , p t ‖ ∞ 2 \displaystyle=\dfrac{-1}{2\alpha}(\alpha_{t}||Q_{s,i_{t}}^{\pi_{t},p_{t}}||{\infty}-||\pi{t,s}-\pi_{t+1,s}||{1})^{2}+\dfrac{\alpha}{2}||Q{s,i_{t}}^{\pi_{t},p_{t}}||_{\infty}^{2}
≤ α 2  ‖ Q s , i t π t , p t ‖ ∞ 2 . \displaystyle\leq\dfrac{\alpha}{2}||Q_{s,i_{t}}^{\pi_{t},p_{t}}||_{\infty}^{2}.
(24)
where we use the Holder's inequality for the first inequality. For the second inequality, we use the Pinsker's inequality as B B is the KL divergence.
Report issue for preceding element
Hence, by summing over t t , and using ( B) we have from ( B),
Report issue for preceding element
∑ t ( Φ  ( π t ) − Φ  ( π ^ ∗ ) ) ≤ 1 1 − β  ∑ t = 0 T − 1 𝔼 s ∼ d ρ π ^ ∗ , p 0  α  ‖ Q s , i π t , p t ‖ ∞ 2 \displaystyle\sum_{t}(\Phi(\pi_{t})-\Phi(\hat{\pi}^{}))\leq\dfrac{1}{1-\beta}\sum_{t=0}^{T-1}\mathbb{E}{s\sim d{\rho}^{\hat{\pi}^{},p_{0}}}\alpha||Q_{s,i}^{\pi_{t},p_{t}}||_{\infty}^{2}
1 α  ( 1 − β )  𝔼 s ∼ d ρ π ^ ∗ , p 0  [ B  ( π ^ ∗ , π t ) − B  ( π ^ ∗ , π t + 1 ) ] + T  ϵ 0 \displaystyle+\dfrac{1}{\alpha(1-\beta)}\mathbb{E}{s\sim d{\rho}^{\hat{\pi}^{},p_{0}}}[B(\hat{\pi}^{},\pi_{t})-B(\hat{\pi}^{*},\pi_{t+1})]+T\epsilon_{0}
≤ 1 ( 1 − β )  ∑ t = 0 T − 1 α  S  1 ( 1 − γ ) 2 + 1 α  ( 1 − β )  𝔼 s ∼ d ρ π ^ ∗ , p 0  B  ( π ^ ∗ , π 0 ) + T  ϵ 0 . \displaystyle\leq\dfrac{1}{(1-\beta)}\sum_{t=0}^{T-1}\alpha S\dfrac{1}{(1-\gamma)^{2}}+\dfrac{1}{\alpha(1-\beta)}\mathbb{E}{s\sim d{\rho}^{\hat{\pi}^{},p_{0}}}B(\hat{\pi}^{},\pi_{0})+T\epsilon_{0}.
(25)
Here, we use the fact that ‖ Q s , a , c i π t , p t ‖ ∞ ≤ 1 1 − γ ||Q_{s,a,c_{i}}^{\pi_{t},p_{t}}||{\infty}\leq\dfrac{1}{1-\gamma} . This is easy to discern for i = { 1 , … , K } i={1,\ldots,K} . For i = 0 i=0 , we have ‖ Q s , a , c 0 π t , p t ‖ ∞ ≤ 1 ( 1 − γ )  λ ≤ min  { ξ / 2 , 1 / 2 } < 1 1 − γ ||Q{s,a,c_{0}}^{\pi_{t},p_{t}}||_{\infty}\leq\dfrac{1}{(1-\gamma)\lambda}\leq\min{\xi/2,1/2}<\dfrac{1}{1-\gamma} as ξ ≤ 1 1 − γ \xi\leq\dfrac{1}{1-\gamma} . Hence, from ( B),
Report issue for preceding element
∑ t ( Φ  ( π t ) − Φ  ( π ^ ∗ ) ) ≤ 1 ( 1 − β )  T  α  S  1 ( 1 − γ ) 2 + 1 α  ( 1 − β )  𝔼 s ∼ d ρ π ^ ∗ , p 0  B  ( π ^ ∗ , π 0 ) + T  ϵ 0 . \displaystyle\sum_{t}(\Phi(\pi_{t})-\Phi(\hat{\pi}^{}))\leq\dfrac{1}{(1-\beta)}T\alpha S\dfrac{1}{(1-\gamma)^{2}}+\dfrac{1}{\alpha(1-\beta)}\mathbb{E}{s\sim d{\rho}^{\hat{\pi}^{},p_{0}}}B(\hat{\pi}^{*},\pi_{0})+T\epsilon_{0}.
(26)
Now, replacing π 0 = 1 | A | \pi_{0}=\dfrac{1}{|A|} , and α = ( 1 − γ ) T  S \alpha=\dfrac{(1-\gamma)}{\sqrt{TS}} , we have
Report issue for preceding element
∑ t ( Φ  ( π t ) − Φ  ( π ^ ∗ ) ) ≤ 1 1 − β  S  T  log  ( | A | )  1 ( 1 − γ ) 2 + T  ϵ 0 . \displaystyle\sum_{t}(\Phi(\pi_{t})-\Phi(\hat{\pi}^{*}))\leq\dfrac{1}{1-\beta}\sqrt{ST}\log(|A|)\dfrac{1}{\sqrt{(1-\gamma)^{2}}}+T\epsilon_{0}.
(27)
Thus,
Report issue for preceding element
Φ  ( π ^ ) − Φ  ( π ^ ∗ ) ≤ 1 T  ∑ t ( Φ  ( π t ) − Φ  ( π ^ ∗ ) ) ≤ S  log  ( | A | ) ( 1 − β )  T  ( 1 − γ ) 2 + ϵ 0 , \displaystyle\Phi(\hat{\pi})-\Phi(\hat{\pi}^{})\leq\dfrac{1}{T}\sum_{t}(\Phi(\pi_{t})-\Phi(\hat{\pi}^{}))\leq\dfrac{\sqrt{S}\log(|A|)}{(1-\beta)\sqrt{T(1-\gamma)^{2}}}+\epsilon_{0},
(28)
where we use the fact that π ^ = arg  min t = 0 , … , T − 1  max  { J c 0 π t , max n  { J c n π t − b n } } \hat{\pi}=\arg\min_{t=0,\ldots,T-1}\max{J_{c_{0}}^{\pi_{t}},\max_{n}{J_{c_{n}}^{\pi_{t}}-b_{n}}} .
Report issue for preceding element
Hence, when T = O  ( 4 ( 1 − γ ) 2  ( 1 − β ) 2  S  log  ( | A | )  ( 1 / ϵ 2 ) ) T=O(\dfrac{4}{(1-\gamma)^{2}(1-\beta)^{2}}S\log(|A|)(1/\epsilon^{2})) iteration, the above is bounded by ϵ \epsilon , if ϵ 0 = ϵ / 2 \epsilon_{0}=\epsilon/2 . The result now follows. ∎
Report issue for preceding element
B.1 Proof of Lemma B.3
Report issue for preceding element
Proof.
Report issue for preceding element
Let i = arg  max  { J c i π − b i } i=\arg\max{J_{c_{i}}^{\pi}-b_{i}} , and p = arg  max  J c i π , P p=\arg\max J_{c_{i}}^{\pi,P} . Now,
Report issue for preceding element
Φ  ( π ) − Φ  ( π ^ ∗ ) ≤ J c i π , p − max P  J c i π ^ ∗ , P . \displaystyle\Phi(\pi)-\Phi(\hat{\pi}^{})\leq J_{c_{i}}^{\pi,p}-\max_{P}J_{c_{i}}^{\hat{\pi}^{},P}.
(29)
We now bound the right-hand side, and assume that p ∗ = arg  max  J c i π ^ ∗ , P p^{}=\arg\max J_{c_{i}}^{\hat{\pi}^{},P}
Report issue for preceding element
V c i π  ( ρ ) − V c i π ^ ∗  ( ρ ) = V c i π  ( ρ ) − 𝔼 s ∼ ρ  𝔼 π ^ ∗  [ c i  ( s , a ) + γ  ∑ s ′ p ∗  ( s ′ | s , a )  V c i π ∗  ( s ′ ) ] \displaystyle V_{c_{i}}^{\pi}(\rho)-V_{c_{i}}^{\hat{\pi}^{}}(\rho)=V^{\pi}{c{i}}(\rho)-\mathbb{E}{s\sim\rho}\mathbb{E}{\hat{\pi}^{}}[c_{i}(s,a)+\gamma\sum_{s^{\prime}}p^{}(s^{\prime}|s,a)V^{\pi^{}}{c{i}}(s^{\prime})]
= 𝔼 s ∼ ρ  𝔼 a ∼ π ^ ∗  [ V c i π  ( ρ ) − c i  ( s , a ) + γ  ∑ s ′ p  ( s ′ | s , a )  V c i π  ( s ′ ) ] \displaystyle=\mathbb{E}{s\sim\rho}\mathbb{E}{a\sim\hat{\pi}^{*}}[V_{c_{i}}^{\pi}(\rho)-c_{i}(s,a)+\gamma\sum_{s^{\prime}}p(s^{\prime}|s,a)V^{\pi}{c{i}}(s^{\prime})]
− 𝔼 s ∼ ρ  𝔼 π ^ ∗  γ  [ ∑ s ′ p ∗  ( s ′ | s , a )  V c i π ^ ∗  ( s ′ ) − ∑ s ′ p  ( s ′ | s , a )  V c i π  ( s ′ ) ] \displaystyle-\mathbb{E}{s\sim\rho}\mathbb{E}{\hat{\pi}^{}}\gamma[\sum_{s^{\prime}}p^{}(s^{\prime}|s,a)V^{\hat{\pi}^{*}}{c{i}}(s^{\prime})-\sum_{s^{\prime}}p(s^{\prime}|s,a)V^{\pi}{c{i}}(s^{\prime})]
≤ ∑ s ∼ ρ ⟨ Q c i π , π − π ^ ∗ ⟩ − γ  𝔼 s ∼ ρ  𝔼 π ^ ∗  [ ∑ s ′ p  ( s ′ | s , a )  ( V c i π ^ ∗  ( s ′ ) − V c i π  ( s ′ ) ) ] \displaystyle\leq\sum_{s\sim\rho}\langle Q_{c_{i}}^{\pi},\pi-\hat{\pi}^{}\rangle-\gamma\mathbb{E}{s\sim\rho}\mathbb{E}{\hat{\pi}^{}}[\sum_{s^{\prime}}p(s^{\prime}|s,a)(V^{\hat{\pi}^{*}}{c{i}}(s^{\prime})-V^{\pi}{c{i}}(s^{\prime}))]
where the inequality follows from the fact that p ∗ = arg  max  ∑ s ′ p ∗  ( s ′ | s , a )  V c i π ^ ∗  ( s ′ ) p^{}=\arg\max\sum_{s^{\prime}}p^{}(s^{\prime}|s,a)V_{c_{i}}^{\hat{\pi}^{*}}(s^{\prime}) . Hence,
Report issue for preceding element
V c i π  ( ρ ) − V c i π ^ ∗  ( ρ ) ≤ ∑ s ∼ ρ ⟨ Q c i π , π − π ^ ∗ ⟩ + β  𝔼 s ∼ ρ  𝔼 π ^ ∗  [ ∑ s ′ p 0  ( s ′ | s , a )  ( V c i π  ( s ′ ) − V c i π ^ ∗  ( s ′ ) ) ] . \displaystyle V_{c_{i}}^{\pi}(\rho)-V_{c_{i}}^{\hat{\pi}^{}}(\rho)\leq\sum_{s\sim\rho}\langle Q_{c_{i}}^{\pi},\pi-\hat{\pi}^{}\rangle+\beta\mathbb{E}{s\sim\rho}\mathbb{E}{\hat{\pi}^{}}[\sum_{s^{\prime}}p_{0}(s^{\prime}|s,a)(V^{\pi}{c{i}}(s^{\prime})-V^{\hat{\pi}^{}}{c{i}}(s^{\prime}))].
(30)
where we use the fact that V c i π  ( s ′ ) ≥ V c i π ^ ∗  ( s ′ ) V_{c_{i}}^{\pi}(s^{\prime})\geq V_{c_{i}}^{\hat{\pi}^{*}}(s^{\prime}) by Assumption 3, and Assumption 2. By recursively, expanding we get the result. ∎
Report issue for preceding element
Appendix C Proof of Theorem 6.1
Report issue for preceding element
Proof.
Report issue for preceding element
Here, we just consider the following objective
Report issue for preceding element
min π  max  { J c 0 π / λ , max n  J c n π − b n } , \displaystyle\min_{\pi}\max{J_{c_{0}}^{\pi}/\lambda,\max_{n}J_{c_{n}}^{\pi}-b_{n}},
(31)
since we do not know ξ \xi , here, we only use max n  J c n π − b n \max_{n}J_{c_{n}}^{\pi}-b_{n} instead of max n  J c n π − b n + ξ \max_{n}J_{c_{n}}^{\pi}-b_{n}+\xi . We consider λ = 2  H / ϵ \lambda=2H/\epsilon .
Report issue for preceding element
Sub-optimality gap: Since π ∗ \pi^{} is feasible, thus, J c 0 π ∗ / λ ≥ max n  J c n π ∗ − b n J_{c_{0}}^{\pi^{}}/\lambda\geq\max_{n}J_{c_{n}}^{\pi^{*}}-b_{n} . Thus,
Report issue for preceding element
( J c 0 π ^ − J c 0 π ∗ ) / λ \displaystyle(J_{c_{0}}^{\hat{\pi}}-J_{c_{0}}^{\pi^{*}})/\lambda
≤ max  { J c 0 π ^ / λ , max n  J c n π ^ − b n } − max  { J c 0 π ∗ / λ , max n  J c n π ∗ − b n } \displaystyle\leq\max{J_{c_{0}}^{\hat{\pi}}/\lambda,\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}}-\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}J_{c_{n}}^{\pi^{}}-b_{n}}
≤ ϵ 2 / ( 2  H ) , \displaystyle\leq\epsilon^{2}/(2H),
(32)
where the inequality follows from Lemma 4.2 with λ = O  ( 1 / ϵ ) \lambda=O(1/\epsilon) . Now, using λ = 2  H / ϵ \lambda=2H/\epsilon and multiplying both the sides we get the results.
Report issue for preceding element
Violation Gap: We now bound the violation.
Report issue for preceding element
max n  J c n π ^ − b n \displaystyle\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}
≤ max  { J c 0 π ^ / λ , max n  J c n π ^ − b n } − max  { J c 0 π ∗ / λ , max n  J c n π ∗ − b n } + H / λ \displaystyle\leq\max{J_{c_{0}}^{\hat{\pi}}/\lambda,\max_{n}J_{c_{n}}^{\hat{\pi}}-b_{n}}-\max{J_{c_{0}}^{\pi^{}}/\lambda,\max_{n}J_{c_{n}}^{\pi^{}}-b_{n}}+H/\lambda
≤ ϵ 2 / ( 2  H ) + ϵ / 2 ≤ ϵ , \displaystyle\leq\epsilon^{2}/(2H)+\epsilon/2\leq\epsilon,
(33)
where we use the fact that J c 0 π ∗ / λ ≤ H / λ ≤ ϵ / 2 J_{c_{0}}^{\pi^{*}}/\lambda\leq H/\lambda\leq\epsilon/2 . Hence, the result follows. ∎
Report issue for preceding element
Appendix D Robust policy evaluator based on KL divergence
Report issue for preceding element
Robust Policy evaluator: Our algorithm assumes the existence of a robust policy evaluator oracle that evaluates max P ∈ ℙ  J c i π , P \max_{P\in\mathbb{P}}J^{\pi,P}{c{i}} for a given π \pi . There are many evaluation techniques that are used to efficiently evaluate a robust policy perturbed by popular uncertainty measures. In this work, we evaluate our policies using a variant EPIRC-PGS algorithm [ 8] for KL uncertainty set (as shown in Algorithm 2).
Report issue for preceding element
The general robust DP equation is given by Equation ( 34)
Report issue for preceding element
(ROBUST DP):
Q c n ( t + 1 )  ( s , a ) = c n  ( s , a ) + γ  max p ∈ ℙ  ∑ s ′ ∈ 𝒮 p  ( s ′ )  V c n t  ( s ′ ) , \displaystyle~Q_{c_{n}}^{(t+1)}(s,a)=c_{n}(s,a)+\gamma\underset{p\in\mathbb{P}}{\max}\sum_{s^{\prime}\in\mathcal{S}}p(s^{\prime})V_{c_{n}}^{t}(s^{\prime}),
(34)
where  V c n t  ( s ′ ) := ∑ a ′ ∈ 𝒜 π  ( s ′ , a ′ )  Q c n t  ( s ′ , a ′ ) . \displaystyle\text{where }V_{c_{n}}^{t}(s^{\prime})=\sum_{a^{\prime}\in\mathcal{A}}\pi(s^{\prime},a^{\prime})Q_{c_{n}}^{t}(s^{\prime},a^{\prime}).
ℙ = ⊗ s , a ℙ ( s , a ) where ℙ ( s , a ) = { P ∈ Δ ( 𝒮 ) | KL [ P | P 0 ( . | s , a ) ] ≤ C K  L } , \displaystyle\mathbb{P}=\otimes_{s,a}\mathbb{P}{(s,a)}\quad\text{where}\quad\mathbb{P}{(s,a)}={P\in\Delta(\mathcal{S})|\mathrm{KL}\left[P|P_{0}(.|s,a)\right]\leq C_{KL}},
where ℙ \mathbb{P} satisfies ( s , a ) (s,a) -rectangularity assumption and KL  [ p | q ] = ∑ s ∈ 𝒮 p  ( s )  ln  p  ( s ) q  ( s ) \mathrm{KL}[p|q]=\sum_{s\in\mathcal{S}}p(s)\ln{\frac{p(s)}{q(s)}} for two probability distribution p , q ∈ Δ  ( 𝒮 ) p,q\in\Delta(\mathcal{S}) . The KL uncertainty evaluator (see Algorithm 2) is justified by Lemma 4 and 5 in [ 8] .
Report issue for preceding element
Algorithm 2 KL Uncertainty Evaluator
1: Input: policy π \pi , nominal probability transition function p 0 p^{0} , perturbation parameter C K  L C_{KL} , c i = [ c 0 , c 1 , …  c K ] c_{i}=\left[c_{0},c_{1},\ldots c_{K}\right] ,discount factor γ \gamma , ρ \rho , | 𝒮 | , | 𝒜 | |\mathcal{S}|,|\mathcal{A}|
2: Q , V Q,V = Robust_Q-table( c i c_{i} , π \pi , p 0 p^{0} , C K  L C_{KL} ) (see Algorithm 3)
3: P ∗ [ s , a , . ] = p 0 [ s , a , . ] exp ( V [ . ] C K  L ) ∑ s ′ ∈ 𝒮 p 0  [ s , a , s ′ ]  exp  ( V  [ s ′ ] C K  L ) ∀ ( s , a ) ∈ 𝒮 × 𝒜 P^{*}[s,a,.]=\frac{p^{0}[s,a,.]\exp{\left(\frac{V[.]}{C_{KL}}\right)}}{\sum_{s^{{}^{\prime}}\in\mathcal{S}}p^{0}[s,a,s^{{}^{\prime}}]\exp{\left(\frac{V[s^{{}^{\prime}}]}{C_{KL}}\right)}}~\forall(s,a)\in\mathcal{S}\times\mathcal{A}
4: T  [ s , s ′ ] = Σ a ∈ 𝒜  π  ( a | s )  P ∗  ( s , a , s ′ ) , ∀ ( s , s ′ ) ∈ 𝒮 × 𝒮 T[s,s^{\prime}]=\underset{a\in\mathcal{A}}{\Sigma}\pi(a|s)P^{*}(s,a,s^{\prime}),\quad\forall(s,s^{\prime})\in\mathcal{S}\times\mathcal{S}
5: Q c i , P ∗ π = ( I − γ  T ) − 1  c i Q^{\pi}{c{i},P^{*}}=(I-\gamma T)^{-1}c_{i}
6: J ^ = ρ T  ( Σ a ∈ 𝒜  ( π  ( a | s )  Q c i , P ∗ π  ( s , a ) ) ) \hat{J}=\rho^{T}\left(\underset{a\in\mathcal{A}}{\Sigma}(\pi(a|s)Q^{\pi}{c{i},P^{*}}(s,a))\right)
7: d P ∗ π = ( 1 − γ )  ( I − γ  T ) − 1  ρ d^{\pi}_{P^{*}}=(1-\gamma)(I-\gamma T)^{-1}\rho
8: ∇ J ^ = H  d P ∗ π  ( s )  Q c i , P ∗ π  ( s , a )  ∀ ( s , a ) ∈ 𝒮 × 𝒜 \nabla\hat{J}=Hd^{\pi}{P^{*}}(s)Q^{\pi}{c_{i},P^{*}}(s,a)~~\forall~(s,a)\in\mathcal{S}\times\mathcal{A}
9: Return: J ^ , ∇ J ^ \hat{J},\nabla\hat{J}
Report issue for preceding element
The KL uncertainty evaluator follows from Lemma D.1. In Algorithm 2, we need the Robust_Q-table. The compact algorithm for that is given in Algorithm 3.
Report issue for preceding element
Algorithm 3 Robust_Q-table
1: Input: c i , π , p 0 , C K  L , ρ c_{i},\pi,p^{0},C_{KL},\rho
2: Initialize: Q  ( s , a ) = 0  ∀ ( s , a ) ∈ 𝒮 × 𝒜 Q(s,a)=0~\forall(s,a)\in\mathcal{S}\times\mathcal{A} , V  ( s ) = 0  ∀ s ∈ 𝒮 , Q p  r  e  v  ( s , a ) = 0  ∀ ( s , a ) ∈ 𝒮 × 𝒜 V(s)=0~\forall s\in\mathcal{S},Q_{prev}(s,a)=0~~\forall(s,a)\in\mathcal{S}\times\mathcal{A}
3: s = ρ ( . ) , τ = 1000 , i = 1 s=\rho(.),~\tau=1000,~i=1
4: while i < τ i<\tau do
5: Q p  r  e  v  ( s , a ) = Q  ( s , a )  ∀ ( s , a ) ∈ 𝒮 × 𝒜 Q_{prev}(s,a)=Q(s,a)~~\forall(s,a)\in\mathcal{S}\times\mathcal{A}
6: a = π ( . | s ) a=\pi(.|s)
7: s ′ = p 0 ( . | s , a ) s^{\prime}=p^{0}(.|s,a)
8: P ∗ = p 0 [ s , a , . ] exp ( V [ . ] C K  L ) ∑ s ′ ∈ 𝒮 p 0  [ s , a , s ′ ]  exp  ( V  [ s ′ ] C K  L )  ∀ ( s , a ) P^{*}=\frac{p^{0}[s,a,.]\exp{\left(\frac{V[.]}{C_{KL}}\right)}}{\sum_{s^{{}^{\prime}}\in\mathcal{S}}p^{0}[s,a,s^{{}^{\prime}}]\exp{\left(\frac{V[s^{{}^{\prime}}]}{C_{KL}}\right)}}~\forall(s,a)
9: Q  [ s , a ] = c i  [ s , a ] + γ  ⟨ P ∗ , V ⟩ Q[s,a]=c_{i}[s,a]+\gamma\langle P^{*},V\rangle
10: V [ s ] = ⟨ π [ . | s ] , Q ( s , . ) ⟩ ∀ s ∈ 𝒮 V[s]=\langle\pi[.|s],Q(s,.)\rangle~~\forall s\in\mathcal{S}
11: s = s ′ s=s^{\prime}
12: if Q  ( s , a ) = Q p  r  e  v  ( s , a )  ∀ ( s , a ) ∈ 𝒮 × 𝒜 Q(s,a)=Q_{prev}(s,a)~~\forall(s,a)\in\mathcal{S}\times\mathcal{A} then
13: Break out of loop
14: end if
15: i = i + 1 i=i+1
16: end while
17: Return: Q , V Q,~V
Report issue for preceding element
Lemma D.1.
Report issue for preceding element
( Lemma 4 in [ 31] ) Let v ∈ ℝ | 𝒮 | v\in\mathbb{R}^{|\mathcal{S}|} and 0 < q < Δ  ( 𝒮 ) 0<q<\Delta(\mathcal{S}) . The value of optimization problem
Report issue for preceding element
min p ∈ Δ  ( 𝒮 ) ⟨ p , v ⟩ s u c h t h a t K L [ p | | q ] < C K  L \underset{p\in\Delta(\mathcal{S})}{\min}\langle p,v\rangle~such~that~KL[p||q]<C_{KL}
(35)
is equal to
Report issue for preceding element
min θ ≥ 0  θ  C K  L + θ  ln  ( ⟨ q , exp  ( − v θ ) ⟩ ) . \displaystyle\min_{\theta\geq 0}\theta C_{KL}+\theta\ln{(\langle q,\exp{(-\frac{v}{\theta})}\rangle)}.
(36)
Let θ ∗ \theta^{*} be the solution of equation ( 36), then the solution of ( 35) becomes,
Report issue for preceding element
p ∝ q  exp  ( − v θ ∗ ) . p\propto q\exp{(-\frac{v}{\theta^{*}})}.
(37)
Using lemma 37, Equation ( 34) can be implemented as
Report issue for preceding element
Q c n ( t + 1 )  ( s , a ) = c n  ( s , a ) + γ  ∑ s ∈ 𝒮 P ( s , a ) ∗  ( s ′ )  V c n ( t )  ( s ′ ) , \displaystyle Q_{c_{n}}^{(t+1)}(s,a)=c_{n}(s,a)+\gamma\sum_{s\in\mathcal{S}}P^{*}{(s,a)}(s^{\prime})V{c_{n}}^{(t)}(s^{\prime}),
(38)
where P ( s , a ) ∗ ∝ p 0 ( . | s , a ) exp ( V c n t ( . ) θ ( s , a ) ∗ ) , \displaystyle\text{where }P^{}{(s,a)}\propto p^{0}(.|s,a)\exp{\left(\frac{V{c_{n}}^{t}(.)}{\theta^{}_{(s,a)}}\right)},
and θ ( s , a ) ∗ := arg min θ ≥ 0 θ C K  L + θ ln ( ⟨ p 0 ( . | s , a ) , exp ( V c n t ( . ) θ ) ⟩ ) . \displaystyle\text{and }\theta^{*}{(s,a)}=\arg\min{\theta\geq 0}\theta C_{KL}+\theta\ln{\left(\langle p^{0}(.|s,a),\exp\left(\frac{V_{c_{n}}^{t}(.)}{\theta}\right)\rangle\right)}.
While Equation ( 36) is convex in nature, solving it for all p ( . | s , a ) ∀ ( s , a ) ∈ ( 𝒮 , 𝒜 ) p(.|s,a)\forall(s,a)\in(\mathcal{S},\mathcal{A}) in Equation ( 38) is computationally extensive in practice. Rather than the exact constrained problem, [ 58] proposed a regularized robust DP update.
Report issue for preceding element
Q c n ( t + 1 ) ( s , a ) = c n ( s , a ) + γ max p ∈ Δ 𝒮 ( ∑ s ′ ∈ 𝒮 p ( s ′ ) V c n t ( s ′ ) − C K  L ′ K L [ p | | p 0 ( . | s , a ) ] ) , \displaystyle Q_{c_{n}}^{(t+1)}(s,a)=c_{n}(s,a)+\gamma\underset{p\in\Delta_{\mathcal{S}}}{\max}\left(\sum_{s^{\prime}\in\mathcal{S}}p(s^{\prime})V_{c_{n}}^{t}(s^{\prime})-C_{KL}^{{}^{\prime}}KL[p||p^{0}(.|s,a)]\right),
(39)
where C K  L ′ > 0 C^{{}^{\prime}}_{KL}>0 is a constant. This regularized form can be efficiently written as Equation ( 40)
Report issue for preceding element
Q c n ( t + 1 ) = c n  ( s , a ) + γ  ( Σ s ′ ∈ 𝒮  P ( s , a ) ∗  ( s ′ )  V c n t  ( s ′ ) ) , \displaystyle Q_{c_{n}}^{(t+1)}=c_{n}(s,a)+\gamma\left(\underset{s^{\prime}\in\mathcal{S}}{\Sigma}P^{*}{(s,a)}(s^{\prime})V{c_{n}}^{t}(s^{\prime})\right),
(40)
where P ( s , a ) ∗ ∝ p 0 ( . | s , a ) exp ( V c n t ( . ) C K  L ′ ) . \displaystyle\text{where }P^{*}{(s,a)}\propto p^{0}(.|s,a)\exp{\left(\frac{V{c_{n}}^{t}(.)}{C^{{}^{\prime}}_{KL}}\right)}.
The equivalence can be concluded from the duality since it is convex optimization problem. The following lemma also shows that the convergence is fast.
Report issue for preceding element
Lemma D.2.
Report issue for preceding element
(Adaptation from Proposition 3.1 and Theorem 3.1 [ 58] ) For any C K  L ′ > 0 C_{KL}^{{}^{\prime}}>0 , there exists C K  L > 0 C_{KL}>0 such that Equation ( 39) converges linearly to the fixed point of Equation ( 38).
Report issue for preceding element
Appendix E Experiments
Report issue for preceding element
The environments where we test our algorithms are as given below (Some results are shown in the main paper under Experiments section (Section 5)). Before moving on to the individual environment, we first state the hyper-parameters that are fixed throughout the environments.
Report issue for preceding element
Common hyperparameters
Report issue for preceding element
The initial state distribution, denoted by ρ \rho , is generated by sampling from a standard normal distribution followed by applying a softmax transformation to convert the resulting values into a valid probability distribution over states. In particular, for each state, a random number is generated from 𝒩  ( 0 , 1 ) \mathcal{N}(0,1) . Then it is normalized using softmax in order to avoid negative values.
Report issue for preceding element
The discount factor γ \gamma is set to 0.99 0.99 across all algorithms and environments to ensure consistency. However, in order to evaluate computational efficiency (wall-clock time), we run EPIRC_PGS with multiple discount factors: γ = 0.9 \gamma=0.9 , 0.99 0.99 , and 0.995 0.995 .
Report issue for preceding element
EPIRC_PGS follows a double-loop structure, as described in [ 8] , where the outer loop uses the iteration index K K and the inner loop uses index T T . In our experiments, we set K = 10 K=10 and T = 100 T=100 , yielding a total of K × T = 1000 K\times T=1000 iterations. This ensures that all algorithms are compared over the same number of update steps.
Report issue for preceding element
Both RPPG and RNPG require an initial policy specification. For RPPG, we initialize the policy uniformly: π 0  ( a ∣ s ) = 1 / | 𝒜 | \pi^{0}(a\mid s)=1/|\mathcal{A}| for all s ∈ 𝒮 s\in\mathcal{S} . In contrast, RNPG parameterizes the policy directly using a vector θ \theta , where θ 0 ∼ 𝒩  ( 0 , 1 ) \theta^{0}\sim\mathcal{N}(0,1) and | θ 0 | = | 𝒮 | × | 𝒜 | |\theta^{0}|=|\mathcal{S}|\times|\mathcal{A}| .
Report issue for preceding element
Both algorithms also depend on the hyperparameter λ \lambda . For RNPG, λ \lambda is fixed at 50 across all experiments. For RPPG, λ \lambda is treated as a variable hyperparameter, with values specified individually in the corresponding experimental sections.
Report issue for preceding element
The learning rate α \alpha is set to 10 − 3 10^{-3} for all algorithms across all environments. Another important hyperparameter is the loop control variable τ \tau , used in Algorithm 3. The operations inside the loop of Algorithm 3 represent a robust Bellman update. It has been shown in [ 31] that the soft Bellman operator is a contraction mapping. Therefore, setting τ \tau to a large value ensures convergence to a fixed point Q  ( s , a ) Q(s,a) , and subsequently to the corresponding value function V  ( s ) V(s) . In our experiments, we fix τ = 1000 \tau=1000 . For theoretical justification, refer to Lemmas 37 and D.2
Report issue for preceding element
E.1 Constrained River-swim
Report issue for preceding element
The River-swim environment is a widely studied benchmark in optimization theory and stochastic control. The detailed explanation of the algorithm is as given below.
Report issue for preceding element
E.1.1 Environment Description
Report issue for preceding element
The environment consists of six distinct states, conceptualized as islands dispersed across a large body of water. At the start of each episode, a swimmer is placed on one of these landmasses.
Report issue for preceding element
The swimmer's objective is to navigate toward one of the two terminal islands—representing the river's endpoints—to receive a reward. At each state, the swimmer can choose between two actions: swimming to the left or to the right. Rewards are only provided upon reaching the terminal states, whereas all intermediate states yield zero reward (refer to Table 2).
Report issue for preceding element
During the transition between states, the swimmer encounters adversarial elements, such as strong water currents and hostile tribal inhabitants residing on certain islands. These hazards are modeled as a cost incurred for occupying a given state. The transition probabilities between states are compactly represented in Table 2, while the immediate state-wise rewards and constraint costs are summarized in Table 3. Note that the reward is high at the extreme right-hand side as this is the best state, however, it also corresponds to high current or high cost. All the parameters including the value of C K  L C_{KL} of the MDP are represented in Table 4.
Report issue for preceding element
Table 2: Transition probability of River-swim environment Report issue for preceding element
Table 3: The reward and constraint cost received at each state Report issue for preceding element
Table 4: Hyperparameter used for all subroutines for CRS environment Report issue for preceding element 
(a) Expected objective function comparison Report issue for preceding element 
(b) Expected cost function comparison Report issue for preceding element
Figure 3: Comparison of RPPG and EPIRC-PGS on CRS environment Report issue for preceding element 
Report issue for preceding element 
Report issue for preceding element
Figure 4: Effect of λ \lambda on RNPG for the CRS environment Report issue for preceding element
E.1.2 Discussions of the result
Report issue for preceding element
The iteration-wise expected reward (value function) and expected constraint cost are illustrated in Figure 3. From Figure 3(a), we observe that EPIRC_PGS (denoted as EPIRC) achieves the highest objective reward. However, as shown in Figure 3(b), it significantly violates the constraint threshold, failing to remain within the designated safe region. Since the agent's goal is not only to maximize long-term reward but also to ensure safety by satisfying the constraint, EPIRC_PGS falls short in this regard.
Report issue for preceding element
RPPG achieves a higher value function than RNPG, as seen in Figure 3(a). However, a closer look at Figure 3(b) reveals that RPPG also marginally violates the constraint boundaries. RNPG effectively captures the trade-off between reward maximization and the constraint satisfaction, navigating as close as possible to the constraint boundary. It stops at the point where further increase in reward would result in constraint violations, thereby maintaining a feasible and safe policy.
Report issue for preceding element
Our algorithm relies on a key hyperparameter, λ \lambda . This parameter plays a crucial role in balancing the objective and constraint terms during policy updates. Specifically, λ \lambda should be chosen to be sufficiently large such that when the constraint violation J c i π t − b i J_{c_{i}}^{\pi_{t}}-b_{i} is marginal (i.e., J c i π t − b i > ξ J_{c_{i}}^{\pi_{t}}-b_{i}>\xi for some small ξ > 0 \xi>0 and for any i ∈ 1 , 2 , … , K i\in{1,2,\ldots,K} ), the scaled objective term J c 0 π t / λ J_{c_{0}}^{\pi_{t}}/\lambda does not dominate the update direction.
Report issue for preceding element
If λ \lambda is set too small, the influence of the objective term becomes large. As a result, the algorithm may prioritize minimizing the objective cost (or maximizing the reward, depending on the environment setting) at the expense of constraint satisfaction. This contradicts our goal of maximizing the expected objective return such that the expected constraint values are below a certain threshold. To illustrate the impact of λ \lambda on the performance and feasibility of RNPG, we conduct experiments using different values of λ \lambda , with results presented in Figure 4. Note that higher value of λ \lambda indeed reduces the value function, but also decreases the cumulative cost. We set λ = 50 \lambda=50 throughout the experiment for RNPG as it corresponds to feasible solution for each environment. Hence, it shows that for RNPG, we do not need to costly hyper-parameter tuning for λ \lambda as a relatively high value of λ \lambda ensures feasibility as the Theory suggested.
Report issue for preceding element
Furthermore, Table 11 presents a comparison of wall-clock time across the algorithms. RNPG completes in the shortest time, running approximately 1.6 × 1.6\times faster than RPPG and at least 4 × 4\times faster than EPIRC_PGS (at γ = 0.9 \gamma=0.9 ). These results demonstrate that RNPG not only achieves competitive performance but also does so with significantly improved computational efficiency compared to both RPPG and EPIRC_PGS.
Report issue for preceding element
The results highlight RNPG's ability to consistently learn robust and safe policies while outperforming RPPG and EPIRC-PGS in terms of both reliability and computational efficiency, even under adverse environmental dynamics.
Report issue for preceding element
E.2 Garnet problem
Report issue for preceding element
E.2.1 Environment Description
Report issue for preceding element
The Garnet environment is a standard Markov Decision Process (MDP) framework commonly used to evaluate reinforcement learning (RL) algorithms in a controlled setting. It is characterized by a predefined number of states n  S nS and actions n  A nA , where the transition probabilities, rewards, and utility functions are randomly sampled from specified distributions. The transition dynamics in Garnet are typically sparse, meaning that each state does not transition to all other states, but instead has a limited number of possible successor states for each action. Mathematically, the environment is defined by a transition probability matrix P  ( s ′ ∣ s , a ) P(s^{\prime}\mid s,a) , a reward function R  ( s , a ) R(s,a) , and, in the case of constrained RL, a utility function U  ( s , a ) U(s,a) . These elements are often drawn from normal distributions, i.e.,
Report issue for preceding element
P  ( s ′ ∣ s , a ) ∼ 𝒩  ( μ a , σ a ) , R  ( s , a ) ∼ 𝒩  ( μ b , σ b ) , U  ( s , a ) ∼ 𝒩  ( μ c , σ c ) P(s^{\prime}\mid s,a)\sim\mathcal{N}(\mu_{a},\sigma_{a}),\quad R(s,a)\sim\mathcal{N}(\mu_{b},\sigma_{b}),\quad U(s,a)\sim\mathcal{N}(\mu_{c},\sigma_{c})
.
Report issue for preceding element
where the means μ a , μ b , μ c \mu_{a},\mu_{b},\mu_{c} are sampled from a uniform distribution Unif  ( 0 , 100 ) \text{Unif}(0,100) . Since the transition probability matrix must be valid (i.e., each row should sum to 1), the probabilities are exponentiated and normalized using a softmax transformation:
Report issue for preceding element
p 0  ( s ′ ∣ s , a ) = exp  ( P  ( s ′ ∣ s , a ) ) ∑ s ′′ exp  ( P  ( s ′′ ∣ s , a ) ) p^{0}(s^{\prime}\mid s,a)=\frac{\exp(P(s^{\prime}\mid s,a))}{\sum_{s^{\prime\prime}}\exp(P(s^{\prime\prime}\mid s,a))}
.
Report issue for preceding element
E.2.2 Implementation details
Report issue for preceding element
In this environment, both the reward and cost values are stochastic, sampled randomly rather than being deterministically assigned. The cost (or reward) values are generated as follows:
Report issue for preceding element
R = c 0 ∼ 𝒩  ( μ b , σ b ) . R=c_{0}\sim\mathcal{N}(\mu_{b},\sigma_{b}).
(41)
where μ b ∼ 𝒰  [ 0 , 10 ] \mu_{b}\sim\mathcal{U}[0,10] and σ b = 1 \sigma_{b}=1 . Similarly we generate the cost function. Here, we use c 0 c_{0} and R R interchangeably because the Garnet environment is formulated as a reward-based MDP with a utility-based constraint function. Unlike the Constrained River-swim environment, the objective here is to maximize the long-term expected reward while ensuring that the expected utility remains above a specified threshold.
Report issue for preceding element
The hyperparameters used for this environment are listed in Table 5
Report issue for preceding element
Table 5: Hyperparameter used for all subroutines for Garnet environment Report issue for preceding element 
(a) Expected objective function comparison Report issue for preceding element 
(b) Expected cost function comparison Report issue for preceding element
Figure 5: Comparison of RPPG and EPIRC-PGS on Garnet(15,20) environment λ = 30 \lambda=30 Report issue for preceding element
E.2.3 Discussion of Results
Report issue for preceding element
The results are shown in Figure 5. As previously discussed, the Garnet environment incorporates a utility function in the constraint rather than a traditional cost function. Therefore, a feasible optimal policy is expected to yield an expected utility (constraint) value that remains above a predefined threshold. For consistency in terminology and to avoid confusion, we refer to the utility function as the “constraint function” in Figure 5(b).
Report issue for preceding element
From Figure 5(b), it is evident that all three algorithms—RNPG, RPPG, and EPIRC_PGS—satisfy the constraint throughout training, thus producing feasible policies at each iteration. However, Figure 5(a) shows that RNPG achieves a noticeably higher expected objective return compared to both EPIRC_PGS and RPPG.
Report issue for preceding element
Figure 5 provides further insight into RNPG's behavior. Initially, RNPG operates well within the safe region and progressively improves its objective return. As it approaches the constraint boundary, the algorithm detects the potential violation and adjusts its trajectory accordingly—prioritizing safety over additional reward. This contrasts with the behavior of RPPG and EPIRC_PGS, which also maintain feasibility but yield comparatively lower objective returns. These results highlight the advantage of incorporating a natural policy gradient approach, which allows RNPG to balance safety and performance more effectively.
Report issue for preceding element
In addition to performance, we compare the computational efficiency of the algorithms. Table 11 shows that RNPG requires a computation time comparable to RPPG, but significantly outperforms EPIRC_PGS in terms of speed. Specifically, RNPG is at least 5 × 5\times faster than EPIRC_PGS when γ = 0.9 \gamma=0.9 , and nearly 8 × 8\times faster when γ = 0.995 \gamma=0.995 . The increased runtime for EPIRC_PGS at higher discount factors is attributed to the longer binary search required for constraint satisfaction as γ \gamma approaches 1. The key takeaway from this experiment is that RNPG demonstrates greater sensitivity to constraint boundaries and exhibits strong potential for scalability to larger state and action spaces. Notably, the Garnet environment used in this study contains 15 states and 20 actions. These results suggest that, with efficient implementation, RNPG can be effectively extended to high-dimensional settings.
Report issue for preceding element
E.3 Modified Frozen-lake
Report issue for preceding element
The general Frozen-lake is as special type of grid world problem. The vanilla Frozen-lake problem can be found in gymnasium library [ 59] . However, in this work, we create a small modification to make the problem more challenging and interesting.
Report issue for preceding element
E.3.1 Environment description
Report issue for preceding element
The Frozen Lake environment is modeled as a d × d d\times d grid world, where the agent begins its journey at the top-left corner, s 0 = ( 0 , 0 ) s_{0}=(0,0) , and aims to reach the bottom-right goal state s d 2 − 1 = ( d − 1 , d − 1 ) s_{d^{2}-1}=(d-1,d-1) . At each time step, the agent may choose one of four primitive actions: move left, right, up, or down, constrained by the grid boundaries.
Report issue for preceding element
The environment contains multiple types of states:
Report issue for preceding element
• Goal state: Reaching the terminal state yields a high reward. Report issue for preceding element
• Hole states: If the agent steps into a hole, it falls in and receives a very low reward. Report issue for preceding element
• Normal states: All other transitions yield a moderate reward. Report issue for preceding element
In addition to reward dynamics, the environment contains hazardous blocks, which are selected randomly at each iteration. These represent dynamic threats (e.g., thin ice, traps, or roaming predators) and impose a high constraint cost when visited. The stochastic nature of these threats introduces uncertainty in the agent's experience, making the problem both risky and difficult to optimize.
Report issue for preceding element
The agent's objective is to learn a policy that maximizes the expected cumulative reward while incurring only marginal harm. In other words, it must learn to reach the goal while minimizing the cumulative constraint cost associated with hazardous states.
Report issue for preceding element
We formulate this problem as a Constrained Markov Decision Process (CMDP) under model uncertainty. For all experiments, we set the grid size to d = 4 d=4 . To map a 2D coordinate ( x , y ) (x,y) to its corresponding 1D state index, we define a wrapping function:
Report issue for preceding element
wrap  ( ( x , y ) ) = x × d + y . \text{wrap}((x,y))=x\times d+y.
The probability distribution function is shown in Table 6.
Report issue for preceding element
Table 6: Transition probabilities for Frozen lake environement Report issue for preceding element
The rewards and cost functions are given in Table 7. In particular, if it reaches the goal state the reward is + 1 +1 . If the agent hits the obstacle, the cost is 1 1 , and and the frozen grid it is 0.3 0.3 . Note that the a grid is obstacle or not is decided randomly at the beginning of an episode.
Report issue for preceding element
Table 7: State wise rewards and constraint cost for the Frozen lake environment Report issue for preceding element
We detail all the other parameters in Table 8.
Report issue for preceding element
Table 8: Hyperparameter used for all subroutines for Modified Frozen-lake environment Report issue for preceding element 
(a) Expected objective function comparison Report issue for preceding element 
(b) Expected cost function comparison Report issue for preceding element
Figure 6: Comparison of RNPG, RPPG and EPIRC-PGS on Modified Frozen-lake environment Report issue for preceding element
E.3.2 Discussion of results
Report issue for preceding element
The results obtained of the given environment is depicted in Figure 6. As seen in Figure 6(b), all the three algorithms successfully learns the feasible policies. However, on observing Figure 6(a), we can clearly notice the dominance of RNPG by learning policies with better rewards. From Table 11, we see that for the frozen lake environment, the computation time of RPPG and RNPG is almost comparable. However, RNPG is atleast 3 3 x as faster as EPIRC-PGS for γ = 0.9 \gamma=0.9 and almost 4 4 x faster than EPIRC-PGS for γ = 0.995 \gamma=0.995 .
Report issue for preceding element
The key takeaway from this enviornment is to show that even with added obstacles randomly, the agent can find a feasible high objective return policy as compared to RPPG and EPIRC-PGS
Report issue for preceding element
E.4 Garbage collection problem
Report issue for preceding element
E.4.1 Environment description
Report issue for preceding element
We model a city as a 4 × 4 4\times 4 grid, where each cell represents a city block. A garbage collection robot is deployed to navigate this grid and collect waste while minimizing operational risk and resource expenditure.
Report issue for preceding element
Certain blocks offer higher rewards due to significant waste accumulation (e.g., near hospitals or markets). However, urban conditions are inherently dynamic. These high-reward blocks are not known in advance and are constantly changing showing the rapid changes of city areas. At each time step, 40 % 40% of the blocks are randomly designated as hazardous, representing unpredictable real-world events such as:
Report issue for preceding element
• Sudden traffic congestion Report issue for preceding element
• Unreported toxic waste dumps Report issue for preceding element
• Temporary road closures or civil disturbances Report issue for preceding element
These hazardous blocks incur a higher constraint cost if visited. Importantly, the set of hazardous blocks changes at every iteration, introducing a layer of real-time uncertainty in the environment.
Report issue for preceding element
The robot must learn a policy that balances the dual objectives of:
Report issue for preceding element
Maximizing long-term reward by collecting from high-value blocks Report issue for preceding element
Minimizing cumulative constraint costs induced by environmental hazards Report issue for preceding element
The transition probabilities are similar to the Frozenlake environment. Hence the transition probabilities for this environment can be depicted by Table 6. The reward and cost structure is given in Table 9. While the reward is fixed at the Goal location, the reward at garbage location is 0.01 0.01 . Note that whether a certain grid is a garbage location or not is decided randomly. Similarly, the cost is 1 1 at a blocked grid. Again, the identities of the blocked grids are randomly decided.
Report issue for preceding element
Table 9: Reward and cost structure for Garbage collector environment Report issue for preceding element
The hyperparameters for the various sub-routines are as listed in Table 10.
Report issue for preceding element
Table 10: Hyperparameter used for all subroutines for Garbage collector environment Report issue for preceding element 
(a) Expected objective function comparison Report issue for preceding element 
(b) Expected cost function comparison Report issue for preceding element
Figure 7: Comparison of RNPG, RPPG and EPIRC-PGS (or, EPIRC_PGS) on Garbage collector environment Report issue for preceding element
E.4.2 Discussion of results
Report issue for preceding element
In this subsection, we will present the performance of the RPPG, EPIRC_PGS and our algorithm (RNPG)(Figure 7). As shown in Figure 7(b), due to the randomness of the environment, the algorithms have some minor fluctuations. However, in this environment, RPPG and RNPG obey the constraints for the complete duration, but, EPIRC_PGS violates the constraint. Although none of the algorithms stabilize completely yet RPPG and RNPG are in the safe zone. In terms of objective return, it can be seen from Figure 7(a), the expected return for RNPG is predominantly higher than RPPG and EPIRC_PGS. While comparing the time (Table 11) for completion RPPG is the fastest in this environment marginally beating RNPG but still the speeds of both algorithms are comparable. When compared with EPIRC_PGS, RNPG is winning fairly with a speedup of 2 2 x compared to EPIRC_PGS when γ = 0.9 \gamma=0.9 and a speedup of nearly 3 3 x compared to EPIRC_PGS when γ = 0.995 \gamma=0.995 .
Report issue for preceding element
This environment demonstrates that, even under random obstacle placement, the agent can successfully learn a feasible policy that outperforms RPPG and EPIRC_PGS in terms of objective return.
Report issue for preceding element
Table 11: Comparison of the best policy objective ( v f v_{f} ) and constraint function ( c f c_{f} ) values. b 1 b_{1} indicates the threshold value. RNPG not only achieves the best value, but also gives a feasible policy. Report issue for preceding element
Appendix F Implementation Details of RNPG and RPPG
Report issue for preceding element
F.1 RNPG
Report issue for preceding element
Note that in ( 11) one can use direct parameterization for policy update in RNPG. To facilitate optimization, we also adopt a soft-max representation of the policy space. Let the policy be parameterized by θ \theta , such that:
Report issue for preceding element
π θ t  ( a ∣ s ) = exp  ( θ t  [ s ] ) ∑ s ∈ 𝒮 exp  ( θ  [ s ] ) . \pi^{\theta_{t}}(a\mid s)=\frac{\exp{(\theta_{t}[s])}}{\sum_{s\in\mathcal{S}}\exp{(\theta[s])}}.
(42)
Using this parameterization, we reformulate the policy update as the solution to the following constrained optimization problem:
Report issue for preceding element
θ t + 1 ∈ arg  max θ t + 1  ⟨ ∇ J c ch π θ t , θ t + 1 − θ t ⟩ − α t  KL  ( π θ t + 1 ∥ π θ t ) , \displaystyle\theta_{t+1}\in\arg\max_{\theta_{t+1}}\left\langle\nabla J^{\pi_{\theta_{t}}}{c{\text{ch}}},\theta_{t+1}-\theta_{t}\right\rangle-\alpha_{t},\mathrm{KL}(\pi_{\theta_{t+1}}|\pi_{\theta_{t}}),
(43)
where the objective index ch is selected as:
Report issue for preceding element
ch = arg  max  { J c 0 π θ t λ , max i = 1 , … , K  ( J c i π θ t − b i ) } . \text{ch}=\arg\max\left{\frac{J_{c_{0}}^{\pi_{\theta_{t}}}}{\lambda},\max_{i=1,\ldots,K}\left(J_{c_{i}}^{\pi_{\theta_{t}}}-b_{i}\right)\right}.
This formulation enables us to apply the Natural Policy Gradient method by incorporating the geometry of the policy space through the Fisher Information Matrix ℱ \mathcal{F} [ 60] . The resulting closed-form update rule is:
Report issue for preceding element
θ t + 1 = θ t − α lr ⋅ 1 2  α t  ℱ − 1  ∇ J c ch π θ t . \theta_{t+1}=\theta_{t}-\alpha_{\text{lr}}\cdot\frac{1}{2\alpha_{t}},\mathcal{F}^{-1}\nabla J^{\pi_{\theta_{t}}}{c{\text{ch}}}.
F.2 Robust Projected Policy Gradient (RPPG)
Report issue for preceding element
We also compare the Robust Projected Policy Gradient (RPPG) which uses ℓ 2 \ell_{2} regularization instead of the KL regularization. Here, we use direct parameterization. The policy update is given in the following.
Report issue for preceding element
π t + 1 ∈ arg  min π ∈ Π  ⟨ ∇ π t J i  ( π t ) , π − π t ⟩ + 1 2  α t  ‖ π − π t ‖ 2 , \displaystyle\pi_{t+1}\in\arg\min_{\pi\in\Pi}\left\langle\nabla_{\pi_{t}}J_{i}(\pi_{t}),\pi-\pi_{t}\right\rangle+\frac{1}{2\alpha_{t}}|\pi-\pi_{t}|^{2},
(44)
where i = arg  max  { J c 0 π λ , max n  ( J c n π − b n + ξ ) } i=\arg\max\left{\frac{J_{c_{0}}^{\pi}}{\lambda},\max_{n}\left(J_{c_{n}}^{\pi}-b_{n}+\xi\right)\right} .
Report issue for preceding element
Upon careful observation, we see that Equation ( 44) is convex. To find the optimal solution of π t + 1 \pi_{t+1} , we use projected gradient descent. Equation ( 44) can be updated as
Report issue for preceding element
π t + 1 = arg  min π ∈ Π  ‖ π − ( π t − α t  ∇ π t J i π t ) ‖ 2 . \displaystyle\pi_{t+1}=\arg\min_{\pi\in\Pi}\left|\pi-\left(\pi_{t}-\alpha_{t}\nabla_{\pi_{t}}J_{i}^{\pi_{t}}\right)\right|^{2}.
(45)
This is the Euclidean projection of the gradient step onto the simplex:
Report issue for preceding element
π t + 1 = Π Δ  ( π t − α t  ∇ π t J i  ( π t ) ) \displaystyle\pi_{t+1}=\Pi_{\Delta}\left(\pi_{t}-\alpha_{t}\nabla_{\pi_{t}}J_{i}(\pi_{t})\right)
(46)
From Lemma 3.1, we get the value of ∇ π t J i  ( π t ) \nabla_{\pi_{t}}J_{i}(\pi_{t}) using the robust Q value evaluator in Algorithm 3. We finally project the resulting value into the policy space simplex, Π \Pi . To perform projection, we find ‖ π − ( π t − α t  ∇ π t J i  ( π t ) ) ‖ 2  ∀ π ∈ Π |\pi-(\pi_{t}-\alpha_{t}\nabla_{\pi_{t}}J_{i}(\pi_{t}))|_{2}~\forall~\pi\in\Pi . However, this process is cumbersome, hence we can leverage the cvxpy package from Python to optimally solve the update equation.
Report issue for preceding element
Algorithm 4 Robust-Projected Policy Gradient for CMDP with uncertainties (R-PPG)
1: Input: Robust Policy evaluator (Algorithm 2), b i  s . t . i ∈ { 1 , K } , ξ , λ b_{i}~~~s.t.~i\in{1,K},\xi,\lambda
2: Initialization: π ^ ( ⋅ | s ) 0 = 1 / | A | \hat{\pi}(\cdot|s)_{0}=1/|A| for all s s , T.
3: for t = 0 , … , T − 1 t=0,\ldots,T-1 do
4: Evaluate J j π t = max P  J j , P π t J_{j}^{\pi_{t}}=\max_{P}J_{j,P}^{\pi_{t}} for j = { c 0  …  c K } j={c_{0}\ldots c_{K}} using the robust policy evaluator oracle.
5: c  h = arg  max  ( J c 0 π t / λ , J c i π t − b i + ξ )  s . t . i ∈ { 1 , K } ch=\arg\max(J_{c_{0}}^{\pi_{t}}/\lambda,J_{c_{i}}^{\pi_{t}}-b_{i}+\xi)~s.t.~i\in{1,K}
6: if c  h ≠ 0 ch\neq 0 then
7: π t + 1 = Proj Π  { π t − α t  ∇ J c c  h π t } \pi_{t+1}=\mathrm{Proj}{\Pi}{\pi{t}-\alpha_{t}\nabla J_{c_{ch}}^{\pi_{t}}} .
8: else
9: π t + 1 = Proj Π  { π t − α t  ∇ J c 0 π t / λ } \pi_{t+1}=\mathrm{Proj}{\Pi}{\pi{t}-\alpha_{t}\nabla J_{c_{0}}^{\pi_{t}}/\lambda}
10: end if
11: end for
12: Output π ^ = arg  min t ∈ 0 , … , T − 1  max  { J c 0 π t / λ , max i  { J c i π t − b + ξ } } \hat{\pi}=\arg\min_{t\in 0,\ldots,T-1}\max{J_{c_{0}}^{\pi_{t}}/\lambda,\max_{i}{J_{c_{i}}^{\pi_{t}}-b+\xi}}
Report issue for preceding element
As shown in Algorithm 4, RPPG leverages Projected Policy Gradient method to reach the optimal policy. In general ℓ 2 \ell_{2} regularizer does not ensure small changes in the policies and might deviate a lot from the previous policy. Thus, KL-regularizer has a better performance over ℓ 2 \ell_{2} regularizer which we further demonstrate by our results in Section E.
Report issue for preceding element
Appendix G Extension to Continuous state space (Robust Constrained Actor Critic)
Report issue for preceding element
We present our robust constrained actor–critic framework designed for the function approximation setting as discussed in Section 6.1. The model comprises two critic networks—one estimating the reward value function J c 0 J_{c_{0}} and the other corresponding to the Constraint value function J c 1 J_{c_{1}} . Although we focus on a single constraint for clarity, the framework readily generalizes to handle multiple constraints. In addition to the critic networks, an actor network is employed to generate actions based on the current state. To model distributional robustness, we consider IPM as described in Section 6.1.
Report issue for preceding element
Let us consider the critic network be parameterized by w w where each layer contains d d paramters including the bias (i.e, w 1 : d l w^{l}{1:d} where w 1 l w^{l}{1} is assumed to be the bias term in the l l -th layer with l ∈ { 1 , 2 , … , L } l\in{1,2,\ldots,L} ). Overall approach is depicted in Algorithm 5.
Report issue for preceding element
Algorithm 5 Robust Constrained Actor Critic (RCAC)
1: Input: T , ρ , b T,\rho,b
2: Initialization: w r w_{r} (for objective estimation), w c w_{c} (for constraint estimation) and θ 0 \theta^{0} for actor network parameterization
3: for t = 0 , … , T − 1 t=0,\ldots,T-1 do
4: Get estimate for J r = ⟨ ρ , V w r  ( s ) ⟩ J_{r}=\langle\rho,V_{w_{r}}(s)\rangle and J c = ⟨ ρ , V w c  ( s ) ⟩ J_{c}=\langle\rho,V_{w_{c}}(s)\rangle
5: c  h = arg  max  ( J r / λ , ( J c − b ) ) ch=\arg\max(J_{r}/\lambda,(J_{c}-b))
6: Update w c  h w_{ch} using w c  h = w c  h + α k . ∇ w c  h w_{ch}=w_{ch}+\alpha_{k}.\nabla_{w_{ch}} MSE( ⟨ ρ , V t  ( s ) ⟩ , J c  h \langle\rho,V_{t}(s)\rangle,J_{ch} ) (Note V t  ( s ) V_{t}(s) is target Value function obtained by Robust_TD_update (using equation ( 15)))
7: Update θ \theta using θ t = θ t − 1 + α . 𝔼 [ ∇ θ log ( π θ ( a | s ) ) . ( Q c  h ( s , a ) − V c  h ( s ) ) ] \theta^{t}=\theta^{t-1}+\alpha.\mathbb{E}\left[\nabla_{\theta}\log(\pi_{\theta}(a|s)).(Q_{ch}(s,a)-V_{ch}(s))\right] (We change this step to Natural Policy Gradient update for RCAC_NPG).
8: end for
Report issue for preceding element
At each step, we get the Value function estimate V r V_{r} and V c V_{c} from the respective Critic networks. After obtaining both, we make a choice as to whether to update the constraint critic parameters or the objective critic parameters. For the selected critic, we find the target value function using the robust bellman operator along with a guided regularization term on the last layer only [ 54] . We compute the robust value according to ( 15).
Report issue for preceding element
For our experiments, we chose the famous Cartpole environment, where the intial state is fixed and deterministic so ρ  ( i ) \rho(i) is a unit vector.(However, it can be extended to different distribution.)
Report issue for preceding element
ρ  ( s ) = { 1 if s = s 0 0 otherwise \rho(s)=\begin{cases}1&\text{if $s=s_{0}$}\ 0&\text{otherwise}\end{cases}
(47)
In our study, we introduced uncertainty in the next-state transition after each action. While alternative sources of uncertainty could be incorporated—such as perturbing the executed actions or simulating external disturbances (e.g., wind forces acting on the cart)—we focused on state transition perturbations because they have a more direct and analyzable impact on value estimation. Perturbing the action space was deemed less meaningful in this environment, as the action set is discrete with only two possible values, making the resulting learning challenge comparatively trivial. The detailed results and observations are presented in the following subsection.
Report issue for preceding element
G.1 Results and discussion
Report issue for preceding element
In this sub-section, we list the results obtained when we tried our algorithm against the standard cartpole-v1 environment available in gymnasium library. The cartpole-v1 algorithm comprises of a continuous state space having 4 components and two discrete actions. We introduce uncertainity by adding noise to the next state obtained after taking an action. The noise is adding a uniform value between 0 and 0.1 to the original next state value ( s ′ = s ′ + U  n  i  f  ( [ 0 , 0.1 ] ) s^{{}^{\prime}}=s^{{}^{\prime}}+Unif([0,0.1]) ) and then clipped it between the predefined bounds of cartpole environment.
Report issue for preceding element
We divided the experiments results into two phases. The first is the training phase (depicted by Figures 8) and the second is during the testing phase (depicted by Figures 9). During the training phase, we only train the robust variants RCAC, RCAC with NPG, Robust CRPO, EPIRC-PGS by considering δ = 0.04 \delta=0.04 . However, for constrained actor-critic (CAC), we do not train the robust version. During the training phase (Figure 8), apart from EPIRC-PGS, all the algorithms perform similarly in terms of reward and the cost value function (We highlight our two algorithms RCAC with NPG, and RCÅC, separately in figure 10). EPIRC-PGS did not converge and could not complete the entire episode highlighting that binary search approach is not possible to scale for large state-space. However, when these algorithms were tested (Figure 9) on the environment having a perturbation uniformly between 0 and 0.04, the performance of CAC is unstable and did not provide any feasible policy. Only, our proposed approaches achieve feasibility while being close to the optimality. Robust CRPO also violates the constraint (slightly) while achieving less reward compared to our approaches. The performances of the algorithms is compactly represented in table 12.
Report issue for preceding element
It is also important to note down the wall clock time for the various algorithms. EPIRC_PGS takes the highest wall clock time approximately 24029.013 seconds which is nearly 4 × 4\times of the time taken for the other algorithms namely RCAC with NPG (7175.31 seconds), CAC(6815.89 seconds), RCAC (5975.65 seconds) and Robust CRPO (4275.67 seconds) in decreasing order of the wall clock time requirements. 9.
Report issue for preceding element 
(a) Value function comparison Report issue for preceding element 
(b) Cost function comparison Report issue for preceding element
Figure 8: Comparison of RCAC, RCAC_NPG, robust CRPO and other standard Constrained MDP solutions on the Cartpole problem during training phase Report issue for preceding element 
(a) Value function comparison Report issue for preceding element 
(b) Cost function comparison Report issue for preceding element
Figure 9: Comparison between RCAC, CRPO and Vanilla Constrained Actor Critic during testing period δ = 0.04 \delta=0.04 (deflection from the nominal model) Report issue for preceding element
Table 12: Tabular comparisons of the average value function and cost function during the testing phase. CAC although returns policies with high objective function but the actions are unsafe as can be inferred from the high constraint function (safety baseline is 200) Report issue for preceding element 
(a) Value function comparison Report issue for preceding element 
(b) Cost function comparison Report issue for preceding element
Figure 10: The comparison plots between our two main variants of Robust Constrained Actor Critic variants (RCAC and RCAC_NPG) Report issue for preceding element
Appendix H Connection with the CRPO
Report issue for preceding element
CRPO is one of the popular approach for non-robust CMDP which has been proposed in [ 11] . In the CRPO algorithm, one minimizes the objective when all the constraints are satisfied, and minimizes the constraint value if the policy violates the constraint for at least one constraint. In particular, the objective function can be represented as
Report issue for preceding element
min π  J c 0 π  𝟙  ( max n  J c n − b n ≤ 0 ) + max n  ( J c n − b n )  𝟙  ( max n  J c n − b n > 0 ) . \displaystyle\min_{\pi}J_{c_{0}}^{\pi}\mathbbm{1}(\max_{n}J_{c_{n}}-b_{n}\leq 0)+\max_{n}(J_{c_{n}}-b_{n})\mathbbm{1}(\max_{n}J_{c_{n}}-b_{n}>0).\vskip-14.45377pt
(48)
Thus, one might think that there are some connections with our approach and the robust CRPO. First, we provide the challenges in extending the results to the RCMDP case. In [ 11] , they bound the difference in the value function corresponding to the policies between two steps using the standard value difference lemma. However, the standard value difference lemma does not hold in the robust case as the worst case transition probabilities differ according to the probabilities.
Report issue for preceding element
In what follows, we point out the difference of our approach and potentially robust CRPO approach. In order to obtain iteration complexity, we seek to use the smoothness property of the objective by invoking Moreu's envelope as done in [ 8] . In particular, we use a smooth function max  { J r π / λ , max n  J c n π − b n } \max{J_{r}^{\pi}/\lambda,\max_{n}J_{c_{n}}^{\pi}-b_{n}} as an objective instead of the one in ( 48). It turns out the this modification is essential for obtaining the iteration complexity. Note the difference–we are not switching to minimize the constraint cost value functions when the constraints are not satisfied, rather we are only minimizing those when max n  J c n π − b n \max_{n}J_{c_{n}}^{\pi}-b_{n} becomes larger than J c 0 π / λ J_{c_{0}}^{\pi}/\lambda . Thus, as λ \lambda becomes larger it becomes similar to CRPO. Also, note that in the asymptotic sense as λ → ∞ \lambda\rightarrow\infty , we can not guarantee the sub-optimality gap anymore showing that perhaps, robust CRPO algorithm may not achieve the iteration complexity bound.
Report issue for preceding element
Report Issue
Report GitHub Issue
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub
Report Issue for Selection
Generated by L A T E xml[LOGO]
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" button.
Open a report feedback form via keyboard, use " Ctrl + ?".
Make a text selection and click the "Report Issue for Selection" button near your cursor.
You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.