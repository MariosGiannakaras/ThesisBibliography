> Source: https://proceedings.mlr.press/v134/wei21b/wei21b.pdf

Proceedings of Machine Learning Research vol 134:1–55, 2021 34th Annual Conference on Learning Theory 
Non-stationary Reinforcement Learning without Prior Knowledge: An Optimal Black-box Approach 
Chen-Yu Wei CHENYU.WEI@USC.EDU 
Haipeng Luo HAIPENGL@USC.EDU 
University of Southern California 
Editors: Mikhail Belkin and Samory Kpotufe 
Abstract We propose a black-box reduction that turns a certain reinforcement learning algorithm with optimal regret in a (near-)stationary environment into another algorithm with optimal dynamic regret in a non-stationary environment, importantly without any prior knowledge on the degree of nonstationarity. By plugging different algorithms into our black-box, we provide a list of examples showing that our approach not only recovers recent results for (contextual) multi-armed bandits achieved by very specialized algorithms, but also significantly improves the state of the art for (generalized) linear bandits, episodic MDPs, and infinite-horizon MDPs in various ways. Specifi-cally, in most cases our algorithm achieves the optimal dynamic regret Õ(min{ 
√ LT ,∆1/3T 2/3}) 
where T is the number of rounds and L and ∆ are the number and amount of changes of the world respectively, while previous works only obtain suboptimal bounds and/or require the knowledge of L and ∆. 
1. Introduction 
Most existing works on reinforcement learning consider a stationary environment and aim to find or be comparable to an optimal policy (known as having low static regret). In many applications, however, the environment is far from being stationary. In these cases, it is much more meaningful to minimize dynamic regret, the gap between the total reward of the optimal sequence of policies and that of the learner. Indeed, there is a surge of studies on this topic recently (Jaksch et al., 2010; Gajane et al., 2018; Li and Li, 2019; Ortner et al., 2020; Cheung et al., 2020; Fei et al., 2020; Domingues et al., 2021; Mao et al., 2021; Zhou et al., 2020; Touati and Vincent, 2020). 
One common issue of all these works, however, is that their algorithms crucially rely on having some prior knowledge on the degree of non-stationarity of the world, such as how much or how many times the distribution changes, which is often unavailable in practice. Cheung et al. (2020) develop a Bandit-over-Reinforcement-Learning (BoRL) framework to relax this assumption, but it introduces extra overhead and leads to suboptimal regret. Indeed, as discussed in their work, there are multiple aspects (which they call endogeneity, exogeneity, uncertainty, and bandit feedback) combined in non-stationary reinforcement learning that make the problem highly challenging. 
For bandit problems, the special case of reinforcement learning, the works of Auer et al. (2019) and Chen et al. (2019) are the first to achieve near-optimal dynamic regret without any prior knowledge on the degree of non-stationarity. The same technique has later been adopted by Chen et al. (2020) for the case of combinatorial semi-bandits. Their algorithms maintain a distribution over arms (or policies/super-arms in the contextual/combinatorial case (Chen et al., 2019, 2020)) with properly controlled variance for all reward estimators. This approach is generally incompatible with standard reinforcement learning algorithms, which are usually built upon the optimism in the face 
© 2021 C.-Y. Wei & H. Luo.
WEI LUO 
of uncertainty principle and do not maintain a distribution over policies (see also (Lykouris et al., 2021; Wang et al., 2020) for related discussions). Another drawback is that their algorithms are very specialized to their problems, and it is highly unclear whether the ideas can be extended to other problems. 
In this work, we address all these issues and make significant progress in this direction. Specif-ically, we propose a general approach that is applicable to various reinforcement learning settings (including bandits, episodic MDPs, infinite-horizon MDPs, etc.) and achieves optimal dynamic regret without any prior knowledge on the degree of non-stationarity. Our approach, called MASTER, is a black-box reduction that turns any algorithm with optimal performance in a (near-)stationary environment and additionally some mild requirements into another algorithm with optimal dynamic regret in a non-stationary environment, again, without the need of any prior knowledge. For example, all existing UCB-based algorithms satisfy the conditions of our reduction and are readily to be plugged into our black-box. 
Applications and comparisons To showcase the versatility of our approach, we provide a list of examples by considering different settings and applying our reduction with different base algorithms. These examples, summarized in Table 1, recover the results of Auer et al. (2019) and Chen et al. (2019) for (contextual) multi-armed bandits, and more importantly, improve the best known results for (generalized) linear bandits, episodic MDPs, and infinite-horizon MDPs in various ways. More specifically, letL and ∆ be the number and amount of changes of the environment respectively (see Section 2.1 for formal definition). For all settings except infinite-horizon MDPs, ignoring other parameters, our algorithms achieve dynamic regret min{Reg?L,Reg?∆} without knowing L and ∆, where Reg?L = 
√ LT , Reg?∆ = ∆1/3T 2/3 + 
√ T , and T is the number of rounds. These bounds are 
known to be optimal even when L and ∆ are known, and they improve over (Cheung et al., 2019; Russac et al., 2019; Kim and Tewari, 2020; Zhao et al., 2020; Zhao and Zhang, 2021) for linear bandits, (Russac et al., 2020; Faury et al., 2021) for generalized linear bandits, (Mao et al., 2021) for episodic tabular MDPs, and (Touati and Vincent, 2020; Zhou et al., 2020) for episodic linear MDPs. For infinite-horizon MDPs, we achieve the same optimal regret when the maximum diameter of the MDPs is known, or when L and ∆ are known, improving over the best existing results by (Gajane et al., 2018) and (Cheung et al., 2020). When none of them is known, we can still adopt the BoRL technique (Cheung et al., 2020) with the price of paying extra T 3/4 regret, which is suboptimal but still outperforms best known results. 
In particular, we emphasize that achieving dynamic regret Reg?L beyond (contextual) multiarmed bandits is one notable breakthrough we make. Indeed, even when L is known, previous approaches based on restarting after a fixed period, a sliding window with a fixed size, or discounting with a fixed discount factor, all lead to a suboptimal bound of Õ(L1/3T 2/3) at best (Gajane et al., 2018). Since this bound is subsumed by Reg?∆, related discussions are also often omitted in previous works. 
We also emphasize that when dealing with problems with linear structures (including linear bandits, generalized linear bandits, and linear MDPs), our bounds Reg?∆ is also new even when ∆ is known. Indeed, although several existing works on non-stationary linear bandits (Cheung et al., 2019; Russac et al., 2019; Kim and Tewari, 2020; Zhao et al., 2020) claim that their algorithms achieve the bound Reg?∆, there is in fact a technical flaw in all of them, as explained and corrected recently in (Zhao and Zhang, 2021; Touati and Vincent, 2020). After the correction, their bounds all deteriorate to ∆1/4T 3/4 + 
√ T , which is no longer near-optimal. On the other hand, our approach not 
2
BLACK-BOX NON-STATIONARY RL 
Table 1: A summary of our results and comparisons with the state-of-the-art. Our algorithms are named in the form of “MASTER + X” where X is the base algorithm used in our reduction. Here, Reg?L = 
√ LT and Reg?∆ = ∆1/3T 2/3 + 
√ T , where T is the number of rounds and L and ∆ are 
the number and amount of changes of the world respectively (dependence on other parameters is omitted). Dmax is the maximum diameters of the MDPs. 
Setting Algorithm Regret in Õ(·) Required knowledge 
Multi-armed bandits (Auer et al., 2019) Reg?L MASTER + UCB1 min{Reg?L,Reg?∆} 
Contextual bandits (Chen et al., 2019) 
min{Reg?L,Reg?∆}MASTER + ILTCB MASTER + FALCON 
Linear bandits (Cheung et al., 2019) ∆1/4T 3/4 + 
√ T ∆ 
(Cheung et al., 2019) ∆1/4T 3/4 + T 3/4 
MASTER + OFUL min{Reg?L,Reg?∆} 
Generalized linear bandits (Russac et al., 2020) L1/3T 2/3 L 
(Faury et al., 2021) ∆1/5T 4/5 + T 3/4 
MASTER + GLM-UCB min{Reg?L,Reg?∆} Episodic MDPs (tabular case) 
(Mao et al., 2021) Reg?∆ ∆ 
MASTER + Q-UCB min{Reg?L,Reg?∆} Episodic MDPs 
(linear case) (Touati and Vincent, 2020) ∆1/4T 3/4 + 
√ T ∆ 
MASTER + LSVI-UCB min{Reg?L,Reg?∆} 
Infinite-horizon communicating MDPs 
(tabular case) 
(Gajane et al., 2018) L1/3T 2/3 L 
(Cheung et al., 2020) ∆1/4T 3/4 + √ T ∆ 
(Cheung et al., 2020) ∆1/4T 3/4 + T 3/4 
MASTER + UCRL Reg?L or Reg?∆ L or ∆ 
MASTER + UCRL min{Reg?L,Reg?∆} Dmax 
MASTER + UCRL + BoRL min{Reg?L,Reg?∆}+ T 3/4 
only sidesteps the difficulty of getting the optimal bound met in all these works, but also avoids the requirement of knowing ∆. Similar technical difficulties also appear in generalized linear bandits (Russac et al., 2020; Faury et al., 2021) and linear MDPs (Touati and Vincent, 2020; Zhou et al., 2020), and our approach overcomes them similarly. 
High-level ideas The high-level idea of our reduction is to schedule multiple instances of the base algorithm with different durations in a carefully-designed randomized scheme, which facilitates non-stationarity detection with little overhead. A related and well-known approach for nonstationary environments is to maintain multiple instances of a base algorithm with different parameter tunings or different starting points and to learn the best of them via another “expert” algorithm, which can be very successful when learning with full information (Hazan and Seshadhri, 2007; Luo 
3
WEI LUO 
and Schapire, 2015; Daniely et al., 2015; Jun et al., 2017) but is suboptimal and has many limitations when learning with partial information (Luo et al., 2018; Cheung et al., 2019, 2020). Our approach is different as we do not try to learn the best instance; instead, we always follow the decision suggested by the instance with the currently shortest scheduled duration, and also only update this instance after receiving feedback from the environment. The is because base algorithms with shorter duration are responsible for detecting larger distribution changes, and always following the shortest one ensure that it is not blocked by the longer ones and thus every scale of distribution change is detected in a timely manner. 
Another related approach is regret balancing, developed recently for model selection in bandit problems (Abbasi-Yadkori et al., 2020; Pacchiano et al., 2020). The idea is also to run multiple base algorithms in parallel, each with a putative regret upper bound. The learner executes one of them in each round which incurs the least regret so far, and also constantly compares the performance among base algorithms, eliminating those whose putative regret bounds are violated. While our algorithm resembles regret balancing in some aspects, the way it chooses the base algorithm in each round is clearly quite different, which is also crucial for our problem. 
Other related work There are also a series of works on learning MDPs with adversarial rewards and a fixed transition (Even-Dar et al., 2009; Neu et al., 2010; Arora et al., 2012; Neu et al., 2012; Dekel and Hazan, 2013; Neu et al., 2013; Zimin and Neu, 2013; Dick et al., 2014; Rosenberg and Mansour, 2019; Cai et al., 2020; Jin et al., 2020a; Shani et al., 2020; Rosenberg and Mansour, 2020; Lee et al., 2020; Jin and Luo, 2020; Chen et al., 2021; Lancewicki et al., 2020). These models can potentially handle non-stationarity in the reward function but not the transition kernel (in fact, most of these works also only consider static regret). Lykouris et al. (2021) investigate an episodic MDP setting where an adversary can corrupt both the reward and the transition for up to L′ episodes, and achieve dynamic regret Õ(min{L′ 
√ T , L′/gap}) without knowing L′, where gap is the minimal 
suboptimality gap and could be arbitrarily small. Since corruption of up to L′ episodes implies that the world changes at most L = 2L′ times, our result improves theirs from Õ(L′ 
√ T ) to Õ( 
√ L′T ) 
when 1/gap > √ T . On the other hand, it is possible that L is much smaller than L′ (e.g. L = Θ(1) 
while L′ = Θ(T )), in which case our results are also significantly better. 
2. Problem Setting, Main Results, and High-level Ideas 
Throughout the paper, we fix a probability parameter δ of order 1/poly(T ), and write h1(x) = Õ(h2(x)) or h2(x) = Ω̃(h1(x)) if h1(x) = O (poly(log(T/δ))h2(x)). We say “with high probability, h1 = Õ(h2(x))” if “with probability 1 − δ, h1 = Õ(h2(x))”. For an integer n, we denote the set {1, 2, . . . , n} by [n]; and for integers s and e, we denote the set {s, s+ 1, . . . , e} by [s, e]. 
2.1. Problem setting 
We consider the following general reinforcement learning (RL) framework that covers a wide range of problems. Ahead of time, the learner is given a policy set Π, and the environment decides T reward functions f1, . . . , fT : Π → [0, 1] unknown to the learner. Then, in each round t = 1, . . . , T , the learner chooses a policy πt ∈ Π and receives a noisy reward Rt ∈ [0, 1] whose mean is ft(πt).1 The dynamic regret of the learner is defined as D-REG = 
∑T t=1 (f?t −Rt), where 
f?t = maxπ∈Π ft(π) is the expected reward of the optimal policy for round t. 
1. The range [0, 1] is only for simplicity. Our results can be directly extended to the case with sub-Gaussian noise. 
4
BLACK-BOX NON-STATIONARY RL 
Many heavily-studied problems fall into this framework. For example, in the classic multiarmed bandit problem (Lai and Robbins, 1985), it suffices to treat each arm as a policy; for finitehorizon episodic RL (e.g. (Jin et al., 2018)), each state-to-action mapping is considered as a policy, and ft(π) is the expected reward of executing π in the t-th episode’s MDP with some transition kernel and some reward function. See more examples in Appendix I. Note that our framework ignores many details of the actual problem we are trying to solve (e.g. not even mentioning the MDPs for RL). This is because our results only rely on certain guarantees provided by a base algorithm, making these details irrelevant to our presentation. There is also some technicality to fit the infinite-horizon RL problem into our framework, which we will discuss in detail in Section 4. 
Non-stationarity measure A natural way to measure the distribution drift between rounds t and t+ 1 is to see how much the expected reward of any policy could change, that is, maxπ∈Π |ft(π)− ft+1(π)|. However, to make our results more general, we take a sligtly more abstract way to define non-stationarity whose exact form eventually depends on what guarantees the base algorithm can provide for a concrete problem. To this end, we define the following. 
Definition 1 ∆ : [T ] → R is a non-stationarity measure if it satisfies ∆(t) ≥ maxπ∈Π |ft(π) − ft+1(π)| for all t. Define for any interval I = [s, e], ∆I = 
∑e−1 τ=s ∆(τ) (note ∆[s,s] = 0) and 
LI = 1 + ∑e−1 
τ=s 1[∆(τ) 6= 0]. With slight abuse of notation, we write ∆ = ∆[1,T ] and L = L[1,T ]. 
Base algorithm and requirements As mentioned, our approach takes a base algorithm that tackles the problem when the environment is (near-)stationary, and turns it into another algorithm that can deal with non-stationary environments. Throughout the paper, we denote the base algorithm by ALG and assumes that it satisfies the following mild requirements when run alone. 
Assumption 1 ALG outputs an auxiliary quantity f̃t ∈ [0, 1] at the beginning of each round t. There exist a non-stationarity measure ∆ and a non-increasing function ρ : [T ] → R such that running ALG satisfies the following: for all t ∈ [T ], as long as ∆[1,t] ≤ ρ(t), without knowing ∆[1,t] 
ALG ensures with probability at least 1− δ T : 
f̃t ≥ min τ∈[1,t] 
f?τ −∆[1,t] and 1 
t 
t∑ τ=1 
( f̃τ −Rτ 
) ≤ ρ(t) + ∆[1,t]. (1) 
Furthermore, we assume that ρ(t) ≥ 1√ t 
and C(t) = tρ(t) is a non-decreasing function. 
We unpack the meaning of this assumption and explain why this is a mild requirement via a few remarks below, followed by examples of existing algorithms that do satisfy our assumption. 
First, consider choosing ∆(t) = maxπ∈Π |ft(π)−ft+1(π)| and see what the assumption means for a stationary environment with ft = f and ∆(t) = 0 for all t. In this case, Eq. (1) simply becomes f̃t ≥ maxπ∈Π f(π) and 
∑t τ=1 
( f̃τ −Rτ 
) ≤ C(t), which are standard properties of 
Upper-Confidence-Bound (UCB)-based algorithms, where f̃t is an optimistic estimator of the optimal reward and C(t) is the regret bound usually of order 
√ t. In fact, even for non-UCB-based 
algorithms that do not explicitly maintain optimistic estimators, by looking into their analysis, it is still possible to extract a quantity f̃t satisfying these two properties (see our example for contextual bandits in Appendix I). We also note that this requirement for the special stationary case is in fact all we need to achieve our claimed regret bound Reg?L. 
5
WEI LUO 
Second, to simultaneously achieve the regret bound Reg?∆ as well, we require slightly more from the base algorithm: in a near-stationary environment with ∆[1,t] ≤ ρ(t), the two aforementioned properties still hold approximately with degradation ∆[1,t] (that is, Eq. (1)).2 We call this a nearstationary environment because ∆[1,t] can be of order Θ(t) in a highly non-stationary environment, while here we restrict it to be at most ρ(t), which is non-increasing in t (and in fact of order 1/ 
√ t 
in all our examples). To the best of our knowledge, all UCB-based algorithms satisfy Assumption 1 with some suitable choice of ∆. The fact that we only require Eq. (1) to hold for near-stationary environments is the key to bypassing the technical difficulty of getting the optimal bound Reg?∆ met in (Cheung et al., 2019; Russac et al., 2019; Zhao et al., 2020; Russac et al., 2020; Faury et al., 2021; Touati and Vincent, 2020; Zhou et al., 2020) for linear bandits, generalized linear bandits, and linear MDPs, as mentioned in Section 1. 
Finally, noting that ρ(t) and C(t) represent an average and an cumulative regret bound respectively, the monotonicity requirement on them is more than natural. The requirement ρ(t) ≥ 1√ 
t is also usually unavoidable without further structures in the problem. Note that while we write ρ and C as a function of t only, they can depend on log(1/δ), log T , the complexity of Π, and other problem-dependent parameters such as the number of states/actions of an MDP. 
Following the order in Table 1, we now give a list of existing algorithms that satisfy Assump-tion 1 in different problem settings with proper non-stationarity measure ∆ and regret bound C. We defer the concrete form of f̃t (which requires introducing other notations) and all the proofs to Appendix I. 
 UCB1 (Auer et al., 2002a): C(t) = Õ( √ At+A) and ∆(t) = Θ(‖rt − rt+1‖∞), where A is 
the number of arms, and rt is the expected reward vector at time t. 
 ILTCB (Agarwal et al., 2014, short for ILOVETOCONBANDITS):C(t) = Õ( √ At log |Π|+ 
A log |Π|) and ∆(t) = Θ (∫ r 
∫ x |Dt(x, r)−Dt+1(x, r)|dxdr 
) , where A is the number of 
actions and Dt is the joint distribution of the context-reward pair (x, r) at time t. 
 FALCON (Simchi-Levi and Xu, 2020): C(t) = Õ( √ At log |Φ| + A log |Φ|) and ∆(t) = 
Θ( √ Amaxx,a |φ?t (x, a) − φ?t+1(x, a)| + 
∫ x |Dt(x) − Dt+1(x)|dx), where A is the number 
of actions, Φ is the set of regressors (each of which maps a context-action pair to a predicted reward), φ?t ∈ Φ is the true regressor at time t, and Dt is the distribution of contexts at time t. 
 OFUL (Abbasi-Yadkori et al., 2011): C(t) = Õ ( d √ t ) 
and ∆(t) = Θ̃(d‖θt−θt+1‖2), where d is the feature dimension and θt ∈ Rd parameterizes the linear reward function at time t. 
 GLM-UCB (Filippi et al., 2010): C(t) = Õ ( kµd cµ 
√ t ) 
and ∆(t) = Θ̃ ( k2µd 
cµ ‖θt − θt+1‖2 
) , 
where d is the feature dimension, θt ∈ Rd parameterizes the linear reward function at time t, and kµ, cµ are the upper and lower bounds of the gradient of the link function. 
 Q-UCB (Jin et al., 2018, short for Q-learning UCB-H):3 C(t) = Õ( √ H5SAt + H3SA) 
