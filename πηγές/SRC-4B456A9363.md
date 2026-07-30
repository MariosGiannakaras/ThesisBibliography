> Source: https://proceedings.mlr.press/v202/feng23e/feng23e.pdf

Non-stationary Reinforcement Learning under General Function Approximation 
Songtao Feng 1 Ming Yin 2 Ruiquan Huang 3 Yu-Xiang Wang 2 Jing Yang 3 Yingbin Liang 1 
Abstract General function approximation is a powerful tool to handle large state and action spaces in a broad range of reinforcement learning (RL) scenarios. However, theoretical understanding of non-stationary MDPs with general function approximation is still limited. In this paper, we make the first such an attempt. We first propose a new complexity metric called dynamic Bell-man Eluder (DBE) dimension for non-stationary MDPs, which subsumes majority of existing tractable RL problems in static MDPs as well as non-stationary MDPs. Based on the proposed complexity metric, we propose a novel confidence-set based model-free algorithm called SW-OPEA, which features a sliding window mechanism and a new confidence set design for non-stationary MDPs. We then establish an upper bound on the dynamic regret for the proposed algorithm, and show that SW-OPEA is provably efficient as long as the variation budget is not significantly large. We further demonstrate via examples of non-stationary linear and tabular MDPs that our algorithm performs better in small variation budget scenario than the existing UCB-type algorithms. To the best of our knowledge, this is the first dynamic regret analysis in non-stationary MDPs with general function approximation. 
1. Introduction Reinforcement learning (RL) commonly refers to the sequential decision making framework modeled by a Markov Decision Process (MDP), where agent aims to maximize its cumulative reward in an unknown environment (Sutton & Barto, 2018). RL has achieved great success in a variety of practical applications, including games (Silver et al., 2016; 2017; 2018; Vinyals et al., 2019), robotics (Kober 
1The Ohio State Univsersity 2The University of California, Santa Barbara 3The Pennsylvania State University. Correspon-dence to: Yingbin Liang <liang.889@osu.edu>. 
Proceedings of the 40 th International Conference on Machine Learning, Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright 2023 by the author(s). 
et al., 2013; Gu et al., 2017), and autonomous driving (Yurt-sever et al., 2019). So far, most existing RL works have focused on a static MDP model, in which both the reward and the transition kernel are time-invariant. However, non-stationarity1 naturally occurs in many sequential decision problems such as online advertisement auctions (Cai et al., 2017; Lu et al., 2019), traffic management (Chen et al., 2020), health-care operations (Shortreed et al., 2010), and inventory control (Agrawal & Jia, 2019). 
Compared to static RL, non-stationary RL can be significantly challenging. Under the general non-stationary environment, designing algorithm that achieve sublinear regret might not be possible due to the worst scenario where rewards and transitions change drastically over time. A line of extensive studies have focused on tabular non-stationary MDPs (Auer et al., 2008; Gajane et al., 2018; Even-Dar et al., 2009; Yu & Mannor, 2009; Yu et al., 2009; Neu et al., 2010; 2012; Zimin & Neu, 2013; Dekel & Hazan, 2013; Rosenberg & Mansour, 2019; Jin et al., 2020; Che-ung et al., 2020; Fei et al., 2020; Mao et al., 2021). How-ever, the performance of these algorithms suffers from large number of states in non-stationary MDPs, which precludes its usage in exponentially large or even continuous state spaces. Therefore, function approximation has become a prominent tool and several works proposed algorithms for non-stationary MDPs with structural assumptions, such as state-action forming a metric space (Domingues et al., 2020), linear MDPs (Zhou et al., 2022; Touati & Vincent, 2020), linear mixture MDPs (Zhong et al., 2021). However, the structural function approximation of (such as linear) MDPs typically restrict the designed algorithms to perform well only under limited classes of MDPs, and may not be applicable generally. This naturally leads to the following open question: 
Can we design an algorithm that achieves a desired regret performance for non-stationary MDPs under general function approximation? 
To this end, there are a few challenges. (a) We need to identify an appropriate complexity metric for non-stationary MDPs that covers many existing problems of interest; 
1We emphasize non-stationarity is different from timeinhomogeneity (e.g. (Yin et al., 2021)). The latter allows transition Pt to be different for t ∈ [H], but Pt’s are fixed across episodes. 
1
Non-stationary RL under General Function Approximation 
(b) We need to design an algorithm that can handle nonstationary without function structures on transition kernels and rewards to exploit; and (c) Establishing a dynamic regret bound that potentially improves those for non-stationary simpler MDPs such as linear and tabular cases is non-trivial. In this paper, we give an affirmative answer to the above question by addressing the aforementioned challenges. 
We summarize our contributions as follows. 
Complexity metric: We propose a new complexity metric named the Dynamic Bellman Eluder (DBE) dimension for non-stationary MDPs, which generalizes the Bellman Eluder (BE) dimension designed for stationary MDPs (Jin et al., 2021), and subsumes a broad class of RL problems including low BE dimension problems in stationary RL and linear MDPs in non-stationary RL. Moreover, when the nonstationarity is relatively small compared to a universal gap (which still allows a certain non-stationarity), we show that the DBE dimension is the same as the BE dimension of one MDP instance of the non-stationary MDPs. 
Algorithm: We then design a new confidence-set based algorithm SW-OPEA for non-stationary MDP, by greedily selecting the candidate value function in the confidence region. This is in contrast to the UCB-type algorithms adopted by all previous studies of non-stationary MDPs. In fact, a UCB-type algorithm is not easily applicable to non-stationary MDPs with general function approximation due to the difficulty of finding an appropriate bonus term. Our main design novelty lies in the construction of the confidence region, which features the sliding window mechanism, and incorporates local variation budget in order to exactly capture the distribution mismatch between current episode and all episodes in the sliding window. Such a design ensures the optimal state-action value function in current episode to lie within the confidence region, and hence the optimism principle remains valid. 
Theory: We theoretically characterize the dynamic regret of SW-OPEA in Theorem 5.2. To demonstrate the advantage of SW-OPEA , we compare our regret bound of SW-OPEA to that of previously proposed UCB-type algorithms (Zhou et al., 2022) for non-stationary linear and tabular MDPs. The comparison shows that our confidence-set based algorithm performs better in terms of the linear feature dimension d̃ and the horizon H , where the dependency on H also matches the minimax lower bound given in Zhou et al. (2022). Our bound is slightly worse in the average variation budget, which suggests that our algorithm is advantageous over UCB-type algorithms in the small variation scenario. 
Analysis: Technically, our analysis features a few new developments. (a) We develop a distribution shift lemma to handle transition kernel variations over time. (b) We come up with new auxiliary random variables to form appropriate 
martingale differences and obtain the concentration results. (c) We use an auxiliary MDP to help bound the difference of two expectations under different underlying models. 
1.1. Related Work 
Non-stationary tabular MDPs: Most works on nonstationary tabular MDPs considered static regret (Auer et al., 2008; Gajane et al., 2018; Even-Dar et al., 2009; Yu & Man-nor, 2009; Yu et al., 2009; Neu et al., 2010; 2012; Zimin & Neu, 2013; Dekel & Hazan, 2013; Rosenberg & Mansour, 2019; Jin et al., 2020). A few recent studies (Cheung et al., 2020; Fei et al., 2020; Mao et al., 2021) focused on dynamic regret for non-stationary tabular MDPs. Specifically, assuming time-varying transitions and rewards, Cheung et al. (2020) proposed a sliding window approach, and Mao et al. (2021) used restart mechanism to handle non-stationarity. While the first two works adopted value-based algorithms, Fei et al. (2020) applied a policy optimization algorithm for full-information feedback of rewards and time-invariant transitions. 
Non-stationary MDPs with function approximation: Un-der non-stationary MDPs with continuous environment where the state-action forms a metric space, Domingues et al. (2020) proposed a kernel-based algorithm. Two concurrent works Zhou et al. (2022) and Touati & Vincent (2020) considered non-stationary RL under linear MDPs, where Zhou et al. (2022) considered dynamic regret and Touati & Vincent (2020) studied static regret. To handle non-stationarity, Zhou et al. (2022) adopted a scheme of restarting the base LSVI-UCB algorithm while Touati & Vin-cent (2020) used weighted least squares value iteration with exponential weights on past data. Under the non-stationary MDPs with linear mixture function approximation of both transitions and rewards, Zhong et al. (2021) considered bandit feedback rewards and dynamic regret. Moreover, Wei & Luo (2021) proposed black-box reduction approach that converts algorithm with optimal regret in stationary MDPs into another algorithm for non-stationary MDPs. 
Recently, Foster et al. (2022) generalized the decisionestimation coefficient (DEC) framework to non-stationary RL setting with the goal of minimizing the static regret. Their framework can potentially cover majority problems but the connection between their result and the existing results is still not well understood. We also remark that the performance under the DEC framework is often worse than the best-known result when restricted to special cases. Further, their work focused on the static regret, whereas our work potentially maintains the sharp performance when restricting to special cases, and our performance metric of dynamic regret is more general. 
Static MDP with general function approximation: Broadly speaking, the line of research on designing sample-
2
Non-stationary RL under General Function Approximation 
efficient RL algorithms with general function approximations in the past has been mainly focused on the static RL setting. Russo & Van Roy (2013); Osband & Roy (2014) initiated the study on the minimal structural assumptions that render sample-efficient learning by proposing a structural condition called Eluder dimension, and Wang et al. (2020) then extended LSVI-UCB for general function approximation with small Eluder dimension. Another well-studied direction is the low-rank conditions, including Bellman rank (Dong et al., 2019; Jiang et al., 2017) for model-free setting and witness rank (Sun et al., 2018) for model-based setting. Jin et al. (2021) proposed a complexity named Bell-man Eluder (BE) dimension for model-free setting, which subsumes low Bellman rank and low Eluder dimension as special cases. Du et al. (2021) proposed Bilinear class, which unifies both model-based and model-free RL for a broad class of loss estimators including Bellman error. Shar-ing the same spirit of unifying model-free and model-based RL, Foster et al. (2021) proposed DEC, which is a necessary and sufficient condition for sample-efficient learning, and then they extended it to an adversarial decision making problem with static regret in Foster et al. (2022). While the sample complexity of Foster et al. (2021); Du et al. (2021) is generally worse than the best-known result when restricted to special cases, Chen et al. (2022) recently extended BE dimension and proposed an Admissible Bellman Character-ization (ABC) framework to include both model-free and model-based RL while maintaining sharp sample efficiency. Very recently, Yin et al. (2023); Zhang et al. (2022) consider parametric differentiable function approximation in offline RL, but there is no study in the online regime. 
Non-stationary bandits: Broadly speaking, our work is also related to a line of research on non-stationary bandits. Methods have been proposed to handle non-stationarity for various non-stationary multi-armed bandit (MAB) settings, including decaying memorey and sliding windows (Garivier & Moulines, 2011; Keskin & Zeevi, 2017) and restart mechanism (Auer et al., 2002; Besbes et al., 2014b;a), which are widely employed in non-stationary RL. More recently, several works developed methods for unknown variation budget (Karnin & Anava, 2016; Cheung et al., 2022), and abrupt changes (Auer et al., 2019). Another line of works focused on Markovian bandits (Ma, 2018), non-stationary contextual bandits (Luo et al., 2017; Chen et al., 2019), linear bandits (Cheung et al., 2019; Zhao et al., 2020), and bandits with slowly changing rewards (Besbes et al., 2019). 
2. Preliminaries 2.1. Non-stationary MDPs 
We consider an episodic MDP with time-varying transitions and rewards (S,A, H, P, r, x1), where S is the state space, A is the action space, H is the length of each 
episode, P = {P k h }(k,h)∈[K]×[H−1] is the collection of 
non-stationary transition kernels with P k h : S ×A 7→ △(S), 
r = {rkh}(k,h)∈[K]×[H] is the collection of adversarial deterministic reward functions with rkh : S ×A 7→ [0, 1], and x1 
is the fixed initial state. 
Suppose an agent sequentially interacts with the nonstationary MDP (S,A, H, P, r, x1). At the beginning of the k-th episode, the reward {rkh}h∈[H] are adversarially chosen by the environment, which possibly depends on the (k − 1) historical trajectories. Meanwhile, the agent determines a policy πk = {πk 
h}h∈[H] where πk h : S 7→ △(A). 
At the h-th step, the agent observes the state xk h, takes an ac-
tion following akh ∼ πk h(·|xk 
h), obtains the reward function rkh which determines the received reward rkh(x 
k h, a 
k h), and 
the MDP evolves into the next state xk h+1 ∼ P k 
h (·|xk h, a 
k h). 
The k-th episode ends after receiving the last reward rkH(xk 
H , akH). For convenience, let xH+1 be a dummy state and P k 
H(xH+1|xk H , akH) = 1 for any (xk 
H , akH) ∈ S × A. Define the state and state-action value functions of policy π = {πh}h∈[H] recursively via the following equation 
Qπ h;(∗,k)(x, a) = rkh(x, a) + (PhV 
π h+1;(∗,k))(x, a), 
V π h;(∗,k)(x) = ⟨Q 
π h;(∗,k)(x, ·), πh(·|x)⟩A, VH+1;(∗,k) = 0, 
where Ph is the operator defined as (Phf)(x, a) := E [f(x′)|x′ ∼ Ph(x 
′|x, a)] for any function f : S 7→ R. Here ⟨·, ·⟩A denotes the inner product over action space A and the subscript A is omitted when appropriate. 
The performance is measured by the dynamic regret, which quantifies the performance difference between the learning policy and the benchmark policy {π(∗,k)}k∈[K] where π(∗,k) = argmaxπ V 
π 1;(∗,k)(x1). Specifically, the dynamic 
regret for K episodes is defined as 
D− Regret(K) := ∑K 
k=1 
( V π(∗,k) 
1;(∗,k) − V πk 
1;(∗,k) 
) (x1). 
2.2. Function Approximation 
Consider a function class F = F1 × · · · × FH , where Fh ⊆ (S×A 7→ [0, H−h+1]) offers a collection of candidate functions to approximate Q 
π(∗,k) 
h;(∗,k), denoted as Q∗ h;(∗,k). 
Since each episode ends in H steps, we set fH+1 = 0. We make the following standard assumptions on the function class F . 
Assumption 2.1 (Realizability). Q∗ h;(∗,k) ∈ Fh for all 
(k, h) ∈ [K]× [H]. 
Realizability assumption requires that the optimal stateaction value function in each episode is contained in the function class F with no approximation error, i.e., (Q∗ 
1;(∗,k), Q ∗ 2;(∗,k), · · · , Q 
∗ H;(∗,k)) ∈ F for k ∈ [K]. 
Given functions f = (f1, f2, · · · , fH) where fh ∈ (S × 
3
Non-stationary RL under General Function Approximation 
A 7→ [0, H − h+ 1]), define 
(T k h fh+1)(x, a) := rkh(x, a) + (Pk 
hfh+1)(x, a), 
(Pk hfh+1)(x, a) = Ex′∼Pk 
h (·|x,a)[max a′∈A 
fh+1(x ′, a′)], 
where T k h is the Bellman operator at step h in episode k. 
Note that Q∗ h;(∗,k)(x, a) = (T k 
h Q∗ h+1;(∗,k))(x, a) for all 
valid x, a, h. Moreover, we define T k h Fh+1 = {T k 
h fh+1 : fh+1 ∈ Fh+1}. Assumption 2.2 (Completeness). T k 
h Fh+1 ⊆ Fh for all (k, h) ∈ [K]× [H]. 
Completeness assumption requires the function class F is closed under Bellman operators of any episode. 
3. Dynamic Eluder Dimension In this section, we introduce a new complexity measure for non-stationary MDPs. We start with the following ϵ-independence between distributions and the distributional Eluder dimension. 
Definition 3.1 (ϵ-independence between distributions (Jin et al., 2021)). Let G be a function class defined on X , and ν, µ1, µ2, · · · , µn be probability measures over X . We say ν is ϵ-independent of {µ1, µ2. · · · , µn} with respect to G if there exists g ∈ G such that 
∑n i=1 (Ex∼µi [g(x)]) 
2 ≤ ϵ2, but |Ex∼ν [g(x)]| > ϵ. 
Definition 3.2 (Distributional Eluder (DE) dimension (Jin et al., 2021)). Let G be a function class defined on X , and Π be a family of probability measures over X . The distributinoal Eluder dimension dimDE(G,Π, ϵ) is the length of the longest sequence {ρ1, ρ2, · · · , ρn} ⊆ Π such that there exists ϵ′ ≥ ϵ where ρi is ϵ′-independent of {ρ1, ρ2, · · · , ρi−1} for all i ∈ [n]. 
The next definition of Bellman Eluder dimension is first introduced in Jin et al. (2021) for stationary MDPs. 
Definition 3.3 (Bellman Eluder dimension (BE)). Let (I − Th)F := {fh − Thfh+1 : f ∈ F , k ∈ [K]} be the set of Bellman residuals in all episodes induced byF at step h, and Π = {Πh}h∈[H] be a collection of H probability measure families over S × A. The ϵ-Bellman Eluder dimension of F with respect to Π is defined as 
dimBE(F ,Π, ϵ) := max h∈[H] 
dimDE ((I − Th)F ,Πh, ϵ) . 
For non-stationary MDPs, the Bellman operators Th varies over time, and hence we introduce our new complexity measure called dynamic Bellman Eluder dimension for nonstationary MDPs. 
Definition 3.4 (Dynamic Bellman Eluder (DBE) dimension). Let (I−T̄h)F := {fh−T k 
h fh+1 : f ∈ F , k ∈ [K]} be the 
set of Bellman residuals in all episodes induced by F at step h, and Π = {Πh}h∈[H] be a collection of H probability measure families over S ×A. The dynamic Bellman Eluder dimension of F with respect to Π is defined as 
dimDBE(F ,Π, ϵ) := max h∈[H] 
dimDE 
( (I − T̄h)F ,Πh, ϵ 
) . 
We focus on the following choice of distribution family D∆ = {D∆,h}h∈[H] where D∆,h = {δ(s,a) : s ∈ S, a ∈ A}. However, our result can be adapted to DF = {DF,h}h∈[H] whereDF,h denotes the collection of all probability measures over S × A at h-th step, generated by executing the greedy policy πf induced by any f ∈ F . 
The DBE dimension is the distributional Eluder dimension on the function class (I−T̄h)F in all episodes, maximizing over step h ∈ [H], which can be viewed as an extension of BE dimension to non-stationary MDPs. The main difference between DBE dimension and BE dimension is that the Bellman operator T k 
h is time-varying, and we include all the Bellman residues induced by T k 
h for k ∈ [K] in the function class. In general, the DBE dimension could be substantially larger than the BE dimension due the fact that the class of functions can be significantly larger. However, we can show that, if the variations in both transitions and rewards are relatively small compared to a universal gap δ̃uϵ defined below, then the DBE dimension equals to the BE dimension with respect to one MDP instance of the non-stationary MDPs. 
Definition 3.5 (Universal gap). If ν is ϵ-independent of µ = (µ1, . . . , µn) with respect to g ∈ G, we define gap δ̃g,ϵ;µ,ν = |Ex∼ν [g(x)]| − ϵ. The universal gap with respect to a function class G is δ̃uϵ = infg∈G,ϵ′≥ϵ,µg 
δ̃g,ϵ′;µg where 
µg is any ϵ′-independent sequence with respect to g. 
Proposition 3.6 (Informal). If the variations in transitions and rewards are relatively small compared to the universal gap δ̃uϵ with respect to (I − T k 
h )F for k ∈ [2 : K], then 
dimDBE(F ,Π, ϵ) = max h∈[H] 
dimDE((I − T 1 h )F ,Π, ϵ), 
where the latter is exactly the BE dimension of the first MDP instance of the non-stationary MDPs. 
The formal statement of the proposition (see Proposi-tion A.4) and its proof is provided in Section A. The intuition is if the variations in transitions and rewards are small (but does not necessarily vanish), then the set of functions (I −T k 
h )F for k ∈ [2 : K] is relatively close to (I −T 1 h )F . 
Therefore their union (I − T̄h)F , constructed for the DBE dimension, remains close to (I − T 1 
h )F . 
Under static MDPs, the DBE dimension naturally reduces to BE dimension, and therefore it subsumes a majority tractable problem classes in stationary RL. Moreover, the DBE framework further includes more tractable problem 
4
Non-stationary RL under General Function Approximation 
classes in non-stationary RL. Below we show that our DBE dimension covers non-stationary linear MDPs. 
Definition 3.7 (Non-stationary Linear MDPs (Zhou et al., 2022)). For linear MDP with feature map ϕ : S ×A 7→ Rd, there exists an unknown measure µk 
h on S and a vector θkh ∈ Rd satisfying P k 
h (s ′|s, a) = ϕ(s, a)⊤µk 
h(s ′) 
and rkh(s, a) = ϕ(s, a)⊤θkh, where ∥ϕ(s, a)∥ ≤ 1 and max{ 
∥∥µk h 
∥∥ ,∥∥θkh∥∥} ≤ √d for all (h, k) ∈ [H]× [K]. 
The next proposition shows that the DBE dimension of non-stationary linear MDPs scales with the linear feature dimension Õ(d). The proof is shown in Appendix B. 
Proposition 3.8. The DBE dimension of non-stationary linear MDPs with the feature dimension d satisfies 
dimDBE(F ,DF , ϵ) ≤ O ( 1 + d log 
( 16H2d/ϵ2 + 1 
)) . 
4. Algorithm In this section, we propose our algorithm SW-OPEA for non-stationary MDPs with general function approximation. 
At high level, SW-OPEA differentiates from the GOLF algorithm (Jin et al., 2021) for static MDPs with general function approximation in its novel designs to handle the nonstationarity of transition kernels and rewards. Specifically, SW-OPEA features the sliding window mechanism and incorporates local variation budget in order to exactly capture the distribution mismatch between current episode and all episodes in the sliding window. Such a design ensures the optimal state-action value function in current episode to lie within the confidence region, and hence the optimism principle remains valid. 
Further in the context of the previous studies of nonstationary MDPs, SW-OPEA is the first confidence-set based algorithm, to the best of our knowledge. In fact, a UCB-type algorithm is not easily applicable to nonstationary MDPs with general function approximation due to the difficulty of finding an appropriate bonus term. As we will show in Section 5 by an example of non-stationary linear MDPs, SW-OPEA performs better than the best known UCB-type algorithms in small variation budget scenarios. 
The pseudocode of SW-OPEA is presented in Algorithm 4. SW-OPEA initializes the dataset {Dh}h∈[H] to be empty sets, and confidence set B0 to be F . Then, in each episode, SW-OPEA performs the following two steps: 
Optimistic planning step (Line 3) greedily selects the most optimistic state-action value function fk from the confidence set Bk−1 constructed in the last episode, and chooses the corresponding greedy policy πk associated with fk. 
Algorithm 1 SW-OPEA (Sliding Window Optimistic-based Exploration and Approximation under non-stationary MDPs) 
1: Input: D1, · · · ,DH ← ∅, B0 ← F . 2: for episode k from 1 to K do 3: Choose πk = πfk , 
where fk = argmaxf∈Bk−1 f1(x1, πf (x1)). 4: Collect a trajectory (xk 
1 , a k 1 , · · · , xk 
H , akH , xk H+1) by 
following πk and reward function {rkh}h∈[H]. 5: Augment Dh=Dh∪{(xk 
h, a k h, x 
k h+1)}, ∀h ∈ [H]. 
6: Update Bk={f ∈F : LDh (fh, fh+1)≤ 
infg∈Gh LDh 
(g,fh+1)+β+2H2∆w P (k, h), ∀h∈ [H]}. 
7: end for 
Sliding window squared Bellman error is defined as 
LDh (ξh, ζh+1) = 
k∑ t=1∨(k−w) 
( ξh(x 
t h, a 
t h)− rkh(x 
t h, a 
t h) 
−max a′∈A 
ζh+1(x t h+1, a 
′) 
)2 
. (1) 
Note that in episode k, we use the latest reward information rkh over the entire window, rather than rth, to form the sliding window squared Bellman error. Such construction exploits the most recent information of the reward function rkh to maximally reduce the non-stationarity of rewards. There-fore, LDh 
tends to be small as long as the transition kernel difference between episode k and t is small. Furthermore, we adopt the sliding window in the squared loss (1), which is based on the “forgetting principle” (Garivier & Moulines, 2011) where the squared loss estimated at episode k relies on the observed history during episode 1 ∨ (k − w) to k instead of all prior observations. The rationale is that under non-stationarity setting, the historical observations far in the past are obsolete, and they are not as informative for the evaluation of the squared loss. 
Confidence set updating step (Line 4-6) first executes policy πk and collects data for the current episode, and then updates the confidence set based on the new data. 
The key novel ingredient of SW-OPEA lies in the construction of the confidence set Bk. For each h ∈ [H], SW-OPEA maintains a local regression constraint using the collected data Dh 
LDh (fh, fh+1)≤ inf 
g∈Gh 
LDh (g, fh+1)+β+2H2∆w 
P (k, h), 
where β is a confidence parameter, and ∆w P is the local 
variation budget defined by 
∆w P (k, h)= 
k∑ t=1∨(k−w) 
sup x∈S,a∈A 
∥∥(P k h − P t 
h)(·|x, a) ∥∥ 1 . (2) 
5
Non-stationary RL under General Function Approximation 
Since the transition kernel varies across episodes, we include an additional term of the local variation budget ∆w 
P (k, h) in the definition of Bk. Intuitively, the local variation budget ∆w 
P (k, h) captures the cumulative transition kernel differences between current episode and all previous episode in the sliding window. Therefore, by compensating a term involving ∆w 
P (k, h) in the confidence set Bk, we ensure that the optimal state-action value function in the k-th episode Q∗ 
h;(∗,k) still lies in the confidence set Bk with high probability (see Lemma C.2). 
We remark that the assumption on the local variation budget involving transition functions are unknown could be relaxed. Inspired by the standard technique to handle unknown variation budget as in linear nonstationary MDPs (Zhou et al., 2022), we propose the following modification of the algorithm. We remove the local variation budget in the bonus term in the algorithm, and instead, design a strategy to adapt the window size to the variation budget (without knowing its value) as in the EXP3-P algorithm (Bubeck & Cesa-Bianchi, 2012). It has been shown that as long as the window sizes are picked to densely cover the entire value range of the window size, such a scheme will result in a performance close enough to the case as if the window size is picked in an optimal way when the variation budget is known. We expect that such a scheme will achieve the same regret (in terms of scaling) as the case with the knowledge of the variation budget. We will investigate the feasibility of the proposed strategy and leave the detailed mathematical analysis in the future work. 
5. Theoretical Guarantees In this section, we first provide our main theoretical result for SW-OPEA, and then present a proof sketch that highlights our novel developments in the analysis. 
5.1. Main Results 
In this section, we provide our characterization of the dynamic regret for SW-OPEA. 
We first state the following generalized completeness assumption (Antos et al., 2008; Chen & Jiang, 2019; Jin et al., 2021). Let G = G1 × · · · × GH be an auxiliary function class provided to the learner where Gh ⊆ (S × A 7→ [0, H − h+ 1]). 
Assumption 5.1 (Generalized completeness). T k h Fh+1 ⊆ 
Gh for all (k, h) ∈ [K]× [H]. 
If we choose G = F , then Assumption 5.1 is equivalent to the standard completeness assumption (Assumption 2.2). Without loss of generality, we assume F ⊆ G and G = F ∪ G. 
Moreover, to quantify the non-stationarity, we define the 
variation in rewards of adjacent episodes and the variation in transition kernels of adjacent episodes as 
∆R(K) = 
K∑ k=1 
H∑ h=1 
sup x∈S,a∈A 
|(rkh − rk−1 h )(x, a)|, (3) 
∆P (K) = 
K∑ k=1 
H∑ h=1 
sup x∈S,a∈A 
∥∥(P k h −P k−1 
h )(·|x, a) ∥∥ 1 , (4) 
where we define P 0 h = P 1 
h and r0h = r1h for all h ∈ [H]. 
The dynamic regret of our algorithm SW-OPEA is characterized in the following theorem. Theorem 5.2 (Dynamic regret of SW-OPEA). Under As-sumption 2.1 and Assumption 5.1, there exists an absolute constant c such that for any δ ∈ (0, 1], K ∈ N, if we choose β = cH2 log KH|G| 
δ in SW-OPEA, then with probability at least 1 − δ, for all k ∈ [K], when k ≥ min{w + 1,dimDBE(F ,D∆,h, 
√ 1/w)} we have 
D− Regret(k) = ∆R(k) +H∆P (k) +O (√ 
w 
+ H2k√ 
w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d sup 
t∈[k] 
∆w P (t, h) 
) , 
where d = dimDBE(F ,D∆,h, √ 1/w). 
Note that the last term depends on the sliding window size w, and we can further optimize w if an upper bound of the local variation budget ∆w 
P (t, h) is given. Below we give an example for optimizing sliding window size w. 
Before we proceed, we first define the average variation budget L as 
L = maxh∈[H],t<k 
∑k−1 s=t supx,a ∥(P s+1 
h −P s h)(·|x,a)∥1 
k−t . (5) 
Clearly, we have L ≤ 1 and ∆w P (k, h) ≤ Lw2, and L can 
be viewed as the the greatest average variation of transition kernels across adjacent episodes over any period of episodes maximized over step h ∈ [H]. Then the following corollary characterizes the dynamic regret by optimizing the window size w based on L. Corollary 5.3. Under the condition of Theorem 5.2 and |G| > 10, with probability at least 1 − δ, the following 
argument holds: if √ L > 1 
K 
(√ log |G| − 1 
H √ d 
) , select 
w = ⌈ √ 
log |G|√ L+ 1 
HK √ 
d 
⌉ and the dynamic regret is bounded by 
Õ ( H 
3 2K 
1 2 d 
1 4 (log |G|) 
1 4 +H2Kd 
1 2L 
1 4 (log |G|) 
1 4 
+∆R +H∆P 
) ; (6) 
otherwise, select w = K and the dynamic regret is bounded by Õ 
( H2K 
1 2 d 
1 2 (log |G|) 1 
2 
) , where d = 
dimDBE(F ,D∆,h, √ 1/w). 
6
Non-stationary RL under General Function Approximation 
We remark that |G| appearing in the log term can be replaced by its ϵ-covering number NG(ϵ) to handle the classes with infinite cardinality. In both Theorem 5.2 and Corollary 5.3, we do not omit log |G| in Õ since for many function classes, log |G| (or logNG(ϵ)) can contribute to a polynomial factor. For example, for d̃ dimensional linear function class, logNG(ϵ) = Õ(d̃) where d̃ is the linear feature dimension. 
Our first term in (6) corresponds to the regret of the static MDP while the remaining term arises due to the non-stationarity. As a result, when transitions and rewards remain the same over time, our result reduces to Õ ( H2K 
1 2 d 
1 2 (log |G|) 1 
2 
) , which matches the static regret 
of GOLF in Jin et al. (2021)2. 
Advantage of SW-OPEA: To understand the advantage of SW-OPEA over the UCB-based algorithms, we take non-stationary linear MDPs as an example. When specializing to non-stationary linear and tabular MDPs, our result becomes Õ 
( H 
3 2T 
1 2 d̃+HTd̃ 
3 4L 
1 4 + TLθ 
) where 
T = HK, d̃ is the feature dimension for linear MDPs and d̃ = |S||A| for tabular MDPs, and Lθ is the average variation budget in rewards. For non-stationary linear MDPs, the result in Zhou et al. (2022) is not comparable to ours due to the different definitions of the variation budget of transition kernels. To make a fair comparison, we convert their bound on the dynamic regret3 to be for tabular MDPs, which gives Õ 
( H 
3 2T 
1 2 d̃ 
3 2 +H 
4 3 d̃ 
3 2T L̃ 
1 3 +H 
4 3 d̃ 
4 3TL 
1 3 
θ 
) . 
The first term corresponds to the regret of static linear MDPs and our result has better dependency on the feature dimension d̃. For the second term due to the non-stationarity of transition kernels, our bound is better in terms of the horizon H and feature dimension d̃ while worse in terms of the average variation budget of transitions L (note that L ≤ 1). For the last term caused by the non-stationary of rewards, our result performs better in the variation budget of rewards, horizon H as well as the feature dimension d̃. 
It also interesting to compare our result with the minimax dynamic regret lower bound Ω 
( H 
1 2T 
1 2 d̃+H 
1 3T d̃ 
2 3 L̃ 
1 3 
) developed in Zhou et al. (2022) for linear MDPs with nonstationary transitions. For such a case, our result becomes Õ ( H 
3 2T 
1 2 d̃+HTd̃ 
3 4L 
1 4 
) . The first term is the regret un-
der stationary MDPs and the second term arises due to the non-stationarity of transitions. We can see that our first term corresponding to static MDPs matches the lower bound both in terms of T and d̃, whereas the upper bound in Zhou et al. (2022) matches the lower bound only in T . For the non-
2The additional H here is due to the definition of rh ∈ [0, 1], whereas Jin et al. (2021) assumes 
∑ h rh ≤ 1. 
3They consider bandit feedback. By adapting their algorithm and analysis, it turns out that the dynamic regret does not benefit from full information feedback in non-stationary linear MDPs. 
stationarity term, our dependency on H and d̃ is closer to the lower bound than that in Zhou et al. (2022), whereas our dependency on the variation budget is close but does not match the lower bound. Overall, these comparisons suggest that our confidence-set based algorithm performs better than UCB-type algorithms in small variation budget scenario under non-stationary linear MDPs. 
When the state-action set forms a metric space, Domingues et al. (2020) proposed a kernel-based approach in nonstationary RL. Ignoring term regarding static MDPs, their result renders Õ 
( SA 
1 2H 
4 3TL 
1 3 + SA 
1 2H 
4 3TL 
1 3 
θ 
) regret 
bound in the tabular case while our result becomes Õ ( (SA) 
3 4HTL 
1 4 + TLθ 
) . For the first term caused by the 
non-stationarity of transition kernels, our result has better dependency on step H , but is worse in the average variation budget of transitions. For the second term caused by the non-stationarity of rewards, the dependency on the variation budget of rewards, horizon H as well as the cardinality of state and action spaces is improved. The comparison suggests our confidence-set based algorithm is advantageous over the kernel-based algorithm in small variation budget and small action space scenario under non-stationary MDPs. 
5.2. Proof Sketch of Theorem 5.2 
In this section, we provide a sketch of the proof for Theo-rem 5.2 and defer all the details to Appendix C. 
The preliminary step is to decompose the dynamic regret of SW-OPEA into three terms as follows: 
D− Regret(k) ≤ 
H + 
k∑ t=1 
H∑ h=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(rt−1 h − rth)(xh, ah)]︸ ︷︷ ︸ 
(I) 
+ 
k∑ t=1 
H∑ h=1 
[ E 
(xh,ah)∼(πt,(∗,t−1)) − E (xh,ah)∼(πt,(∗,t)) 
] [rth(xh, ah)]︸ ︷︷ ︸ 
(II) 
+ 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1)︸ ︷︷ ︸ 
(III) 
. (7) 
Term (I) can be bounded by ∆R(k) by the definition of the variation budget of rewards (3). In the sequel, we aim to bound (II) in step II and bound (III) in the remaining steps. 
Step I: We introduce a novel auxiliary MDP to help bound term (II). For a fixed tuple (k, h) ∈ [K] × [H], we design an episodic MDP (S,A, H, P k, r̃, x1) with reward r̃h′ = rkh(x, a)1{h′ = h} and the corresponding state value function of policy {πh′}h′∈[H] is defined as Ṽ π 
h′;,(∗,k). Then, 
7
Non-stationary RL under General Function Approximation 
we show in Lemma C.1 that( E 
(xh,ah)∼(πk,(∗,k−1)) − E 
(xh,ah)∼(πk,(∗,k)) 
) [rkh(xh, ah)] = 
[ Ṽ πk 
1;(∗,k−1)− Ṽ πk 
1;(∗,k) 
] (x1)≤ 
h−1∑ i=1 
sup x,a 
∥∥∥(P k h −P k−1 
h )(·|x, a) ∥∥∥ 1 . 
Replacing k by t, and summing over t ∈ [k], h ∈ [H] gives 
(II) ≤ k∑ 
t=1 
H∑ h=1 
sup x,a 
h−1∑ i=1 
∥∥(P t−1 i − P t 
i )(·|x, a) ∥∥ 1 
≤ H∑ 
h=1 
( k∑ 
t=1 
H∑ i=1 
sup x,a 
∥∥(P t−1 i − P t 
i )(·|x, a) ∥∥ 1 
) ≤ H∆P (k). 
Step II: This step together with the next step establishes important properties to bound term (III) in step IV. 
First, we develop the following crucial probability distribution shift lemma, which will handle the transition kernel variation in non-stationary MDPs. Lemma 5.4 (Probability distribution shift lemma). Suppose P and Q are two probability distributions of a random variable x and define fm = supx |f(x)|. Then we have∣∣∣∣∣( E 
x∼P f(x)− C 
)2 − ( 
E x∼Q 
f(x)− C 
)2 ∣∣∣∣∣ 
≤ (2fm + 2|C|)fm · TV(P,Q). 
The proof can be found in Appendix C.6. 
Next, we show in Lemma C.2 that Q∗ (∗,k), the optimal state-
action value function at step h, lies in the confidence set Bk for all k ∈ [K] with high probability. The argument is proved by the martingale concentration and the confidence set we design. Technically, we define 
#k,h(x t h, a 
t h) 
= rkh(s t h, a 
t h) + E 
x′∼P t h (·|xt 
h ,at 
h ) max a′∈A 
Qh+1;(∗,k)(x ′, a′), 
to form an appropriate martingale difference, which is similar to the h-th step Bellman update of the state-action value function in episode k except that the expectation is taken with respect to P t 
h instead of P k h . By Lemma 5.4, the 
cumulative mismatch during the sliding window between #k,h(x 
t h, a 
t h) and the h-step Bellman update of state-action 
value function in episode k is captured by the local pathlength ∆w 
P (k, h). Finally, by the design of confidence set Bk, we can show that Q∗ 
(∗,k) ∈ B k. 
Given Q∗ (∗,k) ∈ B 
k for all k ∈ [K], the optimistic planning step (Line 1) guarantees V ∗ 
1;(∗,k−1)(x1) ≤ supa f k 1 (x1, a) 
for every episode k ∈ [K]. Combining the optimism and the generalized policy loss decomposition (see Lemma C.8), we have 
(III) ≤ k∑ 
t=1 
( max a∈A 
f t 1(x1, a)− V πt 
1;(∗,t−1)(x1) 
) 
≤ H∑ 
h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)]. 
(8) 
Step III: We will show the sharpness of our confidence set Bk. Under the construction of Bk, fk selected from Bk−1 
is guaranteed to have small loss LDh (fk 
h , f h+1 h ). Note that 
data used in episode k are collected by executing πi for one episode for all i ∈ [1∨ (k−w), k], by the concentration and the completeness assumption. We can show in Lemma C.3 that with high probability, for all (k, h) ∈ [K]× [H], 
k−1∑ t=1∨(k−w−1) 
[ fk h (s 
t h, a 
t h)− rk−1 
h (sth, a t h) 
− E x′∼Pk−1 
h (xt 
h ,at 
h ) 
max a′∈A 
fk h+1(s 
′, a′) ]2 
≤ 6H2∆w P (k − 1, h) +O(β). (9) 
Technically, we define the following helpful random variable 
#f k,h(x 
t h, a 
t h) = rkh(s 
t h, a 
t h) + E 
x′∼P t h (xt 
h ,at 
h ) max a′∈A 
fh+1(s ′, a′) 
to form an appropriate martingale and obtain the martingale concentration result. Then, applying our probability distribution shift lemma (Lemma 5.4), the definition of Bk and the completeness assumption gives (9). 
Step IV: We establish the relationship between (8) and (9). Specifically, we aim to upper bound (8) given (9) holds. Note that their forms are similar except that the latter is the squared Bellman error, and the data (st, at) is taken under policy πi for i ∈ [1 ∨ (k − w) : k − 1]. It turns out that the DBE dimension plays an important role in connecting these two terms, as summarized in the following lemma. Lemma 5.5. Given a function class Φ defined on X with |ϕ(x)| ≤ C for all (g, x) ∈ Φ × X , and a family of probability measures Π over X . Suppose {ϕk}k∈[K] ⊆ Φ and {µk}k∈[K] ⊆ Π satisfy that for all k ∈ [K],∑k−1 
t=1∨(k−w−1)(Ex∼µt [ϕk(x)]) 
2 ≤ β. Then for all k ∈ [K] and ω > 0, 
k∑ t=1∨(k−w) 
|Ex∼µt [ϕt(x)]| 
≤ O (√ 
dimDE(Φ,Π, θ)β[k ∧ (w + 1)] 
+ min{w + 1, k,dimDE(Φ,Π, θ)}C + [k ∧ (w + 1)]θ ) . 
The proof is adapted from the proof of Lemma 41 in (Jin et al., 2021) and provided in Appendix C.5. 
Based on the DBE dimension and Lemma 5.5, we are ready to bound (III) via term (8) . By choosing Φ to be the function class of Bellman residuals, and µk to be the distribution under policy πk, term (III) is upper bounded by 
H∑ h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
8
Non-stationary RL under General Function Approximation 
≤ O ( H √ w + 
H2k√ w 
√ dimDBE(F ,D∆, 
√ 1/K) log 
KH|F| δ 
+ Hk√ w 
√ dimDBE(F ,D∆, 
√ 1/K) 
H∑ h=1 
√ sup k∈[K] 
∆w P (k, h) 
) . 
Combining all the steps, the dynamic regret of our algorithm SW-OPEA is 
D− Regret(k) ≤ ∆R(k) +H∆P (k) +O ( H √ w 
H2k√ w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d supt∈[k] ∆ 
w P (t, h) 
) where we suppress the first term H in (7) since it is dominated by the fourth term herein. 
5.3. Bandit Feedback 
In this section, we extend our algorithm to bandit feedback scenario. We defer all the details to Appendix D. 
In bandit feedback scenario, the reward function rkh(·, ·) is no long available, and the agent can only get access to the reward obtained from the trajectory. Therefore, we need to capture the non-stationarity of rewards in the construction of the sliding window Bellman error and the confidence set. Specifically, we replace the sliding window squared Bellman error (1) with 
LDh(ξh, ζh+1) = 
k∑ t=1∨(k−w) 
( ξh(x 
t h, a 
t h)− rth 
−max a′∈A 
ζh+1(x t h+1, a 
′) 
)2 
, 
where rth is the reward obtained at step h in episode t. More-over, the local regression constraint for the confidence set is 
LDh(fh, fh+1) ≤ inf g∈Gh 
LDh(g, fh+1) + β 
+ 2H2∆w P (k, h) + 2H∆w 
R(k, h), 
where β is a confidence parameter, ∆w P is the local variation 
budget in transitions defined in (2) and ∆w R is the local 
variation budget in rewards defined as 
∆w P (k, h) = 
∑k t=1∨(k−w) supx∈S,a∈A |(rkh − rth)(x, a)|. 
Our main theoretical result for the bandit feedback scenario is provided in the next theorem. Theorem 5.6. Under Assumption 2.1 and Assumption 5.1, there exists an absolute constant c such that for any δ ∈ (0, 1], K ∈ N, if we choose β = cH2 log KH|G| 
δ in SW-OPEA, then with probability at least 1− δ, for all k ∈ [K], when k ≥ min{w+1,dimDBE(F ,D∆,h, 
√ 1/w)} we have 
D− Regret(k) = ∆R(k) +H∆P (k) +O ( H √ w 
+ H2k√ 
w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d sup 
t∈[k] 
∆w P (t, h) 
+ H3/2k√ 
w 
√ d sup 
t∈[k] 
∆w R(t, h) 
) , 
where d = dimDBE(F ,D∆,h, √ 1/w). 
Besides the average variation budget L in transitions defined in (5), we define the average variation budget Lθ in rewards 
Lθ = maxh∈[H],t<k 
∑k−1 s=t supx,a |(rs+1 
h −rsh)(x,a)| k−t . (10) 
By optimizing the window size w, we have the following corollary. Corollary 5.7. Under the condition of Theorem 5.6 and |G| > 10, with probability at least 1 − δ, the following argument holds: if 
√ L + 
√ Lθ√ H 
> 
1 K 
(√ log |G| − 1 
H √ d 
) , select w = ⌈ 
√ log |G| 
√ L+ 
√ Lθ√ H 
+ 1 
HK √ 
d 
⌉, 
the dynamic regret is upper-bounded by 
Õ ( H 
3 2K 
1 2 d 
1 4 (log |G|) 
1 4 +H2KL 
1 4 d 
1 2 (log |G|) 
1 4 
+H 7 4KL 
1 4 θ d 
1 2 (log |G|) 
1 4 +∆R +H∆P 
) ; 
otherwise, select w = K and the dynamic regret is upper-bounded by Õ 
( H2K 
1 2 d 
1 2 (log |G|) 1 
2 
) , where d = 
dimDBE(F ,D∆,h, √ 1/w). 
6. Conclusion and Future Work In this paper, we proposed a new complexity metric named Dynamic Bellman Eluder (DBE) dimension for nonstationary MDPs, which extends the Bellman Eluder (BE) dimension for static MDPs. When the variations in transition kernels and rewards are relatively small compared to a universal gap, we show that the DBE dimension is exactly the BE dimension of one MDP instance in the non-stationary MDPs. We then incorporated the sliding window mechanism and a novel design for the confidence set into our confidence-set based algorithm SW-OPEA, and provided its theoretical upper bound on the dynamic regret. We further demonstrate the advantage of our algorithm by comparing our dynamic regret bound to that of previously proposed algorithms for non-stationary linear and tabular MDPs. One interesting future direction is to further improve the dependency of the dynamic regret on the average variation L. 
Acknowledgements The work of S. Feng was supported in part by the startup fund of the Ohio State University. The work of Y. Liang was supported in part by the U.S. National Science Founda-tion under the grants DMS-2134145 and RINGS-2148253. The work of R. Huang and J. Yang was supported by the U.S. National Science Foundation under the grants CNS-1956276 and CNS-2003131. M. Yin and Y. Wang were partially supported by National Science Foundation grants #2007117 and #2003257. 
9
Non-stationary RL under General Function Approximation 
References Agrawal, S. and Jia, R. Learning in structured mdps with 
convex cost functions: Improved regret bounds for inventory management. In Proceedings of the 2019 ACM Conference on Economics and Computation, 2019. 
Antos, A., Szepesvári, C., and Munos, R. Learning near-optimal policies with bellman-residual minimization based fitted policy iteration and a single sample path. Mach. Learn., 71(1):89–129, apr 2008. 
Auer, P., Cesa-Bianchi, N., Freund, Y., and Schapire, R. E. The nonstochastic multiarmed bandit problem. SIAM Journal on Computing, 32(1):48–77, 2002. 
Auer, P., Jaksch, T., and Ortner, R. Near-optimal regret bounds for reinforcement learning. In Advances in Neural Information Processing Systems, 2008. 
Auer, P., Gajane, P., and Ortner, R. Adaptively tracking the best bandit arm with an unknown number of distribution changes. In Proceedings of the Thirty-Second Conference on Learning Theory, 2019. 
Besbes, O., Gur, Y., and Zeevi, A. Stochastic multi-armed-bandit problem with non-stationary rewards. In Advances in Neural Information Processing Systems, 2014a. 
Besbes, O., Gur, Y., and Zeevi, A. Stochastic multi-armed-bandit problem with non-stationary rewards. In Advances in Neural Information Processing Systems, 2014b. 
Besbes, O., Gur, Y., and Zeevi, A. Optimal exploration–exploitation in a multi-armed bandit problem with non-stationary rewards. Stochastic Systems, 9(4):319– 337, 2019. 
Bubeck, S. and Cesa-Bianchi, N. Regret analysis of stochastic and nonstochastic multi-armed bandit problems. Found. Trends Mach. Learn., 5(1):1–122, 2012. 
Cai, H., Ren, K., Zhang, W., Malialis, K., Wang, J., Yu, Y., and Guo, D. Real-time bidding by reinforcement learning in display advertising. In Proceedings of the Tenth ACM International Conference on Web Search and Data Mining (WSDM), 2017. 
Chen, C., Wei, H., Xu, N., Zheng, G., Yang, M., Xiong, Y., Xu, K., and Zhenhui. Toward a thousand lights: De-centralized deep reinforcement learning for large-scale traffic signal control. In AAAI Conference on Artificial Intelligence, 2020. 
Chen, J. and Jiang, N. Information-theoretic considerations in batch reinforcement learning. In Proceedings of the 36th International Conference on Machine Learning, 2019. 
Chen, Y., Lee, C.-W., Luo, H., and Wei, C.-Y. A new algorithm for non-stationary contextual bandits: Efficient, optimal and parameter-free. In Proceedings of the Thirty-Second Conference on Learning Theory, 2019. 
Chen, Z., Li, C. J., Yuan, A., Gu, Q., and Jordan, M. A general framework for sample-efficient function approximation in reinforcement learning. ArXiv, abs/2209.15634, 2022. 
Cheung, W. C., Simchi-Levi, D., and Zhu, R. Learning to optimize under non-stationarity. In Proceedings of the Twenty-Second International Conference on Artificial Intelligence and Statistics, 2019. 
Cheung, W. C., Simchi-Levi, D., and Zhu, R. Reinforcement learning for non-stationary Markov decision processes: The blessing of (More) optimism. In Proceedings of the 37th International Conference on Machine Learning, 2020. 
Cheung, W. C., Simchi-Levi, D., and Zhu, R. Hedging the drift: Learning to optimize under nonstationarity. Man-agement Science, 68(3):1696–1713, 2022. 
Dekel, O. and Hazan, E. Better rates for any adversarial deterministic MDP. In Proceedings of the 30th Interna-tional Conference on Machine Learning, 2013. 
Domingues, O. D., M’enard, P., Pirotta, M., Kaufmann, E., and Valko, M. A kernel-based approach to non-stationary reinforcement learning in metric spaces. In International Conference on Artificial Intelligence and Statistics, 2020. 
Dong, K., Peng, J., Wang, Y., and Zhou, Y. √ n-regret 
for learning in markov decision processes with function approximation and low bellman rank. ArXiv, 2019. 
Du, S. S., Kakade, S. M., Lee, J. D., Lovett, S., Mahajan, G., Sun, W., and Wang, R. Bilinear classes: A structural framework for provable generalization in RL. In International Conference on Machine Learning, 2021. 
Even-Dar, E., Kakade, S. M., and Mansour, Y. Online markov decision processes. Mathematics of Operations Research, 34(3):726–736, 2009. 
Fei, Y., Yang, Z., Wang, Z., and Xie, Q. Dynamic regret of policy optimization in non-stationary environments. In Advances in Neural Information Processing Systems, 2020. 
Foster, D. J., Kakade, S. M., Qian, J., and Rakhlin, A. The statistical complexity of interactive decision making. ArXiv, 2021. 
Foster, D. J., Rakhlin, A., Sekhari, A., and Sridharan, K. On the Complexity of Adversarial Decision Making. ArXiv, 2022. 
10
Non-stationary RL under General Function Approximation 
Gajane, P., Ortner, R., and Auer, P. A sliding-window algorithm for markov decision processes with arbitrarily changing rewards and transitions. ArXiv, 2018. 
Garivier, A. and Moulines, E. On upper-confidence bound policies for switching bandit problems. In Proceedings of the 22nd International Conference on Algorithmic Learn-ing Theory, 2011. 
Gu, S., Holly, E., Lillicrap, T., and Levine, S. Deep reinforcement learning for robotic manipulation with asynchronous off-policy updates. In 2017 IEEE international conference on robotics and automation (ICRA), 2017. 
Jiang, N., Krishnamurthy, A., Agarwal, A., Langford, J., and Schapire, R. E. Contextual decision processes with low Bellman rank are PAC-learnable. In Proceedings of the 34th International Conference on Machine Learning, 2017. 
Jin, C., Jin, T., Luo, H., Sra, S., and Yu, T. Learning adversarial markov decision processes with bandit feedback and unknown transition. In International Conference on Machine Learning, 2020. 
Jin, C., Liu, Q., and Miryoosefi, S. Bellman eluder dimension: New rich classes of RL problems, and sampleefficient algorithms. In Advances in Neural Information Processing Systems, 2021. 
Karnin, Z. S. and Anava, O. Multi-armed bandits: Com-peting with optimal sequences. In Advances in Neural Information Processing Systems, 2016. 
Keskin, N. B. and Zeevi, A. Chasing demand: Learning and earning in a changing environment. Mathematics of Operations Research, 42(2):277–307, 2017. 
Kober, J., Bagnell, J. A., and Peters, J. Reinforcement learning in robotics: A survey. International Journal of Robotics Research, 32(11):1238–1274, 2013. 
Lu, J., Yang, C., Gao, X., Wang, L., Li, C., and Chen, G. Reinforcement learning with sequential information clustering in real-time bidding. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management, 2019. 
Luo, H., Agarwal, A., and Langford, J. Efficient contextual bandits in non-stationary worlds. In Annual Conference Computational Learning Theory, 2017. 
Ma, W. Improvements and generalizations of stochastic knapsack and markovian bandits approximation algorithms. Mathematics of Operations Research, 43(3):789– 812, 2018. 
Mao, W., Zhang, K., Zhu, R., Simchi-Levi, D., and Basar, T. Near-optimal model-free reinforcement learning in nonstationary episodic MDPs. In Proceedings of the 38th International Conference on Machine Learning, 2021. 
Neu, G., György, A., and Szepesvari, C. The online loop-free stochastic shortest-path problem. In Annual Confer-ence Computational Learning Theory, 2010. 
Neu, G., Gyorgy, A., and Szepesvari, C. The adversarial stochastic shortest path problem with unknown transition probabilities. In Proceedings of the Fifteenth Interna-tional Conference on Artificial Intelligence and Statistics, 2012. 
Osband, I. and Roy, B. V. Model-based reinforcement learning and the eluder dimension. In Proceedings of the 27th International Conference on Neural Information Process-ing Systems, 2014. 
Rosenberg, A. and Mansour, Y. Online convex optimization in adversarial markov decision processes. In International Conference on Machine Learning, 2019. 
Russo, D. and Van Roy, B. Eluder dimension and the sample complexity of optimistic exploration. In Advances in Neural Information Processing Systems, 2013. 
Shortreed, S. M., Laber, E. B., Lizotte, D. J., Stroup, T. S., Pineau, J., and Murphy, S. A. Informing sequential clinical decision-making through reinforcement learning: an empirical study. Machine Learning, 84:109–136, 2010. 
Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., et al. Mastering the game of go with deep neural networks and tree search. nature, 529(7587):484–489, 2016. 
Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Grae-pel, T., et al. Mastering chess and shogi by self-play with a general reinforcement learning algorithm. ArXiv, 2017. 
Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Grae-pel, T., et al. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. Sci-ence, 362(6419):1140–1144, 2018. 
Sun, W., Jiang, N., Krishnamurthy, A., Agarwal, A., and Langford, J. Model-based rl in contextual decision processes: Pac bounds and exponential improvements over model-free approaches. In Annual Conference Computa-tional Learning Theory, 2018. 
Sutton, R. S. and Barto, A. G. Reinforcement Learning: An Introduction. The MIT Press, second edition, 2018. 
11
Non-stationary RL under General Function Approximation 
Touati, A. and Vincent, P. Efficient learning in nonstationary linear markov decision processes. ArXiv, 2020. 
Vinyals, O., Babuschkin, I., Czarnecki, W. M., Mathieu, M., Dudzik, A., Chung, J., Choi, D. H., Powell, R., Ewalds, T., Georgiev, P., Oh, J., Horgan, D., Kroiss, M., Danihelka, I., Huang, A., Sifre, L., Cai, T., Agapiou, J. P., Jaderberg, M., Vezhnevets, A. S., Leblond, R., Pohlen, T., Dalibard, V., Budden, D., Sulsky, Y., Molloy, J., Paine, T. L., Gulcehre, C., Wang, Z., Pfaff, T., Wu, Y., Ring, R., Yogatama, D., Wünsch, D., McKinney, K., Smith, O., Schaul, T., Lillicrap, T. P., Kavukcuoglu, K., Hassabis, D., Apps, C., and Silver, D. Grandmaster level in starcraft II using multi-agent reinforcement learning. Nature, pp. 1–5, 2019. 
Wang, R., Salakhutdinov, R. R., and Yang, L. Reinforce-ment learning with general value function approximation: Provably efficient approach via bounded eluder dimension. In Advances in Neural Information Processing Systems, 2020. 
Wei, C.-Y. and Luo, H. Non-stationary reinforcement learning without prior knowledge: An optimal black-box approach. ArXiv, 2021. 
Yin, M., Bai, Y., and Wang, Y.-X. Near-optimal provable uniform convergence in offline policy evaluation for reinforcement learning. In International Conference on Arti-ficial Intelligence and Statistics, pp. 1567–1575. PMLR, 2021. 
Yin, M., Wang, M., and Wang, Y.-X. Offline reinforcement learning with differentiable function approximation is provably efficient. International Conference on Learning Representations, 2023. 
Yu, J. Y. and Mannor, S. Arbitrarily modulated markov decision processes. In Proceedings of the 48h IEEE Conference on Decision and Control (CDC) held jointly with 2009 28th Chinese Control Conference, 2009. 
Yu, J. Y., Mannor, S., and Shimkin, N. Markov decision processes with arbitrary reward processes. Mathematics of Operations Research, 34(3):737–757, 2009. 
Yurtsever, E., Lambert, J., Carballo, A., and Takeda, K. A survey of autonomous driving: Common practices and emerging technologies. IEEE Access, 8:58443–58469, 2019. 
Zhang, R., Zhang, X., Ni, C., and Wang, M. Off-policy fitted q-evaluation with differentiable function approximators: Z-estimation and inference theory. In International Con-ference on Machine Learning, 2022. 
Zhao, P., Zhang, L., Jiang, Y., and Zhou, Z.-H. A simple approach for non-stationary linear bandits. In Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, 2020. 
Zhong, H., Yang, Z., Wang, Z., and Szepesvári, C. Opti-mistic policy optimization is provably efficient in nonstationary MDPs. ArXiv, 2021. 
Zhou, H., Chen, J., Varshney, L. R., and Jagmohan, A. Nonstationary reinforcement learning with linear function approximation. Transactions on Machine Learning Research, 2022. 
Zimin, A. and Neu, G. Online learning in episodic markovian decision processes by relative entropy policy search. In Advances in Neural Information Processing Systems, 2013. 
12
Non-stationary RL under General Function Approximation 
A. Proof of Proposition 3.6 In this section, we extend Bellman Eluder (BE) dimension to dynamic Bellman Eluder dimension (DBE) under the setting of small variations in transitions and rewards in the following steps. 
The First Step is to generalize the class of Bellman residues considered in Bellman Eluder dimension. We restate the definition of Bellman Eluder dimension (Jin et al., 2021). Definition A.1 (Bellman Eluder dimension (BE)). Let (I − Th)F := {fh − Thfh+1 : f ∈ F} be the set of Bellman residuals in all episodes induced by F at step h, and Π = {Πh}h∈[H] be a collection of H probability measure families over S ×A. The ϵ-Bellman Eluder dimension of F with respect to Π is defines as 
dimBE(F ,Π, ϵ) := max h∈[H] 
dimDE ((I − Th)F ,Πh, ϵ) . 
For ease of presentation, we use (f, Th) to denote the element fh − Thfh+1 in the set (I − Th)F . For any (f, Th) pair, we introduce the complement of (f, Th), denoted by (−f,−Th), where −Thf ′ = −rh + Phf 
′ for any f ′. Let −(I − Th)F be the set of all complements of (f, Th) ∈ (I − Th)F . Then, we define the extended class of Bellman residuals 
dimBE(F̃ ,Π, ϵ) := max h∈[H] 
dimDE 
( (I − T̃h)F̃ ,Πh, ϵ 
) , 
where (I − T̃h)F̃ = ((I − Th)F) ∪ (−(I − Th)F). 
We first show that the BE dimension of the extended class of Bellman residuals equals to that of the original class of Bellman residuals, as formalized in the following lemma. Lemma A.2. Let F̃ be defined in the above context, then we have dimBE(F̃ ,Π, ϵ) = dimBE(F ,Π, ϵ). 
Proof. Since (I − Th)F ⊆ (I − T̃h)F̃ , it is obvious that dimBE(F̃ ,Π, ϵ) ≥ dimBE(F ,Π, ϵ). Next, we show dimBE(F̃ ,Π, ϵ) ≤ dimBE(F ,Π, ϵ). Let µ be independent of ρ1, . . . , ρm with respect to (I − T̃h)F̃ . We aim to show µ is also independent of ρ1, . . . , ρm with respect to (I − Th)F . 
By the definition of ϵ-independence between distributions, there exists a function g from either (I − Th)F or −(I − Th)F such that the there exists ϵ′ ≥ ϵ such that 
√∑m i=1 Eρi 
[g] ≤ ϵ and |Eµ[g]| > ϵ. If g is from (I − Th)F , then µ is obviously independent of ρ1, . . . , ρm with respect to (I −Th)F . If g is from −(I −Th)F , i.e., g has form g = −fh− (−Th)(−fh+1) for some f and Th, we have 
m∑ t=1 
(Ex∼ρi [−fh − (−Th)(−fh+1)]) 2 = 
m∑ t=1 
(Ex∼ρi [−fh + rh + Phfh+1]) 2 ≤ ϵ2, 
|Ex∼µ[−fh − (−Th)(−fh+1)]| = |Ex∼µ[−fh + rh + Phfh+1]| > ϵ, 
which again implies µ is independent of ρ1, . . . , ρm with respect to dimBE(F ,Π, ϵ). 
We have shown that if µ be independent of ρ1, . . . , ρm with respect to dimBE(F̃ ,Π, ϵ), then µ is also independent of ρ1, . . . , ρm with respect to dimBE(F ,Π, ϵ). Therefore, the length of the longest independent sequence in dimBE(F ,Π, ϵ) 
must be equal or longer than that in dimBE(F̃ ,Π, ϵ), i.e., dimBE(F̃ ,Π, ϵ) ≤ dimBE(F ,Π, ϵ). 
The Second step is to investigate the difference between two BE dimensions for different Bellman operators. Before we proceed, we define the gap in the definition of ϵ-independence between distributions. 
It turns out that if the variation of the transitions and rewards are smaller than the gap δ̃uϵ , which will be defined later, then two BE dimensions induced by difference Bellman operators are comparable, as summarized in the following theorem. 
Lemma A.3. Suppose there are two MDP instances with Bellman operator T 1 h and T 2 
h , where h ∈ [H]. Let δ̃uϵ be the universal gap with respect to (I − T̃ 2 
h )F̃ (see Definition 3.5). Then, if the variation of two instances is relatively small compared to the universal gap δ̃ satisfying 
max h 
√ 6mmaxH 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) + 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) ≤ δ̃uϵ , 
13
Non-stationary RL under General Function Approximation 
where mmax = dimBE((I − T 2 h )F ,Π, ϵ), then 
dimDE((I − T 2 h )F ,Π, ϵ) ≤ dimDE((I − T 1 
h )F ,Π, ϵ), 
and 
dimDE(((I − T 2 h )F) ∪ ((I − T 1 
h )F),Π, ϵ) = dimDE((I − T 1 h )F ,Π, ϵ), 
Proof. Fix h ∈ [H]. Let µ1, . . . , µm be independent sequence with respect to (I − T̃ 2 h )F̃ . By the definition of BE 
dimension, m ≤ dimBE((I − T̃ 2 h )F̃ ,Πh, ϵ). If we can show µ1, . . . , µm is also an independent sequence with respect to 
(I − T̃ 1 h )F̃ , then the longest independent sequence with respect to (I − T̃ 1 
h )F̃ must be equal or longer than that with respect to (I − T̃ 2 
h )F̃ and the proof is complete. In the following, we will focus on proving this argument. 
By the condition, there exists ϵ′ ≥ ϵ such that for all i ∈ [m] we have 
i−1∑ t=1 
(Eµt [f i 
h − T 2 h f 
i h+1]) 
2 ≤ ϵ′2, 
|Eµi [f i 
h − T 2 h f 
i h+1]| ≥ ϵ′ + δ̃i;µ1,...,µi 
. 
Here, with a little abuse of notation, the subscript i of δ̃i;µ1,...,µi represents the function f i h − T 2 
h f i h+1. 
By Lemma A.5, we have 
i−1∑ t=1 
(Ex∼µt [f i 
h − T 1 h f 
i h]) 
2 ≤ ϵ′2 + 6mH 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) 
≤ 
( ϵ′ + 
√ 6mH 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
))2 
. (11) 
We point it out that both the (f i, T 1 h ) from (I − Th)F and (−f i,−T i 
h ) from −(I − Th)F satisfy the above inequality. 
Next, consider 
min 
{∣∣∣∣∣∣Ex∼P [fh − r2h − P 2 hfh+1] 
∣∣− ∣∣Ex∼P [fh − r1h − P 1 hfh+1] 
∣∣∣∣∣∣,∣∣∣∣∣∣Ex∼P [−fh − (−r2h)− P 2 h (−fh+1)] 
∣∣− ∣∣Ex∼P [fh − r1h − P 1 hfh+1] 
∣∣∣∣∣∣}. The first argument in the min function corresponds to the difference between pair (f, T 1 
h ) and (f, T 2 h ) while the second one 
is the difference between pair (f, T 1 h ) and (−f,−T 2 
h ). 
If (Ex∼P [fh − r2h − P 2 hfh+1)(Ex∼P [fh − r1h − P 1 
hfh+1]) ≥ 0, then by Lemma A.6, the first argument in the min function is upper bounded by supx,a |r1h − r2h|+TV(P 1 
h , P 2 h ). 
If (Ex∼P [fh− r2h−P 2 hfh+1)(Ex∼P [fh− r1h−P 1 
hfh+1]) < 0, then by Lemma A.6, the second argument is upper bounded by supx,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ). 
Therefore, the quantity we considered is upper bounded by supx,a |r1h − r2h| +H · TV(P 1 h , P 
2 h ). By triangle inequality, 
either ∣∣Ex∼µ1 [f i 
h − T 1 h f 
i h] ∣∣ ≥ ∣∣Ex∼µ1 
[f i h − T 2 
h f i h] ∣∣− (sup 
x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) ≥ ϵ′ + δ̃i;µ1,...,µi 
− ( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) (12) 
holds or ∣∣Ex∼µ1 [−f i 
h − (−T 1 h )(−f i 
h)] ∣∣ ≥ ∣∣Ex∼µ1 
[f i h − T 2 
h f i h] ∣∣− (sup 
x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) 14
Non-stationary RL under General Function Approximation 
≥ ϵ′ + δ̃i;µ1,...,µi − ( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) (13) 
holds. 
Recall δ̃uϵ is the universal gap with respect to (I − T̃ 2 h )F̃ (see Definition 3.5), and mmax = dimBE((I − T̃ 2 
h )F̃ ,Πh, ϵ). If it holds that 
max h 
√ 6mmaxH 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) + 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
) ≤ δ̃uϵ , 
which implies 
γ = 
( ϵ′ + 
√ 6mH 
( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
)) − ( ϵ′ + δ̃i;µ1,...,µi 
− ( sup x,a |r1h − r2h|+H · TV(P 1 
h , P 2 h ) 
)) ≥ 0. 
The above inequality together with (11)-(13) shows that for the sequence µ1, . . . , µi, there exists a function g from (I−T̃ 1 h )F̃ , 
and a ϵ̃ ∈ [ϵ′, ϵ′ + γ) satisfying ϵ̃ ≥ ϵ such that 
i−1∑ t=1 
(Eµt [g])2 ≤ ϵ̃2, 
|Eµi [g]| > ϵ̃. 
The above argument holds for all i ∈ [m] and we conclude that µ1, . . . , µm is again an independent sequence with respect to (I − T̃ 1 
h )F̃ . The proof for the first inequality is complete by noting that dimBE(F̃ ,Π, ϵ) = dimBE(F ,Π, ϵ) by Lemma A.2. 
For the second inequality, we are left to show dimDE(((I −T 2 h )F)∪ ((I −T 1 
h )F),Π, ϵ) ≤ dimDE((I −T 1 h )F ,Π, ϵ). The 
proof is by showcasing every independence sequence with respect to ((I −T 2 h )F)∪ ((I −T 1 
h )F) must also be independent with respect to (I − T 1 
h )F , which follows exactly the same argument as above and is omitted here. 
The Step three is to build connection between BE dimension to DBE dimension when the variations in transitions and rewards are small. In general, DBE dimension could be substantially larger than BE dimension of one MDP instance in the non-stationary MDPs. However, if the variation of all instances are small enough compared to the universal gap δ̃uk;ϵ with respect to (I − T k 
h )F for all k ∈ [2 : K], DBE dimension is indeed equal to BE dimension. The following proposition is an immediate result from Lemma A.3. 
Proposition A.4. If it holds that for all k, 
max h 
√ 6mkH 
( sup x,a |r1h − rkh|+H · TV(P 1 
h , P k h ) 
) + 
( sup x,a |r1h − rkh|+H · TV(P 1 
h , P k h ) 
) ≤ δ̃uk;ϵ, 
where mk = dimBE((I − T k h )F ,Π, ϵ), and δ̃uk;ϵ is the universal gap with respect to function class (I − T k 
h )F . Then 
dimDBE(F ,Π, ϵ) = dimDE((I − T 1 h )F ,Π, ϵ), 
where the latter is exactly the BE dimension for the first MDP instance. 
A.1. Supporting Lemmas 
Lemma A.5. Suppose fh ≤ H for all h, and r, r′ ≤ 1, we have∣∣∣(Ex∼P [fh − r − Pfh+1]) 2 − (Ex∼P [fh − r′ − P ′fh+1]) 
2 ∣∣∣ ≤ 6H 
( sup x,a 
(r − r′) + TV(P, P ′) 
) . 
15
Non-stationary RL under General Function Approximation 
Proof. Note that ∣∣∣(Ex∼P [fh − r − Pfh+1]) 2 − (Ex∼P [fh − r′ − P ′fh+1]) 
2 ∣∣∣ 
≤ 6H |Ex∼P [r − r′] + Ex∼P [(P − P ′)fh+1]| ≤ 6H (|Ex∼P [r − r′]|+H |Ex∼P [(P − P ′)fh+1]|) 
≤ 6H 
( sup x,a 
(r − r′) +H · TV(P, P ′) 
) . 
Lemma A.6. Suppose fh ≤ H for all h, and r, r′ ≤ 1, we have 
|Ex∼P [fh − r − Pfh+1]− Ex∼P [fh − r′ − P ′fh+1]| ≤ sup x,a 
(r − r′) +H · TV(P, P ′). 
Proof. Note that 
|Ex∼P [fh − r − Pfh+1]− Ex∼P [fh − r′ − P ′fh+1]| ≤ |Ex∼P [r − r′] + Ex∼P [(P − P ′)fh+1]| ≤ |Ex∼P [r − r′]|+ |Ex∼P [(P − P ′)fh+1]| ≤ sup 
x,a (r − r′) +H · TV(P, P ′). 
B. Proof of Propostion 3.8 
In this section, we show the DBE dimension of non-stationary linear MDP is Õ(d) where d is the feature dimension. 
Define m = dimDBE((I − Th)F ,DF,h, ϵ) and let h = argmaxh∈[H] dimDBE((I − Th)F ,DF , ϵ). 
Let µ1, . . . , µm be an independent sequence with respect to (I − Th)F . By definition, there exists (f1, T 1), . . . , (f i, T i) such that for all i ∈ [m], we have 
i−1∑ t=1 
( E 
(x,a)∼µt 
[ (f i 
h − T i−1 h f i 
h+1)(x, a) ])2 
≤ ϵ2, and∣∣∣∣ E (x,a)∼µi 
[ (f i 
h − T i−1 h f i 
h+1)(x, a) ]∣∣∣∣ > ϵ. 
We aim to show m = Õ(d). 
For linear MDP, a natural function class Fh is 
{f ∈ ((S ×A) 7→ [0, H − h+ 1]) : ϕ(x, a)⊤wh, ∥ϕ(x, a)∥ ≤ 1,∀(x, a) and ∥wh∥ ∈ 2(H − h+ 1) √ d}. 
Note that 
(f i h − T i−1 
h f i h+1)(x, a) = ϕ(x, a)⊤(whi − w̃h,i), 
where w̃h,i = θh,i−1 + ∫ x′ µh,i−1(x 
′)maxa f i h+1(x 
′, a) and we have max{∥wh,i∥ , ∥w̃h,i∥} ≤ 2H √ d for all h ∈ [H]. 
Therefore, for all i ∈ [m] 
i−1∑ t=1 
( E 
(x,a)∼µt 
[ ϕ(x, a)⊤(w̃i 
h − wi−1 h ) 
])2 
≤ ϵ2, and 
16
Non-stationary RL under General Function Approximation∣∣∣∣ E (x,a)∼µi 
[ ϕ(x, a)⊤(w̃i 
h − wi−1 h ) 
]∣∣∣∣ > ϵ. 
For ease of exposition, we set 
xi = w̃i h − wi−1 
h , zi = E (x,a)∼µi 
[ϕ(x, a)], Vi = 
i−1∑ t=1 
ztzt ⊤ + 
ϵ2 
ζ · I, 
where ζ = 4H √ d. 
The previous argument implies that for all i ∈ [m], 
∥xi∥Vi ≤ √ 2ϵ, 
∥xi∥Vi · ∥zi∥V−1 
i > ϵ. 
Therefore, we have ∥zi∥V−1 i ≥ 1√ 
2 . 
By matrix determinant lemma, 
det[Vm] = det[Vm−1] ( 1 + ∥zm∥2V−1 
m 
) ≥ · · · ≥ ( 
3 
2 )m−1( 
ϵ2 
ζ )d. 
Moreover, 
det[Vm] ≤ ( tr[Vm] 
d 
)d 
≤ ( ζ(m− 1) 
d + 
ϵ2 
ζ 
)d 
. 
Therefore, 
( 3 
2 )m−1 ≤ 
( ζ2(m− 1) 
dϵ2 + 1 
)d 
. 
Taking logarithm on both sides gives 
m ≤ 4 
[ 1 + d log 
( ζ2(m− 1) 
dϵ2 + 1 
)] , 
which implies 
m ≤ O ( 1 + d log 
( ζ2 
ϵ2 + 1 
)) . 
C. Proofs of SW-OPEA In this section, we provide the formal Proof of Theorem 5.2. 
C.1. Proof of Theorem 5.2 
We decompose the dynamic regret in the following way 
D− Regret(k) = 
k∑ t=1 
( V π(∗,t) 
1;(∗,t) − V πt 
1;(∗,t) 
) (x1) 
= 
k∑ t=1 
( V π(∗,t) 
1;(∗,t) − V π(∗,t−1) 
1;(∗,t−1) + V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) + V πt 
1;(∗,t−1) − V πt 
1;(∗,t) 
) (x1) 
17
Non-stationary RL under General Function Approximation 
= ( V π(∗,k) 
1;(∗,k) − V π(∗,0) 
1;(∗,0) 
) (x1) + 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1) 
+ 
k∑ t=1 
H∑ h=1 
( E 
(xh,ah)∼(πt,(∗,t−1)) [rt−1 
h (xh, ah)]− E (xh,ah)∼(πt,(∗,t)) 
[rth(xh, ah)] 
) 
≤ H + 
k∑ t=1 
H∑ h=1 
( E 
(xh,ah)∼(πt,(∗,t−1)) [(rt−1 
h − rth)(xh, ah)] 
) ︸ ︷︷ ︸ 
(I) 
+ 
k∑ t=1 
H∑ h=1 
(( E 
(xh,ah)∼(πt,(∗,t−1)) − E 
(xh,ah)∼(πt,(∗,t)) 
) [rth(xh, ah)] 
) ︸ ︷︷ ︸ 
(II) 
+ 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1)︸ ︷︷ ︸ 
(III) 
. 
By the definition of variation in rewards (3), we have (I) ≤ ∆R(k). 
We bound (II) using the following lemma. Lemma C.1. Fix (k, h) ∈ [K]× [H], we have( 
E (xh,ah)∼(πk,(∗,k−1)) 
− E (xh,ah)∼(πk,(∗,k)) 
) [rkh(xh, ah)] ≤ 
h−1∑ i=1 
∥∥Pk−1 i − Pk 
i 
∥∥ ∞ . 
Moreover, 
k∑ t=1 
H∑ h=1 
( E 
(xh,ah)∼(πt,(∗,t−1)) − E 
(xh,ah)∼(πt,(∗,t)) 
) [rth(xh, ah)] ≤ H∆P (k). 
The proof of C.1 is provided in Appendix C.3. 
Therefore, 
D− Regret(k) = H +∆R(k) +H∆P (k) + 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1)︸ ︷︷ ︸ 
(III) 
. 
Before we proceed, we present the next two lemmas. 
Lemma C.2. If β = cH2 log KH|G| δ , then with probability at least 1− δ, we have Q∗ 
(∗,k) ∈ B k for all k ∈ [K]. 
Lemma C.3. If β = cH2 log KH|G| δ , then with probability at least 1− δ, for all (k, h) ∈ [K]× [H], we have 
k−1∑ t=1∨(k−w−1) 
[ fk h (s 
t h, a 
t h)− rk−1 
h (sth, a t h)− E 
x′∼Pk−1 h (xt 
h,a t h) max a′∈A 
fk h+1(s 
′, a′) 
]2 ≤ 6H2∆w 
P (k − 1, h) +O(β). 
The proofs of Lemma C.2 and C.3 are based on martingale concentration and provided in Appendix C.4. 
By Lemma C.2, with probability at least 1− δ, we have 
(III) = 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1) 
18
Non-stationary RL under General Function Approximation 
≤ k∑ 
t=1 
( max a∈A 
f t 1(x1, a)− V πt 
1;(∗,t−1)(x1) 
) 
≤ H∑ 
h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)], 
where the first inequality follows from Lemma C.2 and the optimistic planning step (line 3) in Algorithm 4 which guarantees that V ∗ 
1;(∗,k−1) ≤ supa f k 1 (x1, a) for every episode k, the last inequality follows from generalized policy loss decomposition 
(Lemma C.8) and the fact that πk = πfk (line 3 in Algorithm 4). 
The next lemma is adapted from ((Jin et al., 2021)) and the proof can be found in Appendix C.5. 
Lemma C.4. Given a function class Φ defined on X with |ϕ(x)| ≤ C for all (g, x) ∈ Φ×X , and a family of probability measures Π over X . Suppose {ϕk}k∈[K] ⊆ Φ and {µk}k∈[K] ⊆ Π satisfy that for all k ∈ [K], 
∑k−1 t=1 (Ex∼µt 
[ϕk(x)]) 2 ≤ β. 
Then for all k ∈ [K] and ω > 0, 
k∑ t=1∨(k−w) 
|Ex∼µt [ϕt(x)]| 
≤ O (√ 
dimDE(Φ,Π, θ)β[k ∧ (w + 1)] + min{w + 1, k, dimDE(Φ,Π, θ)}C + [k ∧ (w + 1)]θ ) . 
We invoke Lemma 5.5 and Lemma C.3 with 
θ = 
√ 1 
w ,C = H, 
X = S ×A,Φ = (I − Th)F , and Π = D∆,h, 
ϕk = fk h − T k−1 
h fk h+1, µk = 1{· = (xk 
h, a k h)} 
and obtain 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ k∑ 
t=1 
(f t h − T t−1 
h f t h+1)(x 
t h, a 
t h) +O 
(√ k log(k) 
) 
≤ O 
 k 
