> Source: https://www.ambujtewari.com/research/kausik24offline.pdf

Offline Policy Evaluation and Optimization under Confounding 
Chinmaya Kausik∗,1 Yangyi Lu∗,2 Kevin Tan∗,3 
Maggie Makar1 Yixin Wang1 Ambuj Tewari1 1University of Michigan 2Pinterest 3University of Pennsylvania 
Abstract 
Evaluating and optimizing policies in the presence of unobserved confounders is a problem of growing interest in offline reinforcement learning. Using conventional methods for offline RL in the presence of confounding can not only lead to poor decisions and poor policies, but also have disastrous effects in critical applications such as healthcare and education. We map out the landscape of offline policy evaluation for confounded MDPs, distinguishing assumptions on confounding based on whether they are memoryless and on their effect on the data-collection policies. We characterize settings where consistent value estimates are provably not achievable, and provide algorithms with guarantees to instead estimate lower bounds on the value. When consistent estimates are achievable, we provide algorithms for value estimation with sample complexity guarantees. We also present new algorithms for offline policy improvement and prove local convergence guarantees. Fi-nally, we experimentally evaluate our algorithms on both a gridworld environment and a simulated healthcare setting of managing sepsis patients. In gridworld, our model-based method provides tighter lower bounds than existing methods, while in the sepsis simulator, we demonstrate the effectiveness of our method and investigate the importance of a clustering sub-routine. 
1 Introduction 
A central problem in sequential decision making is learning from offline data, since collecting data in an online fashion is often prohibitively expensive or unsafe (Levine et al., 2020). Since real-life data is often 
Proceedings of the 27th International Conference on Artifi-cial Intelligence and Statistics (AISTATS) 2024, Valencia, Spain. PMLR: Volume 238. Copyright 2024 by the author(s). 
affected by latent variables, there has been a rise of interest in formulations of reinforcement learning problems with hidden information (Nair and Jiang, 2021; Miao et al., 2022; Wang et al., 2020). The most general kind of latent information is considered by partially observable MDPs or POMDPs (Kaelbling et al., 1998; Tennenholtz et al., 2019), where the latent information can affect both rewards and transitions. However, the reward is often designed by the user based only on observable variables. In medical examples, the reward could be given based on observed vitals, but unrecorded genetic conditions and socio-economic status can affect actions taken and future states. These examples motivate the important case of reinforcement learning with unobserved confounders, defined as latent information that affects transitions, but not rewards1 (Kallus and Zhou, 2020; Bruns-Smith, 2021; Bruns-Smith and Zhou, 2023). 
The hardness of learning from offline data under confounding comes from the fact that partially observed transitions can be further obscured by behavior policies that might have known the unrecorded confounder (Kallus and Zhou, 2020). Two offline data distributions might thus be identical despite coming from different confounded MDPs, if the behavior policies accommodated for this difference (see Theorem 1). 
To provide guarantees for learning from offline data, the most common assumption in previous work is that confounders are "memoryless" (Assumption 1). This assumption essentially means that they are sampled afresh at each step independently of past confounders, states, or actions (Bruns-Smith and Zhou, 2023). In many real-life applications like healthcare and epidemiology (Daniel et al., 2013; Clare et al., 2018; Mansournia et al., 2017; Platt et al., 2009), it is more appropriate to assume that the confounders are sampled "with memory" of previous confounders, and even states and actions. A lot of work also assumes that behavior policies 
1Some papers define confounders using a kind of "memorylessness," and allow them to affect rewards (Zhang and Bareinboim, 2016; Wang et al., 2020). We only consider unconfounded rewards.
Offline Policy Evaluation and Optimization under Confounding 
With Sensitivity Constraint Without Sensitivity Constraint 
Memoryless Con-founders 
Consistency not possible (Theo-rem 1, Ω(εH) error lower bound), O(εH2) error upper bound with 3 methods (Theorems 2, 3, 4) 
Ω(H) error lower bound (Theo-rem 1) 
Confounders with Memory 
Methods mentioned above have Ω(H) error lower bounds, even with unconfounded πb and πe 
(Theorem 6) 
Ω(H) lower bound in general. For global confounders, consistency possible, sample complexity guarantees given (Theo-rem 7) 
Table 1: Hardness of the OPE problem under different assumptions on the nature of confounding present. Γ is a so-called sensitivity parameter, with Γ = 1 +O(ε). Higher ε corresponds to more confounded πb. 
follow a sensitivity constraint (Assumption 3) (Kallus and Zhou, 2020; Bruns-Smith, 2021). Motivated by these observations, we take the first step towards providing a structured view of the landscape of offline RL for confounded MDPs, distinguishing settings in terms of sensitivity assumptions and whether confounders have memory. We also introduce and study an important sub-case of confounders with memory, called global confounders (Assumption 2). Specifically, we ask the following questions for each setting: 
Q.1. If consistent offline policy estimation (OPE) is not possible, can we prove lower bounds on the error? What guarantees can we give for algorithms that instead estimate bounds on the value? 
Q.2. If consistent OPE is possible, then what algorithms achieve this? What is their sample complexity? 
Q.3. How can we use these insights for offline policy improvement? 
Paper Structure and Contributions. We detail our contributions below. A summary of key results is provided in Table 1. 
OPE for Memoryless Confounders, Section 3: In The-orem 1, we give the first lower bound for OPE error that depends on a sensitivity parameter Γ and horizon length H. By choosing Γ appropriately, we show that value estimation can be arbitrarily bad without a sensitivity constraint. The theorem also shows that the lower bound on error grows with H and consistent estimates are not possible, even under a sensitivity constraint. We are the first to quantitatively study the errors of FQE and CFQE. To provide algorithms that estimate lower bounds on the value, we modify the CFQE algorithm due to Bruns-Smith (2021) to our more general definition of memoryless confounding. We are the first to compute quantitative upper bounds on its error and the error for FQE, in Theorems 2 and 3. We further provide a new model-based algorithm that improves over CFQE for stationary transition structures, and provide guarantees for it in Theorems 4 and 5. 
OPE for Confounders with Memory, Section 4: While FQE is a standard workhorse for OPE and also enjoys guarantees for memoryless confounders, it is unclear if (and how badly) FQE fails for confounders with memory. In particular, it is non-trivial to produce lower bound examples in this case. We are the first to present one in Theorem 6, where we show that FQE can have arbitrarily large error for confounders with memory, even for unconfounded πb and πe with bounded concentrability. This shows the hardness of OPE for general confounders with memory. In this light, we introduce and study the important sub-case of global confounders, where the confounder is fixed at the beginning of each trajectory. We leverage the work of Kausik et al. (2022) on clustering mixtures of MDPs to provide an algorithm for OPE under this assumption, along with sample complexity guarantees in Theorem 7. While past work on confounded RL has focused only on consistency, we are the first to address the sample complexity of OPE under confounding. 
Offline Policy Improvement, Section 5: We address offline policy improvement in Section 5, presenting policy gradient methods for memoryless confounders under a sensitivity assumption, as well as for global confounders. We prove local convergence for both. 
Experiments, Section 6: We test and compare OPE methods for memoryless confounders in the gridworld environment provided by Bruns-Smith (2021). Our experiments show that our model-based method gives tighter lower bounds than existing methods. We also successfully run our policy gradient method for memoryless confounders in the same environment. OPE and policy gradient methods for global confounders are tested in the sepsis simulator from Oberst and Sontag (2019), where we significantly outperform confounderoblivious implementations of both FQE and policy gradients. 
Related Work. Many specific assumptions on confounders have been studied in recent literature. Kallus
Kausik, Lu, Tan, Makar, Wang, Tewari 
and Zhou (2020); Bruns-Smith (2021); Namkoong et al. (2020) all provide algorithms that estimate bounds on the value under a sensitivity assumption. The first two assume variants of memorylessness, while the third assumes that the confounding occurs during only a single timestep. Other work like Bennett et al. (2020) uses a latent variable model for states and actions to get consistent point estimates. This is similar to work in the POMDP setting (Tennenholtz et al., 2019), and neither approach directly applies to our settings. In general, a treatment of confounders with memory and a bigpicture view of the OPE problem under confounding is still missing. 
On the other hand, literature on offline policy improvement in the presence of confounders has grown more gradually. Bruns-Smith and Zhou (2023) provide robust fitted-Q-iteration methods under a sensitivity model and a memoryless assumption. This does not apply to confounders with memory, like global confounders. Other work like Wang et al. (2020); Liao et al. (2021); Fu et al. (2022) uses auxiliary variables from the data to adjust for confounding bias. However, these do not directly apply to our settings. 
2 Setup and Assumptions 
2.1 Background 
We define an episodic confounded MDP by a tuple (S × U ,A, H, {Ph}Hh=1, r, d0), described as follows. S is the set of S observed states and U the set of U unobserved confounders; A is the set of A actions; H is the horizon of each episode; d0 is the distribution for initial states (s1, u1) ∼ d0; r : S × A → [0, 1] denotes the reward function; and Ph(s 
′, u′ | s, u, a) denotes the state transition probability at timestep h. 
The data is collected under a behavior policy πb specified by πb,h(a | s, u), which might have used the unrecorded confounders and been time-dependent. The observed behavior policy is obtained by marginalizing u over the induced distribution at timestep h, and is called πb,h(a | s). The goal is to estimate the value function V πe 
1 of a possibly time-dependent evaluation policy πe that does not use confounders Bruns-Smith (2021). This is motivated by the fact that confounders can be harder to observe and account for during deployment. 
2.2 Assumptions on Sensitivity and Memory 
We consider two kinds of assumptions on unobserved confounders. The first is whether they "have memory." We define memoryless confounders below to be sampled afresh at each step Bruns-Smith and Zhou (2023). A memoryless confounder in a healthcare application could be an accident encountered mid-treatment, or in an economics application could be a supply shock 
affecting the price of oil, as Bruns-Smith (2021) highlights. 
Assumption 1 (Memoryless Confounders). At each timestep h, we draw a fresh confounder uh ∼ Ph(u | s = sh), possibly dependent on the current state sh, but independent of past confounders, states and actions. 
On the other hand, confounders with memory could depend on all past (s, a, u) tuples. We introduce an important sub-case of this, which we call the global confounder assumption. This is an extreme case of confounders with memory, where the confounder is not just dependent on, but the same as all past confounders in the trajectory. In the example of healthcare applications, this could be an unrecorded patient demographic characteristic or genetic condition that does not change over the course of treatment. 
Assumption 2 (Global Confounders). A global confounder is generated by u ∼ P (u) at the beginning of an episode, and remains unchanged throughout the episode. 
A commonly-used assumption for the effect of confounder on πb is a sensitivity model found in Bruns-Smith (2021); Kallus and Zhou (2020); Namkoong et al. (2020). Note that Γ = 1 below corresponds to the case where πb is confounder-oblivious, that is, independent of the confounder. 
Assumption 3 (Confounding Sensitivity Model). Given Γ ≥ 1, for all s ∈ S, u ∈ U , h ∈ {1, 2, · · ·H} and a ∈ A: 
1 
Γ ≤ ( 
πb,h(a | s, u) 1− πb,h(a | s, u) 
) / 
( πb,h(a | s) 
1− πb,h(a | s) 
) ≤ Γ, 
where πb,h(a | s) = ∑ 
u Ph(u | s)πb,h(a | s, u) is the marginalized (observed) behavior policy. The above inequality implies the bounds αh(s, a) ≤ πb,h(a|s) 
πb,h(a|s,u) ≤ βh(s, a), where αh(s, a) := πb,h(a | s)+ 1 
Γ (1−πb,h(a | s)) and βh(s, a) := Γ + πb,h(a | s)(1− Γ). 
3 OPE under Memoryless Confounders 
We discuss OPE when confounders are memoryless. We first open with a result showing that in the absence of a sensitivity assumption like Assumption 3, we can incur an estimation error as bad as Ω(H). Note that the value functions lie in the range [0, H], so the worst possible OPE error is H. 
Theorem 1 (Lower Bound for Memoryless Con-founders). There exists a parameter ε that determines a pair of confounded MDPsM1 andM2 with i.i.d. (and thus memoryless) confounders along with stationary policies πb1 , πb2 and πe, so that data collected fromMi
Offline Policy Evaluation and Optimization under Confounding 
using πbi has the same distribution for i = 1, 2, but the values under πe differ by |V πe 
1 (M1)−V πe 1 (M2)| = 2εH. 
In particular, when ε = 1 2 − 
1 H2 , the values under πe 
differ by Ω(H). 
It can be seen from the proof of the theorem in Ap-pendix B that when ε = 1 
2 − 1 
H2 , Γ = Ω(H2). It is then clear that a bound on the sensitivity is necessary. The proof shows that for small ε in our example, Γ = 1+O(ε). In this light, even with a sensitivity constraint of 1+O(ε), we cannot get a consistent estimate of the value of a policy. This is because by Theorem 1, even two observationally indistinguishable confounded MDPs can differ in value under a new πe by Ω(εH). 
Thus, even with infinite data, we can only hope for bounds on the value, and the minimum-possible error deteriorates with horizon H. We now analyze and present algorithms for obtaining such bounds. 
3.1 FQE and Confounded FQE 
Fitted Q-Evaluation (FQE), which we recall in Ap-pendix C, is a standard workhorse for OPE. We first present a new result on the estimation error of FQE under memoryless confounding, proved in Appendix D. 
Theorem 2 (FQE Error). Suppose Γ = 1 + ε in As-sumption 3. Then in the limit of infinite samples, the point estimate f̂1(s, a) of the Q-function produced by FQE has a worst-case error of |V πe 
1 (s) − ∑ 
a πe,1(a | s)f̂1(s, a)| = O(εH2) for small ε. 
Note that FQE gives a point estimate instead of a lower bound on the value function. For many safety-critical applications, it is important to have conservative lower bounds for policy estimation. Using the proof of Theo-rem 2, we can produce a straightforward lower bound of ∑ 
a πe,1(a | s)f̂1(s, a)− kεH2 on the value function, for some k depending on ε. However, this is a worstcase, data-oblivious lower bound. We note that we can get a sharper lower bound using confounded FQE (CFQE), introduced by Bruns-Smith (2021) for i.i.d. confounders. Confounded FQE gives a lower bound on the value by sequentially searching for the worst possible policies that are consistent with the data and the sensitivity assumption. We adapt it to general memoryless confounders and describe it in Appendix C. We also provide a new theoretical guarantee for the worst-case error of CFQE below, proved in Appendix D. 
Theorem 3 (CFQE Error). Suppose Γ = 1 + ε in Assumption 3. Then the worst-case error for the lower bound f̂1(s, a) generated by CFQE in the infinite-sample case is |V πe 
1 (s)− ∑ 
a πe,1(a | s)f̂1(s, a)| = O(εH2) for any range of ε. 
Although it has the same worst-case error as FQE, we note that CFQE provides an instance-dependent lower 
bound that is sharper than the naive one mentioned above. We confirm in experiments that the naive FQE lower bound and the CFQE lower bound are in fact at different orders of magnitude. 
3.2 Model-Based Method For Stationary Transition Kernels 
While CFQE searches for the worst-possible policies, we discuss a method here that searches for the worst possible transition dynamics that are consistent with the data. Note that since πe is confounder-oblivious, the induced transitions Pπe 
h (s′ | s) are determined by the marginalized transition dynamics defined as Ph(s 
′ | s, a) := ∑ 
u Ph(u | s)Ph(s ′ | s, a, u). 
This is clear from the following computation: Pπe 
h (s′ | s) = ∑ 
u,a πe,h(a | s)Ph(u | s)Ph(s ′ | s, a, u) =∑ 
a πe,h(a | s) ( ∑ 
u Ph(u | s)Ph(s ′ | s, a, u)) =∑ 
a πe,h(a | s)Ph(s ′ | s, a). 
We note that CFQE optimizes separately over the data at each timestep h. In particular, if the marginalized transition kernel were stationary, then the method would not leverage its stationarity. Our model-based method can leverage this, and we therefore assume the stationarity of transition dynamics and of P (u | s) in this section. For ease of exposition, we also assume that πb and πe are stationary. The method can be modified to work for potentially time-dependent πb 
and πe, which we do in Appendix E. 
We now describe the method. Let the empirically observed transitions be P̂πb(s′ | s, a), and denote its value in the limit of infinite data by Pπb(s′ | s, a). We know that the latter is stationary under our expository simplification. Let α̂(s, a) and β̂(s, a) be obtained using the estimate π̂b(s, a) Denote by G the set of marginalized transitions P(s′|s, a) that fall between α̂(s, a)(P̂πb(s′|s, a)) and ˆβ(s, a)(P̂πb(s′|s, a)) for each s′, a, s. Our model-based method amounts to solving the following optimization problem: 
min V1(s0),V2,...,VH ,VH+1=0,P 
V1(s0) (1) 
s.t. P ∈ G, ∑ s′ 
P(s′ | s, a) = 1 ∀s, a. 
Vh(s) = πe(· | s)T (Rs + PsVh+1(·)) ∀h ∈ {1, ...,H}, s 
where VH+1 = 0 and Ps ∈ RA×S is the matrix whose rows are P(· | s, a) for each a, Rs ∈ RA and Vh+1(·) ∈ RS . This corresponds to minimizing the value function V1(s0) over the set G of state transition probabilities, using H · S Bellman backup constraints to encode the Bellman equation. 
While this method is similar to the model-based method in Bruns-Smith (2021) inspired by robust MDP literature, it is important to note that unlike Bruns-Smith
Kausik, Lu, Tan, Makar, Wang, Tewari 
(2021), we look at uncertainty sets for each s, a (instead of just one for each s) and make no additional assumption on model-sensitivity. In particular, model sensitivity and the uncertainty sets for the true marginalized transition kernel are completely determined by Γ. This method possesses several theoretical guarantees, proved in Appendix E. 
Theorem 4 (Error for the Model-Based Method). Sup-pose Γ = 1 + ε in Assumption 3. Then the value estimation from solving (1) with infinite data, denoted by Ṽ1, provides a lower bound no looser than CFQE and satisfies that |V πe 
1 (s0)− Ṽ1(s0)| = O(εH2) for any range of ε. 
We will find in experiments that the lower bound produced by the model-based method is in fact tighter in some scenarios. In the finite-sample setting, we use point estimates P̂πb to construct G. In another version for finite samples, one can account for estimation error of P̂πb by constructing a Hoeffding confidence interval for the state transition probabilities, and using it to construct G instead. We discuss this in Appendix E. Denoting the output of either version by V̂1, the theorem below guarantees that V̂1 is a consistent estimate for the infinite-sample lower bound Ṽ1. We prove it in Appendix E, and the Hausdorff-distance-based technique developed for the proof can be used to provide similar guarantees for FQE and CFQE. 
Theorem 5 (Consistent Estimation of the Lower Bound). The estimated lower bound from the model-based method is strongly consistent for the lower bound Ṽ1, where Ṽ1 is the lower bound estimate of the value function from solving (1) with infinite data. That is, V̂1 
a.s.→ Ṽ1. 
A Computationally Efficient Method. Although the non-convex optimization problem in (1) is solvable with off-the-shelf solvers, such problems can be difficult to solve efficiently. We provide a method, Al-gorithm 5, in Appendix F for quicker computation of lower bounds. This method approximately solves the model-based optimization problem in (1) via projected gradient descent, optimizing over P while maintaining the Bellman constraints. 
Non-Stationary Model-Based Method. To handle non-stationary settings, we provide Algorithm 4 in Appendix F. This relaxes the Bellman backup constraints in (1) by sequentially solving H efficiently solvable quadratic programs. This is essentially the model-based analogue to CFQE. 
4 OPE under Confounders with Memory 
Sensitivity constraints do not alone contribute to the error upper bounds in Section 3 – the memorylessness of confounders is an important ingredient. We demonstrate below that OPE under confounders with memory is hard even for πb with the best-case sensitivity, Γ = 1. Recall that Γ = 1 corresponds to confounder-oblivious behavior policies. Specifically, the theorem below shows FQE and any method that lower bounds FQE will have Ω(H) worst-case error for confounders with memory, even for unconfounded πb and πe with bounded concentrability and given infinite data. We prove it in Appendix G. 
Theorem 6 (Lower Bound for Confounders with Mem-ory). There exists an MDPM having confounders with memory, a stationary unconfounded behavior policy πb 
with sensitivity Γ = 1, a stationary evaluation policy πe with πe(a|s) 
πb(a|s) ≤ 2 ∀s, a, and a state s1, so that V πe 1 (s1) = Ω(H) while the output of FQE for πe is 
O(logH), even with infinite data. 
While the challenges of FQE for POMDPs in general are qualitatively understood Uehara et al. (2022), we show that it can be arbitrarily bad even in the much milder setting of confounded MDPs with unconfounded πb and πe. This suggests that making more specific assumptions about confounders with memory is necessary for designing OPE algorithms with theoretical guarantees. One example of such an assumption is the global confounder assumption, discussed below. 
4.1 Clustering-Based OPE for Global Confounders 
The main message of this section is that the dependence of confounders across timesteps can make it possible to pin down the effect of confounding and achieve consistent OPE, given enough structure to the dependence. We bring our focus to global confounders (Assumption 2) in the case where transition dynamics are stationary, and so are the behavior and evaluation policies. Notice that in the stationary setting, global confounders exactly describe a mixture of MDPs. Let the value of the evaluation policy πe under the dynamics induced by confounder u be V1(s0;u, πe). If one can estimate this value and P (u) for each u, then one can provide point estimates of the policy value V πe 1 (s0) = 
∑ u P (u)V1(s0;Cu, πe). 
We use Algorithm 1 as a broad meta-algorithm that takes a clustering algorithm and an OPE algorithm as input. We cluster the data and apply the OPE algorithm separately to each cluster to obtain a consistent final policy value estimate V̂1(s0;πe). The crucial intuition behind this algorithm is the fact that the value
Offline Policy Evaluation and Optimization under Confounding 
estimate is a weighted average of value estimates over each confounder. 
Algorithm 1 Clustering-Based OPE 1: input: Number of clusters U , evaluation policy πe, 
clustering algorithm cluster(), OPE estimator ope(). 
2: run subroutine: Use cluster() to obtain clusters C1, ..., CU . 
3: Obtain cluster weight estimates P̂ (u) := |Cu| Ntraj 
. 
4: run subroutine: Estimate V̂1(s0;Cu, πe) for each cluster Cu using ope(). 
5: return: Output the final policy value estimate V̂1(s0;πe) = 
∑U u=1 P̂ (ui)V̂1(s0;Cu, πe). 
To present an end-to-end theoretical guarantee, we instantiate the meta-algorithm using the recent work of Kausik et al. (2022) as our clustering algorithm and the data-splitting tabular-MIS (marginalized importance sampling) estimator from Yin and Wang (2020) as our OPE estimator. To satisfy the assumptions of Kausik et al. (2022) and Yin and Wang (2020), we require 3 additional assumptions, discussed in their papers. 
Assumption 4 (Mixing, from Kausik et al. (2022)). Let the U Markov chains on S ×A induced by the various behavior policies π(a | s, u), each achieve mixing to a stationary distribution du(s, a) with mixing time tmix,u. Define the overall mixing time of the mixture of MDPs to be tmix := maxu tmix,u. 
Assumption 5 (Model Separation, from Kausik et al. (2022)). There exist α,∆ > 0 so that for each pair u1, u2 of confounders, there exists a state action pair (s, a) (possibly depending on u1, u2) so that the stationary distributions under each confounder du1(s, a), du2(s, a) ≥ α and ∥P(u1)(· | s, a) − P(u2)(· | s, a)∥2 ≥ ∆. 
Assumption 6 (Concentrability and Exploration, from Yin and Wang (2020)). For dm := min{dπb 
h (s) | dπe 
h (s) > 0}, dm > 0, and there exist constants τa and τs so that for all s, a, h dπe 
h (s) 
d πb h (s) 
≤ τs and πe(a|s) πb(a|s) ≤ τa. 
We can therefore leverage the work of Kausik et al. (2022) to achieve exact clustering with enough data under Assumptions 2, 4, and 5, recovering the unobserved global confounder un in each trajectory up to permutation2. Then, when using the estimator from Yin and Wang (2020) under Assumption 6, we obtain the following guarantee. 
Theorem 7 (Sample Complexity for OPE under Global Confounding). Under Assumptions 2, 4, 5, 
2They recover clusters, which is sufficient as we only need to know confounders up to renaming the labels. 
6, there are constants H0, N0 depending polynomially on 1 
α ,∆, 1 minu P (u) , log(1/δ), so that for n trajec-
tories of length H ≥ H0tmix log(n), we have that |V̂1(s0;πe) − V1(s0;πe)| < ϵ with probability at least 1− δ if n ≥ Ω(max(n1, n2, n3, n4)), where 
n1 := U2SN0 log(1/δ), n2 := log(U/δ) 
min(ϵ2/H2,minu P (u)2) 
n3 := H2τaτsSA log(U/δ) 
ϵ2 , n4 := 
τaH 
dm 
The first term represents the sample complexity for exact clustering (given in Kausik et al. (2022)), the second term corresponds to estimating P (u) accurately and the third and fourth come from the sample complexity of the OPE estimator (given in Yin and Wang (2020)). In Appendix H, we prove a more general version of this theorem, where the OPE estimator makes an assumption A(b) depending on a parameter vector b and has sample complexity N2(δ, ϵ, b). Results analogous to Theorem 7 can thus be produced using Corollary 1 of Duan and Wang (2020), or other off-policy estimators listed in section 2 of Zhang et al. (2022) viewed in a tabular setting. This is the first result that provides sample complexity guarantees for consistent point estimates under confounding. Theorem 12 in Appendix I shows that requiring that H ≥ Ω(tmix) in Theorem 7 is unavoidable, even for small tmix = O(log(S)). 
5 Policy Optimization under Confounding 
We first make an elementary observation that given a bound on the OPE error |V̂1(π) − V1(π)| and an optimizer for the value estimate π̂∗ ∈ argmax V̂1(π), we can obtain a sub-optimality bound for π̂∗. We show this explicitly in Appendix J, noting that this is agnostic to the existence and the nature of confounding. 
Policy Gradients on Lower Bounds under Mem-oryless Confounding. Recall that in Section 3, we produced lower bounds on the value function under memoryless confounding with a sensitivity model. In lieu of optimizing a point estimate of the policy’s value, we can instead improve this lower bound. 
Recall that Algorithm 5 in Appendix F computes a lower bound on V1(s0) by projected gradient descent. We can backpropagate gradients relative to the evaluation policy, improving the lower bound on V1(s0), and therefore the policy, with gradient ascent. We present the case with stationary transition structures in the max-min formulation below in the interest of lucidity, noting that it immediately generalizes to non-stationary transition structures as well. 
max θ∈Θ 
min P∈G 
V1(s0;πθ,P) (2)
Kausik, Lu, Tan, Makar, Wang, Tewari 
We repeat the alternating process of finding P ∈ G to minimize V1(s0) given an evaluation policy πθ and then performing a gradient ascent update on πθ. This is illustrated fully in Algorithm 6 in Appendix J,3 where we discuss local convergence guarantees for the method. 
Policy Gradients under Global Confounding. Recall that we hope to solve argmaxπe 
V1(s0;πe), where V1(s0;πe) = 
∑ u P (u)V1(s0;u;πe), for confounder-
unaware evaluation policy πe. This is the Weighted-Value Problem in Steimle et al. (2021), which is NP-hard according to Proposition 2 in their paper. 
We discuss a policy gradient method for this problem. Let Z(θ) := ∇θV1(s0;πθ). By Assumption 2, Z(θ) = ∇θEu[V1(s0;u, πθ)] = ∇θ 
∑ u P (u)V1(s0;u, πθ) =∑ 
u P (u)∇θV1(s0;u, πθ). Therefore, if we have gradient estimates Ẑi(θ) of Zi(θ) = ∇θV1(s0;ui, πθ) for each cluster, we can obtain the final policy gradient estimate as a weighted sum, given by Ẑ(θ) = 
∑U u=1 P̂ (ui)Ẑi(θ). 
We present this as Algorithm 7 in Appendix K. 
We then perform standard gradient descent for T iterations on the policy parameters θ, with the update rule given by θt+1 = θt − ηẐ(θt). In analyzing this procedure, we instantiate Ẑi using the (statistically) Efficient Off-Policy Policy Gradient (EOPPG) estimator from Kallus and Uehara (2020), which enjoys an Θ(H4/n) MSE guarantee instead of the 2Θ(H)Θ(1/n) worst-case sample complexity of REINFORCE Kallus and Uehara (2020). We assume that the gradient of V1 is bounded by L, which holds if V1 is L-Lipschitz. Additionally, let assumptions for Theorem 12 in Kallus and Uehara (2020) hold. We obtain a bound on the norm of the policy gradient that shows convergence to a stationary point in Theorem 8 below. It is proved in Appendix K. 
Theorem 8. Let us have large enough β > 1 and T = 
nβ, for n ≥ Ω ( max 
( U2SN0 log(1/δ), 
log(U/δ) minu P (u)2 
)) . 
Also let H ≥ H0tmix log n, for H0, N0 as in Theo-rem 7. Then we have that 1 
T 
∑T t=1 ||∇θV1(s0;πθt)||2 = 
O(max(ϵMSE , ϵfreq), where ϵMSE = H4 log(nU/δ) nminu P (u) , and 
ϵfreq = L2 log(U/δ) n 
6 Numerical Experiments 
We detail our experiments for memoryless and global confounders below. The code for all experiments can be found at https://github.com/hetankevin/off-policy. 
3Given libraries like cvxpylayers, we can also perform gradient ascent on any lower bound from differentiable convex optimization. This includes the lower bounds generated by the relaxation of the model-based algorithm (Alg. 4) and CFQE (Alg. 3). We state general lemmas that back our claims. 
Figure 1: OPE for Memoryless Confounders. Compari-son of our model-based method, its non-stationary relaxation (Alg. 4), its projected gradient descent variant (Alg. 5), and CFQE on state 13 in a 16-state gridworld. Confidence intervals (CIs) are one standard deviation wide and computed over 30 trials. H = 8. 
Gridworld for Memoryless Confounders. We examine the performance of the methods in Section 3 on the 4x4 gridworld environment used by Bruns-Smith (2021), with i.i.d. (and thus memoryless) confounders. We implement the model-based method and its variations using the point estimates P̂πb instead of Hoeffding confidence intervals for Pπb , for a fair comparison with CFQE. The horizon is H = 8, and Γ ranges from 1 to 50. We plot the policy values against Γ in Figure 1. Across all 16 states, the model-based method’s lower bound is always either as good as or tighter than that of CFQE, but the gap in performance is seen most starkly in state 13 (which we display in Figure 1). The output of FQE is obtained at Γ = 1 and is at most −0.7. By the remark after the proof of Theorem 2, the naive lower bound obtained using FQE is less than −0.7− εH2 
2 = −0.7− 32ε. This is quite literally "off-the-chart" here, showing that using FQE for lower bounds would be ineffective in practice. Note that our model-based method gives the closest lower bound after projected gradient descent. Projected gradient descent only approximately solves the appropriate optimization problem, and it is thus not guaranteed to return a true lower bound. So, our model-based method is empirically the best method here with guarantees. 
We also study policy improvement. Figure 2 displays the training dynamics and convergence of Algorithm 6, where we perform gradient ascent on a lower bound obtained by Algorithm 5. We visualize the learned policy, which is appropriately conservative: on a horizon of 8, the agent will likely not reach the goal state from the first few states and move to the top left corner appropriately. Finally, we plot the increase in the lower bound on policy value against progressing gradient as-
Offline Policy Evaluation and Optimization under Confounding 
cent iterations, starting at πe. Note that even our lower bounds all eventually exceed the true (ground truth) values of πb and πe, displaying improvement. 
Figure 2: Policy Improvement for Memoryless Con-founders. Top Left: Loss curve dynamics of max-min gradient descent. Top Right: Resulting policy π̂∗ for Γ = 10 in 4x4 gridworld with actions indexed by WENS. Brighter colors indicate higher π̂∗(a | s). Bottom: In-crease in the lower bound on V πθ 
1 as gradient ascent iterations progress. H = 8. 
Sepsis Simulator for Global Confounders. We examine the performance of the method of Algorithm 1 on the sepsis simulator of Oberst and Sontag (2019), especially in terms of the choice of the clustering algorithm. Once we hide the diabetes status of each patient, it becomes a global confounder. The confounderaware behavior policy is the same behavior policy in Oberst and Sontag (2019), and the evaluation policy is πe := 
1 U 
∑ u πb(a|s, u). In the simulator, glucose levels 
are generated i.i.d, with their distribution determined by the presence or absence of diabetes. This makes them easy proxies for diabetes, so we hide glucose levels during the clustering phase to make the clustering problem harder. 
On the top left of Figure 3, we compare the clustering error for the method of Kausik et al. (2022) with that of classical soft EM with random initialization. In the top right, we plot a measure of the relative error in OPE against trajectory length. The relative error is computed as maxs |V̂ πe 
1 (s)−V πe 1 (s)| 
maxs |V πe 1 (s)| . The plot compares 
the performance of Algorithm 1 instantiated with FQE 
coupled with either soft EM with random initialization or the method of Kausik et al. (2022). At the bottom, we show the convergence of Algorithm 7, instantiated using the off-policy policy gradient variant that Kallus and Uehara (2020) attributes to Degris et al. (2013). We compare the same possibilities for clustering as above. We observe that in general, the method of Kausik et al. (2022) outperforms randomly initialized soft EM, allowing for both OPE and policy improvement. Our experimental results highlight the effectiveness of our method as well as the importance of the clustering algorithm. 
Figure 3: Top Left: Average performance of the clustering method from Kausik et al. Top Right: Average relative error of clustering-based OPE with different clustering algorithms. Bottom: Improvement in estimates of policy values under gradient ascent coupled with different clustering algorithms, see Appendix A for details. We average over 30 trials, confidence intervals are 1 standard deviation wide. H = 60. 
7 Conclusion and Future Work We have provided a broad, structured view of the landscape of confounded MDPs, studying the OPE and OPI problems under various confounding assumptions. The paper has discussed existing methods, presented new ones and provided theoretical and empirical grounding for the methods. We hope that the insights here will springboard further work on confounded MDPs. In particular, while we address the sensitivity assumption, a big-picture view of other assumptions like bridge functions and instrumental variables is needed. For general confounders with memory, note that while Theorem 6
Kausik, Lu, Tan, Makar, Wang, Tewari 
rules out FQE and related methods, other methods must be explored. There are also specific structures on confounders with memory, besides global confounders, that can be formulated and studied. Finally, many of our methods (such as the gradient-based methods presented) can be extended to handle continuous state spaces via function approximation. Shi et al. (2021) provide methods under assumptions on the existence and learnability of bridge functions, being one of the first works to address this. However, work on confounding with continuous state and action spaces is still relatively sparse, and is an exciting setting to explore. 
8 Acknowledgements We would like to acknowledge the support of NSF via grants CHE-2231174, DMS-2310831 (YW), IIS-2007055 (AT), and IIS-2153083 (MM) and of ONR via grant N00014-23-1-2590 (YW). Most of this work was done while KT was an undergraduate student at the University of Michigan. 
References Bennett, A., Kallus, N., Li, L., and Mousavi, A. 
(2020). Off-policy evaluation in infinite-horizon reinforcement learning with latent confounders. CoRR, abs/2007.13893. 
Bruns-Smith, D. and Zhou, A. (2023). Robust fitted-q-evaluation and iteration under sequentially exogenous unobserved confounders. 
Bruns-Smith, D. A. (2021). Model-free and model-based policy evaluation when causality is uncertain. In International Conference on Machine Learning, pages 1116–1126. PMLR. 
Clare, P. J., Dobbins, T. A., and Mattick, R. P. (2018). Causal models adjusting for time-varying confounding—a systematic review of the literature. Interna-tional Journal of Epidemiology, 48(1):254–265. 
Daniel, R. M., Cousens, S. N., De Stavola, B. L., Ken-ward, M. G., and Sterne, J. A. C. (2013). Methods for dealing with time-dependent confounding. Stat. Med., 32(9):1584–1618. 
Daskalakis, C. and Panageas, I. (2018). The limit points of (optimistic) gradient descent in min-max optimization. 
Degris, T., White, M., and Sutton, R. S. (2013). Off-policy actor-critic. 
Duan, Y. and Wang, M. (2020). Minimax-optimal offpolicy evaluation with linear function approximation. CoRR, abs/2002.09516. 
Fu, Z., Qi, Z., Wang, Z., Yang, Z., Xu, Y., and Kosorok, M. R. (2022). Offline reinforcement learning with instrumental variables in confounded markov decision processes. 
Kaelbling, L. P., Littman, M. L., and Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. Artificial Intelligence, 101(1):99– 134. 
Kallus, N. and Uehara, M. (2020). Statistically efficient off-policy policy gradients. 
Kallus, N. and Zhou, A. (2020). Confounding-robust policy evaluation in infinite-horizon reinforcement learning. arXiv preprint arXiv:2002.04518. 
Kausik, C., Tan, K., and Tewari, A. (2022). Learning mixtures of markov chains and mdps. 
Lee, J. D., Simchowitz, M., Jordan, M. I., and Recht, B. (2016). Gradient descent converges to minimizers. 
Levin, D. A. and Peres, Y. (2017). Markov chains and mixing times, volume 107. American Mathematical Soc. 
Levine, S., Kumar, A., Tucker, G., and Fu, J. (2020). Offline reinforcement learning: Tutorial, review, and perspectives on open problems. CoRR, abs/2005.01643. 
Liao, L., Fu, Z., Yang, Z., Wang, Y., Kolar, M., and Wang, Z. (2021). Instrumental variable value iteration for causal offline reinforcement learning. 
Mansournia, M. A., Etminan, M., Danaei, G., Kauf-man, J. S., and Collins, G. (2017). Handling time varying confounding in observational research. BMJ: British Medical Journal, 359. 
Miao, R., Qi, Z., and Zhang, X. (2022). Off-policy evaluation for episodic partially observable markov decision processes under non-parametric models. In Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A., editors, Advances in Neural Information Processing Systems, volume 35, pages 593–606. Curran Associates, Inc. 
Nair, Y. and Jiang, N. (2021). A spectral approach to off-policy evaluation for pomdps. ArXiv, abs/2109.10502. 
Namkoong, H., Keramati, R., Yadlowsky, S., and Brun-skill, E. (2020). Off-policy policy evaluation for sequential decisions under unobserved confounding. arXiv preprint arXiv:2003.05623. 
Oberst, M. and Sontag, D. (2019). Counterfactual offpolicy evaluation with gumbel-max structural causal models. 
Platt, R. W., Schisterman, E. F., and Cole, S. R. (2009). Time-modified Confounding. American Journal of Epidemiology, 170(6):687–694. 
Shi, C., Uehara, M., Huang, J., and Jiang, N. (2021). A minimax learning approach to off-policy evaluation in confounded partially observable markov decision processes. In International Conference on Machine Learning.
Offline Policy Evaluation and Optimization under Confounding 
Steimle, L., Kaufman, D., and Denton, B. (2021). Multi-model markov decision processes. IISE Transactions, 53:1–39. 
Tennenholtz, G., Mannor, S., and Shalit, U. (2019). Off-policy evaluation in partially observable environments. CoRR, abs/1909.03739. 
Uehara, M., Kiyohara, H., Bennett, A., Chernozhukov, V., Jiang, N., Kallus, N., Shi, C., and Sun, W. (2022). Future-dependent value-based off-policy evaluation in pomdps. 
Wang, L., Yang, Z., and Wang, Z. (2020). Provably efficient causal reinforcement learning with confounded observational data. CoRR, abs/2006.12311. 
Yin, M. and Wang, Y.-X. (2020). Asymptotically efficient off-policy evaluation for tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 3948–3958. PMLR. 
Zhang, J. and Bareinboim, E. (2016). Markov decision processes with unobserved confounders : A causal approach. 
Zhang, R., Zhang, X., Ni, C., and Wang, M. (2022). Off-policy fitted q-evaluation with differentiable function approximators: Z-estimation and inference theory. In Chaudhuri, K., Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato, S., editors, Proceedings of the 39th International Conference on Machine Learn-ing, volume 162 of Proceedings of Machine Learning Research, pages 26713–26749. PMLR. 
Checklist 
1. For all models and algorithms presented, check if you include: 
(a) A clear description of the mathematical setting, assumptions, algorithm, and/or model. [Yes/No/Not Applicable] 
In each section, we clearly introduce the relevant assumptions made and the mathematical problem setup. Algorithms are presented in pseudocode. 
(b) An analysis of the properties and complexity (time, space, sample size) of any algorithm. [Yes/No/Not Applicable] 
We analyze the properties of each of the algorithms provided, with theoretical results on sample complexity and error bounds. 
(c) (Optional) Anonymized source code, with specification of all dependencies, including external libraries. [Yes/No/Not Applicable] 
Source code is provided in a zip file along with the paper submission. 
2. For any theoretical claim, check if you include: 
(a) Statements of the full set of assumptions of all theoretical results. [Yes/No/Not Applicable] 
In each section, we clearly introduce the relevant assumptions made and the mathematical problem setup. 
(b) Complete proofs of all theoretical results. [Yes/No/Not Applicable] 
Each theoretical result is presented with proof. 
(c) Clear explanations of any assumptions. [Yes/No/Not Applicable] 
We explain each assumption as we make them. 
3. For all figures and tables that present empirical results, check if you include: 
(a) The code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL). [Yes/No/Not Applicable] 
Source code is provided in a zip file along with the paper submission. 
(b) All the training details (e.g., data splits, hyperparameters, how they were chosen). [Yes/No/Not Applicable] 
(c) A clear definition of the specific measure or statistics and error bars (e.g., with respect to the random seed after running experiments multiple times). [Yes/No/Not Applicable] 
See figures in section 6. 
(d) A description of the computing infrastructure used. (e.g., type of GPUs, internal cluster, or cloud provider). [Yes/No/Not Applicable] 
See Appendix A 
4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets, check if you include: 
(a) Citations of the creator If your work uses existing assets. [Yes/No/Not Applicable] 
(b) The license information of the assets, if applicable. [Yes/No/Not Applicable] 
(c) New assets either in the supplemental material or as a URL, if applicable. [Yes/No/Not Applicable] 
(d) Information about consent from data providers/curators. [Yes/No/Not Applica-ble]
Kausik, Lu, Tan, Makar, Wang, Tewari 
(e) Discussion of sensible content if applicable, e.g., personally identifiable information or offensive content. [Yes/No/Not Applicable] 
5. If you used crowdsourcing or conducted research with human subjects, check if you include: 
(a) The full text of instructions given to participants and screenshots. [Yes/No/Not Appli-cable] 
(b) Descriptions of potential participant risks, with links to Institutional Review Board (IRB) approvals if applicable. [Yes/No/Not Appli-cable] 
(c) The estimated hourly wage paid to participants and the total amount spent on participant compensation. [Yes/No/Not Applica-ble]
Offline Policy Evaluation and Optimization under Confounding 
A Experimental Details 
Computing Infrastructure. All numerical experiments were run on a single desktop computer with an Intel i9-13900K CPU, 128 gigabytes of RAM, and an NVIDIA RTX 3090 graphics card. 
Estimating Policy Values for Global Confounders. Due to computationally expensive operations needed to compute the exact policy value for confounders, we use estimates of the policy values instead. Namely, we get estimates V̂1(s0, u, π) for a policy π, and report 
∑ u P (u)V̂1(s0, u, π). Computing the true values V1(s0, u, π) is 
computationally far more expensive. The estimates V̂1(s0, u, π) are obtained using standard FQE applied to the standard, unconfounded MDP determined by confounder u. 
B Lower Bounds for Memoryless Confounders 
We recall and prove Theorem 1. 
Theorem 1 (Lower Bound for Memoryless Confounders). There exists a parameter ε that determines a pair of confounded MDPs M1 and M2 with i.i.d. (and thus memoryless) confounders along with stationary policies πb1 , πb2 and πe, so that data collected from Mi using πbi has the same distribution for i = 1, 2, but the values under πe differ by |V πe 
1 (M1)− V πe 1 (M2)| = 2εH. In particular, when ε = 1 
2 − 1 
H2 , the values under πe differ by Ω(H). 
Proof. Consider two confounded MDP environments M1 and M2. 
Environments. In both environments: 
 S = {1, 2}, U = {1, 2}, A = {1, 2}, horizon H. 
 r(s = 1) = 1, r(s = 2) = 0. 