and ∆(t) = Θ(H ∑H 
h=1 maxs,a |rth(s, a) − rt+1 h (s, a)| + H2 
∑H h=1 maxs,a ‖pth(·|s, a) − 
pt+1 h (·|s, a)‖1), where H , S and A are the numbers of layers, states, and actions of the MDP 
respectively, and pth and rth are the transition and reward functions for layer h of episode t. 
2. We use minτ∈[1,t] f ? τ instead of the more natural one f?t since the former is weaker and the difference between these 
two is at most ∆[1,t] anyway. 3. For ease of comparison, here, the reward range is changed from [0, 1] to the more common [0, H]. 
6
BLACK-BOX NON-STATIONARY RL 
 LSVI-UCB (Jin et al., 2020b):4 C(t) = Õ( √ d3H4t) and ∆(t) = Θ̃(dH 
∑H h=1 ‖θth − 
θt+1 h ‖2 + dH2 
∑H h=1 ‖µth − µt+1 
h ‖F ), where d is the feature dimension, H is the number of layers, and θth and µth are the parameters of the linear MDP for layer h of episode t. 
2.2. Main results 
Our main result is that, with an algorithm satisfying Assumption 1 at hand, our proposed black-box reduction, MASTER (Algorithm 3), ensures the following dynamic regret bound. 
Theorem 2 If Assumption 1 holds with C(t) = c1t p + c2 for some p ∈ [1 
2 , 1) and c1, c2 > 0, then MASTER (Algorithm 3), without knowing L and ∆, guarantees with high probability: 
D-REG = Õ ( 
min 
{( c1 + 
c2 
c1 
)√ LT , 
( c 2/3 1 + c2c 
−4/3 1 
) ∆ 
1/3T 2/3 + 
( c1 + 
c2 
c1 
)√ T 
}) when p = 1 
2 , and D-REG = Õ ( 
min { c1L 
1−pT p, ( c1∆1−pT 
) 1 2−p + c1T 
p }) 
when p > 1 2 (omit-
ting some lower-order terms). 
For ease of presentation, in this theorem we assume that C(·) takes a certain form that is common in the literature and holds for all our examples with p = 1 
2 . Applying this theorem to all the examples discussed earlier, we achieve all the optimal min{Reg?L,Reg?∆} bounds listed in Ta-ble 1 (except for infinite-horizon MDPs which will be discussed in Section 4). Our definitions of L are the same as in previous works, and our definitions of ∆ are sometimes larger by some problem-dependent factors (such as d andH) in order to fit Assumption 1. More specifically, for (contextual) bandits, our MASTER combined with UCB1 and ILTCB recovers the same optimal bounds (in terms of all parameters) achieved by (Auer et al., 2019; Chen et al., 2019). MASTER with FALCON obtains a similar bound as in (Chen et al., 2019) but with a different definition of ∆ specific to the regressor setting. For other settings, we present our results in terms of the common definition of the non-stationarity measure (denoted by ∆̂) and compare them with the state of the art: 
 MASTER + OFUL: D-REG = Õ(min{d √ LT , d∆̂1/3T 2/3 + d 
√ T}), where ∆̂ = 
∑ t ‖θt − 
θt+1‖2. This improves (Cheung et al., 2019; Russac et al., 2019; Kim and Tewari, 2020; Zhao et al., 2020; Zhao and Zhang, 2021) which get Õ(d7/8∆̂1/4T 3/4 + d 
√ T ) when ∆̂ is known. 
 MASTER + GLM-UCB: D-REG = Õ ( 
min { kµ cµ d √ LT , 
k 4/3 µ 
cµ d∆̂1/3T 2/3 + 
kµ cµ d √ T }) 
, where 
∆̂ = ∑ 
t ‖θt − θt+1‖2. This improves (Russac et al., 2020) which gets Õ (kµ cµ d2/3L1/3T 2/3 
) when L is known, and (Faury et al., 2021) which gets Õ 
(kµ cµ d9/10∆̂1/5T 4/5 
) . 
 MASTER + Q-UCB: D-REG = Õ(min{ √ H5SALT , (H7SA∆̂)1/3T 2/3 + 
√ H5SAT}), 
where ∆̂ = ∑ 
t,h maxs,a(|rth(s, a)− rt+1 h (s, a)|+ ‖pth(·|s, a)− pt+1 
h (·|s, a)‖1).5 (Mao et al., 2021, Theorem 3) gets Õ((H5SA∆̂)1/3T 2/3 + 
√ H3SAT ) when ∆̂ is known.6 
4. Same as Footnote 3. 5. Due to the scaling mentioned in Footnote 3, here, we first scale down C(·) and ∆ by an H factor, then apply 
Theorem 2, and finally scale up the final bound by an H factor. 6. The bound reported in (Mao et al., 2021) is (H3SA∆̂) 
1/3T 2/3 + 
√ H2SAT ; however, their T is the total number 
of timesteps while our T is the number of episodes, and we have performed a proper translation between notations here. Their bound has a better H dependency thanks to the use of Freedman-style confidence bounds. The same idea unfortunately does not improve our bound due to the lower-order term c2 in the definition of C(t). 
7
WEI LUO 
𝜏 
𝑓𝜏 
⋆ 
𝑈𝜏 
I 
new instance of ALG 
Learner’s average performance in new ALG 
Figure 1: An illustration of how we detect non-stationarity via multiple instances of ALG 
 MASTER + LSVI-UCB: D-REG = Õ(min{ √ d3H4LT , (d4H6∆̂)1/3T 2/3 + 
√ d3H4T}), 
where ∆̂ = ∑ 
t,h(‖θth − θ t+1 h ‖2 + ‖µth − µ 
t+1 h ‖F ). This improves (Zhou et al., 2020; Touati 
and Vincent, 2020) which get Õ((d5H8∆̂)1/4T 3/4 + √ d3H4T ) when ∆̂ is known.7 
2.3. High-level ideas 
To get a high-level idea of our approach, first consider what could go wrong when running ALG alone in a non-stationary environment and how to fix that intuitively. Decompose the dynamic regret as follows: 
t∑ τ=1 
( f?τ − f̃τ 
) ︸ ︷︷ ︸ 
term1 
+ 
t∑ τ=1 
( f̃τ −Rτ 
) ︸ ︷︷ ︸ 
term2 
. (2) 
As mentioned, in a stationary environment, ALG ensures that term1 is simply non-positive and term2 is bounded by C(t) directly. In a non-stationary environment, however, both terms can be substantially larger. If we can detect the event that either of them is abnormally large, we know that the environment has changed substantially, and should just restart ALG. This detection can be easily done for term2 since both f̃τ and Rτ are observable, but not for term1 since f?τ is of course unknown. Note that, a large term1 implies that a policy, possibly suboptimal in the past, now becomes the optimal one with a much larger reward. A single instance of ALG run from the beginning thus cannot detect this because suboptimal polices are naturally selected very infrequently. 
To address this issue, our main idea is to maintain different instances of ALG to facilitates nonstationarity detection, illustrated via an example in Figure 1. Here, there is one distribution change that happens in interval I, making the value of f?τ (the blue curve) drastically increase. If within this interval, we start running another instance of ALG (the red interval), then its performance (the black curve) will gradually approach f?τ due to its regret guarantee in a stationary environment. Hy-pothetically, if another instance of ALG run from the beginning could coexist with this new instance, we would see that the latter significantly outperforms the former and infer that the environment has changed. The issue is that we cannot have multiple instances running and making decisions simultaneously, and here is where the optimistic estimators f̃τ ’s can help. Specifically, since the quantity Uτ = mins≤τ f̃s (the green non-increasing curve) should always be an upper bound of the learner’s 
7. The same scaling as in Footnote 5 and Footnote 6 has been performed here. 
8
BLACK-BOX NON-STATIONARY RL 
Procedure 1: A procedure that randomly schedules ALG of different lengths within 2n rounds input: n, ρ(·) for τ = 0, . . . , 2n − 1 do 
for m = n, n− 1, . . . , 0 do If τ is a multiple of 2m, with probability ρ(2n) 
ρ(2m) , schedule a new instance alg of ALG that starts at alg.s = τ + 1 and ends at alg.e = τ + 2m. 
end end 
Algorithm 2: MALG (Multi-scale ALG) input: n, ρ(·) Initialization: run Procedure 1 with inputs n and ρ(·). At each time t, let the unique active instance be alg, output g̃t (which is the f̃t output by alg), 
follow alg’s decision πt, and update alg after receiving feedback from the environment. 
performance in a stationary environment, if we find that the new instance of ALG significantly outperforms this quantity at some point (as shown in Figure 1), we can also infer that the environment has changed, and prevent term1 ≤ 
∑t τ=1(f?τ − Uτ ) from growing too large by restarting. 
To formally implement the ideas above, we need to decide when to start a new instance, how long it should last, which instance should be active if multiple exist, and others. In Section 3, we propose a randomized multi-scale scheme to do so, which is reminiscent of the ideas of sampling obligation in (Auer et al., 2019) and replay phase in (Chen et al., 2019), although their mechanisms are highly specific to their algorithms and problems. 
3. Algorithm 
In this section, we first introduce MALG, an algorithm that schedules and runs multiple instances of the base algorithm ALG in a multi-scale manner (Section 3.1). Then, equipping MALG with non-stationarity detection, we introduce our final black-box reduction MASTER (Section 3.2). 
3.1. MALG: Running the Base Algorithm with Multiple Scales 
We always run MALG for an interval of length 2n, which we call a block, for some integer n (unless it is terminated by the non-stationarity detection mechanism). During initialization, MALG uses Procedure 1 to schedule multiple instances of ALG within the block in the following way: for every m = n, n− 1, . . . , 0, partition the block equally into 2n−m sub-intervals of length 2m, and for each of these sub-intervals, with probability ρ(2n) 
ρ(2m) ≤ 1 schedule an instance of ALG (otherwise skip this sub-interval). We call these instances of length 2m order-m instances. 
Note that by definition there is always an order-n instance covering the entire block. We use alg to denote a particular instance of ALG, and use alg.s and alg.e to denote its start and end time. 
After the initialization, MALG starts interacting with the environment as follows. In each time t, the unique instance covering this time step with the shortest length is considered as being active, while all others are inactive. MALG follows the decision of the active instance, and update it after receiving feedback from the environment. All inactive instances do not make any decisions or 
9
WEI LUO 
m=4 
m=3 
m=2 
m=1 
m=0 
① 
② 
inactive active inactiveactive 
Figure 2: An illustration of MALG with n = 4 (see detailed explanation in Section 3.1) 
updates, that is, they are paused (they might be resumed at some point though). We use g̃t to denote the scalar f̃t output by the active instance. See Algorithm 2 for the pseudocode. 
For better illustration, we give an example with n = 4 in Figure 2. Suppose that the realization of the random scheduling by Procedure 1 is: one order-4 instance (red), zero order-3 instance, two order-2 instances (green), two order-1 instances (blue), and five order-0 instances (purple). The bolder part of the segment indicates the period of time when the instances are active, while the thinner part indicates the inactive period. For example, the red order-4 instance is active for the first round, then paused for the next 8 rounds, and then resumed (from the frozen internal states) for another 3 rounds before becoming inactive again. The dashed black arrow marked with 1 
indicates that ALG is executed as if the two sides of the arrow are concatenated. On the other hand, as another example, the two purple instances on the two sides of the dashed line marked with 2 
are two different order-0 instances, so the second one should start from scratch even though they are consecutive. One can see that at any point of time, the active instance is always the one with the shortest length. 
Regret analysis of MALG The multi-scale nature of MALG allows the learner’s regret to also enjoy a multi-scale structure, as shown in the next lemma (proof deferred to Appendix B). 
Lemma 3 Let n̂ = log2 T + 1 and ρ̂(t) = 6n̂ log(T/δ)ρ(t). MALG with input n ≤ log2 T guarantees the following: for any instance alg that MALG maintains and any t ∈ [alg.s, alg.e], as long as ∆[alg.s,t] ≤ ρ(t′) where t′ = t− alg.s+ 1, we have with probability at least 1− δ 
T : 
g̃t ≥ min τ∈[alg.s,t] 
f?τ −∆[alg.s,t], 1 
t′ 
t∑ τ=alg.s 
(g̃τ −Rτ ) ≤ ρ̂(t′) + n̂∆[alg.s,t], (3) 
and the number of instances started within [alg.s, t] is upper bounded by 6n̂ log(T/δ)C(t′) C(1) . 
Note that Eq. (3) is essentially the analogue of Eq. (1) (up to logarithmic terms) with the starting time changed from 1 to alg.s. It shows that even if we have multiple instances interleaving in a complicated way, the regret for a specific interval is still almost the same as running ALG alone on this interval, thanks to the carefully chosen probability in Procedure 1. Recall that there is always an order-n instance starting from the beginning of the block, so MALG is always providing 
10
BLACK-BOX NON-STATIONARY RL 
Algorithm 3: MALG with Stationarity TEsts and Restarts (MASTER) input: ρ̂(·) (defined in Lemma 3) Initialize: t← 1 for n = 0, 1, . . . do 
Set tn ← t and initialize an MALG (Algorithm 2) for the block [tn, tn + 2n − 1]. while t < tn + 2n do 
Receive g̃t and πt from MALG, execute πt, and receive reward Rt. Update MALG with any feedback from the environment, and set Ut = minτ∈[tn,t] g̃τ . Perform Test 1 and Test 2 (see below). Increment t← t+ 1. if either test returns fail then restart from Line 3. 
end end Test 1: If t = alg.e for some order-m alg and 1 
2m ∑alg.e 
τ=alg.sRτ ≥ Ut + 9ρ̂(2m), return fail. Test 2: If 1 
t−tn+1 
∑t τ=tn 
(g̃τ −Rτ ) ≥ 3ρ̂(t− tn + 1), return fail. 
a stronger multi-scale guarantee compared to running ALG alone. This richer guarantee facilitates non-stationarity detection as we show next. 
3.2. MASTER: Equipping MALG with Stationarity Tests 
We are now ready to present our final algorithm MASTER, short for MALG with Stationarity TEsts and Restarts (see Algorithm 3). MASTER runs MALG in a sequence of blocks with doubling lengths (20, 21, . . .). Within each block of length 2n (with tn being the starting time), MASTER simply runs a new instance of MALG and records the minimum optimistic predictor thus far for this block Ut = minτ∈[tn,t] g̃τ . At the end of each time, MASTER performs two tests (Test 1 and Test 2), and if either of them returns fail, MASTER restarts from scratch. 
The two tests exactly follow the ideas described in Section 2.3 (recall Figure 1). Following Eq. (2), we decompose the regret on [tn, t] as term1 + term2 where term1 = 
∑t τ=tn 
(f?τ − g̃τ ) and term2 = 
∑t τ=tn 
(g̃τ −Rτ ). Test 1 prevents term1 ≤ ∑t 
τ=tn (f?τ − Uτ ) from growing too large by 
testing if there is some order-m instance’s interval during which the learner’s average performance 1 
2m ∑alg.e 
τ=alg.sRτ is larger than the promised performance upper bound Ut by an amount of 9ρ̂(2m). On the other hand, Test 2 presents term2 from growing too large by directly testing if its average is large than something close to the promised regret bound 3ρ̂(t− tn + 1). 
It is now clear that MASTER indeed does not require the knowledge of L or ∆ at all. To analyze MASTER, we prove the following key lemma that bounds the regret on a single block [tn, En] where En is either tn + 2n − 1 or something smaller in the case where a restart is triggered. 
Lemma 4 With high probability, the dynamic regret of MASTER on any block J = [tn, En] where En ≤ tn + 2n − 1 is bounded as 
∑ τ∈J 
(f?τ −Rτ ) ≤ Õ 
(∑̀ i=1 
C(|I ′i|) + 
n∑ m=0 
ρ(2m) 
ρ(2n) C(2m) 
) . (4) 
where {I ′1, . . . , I ′`} is any partition of J such that ∆I′i ≤ ρ(|I ′i|) for all i. 
11
WEI LUO 
See Appendix C for the proof. When ρ(t) = Θ(1/ √ t) (as in all our examples), the first term 
is Õ( ∑` 
i=1 
√ |I ′i|) = Õ( 
√ `|J |) by Cauchy-Schwarz; the second term is of order Õ( 
√ 2n). To 
derive a bound in terms of L, we can simply choose the partition {I ′1, . . . , I ′`} in a way such that ∆I′i = 0 and ` = LJ , while to derive a bound in terms of ∆, the partition needs to be chosen more carefully depending on the value of ∆J . Noting that the number of blocks between two restarts is always at most log2 T , to finally prove Theorem 2, it remains to bound the number of restarts, which intuitively should scale with L or ∆ because by design a restart will not be triggered when the environment is stationary. The complete proof is deferred to Appendix D–Appendix F. 
4. Extension to Reinforcement Learning in Infinite-horizon Communicating MDPs 
As mentioned, applying our results to infinite-horizon RL (Jaksch et al., 2010) requires some extra care and extensions. We refer the reader to (Cheung et al., 2020) for a thorough introduction on the problem setup of infinite-horizon RL in time-varying communicating MDPs. Here, we only highlight its difference compared to episode RL and explain how to fit it into our framework. Specif-ically, in episodic RL, we have treated each episode (consisting of multiple steps in an MDP) as one round of our framework, each state-to-action mapping as a policy π, and the expected reward of executing π in the MDP for round t as ft(π). In infinite-horizon RL, while the meaning of π and ft remains the same, there is no episode any more and the learner interacts with the changing MDP from the start to the end without any reset on her state. In this case, we treat each step (that is, each state transition) in the MDP as one round in our framework, and the meaning of the reward feedback Rt has now changed from a noisy observation of the policy’s reward ft(πt) to just the reward of πt for this single step. With this change, the dynamic regret definition remains the same. 
Due to the black-box nature of our approach, if one has a base algorithm that satisfies something close to Assumption 1 within this setup, then it is not hard to imagine that the same idea of MASTER can be applied. In Section 4.1, we provide such a base algorithm, and in Section 4.2, we combine it with appropriate multi-scale scheduling and detection to obtain our final results. 
4.1. UCRL with Adaptive Confidence Widening 
Our base algorithm, UCRL-ACW, is an improvement of the standard UCRL algorithm (Jaksch et al., 2010) and its variant UCRL-CW (Cheung et al., 2020). The pseudocode is shown in Algorithm 4 (Appendix A), where we highlight the differences compared to UCRL and UCRL-CW in blue. 
The first difference is the explicit mention that the next state of the learner might sometime be arbitrarily assigned instead of following the transition of the current MDP (Line 4). This is necessary because of the multi-scale scheduling of MALG. Indeed, recall that in MALG, an instance of the base algorithm can sometimes be paused and then resumed later. In the infinite-horizon RL setup, this means that the instance can be resumed from an arbitrary state. Other than making this detail explicit, however, nothing really needs to be changed in the algorithm, since this happens infrequently and only incurs small additional regret due to the communicating property of the MDPs. 
The second key difference is an adaptive version of the Confidence Widening technique of (Che-ung et al., 2020) (see Line 4–Line 4). As pointed out in (Cheung et al., 2020), in non-stationary environments, the Extended Value Iteration (EVI) subroutine of UCRL might return a bias vector (h̃k) with span much larger than Dmax, the maximum diameters of all the MDPs. To address this issue, their confidence widening technique adds a constant η, tuned based on ∆, to the confidence level of the confidence set Pk, which eventually leads to sub-optimal regret ∆1/4T 3/4. Our adaptive 
12
BLACK-BOX NON-STATIONARY RL 
confidence widening, on the other hand, adaptively selects the value of η in a doubling manner, so that in a relatively stationary environment we only widen the confidence set slightly, while in a more non-stationary environment the widening is more significant. To avoid incurring too much additional regret in the latter case, we also monitor the cumulative widening amount and terminate the algorithm if it exceeds a certain threshold (Line 4–Line 4), because this implies that the environment is highly non-stationary. (This termination will also be a restart signal for MASTER.) 
Finally, notice that our black-box approach requires knowing the regret bound ρ(·) of the base algorithm, which in this case depends on Dmax, a potentially unknown quantity. To deal with this issue, UCRL-ACW takes a guess D on the value of Dmax as an additional input. In the next subsection, we discuss how MASTER decides the value of D when Dmax is unknown. 
With all these modifications, our base algorithm UCRL-ACW indeed provides a guarantee similar to Eq. (1) of Assumption 1; see Lemma 11. 
4.2. Multi-scale UCRL-ACW and Its Combination with MASTER 
Now, we use the same idea as in Section 3.1 to create a multi-scale version of UCRL-ACW, under a fixed input D. The resulted algorithm is called Multi-scale UCRL-ACW or MUCRL for short (see Algorithm 5). MUCRL is basically identical to MALG with UCRL-ACW as the base algorithm, except that we let MUCRL terminate whenever the currently active UCRL-ACW instance makes a restart signal (due to having an abnormally large cumulative widening amount). The guarantee for MUCRL is provided in Lemma 12, which parallels Lemma 3. 
Next, as in Section 3.2, we further combine MUCRL with non-stationarity tests, leading to MASTER-UCRL (see Algorithm 6). The only difference compared to MASTER is an additional condition to restart (highlighted in blue) — when MUCRL terminates due to a restart signal from an UCRL-ACW instance. We provide a single-block regret bound guarantee for MASTER-UCRL under a fixed D in Lemma 13, which parallels Lemma 4. Finally, we discuss three different cases with knowledge of different parameters (if any), leading to the three results listed in Table 1. 
Known Dmax When Dmax is known, we simply set D = Dmax. In this case, all restarts of MASTER-UCRL are due to non-stationarity, and we can bound their number in terms of L or ∆. Together with the single-block regret guarantee from Lemma 13, we prove that MASTER-UCRL’s dynamic regret is Õ(min{Reg?L,Reg?∆}); see Theorem 28 for the dependence on other parameters. 
Unknown Dmax and Known L or ∆ When Dmax is unknown, we unfortunately require the knowledge of L to get Reg?L and the knowledge of ∆ to get Reg?∆. However, as shown in Table 1, this still significantly improves over the best existing bounds Õ(L1/3T 2/3) and Õ(∆1/4T 3/4) when L and ∆ are known. Specifically, we apply a doubling trick to set the value of D following the strategy below, where we call the interval between two restarts an epoch: 
1. Initialize D ← 1. 
2. Run MASTER-UCRL with D. If the number of epochs exceeds N , then double D and repeat this step. Here, N is set to L if L is known or 1 + 3(S−2A−1∆2T )1/3 if ∆ is known. 
The rationale behind monitoring the number of epochs is that, whenD is too small, UCRL-ACW might have an abnormally large cumulative widening amount and signal a restart even in a fairly stationary environment. In Lemma 26, we show that if D ≥ Dmax, the number of epochs produced by MASTER-UCRL is upper bounded by the value of N set above. Therefore, if it exceeds this 
13
WEI LUO 
number, we can infer D < Dmax and double its value. This allows us to prove the regret bound Reg?L or Reg?∆ again; see Theorem 29 for the details. 
No prior knowledge at all When nothing is known, we apply the Bandit-over-Reinforcment-Learning (BoRL) framework of (Cheung et al., 2019, 2020) to get a suboptimal bound of order Õ(min{Reg?L,Reg?∆} + T 3/4). BoRL also serves as a black-box reduction to obtain parameter-free algorithms (albeit suboptimal), so applying it to our algorithm is straightforward. We omit the details and only give the concrete bound in Appendix H. We leave the question of whether the optimal bound is achievable when L, ∆, and Dmax are all unknown as a future direction. 
5. Conclusion and Future Directions 
In this work, we study reinforcement learning in non-stationary environments. We propose a general black-box approach that can convert an algorithm with near-optimal regret in a (near-)stationary environment to another algorithm with near-optimal dynamic regret in a non-stationary environment. Prior to our work, the bound of Õ(∆1/3T 2/3) is only achievable with the knowledge of ∆, and no algorithm achieves the bound of Õ( 
√ LT ) even with the knowledge of L. Our algorithm achieves 
both bounds simultaneously without any prior knowledge. It would be interesting to see whether algorithms with data-dependent bounds work with our 
black-box approach. Previous work in this direction (Wei et al., 2016) achieves an improved dynamic regret bound for multi-armed bandits when the cumulative variance of the loss is small; however, their approach crucially relies on the knowledge on the degree of non-stationarity as well as the cumulative variance. On the other hand, there are some immediate difficulties in applying our black-box approach to data-dependent algorithms. For example, the monotonicity of the the average regret ρ(·) may not hold anymore, and it is unclear how to set the probability of initiating a new base algorithm. Therefore, the task of achieving data-dependent dynamic bounds without prior knowledge seems to be challenging and requires other innovations. 
Another future direction is to study a class of contextual bandit problems where the context is adversarially generated (Abbasi-Yadkori et al., 2011; Cheung et al., 2019; Foster and Rakhlin, 2020). In this case, the expected reward of the optimal policy changes over time even if the environment is stationary, so our current algorithm cannot be directly applied. For linear contextual bandits with adversarial contexts (Abbasi-Yadkori et al., 2011; Cheung et al., 2019), the fix is straightforward though: instead of requiring the base algorithm to generate a scalar f̃t in each round, we let it generate a confidence set for the hidden parameter, and check the inconsistency of the confidence set over time. However, for general contextual bandits with adversarial contexts, where algorithms do not necessarily maintain a confident set for the hidden parameter (Foster and Rakhlin, 2020), the extension is less clear and is left for future investigation. 
Finally, we are not aware of any near-optimal convex bandit algorithm satisfying our Assump-tion 1, so achieving near-optimal dynamic regret bound in general convex bandits is also left open. 
Acknowledgments We thank Peng Zhao for pointing out the technical flaw made in previous works on non-stationary linear bandits as well as a fix in (Zhao and Zhang, 2021). We also thank anonymous reviewers for pointing out the relation between our algorithm and regret balancing (Abbasi-Yadkori et al., 2020; Pacchiano et al., 2020). This work is supported by NSF Award IIS-1943607 and a Google Faculty Research Award. 
14
BLACK-BOX NON-STATIONARY RL 
References 
Yasin Abbasi-Yadkori, Dávid Pál, and Csaba Szepesvári. Improved algorithms for linear stochastic bandits. Advances in neural information processing systems, 24:2312–2320, 2011. 
Yasin Abbasi-Yadkori, Aldo Pacchiano, and My Phan. Regret balancing for bandit and rl model selection. arXiv preprint arXiv:2006.05491, 2020. 
Alekh Agarwal, Daniel Hsu, Satyen Kale, John Langford, Lihong Li, and Robert Schapire. Taming the monster: A fast and simple algorithm for contextual bandits. In International Conference on Machine Learning, pages 1638–1646, 2014. 
Raman Arora, Ofer Dekel, and Ambuj Tewari. Deterministic mdps with adversarial rewards and bandit feedback. In Proceedings of the Twenty-Eighth Conference on Uncertainty in Artificial Intelligence, pages 93–101, 2012. 
Peter Auer, Nicolo Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3):235–256, 2002a. 
Peter Auer, Nicolo Cesa-Bianchi, Yoav Freund, and Robert E Schapire. The nonstochastic multiarmed bandit problem. SIAM journal on computing, 32(1):48–77, 2002b. 
Peter Auer, Pratik Gajane, and Ronald Ortner. Adaptively tracking the best bandit arm with an unknown number of distribution changes. In Conference on Learning Theory, pages 138–158, 2019. 
Qi Cai, Zhuoran Yang, Chi Jin, and Zhaoran Wang. Provably efficient exploration in policy optimization. In International Conference on Machine Learning, pages 1283–1294. PMLR, 2020. 
Liyu Chen, Haipeng Luo, and Chen-Yu Wei. Minimax regret for stochastic shortest path with adversarial costs and known transition. In Conference on Learning Theory, 2021. 
Wei Chen, Liwei Wang, Haoyu Zhao, and Kai Zheng. Combinatorial semi-bandit in the nonstationary environment. arXiv preprint arXiv:2002.03580, 2020. 
Yifang Chen, Chung-Wei Lee, Haipeng Luo, and Chen-Yu Wei. A new algorithm for non-stationary contextual bandits: Efficient, optimal and parameter-free. In Conference on Learning Theory, pages 696–726, 2019. 
Wang Chi Cheung, David Simchi-Levi, and Ruihao Zhu. Learning to optimize under nonstationarity. In The 22nd International Conference on Artificial Intelligence and Statistics, pages 1079–1087. PMLR, 2019. 
Wang Chi Cheung, David Simchi-Levi, and Ruihao Zhu. Reinforcement learning for non-stationary markov decision processes: The blessing of (more) optimism. In International Conference on Machine Learning, pages 1843–1854. PMLR, 2020. 
Amit Daniely, Alon Gonen, and Shai Shalev-Shwartz. Strongly adaptive online learning. In Inter-national Conference on Machine Learning, pages 1405–1411, 2015. 
15
WEI LUO 
Ofer Dekel and Elad Hazan. Better rates for any adversarial deterministic mdp. In International Conference on Machine Learning, pages 675–683, 2013. 
Travis Dick, Andras Gyorgy, and Csaba Szepesvari. Online learning in markov decision processes with changing cost sequences. In International Conference on Machine Learning, pages 512– 520, 2014. 
Omar Darwiche Domingues, Pierre Ménard, Matteo Pirotta, Emilie Kaufmann, and Michal Valko. A kernel-based approach to non-stationary reinforcement learning in metric spaces. In Interna-tional Conference on Artificial Intelligence and Statistics, pages 3538–3546. PMLR, 2021. 
Eyal Even-Dar, Sham M Kakade, and Yishay Mansour. Online markov decision processes. Mathe-matics of Operations Research, 34(3):726–736, 2009. 
Louis Faury, Yoan Russac, Marc Abeille, and Clément Calauzènes. Regret bounds for generalized linear bandits under parameter drift. arXiv preprint arXiv:2103.05750, 2021. 
Yingjie Fei, Zhuoran Yang, Zhaoran Wang, and Qiaomin Xie. Dynamic regret of policy optimization in non-stationary environments. Advances in Neural Information Processing Systems, 33, 2020. 
Sarah Filippi, Olivier Cappé, Aurélien Garivier, and Csaba Szepesvári. Parametric bandits: the generalized linear case. In Proceedings of the 23rd International Conference on Neural Information Processing Systems-Volume 1, pages 586–594, 2010. 
Dylan Foster and Alexander Rakhlin. Beyond ucb: Optimal and efficient contextual bandits with regression oracles. In International Conference on Machine Learning, pages 3199–3210. PMLR, 2020. 
Pratik Gajane, Ronald Ortner, and Peter Auer. A sliding-window algorithm for markov decision processes with arbitrarily changing rewards and transitions. arXiv preprint arXiv:1805.10066, 2018. 
Elad Hazan and Comandur Seshadhri. Adaptive algorithms for online decision problems. In Elec-tronic colloquium on computational complexity (ECCC), volume 14, 2007. 
Thomas Jaksch, Ronald Ortner, and Peter Auer. Near-optimal regret bounds for reinforcement learning. Journal of Machine Learning Research, 11(4), 2010. 
Chi Jin, Zeyuan Allen-Zhu, Sebastien Bubeck, and Michael I Jordan. Is q-learning provably efficient? In Advances in neural information processing systems, pages 4863–4873, 2018. 
Chi Jin, Tiancheng Jin, Haipeng Luo, Suvrit Sra, and Tiancheng Yu. Learning adversarial markov decision processes with bandit feedback and unknown transition. In International Conference on Machine Learning, pages 4860–4869. PMLR, 2020a. 
Chi Jin, Zhuoran Yang, Zhaoran Wang, and Michael I Jordan. Provably efficient reinforcement learning with linear function approximation. In Conference on Learning Theory, pages 2137– 2143. PMLR, 2020b. 
16
BLACK-BOX NON-STATIONARY RL 
Tiancheng Jin and Haipeng Luo. Simultaneously learning stochastic and adversarial episodic mdps with known transition. Advances in Neural Information Processing Systems, 33, 2020. 
Kwang-Sung Jun, Francesco Orabona, Stephen Wright, and Rebecca Willett. Improved strongly adaptive online learning using coin betting. In Artificial Intelligence and Statistics, pages 943– 951, 2017. 
Baekjin Kim and Ambuj Tewari. Randomized exploration for non-stationary stochastic linear bandits. In Uncertainty in Artificial Intelligence, 2020. 
Tze Leung Lai and Herbert Robbins. Asymptotically efficient adaptive allocation rules. Advances in applied mathematics, 6(1):4–22, 1985. 
Tal Lancewicki, Aviv Rosenberg, and Yishay Mansour. Learning adversarial markov decision processes with delayed feedback. arXiv preprint arXiv:2012.14843, 2020. 
Chung-Wei Lee, Haipeng Luo, Chen-Yu Wei, and Mengxiao Zhang. Bias no more: high-probability data-dependent regret bounds for adversarial bandits and mdps. Advances in Neural Information Processing Systems, 33, 2020. 
Yingying Li and Na Li. Online learning for markov decision processes in nonstationary environments: A dynamic regret analysis. In 2019 American Control Conference (ACC), pages 1232– 1237. IEEE, 2019. 
Haipeng Luo and Robert E Schapire. Achieving all with no parameters: Adanormalhedge. In Conference on Learning Theory, pages 1286–1304, 2015. 
Haipeng Luo, Chen-Yu Wei, Alekh Agarwal, and John Langford. Efficient contextual bandits in non-stationary worlds. In Conference On Learning Theory, pages 1739–1776. PMLR, 2018. 
Thodoris Lykouris, Max Simchowitz, Aleksandrs Slivkins, and Wen Sun. Corruption robust exploration in episodic reinforcement learning. In Conference on Learning Theory, 2021. 
Weichao Mao, Kaiqing Zhang, Ruihao Zhu, David Simchi-Levi, and Tamer Başar. Is model-free learning nearly optimal for non-stationary rl? In International Conference on Machine Learning, 2021. 
Gergely Neu, András György, and Csaba Szepesvári. The online loop-free stochastic shortest-path problem. In COLT, volume 2010, pages 231–243. Citeseer, 2010. 
Gergely Neu, Andras Gyorgy, and Csaba Szepesvári. The adversarial stochastic shortest path problem with unknown transition probabilities. In Artificial Intelligence and Statistics, pages 805– 813, 2012. 
Gergely Neu, András György, Csaba Szepesvári, and András Antos. Online markov decision processes under bandit feedback. IEEE Transactions on Automatic Control, 59(3):676–691, 2013. 
Ronald Ortner, Pratik Gajane, and Peter Auer. Variational regret bounds for reinforcement learning. In Uncertainty in Artificial Intelligence, pages 81–90. PMLR, 2020. 
17
WEI LUO 
Aldo Pacchiano, Christoph Dann, Claudio Gentile, and Peter Bartlett. Regret bound balancing and elimination for model selection in bandits and rl. arXiv preprint arXiv:2012.13045, 2020. 
Aviv Rosenberg and Yishay Mansour. Online convex optimization in adversarial markov decision processes. In International Conference on Machine Learning, pages 5478–5486, 2019. 
Aviv Rosenberg and Yishay Mansour. Stochastic shortest path with adversarially changing costs. arXiv preprint arXiv:2006.11561, 2020. 
Yoan Russac, Claire Vernade, and Olivier Cappé. Weighted linear bandits for non-stationary environments. Advances in Neural Information Processing Systems, 2019. 
Yoan Russac, Olivier Cappé, and Aurélien Garivier. Algorithms for non-stationary generalized linear bandits. arXiv preprint arXiv:2003.10113, 2020. 
Lior Shani, Yonathan Efroni, Aviv Rosenberg, and Shie Mannor. Optimistic policy optimization with bandit feedback. In International Conference on Machine Learning, pages 8604–8613. PMLR, 2020. 
David Simchi-Levi and Yunzong Xu. Bypassing the monster: A faster and simpler optimal algorithm for contextual bandits under realizability. Available at SSRN, 2020. 
Ahmed Touati and Pascal Vincent. Efficient learning in non-stationary linear markov decision processes. arXiv preprint arXiv:2010.12870, 2020. 
Ruosong Wang, Simon S Du, Lin F Yang, and Sham M Kakade. Is long horizon reinforcement learning more difficult than short horizon reinforcement learning? Advances in Neural Informa-tion Processing Systems, 2020. 
Chen-Yu Wei, Yi-Te Hong, and Chi-Jen Lu. Tracking the best expert in non-stationary stochastic environments. Advances in neural information processing systems, 29:3972–3980, 2016. 
Peng Zhao and Lijun Zhang. Non-stationary linear bandits revisited. arXiv preprint arXiv:2103.05324, 2021. 
Peng Zhao, Lijun Zhang, Yuan Jiang, and Zhi-Hua Zhou. A simple approach for non-stationary linear bandits. In Silvia Chiappa and Roberto Calandra, editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 746–755. PMLR, 26–28 Aug 2020. 
Huozhi Zhou, Jinglin Chen, Lav R Varshney, and Ashish Jagmohan. Nonstationary reinforcement learning with linear function approximation. arXiv preprint arXiv:2010.04244, 2020. 
Alexander Zimin and Gergely Neu. Online learning in episodic markovian decision processes by relative entropy policy search. Advances in neural information processing systems, 26:1583– 1591, 2013. 
18
BLACK-BOX NON-STATIONARY RL 
Appendix A. Omitted Algorithms and Main Results in Section 4 
Algorithm 4: UCRL with Adaptive Confidence Widening (UCRL-ACW) 
input: D ≥ 1 t← 1. N1(s, a)← 0 for all s, a. Γ← 0 for episode k = 1, . . . , do 
Set tk = t, νk(s, a) = 0 for all s, a. Define for all s, a: 
p̂k(s ′|s, a) = 
∑t−1 τ=1 1[(sτ , aτ , s 
′ τ+1) = (s, a, s′)] 
N+ k (s, a) 
, 
r̂k(s, a) = 
∑t−1 τ=1Rτ1[(sτ , aτ ) = (s, a)] 
N+ k (s, a) 
. 
and for any η: 
Pηk (s, a) = { p̃(·|s, a) ∈ ∆S : ‖p̃(·|s, a)− p̂k(·|s, a)‖1 ≤ 
√ S · confk(s, a) + η 
} Rk(s, a) = {r̃(s, a) ∈ [0, 1] : |r̃(s, a)− r̂k(s, a)| ≤ confk(s, a)} 
where confk(s, a) , 8 
√ log(SAT/δ) 
N+ k (s,a) 
and N+ k (s, a) = max{1, Nk(s, a)}. 
η ← 1 T 
while true do Perform EVI on (Pηk ,Rk) with error parameter εk = 
√ 1 t , and obtain π̃, h̃, J̃ . 
if sp(h̃) ≤ 2D then break η ← 2η 
end πk ← π̃, h̃k ← h̃, J̃k ← J̃ , ηk ← η / Adaptive confidence widening 
while νk(s, a) < N+ k (s, a) for all s, a do 
Choose action at ∼ πk(st). νk(st, at)← νk(st, at) + 1 Γ← Γ + ηk if Γ > 4S 
√ At log(SAT/δ) then terminate and signal restart / Early termination 
Observe the reward Rt with E[Rt] = rt(st, at) Observe s′t+1 ∼ pt(·|st, at). The next state st+1 is either equal to s′t+1, or re-assigned as an arbitrary state 
/ The next state might be re-assigned t← t+ 1 
end Nk+1(s, a)← Nk(s, a) + νk(s, a) for all s, a. 
end 
The following is the main result for the infinite-horizon MDP case. Its proof requires several lemmas 
19
WEI LUO 
Algorithm 5: Multi-scale UCRL-ACW (MUCRL) 
input: n, ρUCRL(· ;D), D Initialization: run Procedure 1 with base algorithm UCRL-ACW and inputs n and ρUCRL. At each time t, let the unique active instance be alg, output g̃t (which is the quantity J̃k(t) of 
alg), follow alg’s decision, and update alg after receiving feedback from the environment. Additionally, terminate if the alg signals restart. 
Algorithm 6: MASTER-UCRL 
input: ρUCRL(· ;D), D Initialize: t← 1 for n = 0, 1, . . . do 
Set tn ← t and initialize an MUCRL (Algorithm 5) for the block [tn, tn + 2n − 1]. while t < tn + 2n do 
Receive g̃t and πt from MUCRL, execute πt, and receive reward Rt. Update MUCRL with any feedback from the environment, and set Ut = minτ∈[tn,t] g̃τ . Perform Test 1 and Test 2 (see below). Increment t← t+ 1. if either test returns fail or MUCRL terminates then restart from Line 6. 
end end Test 1: If t = alg.e for some order-m alg and 1 
2m ∑alg.e 
τ=alg.sRτ ≥ Ut + 9ρ̂UCRL(2m;D), return fail. 
Test 2: If 1 t−tn+1 
∑t τ=tn 
(g̃τ −Rτ ) ≥ 3ρ̂UCRL(t− tn + 1;D), return fail. 
in the rest of this section, in addition to those from Appendix B–Appendix E whose ideas are mostly aligned with the standard setting. The final analysis is done in Appendix G and Appendix H (see Theorem 28, Theorem 29, and the discussions in Appendix H). Note that to be consistent with prior works in this setting, we adopt the notation Jt(π), which is the expected average reward of executing π under the MDP for time t, and corresponds to the notation ft(π) we use in our general framework. Similarly, define J?t = maxπ Jt(π). 
Theorem 5 Define non-stationarity measures 
∆ = 
T−1∑ t=1 
( max s,a |rt(s, a)− rt+1(s, a)|+ max 
s,a ‖pt(·|s, a)− pt+1(·|s, a)‖1 
) , 
L = 1 + 
T−1∑ t=1 
1 
{ max s,a |rt(s, a)− rt+1(s, a)|+ max 
s,a ‖pt(·|s, a)− pt+1(·|s, a)‖1 6= 0 
} . 
There exists an algorithm that takes Dmax as input and achieves 
T∑ t=1 
(J?t −Rt) = Õ ( 
min { DmaxS 
√ ALT, DmaxS 
2 3A 
1 3 ∆ 
1 3T 
2 3 +DmaxS 
√ AT }) 
20
BLACK-BOX NON-STATIONARY RL 
without knowing L or ∆. There is also an algorithm that takes L or ∆ as input and achieves 
T∑ t=1 
(J?t −Rt) = Õ ( DmaxS 
√ ALT 
) or 
T∑ t=1 
(J?t −Rt) = Õ ( DmaxS 
2 3A 
1 3 ∆ 
1 3T 
2 3 +DmaxS 
√ AT ) 
respectively, without knowing Dmax. Finally, there is an algorithm that achieves 
T∑ t=1 
(J?t −Rt) = Õ ( Dmax(S2A) 
1/4T 3/4 + min 
{ DmaxS 
√ ALT, Dmax(S2A) 
1 3 ∆ 
1 3T 
2 3 
}) without knowing L,∆, or Dmax. 
A.1. Auxiliary Lemmas related to Extended Value Iteration and Bellman Equation 
In this subsection, we provide auxiliary lemmas related to EVI and Bellman Equation. The results are extracted from (Jaksch et al., 2010; Cheung et al., 2020; Ortner et al., 2020). We restate them here for completeness. 
Lemma 6 (Properties 1 and 2 in (Cheung et al., 2020)) Let J̃ , h̃, and π̃ be the set of solution obtained from EVI with confidence set R and P for reward and transition respectively, and error parameter ε. Then 
J̃ + h̃(s) ≥ max a 
( max 
r̃∈R(s,a) r̃(s, a) + max 
p̃∈P(s,a) 
∑ s′ 
p̃(s′|s, a)h̃(s′) 
) , (5) 
J̃ + h̃(s) ≤ max r̃∈R(s,π̃(s)) 
r̃(s, π̃(s)) + max p̃∈P(s,π̃(s)) 
∑ s′ 
p̃(s′|s, π̃(s))h̃(s′) + ε. (6) 
Lemma 7 (Lemma 2 of (Cheung et al., 2020)) Let J̃ , h̃, and π̃ be the set of solution obtained from EVI with confidence set R and P for reward and transition respectively. If P and R contain an MDP with diameter upper bounded by D, then sp(h̃) ≤ 2D. 
Lemma 8 (Eq. (16) of (Cheung et al., 2020)) Let r, p define the reward function and the transition kernel for a communicating MDP, respectively. Let J̃ ∈ R, h̃ ∈ RS be bounded and satisfy 
J̃ + h̃(s) ≥ r(s, a) + ∑ s′ 
p(s′|s, a)h̃(s′) 
for all s and a. Then J̃ ≥ J?, where J? is the average reward of the optimal policy under the MDP. 
A.2. Guarantees of the UCRL-ACW Algorithm (when running alone with an input D) 
Definition 9 Define ∆r(t) , maxs,a |rt(s, a) − rt+1(s, a)|, ∆p(t) , maxs,a ‖pt(·|s, a) − pt+1(·|s, a)‖1, ∆J(t) , maxπ |Jt(π) − Jt+1(π)|. Similar to Definition 1, define ∆I =∑e−1 
τ=s ∆(τ) for interval I = [s, e], where  = r, p, or J . Finally, we define ∆I;D , 
∆r I + 2D∆p 
I + ∆J I . 
Lemma 10 (Theorem 1 of (Ortner et al., 2020)) ∆J(t) ≤ ∆r(t) +Dmax∆p(t). 
21
WEI LUO 
Lemma 11 (c.f. Assumption 1) When run alone, Algorithm 4 with input D guarantees for all t before it terminates: 
J̃k(t) ≥ min τ∈[1,t] 
J?τ −∆[1,t];D 
1 
t 
t∑ τ=1 
( J̃k(τ) −Rτ 
) ≤ ρUCRL 
( t;D 
) + 
2 
t Ddisc[1,t] + ∆[1,t];D, 
where ρUCRL(t;D) = Θ̃ 
( min 
{ DS √ 
A t + DSA 
t , D }) 
, discI , ∑ 
t∈I 1[st  
pt−1(·|st−1, at−1)] is the number of state re-assignments within I (Line 4 of Algorithm 4), and k(t) is the index of the episode time t belongs to. 
Proof Suppose that at time t the algorithm has not terminated. For any episode k that starts before t, we have 
rk(s, a) = 
∑tk−1 τ=1 rτ (s, a)1[(sτ , aτ ) = (s, a)] 
N+ k (s, a) 
, pk(s ′|s, a) = 
∑tk−1 τ=1 pτ (s′|s, a)1[(sτ , aτ ) = (s, a)] 
N+ k (s, a) 
. 
By Azuma’s inequality, rk(s, a) ∈ Rk(s, a) and pk(·|s, a) ∈ Pηkk (s, a) with high probability for all k, s, a. 
To show the first part of the lemma, we lower bound the right-hand side of Eq. (5): 
J̃k + h̃k(s) ≥ r(s, a) + ∑ s′ 
p(s′|s, a)h̃k(s ′) 
≥ rτ (s, a) + ∑ s′ 
pτ (s′|s, a)h̃k(s ′)− 
( ∆r 
[1,t] + 2D∆p [1,t] 
) , (for any τ ∈ [1, t]) 
where in the last inequality we use |r(s, a) − rτ (s, a)| ≤ ∆r [1,t] and 
∑ s′ |p(s′|s, a) − 
pτ (s′|s, a)|h̃k(s′) ≤ ‖p(·|s, a)− pτ (·|s, a)‖1sp(h̃k) ≤ 2∆p [1,t]D. Using Lemma 8, we get 
J̃k + ∆[1,t];D ≥ J̃k + ( 
∆r [1,t] + 2D∆p 
[1,t] 
) ≥ J?τ , 
implying the first part of the lemma. To show the second part of the lemma, starting from Eq. (6), we have with high probability 
J̃k + h̃k(s) (7) 
≤ rk(s, πk(s)) + ∑ s′ 
pk(s ′|s, πk(s))h̃k(s′) + 2D 
√ S · confk(s, πk(s)) + 2Dηk + εk 
(rk(s, a) ∈ Rk(s, a) and pk(s, a) ∈ Pk(s, a)) 
≤ rτ (s, πk(s)) + ∑ s′ 
pτ (s′|s, πk(s))h̃k(s′) + 2D √ S · confk(s, πk(s)) + 
( ∆r 
[1,t] + 2D∆p [1,t] 
) + 2Dηk + εk. 
(8) 
Now, we apply Eq. (8) with (k, τ, s) = {k(τ), τ, sτ}tτ=1 respectively, and sum them up. Notice that aτ = πk(τ)(sτ ). Then we get 
t∑ τ=1 
( J̃k(τ) −Rτ 
) ≤ 
t∑ τ=1 
(∑ s′ 
pτ (s′|sτ , aτ )h̃k(τ)(s ′)− h̃k(τ)(sτ ) 
) + 
t∑ τ=1 
(rτ (sτ , aτ )−Rτ ) 
22
BLACK-BOX NON-STATIONARY RL 
+ t∑ 
τ=1 
2D √ S · confk(τ)(sτ , aτ ) + t∆[1,t];D + 2D 
t∑ τ=1 
ηk(τ) + t∑ 
τ=1 
εk(τ). 
We bound the terms on the right-hand side individually: for the first term, notice that when there is no state-reassignment at time τ + 1, Eτ [h̃k(τ)(sτ+1)] = 
∑ s′ pτ (s′|sτ , aτ )h̃k(τ)(s 
′). Therefore, 
t∑ τ=1 
(∑ s′ 
pτ (s′|sτ , aτ )h̃k(τ)(s ′)− h̃k(τ)(sτ ) 
) 
≤ t∑ 
τ=1 
( Eτ [ h̃k(τ)(sτ+1) 
] − h̃k(τ)(sτ ) 
) + 2Ddisc[1,t] 
≤ 2D √ t log(SAT ) + 2D 
t∑ τ=1 
1 
[ h̃k(τ) 6= h̃k(τ+1) 
] + 2Ddisc[1,t] (by Azuma’s inequality) 
≤ 2D √ t log(SAT ) + 2DSA log2 T + 2Ddisc[1,t], 
where in the last inequality we use the fact that the number of episodes cannot exceed SA log2 T . For the other terms: 
∑t τ=1 (rτ (sτ , aτ )−Rτ ) ≤ Õ 
(√ t ) 
by Azuma’s inequality; ∑t 
τ=1 2D √ S · 
confk(τ)(sτ , aτ ) = Õ ( DS √ At ) 
by the standard pigeonhole argument; 2D ∑t 
τ=1 ηk(τ) = 
Õ ( DS √ At ) 
by the termination condition specified in Line 4; ∑t 
τ=1 εk(τ) is also upper bounded 
by Õ ( DS √ At ) 
by the way we choose the error parameter. Combining all the above arguments, we get 
t∑ τ=1 
( J̃k(τ) −Rτ 
) ≤ Õ 
( DS √ At+DSA 
) + 2Ddisc[1,t] + t∆[1,t];D 
with high probability. On the other hand, ∑t 
τ=1 
( J̃k(τ) −Rτ 
) ≤ Dt is trivially true. Combining 
them we get the second claim of the lemma. 
Appendix B. Analysis for the Multi-scale Algorithms 
Proof of Lemma 3 Below, we fix an alg and fix a t ∈ [alg.s, alg.e], and consider the case ∆[alg.s,t] ≤ ρ(t′) as specified in the lemma statement. For the first part of the lemma, note that 
g̃t of MALG is defined as f̃alg′ t where alg′ is the active instance of ALG at round t. By Procedure 1, 
alg′ can only be an instance that starts within [alg.s, t] (i.e., alg′.s ≥ alg.s). Therefore, the distribution drift undergone by alg′ up to t is upper bounded by ∆[alg.s,t] ≤ ρ(t′), which is further upper bounded by ρ(t′′) where t′′ is the number of active rounds alg′ runs within [alg.s, t], because ρ(·) is a decreasing function. Therefore, the conditions in Assumption 1 is satisfied for this alg′, and thus we have 
g̃t = f̃alg′ t ≥ min 
τ≤t: alg′ is active at τ f?τ −∆[alg′.s,t] ≥ min 
τ∈[alg.s,t] f?τ −∆[alg.s,t], 
proving the first part. 
23
WEI LUO 
Next, we prove the second part of the lemma. We use Sm to denote the set of order-m instances which start within [alg.s, t]. Note that 
t∑ τ=alg.s 
(g̃τ −Rτ ) = t∑ 
τ=alg.s 
n∑ m=0 
∑ alg′∈Sm 
1[alg′ is active at τ ] ( f̃alg′ τ −Rτ 
) 
= n∑ 
m=0 
∑ alg′∈Sm 
t∑ τ=alg.s 
1[alg′ is active at τ ] ( f̃alg′ τ −Rτ 
) ︸ ︷︷ ︸ 
(∗) 
. (9) 
The first equality holds because g̃τ of MALG is defined as the f̃τ of the active instance at round t. Next, we focus on a specific m, and bound the (∗) term in Eq. (9). Let |Sm| = ` and Sm = 
{alg′1, . . . , alg′`}, and let Ii , [alg′i.s, alg′i.e] ∩ [alg.s, t] for i = 1, . . . , ` (i.e., Ii are the rounds within [alg.s, t] where alg′i is scheduled). Clearly, |Ii| ≤ min{alg′i.e− alg′i.s+ 1, t− alg.s+ 1} = min {2m, t′}. By Assumption 1, we have 
(∗) = ∑̀ i=1 
t∑ τ=alg.s 
1[alg′i is active at τ ] ( f̃ 
alg′i τ −Rτ 
) 
≤ ∑̀ i=1 
(C(|Ii|) + |Ii|∆Ii) 
≤ `C(min{2m, t′}) + t′∆[alg.s,t], (10) 
where in the first inequality we use Assumption 1, and that alg′i updates for no more than |Ii| rounds in the interval [alg.s, t] (also, the condition in Assumption 1 is satisfied because ∆Ii ≤ ∆[alg.s,t] ≤ ρ(t′) ≤ ρ(|Ii|)). In the last inequality, for the first term, we use that C(·) is increasing; for the second term, we use |Ii| ≤ t′, and that ∆I1 + · · · + ∆I` ≤ ∆[alg.s,t] since I1, . . . , I` are non-overlapping intervals lying within [alg.s, t]. 
By Procedure 1, for every m, the expected number of order-m ALG’s that starts within the interval [alg.s, t] can be upper bounded as 
E[|Sm|] ≤ ρ(2n) 
ρ(2m) 
⌈ t′ 
2m 
⌉ ≤ ρ(2n) 
ρ(2m) 
( t′ 
2m + 1 
) ≤ ρ(2n) 
ρ(2m) 
t′ 
2m + 1 (11) 
By Bernstein’s inequality, with probability 1 − δ T , |Sm| ≤ E[|Sm|] + 
√ 2E[|Sm|] log(T/δ) + 
log(T/δ) ≤ 2E[|Sm|] + 2 log(T/δ). Thus, continuing from Eq. (10), we have with probability at least 1− δ 
T , 
(∗) ≤ 2 · ( ρ(2n) 
ρ(2m) 
t′ 
2m + 1 
) C(min{2m, t′}) + 2 log(T/δ)C(min{2m, t′}) + t′∆[alg.s,t] 
≤ 2 
( C(t′) 
C(2m) + 2 
) log(T/δ)C(min{2m, t′}) + t′∆[alg.s,t] (ρ(2n)t′ ≤ ρ(t′)t′ = C(t′)) 
≤ 6C(t′) log(T/δ) + t′∆[alg.s,t] (C(·) is an increasing function) 
(12) 
24
BLACK-BOX NON-STATIONARY RL 
Finally, using this in Eq. (9), we get the second claim of the lemma: with probability at least 1− δ T , 
t∑ τ=alg.s 
(g̃τ −Rτ ) ≤ 6(n+ 1)C(t′) log(1/δ) + t′(n+ 1)∆[alg.s,t]. (13) 
For the third part of the lemma, as we calculated above, with probability at least 1 − δ T , the 
number of instances started within [alg.s, t] is upper bounded by 
n∑ m=0 
2 · ( ρ(2n) 
ρ(2m) 
t′ 
2m + 2 
) log(T/δ) ≤ 2n̂ 
( C(t′) 
C(1) + 2 
) log(T/δ) ≤ 6n̂ 
C(t′) 
C(1) log(T/δ) 
where we use ρ(2m)2m = C(2m) ≥ C(1) and ρ(2n)t′ ≤ ρ(t′)t′ = C(t′). 
Lemma 12 (c.f. Lemma 3) Before MUCRL terminates, for every alg and t ∈ [alg.s, alg.e], MU-CRL guarantees with high probability 
g̃t ≥ min τ∈[alg.s,t] 
J?τ −∆[alg.s,t];D 
1 
t′ 
t∑ τ=alg.s 
(g̃τ −Rτ ) ≤ ρ̂UCRL ( t′;D 
) + n̂∆[alg.s,t];D 
where t′ = t− alg.s+ 1, n̂ = log2 T + 1, and ρ̂UCRL ( t;D 
) = 18n̂ log(T/δ)ρUCRL(t;D). 
Proof This proof is similar to that of Lemma 3. For the first part of the lemma, we can simply follow the proof of the first part of Lemma 3, with f̃t replaced by J̃k(t), and ∆[alg.s,t] by ∆[alg.s,t];D. 
For the second part, the analysis still tightly follows that of Lemma 3, but we need to add the additional cost caused by state re-assignment (i.e., the Ddisc[1,t] term in Lemma 11). Following the same arguments as in proof as in Eq. (9) and Eq. (10), we get 
t∑ τ=alg.s 
(g̃τ −Rτ ) = n∑ 
m=0 
∑ alg′∈Sm 
t∑ τ=alg.s 
1[alg′ is active at τ ] ( f̃alg′ τ −Rτ 
) (Sm , the set of order-m ALG initiated within [alg.s, t]) 
≤ n∑ 
m=0 
|Sm|∑ i=1 
t∑ τ=alg.s 
1[alg′m,i is active at τ ] 
( f̃ 
alg′m,i τ −Rτ 
) (Let Sm = {alg′m,1, alg′m,2, . . .}) 
≤ n∑ 
m=0 
|Sm|∑ i=1 
( CUCRL(|Im,i|;D) + |Im,i|∆Im,i;D + 2Ddisc 
alg′m,i Im,i 
) (by Lemma 11) 
(14) 
where in the last expression, we denote Im,i = [alg′m,i.s, alg′m,i.e] ∩ [alg.s, t] (the time within 
[alg.s, t] where alg′m,i is scheduled), and discalg′ I is the total number of times within I when alg′ 
encounters state-reassignments. 
25
WEI LUO 
For a fixed m, observe that all order-m instances are non-overlapping. Also, the aggregated number of state re-assignment for all order-m instances started within [alg.s, t] is upper bounded by the total number of new instances of order not larger than m − 1 started within [alg.s, t]. The latter is further upper bounded by 6n̂ log(T/δ)CUCRL(t′;D) 
CUCRL(1;D) according to the last claim of Lemma 3. 
In other words, for every m, with probability 1− δ T , 
|Sm|∑ i=1 
disc alg′m,i Im,i = 6n̂ log(T/δ) 
CUCRL(t′;D) 
CUCRL(1;D) . 
Following the same calculation as in Eq. (10), Eq. (11) and Eq. (12), we also have that for every m, with probability 1− δ 
T , 
|Sm|∑ i=1 
( CUCRL(|Im,i|;D) + |Im,i|∆Im,i;D 
) ≤ 6n̂ log(T/δ)CUCRL(t′;D) + t′∆[alg.s,t];D. 
Using the above two bounds in Eq. (14), we get 
t∑ τ=alg.s 
(g̃τ −Rτ ) = 6n̂ log(T/δ)CUCRL(t′;D) + n̂t′∆[alg.s,t];D + 2D × 6n̂ log(T/δ) CUCRL(t′;D) 
CUCRL(1;D) 
= 18n̂ log(T/δ)CUCRL(t′;D) + n̂t′∆[alg.s,t];D 
where we use CUCRL(1;D) ≥ D (by the definition of ρUCRL(· , D) in Lemma 11). Dividing both sides by t′ finishes the proof. 
Appendix C. Single-block Regret Analysis I 
In this section, we focus on the regret in a block of index n. The analysis applies to both the standard case (Lemma 4), and the infinite-horizon RL case summarized in the following lemma. 
Lemma 13 (c.f. Lemma 4) In a block of index n that starts from tn and ends on En (En could be equal to tn + 2n − 1, or smaller, if any stationarity test fails or MUCRL terminates), we have 
En∑ τ=tn 
(f?τ −Rτ ) ≤ Õ 
(∑̀ i=1 
CUCRL(|I ′i|;D) + n∑ 
m=0 
ρ(2m;D) 
ρ(2n;D) CUCRL(2m;D) 
) 
where I ′1, . . . , I ′` are intervals that partition [tn, En] such that ∆I′i;D ≤ ρUCRL(|I ′i|;D) for all i. 
Throughout this section, if infinite-horizon RL is considered, ρ(·) , ρUCRL(· ;D), ρ̂(·) , ρ̂UCRL(· ;D), ∆I , ∆I;D = ∆r 
I + 2D∆p I + ∆J 
I with a fixed D, and f?t , J ? t . 
For the purpose of conducting analysis, we divide [tn, tn + 2n − 1] into consecutive intervals I1 = [s1, e1], I2 = [s2, e2], . . . , IK = [sK , eK ] (s1 = tn, ei + 1 = si+1, eK = tn + 2n − 1) in a way such that for all i: 
∆Ii ≤ ρ(|Ii|) (15) 
26
BLACK-BOX NON-STATIONARY RL 
One simple way to divide the intervals is to let ∆Ii = 0 in each Ii. Then the number of intervals K would be upper bounded by the number of stationary intervals within [tn, tn + 2n − 1]. Intuitively, the number of intervals can also be related to ∆[tn,tn+2n−1]. We defer the calculation of the required number of intervals to Lemma 19. For now, we only need the fact that the partition satisfies Eq. (15). From a high level, this partition makes the distribution in each interval close to stationary. Notice that this partition is independent of the learner’s behavior in block n. 
For convenience, we further define the following quantities that depend on the learner’s behavior in block n: 
Definition 14 Define En as the index of the last round in block n. Since the block might terminate earlier than planned, we have En ≤ tn + 2n − 1. Let ` ∈ [K] be such that En ∈ I` (that is, ` is the index of the interval where block n ends). Define e′i = min{ei, En} and I ′i = [si, e 
′ i] (therefore, 
I ′i = ∅ for i > `). 
Recall the definition of n̂ and ρ̂(t) from Lemma 3 (or Lemma 12). For simplicity, we define αm , ρ(2m), α̂m , ρ̂(2m), and also Ĉ(t) , tρ̂(t). Furthermore, we define the following technical quantities. 
Definition 15 For every i ∈ {1, . . . ,K}, and every m ∈ {0, 1, . . . , n}, define 
τi(m) = min { τ ∈ I ′i : f?τ − g̃τ ≥ 12α̂m 
} ; 
that is, τi(m) is the first time τ in I ′i = Ii ∩ [tn, En] such that f?τ − g̃τ exceeds 12α̂m. If such τ does not exist or I ′i is empty, we let τi(m) =∞. 
Besides, we define ξi(m) = [e′i − τi(m) + 1]+ where [a]+ = max{0, a} (which is the length of the interval [τi(m), e′i] when τi(m) is not∞). 
The intuition for τi(m) and ξi(m) is as follows. Suppose that block n has not ended at τ . If there exists some τ ∈ Ii such that f?τ−g̃τ ≥ 12α̂m (which first happens at τi(m)), and if Ii is long enough (i.e., ξi(m) is large enough) so that after τi(m), an order-m instance of ALG can run entirely within Ii, then the learner is able to discover the fact that f?τ − g̃τ is large, and then restart. This coincides with our explanation in Figure 1. The derivation in this section will formalize this intuition. 
Lemma 16 Let the high-probability events described in Lemma 3 (or Lemma 12) hold. Then with high probability, 
En∑ τ=tn 
(g̃τ −Rτ ) ≤ 4Ĉ(2n), 
En∑ τ=tn 
(f?τ − g̃τ ) ≤ 96n̂ ∑̀ i=1 
Ĉ(|I ′i|) + 60 n∑ 
m=0 
αm αn 
Ĉ(2m) log(T/δ) 
(notations are defined at the beginning of this section). 
Proof ∑En 
τ=tn (g̃τ −Rτ ) is trivially upper bounded by 3Ĉ(En − tn + 1) + 1 ≤ 4Ĉ(2n) because it 
is guarded by Test 2. Below we focus on the second claim. 
27
WEI LUO 
Note that we can write for all i = 1, . . . ,K,∑ τ∈I′i 
(f?τ − g̃τ ) 
≤ 12 ∑ τ∈I′i 
( 1 
[ f?τ − g̃τ ≤ 12α̂n 
] α̂n + 
n∑ m=1 
1 
[ 12α̂m < f?τ − g̃τ ≤ 12α̂m−1 
] α̂m−1 + 1 
[ f?τ − g̃τ > 12α̂0 
] 1 
) 
≤ 12 
( |I ′i|α̂n + 
n∑ m=1 
α̂m−1ξi(m) + ρ(1)ξi(0) 
) (ρ(1) ≥ 1 by Assumption 1) 
≤ 12|I ′i|α̂n + 24 n∑ 
m=0 
α̂mξi(m) (α̂m = Ĉ(2m) 2m ≤ Ĉ(2m+1) 
2m = 2α̂m+1) 
where in the second-to-last inequality we use ∑ 
τ∈I′i 1 [ f?τ − g̃τ ≥ 12α̂m 
] = ∑ 
τ∈[τi(m),e′i] 1 [ f?τ − 
g̃τ ≥ 12α̂m ] ≤ ξi(m) by the definition of τi(m). 
Summing the above over intervals i and notice that ∑` 
i=1 |I ′i| ≤ 2n, we get 
En∑ τ=tn 
(f?τ − g̃τ ) ≤ 12 · 2nα̂n + 24 n∑ 
m=0 
∑̀ i=1 
α̂mξi(m) = 12Ĉ(2n) + 24 n∑ 
m=0 
∑̀ i=1 
α̂mξi(m). (16) 
Next, we upper bound ∑` 
i=1 α̂mξi(m) for each m. 
∑̀ i=1 
α̂mξi(m) = ∑̀ i=1 
α̂m min {ξi(m), 4 · 2m}+ ∑̀ i=1 
α̂m [ξi(m)− 4 · 2m]+ . (17) 
(using a = min{a, b}+ [a− b]+) 
The first term on the right-hand side of Eq. (17) can be bounded as below: 
∑̀ i=1 
α̂m min {ξi(m), 4 · 2m} ≤ 4 ∑̀ i=1 
ρ̂(2m)×min {ξi(m), 2m} 
≤ 4 ∑̀ i=1 
ρ̂(min{ξi(m), 2m})×min {ξi(m), 2m} 
(ρ̂(·) is a decreasing function) 
= 4 ∑̀ i=1 
Ĉ(min{ξi(m), 2m}) 
≤ 4 ∑̀ i=1 
Ĉ(|I ′i|). (Ĉ(·) is an increasing function) 
The second term on the right-hand side of Eq. (17) is bounded using Lemma 17 below. Combining them into Eq. (16) finishes the proof. 
28
BLACK-BOX NON-STATIONARY RL 
Lemma 17 Let the high probability events described in Lemma 3 (or Lemma 12) hold. Then with high probability, 
∑̀ i=1 
α̂m [ξi(m)− 4 · 2m]+ ≤ 2αm αn 
Ĉ(2m) log(T/δ). 
Proof Using the fact that [[a]+ − b]+ = [a− b]+ when b ≥ 0, we have 
[ξi(m)− 4 · 2m]+ = [ e′i − τi(m) + 1− 4 · 2m 
] + . (18) 
Next, we consider the following quantity: “the number of rounds in the interval [τi(m), e′i − 2 · 2mB] which are candidate starting points of an order-m ALG”. By Procedure 1, this quantity can be written and lower bounded as 
Ai , ∑ t∈Ii 
1 
[ t ∈ [τi(m), e′i − 2 · 2m], (t− tn) mod 2m = 0 
] ≥ 
[e′i − τi(m) + 1− 4 · 2m]+ 2m 
where we use the fact in an interval of length w, there are at least w+2−2u u points whose indices 
are multiples of u. Notice that the right-hand side is related to what we want to upper bound in the lemma according to Eq. (18). Thus we continue to upper bound the left-hand side above. We define the following events: 
Wt = {τi(m) ≤ t ≤ ei − 2 · 2m where i is such that t ∈ Ii} , Xt = {t ≤ En − 2 · 2m} , Yt = {t ≤ En and (t− tn) mod 2m = 0} , Zt = {∃ order-m alg such that alg.s = t} , Vt = {∃τ ∈ [tn, t] such that Wτ ∩ Yτ ∩ Zτ} . 
Then we can write (recall the definition of K in the beginning of this section) 
∑̀ i=1 
Ai = 
K∑ i=1 
Ai = 
tn+2n−1∑ t=tn 
1[Wt, Xt, Yt] ≤ tn+2n−1∑ t=tn 
1[Wt, Yt, Vt]︸ ︷︷ ︸ term3 
+ 
tn+2n−1∑ t=tn 
1[Xt, Vt]︸ ︷︷ ︸ term4 
For term3, notice that conditioned on Wt∩Yt, the event Zt happens with a constant probability αn αm 
(by Procedure 1). Therefore, term3 counts the number of trials up to the first success in a repeated trial with success probabiliy αn 
αm . Therefore, with probability 1− δ 
T , term3 ≤ 1 + log(T/δ) 
− log ( 
1− αn αm 
) ≤ 2αm αn 
log(T/δ). Next, we deal with term4. Below we show that term4 = 0. The event Vt implies that there exists 
some order-m alg which starts at alg.s = t?, where t? ≤ t and τi(m) ≤ t? ≤ ei−2 ·2m. Therefore, we have alg.e = alg.s+ 2m − 1 = t? + 2m − 1 ≤ ei − 2m − 1 < ei, and thus [alg.s, alg.e] ⊆ Ii. Together with Xt, the event Vt ∩Xt implies that alg.e = alg.s+ 2m − 1 ≤ t+ 2m − 1 < En, and therefore, and time alg.e, block n has not ended. 
29
WEI LUO 
Since at time alg.e, block n is still on-going, the learner performs Test 1. By Lemma 3 (or Lemma 12 for the infinite-horizon RL case), with high probability, we have 
1 
2m 
alg.e∑ τ=alg.s 
Rτ ≥ 1 
2m 
alg.e∑ τ=alg.s 
g̃τ − α̂m − n̂∆[alg.s,alg.e] (Lemma 3 or Lemma 12) 
≥ min τ∈Ii 
f?τ − α̂m − (n̂+ 1)∆Ii (because [alg.s, alg.e] ⊆ Ii) 
≥ f?τi(m) − α̂m − (n̂+ 3)∆Ii (|minτ∈Ii f ? τ − f?τi(m)| ≤ 2∆Ii) 
≥ g̃τi(m) + 12α̂m − 2α̂m 
(by the definition of τi(m) and ∆Ii ≤ ρ(|Ii|) ≤ ρ(2m) ≤ α̂m 6n̂ ) 
≥ Ualg.e + 10α̂m (Because alg.e ≥ τi(m), Ualg.e ≤ g̃τi(m) by the algorithm) 
This should trigger the restart at time alg.e < En, contradicting the definition of En. Therefore, 1[Xt, Vt] = 0. 
Finally, combining all previous arguments, we have that with high probability, 
∑̀ i=1 
α̂m [ξi(m)− 4 · 2m]+ = ∑̀ i=1 
α̂m [ e′i − τi(m) + 1− 4 · 2m 
] + ≤ α̂m2m 
∑̀ i=1 
Ai 
= Ĉ(2m) ∑̀ i=1 
Ai ≤ 2αm αn 
Ĉ(2m) log(T/δ), 
finishing the proof. 
Appendix D. Single-block Regret Analysis II (under a Special Form of C(·)) 
In Appendix C, we have derived the regret bound in a single block for both the standard setting and the infinite-horizon MDP setting (Lemma 4 and Lemma 13). They are both of the form 
∑ τ∈J 
(f?τ −Rτ ) = Õ 
(∑̀ i=1 
C(|I ′i|) + 
n∑ m=0 
ρ(2n) 
ρ(2m) C(2m) 
) . (19) 
(replacing C(·) and ρ(·) by CUCRL(·;D) and ρ(·;D) for the case of infinite-horizon MDP). In this section, we further derive more concrete dynamic regret bounds for both cases by assum-
ing that C(·) is of some specific form. The form of C(·) we consider in this section is defined as follows: 
Definition 18 We define a form of C(t) as C(t) = min{c1t p + c2, c3t} for some p ∈ [1 
2 , 1) and some c1, c2, c3 (c3 ≥ 1) that capture dependencies on log(T/δ) and other problem-dependent constants. 
In fact, usually, a regret bound is only written in the form of c1t p + c2. However, since the reward is 
bounded between 0 and 1, the regret bound of min{c1t p+c2, t} is also trivially correct. Definition 18 
is slightly more general than this by allowing a coefficient c3 ≥ 1 (the regret bound would still be 
30
BLACK-BOX NON-STATIONARY RL 
trivially correct). In some cases, we make c1, c2, c3 larger than their tightest possible values to make the final regret bound better — notice that the choice of c1, c2, c3 affects the probability specified in Procedure 1, and thus smaller c1, c2, c3 does not necessarily make the final regret bound smaller. This subtle issue can be observed from the analysis. 
To get a concrete bound, we also need to decide the number ` in the single-block regret bound above. In Appendix C, we have stated the condition (i.e., Eq. (15)) that should be satisfied by I ′1, . . . , I ′` (or I1, . . . , IK). In the next lemma, we upper bound the value of ` that is required to fulfill the condition. 
Lemma 19 Let J = [tn, En]. Then we have ` ≤ LJ . Furthermore, if C(t) is in the form specified 
in Definition 18, we also have ` ≤ 1 + 2 ( c−1 
1 ∆J |J |1−p ) 1 
2−p + c−1 3 ∆J . 
Proof The fact that ` ≤ LJ is straightforward to see (and has been explained in Appendix C): to satisfy the condition Eq. (15), one way to divide the block is to make each Ii a stationary interval, which makes ∆Ii = 0 for all i ∈ [K]. This way of division leads to ` ≤ LJ . 
For the second claim, we follow the same procedure as decribed in the proof of Lemma 5 in (Chen et al., 2019). Basically, the procedure divides [tn, tn + 2n − 1] in a greedy way, making all Ii = [si, ei] satisfy ∆[si,ei] ≤ ρ(ei − si + 1) and ∆[si,ei+1] > ρ(ei − si + 2) for all i ∈ [K − 1] (i.e., except for the last interval). Then we have 
∆J ≥ `−1∑ i=1 
∆[si,ei+1] (by the definition of ∆[·,·]) 
> 
`−1∑ i=1 
ρ(ei − si + 2) 
≥ `−1∑ i=1 
min { c1(ei − si + 2)p−1, c3 
} (by Definition 18) 
≥ `−1∑ i=1 
min 
{ 1 
2 c1(ei − si + 1)p−1, c3 
} ((x+ 2)p−1 ≥ (2(x+ 1))p−1 ≥ 1 
2(x+ 1)p−1 for any x ≥ 0 and p ≤ 1) 
= 1 
2 
`1∑ i=1 
c1(ei − si + 1)p−1 + 
`2∑ i=1 
c3 
where in the last equality we separate the intervals where min { 
1 2c1(ei − si + 1)p−1, c3 
} takes the 
former or the latter value. Note that `1 + `2 = `− 1. The above inequality implies that ∆J upper bounds both 1 
2 
∑`1 i=1 c1(ei−si+1)p−1 and 
∑`2 i=1 c3. 
Thus, `2 ≤ c−1 3 ∆J , and by Hölder’s inequality, 
`1 ≤ 
( `1∑ i=1 
(ei − si + 1)p−1 
) 1 2−p ( 
`1∑ i=1 
(ei − si + 1) 
) 1−p 2−p 
≤ ( 
2∆J c1 
) 1 2−p |J | 
1−p 2−p . 
Combining them finishes the proof. 
31
WEI LUO 
In the following Lemma 20, we bound the regret within a block by combining Eq. (19) and Lemma 19. We will frequently use the following two properties: let {S1,S2, . . . ,SK} be a partition of the interval S. Then 
K∑ i=1 
LSi ≤ LS + (K − 1), (20) 
K∑ i=1 
∆Si ≤ ∆S . (21) 
They can be derived using the definitions of L[·,·] and ∆[·,·]. 
Lemma 20 If C(t) is of the form specified in Definition 18, then 
En∑ τ=tn 
(f?τ −Rτ ) ≤ Õ ( 
min { 
RegL(J ),Reg∆(J ) } 
+ c12np + c2c3 
c1 2n(1−p) + 
c2 2 
c3 
) , 
where RegL(J ) , c1L 1−p J |J |p + c2LJ and 
Reg∆(J ) , ( c1∆1−p 
J |J | ) 1 
2−p + c1|J |p + c1(c−1 
3 ∆J )1−p|J |p + c2 
( c−1 
1 ∆J |J |1−p ) 1 
2−p + c2 + c2c −1 3 ∆J . 
Proof We bound each term in Eq. (19) using Definition 18. First, notice that 
Õ 
(∑̀ i=1 
C(|I ′i|) 
) = Õ 
(∑̀ i=1 
min { c1|I ′i|p + c2, c3t 
}) 
≤ Õ 
(∑̀ i=1 
(c1|I ′i|p + c2) 
) ≤ Õ 
( c1` 
1−p|J |p + c2` ) . (22) 
Using the first upper bound for ` given in Lemma 19, Eq. (22) can be bounded by Õ (RegL(J )); using the second upper bound, Eq. (22) can be bounded by Õ (Reg∆(J )). Next, we have 
Õ ( ρ(2m) 
ρ(2n) C(2m) 
) = Õ 
( c12np + 
c2c3 
c1 2n(1−p) + 
c2 1 
c3 2m(2p−1) + 
c2 2 
c3 2−m 
) . 
by Lemma 21 below. Notice that because c3 ≥ 1 and p ≥ 1 2 , c 
2 1 c3 
2m(2p−1) ≤ c2 12n(2p−1) ≤ c12np 
when c1 ≤ 2n(1−p). This is indeed the regime we care about since if c1 > 2n(1−p) then the first term c12np > 2n, which is a vacuous bound for the regret of block n. Therefore, we can drop this term. Thus, the dynamic regret in block n can be summarized as the following based on Eq. (19): 
Õ ( 
min { 
RegL(J ),Reg∆(J ) } 
+ c12np + c2c3 
c1 2n(1−p) + 
c2 2 
c3 
) , (23) 
finishing the proof. 
32
BLACK-BOX NON-STATIONARY RL 
Lemma 21 Let C(t) be of the form in Definition 18. Then 
ρ(2m) 
ρ(2n) C(2m) = O 
( c12np + 
c2c3 
c1 2n(1−p) + 
c2 1 
c3 2m(2p−1) + 
c2 2 
c3 2−m 
) . 
Proof This is by direct calculation: 
ρ(2m) 
ρ(2n) C(2m) = 
C(2m)2 
C(2n) 2n−m 
= O ( 
min{c2 122mp + c2 
2, c 2 322m} 
c12np + c2 2n−m + 
min{c2 122mp + c2 
2, c 2 322m} 
c32n 2n−m 
) = O 
( min 
{ c12np2(n−m)(1−2p) + 
c2 2 
c1 2n(1−p)−m, 
c2 3 
c1 2n(1−p)+m 
} + c2 
1 
c3 2m(2p−1) + 
c2 2 
c3 2−m 
) = O 
( c12np + min 
{ c2 
2 
c1 2n(1−p)−m, 
c2 3 
c1 2n(1−p)+m 
} + c2 
1 
c3 2m(2p−1) + 
c2 2 
c3 2−m 
) = O 
( c12np + 
c2c3 
c1 2n(1−p) + 
c2 1 
c3 2m(2p−1) + 
c2 2 
c3 2−m 
) . 
Appendix E. Single-epoch Regret Analysis 
We call [t0, E] an epoch if t0 is the first step after restart (or t0 = 1), and E is the first time after round t0 when the restart is triggered. In this section, we continue the discussion in Appendix D and bound the regret in a single epoch. Recall that the we consider cases where the single-block regret can be written as Eq. (19) and C(·) is in the form of Definition 18. This holds both for the case of the standard setting and the infinite-horizon MDP setting. 
Lemma 22 Let E be an epoch. Then∑ τ∈E ≤ Õ 
( min 
{ RegL(E),Reg∆(E) 
} + c2c3 
c1 |E|1−p + 
c2 2 
c3 
) (RegL(·) and Reg∆(·) are defined in Lemma 20) 
Proof Let E be an epoch whose last block is indexed by n. Then |E| = Θ(2n). Let J1, . . . ,Jn be blocks in E . Then by Lemma 20, the dynamic regret in E is upper bounded by 
Õ 
( min 
{ n∑ 
m=0 
RegL(Jm), n∑ 
m=0 
Reg∆(Jm) 
} + c1 
n∑ m=0 
2mp + c2c3 
c1 
n∑ m=0 
2m(1−p) + n∑ 
m=0 
c2 2 
c3 
) . 
By Hölder’s inequality, 
n∑ m=0 
RegL(Jm) = c1 
( n∑ 
m=0 
LJm 
)1−p( n∑ m=0 
|Jm| 
)p + c2 
n∑ m=0 
LJm 
33
WEI LUO 
≤ c1 (LE + n)1−p |E|p + c2 (LE + n) (using Eq. (20)) 
≤ Õ ( c1L 
1−p E |E| 
p + c2LE 
) = Õ (RegL(E)) (because n = O(log T ) = Õ(1)) 
Similarly, ∑n 
m=0 Reg∆(Jm) = Õ (Reg∆(E)). On the other hand, 
c1 ∑n 
m=0 2mp + c2c3 c1 
∑n m=0 2m(1−p) + 
∑n m=0 
c22 c3 
= Õ ( c12np + c2c3 
c1 2n(1−p) + 
c22 c3 
) = 
Õ ( c1|E|p + c2c3 
c1 |E|1−p + 
c22 c3 
) . In summary, the dynamic regret within an epoch is of order 
Õ ( 
min { 
RegL(E),Reg∆(E) } 
+ c2c3 
c1 |E|1−p + 
c2 2 
c3 
) (24) 
(the c1|E|p term is absorbed into min {RegL(E),Reg∆(E)}). 
Appendix F. Proof of Theorem 2 
We are now ready to prove Theorem 2 after showing the following two lemmas. 
Lemma 23 Let t be in an epoch starting from t0. If ∆[t0,t] ≤ ρ(t − t0 + 1), then with high probability, no restart would be triggered at time t. 
Proof We first verify that Test 1 would not fail with high probability. Let t = alg.e where alg is any order-m ALG in block n. Then with high probability, 
Ut = min τ∈[tn,t] 
g̃τ 
≥ min τ∈[tn,t] 
f?τ −∆[tn,t] (by Lemma 3) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
f?τ − 3∆[tn,t] ([alg.s, t] ⊆ [tn, t]) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 2 
√ log(T/δ) 
2m − 3ρ(t− t0 + 1) 
(E[Rτ ] = E[fτ (πt)] ≤ f?τ and we use Azuma’s inequality) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − ρ̂(2m)− 3ρ(t− t0 + 1) 
(By Assumption 1, ρ̂(2m) ≥ 6 log(T/δ)ρ(2m) ≥ 6 log(T/δ) √ 
1 2m ) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 2ρ̂(2m). (ρ(t− t0 + 1) ≤ ρ(2m) because ρ(·) is decreasing) 
So with high probability, Test 1 will not return fail. Furthermore, by Lemma 3, with high probability, 
1 
t− tn + 1 
t∑ τ=tn 
(g̃τ −Rτ ) ≤ ρ̂(t− tn + 1) + ∆[tn,t] ≤ 2ρ̂(t− tn + 1). 
34
BLACK-BOX NON-STATIONARY RL 
Therefore, with high probability, Test 2 will not return fail either. 
Lemma 24 With high probability, the number of epochs is upper bounded by L. If C(·) is in the 
form of Definition 18, the number of epochs is also upper bounded by 1+2 ( c−1 
1 ∆T 1−p) 1 2−p +c−1 
3 ∆. 
Proof By Lemma 23, if [t0, E] is not the last epoch, then ∆[t0,E] > ρ(E − t0 + 1) with high probability. Then following the exact same arguments as in Lemma 19 proves the lemma. 
Proof [Proof of Theorem 2] If C(t) = c1t p + c2 satisfies Assumption 1, then C(t) = min{c1t 
p + c2, t} also satisfies it (since the reward is bounded in [0, 1]). Below we useC(t) = min{c1t 
p+c2, t} as the input to our algorithm. Notice that this is in the form of Definition 18 with c3 = 1. Let E1, . . . , EN be epochs in [1, T ]. Then by Lemma 22, the dynamic regret in [1, T ] is upper bounded by 
Õ 
( min 
{ N∑ i=1 
RegL(Ei), N∑ i=1 
Reg∆(Ei) 
} + c2 
c1 
N∑ i=1 
|Ei|1−p + c2 2N 
) . (25) 
By Hölder’s inequality and Eq. (20), 
N∑ i=1 
RegL(Ei) ≤ Õ ( c1 (L+N − 1)1−p T p + c2(L+N − 1) 
) ≤ Õ 
( c1L 
1−pT p + c2L ) , 
where in the last inequality we use Lemma 24 to bound N . Similarly, 
N∑ i=1 
Reg∆(Ei) 
≤ Õ (( c1∆1−pT 
) 1 2−p + c1N 
1−pT p + c1∆1−pT p + c2 
( c−1 
1 ∆T 1−p) 1 2−p + c2N + c2∆ 
) ≤ Õ 
(( c1∆1−pT 
) 1 2−p + c1T 
p + c1∆1−pT p + c2 
( c−1 
1 ∆T 1−p) 1 2−p + c2 + c2∆ 
) . 
(using Lemma 24 to bound N ) 
Then we deal with the second term in Eq. (25): 
c2 
c1 
N∑ i=1 
|Ei|1−p ≤ c2 
c1 NpT 1−p, 
which can be either bounded by Õ ( c2 c1 LpT 1−p 
) or 
Õ ( c2 
c1 T 1−p + 
c2 
c1 
( c−p1 ∆pT 2−2p 
) 1 2−p 
+ c2 
c1 ∆pT 1−p 
) 
35
WEI LUO 
using the upper bound for N in Lemma 24. Finally, the third term in Eq. (25) can be upper bounded either by Õ 
( c2 
2L ) 
or 
Õ ( c2 
2 + c2 2 
( c−1 
1 ∆T 1−p) 1 2−p + c2 
2∆ 
) . 
With all terms expanded, below, we collect the dominant terms for the cases of p = 1 2 and 
p > 1 2 . We say term a(T ) is dominated by b(T ) if limT→∞ a(T )/b(T ) = 0 under any sublinear 
growth rate of L or ∆ (e.g., √ 
∆T is dominated by ∆1/3T 2/3 and L is dominated by √ LT ). And 
below we only write down terms that are not dominated by other terms. 
The case for p = 1 2 : 
Õ ( 
min 
{( c1 + 
c2 
c1 
)√ LT , 
( c 2/3 1 + c2c 
−4/3 1 
) ∆ 
1/3T 2/3 + 
( c1 + 
c2 
c1 
)√ T 
}) ; 
The case for p > 1 2 : 
Õ ( 
min { c1L 
1−pT p, ( c1∆1−pT 
) 1 2−p + c1T 
p }) 
. 
This finishes the proof. 
Appendix G. Main Results for Infinite-horizon MDP 
Lemma 25 (c.f. Lemma 23) Let t be in an epoch started from round t0. If ∆[t0,t];D < 
DS √ 
A t−t0+1 and D ≥ Dmax, then with high probability, no restart will be triggered at time t. 
Proof To verify that Test 1 will not fail with high probability, we follow very similar steps as in Lemma 23. Let t = alg.e where alg is an order-m ALG in block n. Then with high probability (the following calculation is same as that in the proof of Lemma 23 except for the third inequality), 
Ut = min τ∈[tn,t] 
g̃τ 
≥ min τ∈[tn,t] 
J?τ −∆[tn,t];D (by Lemma 12) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
J?τ − 3∆[tn,t];D ([alg.s, t] ⊆ [t0, t]) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 4D 
√ log(T/δ) 
2m − 4∆[tn,t];D 
(explained below) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 4ρ̂UCRL(2m;D)− 4ρUCRL(t− t0 + 1;D) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 8ρ̂UCRL(2m;D). (ρ(t− t0 + 1) ≤ ρ(2m) because ρ(·) is decreasing) 
36
BLACK-BOX NON-STATIONARY RL 
where the third inequality is based on the following calculation: for all τ ∈ [alg.s, t], 
J?t = rt(sτ , aτ ) + ∑ s′ 
pt(s ′|sτ , aτ )h?t (s 
′)− h?t (sτ ) 
≥ rτ (sτ , aτ ) + ∑ s′ 
pτ (s′|sτ , aτ )h?t (s ′)− h?t (sτ )− 
( ∆r 
[alg.s,t] +Dmax∆p [alg.s,t] 
) ≥ rτ (sτ , aτ ) + 
∑ s′ 
pτ (s′|sτ , aτ )h?t (s ′)− h?t (sτ )− 
( ∆r 
[alg.s,t] +D∆p [alg.s,t] 
) (by the assumption D ≥ Dmax) 
and thus 
1 
2m 
∑ τ∈[alg.s,t] 
J?τ ≥ J?t −∆J [alg.s,t] 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
( rτ (sτ , aτ ) + 
∑ s′ 
pτ (s′|sτ , aτ )h?t (s ′)− h?t (sτ ) 
) −∆[alg.s,t];D 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
( Rτ + h?t (sτ+1)− h?t (sτ ) 
) − 2Dmax 
√ 2 log(SAT/δ) 
2m −∆[alg.s,t];D 
(Azuma’s inequality) 
≥ 1 
2m 
∑ τ∈[alg.s,t] 
Rτ − 4D 
√ log(SAT/δ) 
2m −∆[alg.s,t];D. (Dmax ≤ D) 
So with high probability, Test 1 will not return fail. Furthremore, by Lemma 12, with high probability, 
1 
t− tn + 1 
t∑ τ=tn 
(g̃τ −Rτ ) ≤ ρ̂UCRL(t− tn + 1;D) + ∆[tn,t];D ≤ 2ρ̂UCRL(t− tn + 1;D) 
where the last inequality is by the condition on ∆[t0,t],D . Therefore, with high probability, Test 2 
will not return fail either. It remains to show that the UCRL-ACW will not terminate and call for restart under the specified 
condition. By Lemma 7, if Pηk contains an MDP whose diameter is upper bounded by D, then the span of the output bias vector is upper bounded by 2D, and then the if-statement in Line 4 of Algorithm 4 will be triggered. Therefore, to show that UCRL-ACW will not terminate, we upper bound the ηk that needs to be added to Pk in order to make at least one true MDP (whose diameter is upper bounded by Dmax ≤ D) lie in Pηkk . Then we further argue that 
∑t τ=t0 
ηk(τ) is not large enough to reach the condition in Line 4 of Algorithm 4. 
For all episode k that starts before t, by Azuma’s inequality, 
‖pk(·|s, a)− p̂k(·|s, a)‖1 ≤ 2 
√ S log(1/δ) 
N+ k (s, a) 
. 
37
WEI LUO 
By the condition on ∆[t0,t];D , we have 
‖pt0(·|s, a)− pk(·|s, a)‖1 ≤ 1 
D ∆[t0,t];D 
≤ S √ 
A 
t− t0 + 1 . 
Combining them, we get 
‖pt0(·|s, a)− p̂k(·|s, a)‖1 ≤ 2 
√ S log(1/δ) 
N+ k (s, a) 
+ S 
√ A 
t− t0 + 1 . 
Therefore, we see that in Line 4 of Algorithm 4, as long as η ≥ S √ 
A t−t0+1 , pt0 is contained in Pηk . 
Then we have sp(h̃) ≤ 2Dmax ≤ 2D by Lemma 7, and the for-loop will be broken at this η. 
Thus we conclude that ηk ≤ 2S √ 
A t−t0+1 for all episode k started before t. Thus, 
∑t τ=t0 
ηk(τ) ≤ 
(t − t0 + 1) × 2S √ 
A t−t0+1 = 2S 
√ A(t− t0 + 1), and thus the algorithm will not terminate and 
call for restart at time t. 
Lemma 26 (c.f. Lemma 24) If D ≥ Dmax, then the number of epochs is upper bounded by 
min 
{ L, 1 + 3 
( ∆r+∆p 
S √ A 
) 2 3 T 
1 3 
} . 
Proof Let E1, . . . , EN be the epochs. By Lemma 25, for i ≤ N − 1, we must have ∆Ei;D ≥ 
DS √ 
A |Ei| . By Hölder’s inequality, 
N − 1 ≤ 
( N−1∑ i=1 
1√ |Ei| 
) 2 3 ( N−1∑ i=1 
|Ei| 
) 1 3 
≤ ( 
∆[1,T ];D 
DS √ A 
) 2 3 
T 1 3 . 
We can further upper bound the term 1 D 
∆[1,T ];D as follows: 
1 
D ∆[1,T ];D = 
1 
D 
( ∆r + 2D∆p + ∆J 
) ≤ 1 
D 
( 2∆r + (2D +Dmax)∆p 
) (by Lemma 10) 
≤ 3 
D 
( ∆r +D∆p 
) ≤ 3(∆r + ∆p). 
Thus we get 
N ≤ 1 + 3 
( ∆r + ∆p 
S √ A 
) 2 3 
T 1 3 . 
Also, by Lemma 25, when D ≥ Dmax, an epoch is created only when the reward function or the transition function changes. Thus the number of epochs is also upper bounded by L. 
38
BLACK-BOX NON-STATIONARY RL 
Lemma 27 In every epoch E , the dynamic regret of MASTER-UCRL is upper bounded by 
Õ ( X +DS 
√ A|E|+DS2A2 
) , 
where X is the minimum of the following two terms: 
DS √ ALE |E|+DSALE 
and ( D 
2 S2A∆E;D|E| 
2 )1/3 
+ SA √ D∆E;D|E|+ 
( DSA2∆2 
E;D |E| )1/3 
+ SA∆E;D. 
Proof Let E1, . . . , EN be the epochs. By Lemma 22, we know that the regret within an epoch E is Õ ( 
min {RegL(E),Reg∆(E)}+ c2c3 c1 |E|1−p + 
c22 c3 
) with 
RegL(E) = c1L 1−p E |E| 
p + c2LE , 
Reg∆(E) = ( c1∆1−p 
E;D |E| ) 1 
2−p + c1|E|p + c1(c−1 
3 ∆E;D)1−p|E|p + c2 
( c−1 
1 ∆E;D|E| 1−p ) 1 
2−p + c2 + c2c 
−1 3 ∆E;D 
when C(t) is in the form of Definition 18. In our case CUCRL(t;D) is in this form with c1 = DS √ A, c2 = DSA, c3 = D, and p = 1 
2 . Using them in the bound above, we get that in an epoch, the dynamic regret is upper bounded by 
Õ ( 
min {RegL(E),Reg∆(E)}+D √ A|E|+DS2A2 
) where 
RegL(E) = DS √ ALE |E|+DSALE 
Reg∆(E) = ( D 
2 S2A∆E;D|E| 
2 )1/3 
+DS √ A|E|+ SA 
√ D∆E;D|E|+ 
( DSA2∆2 
E;D |E| )1/3 
+DSA+ SA∆E;D. 
Collecting terms finishes the proof. 
Theorem 28 If Dmax ≤ D ≤ 2Dmax, then MASTER-UCRL guarantees the following dynamic regret bound: 
Õ ( 
min { DmaxS 
√ ALT,Dmax 
( S2A 
)1/3 (∆r + ∆r) 
1/3T 2/3 +DmaxS 
√ AT }) 
. 
Proof Let E1, . . . , EN be the epochs. The per epoch dynamic regret is given by Lemma 27. Com-bining them with Hölder’s inequality and Eq. (20), Eq. (21), the dynamic regret in [1, T ] can be upper bounded by 
Õ ( 
min{RegL,Reg∆}+DS √ ANT +DS2A2N 
) (26) 
39
WEI LUO 
where 
RegL = DS √ A(L+N)T +DSA(L+N) (27) 
and 
Reg∆ = ( D 
2 S2A∆[1,T ];DT 
2 )1/3 
+ SA √ D∆[1,T ];DT + 
( DSA2∆2 
[1,T ];D T )1/3 
+ SA∆[1,T ];D. 
(28) 
Since D ≥ Dmax, the number of epochs can be bounded using Lemma 26: 
N ≤ min 
{ L, 1 + 3 
( ∆r + ∆p 
S √ A 
) 2 3 
T 1 3 
} . 
With N ≤ L, Eq. (26), and Eq. (27), the dynamic regret in [1, T ] can bounded by (omitting lower order terms) 
Õ ( DS √ ALT 
) . (29) 
With N ≤ 1 + 3 ( 
∆r+∆p 
S √ A 
) 2 3 T 
1 3 , Eq. (26), and Eq. (28), the regret can alternatively be upper 
bounded by (omitting lower order terms) 
Õ (( 
D 2 S2A∆[1,T ];DT 
2 )1/3 
+DS √ AT +D(S2A) 
1/3(∆r + ∆p) 1/3T 
2/3 
) . (30) 
Then notice that D ≤ 2Dmax and thus ∆[1,T ];D = ∆r + 2D∆p + ∆J = O(∆r +Dmax∆p) where we use Lemma 10. Using these in Eq. (29) and Eq. (30) finishes the proof. 
Theorem 29 The doubling trick strategy described in Section 4.2 for the unknown Dmax and known L case has a dynamic regret bound of Õ 
( DmaxS 
√ ALT 
) ; for the unknown Dmax and 
known ∆ case, the bound is 
Õ ( DmaxS 
√ AT +Dmax(S2A) 
1/3(∆r + ∆p) 1/3T 
2/3 ) . 
Proof For the known L case, when D ≤ Dmax, recall that the number of epochs is forced to be N ≤ L. Similar to the proof of Theorem 28, the regret in any of these epochs is upper bounded by 
Õ ( DS √ ANT 
) = Õ 
( DS √ ALT 
) . 
Summing the above over D = 1, 2, 4, . . . , Dmax, we get Õ ( DmaxS 
√ ALT 
) . When D first enters 
[Dmax, 2Dmax], we use Theorem 28 to bound the regret in the rest of the rounds, which is still of order Õ 
( DmaxS 
√ ALT 
) . 
40
BLACK-BOX NON-STATIONARY RL 
For the case of known ∆ = ∆r + ∆p, the analysis is similar: when D ≤ Dmax, we force N = 1 + 3(S−2A−1∆2T )1/3, and thus the regret within any of these epochs is upper bounded by (similarly to the proof of Theorem 28) 
Õ (( 
D 2 S2A∆[1,T ];DT 
2 )1/3 
+DS √ AT +D(S2A) 
1/3(∆r + ∆p) 1/3T 
2/3 
) . 
Summing this over D = 1, 2, . . . , Dmax and using ∆[1,T ];D = ∆r + 2D∆p + ∆J = O(∆r + 
Dmax∆p) for D = O(Dmax), we get Õ ( Dmax 
( S2A∆T 2 
)1/3 +DmaxS 
√ AT ) 
. When D first enters [Dmax, 2Dmax], we use Theorem 28 to bound the regret in the rest of the rounds, which is still of the same order. 
Appendix H. Bandit-over-Reinforcement-Learning Approach 
The idea of the BoRL framework is to run a multi-armed bandit algorithm over a set of subalgorithms each using a different parameter. In our case, each sub-algorithm is a MASTER-UCRL with a different guess on Dmax. The set of D only needs to span the range of [1, 
√ T ], since if 
Dmax = Ω( √ T ), the regret bound would be vacuous. 
We divide the horizon into T B equal-length intervals each of length B = S 
√ AT . In each 
interval, sub-algorithm i restarts a MASTER-UCRL with D = 2i−1. The reward of sub-algorithm i in interval b ∈ [ TB ] is its total reward gained in the MDP for this interval. We denote i? as the sub-algorithm that uses D ∈ [Dmax, 2Dmax]. 
On top of these sub-algorithms, we run the EXP3.P algorithm (Auer et al., 2002b). The “arms” are the sub-algorithms. From the above description, for this EXP3.P, there are M = dlog2 
√ T e 
arms, the algorithm proceeds for T B rounds, and in each round the reward range is B. By the 
standard regret bound of EXP3.P, the learner’s regret against sub-algorithm i? is of order 
Õ 
( B 
√ M T 
B +BM 
) = Õ 
(√ BT ) . 
with high probability. On the other hand, in each interval b ∈ 
[ T B 
] , since sub-algorithm i? uses a correct guess of D, 
by Theorem 28, its regret against the best sequence of policy in that interval is 
Õ ( 
min { DmaxS 
√ ALbB, Dmax(S2A) 
1 3 (∆b) 
1 3B 
2 3 +DmaxS 
√ AB }) 
where we abuse notations and denote Lb = L[(b−1)B+1,bB], ∆b = ∆[(b−1)B+1,bB]. Combining the two bounds above, we get that the regret of the learner against the best sequence 
of policies in [1, T ] is 
Õ 
√BT + 
T B∑ b=1 
min { DmaxS 
√ ALbB, Dmax(S2A) 
1 3 (∆b) 
1 3B 
2 3 +DmaxS 
√ AB } 
= Õ 
( √ BT + min 
{ DmaxS 
√ A 
( L+ 
T 
B 
) T , Dmax(S2A) 
1 3 (∆) 
1 3T 
2 3 +DmaxS 
√ AB × T 
B 
}) (using Eq. (20) and Eq. (21)) 
41
WEI LUO 
= Õ 
( √ BT +DmaxS 
√ A 
B T + min 
{ DmaxS 
√ ALT, Dmax(S2A) 
1 3 ∆ 
1 3T 
2 3 
}) . 
Using the B that we specified above, we get 
Õ ( Dmax(S2A) 
1/4T 3/4 + min 
{ DmaxS 
√ ALT, Dmax(S2A) 
1 3 ∆ 
1 3T 
2 3 
}) . 
Appendix I. Verifying Assumption 1 for Several Algorithms 
To prove Eq. (1), it suffices to prove the following. 
Assumption 1’ There exist universal constants c1, c2, c3, c4, c5, c6 > 0 such that for all t = 1, 2, . . ., as long as ∆[1,t] ≤ c1ρ(t), the following holds with probability 1− δ 
T : 
f̃t ≥ min τ∈[1,t] 
f?τ − c2∆[1,t] (31) 
1 
t 
t∑ τ=1 
( f̃τ −Rτ 
) ≤ c3ρ(t) + c4∆[1,t]. (32) 
Furthermore, ρ(t) ≥ c5√ t , ∆(t) ≥ c6 maxπ |ft(π)− ft+1(π)|. 
This is because for an algorithm satisfying Assumption 1’, we can redefine ∆(t)← (c3/c1 + c2 + c4 + 1/(c1c5) + 1/c6)∆(t) and ρ(t) ← (c3 + c1c2 + c1c4 + 1/c5 + c1/c6)ρ(t). Then Eq. (1) is satisfied. Our verification below is thus mostly based on Assumption 1’ for simplicity. 
The following proofs are brief (some of them are just sketches) since they follow standard analysis and mostly appear in previous works. Please find more details in the references. We sometimes make minor modifications to the original algorithm to make them more aligned with our framework. 
I.1. UCB1 for Multi-armed Bandits 
Algorithm 7: UCB1 for multi-armed bandits input: A (number of arms), T, δ. for t = 1, . . . , T do 
Choose at = argmaxa∈[A] 
( r̂t,a + c 
√ log(T/δ) 
N+ t,a 
) / c > 0 is some universal constant 
where 
r̂t,a = 
∑t−1 τ=1Rτ1[aτ = a] 
N+ t,a 
, N+ t,a = max 
{ 1, 
t−1∑ τ=1 
1[aτ = a] 
} . (33) 
Receive Rt with E[Rt] = rt,at . end 
In this subsection, we consider the multi-armed bandit problem and the UCB1 algorithm by Auer et al. (2002a). Suppose there are A arms, and let rt,a denote the expected reward of arm a at 
42
BLACK-BOX NON-STATIONARY RL 
time t. Then the multi-armed bandit problem fits in our framework with Π = [A] and ft(a) = rt,a. Below, we show that the UCB1 algorithm satisfies Assumption 1’. 
The pseudocode of UCB1 is presented in Algorithm 7. At time t, UCB1 chooses the arm that 
has the highest optimistic reward estimator r̃t,a , r̂t,a + c 
√ log(T/δ) 
N+ t,a 
, where r̂t,a is the empirical 
mean of the reward of arm a up to time t− 1, Nt,a is the cumulative number of pulls of arm a up to time t − 1 and N+ 
t,a = max{1, Nt,a}, all defined in Eq. (33); c > 0 is some universal constant that is determined by Azuma’s inequality. 
To see that UCB1 satisfies Assumption 1’, we define 
∆(t) = max a |rt,a − rt+1,a|, f̃t = max 
a r̃t,a, ρ(t) = 
√ A log(T/δ) 
t + A log(T/δ) 
t . (34) 
Furthermore, denote rt,a = ∑t−1 τ=1 rτ,a1[at=a] 
Nt,a (define rt,a = 1 if Nt,a = 0 for simplicity). Note that 
with high probability, 
f̃t ≥ max a 
rt,a ≥ max a 
max τ≤t 
rτ,a −∆[1,t] ≥ min τ≤t 
max a 
rτ,a −∆[1,t], 
where the first inequality is because with high probability, r̃t,a ≥ rt,a by Azuma’s inequality. This verifies Eq. (31). 
On the other hand, by the selection rule at = argmaxa r̃t,a, we have with probability 1− δ, 
t∑ τ=1 
(f̃τ −Rτ ) ≤ t∑ 
τ=1 
(r̃τ,aτ − rτ,aτ ) + t∑ 
τ=1 
(rτ,aτ −Rτ ) 
= t∑ 
τ=1 
( rτ,aτ − rτ,aτ + c 
√ log(T/δ) 
N+ τ,a 
) + 
t∑ τ=1 
(rτ,aτ −Rτ ) 
≤ t∆[1,t] +O (√ 
At log(T/δ) +A log(T/δ) ) 
where in the last inequality we use rτ,aτ −rτ,aτ ≤ ∆[1,t] and the standard pigeonhole argument, and use Azuma’s inequality to bound 
∑t τ=1(rτ,aτ −Rτ ). This proves Eq. (32). Note that the condition 
∆[1,t] = O(ρ(t)) in Assumption 1’ is even not needed. 
I.2. OFUL for Linear Bandits 
In this subsection, we consider linear bandits with a fixed action set, and the OFUL algorithm by Abbasi-Yadkori et al. (2011). The original OFUL algorithm handles the case where the action set can change over time (also known as the linear contextual bandit setting), but this is beyond the main focus of this paper. Let A be the action set, and θt be the reward vector at time t. Then the linear bandit problem fits in our framework with Π = A and ft(a) = a>θt. 
The pseudocode of OFUL (with a fixed action set) is presented in Algorithm 8. For simplicity, assume that for all actions a ∈ A, ‖a‖2 ≤ 1, and for all t, the reward vector θt satisfies ‖θt‖2 ≤ 1. The OFUL algorithm chooses the action at = argmaxa a 
>θ̂t + 2β‖a‖Λ−1 t 
at time t, where β, 
Λt = I + ∑t−1 
τ=1 aτa > τ , and θ̂t are defined in Eq. (35). 
43
WEI LUO 
Algorithm 8: OFUL for linear bandits 
input: A ⊂ Rd (action set), T, δ. for t = 1, 2, . . . , T do 
Choose at = argmaxa∈A 
( a>θ̂t + 2β‖a‖Λ−1 
t 
) , 
where 
β = 4 √ d log(T/δ), Λt = I + 
t−1∑ τ=1 
aτa > τ , θ̂t = Λ−1 
t 
t−1∑ τ=1 
Rτaτ . (35) 
Receive Rt with E[Rt] = a>t θt. end 
Then we define 
∆(t) = d √ 
log(T/δ)‖θt − θt+1‖2, f̃t = max a∈A 
( a>θ̂t + 2β‖a‖Λ−1 
t 
) , ρ(t) = β 
√ d log(T/δ) 
t . 
(36) 
Below, we verify that OFUL satisfies Assumption 1’ with the choices in Eq. (36). Under the assumption that ∆[1,t] ≤ ρ(t), for any action a, by similar arguments as in (Zhao et al., 2020, Lemma 1), 
∣∣∣a>(θt − θ̂t) ∣∣∣ ≤ ∣∣∣∣∣a>Λ−1 
t 
t−1∑ τ=1 
aτa > τ (θs − θt) 
∣∣∣∣∣+ β‖a‖Λ−1 t 
≤ t−1∑ τ=1 
∣∣∣a>Λ−1 t aτ 
∣∣∣ ∣∣∣a>τ (θτ − θt) ∣∣∣+ β‖a‖Λ−1 
t 
≤ ∆[1,t] 
d √ 
log(T/δ) × 
( t−1∑ τ=1 
‖a‖Λ−1 t ‖aτ‖Λ−1 
t 
) + β‖a‖Λ−1 
t 
( a>τ (θτ − θt) ≤ ‖θτ − θt‖2 ≤ ∆[1,t] 
d √ 
log(T/δ) ) 
≤ ∆[1,t] 
d √ 
log(T/δ) × ‖a‖Λ−1 
t × 
√√√√(t− 1) 
t−1∑ τ=1 
‖aτ‖2Λ−1 t 
+ β‖a‖Λ−1 t 
(Cauchy-Schwarz) 
≤ 
( β + ∆[1,t] 
√ t 
d log(T/δ) 
) ‖a‖Λ−1 
t 
( ∑t−1 
τ=1 ‖aτ‖2V −1 t−1 
= tr(Λ−1 t 
∑t−1 τ=1 aτa 
> τ ) ≤ d) 
≤ 2β‖a‖Λ−1 t . (by the assumption ∆[1,t] ≤ ρ(t)) 
(37) 
44
BLACK-BOX NON-STATIONARY RL 
Thus, 
t∑ τ=1 
( f̃τ −Rτ 
) = 
t∑ τ=1 
( f̃τ − a>τ θτ 
) + 
t∑ τ=1 
( a>τ θτ −Rτ 
) = 
t∑ τ=1 
a>τ 
( θ̂τ − θτ 
) + 2 
t∑ τ=1 
β‖aτ‖Λ−1 τ 
+O (√ 
t log(T/δ) ) 
(by the definition of f̃τ and that OFUL chooses aτ = argmaxa 
( a>θ̂τ + 2β‖a‖Λ−1 
τ 
) ) 
= O 
( t∑ 
s=1 
β‖as‖Λ−1 s 
) +O 
(√ t log(T/δ) 
) (by Eq. (37)) 
= O ( β √ dt log t 
) = O (tρ(t)) ≤ O 
( tρ(t) + t∆[1,t] 
) . 
This verifies Eq. (32). Also, by Eq. (37), 
f̃t = max a 
( a>θ̂t + 2β‖a‖Λ−1 
t 
) ≥ max 
a a>θt = f?t ≥ min 
τ∈[1,t] f?τ −∆[1,t]. 
This verifies Eq. (31). 
I.3. GLM-UCB for Generalized Linear Bandits 
Algorithm 9: GLM-UCB for generalized linear bandits 
input: A ⊂ Rd, T, δ, µ (link function), λ. define: kµ = supx∈[0,1] 
dµ(x) dx , cµ = infx∈[0,1] 
dµ(x) dx > 0. 
for t = 1, . . . , T do Choose at = argmaxa∈A 
( µ(a>θ̂t) + 2β‖a‖Λ−1 
t 
) where 
β = 4kµ cµ 
(√ d log(cµT/(λδ)) + cµ 
√ λ 
) , Λt = λI + 
t−1∑ τ=1 
aτa > τ , 
and θ̂t is the unique solution of the following set of equations (define gt(x) , λcµx+ 
∑t−1 τ=1 µ(a>τ x)aτ ): 
gt(θ ′ t) = 
t−1∑ τ=1 
Rτaτ , θ̂t = argmin θ:‖θ‖2≤1 
∥∥gt(θ′t)− gt(θ)∥∥Λ−1 t . 
Receive Rt with E[Rt] = µ(a>t θt). end 
Generalized linear bandit is proposed by Filippi et al. (2010) and extended to the non-stationary case by Cheung et al. (2019); Zhao et al. (2020); Russac et al. (2020); Faury et al. (2021). We refer 
45
WEI LUO 
the readers to these papers for the introduction of the setting. Again, we consider the special case where the action set is fixed over time, and for simplicity, we assume that the action setA is a subset of {a ∈ Rd : ‖a‖2 ≤ 1} and the hidden parameter θt satisfies ‖θt‖2 ≤ 1. The generalized linear bandit problem is accompanied with an increasing link function µ : R→ R. It fits in our framework with Π = A and ft(a) = µ(a>θt). 
The standard GLM-UCB is presented in Algorithm 9. Below we show that GLM-UCB satisfies Assumption 1’ with the following definitions: 
∆(t) = k2 µd 
cµ 
√ log(T/δ)‖θt − θt+1‖2, f̃t = max 
a∈A 
( µ(a>θ̂t) + 2β‖a‖Λ−1 
t 
) , ρ(t) = β 
√ d log(T/δ) 
t , 
where cµ and kµ are the inifimum and supremum of the derivative of µ (defined in Algorithm 9). De-
fineGt , ∑t−1 
τ=1 
[∫ 1 v=0 ·µ 
( 〈aτ , (1− v)θ̂t + vθt〉dv 
)] aτa > τ +λcτI  cµΛt. Under the assumption 
that ∆(t) ≤ ρ(t), for all a ∈ A,∣∣∣µ(a>θt)− µ(a>θ̂t) ∣∣∣ ≤ ku ∣∣∣a>(θt − θ̂t) 
∣∣∣ ≤ kµ ∣∣∣a>G−1 t (gt(θt)− gt(θ̂t)) 
∣∣∣ ≤ kµ‖a‖G−1 
t 
∥∥∥gt(θt)− gt(θ̂t)∥∥∥ G−1 t 
≤ kµ cµ ‖a‖Λ−1 
t 
∥∥∥gt(θt)− gt(θ̂t)∥∥∥ Λ−1 t 
≤ kµ cµ ‖a‖Λ−1 
t 
∥∥gt(θt)− gt(θ′t)∥∥Λ−1 t 
= kµ cµ ‖a‖Λ−1 
t 
∥∥∥∥∥ t−1∑ τ=1 
( µ(a>τ θt)− µ(a>τ θτ ) 
) aτ + 
t−1∑ τ=1 
( µ(a>τ θτ )−Rτ ) 
) aτ + λcµθt 
∥∥∥∥∥ Λ−1 t 
≤ kµ cµ ‖a‖Λ−1 
t 
kµ max τ≤t ‖θt − θτ‖2 
t−1∑ τ=1 
‖aτ‖Λ−1 t 
+ 
∥∥∥∥∥ t−1∑ τ=1 
ητaτ 
∥∥∥∥∥ Λ−1 t 
+ √ λcµ 
 (define ητ = µ(a>τ θτ )−Rτ ) 
≤ kµ cµ ‖a‖Λ−1 
t 
( kµ 
cµ∆[1,t] 
k2 µd √ 
log(T/δ) 
√ dt+ 
√ d log(cµT/δ) + 
√ λcµ 
) 
≤ kµ cµ ‖a‖Λ−1 
t 
( cµρ(t) 
kµ 
√ t 
d log(T/δ) + √ d log(cµT/δ) + 
√ λcµ 
) (by the assumption ∆[1,t] ≤ ρ(t)) 
≤ 2β‖a‖Λ−1 t . (38) 
Thus, 
t∑ τ=1 
( f̃τ −Rτ 
) = 
t∑ τ=1 
( f̃τ − µ(a>τ θτ ) 
) + 
t∑ τ=1 
( µ(a>τ θτ )−Rτ 
) ≤ 
t∑ τ=1 
( µ(a>τ θ̂τ )− µ(a>τ θτ ) 
) + 2β 
t∑ τ=1 
‖aτ‖Λ−1 t 
+O (√ 
t log(T/δ) ) 
46
BLACK-BOX NON-STATIONARY RL 
≤ O 
( β 
t∑ τ=1 
‖aτ‖Λ−1 t 
) = O 
( β √ dt log(T/δ) 
) = O (tρ(t)) = O 
( tρ(t) + t∆[1,t] 
) . 
This verifies Eq. (32). Furthermore, by Eq. (38), 
f̃t = max a∈A 
( µ(a>θ̂t) + 2β‖a‖Λ−1 
t 
) ≥ max 
a∈A µ(a>θt) = f?t ≥ min 
τ∈[1,t] f?τ −∆[1,t]. 
This verifies Eq. (31). 
I.4. Q-UCB for Finite-horizon Tabular MDPs 
Algorithm 10: Q-UCB for finite-horizon tabular MDPs input: S (number of states), A (number of actions), H , T, δ. Qh(s, a)← H, Nh(s, a)← 0 for all h, s, a. for t = 1, . . . , T do 
for h = 1, . . . ,H do Choose ath ← argmaxaQh(sth, a). τ = Nh(sth, a 
t h)← Nh(sth, a 
t h) + 1, bτ ← c 
√ H3 log(SAT/δ)/τ . 
/ c is a universal constant Qh(sth, a 
t h)← (1− ατ )Qh(sth, a 
t h) + ατ 
[ rth(sth, a 
t h) + Vh+1(sth+1) + bτ 
] . / ατ , H+1 
H+τ 
Vh(sth)← min { H,maxaQh(sth, a) 
} . 
end end 
The finite-horizon tabular MDP problem fits in our framework with Π being the set of deterministic polices on the MDP, and ft(π) being the expected reward of policy π in episode t. Q-UCB (Hoeffding-style) is a model-free algorithm for finite-horizon tabular MDPs proposed by Jin et al. (2018), whose pseudocode is in Algorithm 10. Let H denote the horizon length, sth, a 
t h denote the 
state and actions visited at step h of episode t, and rth, pth denote the reward and transition functions at step h of episode t. Without loss of generality, we assume that st1 = s1 for all t (i.e., the initial state is fixed). 
It has been shown in the proof of (Mao et al., 2021, Theorem 1) that Q-UCB satisfy Assumption 1’ with the following choices: 
∆(t) = H H∑ h=1 
max s,a |rth(s, a)− rt+1 
h (s, a)|+H2 H∑ h=1 
max s,a ‖pth(·|s, a)− pt+1 
h (·|s, a)‖1, 
f̃t = V t h(s1), (V t 
h is the Vh in Algorithm 10 at the beginning of episode t) 
ρ(t) = Õ 
(√ H5SA 
t + H3SA 
t 
) . 
The proof details are omitted here. 
47
WEI LUO 
Algorithm 11: LSVI-UCB for finite-horizon linear MDP 
input: S (state space), A (action space), φ(·, ·) : S ×A → Rd, H, T, δ. for t = 1, . . . , T do 
for h = H, . . . , 1 do Λh ← 
∑t−1 τ=1 φ(sτh, a 
τ h)φ(sτh, a 
τ h)> + I . 
wh ← Λ−1 h 
∑t−1 τ=1 φ(sτh, a 
τ h) [ rτh(xτh, a 
τ h) + maxa∈AQh+1(xτh+1, a) 
] . 
Qh(·, ·)← min { w>h φ(·, ·) + 2β 
( φ(·, ·)Λ−1 
h φ(·, ·) )1/2 
, H } 
. 
/ β = cdH √ 
log(T/δ) for some universal constant c end for h = 1, . . . ,H do 
Take action ath ← argmaxa∈AQh(sth, a). end 
end 
I.5. LSVI-UCB for Finite-horizon Linear MDPs 
See (Zhou et al., 2020; Touati and Vincent, 2020) for the non-stationary finite-horizon linear MDP setting. We assume that the reward function and the transition function at step h of episode t are rth(s, a) = φ(s, a)>θth and pth(s′|s, a) = φ(s, a)>µth(s′) where φ(·, ·) is the feature function that maps a state-action pair to a d-dimensional feature vector. The problem fits in our framework with Π being the set of deterministic policies, and ft(π) being the expected reward of policy π in episode t. The LSVI-UCB algorithm is an optimism-based algorithm proposed by Jin et al. (2020b), whose pseudocode is shown in Algorithm 11. We define Qth, w 
t h,Λ 
t h to be the Qh, wh,Λh at Line 11 of 
round t. Furthermore, define V t h(s) = maxa∈AQ 
t h(s, a). Again, without loss of generality, we 
assume st1 = s1 (the initial state is fixed). We define 
∆(t) = dH √ 
log(T/δ) 
( H∑ h=1 
‖θth − θt+1 h ‖2 +H 
H∑ h=1 
‖µth − µt+1 h ‖F 
) , 
f̃t = V t 1 (s1), 
ρ(t) = c 
√ d3H4 
t log(T/δ) = βH 
√ d log(T/δ) 
t . (c and β defined in Algorithm 11) 
Below, we verify that LSVI-UCB satisfies Assumption 1’ with the ∆, f̃ , and ρ defined above. Assume that ∆[1,t] ≤ ρ(t). By similar arguments as in the proof of (Zhou et al., 2020, Lemma 3), we have∣∣∣φ(s, a)>wth −Q?h(s, a)− Pth(V t 
h − V ? h )(s, a) 
∣∣∣ ≤ (β + √ dtBθ,[1,t] +H 
√ dtBµ,[1,t] 
) ‖φ(s, a)‖ 
(Λth) −1 
(39) 
where Bθ,[1,t] = ∑t−1 
τ=1 
∑H h=1 ‖θτh − θ 
τ+1 h ‖2 and Bµ,[1,t] = 
∑t−1 τ=1 
∑H h=1 ‖µτh − µ 
τ+1 h ‖F . By the 
definition of ∆(t), the right-hand side of Eq. (39) can be further upper bound by( β + 
1 
H 
√ t 
d log(T/δ) ∆[1,t] 
) ‖φ(s, a)‖ 
(Λth) −1 ≤ 2β ‖φ(s, a)‖ 
(Λth) −1 , (40) 
48
BLACK-BOX NON-STATIONARY RL 
where the inequality is by the assumption that ∆[1,t] ≤ ρ(t). Similar to the proof of (Zhou et al., 2020, Lemma 4), we can then show that for any t, h, 
Qth(s, a)−Q?h(s, a) = φ(s, a)>wth −Q?h(s, a) + 2β‖φ(s, a)‖ (Λth) 
−1 
≥ max s′ 
( V t h+1(s′)− V ? 
h+1(s′) ) 
(by Eq. (39) and Eq. (40)) 
and further using induction to show that V t 1 (s) ≥ V ? 
1 (s). Thus, f̃t = V t 1 (s1) ≥ V ? 
1 (s1), which 
verifies Eq. (31). One can also show that ∑t 
τ=1 
( f̃τ −Rτ 
) = O(tρ(t)) using the standard analysis 
of LSVI-UCB (e.g., (Jin et al., 2020b, Theorem 3.1), (Zhou et al., 2020, Theorem 5)). This verifies Eq. (32). 
I.6. ILOVETOCONBANDITS for Contextual Bandits 
Algorithm 12: ILOVETOCONBANDITS for contextual bandits input: Π (policy set), A (action set), T , δ. for t = 1, . . . , T do 
Calculate Qt ∈ ∆Π that satisfies the following constraints with some universal constant c′ > 0: ∑ 
π 
Q(π)R̂eg[1,t−1](π) ≤ 2c′Aµt 
∀π ∈ Π, 1 
t− 1 
t−1∑ τ=1 
1 
Qµt(π(xτ )|xτ ) ≤ 2A+ 
R̂eg[1,t−1](π) 
c′µt 
where µt , √ 
log(|Π|T/δ) At , Qµ(a|x) , (1−Aµ) 
∑ π∈ΠQ(π)1[π(x) = a] + µ, and 
R̂egI(π) , 1 
|I| max π′ 
∑ τ∈I 
( r̂τ (π′(xτ ))− r̂τ (π(xτ )) 
) , r̂τ (a) , 
Rτ1[aτ = a] 
pτ (a) . 
Let pt(·) = Qµt(·|xt) and sample at ∼ pt. end 
In the contextual bandit problem, in each round, the learner first sees a context xt ∈ X , and then chooses an action at ∈ [A] based on it. The learner then receives the reward rt(at) ∈ R. We assume that (xt, rt) is sampled from the distributionDt. The goal of the learner is to be comparable to the best mapping π : X → [A] within a given set of mappings Π (which are called policies), i.e., the learner wants to minimize 
∑ t(rt(π 
∗ t (xt)) − rt(at) where π∗t , maxπ′∈Π E(x,r)∼Dt [r(π 
′(x))]. See (Agarwal et al., 2014) for more detailed description of the problem. This problem fits in our framework with the same Π and ft(π) = E(x,r)∼Dt [r(π(x))]. 
The algorithm ILOVETOCONBANDITS (Algorithm 12) by Agarwal et al. (2014) achieves the optimal regret bound in the i.i.d. case. The analysis for ILOVETOCONBANDITS is more involved. Fortunately, Chen et al. (2019) already has helpful lemmas for ILOVETOCONBANDITS in the non-stationary case, and we can simply reuse them. We show a more general result that Assumption 1 is satisfied no matter how large ∆[1,t] is. 
49
WEI LUO 
Let RI(π) = 1 |I| ∑ 
τ∈I E(x,r)∼Dτ [r(π(x))] be the expected of policy π in the interval I, 
R̂I(π) = 1 |I| ∑ 
τ∈I r̂τ (π(xτ )) be an unbiased estimator of RI(π), with r̂τ an unbiased estimator for the action reward constructed with inverse propensity weighting at time τ . Let RegI(π) = 
maxπ′ RI(π′)−RI(π) and R̂egI(π) = maxπ′ R̂I(π′)−R̂I(π). Below, we will show that ILOVE-TOCONBANDITS satisfies Assumption 1’ with the following definitions: 
∆(t) , ‖Dt −Dt+1‖TV = 
∫ r 
∫ x |Dt(x, r)−Dt+1(x, r)|dxdr, 
f̃t , max π R̂[1,t−1](π) + c2Aµt−1 (for some universal constant c2 > 0) 
ρ(t) , 
√ A log(|Π|T/δ) 
t . 
Note that ∆(t) upper bounds |E(x,r)∼Dt [r(π(x))]− E(x,r)∼Dt+1 [r(π(x))]|. 
Combining the proofs of Lemma 14 and Lemma 16 in (Chen et al., 2019), we get the following guarantee with probability at least 1− δ for any policy π:∣∣∣R̂[1,t](π)−R[1,t](π) 
∣∣∣ ≤ c1R̂eg[1,t](π) + c2Aµt + c3∆[1,t], (41) 
where µt = 
√ log(|Π|T/δ) 
At and c1, c2, c3 are universal constants. To see how to get 
Eq. (41), notice that Lemma 14 of (Chen et al., 2019) gives ∣∣∣R̂[1,t](π)−R[1,t](π) 
∣∣∣ ≤ O ( µt t 
∑t τ=1 Uτ + log(|Π|T/δ) 
tµt 
) , and they further upper bound Uτ by O 
( Reg[1,t] µt 
+A+ ∆[1,t] 
µt 
) in 
the second-to-last line in their proof of Lemma 16. Combining them yields Eq. (41). Notice that they have an additional log T factor which we do not suffer. 
Below, let πt = argmaxπR[1,t](π). Then we have 
max π R̂[1,t](π) ≥ R̂[1,t](πt) ≥ R[1,t](πt)− c3∆[1,t] − c2Aµt 
= max π R[1,t](π)− c3∆[1,t] − c2Aµt, (42) 
where in the second inequality we use Eq. (41) with the fact that Reg[1,t](πt) = 0. Therefore, if we 
choose f̃t = maxπ R̂[1,t−1](π) + c2Aµt−1, then 
f̃t ≥ max π R[1,t−1](π)− c3∆[1,t−1] (using Eq. (42) and the definition of f̃t) 
≥ max π 
max τ∈[1,t] 
Rτ (π)− (c3 + 1)∆[1,t] (43) 
which proves Eq. (31). Next, we show Eq. (32): 
f̃t − Et[Rt] ≤ ∑ π 
Qt(π) ( f̃t −Rt(π) 
) +O(Aµt) 
(by the algorithm, which uses O(Aµt) probability to explore actions) 
= ∑ π 
Qt(π) 
( max π′ R̂[1,t−1](π 
′)−Rt(π) 
) +O(Aµt) 
50
BLACK-BOX NON-STATIONARY RL 
≤ ∑ π 
Qt(π) 
( max π′ R̂[1,t−1](π 
′)−R[1,t−1](π) 
) +O 
( Aµt + ∆[1,t] 
) = ∑ π 
Qt(π) ( 
R̂eg[1,t−1](π) + R̂[1,t−1](π)−R[1,t−1](π) ) 
+O ( Aµt + ∆[1,t] 
) ≤ ∑ π 
Qt(π) ( 
R̂eg[1,t−1](π) + c1Reg[1,t−1](π) ) 
+O ( Aµt + ∆[1,t] 
) (by Eq. (41)) 
≤ (1 + 2c1) ∑ π 
Qt(π)R̂eg[1,t−1](π) +O ( Aµt + ∆[1,t] 
) (44) 
where the last inequality is by Lemma 16 of (Chen et al., 2019), which bounds Reg[1,t−1](π) by 
2R̂eg[1,t−1](π) +O ( Aµt + ∆[1,t] 
) . By the algorithm, 
∑ π Qt(π)R̂eg[1,t−1](π) is of orderO (Aµt). 
Therefore, the last expression can further be upper bounded by O ( Aµt + ∆[1,t] 
) . Finally, with the 
above calculation and Azuma’s inequality, we get 
t∑ τ=1 
( f̃τ −Rτ 
) ≤ 
t∑ τ=1 
( f̃τ − Eτ [Rτ ] 
) + 
t∑ τ=1 
(Eτ [Rτ ]−Rτ ) ≤ O (√ 
At log(|Π|T/δ) + ∆[1,t] 
) Since we choose ρ(t) = 
√ A log(|Π|T/δ) 
t , Eq. (32) is also satisfied. 
I.7. FALCON for Contextual Bandits 
Algorithm 13: FALCON for realizable contextual bandits input: Φ (reward function class), A (action sets), T, δ. for t = 1, . . . , T do 
Let γt = √ At/ log(|Φ|T/δ). 
Compute φ̂t = argminφ∈Φ 
∑t−1 τ=1(φ(xτ , aτ )− rt(at))2 
Observe context xt. Let ât = argmaxa∈A φ̂(xt, a). Define 
pt(a) , 
 1 
A+γt(φ̂t(xt,ât)−φ̂t(xt,a)) , for a 6= ât, 
1− ∑ 
a′ 6=ât pt(a ′), for a = ât. 
Sample at ∼ pt and observe reward Rt. end 
FALCON is an algorithm for stationary contextual bandits. It relies on the assumption that the expected reward of action a under context x is given by an unknown function φ?(x, a) : X ×A → [0, 1]. The learner is given the function class Φ that contains φ?. For each φ ∈ Φ, one can derive a policy πφ : X → A such that πφ(x) = argmaxa∈A φ(x, a). It is straightforward to see that the optimal policy is πφ? , and the learner’s goal is to be competitive with it. This problem falls into our framework with Π = {πφ : φ ∈ Φ} and ft(π) = Ex∈Dt [φ∗(x, π(x))] where Dt is the distribution of context at time t. The algorithm FALCON is shown in Algorithm 13. 
Below, we show that it also satisfies Assumption 1’. 
51
WEI LUO 
At time t, the context xt is sampled from Dt, and the reward is generated by E[rt(xt, at)] = φ?t (xt, at). We slightly modify their algorithm so that at every round t, the algorithm call the regression oracle once and obtain φ̂t = argminφ∈Φ 
∑t−1 τ=1(φ(xτ , aτ ) − Rτ )2 (the original algorithm 
does this only when the time index doubles), and then construct a mapping from context to action distribution pt(·|·) as specified in their algorithm. Analogous to their definitions, we define 
R[1,t−1](π) = 1 
t− 1 
t−1∑ τ=1 
Ex∼Dτ [φ?τ (x, π(x))] , 
R̂[1,t−1](π) = 1 
t− 1 
t−1∑ τ=1 
Ex∼Dτ [ φ̂t(x, π(x)) 
] , 
R̂eg[1,t−1](π) = R̂[1,t−1](πφ̂t)− R̂[1,t−1](π), 
Reg[1,t−1](π) = max φ∈Φ R[1,t−1](πφ)−R[1,t−1](π), 
Vt(p, π) = Ex∼Dt [ 
1 
p(π(x)|x) 
] , 
Vt(π) = max τ∈[1,t] 
Vτ (pτ , π). 
We will show that FALCON satisfies Assumption 1’ with the following definitions: 
∆(t) = √ Amax 
x,a |φ?t (x, a)− φ?t+1(x, a)|+ 
∫ x |Dt(x)−Dt+1(x)|dx, 
ρ(t) = 
√ A log(|Φ|T/δ) 
t 
By the same calculation as in Lemma 7 of (Simchi-Levi and Xu, 2020), for any π, 
(t− 1) ∣∣∣R̂[1,t−1](π)−R[1,t−1](π) 
∣∣∣2 = 
1 
t− 1 
( t−1∑ τ=1 
Ex∼Dτ [ φ̂t(x, π(x))− φ?τ (x, π(x)) 
])2 
≤ t−1∑ τ=1 
( Ex∼Dτ 
[ φ̂t(x, π(x))− φ?τ (x, π(x)) 
])2 
≤ t−1∑ τ=1 
( Ex∼Dτ 
[√ 1 
pτ (π(x)|x) pτ (π(x)|x) 
( φ̂t(x, π(x))− φ?τ (x, π(x)) 
)2 ])2 
≤ t−1∑ τ=1 
( Ex∼Dτ 
[√ 1 
pτ (π(x)|x) Ea∼pτ (·|x) 
( φ̂t(x, a)− φ?τ (x, a) 
)2 ])2 
≤ t−1∑ τ=1 
Ex∼Dτ [ 
1 
pτ (π(x)|x) 
] Ex∼DτEa∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] 
≤ t−1∑ τ=1 
Vτ (pτ , π)Ea∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] 
52
BLACK-BOX NON-STATIONARY RL 
≤ Vt−1(π) t−1∑ τ=1 
Ea∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] . 
Using Lemma 30 and Lemma 31 below, when ∆̂[1,t] ≤ O (ρ(t)), we have 
t−1∑ τ=1 
Ex∼Dτ ,a∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] ≤ O (log(T |Φ|/δ)) 
and Vt−1(π) ≤ O(A) + maxτ∈[1,t−2] γτ R̂eg[1,τ ](π), where γt = Θ (√ 
At log(|Φ|T/δ) 
) . Note that 
they are actually of the same order as in the Lemma 7 of (Simchi-Levi and Xu, 2020) since the additional terms contributed by ∆[1,t] are dominated by other terms. Thus, the bound we get for∣∣∣R[1,t−1] − R̂[1,t−1] 
∣∣∣ is of the same order as their Lemma 7, which is 
∣∣∣R[1,t−1](π)− R̂[1,t−1](π) ∣∣∣ ≤ O(√ log(T |Φ|/δ) 
t 
( A+ max 
τ∈[1,t−2] γτ R̂eg[1,τ ](π) 
)) (45) 
≤ 1 
16 max 
τ∈[1,t−2] R̂eg[1,τ ](π) +O (ρ(t)) . (by AM-GM) 
(46) 
Then one can follow the derivation in their Lemma 8 using Eq. (46), and get 
Reg[1,t](π)− R̂eg[1,t](π) ≤ 1 
8 max 
τ∈[1,t−1] R̂eg[1,τ ](π) +O(ρ(t)), 
R̂eg[1,t](π)− Reg[1,t](π) ≤ 1 
8 max 
τ∈[1,t−1] R̂eg[1,τ ](π) +O(ρ(t)). 
Using these two inequalities, together with ∣∣∣Reg[1,τ ](π)− Reg[1,t](π) 
∣∣∣ ≤ O(∆[1,t]) = O (ρ(t)), we can also prove 
Reg[1,t](π) ≤ 2R̂eg[1,t](π) +O(ρ(t)), R̂eg[1,t](π) ≤ 2Reg[1,t](π) +O(ρ(t)) (47) 
by induction as their Lemma 8. One can see that all bounds we obtain are of the same order as in the stationary case shown in (Simchi-Levi and Xu, 2020), thanks to the condition ∆[1,t] = O(ρ(t)). 
Then following their Lemmas 9 and 10, we obtain regret bound maxφ tR[1,t](πφ)− ∑t 
τ=1Rτ = 
O (√ 
At log(T |Φ|/δ) ) 
. 
Similar to the calculation in Eq. (43), by picking f̃t = R̂[1,t−1](πφ̂t) + c 
√ A log(T |Φ|/δ) 
t with large enough c, we have 
f̃t ≥ max φ R[1,t−1](πφ) + c 
√ A log(T |Φ|/δ) 
t −O(ρ(t)) (by Eq. (46)) 
≥ R[1,t−1](πφ?1) ≥ R1(πφ?1)−O(∆[1,t]) ≥ min τ∈[1,t] 
max φ Rτ (πφ)−O(∆[1,t]), 
which verifies Eq. (31). To upper bound ∑t 
τ=1 
( f̃τ −Rτ 
) , we follow a similar calculation as 
Eq. (44), and use the condition ∆[1,t] = O(ρ(t)). This verifies Eq. (32). 
53
WEI LUO 
Lemma 30 If ∆[1,t] ≤ O (ρ(t)), then 
t−1∑ τ=1 
Ex∼Dτ ,a∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] 
= O (log(T |Φ|/δ)) . 
Proof First, we consider a speicific φ. Define Yτ = (φ(xτ , aτ )−Rτ )2−(φ?τ (xτ , aτ )−Rτ )2. Then we have E[Yτ ] = E 
[ (φ(xτ , aτ )− φ?τ (xτ , aτ ))2 
] and E 
[ Y 2 τ 
] ≤ 4E 
[ (φ(xτ , aτ )− φ?τ (xτ , aτ ))2 
] = 
4E[Yτ ]. By Freedman’s inequality, 
t−1∑ τ=1 
Yτ ≥ t−1∑ τ=1 
E[Yτ ]− c1 
√√√√ t−1∑ τ=1 
E [Y 2 τ ] log(T/δ)− c2 log(T |Φ|/δ) 
≥ t−1∑ τ=1 
E[Yτ ]− 2c1 
√√√√ t−1∑ τ=1 
E [Yτ ] log(T/δ)− c2 log(T |Φ|/δ). 
The above implies (by solving for ∑t−1 
τ=1 E[Yτ ]) 
t−1∑ τ=1 
E[Yτ ] ≤ 2 t−1∑ τ=1 
Yτ + 4(c2 1 + c2) log(T |Φ|/δ). (48) 
For the other direction, we also have 
t−1∑ τ=1 
Yτ ≤ 2 t−1∑ τ=1 
E[Yτ ] + 
( c2 
1 
4 + c2 
) log(T |Φ|/δ). (49) 
Then we can bound 
t−1∑ τ=1 
Ex∼Dτ ,a∼pτ (·|x) 
[( φ̂t(x, a)− φ?τ (x, a) 
)2 ] 
(using Eq. (48)) 
≤ 2 t−1∑ τ=1 
( φ̂t(xτ , aτ )−Rτ 
)2 − 2 
t−1∑ τ=1 
(φ?τ (xτ , aτ )−Rτ )2 + 4(c2 1 + c2) log(T |Φ|/δ) 
≤ 2 
t−1∑ τ=1 
(φ?1(xτ , aτ )−Rτ )2 − 2 
t−1∑ τ=1 
(φ?τ (xτ , aτ )−Rτ )2 + 4(c2 1 + c2) log(T |Φ|/δ) 
(by the optimality of φ̂t) 
≤ 4 t−1∑ τ=1 
E [ (φ?1(xτ , aτ )− φ?τ (xτ , aτ ))2 
] + c3 log(T |Φ|/δ) (using Eq. (49)) 
≤ 4(t− 1) 
A ∆2 
[1,t] + c3 log(T |Φ|/δ). (by the definition of ∆[·,·]) 
By the condition on ∆[1,t], we have 4(t−1) A ∆2 
[1,t] = O (log(T |Φ|/δ)), which proves the lemma. 
54
BLACK-BOX NON-STATIONARY RL 
Lemma 31 If ∆[1,t] ≤ O (ρ(t)), then 
Vt(π) ≤ O(A) + max τ∈[1,t−1] 
γτ R̂eg[1,τ ](π) 
where γt = Θ (√ 
At log(|Φ|T/δ) 
) . 
Proof Similar to Lemma 6 of FALCON, for τ ∈ [1, t], 
Vτ (pτ , π) ≤ A+ γτ−1Ex∼Dτ [ φ̂τ (x, π 
φ̂τ (x))− φ̂τ (x, π(x)) 
] ≤ A+ 
γτ−1 
τ − 1 
τ−1∑ s=1 
Ex∼Ds [ φ̂τ (x, π 
φ̂τ (x))− φ̂τ (x, π(x)) 
] + γτ−1∆[1,t] 
≤ A+ γτ−1R̂eg[1,τ−1](π) + γτ−1∆[1,t]. 
By the condition ∆̂[1,t] ≤ O (ρ(t)), that last term γτ−1∆[1,t] is of order O (A). By the definition of Vt(π), this finishes the proof. 
55