w 
√√√√w · dimDBE(F ,D∆,h, √ 
1/w) 
( H2 log[KH|G|/δ] +H2 sup 
t∈[k] 
∆w P (t, h) 
) + √ w 
 ≤ O 
( Hk√ w 
√ d log[kH|G|/δ] + Hk√ 
w 
√ d sup t∈[k] 
∆w P (t, h) + 
√ w 
) , 
where the second inequality follows from Azuma-Hoeffding inequality, and in the last inequality, we use √ a+ b ≤ 
√ a+ √ b 
for any positive a, b ≥ 0 and we define d = dimDBE(F ,D∆,h, √ 
1/w). 
Summing over step h ∈ [H] gives 
H∑ h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ O 
( H2k√ 
w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d sup t∈[k] 
∆w P (t, h) +H 
√ w 
) , 
which completes the proof. 
19
Non-stationary RL under General Function Approximation 
C.2. Proof of Corollary 5.3 
For ease of exposition, let d = dimDBE(F ,D∆,h, √ 1/w). We adopt average variation L defined in (5). Then we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ Õ ( H2K√ 
w 
√ d √ 
log |G|+ H2K√ w 
√ dLw2 +H 
√ w 
) ≤ Õ 
( H2K 
√ d 
(√ log |G|√ w 
+ ( √ L+ 
1 
HK √ d ) √ w 
)) . 
Note first that √ 
log |G|√ L+ 1 
HK √ 
d 
> 1 when |G| > 10. 
If √ 
log |G|√ L+ 1 
HK √ 
d 
≥ K, i.e., √ L ≤ 1 
K 
(√ log |G| − 1 
H √ d 
) , we select w = K and we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] ≤ Õ 
( H2K 
1 2 d 
1 2 (log |G|) 1 
2 
) . 
If √ 
log |G|√ L+ 1 
HK √ 
d 
< K, i.e., √ L > 1 
K 
(√ log |G| − 1 
H √ d 
) , we select w = ⌈ 
√ log |G|√ 
L+ 1 
HK √ 
d 
⌉ and we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] ≤ Õ 
( H2KL 
1 4 d 
1 2 (log |G|) 1 
4 +H 3 2K 
1 2 d 
1 4 (log |G|) 1 
4 
) . 
C.3. Proof of Lemma C.1 
Proof. Fix (k, h) ∈ [K] × [H], define reward function r̃h′ = rkh(x, a)1{h′ = h} for all h′ ∈ [H]. For an episodic MDP (S,A, H, P k, r̃, x1) where {P k 
h′}h′∈[H] and {r̃h′}h′∈[H], the state value function and state-action value function of policy {πh′}h′∈[H] are Ṽ π 
h′;,(∗,k) and Q̃π h′;,(∗,k). Clearly, we have( 
E (xh,ah)∼(πk,(∗,k−1)) 
− E (xh,ah)∼(πk,(∗,k)) 
) [rkh(xh, ah)] = 
( Ṽ πk 
1;(∗,k−1) − Ṽ πk 
1;(∗,k) 
) (x1). 
For any function f : S ×A → R and any (k, h, x) ∈ [K]× [H]× S , define the following operator 
(Jk,hf)(x) = ⟨f(x, ·), πk h(·|x)⟩. 
Note that 
Ṽ πk 
1;(∗,k−1) − Ṽ πk 
1;(∗,k) 
= Jk,1 ( Q̃πk 
1;(∗,k−1) − Q̃πk 
1;(∗,k) 
) = Jk,1 
( Pk−1 1 Ṽ πk 
2;(∗,k−1) − Pk 1 Ṽ 
πk 
2;(∗,k) 
) = Jk,1Pk−1 
1 
( Ṽ πk 
2;(∗,k−1) − Ṽ πk 
2;(∗,k) 
) + Jk,1 
( Pk−1 1 − Pk 
1 
) Ṽ πk 
2;(∗,k) 
= 
h∏ i=1 
( Jk,iPk−1 
i 
) ( Ṽ πk 
h+1;(∗,k−1) − Ṽ πk 
h+1;(∗,k) 
) ︸ ︷︷ ︸ 
=0 
+ 
h∑ i=1 
i−1∏ ℓ=1 
( Jk,ℓPk−1 
ℓ 
) Jk,i 
( Pk−1 i − Pk 
i 
) Ṽ πk 
i+1,(∗,k) 
= 
h−1∑ i=1 
i−1∏ ℓ=1 
( Jk,ℓPk−1 
ℓ 
) Jk,i 
( Pk−1 i − Pk 
i 
) Ṽ πk 
i+1,(∗,k). 
20
Non-stationary RL under General Function Approximation 
where in the second equality we use the fact that reward r̃ is identical. I.e.,( Ṽ πk 
1;(∗,k−1) − Ṽ πk 
1;(∗,k) 
) (x1) 
= 
h−1∑ i=1 
E (xi,ai)∼(πk,(∗,k−1)) 
[(( Pk−1 i − Pk 
i 
) Ṽ πk 
i+1,(∗,k) 
) (xi, ai) 
] ≤ 
h−1∑ i=1 
sup x,a 
∥∥P k−1 i (·|x, a)− P k 
i (·|x, a) ∥∥ 1 
Therefore, 
k′∑ k=1 
H∑ h=1 
( E 
(xh,ah)∼(πk,(∗,k−1)) − E 
(xh,ah)∼(πk,(∗,k)) 
) [rkh(xh, ah)] 
≤ k′∑ 
k=1 
H∑ h=1 
h−1∑ i=1 
sup x,a 
∥∥P k−1 i (·|x, a)− P k 
i (·|x, a) ∥∥ 1 
≤ k′∑ 
k=1 
H∑ h=1 
H∑ i=1 
sup x,a 
∥∥P k−1 i (·|x, a)− P k 
i (·|x, a) ∥∥ 1 
≤ H∑ 
h=1 
 k′∑ k=1 
