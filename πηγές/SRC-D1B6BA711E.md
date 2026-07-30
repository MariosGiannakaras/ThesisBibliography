> Source: https://arxiv.org/pdf/2209.13841

Online Policy Optimization for Robust MDP 
Jing Dong ∗ 
jingdong@link.cuhk.edu.cn 
Jingwei Li † 
ljw22@mails.tsinghua.edu.cn 
Baoxiang Wang ∗ 
bxiangwang@cuhk.edu.cn 
Jingzhao Zhang † 
jingzhaoz@mail.tsinghua.edu.cn 
Abstract 
Reinforcement learning (RL) has exceeded human performance in many synthetic settings such as video games and Go. However, real-world deployment of end-to-end RL models is less common, as RL models can be very sensitive to slight perturbation of the environment. The robust Markov decision process (MDP) framework—in which the transition probabilities belong to an uncertainty set around a nominal model—provides one way to develop robust models. While previous analysis shows RL algorithms are effective assuming access to a generative model, it remains unclear whether RL can be efficient under a more realistic online setting, which requires a careful balance between exploration and exploitation. In this work, we consider online robust MDP by interacting with an unknown nominal system. We propose a robust optimistic policy optimization algorithm that is provably efficient. To address the additional uncertainty caused by an adversarial environment, our model features a new optimistic update rule derived via Fenchel conjugates. Our analysis establishes the first regret bound for online robust MDPs. 
1 Introduction 
The rapid progress of reinforcement learning (RL) algorithms enables trained agents to navigate around complicated environments and solve complex tasks. The standard reinforcement learning methods, however, may fail catastrophically in another environment, even if the two environments only differ slightly in dynamics [Farebrother et al., 2018, Packer et al., 2018, Cobbe et al., 2019, Song et al., 2019, Raileanu and Fergus, 2021]. In practical applications, such mismatch of environment dynamics are common and can be caused by a number of reasons, e.g., model deviation due to incomplete data, unexpected perturbation and possible adversarial attacks. Part of the sensitivity of standard RL algorithms stems from the formulation of the underlying Markov decision process (MDP). In a sequence of interactions, MDP assumes the dynamic to be unchanged, and the trained agent to be tested on the same dynamic thereafter. 
To model the potential mismatch between system dynamics, the framework of robust MDP is introduced to account for the uncertainty of the parameters of the MDP [Satia and Lave Jr, 1973, White III and Eldeib, 1994, Nilim and El Ghaoui, 2005, Iyengar, 2005]. Under this framework, the dynamic of an MDP is no longer fixed but can come from some uncertainty set, such as the 
Authors are listed in alphabetical order. ∗The Chinese University of Hong Kong, Shenzhen †Tsinghua University 
1 
 
 
 
 
 
 
 
 
 
 
rectangular uncertainty set, centered around a nominal transition kernel. The agent sequentially interacts with the nominal transition kernel to learn a policy, which is then evaluated on the worst possible transition from the uncertainty set. Therefore, instead of searching for a policy that may only perform well on the nominal transition kernel, the objective is to find the worst-case bestperforming policy. This can be viewed as a dynamical zero-sum game, where the RL agent tries to choose the best policy while nature imposes the worst possible dynamics. Intrinsically, solving the robust MDPs involves solving a max-min problem, which is known to be challenging for efficient algorithm designs. 
More specifically, if a generative model (also known as a simulator) of the environment or a suitable offline dataset is available, one could obtain a ε-optimal robust policy with Õ(ε−2) samples under a rectangular uncertainty set [Qi and Liao, 2020, Panaganti and Kalathil, 2022, Wang and Zou, 2022, Ma et al., 2022]. Yet the presence of a generative model is stringent to fulfill for real applications. In a more practical online setting, the agent sequentially interacts with the environment and tackles the exploration-exploitation challenge as it balances between exploring the state space and exploiting the high-reward actions. In the robust MDP setting, previous sample complexity results cannot directly imply a sublinear regret in general Dann et al. [2017] and so far no asymptotic result is available. A natural question then arises: 
Can we design a robust RL algorithm that attains sublinear regret under robust MDP with rectangular uncertainty set? 
In this paper, we answer the above question affirmatively and propose the first policy optimization algorithm for robust MDP under a rectangular uncertainty set. One of the challenges for deriving a regret guarantee for robust MDP stems from its adversarial nature. As the transition dynamic can be picked adversarially from a predefined set, the optimal policy is in general randomized [Wiesemann et al., 2013]. This is in contrast with conventional MDPs, where there always exists a deterministic optimal policy, which can be found with value-based methods and a greedy policy (e.g. UCB-VI algorithms). Bearing this observation, we resort to policy optimization (PO)-based methods, which directly optimize a stochastic policy in an incremental way. 
With a stochastic policy, our algorithm explores robust MDPs in an optimistic manner. To achieve this robustly, we propose a carefully designed bonus function via the dual conjugate of the robust bellman equation. This quantifies both the uncertainty stemming from the limited historical data and the uncertainty of the MDP dynamic. In the episodic setting of robust MDPs, we show that our algorithm attains sublinear regret O( 
√ K) for both (s, a) and s-rectangular uncertainty 
set, where K is the number of episodes. In the case where the uncertainty set contains only the nominal transition model, our results recover the previous regret upper bound of non-robust policy optimization [Shani et al., 2020]. Our result achieves the first provably efficient regret bound in the online robust MDP problem, as shown in Table 1. We further validated our algorithm with experiments. 
2 Related work 
RL with robust MDP Different from conventional MDPs, robust MDPs allow the transition kernel to take values from an uncertainty set. The objective in robust MDPs is to learn an optimal robust policy that maximizes the worst-case value function. When the exact uncertainty set is known, this can be solved through dynamic programming methods [Iyengar, 2005, Nilim and 
2
Table 1: Comparisons of previous results and our results, where S,A are the size of the state space and action space, H is the length of the horizon, K is the number of episodes, ρ is the radius of the uncertainty set and ε is the level of suboptimality. We shorthand ι = log(SAH2K3/2(1 + ρ)). The regret upper bound by Panaganti and Kalathil [2022] are obtained through converting their sample complexity results and the sample complexity result for our work is converted through our regret bound. We use “GM” to denote the requirement of a generative model and “for PE” to denote that the result is only for robust policy evaluation (estimating a robust value function for a fixed policy). The reference to the previous works are [A]: Panaganti and Kalathil [2022], [B]: Wang and Zou [2021], [C]: Badrinath and Kalathil [2021], [D]: Yang et al. [2021]. 
Algorithm Requires Rectangular Regret Sample Complexity 
[A] Value based 
GM (s, a) NA O ( H4S2A ε2 
) [B] 
Value based 
- (s, a) NA Asymptotic 
[C] Policy based 
- (s, a) NA Asymptotic 
[D] Value based 
GM (s, a) NA Õ 
( H2S2A(2+ρ)2 
ρ2ε2 
) for PE 
s NA Õ ( H2S2A2(2+ρ)2 
ρ2ε2 
) for PE 
Ours Policy based 
-(s, a) O 
( SH2 
√ AKι 
) O ( H4S2Aι 
ε2 
) s O 
( SA2H2 
√ Kι ) 
O ( H4S2A4ι 
ε2 
) El Ghaoui, 2005, Mannor et al., 2012]. Yet knowing the exact uncertainty set is a rather stringent requirement for most real applications. If one has access to a generative model, several model-based reinforcement learning methods are proven to be statistically efficient. With the different characterization of the uncertainty set, these methods can enjoy a sample complexity of O(1/ε2) for an ε-optimal robust value function [Panaganti and Kalathil, 2022, Yang et al., 2021]. Similar results can also be achieved if an offline dataset is present, for which previous works Qi and Liao [2020], Zhou et al. [2021], Kallus et al. [2022], Ma et al. [2022] show the O(1/ε2) sample complexity for an ε-optimal policy. 
In the case of online RL, the only results available are asymptotic. In the case of discounted MDPs, Wang and Zou [2021], Badrinath and Kalathil [2021] study the policy gradient method and show an O(ε−3) convergence rate for an alternative learning objective (a smoothed variant), which could be equivalent to the original policy gradient objective in an asymptotic regime. These results in sample complexity and asymptotic regimes in general cannot imply sublinear regret in robust MDPs [Dann et al., 2017]. 
RL with adversarial MDP Another line of works characterizes the uncertainty of the environment through the adversarial MDP formulation, where the environmental parameters can be adversarially chosen without restrictions. This problem is proved to be NP-hard to obtain a low regret [Even-Dar et al., 2004]. Several works study the variant where the adversarial could only modify the reward function, while the transition dynamics of the MDP remain unchanged. In this case, it is possible to obtain policy-based algorithms that are efficient with a sublinear regret [Rosenberg and Mansour, 2019, Jin and Luo, 2020, Jin et al., 2020, Shani et al., 2020, Cai et al., 2020]. On a separate vein, it investigates the setting where the transition is only allowed to be 
3
adversarially chosen for C out of the K total episodes. A regret of O(C2 + √ K) are established 
thereafter [Lykouris et al., 2021, Chen et al., 2021b, Zhang et al., 2022]. 
Non-robust policy optimization The problem of policy optimization has been extensively investigated under non-robust MDPs [Neu et al., 2010, Cai et al., 2020, Shani et al., 2020, Wu et al., 2022, Chen et al., 2021a]. The proposed methods are proved to achieve sublinear regret. The methods are also closely related to empirically successful policy optimization algorithms in RL, such as PPO Schulman et al. [2017] and TRPO Schulman et al. [2015]. 
3 Robust MDP and uncertainty sets 
In this section, we describe the formal setup of robust MDP. We start with defining some notations. 
Robust Markov decision process We consider an episodic finite horizon robust MDP, which can denoted by a tuple M = 〈S,A, H, {P}Hh=1, {r}Hh=1〉. Here S is the state space, A is the action space, {r}Hh=1 is the time-dependent reward function, and H is the length of each episode. Instead of a fixed step of time-dependent uncertainty kernels, the transitions of the robust MDP is governed by kernels that are within a time-dependent uncertainty set {P}Hh=1, i .e., time-dependent transition Ph ∈ Ph ⊆ ∆S at time h. 
The uncertainty set P is constructed around a nominal transition kernel Ph = {P oh}, and all transition dynamics within the set are close to the nominal kernel with a distance metric of one’s choice. Different from an episodic finite-horizon non-robust MDP, the transition kernel P may not only be time-dependent but may also be chosen (even adversarially) from a specified time-dependent uncertainty set P. We consider the case where the rewards are stochastic. This is, on state-action (s, a) at time h, the immediate reward is Rh(s, a) ∈ [0, 1], which is drawn i.i.d from a distribution with expectation rh(s, a). With the described setup of robust MDPs, we now define the policy and its associated value. 
Policy and robust value function A time-dependent policy π is defined as π = {πh}Hh=1, where each πh is a function from S to the probability simplex over actions, ∆(A). If the transition kernel is fixed to be P , the performance of a policy π starting from state s at time h can be measured by its value function, which is defined as 
V π,P h (s) = Eπ,P 
[ H∑ 
h′=h 
rh′(sh′ , ah′) | sh = s 
] . 
In robust MDP, the robust value function instead measures the performance of π under the worst possible choice of transition P within the uncertainty set. Specifically, the value and the Q-value function of a policy given the state action pair (s, a) at step h are defined as 
V π h (s) = min 
{Ph}∈{Ph} V π,{P} h (s) , 
Qπh(s, a) = min {Ph}∈{Ph} 
Eπ,{P} 
[ H∑ 
h′=h 
rh(sh′ , ah′) | (sh, ah) = (s, a) 
] . 
4
The optimal value function is defined to be the best possible value attained by a policy 
V ∗h (s) = max π 
V π h (s) = max 
π min 
{Ph}∈{Ph} V π,{P} h (s) . 
The optimal policy is then defined to be the policy that attains the optimal value. 
Robust Bellman equation Similar to non-robust MDP, robust MDP has the following robust bellman equation, which characterizes a relation to the robust value function. 
Qπh(s, a) = r(s, a) + σPh(V π h+1)(s, a) , V π 
h (s) = 〈Qπh(s, ·), πh(·, s)〉 , 
where 
σPh(V π h+1)(s, a) = min 
Ph∈Ph Ph(· | s, a)V π 
h+1 , Ph(· | s, a)V = ∑ s′∈S 
Ph(s′ | s, a)V (s′) . (1) 
Without additional assumptions on the uncertainty set, the optimal policy and value of the robust MDP are in general NP-hard to solve [Wiesemann et al., 2013]. One of the most commonly assumptions that make solving optimal value feasible is the rectangular assumption [Iyengar, 2005, Wiesemann et al., 2013, Badrinath and Kalathil, 2021, Yang et al., 2021, Panaganti and Kalathil, 2022]. 
Rectangular uncertainty sets To limit the level of perturbations, we assume that the transition kernels is close to the nominal transition measured via `1 distance. We consider two cases. 
The (s, a)-rectangular assumption assumes that the uncertain transition kernel within the set takes value independently for each (s, a). We further use `1 distance to characterize the (s, a)-rectangular set around a nominal kernel with a specified level of uncertainty. 
Definition 3.1 ((s, a)-rectangular uncertainty set Iyengar [2005], Wiesemann et al. [2013]). For all time step h and with a given state-action pair (s, a), the (s, a)-rectangular uncertainty set Ph(s, a) is defined as 
Ph(s, a) = {‖Ph(· | s, a)− P oh(· | s, a)‖1 ≤ ρ, Ph(· | s, a) ∈ ∆(S)} , 
where P oh is the nominal transition kernel at h, P oh(· | s, a) > 0, ∀(s, a) ∈ S × A, ρ is the level of uncertainty. 
With the (s, a)-rectangular set, it is shown that there always exists an optimal policy that is deterministic Wiesemann et al. [2013]. 
One way to relax the (s, a)-rectangular assumption is to instead let the uncertain transition kernels within the set take value independent for each s only. This characterization is then more general and its solution gives a stronger robustness guarantee. 
Definition 3.2 (s-rectangular uncertainty set Wiesemann et al. [2013]). For all time step h and with a given state s, the s-rectangular uncertainty set Ph(s) is defined as 
Ph(s) = 
{∑ a∈A ‖Ph(· | s, a)− P oh(· | s, a)‖1 ≤ Aρ, Ph(· | s, ·) ∈ ∆(S)A 
} , 
where P oh is the nominal transition kernel at h, P oh(· | s, a) > 0, ∀(s, a) ∈ S × A, ρ is the level of uncertainty. 
5
Different from the (s, a)-rectangular assumption, which guarantees the existence of a deterministic optimal policy, the optimal policy under s-rectangular set may need to be randomized [Wiesemann et al., 2013]. We also remark that the requirement of P oh(· | s, a) > 0 is mostly for technical convenience. 
Equipped with the characterization of the uncertainty set, we now describe the learning protocols and the definition of regret under the robust MDP. 
Learning protocols and regret We consider a learning agent repeatedly interacts with the environment in an episodic manner, over K episodes. At the start of each episode, the learning agent picks a policy πk and interacts with the environment while executing πk. Without loss of generality, we assume the agents always start from a fixed initial state s. The performance of the learning agent is measured by the cumulative regret incurred over the K episodes. Under the robust MDP, the cumulative regret is defined to be the cumulative difference between the robust value of πk and the robust value of the optimal policy, 
Regret(K) = K∑ k=1 
V ∗1 (s0)− V πk 1 (s0) , 
where sk0 is the initial state. We highlight that the transition of the states in the learning process is specified by the nominal 
transition kernel {P oh}Hh=1, though the agent only has access to the nominal kernel in an online manner. We remark that if the agent is asked to interact with a potentially adversarially chosen transition, the learning problem is NP-hard Even-Dar et al. [2004]. 
One practical motivation for this formulation could be as follows. The policy provider only sees feedback from the nominal system, yet she aims to minimize the regret for clients who refuse to share additional deployment details for privacy purposes. 
4 Algorithm 
Before we introduce our algorithm, we first illustrate the importance of taking uncertainty into consideration. With the robust MDP, one of the most naive methods is to directly train a policy with the nominal transition model. However, the following proposition shows an optimal policy under the nominal policy can be arbitrarily bad in the worst-case transition (even worse than a random policy). 
Claim 4.1 (Suboptimality of non-robust optimal policy). There exists a robust MDP M = 〈S,A,P, r,H〉 with uncertainty set P of uncertainty radius ρ, such that the non-robust optimal policy is Ω(1)-suboptimal to the uniformly random policy. 
The proof of Proposition 4.1 is deferred to Appendix D. With the above-stated result, it implies the policy obtained with non-robust RL algorithms, can have arbitrarily bad performance when the dynamic mismatch from the nominal transition. Therefore, we present the following robust optimistic policy optimization 1 to avoid this undesired result. 
6
4.1 Robust optimistic policy optimization 
With the presence of the uncertainty set, the optimal policies may be all randomized [Wiesemann et al., 2013]. In such cases, value-based methods may be insufficient as they usually rely on a deterministic policy. We thus resort to optimistic policy optimization methods Shani et al. [2020], which directly learn a stochastic policy. 
Our algorithm performs policy optimization with empirical estimates and encourages exploration by adding a bonus to less explored states. However, we need to propose a new efficiently computable bonus that is robust to adversarial transitions. We achieve this via solving a suboptimization problem derived from Fenchel conjugate. We present Robust Optimistic Policy Opti-mization (ROPO) in Algorithm 1 and elaborate on its design components. 
To start, as our algorithm has no access to the actual reward and transition function, we use the following empirical estimator of the transition and reward: 
r̂kh(s, a) = 
∑k−1 k′=1R 
k′ h (s, a)I 
{ sk ′ h = s, ak 
′ h = a 
} Nk h (s, a) 
, 
P̂ o,kh (s, a) = 
∑k−1 k′=1 I 
{ sk ′ h = s, ak 
′ h = a, sk 
′ h+1 = s′ 
} Nk h (s, a) 
, (2) 
where Nk h (s, a) = max 
{∑k−1 k′=1 I 
{ sk ′ h = s, ak 
′ h = a 
} , 1 } 
. 
Challenges in Optimistic Robust Policy Evaluation In each episode, the algorithm estimates Q-values with an optimistic variant of the bellman equation. Specifically, to encourage exploration in the robust MDP, we add a bonus term bkh(s, a), which compensates for the lack of knowledge of the actual reward and transition model as well as the uncertainly set, with order 
bkh(s, a) = O 
( 1/ √ Nk h (s, a) 
) . 
Q̂kh(s, a) = min { r̂(s, a) + σP̂h(V̂ π 
h+1)(s) + bkh(s, a), H } . 
Intuitively, the bonus term bkh desires to characterize the optimism required for efficient exploration for both the estimation errors of P and the robustness of P . It is hard to control the two quantities in their primal form because of the coupling between them. We propose the following procedure to address the problem. 
Note that the key difference between our algorithm and standard policy optimization is that σP̂h(V̂ π 
h+1)(s) requires solving an inner minimization (1). Through relaxing the constraints with Lagrangian multiplier and Fenchel conjugates, under (s, a)-rectangular set, the inner minimization problem can be reduced to a one-dimensional unconstrained convex optimization problem on R (Lemma 4). 
sup η η − 
(η −min s V̂ πk h+1(s))+ 
2 ρ− 
∑ s′ 
P̂ oh(s′ | s, a) ( η − V̂ πk 
h+1(s ′) ) + . (3) 
The optimum of Equation (3) is then computed efficiently with bisection or sub-gradient methods. We note that while the dual form has been similarly used before under the presence of a generative 
7
model or with an offline dataset [Badrinath and Kalathil, 2021, Panaganti and Kalathil, 2022, Yang et al., 2021], it remains unclear whether it is effective for the online setting. 
Similarly, in the case of s-rectangular set, the inner minimization problem is equivalent to a A-dimensional convex optimization problem. 
sup η 
∑ a′ 
ηa′ − ∑ s′,a′ 
P̂ oh(s′ | s, a′) ( ηa′ − I{a′ = a}V πk 
h+1(s ′) ) + −min 
s′,a′ 
Aρ(ηa′ − I{a′ = a}V πk h+1(s 
′))+ 
2 . 
(4) 
This optimum in RA can be computed efficiently in Õ(A) iterations by methods like gradient descent. 
In addition to reducing computational complexity, the dual form (Equation (3) and Equation (4)) decouples the uncertainty in estimation error and in robustness, as ρ and P̂ oh are not in different terms. The exact form of bkh is presented in the Equation (5) and (6). 
Policy Improvement Step Using the optimistic Q-value obtained from policy evaluation, the algorithm improves the policy with a KL regularized online mirror descent step, 
πk+1 h ∈ arg min 
π β〈∇V̂ πk 
h , π〉 − πkh +DKL(π||πkh) , 
where β is the learning rate. Equivalently, the updated policy is given by the closed-form solution 
πk+1 h (a | s) = 
πkh exp(βQ̂πh(s, a))∑ a′ exp(βQ̂πh(s, a′)) 
. 
An important property of policy improvement is to use a fundamental inequality (7) of online mirror descent presented in [Shani et al., 2020]. We suspect that other online algorithms with sublinear regret could also be used in policy improvement. 
In the non-robust case, this improvement step is also shown to be theoretically efficient [Shani et al., 2020, Wu et al., 2022]. Many empirically successful policy optimization algorithms, such as PPO [Schulman et al., 2017] and TRPO Schulman et al. [2015], also take a similar approach to KL regularization for non-robust policy improvement. 
The proposed algorithm is summarized in Algorithm 1. 
5 Theoretical results 
We are now ready to analyze the theoretical results of our algorithm under the uncertainly set. 
5.1 Results under (s, a)-rectangular uncertainty set 
Equipped with Algorithm 1 and the bonus function described in Equation 5. We obtain the regret upper bound under (s, a)-rectangular uncertainty set described in the following Theorem. 
Theorem 1 (Regret under (s, a)-rectangular uncertainty set). With learning rate β = √ 
2 logA H2K 
and bonus term bkh as (5), with probability at least 1− δ, the regret incurred by Algorithm 1 over K episodes is bounded by 
Regret(K) = O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) . 
8
Algorithm 1 Robust Optimistic Policy Optimization (ROPO) 
Input: learning rate β, bonus function bkh. for k = 1, . . . ,K do 
Collect a trajectory of samples by executing πk. # Robust Policy Evaluation for h = H, . . . , 1 do 
for ∀(s, a) ∈ S ×A do Solve σP̂h(V̂ π 
h+1)(s, a) according to Equation (3) for (s, a)-rectangular set or Equation (4) for s-rectangular set. 
Q̂kh(s, a) = min { r̂(s, a) + σP̂h(V̂ π 
h+1)(s, a) + bkh(s, a), H } 
. 
end for for ∀s ∈ S do V̂ k h (s) = 
〈 Q̂kh(s, ·), πkh(· | s) 
〉 . 
end for end for # Policy Improvement for ∀h, s, a ∈ [H]× S ×A do 
πk+1 h (a | s) = 
πkh exp(−βQ̂πh(s,a))∑ a′ exp(−βQ̂πh(s,a′)) 
. 
end for Update empirical estimate r̂, P̂ with Equation (2). 
end for 
Remark 5.1. When ρ = 0, the problem reduces to non-robust reinforcement learning. In such 
case our regret upper bound is Õ ( H2S 
√ AK 
) , which is in the same order of policy optimization 
algorithms for the non-robust case Shani et al. [2020]. 
While we defer the detailed proof to the appendix A, we remark on the techniques used in our proof. 
The main challenge of deriving a robust regret is to quantify the uncertainty of the transition. In the non-robust case, this uncertainty is solely incurred by limited interaction with the environment. However, in the robust case, the uncertainty is caused by both the limited interaction and the uncertainty set. With the compound causes of uncertainty we choose not to directly use concentration inequality σP̂(s,a) 
(V )− σP(s,a) (V ) and instead resort to the dual form Equation (3). 
Notice that now the difference of σP̂(s,a) (V ) − σP(s,a) 
(V ) is only incurred by difference in the 
value of ∑ 
s′ P o h(s′ | s, a) 
( η − V̂ πk 
h+1(s ′) ) + 
. When η is bounded, we can use Hoeffding’s inequality to 
control it. We then investigate the range of possible optimal values of η and use an ε-net argument. Our algorithm and analysis techniques can also extend to other uncertainty sets, such as KL 
divergence constrained uncertainly set. We include the KL divergence result in Appendix C. 
5.2 Results under s-rectangular uncertainty set 
Beyond the (s, a)-rectangular uncertainty set, we also extends to s-rectangular uncertainty set (Definition 3.2). Recall that value-based methods do not extend to s-rectangular uncertainty set 
9
as there might not exist a deterministic optimal policy. 
Theorem 2 (Regret under s-rectangular uncertainty set). With learning rate β = √ 
2 logA H2K 
and 
bonus term bkh as (6), with probability at least 1− δ, the regret of Algorithm 1 is bounded by 
Regret(K) = O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) . 
Remark 5.2. When ρ = 0, the problem reduces to non-robust reinforcement learning. In such 
case our regret upper bound is Õ ( SA2H2 
√ K ) 
. Our result is the first theoretical result for learning 
a robust policy under s-rectangular uncertainty set, as previous results only learn the robust value function [Yang et al., 2021]. 
The analysis and techniques used for Theorem 2 hold great similarity to those ones used for Theorem 1. The main difference is on bounding σP̂h(s)(V̂ 
πk h+1)(s, a) − σPh(s)(V̂ 
πk h+1)(s, a). As the 
robustness of σP̂h(s)(V̂ πk h+1)(s, a) is no longer independent for different actions, we can not reduce 
the problem of σP̂h(s)(V̂ πk h+1)(s, a) into a scalar optimization problem. Instead, through analyzing 
the Lagrangian form, we obtain the A-dimensional convex optimization problem (4), which is solvable in O(A). Different from the (s, a)-rectangular case, our Lagrangian form has A times more variables, which complicates the solution regions of the optimum. Through proof by contradiction argument, we find the optimal ranges of each dual variable separately. With the optimum of η, we can apply concentration inequalities uniformly over the range of dual variables. The theorem follows the same arguments of Theorem 1 thereafter. 
6 Empirical results 
To validate our theoretical findings, we conduct a preliminary empirical analysis of our purposed robust policy optimization algorithm. 
Figure 1: Example of the Grid-world environment. 
Environment We conduct the experiments with the Gridworld environment, which is an early example of reinforcement learning from Sutton and Barto [2018]. The environment is two-dimensional and is in a cell-like environment. Specifically, the environment is a 5 × 5 grid, where the agent starts from the upper left cell. The cells consist of three types, road (labeled with o), wall (labeled with x), or reward state (labeled with +). The agent can safely walk through the road cell but not the wall cell. Once the agent steps on the reward cell, it will receive a reward of 1, and it will receive no rewards otherwise. The goal of the agents is to collect as many rewards as possible within the allowed time. The agent has four types of actions at each step, up, down, left, and right. After taking the action, the agent has a success probability of p to move according to the desired direction, and with the remaining probability of moving to other directions. 
10
Robust MDP To simulate the robust MDP, we create a nominal transition dynamic with success probability p = 0.9. The learning agent will interact with this nominal transition during training time and interact with a perturbed transition dynamic during evaluation. The transitions are perturbed along the direction is agent is directing with a constraint of ρ under (s, a)-rectangular set. Figure 1 shows an example of our environment, where the perturbation caused some of the optimal policies under nominal transition to be sub-optimal under robust transitions. We denote the perturbed transition as robust transitions in our results. 
Algorithm configuration We implement our proposed robust policy optimization algorithm along with the non-robust variant of it Shani et al. [2020]. The inner minimization of our Algorithm 1 is computed through its dual formulation for efficiency. Our algorithm is implemented with the rLberry framework [Domingues et al., 2021]. 
Results We present results with ρ = 0.1, 0.2, 0.3 here in Figure 2. We present the averaged cumulative rewards during evaluation. Regardless of the level of uncertainty, we observe that the robust variant of the policy optimization algorithm is more robust to dynamic changes as it is able to obtain a higher level of rewards than its non-robust variant. 
(a) ρ = 0.1 (b) ρ = 0.2 (c) ρ = 0.3 
Figure 2: Cumulative rewards obtained by robust and non-robust policy optimization on robust transition with different level of uncertainty ρ = 0.1, 0.2, 0.3 under `1 distance. 
7 Conclusion and future directions 
In this paper, we studied the problem of regret minimization in robust MDP with a rectangular uncertainty set. We proposed a robust variant of optimistic policy optimization, which achieves sublinear regret in all uncertainty sets considered. Our algorithm delicately balances the explorationexploitation trade-off through a carefully designed bonus term, which quantifies not only the uncertainty due to the limited observations but also the uncertainty of robust MDPs. Our results are the first regret upper bounds in robust MDPs as well as the first non-asymptotic results in robust MDPs without access to a generative model. 
For future works, while our analysis achieves the same bound as the policy optimization algorithm in Shani et al. [2020] when the robustness level ρ = 0, we suspect some technical details 
11
could be improved. For example, we required P oh to be positive for any s, a so that we could do a change of variable to form an efficiently solvable Fenchel dual. However, the actual positive value gets canceled out later and does not show up in the bound, suggesting that the strictly positive assumption might be an artifact of analysis. 
Furthermore, our work could also be extended in several directions. One is to consider other characterization of uncertainty sets, such as the Wasserstein distance metric. Another direction is to extend robust MDPs to a wider family of MDPs, such as the MDP with infinitely many states and with function approximation. 
References 
Alekh Agarwal, Nan Jiang, Sham M Kakade, and Wen Sun. Reinforcement learning: Theory and algorithms. CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep, pages 10–4, 2019. 
Kishan Panaganti Badrinath and Dileep Kalathil. Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In International Conference on Machine Learning, 2021. 
Peter Bartlett. Theoretical statistics. lecture 12, 2013. 
Qi Cai, Zhuoran Yang, Chi Jin, and Zhaoran Wang. Provably efficient exploration in policy optimization. In International Conference on Machine Learning, 2020. 
Liyu Chen, Haipeng Luo, and Chen-Yu Wei. Minimax regret for stochastic shortest path with adversarial costs and known transition. In Conference on Learning Theory, 2021a. 
Yifang Chen, Simon Du, and Kevin Jamieson. Improved corruption robust algorithms for episodic reinforcement learning. In International Conference on Machine Learning, 2021b. 
Karl Cobbe, Oleg Klimov, Chris Hesse, Taehoon Kim, and John Schulman. Quantifying generalization in reinforcement learning. In International Conference on Machine Learning, 2019. 
Christoph Dann, Tor Lattimore, and Emma Brunskill. Unifying pac and regret: Uniform pac bounds for episodic reinforcement learning. Advances in Neural Information Processing Systems, 2017. 
Omar Darwiche Domingues, Yannis Flet-Berliac, Edouard Leurent, Pierre Ménard, Xuedong Shang, and Michal Valko. rlberry - A Reinforcement Learning Library for Research and Education, 10 2021. URL https://github.com/rlberry-py/rlberry. 
Eyal Even-Dar, Sham M Kakade, and Yishay Mansour. Experts in a markov decision process. Advances in neural information processing systems, 2004. 
Jesse Farebrother, Marlos C Machado, and Michael Bowling. Generalization and regularization in dqn. arXiv preprint arXiv:1810.00123, 2018. 
Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2): 257–280, 2005. 
12
Chi Jin, Tiancheng Jin, Haipeng Luo, Suvrit Sra, and Tiancheng Yu. Learning adversarial Markov decision processes with bandit feedback and unknown transition. In International Conference on Machine Learning, 2020. 
Tiancheng Jin and Haipeng Luo. Simultaneously learning stochastic and adversarial episodic mdps with known transition. Advances in neural information processing systems, 2020. 
Nathan Kallus, Xiaojie Mao, Kaiwen Wang, and Zhengyuan Zhou. Doubly robust distributionally robust off-policy evaluation and learning. International Conference on Machine Learning, 2022. 
Thodoris Lykouris, Max Simchowitz, Alex Slivkins, and Wen Sun. Corruption-robust exploration in episodic reinforcement learning. In Conference on Learning Theory, 2021. 
Xiaoteng Ma, Zhipeng Liang, Li Xia, Jiheng Zhang, Jose Blanchet, Mingwen Liu, Qianchuan Zhao, and Zhengyuan Zhou. Distributionally robust offline reinforcement learning with linear function approximation. arXiv preprint arXiv:2209.06620, 2022. 
Shie Mannor, Ofir Mebel, and Huan Xu. Lightning does not strike twice: robust mdps with coupled uncertainty. In Proceedings of the 29th International Coference on International Conference on Machine Learning, 2012. 
Gergely Neu, Andras Antos, András György, and Csaba Szepesvári. Online markov decision processes under bandit feedback. Advances in Neural Information Processing Systems, 2010. 
Arnab Nilim and Laurent El Ghaoui. Robust control of markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005. 
Charles Packer, Katelyn Gao, Jernej Kos, Philipp Krähenbühl, Vladlen Koltun, and Dawn Song. Assessing generalization in deep reinforcement learning. arXiv preprint arXiv:1810.12282, 2018. 
Kishan Panaganti and Dileep Kalathil. Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics, 2022. 
Zhengling Qi and Peng Liao. Robust batch policy learning in markov decision processes. arXiv preprint arXiv:2011.04185, 2020. 
Roberta Raileanu and Rob Fergus. Decoupling value and policy for generalization in reinforcement learning. In International Conference on Machine Learning, 2021. 
Aviv Rosenberg and Yishay Mansour. Online convex optimization in adversarial markov decision processes. In International Conference on Machine Learning, 2019. 
Jay K Satia and Roy E Lave Jr. Markovian decision processes with uncertain transition probabilities. Operations Research, 21(3):728–740, 1973. 
John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust region policy optimization. In International conference on machine learning, 2015. 
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017. 
13
Lior Shani, Yonathan Efroni, Aviv Rosenberg, and Shie Mannor. Optimistic policy optimization with bandit feedback. In International Conference on Machine Learning, 2020. 
Xingyou Song, Yiding Jiang, Stephen Tu, Yilun Du, and Behnam Neyshabur. Observational overfitting in reinforcement learning. In International Conference on Learning Representations, 2019. 
Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
Yue Wang and Shaofeng Zou. Online robust reinforcement learning with model uncertainty. Ad-vances in Neural Information Processing Systems, 2021. 
Yue Wang and Shaofeng Zou. Policy gradient method for robust reinforcement learning. Interna-tional Conference on Machine Learning, 2022. 
Chelsea C White III and Hany K Eldeib. Markov decision processes with imprecise transition probabilities. Operations Research, 42(4):739–749, 1994. 
Wolfram Wiesemann, Daniel Kuhn, and Berç Rustem. Robust markov decision processes. Mathe-matics of Operations Research, 38(1):153–183, 2013. 
Tianhao Wu, Yunchang Yang, Han Zhong, Liwei Wang, Simon Du, and Jiantao Jiao. Nearly optimal policy optimization with stable at any time guarantee. In International Conference on Machine Learning, 2022. 
Wenhao Yang, Liangyu Zhang, and Zhihua Zhang. Towards theoretical understandings of robust markov decision processes: Sample complexity and asymptotics. arXiv preprint arXiv:2105.03863, 2021. 
Xuezhou Zhang, Yiding Chen, Xiaojin Zhu, and Wen Sun. Corruption-robust offline reinforcement learning. In International Conference on Artificial Intelligence and Statistics, 2022. 
Zhengqing Zhou, Zhengyuan Zhou, Qinxun Bai, Linhai Qiu, Jose Blanchet, and Peter Glynn. Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, 2021. 
14
A Proofs of Theorem 1 
A.1 Good events 
We first define the following good events, in which case we estimate the reward function and the nominal transition functions fairly accurately. 
Grk = 
{ ∀s, a, h : 
∣∣∣rh(s, a)− r̂kh(s, a) ∣∣∣ ≤√2 ln(2SAH2K/δ′) 
Nk h (s, a) 
} , 
Gpk = { ∀s, a, h : σPh(s,a)(V̂ 
πk h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s) ≤ C 
k h(s, a) 
} , 
where Ckh(s, a) = H 
√ 4S log(3SAH2K3/2(4+ρ)/δ′) 
Nk h (s,a) 
+ 1√ K 
. 
When the two good events happens at the same time, we say the algorithm in inside the 
good event G = (⋂K 
k=1 Grk )⋂(⋂K 
k=1 G p k 
) . The following lemma shows that G happens with high 
probability by setting δ′ properly. 
Lemma 1 (Good event). Let δ = 2δ′, then the good event happens with high probability, i.e. P [G] ≥ 1− δ. 
Proof. By Hoeffding’s inequality and an union bound on all s, a, all possible values of Nk(s, a) and 
k, we have P [⋂K 
k=1 Grk ] ≥ 1− δ′. By Lemma 4, we have P 
[⋂K k=1 G 
p k 
] ≥ 1− δ′ Then set δ = 2δ′ and 
we have the desired result. 
A.2 Design of the bonus function 
In the case of (s, a)-rectangular uncertainty set, we use the following bonus function bkh(s, a) to encourage exploration. 
bkh(s, a) = 
√ 2 log(3SAH2K/δ) 
Nk h (s, a) 
+H 
√ 4S log(3SAH2K3/2(4 + ρ)/δ) 
Nk h (s, a) 
+ 1√ K . (5) 
A.3 Regret Analysis 
Armed with the defined good event, we are now ready to present the anlysis of Theorem 1, which establishes the regret of the Algorithm under (s, a)-uncertainty set. 
Theorem 1 (Regret under (s, a)-rectangular uncertainty set). With learning rate β = √ 
2 logA H2K 
and bonus term bkh as (5), with probability at least 1− δ, the regret incurred by Algorithm 1 over K episodes is bounded by 
Regret(K) = O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) . 
Proof. We start with decomposing the regret as follows, 
Regret(K) = 
K∑ k=1 
V ∗1 (s)− V πk 1 (s) 
15
= K∑ k=1 
( V ∗1 (s)− V̂ πk 
1 (s) ) 
+ ( V̂ πk 1 (s)− V πk 
1 (s) ) . 
By Lemma 2 and Lemma 4, with probability at least 1− δ, we have 
Regret(K) = O ( H2 √ K logA 
) +O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) = O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) . 
Lemma 2. With probability at least 1− δ, we have 
K∑ k=1 
V ∗1 (s)− V̂ πk 1 (s) = O 
( H2 √ K logA 
) . 
Proof. For any h ∈ [1, H], we have 
V ∗h (s)− V̂ πk h (s) 
= 〈Q∗h(s, ·), π∗(· | s)〉 − 〈Q̂πkh (s, ·), πk(· | s)〉 = 〈Q∗h(s, ·)− Q̂πkh (s, ·), π∗(· | s)〉+ 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
= Eπ∗ [ (rh(s, a)− r̂kh(s, a)) + (σPh(s,a)(V 
∗ h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s))− b 
k h(s, a) 
] + 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
= Eπ∗ [ (rh(s, a)− r̂kh(s, a)) + (σPh(s,a)(V̂ 
πk h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s))− b 
k h(s, a) 
] + Eπ∗ 
[ σPh(s,a)(V 
∗ h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) 
] + 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 , 
where the third equality is by the update rule of our algorithm and the robust bellman equation. By the design of our bonus function, conditioned on the good event, we have 
(rh(s, a)− r̂kh(s, a)) + (σPh(s,a)(V ∗ h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s))− b 
k h(s, a) ≤ 0 . 
Let qh(· | s, a) = arg min Ph∈Ph 
Ph(· | s, a)V̂ πk h+1, then we have 
σPh(s,a)(V ∗ h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) 
= min Ph∈Ph 
Ph(· | s, a)V ∗h+1 − min Ph∈Ph 
Ph(· | s, a)V̂ πk h+1 
= min Ph∈Ph 
Ph(· | s, a)V ∗h+1 − qh(· | s, a)V̂ πk h+1 
≤ qh(· | s, a)(V ∗h+1 − V̂ πk h+1) 
≤ max Ph∈Ph 
Ph(· | s, a)(V ∗h+1 − V̂ πk h+1) . 
16
Let ph(· | s, a) = arg max Ph∈Ph 
Ph(· | s, a)(V ∗h+1)(s, a), Then we have the following relation hold 
conditioned on the good event: 
V ∗h (s)− V̂ πk h (s) 
≤ Eπ∗ 
[ sup Ph∈Ph 
Ph(· | s, a)(V ∗h+1 − V̂ πk h+1) 
] + 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
= Eπ∗,ph [ V ∗h+1(s)− V̂ 
πk h+1(s) 
] + 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 . 
Then, by applying above relation recursively and with the fact that for any policy π and state s, V ∗H+1(s) = V̂ πk 
H+1(s) = 0, we have 
V ∗1 (s)− V̂ πk 1 (s) ≤ 
H∑ h=1 
Eπ∗,{pt}h−1 t=1 
[ 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
] . 
Summing over k, we get 
K∑ k=1 
V ∗1 (s)− V̂ πk 1 (s) ≤ 
K∑ k=1 
H∑ h=1 
Eπ∗,{pt}h−1 t=1 
[ 〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
] = 
H∑ h=1 
Eπ∗,{pt}h−1 t=1 
[ K∑ k=1 
〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 
] . 
By standard results for online mirror descent (Lemma 13), we have 
K∑ k=1 
〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 ≤ log(A) 
β + β 
2 
K∑ k=1 
∑ a∈A 
π∗h(a | s)(Q̂πkh (s, a))2 . 
By the update rule of Algorithm 1, we have 0 ≤ Q̂πkh (s, a) ≤ H, for all h, k. Then take β = √ 
2 logA H2K 
, 
K∑ k=1 
〈Q̂πkh (s, ·), π∗(· | s)− πk(· | s)〉 ≤ √ 
2H2K logA . 
Finally, we have 
K∑ k=1 
V ∗1 (s)− V̂ πk 1 (s) ≤ H 
√ 2H2K logA = O 
( H2 √ K logA 
) . 
Lemma 3. With probability at least 1− δ, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) . 
17
Proof. By the algorithm’s update rule and the robust bellman equation, we have 
(V̂ πk h − V 
πk h )(s) = 〈Q̂πkh (s, ·)−Qπkh (s, ·), πk(· | s)〉 
= 〈 r̂kh(s, ·)− rkh(s, ·) + (σP̂(s,·) 
(V̂ πk h+1)(s, ·)− σP(s,·)(V 
πk h+1)(s, ·)) + bkh(s, ·), πk(· | s) 
〉 = Eπk 
[ r̂kh(s, a)− rkh(s, a) + (σP̂h(s,a)(V̂ 
πk h+1)(s)− σPh(s,a)(V 
πk h+1)(s)) + bkh(s, a) 
] . 
By adding and subtracting a term σPh(s,a)(V̂ πk h+1)(s, a), we have 
σP̂h(s,a)(V̂ πk h+1)(s)− σPh(s,a)(V 
πk h+1)(s) 
= σP̂h(s,a)(V̂ πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) + σPh(s,a)(V̂ 
πk h+1)(s)− σPh(s,a)(V 
πk h+1)(s) 
≤ σP̂h(s,a)(V̂ πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) + max 
Ph∈Ph Ph(· | s, a)(V̂ πk 
h+1 − V πk h+1) . 
Let ph(· | s, a) = arg max Ph∈Ph 
Ph(· | s, a)(V̂ πk h+1 − V 
πk h+1), we have 
(V̂ πk h − V 
πk h )(s) 
≤ Eπk [ r̂kh(s, a)− rkh(s, a) + σP̂h(s,a)(V̂ 
πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) + ph(· | s, a)(V̂ πk 
h+1 − V πk h+1) + bkh(s, a) 
] = Eπk,ph 
[ r̂kh(s, a)− rkh(s, a) + σP̂h(s,a)(V̂ 
πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) + V̂ πk 
h+1(s)− V πk h+1(s) + bkh(s, a) 
] By applying the above relation recursively and with the fact that for any policy π and state s, 
V πk H+1(s) = V̂ πk 
H+1(s) = 0, we have 
(V̂ πk 1 − V πk 
1 )(s) ≤ H∑ h=1 
Eπk,{pt}ht=1 
[ r̂kh(s, a)− rkh(s, a) + σP̂h(s,a)(V̂ 
πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) + bkh(s, a) 
] . 
Conditioned on the good even and by the design of our bonus function, we have 
r̂kh(s, a)− rkh(s, a) + σP̂h(s,a)(V̂ πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) ≤ b 
k h(s, a) . 
Then, with probability at least 1− δ, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) ≤ K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[ 2bkh(s, a) 
] ≤ H 
√ K +O 
( H √ S log(SAH2K3/2(4 + ρ)/δ) 
) K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[√ 1 
Nk h (s, a) 
] . 
By Lemma 12, we have the bound of the visitation counts: 
K∑ k=1 
H∑ h=1 
√ 1 
Nk h (s, a) 
≤ 2H √ SAK . 
Combining everything, with probability at least 1− δ K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( H2S 
√ AK log 
( SAH2K3/2(1 + ρ)/δ 
)) . 
18
Lemma 4. For any h, k, s, a, the following inequality holds with probability at least 1− δ′, 
σPh(s,a)(V̂ πk h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s) ≤ H 
√ 4S log(3SAH3K3/2(4 + ρ)/δ′) 
Nk h (s, a) 
+ 1 
H √ K . 
Proof. By the definition of σPh(s,a)(V̂ πk h+1)(s) = min 
Ph∈Ph 
∑ s′ Ph(s′ | s, a)V̂ πk 
h+1(s ′), we have the follow-
ing optimization problem: 
min Ph 
∑ s′ 
Ph(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′ |Ph(s′ | s, a)− P oh(s′ | s, a)| ≤ ρ ,∑ s′ Ph(s′ | s, a) = 1 , 
P oh(· | s, a) > 0, Ph(· | s, a) ≥ 0 . 
Define P̃h(s′ | s, a) = Ph(s ′|s,a) 
P oh (s ′|s,a) , we can rewrite the above optimization problem as 
min P̃h 
∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′ |P̃h(s′ | s, a)− 1|P oh(s′ | s, a) ≤ ρ ,∑ s′ P̃h(s′ | s, a)P oh(s′ | s, a) = 1 , 
P̃h(s′ | s, a) ≥ 0 ∀s′ ∈ S . 
Using the Lagrangian multiplier method, we have the following Lagrangian L(P̃h, η, λ) with Lagrangian multiplier η ∈ R, λ ≥ 0, 
L(P̃h, η, λ)(s, a) = ∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) + λ 
(∑ s′ 
|P̃h(s′ | s, a)− 1|P oh(s′ | s, a)− ρ 
) 
− η 
(∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)− 1 
) 
= η − λρ− λ ∑ s′ 
P oh(s′ | s, a) 
( η 
λ P̃h(s′ | s, a)− |P̃h(s′ | s, a)− 1| − 
P̃h(s′ | s, a)V̂ πk h+1(s 
′) 
λ 
) 
= η − λρ− λ ∑ s′ 
P oh(s′ | s, a) 
( η − V̂ πk 
h+1(s ′) 
λ P̃h(s′ | s, a)− |P̃h(s′ | s, a)− 1| 
) . 
We define f(x) = |x − 1| and the convex conjugate is f∗(y) = max x 〈x, y〉 − f(x). Let x be P̃h 
and by using f∗, we can optimize over P̃h and rewrite the Lagrangian as 
L(η, λ)(s, a) = min P̃h 
L(P̃h, η, λ)(s, a) = η − λρ− λ ∑ s′ 
P oh(s′ | s, a)f∗ 
( η − V̂ πk 
h+1(s ′) 
λ 
) . 
Notice that conditioned on x ≥ 0, f(x) = |x − 1|’s convex conjugate has the following closed form: 
f∗(y) = max x 〈x, y〉 − f(x) = 
 −1 y ≤ −1 , 
y y ∈ [−1, 1] , 
+∞ y > 1 . 
19
Let η̃ = η + λ, then using the closed form of f∗(y), the equality max {a, b} = (a− b)+ + b and 
condition on η−V̂ πkh+1(s 
′) 
λ ≤ 1, we can rewrite the optimization problem as 
L(η̃, λ)(s, a) = η − λρ− λ ∑ s′ 
P oh(s′ | s, a)f∗ 
( η − V̂ πk 
h+1(s ′) 
λ 
) 
= η̃ − λ− λρ− λ ∑ s′ 
P oh(s′ | s, a) max 
{ η − V̂ πk 
h+1(s ′) 
λ ,−1 
} 
= η̃ − λ− λρ− λ ∑ s′ 
P oh(s′ | s, a) 
(( η − V̂ πk 
h+1(s ′) 
λ − (−1) 
) + 
+ (−1) 
) = η̃ − λ− λρ− 
∑ s′ 
P oh(s′ | s, a)(η̃ − V̂ πk h+1(s 
′))+ + λ 
= η̃ − λρ− ∑ s′ 
P oh(s′ | s, a)(η̃ − V̂ πk h+1(s 
′))+ . 
with the constraint of λ being 
λ ≥ 0, η̃ −min s V̂ πk h+1(s) ≤ 2λ. 
Note that L(η̃, λ)(s, a) is inversely proportional to λ, it achieves the maximum when λ = (η̃−min 
s V̂ πk h+1(s))+ 
2 . By directly optimizing it over λ, we can reduce the problem to 
L(η̃)(s, a) = η̃ − (η̃ −min 
s V̂ πk h+1(s))+ 
2 ρ− 
∑ s′ 
P oh(s′ | s, a)(η̃ − V̂ πk h+1(s 
′))+ . 
Define the function g as 
g(η̃, P oh) = −L(η̃)(s, a) = ∑ s′ 
P oh(s′ | s, a) ( η̃ − V̂ πk 
h+1(s ′) ) + − η̃ + 
(η̃ −min s V̂ πk h+1(s))+ 
2 ρ . 
Then we investigate the optimum of g. First notice that g(0) = 0, when η̃ ≤ 0, g(η̃, P oh) = −η̃ ≥ 0. 
On the other hand, when η̃ ≥ H, 
g(η̃, P oh) = ∑ s′ 
P oh(s′ | s, a)(η̃ − V̂ πk h+1(s 
′))− η̃ + (η̃ −min 
s V̂ πk h+1(s)) 
2 ρ 
= − ∑ s′ 
P oh(s′ | s, a)V̂ πk h+1(s 
′) + (η̃ −min 
s V̂ πk h+1(s)) 
2 ρ . 
Note that now g is directly proportional to η̃, therefore g achieves the minimum within the range of η̃ ∈ [0, H]. We remark that the same form is also used for analyzing robust policy evaluation (Lemma B.1 [Yang et al., 2021]). 
20
With this, we can rewrite 
σP̂h(s,a)(V̂ πk h+1)(s)− σPh(s,a)(V̂ 
πk h+1)(s) = − min 
η1∈[0,H] g(η1, P̂ 
o,k h ) + min 
η2∈[0,H] g (η2, P 
o h) 
≤ max η∈[0,H] 
|g ( η, P̂ o,kh 
) − g (η, P oh) | . 
To upper bound σP̂h(s,a)(V̂ πk h+1)(s) − σPh(s,a)(V̂ 
πk h+1)(s), we first upper bound |g 
( η, P̂ o,kh 
) − 
g (η, P oh) |. 
|g ( η, P̂ o,kh 
) − g (η, P oh) | = 
∣∣∣∣∣∑ s′ 
P̂ o,kh (s′ | s, a) ( η − V̂ πk 
h+1(s ′) ) + − ∑ s′ 
P oh(s′ | s, a) ( η − V̂ πk 
h+1(s ′) ) + 
∣∣∣∣∣ ≤ ∥∥∥P̂ o,kh (· | s, a)− P oh(· | s, a) 
∥∥∥ 1 
max s∈S |η − V̂ πk 
h+1(s)|∞ 
≤ H ∥∥∥P̂ o,kh (· | s, a)− P oh(· | s, a) 
∥∥∥ 1 , 
where the first inequality is by Cauchy-Schwarz inequality, the second inequality follows from η ∈ [0, H]. 
By Hoeffding’s inequality and an union bound over all s, a, the following inequality holds with probability at least 1− δ′: 
∥∥∥P̂ o,kh (· | s, a)− P oh(· | s, a) ∥∥∥ 1 ≤ 
√ 4S log(3SAH2K/δ′) 
Nk h (s, a) 
. 
To upper bound the error with maximum over η, we first create an ε-net Nε(η) with g over η ∈ [0, H] such that 
max η∈[0,H] 
|g ( η, P̂ o,kh 
) − g (η, P oh) | ≤ max 
η∈Nε(η) |g ( η, P̂ o,kh 
) − g (η, P oh) |+ 2ε . 
By taking an union bound over Nε(η), we have 
max η∈[0,H] 
|g ( η, P̂ o,kh 
) − g (η, P oh) | ≤ H 
√ 4S log(3SAH2K|Nε(η)|/δ′) 
Nk h (s, a) 
+ 2ε , 
where |Nε(η)| is the size of the ε-net. It now remains to bound the size of |Nε(η)|, which can be obtained easily if g is Lischitz. Notice 
that 
|g(η̃1, P o h)− g(η̃2, P 
o h)| ≤ 
∑ s′ 
P oh(s′ | s, a)|η̃1 − η̃2|+ |η̃1 − η̃2|+ |η̃1 − η̃2| 
2 ρ 
= 4 + ρ 
2 |η̃1 − η̃2| , 
where the first inequality is by the absolute inequality and |(a)+ − (b)+| ≤ |a− b|. 
21
Then g is a 4+ρ 2 -Lipschitz function over η ∈ [0, H], thus combined with Lemma 11, we have 
|Nε(η)| = O ( 4+ρ 2ε 
) . Hence, we have the following inequality happens with at least 1−δ′ probability: 
max η∈[0,H] 
|g ( η, P̂ o,kh 
) − g (η, P oh) | ≤ H 
√ 4S log(3SAH2K(4 + ρ)/2εδ′) 
Nk h (s, a) 
+ 2ε . 
Take ε = 1 2 √ K 
, we have the following inequality happens with at least 1− δ′ probability: 
σPh(s,a)(V̂ πk h+1)(s)− σP̂h(s,a)(V̂ 
πk h+1)(s) ≤ max 
η∈[0,H] |g ( η, P̂ o,kh 
) − g (η, P oh) | 
≤ H 
√ 4S log(3SAH2K3/2(4 + ρ)/δ′) 
Nk h (s, a) 
+ 1√ K . 
22
B Proof of Theorem 2 
B.1 Good events 
We first define the following good events, in which case we estimate the reward function and the nominal transition functions fairly accurately. 
Grk = 
{ ∀s, a, h : 
∣∣∣rh(s, a)− r̂kh(s, a) ∣∣∣ ≤√2 ln(2SAH2K/δ′) 
Nk h (s, a) 
} , 
Gpk = { ∀s, a, h : σPh(s)(V̂ 
πk h+1)(s)− σP̂h(s)(V̂ 
πk h+1)(s) ≤ C 
k h(s, a) 
} , 
where 
Ckh(s, a) = AH 
√ 4SA log(3SA2H3K3/2(4 + ρ)/δ′) 
Nk h (s, a) 
+ 1 
H √ K . 
When the two good events happens at the same time, we say the algorithm in inside the good event 
G = (⋂K 
k=1 Grk )⋂(⋂K 
k=1 G p k 
) . The following lemma shows that G happens with high probability. 
Lemma 5 (Good event). Let δ = 2δ′, then the good event happens with high probability, i.e. P [G] ≥ 1− δ. 
Proof. By Hoeffding’s inequality and an union bound on all s, a, all possible values of Nk(s, a) and 
k, we have P [⋂K 
k=1 Grk ] ≥ 1− δ′. By Lemma 7, we have P 
[⋂K k=1 G 
p k 
] ≥ 1− δ′ Then set δ = 2δ′ and 
we have the desired result. 
B.2 Design of the bonus function 
In the case of s-rectangular uncertainty set, we use the following bonus function bkh(s, a) to encourage exploration. 
bkh(s, a) = AH 
√ 4SA log(3SA2H2K3/2(4 + ρ)/δ) 
Nk h (s, a) 
+ 1√ K 
+ 
√ 2 log(3SAH2K/δ′) 
Nk h (s, a) 
. (6) 
B.3 Regret analysis 
Theorem 2 (Regret under s-rectangular uncertainty set). With learning rate β = √ 
2 logA H2K 
and 
bonus term bkh as (6), with probability at least 1− δ, the regret of Algorithm 1 is bounded by 
Regret(K) = O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) . 
Proof. Similar to the case of (s, a)-rectangular set, we start with decomposing the regret as follows, 
Regret(K) = 
K∑ k=1 
V ∗1 (s)− V πk 1 (s) 
23
= K∑ k=1 
( V ∗1 (s)− V̂ πk 
1 (s) ) 
+ ( V̂ πk 1 (s)− V πk 
1 (s) ) . 
By Lemma 2 and Lemma 6, with probability at least 1− δ, we have 
Regret(K) = O ( H2 √ K logA 
) +O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) = O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) . 
Lemma 6. With Algorithm 1, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) . 
Proof. Similar to the case with (s, a)-rectangular uncertainty set, for any k, we can decompose (V̂ πk 
1 − V̂ πk 1 )(s) as, 
(V̂ πk 1 − V̂ πk 
1 )(s) 
≤ H∑ h=1 
Eπk,{pt}ht=1 
[ (rkh(s, a)− r̂kh(s, a)) + 
( σP̂h(s) 
( V̂ πk h+1 
) (s)− σPh(s) 
( V̂ πk h+1 
) (s) ) 
+ bkh(s, a) ] . 
Thus by the design of our bonus function and with probability at least 1− δ, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) 
≤ 2 K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[ bkh(s, a) 
] = H 
√ K +O 
( HA 
√ SA log(SA2H2K3/2(1 + ρ)/δ) 
) K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[√ 1 
Nk h (s, a) 
] . 
By Lemma 12, we have the bound of visitation counts: 
K∑ k=1 
H∑ h=1 
√ 1 
Nk h (s, a) 
≤ 2H √ SAK . 
Combining everything, conditioned on the good event we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( SA2H2 
√ K log(SA2H2K3/2(1 + ρ)/δ) 
) . 
24
Lemma 7. For any h, k, s, a, the following inequality holds with probability at least 1− δ, 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ AH 
√ 4SA log(3SA2H2K3/2(4 + ρ)/δ) 
Nk h (s, a) 
+ 1√ K . 
Proof. By the definition of σPh(s)(V̂ πk h+1)(s) = inf 
Ph∈Ph 
∑ s′ Ph(s′ | s, a)V̂ πk 
h+1(s ′), we consider the fol-
lowing optimization problem: 
min Ph 
∑ s′ 
Ph(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′,a′ |Ph(s′ | s, a′)− P oh(s′ | s, a′)| ≤ Aρ ,∑ s′ Ph(s′ | s, a′) = 1 ,∀a′ ∈ A , 
P oh(· | s, a′) > 0, Ph(· | s, a′) ≥ 0 ,∀a′ ∈ A . 
Let P̃h(s′ | s, a) = Ph(s ′|s,a) 
P oh (s ′|s,a) , we can rewrite the above optimization problem as 
min P̃h 
∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′,a′ |(P̃h(s′ | s, a′)− 1|P oh(s′ | s, a′) ≤ Aρ ,∑ s′ P̃h(s′ | s, a′)P oh(s′ | s, a′) = 1 , ∀a′ ∈ A 
P̃h(· | s, a′) ≥ 0 , ∀a′ ∈ A . 
Use the Lagrangian multiplier method and f(x) = |x− 1|, we have the Lagrangian L(P̃h, η, λ) with multiplier η = {ηa}a∈A, ηa ∈ R, λ ≥ 0, 
L ( P̃h, η, λ 
) (s, a) 
= ∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) + λ 
∑ s′,a′ 
∣∣∣(P̃h(s′ | s, a′)− 1 ∣∣∣P oh(s′ | s, a′)−Aρ 
 − ∑ a′ 
ηa′ 
(∑ s′ 
P̃h(s′ | s, a′)P oh(s′ | s, a′)− 1 
) 
= − λAρ+ ∑ a′ 
ηa′ + λ ∑ s′,a′ 
P oh(s′ | s, a′) ( f ( P̃h(s′ | s, a′) 
) − P̃h(s′ | s, a′) 
( ηa′ − I{a′ = a}V πk 
h+1(s ′) 
λ 
)) . 
The convex conjugate of f is f∗(y) = max x 〈x, y〉 − f(x). Using f∗, we can thus optimize over 
P̃h and rewrite the Lagrangian over as 
L(η, λ)(s, a) = min P̃h 
L ( P̃h, η, λ 
) (s, a) 
= − λAρ+ ∑ a′ 
ηa′ − λ ∑ s′,a′ 
P oh(s′ | s, a′)f∗ ( ηa′ − I{a′ = a}V πk 
h+1(s ′) 
λ 
) . 
25
Conditioned on x ≥ 0, f(x) = |x− 1|, notice that the conjugate f∗(y) has the following closed form, 
f∗(y) = max x 〈x, y〉 − f(x) = 
 −1 y ≤ −1 , 
y y ∈ [−1, 1] , 
+∞ y > 1 . 
Let η̃a = ηa + λ, using the closed form of f∗(y), the equality max {a, b} = (a − b)+ + b and 
conditioned on ηa′−I{a′=a}V 
πk h+1(s 
′) 
λ ≤ 1, we can rewrite the optimization problem as 
L(η̃, λ)(s, a) = −λAρ+ ∑ a′ 
ηa′ − λ ∑ s′,a′ 
P oh(s′ | s, a′)f∗ ( ηa′ − I{a′ = a}V πk 
h+1(s ′) 
λ 
) 
= −λAρ− λA+ ∑ a′ 
η̃a′ − λ ∑ s′,a′ 
P oh(s′ | s, a′) max 
{ ηa′ − I{a′ = a}V πk 
h+1(s ′) 
λ ,−1 
} = −λAρ+ 
∑ a′ 
η̃a′ − ∑ s′,a′ 
P oh(s′ | s, a′) ( η̃a′ − I{a′ = a}V πk 
h+1(s ′) ) + . 
where constraint of λ is 
λ ≥ 0, η̃a′ − I{a′ = a}V πk h+1(s 
′) ≤ 2λ, ∀a′, s′ . 
Note that the above Lagrangian is inversely proportional to λ and it achieves the maximum 
when λ = max s′,a′ 
(η̃a′−I{a′=a}V πk h+1(s 
′))+ 2 . Directly optimize over λ, we can reduce the problem to 
L(η̃)(s, a) = ∑ a′ 
η̃a′ − ∑ s′,a′ 
P oh(s′ | s, a′) ( η̃a′ − I{a′ = a}V πk 
h+1(s ′) ) + −max 
s′,a′ 
Aρ(η̃a′ − I{a′ = a}V πk h+1(s 
′))+ 
2 . 
Define g (η̃, P oh) = −L(η̃)(s, a) as 
g(η̃, P oh) = − ∑ a′ 
η̃a′ + ∑ s′,a′ 
P oh(s′ | s, a′) ( η̃a′ − I{a′ = a}V πk 
h+1(s ′) ) + 
+ max s′,a′ 
Aρ(η̃a′ − I{a′ = a}V πk h+1(s 
′))+ 
2 . 
Assume g achieves its minimum when η̃ = {η̃1, · · · , η̃A}. Suppose η̃ has a component η̃a < 0. Consider η′ = {η̃1, · · · , 0, · · · , η̃a}, where we change the zero element η̃a to 0 and keep other components unchanged. Then we have 
g(η̃, P oh)− g(η′, P oh) = −η̃A > 0 , 
which contradict with the hypothesis that g achieves its minimum in η̃. On the other hand, suppose η̃ has a component η̃a > H. Then consider η′ = {η̃1, · · · , H, · · · , η̃a}, 
where we change corresponding η̃a to 0 and keep other components unchanged. Denote f(η̃) = 
max s′,a′ 
Aρ(η̃a′−I{a′=a}V πk h+1(s 
′))+ 2 , and we have 
g (η̃, P oh)− g ( η′, P oh 
) = − η̃A +H + 
∑ s′ 
P oh(s′ | s, a)(η̃a −H) + f(η̃)− f(η′) 
26
≥ − η̃A +H + ∑ s′ 
P oh(s′ | s, a)(η̃a −H) 
= 0 . 
Therefore, g achieves its minimum with η̃, with 0 ≤ ηa ≤ H,∀a ∈ A. We remark that a similar form and technique are also used for analyzing robust policy evaluation (Lemma C.1 [Yang et al., 2021]). 
We can now rewrite 
σP̂h(s) 
( V̂ πk h+1 
) (s)− σPh(s) 
( V̂ πk h+1 
) (s) = min 
η1∈[0,H]|A| g(η1, P̂ 
o,k h )− min 
η2∈[0,H]|A| g(η2, P 
o h) 
≤ max η∈[0,H]|A| 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣ . To upper bound σP̂h(s) 
( V̂ πk h+1 
) (s)−σPh(s) 
( V̂ πk h+1 
) (s), we first consider the bound of 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣,∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣ = 
∣∣∣∣∣∣ ∑ s′,a′ 
P̂ o,kh (s′ | s, a′) ( ηa′ − I{a′ = a}V πk 
h+1(s ′) ) + − ∑ s′,a′ 
P oh(s′ | s, a′) ( ηa′ − I{a′ = a}V πk 
h+1(s ′) ) + 
∣∣∣∣∣∣ = 
∣∣∣∣∣ ∑ a′ 
∑ s′ 
( P̂ o,kh (s′ | s, a′)− P oh(s′ | s, a′) 
) ( ηa′ − I{a′ = a}V πk 
h+1(s ′) ) + 
∣∣∣∣∣ ≤ ∑ a′ 
∥∥∥P̂ o,kh (· | s, a′)− P oh(· | s, a′) ∥∥∥ 1 
max s∈S 
∣∣ηa′ − I{a′ = a}V πk h+1(s) 
∣∣ ≤ H 
∑ a′ 
∥∥∥P̂ o,kh (· | s, a′)− P oh(· | s, a′) ∥∥∥ 1 , 
where the first inequality is by Cauchy-Schwarz inequality, the second inequality follows from ηa ∈ [0, H], ∀a ∈ A. 
By Hoeffding’s inequality and an union bound over all s, a′, Nk h (s, a), the following inequality 
holds with probability at least 1− δ, 
∥∥∥P̂ o,kh (· | s, a′)− P oh(· | s, a′) ∥∥∥ 1 ≤ 
√ 4S log(SAH2K/δ) 
Nk h (s, a) 
. 
To upper bound maxη∈[0,H]|A| 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣, we first create an ε-net Nε(η) with g over 
η ∈ [0, H] such that 
max η∈[0,H] 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣ ≤ max η∈Nε(η) 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣+ 2ε . 
Taking an union bound over Nε(η), we have 
max η∈[0,H] 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣ ≤ HA√4S log(3SAH2K|Nε(η)|/δ) Nk h (s, a) 
+ 2ε , 
27
where |Nε(η)| is the size of the ε-net. It now remains to find the size of the ε-net, which can be easily obtained if g is Lipschitz. Notice 
that 
|g(η̃1, P o h)− g(η̃2, P 
o h)| 
≤ ∑ s′,a′ 
P oh(s′ | s, a)|η̃1,a′ − η̃2,a′ |+ ∑ a′ 
|η̃1,a′ − η̃2,a′ |+ max a′ |η̃1,a′ − η̃2,a′ | 
2 Aρ 
≤ A(4 + ρ) 
2 ‖η̃1 − η̃2‖∞ , 
where the first inequality is by the absolute inequality, the property of maximum function and |(a)+ − (b)+| ≤ |a− b|, the second inequality follows from the definition of infinity norm. 
Therefore g is a A(4+ρ) 2 -Lipschitz function over η ∈ [0, H]. Thus combining with Lemma 11, we 
have |Nε(η)| ≤ ( A(4+ρ) 
2ε 
)A . Hence, we have the following inequality happens with at least 1 − δ′ 
probability: 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ max 
ηa∈[0,H]|A| 
∣∣∣g (η, P̂ o,kh ) − g (η, P oh) 
∣∣∣ ≤ AH 
√ 4SA log(3SA2H2K(4 + ρ)/2εδ′) 
Nk h (s, a) 
+ 2ε . 
Take ε = 1 2 √ K 
, then 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ AH 
√ 4SA log(3SA2H2K3/2(4 + ρ)/δ′) 
Nk h (s, a) 
+ 1√ K . 
28
C Extension to uncertainty set with KL divergence 
In this section, we extend our algorithm and analysis to uncertainty sets with KL divergence as a distance metric. We first formally define the uncertainty set considered, which is similar to the one in Definition 3.1. 
Definition C.1 ((s, a)-rectangular uncertainty set Iyengar [2005], Wiesemann et al. [2013]). For all time step h and with a given state-action pair (s, a), the (s, a)-rectangular uncertainty set Ph(s, a) is defined as 
Ph(s, a) = {DKL (Ph(· | s, a), P oh(· | s, a)) ≤ ρ , Ph(· | s, a) ∈ ∆(S)} , 
where P oh is the nominal transition kernel at h, P oh(· | s, a) > 0, ∀(s, a) ∈ S × A, ρ is the level of 
uncertainty and DKL (p(· | s, a), q(· | s, a)) = ∑ 
s′∈S p(s ′ | s, a) log 
( p(s′|s,a) q(s′|s,a) 
) . 
With the above described uncertainty set, our algorithm solves σP̂h(V̂ π h+1)(s, a) by solving the 
following sub-problem, 
min λ λρ+ λ log 
(∑ s′ 
P̂ oh(s′ | s, a) exp 
( −V̂ πk 
h+1(s ′) 
λ 
)) . 
Our algorithm also uses the following bonus function in the robust policy evaluation step, 
bkh(s, a) = Ckh(s, a) + 
√ 2 log(3SAH2K/δ′) 
Nk h (s, a) 
. 
With these modifications to algorithm 1, the following theorem states the formal regret guarantee. 
Theorem 3 (Regret under KL divergence (s, a)-rectangular uncertainty set). Setting the learning 
rate β = √ 
2 logA H2K 
, then with probability at least 1 − δ, the regret incurred by Algorithm over K 
episodes is bounded by 
Regret(K) = O 
( SH 
ρc 
√ AK log(SAH4K3/2/δ) 
) , 
where 0 < c ≤ 1 the minimal element of P oh , over all h ∈ [H]. 
In the following, we present the detailed analysis of Theorem 3 
C.1 Good events 
We first define the following good events, in which case we estimate the reward function and the nominal transition functions fairly accurately. 
Grk = 
{ ∀s, a, h : 
∣∣∣rh(s, a)− r̂kh(s, a) ∣∣∣ ≤√2 ln(2SAH2K/δ′) 
Nk h (s, a) 
} , 
29
Gpk = { ∀s, a, h : σPh(s)(V̂ 
πk h+1)(s)− σP̂h(s)(V̂ 
πk h+1)(s) ≤ C 
k h(s, a) 
} , 
where 
Ckh(s, a) = 2H 
ρc 
√ 4S log(8SAH4K2/δ′ρ) 
Nk h (s, a) 
+ 1√ K , 
and c is the minimal element of P oh , over all h ∈ [H]. When the two good events happens at 
the same time, we say the algorithm in inside the good event G = (⋂K 
k=1 Grk )⋂(⋂K 
k=1 G p k 
) . The 
following lemma shows that G happens with high probability. 
Lemma 8 (Good event). Let δ = 2δ′, then the good event happens with high probability, i.e. P [G] ≥ 1− δ. 
Proof. By Hoeffding’s inequality and an union bound on all s, a, all possible values of Nk(s, a) and 
k, we have P [⋂K 
k=1 Grk ] ≥ 1 − δ′. By Lemma 10, we have P 
[⋂K k=1 G 
p k 
] ≥ 1 − δ′ Then set δ = 2δ′ 
and we have the desired result. 
C.2 Regret analysis 
Proof. Similar to the case of (s, a)-rectangular set, we start with decomposing the regret as follows, 
Regret(K) = 
K∑ k=1 
V ∗1 (s)− V πk 1 (s) 
= K∑ k=1 
( V ∗1 (s)− V̂ πk 
1 (s) ) 
+ ( V̂ πk 1 (s)− V πk 
1 (s) ) . 
By Lemma 2 and Lemma 9, with probability at least 1− δ, we have 
Regret(K) = O ( H2 √ K logA 
) +O 
( SH 
ρc 
√ AK log(SAH4K3/2/δ) 
) = O 
( SH 
ρc 
√ AK log(SAH4K3/2/δ) 
) , 
where c is the minimal element of P oh , over all h ∈ [H]. 
Lemma 9. With Algorithm 1, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( 1 
ρc SH √ AK log(SAH4K3/2/δ) 
) . 
Proof. Similar to the case with (s, a)-rectangular uncertainty set, for any k, we can decompose (V̂ πk 
1 − V̂ πk 1 )(s) as, 
(V̂ πk 1 − V̂ πk 
1 )(s) ≤ H∑ h=1 
Eπk,{pt}ht=1 
[ (rkh(s, a)− r̂kh(s, a)) + 
( σP̂h(s) 
( V̂ πk h+1 
) (s)− σPh(s) 
( V̂ πk h+1 
) (s) ) 
+ bkh(s, a) ] . 
30
Thus by the design of our bonus function and with probability at least 1− δ, we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) 
≤ 2 K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[ bkh(s, a) 
] = H 
√ K +O 
( 1 
ρc 
√ S log(SAH4K3/2/δ) 
) K∑ k=1 
H∑ h=1 
Eπk,{pt}ht=1 
[√ 1 
Nk h (s, a) 
] , 
where c is a problem dependent constant. By Lemma 12, we have the bound of visitation counts: 
K∑ k=1 
H∑ h=1 
√ 1 
Nk h (s, a) 
≤ 2H √ SAK . 
Combining everything, conditioned on the good event we have 
K∑ k=1 
(V̂ πk 1 − V πk 
1 )(s) = O 
( SH 
ρc 
√ AK log(SAH4K3/2/δ) 
) . 
Lemma 10. For any h, k, s, a, the following inequality holds with probability at least 1− δ, 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ 
2H 
ρc 
√ 4S log(8SAH4K2/δ′ρ) 
Nk h (s, a) 
+ 1√ K . 
where c is the minimal element of P oh . 
Proof. By the definition of σPh(s) 
( V̂ πk h+1 
) (s) = inf 
Ph∈Ph 
∑ s′ Ph(s′ | s, a)V̂ πk 
h+1(s ′), we consider the 
following optimization problem: 
min Ph 
∑ s′ 
Ph(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′ Ph(s′ | s, a) log ( Ph(s 
′|s,a) P oh (s 
′|s,a) 
) ≤ ρ ,∑ 
s′ Ph(s′ | s, a) = 1 , P oh(· | s, a) > 0, Ph(· | s, a) ≥ 0 . 
Let P̃h(s′ | s, a) = Ph(s ′|s,a) 
P oh (s ′|s,a) , we can rewrite the above optimization problem as 
min P̃h 
∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) 
s.t. 
 ∑ 
s′ P̃h(s′ | s, a′)P oh(s′ | s, a′) log ( P̃h(s′ | s, a) 
) ≤ ρ ,∑ 
s′ P̃h(s′ | s, a′)P oh(s′ | s, a) = 1 , 
P̃h(· | s, a) ≥ 0 . 
31
Use the Lagrangian multiplier method and f(x) = x log x, we have the Lagrangian L(P̃h, η, λ) with multiplier η ∈ R, λ ≥ 0, 
L(P̃h, η, λ)(s, a) 
= ∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)V̂ πk h+1(s 
′) + λ 
(∑ s′ 
P̃h(s′ | s, a′)P oh(s′ | s, a′) log(P̃h(s′ | s, a))− ρ 
) 
− η 
(∑ s′ 
P̃h(s′ | s, a)P oh(s′ | s, a)− 1 
) 
= − λρ+ η + λ ∑ s′ 
P oh(s′ | s, a) 
( f ( P̃h(s′ | s, a′) 
) − P̃h(s′ | s, a′) 
( η − V πk 
h+1(s ′) 
λ 
)) . 
The convex conjugate of f is f∗(y) = max x 〈x, y〉 − f(x). Using f∗, we can thus optimize over 
P̃h and rewrite the Lagrangian over as 
L(η, λ)(s, a) = min P̃h 
L(P̃h, η, λ)(s, a) = −λρ+ η − λ ∑ s′ 
P oh(s′ | s, a)f∗ ( η − V πk 
h+1(s ′) 
λ 
) . 
Conditioned on x ≥ 0, f(x) = x log x, notice that the conjugate f∗(y) has the following closed form, 
f∗(y) = max x 〈x, y〉 − f(x) = exp(y − 1) . 
Using the closed form of f∗(y), we can rewrite the optimization problem as 
L(η, λ)(s, a) = −λρ+ η − λ ∑ s′ 
P oh(s′ | s, a)f∗ ( η − V πk 
h+1(s ′) 
λ 
) 
= −λρ+ η − λ ∑ s′ 
P oh(s′ | s, a) exp 
( η − V πk 
h+1(s ′)− λ 
λ 
) . 
Taking the derivative of η, 
∂L 
∂η = 1− 
∑ s′ 
P oh(s′ | s, a) exp 
( η − V πk 
h+1(s ′)− λ 
λ 
) = 0 , 
η = λ− λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) . 
Directly optimize over η, we can reduce the problem to 
L(λ)(s, a) = λ(1− ρ)− λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) − λ , 
= −λρ− λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) . 
32
Define g(λ, P oh) = −L(λ)(s, a) as 
g(λ, P oh) = λρ+ λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) . 
Note that the Lagrangian multiplier λ ≥ 0. Then we prove g is bounded within [−H,H] over [0, H/ρ]. 
g(λ, P oh) = λρ+ λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) , 
≤ λρ+ λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
( −0 
λ 
)) , 
= λρ ≤ H , 
where the first inequality follows from V πk h+1(s 
′) ≥ 0 and the second inequality is by λ ≤ H/ρ. 
g(λ, P oh) = λρ+ λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) , 
≥ λρ+ λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
( −H λ 
)) , 
= λρ−H ≥ −H , 
where the first inequality follows from V πk h+1(s 
′) ≤ H and the second inequality is by λ ≥ 0. Moreover, from the induction above we know that for any P , g(0, P ) ≤ 0 and for λ > H/ρ, 
g (λ, P ) ≥ λρ+ λ log(exp(−H/λ)) > 0 . 
Therefore, g achieves its minimum over λ ∈ [0, H/ρ]. We remark that the same form is also used for sample complexity results ( [Badrinath and Kalathil, 2021, Yang et al., 2021]). 
We can now rewrite 
σP̂h(s) 
( V̂ πk h+1 
) (s)− σPh(s) 
( V̂ πk h+1 
) (s) = min 
0≤λ1≤H/ρ g ( λ1, P̂ 
o,k h 
) − min 
0≤λ2≤H/ρ g (λ2, P 
o h) 
≤ max 0≤λ≤H/ρ 
∣∣∣g (λ, P̂ o,kh ) − g (λ, P oh) 
∣∣∣ . By Nilim and El Ghaoui [2005] (Appendix C), when λ = 0, g 
( λ, P̂ o,kh 
) = g (λ, P oh) = mins∈S V 
πk h+1(s). 
Therefore, it suffice to bound over maxc≤λ≤H/ρ 
∣∣∣g (λ, P̂ o,kh ) − g (λ, P oh) 
∣∣∣, where c > 0. We now have∣∣∣g (λ, P̂ o,kh ) − g (λ, P oh) 
∣∣∣ = 
∣∣∣∣∣λ log 
(∑ s′ 
P̂ o,kh (s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
)) − λ log 
(∑ s′ 
P oh(s′ | s, a) exp 
(−V πk h+1(s 
′) 
λ 
))∣∣∣∣∣ 33
= ∣∣∣∣∣∣∣∣λ log 
1 + 
∑ s′(P̂ 
o,k h (s′ | s, a)− P oh(s′ | s, a)) exp 
( −V πkh+1(s 
′) 
λ 
) ∑ 
s′ P o h(s′ | s, a) exp 
( −V πkh+1(s 
′) 
λ 
)  ∣∣∣∣∣∣∣∣ 
≤ 2λ 
∣∣∣∣∣∣∣∣ ∑ 
s′(P̂ o,k h (s′ | s, a)− P oh(s′ | s, a)) exp 
( −V πkh+1(s 
′) 
λ 
) ∑ 
s′ P o h(s′ | s, a) exp 
( −V πkh+1(s 
′) 
λ 
) ∣∣∣∣∣∣∣∣ 
≤ 2λmax s′ 
∣∣∣∣∣ P̂ o,kh (s′ | s, a)− P oh(s′ | s, a) 
P oh(s′ | s, a) 
∣∣∣∣∣ where the first inequality follows from | log(1 + x)| ≤ 2|x| and the second inequality follows from the Holder’s inequality. 
By Hoeffding’s inequality and an union bound over all s, a′, Nk h (s, a), the following inequality 
holds with probability at least 1− δ, 
max s′ 
∣∣∣P̂ o,kh (s′ | s, a)− P oh(s′ | s, a) ∣∣∣ ≤ ∥∥∥P̂ o,kh (· | s, a)− P oh(· | s, a) 
∥∥∥ 1 ≤ 
√ 4S log(SAH2K/δ) 
Nk h (s, a) 
. 
Then we create an ε-net Nε(λ) with g over λ ∈ [0, H/ρ] such that 
max λ∈[0,H/ρ] 
|g(λ, P̂ o,kh )− g(λ, P oh)| ≤ max λ∈Nε(η) 
|g(λ, P̂ o,kh )− g(λ, P oh)|+ 2ε . 
Then we know that |Nε(λ)| is bounded by the area of the rectangle [0, H/ρ]× [−H,H] over ε2, 
|Nε(λ)| ≤ 2H2 
ρε2 . 
Taking an union bound over Nε(λ) and denote c = min s′ P oh(· | s, a), we have the following 
inequality happens with at least 1− δ′ probability: 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ max 
λ∈[0,H/ρ] |g(λ, P̂ o,kh )− g(λ, P oh)| 
≤ max λ∈Nε(λ) 
|g(λ, P̂ o,kh )− g(λ, P oh)|+ 2ε 
≤ 2 H 
ρ max s′ 
∣∣∣∣∣ P̂ o,kh (s′ | s, a)− P oh(s′ | s, a) 
P oh(s′ | s, a) 
∣∣∣∣∣+ 2ε 
≤ 2 H 
ρc 
√ 4S log(2SAH4K/δ′ρε2) 
Nk h (s, a) 
+ 2ε , 
Take ε = 1 2 √ K 
, then 
σP̂h(s)(V̂ πk h+1)(s)− σPh(s)(V̂ 
πk h+1)(s) ≤ 2 
H 
ρc 
√ 4S log(8SAH4K2/δ′ρ) 
Nk h (s, a) 
+ 1√ K . 
34
D Proof of Proposition 1 
Claim 4.1 (Suboptimality of non-robust optimal policy). There exists a robust MDP M = 〈S,A,P, r,H〉 with uncertainty set P of uncertainty radius ρ, such that the non-robust optimal policy is Ω(1)-suboptimal to the uniformly random policy. 
Proof. We consider a robust MDP with three states s0, s1, s2 and two actions a0, a1. Without loss of generality, we let s0 be the initial state. On the initial state s0, both actions will lead to a reward of 0. On state s1, a reward of 1/(H − 1) is given for both actions. On state s2, a reward of −1/(H−1) is given for both actions. The nominal transition dynamic of the MDP is the following. Taking action a0 on s0 will be transited to s1 with a probability of ε and be transited to s2 with a probability of ε, while ε > 0.5. Taking the other action a1 will have equal probability of transiting to s1 and s2. The states s1 and s2 are absorbing, in the sense that taking any action on these two states will be transited by to the same state. The transition of the MDP is also illustrated in Figure 3, where a dashed line denotes a probabilistic transition and a solid line denotes deterministic transition. With the nominal transition, it is clear that an optimal policy would be always taking 
Figure 3: The left figure describes the nominal transition dynamic of the MDP. The right figure describes the robust transition dynamic of the MDP. 
a0. Denote this policy as πo,∗, the value for this policy under nominal transition over K episodes is 
V πo,∗(s0) = K(H − 1) 
( ε · 1 
H − 1 − (1− ε) · 1 
H − 1 
) = 2ε− 1 > 0 , 
where the last inequality is due to ε > 0. However, consider the uncertainty radius ρ and the robust transition denoted by the right figure 
of Figure 3. That is, taking a0 on s0 will leads to a transition to s1 with probability ε− ρ/2 and to s2 with probability 1−ε+ρ/2. Note that as ε > 0.5, ρ ≤ 1, ε−ρ/2 > 0. Moreover, this transition is indeed the worst case transition for any non-uniform policy. Let Ṽ denotes the robust value under the above described transition. With a uniform policy π, the value of it under this transition is 
Ṽ π(s0) = K(H − 1) 
( 0.5 ( ε− ρ 
2 
) · 1 
H − 1 − 0.5 
( 1− ε+ 
ρ 
2 
) ) · 1 
H − 1 
) = ε− ρ/2− 0.5 . 
The value of πo,∗ is, however, 
Ṽ πo,∗(s0) = K(H − 1) 
(( ε− ρ 
2 
) · 1 
H − 1 − ( 
1− ε+ ρ 
2 
) ) · 1 
H − 1 
) = 2ε− ρ− 1 . 
35
For any 2ε− 1 ≤ ρ ≤ 1, we have Ṽ πo,∗(s0) ≤ Ṽ π(s0). Since ε > 0.5 is arbitrary, the optimal policy under the nominal transition is non-robust even under the slightest perturbation. 
36
E Auxiliary lemmas 
Lemma 11 (Bartlett [2013]). An ε-cover of a subset T of a pseudometric space (S, d) is a set T̂ ⊂ T such that for each t ∈ T there is a t̂ ∈ T̂ such that d(t, t̂) ≤ ε. The ε-covering number of T is 
N(ε, T, d) = min { |T̂ | : T̂ is an ε-cover of T 
} . 
Let Fd be the set of L-Lipschitz functions (wrt ‖ · ‖∞ ) mapping from [0, 1]d to [0, 1]. Then 
logN (ε, Fd, ‖ · ‖∞) = Θ 
(( L 
ε 
)d) . 
Lemma 12 (Lemma 7.5 Agarwal et al. [2019]). For arbitrary K sequence of trajectories {skh, akh}Hh=1, k = 1, . . . ,K, we have 
K∑ k=1 
H∑ h=1 
1√ Nk h (skh, a 
k h) ≤ 2H 
√ SAK . 
Proof. We have 
K∑ k=1 
H∑ h=1 
1√ Nk h 
( skh, a 
k h 
) = H∑ h=1 
∑ (s,a)∈S×A 
NK h (s,a)∑ i=1 
1√ i 
≤ 2 H∑ h=1 
∑ (s,a)∈S×A 
√ NK h (s, a) 
≤ H∑ h=1 
√ SA 
∑ s,a 
NK h (s, a) 
= H √ SAK , 
where the first inequality is by ∑N 
i=1 1√ i ≤ 2 √ N and the second inequality follows by Cauchy-
Schwarz inequality. 
Lemma 13 (Fundamental inequality of Online Mirror Descent for RL (Lemma 17 Shani et al. [2020])). Let β > 0. Let π1h(· | s) be the uniform distribution. Then, by updating with OMD and with KL divergence regularization, for any k ∈ [K], h ∈ [H] and s ∈ S, the following holds for any stationary policy π, 
K∑ k=1 
〈 Qkh(· | s), πkh(· | s)− πh(· | s) 
〉 ≤ logA 
β + β 
2 
K∑ k=1 
∑ a 
πkh(a | s) ( Qkh(s, a) 
)2 . (7) 
37
F More experimental details 
Other configurations and set up The episode length is set to 20 and all algorithms are trained with 3000 episodes. The evaluation results are averaged over 20 runs and is presented with 1 standard deviation. All experiments are conducted with 64 core ADM 3990X. 
Results with KL divergence uncertainty sets With the uncertainty set described with KL divergence, we present the following experimental results. All other configurations and set up remains the same with those for uncertainty set with `1 distance. 
(a) ρ = 0.1 (b) ρ = 0.2 (c) ρ = 0.3 
Figure 4: Cumulative rewards obtained by robust and non-robust policy optimization on robust transition with different level of uncertainty ρ = 0.1, 0.2, 0.3 under KL divergence. 
38