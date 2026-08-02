> Source: https://proceedings.neurips.cc/paper_files/paper/2024/file/170dc3e41f2d03e327e04dbab0fccbfb-Paper-Conference.pdf

Distributionally Robust Reinforcement Learning with Interactive Data Collection: Fundamental Hardness 
and Near-Optimal Algorithms 
Miao Lu1∗ Han Zhong2∗ Tong Zhang3 Jose Blanchet1 
1Department of Management Science and Engineering, Stanford University 2Center for Data Science, Peking University 
3Department of Computer Science, University of Illinois Urbana-Champaign 
Abstract 
Distributionally robust reinforcement learning (DRRL), often framed as a robust Markov decision process (RMDP), seeks to find a robust policy that achieves good performance under the worst-case scenario among all environments within a prespecified uncertainty set centered around the training environment. Unlike previous work, which relies on a generative model or a pre-collected offline dataset enjoying good coverage of the deployment environment, we tackle robust RL via interactive data collection, where the learner interacts with the training environment only and refines the policy through trial and error. In this robust RL paradigm, two main challenges emerge: managing the distributional robustness while striking a balance between exploration and exploitation during data collection. Initially, we establish that sample-efficient learning without additional assumptions is unattainable owing to the curse of support shift; i.e., the potential disjointedness of the distributional supports between training and testing environments. To circumvent such a hardness result, we introduce the vanishing minimal value assumption to RMDPs with a total-variation distance robust set, postulating that the minimal value of the optimal robust value function is zero. Such an assumption effectively eliminates the support shift issue for RMDPs with a TV distance robust set, and we present an algorithm with a provable sample complexity guarantee. Our work makes the initial step to uncovering the inherent difficulty of robust RL via interactive data collection and sufficient conditions for sample-efficient algorithms with sharp sample complexity. 
1 Introduction 
Reinforcement learning (RL) serves as a framework for addressing complex decision-making problems through iterative interactions with environments. The advancements in deep reinforcement learning have enabled the successful application of the general RL framework across various domains, including mastering strategic games, such as Go (Silver et al., 2017), robotics (Kober et al., 2013), and tuning large language models (LLMs; Ouyang et al. (2022)). The critical factors contributing to these successes encompass not only the potency of deep neural networks and modern deep RL algorithms but also the availability of substantial training data. However, there are scenarios, such as healthcare (Wang et al., 2018) and autonomous driving (Kiran et al., 2021), among others, where collecting data in the target domain is challenging, costly, or even unfeasible. 
In such cases, the sim-to-real transfer (Kober et al., 2013; Sadeghi and Levine, 2016; Peng et al., 2018; Zhao et al., 2020) becomes a remedy – a process in which the RL agents are trained in some simulated environment and subsequently deployed in real-world settings. Nevertheless, the training 
∗Equal contribution. Email to miaolu@stanford.edu, hanzhong@stu.pku.edu.cn 
38th Conference on Neural Information Processing Systems (NeurIPS 2024).
environment may differ from the real-world environment. Such a discrepancy, also known as the sim-to-real gap, will typically result in suboptimal performance of RL agents in real-world applications. One promising strategy to control the impact in performance degradation due to the sim-to-real gap is robust RL (Iyengar, 2005; Pinto et al., 2017; Hu et al., 2022), which aims to learn policies exhibiting strong (i.e. robust) performance under environmental deviations from the training environment, effectively hedging the epistemological uncertainty arising from the differences between the training environment and the unknown testing environments. 
A robust RL problem is often formulated within a robust Markov decision process (RMDP) framework, with various types of robust sets characterizing different environmental perturbations. In this robust RL context, prior works have developed algorithms with provable sample complexity guarantees. However, these algorithms typically rely on either a generative model (Yang et al., 2022; Panaganti and Kalathil, 2022; Xu et al., 2023; Shi et al., 2023) or offline data with good coverage of deployment environments (Zhou et al., 2021b; Panaganti et al., 2022; Shi and Chi, 2022; Ma et al., 2022; Blanchet et al., 2023). Notably, the current literature does not explicitly address the exploration problem, which stands as one of the fundamental challenges in reinforcement learning through trial-and-error (Sutton and Barto, 2018). Meanwhile, the empirical success of robust RL methods (Pinto et al., 2017; Kuang et al., 2022; Moos et al., 2022) typically relies on reinforcement learning through interactive data collection in the training environment, where the agent iteratively and actively interacts with the environment, collecting data, optimizing and robustifying its policy. Given that all the existing literature on robust RL theory relies on a generative model or pre-collected data, it is natural to ask: 
Can we design a provably sample-efficient robust RL algorithm that relies on interactive data collection in the training environment? 
Answering the above question faces a fundamental challenge, namely, that during the interactive data collection process, the learner no longer has the oracle control over the training data distributions that are induced by the policy learned through the interaction process. In particular, it could be the case that certain data patterns that are crucial for the policy to be robust across all testing environments are not accessible through interactive data collection, even through a sophisticated design of an exploration mechanism during the interaction process. For example, specific states may not be accessible within the training environment dynamics but could be reached in the testing environment dynamics. 
In contrast, previous work has demonstrated that robust RL through a generative model or a precollected offline dataset with good coverage does not face such difficulty. In the generative model setup, fortunately, the learner can directly query any state-action pair and obtain the sampled next state from the generator. Intuitively, once the states that could appear in the testing environment trajectory are queried enough times, it is possible to guarantee the performance of the learned policy in testing environments. The situation is similar if one has a pre-collected offline dataset that possesses good coverage of the testing environment. This motivates us to take the initial steps towards answering the above questions regarding robust RL with interactive data collection. 
1.1 Contributions 
In this work, we study robust RL in a finite-horizon RMDP with an S ×A-rectangular total-variation distance (TV) robust set (see Assumption 2.1 and Definition 2.4) through interactive data collection. We give both a fundamental hardness result in the general case and a sample-efficient algorithm within tractable settings. More specifically, our contributions are three folds. 
Fundamental hardness. We construct a class of hard-to-learn RMDPs (see Example 3.1) and demonstrate that any learning algorithm inevitably incurs an Ω(ρ ·HK)-online regret (Theorem 3.2) under at least one RMDP instance. Here, ρ signifies the radius of the TV robust uncertainty set, H is the horizon, and K is the number of interactive episodes. This linear regret lower bound underscores the impossibility of sample-efficient robust RL via interactive data collection in general. 
Identifying a tractable case. Upon close examination of the challenging instance, we recognize that the primary obstacle to achieving sample-efficient learning lies in the curse of support shift, i.e., the disjointedness of distributional support between the training environment and the testing environments. In a broader sense, the curse of support shift also refers to the situation when the states appearing in testing environments are extremely hard to arrive in the training environment. 
2
Table 1: Comparison between OPROVI-TV and prior results on RMDP with S ×A-rectangular TV robust sets under various settings (generative model/offline dataset/interactive data collection). For the infinite horizon γ-discounted RMDPs, we denote Hγ := (1− γ)−1 as the effective horizon length. In the offline setting, C⋆ 
rob 
and Cfull represent the robust partial coverage coefficient and full coverage coefficient, respectively. In the general case, our lower bound reads intractable, meaning that there exist hard instances where it is impossible to learn the nearly optimal robust policy via a finite number of interactive samples. 
Model Assump. Algorithm Data oracle Sample complexity ρ ∈ [0, 1) 
general case 
RPVL (Xu et al., 2023) generative model Õ ( 
H5SA ε2 
) DRVI (Shi et al., 2023) generative model Õ 
( min{Hγ ,ρ 
−1}H2 γSA 
ε2 
) lower bound (Shi et al., 2023) generative model Ω 
( min{Hγ ,ρ 
−1}H2 γSA 
ε2 
) P2MPO (Blanchet et al., 2023) offline dataset Õ 
( C⋆ robH 
4S2A ε2 
) lower bound (this work) interactive data collection intractable 
“fail-state” assumption RFQI (Panaganti et al., 2022) offline dataset Õ 
( CfullH 
4 γSA 
ρ2ε2 
) vanishing 
minimal value (Assumption 4.1) 
OPROVI-TV (this work) interactive data collection Õ ( 
min{H,ρ−1}H2SA ε2 
) To rule out these pathological instances, we propose the vanishing minimal value assumption (As-sumption 4.1), positing that the optimal robust value function reaches zero at a specific state. Such an assumption naturally applies to the sparse reward RL paradigm and offers a broader scope compared to the “fail-state” assumption utilized in prior studies on offline RMDP with function approximation (Panaganti et al., 2022). For a comprehensive discussion on this comparison, please see Remark B.3. On the theoretical front, we establish that the vanishing minimal value assumption effectively mitigates the support shift issues between the training and the testing environments (Proposition 4.2), rendering robust RL with interactive data collection feasible for RMDPs with TV robust sets. 
Efficient algorithm with sharp sample complexity. Under the vanishing minimal value assumption, we develop an algorithm named OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV, Algorithm 1), that is capable of finding an ε-optimal robust policy with a total number of 
Õ ( min{H, ρ−1} ·H2SA/ε2 
) (1.1) 
interactive samples (Theorem 4.3). Here S andA denote the number of states and actions, ρ represents the radius of the TV robust set, and H is the horizon length of each episode. To our best knowledge, this is the first provably sample-efficient algorithm for robust RL with interactive data collection. 
According to (1.1), the sample complexity of finding an ε-optimal robust policy decreases as the radius ρ of the robust set increases. When the radius ρ = 0, an RMDP reduces to a standard MDP, and the sample complexity (1.1) recovers the minimax-optimal sample complexity for online RL in standard MDPs up to logarithm factors, i.e., Õ(H3SA/ε2). 
In the end, we further extend our algorithm and theory to a new type of RMDPs, S ×A-rectangular discounted RMDP equipped with robust sets consisting of transition probabilities with bounded ratio to the nominal kernel (See Appendix B.4.2). This newly identified class of RMDPs naturally does not suffer from the support shift issue. It is equivalent to the S × A-rectangular RMDP with TV robust set and vanishing minimal value assumption in an appropriate sense due to Proposition 4.2. Consequently, by a clever usage of Algorithm 1, we can also solve this new model sample-efficiently, as shown in Corollary B.5. Such a result echoes our intuition on the curse of support shift. 
Comparison to related works. Due to the space limit, we only compare with the most related works through Table 1. A detailed discussion of related works is in Appendix A. 
2 Preliminaries 
Notations. For a set X , we denote ∆(X ) as the set of probability distributions on X . For a distribution p ∈ ∆(X ), we define the shorthand for expectation and variance as Ep(·)[f ] := EX∼p(·)[f(X)] and Vp(·)[f ] = Ep(·)[f 
2] − (Ep(·)[f ]) 2. Given any set Q ⊆ ∆(X ), we define the robust expectation 
3
operator as EQ[f ] := infp(·)∈Q EX∼p(·)[f(X)]. For any x, a ∈ R, we denote (x)+ = max{x, 0} and x ∨ a = max{x, a}. We use O(·) to hide absolute constant factors and use Õ to further hide logarithmic factors. For a positive integer H ∈ N+, we denote the set {1, 2, . . . ,H} by [H]. 
2.1 Robust Markov Decision Processes 
We first introduce our underlying model for doing robust RL, the episodic robust Markov decision process (RMDP), denoted by a tuple (S,A, H, P ⋆, R,Φ). Here the set S is the state space and the set A is the action space, both with finite cardinality. The integer H is the length of each episode. The set P ⋆ = {P ⋆ 
h}Hh=1 is the collection of nominal transition kernels where P ⋆ h : S ×A 7→ ∆(S). The 
set R = {Rh}Hh=1 is the collection of reward functions where Rh : S ×A 7→ [0, 1]. For simplicity, we denote P = {P (·|·, ·) : S ×A 7→ ∆(S)} as the space of all possible transition kernels, and we denote S = |S| and A = |A|. Most importantly and different from standard MDPs, the RMDP is equipped with a mapping Φ : P 7→ 2P that characterizes the robust set of any transition kernel in P . Formally, for any transition kernel P ∈ P , we call Φ(P ) the robust set of P . One could interpret the nominal transition kernel P ⋆ 
h as the transition of the training environment, while Φ(P ⋆ h ) contains all 
possible transitions of the testing environments. 
Given an RMDP (S,A, H, P ⋆, R,Φ), we consider using a Markovian policy to make decisions. A Markovian decision policy (or simply, policy) is defined as π = {πh}Hh=1 with πh : S 7→ ∆(A) for each step h ∈ [H]. To measure the performance of a policy π in the RMDP, we introduce its robust value function, defined as for any (s, a) ∈ S ×A, 
V π h,P⋆,Φ(s) := inf 
P̃h∈Φ(P⋆ h ),1≤h≤H 
E{P̃h}H h=1,{πh}H 
h=1 
[ H∑ i=h 
Ri(si, ai) 
∣∣∣∣∣ sh = s 
] , 
Qπ h,P⋆,Φ(s, a) := inf 
P̃h∈Φ(P⋆ h ),1≤h≤H 
E{P̃h}H h=1,{πh}H 
h=1 
[ H∑ i=h 
Ri(si, ai) 
∣∣∣∣∣ sh = s, ah = a 
] . 
Here the expectation is taken w.r.t. the state-action trajectories induced by policy π under the transition P̃ . One can also extend the definition of the robust value functions in terms of any collection of transition kernel P = {Ph}Hh=1 ⊂ P as V π 
h,P,Φ and Qπ h,P,Φ, which we usually use in the sequel. 
Among all the policies, we define the optimal robust policy π⋆ as the policy that can maximize the robust value function at the initial time step h = 1, i.e., 
π⋆ ∈ argmax π={πh}H 
h=1 
V π 1,P⋆,Φ(s1), ∀s1 ∈ S. (2.1) 
In other words, the optimal robust policy π⋆ maximizes the worst case expected total rewards in all possible testing environments. For simplicity and without loss of generality, we assume in the sequel that the initial state s1 ∈ S is fixed. Our results could be directly generalized to s1 ∼ p0(·) ∈ ∆(S). Similarly, we can also define the optimal robust policy associated with a given stochastic process defined through any collection of transition kernels P = {Ph}Hh=1 ⊂ P in the same way as (2.1). We denote the optimal robust value functions associated with P as V ⋆ 
h,P,Φ and Q⋆ h,P,Φ respectively. 
S × A-rectangularity and robust Bellman equations. We consider robust sets Φ that have the S × A-rectangular structure (Iyengar, 2005). which requires that the robust set is decoupled and independent across different (s, a)-pairs. This kind of structure results in a dynamic programming representation of the robust value functions (efficient planning), and is thus commonly adopted in the literature of distributionally robust RL. More specifically, we assume the following. 
Assumption 2.1 (S ×A-rectangularity). We assume that the mapping Φ satisfies for any transition kernel P ∈ P , the robust set Φ(P ) is in the form of 
Φ(P ) = ⊗ 
(s,a)∈S×A 
P(s, a;P ), where P(s, a;P ) ⊆ ∆(S). 
Under above Assumption 2.1, we have the so-called robust Bellman equation (Iyengar, 2005; Blanchet et al., 2023) which gives a dynamic programming representation of robust value functions. 
4
Proposition 2.2 (Robust Bellman equation). Under Assumption 2.1, for any transition P = {Ph}Hh=1 ⊆ P and any policy π = {πh}Hh=1 with πh : S 7→ ∆(A), it holds that 
V π h,P,Φ(s) = Eπh(·|s) 
[ Qπ 
h,P,Φ(s, ·) ] , Qπ 
h,P,Φ(s, a) = Rh(s, a) + EP(s,a;Ph) 
[ V π h+1,P,Φ 
] . 
Regarding the robust value functions of the optimal robust policy, we also have the following dynamic programming solution which plays a key role in our algorithm design and theoretical analysis. 
Proposition 2.3 (Robust Bellman optimal equation). Under Assumption 2.1, for any P = {Ph}Hh=1 ⊆ P , the robust value functions of any optimal robust policy of P satisfies that, 
V ⋆ h,P,Φ(s) = max 
a∈A Q⋆ 
h,P,Φ(s, a), Q⋆ h,P,Φ(s, a) = Rh(s, a) + EP(s,a;Ph) 
[ V ⋆ h+1,P,Φ 
] . 
Taking π⋆ h(·|s) = argmaxa∈AQ 
⋆ h,P,Φ(s, a), then π⋆ = {π⋆ 
h}Hh=1 is optimal robust policy under P . 
Total-variation distance robust set. In Assumption 2.1, the robust set P(s, a;P ) is often modeled as a “distribution ball” centered at P (·|s, a). In this paper, we mainly consider this type of robust sets specified by a total-variation distance ball. We put it in the following definition. 
Definition 2.4 (Total-variation distance robust set). Total-variation distance robust set is defined as 
Pρ(s, a;P ) := { P̃ (·) ∈ ∆(S) : DTV 
( P̃ (·) 
∥∥P (·|s, a)) ≤ ρ } , 
for some ρ ∈ [0, 1), where DTV(·∥·) denotes the total variation distance defined as 
DTV 
( p(·)∥q(·) 
) := 
1 
2 
∑ s∈S 
∣∣p(s)− q(s) ∣∣, ∀p(·), q(·) ∈ ∆(S). (2.2) 
The TV robust set has recently been extensively studied by Yang et al. (2022); Panaganti and Kalathil (2022); Panaganti et al. (2022); Xu et al. (2023); Blanchet et al. (2023); Shi et al. (2023), which all focus on robust RL with a generative model or with a pre-collected offline dataset. More importantly, we emphasize that by (2.2) in Definition 2.4, we do not define the TV distance through the notion of f -divergence which requires that the distribution p is absolute continuous w.r.t. q, as is generally adopted by the above previous works on learning RMDPs with TV robust sets. According to (2.2), we allow p to have a different support than q. That is, there might exist an s ∈ S such that p(s) > 0 and q(s) = 0. Given that, the TV robust set in Definition 2.4 could contain transition probabilities that have different supports than the nominal transition probability P ⋆(·|s, a). An essential property of the TV robust set is that the robust expectation involved in the robust Bellman equations (Propositions 2.2 and 2.3) has a duality representation that only uses the expectation under the nominal transition kernel, as is shown in the following theorem and proved in Appendix C.1. 
Proposition 2.5 (Strong duality representation). Under Definition 2.4, the following duality representation for the robust expectation holds, for any V : S 7→ [0, H] and Ph : S ×A 7→ ∆(S), 
EPρ(s,a;Ph) 
[ V ] = sup 
η∈[0,H] 
{ − EPh(·|s,a) 
[ (η − f)+ 
] − ρ 
2 · ( η −min 
s∈S V (s) 
) + + η } . (2.3) 
Value gap between maximum and minimum. Finally, another useful property of the robust value functions of an RMDP with TV robust sets is a fine characterization of the gap between the maximum and the minimum of the robust value function, which is first identified and utilized by Shi et al. (2023) for an infinite horizon RMDP with TV robust sets. In this work, we prove and use a similar result for the finite horizon case, concluded in the following proposition. The proof is in Appendix C.2. 
Proposition 2.6 (Gap between maximum and minimum). Under Assumption 2.1 with the robust set specified by Definition 2.4, the robust value functions satisfies that 
max (s,a)∈S×A 
Qπ h,P,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P,Φ(s, a) ≤ min { H, ρ−1 
} , 
max s∈S 
V π h,P,Φ(s)−min 
s∈S V π h,P,Φ(s) ≤ min 
{ H, ρ−1 
} , 
for any transition P = {Ph}Hh=1 ⊂ P , any policy π, and any step h ∈ [H]. 
5
2.2 Robust RL with Interactive Data Collection 
We study how to learn the optimal robust policy π⋆ in (2.1) from interactive data collection. Specifi-cally, the learner is required to interact with only the training environment, i.e., P ⋆, for some K ∈ N episodes. In each episode k, the learner adopts a policy πk to interact with the training environment P ⋆ and to collect data. When the k-th episode ends, the learner updates its policy to πk+1 based on historical data and proceeds to the subsequent (k + 1)-th episode. The process ends after K episodes. 
Sample complexity. We use the notion of sample complexity as the key evaluation metric. For any given algorithm and predetermined accuracy level ε > 0, the sample complexity is the minimum number of episodes K required for the algorithm to output an ε-optimal robust policy π̂ satisfying V ⋆ 1,P⋆,Φ(s1) − V π̂ 
1,P⋆,Φ(s1) ≤ ε. The goal is to design algorithms whose sample complexity has small or even optimal dependence on the problem parameters S,A,H, ρ, and 1/ε. 
Online regret. Another evaluation metric that is related to the minimization of sample complexity is the online regret, which is the cumulative difference between the optimal robust policy π⋆ and the executed policies {πk}Kk=1. Formally, we define RegretΦ(K) := 
∑K k=1 V 
⋆ 1,P⋆,Φ(s1)−V πk 
1,P⋆,Φ(s1). The goal is to design algorithms that can achieve a sublinear-in-K regret with small dependence on S,A,H, ρ. It turns out that any sublinear-regret algorithm can be easily converted to a polynomialsample complexity algorithm by applying the standard online-to-batch conversion (Jin et al., 2018). 
3 A Hardness Result: The Curse of Support Shift 
Unfortunately, we show in this section that in general such a problem of robust RL with online data collection is impossible – there exists a simple class of two RMDPs such that an Ω(K)-online regret lower bound exists. However, previous works on robust RL with a generative model or offline data with good coverage do provide sample-efficient ways to find the optimal robust policy for this class of RMDPs. This is a separation between robust RL with interactive data collection and generative model/offline data. Please see also Figure 1 for an illustration of the example. 
Example 3.1 (Hard example of robust RL with interactive data collection). Consider two RMDPs M0 
and M1 which only differ in their nominal transition kernels. The state space is S = {sgood, sbad}, and the action space is A = {0, 1}. The horizon length H = 3. The reward function R always is 1 at the good state sgood and is 0 at the bad state sbad, i.e., 
Rh(s, a) = 
{ 1, s = sgood 0, s = sbad 
, ∀(a, h) ∈ A× [H]. 
For the good state sgood, the next state is always sgood. For the bad state sbad, there is a chance to get to the good state sgood, with the transition probability depending on the action it takes. Formally, 
P ⋆,Mθ 
h (sgood|sgood, a) = 1, ∀(a, h) ∈ A× {1, 2}, ∀θ ∈ {0, 1}, 
P ⋆,Mθ 
2 (sgood|sbad, a) = { p, a = θ 
q, a = 1− θ , ∀θ ∈ {0, 1}, 
where p, q are two constants satisfying 0 < q < p < 1. Intuitively, when at the bad state, the optimal action would result in a higher transition probability p to the good state than the transition probability q induced by the other action. Finally, we consider the robust set being specified by a total-variation distance ball centered at the nominal transition kernel, that is, for any P , 
Φ(P ) = ⊗ 
(s,a)∈S×A 
Pρ(s, a;P ), Pρ(s, a;P ) = { P̃ (·) ∈ ∆(S) : DTV 
( P̃ (·) 
∥∥P (·|s, a)) ≤ ρ } , (3.1) 
where ρ ∈ [0, q] is the parameter characterizing the size of the robust set. We set s1 = sgood. 
For this class of RMDPs, we have the following hardness result for doing robust RL with interactive data collection, an Ω(ρ ·K)-online regret lower bound. The proof is in Appendix D.1. 
Theorem 3.2 (Hardness result (based on Example 3.1)). There exists two RMDPs {M0,M1}, the following regret lower bound holds, 
6
sgood sgood sgood 
sbad sbad 
R1 = 1 R2 = 1 R3 = 1 
R2 = 0 R3 = 0 
Figure 1: Illustration of the hard example in Example 3.1. The solid lines represent possible transitions of the nominal transition kernel. The dashed lines represent the transitions induced by the worst case transition kernel in the robust set. The red solid line represents the transition where the two RMDP instances differ in that different actions lead to higher transition probability from sbad to sgood. We notice that when starting from s1 = sgood, the nominal transition kernel keeps the agent at sgood and no information at sbad is revealed. 
inf ALG 
sup θ∈{0,1} 
E [ RegretMθ,ALG 
Φ (K) ] ≥ Ω 
( ρ ·HK 
) , 
where RegretMθ,ALG Φ (K) refers to the online regret of algorithm ALG for RMDP Mθ. 
The reason why any algorithm fails for this class of RMDPs is the support shift of the worst-case transition kernel. In robust RL, the performance of a policy π is evaluated via the robust expected total rewards, or equivalently, the expected return under the most adversarial transition kernel P †,π. In such an example, as we explicitly show in the proof, when in the good state sgood, the worst-case transition kernel P †,π would transit the state to sbad with a constant probability ρ > 0. But the state sbad is out of the scope of the data collection process because starting from s1 = sgood the nominal transition kernel always transits the state to sgood. As a result, the performance of the learned policy at the bad state sbad is not guaranteed, and inevitably incurs an Ω(ρ ·K)-lower bound of regret, a hardness result. Furthermore, by strategically constructing RMDPs with the horizon 3H based on Example 3.1, we can derive a lower bound of Ω(ρ ·HK). See Appendix B.3 for more discussions. 
4 A Solvable Case, Efficient Algorithm, and Sharp Analysis Motivated by the hard instance (Example 3.1), we now investigate a special subclass of RMDPs with S ×A-rectangular total variation robust set that we show allows for doing sample-efficient robust RL through interactive data collection. In Section 4.1, we introduce the assumption we impose on the RMDP. We propose our algorithm design in Section 4.2, with theoretical analysis in Section 4.3. 
4.1 Vanishing Minimal Value: Eliminating Support Shift 
To overcome the difficulty of support shift identified in Section 3, we make the following vanishing minimal value assumption on the underlying RMDP. 
Assumption 4.1 (Vanishing minimal value). We assume that the underlying RMDP satisfies that mins∈S V 
⋆ 1,P⋆,Φ(s) = 0. Also, WLOG, we assume that the initial state s1 /∈ argmins∈S V 
⋆ 1,P⋆,Φ(s). 
Assumption 4.1 imposes that the minimal robust expected total rewards over all possible initial states is 0. Assuming that the initial state s1 /∈ argmins∈S V 
⋆ 1,P⋆,Φ(s) avoids making the problem trivial. 
A close look at Assumption 4.1 actually gives that the minimal robust value function of any policy π at any step is zero, that is, mins∈S V 
π h,P⋆,Φ(s) = 0 for any policy π and any step h ∈ [H]. With this 
observation, the following proposition explains why this assumption helps to overcome the difficulty, with the proof of the proposition in Appendix C.3. 
Proposition 4.2 (Equivalent expression of TV robust set with vanishing minimal value). For any function V : S 7→ [0, H] with mins∈S V (s) = 0, we have that 
EPρ(s,a;P⋆ h ) [V ] = ρ′ · EBρ′ (s,a;P 
⋆ h )[V ], with ρ′ = 1− ρ 
2 > 0, 
where the TV robust set Pρ(s, a;P ⋆ h ) is defined in (3.1) and the set Bρ′(s, a;P ⋆ 
h ) is defined as2 
Bρ′(s, a;P ⋆ h ) = 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} . 
2Here we implicitly define 0 0 = 0 and a 
0 = ∞ for any a > 0. 
7
Algorithm 1 OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV) 
1: Initialize: dataset D = ∅. 2: for episode k = 1, · · · ,K do 3: Training environment transition estimation: 4: Update the count functions Nk 
h (s, a, s ′) and Nk 
h (s, a) based on D. 5: Calculate the transition kernel estimator P̂ k 
h as Nk h (s, a, s 
′)/(Nk h (s, a) ∨ 1). 
6: Optimistic robust planning: 7: Set V 
k 
H+1 = V k H+1 = 0. 
8: for step h = H, · · · , 1 do 9: Set Q 
k 
h(·, ·) and Qk 
h (·, ·) as (4.2) and (4.3), with bonuskh(·, ·) defined in (4.5). 
10: Set πk h(·|·) = argmaxa∈A Q 
k 
h(·, a), V k 
h(·) = Eπk h(·|·) 
[Q k 
h(·, ·)], and V k h(·) = 
Eπk h(·|·) 
[Qk 
h (·, ·)]. 
11: end for 12: Execute the policy in training environment and collect data: 13: Receive the initial state sk1 ∈ S. 14: for step h = 1, · · · , H do 15: Take action akh ∼ πk 
h(·|skh), observe reward Rh(s k h, a 
k h) and the next state skh+1. 
16: end for 17: Set D as D ∪ {(skh, akh, skh+1)}Hh=1. 18: end for 19: Output: Randomly (uniformly) return a policy from {πk}Kk=1. 
As Proposition 4.2 indicates, under Assumption 4.1, the robust Bellman equations (Propositions 2.2 and 2.3) at step h ∈ [H] is equivalent to taking an infimum over another robust set Bρ′(s, a;P ⋆ 
h ) that shares the same support as the nominal transition kernel P ⋆(·|s, a), discounted by a constant ρ′ < 1. Intuitively, this new robust set rules out the difficulty originated in unseen states in training environments and the discount factor ρ′ hedges the difficulty from prohibitively small probability of reaching certain states that may appear often in the testing environments. This renders robust RL with interactive data collection possible. See Appendix B.4.1 for discussions/examples of Assumption 4.1. 
4.2 Algorithm Design: OPROVI-TV 
In this section, we propose our algorithm that solves robust RL with interactive data collection for RMDPs with S × A-rectangular total-variation (TV) robust sets (Assumption 2.1 and Defini-tion 2.4) and satisfying the vanishing minimal value assumption (Assumption 4.1). Our algorithm, OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV, Algorithm 1), can automatically balance exploitation and exploration during the interactive data collecting process while managing the distributional robustness of the learned policy. The full algorithm OPROVI-TV is given in Algorithm 1. 
Step I: Training Environment Transition Estimation (Line 3 to 5). At the beginning of each episode k ∈ [K], we maintain an estimate of the transition kernel P ⋆ of the training environment by using the historical data D = {(sτh, aτh, sτh+1)} 
k−1,H τ=1,h=1 collected from the interactiion with 
the training environment. Specifically, we simply adopt a vanilla empirical estimator, defined as P̂ k 
h (s ′|s, a) = Nk 
h (s, a, s ′)/(Nk 
h (s, a) ∨ 1) for any (s, a, h, s′) ∈ S × A × S × [H], where the count functions Nk 
h (s, a, s ′) and Nk 
h (s, a) are calculated based on the current dataset D by Nk 
h (s, a, s ′) = 
∑k−1 τ=1 1 
{ (sτh, a 
τ h, s 
τ h+1) = (s, a, s′) 
} and Nk 
h (s, a) = ∑ 
s′∈S N k h (s, a, s 
′) for any (s, a, h, s′) ∈ S ×A×S × [H]. This just coincides with the transition estimator adopted by existing non-robust online RL algorithms (Auer et al., 2008; Azar et al., 2017; Zhang et al., 2021). 
Step II: Optimistic Robust Planning (Line 6 to 11). Given P̂ k(·|·, ·) that estimates the training environment, we perform an optimistic robust planning to construct the policy πk to execute. Basically, the optimistic robust planning follows the robust Bellman optimal equation (Proposition 2.3) to approximate the optimal robust policy, but differs in that it maintains an upper bound and a lower bound of the optimal robust value function and chooses the policy that maximizes the optimistic 
8
estimate to incentivize exploration during data collection. Here the purpose of maintaining the lower bound estimate is to facilitate the construction of the variance-aware optimistic bonus (see following), which helps to sharpen our theoretical analysis. 
▷ Simplifying the robust expectation. To utilize the vanishing minimal value condition (Assump-tion 4.1), we take a closer look into the robust Bellman equation. By strong duality (Proposition 2.5), the robust expectation EPρ(s,a;P )[V ] for any V ∈ [0, H] satisfying mins∈S V (s) = 0 is equivalent to 
EPρ(s,a;P ) 
[ V ] = sup 
η∈[0,H] 
{ − EP (·|s,a) 
[( η − V 
) + 
] + ( 1− ρ 
2 
) · η } . (4.1) 
Consequently, with a slight abuse of the notation, in the remaining of the paper, we re-define the operator EPρ(s,a;P )[V ] as the right hand side of (4.1). Due to Assumption 4.1, the robust Bellman (optimal) equation (Proposition 2.2 and Proposition 2.3) still holds under this new definition. 
▷ Optimistic robust planning. With this in mind, the optimistic robust planning goes as follows. Starting from V 
k 
H+1 = V k H+1 = 0, we recursively define that for any (s, a) ∈ S ×A, 
Q k 
h(s, a) = min { Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a),min 
{ H, ρ−1 
}} , (4.2) 
Qk 
h (s, a) = max 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − bonuskh(s, a), 0 
} , (4.3) 
where the robust expectation EPρ(s,a;P̂k h ) follows the definition in the right hand side of (4.1), and the 
bonus function bonuskh(s, a) ≥ 0 is defined later. Here we truncate the optimistic estimateQ k 
h via the upper bound min{H, ρ−1} of the true optimal robust value function Q⋆ 
h,P⋆,Φ. This truncation arises from the combined implication of Proposition 2.6 and the fact that min(s,a)∈S×AQ 
⋆ h,P⋆,Φ(s, a) = 0 
under Assumption 4.1. As we establish in Lemma E.2, Q k 
h and Qk 
h form upper and lower bounds 
for Q⋆ h,P⋆,Φ and Qπk 
h,P⋆,Φ under a proper choice of the bonus. After performing (4.2) and (4.3), we choose the data collection policy πk 
h to be the optimal policy with respect to the optimistic estimator Q 
k 
h and define V k 
h and V k h accordingly by 
πk h(·|·) = argmax 
a∈A Q 
k 
h(·, a), V k 
h(s) = Eπk h(·|s) 
[ Q 
k 
h(s, ·) ] , V k 
h(s) = Eπk h(·|s) 
[ Qk 
h (s, ·) 
] . (4.4) 
We remark that the purpose of maintaining the lower bound estimate (4.3) is to facilitate the construction of the bonus and to help sharpen our theoretical analysis. The construction of the policy πk is still based on the optimistic estimator, which is why we call it optimistic robust planning. As indicated by theory, the optimistic robust planning can effectively guide the policy to explore uncertain robust value function estimates, striking a balance between exploration and exploitation while managing distributional robustness. 
▷ Bonus function. The bonus function bonuskh(s, a) is a Bernstein-style bound defined as√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K ,(4.5) 
where ι = log(S3AH2K3/2/δ), c1, c2 > 0 are absolute constants, and δ signifies a pre-selected fail probability. Under (4.5), Q 
k 
h and Qk 
h become upper and lower bounds of the optimal robust value 
functions (Lemma E.2). More importantly, the bonus (4.5) is carefully designed for robust value functions such that the summation of this bonus term (especially the leading variance term in (4.5)) over time steps is well controlled, for which we also develop new analysis methods. This is critical for obtaining a sharp sample complexity of Algorithm 1. 
4.3 Theoretical Guarantees 
This section establishes the online regret and the sample complexity of OPROVI-TV (Algorithm 1). Our main result is the following, upper bounding the online regret of Algorithm 1, proved in Appendix E. 
9
Theorem 4.3 (Online regret of OPROVI-TV). Given an RMDP with S×A-rectangular total-variation robust set of radius ρ ∈ [0, 1) (Assumption 2.1 and Definition 2.4) satisfying Assumptions 4.1, choosing the bonus function as (4.5) with sufficiently large c1, c2 > 0, then with probability at least 1− δ, Algorithm 1 satisfies 
RegretΦ(K) ≤ O (√ 
min { H, ρ−1 
} H2SAKι′ 
) , 
where ι′ = log2(SAHK/δ) and O(·) hides absolute constants and lower order terms in K. 
Theorem 4.3 shows that Algorithm 1 enjoys a sublinear online regret of Õ( √ K), meaning that it is 
able to approximately find the optimal robust policy through interactive data collection. This is in contrast with the general hardness result in Section 3 where sample-efficient learning is impossible in the worst case. Thus we show the effectiveness of the minimal value assumption for robust RL with interactive data collection. As a corollary, we have the following sample complexity bound for Algorithm 1. It is obtained directly from Theorem 4.3 and a standard online to batch conversion. 
Corollary 4.4 (Sample complexity of OPROVI-TV). Under the same setup and conditions as in Theorem 4.3, with probability at least 1− δ, Algorithm 1 can output an ε-optimal policy within 
O ( min 
{ H, ρ−1 
} H2SAι′′/ε2 
) (4.6) 
episodes, where ι′′ = log(SAH/εδ) and O(·) hides absolute constants. The valid range of ε satisfies ε ∈ (0, c ·min{1, 1/(ρH)}] for some constant c > 0. 
We compare the sample complexity (4.6) with prior arts on non-robust online RL and robust RL with a generative model. On the one hand, (4.6) with ρ = 0 equals to Õ(H3SA/ε2), matching the minimax sample complexity lower bound for online RL in non-robust MDPs (Azar et al., 2017). This means that our algorithm design can naturally handle non-robust MDPs as a special case (please also see Remark B.4 for why one can reduce Algorithm 1 to general non-robust MDPs under Assumption 4.1). On the other hand, the previous work of Shi et al. (2023) for robust RL in infinite horizon RMDPs with a TV robust set and a generative model showcases a minimax optimal sample complexity of 
Õ ( min 
{ Hγ , ρ 
−1 } H2 
γSA/ε 2 ) , 
for ρ ∈ [0, 1), where weHγ := 1/(1−γ) is the effective horizon of the infinite γ-discounted RMDPs. As a result, the sample complexity (4.6) of Algorithm 1 matches their result. We highlight that our algorithm does not rely on a generative model and operates purely through interactive data collection. 
Extensions of Algorithm 1 and its theory. In Appendix B.4.2, we extend Algorithm 1 to solve a new type of RMDPs whose robust set consists of transition probabilities with bounded ratio to the nominal kernel. The intuition is because it is equivalent to the S ×A-rectangular RMDP with a TV robust set and vanishing minimal value assumption in an appropriate sense (Proposition 4.2) Consequently, by a clever usage of Algorithm 1, we can also solve this new model sample-efficiently, as is shown in Corollary B.5. Such a result echoes our intuition on the curse of support shift. 
5 Conclusions and future works 
This work shows that in the absence of any structural assumptions, robust RL via interactive data collection necessarily induces a linear regret lower bound in the worst case due to the curse of support shift. Under the vanishing minimal value assumption, an assumption that is able to effectively rule out the potential support shift issues for RMDPs with a TV robust set, we propose a sample-efficient robust RL algorithm for those RMDPs with sharp analysis. Potential future works include extending to function approximation settings and other types of robust sets. See discussion in Appendix B.5. 
Acknowledgments and Disclosure of Funding 
The material in this paper is based upon work supported by the Air Force Office of Scientific Research under award number FA9550-20-1-0397. Additional support is gratefully acknowledged from NSF 1915967, 2118199, 2229012, 2312204. The authors would like to thank the anonymous reviewers for their helpful comments. The authors would also like to thank Pan Xu and Zhishuai Liu for their feedback on an early draft of this work. 
10
References AGARWAL, A., JIANG, N., KAKADE, S. M. and SUN, W. (2019). Reinforcement learning: Theory 
and algorithms. CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep 10–4. 44 
AGARWAL, A., JIN, Y. and ZHANG, T. (2023). Vo q l: Towards optimal regret in model-free rl with nonlinear function approximation. In The Thirty Sixth Annual Conference on Learning Theory. PMLR. 16, 17 
AUER, P., JAKSCH, T. and ORTNER, R. (2008). Near-optimal regret bounds for reinforcement learning. Advances in neural information processing systems 21. 8 
AYOUB, A., JIA, Z., SZEPESVARI, C., WANG, M. and YANG, L. (2020). Model-based reinforcement learning with value-targeted regression. In International Conference on Machine Learning. PMLR. 16 
AZAR, M. G., OSBAND, I. and MUNOS, R. (2017). Minimax regret bounds for reinforcement learning. In International Conference on Machine Learning. PMLR. 8, 10, 16, 41 
BADRINATH, K. P. and KALATHIL, D. (2021). Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In International Conference on Machine Learning. PMLR. 16 
BLANCHET, J., LU, M., ZHANG, T. and ZHONG, H. (2023). Double pessimism is provably efficient for distributionally robust offline reinforcement learning: Generic algorithm and robust partial coverage. arXiv preprint arXiv:2305.09659 . 2, 3, 4, 5, 16, 17, 18, 21, 24 
CLAVIER, P., PENNEC, E. L. and GEIST, M. (2023). Towards minimax optimality of model-based robust reinforcement learning. arXiv preprint arXiv:2302.05372 . 16 
DANN, C., LATTIMORE, T. and BRUNSKILL, E. (2017). Unifying pac and regret: Uniform pac bounds for episodic reinforcement learning. Advances in Neural Information Processing Systems 30. 16 
DING, W., SHI, L., CHI, Y. and ZHAO, D. (2024). Seeing is not believing: Robust reinforcement learning against spurious correlation. Advances in Neural Information Processing Systems 36. 16 
DONG, J., LI, J., WANG, B. and ZHANG, J. (2022). Online policy optimization for robust mdp. arXiv preprint arXiv:2209.13841 . 17 
DU, S., KAKADE, S., LEE, J., LOVETT, S., MAHAJAN, G., SUN, W. and WANG, R. (2021). Bilinear classes: A structural framework for provable generalization in rl. In International Conference on Machine Learning. PMLR. 16 
EL GHAOUI, L. and NILIM, A. (2005). Robust solutions to markov decision problems with uncertain transition matrices. Operations Research 53 780–798. 16 
FOSTER, D. J., KAKADE, S. M., QIAN, J. and RAKHLIN, A. (2021). The statistical complexity of interactive decision making. arXiv preprint arXiv:2112.13487 . 16 
HE, J., ZHAO, H., ZHOU, D. and GU, Q. (2023). Nearly minimax optimal reinforcement learning for linear markov decision processes. In International Conference on Machine Learning. PMLR. 16 
HU, J., ZHONG, H., JIN, C. and WANG, L. (2022). Provable sim-to-real transfer in continuous domain with partial observations. arXiv preprint arXiv:2210.15598 . 2 
HUANG, J., ZHONG, H., WANG, L. and YANG, L. F. (2023a). Horizon-free and instance-dependent regret bounds for reinforcement learning with general function approximation. arXiv preprint arXiv:2312.04464 . 17 
HUANG, J., ZHONG, H., WANG, L. and YANG, L. F. (2023b). Tackling heavy-tailed rewards in reinforcement learning with function approximation: Minimax optimal and instance-dependent regret bounds. arXiv preprint arXiv:2306.06836 . 16 
11
IYENGAR, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research 30 257–280. 2, 4, 16, 17 
JIANG, N., KRISHNAMURTHY, A., AGARWAL, A., LANGFORD, J. and SCHAPIRE, R. E. (2017). Contextual decision processes with low bellman rank are pac-learnable. In International Conference on Machine Learning. PMLR. 16 
JIN, C., ALLEN-ZHU, Z., BUBECK, S. and JORDAN, M. I. (2018). Is q-learning provably efficient? Advances in neural information processing systems 31. 6, 16 
JIN, C., LIU, Q. and MIRYOOSEFI, S. (2021). Bellman eluder dimension: New rich classes of rl problems, and sample-efficient algorithms. Advances in neural information processing systems 34 13406–13418. 16 
JIN, C., YANG, Z., WANG, Z. and JORDAN, M. I. (2020). Provably efficient reinforcement learning with linear function approximation. In Conference on Learning Theory. PMLR. 16 
KIRAN, B. R., SOBH, I., TALPAERT, V., MANNION, P., AL SALLAB, A. A., YOGAMANI, S. and PÉREZ, P. (2021). Deep reinforcement learning for autonomous driving: A survey. IEEE Transactions on Intelligent Transportation Systems 23 4909–4926. 1 
KOBER, J., BAGNELL, J. A. and PETERS, J. (2013). Reinforcement learning in robotics: A survey. The International Journal of Robotics Research 32 1238–1274. 1 
KUANG, Y., LU, M., WANG, J., ZHOU, Q., LI, B. and LI, H. (2022). Learning robust policy against disturbance in transition dynamics via state-conservative policy optimization. In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36. 2, 16 
LI, G., CAI, C., CHEN, Y., WEI, Y. and CHI, Y. (2023). Is q-learning minimax optimal? a tight sample complexity analysis. Operations Research . 16 
LI, Y. and LAN, G. (2023). First-order policy optimization for robust policy evaluation. arXiv preprint arXiv:2307.15890 . 16 
LIU, Z., LU, M., WANG, Z., JORDAN, M. and YANG, Z. (2022). Welfare maximization in competitive equilibrium: Reinforcement learning for markov exchange economy. In International Conference on Machine Learning. PMLR. 17 
LIU, Z., LU, M., XIONG, W., ZHONG, H., HU, H., ZHANG, S., ZHENG, S., YANG, Z. and WANG, Z. (2023). One objective to rule them all: A maximization objective fusing estimation and planning for exploration. arXiv preprint arXiv:2305.18258 . 17 
LIU, Z. and XU, P. (2024a). Distributionally robust off-dynamics reinforcement learning: Provable efficiency with linear function approximation. arXiv preprint arXiv:2402.15399 . 16 
LIU, Z. and XU, P. (2024b). Minimax optimal and computationally efficient algorithms for distributionally robust offline reinforcement learning. arXiv preprint arXiv:2403.09621 . 16 
LYKOURIS, T., SIMCHOWITZ, M., SLIVKINS, A. and SUN, W. (2021). Corruption-robust exploration in episodic reinforcement learning. In Conference on Learning Theory. PMLR. 17 
MA, X., LIANG, Z., XIA, L., ZHANG, J., BLANCHET, J., LIU, M., ZHAO, Q. and ZHOU, Z. (2022). Distributionally robust offline reinforcement learning with linear function approximation. arXiv preprint arXiv:2209.06620 . 2, 16 
MAURER, A. and PONTIL, M. (2009). Empirical bernstein bounds and sample variance penalization. arXiv preprint arXiv:0907.3740 . 29 
MÉNARD, P., DOMINGUES, O. D., SHANG, X. and VALKO, M. (2021). Ucb momentum q-learning: Correcting the bias without forgetting. In International Conference on Machine Learning. PMLR. 16 
MOOS, J., HANSEL, K., ABDULSAMAD, H., STARK, S., CLEVER, D. and PETERS, J. (2022). Robust reinforcement learning: A review of foundations and recent advances. Machine Learning and Knowledge Extraction 4 276–315. 2 
12
OUYANG, L., WU, J., JIANG, X., ALMEIDA, D., WAINWRIGHT, C., MISHKIN, P., ZHANG, C., AGARWAL, S., SLAMA, K., RAY, A. ET AL. (2022). Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems 35 27730– 27744. 1 
PANAGANTI, K. and KALATHIL, D. (2022). Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics. PMLR. 2, 5, 16, 17, 18 
PANAGANTI, K., XU, Z., KALATHIL, D. and GHAVAMZADEH, M. (2022). Robust reinforcement learning using offline data. arXiv preprint arXiv:2208.05129 . 2, 3, 5, 16, 17, 18, 19 
PENG, X. B., ANDRYCHOWICZ, M., ZAREMBA, W. and ABBEEL, P. (2018). Sim-to-real transfer of robotic control with dynamics randomization. In 2018 IEEE international conference on robotics and automation (ICRA). IEEE. 1 
PINTO, L., DAVIDSON, J., SUKTHANKAR, R. and GUPTA, A. (2017). Robust adversarial reinforcement learning. In International Conference on Machine Learning. PMLR. 2 
SADEGHI, F. and LEVINE, S. (2016). Cad2rl: Real single-image flight without a single real image. arXiv preprint arXiv:1611.04201 . 1 
SHI, L. and CHI, Y. (2022). Distributionally robust model-based offline reinforcement learning with near-optimal sample complexity. arXiv preprint arXiv:2208.05767 . 2, 16, 21 
SHI, L., LI, G., WEI, Y., CHEN, Y., GEIST, M. and CHI, Y. (2023). The curious price of distributional robustness in reinforcement learning with a generative model. arXiv preprint arXiv:2305.16589 . 2, 3, 5, 10, 16, 17, 18, 21, 23 
SI, N., ZHANG, F., ZHOU, Z. and BLANCHET, J. (2023). Distributionally robust batch contextual bandits. Management Science . 16 
SILVER, D., SCHRITTWIESER, J., SIMONYAN, K., ANTONOGLOU, I., HUANG, A., GUEZ, A., HUBERT, T., BAKER, L., LAI, M., BOLTON, A. ET AL. (2017). Mastering the game of go without human knowledge. nature 550 354–359. 1 
SUN, W., JIANG, N., KRISHNAMURTHY, A., AGARWAL, A. and LANGFORD, J. (2019). Model-based rl in contextual decision processes: Pac bounds and exponential improvements over model-free approaches. In Conference on learning theory. PMLR. 16 
SUTTON, R. S. and BARTO, A. G. (2018). Reinforcement learning: An introduction. MIT press. 2 
WANG, H., SHI, L. and CHI, Y. (2024). Sample complexity of offline distributionally robust linear markov decision processes. arXiv preprint arXiv:2403.12946 . 16 
WANG, L., ZHANG, W., HE, X. and ZHA, H. (2018). Supervised reinforcement learning with recurrent neural network for dynamic treatment recommendation. In Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining. 1 
WANG, Q., HO, C. P. and PETRIK, M. (2022). On the convergence of policy gradient in robust mdps. arXiv preprint arXiv:2212.10439 . 16 
WANG, Q., HO, C. P. and PETRIK, M. (2023a). Policy gradient in robust MDPs with global convergence guarantee. In Proceedings of the 40th International Conference on Machine Learning (A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato and J. Scarlett, eds.), vol. 202 of Proceedings of Machine Learning Research. PMLR. 16 
WANG, S., SI, N., BLANCHET, J. and ZHOU, Z. (2023b). A finite sample complexity bound for distributionally robust q-learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 16 
WANG, S., SI, N., BLANCHET, J. and ZHOU, Z. (2023c). On the foundation of distributionally robust reinforcement learning. arXiv preprint arXiv:2311.09018 . 16 
13
WANG, S., SI, N., BLANCHET, J. and ZHOU, Z. (2023d). Sample complexity of variance-reduced distributionally robust q-learning. arXiv preprint arXiv:2305.18420 . 16 
WANG, Y. and ZOU, S. (2021). Online robust reinforcement learning with model uncertainty. Advances in Neural Information Processing Systems 34 7193–7206. 16 
WANG, Y. and ZOU, S. (2022). Policy gradient method for robust reinforcement learning. In International Conference on Machine Learning. PMLR. 16 
WEI, C.-Y., DANN, C. and ZIMMERT, J. (2022). A model selection approach for corruption robust reinforcement learning. In International Conference on Algorithmic Learning Theory. PMLR. 17 
WIESEMANN, W., KUHN, D. and RUSTEM, B. (2013). Robust markov decision processes. Mathe-matics of Operations Research 38 153–183. 16 
WU, T., YANG, Y., ZHONG, H., WANG, L., DU, S. and JIAO, J. (2022). Nearly optimal policy optimization with stable at any time guarantee. In International Conference on Machine Learning. PMLR. 16 
XU, H. and MANNOR, S. (2010). Distributionally robust markov decision processes. Advances in Neural Information Processing Systems 23. 16 
XU, Y. and ZEEVI, A. (2023). Bayesian design principles for frequentist sequential learning. In International Conference on Machine Learning. PMLR. 17 
XU, Z., PANAGANTI, K. and KALATHIL, D. (2023). Improved sample complexity bounds for distributionally robust reinforcement learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 2, 3, 5, 16, 17, 18, 21 
YANG, R., ZHONG, H., XU, J., ZHANG, A., ZHANG, C., HAN, L. and ZHANG, T. (2023a). Towards robust offline reinforcement learning under diverse data corruption. arXiv preprint arXiv:2310.12955 . 17 
YANG, W., WANG, H., KOZUNO, T., JORDAN, S. M. and ZHANG, Z. (2023b). Avoiding model estimation in robust markov decision processes with a generative model. arXiv preprint arXiv:2302.01248 . 16 
YANG, W., ZHANG, L. and ZHANG, Z. (2022). Toward theoretical understandings of robust markov decision processes: Sample complexity and asymptotics. The Annals of Statistics 50 3223–3248. 2, 5, 16, 17, 18, 21 
YE, C., HE, J., GU, Q. and ZHANG, T. (2024). Towards robust model-based reinforcement learning against adversarial corruption. arXiv preprint arXiv:2402.08991 . 17 
YE, C., XIONG, W., GU, Q. and ZHANG, T. (2023a). Corruption-robust algorithms with uncertainty weighting for nonlinear contextual bandits and markov decision processes. In International Conference on Machine Learning. PMLR. 17 
YE, C., YANG, R., GU, Q. and ZHANG, T. (2023b). Corruption-robust offline reinforcement learning with general function approximation. arXiv preprint arXiv:2310.14550 . 17 
YU, Z., DAI, L., XU, S., GAO, S. and HO, C. P. (2023). Fast bellman updates for wasserstein distributionally robust mdps. In Thirty-seventh Conference on Neural Information Processing Systems. 16 
ZANETTE, A. and BRUNSKILL, E. (2019). Tighter problem-dependent regret bounds in reinforcement learning without domain knowledge using value function bounds. In International Conference on Machine Learning. PMLR. 16 
ZHANG, X., CHEN, Y., ZHU, X. and SUN, W. (2022). Corruption-robust offline reinforcement learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 17 
ZHANG, Z., CHEN, Y., LEE, J. D. and DU, S. S. (2023). Settling the sample complexity of online reinforcement learning. arXiv preprint arXiv:2307.13586 . 16 
14
ZHANG, Z., JI, X. and DU, S. (2021). Is reinforcement learning more difficult than bandits? a near-optimal algorithm escaping the curse of horizon. In Conference on Learning Theory. PMLR. 8, 16 
ZHANG, Z., ZHOU, Y. and JI, X. (2020). Almost optimal model-free reinforcement learningvia reference-advantage decomposition. Advances in Neural Information Processing Systems 33 15198–15207. 16 
ZHAO, W., QUERALTA, J. P. and WESTERLUND, T. (2020). Sim-to-real transfer in deep reinforcement learning for robotics: a survey. In 2020 IEEE Symposium Series on Computational Intelligence (SSCI). IEEE. 1 
ZHONG, H., XIONG, W., ZHENG, S., WANG, L., WANG, Z., YANG, Z. and ZHANG, T. (2022). Gec: A unified framework for interactive decision making in mdp, pomdp, and beyond. arXiv preprint arXiv:2211.01962 . 17 
ZHONG, H. and ZHANG, T. (2023). A theoretical analysis of optimistic proximal policy optimization in linear markov decision processes. arXiv preprint arXiv:2305.08841 . 16 
ZHOU, D., GU, Q. and SZEPESVARI, C. (2021a). Nearly minimax optimal reinforcement learning for linear mixture markov decision processes. In Conference on Learning Theory. PMLR. 16 
ZHOU, R., LIU, T., CHENG, M., KALATHIL, D., KUMAR, P. and TIAN, C. (2023). Natural actorcritic for robust reinforcement learning with function approximation. In Thirty-seventh Conference on Neural Information Processing Systems. 16 
ZHOU, Z., ZHOU, Z., BAI, Q., QIU, L., BLANCHET, J. and GLYNN, P. (2021b). Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 2, 16 
15
A Related Works 
We give a detailed discussion on the related works in this section. 
Robust reinforcement learning in robust Markov decision processes. Robust RL is usually framed as a robust Markov decision process (RMDP) (Iyengar, 2005; El Ghaoui and Nilim, 2005; Wiesemann et al., 2013). There is a long line of work dedicated to the problem of how to solve for the optimal robust policy of a given RMDP, i.e., planning (Iyengar, 2005; El Ghaoui and Nilim, 2005; Xu and Mannor, 2010; Wang and Zou, 2022; Wang et al., 2022; Kuang et al., 2022; Wang et al., 2023a; Yu et al., 2023; Zhou et al., 2023; Li and Lan, 2023; Wang et al., 2023c; Ding et al., 2024). Recently, the community has also witnessed a growing body of work on sample-efficient robust RL in RMDPs with different data collection oracles, including the generative model setup (Yang et al., 2022; Panaganti and Kalathil, 2022; Si et al., 2023; Wang et al., 2023b; Yang et al., 2023b; Xu et al., 2023; Clavier et al., 2023; Wang et al., 2023d; Shi et al., 2023), offline setting (Zhou et al., 2021b; Panaganti et al., 2022; Shi and Chi, 2022; Ma et al., 2022; Blanchet et al., 2023; Liu and Xu, 2024b; Wang et al., 2024), and interactive data collection setting (Badrinath and Kalathil, 2021; Wang and Zou, 2021; Liu and Xu, 2024a). 
Our work falls into the paradigm of sample-efficient robust RL with interactive data collection. Wang and Zou (2021) and Badrinath and Kalathil (2021) propose efficient online learning algorithms to obtain the optimal robust policy of an infinite horizon RMDP, but none of them handle the challenge of exploration in online RL by assuming the access to explorative policies. This assumption enables the learner to collect high-quality data essential for effective learning and decision-making. In contrast, our work focuses on developing efficient algorithms for the fully online setting, where there is no predefined exploration policy to use. Under this more challenging setting, we address the exploration challenge through algorithmic design rather than relying on assumed access to explorative policies. 
During the preparation of this work, we are aware of several concurrent and independent works (Liu and Xu, 2024a,b; Wang et al., 2024), which study a different type of RMDPs known as d-rectangular linear MDPs (Ma et al., 2022; Blanchet et al., 2023). In particular, Liu and Xu (2024b) and Wang et al. (2024) consider the offline setting, while Liu and Xu (2024a) investigate robust RL through interactive data collection (off-dynamics learning), thus bearing closer relevance to our work. More specifically, under the existence of a “fail-state”, the algorithm in Liu and Xu (2024a) can learn an ε-optimal robust policy with provable sample efficiency. In contrast, our work first explicitly uncovers the fundamental hardness of doing robust RL in RMDPs with a TV distance based robust set and without additional assumptions. To overcome the inherent difficulty, we adopt a vanishing minimal value assumption that strictly generalizes the “fail-state” assumption used in Liu and Xu (2024a). Moreover, our focus is on tabular S ×A-rectangular RMDPs, with customized algorithmic design and theoretical analysis which allow us to obtain a sharp sample complexity bound. 
Finally, in Table 1, we compare the sample complexity of our algorithm with prior work on robust RL for RMDPs with S ×A-rectangular TV robust sets under various settings (generative model/offline dataset). We remark that the works of Panaganti and Kalathil (2022) and Blanchet et al. (2023) are in the paradigm of function approximation, and here we reduce their general sample complexity result to the tabular setup we consider. 
Sample-efficient online non-robust reinforcement learning. Our work is also closely related to online non-robust RL, which is often formulated as a Markov decision process (MDP) with online data collection. For non-robust online RL, the key challenge is the exploration-exploitation tradeoff. There has been a long line of work (Azar et al., 2017; Dann et al., 2017; Jin et al., 2018; Zanette and Brunskill, 2019; Zhang et al., 2020, 2021; Ménard et al., 2021; Wu et al., 2022; Li et al., 2023; Zhang et al., 2023) addressing this challenge in the context of tabular MDPs, where the state space and action space are finite and also relatively small. In particular, many algorithms (e.g., UCBVI in Azar et al. (2017)) have been proven capable of finding an ε-optimal policy within Õ(H3SA/ε2) sample complexity. Notably, a standard MDP corresponds to an RMDP with a TV robust set and ρ = 0, suggesting that OPROVI-TV can naturally achieve nearly minimax-optimality for non-robust RL. Moving beyond the tabular setups, recent works also investigate online non-robust RL with linear function approximation (Jin et al., 2020; Ayoub et al., 2020; Zhou et al., 2021a; Zhong and Zhang, 2023; Huang et al., 2023b; He et al., 2023; Agarwal et al., 2023) and even general function approximations (Jiang et al., 2017; Sun et al., 2019; Du et al., 2021; Jin et al., 2021; Foster et al., 
16
2021; Liu et al., 2022; Zhong et al., 2022; Liu et al., 2023; Huang et al., 2023a; Xu and Zeevi, 2023; Agarwal et al., 2023). 
Corruption robust reinforcement learning. Generally speaking, our research is also related to another form of robust RL, namely corruption robust RL (Lykouris et al., 2021; Wei et al., 2022; Zhang et al., 2022; Ye et al., 2023a,b; Yang et al., 2023a; Ye et al., 2024). This branch of researches on robust RL addresses scenarios where training data is corrupted, presenting a distinct challenge from distributionally robust RL. The latter concerns testing time robustness, where the agent is evaluated in a perturbed environment after being trained on nominal data. These two forms of robust RL, while sharing the overarching goal to enhance agent resilience, operate within different contexts and confront distinct challenges. Thus, a direct comparison between these two types of robust RL is difficult because each addresses unique aspects of resilience. 
B Further Discussions 
This section complements the main part of the paper by further commenting and discussing several aspects of the paper. Due to space limits, these important remarks are provided here. 
B.1 Discussions on Introduction (Section 1) 
About a generative model and a simulator. A generative model here means a mechanism that when queried at some state, action, and time step, returns a sample of next state. Here we distinguish this notion with the notion of simulator or simulated environment which generally refers to a humanmade training environment that mimics the real-world environment. With a generative model on hand, interactive data collection is no longer needed, but in a simulated environment, it is common to train a robust policy through interactive data collection in practice. 
The definition of total-variation robust set. We notice that all of the previous work on sampleefficient robust RL in RMDPs with TV robust sets (Yang et al., 2022; Panaganti and Kalathil, 2022; Panaganti et al., 2022; Xu et al., 2023; Blanchet et al., 2023; Shi et al., 2023) relies on defining the TV distance through the general f -divergence so that a strong duality representation holds. But this implicitly requires the testing environment transition probability is absolute continuous w.r.t. the training environment transition probability. In this paper, we do not make such a restriction. We prove the same strong duality even if the absolute continuity does not hold. In fact, all the previous work can be directly extended to such TV distance definition via our more general strong duality result. 
An existing work. We note that an existing work (Dong et al., 2022) also studies the problem of robust RL with interactive data collection. They study S ×A-rectangular RMDPs with a TV robust set, assuming that the support of the training environment transition is the full state space S. They claim the existence of an algorithm that enjoys a Õ( 
√ K)-online regret. We point out that their proof 
exhibits an essential flaw (misuse of Lemma 12 therein) and therefore the regret they claim is invalid. 
The range of the robust set size ρ. We do not signify the situation when ρ = 1 since in that case the TV robust set contains all possible transition probabilities, making the problem statistically trivial. In that case, no sample is needed. 
B.2 Discussions on Preliminaries (Section 2) 
B.2.1 Robust Markov Decision Processes 
Robust Bellman equations. We remark that the original version of the robust Bellman equation (Iyengar, 2005) is for infinite horizon RMDPs and a customized proof of robust Bellman equation for finite horizon RMDPs (Proposition 2.2) can be found in Appendix A.1 of Blanchet et al. (2023). The robust Bellman optimal equation (Proposition 2.3) is then a corollary or can be proved similarly. 
Strong duality under TV distance robust set. An essential property of the TV robust set is that the robust expectation involved in the robust Bellman equations (Propositions 2.2 and 2.3) has a duality representation that only uses the expectation under the nominal transition kernel. Previous 
17
works, e.g., Yang et al. (2022), have proved such a result when the TV distance is defined through f -divergence. Here we extend such a result to the TV distance defined directly though (2.2) that allows a difference support between p and q. 
Remark B.1. Despite all previous works on RMDPs with TV robust sets relying on the definition of TV distance DTV(p(·)∥q(·)) with absolute continuity of p with respect to q to obtain the strong duality representation in the form of (2.3), their results can be directly extended to TV distance that allows for different support between p and q thanks to Proposition 2.5. 
Value gap between maximum. We note that in the proof of Proposition 2.6, we actually show a tighter form of bound of the gap between the maximum and minimum as 
1 
ρ · ( 1− (1− ρ)H 
) . 
But in the sequel, we mainly use the form of min{H, ρ−1} for its brevity and the fact of (1− (1− ρ)H)/ρ = Θ(min{H, ρ−1}) in the sense that 
c ·min { H, ρ−1 
} ≤ (1− (1− ρ)H)/ρ ≤ min 
{ H, ρ−1 
} for any H ≥ H0 ∈ N+ and ρ ∈ [0, 1] with some constant c > 0 that is independent of (H, ρ). 
In contrast with a crude bound of H , such a fine upper bound decreases when ρ is large, which is essential to understanding the statistical limits of doing robust RL in RMDPs with TV robust sets. 
B.2.2 Robust RL with Interactive Data Collection 
Sample complexity. The metric of sample complexity is connected with the sample complexity used in robust RL with generative models and offline settings (see related works for the references), wherein the sample complexity means the minimum number of generative samples or pre-collected offline data required to achieve ε-optimality. In contrast, here the sample complexity is measuring the least number of interactions with the training environment needed to learn π⋆, where no generative or offline sample is available. Such a learning protocol casts unique challenges on the algorithmic design and theoretical analysis to get the optimal sample complexity. 
B.3 Discussions on Hardness Result: The Curse of Support Shift (Section 3) 
In contrast to the interactive data collection setting we consider, doing robust RL with a generative model or an offline dataset with good coverage properties does not face the difficulty we displayed through Example 3.1. It turns out that any RMDP with S ×A-rectangular total-variation robust set (including Example 3.1) can be solved in a sample-efficient manner therein, see Yang et al. (2022); Panaganti and Kalathil (2022); Panaganti et al. (2022); Xu et al. (2023); Blanchet et al. (2023); Shi et al. (2023) and Remark B.1. The intuitive reason is that, for the generative model setting, the learner can directly query any state-action pair to estimate the nominal transition kernel P ⋆, and thus no support shift happens. The same reason holds for the offline setup with a good-coverage dataset. 
There is a broader understanding of the curse of support shift that hinders the tractability of robust RL via interactive data collection. The concept of support shift could be comprehended within a broader context beyond the disjointness of certain parts of the support sets of the training and testing environments. Instead, ensuring a “high probability of disjointness” is enough to maintain the integrity of the hardness result. For instance, we can modify the state sgood in Example 3.1 so that it is no longer an absorbing state. Rather, sgood could transit to sbad with a small probability, such as 2−H . This modification expands the support of the training environment to encompass the entire state space. Nevertheless, acquiring information about sbad necessitates exponential samples, thereby preserving the hardness result. 
B.4 Discussions on A Solvable Case, Efficient Algorithm, and Sharp Analysis (Section 4) 
B.4.1 Vanishing Minimal Value Assumption 
Another understanding of Assumption 4.1. To understand this from another perspective, it could be shown that under the conclusions of Proposition 4.2, the robust value function of any 
18
policy π is equivalent to the robust value function of this policy under another discounted RMDP (S,A, H, P ⋆, R′,Φ′) with R′ 
h(s, a) = (ρ′)h−1Rh(s, a) and Φ′ given by 
Φ′(P ) = ⊗ 
(s,a)∈S×A 
Bρ′(s, a;P ). (B.1) 
And therefore we are equivalently considering this new type of RMDPs. Please refer to Section B.4.2 for more discussions on the connections between the two types of RMDPs. 
Examples of Assumption 4.1. In the sequel, we provide a concrete condition that makes Assump-tion 4.1 hold, which imposes that the state space of the RMDP has a “closed” subset of “fail-states” with zero rewards. 
Condition B.2 (Fail-states). There exists a subset Sf ⊂ S of fail states such that Rh(s, a) = 0, P ⋆ 
h (Sf |s, a) = 1, ∀(s, a, h) ∈ Sf ×A× [H]. 
This type of “fail-states” condition is first proposed by Panaganti et al. (2022) (with |Sf | = 1) to handle the computational issues for robust offline RL under function approximations (out of the scope of our work). In contrast, here we make the vanishing minimal value assumption in order to tackle the support shift or extrapolation issue for the interactive data collection setup. The comparison between the vanishing minimal value assumption (Assumption 4.1) and the “fail-states” condition (Condition B.2) is given below. 
Remark B.3 (Comparison between Assumption 4.1 and Condition B.2). We first observe that Condition B.2 implies that mins∈S V 
π h,P⋆,Φ(s) = 0 for any policy π and step h ∈ [H], therefore 
satisfying the minimal value assumption (Assumption 4.1). Conversely, the vanishing minimal value assumption in Assumption 4.1 is strictly more general than the fail-state condition in Condition B.2. To illustrate, one can consider an RMDP characterized by the state space S = {s1, s2}, action space A = {a1}, time horizon H = 2, reward function Rh(s, a) = 1{s = s2}, and transition probabilities defined as follows: 
P ⋆ 1 (s1|s1, a1) = 1− ρ, P ⋆ 
1 (s2|s1, a1) = ρ, P ⋆ 1 (s1|s2, a1) = 0, P ⋆ 
1 (s2|s2, a1) = 1, 
where ρ is the radius of the robust set. It is evident that no fail-state emerges within such an RMDP structure. However, this RMDP satisfies the vanishing minimal value assumption since V ⋆ 1,P⋆,Φ(s1) = 0. 
Remark B.4 (Reduction to non-robust MDP without loss of generality). It is noteworthy that assuming the vanishing minimal value (Assumption 4.1) or the presence of fail-states (Condition B.2) in the non-robust case (ρ = 0) is without loss of generality. This is achievable by expanding the prior state space S of MDP to include an additional state sf , denoted as the fail-state. More importantly, this augmentation does not alter the optimal value or the optimal value function of the original MDP. Consequently, it becomes sufficient to seek the optimal policy within the augmented MDP, which satisfies the conditions of vanishing minimal value (Assumption 4.1) or the existence of fail-states (Condition B.2). This indicates that our algorithm and theoretical analysis in the sequel can be directly reduced to non-robust MDPs without additional assumptions. 
B.4.2 Extensions to Robust Set with Bounded Transition Probability Ratio 
In this section, we show that our algorithm design (Algorithm 1) can also be applied to S × A-rectangular discounted RMDPs with robust sets given by (B.1) (i.e., bounded ratio between training and testing transition probabilities). We establish that our main theoretical result in Section 4.3 can imply a sublinear regret upper bound for this model, which means that this type of RMDPs can also be solved sample-efficiently by a clever usage of Algorithm 1. This coincides with our intuition on support shift in Section 4.1. 
S × A-rectangular discounted RMDPs with robust set (B.1). We first formally define the model we consider. We define a finite-horizon discounted RMDP as a finite-horizon RMDP Mγ = (S,A, H, P ⋆, Rγ ,Φ 
′), where the robust set Φ′ is given by (B.1), i.e., 
Φ′(P ) = ⊗ 
(s,a)∈S×A 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} := 
⊗ (s,a)∈S×A 
Bρ′(s, a;P ⋆). (B.2) 
19
This robust set contains transition probabilities that share the same support as the nominal transition kernel. The reward function Rγ = {γh−1 · Rh}Hh=1, where γ ∈ (0, 1) is the discount factor and Rh ∈ [0, 1] is the true reward at step h. That is, the robust value function is now the worst case expected discounted total reward. 
Algorithm and regret bound. Now we show that we can apply Algorithm 1 to solve robust RL in S ×A-rectangular discounted RMDPs with robust set (B.2) via interactive data collection. 
As motivated by the discussions under Proposition 4.2, we define an auxiliary finite-horizon TV-RMDP M̃ as M̃ = (S̃,A, H, P̃ ⋆, R̃, Φ̃) which include an additional “fail-state” sf . More specifically, the state space S̃ = S ∪ {sf}. The transition kernel P̃ ⋆ is defined as, for any step h ∈ [H], 
P̃ ⋆ h (·|s, a) = P ⋆ 
h (·|s, a), ∀(s, a) ∈ S ×A and P̃ ⋆ h (·|sf , a) = δsf (·), ∀a ∈ A. (B.3) 
The reward function R̃ is defined as, for any step h ∈ [H], 
R̃h(s, a) = 
( γ 
ρ′ 
)h−1 
·Rh(s, a), ∀(s, a) ∈ S ×A and R̃h(sf , a) = 0, ∀a ∈ A. 
We suppose that the discount factor γ ≤ ρ′ so that the reward function R̃h ∈ [0, 1]. The robust mapping Φ̃ is defined as, for any P̃ : S̃ × A 7→ ∆(S̃), 
Φ̃(P̃ ) = ⊗ 
(s,a)∈S̃×A 
{ P̃ (·) ∈ ∆(S̃) : DTV 
( P (·) 
∥∥P̃ (·|s, a)) ≤ ρ } 
:= ⊗ 
(s,a)∈S̃×A 
P̃ρ(s, a; P̃ ), ρ = 2− 2ρ′. 
Therefore, M̃ is an RMDP with S × A-rectangular TV robust set of radius ρ and satisfying As-sumption 4.1 (because it satisfies the “fail-state” Condition B.2). Furthermore, for any initial state s1 ∈ S̃ \ {sf} = S, the interaction with the transition kernel P̃ ⋆ is equivalent to the interaction with the transition kernel P ⋆ of the original RMDP Mγ , since by the definition (B.3), starting from any s ̸= sf the agent would follow the same dynamics as P ⋆. What’s more, for any policy π̃h : S̃ 7→ ∆(A) for M̃, it naturally induces the unique policy π̃S,h : S 7→ ∆(A) for the original RMDP Mγ . 
Therefore, we can run Algorithm 1 on the auxiliary RMDP M̃, starting from the initial state s1 ∈ S̃ \ {sf}, which only needs the interaction with P ⋆. Suppose the output policy by the algorithm is {π̃k}Kk=1, then the following corollary shows the induced policy {π̃k 
S}Kk=1 for the original RMDP Mγ enjoys a sublinear regret. 
Corollary B.5 (Online regret of Algorithm 1 for discounted RMDPs with robust sets (B.2)). Consider an S × A-rectangular γ-discounted RMDP with robust set (B.2) satisfying 0 ≤ γ ≤ ρ′ ∈ (1/2, 1]. There exists an algorithm ALG (specified by the above discussion) such that its online regret for this RMDP is bounded by 
RegretALG Φ′ (K) ≤ O 
(√ min 
{ H, (2− 2ρ′)−1 
} H2SAKι′ 
) , 
where ι′ = log2(SAHK/δ) and O(·) hides absolute constants and lower order terms in K. 
Proof of Corollary B.5. See Appendix F.1 for a detailed proof of Corollary B.5. 
Corollary B.5 shows that besides S × A-rectangular RMDPs with TV robust set and vanishing minimal value assumption, the S × A-rectangular discounted RMDP with robust set of bounded transition probability ratio (B.2) can also be solved sample-efficiently by robust RL via interactive data collection. This also echoes our intuition on the support shift issue in Section 4.1. Furthermore, the regret decays as ρ′ decays in which case the transition probability ratio bound becomes higher, i.e., the robust set becomes larger. 
Remark B.6. The upper bound in Corollary B.5 does not depend on the discount factor γ since Algorithm 1 adopts a coarse bound of R̃h ≤ 1. The upper bound can be directly improved to be γ-dependent using a tighter truncation in step (4.2) of Algorithm 1. 
20
B.5 Discussions of Limitations and Future Works 
In this work, we show that in the absence of any structural assumptions, robust RL through interactive data collection necessarily induces a linear regret lower bound in the worst case due to the curse of support shift. Meanwhile, under the vanishing minimal value assumption, an assumption that is able to effectively rule out the potential support shift issues for RMDPs with a TV robust set, we propose a sample-efficient robust RL algorithm for those RMDPs. We discuss some potential extensions here and the associated challenges next. 
Extension to function approximation setting. The vanishing minimal value assumption also suffices for developing sample-efficient algorithms for S ×A-rectangular TV-robust-set RMDPs with linear or even general function approximation (Blanchet et al., 2023). Nonetheless, achieving the nearly optimal rate under general function approximation remains elusive. 
Extension to other types of robust set. Beyond the TV distance based robust set we consider, recent literature on robust RL also investigate other types of ϕ-divergence based robust set including KL divergence, χ2 distance (Yang et al., 2022; Shi and Chi, 2022; Blanchet et al., 2023; Xu et al., 2023; Shi et al., 2023). An interesting direction of future work is to investigate is it also possible and, if possible, can we design provably sample-efficient robust RL algorithms with interactive data collection for RMDPs with those types of robust sets. Notably, the KL divergence based robust set naturally does not suffer from the curse of support shifts that gives rise to the hardness for the TV robust set case. However, we find that there are other difficulties for robust RL in KL divergence based RMDPs through interactive data collection. Meanwhile, the optimal sample complexity for robust RL in RMDPs with KL divergence robust set is still elusive even in the offline learning setup (Shi and Chi, 2022). We leave the study of RMDPs with KL divergence robust set for future work. 
C Proofs for Properties of RMDPs with TV Robust Sets 
C.1 Proof of Proposition 2.5 
To simplify the notations, we present the following lemma, which directly implies Proposition 2.5. 
Lemma C.1 (Strong duality for TV robust set). The following duality for total variation robust set holds, for f : S 7→ [0, H], 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈[0,H] 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ 
2 · ( η −min 
s∈S f(s) 
) + 
+ η 
} , 
where σ ∈ [0, 1] and the TV distance DTV(Q(·)∥Q⋆(·)) is defined as 
DTV(Q(·)∥Q⋆(·)) = 1 
2 
∑ s∈S 
|Q(s)−Q⋆(s)|. 
Proof of Lemma C.1. First, we note that when Q⋆(s) > 0 for any s ∈ S, i.e., any Q(·) ∈ ∆(S) is absolute continuous w.r.t. Q⋆(·), it has been proved by Yang et al. (2022) that 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈R 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ 
2 · ( η −min 
s∈S f(s) 
) + 
+ η 
} . 
Furthermore, as is shown in Lemma H.8 in Blanchet et al. (2023), the optimal dual variable η⋆ lies in [0, H] when f ∈ [0, H]. Therefore, for Q⋆(·) such that Q⋆(s) > 0 for any s ∈ S, we have 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈[0,H] 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ 
2 · ( η −min 
s∈S f(s) 
) + 
+ η 
} . 
Now for any Q⋆(·) ∈ ∆(S), we can prove the same result by averaging Q⋆(·) with a uniform distribution and taking the limit. More specifically, denote U(·) ∈ ∆(S) as the uniform distribution 
21
on S, i.e., U(s) = 1/|S| for any s ∈ S. Consider the following distributionally robust optimization problem, for any ϵ ∈ [0, 1], 
P(ϵ) := inf Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ]. 
By our previous discussions, since (1− ϵ)Q⋆(s) + ϵ · U(s) > 0 for any s ∈ S and ϵ > 0, we have that 
P(ϵ) = D(ϵ), ∀ϵ ∈ (0, 1], (C.1) 
where the function D(·) : [0, 1] 7→ R+ is defined as 
D(ϵ) := sup η∈[0,H] 
{ −(1− ϵ) · EQ⋆(·) 
[ (η − f)+ 
] − ϵ · EU(·) 
[ (η − f)+ 
] − σ 
2 · ( η −min 
s∈S f(s) 
) + 
+ η 
} . 
By the definition of P(·) and D(·), our goal is to prove that P(0) = D(0). To this end, it suffices to prove that (i) limϵ→0+ D(ϵ) exists and limϵ→0+ D(ϵ) = D(0); and (ii) limϵ→0+ P(ϵ) = P(0). To prove (i), consider that for any ϵ > 0, by the definition of D(·), 
|D(0)− D(ϵ)| ≤ sup η∈[0,H] 
{ ϵ · EQ⋆(·) 
[ (η − f)+ 
] + ϵ · EU(·) 
[ (η − f)+ 
]} ≤ ϵ · 2H. 
Since the right hand side tends to 0 as ϵ tends to 0, we know that limϵ→0+ D(ϵ) exists, limϵ→0+ D(ϵ) = D(0). This also indicates that limϵ→0+ P(ϵ) exists due to (C.1). This proves (i). Now we prove (ii). Notice that since the set{ 
Q(·) ∈ ∆(S) : DTV 
( Q(·)∥(1− ϵ)Q⋆(·) + ϵ · U(·) 
) ≤ σ 
} is a closed subset of R|S|, and EQ(·)[f ] is a continuous function of Q(·) ∈ R|S| w.r.t. the ∥ · ∥2-norm, we can denote the optimal solution to the optimization problem involved in P(ϵ) as 
Q† ϵ(·) = arginf 
Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ], 
which also gives that 
P(ϵ) = EQ† ϵ(·)[f ] = 
∑ s∈S 
Q† ϵ(s)f(s). 
With these preparations, we are able to prove (ii). On the one hand, consider for any ϵ ∈ (0, 1], 
DTV 
( (1− ϵ) ·Q† 
0(·) + ϵ · U(·) ∥∥(1− ϵ) ·Q⋆(·) + ϵ · U(·) 
) ≤ (1− ϵ) · σ ≤ σ. 
Therefore, for any ϵ ∈ (0, 1], it holds that 
P(ϵ) = inf Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ] 
≤ E(1−ϵ)·Q† 0(·)+ϵ·U(·)[f ] = (1− ϵ) · EQ† 
0 [f ] + ϵ · EU(·)[f ], 
which implies that 
lim ϵ→0+ 
P(ϵ) ≤ EQ† 0 [f ] = P(0). (C.2) 
On the other hand, for any ϵ ∈ (0, 1], 
σ ≥ 1 
2 
∑ s∈S 
∣∣∣Q† ϵ(s)− (1− ϵ) ·Q⋆(s)− ϵ · U(s) 
∣∣∣ ≥ (1− ϵ) ·DTV(Q 
† ϵ(·)∥Q⋆(·))− ϵ ·DTV(Q 
† ϵ(·)∥U(·)), 
and by using DTV(Q † ϵ(·)∥U(·)) ≤ 1, we obtain that 
DTV(Q † ϵ(·)∥Q⋆(·)) ≤ σ + ϵ 
1− ϵ . (C.3) 
22
Consider a sequence of {ϵi}∞i=1 converging to 0, i.e., limi→0+ ϵi = 0. Since {Q† ϵi(·)} 
∞ i=1 is a 
sequence contained in a compact subset of R|S|, it has a converging (w.r.t. ∥ · ∥2) subsequence denoted by {Q† 
ϵik (·)}∞k=1 whose limit is denoted as Q†(·) ∈ ∆(S). By (C.3), we know that 
DTV(Q † ϵik 
(·)∥Q⋆(·)) ≤ σ + ϵik 1− ϵik 
. (C.4) 
Taking limit on both sides of (C.4) (limit of LHS exists since the TV distance is a continuous function (w.r.t. ∥ · ∥2) of its first entry and the limit of RHS obviously exists), we obtain that 
DTV(Q †(·)∥Q⋆(·)) ≤ σ. (C.5) 
Now we can arrive at the following, 
lim ϵ→0+ 
P(ϵ) = lim ϵ→0+ 
EQ† ϵ(·)[f ] = lim 
k→0+ EQ† 
ϵik (·)[f ] = EQ†(·)[f ] 
≥ inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = P(0), (C.6) 
where the first and the last equality follows from the definition of P(·), the second equality follows from the choice of the sequence {ϵik}∞k=1 that converges to 0, the third equality is due to the continuity of EQ(·)[f ] of Q(·) (w.r.t. ∥ · ∥2), and the inequality follows from (C.5). Finally, with (C.2) and (C.6), we conclude that 
lim ϵ→0+ 
P(ϵ) = P(0), 
which proves (ii). Consequently, by (i) and (ii) 
P(0) = lim ϵ→0+ 
P(ϵ) = lim ϵ→0+ 
D(ϵ) = D(0). 
Recalling the definitions of P(·) and D(·), we conclude the proof of Lemma C.1. 
C.2 Proof of Proposition 2.6 
Proof of Proposition 2.6. Here we prove a stronger result that for any policy π and step h ∈ [H] 
max (s,a)∈S×A 
Qπ h,P,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P,Φ(s, a) ≤ 1 
ρ · ( 1− (1− ρ)H−h+1 
) , (C.7) 
max s∈S 
V π h,P,Φ(s)−min 
s∈S V π h,P,Φ(s) ≤ 
1 
ρ · ( 1− (1− ρ)H−h+1 
) . (C.8) 
First, we note that for the last step h = H , (C.7) and (C.8) naturally hold since RH ∈ [0, 1]. Now suppose that (C.8) hold for some step h+ 1. By robust Bellman equation (Proposition 2.2), we have that 
Qπ h,P⋆,Φ(s, a) = Rh(s, a) + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] ≤ 1 + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] , ∀(s, a) ∈ S ×A, (C.9) 
where the inequality uses the fact that Rh ≤ 1. Now we denote the state with the least robust value as 
s0 ∈ argmin s∈S 
V π h+1,P⋆,Φ(s). (C.10) 
Inspired by Shi et al. (2023), we choose a transition kernel P̃h satisfying that∥∥∥P̃h(·|s, a) ∥∥∥ 1 = 1− ρ, P ⋆ 
h (s ′|s, a) ≥ P̃h(s 
′|s, a) ≥ 0, ∀(s, a, s′) ∈ S ×A× S, 
which implies that 
DTV 
( P̃h(·|s, a) + ρ · δs0(·) 
∥∥∥P ⋆ h (·|s, a) 
) ≤ ρ, ∀(s, a) ∈ S ×A. 
23
Here δs0(·) is the point measure centered at s0 defined in (C.10). Combined with (C.9), we have that 
Qπ h,P⋆,Φ(s, a) ≤ 1 + EP̃h(·|s,a)+ρ·δs0 (·) 
[ V π h+1,P⋆,Φ 
] = 1 + EP̃h(·|s,a) 
[ V π h+1,P⋆,Φ 
] + ρ · V π 
h+1,P⋆,Φ(s0) 
≤ 1 + (1− ρ) ·max s∈S 
V π h+1,P⋆,Φ(s) + ρ ·min 
s∈S V π h+1,P⋆,Φ(s). (C.11) 
Consequently from (C.11), we further obtain that for any (s, a) ∈ S ×A, 
Qπ h,P⋆,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
≤ 1 + (1− ρ) ·max s∈S 
V π h+1,P⋆,Φ(s) + ρ ·min 
s∈S V π h+1,P⋆,Φ(s)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
= 1 + (1− ρ) · ( max s∈S 
V π h+1,P⋆,Φ(s)−min 
s∈S V π h+1,P⋆,Φ(s) 
) +min 
s∈S V π h+1,P⋆,Φ(s)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
≤ 1 + (1− ρ) · ( max s∈S 
V π h+1,P⋆,Φ(s)−min 
s∈S V π h+1,P⋆,Φ(s) 
) , (C.12) 
where the first inequality uses (C.11) and the last inequality uses the following fact, 
min (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a) = min 
(s,a)∈S×A 
{ Rh(s, a) + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
]} ≥ min 
s∈S V π h+1,P⋆,Φ(s). 
Now applying the assumption that (C.8) holds at step h+1 to the right hand side of (C.12), we obtain that 
max (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) ≤ 1 + 1− ρ 
ρ · ( 1− (1− ρ)H−h 
) = 
1 
ρ · ( 1− (1− ρ)H−h+1 
) . 
Thus given (C.8) at step h+ 1, we can derive (C.7) at step h. Now by noticing that 
min (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a) ≤ min 
s∈S V π h,P⋆,Φ(s) ≤ max 
s∈S V π h,P⋆,Φ(s) ≤ max 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a), 
we can conclude that (C.8) also holds at step h. As a result, by an induction argument, we finish the proof of Proposition 2.6. 
C.3 Proof of Proposition 4.2 
Proof of Proposition 4.2. We consider some fixed (s, a, h) ∈ S × A × [H] throughout proof. By Lemma C.1, we have that 
EPρ(s,a;P⋆ h ) [V ] = sup 
η∈R 
{ −EP⋆ 
h (·|s,a) [ (η − V )+ 
] − ρ 
2 · ( η −min 
s∈S V (s) 
) + 
+ η 
} 
= sup η∈[0,H] 
{ −EP⋆ 
h (·|s,a) [ (η − V )+ 
] − ρ 
2 · ( η −min 
s∈S V (s) 
) + 
+ η 
} 
= sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + ( 1− ρ 
2 
) · η } , (C.13) 
where the second equality follows from the fact the optimal dual variable η⋆ is in [0, H] when V ∈ [0, H] (see e.g., Lemma H.8 in Blanchet et al. (2023)), and the last equality is obtained by the fact that mins∈S V (s) = 0. 
24
Part (i). For any η ∈ [0, H] and Q ∈ Bρ′(s, a;P ⋆ h ), we have that 
−EP⋆ h (·|s,a) 
[ (η − V )+ 
] + ( 1− ρ 
2 
) · η ≤ 
( 1− ρ 
2 
) · ( − EQ(·) 
[ (η − V )+ 
] + η ) 
≤ ( 1− ρ 
2 
) · ( − EQ(·) 
[ η − V 
] + η ) 
= ( 1− ρ 
2 
) · EQ(·) 
[ V ] , (C.14) 
where the first inequality uses the definition of Bρ′(s, a;P ⋆ h ), the second equality follows from the 
fact that (x)+ ≥ x. Furthermore, by (C.14) we have that 
sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + ( 1− ρ 
2 
) · η } 
≤ ( 1− ρ 
2 
) · inf Q∈Bρ′ (s,a;P 
⋆ h ) 
EQ(·) [ V ] .(C.15) 
Combining (C.13) and (C.15), we have that 
EPρ(s,a;P⋆ h ) 
[ V ] ≤ ρ′ · EBρ′ (s,a;P 
⋆ h ) 
[ V ] . 
Part (ii). Since ρ ∈ [0, 1], we know that there exists a η̃ ∈ [0, H] such that∑ s′:V (s′)<η̃ 
P ⋆ h (s 
′|s, a) ≤ 1− ρ 
2 ≤ 
∑ s′:V (s′)≤η̃ 
P ⋆ h (s 
′|s, a), 
which further implies that we have the following interpolation for some λ ∈ [0, 1]: 
1− ρ 
2 = λ 
∑ s′:V (s′)<η̃ 
P ⋆ h (s 
′|s, a) + (1− λ) ∑ 
s′:V (s′)≤η̃ 
P ⋆ h (s 
′|s, a). 
We define a probability measure P̃ ⋆ ∈ ∆(S) as 
P̃ ⋆ h = 
λP ⋆ h (s 
′|s, a) · 1{V (s′) > η̃}+ (1− λ)P ⋆ h (s 
′|s, a) · 1{V (s′) ≥ η̃} 1− ρ 
2 
. (C.16) 
It is not difficult to verify that P̃ ⋆ h ∈ Bρ′(s, a;P ⋆ 
h ). Hence, we have( 1− ρ 
2 
) · EBρ′ (s,a;P 
⋆ h )[V ] ≤ 
( 1− ρ 
2 
) · EP̃⋆ 
h (·) [ V ] 
= ( 1− ρ 
2 
) · EP̃⋆ 
h (·) [ V − η̃ 
] + ( 1− ρ 
2 
) · η̃ 
= −EP⋆ h (·|s,a) 
[ (η̃ − V )+ 
] + ( 1− ρ 
2 
) · η̃, (C.17) 
where the last inequality uses the definition of P̃ ⋆ h in (C.16). Furthermore, by (C.17) we have that 
ρ′ · EBρ′ (s,a;P ⋆ h ) 
[ V ] ≤ sup 
η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + ( 1− ρ 
2 
) · η } 
(C.18) 
= EPρ(s,a;P⋆ h ) 
[ V ] , 
where the equality follows from (C.13). 
Combining Part (i) and Part (ii). Finally, combining (C.15) and (C.18), we prove Proposition 4.2. 
D Proofs for Hardness Results 
D.1 Proof of Theorem 3.2 
Proof of Theorem 3.2. We first explicitly give the expressions of the robust value functions in Exam-ple 3.1, based on which we derive the desired online regret lower bound. 
25
Robust value function. Firstly, we can explicitly write down the expression of the robust value functions for any policy π under Example 3.1, i.e., V π 
h,P⋆,Mθ ,Φ and Qπ 
h,P⋆,Mθ ,Φ . From now on we 
fix a policy π. 
For step h = 3, the robust value function is the reward received. We can directly obtain for any a ∈ A, 
Qπ 3,P⋆,Mθ ,Φ(sgood, a) = V π 
3,P⋆,Mθ ,Φ(sgood) = 1, (D.1) 
Qπ 3,P⋆,Mθ ,Φ(sbad, a) = V π 
3,P⋆,Mθ ,Φ(sbad) = 0. 
For step h = 2, by the robust Bellman equation (Proposition 2.2), we have that for the good state sgood, 
Qπ 2,P⋆,Mθ ,Φ(sgood, a) (D.2) 
= 1 + inf P∈Pρ(sgood,a;P 
⋆,Mθ 2 ) 
EP (·) [ V π 3,P⋆,Mθ ,Φ 
] = 1 + (1− ρ), ∀a ∈ A, 
where the last equality is because V π 3,P⋆,Mθ ,Φ 
takes the minimal value 0 at the bad state sbad and thus the most adversarial transition distribution is achieved at 
P †(s′) = (1− ρ) · 1{s′ = sgood}+ ρ · 1{s′ = sbad}. Similarly, we have that for the bad state sbad, 
Qπ 2,P⋆,Mθ ,Φ(sbad, a) = 0 + inf 
P∈Pρ(sbad,a;P ⋆,Mθ 2 ) 
EP (·) [ V π 3,P⋆,Mθ ,Φ 
] (D.3) 
= 
{ p− ρ, a = θ 
q − ρ, a = 1− θ . 
Finally by the robust Bellman equation again, we have that 
V π 2,P⋆,Mθ ,Φ(sgood) = 1 + (1− ρ), 
V π 2,P⋆,Mθ ,Φ(sbad) = π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ). 
Notice that by q < p we know that V π 2,P⋆,Mθ ,Φ 
(sbad) < p− ρ < 1 + (1− ρ) < V π 2,P⋆,Mθ ,Φ 
(sgood). 
For step h = 1, we consider the robust values on the initial state s1 = sgood, by robust Bellman equation, 
Qπ 1,P⋆,Mθ ,Φ(sgood, a) = 1 + inf 
P∈Pρ(sgood,a;P ⋆,Mθ 1 ) 
EP (·) [ V π 2,P⋆,Mθ ,Φ 
] (D.4) 
= 1 + (1− ρ) · [ 1 + (1− ρ) 
] + ρ · 
[ π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
] , ∀a ∈ A. 
By robust Bellman equation, we also derive V π 1,P⋆,Mθ ,Φ 
(sgood) = Qπ 1,P⋆,Mθ ,Φ 
(sgood, a) for ∀a ∈ A. 
Lower bound the online regret under Example 3.1. With all the previous preparation, we can lower bound the online regret for robust RL with interactive data collection in Example 3.1. But first, we present the following general lemma. 
Lemma D.1 (Performance difference lemma for robust value function). For any RMDP satisfying Assumption 2.1 and any policy π, the following inequality holds, 
V π⋆ 
1,P⋆,Φ(s)− V π 1,P⋆,Φ(s) 
≥ E(Pπ⋆,†,π⋆) 
[ H∑ 
h=1 
∑ a∈A 
( π⋆ h(a|sh)− πh(a|sh) 
) ·Qπ 
h,P⋆,Φ(sh, a) 
∣∣∣∣∣s1 = s 
] , 
where the expectation is taken with respect to the trajectories induced by policy π⋆, transition kernel Pπ⋆,†. Here the transition kernel Pπ⋆,† is defined as 
Pπ⋆,† h (·|s, a) = arginf 
P∈P(s,a;P⋆ h ) 
EP (·) [ V π⋆ 
h+1,P⋆,Φ 
] , 
where P(s, a;P ⋆ h ) is the robust set for state-action pair (s, a) (see Assumption 2.1). 
26
Proof of Lemma D.1. Please refer to Appendix D.2 for a detailed proof of Lemma D.1. 
Now back to Example 3.1, our previous calculation actually shows that, by (D.1) for step h = 3,∑ a∈A 
( π⋆,Mθ 
3 (a|s3)− π3(a|s3) ) ·Qπ 
3,P⋆,Mθ ,Φ(s3, a) = 0, ∀s3 ∈ {sgood, sbad}. (D.5) 
and by (D.4) we also have that for step h = 1,∑ a∈A 
( π⋆,Mθ 
1 (a|s1)− π1(a|s1) ) ·Qπ 
1,P⋆,Mθ ,Φ(s1, a) = 0, where s1 = sgood. (D.6) 
Finally, let’s consider step h = 2. By (D.2), we have that for the good state, it holds that∑ a∈A 
( π⋆,Mθ 
2 (a|sgood)− π2(a|sgood) ) ·Qπ 
2,P⋆,Mθ ,Φ(sgood, a) = 0, (D.7) 
Meanwhile, by (D.3), we have that for the bad state, it holds that (recall that q < p)∑ a∈A 
( π⋆,Mθ 
2 (a|sbad)− π2(a|sbad) ) ·Qπ 
2,P⋆,Mθ ,Φ(sbad, a) 
= max { p− ρ, q − ρ 
} − ( π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
) = p− ρ− 
( π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
) = p− q 
2 · ( ∣∣∣π⋆,Mθ 
2 (θ|sbad)− π2(θ|sbad) ∣∣∣+ ∣∣∣π⋆,Mθ 
2 (1− θ|sbad)− π2(1− θ|sbad) ∣∣∣ ) 
= (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) , (D.8) 
where according to (D.3) the optimal policy of Mθ at h = 2 and sbad is π⋆,Mθ 
2 (θ|sbad) = 1. Now combining (D.5), (D.6), (D.7), and (D.8) with Lemma D.1, we can conclude that 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V π 1,P⋆,Mθ ,Φ(sgood) 
≥ E a1∼π 
⋆,Mθ 1 (·|sgood),s2∼Pπ⋆,Mθ ,† 
1 (·|sgood,a1) 
[∑ a∈A 
( π⋆ 2(a|s2)− π2(a|s2) 
) ·Qπ 
2,P⋆,Mθ ,Φ(s2, a) 
] 
= Pπ⋆,Mθ ,† 1 (sbad|sgood, 0) · (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) , (D.9) 
where the adversarial transition kernel Pπ⋆,Mθ ,† 1 is given by 
Pπ⋆,Mθ ,† 1 (·|sgood, 0) = argmin 
P∈P(sgood,0;P ⋆,Mθ 1 ) 
EP (·) 
[ V π⋆,Mθ 
2,P⋆,Mθ ,Φ 
] = (1− ρ) · 1{· = sgood}+ ρ · 1{· = sbad}. (D.10) 
Consequently, taking (D.10) back into (D.9), we have that 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V π 1,P⋆,Mθ ,Φ(sgood) ≥ ρ · (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) . 
This implies that for any algorithm executing π1, · · · , πK , its online regret is lower bounded by the following, 
RegretMθ,ALG Φ (K) = 
K∑ k=1 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V πk 
1,P⋆,Mθ ,Φ(sgood) 
≥ ρ · (p− q) · K∑ 
k=1 
DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥πk 
2 (·|sbad) ) . 
27
However, since in RMDPs of Example 3.1, the online interaction process is always kept in sgood and there is no information on θ which can only be accessed at (s, h) = (sbad, 2). As a result, the estimates πk 
2 (·|sbad) of π⋆,Mθ 
2 (·|sbad) = 1{· = θ} can do no better than a random guess. Put it formally, consider that 
sup θ∈{0,1} 
EMθ,ALG 
[ RegretMθ,ALG 
Φ (K) ] 
≥ ρ · (p− q) · sup θ∈{0,1} 
EMθ,ALG 
[ K∑ 
k=1 
DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥πk 
2 (·|sbad) )] 
= ρ · (p− q) · sup θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] . (D.11) 
Here in the last equality we can drop the subscription of Mθ because the algorithm outputs πk 2 
independent of the θ due to our previous discussion. Notice that∑ θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] = 
K∑ k=1 
∑ θ∈{0,1} 
EALG [ πk 2 (1− θ|sbad) 
] = 
K∑ k=1 
1 = K, 
which further indicates that 
sup θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] ≥ K 
2 . (D.12) 
Therefore, by combining (D.11) and (D.12), we conclude that 
inf ALG 
sup θ∈{0,1} 
EMθ,ALG 
[ RegretMθ,ALG 
Φ (K) ] ≥ (p− q) · ρK 
2 . 
This is the desired online regret lower bound of Ω(ρ ·K) for the RMDPs presented in Example 3.1. Furthermore, we can construct two RMDPs {M̃0,M̃1} with horizon 3H by concatenating H 
RMDPs {M0,M1} presented in Example 3.1. Notably, at any steps {3i+ 1}H−1 i=0 , we define 
R3i+1(sbad, a) = 1, P ⋆,M̃θ 
3i+1 (sgood|sbad, a) = 1, ∀(a, θ) ∈ A× {0, 1}. Then we have 
inf ALG 
sup θ∈{0,1} 
EM̃θ,ALG 
[ RegretM̃θ,ALG 
Φ (K) ] ≥ H · Ω(ρ ·K) = Ω(ρ ·HK), 
which completes the proof of Theorem 3.2. 
D.2 Proof of Lemma D.1 
Proof of Lemma D.1. For any step h ∈ [H], we have that by robust Bellman equation (Proposi-tion 2.2), 
Qπ⋆ 
h,P⋆,Φ(s, a)−Qπ h,P⋆,Φ(s, a) = EPρ(s,a;P⋆ 
h ) 
[ V π⋆ 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] . 
By the definition of the transition kernel Pπ⋆,† in Lemma D.1 and the property of infimum, we have that 
Qπ⋆ 
h,P⋆,Φ(s, a)−Qπ h,P⋆,Φ(s, a) ≥ E 
Pπ⋆,† h (·|s,a) 
[ V π⋆ 
h+1,P⋆,Φ 
] − E 
Pπ⋆,† h (·|s,a) 
[ V π h+1,P⋆,Φ 
] = E 
Pπ⋆,† h (·|s,a) 
[ V π⋆ 
h+1,P⋆,Φ − V π h+1,P⋆,Φ 
] . (D.13) 
By robust Bellman equation (Proposition 2.2) and (D.13), we further obtain that 
V π⋆ 
h,P⋆,Φ(s)− V π h,P⋆,Φ(s) = Eπ⋆ 
h(·|s) [ Qπ⋆ 
h,P⋆,Φ(s, ·) ] − Eπh(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] 
= Eπ⋆ h(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] − Eπh(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] 
+ Eπ⋆ h(·|s) 
[ Qπ⋆ 
h,P⋆,Φ(s, ·) ] − Eπ⋆ 
h(·|s) [ Qπ 
h,P⋆,Φ(s, ·) ] 
≥ ∑ a∈A 
( π⋆ h(a|s)− πh(a|s) 
) ·Qπ 
h,P⋆,Φ(s, a) 
+ E a∼π⋆ 
h(·|s),P π⋆,† h (·|s,a) 
[ V π h,P⋆,Φ − V π 
h,P⋆,Φ 
] . (D.14) 
28
Thus by recursively applying (D.14) over h ∈ [H], we can conclude that 
V π⋆ 
1,P⋆,Φ(s)− V π 1,P⋆,Φ(s) 
≥ E(Pπ⋆,†,π⋆) 
[ H∑ 
h=1 
∑ a∈A 
( π⋆ h(a|sh)− πh(a|sh) 
) ·Qπ 
h,P⋆,Φ(sh, a) 
∣∣∣∣∣s1 = s 
] , 
which completes the proof of Lemma D.1. 
E Proofs for Theoretical Analysis of OPROVI-TV 
In this section, we prove our main theoretical results (Theorem 4.3). In Appendix E.1, we outline the proof of the theorem. In Appendix E.2, we list all the key lemmas used in the proof of the theorem. We defer the proof of all the lemmas to subsequent sections (Appendices E.3 to E.8). 
Before presenting all the proofs, we define the typical event E as 
E = 
 ∣∣∣∣ (EP⋆ 
h (·|s,a) − EP̂k h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
∣∣∣P ⋆ h (s 
′|s, a)− P̂h(s ′|s, a) 
∣∣∣ ≤ √√√√min 
{ P ⋆ h (s 
′|s, a), P̂ k h (s 
′|s, a) } · c1ι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
, 
∀(s, a, s′, h, k) ∈ S ×A× S × [H]× [K], ∀η ∈ N1/(S √ K) 
( [0, H] 
), where ι = log(S3AH2K3/2/δ), c1, c2 > 0 are two absolute constants, N1/S 
√ K([0, H]) denotes an 
1/S √ K-cover of the interval [0, H]. 
Lemma E.1 (Typical event). For the typical event E defined in (E.35), it holds that P(E) ≥ 1− δ. 
Proof of Lemma E.1. This is a direct application of Bernstein inequality and its empirical version (Maurer and Pontil, 2009), together with a union bound over (s, a, s′, h, k, η) ∈ S ×A×S × [H]× [K]×N1/(S 
√ K)([0, H]). Note that the size of N1/(S 
√ K)([0, H]) is of order SH 
√ K. 
In this section, we always let the event E hold, which by Lemma E.1 is of probability at least 1− δ. 
E.1 Proof of Theorem 4.3 
Proof of Theorem 4.3. With Lemma E.2 (optimism and pessimism), we upper bound the regret as 
RegretΦ(K) = 
K∑ k=1 
V ⋆ 1,P⋆,Φ(s1)− V πk 
1,P⋆,Φ(s1) ≤ K∑ 
k=1 
V k 
1(s1)− V k 1(s1). (E.1) 
In the sequel, we break our proof into three steps. 
Step 1: upper bounding (E.1). According to the choice of Q k 
h, Qk 
h , V 
k 
h, V k h in (4.2), (4.3), and 
(4.4), let’s consider that for any (h, k) ∈ [H]× [K] and (s, a) ∈ S ×A, 
Q k 
h(s, a)−Qk 
h (s, a) 
= min 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a), min 
{ H, ρ−1 
}} 
29
−max 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − bonuskh(s, a), 0 
} ≤ EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] + 2 · bonuskh(s, a) 
= EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] ︸ ︷︷ ︸ 
Term (i) 
+ EPρ(s,a;P⋆ h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] ︸ ︷︷ ︸ 
Term (ii) 
+2 · bonuskh(s, a). (E.2) 
Step 1.1: upper bounding Term (i). By using a Bernstein-style concentration argument customized for TV robust expectations (Lemma E.3), we can bound Term (i) by the bonus function, i.e., 
Term (i) ≤ 2 · bonuskh(s, a). (E.3) 
Step 1.2: upper bounding Term (ii). By our definition of the operator EPρ(s,a;P⋆ h )[V ] in (4.1), we 
have 
Term (ii) = sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V 
k 
h+1 
) + 
] + ( 1− ρ 
2 
) · η } 
− sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V k 
h+1 
) + 
] + ( 1− ρ 
2 
) · η } 
≤ sup η∈[0,H] 
{ EP⋆ 
h (·|s,a) 
[( η − V k 
h+1 
) + − ( η − V 
k 
h+1 
) + 
]} . (E.4) 
By Lemma E.2 which shows that V k 
h+1 ≥ V k h+1 and the fact that (η − x)+ − (η − y)+ ≤ y − x for 
any y > x, we can further upper bound the right hand side of (E.4) by 
Term (ii) ≤ EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . (E.5) 
Step 1.3: combining the upper bounds. Now combining (E.3) and (E.5) with (E.2), we have that 
Q k 
h(s, a)−Qk 
h (s, a) ≤ EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 4 · bonuskh(s, a). 
By Lemma E.4, we can upper bound the bonus function, and after rearranging terms we further obtain that 
Q k 
h(s, a)−Qk 
h (s, a) ≤ 
( 1 + 
12 
H 
) · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] 
+ 4 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 4√ K , (E.6) 
where c1, c2 > 0 are two absolute constants. For the sake of brevity, we introduce the following notations of differences, for any (h, k) ∈ [H]× [K], 
∆k h := V 
k 
h(s k h)− V k 
h(s k h), 
ζkh := ∆k h − 
( Q 
k 
h(s k h, a 
k h)−Qk 
h (skh, a 
k h) ) , (E.7) 
ξkh := EP⋆ h (·|skh,a 
k h) 
[ V 
k 
h − V k h 
] −∆k 
h+1. (E.8) 
If we further define the filtration {Fh,k}(h,k)∈[H]×[K] as 
Fh,k = σ ( {(sτi , aτi )}(i,τ)∈[H]×[k−1] 
⋃ {(ski , aki )}i∈[h−1] 
⋃ {skh} 
) , 
30
then we can find that {ζkh}(h,k)∈[H]×[K] is a martingale difference sequence with respect to {Fh,k}(h,k)∈[H]×[K] and {ξkh}(h,k)∈[H]×[K] is a martingale difference sequence with respect to {Fh,k ∪ {akh}}}(h,k)∈[H]×[K]. Also, we further have that 
∆k h = ζkh + 
( Q 
k 
h(s k h, a 
k h)−Qk 
h (skh, a 
k h) ) 
(E.9) 
≤ ζkh + 
( 1 + 
12 
H 
) · EP⋆ 
h (·|skh,a k h) 
[ V 
k 
h+1 − V k h+1 
] 
+ 4 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4√ K 
= ζkh + 
( 1 + 
12 
H 
) · ξkh + 
( 1 + 
12 
H 
) ·∆k 
h+1+ 
4 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4√ K , 
where the inequality applies (E.6). Recursively applying (E.9) and using the fact that (1 + 12 H )h ≤ 
(1 + 12 H )H ≤ c for some absolute constant c > 0, we can upper bound the right hand side of (E.1) as 
RegretΦ(K) ≤ K∑ 
k=1 
∆k 1 ≤ C1 · 
K∑ k=1 
H∑ h=1 
(ζkh + ξkh) 
+ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ H2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 1√ K . (E.10) 
where C1 > 0 is an absolute constant. 
Step 2: controlling the summation of variance terms. In view of (E.10), it suffices to upper bound its right hand side. The key difficulty is the analysis of the summation of the variance terms, which we focus on now. By Cauchy-Schwartz inequality, 
K∑ k=1 
H∑ h=1 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] Nk 
h (s k h, a 
k h) ∨ 1 
≤ 
√√√√ K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] · 
K∑ k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
. (E.11) 
On the right hand side of (E.11), the summation of the inverse of the count function is a well bounded term (Lemma E.13). So the key is to upper bound the the summation of the variance of the robust value functions to obtain a sharp bound. To this end, we invoke Lemma E.5 to obtain that with probability at least 1− δ, 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ C2 · 
( min 
{ H, ρ−1 
} ·HK +min 
{ H, ρ−1 
}3 ·Hι), (E.12) 
where C2 > 0 is an absolute constant. With inequality (E.12) and Lemma E.13 that K∑ 
k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ C ′ 2 ·HSAι, 
with C ′ 2 > 0 being another constant, we can upper bound the summation of the variance terms (E.11) 
as 
K∑ k=1 
H∑ h=1 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] Nk 
h (s k h, a 
k h) ∨ 1 
31
≤ C3 
√ min 
{ H, ρ−1 
} ·H2SAKι+min 
{ H, ρ−1 
}3 ·H2SAι2. (E.13) 
where C3 > 0 is also an absolute constant. 
Step 3: finishing the proof. With (E.10) and (E.13), it suffices to control the remaining terms. For the summation of the martingale difference terms, notice that by the definitions in (E.7) and (E.8), both ζkh and ξkh are bounded by min{H, ρ−1} according to (4.2) and Lemma E.2 (optimism and pessimism). As a result, using Azuma-Hoeffding inequality, with probability at least 1− δ 
K∑ k=1 
H∑ h=1 
(ζkh + ξkh) ≤ C4 ·min { H, ρ−1 
} · √ HKι, 
where C4 > 0 is an absolute constant. For the summation of the inverse of the count function in (E.10), it suffices to invoke again Lemma E.13. Combining all together, with probability at least 1− 3δ, we have 
RegretΦ(K) ≤ C5 · (√ 
min { H, ρ−1 
} ·H2SAKι2 +min 
{ H, ρ−1 
}3 ·H2SAι3 
+min { H, ρ−1 
} · √ HKι+H3S2Aι2 +H 
√ K 
) = O 
(√ min 
{ H, ρ−1 
} ·H2SAKι′ 
) , 
where C5 > 0 is an absolute constant and ι′ = log2(SAHK/δ). This completes the proof of Theorem 4.3. 
E.2 Key Lemmas 
Lemma E.2 (Optimistic and pessimistic estimation of the robust values). By setting the bonuskh as in (4.5), then under the typical event E , it holds that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a), 
V k h(s) ≤ V πk 
h,P⋆,Φ(s) ≤ V ⋆ h,P⋆,Φ(s) ≤ V 
k 
h(s), (E.14) 
for any (s, a, h, k) ∈ S ×A× [H]× [K]. 
Proof of Lemma E.2. See Appendix E.3 for a detailed proof. 
Lemma E.3 (Proper bonus for TV robust sets and optimistic and pessimistic value estimators). By setting the bonuskh as in (4.5), then under the typical event E , it holds that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] ≤ 2 · bonuskh(s, a), 
Proof of Lemma E.3. See Appendix E.4 for a detailed proof. 
Lemma E.4 (Control of the bonus term). Under the typical event E , the bonuskh in (4.5) is bounded by 
bonuskh(s, a) 
≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 4 · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1−V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c2 > 0 are absolute constants. 
Proof of Lemma E.4. See Appendix E.5 for a detailed proof. 
32
Lemma E.5 (Total variance law for robust MDP with TV robust sets). With probability at least 1− δ, the following inequality holds 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ c3 · 
( min{H, ρ−1} ·HK +min{H, ρ−1}3 ·Hι 
) . 
where ι = log(S3AH2K3/2/δ) and c3 > 0 is an absolute constant. 
Proof of Lemma E.5. See Appendix E.6 for a detailed proof. 
E.3 Proof of Lemma E.2 
Proof of Lemma E.2. We prove Lemma E.2 by induction. Suppose the conclusion (E.14) holds at step h+ 1. For step h, let’s first consider the robust Q function part. Specifically, by using the robust Bellman optimal equation (Proposition 2.3) and (4.2), we have that 
Q⋆ h,P⋆,Φ(s, a)−Q 
k 
h(s, a) 
≤ max 
{ EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − bonuskh(s, a), 
Q⋆ h,P⋆,Φ(s, a)−min 
{ H, ρ−1 
}} ≤ max 
{ EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − bonuskh(s, a), 0 
} ,(E.15) 
where the second inequality follows from the induction of V ⋆ h+1,P⋆,Φ ≤ V 
k 
h+1 at step h+ 1 and the fact that Q⋆ 
h,P⋆,Φ ≤ min{H, ρ−1} (by Proposition 2.6 and Assumption 4.1). By Lemma E.7, we have that 
EPρ(s,a;P⋆ h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
Now by further applying Lemma E.11 to the variance term in the above inequality, we can obtain that 
EPρ(s,a;P⋆ h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] 
≤ 
√√√√(VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] + 4H · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
]) · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√√√√EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] · 4Hc1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 1√ K , (E.16) 
33
where the first inequality is due to Lemma E.11, the second inequality is due to √ a+ b ≤ 
√ a+ 
√ b, 
and the last inequality is from √ ab ≤ a + b where c′2 > 0 is an absolute constant. Therefore, 
combining (E.15) and (E.16), and the choice of bonuskh(s, a) in (4.5), we can conclude that 
Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a). 
Furthermore, it holds that Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a). Thus it reduces to prove Qk 
h (s, a) ≤ 
Qπk 
h,P⋆,Φ(s, a). Again, by using the robust Bellman equation (Proposition 2.2) and (4.3), we have that 
Qk 
h (s, a)−Qπk 
h,P⋆,Φ(s, a) 
≤ max 
{ EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − bonuskh(s, a), 
0−Qπk 
h,P⋆,Φ(s, a) 
} ≤ max 
{ EPρ(s,a;P̂k 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − bonuskh(s, a), 0 
} ,(E.17) 
where the second inequality follows from the induction of V k h+1 ≤ V πk 
h+1,P⋆,Φ at step h+ 1 and the 
fact that Qπk 
h,P⋆,Φ ≥ 0. By Lemma E.8, we have that 
EPρ(s,a;P̂k h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
Now by applying Lemma E.11 to the variance term, with an argument similar to (E.16), we can obtain that 
EPρ(s,a;P̂k h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] (E.18) 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
Thus by combining (E.17) and (E.18), and the choice of bonuskh(s, a) in (4.5), we can conclude that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a). 
Therefore, we have proved that at step h, it holds that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a). 
Finally for the robust V function part, consider that by robust Bellman equation (Proposition 2.2) and (4.4), 
V k h(s) = Eπk 
h(·|s) 
[ Qk 
h (s, ·) 
] ≤ Eπk 
h(·|s) 
[ Qπk 
h,P⋆,Φ(s, ·) ] = V πk 
h,P⋆,Φ(s), 
and that by robust Bellman optimal equation (Proposition 2.3), the choice of πk, and (4.4), 
V ⋆ h,P⋆,Φ(s) = max 
a∈A Q⋆ 
h,P⋆,Φ(s, a) ≤ max a∈A 
Q k 
h(s, a) = V k 
h(s), 
which proves that 
V k h(s) ≤ V πk 
h,P⋆,Φ(s) ≤ V ⋆ h,P⋆,Φ(s) ≤ V 
k 
h(s). 
Since the conclusion (E.14) holds for the V function part at step H + 1, an induction proves Lemma E.2. 
34
E.4 Proof of Lemma E.3 
Proof of Lemma E.3. We upper bound the differences by a concentration inequality Lemma E.9, 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] 
≤ 2 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 2 · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 2c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 2√ K , (E.19) 
where c1, c′2 > 0 are absolute constants. Then applying Lemma E.11 to the variance term in (E.19), with an argument the same as (E.16) in the proof of Lemma E.2, we can obtain that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] 
≤ 2 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 4 · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 2c′′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 2√ K . 
Therefore, by looking into the choice of bonuskh(s, a) in (4.5), we can conclude that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] ≤ 2 · bonuskh(s, a), 
This finishes the proof of Lemma E.3. 
E.5 Proof of Lemma E.4 
Proof of Lemma E.4. Recall that the bonuskh(s, a) is defined as 
bonuskh(s, a) = 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
The main thing we need to consider is to control the first term and the second term. We first deal with the second term of bonuskh(s, a) by invoking Lemma E.10, which gives 
2EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
≤ ( 
2 
H + 
2 
H2 
) · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′2HSι 
Nk h (s, a) ∨ 1 
≤ 3EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2HSι 
Nk h (s, a) ∨ 1 
, (E.20) 
35
where the second inequality is from H ≥ 2. Then we deal with the first term (variance term) of bonuskh(s, a) by invoking Lemma E.12, which gives√√√√VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
(E.21) 
≤ 
√√√√(VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] + 4H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′′2 H 4Sι 
Nk h (s,a)∨1 
+ 1 ) · c1ι 
Nk h (s, a) 
≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√√√√4H · EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√ c1c′′2SH 
2ι 
Nk h (s, a) ∨ 1 
+ 
√ c1ι 
Nk h (s, a) ∨ 1 
≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c′1ι 
Nk h (s, a) ∨ 1 
+ EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 
( 4c1 + 
√ c1c′′2S 
) H2ι 
Nk h (s, a) ∨ 1 
Thus by combining (E.20) and (E.21) with the choice of bonuskh, we can conclude the proof of Lemma E.4. 
E.6 Proof of Lemma E.5 
Proof of Lemma E.5. The key idea is to relate the visitation distribution (w.r.t. P ⋆) and the variance (w.r.t. P ⋆) to the value function of πk, after which we can derive an upper bound for the total variance. Throughout this proof, we use the shorthand that 
H = min { H, ρ−1 
} . 
According to Proposition 2.6 and Assumption 4.1, for any policy π and any step h, the robust value function of π holds that 
max s∈S 
V π h,P⋆,Φ(s) ≤ H, (E.22) 
which we usually apply in the sequel. Also, to facilitate our analysis, we define 
T̃ k h (·|s, a) = argmin 
P (·)∈Ph(s,a;P⋆ h ) 
EP (·) 
[ V πk 
h+1,P⋆,Φ 
] , ∀(s, a, h) ∈ S ×A× [H], 
and set T̃ k = {T̃ k h }Hh=1, which is the most adversarial transition for the true robust value function of 
πk. 
Now consider the following decomposition of our target, 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] = 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] − E(skh,a 
k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
+ 
K∑ k=1 
E(skh,a k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
= 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] − E(skh,a 
k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] ︸ ︷︷ ︸ 
Term (i): martingale difference term 
36
+ K∑ k=1 
E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VT̃k h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] ︸ ︷︷ ︸ 
Term (ii): total variance law 
+ 
K∑ k=1 
E(skh,a k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] − E(skh,a 
k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VT̃k h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] ︸ ︷︷ ︸ 
Term (iii): error from P ⋆ to T̃ k 
. 
In the sequel, we upper bound each of the three terms respectively. 
Term (i): martingale difference term. This is a summation of martingale difference term (with respect to filtration Gk = σ({(sτh, aτh)}(h,τ)∈[H]×[k])). By Azuma-Hoeffding’s inequality, with probability at least 1− δ, 
Term (i) ≤ c ·H ·H2 · √ Kι, (E.23) 
where c > 0 is an absolute constant. We have utilized the fact of (E.22) to obtain the upper bound HH 
2 on each martingale difference term in the summation. 
Term (ii): total variance law. The upper bound of this term is the core part of the analysis, for which we summarize it in the following lemma. 
Lemma E.6 (Total variance law). Under the same setup as Theorem 4.3, given any deterministic policy π, define that 
T̃h(·|s, a) = argmin P (·)∈Pρ(s,a;P⋆ 
h ) 
EP (·) 
[ V π h+1,P⋆,Φ 
] , ∀(s, a, h) ∈ S ×A× [H], (E.24) 
and set T̃ = {T̃h}Hh=1. Then we have 
E(sh,ah)∼(T̃ ,π) 
[ H∑ 
h=1 
VT̃h(·|sh,ah) 
[ V π h+1,P⋆,Φ 
]] ≤ 2H ·H. 
We defer the proof of Lemma E.6 to Appendix E.7. With Lemma E.6, we consider taking policy π = πk for k ∈ [K] therein (which are deterministic policies), and obtain that the Term (ii) is upper bounded by 
Term (ii) ≤ 2H ·H ·K. (E.25) 
Term (iii): error from P ⋆ to T̃ k. We first relate the visitation distribution under P ⋆ to that under T̃ k. On the one hand, by the choice of the adversarial transition kernel T̃ k 
h , it holds that 
DTV 
( P ⋆ h (·|s, a) 
∥∥∥ T̃ k h (·|s, a) 
) ≤ ρ, ∀(s, a, h) ∈ S ×A× [H]. (E.26) 
On the other hand, by (E.22), we can upper bound the variance term by 
VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] ≤ H 
2 , ∀(s, a, h) ∈ S ×A× [H]. (E.27) 
Therefore, by combining (E.26) and (E.27), we can conclude that 
E(skh,a k h)∼(P⋆ 
h ,πk) 
[ H∑ 
h=1 
VP⋆(·|skh,a k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
≤ E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
37
+H · 
( sup 
(s,a,h)∈S×A×[H] 
DTV 
( P ⋆ h (· | s, a) 
∥∥∥ T̃ k h (· | s, a) 
) · sup (s,a,h)∈S×A×[H] 
VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]) 
≤ E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] + ρH ·H2 
. (E.28) 
We then relate the variance term under P ⋆ to that under T̃ k. Specifically, we have 
VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] = EP⋆ 
h (·|s,a) 
[( V πk 
h+1,P⋆,Φ 
)]2 − ( EP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
])2 ≤ ET̃k 
h (·|s,a) 
[( V πk 
h+1,P⋆,Φ 
)]2 − ( ET̃k 
h (·|s,a) 
[ V πk 
h+1(s ′) ])2 
+ 2 · sup (s,a)∈S×A 
DTV 
( P ⋆ h (·|s, a) 
∥∥∥ T̃ k h (·|s, a) 
) · ( max s′∈S 
V π h+1,P⋆,Φ(s 
′) 
)2 
≤ VT̃k h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] + 2ρ ·H2 
, ∀(s, a, h) ∈ S ×A× [H], (E.29) 
where the last inequality follows from the definition of T̃ k and (E.22). Combining (E.28) and (E.29), we can upper bound Term (iii) by the following, 
Term (iii) = K∑ 
k=1 
E(skh,a k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] (E.30) 
− E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
+ 
K∑ k=1 
E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] 
− E(skh,a k h)∼(T̃k,πk) 
[ H∑ 
h=1 
VT̃k h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]] ≤ 3ρH ·H2 ·K ≤ 3H ·H ·K, 
where in the last inequality we use the fact that for any ρ ∈ [0, 1], it holds that 
ρH = ρ ·min { H, ρ−1 
} = min 
{ ρH, 1 
} ≤ 1. 
Finishing the proof. Finally, combining the upper bounds for Terms (i), (ii), and (iii), i.e., (E.23), (E.25), and (E.30), we conclude that with probability at least 1− δ, it holds that 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ c ·H ·H2 · 
√ Kι+ 2H ·H ·K + 3H ·H ·K 
≤ c′ ·H ·H ·K + c′′ ·H ·H3 · ι, 
where in the last inequality we use √ ab ≤ a + b for any a, b > 0. Plug in the notation that 
H = min{H, ρ−1} and finish the proof of Lemma E.5. 
E.7 Proof of Lemma E.6 
Proof of Lemma E.6. Using the property of variance, we have that for any (sh, ah) ∈ S ×A, 
VT̃h(·|sh,ah) 
[ V π h+1,P⋆,Φ 
] = ET̃h(·|sh,ah) 
[( V π h+1,P⋆,Φ 
)2]− (ET̃h(·|sh,ah) 
[ V π h+1,P⋆,Φ 
])2 . (E.31) 
38
By robust Bellman equation (Proposition 2.2) and the definition of T̃h in (E.24), we have that 
V π h,P⋆,Φ(sh) = Rh(sh, πh(sh)) + ET̃h(·|sh,πh(sh)) 
[ V π h+1,P⋆,Φ 
] . (E.32) 
Therefore, by (E.31) and (E.32), we have that 
VT̃h(·|sh,πh(sh)) 
[ V π h+1,P⋆,Φ 
] = ET̃h(·|sh,πh(sh)) 
[( V π h+1,P⋆,Φ 
)2]− (V π h,P⋆,Φ(sh)−Rh(sh, πh(sh)) 
)2 . (E.33) 
For the second term in (E.33), we can calculate it as 
− ( V π h,P⋆,Φ(sh)−Rh(sh, πh(sh)) 
)2 = − 
( V π h,P⋆,Φ 
)2 (sh) + 2 · V π 
h,P⋆,Φ(sh) ·Rh(sh, πh(sh))−R2 h(sh, πh(sh)) 
≤ − ( V π h,P⋆,Φ 
)2 (sh) + 2H, (E.34) 
where the last inequality utilizes the facts that 0 ≤ Rh(sh, πh(sh)) ≤ 1, R2 h(sh, πh(sh)) ≥ 0, and 
(E.22) that V π h,P⋆,Φ(sh) ≤ H . Combining (E.33) and (E.34), we have that 
VT̃h(·|sh,πh(sh)) 
[ V π h+1,P⋆,Φ 
] ≤ ET̃h(·|sh,πh(sh)) 
[( V π h+1,P⋆,Φ 
)2]− (V π h,P⋆,Φ 
)2 (sh) + 2H, 
which further implies that 
E(sh,ah)∼(T̃ ,π) 
[ VT̃h(·|sh,ah) 
[ V π h+1,P⋆,Φ 
]] = Esh∼(T̃ ,π) 
[ VT̃h(·|sh,πh(sh)) 
[ V π h+1,P⋆,Φ 
]] ≤ Esh∼(T̃ ,π) 
[ ET̃h(·|sh,πh(sh)) 
[( V π h+1,P⋆,Φ 
)2]− (V π h,P⋆,Φ 
)2 + 2H 
] = Esh+1∼(T̃ ,π) 
[( V π h+1,P⋆,Φ 
)2]− Esh∼(T̃ ,π) 
[( V π h,P⋆,Φ 
)2] + 2H. 
Taking summation over h ∈ [H] gives that 
E(sh,ah)∼(T̃ ,π),h∈[H] 
[ H∑ 
h=1 
VT̃h(·|sh,ah) 
[ V π h+1,P⋆,Φ 
]] ≤ 2H ·H = 2H ·min 
{ H, ρ−1 
} , 
which concludes the proof of Lemma E.6. 
E.8 Other Technical Lemmas 
Before presenting all lemmas, we recall that the typical event E is defined as 
E = 
 ∣∣∣∣ (EP⋆ 
h (·|s,a) − EP̂k h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
∣∣∣P ⋆ h (s 
′|s, a)− P̂h(s ′|s, a) 
∣∣∣ ≤ √√√√min 
{ P ⋆ h (s 
′|s, a), P̂ k h (s 
′|s, a) } · c1ι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
, 
∀(s, a, s′, h, k) ∈ S ×A× S × [H]× [K], ∀η ∈ N1/(S √ K) 
( [0, H] 
), (E.35) 
where ι = log(S3AH2K3/2/δ), c1, c2 > 0 are two absolute constants, N1/S √ K([0, H]) denotes an 
1/S √ K-cover of the interval [0, H]. where c1, c2 > 0 are two absolute constants, N1/S 
√ K([0, H]) 
denotes an 1/S √ K-cover of the interval [0, H]. 
39
E.8.1 Concentration Inequalities 
Lemma E.7 (Bernstein bound for TV robust sets and the optimal robust value function). Under event E in (E.35), it holds that∣∣∣∣EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ). 
Proof of Lemma E.7. By our definition of the operator EPρ(s,a;P̂k h )[V 
⋆ h+1,P⋆,Φ] in (4.1), we can arrive 
that ∣∣∣∣EPρ(s,a;P̂k h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ = 
∣∣∣∣∣ sup η∈[0,H] 
{ − EP̂k 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] + ( 1− ρ 
2 
) · η } 
− sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] + ( 1− ρ 
2 
) · η }∣∣∣∣∣ 
≤ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } , (E.36) 
Now according to the first inequality of event E , we have that∣∣∣∣ (EP⋆ h (·|s,a) − EP̂k 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
for any η ∈ N1/(S √ K)([0, H]). Here the second inequality is because Var[(a −X)+] ≤ Var[X]. 
Therefore, by a covering argument, for any η ∈ [0, H], it holds that∣∣∣∣ (EP⋆ h (·|s,a) − EP̂k 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
This finishes the proof of Lemma E.7. 
Lemma E.8 (Bernstein bound for TV robust sets and the robust value function of πk). Under event E in (E.35), suppose that the optimism and pessimism (E.14) holds at (h+ 1, k), then it holds that∣∣∣∣EPρ(s,a;P̂k 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c′2 are absolute constants. 
40
Proof of Lemma E.8. By our definition of the operator EPρ(s,a;P )[V πk 
h+1,P⋆,Φ] in (4.1), we can arrive that,∣∣∣∣EPρ(s,a;P̂k 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ = 
∣∣∣∣∣ sup η∈[0,H] 
{ − EP̂k 
h (·|s,a) 
[( η − V πk 
h+1,P⋆,Φ 
) + 
] + ( 1− ρ 
2 
) · η } 
− sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V πk 
h+1,P⋆,Φ 
) + 
] + ( 1− ρ 
2 
) · η }∣∣∣∣∣ 
≤ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V πk 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
≤ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
︸ ︷︷ ︸ Term (i) 
+ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V πk 
h+1,P⋆,Φ 
) + − ( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
︸ ︷︷ ︸ Term (ii) 
. 
We deal with Term (i) and Term (ii) respectively. For Term (i), this is exactly the same as the right hand side of (E.36). Therefore, applying the same argument as Lemma E.7 gives the following upper bound, 
Term (i) ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K . (E.37) 
For Term (ii), we first apply the second inequality of event E to obtain that, 
Term (ii) (E.38) 
≤ sup η∈[0,H] 
{∑ s′∈S 
(√ P̂ k h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
) 
· ∣∣∣(η − V πk 
h+1,P⋆,Φ(s ′) ) + − ( η − V ⋆ 
h+1,P⋆,Φ(s ′) ) + 
∣∣∣}. By the assumption that (E.14) holds at (h+ 1, k), we can upper bound the absolute value above by∣∣∣(η − V πk 
h+1,P⋆,Φ(s ′) ) + − ( η − V ⋆ 
h+1,P⋆,Φ(s ′) ) + 
∣∣∣ ≤ ∣∣∣V πk 
h+1,P⋆,Φ(s ′)− V ⋆ 
h+1,P⋆,Φ(s ′) ∣∣∣ 
≤ V k 
h+1(s ′)− V k 
h+1(s ′). (E.39) 
where the first inequality is due to the 1-Lipschitz continuity of ψη(x) = (η − x)+, and the second inequality is due to (E.14). Thus combining (E.38) and (E.39), we know that 
Term (ii) ≤ ∑ s′∈S 
√ P̂ k h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
 · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) . (E.40) 