H∑ i=1 
sup x,a 
∥∥P k−1 i (·|x, a)− P k 
i (·|x, a) ∥∥ 1 
 ≤ H∆P (k 
′). 
C.4. Proofs of concentration lemmas 
The Freedman’s inquaulity controls the sum of martingale difference by the sum of their variance. 
Lemma C.5 (Freedman’s inequality ((Jin et al., 2021))). Let {Zt}t∈[T ] be a real-valued martingale difference sequence adapted to filtration Ft, and let Et[·] = E[·|Ft]. If |Zt| ≤ R almost surely, then for any η ∈ (0, R), it holds that with probability at least 1− δ, 
T∑ t=1 
Zt ≤ O 
( η 
T∑ t=1 
Et−1[Z 2 t ] + 
log(δ−1) 
η 
) . 
C.4.1. PROOF OF LEMMA C.2 
Proof. Define 
#k,h(x t h, a 
t h) := rkh(s 
t h, a 
t h) + E 
x′∼P t h(·|x 
t h,a 
t h) max a′∈A 
Qh+1;(∗,k)(x ′, a′). 
Fix a tuple (k, h, g) ∈ [K]× [H]× G. Let 
Wt(h, f) : = 
[ gh(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′)) 
]2 − [ #k,h(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′)) 
]2 = [gh(x 
t h, a 
t h)−#k,h(x 
t h, a 
t h)] 
[ gh(x 
t h, a 
t h) + #k,h(x 
t h, a 
t h)− 2 
( rkh +max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
)] and Ft,h be the filtration induced by {xi 
1, a i 1, · · · , xi 
H}i∈[t−1] ∪ {xt 1, a 
t 1, · · · , xt 
h, a t h} ∪ {rih} 
i∈[t−1] h∈[H] . We have 
E[Wt(h, g)|Ft,h] = [ (gh −#k,h) (x 
t h, a 
t h) ]2 
, 
21
Non-stationary RL under General Function Approximation 
Var[Wt(h, g)|Ft,h] ≤ 36H2E[Wt(h, g)|Ft,h]. 
By Freedman’s inequality, with probability at least 1− δ,∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√log(1/δ) 
k∑ t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + log(1/δ) 
 . 