For confounders: 
 P1(u = 1) = 1 2 − ε, P1(u = 2) = 1 
2 + ε. 
 P2(u = 1) = 1 2 + ε, P2(u = 2) = 1 
2 − ε. 
For full state transitions: 
P1(s ′ = 1 | s, u = 1, a = 1) = z,P1(s 
′ = 1 | s, u = 2, a = 1) = 1− z 
P1(s ′ = 1 | s, u = 1, a = 2) = z1,P1(s 
′ = 1 | s, u = 2, a = 2) = z2 
P2(s ′ = 1 | s, u = 1, a = 1) = z,P2(s 
′ = 1 | s, u = 2, a = 1) = 1− z 
P2(s ′ = 1 | s, u = 1, a = 2) = z2,P2(s 
′ = 1 | s, u = 2, a = 2) = z1 
Next, consider two behavior policies πb1 and πb2 : 
πb1(a = 1 | s, u = 1) = 1 
2 + ε, πb1(a = 1 | s, u = 2) = 
1 
2 − ε 
πb2(a = 1 | s, u = 1) = 1 
2 − ε, πb2(a = 1 | s, u = 2) = 
1 
2 + ε 
And an evaluation policy πe: 
πe(s) = 1, for s = {1, 2}. 
Data Collection. Suppose we collect data using πb1 in M1 and using πb2 in M2. Notice that the sensitivity Γ is given by 
Γ = 
( 1 2 + ε 1 2 − ε 
)( 1 2 + ε2 
1 2 − ε2 
)
Kausik, Lu, Tan, Makar, Wang, Tewari 
Observations. Note that in the limit, i.e. infinite data, the observed transition probabilities and policies are given by 
P̂1(s ′, a | s) = 
∑ u 
P1(u)πb1(a | s, u)P1(s ′ | s, u, a), 
π1(a | s) = ∑ u 
P (u)π1(a | s, u), 
P̂1(s ′ | s, a) = P̂1(s 
′, a | s)/π1(a | s). 
One can then easily verify that for all s, a, s′, the observed transition probabilities will be equal: 
P̂1(s ′, a | s) = P̂2(s 
′, a | s), 
For example, P̂i(s ′ = 1, a = 1 | s) = x(1− x) for i = 1, 2. 
The state transition and the observed policy induced by the two policies in their corresponding environment are thus also equal: 
π1(a | s) = π2(a | s), P̂1(s 
′ | s, a) = P̂2(s ′ | s, a). 
That means, no algorithm can distinguish the two environments based on the given two datasets. 
Value under the evaluation policy. Recall that at each step, we take action 1. Note that the true marginalized state transitions will be different, which are what a confounder-oblivious policy will interact with: 
P1(s ′ = 1 | s, a = 1) = 
∑ u 
P1(u)P1(s ′ = 1 | s, u, a = 1) = 
( 1 
2 + ε 
) (1− z) + 
( 1 
2 − ε 
) z 
P2(s ′ = 1 | s, a = 1) = 
∑ u 
P2(u)P2(s ′ = 1 | s, u, a = 1) = 
( 1 
2 − ε 
) (1− z) + 
( 1 
2 + ε 
) z 
Note that Pπe i (s′ = 1 | s) = Pi(s 
′ = 1 | s, a = 1). Since state transitions are independent of the initial state, this is the same as generating a state independently at each step based on the action taken. Then under the evaluation policy πe(a = 1 | s) = 1, the state s = 1 is generated i.i.d. at each step with probability pi = Pi(s 
′ = 1 | s, a = 1) inMi, while s = 2 is generated with probability 1− pi. So, the reward of a trajectory is distributed according to Bin(H, pi), having an expected value of V πe 
1 (Mi) = Hpi = HPi(s ′ = 1 | s, a = 1). 
Necessity of a Sensitivity Assumption Let ε = 1 2 − 
1 H2 , z = 0. We then have the following 
V πe 1 (M1) = H((1− 1 
H2 )2 + 1/H4) = O(H) 
V πe 1 (M2) = 2H · 1 
H2 (1− 1 
H2 ) = O( 
1 
H ). 
From this example, we see that without information about Γ, no algorithm can universally give meaningful lower bounds for the true value function. One can compute that in this example, Γ = Θ(H2). 
Lower Bound on Value Estimation Under Sensitivity Let ε be small and let z = 0. We then have the following. 
V πe 1 (M1) = H( 
1 
2 − ε) 
V πe 1 (M2) = H( 
1 
2 + ε) 
Note that Γ = 1 + O(ε+ ε2) = 1 + O(ε) for small ε. Since any estimator will return the same value for both MDPs (because they are observationally indistinguishable under the behavior policy), any estimator will have a worst-case error of at least εH. Thus, there does not exist a consistent estimator whenever Γ > 1.
Offline Policy Evaluation and Optimization under Confounding 
C FQE and Confounded FQE 
We describe the FQE and CFQE algorithms here, adapted for memoryless systems instead of merely stationary ones. 
C.1 FQE Algorithm 
Algorithm 2 FQE 1: input: evaluation policy πe. 2: initialize: f̂H+1 ← 0. 3: for h = H,H − 1, . . . , 1 do 3: f̂h(s, a)← E(s,a,s′)∼Dπb 
,h 
[ rh(s, a) + 
∑ a′ πe,(h+1)(a 
′ | s′)f̂h+1(s ′, a′) 
] ,∀s, a. 
4: end for 5: return: 
∑ a πe,1(a | s)f̂1(s, a) for ∀s. 
C.2 Confounded FQE Algorithm Confounded FQE (CFQE), proposed by Bruns-Smith (2021), provides an estimate for a lower bound by taking the characteristics of the data into account. Given infinite samples, this will actually be a lower bound, unlike the case of FQE. In particular, CFQE obtains an estimate for a lower bound by sequentially searching over the worst behavior policy consistent with the observations. 
Let π̂b,h(a | s) and P̂h(s ′ | s, a) be empirical estimates from finite data Dπb,h. Let Pπb 
h (s′ | s, a) be the limit of P̂h(s 
′ | s, a) under infinite data. We then define the following uncertainty sets. 
Definition 1 (Valid Behavior Policy Set). Under a memoryless confounder, for all s, a, s′, define Bsa,h to be the set of all π(a | s, ·) that satisfy Assumption 3 and the two equations below.∑ 
u∈U Ph(u | s)πb,h(a | s, u) = πb,h(a | s)∑ 
u∈U Ph(u | s)πb,h(a | s, u)P (s′ | s, u, a) = πb,h(a | s)Pπb 
h (s′ | s, a). 
Now we define the following quantity using the posteriors Pπb 
h (u | s, a), a confounded analog to inverse propensity weights. 
gh(s, a, s ′) := 
∑ u 
( Pπb 
h (u | s, a)Ph(s ′ | s, a, u) 
P̂πb 
h (s′ | s, a) 
) 1 
πb,h(a | s, u) 
= ∑ u 
( Ph(u | s)Ph(s 
′ | s, a, u) P̂πb 
h (s′ | s, a) 
) 1 
πb,h(a | s) 
Theorem 1 and the discussion following that in Bruns-Smith (2021) shows that we can reflect the same uncertainty using the set B̃sa,h of possible values of gh(s, a, ·). 
B̃sa,h := {gh(s, a, ·) | αh(s, a) ≤ πb,h(a | s)gh(s, a, s′) ≤ βh(s, a),∑ s′ 
πb,h(a | s)gh(s, a, s′)Pπb 
h (s′ | s, a) = 1} (3) 
B̃sa,h presents a reparameterization of the uncertainty that allows us to get rid of the explicit presence of the unknown variable u while optimizing over the uncertainty set. Let B̂sa,h and ˆ̃Bsa,h be the version of these sets determined by the point estimates π̂b and P̂(s′ | s, a) under finite data, instead of by their true values. 
However, if a very poor estimate of π̂b and P̂πb (s′ | s, a) is collected (due to low N(s, a) and/or N(s)), the 
estimated lower bound will be a lower bound on the output of FQE but not on the true value. To get a lower
Kausik, Lu, Tan, Makar, Wang, Tewari 
Algorithm 3 Confounded FQE (adapted from Bruns-Smith (2021)) 
1: input: evaluation policy πe. 2: initialize: f̂H+1 ← 0. 3: for h = H,H − 1, . . . , 1 do 4: Compute 
f̂h(s, a) := 
min gh(s,a,·)∈ ˆ̃Bsa,h 
E(s,a,s′)∼Dπb,h 
[ π̂b,h(a | s)gh(s, a, s′) 
( rh(s, a) + 
∑ a′ 
πe,h(a ′ | s′)f̂h+1(s 
′, a′) 
)] 
5: end for 6: return: 
∑ a πe(a | s)f̂1(s, a) for ∀s. 
bound on the true value with probability at least 1 − δ, we modify ˆ̃Bsa,h using error bounds errπ(N(s)) and errP(N(s, a)) obtained using the Hoeffding inequality to get the following set. 
{gh(s, a, ·) | αh(s, a) ≤ πb,h(a | s)gh(s, a, s′) ≤ βh(s, a),∑ s′ 
πb,h(a | s)gh(s, a, s′)Pπb 
h (s′ | s, a) = 1 
|πb,h(s, a)− π̂b,h(s, a)| ≤ errπ(N(s)), 
|Pπb 
h (s′ | s, a)− P̂h(s ′ | s, a)| ≤ errP(N(s, a))} 
Additionally, the observant reader will note that CFQE finds a different optimal gh for each time step. That is, it finds H different functions g1(s, a, ·), ..., gH(s, a, ·) ∈ B̃sa. If the transition structures were stationary, this does not leverage the stationarity. In that case, it is advisable to use our model-based method and its projected gradient descent version, as discussed in Section 3.
Offline Policy Evaluation and Optimization under Confounding 
D FQE and CFQE Theoretical Results D.1 Proof of FQE Error Bounds, Theorem 2 We recall the theorem below. 
Theorem 2 (FQE Error). Suppose Γ = 1 + ε in Assumption 3. Then in the limit of infinite samples, the point estimate f̂1(s, a) of the Q-function produced by FQE has a worst-case error of |V πe 
1 (s)− ∑ 
a πe,1(a | s)f̂1(s, a)| = O(εH2) for small ε. 
Proof. In the limit of an infinite amount of data, at every step of FQE, the update evaluates f̂h(s, a) using: 
f̂h(s, a) = argminfh(s,a) E(s,a,s′)∼Dh πb 
[lossFQE(fh(s, a), s ′)] 
= argminfh(s,a) ∑ u,s′ 
Pπb(s′, u | s, a)lossFQE(fh(s, a), s ′) 
= argminfh(s,a) ∑ u,s′ 
Pπb 
h (u | s, a)Ph(s ′ | s, u, a)lossFQE(fh(s, a), s 
′) 
= argminfh(s,a) ∑ u,s′ 
Ph(u | s) πb,h(a | s, u) πb,h(a | s) 
∑ s′ 
Ph(s ′ | s, u, a)lossFQE(fh(s, a), s 
′) 
where Pπb 
h (u | s, a) is the posterior on u under πb and 
lossFQE(fh(s, a), s ′) = 
( fh(s, a)− r(s, a)− 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
)2 
f̂h(s, a) is then given by the following expression. 
∑ u,s′ 
Ph(u | s) πb,h(a | s, u) πb,h(a | s) 
Ph(s ′ | s, u, a) 
( r(s, a) + 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
) 
= r(s, a) + ∑ u,s′ 
Ph(u | s) πb,h(a | s, u) πb,h(a | s) 
Ph(s ′ | s, u, a) 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
True marginalized transition structure. Note that under any confounding-unaware policy πe, the induced transition structure Pπe 
h (s′ | s) is determined by the marginalized transition dynamics Ph(s ′ | s, a) := 
∑ u Ph(u | 
s)Ph(s ′ | s, a, u). This is clear from the computation below. 
Pπe 
h (s′ | s) = ∑ u,a 
πe,h(a | s)Ph(u | s)Ph(s ′ | s, a, u) 
= ∑ a 
πe,h(a | s) 
(∑ u 
Ph(u | s)Ph(s ′ | s, a, u) 
) = ∑ a 
πe,h(a | s)Ph(s ′ | s, a) 
Bounding f̂h(s, a). By Assumption 3 and the computations above, we can bound f̂h(s, a) by: 
f̂h(s, a) ≤ r(s, a) + 1 
αh(s, a) 
∑ s′ 
Ph(s ′ | s, a) 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′), 
f̂h(s, a) ≥ r(s, a) + 1 
βh(s, a) 
∑ s′ 
Ph(s ′ | s, a) 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′). 
The ultimate goal is to bound V πe 1 (s) − 
∑ a πe,1(a | s)f̂1(s, a), which is given by 
∑ a πe,1(a | 
s) ( Qπe 
1 (s, a)− f̂1(s, a) ) . So, we consider the error of f̂h(s, a) at every step, given by errh(s, a) := Qπe 
h (s, a) −
Kausik, Lu, Tan, Makar, Wang, Tewari 
f̂h(s, a). We will use the following relation. 
Qπe 
h (s, a) = r(s, a) + ∑ u,s′ 
Ph(u | s)Ph(s ′ | s, a, u)V πe 
h+1(s ′) 
= r(s, a) + ∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) (4) 
At h = H, by definition 
f̂H(s, a) = r(s, a) = Qπe 
H (s, a). 
Thus, we get that errH(s, a) = 0 for all s, a. Let βmax := maxs,a,h βh(s, a) and let αmin = mins,a,h αh(s, a). 
For step H − 1, 
errH−1(s, a) ≤ ∑ s′ 
PH−1(s ′ | s, a)V πe 
H (s′)− 1 
βH(s, a) 
∑ s′ 
PH−1(s ′ | s, a) 
∑ a′ 
πe,H(a′ | s′)f̂H(s′, a′) 
= (1− 1 
βH(s, a) ) ∑ s′ 
PH−1(s ′ | s, a)V πe 
H (s′) 
≤ ( 1− 1 
βmax 
)∑ s′ 
PH−1(s ′ | s, a) 
( 1− 1 
βmax 
) 
By induction, we will show that for all h, the following holds. 
errh(s, a) ≤ H − h− H−h∑ i=1 
1 
βi max 
We know this for h = H − 1. For the induction step, we show this for h− 1 given the statement for h using the following computation. 
errh−1 ≤ ∑ s′ 
Ph−1(s ′ | s, a)V πe 
h (s′)− 1 
βh(s, a) 
∑ s′ 
Ph−1(s ′ | s, a) 
∑ a′ 
πe,h(a ′ | s′)f̂h(s′, a′) 
≤ ∑ s′ 
Ph−1(s ′ | s, a)V πe 
h (s′) 
+ 1 
βh(s, a) 
∑ s′ 
Ph−1(s ′ | s, a) 
∑ a′ 
πe,h(a ′ | s′)(errh(s, a)−Qπe 
h (s, a)) 
= (1− 1 
βh(s, a) ) ∑ s′ 
Ph−1(s ′ | s, a)V πe 
h (s′) + 1 
βh(s, a) errh(s, a) 
≤ ( 1− 1 
βmax 
)∑ s′ 
Ph−1(s ′ | s, a)(H − h+ 1) + + 
1 
βh(s, a) errh(s, a) 
≤ ( 1− 1 
βmax 
) (H − h+ 1) + 
1 
βmax 
( H − h− 
H−h∑ i=1 
1 
βi max 
) 
= H − h+ 1− H−h+1∑ 
i=1 
1 
βi max 
Thus, the result holds by induction, giving us the following final bound. 
Qπe 1 (s, a)− f̂1(s, a) ≤ H − 1− 
H−1∑ i=1 
1 
βi max 
= H − 1− 1 
βH max 
1− 1 βmax
Offline Policy Evaluation and Optimization under Confounding 
Similarly, we have the lower bound below: 
Qπe 1 (s, a)− f̂1(s, a) ≥ H − 1− 
H−1∑ i=1 
1 
αi min 
= H − 1− 1 
αH min 
1− 1 αmin 
Recall that αh(s, a) = πb,h(a | s) + 1 Γ (1− πb,h(a | s)) and βh(s, a) = Γ + πb,h(a | s)(1− Γ). So, αh(s, a) ≥ 1 
Γ and βh(s, a) ≤ Γ for all s, a, h. In particular, αmin ≥ 1 
Γ = 1 1+ε and βmax ≤ Γ = 1 + ε. 
In particular, we have the following bound. 
1 + εH − (1 + ε)H 
ε ≤ V πe 
1 (s)− ∑ a 
πe,1(a | s)f̂1(s, a) ≤ 1 
(1+ε)H − (1− εH) 
ε 
We know that we have the following bounds for small ε: (1+ε)H ≥ 1+εH+O(εH2) and 1 (1+ε)H 
≤ 1−εH+O(εH2), giving us the following bound for small ε. 
|V πe 1 (s)− 
∑ a 
πe,1(a | s)f̂1(s, a)| ≤ O(εH2) 
Remark. For any ε, the lower bound 1+εH−(1+ε)H 
ε ≤ − εH2 
2 , and thus we need to be at least as conservative as subtracting ϵH2 
2 from the FQE estimate to get a lower bound, if not more. This remark will be used in Section 6. 
We further remark in Section 3 that the bound in the theorem is data-oblivious, being only dependent on the confounding sensitivity model and horizon, and note that the other two methods below (CFQE and MB) both produce bounds at least as tight as this one. 
D.2 Proof of CFQE Error Bounds, Theorem 3 We recall the theorem below. 
Theorem 3 (CFQE Error). Suppose Γ = 1 + ε in Assumption 3. Then the worst-case error for the lower bound f̂1(s, a) generated by CFQE in the infinite-sample case is |V πe 
1 (s) − ∑ 
a πe,1(a | s)f̂1(s, a)| = O(εH2) for any range of ε. 
Proof. In the limit of infinite data, the true value of gh always lies in the set B̃sa,h by the sensitivity assumption. So, CFQE trivially gives a lower bound on the true value function in the limit of infinite data. We now give bounds on its error below. 
We define the error term at each step by errh(s, a) := maxs,a Q πe 
h (s, a)− f̂h(s, a), where here f is generated by CFQE. We claim that 
errh(s, a) = (H − h)− αmin 
βmax − · · · − αH−h 
min 
βH−h max 
. (5) 
Then, the following bound follows for any ε. 
V πe 1 (s)− 
∑ a 
πe(a | s)f̂1(s, a) ≤ H − 1− αmin 
βmax − · · · − αH−1 
min 
βH−1 max 
≤ H − H−1∑ i=0 
1 
(1 + ε)2i 
≤ 2εH2 
This completes the proof since by induction, f̂h(s, a) ≤ Q(s, a) for all h, and so we already have the lower bound V πe 1 (s)− 
∑ a πe(a | s)f̂1(s, a) ≥ 0. Thus, it remains to prove 5.
Kausik, Lu, Tan, Makar, Wang, Tewari 
At step H of CFQE, we have 
f̂H(s, a) = r(s, a). 
Then as in the previous proof, the error at step H is given by errH(s, a) = 0. 
At step h+ 1, suppose errh+1(s, a) = (H − h− 1)− αmin 
βmax − · · · − αH−h−1 
min 
βH−h−1 max 
. Then for step h, we have the following 
chain of inequalities for errh(s, a) = Qπe 
h (s, a)− f̂h(s, a).∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) 
− ∑ u,s′ 
Pπb(s′, u | s, a)πb,h(a | s)gh(s, a, s′) ∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
= ∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) 
− ∑ u,s′ 
Pπb 
h (u | s, a)Ph(s ′ | s, u, a)πb,h(a | s)gh(s, a, s′) 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
= ∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) 
− ∑ u,s′ 
Ph(u | s) πb,h(a | s, u) πb,h(a | s) 
Ph(s ′ | s, u, a)πb,h(a | s)gh(s, a, s′) 
∑ a′ 
πe,h+1(a ′ | s′)f̂h+1(s 
′, a′) 
≤ ∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) 
− αh(s, a) 
βh(s, a) 
∑ u,s′ 
Ph(u | s)Ph(s ′ | s, u, a) 
∑ a′ 
πe,h+1(a ′ | s′)(errh+1 −Qπe 
h+1(s, a)) 
= 
( 1− αh(s, a) 
βh(s, a) 
)∑ s′ 
Ph(s ′ | s, a)V πe 
h+1(s ′) + 
αh(s, a) 
βh(s, a) errh+1 
≤ ( 1− αh(s, a) 
βh(s, a) 
) (H − h) + 
αh(s, a) 
βh(s, a) 
( H − h− 1− αmin 
βmax − · · · − αH−h−1 
min 
βH−h−1 max 
) 
≤ ( 1− αmin 
βmax 
) (H − h) + 
αmin 
βmax 
( H − h− 1− αmin 
βmax − · · · − αH−h−1 
min 
βH−h−1 max 
) 
=H − h− αmin 
βmax − · · · − αH−h 
min 
βH−h max 
. 
The first expression comes from using equation 4 as well as explicitly computing the argmin involved in CFQE in the limit of infinite data, analogous to the proof of Theorem 2 above. In the first inequality, we use the facts that πb,h(a|s,u) 
πb,h(a|s) ≥ 1 
βh(s,a) and πb,h(a | s)gh(s, a, s′) ≤ αh(s, a). In the equality after that, we use the definition of 
errh(s, a). In the second inequality, we use equation 4. 
Thus, errh(s, a) = H − h− αmin 
βmax − · · · − αH−h 
min 
βH−h max 
and (5) is proved.
Offline Policy Evaluation and Optimization under Confounding 
E Model-Based Method 
E.1 General Memoryless Version 
Notice that the model-based method leverages the fact that the marginalized transition dynamics are stationary. In particular, we only need Ph(s 
′ | s, a, u) and Ph(u | s) to be stationary, since this makes the marginalized transition structure stationary. In that light, we discuss here the version of the method where πb and πe are non-stationary. 
Consider the observed transition structure at timestep h, given by P̂πb 
h , denote by π̂b,h the observed behavior policy and by α̂h(s, a) and β̂h(s, a) the versions of αh(s, a) and βh(s, a) computed using π̂b,h. Let πe also be non-stationary. For the model to improve over CFQE, we still need Ph(u | s) to be the same for all timesteps h, so that the marginalized transition structure is stationary. 
Define Gh := {P : α̂h(s, a)P̂ πb 
h (s′ | s, a) ≤ P(s′ | s, a) ≤ β̂h(s, a)P̂ πb 
h (s′ | s, a), ∀s, a, s′} 
Note that in the limit of infinite data, the true marginalized transition structure satisfies the following relation for each h. 
αh(s, a)P πb 
h (s′ | s, a) ≤ P(s′ | s, a) ≤ βh(s, a)P πb 
h (s′ | s, a), ∀s, a, s′ 
So, in the limit of infinite data, the true marginalized structure lies in ∩hGh. We then define this to be G := ∩hGh even in the finite sample case. 
With this as our G, we have the same program for obtaining a model-based lower bound on the value function. 
min V1(s0),V2,...,VH ,VH+1=0,P 
V1(s0) (6) 
s.t. P ∈ G, ∑ s′ 
P(s′ | s, a) = 1 ∀s, a. 
Vh(s) = πe,h(· | s)T (Rs + PsVh+1(·)) ∀h ∈ {1, ...,H}, s 
Remark. Note that assuming stationarity of πb allows us to use data across timesteps to estimate a universal P̂πb , which helps with finite samples in practice. 
We present our proofs below for stationary πb and πe for clarity, noting that they can easily be modified for general memoryless πb and πe in a similar vein as the proofs for CFQE. 
E.2 Confidence Interval for State Transitions 
We can use the following lemma to modify our definition of the set G to use confidence intervals instead of point estimates. We show that both methods converge to the lower bound obtained with infinite data. However, using Hoeffding confidence intervals to modify G ensures that for any amount of data, the output of the model-based method is a true lower bound on the value function. In the version that uses point estimates of πb and Pπb , we only get estimates of a lower bound with finite data. 
Let N(s) and N(s, a) be the counts of s and (s, a) in the data. 
Lemma 9 (Confidence Interval for State Transitions). For ∆π := √ 
1 2N∗(s) log( 
2SA δ1 
), ∆P := √ 
1 2N∗(s,a) log( 
2S2A δ2 
), bounds αδ1(s, a) := 1/Γ − (1 − 1/Γ)(π̂b(a|s) + ∆π) and βδ1(s, a) := Γ + (1 − Γ)(π̂b(a|s) + ∆π), and N∗(s) = − logmeanexp({−N(s1), ...}), P(s′|s, a) falls between αδ1(s, a)(P̂ 
πb(s′|s, a)−∆P) and βδ1(s, a)(P̂ πb(s′|s, a) + ∆P) 
with probability at least 1− δ1 − δ2. 
Proof. We attempt to use the data collected by πb to construct a confidence interval for P̂(s′ | s, a) that also takes into account estimation error in the bounds αδ1(s, a) and βδ1(s, a). We consider below empirical estimation for P(s′ | s, a) and πb(a|s) using data collected by πb: 
P̂πb(s′ | s, a) = N(s, a, s′) 
N(s, a) , π̂b(a|s) = 
N(s, a) 
N(s) 
where N(s, a, s′) := ∑n 
i=1 1{si=s,ai=a,s′i=s′}, N(s, a) := ∑n 
i=1 1{si=s,ai=a}, and N(s) := ∑n 
i=1 1{si=s}.
Kausik, Lu, Tan, Makar, Wang, Tewari 
Note that P(s′ | s, a) = ∑ 
u P (u | s)P(s′ | s, u, a), while Pπb(s′ | s, a) = ∑ 
u Pπb(u | s, a)P(s′ | s, u, a). In πb, u and a are dependent. 
We also have: 
Pπb(s′ | s, a) = ∑ u 
Pπb(s′, u | s, a) = ∑ u 
Pπb(u | s, a)P(s′ | s, u, a) 
= ∑ u 
P (u | s)πb(a | s, u) πb(a | s) 
P(s′ | s, u, a). 
By Assumption 3, 
1 
β(s, a) P(s′ | s, a) ≤ Pπb(s′ | s, a) ≤ 1 
α(s, a) P(s′ | s, a) (7) 
α(s, a)Pπb(s′ | s, a) ≤ P(s′ | s, a) ≤ β(s, a)Pπb(s′ | s, a). (8) 
We claim that by Hoeffding’s inequality and the union bound, with probability at least 1− δ1 − δ2, 
|π̂b(a | s)− πb(s | a)| ≤ 
√ 1 
2N∗(s) log 
( 2SA 
δ1 
) = ∆π 
∣∣∣P̂πb(s′ | s, a)− Pπb(s′ | s, a) ∣∣∣ ≤√ 1 
2N∗(s, a) log 
( 2S2A 
δ2 
) = ∆P (9) 
where N∗(s) = − logmeanexp({−N(s1), ...}) and N∗(s, a) = − logmeanexp({−N(s1, a1), ...}). 
We illustrate this by showing the result for P̂πb(s′ | s, a), and the other case follows analogously. 
P(∃s′, s, a s.t. |P̂πb(s′ | s, a)− Pπb(s′ | s, a)| ≤ ϵ) ≤ ∑ s′,s,a 
P(|P̂πb(s′ | s, a)− Pπb(s′ | s, a)| ≤ ϵ) 
≤ ∑ s′,s,a 
2 exp{−2ϵ2N(s, a)} 
= S ∑ s,a 
2 exp{−2ϵ2N(s, a)} 
≤ 2S2A exp{−2ϵ2N∗(s, a)} = δ 
for some N∗ that satisfies the last inequality above. Various choices for N∗ exist. Perhaps the most obvious choice is the min function, though it can be shown that − logmeanexp(−x) is optimal, as: 
x∗ s.t. ∑ n 
eXn = nex ∗ ⇐⇒ ex 
∗ = 
1 
n 
∑ n 
eXn ⇐⇒ logmeanexp(X1, ..., Xn) = x∗ 
The logmeanexp function returns a value between the maximum and the mean, and in our case, we use it to obtain a soft approximation to the minimum that provides a less conservative bound than using the minimum of counts over all states (or states and actions). 
Combining our inequalities 9 and 8 with the definitions of α(s, a) and β(s, a), we have our result. 
E.3 Solving (1) Gives Better Lower Bound than Confounded FQE, Proof of Theorem 4 Recall Theorem 4 below. 
Theorem 4 (Error for the Model-Based Method). Suppose Γ = 1+ε in Assumption 3. Then the value estimation from solving (1) with infinite data, denoted by Ṽ1, provides a lower bound no looser than CFQE and satisfies that |V πe 
1 (s0)− Ṽ1(s0)| = O(εH2) for any range of ε.
Offline Policy Evaluation and Optimization under Confounding 
We consider the infinite sample setting, which means: 
G = {P : α(s, a) ≤ P(s′ | s, a) Pπb(s′ | s, a) 
≤ β(s, a), for ∀s, a, s′} 
The key to the proof is the observation that we can always get a valid gh from a valid P ∈ G by setting gh(s, a, s 
′) := P(s′|s,a) Pπb (s′|s,a)πb(a|s) , which formalizes the intuition that the uncertainty set G for P is tighter. Since we 
are in the stationary case, we drop all unnecessary h in subscripts. 
Proof. We denote the solution of (1) in the infinite-sample setting by Ṽ1, . . . , ṼH , ṼH+1, P̃. We will show that Ṽ1 
gives a lower bound on the true value function that is larger than the lower bound given by CFQE. That is, if the iterates of CFQE are f̂h(s, a), then 
∑ a πe(a | s)f̂1(s, a) ≤ Ṽ1(s) ≤ V πe 
1 (s). Combining this with Theorem 3 gives us the whole theorem. 
First note that in the infinite data setting, the marginalized transition kernel lies in G, so the optimization problem minimizes V1 over values of P that include the true marginalized transition structure. Thus, we trivially get that Ṽ1(s) ≤ V πe 
1 (s). 
We now prove that Vh(s) ≥ ∑ 
a πe(a | s)f̂h(s, a) holds for all h by induction. Note that the argument below also works for the finite-sample case by merely replacing every quantity associated with πb (such as Pπb) by its finite sample version. 
For h = H + 1: 
ṼH+1(s) = 0 ≥ 0 = ∑ a 
πe(a | s)f̂H+1(s, a) 
Suppose we have Ṽh+1(s) ≥ ∑ 
a πe(a | s)f̂h+1(s, a). Then for step h: 
Ṽh(s) = ∑ a 
πe(a | s) 
[ R(s, a) + 
∑ s′ 
P̃(s′ | s, a)Ṽh+1(s ′) 
] 
f̂h(s, a) = min g∈B̃sa 
∑ u,s′ 
Pπb(s′, u | s, a)CFQE(f̂h+1, g) 
 ≤ ∑ u,s′ 