Now following the argument first identified by Azar et al. (2017), we proceed to upper bound (E.40) as 
Term (ii) ≤ ∑ s′∈S 
( P̂ k h (s 
′|s, a) H 
+ c1Hι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
) · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) 
41
≤ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
, (E.41) 
where c′2 > 0 is another absolute constant. The first inequality is by √ ab ≤ a + b and the 
second inequality is due to V k 
h+1, V k h+1 ∈ [0, H]. Finally, combining (E.37) and (E.41), we prove 
Lemma E.8. 
Lemma E.9 (Bernstein bounds for TV robust sets and optimistic and pessimistic robust value estimators). Under event E in (E.35), suppose that the optimism and pessimism (E.14) holds at (h+ 1, k), it holds that 
max 
{ ∣∣∣EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
]∣∣∣ , ∣∣∣EPρ(s,a;P̂k h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
]∣∣∣ } 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c′2 are absolute constants. 
Proof of Lemma E.9. This follows from the same proof as Lemma E.8 and is thus omitted. 
Lemma E.10 (Non-robust concentration). Under event E in (E.35), suppose that the optimism and pessimism (E.14) holds at (h+ 1, k), then it holds that∣∣∣∣ (EP̂k 
h (·|s,a) − EP⋆ h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ 1 
H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′2H 2Sι 
Nk h (s, a) ∨ 1 
. 
where ι = log(S2AH2K3/2/δ) and c′2 is an absolute constant. 
Proof of Lemma E.10. According to the second inequality of event E , we have that∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ ∑ s′∈S 
(√ P ⋆ h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
) · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) , 
where we also apply (E.14) that V k 
h+1(s ′) ≥ V k 
h+1(s ′). Now using the same argument as (E.41) in 
the proof of Lemma E.8, we can arrive at∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ 
EP⋆ h (·|s,a) 
[ V 
k 
h+1(s ′)− V k 
h+1(s ′) ] 
H + 
c′2H 2Sι 
Nk h (s, a) ∨ 1 
, 
which finishes the proof of Lemma E.10. 
E.8.2 Variance Analysis 
Lemma E.11 (Variance analysis 1). Suppose that the optimism and pessimism (E.14) holds at (h+ 1, k), then the following inequality holds,∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . 
42
Proof of Lemma E.11. Directly consider that the left hand side can be upper bounded by the following, ∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 
∣∣∣∣∣EP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
)2 /4 
] − EP̂k 
h (·|s,a) 
[( V ⋆ h+1,P⋆,Φ 
)2]∣∣∣∣∣ + 
∣∣∣∣ (EP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ])2 
− ( EP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
])2 ∣∣∣∣. (E.42) 
Since all of V k 
h+1, V k h+1, V 
⋆ h+1,P⋆,Φ ∈ [0, H] (by the correctness of (E.14) and the definitions of 
V k 
h+1, V k h+1), we can further upper bound the right hand side of (E.42) as∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP̂k 
h (·|s,a) 
[∣∣∣(V k 
h+1 + V k h+1 
) /2− V ⋆ 
h+1,P⋆,Φ 
∣∣∣] ≤ 4H · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] , 
where the last inequality is due to the correctness of (E.14) at (h+1, k). This proves Lemma E.11. 
Lemma E.12 (Variance analysis 2). Under event E in (E.35), suppose that optimism and pessimism (E.14) holds at (h+ 1, k), then it holds that∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + c′2H 
4Sι 
Nk h (s, a) 
+ 1. 
Proof of Lemma E.12. We first relate the variance on P̂ k h to the variance on P ⋆ 
h . Specifically, we have∣∣∣∣VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ]∣∣∣∣ 
= 
∣∣∣∣∣∣EP̂k h (·|s,a) 
[(( V 
k 
h+1 + V k h+1 
) /2− EP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ])2 
] ∣∣∣∣∣∣ + 
∣∣∣∣∣∣EP⋆ h (·|s,a) 
[(( V 
k 
h+1 + V k h+1 
) /2− EP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ])2 
] ∣∣∣∣∣∣.(E.43) 
Since (V k 
h+1 + V k h+1)/2 ∈ [0, H], we can further upper bound (E.43) by∣∣∣∣VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ]∣∣∣∣ 
≤ H2 · ∑ s′∈S 
∣∣∣P ⋆ h (s 
′|s, a)− P̂h(s ′|s, a) 
∣∣∣ ≤ H2 · 
∑ s′∈S 
(√ P ⋆ h (·|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
) 
≤ H2 · 
(√ c1Sι 
Nk h (s, a) ∨ 1 
+ c2Sι 
Nk h (s, a) ∨ 1 
) 
≤ 1 + c′2H 
4Sι 
Nk h (s, a) ∨ 1 
, (E.44) 
43
where the second inequality is by the second inequality in event E , the third inequality is by Cauchy-Schwartz inequality and the probability distribution sums up to 1, and the last inequality is from√ ab ≤ a+ b. Thus by (E.44), we can bound our target as∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ ∣∣∣∣VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ + 
c′2H 4Sι 
Nk h (s, a) ∨ 1 
+ 1. (E.45) 
Now by the same proof of Lemma E.11, using the correctness of (E.14) at (h+ 1, k), we can show that ∣∣∣∣VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . (E.46) 
Combining (E.45) and (E.46), we can finish the proof of Lemma E.12. 
E.8.3 Other Auxiliary Lemmas 
Lemma E.13 (Lemma 7.5 in Agarwal et al. (2019)). For the sequences of {skh, akh} H,K h,k=1, it holds 
that K∑ 
k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ c ·HSA log(K). 
where c > 0 is an absolute constant. 
Proof of Lemma E.13. See Lemma 7.5 in Agarwal et al. (2019) for a detailed proof. 
F Proofs for Extensions in Section B.4.2 
In this section, we prove the theoretical results in Section B.4.2. 
F.1 Proof of Corollary B.5 
Proof of Corollary B.5. We consider applying Algorithm 1 on the auxiliary S×A-rectangular RMDP with a TV robust set M̃ (see Section B.4.2) which satisfies the vanishing minimal value assumption (Assumption 4.1). Suppose the algorithm outputs π̃1, · · · , π̃K for the K episodes. Then Theorem 4.3 shows that by a proper choice of the hyperparameters, with probability at least 1− δ 
RegretΦ̃(K) = 
K∑ k=1 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1)− V π̃k 
1,P̃⋆,Φ̃ (s1) 
≤ O (√ 
min { H, ρ−1 
} H2(S + 1)AKι′ 
) , . (F.1) 
where ι′ = log2(SAHK/δ) and ρ = 2 − 2ρ′ ∈ [0, 1). In the sequel, we prove that for any policy π̃ of M̃ and its induced policy π̃S of Mγ , their robust value functions coincide at the initial state s1 ∈ S, that is, 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = V π̃S 1,P⋆,Φ′(s1), 
where V π̃ 1,P̃⋆,Φ̃ 
is the robust value function of π̃ in M̃ = (S̃,A, H, P̃ ⋆, R̃, Φ̃), and V π̃S 1,P⋆,Φ′ is the 
robust value function of π̃S in Mγ = (S,A, H, P ⋆, Rγ ,Φ ′). To this end, we actually prove a 
stronger result that for any step h ∈ [H], it holds that 
(ρ′)h−1 · V π̃ h,P̃⋆,Φ̃ 
(s) = V π̃S h,P⋆,Φ′(s), ∀s ∈ S. (F.2) 
44
We prove (F.2) by induction. For step H , by robust Bellman equation, we have that, for any (s, a) ∈ S ×A, 
(ρ′)H−1 ·Qπ̃ H,P̃⋆,Φ̃ 
(s, a) = (ρ′)H−1 · ( γ 
ρ′ 
)H−1 
·RH(s, a) = Rγ,H(s, a) = Qπ̃S H,P⋆,Φ′(s, a), 
and thus for any s ∈ S, 
(ρ′)H−1 · V π̃ h,P̃⋆,Φ̃ 
(s) = Eπ̃(·|s) 
[ (ρ′)H−1 ·Qπ̃ 
H,P̃⋆,Φ̃ (s, ·) 
] = Eπ̃S(·|s) 
[ Qπ̃S 
H,P⋆,Φ(s, ·) ] 
= V π̃S H,P⋆,Φ′(s). 
This proves (F.2) for step H . Suppose that (F.2) holds at some step h+ 1, that is, 
(ρ′)h · V π̃ h+1,P̃⋆,Φ̃ 
(s) = V π̃S h+1,P⋆,Φ′(s), ∀s ∈ S. (F.3) 
Then for step h, by robust Bellman equation and Proposition 4.2, we have that 
(ρ′)h−1 ·Qπ̃ h,P̃⋆,Φ̃ 
(s, a) = (ρ′)h−1 · ( γ 
ρ′ 
)H−1 
·Rh(s, a) + (ρ′)h−1 · EP̃ρ(s,a;P̃⋆ h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] = Rγ,h(s, a) + (ρ′)h−1 · ρ′ · EB̃ρ(s,a;P̃⋆ 
h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] , (F.4) 
where the last equality utilizes Proposition 4.2 since mins∈S̃ V π̃ h+1,P̃⋆,Φ̃ 
(s) = 0, and we adopt the notation 
B̃ρ(s, a; P̃ ⋆ h ) = 
{ P̃ (·) ∈ ∆(S̃) : sup 
s′∈S̃ 
P̃ (s′) 
P̃ ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} . 
Notice that by the definition (B.3), we know for (s, a) ∈ S ×A it holds that P̃ ⋆ h (·|s, a) = P ⋆ 
h (·|s, a) which is supported on S. Therefore, we can equivalently write 
B̃ρ(s, a; P̃ ⋆ h ) = 
{ P̃ (·) ∈ ∆(S̃) : sup 
s′∈S 
P̃ (s′) 
P̃ ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} 
= 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} = Bρ(s, a;P 
⋆ h ). (F.5) 
Thus by (F.4) and (F.5) and the induction hypothesis (F.3), we obtain that for any (s, a) ∈ S ×A, 
(ρ′)h−1 ·Qπ̃ h,P̃⋆,Φ̃ 
(s, a) = Rγ,h(s, a) + (ρ′)h · EBρ(s,a;P⋆ h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] = Rγ,h(s, a) + EBρ(s,a;P⋆ 
h ) 
[ V π̃S h+1,P⋆,Φ 
] = Qπ̃S 
h,P⋆,Φ(s, a), 
where the second equality applies (F.3) and the last equality is from robust Bellman equation. Consequently, for any s ∈ S, we have that 
(ρ′)h−1 · V π̃ h,P̃⋆,Φ̃ 
(s) = Eπ̃(·|s) 
[ (ρ′)h−1 ·Qπ̃ 
h,P̃⋆,Φ̃ (s, ·) 
] = Eπ̃S(·|s) 
[ Qπ̃S 
h,P⋆,Φ(s, ·) ] 
= V π̃S h,P⋆,Φ′(s), 
which finishes the induction argument, proving our claim (F.2). By taking h = 1, we can derive that for any initial state s1 ∈ S, it holds that for any policy π̃ of M̃ and its induced policy π̃S of Mγ , 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = V π̃S 1,P⋆,Φ′(s1). 
45
This indicates two facts: the first is that 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = max π 
V π 1,P⋆,Φ′(s1), (F.6) 
where on the right hand side the maximization is with respect to all the policies for Mγ ; the second is that 
V π̃k 
1,P̃⋆,Φ̃ (s1) = V 
π̃k S 
1,P⋆,Φ′(s1), (F.7) 
for each k ∈ [K], where recall that π̃k is the policy output by Algorithm 1 for episode k. As a result, the k policies {π̃k 
S}Kk=1 of Mγ during interactive data collection satisfies with probability at least 1− δ, 
RegretΦ′(K) = 
K∑ k=1 
max π 
V π 1,P⋆,Φ′(s1)− V 
π̃k S 
1,P⋆,Φ′(s1) 
= 
K∑ k=1 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1)− V π̃k 
1,P̃⋆,Φ̃ (s1) 
≤ O (√ 
min { H, (2− 2ρ′)−1 
} H2SAKι′ 
) , 
where in the second equality we apply the facts (F.6) and (F.7), and the last inequality follows from (F.1) and that ρ = 2− 2ρ′. This completes the proof of Corollary B.5. 
46
NeurIPS Paper Checklist 
The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit. 
Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist: 
 You should answer [Yes] , [No] , or [NA] . 
 [NA] means either that the question is Not Applicable for that particular paper or the 