Taking union bound over [K]× [H]× G,∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√ι k∑ 
t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + ι 
 , 
where ι = log(HK|G|/δ). We have 
− k∑ 
t=1∨(k−w) 
Wt(h, g) 
≤ − k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2 
+O 
H 
√√√√ι 
k∑ t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + ι 
 ≤ O(H2ι). 
I.e., 
k∑ t=1∨(k−w) 
[ #k,h(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 
≤ k∑ 
t=1∨(k−w) 
[ gh(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 +O(H2ι). 
Therefore, 
k∑ t=1∨(k−w) 
[ Qh;(∗,k)(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 
≤ k∑ 
t=1∨(k−w) 
[ #k,h(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k, h) 
≤ k∑ 
t=1∨(k−w) 
[ gh(x 
t h, a 
t h)− rkh −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k, h) +O(H2ι), 
where the first inequality follows from Lemma C.7 and Eqn. (2). By the definition of Bk and β = cH2 log KH|G| δ with some 
large absolute constant c, we conclude that with probability at least 1− δ, Q(∗,k) ∈ Bk for all k ∈ [K]. 
22
Non-stationary RL under General Function Approximation 
C.4.2. PROOF OF LEMMA C.3 
Proof. Define 
#f k,h(x 
t h, a 
t h) = rkh(s 
t h, a 
t h) + E 
x′∼P t h(x 
t h,a 
t h) max a′∈A 
fh+1(s ′, a′). 
Fix a tuple (k, h, f) ∈ [K]× [H]× G. Let 
Wt(h, f) : = 
[ fh(x 
t h, a 
t h)− rkh −max 
a′∈A fh+1(x 
t h+1, a 
′) 
]2 − [ #f 
k,h(x t h, a 
t h)− rkh −max 
a′∈A fh+1(x 
t h+1, a 
′) 
]2 = [fh(x 
t h, a 
t h)−#f 
k,h(x t h, a 
t h)] 
[ fh(x 
t h, a 
t h) + #f 
k,h(x t h, a 
t h)− 2 
( rkh +max 
a′∈A fh+1(x 
t h+1, a 
′) 
)] and Ft,h be the filtration induced by {xi 
1, a i 1, · · · , xi 
H}i∈[t−1] ∪ {xt 1, a 
t 1, · · · , xt 
h, a t h} ∪ {rih} 
i∈[t−1] h∈[H] . We have 
E[Wt(h, f)|Ft,h] = [( 
fh −#f k,h 
) (xt 
h, a t h) ]2 
, 
Var[Wt(h, f)|Ft,h] ≤ 36H2E[Wt(h, g)|Ft,h]. 
By Freedman’s inequality, we have∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, f)− k∑ 
t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√log(1/δ) 
k∑ t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2 
+ log(1/δ) 
 . 
Taking union bound over [K]× [H]× G, we have∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2∣∣∣∣∣∣ ≤ O 
H 
√√√√ι 
k∑ t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2 
+ ι 
 , 
where ι = log(KH|G|/δ). 
Note that 
k−1∑ t=1∨(k−w−1) 
Wt(h, f k) 
= 
k−1∑ t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
− k−1∑ 
t=1∨(k−w−1) 
[ #fk 
k−1,h(x t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
≤ k−1∑ 
t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
− k−1∑ 
t=1∨(k−w−1) 
[ T k−1 h fk 
h+1(x t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k − 1, h) 
≤ k−1∑ 
t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
23
Non-stationary RL under General Function Approximation 
− inf g∈G 
k−1∑ t=1∨(k−w−1) 
[ gh(x 
t h, a 
t h)− rk−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k − 1, h) 
≤ β + 4H2∆w P (k − 1, h), 
where the first inequality follows from Lemma C.7 and Eqn. (2), the second inequality follows from Assumption 5.1, and the last inequality follows from the definition of Bk−1. 
Therefore, 
k−1∑ t=1∨(k−w−1) 
[ (fk 
h −#fk 
k−1,h)(x t h, a 
t h) ]2 ≤ β + 4H2∆w 
P (k − 1, h) +O ( H2ι 
) . 
Finally, we use Lemma C.7 once more and obtain 
k−1∑ t=1∨(k−w−1) 
[ (fk 
h − T k−1 h fk 
h+1)(x t h, a 
t h) ]2 
≤ k−1∑ 
t=1∨(k−w−1) 
[ (fk 
h −#fk 
k−1,h)(x t h, a 
t h) ]2 
+ 2H2∆w P (k − 1, h) 
≤ 6H2∆w P (k − 1, h) +O(β). 
C.5. Proof of Lemma 5.5 
The proof in the subsection essentially follows the same arguments as in (Jin et al., 2021), and we adapt it to the sliding window scenario. 
Lemma C.6. Given a function class Φ defined on X × Y , and a family of probability measures Π over X . Suppose sequence {ϕk}k∈[K] ⊆ Φ and {µk}k∈[K] ⊆ Π satisfy that for all k ∈ [K], 
∑k−1 t=1∨(k−w−1)(Ex∼µt [ϕk(x)]) 
2 ≤ β. Then for all k ∈ [K], 
k∑ t=1∨(k−w) 
1{|Ex∼µt [ϕt(x)]| > ϵ} ≤ ( 
β 
ϵ2 + 1) dimDE(Φ,Π, ϵ) 
Proof. First, suppose for all k ∈ [κ], ∑k−1 
t=1 (Ex∼µt [ϕk(x)]) 
2 ≤ β, we show that if for some k ∈ [κ] we have |Ex∼µk 
[ϕk(x)]| > ϵ, then µk is ϵ-dependent on at most ⌈β/ϵ2⌉ − 1 disjoint subsequences in {µ1, . . . , µk−1}. By definition of GDE, if |Ex∼µk 
[ϕk(x)]| > ϵ and µk is ϵ-dependent on a subsequence {ν1, . . . , νℓ} of {µ1, . . . , µk−1}, then we should have 
∑ℓ t=1(Ex∼νt 
[ϕk(x)]) 2 > ϵ2. It implies that if µk is ϵ-dependent on L disjoint subsequences in {µ1, . . . , µk−1}, we 
have 
β ≥ k−1∑ 
t=1∨(k−w−1) 
(Ex∼µt [ϕk(x)]) 
2 > Lϵ2, 
which implies L ≤ ⌈β/ϵ2⌉ − 1. 
Second, we show that for any sequence {ν1, . . . , νκ} ⊆ Π, there exists j ∈ [κ] such that νj is ϵ-dependent on at least L = ⌈(κ− 1)/ dimDE(Φ,Π, ϵ)⌉ disjoint subsequences in {ν1, . . . , νj−1}. We prove the argument by the following artificial procedure: we start with singleton sequences B1 = {ν1}, B2 = {ν2}, . . ., BL = {νL} and j = L+ 1. For each j, if νj is ϵ-dependent on B1, B2, . . . , BL, we already achieved the goal and we stop; otherwise, we pick an i ∈ [L] such that νj is ϵ-independent of Bi and update Bi ∪ {νj}. Then we increment j by 1 continue this process. By the definition of GDE dimension, the size of each B1, B2, . . . , BL cannot get bigger than dimDE(Φ,Π, ϵ) at any point in this process. Therefore, the process stops before or on j = LdimDE(Φ,Π, ϵ) + 1 ≤ κ. 
24
Non-stationary RL under General Function Approximation 
Now fix k ∈ [K] and let {ν1, . . . , νκ} be the subsequence of {µ1∨(k−w), . . . , µk}, consisting of elements for which |Ex∼µt [|ϕt(x)]| > ϵ and the corresponding bijective function is θ : [κ] 7→ [1 ∨ (k − w) : k]. Note that for all ℓ ∈ [κ], we have |Ex∼νℓ 
[|ϕθ(ℓ)(x)]| > ϵ and 
ℓ−1∑ t=1 
(Ex∼νt [ϕθ(ℓ)(x)]) ≤ 
θ(ℓ)−1∑ t=1∨θ(ℓ)−w−1 
(Ex∼µt [ϕθ(ℓ)(x)]) ≤ β. 
Using the first claim, we know that each νj is ϵ-dependent on at most L < ⌈β/ϵ2⌉ − 1 disjoint subsequences of {ν1, ν2, . . . , νj−1}. Using the second claim, we know that there exists j ∈ [κ] such that νj is ϵ-dependent on at least ⌈(κ− 1)/ dimDE(Φ,Π, ϵ)⌉ disjoint subsequences of {ν1, ν2, . . . , νj−1}. Therefore, we have ⌈(κ− 1)/ dimDE(Φ,Π, ϵ)⌉ ≤ ⌈β/ϵ2⌉ − 1, which implies 
κ < ( β 
ϵ2 + 1) dimDE(Φ,Π, ϵ). 
Proof of Lemma 5.5. Fix k ∈ [K] and let d = dimDE(Φ,Π, ϵ). Sort the sequence{ |Ex∼µ1∨(k−w) 
[ϕ1∨(k−w)(x)]|, . . . , |Ex∼µk [ϕk(x)]| 
} in decreasing order and denote it by {e1, e2, . . . , ek∧(w+1)} (e1 ≥ e2 ≥ · · · ≥ ek∧(w+1)). Note that 
k∑ t=1∨(k−w) 
|Ex∼µt [ϕt(x, y)]| = k∧(w+1)∑ 
t=1 
et = 
k∧(w+1)∑ t=1 
et1{et ≤ θ}+ k∧(w+1)∑ 
t=1 
et1{et > θ} 
≤ [k ∧ (w + 1)]θ + 
k∧(w+1)∑ t=1 
et1{et > θ} 
For t ∈ [k], we show that if et > θ, then we have et ≤ min{ √ 
dβ t−d , C}. Assume t ∈ [k] satisfies et > θ. Then there exists 
an α such that et > α ≥ θ. By Lemma C.6, we have 
t ≤ k∧(w+1)∑ 
i=1 
1{ei > α} ≤ ( β 
α2 + 1) dimDE(Φ,Π, α) ≤ ( 
β 
α2 + 1) dimDE(Φ,Π, ω), 
which implies α ≤ √ 
dβ t−d . Letting α→ et, we have et ≤ 
√ dβ t−d . Besides, recall et ≤ C, so we have et ≤ min{ 
√ dβ t−d , C}. 
Finally, we have 
k∧(w+1)∑ t=1 
et1{et > ω} ≤ min{d, k, w + 1}C + 
k∧(w+1)∑ t=d+1 
√ dβ 
t− d 
≤ min{d, k, w + 1}C + √ dβ 
∫ k∧(w+1) 
0 
1√ t dt 
= min{d, k, w + 1}C + 2 √ dβ[k ∧ (w + 1)]. 
C.6. Auxiliary Lemmas 
Lemma C.7. Suppose P and Q are two probability distributions of a random variable x, then∣∣∣∣∣( E x∼P 
f(x)− C )2 − ( 
E x∼Q 
f(x)− C 
)2 ∣∣∣∣∣ ≤ (2fm + 2|C|)fm · TV(P,Q), 
where fm = supx |f(x)|. 
25
Non-stationary RL under General Function Approximation 
Proof. Note that ∣∣∣∣∣( E x∼P 
f(x)− C )2 − ( 
E x∼Q 
f(x)− C 
)2 ∣∣∣∣∣ 
= 
∣∣∣∣( E x∼P 
f(x) + E x∼Q 
f(x)− 2C 
)( E 
x∼P f(x)− E 
x∼Q f(x) 
)∣∣∣∣ ≤ (2fm + 2|C|) 
∣∣∣∣∫ x 
f(x)(dP − dQ) 
∣∣∣∣ ≤ (2fm + 2|C|)fm · TV(P,Q). 
Lemma C.8 (Generalized policy loss decomposition). For any t, k, we have 
f t 1(x1, π 
t 1(x1))− V πt 
1;(∗,k)(x1) = 
H∑ h=1 
E (xh,ah)∼(πt,(∗,k)) 
[ (f t 
h − rh;(∗,k) − Pk hf 
t h+1)(xh, ah) 
] , 
where πt := πft , the greedy policy under function approximation f t. 
Proof. Note that 
H∑ h=1 
E (xh,ah)∼(πt,(∗,k)) 
[ (f t 
h − rh;(∗,k) − Pk hf 
t h+1)(xh, ah) 
] = 
H∑ h=1 
E (xh,ah,xh+1)∼(πt,(∗,k)) 
[ f t h(xh, ah)− rh;(∗,k)(xh, ah)−max 
a∈A f t h+1(xh+1, a) 
] 
= 
H∑ h=1 
E (xh,ah)∼(πt,(∗,k)) 
[ f t h(xh, ah)− rh;(∗,k)(xh, ah)− E 
(xh+1,ah+1)∼(πt,(∗,k)) [f t 
h+1(xh+1, ah+1)] 
] 
= E (x1:H ,a1:H)∼(πt,(∗,k)) 
[ H∑ 
h=1 
( f t h(xh, ah)− f t 
h+1(xh+1, ah+1) )] − E 
(x1:H ,a1:H)∼(πt,(∗,k)) 
[ H∑ 
h=1 
rh;(∗,k)(xh, ah) 
] = f t 
1(x1, π t 1(x1))− V πt 
1;(∗,k)(x1), 
where the second equality follows from πt = πft . 
D. Bandit Feedback We extend our algorithm to bandit feedback scenario, and the pseudocode is presented in Algorithm 2. In bandit feedback scenario, the reward function rkh(·, ·) is no long available, and the agent can only get access to the reward obtained from the trajectory. Therefore, the non-stationarity of rewards plays an important role in the construction of the sliding window Bellman error and the confidence set. Specifically, we replace the sliding window squared Bellman error (1) with 
LDh (ξh, ζh+1) = 
k∑ t=1∨(k−w) 
( ξh(x 
t h, a 
t h)− rth −max 
a′∈A ζh+1(x 
t h+1, a 
′) 
)2 
, 
where rth is the reward obtained at step h in episode t. Moreover, the local regression constraint is 
LDh (fh, fh+1) ≤ inf 
g∈Gh 
LDh (g, fh+1) + β + 2H2∆w 
P (k, h) + 2H∆w R(k, h), 
where β is a confidence parameter, ∆w P is the local variation budget defined in (2) and ∆w 
R is defined as 
∆w P (k, h) = 
k∑ t=1∨(k−w) 
sup x∈S,a∈A 
|(rkh − rth)(x, a)|. 
26
Non-stationary RL under General Function Approximation 
Algorithm 2 SW-OPEA (bandit feedback) 1: Input: D1, · · · ,DH ← ∅, B0 ← F . 2: for episode k from 1 to K do 3: Choose πk = πfk , 
where fk = argmaxf∈Bk−1 f1(x1, πf (x1)). 4: Collect a trajectory (xk 
1 , a k 1 , · · · , xk 
H , akH , xk H+1) by following πk and reward function {rkh}h∈[H]. 
5: Augment Dh = Dh ∪ {(xk h, a 
k h, x 
k h+1)}, ∀h ∈ [H]. 
6: Update Bk = {f ∈ F : LDh (fh, fh+1) ≤ infg∈Gh 
LDh (g, fh+1) + β + 2H2∆w 
P (k, h) + 2H∆w R(k, h), ∀h ∈ [H]}, 
where LDh (ξh, ζh+1) = 
∑k t=1∨(k−w) 
( ξh(x 
t h, a 
t h)− rth −maxa′∈A ζh+1(x 
t h+1, a 
′) )2 
7: end for 
D.1. Algorithm and Theorem Theorem D.1. Under Assumption 2.1 and Assumption 5.1, there exists an absolute constant c such that for any δ ∈ (0, 1], K ∈ N, if we choose β = cH2 log KH|G| 
δ in SW-OPEA, then with probability at least 1 − δ, for all k ∈ [K], when k ≥ min{w + 1,dimDBE(F ,D∆,h, 
√ 1/w)} we have 
D− Regret(k) =∆R(k) +H∆P (k) 
+O 
( H √ w + 
H2k√ w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d sup t∈[k] 
∆w P (t, h) + 
H3/2k√ w 
√ d sup t∈[k] 
∆w R(t, h) 
) . 
where d = dimDBE(F ,D∆,h, √ 1/w). 
D.2. Proof of Theorem 5.6 
Following the same argument in Appendix C gives 
D− Regret(k) = H +∆R(k) +H∆P (k) + 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1)︸ ︷︷ ︸ 
(I) 
. 
In the sequel, we strive to bound term (I). We first introduce a different probability distribution shift lemma. Compared to Lemma 5.4, the new lemma is more general and can handle the bandit feedback scenario. 
Lemma D.2. Suppose P and Q are two probability distributions of a random variable x, then∣∣∣∣∣( E x∼P 
f(x) + Eg1(y)− C )2 − ( 
E x∼Q 
f(x) + Eg2(y)− C 
)2 ∣∣∣∣∣ ≤ (2fm + 2gm + 2|C|)fm · TV(P,Q), 
where fm = supx |f(x)|, gm = maxi=1,2 supy gi(y). 
Proof. Note that∣∣∣∣∣( E x∼P 
f(x)− C )2 − ( 
E x∼Q 
f(x)− C 
)2 ∣∣∣∣∣ 
= 
∣∣∣∣( E x∼P 
f(x) + E x∼Q 
f(x) + Eg1(y) + Eg2(y)− 2C 
)( E 
x∼P f(x)− E 
x∼Q f(x) + Eg1(y)− Eg2(y) 
)∣∣∣∣ ≤ (2fm + 2gm + 2|C|) 
(∣∣∣∣∫ x 
f(x)(dP − dQ) 
∣∣∣∣+ sup y |g1(y)− g2(y)| 
) ≤ (2fm + 2gm + 2|C|)(fm · TV(P,Q) + sup 
y |g1(y)− g2(y)|). 
27
Non-stationary RL under General Function Approximation 
Thanks to Lemma D.2, we are able to obtain the following two lemmas. 
Lemma D.3. If β = cH2 log KH|G| δ , then with probability at least 1− δ, we have Q∗ 
(∗,k) ∈ B k for all k ∈ [K]. 
Proof. Define 
#k,h(x t h, a 
t h) := E[rth(sth, ath)] + E 
x′∼P t h(·|x 
t h,a 
t h) max a′∈A 
Qh+1;(∗,k)(x ′, a′). 
Fix a tuple (k, h, g) ∈ [K]× [H]× G. Let 
Wt(h, f) : = 
[ gh(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′)) 
]2 − [ #k,h(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′)) 
]2 = [gh(x 
t h, a 
t h)−#k,h(x 
t h, a 
t h)] 
[ gh(x 
t h, a 
t h) + #k,h(x 
t h, a 
t h)− 2 
( rth +max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
)] and Ft,h be the filtration induced by {xi 
1, a i 1, · · · , xi 
H}i∈[t−1] ∪ {xt 1, a 
t 1, · · · , xt 
h, a t h} ∪ {rih} 
i∈[t−1] h∈[H] . We have 
E[Wt(h, g)|Ft,h] = [ (gh −#k,h) (x 
t h, a 
t h) ]2 
, 
Var[Wt(h, g)|Ft,h] ≤ 36H2E[Wt(h, g)|Ft,h]. 
By Freedman’s inequality, with probability at least 1− δ,∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√log(1/δ) 
k∑ t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + log(1/δ) 
 . 
Taking union bound over [K]× [H]× G,∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√ι 
k∑ t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + ι 
 , 
where ι = log(HK|G|/δ). We have 
− k∑ 
t=1∨(k−w) 
Wt(h, g) 
≤ − k∑ 
t=1∨(k−w) 
[( gh(x 
t h, a 
t h)−#k,h 
) (xt 
h, a t h) ]2 
+O 
H 
√√√√ι 
k∑ t=1∨(k−w) 
[(gh(xt h, a 
t h)−#k,h) (xt 
h, a t h)] 
2 + ι 
 ≤ O(H2ι). 
I.e., 
k∑ t=1∨(k−w) 
[ #k,h(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 
≤ k∑ 
t=1∨(k−w) 
[ gh(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 +O(H2ι). 
28
Non-stationary RL under General Function Approximation 
Therefore, 
k∑ t=1∨(k−w) 
[ Qh;(∗,k)(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 
≤ k∑ 
t=1∨(k−w) 
[ #k,h(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k, h) + 2H∆w R(k, h) 
≤ k∑ 
t=1∨(k−w) 
[ gh(x 
t h, a 
t h)− rth −max 
a′∈A Qh+1;(∗,k)(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k, h) + 2H∆w R(k, h) +O(H2ι), 
where the first inequality follows from Lemma D.2 and the definition of ∆w P and ∆w 
P . By the definition of Bk and β = cH2 log KH|G| 
δ with some large absolute constant c, we conclude that with probability at least 1− δ, Q(∗,k) ∈ Bk for all k ∈ [K]. 
Lemma D.4. If β = cH2 log KH|G| δ , then with probability at least 1− δ, for all (k, h) ∈ [K]× [H], we have 
k−1∑ t=1∨(k−w−1) 
[ fk h (s 
t h, a 
t h)− rk−1 
h (sth, a t h)− E 
x′∼Pk−1 h (xt 
h,a t h) max a′∈A 
fk h+1(s 
′, a′) 
]2 ≤ 6H2∆w 
P (k − 1, h) + 6H∆w R(k − 1, w) +O(β). 
Proof. Define 
#f k,h(x 
t h, a 
t h) = E[rth(sth, ath)] + E 
x′∼P t h(x 
t h,a 
t h) max a′∈A 
fh+1(s ′, a′). 
Fix a tuple (k, h, f) ∈ [K]× [H]× G. Let 
Wt(h, f) : = 
[ fh(x 
t h, a 
t h)− rth −max 
a′∈A fh+1(x 
t h+1, a 
′) 
]2 − [ #f 
k,h(x t h, a 
t h)− rth −max 
a′∈A fh+1(x 
t h+1, a 
′) 
]2 = [fh(x 
t h, a 
t h)−#f 
k,h(x t h, a 
t h)] 
[ fh(x 
t h, a 
t h) + #f 
k,h(x t h, a 
t h)− 2 
( rth +max 
a′∈A fh+1(x 
t h+1, a 
′) 
)] and Ft,h be the filtration induced by {xi 
1, a i 1, · · · , xi 
H}i∈[t−1] ∪ {xt 1, a 
t 1, · · · , xt 
h, a t h} ∪ {rih} 
i∈[t−1] h∈[H] . We have 
E[Wt(h, f)|Ft,h] = [( 
fh −#f k,h 
) (xt 
h, a t h) ]2 
, 
Var[Wt(h, f)|Ft,h] ≤ 36H2E[Wt(h, g)|Ft,h]. 
By Freedman’s inequality, we have∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, f)− k∑ 
t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2∣∣∣∣∣∣ 
≤ O 
H 
√√√√log(1/δ) 
k∑ t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2 
+ log(1/δ) 
 . 
Taking union bound over [K]× [H]× G, we have∣∣∣∣∣∣ k∑ 
t=1∨(k−w) 
Wt(h, g)− k∑ 
t=1 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2∣∣∣∣∣∣ ≤ O 
H 
√√√√ι 
k∑ t=1∨(k−w) 
[ (fh −#f 
k,h)(x t h, a 
t h) ]2 
+ ι 
 , 
29
Non-stationary RL under General Function Approximation 
where ι = log(KH|G|/δ). 
Note that 
k−1∑ t=1∨(k−w−1) 
Wt(h, f k) 
= 
k−1∑ t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
− k−1∑ 
t=1∨(k−w−1) 
[ #fk 
k−1,h(x t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
≤ k−1∑ 
t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
− k−1∑ 
t=1∨(k−w−1) 
[ T k−1 h fk 
h+1(x t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k − 1, h) + 2H∆w R(k − 1, w) 
≤ k−1∑ 
t=1∨(k−w−1) 
[ fk h (x 
t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 
− inf g∈G 
k−1∑ t=1∨(k−w−1) 
[ gh(x 
t h, a 
t h)− rt−1 
h −max a′∈A 
fk h+1(x 
t h+1, a 
′) 
]2 + 2H2∆w 
P (k − 1, h) + 2H∆w R(k − 1, w) 
≤ β + 4H2∆w P (k − 1, h) + 4H∆w 
R(k − 1, w), 
where the first inequality follows from Lemma D.2 and the definition of ∆w P and ∆w 
P , the second inequality follows from Assumption 5.1, and the last inequality follows from the definition of Bk−1. 
Therefore, 
k−1∑ t=1∨(k−w−1) 
[ (fk 
h −#fk 
k−1,h)(x t h, a 
t h) ]2 ≤ β + 4H2∆w 
P (k − 1, h) + 4H∆w R(k − 1, w) +O 
( H2ι 
) . 
Finally, we use Lemma D.2 again and obtain 
k−1∑ t=1∨(k−w−1) 
[ (fk 
h − T k−1 h fk 
h+1)(x t h, a 
t h) ]2 
≤ k−1∑ 
t=1∨(k−w−1) 
[ (fk 
h −#fk 
k−1,h)(x t h, a 
t h) ]2 
+ 2H2∆w P (k − 1, h) + 2H∆w 
R(k − 1, w) 
≤ 6H2∆w P (k − 1, h) + 6H∆w 
R(k − 1, w) +O(β). 
By Lemma D.3, with probability at least 1− δ, we have 
(I) = 
k∑ t=1 
( V π(∗,t−1) 
1;(∗,t−1) − V πt 
1;(∗,t−1) 
) (x1) 
≤ k∑ 
t=1 
( max a∈A 
f t 1(x1, a)− V πt 
1;(∗,t−1)(x1) 
) 
30
Non-stationary RL under General Function Approximation 
≤ H∑ 
h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)], 
where the first inequality follows from Lemma D.3 and the optimistic planning step (line 3) in Algorithm 2 which guarantees that V ∗ 
1;(∗,k−1) ≤ supa f k 1 (x1, a) for every episode k, the last inequality follows from generalized policy loss decomposition 
(Lemma C.8) and the fact that πk = πfk (line 3 in Algorithm 2). 
Now we invoke Lemma 5.5 and Lemma D.4 with 
θ = 
√ 1 
w ,C = H, 
X = S ×A,Φ = (I − Th)F , and Π = D∆,h, 
ϕk = fk h − T k−1 
h fk h+1, µk = 1{· = (xk 
h, a k h)} 
and obtain 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ k∑ 
t=1 
(f t h − T t−1 
h f t h+1)(x 
t h, a 
t h) +O 
(√ k log(k) 
) 
≤ O 
 k 
w 
√√√√w · dimDBE(F ,D∆,h, √ 
1/w) 
( H2 log[KH|G|/δ] +H2 sup 
t∈[k] 
∆w P (t, h) +H sup 
t∈[k] 
∆w R(t, h) 
) + √ w 
 ≤ O 
( Hk√ w 
√ d log[kH|G|/δ] + Hk√ 
w 
√ d sup t∈[k] 
∆w P (t, h) + 
√ Hk√ w 
√ d sup t∈[k] 
∆w R(t, h) + 
√ w 
) , 
where the second inequality follows from Azuma-Hoeffding inequality, and in the last inequality, we use √ a+ b ≤ 
√ a+ √ b 
for any positive a, b ≥ 0 and we define d = dimDBE(F ,D∆,h, √ 
1/w). 
Summing over step h ∈ [H] gives 
H∑ h=1 
k∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ O 
( H2k√ 
w 
√ d log[KH|G|/δ] + H2k√ 
w 
√ d sup t∈[k] 
∆w P (t, h) + 
H3/2k√ w 
√ d sup t∈[k] 
∆w R(t, h) +H 
√ w 
) , 
which completes the proof. 
D.3. Proof of Corollary 5.7 
For ease of exposition, let d = dimDBE(F ,D∆,h, √ 
1/w). We adopt average variation L defined in (5) and average variation L in rewards defined in (10). Then we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ Õ 
( H2K√ 
w 
√ d √ log |G|+ H2K√ 
w 
√ dLw2 + 
H 3 2K√ w 
√ dLθw2 +H 
√ w 
) 
≤ Õ 
( H2K 
√ d 
(√ log |G|√ w 
+ ( √ L+ 
√ Lθ√ H 
+ 1 
HK √ d ) √ w 
)) . 
31
Non-stationary RL under General Function Approximation 
Note first that √ 
log |G| √ L+ 
√ Lθ√ H 
+ 1 
HK √ 
d 
> 1 when |G| > 10. 
If √ 
log |G| √ L+ 
√ Lθ√ H 
+ 1 
HK √ 
d 
≥ K, i.e., √ L+ 
√ Lθ√ H ≤ 1 
K 
(√ log |G| − 1 
H √ d 
) , we select w = K and we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] ≤ Õ 
( H2K 
1 2 d 
1 2 (log |G|) 1 
2 
) . 
If √ 
log |G| √ L+ 
√ Lθ√ H 
+ 1 
HK √ 
d 
< K, i.e., √ L+ 
√ Lθ√ H 
> 1 K 
(√ log |G| − 1 
H √ d 
) , we select w = ⌈ 
√ log |G| 
√ L+ 
√ Lθ√ H 
+ 1 
HK √ 
d 
⌉ and we have 
H∑ h=1 
K∑ t=1 
E (xh,ah)∼(πt,(∗,t−1)) 
[(f t h − T t−1 
h f t h+1)(xh, ah)] 
≤ Õ ( H2KL 
1 4 d 
1 2 (log |G|) 1 
4 +H 7 4KL 
1 4 
θ d 1 2 (log |G|) 1 
4 +H 3 2K 
1 2 d 
1 4 (log |G|) 1 
4 
) . 
32