Pπb(s′, u | s, a) P̃(s′ | s, a) Pπb(s′ | s, a) 
[ R(s, a) + 
∑ a′ 
πe(a ′ | s′)f̂h+1(s 
′, a′) 
] 
= ∑ s′ 
P̃(s′ | s, a) 
[ R(s, a) + 
∑ a′ 
πe(a ′ | s′)f̂h+1(s 
′, a′) 
] ≤ R(s, a) + 
∑ s′ 
P̃(s′ | s, a)Ṽh+1(s ′). 
where 
CFQE(f̂h+1, g) := 
(∑ s′ 
πb(a | s)g(s, a, s′) 
[ R(s, a) + 
∑ a′ 
πe(a ′ | s′)f̂h+1(s 
′, a′) 
]) 
The first inequality in above is achieved by setting g(s, a, s′) = P̃(s′|s,a) Pπb (s′|s,a)πb(a|s) . It’s easy to check that by 
this choice, g(s, a, ·) ∈ B̃sa by (8). The second inequality is by the induction hypothesis. Thus, we have Ṽh(s) ≥ 
∑ a πe(a | s)f̂h(s, a). 
By induction, Ṽ1(s) ≥ ∑ 
a πe(a | s)f̂1(s, a), which means the lower bound provided by (1) is always no worse than confounded FQE (Alg. 3).
Kausik, Lu, Tan, Makar, Wang, Tewari 
E.4 Worst-Case Error for the Model-Based Method, An Independent Alternative Proof In this section, we give an alternative proof of the fact that the output of (1) satisfies |V πe 
1 (s)− Ṽ1| = O(εH2) for Γ = 1 + ε without comparing to CFQE. Again, recall that we consider the infinite sample setting, which means the following. 
G = {P : α(s, a) ≤ P(s′ | s, a) Pπb(s′ | s, a) 
≤ β(s, a), for ∀s, a, s′} 
Proof. By definition, we know V πe 
H (s) = ṼH(s) for all s. We define δh = maxs |V πe 
h (s)− Ṽh(s)|. Note that δH = 0. Next, consider |V πe 
h (s)− Ṽh(s)|: 
δh := max s |V πe 
h (s)− Ṽh(s)| 
= max s | ∑ a 
πe(a | s) ∑ s′ 
P(s′ | s, a)Vh+1(s ′)− 
∑ a 
πe(a | s) ∑ s′ 
P̃(s′ | s, a)Ṽh+1(s ′)| 
≤ max s | ∑ a 
πe(a | s) ∑ s′ 
P(s′ | s, a)Vh+1(s ′)− 
∑ a 
πe(a | s) ∑ s′ 
P̃(s′ | s, a)Vh+1(s ′)| 
+max s | ∑ a 
πe(a | s) ∑ s′ 
P̃(s′ | s, a)Vh+1(s ′)− 
∑ a 
πe(a | s) ∑ s′ 
P̃(s′ | s, a)Ṽh+1(s ′)| 
= max s | ∑ a 
πe(a | s) ∑ s′ 
P(s′ | s, a)Vh+1(s ′)− 
∑ a 
πe(a | s) ∑ s′ 
P̃(s′ | s, a)Vh+1(s ′)| 
+ δh+1 
≤ (βmax − αmin)(H − h) + δh+1, 
where βmax := max 
s,a Γ + πb(a | s)(1− Γ) ≤ 1 + ε 
and αmin := min 
πb(a|s) 
ε 
1 + ε πb(a | s) + 
1 
1 + ε ≥ 1 
1 + ε 
It is easy to check βmax − αmin = ε + ε 1+ε = O(ε) (ignoring higher order terms of ε). So, we get that 
δh ≤ O(ε(H − h)) + δh+1 from h = 1, . . . ,H. So, we have that 
δ1 ≤ O(εH2) 
E.5 Consistency of the Model-Based Method We first prove this extremely elementary and useful geometric lemma. 
Lemma 10. If a function f : X → R on a Hausdorff metric space X is continuous (resp. Lipschitz), then fmin : Comp(X) → R given by fmin(K) := infx∈K f(x) is also continuous (resp. Lipschitz) in the Hausdorff metric on the space Comp(X) of compact subsets of X. The same holds for fmax(K) := supx∈K f(x). 
Proof. We prove this for α-Lipschitz f and fmin, the other cases are similar. Consider compact sets K1 and K2, so that the infima are attained at xi ∈ Ki. This means that fmin(Ki) = f(xi). Since Kj are closed, we have points uj that attain the closest distance from xi to Kj . Combining these, we know that 
d(xi,Kj) ≤ dHaus(Ki,Kj) 
and d(xi, uj) = d(xi,Kj) := infu∈Kjd(xi, u) 
Using the Lipschitzness of f , 
|f(xi)− f(uj)| ≤ αd(xi, uj) ≤ αdHaus(Ki,Kj)
Offline Policy Evaluation and Optimization under Confounding 
Also, f(uj) ≥ f(xj) by definition of xj , since uj ∈ Kj and xj minimizes f over Kj . So, 
f(xi) ≥ f(uj)− αdHaus(Ki,Kj) ≥ f(xj)− αdHaus(Ki,Kj) 
This holds for (i, j) = (1, 2), (2, 1), so we get that 
|fmin(Ki)− fmin(Kj)| = |f(xi)− f(xj)| ≤ αdHaus(Ki,Kj) 
We use Lemma 10 along with the fact that the objective function is Lipschitz. We will prove it for the version of the Model-Based method incorporating Hoeffding-based bounds (which are incorporated to give finite sample guarantees). The proof for the version with point estimates of the relevant quantities is in fact easier and subsumed by this by setting ∆π = ∆P = 0. We first need the lemma below, which will we later combine with Lemma 10. 
Lemma 11. Let the feasible region given by the values of Pπb , α(s, a) and β(s, a) in the limit of infinite data be 
F . Let the feasible region obtained using our finite sample estimates in Lemma 9 be F̂ . Then there is a constant K depending on Γ so that 
dHaus(F, F̂ ) ≤ 2S2AΓ ( |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ |πb(s | a)− π̂b(s | a)|+∆P +∆π 
) Notice that this also applies to the case of replacing the Hoeffding-based intervals by the point estimates, since that merely involves replacing ∆π and/or ∆P by 0. 
Proof. Notice that the condition ∑ s′ 
P(s′ | s, a) = 1 
is identical across both sets, so the difference is only induced by the infinite-sample G∞ and the finite sample G. That is, for P ∈ G∞, we have the following 
α(s, a)Pπb(s′|s, a) ≤ P(s′ | s, a) ≤ β(s, a)Pπb(s′|s, a) 
Let’s call the interval above Is,a. For P ∈ G, we instead have 
αδ1(s, a)(P̂ πb(s′|s, a)−∆P) ≤ P(s′ | s, a) ≤ βδ1(s, a)(P̂ 
πb(s′|s, a) + ∆P) 
We can check that using the inequalities above, the following hold for ŵ ∈ F̂ : 
 If ŵs′,s,a < α(s, a)Pπb(s′ | s, a), then 