relevant information is Not Available. 
 Please provide a short (1–2 sentence) justification right after your answer (even for NA). 
The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper. 
The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While "[Yes] " is generally preferable to "[No] ", it is perfectly acceptable to answer "[No] " provided a proper justification is given (e.g., "error bars are not reported because it would be too computationally expensive" or "we were unable to find the license for the dataset we used"). In general, answering "[No] " or "[NA] " is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found. 
IMPORTANT, please: 
 Delete this instruction block, but keep the section heading “NeurIPS paper checklist", 
 Keep the checklist subsection headings, questions/answers and guidelines below. 
 Do not modify the questions and only use the provided macros for your answers. 
1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Sections 2, 3, 4. Guidelines: 
 The answer NA means that the abstract and introduction do not include the claims made in the paper. 
 The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. 
 The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. 
 It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 
2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: Section B.5 
47
Guidelines: 
 The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. 
 The authors are encouraged to create a separate "Limitations" section in their paper. 
 The paper should point out any strong assumptions and how robust the results are to 
violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. 
 The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. 
 The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. 
 The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. 
 If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. 
 While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 
3. Theory Assumptions and Proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? 
Answer: [Yes] 
Justification: Sections 3, 4, and the Appendix. 
Guidelines: 
 The answer NA means that the paper does not include theoretical results. 
 All the theorems, formulas, and proofs in the paper should be numbered and cross-