d(ŵs′,s,a, Is,a) 
≤ α(s, a)|Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ α(s, a)∆P 
+ (P̂πb(s′ | s, a) + ∆P)|α(s, a)− αδ1(S, a)| 
≤ |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+∆P + 2 
( 1− 1 
Γ 
) (|πb(s | a)− π̂b(s | a)|+∆π) 
≤ |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+K1|πb(s | a)− π̂b(s | a)|+∆P +K1∆π 
where K1 = 2 ( 1− 1 
Γ 
) . 
 If ŵs′,s,a > β(s, a)Pπb(s′ | s, a) then we get terms using β, so that we have 
d(ŵs′,s,a, Is,a) ≤ K3|Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+K2|πb(s | a)− π̂b(s | a)|+K3∆P +K2∆π 
with K2 = 2(Γ− 1) and K3 = Γ 
 In the third case, ŵs′,s,a ∈ Is,a, so d(ŵs′,s,a, Is,a) = 0
Kausik, Lu, Tan, Makar, Wang, Tewari 
Combining these and noting that 2Γ ≥ K1,K2,K3, we have that 
d(ŵs′,s,a, Is,a) ≤ 2Γ(|Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ |πb(s | a)− π̂b(s | a)|+∆P +∆π) 
This means that by the triangle inequality, for any matrix/vector norm on RS2A, 
d(ŵ, F ) = d(ŵ, ∏ s′,s,a 
Is,a) ≤ S2Amax s′,s,a 
d(ŵs′,s,a, Is,a) 
≤ 2S2AΓ ( |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ |πb(s | a)− π̂b(s | a)|+∆P +∆π 
) Since ŵ ∈ F̂ is arbitrary, 
dHaus(F, F̂ ) ≤ 2S2AΓ ( |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ |πb(s | a)− π̂b(s | a)|+∆P +∆π 
) 
We finally recall and prove our consistency result below. 
Theorem 5 (Consistent Estimation of the Lower Bound). The estimated lower bound from the model-based method is strongly consistent for the lower bound Ṽ1, where Ṽ1 is the lower bound estimate of the value function from solving (1) with infinite data. That is, V̂1 
a.s.→ Ṽ1. 
Proof. To remind the reader of the precise sense in which "limit of infinite data" is used here, we mean that the behavior policy is exploratory, so that every s, a has a non-zero probability of occurring in the trajectory. In particular N(s), N(s, a)→∞ as we observe infinitely many trajectories. 
We know that our objective function is a polynomial in the entries of w = P(· | ·, ·). Since the entries of w lie in [0, 1], the domain of our multivariate polynomial is compact and it is thus Lipschitz, since it is C1. Let its Lipschitz constant be α. Call the minimum in the infinite data case Ṽ1 and the one in the finite sample case V̂1. Combining Lemma 11 with Lemma 10, we get that 
|Ṽ1 − V̂1| ≤ αdHaus(F, F̂ ) 
≤ 2αS2AΓ ( |Pπb(s′ | s, a)− P̂πb(s′ | s, a)|+ |πb(s | a)− π̂b(s | a)|+∆P +∆π 
) Note that as N(s), N(s, a) → ∞, |Pπb(s′ | s, a) − P̂πb(s′ | s, a)|, |πb(s | a) − π̂b(s | a)| → 0 almost surely, and ∆P,∆π → 0. This implies that as N(s), N(s, a)→∞, |Ṽ1 − V̂1| → 0 almost surely.
Offline Policy Evaluation and Optimization under Confounding 
F Relaxation of the Model-Based Method F.1 Relaxation of (1) Recall that in (1), we solved a non-convex optimization problem with H · |S|+ 1 Bellman backup constraints. If one were to not require the P(s′|s, a) to stay constant at every step, one could sequentially solve H · |S|+ 1 convex programs to obtain a lower bound that is looser than one obtained by (1). Gh is as defined in Appendix E. Computationally, to compute policy values for each starting state, confounded FQE (Alg. 3) solves (H+1) · |S| · |A| linear programs, while Alg. 4 below solves (H + 1) · |S| convex programs. 
Algorithm 4 Relaxation of Model-Based Method 1: input: evaluation policy πe, starting state s0. 2: initialize: VH+1 ← 0. 3: for h = H,H − 1, . . . , 1 do 4: 
Vh(s) := min Ph∈Gh 
∑ a 
πe,h(a | s) 
[ R(s, a) + 
∑ s′ 
Ph(s ′ | s, a)Vh+1(s 
′) 
] = min 
Ph∈Gh 
πe,h(· | s)T (Rs + Ps,hVh+1(·)). 
5: end for 6: return V1(s0) 
Notice that this is similar to confounded FQE (Alg. 3) in that it optimizes over Ph(s ′|s, a) at each step, instead of 
requiring it to stay constant for all h = 1, ...H. Consider the bijection gh(s, a, s ′)↔ Ph(s 
′|s,a) P̂ πb h (s′|s,a)π̂b,h(a|s) 
between 
the uncertainty sets ∏ 
h B̃sa,h and ∏ 
h Gh for g1, . . . gH and P1, . . . ,PH respectively. It is easy to check using the definitions of the sets that this is truly a bijection. We can see using this bijection and with an argument similar to the proof of Theorem 4, that the value estimates from this relaxation and CFQE are equal at each step. By the remark made in the proof of Theorem 4, this also holds for the finite sample versions. 
F.2 Projected Gradient Descent In a similar vein to Algorithm 4.1 in Kallus and Zhou (2020), we provide a method to efficiently compute the lower bound with projected gradient descent. 
Given an estimate of P, the corresponding estimate of V1(s0) can be obtained by iteratively performing H + 1 Bellman backups, each of which is dependent on P itself. Each Bellman backup is obtained by translations and matrix multiplications of P. As such, V1(s0) is differentiable with respect to P, and the gradient ∇PV1(s0) can be easily obtained with modern autograd tools. 
Algorithm 5 Projected Gradient Descent for Model-Based Lower Bound 1: input: evaluation policy πe, empirical estimate of P, decaying learning rate ηt, starting state s0. 2: initialize: VH+1 ← 0. 3: for t = 1, ..., N do 4: for h = H,H − 1, . . . , 1 do 5: 
Vh(s) := ∑ a 
πe(a | s) 
[ R(s, a) + 
∑ s′ 
P(s′ | s, a)Vh+1(s ′) 
] = πe(· | s)T (Rs + PsVh+1(·)). 
6: end for 7: P← ProjG(P− ηt∇PV1(s0)) 8: end for 9: return the lowest V1(s0) encountered.
Kausik, Lu, Tan, Makar, Wang, Tewari 
G FQE Does Not Work for Confounders with Memory We recall Theorem 6 below. 
Theorem 6 (Lower Bound for Confounders with Memory). There exists an MDP M having confounders with memory, a stationary unconfounded behavior policy πb with sensitivity Γ = 1, a stationary evaluation policy πe 
with πe(a|s) πb(a|s) ≤ 2 ∀s, a, and a state s1, so that V πe 
1 (s1) = Ω(H) while the output of FQE for πe is O(logH), even with infinite data. 
Proof. We demonstrate that there exists a confounded MDP with non-memoryless confounders and a behavior policy πe where even under the limit of infinite data, if the estimate obtained using FQE is f̂1(s, a) and the true value function is V πe 
1 (s), then V πe 1 (s)− 
∑ a πe(a | s)f̂1(s, a) = O(H). 
Environment: 
 Consider S = {s1, s2}, A = {a1, a2}, U = {u0, ua1}, horizon H. 
 Rewards: r(s = s1, a1) = 1, otherwise 0 reward. 
 Starting state: Let the starting state be s1. 
Confounder distribution: The confounder’s distribution starts at ua1 and is induced by confounder transitions 
with memory. Specifically, consider the following confounder transitions. 
 If u = ua1 and the current action is a1, stay in ua1 . 
 In all other cases, transition to u0. 
State transitions: P(s1 | s, a1, ua1 ) = 1 for any s, and for all other s, a, u, we have that P(s1 | s, a, u) = 1/H 
and P(s2 | s, a, u) = 1− 1/H 
Behavior policy: Let πb(a | s, u) = 1 2 for any s, a, u. 
Evaluation policy: Let πe(a1 | s) = 1. 
Policy values: Notice that in the evaluation policy, we are always in ua1 and always take action a1, so we are 
always in state s1. Thus the reward at each step is 1 and V πe 1 (s1) = H. 
FQE Output: First note that to iterate through FQE for πe, we need only compute f̂h(s, a1) for all s, h. Notice that under the behaviour policy, at timestep h, Pπb,h(ua1 
) = 1 2h−1 and Pπb,h(u0) = 1 − 1 
2h−1 . We start with f̂H+1(s, a) := 0 and the update rule is given by 
f̂h(s, a) = E(s,a,s′)∈Dπb,h [r(s, a) + 
∑ a′ 
πe(a ′ | s′)f̂h+1(s 
′, a′)] 
= E(s,a,s′)∈Dπb,h [r(s, a) + f̂h+1(s 
′, a1)] 
= r(s, a) + ∑ s′,u 
Pπb,h(s ′, u | s, a)f̂h+1(s 
′, a1) 
= r(s, a) + ∑ s′,u 
P(s′ | s, a, u)Pπb,h(u | s, a)f̂h+1(s ′, a1) 
Note that for u = u0, ua1 
Pπb,h(u | s, a) = Pπb,h(s, a | u)Pπb,h(u) 
Pπb,h(s, a | u0)Pπb,h(u0) + Pπb,h(s, a | ua1 )Pπb,h(ua1 
) 
For s = s2, P(s2, a | ua1 ) = 0, so P(ua1 
| s2, a) = 0. On the other hand, for s1, a1, we have the following. 
Pπb,h(ua1 | s1, a1) = 
1 2h−1 
1 2H 
( 1− 1 
2h−1 
) + 1 
2h−1 
≤ min 
( 1, 
2H 
2h−1 
)
Offline Policy Evaluation and Optimization under Confounding 
Thus, Pπb,h(u0 | s1, a1) ≥ 1− 2H 2h−1 
Thus, for s1, a1, the update rule is given by 
f̂h(s1, a1) = 1 + 1 
H Pπb,h(u0 | s1, a1)f̂h+1(s1, a1) + 
( 1− 1 
H 
) Pπb,h(u0 | s1, a1)f̂h+1(s2, a1) 
+ Pπb,h(ua1 | s1, a1)f̂h+1(s1, a1) 
≤ 1 + 
( 1 
H +min 
( 1, 
2H 
2h−1 
)) f̂h+1(s1, a1) + 
( 1− 1 
H 
) f̂h+1(s2, a1) 
For s2, it is given by 
f̂h(s2, a1) = 1 + 1 
H Pπb,h(u0 | s1, a1)f̂h+1(s1, a1) + 
( 1− 1 
H 
) Pπb,h(u0 | s1, a1)f̂h+1(s2, a1) 
+ Pπb,h(ua1 | s1, a1)f̂h+1(s1, a1) 
= 1 
H f̂h+1(s1, a1) + 
( 1− 1 
H 
) f̂h+1(s2, a1) 
We can use these to perform a straightforward but tedious calculation and inductively verify that for h ≥ 2 log(H) + 6, f̂h(s1, a1) ≤ 1 + 2H−2h 
H and f̂h(s2, a1) ≤ 2H−2h H . Induction starts at h = H and works backwards. 
For h ≤ 2 log(H) + 6, we use the simple upper bounds on the FQE recursion. 
f̂h(s1, a1) ≤ 1 + max(f̂h+1(s1, a1), f̂h+1(s2, a1)) 
f̂h(s2, a1) ≤ max(f̂h+1(s1, a1), f̂h+1(s2, a1)) 
In particular, max(f̂h(s1, a1), f̂h(s2, a1)) ≤ 1 + max(f̂h+1(s1, a1), f̂h+1(s2, a1)) 
This gives us the following relation. 
f̂1(s1, a1) ≤ max(f̂1(s1, a1), f̂1(s2, a1)) ≤ (2 logH + 6) + 1 + 2(H − (2 logH + 6)) 
H ≤ 2 logH + 9 
In particular, FQE gives an underestimate of the value and its estimation error is 
V πe 1 (s1)− 
∑ a 
πe(a | s)f̂1(s1, a) = O(H)
Kausik, Lu, Tan, Makar, Wang, Tewari 
H Proof of Consistency for Clustering OPE, Theorem 7 We first rephrase the end-to-end clustering guarantee from Kausik et al. (2022) in our context. 
Theorem. Under Assumptions 2, 4, and 5, there are constants H0, N0 depending polynomially on 1 α ,∆, 1 
minu P (u) , log(1/δ), so that for n ≥ U2SN0 log(1/δ) trajectories of length H ≥ H0tmix log(n), we recover all clusters of trajectories exactly with probability at least 1− δ. 
We now recall Theorem 7. 
Theorem 7 (Sample Complexity for OPE under Global Confounding). Under Assumptions 2, 4, 5, 6, there are constants H0, N0 depending polynomially on 1 
α ,∆, 1 minu P (u) , log(1/δ), so that for n trajectories of length H ≥ 
H0tmix log(n), we have that |V̂1(s0;πe)−V1(s0;πe)| < ϵ with probability at least 1−δ if n ≥ Ω(max(n1, n2, n3, n4)), where 
n1 := U2SN0 log(1/δ), n2 := log(U/δ) 
min(ϵ2/H2,minu P (u)2) 
n3 := H2τaτsSA log(U/δ) 
ϵ2 , n4 := 
τaH 
dm 
As discussed in Section 4, we prove a more general version of this, in the form of the theorem below. Assume that we instantiate Algorithm 1 with an OPE estimator that requires an assumption A(b) parameterized by a vector b and has sample complexity N2(δ, ϵ, b). 
Theorem. Under Assumptions 2, 4, 5, and A(b), there are constants H0, N0 depending polynomially on 1 α ,∆, 1 
minu P (u) , log(1/δ), so that for n trajectories of length H ≥ H0tmix log(n), we have that |V̂1(s0;πe) − V1(s0;πe)| < ϵ with probability at least 1− δ if 
n ≥ Ω 
( max 
( U2SN0 log(1/δ), 
log(U/δ) 
min(ϵ2/H2,minu P (u)2) , N2(δ/U, ϵ, b) 
)) . 
Proof. Note that V1(s0;πe) = Eu[V1(s0;u, πe)] = ∑ 
u P (u)V1(s0;u, πe). Using the clustering guarantee from Kausik et al. (2022) (rephrased above), we know that for the same H0 and N0 as in the clustering guarantee, given n ≥ N(δ) = U2SN0 log(1/δ) trajectories of length H ≥ H0tmix log(n), we recover clusters C1, ..., CU consisting of trajectories with the same confounders with probability at least 1− δ. Recall that H0 is not explicitly dependent on S,A and tmix, but could depend on the model. 
We only identify the confounder labels in each trajectory up to permutation upon obtaining exact clustering, but for any permutation σ ∈ SU , 
∑K u=1 P (u)V1(s0;Cu, πe) = 
∑U u=1 P (σ(u))V1(s0;Cσ(u), πe). That is, the result of 
the sum is independent of the order of its terms P (u)V̂1(s0;Cu, πe). So, we assume WLOG that we recover the true cluster labels. 
Upon obtaining the confounder labels un in each trajectory, we can estimate P (u) with P̂ (u) := 1 Ntraj 
∑ n 1(un = u) 
via label proportions. By a simple application of Hoeffding’s inequality, there is another function N1(δ, α) so that for n ≥ N1(δ/U, α), the weights satisfy |P̂ (u)− P (u)| ≤ α for all u with probability at least 1− δ. 
We use |ab− cd| ≤ |b||a− c|+ |c||b− d| to conclude that for n ≥ N1(δ/U, ϵ/2H), we have the following bound with probability at least 1− δ. 
|V1(s0;πe)− V̂1(s0;πe)| ≤ ϵ 
2H max u 
V̂1(s0;Cu, πe) + max u 
(P (u)|∆(u)|) ≤ ϵ 
2 + max 
u |∆(u)| (10) 
where ∆(u) := V1(s0;Cu, πe)− V̂1(s0;Cu, πe). 
So, whenever we have exact clustering, there is a function N2(δ, ϵ, b) so that |∆(u)| < ϵ for all u outside of a set of probability δ whenever 
∑ n 1(un = u) ≥ N2(δ/U, ϵ, b). By Hoeffding’s inequality from above,∑ 
n 1(un = u) ≥ n(P (u)− α) ≥ nP (u)/2 for α ≤ minu P (u)/2. 
So, for n ≥ max ( N ( δ 3 
) , N1 
( δ 3U ,min 
( ϵ 
2H , minu P (u) 2 
)) , 2 minu P (u)N2 
( δ 3U , ϵ 
2 , b )) 
, we get that |V1(s0;πe) − V̂1(s0;πe)| ≤ ϵ
Offline Policy Evaluation and Optimization under Confounding 
Note that N(δ/3) = U2SN0 log(3/δ) and N1 
( δ 3U ,min 
( ϵ 
2H , minu P (u) 2 
)) = 2 log(3U/δ) 
min(ϵ2,minu P (u)2) . This gives us our final bound.
Kausik, Lu, Tan, Makar, Wang, Tewari 
I The Necessity of the Horizon Being O(tmix) 
We showed in Section ?? that under Assumptions 2, 4, 5 and 6, Algorithm 1 provides a point estimate of the policy’s value with provable sample complexity guarantees. The only additional requirement was that H ≥ H0tmix log n. We claim that the tmix dependence is not an artifact of the clustering method used. In fact, the theorem below shows that if H ≤ Õ(tmix), clustering and value estimation can be arbitrarily bad even when tmix is small. It essentially produces an example with logarithmically small tmix where the confounders cannot be identified for H ≤ Õ(tmix). We prove it in Appendix I. We state Theorem 12 below. 
Theorem 12 (Necessity of H ≥ Ω(tmix)). There exist globally confounded MDPs M1 and M2 and a behavior policy πb with induced mixing time tmix = O(logS) so that for H ≤ Õ(tmix), trajectories from confounders in both MDPs have the same distribution. Furthermore, there exists a stationary evaluation policy πe and a starting state s so that |V πe 
1 (s,M1)− V πe 1 (s,M2)| = Ω(H). 
Proof. We construct two MDPs which satisfy all our assumptions, but have the same distribution over a horizon less than tmix and thus cannot be distinguished. We will also note that given the reward structure, under a different starting distribution, the MDPs will have value functions differing by O(H). 
The intuition is that the state space is an n-dimensional Boolean hypercube with an extra rewarding state sr, thought of as a "twin" to (1, 1, . . . 1). If one identifies sr to (1, 1, . . . 1), then a = 1 pushes states to have more ones while a = 2 pushes states to have more zeros, and the actions taken with probability 1/2 combine to produce a lazy random walk on the Boolean hypercube. Depending on which MDP one is in, sr and (1, 1, . . . 1) have proportional transition dynamics, with different levels of "traffic." Controlling this "traffic" allows us to control the rewards of a different evaluation policy in the MDPs, because we choose all states besides sr to have 0 reward. 
Environments: 
 Consider S = {0, 1}n ∪ {sr}, A = {1, 2}, U = {1, 2}, horizon H. 
 Rewards: r(s = sr, a) = 1 for any action a, otherwise 0 reward. 
 Starting state: Let the starting state be (0, 0 . . . 0). 
 Confounders: P(u = 1) = P(u = 2) = 1 2 . 