referenced. 
 All assumptions should be clearly stated or referenced in the statement of any theorems. 
 The proofs can either appear in the main paper or the supplemental material, but if 
they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. 
 Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. 
 Theorems and Lemmas that the proof relies upon should be properly referenced. 
4. Experimental Result Reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? 
Answer: [NA] 
Justification: This is a theoretical work and we do not conduct experiments. 
Guidelines: 
 The answer NA means that the paper does not include experiments. 
48
 If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. 
 If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. 
 Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. 
 While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how 
to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe 
the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should 
either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). 
(d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 
5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? 
Answer: [NA] 
Justification: This is a theoretical work and we do not conduct experiments. 
Guidelines: 
 The answer NA means that paper does not include experiments requiring code. 
 Please see the NeurIPS code and data submission guidelines (https://nips.cc/ public/guides/CodeSubmissionPolicy) for more details. 
 While we encourage the release of code and data, we understand that this might not be possible, so “No” is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark). 
 The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines (https: //nips.cc/public/guides/CodeSubmissionPolicy) for more details. 
 The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc. 
 The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why. 
 At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable). 
49
 Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted. 
6. Experimental Setting/Details Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results? 
Answer: [NA] 
Justification: This is a theoretical work and we do not conduct experiments. 
Guidelines: 
 The answer NA means that the paper does not include experiments. 
 The experimental setting should be presented in the core of the paper to a level of detail 
that is necessary to appreciate the results and make sense of them. 
 The full details can be provided either with the code, in appendix, or as supplemental 
material. 
7. Experiment Statistical Significance Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments? 
Answer: [NA] 
Justification: This is a theoretical work and we do not conduct experiments. 
Guidelines: 
 The answer NA means that the paper does not include experiments. 
 The authors should answer "Yes" if the results are accompanied by error bars, confi-
dence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper. 
 The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions). 
 The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.) 
 The assumptions made should be given (e.g., Normally distributed errors). 
 It should be clear whether the error bar is the standard deviation or the standard error 
of the mean. 
 It is OK to report 1-sigma error bars, but one should state it. The authors should 
preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified. 
 For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates). 
 If error bars are reported in tables or plots, The authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text. 
8. Experiments Compute Resources Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments? 
Answer: [NA] 
Justification: This is a theoretical work and we do not conduct experiments. 
Guidelines: 
 The answer NA means that the paper does not include experiments. 
 The paper should indicate the type of compute workers CPU or GPU, internal cluster, 
or cloud provider, including relevant memory and storage. 
50
 The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute. 
 The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper). 
9. Code Of Ethics Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines? Answer: [Yes] Justification: The research in this work conforms with the NeurIPS Code of Ethics. Guidelines: 
 The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics. 
 If the authors answer No, they should explain the special circumstances that require a 
deviation from the Code of Ethics. 
 The authors should make sure to preserve anonymity (e.g., if there is a special consid-
eration due to laws or regulations in their jurisdiction). 10. Broader Impacts 
Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed? Answer: [NA] Justification: There is no societal impact of the work performed. Guidelines: 
 The answer NA means that there is no societal impact of the work performed. 
 If the authors answer NA or No, they should explain why their work has no societal 
impact or why the paper does not address societal impact. 
 Examples of negative societal impacts include potential malicious or unintended uses 