Transitions: We describe the transition structure below. Pick a parameter pi,j ∈ [0, 1] for MDP Mi and confounder u = j, whose role will be clear below. For both MDPsM1 andM2 and both confounders u = 1, 2, consider the following transition structure. 
 Under a = 1: Consider s ̸= sr, and let it have k > 1 zeros. Pick one of the zeros with probability 1 n each 
and change it to a 1, doing nothing and staying in s with probability n−k n . If s has exactly 1 zero, then for 
MDP Mi and confounder u = j, let s transition to sr with probability pi,j 
n , to (1, 1, . . . 1) with probability 1−pi,j 
n and stay at s with probability 1− 1 n . Fix p2,1 = p2,2 = 1 
2 . If s = sr, then inMi and confounder uj , move to (1, 1, . . . 1) with probability 1− pi,j , staying with probability pi,j . If s = (1, 1, . . . 1), then inMi and confounder uj , move from to sr with probability pi,j , staying with probability 1− pi,j . 
 Under a = 2: Consider s ̸= sr, and let it have k > 0 zeros. Pick one of the ones with probability 1 n each 
and change it to a zero, doing nothing and staying in s with probability k n . If s = sr, (1, 1, . . . 1), then let it 
transition to a state with a single zero with probability 1 n . 
Behavior policies: In both MDPs, choose the same policy π(a | s) = 1 2 for all a, s. One can check that the 
occupancies of sr and (1, 1, . . . 1) are only non-zero together and always have the ratio pi,j/(1− pi,j) in MDP Mi and confounder u = j. This will thus also hold in the stationary distribution. Note that while in general, identifying states in a Markov chain does not create a Markov chain, this is true if two states always have the same ratio of occupancies. Additionally, since the occupancy ratios are fixed, for any MDP and confounder in our system, the TV distance between the distribution of the system and at any time t from the stationary distribution is the same if we identified sr and (1, 1, . . . 1). Thus, this system has the same mixing time as it would if we identified sr and (1, 1, . . . 1). 
Notice that the transition structure of the induced Markov chains in both MDPs after identifying sr and (1, 1, . . . 1) is identical, and in fact it is the same as picking a bit in a state uniformly at random and flipping it with probability
Offline Policy Evaluation and Optimization under Confounding 
1/2, doing nothing otherwise. This is in fact the same as the lazy random walk on the Boolean hypercube in Levin and Peres (2017). We thus know from Levin and Peres (2017) that both induced Markov chains have the same mixing time tmix = O(n log n). Let k be a constant so that tmix ≤ kn log n. 
Observational indistinguishability: Consider H ≤ tmix 
4k log(tmix) ≤ n 
4 . Since the MDPs have identical transition structures for s ̸= sr with s having 2 or more zeros, and no state can have fewer than 2 zeros after less than n 
4 bit flips starting from the starting state (0, 0 . . . 0), trajectories generated under either MDP and either confounder have the same probability. 
In particular, the confounders are observationally indistinguishable in either MDP and cannot be clustered even with infinite observations, even though transitions differ in n+2 of the states with ∆ > max(|1−2pi,j |, |pi,1−pi,2|) > 0. Moreover, the MDPs themselves are observationally indistinguishable as well. 
Evaluation policy: One can produce many examples of an evaluation policy πe so that there is a state s with V πe 1,i (s) very different across the two MDPs. Here we present a trivial one. Consider πe(a = 1 | s, u) = 1 for all 
s, u. 
Policy values: Let us say that we intend to find V πe 1,i ((1, 1, . . . 1)). Notice that in the first step in confounder 
u = j and MDPMi, the distribution of states will be P(sr) = pi,j and P((1, 1, . . . 1)) = 1− pi,j and stays that way for all future steps. This means that V πe 
1,i ((1, 1, . . . 1)) = (∑2 
j=1 pi,j 
2 
) (H − 1) in MDP Mi. 
The difference in values is given by |V πe 1,1((1, 1, . . . 1))− V πe 
1,2((1, 1, . . . 1))| = (H − 1)(p1,1 + p1,2 − p2,1 − p2,2). We arbitrarily instantiate our parameters to be say p1,1 = 1− 1 
100 , p1,2 = 1− 2 100 , p2,1 = − 1 
100 , p2,2 = 2 100 , to get that 
|V πe 1,1((1, 1, . . . 1))− V πe 
1,2((1, 1, . . . 1))| = 94 
100 (H − 1) = Ω(H)
Kausik, Lu, Tan, Makar, Wang, Tewari 
J Policy Optimization under General and Memoryless Confounders J.1 Bounds on Sub-optimality given Optimization Oracles Here, we elaborate on the comment at the beginning of Section 5, where we claim that given error bounds on our value estimate V̂1 and an optimizer for V̂1, we can get suboptimality bounds for the output of the optimizer. Notice the slight change in notation below. 
Lemma 13. Fix an arbitrary starting distribution d0. If for any policy π, |V̂1(π) − V1(π)| ≤ ϵ, then for π̂∗ = argmaxπ V̂1(π) and π∗ = argmaxπ V1(π), we have that 0 ≤ V1(π 
∗)− V1(π̂∗) ≤ 2ϵ. 
Proof. Consider the following chain of inequalities. 
V1(π ∗)− V1(π̂ 
∗) 
= V1(π ∗)− V̂1(π 
∗) + V̂1(π ∗)− V̂1(π̂ 
∗) + V̂1(π̂ ∗)− V1(π̂ 
∗) 
≤ ϵ+ 0 + ϵ 
Here, the first part of the last inequality holds by our assumption applied to π = π∗, while the second part holds by the definition of π̂∗ as the optimal policy for V̂1. The third part holds by applying our assumption to π = π∗. 
Finally, by the definition of π∗ as the optimal policy for V1, V1(π ∗)− V1(π̂∗) ≥ 0. Combining these, we have our 
results. 
J.2 Gradient Ascent on the Lower Bound 
Algorithm 6 Gradient Ascent on Differentiable Lower Bounds for Policy Improvement under Confounding 1: input: decaying learning rate ηt, πθ. 2: for t = 1, ..., N do 3: run subroutine: obtain differentiable lower bound V1(s0;πθ) on πθ via Alg. 5, Alg. 4, or Alg. 3 4: update: θ ← θ + ηt · ∇θV1(s0;πθ) 5: end for 6: return πθ 
This enjoys the following elementary local convergence guarantees. 
Lemma 14. If ∇θV1(s0;πθ,P) and ∇PV1(s0;πθ,P) are Lipschitz, every local max-min is a gradient ascent/descent stable point. 
Lemma 15. If V1(s0;πθ,P) is twice differentiable with a Lipschitz continuous gradient, its saddle points are a strict-saddle, and one waits for the inner minimization to converge in each iteration, in the limit of infinite trajectories the procedure converges to a local maxima of V1(s0;πθ,P). 
The first result follows from Section 2 in Daskalakis and Panageas (2018), given the knowledge that V1(s0;πθ,P), being constructed from translations and matrix multiplications, is smooth, and therefore so are its gradients. The second result follows from Lee et al. (2016).
Offline Policy Evaluation and Optimization under Confounding 
K Policy Optimization under Global Confounders 
Algorithm 7 Clustering-Based Policy Gradient 1: input: Number of clusters U , clustering algorithm cluster(), offline policy gradient estimator gradient(), 
learning rate η, initial policy parameters θ0. 2: run subroutine: Perform clustering on trajectories with clustering algorithm cluster(), obtain clusters 
C1, ..., CK . 3: Obtain cluster weight estimates P̂ (u) := |Cu| 
Ntraj . 
4: for t = 1, ..., T : do 5: run subroutine: Use offline policy gradient estimator gradient() to estimate Zi(θt) = ∇θV1(s0;ui, πθt) 
for each cluster Ci, obtaining Ẑi(θt). 6: Obtain gradient estimate of Z(θt) = ∇θV1(s0;πθt) with Ẑ(θt) = 
∑U u=1 P̂ (ui)Ẑi(θt). 
7: Update θt+1 := θt − ηẐ(θt). 8: end for 9: return: Output the final policy πθT+1 
. 
We now recall Theorem 8 below. We remind the reader that like Theorem 7, the theorem below holds when H ≥ H0tmix log n. 
Theorem 8. Let us have large enough β > 1 and T = nβ, for n ≥ Ω ( max 
( U2SN0 log(1/δ), 
log(U/δ) minu P (u)2 
)) . 
Also let H ≥ H0tmix log n, for H0, N0 as in Theorem 7. Then we have that 1 T 
∑T t=1 ||∇θV1(s0;πθt)||2 = 
O(max(ϵMSE , ϵfreq), where ϵMSE = H4 log(nU/δ) nminu P (u) , and ϵfreq = L2 log(U/δ) 
n 
To prove this, we first provide a high-probability guarantee for the overall gradient estimate across all clusters analogous to that of Theorem 7 for OPE. This is proved in Section K.1. 
Theorem 16. When Assumptions 2, 4, 5 and 6 are satisfied, there are constants H0, N0 depending polynomially on 1 
α ,∆, 1 minu P (u) , log(1/δ), so that for n trajectories of length H ≥ H0tmix log(n), if we use the EOPPG offline 
policy gradient estimator from Kallus and Uehara (2020), 
n ≥ max 
( U2SN0 log(3/δ), 
8 log(6U/δ) 
min{ϵ2/L2,minu P (u)2} , 
C 
minu P (u) 
H4 log(nU/δ) 
ϵ2 
) 
then ||Z(θ)− Ẑ(θ)|| ≤ ϵ with probability 1− δ for some constant C. 
The following result for the convergence of unconstrained gradient descent is effectively Theorem 11 in Kallus and Uehara (2020), combined with the bound in Theorem 16. We repeat the proof in Section K.2 for completeness. 
Theorem 17. Assume V1(s0;u, πθ) and V1(s0;πθ) are differentiable and M -smooth in θ for all u ∈ U , and the learning rate η < 1 
4M . Then, if the number of trajectories n satisfies the condition in Theorem 16, the iterates θt from Algorithm 7 offer 
1 
T 
T∑ t=1 
||∇θZ(θt)||2 = 1 
T 
T∑ t=1 
||∇θV1(s0;πθt)||2 ≤ 4 
ηT (V1(s0;πθ∗)− V1(s0;πθ1)) + 3ϵ2 
The result of Theorem 8 then follows immediately from the two results above. The only additional observation needed is that since V1 is Lipschitz, it is bounded in a compact domain and so the first term in Theorem 17 is O(1/nβ) ≤ O(1/n). 
Another Formulation of Policy Optimization Notice that the nature of the global confounder assumption permits another kind of policy optimization. One can optimize U different policies, one for each value of the confounder, with standard off-policy improvement methods. To deploy them, one will have to identify the confounder online, which is a nontrivial problem in itself. One avenue is to first deploy each of the U behavior policy components in any order for O(tmix) time each, and then attempt to identify the confounder using the classification algorithm in Kausik et al. (2022). If the classification algorithm successfully classifies trajectories
Kausik, Lu, Tan, Makar, Wang, Tewari 
generated in this way, we can achieve the optimal reward thereafter by deploying the optimal policy for the confounder in question. 
K.1 Proof of Theorem 16 
Proof. Note that ∇θV1(s0;πθ) = Eu[∇θV1(s0;u, πθ)] = ∑ 
u P (u)∇θV1(s0;u, πθ). 
Using the clustering guarantee from Kausik et al. (2022) rephrased in Section H, we know that there are numbers N0 and H0 so that given n ≥ U2SN0 log(1/δ) trajectories of length H ≥ H0tmix log(n), we recover clusters C1, ..., CU consisting of trajectories with the same confounders with probability at least 1− δ. Recall that N0 
and H0 are not explicitly dependent on S,A and tmix, but could depend on the model. 
Write Z(θ) = ∇θV1(s0;πθ), Zi(θ) = ∇θV1(s0;ui, πθ) and Ẑi(θ) for the estimate of Zi(θ) and Ẑ(θ) =∑U i=1 P̂ (ui)Ẑi(θ) for the estimate of Z(θ). We only identify the confounder labels in each trajectory up to 
permutation upon obtaining exact clustering, but as above we assume WLOG that we recover the true cluster labels. 
Estimate P (u) with P̂ (u) := 1 Ntraj 
∑ n 1(un = u) via label proportions. By a simple application of Hoeffding’s 
inequality and the union bound, for n ≥ 2 log(2U/δ) α2 , the weights satisfy |P̂ (u) − P (u)| ≤ α with probability at 
least 1− δ. 
We can then bound 
||Z(θ)− Ẑ(θ)|| = 
∥∥∥∥∥ U∑ i=1 
( P (ui)Zi(θ)− P̂ (ui)Ẑi(θ) 
)∥∥∥∥∥ (11) 
= 
U∑ i=1 
∥∥∥P (ui)Zi(θ)− P̂ (ui)Ẑi(θ) ∥∥∥ (12) 
≤ U∑ i=1 
||Zi(θ)||(P (ui)− P̂ (ui)) + P̂ (ui)||Zi(θ)− Ẑi(θ)|| (13) 
= 
U∑ i=1 
||Zi(θ)||(P (ui)− P̂ (ui)) + 
U∑ i=1 
P̂ (ui)||Zi(θ)− Ẑi(θ)|| (14) 
≤ α 
U∑ i=1 
||Zi(θ)||+ U∑ i=1 
P̂ (ui)||Zi(θ)− Ẑi(θ)|| (15) 
≤ α 
U∑ i=1 
||Zi(θ)||+ U∑ i=1 
2P (ui)||Zi(θ)− Ẑi(θ)|| (16) 
where the second inequality holds with high probability and the last inequality holds for sufficiently small α. If all ||Zi(θ)− Ẑi(θ)|| ≤ ϵ/4 for some ϵ > 0, then we would have ||Z(θ)− Ẑ(θ)|| ≤ 
∑U i=1 2P (ui)||Zi(θ)− Ẑi(θ)|| ≤ ϵ/2. 
It remains to bound the error of each Ẑi. Notice that the result of Theorem 7 in Kallus and Uehara (2020) is independent of the gradient update rule or the value of θ and only depends on the number of samples used to estimate ẐEOPPG. So, it also holds for Ẑi with ni samples. Additionally, note that the proof of Theorem 12 in Kallus and Uehara (2020) only uses the supremum of the error over all possible values of θ and does not use any facts about the gradient update, it follows verbatim for Ẑi with ni samples. In particular, with probability at least 1− δ/U , 
∥Zi(θ)− Ẑi(θ)∥2 ≤ O 
( H4 log(TU/δ) 
ni 
) 
and so for T = nβ , we need ni ≥ Ω ( 
H4 log(nU/δ) ϵ2 
) trajectories for ||Zi(θ) − Ẑi(θ)|| ≤ ϵ to hold for all ui with 
probability 1− δ. To convert this into a bound for n, we use Hoeffding’s inequality from above in a similar way to the previous proof to find ni = 
∑ n 1(un = u) ≥ n(P (u)− α) ≥ nP (u)/2 for α ≤ minu P (u)/2. We therefore 
need n ≥ Ω ( 
1 minu P (u) 
H4 log(nU/δ) ϵ2 
) for the error of each Zi to be bounded by ϵ with probability 1− δ.
Offline Policy Evaluation and Optimization under Confounding 
We then bound α ∑U 
i=1 ||Zi(θ)|| ≤ ϵ/2. Let L be a uniform bound over θ ∈ Θ on the magnitude of the gradients Z(θ) (in the continuous case, this corresponds to a Lipschitz-type assumption on the value functions). It then suffices to require α ≤ ϵ 
2L . 
Splitting the failure probability into δ/3, requiring α ≤ minu P (u)/2, ϵ/2L, and bounding the error of each Zi by ϵ/4, we get ||Z(θ)− Ẑ(θ)|| ≤ ϵ with probability 1− δ when 
n ≥ Ω 
( max 
( U2SN0 log(1/δ), 
log(U/δ) 
min{ϵ2/L2,minu P (u)2} , 
1 
minu P (u) 
H4 log(nU/δ) 
ϵ2 
)) (17) 
K.2 Proof of Theorem 17 Proof. The result is largely analogous to Theorem 11 from Kallus and Uehara (2020), and in fact, we can transform our problem into theirs and follow their proof. 
Assume V1(s0;u, πθ) and V1(s0;πθ) are differentiable and M -smooth in θ for all u ∈ U . Let f(θ) = −V1(s0;πθ), and fi(θ) = −V1(s0;ui, πθ) for each ui. For simplicity, fix the learning rate for all time steps to be some η < 1 
4M . By M -smoothness, 
f(θt+1) ≤ f(θt) + ⟨∇f(θt, θt+1 − θt⟩+ M 
2 ||θt+1 − θt||2. 
Define Bit = Ẑi(θ)− Zi(θ) for confounder ui, Bt = Ẑ(θ)− Z(θ), wi = P̂ (ui). Observe that 
θt+1 = θt − η∇f(θt)− ηBt = θt − η ∑ i 
∇wif(θt)− η ∑ i 
wiBit. 
Then, similarly to the proof in Kallus and Uehara (2020), 
f(θt)− f(θt+1) ≥ −⟨∇f(θt), θt+1 − θt⟩ − M 
2 ||θt+1 − θt||2 (18) 
= η⟨∇f(θt),∇f(θt)−Bt⟩ − η2M 
2 ||∇f(θt)−Bt||2 (19) 
= η||∇f(θt)||2 + η⟨∇f(θt), Bt⟩ − η2M 
2 ||∇f(θt)−Bt||2 (20) 
≥ η||∇f(θt)||2 − η|⟨∇f(θt), Bt⟩| − η2M 
2 ||∇f(θt)−Bt||2 (21) 
≥ η||∇f(θt)||2 − 0.5η(||∇f(θt)||2 + ||Bt||2)− η2M ||∇f(θt)−Bt||2 (22) 
≥ 0.25η||∇f(θt)||2 − 0.5η||Bt||2 − 0.25η||Bt||2 (23) 
where the second-last inequality uses the parallelogram law and the last inequality uses the fact that η < 1 4M . We 
then obtain 
f(θt)− f(θt+1) + 0.75η||Bt||2 ≥ 0.25η||∇f(θt)||2. 
Similarly, by a telescoping sum, 
(f(θ1)− f(θ∗))/T + 0.75η 
T 
∑ t 
||Bt||2 ≥ 0.25η 
T 
∑ t 
||∇f(θt)||2, 
(V1(s0;πθ∗)− V1(s0;πθ1))/T + 0.75η 
T 
∑ t 
||Bt||2 ≥ 0.25η 
T 
∑ t 
||∇f(θt)||2, 
η 
T 
∑ t 
||∇f(θt)||2 ≤ 4 
T (V1(s0;πθ∗)− V1(s0;πθ1)) + 
3η 
T 
∑ t 
||Bt||2,
Kausik, Lu, Tan, Makar, Wang, Tewari 
1 
T 
∑ t 
||∇f(θt)||2 ≤ 4 
ηT (V1(s0;πθ∗)− V1(s0;πθ1)) + 
3 
T 
∑ t 
||Bt||2, 
1 
T 
∑ t 
||∇f(θt)||2 ≤ 4 
ηT (V1(s0;πθ∗)− V1(s0;πθ1)) + 3max 
t ||Bt||2, 
and finally by applying Theorem 16 for an n that fulfills its conditions for some error threshold ϵ, we obtain 
1 
T 
∑ t 
||Z(θt)||2 = 1 
T 
∑ t 
||∇f(θt)||2 ≤ 4 
ηT (V1(s0;πθ∗)− V1(s0;πθ1)) + 3ϵ2.