(e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations. 
 The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster. 
 The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology. 
 If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML). 
11. Safeguards Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)? Answer: [NA] Justification: The paper poses no such risks. Guidelines: 
 The answer NA means that the paper poses no such risks. 
51
 Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters. 
 Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images. 
 We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort. 
12. Licenses for existing assets Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected? 
Answer: [NA] 
Justification: The paper does not use existing assets. 
Guidelines: 
 The answer NA means that the paper does not use existing assets. 
 The authors should cite the original paper that produced the code package or dataset. 
 The authors should state which version of the asset is used and, if possible, include a 
URL. 
 The name of the license (e.g., CC-BY 4.0) should be included for each asset. 
 For scraped data from a particular source (e.g., website), the copyright and terms of 
service of that source should be provided. 
 If assets are released, the license, copyright information, and terms of use in the 
package should be provided. For popular datasets, paperswithcode.com/datasets has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset. 
 For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided. 
 If this information is not available online, the authors are encouraged to reach out to the asset’s creators. 
13. New Assets Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets? 
Answer: [NA] 
Justification: The paper does not release new assets. 
Guidelines: 
 The answer NA means that the paper does not release new assets. 
 Researchers should communicate the details of the dataset/code/model as part of their 
submissions via structured templates. This includes details about training, license, limitations, etc. 
 The paper should discuss whether and how consent was obtained from people whose asset is used. 
 At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file. 
14. Crowdsourcing and Research with Human Subjects Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)? 
Answer: [NA] 
Justification: The paper does not involve crowdsourcing nor research with human subjects. 
52
Guidelines: 
 The answer NA means that the paper does not involve crowdsourcing nor research with 
human subjects. 
 Including this information in the supplemental material is fine, but if the main contribu-
tion of the paper involves human subjects, then as much detail as possible should be included in the main paper. 
 According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector. 
15. Institutional Review Board (IRB) Approvals or Equivalent for Research with Human Subjects Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained? Answer: [NA] Justification: The paper does not involve crowdsourcing nor research with human subjects. Guidelines: 
 The answer NA means that the paper does not involve crowdsourcing nor research with human subjects. 
 Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper. 
 We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution. 
 For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review. 
53